import os
#report_file = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/report/')
#print(report_file)

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace('\\', '/')
print(root_dir)