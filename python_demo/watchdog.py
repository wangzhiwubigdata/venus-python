#!/usr/bin/env python
import sys
import subprocess
def monitor_process(key_word, cmd):
    p1 = subprocess.Popen(['ps','-ef'], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['grep', key_word],stdin=p1.stdout, stdout=subprocess.PIPE)
    p3 = subprocess.Popen(['grep','-v', 'grep'], stdin=p2.stdout, stdout=subprocess.PIPE)
    lines = p3.stdout.readlines()
    if len(lines) > 0:
       return
    sys.stderr.write('process[%s] is lost, run [%s]\n' % (key_word,cmd))
    subprocess.call(cmd, shell=True)

monitor_process("test.sh","/home/hadoop/test.sh")