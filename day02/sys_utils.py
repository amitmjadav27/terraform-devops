# Blueprint / template
import os
class Utilities:
    def show_disk_space(self):
        print(os.system("df -h"))
    
    def show_ram(self):
        print(os.system("free -h"))
    
    def show_syayem_details(self):
        print(os.uname().sysname)

machine_a = Utilities() # machine_a is an object 
machine_a.show_disk_space()
machine_b = Utilities() # machine_b is an object
machine_b.show_ram()