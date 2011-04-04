#!/usr/bin/env python

import csv
from cStringIO import StringIO

def guess_format(filename):
    """
    Try to guess a file's format based on its extension (or lack thereof).
    """
    last_period = filename.rfind('.')

    if last_period == -1:
        # No extension: assume fixed-width
        return 'fixed'

    extension = filename[last_period + 1:]

    if extension == 'xls':
        return extension

    return None

def rows_to_csv_string(rows):
    """
    Converts an list of row lists to an string representation of a CSV file. 
    """
    o = StringIO()
    writer = csv.writer(o, lineterminator='\n')
    writer.writerows(rows)
    output = o.getvalue()
    o.close()

    return output