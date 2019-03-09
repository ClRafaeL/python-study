from Read_File import Read_File
from Corredor import Corredor

txt = Read_File()

txt.receiv_name('text.txt')
file_open = txt.read()

for i in file_open[1:]:
    corredor = Corredor(i[18:21], i[24:39])

    corredor.print()



    # obj_corr.turns = i[58:59]
    # obj_corr.time_turns = i[72:80]
    # obj_corr.veloc_turns = i[105:110]
    # obj_corr.hours = i[1:12]


    



