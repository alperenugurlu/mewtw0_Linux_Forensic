#!/usr/bin/python
# -*- coding: latin-1 -*-
# -*- coding: ascii -*-
# This Python file uses the following encoding: utf-8

import os, sys
import time

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))


prCyan('''
                                _                 ___  
                               | |               / _ \ 
  _ __ ___     ___  __      __ | |_  __      __ | | | -|
 | '_ ` _ \   / _ \ \ \ /\ / / | __| \ \ /\ / / | | |----|
 | | | | | | |  __/  \ V  V /  | |_   \ V  V /  | |_| --|
 |_| |_| |_|  \___|   \_/\_/    \__|   \_/\_/    \___/ 
                                                       
                                                                                                                         

		 _                 
		//\lperen  |U|gurlu
				   `-'     

                      
''' )
            
            

prRed('''''''''''''''


		Linux Compromise Assessment
		 *    *      * * *  *   *  
		* *    ******          * * 
		   **         *   ** **   *
						 *         
					  *   ** **    
		*     *                   *
		   *    *   *          *   
		  *            *    *   ** 
			   *   *               
			*    *                 
								   
		 *        *  *             


''''''''''''''')


prGreen('''                Scanning In Progress......
''')


time.sleep(4.0)



prRed('''
Operating System Information:
''')

def scan1():
        op_system = os.system('cat' + ' ' + '/etc/os-release')
        print(op_system)  
        prRed('''
        
        
It Is The File Where Connections to The System and Authentication Are Saved:
        ''')


def scan3():
    cd1 = os.system('cd' + ' ' + '/root/')
    



def scan2():
        log_in = os.system('cat' + ' ' + '/var/log/auth.log')
        print(log_in)
        prRed('''
        
        
Provides System Status, System Reboot Time and User Login Information:
        ''')
       
      
        
def scan4():
    cd2 = os.system('cd' + ' ' + '/root/')
    


def scan5():
        log_reboot = os.system('last' + ' ' + '-f' + ' ' + '/var/log/wtmp')
        print(log_reboot)
        prRed('''
        
        
Log of Failed Login Attempts:
        ''')


def scan6():
    cd3 = os.system('cd' + ' ' + '/root/')
    


def scan7():
        log_off = os.system('last' + ' ' + '-f' + ' ' + '/var/log/btmp')
        print(log_off)
        prRed('''
        
        
You Can Find Out If Any Suspicious Account Has Been Created And What Commands A User Can Run With Privilege Permission:
        ''')



def scan8():
    cd4 = os.system('cd' + ' ' + '/root/')
    


def scan9():
        users = os.system('cat' + ' ' + '/etc/passwd')
        print(users)
        prGreen('''                Scanning In Progress......
''')
        sudo_users = os.system('cat' + ' ' + '/etc/sudoers')
        print(sudo_users)
        prRed('''
        
        
It's a Log Of All Runs With Sudo:
        ''')


def scan10():
    cd5 = os.system('cd' + ' ' + '/root/')
    


def scan11():
        sudo_run = os.system('strings' + ' ' + '/var/log/auth.log*' + ' ' + '|' + ' ' + 'grep' + ' ' + '-i' + ' ' + 'COMMAND')
        print(sudo_run)

        prRed('''
        

Background Processes/Services Provide Invaluable Logs for A User's Activities:
        ''')
        
        
def scan12():
    cd6 = os.system('cd' + ' ' + '/root/')
    

def scan13():
        logc = os.system('cat' + ' ' + '/var/log/daemon.log')
        print(logc)

        prRed('''
        

Contains General System Messages. Particularly, It Also Contains Cron Job Execution With Its Associated Commands:
        ''')


def scan14():
    cd7 = os.system('cd' + ' ' + '/root/')
    

def scan15():
        logd = os.system('cat' + ' ' + '/var/log/syslog')
        print(logd)


        prRed('''
        

WebShell Access Detection Logs:
        ''')


def scan18():
    cd9 = os.system('cd' + ' ' + '/root/')
    

def scan19():
        loga = os.system('cat' + ' ' + '/var/log/apache2/access.log')
        print(loga)
  
        

        prRed('''
        

Monitor The Network For Unusual Network Traffic and Connections:
        ''')
        

def scan20():
    cd10 = os.system('cd' + ' ' + '/root/')
    

def scan21():
        logz = os.system('ps -auxwf')
        print(logz)
  
        

        prRed('''
        

MySQL Database Server Log File:
        ''')
        

def scan22():
    cd11 = os.system('cd' + ' ' + '/root/')
    

def scan23():
        logf = os.system('cat' + ' ' + '/var/log/mysqld.log')
        print(logf)
  
        

        prRed('''
        

Nginx Access And Error Logs Directory:
        ''')
        
        
def scan24():
    cd12 = os.system('cd' + ' ' + '/root/')
    

def scan25():
        logfs = os.system('cat' + ' ' + '/var/log/nginx/access.log')
        print(logfs)
  
        

        prRed('''
        

Kernel Log:
        ''')
        
        
def scan26():
    cd13 = os.system('cd' + ' ' + '/root/')
    

def scan27():
        logrt = os.system('cat' + ' ' + '/var/log/debug')
        print(logrt)
  
        

        prRed('''
        

As An event Responder, You Must Determine If There Are Any Anomalies In The Services:
        ''')
        
        
def scan28():
    cd14 = os.system('cd' + ' ' + '/root/')
    

def scan29():
        logrtc = os.system('service --status-all')
        print(logrtc)
  
        

        prRed('''
        

Open Network Ports Or Raw Sockets:
        ''')
        
        
def scan30():
    cd15 = os.system('cd' + ' ' + '/root/')
    

def scan31():
        logrtct = os.system('netstat -nalpn')
        print(logrtct)
  
        

        prRed('''
        

Process Working Directory:
        ''')
        
        
def scan32():
    cd16 = os.system('cd' + ' ' + '/root/')
    

def scan33():
        logrtcti = os.system('ls -alR /proc/*/cwd')
        print(logrtcti)
  
        

        prRed('''
        

Check Scheduled Tasks:
        ''')
        
        
def scan34():
    cd17 = os.system('cd' + ' ' + '/root/')
    

def scan35():
        logrtctis = os.system('systemctl list-timers  --all')
        print(logrtctis)
  
        

        prRed('''
        
 ________  __                        ________                  __             
/        |/  |                      /        |                /  |            
$$$$$$$$/ $$ |____    ______        $$$$$$$$/  _______    ____$$ |            
   $$ |   $$      \  /      \       $$ |__    /       \  /    $$ |            
   $$ |   $$$$$$$  |/$$$$$$  |      $$    |   $$$$$$$  |/$$$$$$$ |            
   $$ |   $$ |  $$ |$$    $$ |      $$$$$/    $$ |  $$ |$$ |  $$ |            
   $$ |   $$ |  $$ |$$$$$$$$/       $$ |_____ $$ |  $$ |$$ \__$$ | __  __  __ 
   $$ |   $$ |  $$ |$$       |      $$       |$$ |  $$ |$$    $$ |/  |/  |/  |
   $$/    $$/   $$/  $$$$$$$/       $$$$$$$$/ $$/   $$/  $$$$$$$/ $$/ $$/ $$/ 
                                                                              
                                                                                                                                              
                                                                                                                         

					 _                 
					//\lperen  |U|gurlu               1992
							   `-'     
								    
            
        ''')
        
        


scan1()
scan3()
scan2()
scan4()
scan5()
scan6()
scan7()
scan8()
scan9()
scan10()
scan11()
scan12()
scan13()
scan14()
scan15()
scan18()
scan19()
scan20()
scan21()
scan22()
scan23()
scan24()
scan25()
scan28()
scan29()
scan30()
scan31()
scan32()
scan33()
scan34()
scan35()


