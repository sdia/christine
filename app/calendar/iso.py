#!/usr/bin/env python
#-*- coding:utf-8 -*-




import convertdate
from _common import Calendar




class ISO(Calendar):

    calendar = convertdate.iso
    columns_list = ['isodate', 'year', 'week_number', 'weekday_number']
    debug = False


    def insert(self):
        todml = ''
        values_tuple = []
        for d in self._generate_date():
            isoyear, isomonth, isoday = d
            isodate = '{:04d}-{:02d}-{:02d}'.format(isoyear, isomonth, isoday)
            year, week_number, weekday_number = self.calendar.from_gregorian(isoyear, isomonth, isoday)
            str_tuple = "('{isodate}',\t{year},\t{week_number},\t{weekday_number})"
            str_tuple = str_tuple.format(
                isodate=isodate,
                year=year,
                week_number=week_number,
                weekday_number=weekday_number)

            values_tuple.append(str_tuple)

        cmd_insert = self.DML_CMD_INSERT.format(
            TABLE_NAME = self.table_name,
            COLUMNS_LIST = ','.join(self.columns_list),
            VALUES_TUPLE = '\n, '.join(values_tuple))

        todml += self.dml_header
        todml += cmd_insert

        if self.debug:
            print 'DEBUG mode'
            print 'writting to {}...'.format(self.dml_path),
            with open(self.dml_path, 'w') as f:
                f.write(todml)
        else:
            print 'Inserting to {}...'.format(self.table_name)
            with self.pgconn.cursor() as cur:
                cur.execute(todml)
            self.pgconn.commit()

        print 'OK.'



if __name__ == '__main__':
    b=ISO()
    b.insert()
