---
title: "ip-monitor(8)"
name: "ip-monitor"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ip-monitor/"
description: "ip-monitor, rtmon – state monitoring"
---

<p>ip-monitor, rtmon &#8211; state monitoring</p>
<h2>Synopsis</h2>
<p><code>ip monitor</code> [ <code>all</code> | <i>OBJECT-LIST</i> ] [ <code>file</code><i> FILENAME </i> ] [ <code>label</code> ] [ <code>all-nsid</code> ] [ <code>dev</code><i> DEVICE </i> ] </p>
<h2>Options</h2>
<dl>
<dt><code>-t</code>,<code> -timestamp</code></p>
<dd>Prints timestamp before the event message on the separated line in format:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Timestamp:&nbsp;&lt;Day&gt;&nbsp;&lt;Month&gt;&nbsp;&lt;DD&gt;&nbsp;&lt;hh:mm:ss&gt;&nbsp;&lt;YYYY&gt;&nbsp;&lt;usecs&gt;&nbsp;usec<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&lt;EVENT&gt; </p>
<dt><code>-ts</code>,<code> -tshort</code></p>
<dd>Prints short timestamp before the event message on the same line in format:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[&lt;YYYY&gt;-&lt;MM&gt;-&lt;DD&gt;T&lt;hh:mm:ss&gt;.&lt;ms&gt;]&nbsp;&lt;EVENT&gt; </p>
</dl>
<h2>Description</h2>
<p>The <code>ip</code> utility can monitor the state of devices, addresses and routes continuously. This option has a slightly different format. Namely, the <code>monitor</code> command is the first in the command line and then the object list follows: <code>ip monitor</code> [ <code>all</code> | <i>OBJECT-LIST</i> ] [ <code>file</code><i> FILENAME </i> ] [ <code>label</code> ] [ <code>all-nsid</code> ] [ <code>dev</code><i> DEVICE </i> ] <i>OBJECT-LIST</i> is the list of object types that we want to monitor. It may contain <code>link</code>, <code>address</code>, <code>route</code>, <code>mroute</code>, <code>prefix</code>, <code>neigh</code>, <code>netconf</code>, <code>rule</code>, <code>nsid</code> and <code>nexthop</code>. If no <code>file</code> argument is given, <code>ip</code> opens RTNETLINK, listens on it and dumps state changes in the format described in previous sections. If the <code>label</code> option is set, a prefix is displayed before each message to show the family of the message. For example: [NEIGH]10.16.0.112 dev eth0 lladdr 00:04:23:df:2f:d0 REACHABLE [LINK]3: eth1: &lt;BROADCAST,MULTICAST&gt; mtu 1500 qdisc pfifo_fast state DOWN group default<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;link/ether 52:54:00:12:34:57 brd ff:ff:ff:ff:ff:ff If the <code>all-nsid</code> option is set, the program listens to all network namespaces that have a nsid assigned into the network namespace were the program is running. A prefix is displayed to show the network namespace where the message originates. Example: [nsid 0]10.16.0.112 dev eth0 lladdr 00:04:23:df:2f:d0 REACHABLE If the <code>file</code> option is given, the program does not listen on RTNETLINK, but opens the given file, and dumps its contents. The file should contain RTNETLINK messages saved in binary format. Such a file can be generated with the <code>rtmon</code> utility. This utility has a command line syntax similar to <code>ip monitor</code>. Ideally, <code>rtmon</code> should be started before the first network configuration command is issued. F.e. if you insert: rtmon file /var/log/rtmon.log in a startup script, you will be able to view the full history later. Nevertheless, it is possible to start <code>rtmon</code> at any time. It prepends the history with the state snapshot dumped at the moment of starting. If the <code>dev</code> option is given, the program prints only events related to this device. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip/">ip</a></code>(8) </p>
<h2>Author</h2>
<p>Original Manpage by Michail Litvak &lt;mci [at] owl.openwall.com&gt;<br />
 Manpage revised by Nicolas Dichtel &lt;nicolas.dichtel [at] 6wind.com&gt;</p>
