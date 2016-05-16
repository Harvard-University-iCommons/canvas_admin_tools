#!/usr/bin/env python


import csv
import pprint
import warnings

from django.core.management.base import LabelCommand
from django.db import transaction

from manage_people.models import SchoolAllowedRole


YES_NO_MAP = {
    'y': True,
    'Y': True,
    'n': False,
    'N': False,
}


class Command(LabelCommand):
    args = '<csv_filename>'
    help = """Replaces the school allowed roles in the database with the contents of a
CSV file.

Assumptions:
* first line of the csv is headers
* the school_id value is in the second column, and is a valid school id
* the canvas_role_id value is in the third column, and is an int
* the xid_allowed value is in the fifth column, and is one of y,Y,n,N
"""

    def handle_label(self, label, **options):
        with open(label) as f:
            reader = csv.reader(f)
            rows = list(reader)
            header, rows = rows[0], rows[1:]

        num_existing, num_created = 0, 0
        failed_rows = []

        with transaction.atomic():
            # NOTE - verify if we should be deleting all rows every time this runs?
            SchoolAllowedRole.objects.all().delete()
            for row in rows:
                try:
                    # TODO - FIXME - HACK - look up column ids by matching headers
                    school_id = row[0].lower()
                    user_role_id = int(row[1])
                    xid_allowed = YES_NO_MAP[row[2]]
                except Exception as e:
                    warnings.warn('Unable to normalize inputs in row {}: {}'.format(
                                      row, str(e)))
                    failed_rows.append(row)
                    continue

                try:
                    sar, created = SchoolAllowedRole.objects.get_or_create(
                                       school_id=school_id,
                                       user_role_id=user_role_id,
                                       xid_allowed=xid_allowed)
                    if created:
                        num_created += 1
                    else:
                        num_existing += 1
                except Exception as e:
                    warnings.warn(
                        'Unable to get_or_create ({}, {}, {}): {}'.format(
                            school_id, user_role_id, xid_allowed, str(e)))
                    failed_rows.append(row)

        self.stdout.write(
            'New rows: {}\nExisting rows: {}\nFailed rows:\n{}'.format(
                num_created, num_existing, pprint.pformat(failed_rows)))
