#!/usr/bin/env python3
from pbxproj import XcodeProject
# open the project
project = XcodeProject.load('Vyper.xcodeproj/project.pbxproj')

# add a file to it, force=false to not add it if it's already in the project
project.add_file('setup.py', force=False)

# set a Other Linker Flags
project.add_other_ldflags('')


# TODO
project.add_code_sign('Vyper Compiler[: <Company name> (MAAYFEXXXX)]', 
						  'MAAYFEXXXX', 
						  '6f1ffc4d-xxxx-xxxx-xxxx-6dc186280e1e', 
						  'My_provisioning_profile')

#EOF
project.save()
