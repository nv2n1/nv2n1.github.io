---
title: "gdomap(8)"
name: "gdomap"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gdomap/"
description: "gdomap – GNUstep Distributed Objects name server"
---

<p>gdomap &#8211; GNUstep Distributed Objects name server </p>
<h2>Synopsis</h2>
<p><code>gdomap</code> [<code>-C</code>|<code>-H</code>] [<code>-I</code> <i>pidfile</i>] [<code>-L</code> <i>name</i>] [<code>-M</code> <i>name</i>] [<code>-N</code>] [<code>-P</code> <i>number</i>] [<code>-R</code> <i>name</i>] [<code>-T</code> <i>type</i>] [<code>-U</code> <i>name</i>] [<code>-a</code> <i>file</i>] [<code>-c</code> <i>file</i>] [<code>-d</code>] [<code>-f</code>] [-i <i>seconds</i>] [-j <i>path</i>] [<code>-p</code>] </p>
<h2>Description</h2>
<p><code>gdomap</code> The gdomap daemon is used by GNUstep programs to look up distributed objects of processes running across the network (and between different user accounts on a single machine). The daemon is NOT used for lookup where two processes belonging to the same user are using a host-local connection. This manual page explains the usage of gdomap. For design and implementation information (and special notes for packagers), please see the HTML documentation installed in $GNUSTEP_SYSTEM_DOC, under Command-line Tools. Usually the gdomap daemon is started at system boot time and binds itself to port 538. See the <i>GNUstep Build Guide </i> for a sample startup script. By default gdomap probes every machine on the local network to see if there is a copy of gdomap running on it. This is done for class-C networks and subnets of class-C networks. If your host is on a class-B or class-A net then the default behaviour is to treat it as a class-C net and probe only the hosts that would be expected on a class-C network of the same number. If you are running on a class-A or class-B network, or if your net has a large number of hosts which will not have gdomap on them &#8211; you may want to supply a configuration file listing the hosts to be probed explicitly, rather than getting gdomap to probe all hosts on the local net. You may also want to supply the <i>configuration file</i> so that hosts which are not actually on your local network can still be found when your code tries to connect to a host using @&quot;*&quot; as the host name. NB. this functionality does not exist in OpenStep. A <i>configuration file </i> consists of a list of IP addresses to be probed. The IP addresses should be in standard &#8216;dot&#8217; notation, one per line. Empty lines are permitted in the configuration file. Anything on a line after a hash (&#8216;#&#8217;) is ignored. You tell gdomap about the config file with the &#8216;-c&#8217; command line option. gdomap uses the SIOCGIFCONF ioctl to build a list of IP addresses and netmasks for the network interface cards on your machine. On some operating systems, this facility is not available (or is broken), so you must tell gdomap the addresses and masks of the interfaces using the &#8216;-a&#8217; command line option. The file named with &#8216;-a&#8217; should contain a series of lines with space separated pairs of addresses and masks in &#8216;dot&#8217; notation. You must NOT include loopback interfaces in this list. If you want to support broadcasting of probe information on a network, you may supply the broadcast address as a third item on the line. If your operating system has some other method of giving you a list of network interfaces and masks, please send me example code so that I can implement it in gdomap. </p>
<h2>Options</h2>
<dl>
<dt><code>-C</p>
<dd>help about configuration</p>
<dt>-H</p>
<dd>general help</p>
<dt>-I</p>
<dd>pid file to write pid</p>
<dt>-L </code><i>name</p>
<dd>perform lookup for name then quit.</p>
<dt></i><code>-M </code><i>name</p>
<dd>machine name for </i><code>-L</code> and <code>-N</code></p>
<dt><code>-N</p>
<dd>list all names registered on host</p>
<dt>-P </code><i>number</p>
<dd>port number required for </i><code>-R </code> option.</p>
<dt><code>-R </code><i>name</p>
<dd>register name locally then quit.</p>
<dt></i><code>-T </code><i>type</p>
<dd>port type for </i><code>-L</code> , <code>-R</code> and <code>-U </code> options &#8211; tcp_gdo, udp_gdo, tcp_foreign, udp_foreign.</p>
<dt><code>-U </code><i>name</p>
<dd>unregister name locally then quit.</p>
<dt></i><code>-a </code><i>file</p>
<dd>use config file for interface list.</p>
<dt></i><code>-c </code><i>file</p>
<dd>use config file for probe.</p>
<dt></i><code>-d</p>
<dd>extra debug logging (normally via syslog).</p>
<dt>-f</p>
<dd>avoid fork() to make debugging easy</p>
<dt>-i </code><i>seconds</p>
<dd>re-probe at this interval (roughly), min 60</p>
<dt></i><code>-j </code><i>path</p>
<dd>place the process in a chroot jail at this path rather than in /tmp</p>
<dt></i><code>-p</p>
<dd>disable probing for other servers</dl>
<p> </code></p>
<h2>Files</h2>
<p>Use the <code>-c </code> option to specify a configuration file for gdomap. See under <code>DESCRIPTION</code> for possible configurations.</p>
<h2>Diagnostics</h2>
<p>Kill with SIGUSR1 to obtain a dump of all known peers in /tmp/gdomap.dump </p>
<p> <code>gdomap -N</code> lists all registered names on the local host.</p>
<h2>See Also</h2>
<p><code>gdomap -C</code> gives above instructions on how to set up gdomap. <a href="/docs/linux/man/1-gdnc/">gdnc</a>(1), <a href="/docs/linux/man/7-gnustep/">GNUstep</a>(7), <a href="/docs/linux/man/1-gpbs/">gpbs</a>(1) <i>The GNUstep Build Guide</i> example rc script: &lt;<a rel="nofollow" href="http://gnustep.made-it.com/BuildGuide/index.html#GNUSTEP.SERVICES">http://gnustep.made-it.com/BuildGuide/index.html#GNUSTEP.SERVICES</a>&gt; </p>
<h2>History</h2>
<p>Work on <code>gdomap</code> started in October 1996. </p>
<p> This manual page first appeared in gnustep-base 1.7.1 (June 2003).</p>
<h2>Authors</h2>
<p><code>gdomap</code> was written by Richard Frith-Macdonald &lt;rfm [at] gnu.org&gt; </p>
<p> This manual page was put together by Martin Brecher &lt;martin [at] mb-itconsulting.com&gt;.</p>
