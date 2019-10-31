import subprocess
#from subprocess import call
number_of_agents = 100
number_of_moves = 50
neighbourhood = 20
random_seed = 7
visual_on = "no"
#cmd='C:\Users\Apai\Anaconda3\python D:\Python_Data\Assigments_Anna\assignment7.py number_0f_agents number_of_moves neighbourhood random_seed'
#cmd='python assignment7.py number_0f_agents number_of_moves neighbourhood random_seed'


start = 20
stop = 120
step = 20

start2 = 200
stop2 = 1200
step2 = 200


for i  in range(start,stop,step):
    number_of_agents = i
    for j in range(start2,stop2,step2): 
        number_of_moves = j
        cmd = 'python practical7_final.py ' + str(number_of_agents) + ' ' + str(number_of_moves) + ' '
        cmd = cmd +  str(neighbourhood) + ' ' + str(random_seed) + ' ' + str(visual_on)
#p =subprocess.run(cmd, capture_output=True, text=True)
#p =subprocess.run(cmd, stdout=subprocess.PIPE, stderr = subprocess.PIPE, text=True)

        with open ('parametersweep_out.txt','a') as f:
            f.write("\n________________________________________________________")
            p =subprocess.run(cmd, stdout= f, stderr = f, text=True)
            f.write("\nSubprocess Arguments: " + str(p.args))
            f.write("\n________________________________________________________\n")
        print("\nSubprocess Arguments: ", p.args)
        print("Subprocess Returncode: ", p.returncode)

#print(p.stdout.decode())
#print(p.stdout)
    
'''
cmd = 'python practical7_final.py ' + str(number_of_agents) + ' ' + str(number_of_moves) + ' ' + str(neighbourhood) + ' ' + str(random_seed) + ' ' + str(visual_on)
print(cmd)
p =subprocess.run(cmd, capture_output=True, text=True)
print(p.stdout)
print(p.returncode)
print(p.stderr)
'''
