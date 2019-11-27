import numpy as np
import struct


''' Tipo de instrução '''
instr_type = np.uint32(399999)
''' Registrador A '''
reg_a = np.uint32(399999)
''' Registrador B '''
reg_b = np.uint32(399999)
''' Registrador destino '''
reg_dest = np.uint32(399999)
''' Registrador endereço de memória '''
reg_addr = np.uint32(399999)
''' Registrador de propósito geral '''
reg[8] = np.uint32(399999)
''' Memória de programa '''
prog_mem[ 0x01000000,0x01010001,0x00000102,0x01030002,0x03020302,0x02020003 ] = np.uint32(399999) 


addr_mem[ 2, 3, 10, 7, 23, 0, 9, 4 ] = np.uint32(399999)


#define WORDS 2
#define LINES 2

var = struct.pack(line, valid, tag, words[WORDS])
bool(valid)
tag = np.uint32(399999)
words[WORDS] = np.uint32(399999)


line = l1[LINES]

def decode(self, instr):
	  # Pegando o tipo de instrução
    
    
	  instr_type = instr >> 24
    

    # Sub
    if instr_type == 0x00:
        print("")

    # Soma
    elif instr_type == 0x03:
        reg_a 	 = (instr & 0x00FF0000) >> 16
        reg_b 	 = (instr & 0x0000FF00) >>  8
        reg_dest = (instr & 0x000000FF) >>  0,

    # LOAD
    elif instr_type ==  0x01:
        reg_dest = (instr & 0x00FF0000) >> 16
        reg_addr = (instr & 0x0000FFFF) >>  0,

    # STORE
    elif instr_type == 0x02:
        reg_a 	 = (instr & 0x00FF0000) >> 16
        reg_addr = (instr & 0x0000FFFF) >>  0,

    else: 
        print(instr_type)
        print(": illegal instruction") 
    



def execute(instr_type):
	  
	# Sub
	if instr_type == 0x00:
			reg[reg_dest] = reg[reg_a] - reg[reg_b]
			print("sub: " + reg[reg_dest])
			
	# LOAD
	elif instr_type == 0x01:
              reg[reg_dest] = addr_mem[reg_addr]
              print("Load: " + reg[reg_dest])
		
	# STORE
	elif instr_type == 0x02:
            addr_mem[reg_addr] = reg[reg_a]
            print("Store: " + addr_mem[reg_addr])
			
		# Soma
	elif instr_type == 0x03:
              reg[reg_dest] = reg[reg_a] + reg[reg_b]
              print("Soma: " + reg[reg_dest]) 
		

def load_cache(self, pc):
	w = pc & 0x00000001
	l = pc & 0x00000002
	tag = pc & 0xFFFFFFFC
	
	if not l1[l].valid or l1[l].tag != tag:
		print("miss")
		l1[l].valid = True
		l1[l].tag = tag
		for (i = 0; i < WORDS; i++)
			l1[l].words[i] = prog_mem[pc + i]


	
	return l1[l].words[w]



def main(self):
          memset(l1, 0, sizeof(line))
          
          for pc in range(0, 6):
                instr = load_cache(pc)
                decode(instr)
                execute()
    
          return 0
