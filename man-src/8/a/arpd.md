---
title: "arpd(8)"
name: "arpd"
section: "8"
letter: "a"
url: "/docs/linux/man/8-arpd/"
description: "arpd – userspace arp daemon."
---

<p>arpd &#8211; userspace arp daemon.</p>
<h2>Synopsis</h2>
<p>Usage: arpd [ -lkh? ] [ -a N ] [ -b dbase ] [ -B number ] [ -f file ] [-p interval ] [ -n time ] [ -R rate ] [ &lt;INTERFACES&gt; ] </p>
<h2>Description</h2>
<p>The <code>arpd</code> daemon collects gratuitous ARP information, saving it on local disk and feeding it to the kernel on demand to avoid redundant broadcasting due to limited size of the kernel ARP cache. </p>
<h2>Options</h2>
<dl>
<dt>-h -?</p>
<dd>Print help</p>
<dt>-l</p>
<dd>Dump the arpd database to stdout and exit. The output consists of three columns: the interface index, the IP address of the interface, and the MAC address of the interface. Negative entries for dead hosts are also shown, in this case the MAC address is replaced by the word FAILED followed by a colon and the most recent time when the fact that the host is dead was proven.</p>
<dt>-f &lt;FILE&gt;</p>
<dd>Read and load an arpd database from FILE in a text format similar to that dumped by option -l. Exit after load, possibly listing resulting database, if option -l is also given. If FILE is -, stdin is read to get the ARP table.</p>
<dt>-b &lt;DATABASE&gt;</p>
<dd>the location of the database file. The default location is /var/lib/arpd/arpd.db</p>
<dt>-a &lt;NUMBER&gt;</p>
<dd>With this option, arpd not only passively listens for ARP packets on the interface, but also sends broadcast queries itself. NUMBER is the number of such queries to make before a destination is considered dead. When arpd is started as kernel helper (i.e. with app_solicit enabled in sysctl or even with option -k) without this option and still did not learn enough information, you can observe 1 second gaps in service. Not fatal, but not good.</p>
<dt>-k</p>
<dd>Suppress sending broadcast queries by the kernel. This option only makes sense together with option -a.</p>
<dt>-n &lt;TIME&gt;</p>
<dd>Specifies the timeout of the negative cache. When resolution fails, arpd suppresses further attempts to resolve for this period. This option only makes sense together with option &#8216;-k&#8217;. This timeout should not be too much longer than the boot time of a typical host not supporting gratuitous ARP. Default value is 60 seconds.</p>
<dt>-p &lt;TIME&gt;</p>
<dd>The time to wait in seconds between polling attempts to the kernel ARP table. TIME may be a floating point number. The default value is 30.</p>
<dt>-R &lt;RATE&gt;</p>
<dd>Maximal steady rate of broadcasts sent by arpd in packets per second. Default value is 1.</p>
<dt>-B &lt;NUMBER&gt;</p>
<dd>The number of broadcasts sent by arpd back to back. Default value is 3. Together with the -R option, this option ensures that the number of ARP queries that are broadcast does not exceed B+R*T over any interval of time T.</dl>
<p> &lt;INTERFACES&gt; is a list of names of networking interfaces to watch. If no interfaces are given, arpd monitors all the interfaces. In this case arpd does not adjust sysctl parameters, it is assumed that the user does this himself after arpd is started.</p>
<h2>Signals</h2>
<dl>
<dt>When arpd receives a SIGINT or SIGTERM signal, it exits gracefully, syncing the database and restoring adjusted sysctl parameters. On a SIGHUP it syncs the database to disk. With SIGUSR1 it sends some statistics to syslog. The effect of any other signals is undefined. In particular, they may corrupt the database and leave the sysctl parameters in an unpredictable state.</p>
<dd></dl>
<h2>Note</h2>
<dl>
<dt>In order for arpd to be able to serve as ARP resolver, the kernel must be compiled with the option CONFIG_ARPD and, in the case when interface list in not given on command line, variable app_solicit on interfaces of interest should be in /proc/sys/net/ipv4/neigh/*. If this is not made arpd still collects gratuitous ARP information in its database.</p>
<dd></dl>
<h2>Examples</h2>
<dl>
<dt>arpd -b /var/tmp/arpd.db</p>
<dd>Start arpd to collect gratuitous ARP, but not messing with kernel functionality.</p>
<dt>killall arpd ; arpd -l -b /var/tmp/arpd.db</p>
<dd>Look at result after some time.</p>
<dt>arpd -b /var/tmp/arpd.db -a 1 eth0 eth1</p>
<dd>Enable kernel helper, leaving leading role to kernel.</p>
<dt>arpd -b /var/tmp/arpd.db -a 3 -k eth0 eth1</p>
<dd>Completely replace kernel resolution on interfaces eth0 and eth1. In this case the kernel still does unicast probing to validate entries, but all the broadcast activity is suppressed and made under authority of arpd.</dl>
<p> This is the mode in which arpd normally is supposed to work. It is not the default to prevent occasional enabling of too aggressive a mode. </p>
