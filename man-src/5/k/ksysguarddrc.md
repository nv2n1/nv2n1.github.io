---
title: "ksysguarddrc(5)"
name: "ksysguarddrc"
section: "5"
letter: "k"
url: "/docs/linux/man/5-ksysguarddrc/"
---

ksysguarddrc - ksysguardd configuration

<h2>Description</h2>

ksysguardd uses a configuration file at /etc/ksysguarddrc.

<h2>Parameters</h2>

There are 2 sections of configuration in the ksysguardd configuration file: LogFiles, Sensors.

<h2>[LogFiles] OPTIONS</h2>

the list of all available logfiles messages:/var/log/messages,kern:/var/log/kern.log,daemon:/var/log/daemon.log,syslog:/var/log/syslog,auth:/var/log/auth.log

<h2>[Sensors] OPTIONS</h2>

Sensors: the list of all accessible sensors 
Apm&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Advanced Power Management 
Acpi&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Advanced Configuration and Power Interface 
CpuInfo&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>CPU-Clock information 
DiskStat&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>partition space. Data comes from mtab, getmntent()&nbsp;<wbr>and statfs() 
DiskStats&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>disk throughput. Data comes from&nbsp;<wbr>/etc/diskstats 
LmSensors&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>information about motherboard and CPU 
LoadAvg&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>system load values 
LogFile&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>local logfiles 
Memory&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>physical memory and swap 
NetDev&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>throughput of network interfaces 
NetStat&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>number of TCP/UDP/ICMP/Unix sockets 
ProcessList&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>current processes 
SoftRaid&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Monitors software raid devices. See mdadm. 
Stat&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>interrupts, CPU and disk throughput. Data comes from&nbsp;<wbr>/etc/stat 
Uptime&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>System uptime. Data comes from&nbsp;<wbr>/etc/uptime Sensors=ProcessList,Memory,Stat,NetDev,NetStat,Apm,Acpi,CpuInfo,LoadAvg,LmSensors,DiskStat,LogFile,DiskStats,Uptime,SoftRaid

<h2>Files</h2>

/etc/ksysguarddrc
