from Components.Console import Console
from os import mkdir, path, remove
from Components.config import config, ConfigSubsection, ConfigInteger, ConfigText, getConfigListEntry, ConfigSelection,  ConfigIP, ConfigYesNo, ConfigSequence, ConfigNumber, NoSave, ConfigEnableDisable, configfile
import os
config.NFRSoftcam.camdir = ConfigText(default = "/usr/emu")
config.NFRSoftcam.camconfig = ConfigText(default = "/usr/keys")
def getcamcmd(cam):
	camname = cam.lower()
	if getcamscript(camname):
		return config.NFRSoftcam.camdir.value + "/" + cam + " start"
	else:
		if "oscam" in camname:
			return config.NFRSoftcam.camdir.value + "/" + cam + " -bc " + \
				config.NFRSoftcam.camconfig.value + "/"
		if "doscam" in camname:
			return config.NFRSoftcam.camdir.value + "/" + cam + " -bc " + \
				config.NFRSoftcam.camconfig.value + "/"				
		elif "wicard" in camname:
			return "ulimit -s 512; " + config.NFRSoftcam.camdir.value + \
			"/" + cam + " -d -c " + config.NFRSoftcam.camconfig.value + \
			"/wicardd.conf"
		elif "camd3" in camname:
			return config.NFRSoftcam.camdir.value + "/" + cam + " " + \
				config.NFRSoftcam.camconfig.value + "/camd3.config"
		elif "mbox" in camname:
			return config.NFRSoftcam.camdir.value + "/" + cam + " " + \
				config.NFRSoftcam.camconfig.value + "/mbox.cfg"
		elif "cccam" in camname:
			return config.NFRSoftcam.camdir.value + "/" + cam + " -C " + \
				config.NFRSoftcam.camconfig.value + "/CCcam.cfg"
                elif "mgcamd" in camname:
	                os.system("rm /dev/dvb/adapter0/ca1")
	                os.system("ln -sf 'ca0' '/dev/dvb/adapter0/ca1'")                 
			return config.NFRSoftcam.camdir.value + "/" + cam + " -bc " + \
				config.NFRSoftcam.camconfig.value + "/"                				
		elif "mpcs" in camname:
			return config.NFRSoftcam.camdir.value + "/" + cam + " -c " + \
				config.NFRSoftcam.camconfig.value
		elif "newcs" in camname:
			return config.NFRSoftcam.camdir.value + "/" + cam + " -C " + \
				config.NFRSoftcam.camconfig.value + "/newcs.conf"
		elif "vizcam" in camname:
			return config.NFRSoftcam.camdir.value + "/" + cam + " -b -c " + \
				config.NFRSoftcam.camconfig.value + "/"
		elif "rucam" in camname:
			return config.NFRSoftcam.camdir.value + "/" + cam + " -b"
		else:
			return config.NFRSoftcam.camdir.value + "/" + cam

def getcamscript(cam):
	cam = cam.lower()
	if cam.endswith('.sh') or cam.startswith('softcam') or \
		cam.startswith('cardserver'):
		return True
	else:
		return False

def stopcam(cam):
	if getcamscript(cam):
		cmd = config.NFRSoftcam.camdir.value + "/" + cam + " stop"
	else:
		cmd = "killall -15 " + cam
	Console().ePopen(cmd)
	print "[NFR-SoftCam Manager] stopping", cam
	try:
		remove("/tmp/ecm.info")
	except:
		pass

def __createdir(list):
	dir = ""
	for line in list[1:].split("/"):
		dir += "/" + line
		if not path.exists(dir):
			try:
				mkdir(dir)
			except:
				print "[NFR-SoftCam Manager] Failed to mkdir", dir

def checkconfigdir():
	if not path.exists(config.NFRSoftcam.camconfig.value):
		__createdir("/usr/keys")
		config.NFRSoftcam.camconfig.value = "/usr/keys"
		config.NFRSoftcam.camconfig.save()
	if not path.exists(config.NFRSoftcam.camdir.value):
		if path.exists("/usr/emu"):
			config.NFRSoftcam.camdir.value = "/usr/emu"
		else:
			__createdir("/usr/emu")
			config.NFRSoftcam.camdir.value = "/usr/emu"
		config.NFRSoftcam.camdir.save()
