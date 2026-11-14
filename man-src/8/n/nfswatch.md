---
title: "nfswatch(8)"
name: "nfswatch"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nfswatch/"
description: "nfswatch – monitor an NFS server"
---

<p>nfswatch &#8211; monitor an <font SIZE="-1">NFS</font> server</p>
<h2>Synopsis</h2>
<p><code>nfswatch</code> [ <code>-dst</code> <i>dsthost</i> ] [ <code>-src</code> <i>srchost</i> ] [ <code>-server</code> <i>serverhost</i> ] [ <code>-all</code> ] [ <code>-dev</code> <i>device</i> ] [ <code>-allif</code> ] [ <code>-f</code> <i>filelist</i> ] [ <code>-lf</code> <i>logfile</i> ] [ <code>-sf</code> <i>snapfile</i> ] [ <code>-map</code> <i>mapfile</i> ] [ <code>-T</code> <i>maxtime</i> ] [ <code>-t</code> <i>timeout</i> ] [ <code>-fs</code> ] [ <code>-if</code> ] [ <code>-auth</code> ] [ <code>-procs</code> ] [ <code>-procs3</code> ] [ <code>-clients</code> ] [ <code>-usage</code> ] [ <code>-l</code> ] [ <code>-bg</code> ]</p>
<h2>Description</h2>
<p><i>nfswatch</i> monitors all incoming network traffic to an <font SIZE="-1">NFS</font> file server and divides it into several categories. The number and percentage of packets received in each category is displayed on the screen in a continuously updated display. The screen is updated every ten seconds by default; this time period is called an <i>interval</i>. </p>
<p> <code>On Irix</code>: You must be the super-user to invoke <i>nfswatch</i> or it must be installed setuid to &#8220;root.&#8221; <code>On SunOS 4.x and SunOS 5.x (Solaris 2.x)</code>: You must be the super-user to invoke <i>nfswatch</i> or it must be installed setuid to &#8220;root.&#8221; <code>On System V Release 4</code>: You must be the super-user to invoke <i>nfswatch</i> or it must be installed setuid to &#8220;root.&#8221; <code>On Ultrix or DEC OSF/1</code>: Any user can invoke <i>nfswatch</i> once the super-user has enabled promiscuous-mode operation using <i><a href="/docs/linux/man/8-pfconfig/">pfconfig</a></i>(8). (For example, &quot;pfconfig +p +c -a&quot;.) <code>On Linux</code>: You must be the super-user to invoke <i>nfswatch</i> or it must be installed setuid to &#8220;root.&#8221; </p>
<p> By default, <i>nfswatch</i> monitors all packets destined for the current host. An alternate destination host to watch for may be specified using the <code>-dst</code> argument. If a source host is specified with the <code>-src</code> argument, then only packets arriving at the destination host which were sent by the source host are monitored. Traffic between a specific server and its clients may be watched by specifying the name of the server with the <code>-server</code> argument. If the <code>-all</code> argument is given, then all <font SIZE="-1">NFS</font> traffic on the network is monitored. It is usually desirable to specify the <code>-all</code> option whenever using the <code>-server</code> option. </p>
<p> The <i>nfswatch</i> screen is divided into three parts. The first part, at the top of the screen, is made up of three lines. The first line displays the name of the host being monitored, the current date and time, and the time elapsed since the start of monitoring. The second line displays the total number of packets received during the most recent interval, and the third line displays the total number of packets received since monitoring started. These two lines display three numbers each: the total number of packets on the network, the total number of packets received by the destination host (possibly subject to being only from the specified source host), and the number of packets dropped by the monitoring interface due to buffer space limitations. Dropped packets are not included in the packet monitoring totals. </p>
<p> The second part of the screen divides the received packets into 16 categories. Each category is displayed with three numbers: the number of packets received this interval, the percentage this represents of all packets received by the host during this interval, and the total number of packets received since monitoring started. The packet categories are not mutually exclusive; some packets may be counted in more than one category (for example, <font SIZE="-1">NFS</font> packets are also <font SIZE="-1">UDP</font> packets). The categories in this section and their meanings are:</p>
<dl>
<dt><font SIZE="-1">NFS</font>3 Read</p>
<dd><font SIZE="-1">NFS v3</font> requests which primarily result in a file system read being performed (read file, read directory, etc.).</p>
<dt><font SIZE="-1">NFS</font>3 Write</p>
<dd><font SIZE="-1">NFS v3</font> requests which primarily result in a file system write being performed (write file, rename file, create file, delete file, etc.).</p>
<dt><font SIZE="-1">NFS</font> Read</p>
<dd><font SIZE="-1">NFS</font> requests which primarily result in a file system read being performed (read file, read directory, etc.).</p>
<dt><font SIZE="-1">NFS</font> Write</p>
<dd><font SIZE="-1">NFS</font> requests which primarily result in a file system write being performed (write file, rename file, create file, delete file, etc.).</p>
<dt><font SIZE="-1">NFS</font> Mount</p>
<dd><font SIZE="-1">NFS</font> mount requests.</p>
<dt>YP/NIS/NIS+</p>
<dd>Sun NIS (Yellow Pages) and NIS+ requests.</p>
<dt><font SIZE="-1">RPC</font> Authorization</p>
<dd>All <font SIZE="-1">RPC</font> reply packets fall into this category, because <font SIZE="-1">RPC</font> replies do not contain the protocol number, and thus cannot be classified as anything else. (If the <code>-all</code> argument is given, then you will see all the <font SIZE="-1">RPC</font> replies on the network in this category.)</p>
<dt>Other <font SIZE="-1">RPC</font> Packets</p>
<dd>All <font SIZE="-1">RPC</font> requests which do not fall into one of the above categories.</p>
<dt><font SIZE="-1">TCP</font> Packets</p>
<dd>Packets sent using the Transmission Control Protocol.</p>
<dt><font SIZE="-1">UDP</font> Packets</p>
<dd>Packets sent using the User Datagram Protocol.</p>
<dt><font SIZE="-1">ICMP</font> Packets</p>
<dd>Packets sent using the Internet Control Message Protocol.</p>
<dt>Routing Control</p>
<dd>Routing Information Protocol (<font SIZE="-1">RIP</font>) packets.</p>
<dt>Address Resolution</p>
<dd>Address Resolution Protocol (<font SIZE="-1">ARP</font>) packets. These packets are not counted on System V Release 4 systems (except for SunOS 5.x), due to limitations of the <i><a href="/docs/linux/man/7-dlpi/">dlpi</a></i>(7) interface.</p>
<dt>Reverse Addr Resol</p>
<dd>Reverse Address Resolution Protocol (<font SIZE="-1">RARP</font>) packets. These packets are not counted on System V Release 4 systems (except for SunOS 5.x), due to limitations of the <i><a href="/docs/linux/man/7-dlpi/">dlpi</a></i>(7) interface.</p>
<dt>Ethernet/FDDI Bdcst</p>
<dd>Ethernet (or FDDI) broadcast packets. These packets are destined for and received by all hosts on the local network. These packets are not counted on System V Release 4 systems (except for SunOS 5.x), due to limitations of the <i><a href="/docs/linux/man/7-dlpi/">dlpi</a></i>(7) interface.</p>
<dt>Other Packets</p>
<dd>A catch-all for any packets not counted in any of the above categories.</dl>
<p> The third part of the display shows the mounted file systems exported by the file server for mounting through <font SIZE="-1">NFS</font>. If <i>nfswatch</i> is monitoring the same host it is being run on, these file systems are listed by path name. Otherwise, the program attempts to decode the server&#8217;s major and minor device numbers for the file system, and displays them in parentheses. (If the <code>-all</code> argument is given, the name of the server is also shown.) With each file system, three numbers are displayed: the number of <font SIZE="-1">NFS</font> requests for this file system received during the interval, the percentage this represents of all <font SIZE="-1">NFS</font> requests received by the host, and the total number of <font SIZE="-1">NFS</font> requests for this file system received since monitoring started. Up to 1024 file systems will be monitored by <i>nfswatch</i> and recorded in the log file, but only as many as will fit (2 * (<font SIZE="-1">LINES</font> &#8211; 16)) will be displayed on the screen. </p>
<p> If the <code>-map</code> <i>mapfile</i> option is specified, <i>nfswatch</i> will read pairs of file system device specifications (as described above) and the proper names of the file systems from <i>mapfile</i>. Each line should contain a string representing what <i>nfswatch</i> would normally print, and then separated from that by whitespace, the name that is preferred. For example, </p>
<p> <center> myhost(7,24)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/homedirs<br />
 </center> </p>
<p> If the <code>-f</code> <i>filelist</i> option is specified, a list of file names (one per line) is read from <i>filelist</i>, and the traffic to these individual files is also monitored. The files must reside in file systems exported by the file server. When this option is specified, the third section of the screen will display counters for these files, instead of for the mounted file systems. Up to 1024 individual files will be monitored by <i>nfswatch</i> and recorded in the log file, but only as many as will fit (2 * (<font SIZE="-1">LINES</font> &#8211; 16)) will be displayed on the screen. </p>
<p> If the <code>-procs</code> or <code>-procs3</code> option is specified, then instead of showing per-file or per-file system statistics, <i>nfswatch</i> shows the frequency of each <font SIZE="-1">NFS</font> procedure (RPC call) (or as many as will fit on the screen). For each procedure, some timing statistics are also displayed; these include the number of completed operations (request and response seen) during the interval, the average response time during the interval (in milliseconds), the standard deviation from the average during the interval, and the maximum response time over all time. </p>
<p> If the <code>-clients</code> option is specified, then instead of showing per-file or per-file system statistics, <i>nfswatch</i> shows the operation rate of each <font SIZE="-1">NFS</font> client of the specified server(s) (or as many as will fit on the screen). </p>
<p> It should be noted here that only <font SIZE="-1">NFS</font> <i>requests</i>, made by client machines, are counted in the <font SIZE="-1">NFS</font> packet monitoring area. The <font SIZE="-1">NFS</font> traffic generated <i>by the server</i> in response to these requests is not counted. </p>
<p> If the <code>-auth</code> option is specified, then the display will show packet counts divided up by user name (or user id, if the login name is not in the local password file). This information is decoded from the AUTH_UNIX authentication part of each RPC packet. <i>nfswatch</i> only decodes AUTH_UNIX authenticators, the other types of authentication (e.g., AUTH_DES) are lumped into a single bucket for each authentication type.</p>
<h2>Logfile</h2>
<p>When logging is on, <i>nfswatch</i> writes one entry to the log file each interval. The information printed to the log file is easily readable, and basically contains a copy of all information on the screen. Additionally, any <font SIZE="-1">NFS</font> traffic to file systems or individual files which was not printed on the screen (due to space limitations) is printed in the log file. Finally, in the log file, the <font SIZE="-1">NFS</font> traffic to file systems and individual files is further broken down into counts of how many times each specific <font SIZE="-1">NFS</font> procedure was called. </p>
<p> The information in the <i>nfswatch</i> log file can be summarized easily using the <i><a href="//www.systutorials.com/docs/linux/man/8L-nfslogsum/">nfslogsum</a></i>(8L) program.</p>
<h2>Commands</h2>
<p><i>nfswatch</i> also allows several commands to be entered at its prompt during execution. The prompt is displayed on the last line of the screen. For most commands, feedback describing the effect of the command is printed on the same line as the prompt. The commands are:</p>
<dl>
<dt><code>^L</code></p>
<dd>Clear and redraw the screen.</p>
<dt><code>a</code></p>
<dd>Switches the display to show statistics on individual users.</p>
<dt><code>c</code></p>
<dd>Switches the display to show statistics on <font SIZE="-1">NFS</font> client hosts instead of per-file or per-filesystem information.</p>
<dt><code>f</code></p>
<dd>Toggle the display of mounted file systems and the display of individual files in the <font SIZE="-1">NFS</font> packet monitoring area. This command is only meaningful if the <code>-f</code> <i>filelist</i> option was specified on the command line. (If the display is showing <font SIZE="-1">NFS</font> procedures or clients, then this command switches the display to show file systems.)</p>
<dt><code>p</code></p>
<dd>Switches the display to show statistics on <font SIZE="-1">NFS</font> procedures instead of per-file or per-filesystem information.</p>
<dt><code>P</code></p>
<dd>Switches the display to show statistics on <font SIZE="-1">NFS v3</font> procedures instead of per-file or per-filesystem information.</p>
<dt><code>l</code></p>
<dd>Toggle the logging feature. If logging is off it is (re)started; if logging is on, it is turned off.</p>
<dt><code>n</code></p>
<dd>Toggle display of host names or host numbers in client mode. By default, client mode displays host names. However, this may not be sufficient for determining the names of unknown remote hosts, since domain names are not displayed. This command tells <i>nfswatch</i> to display host numbers instead, enabling each host to be uniquely identified.</p>
<dt><code>s</code></p>
<dd>Take a &#8220;snapshot&#8221; of the current screen and save it to a file. This is useful to record occasional copies of the data when the logfile is not needed.</p>
<dt><code>u</code></p>
<dd>Toggle the sort key for the display of mounted file systems in the <font SIZE="-1">NFS</font> packet monitoring area. By default, these are sorted by file system name, but they can also be sorted in declining order of percent usage.</p>
<dt><code>&#8211;</code></p>
<dd>Decrease the cycle time (interval length) by ten seconds. This will take effect after the next screen update.</p>
<dt><code>+</code></p>
<dd>Increase the cycle time (interval length) by ten seconds. This will take effect after the next screen update.</p>
<dt><code>&lt;</code></p>
<dd>Decrease the cycle time (interval length) by one second. This will take effect after the next screen update.</p>
<dt><code>&gt;</code></p>
<dd>Increase the cycle time (interval length) by one second. This will take effect after the next screen update.</p>
<dt><code>]</code></p>
<dd>Scroll forward through the bottom part of the display, if there are files/file systems/clients/procedures not being displayed due to lack of space.</p>
<dt><code>[</code></p>
<dd>Scroll back.</p>
<dt><code>q</code></p>
<dd>Exit <i>nfswatch</i>. Using the interrupt key will also cause <i>nfswatch</i> to exit.</dl>
<p> Typing any other character will cause a help screen to be displayed.</p>
<h2>Options</h2>
<p><i>nfswatch</i> can usually be run without arguments and will obtain useful results. However, for those occasions when the defaults are not good enough, the following options are provided:</p>
<dl>
<dt><code>-dst</code> <i>dsthost</i></p>
<dd>Monitor packets destined for <i>dsthost</i> instead of the local host.</p>
<dt><code>-src</code> <i>srchost</i></p>
<dd>Restrict packets being counted to those sent by <i>srchost</i>.</p>
<dt><code>-server</code> <i>serverhost</i></p>
<dd>Restrict packets being counted to those sent to or from <i>serverhost</i>.</p>
<dt><code>-all</code></p>
<dd>Monitor packets to and from all <font SIZE="-1">NFS</font> servers on the local network.</p>
<dt><code>-dev</code> <i>device</i></p>
<dd><code>On non-DEC systems</code>: Use network interface device <i>device</i> to read packets from. By default, <i>nfswatch</i> will use the system&#8217;s default network device for an Internet datagram. <code>On Ultrix or DEC OSF/1</code>: <i>device</i> specifies the packet filter interface from which to read packets. You can specify interfaces either by their actual names (such as <i>ln0</i>) or by their generic packet filter interface names (<i>pfN,</i> for <i>N</i> a small integer). By default, <i>pf0</i> (the first configured interface that supports the packet filter) is used.</p>
<dt><code>-allif</code></p>
<dd>Read packets from all configured network interfaces, instead of a single device. <code>On Irix</code>: The first five (0-4) of each of the following devices are checked: <i>ec</i>, <i>et</i>, <i>fxp</i>, <i>enp</i>, and <i>epg</i>. If configured, they will be monitored. <code>On SunOS</code>: The first five <i>le</i> (0-4) devices, the first five <i>ie</i> (0-4) devices, and the first five <i>fddi</i> (0-4) devices are checked, and if configured, will be monitored. <code>On System V Release 4</code>: The first five <i>emd</i> (0-4) devices are checked, and if configured, will be monitored. <code>On Ultrix and DEC OSF/1</code>: The first ten <i>pf</i> devices (0-9) are checked, and if configured, will be monitored.</p>
<dt><code>-f</code> <i>filelist</i></p>
<dd>Read a list of file names (one per line) from <i>filelist</i> and monitor the <font SIZE="-1">NFS</font> traffic to these files in addition to the normal monitoring of exported file systems.</p>
<dt><code>-lf</code> <i>logfile</i></p>
<dd>When logging, write information to the file <i>logfile</i>. The default is <i>nfswatch.log</i>.</p>
<dt><code>-sf</code> <i>snapfile</i></p>
<dd>Write snapshots to the file <i>snapfile</i>. The default is <i>nfswatch.snap</i>.</p>
<dt><code>-map</code> <i>mapfile</i></p>
<dd>Read a list of device names and file system names (one pair per line) from <i>mapfile</i> and translate from one to the other when displaying file system names.</p>
<dt><code>-T</code> <i>maxtime</i></p>
<dd>Terminate execution after running for <i>maxtime</i> seconds. This is primarily for use with the <code>-bg</code> option.</p>
<dt><code>-t</code> <i>timeout</i></p>
<dd>Set the cycle time (interval length) to <i>timeout</i> seconds. The default is 10. The cycle time may also be adjusted from the command prompt.</p>
<dt><code>-fs</code></p>
<dd>Display the file system <font SIZE="-1">NFS</font> monitoring data instead of the individual file data. This option is only meaningful if the <code>-f</code> <i>filelist</i> option was specified. The display may also be controlled from the command prompt.</p>
<dt><code>-if</code></p>
<dd>Display the individual file <font SIZE="-1">NFS</font> monitoring data instead of the file system data. This option is only meaningful if the <code>-f</code> <i>filelist</i> option was specified. The display may also be controlled from the command prompt.</p>
<dt><code>-auth</code></p>
<dd>Display statistics on authentication packets (individual users).</p>
<dt><code>-procs</code></p>
<dd>Display statistics on <font SIZE="-1">NFS</font> procedures (RPC calls) instead of per-file or per-filesystem data.</p>
<dt><code>-procs3</code></p>
<dd>Display statistics on <font SIZE="-1">NFS v3</font> procedures (RPC calls) instead of per-file or per-filesystem data.</p>
<dt><code>-client</code></p>
<dd>Display statistics on <font SIZE="-1">NFS</font> client operation rates instead of per-file or per-filesystem data.</p>
<dt><code>-usage</code></p>
<dd>Set file system, procedure, or client display to be sorted in declining order of percent usage. By default, the display is sorted alphabetically. This may also be toggled from the command prompt.</p>
<dt><code>-l</code></p>
<dd>Turn logging on at startup time. Logging is turned off by default, but may be enabled from the command prompt.</p>
<dt><code>-bg</code></p>
<dd>Start as a daemon, running in the background. No screen updates will be performed; all data will be written to the log file only. When started with this option, <i>nfswatch</i> will print the process id of the daemon process. To terminate <i>nfswatch</i>, send the process a SIGTERM signal, or use the <code>-T</code> option to set the maximum execution time.</dl>
<h2>Bugs</h2>
<p>To monitor <font SIZE="-1">NFS</font> traffic to files and file systems, <i>nfswatch</i> must extract information from the <font SIZE="-1">NFS</font> file handle. The file handle is a server-specific item, and its contents vary from vendor to vendor and operating system to operating system. Unfortunately, there is no server-independent way to extract information from a file handle. <i>nfswatch</i> uses a set of heuristics to parse the file handle format used by many popular NFS servers, but in some cases there is no way to disambiguate the file handle format, and the program may get the wrong answer. It should, however, get the right answer for file handles generated by the host it is running on. </p>
<p> <i>nfswatch</i> uses the Snoop (<i><a href="/docs/linux/man/7-snoop/">snoop</a></i>(7)) network monitoring protocol under Irix 4.<i>x</i>, the Network Interface Tap (<i><a href="/docs/linux/man/4-nit/">nit</a></i>(4)) under SunOS 4.<i>x</i>, the Data Link Provider Interface (<i><a href="/docs/linux/man/7-dlpi/">dlpi</a></i>(7)) under SunOS 5.<i>x</i> (Solaris 2.<i>x</i>) and System V Release 4, the Packet Filter {(<i><a href="/docs/linux/man/4-packetfilter/">packetfilter</a></i>(4)) under Ultrix (4.0 or later); (<i><a href="/docs/linux/man/7-packetfilter/">packetfilter</a></i>(7)) under DEC OSF/1 (V1.3 or later)}, and the packet interface (<i><a href="/docs/linux/man/7-packet/">packet</a></i>(7)) under Linux. To run on other systems, code will have to be written to read packets from the network in promiscuous mode. </p>
<p> On Ultrix systems, FDDI is only supported under appropriately patched versions of Ultrix 4.2 (the kernel modules net_common.o and pfilt.o must be replaced; contact your Customer Support Center). Native FDDI support is standard in Ultrix 4.3 and later systems.</p>
<h2>See Also</h2>
<p><i><a href="//www.systutorials.com/docs/linux/man/8c-etherfind/">etherfind</a></i>(8c), <i><a href="/docs/linux/man/7-dlpi/">dlpi</a></i>(7), <i><a href="/docs/linux/man/4-nit/">nit</a></i>(4), <i><a href="//www.systutorials.com/docs/linux/man/8L-nfslogsum/">nfslogsum</a></i>(8L), <i>packetfilter</i>(4/7), <i><a href="//www.systutorials.com/docs/linux/man/1m-snoop/">snoop</a></i>(1m), <i><a href="/docs/linux/man/7-snoop/">snoop</a></i>(7), <i><a href="/docs/linux/man/7-packet/">packet</a></i>(7)</p>
<h2>Authors</h2>
<p>David A. Curry<br />
 Purdue University<br />
 Engineering Computer Network<br />
 1285 Electrical Engineering Building<br />
 West Lafayette, <font SIZE="-1">IN</font> 47907-1285<br />
 davy [at] ecn.purdue.edu </p>
<p> Jeffrey C. Mogul<br />
 Digital Equipment Corporation<br />
 Western Research Laboratory<br />
 250 University Avenue<br />
 Palo Alto, <font SIZE="-1">CA</font> 94301<br />
 mogul [at] wrl.dec.com </p>
<p> Christian Iseli<br />
 Ludwig Institute for Cancer Research<br />
 UNIL &#8211; BEP<br />
 Lausanne, <font SIZE="-1">CH</font>-1015<br />
 Christian.Iseli [at] licr.org</p>
