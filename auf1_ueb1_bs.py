import os 
import multiprocessing as mp 



def run(name): 
    print(f"process {name} hat PID:{os.getpid()} und Parent-PId:{os.getppid()}")


if __name__ == '__main__':
    p1 = mp.Process(target=run, args=('eins',))
    p2 = mp.Process(target=run, args=('zwei',))

    p1.start() # start den Prozess p1
    p2.start()

    p1.join() # wartet bis zur Terminierung des Prozess p1
    p2.join()
    
    print("die Prozessen wurden beendet...")
    print(f"Hauptprozess (python) PID:{os.getpid()} und Vater-PID:{os.getppid()} (Shell)")
