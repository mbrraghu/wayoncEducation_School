# -*- coding: utf-8 -*-
##############################################################################
#
#    wayoncEducation Inc
#    Copyright (C) 2009-TODAY wayoncEducation Inc(<https://wayonc.in>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'WayOnC Education ERP',
    'version': '17.0.1.0',
    'license': 'LGPL-3',
    'category': 'Education',
    "sequence": 3,
    'summary': 'Manage Students, Faculties and Education Institute',
    'complexity': "easy",
    'author': 'WayOnC Technologies',
    'website': 'https://wayonc.in',
    'depends': [
        'wayoncEducation_admission',
        'wayoncEducation_assignment',
        'wayoncEducation_attendance',
        'wayoncEducation_library',
        'wayoncEducation_parent',
        'wayoncEducation_exam',
        'web_wayoncEducation',
    ],
    'images': [
        'static/description/icon.png',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
