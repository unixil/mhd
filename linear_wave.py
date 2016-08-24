# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 17:43:15 2016

@author: waffle
"""
import os
#import subprocess
import math
basename=r"/home/waffle/Dropbox/research_project/mhd/athenaCode/testathena/"
basename2=r"/home/waffle/Dropbox/research_project/mhd/athenaCode/testathena/athinput.linear_wave1d"
os.system("rm -rf result/*")
os.system("mkdir -p result/roe")
os.system("mkdir -p result/hlld")
os.system("mkdir -p result/hlle")
#######################################################################
#######################################################################
#  roe#################################################################
###############################################################################
os.system("make clean")
os.system("./configure --with-flux=roe --with-problem=linear_wave")
os.system("make all")
for wave_flag in (4,5,6):
    for nx1 in range (10,1024):
        fhandler=open(basename2,"r")
        fhandler.seek(0,0)
        lineslist=fhandler.readlines()
        lineslist[28]="Nx1             = "+str(nx1)+"       # Number of zones in X1-direction\n"
        lineslist[48]="Nx1             = "+str(int(math.floor(nx1/4)))+"       # Number of zones in X1-direction\n"
        lineslist[51]="iDisp           = "+str(int(math.floor(nx1/8)))+"        # i-displacement measured in cells of this level\n"
        lineslist[57]="Nx1             = "+str(int(math.floor(nx1/4)))+"       # Number of zones in X1-direction\n"
        lineslist[60]="iDisp           = "+str(int(math.floor(nx1/8+nx1/4)))+"       # i-displacement measured in cells of this level\n"
        lineslist[66]="Nx1             = "+str(int(math.floor(nx1/4)))+"       # Number of zones in X1-direction\n"
        lineslist[69]="iDisp           = "+str(int(math.floor(nx1-nx1/8)))+"       # i-displacement measured in cells of this level\n"
        lineslist[76]="wave_flag       = "+str(wave_flag)+"         # Wave family number (0-6)\n"

        fhandler2=open(basename+"tst/1D-mhd/athinput.linear_wave1d2","w+")
        for line in lineslist:
            fhandler2.write(str(line))
        fhandler2.close()
        fhandler.close()
        os.system("mv /home/waffle/Dropbox/research_project/mhd/athenaCode/testathena/tst/1D-mhd/athinput.linear_wave1d2 /home/waffle/Dropbox/research_project/mhd/athenaCode/testathena/tst/1D-mhd/athinput.linear_wave1d")
        os.system("bin/athena -i tst/1D-mhd/athinput.linear_wave1d")
        os.system("rm *.tab")
        os.system("rm *.hst")
        os.system("mv *errors* result/roe/LinWave-errors-roe."+str(nx1)+"."+str(wave_flag)+".dat")
        os.system("rm -rf bin/*.tab && rm -rf bin/*.hst")
#######################################################################
#######################################################################
# hlle#################################################################
#######################################################################
os.system("make clean")
os.system("./configure --with-flux=hlld --with-problem=linear_wave")
os.system("make all")
for wave_flag in (4,5,6):
    for nx1 in range (10,1024):
        fhandler=open(basename2,"r")
        fhandler.seek(0,0)
        lineslist=fhandler.readlines()
        lineslist[28]="Nx1             = "+str(nx1)+"       # Number of zones in X1-direction\n"
        lineslist[48]="Nx1             = "+str(int(math.floor(nx1/4)))+"       # Number of zones in X1-direction\n"
        lineslist[51]="iDisp           = "+str(int(math.floor(nx1/8)))+"        # i-displacement measured in cells of this level\n"
        lineslist[57]="Nx1             = "+str(int(math.floor(nx1/4)))+"       # Number of zones in X1-direction\n"
        lineslist[60]="iDisp           = "+str(int(math.floor(nx1/8+nx1/4)))+"       # i-displacement measured in cells of this level\n"
        lineslist[66]="Nx1             = "+str(int(math.floor(nx1/4)))+"       # Number of zones in X1-direction\n"
        lineslist[69]="iDisp           = "+str(int(math.floor(nx1-nx1/8)))+"       # i-displacement measured in cells of this level\n"
        lineslist[76]="wave_flag       = "+str(wave_flag)+"         # Wave family number (0-6)\n"
        fhandler2=open(basename+"tst/1D-mhd/athinput.linear_wave1d2","w+")
        for line in lineslist:
            fhandler2.write(str(line))
        fhandler2.close()
        fhandler.close()
        os.system("mv /home/waffle/Dropbox/research_project/mhd/athenaCode/testathena/tst/1D-mhd/athinput.linear_wave1d2 /home/waffle/Dropbox/research_project/mhd/athenaCode/testathena/tst/1D-mhd/athinput.linear_wave1d")
        os.system("bin/athena -i tst/1D-mhd/athinput.linear_wave1d")
        os.system("rm *.tab")
        os.system("rm *.hst")
        os.system("mv *errors* result/hlld/LinWave-errors-hlld."+str(nx1)+"."+str(wave_flag)+".dat")
#######################################################################
#######################################################################
# hlle#################################################################
#######################################################################
os.system("make clean")
os.system("./configure --with-flux=hlle --with-order=3 --with-problem=linear_wave")
os.system("make all")
for wave_flag in (4,5,6):
    for nx1 in range (10,1024):
        fhandler=open(basename2,"r")
        fhandler.seek(0,0)
        lineslist=fhandler.readlines()
        lineslist[28]="Nx1             = "+str(nx1)+"       # Number of zones in X1-direction\n"
        lineslist[48]="Nx1             = "+str(int(math.floor(nx1/4)))+"       # Number of zones in X1-direction\n"
        lineslist[51]="iDisp           = "+str(int(math.floor(nx1/8)))+"        # i-displacement measured in cells of this level\n"
        lineslist[57]="Nx1             = "+str(int(math.floor(nx1/4)))+"       # Number of zones in X1-direction\n"
        lineslist[60]="iDisp           = "+str(int(math.floor(nx1/8+nx1/4)))+"       # i-displacement measured in cells of this level\n"
        lineslist[66]="Nx1             = "+str(int(math.floor(nx1/4)))+"       # Number of zones in X1-direction\n"
        lineslist[69]="iDisp           = "+str(int(math.floor(nx1-nx1/8)))+"       # i-displacement measured in cells of this level\n"
        lineslist[76]="wave_flag       = "+str(wave_flag)+"         # Wave family number (0-6)\n"
        fhandler2=open(basename+"tst/1D-mhd/athinput.linear_wave1d2","w+")
        for line in lineslist:
            fhandler2.write(str(line))
        fhandler2.close()
        fhandler.close()
        os.system("mv /home/waffle/Dropbox/research_project/mhd/athenaCode/testathena/tst/1D-mhd/athinput.linear_wave1d2 /home/waffle/Dropbox/research_project/mhd/athenaCode/testathena/tst/1D-mhd/athinput.linear_wave1d")
        os.system("bin/athena -i tst/1D-mhd/athinput.linear_wave1d")
        os.system("rm *.tab")
        os.system("rm *.hst")
        os.system("mv *errors* result/hlle/LinWave-errors-hlle."+str(nx1)+"."+str(wave_flag)+".dat")
####EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF####
####EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF####
####EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF####
####EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF####
####EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF####
####EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF#EOF####
###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################



