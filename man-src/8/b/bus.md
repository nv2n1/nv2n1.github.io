---
title: "bus(8)"
name: "bus"
section: "8"
letter: "b"
url: "/docs/linux/man/8-bus/"
description: "les, bus – ATM LAN Emulation service demons"
---

<p>les, bus &#8211; ATM LAN Emulation service demons</p>
<h2>Synopsis</h2>
<p><code>les</code> [<code>-d&nbsp;<wbr></code><i>module</i>] [<code>-m&nbsp;<wbr></code><i>module</i>] [<code>-f&nbsp;<wbr></code><i>configuration_file</i>] </p>
<p> <code>bus</code> [<code>-d&nbsp;<wbr></code><i>module</i>] [<code>-m&nbsp;<wbr></code><i>module</i>] [<code>-f&nbsp;<wbr></code><i>configuration_file</i>]</p>
<h2>Description</h2>
<p>LE Service consists of three components: LAN Emulation Configuration Server (<code><a href="/docs/linux/man/8-lecs/">lecs</a>(8)</code>), LAN Emulation Server (<code>les</code>) and Broadcast and Unknown Server (<code>bus</code>). </p>
<p> <code>Les</code> performs the control coordination function for the emulated LAN. LE clients register MAC addresses and/or route descriptors they represent to <code>les</code>, and later query it when they want to resolve MAC addresses/route descriptors into ATM addresses. Other LE control messages which are to be distributed to every client in ELAN are also sent to <code>les</code>. <code>Les</code> forwards these messages using Control Distribute VCC which it has set up to every client in ELAN. </p>
<p> <code>Bus</code> handles data sent by clients to broadcast and multicast MAC addresses and some of the data directed to unicast addresses. LE Client has a possibility to send data directed to some unicast address to the <code>bus</code> before target&#8217;s ATM address has been resolved and the Data Direct VCC has been established. </p>
<p> Configuration file example for <code>les</code> and <code>bus</code>: </p>
<pre>[main]
memdebug=True
debug=True
[load]
#memdebug=True
#debug=True
[conn]
debug=True
#S1, LE Server's ATM address
#S1=:47:00:23:00:00:00:03:00:00:01:00:02:01:00:20:ea:00:05:aa:00
S1=:47:00:23:00:00:00:03:03:00:01:00:02:01:00:20:ea:00:0a:e9:01
#S2, LAN Type
S2=&quot;802.3&quot;
#S3, Maximum Frame Size
S3=1516
#S4, Join Timeout, s
S4=15
#S5, Maximum Frame Age, s
S5=6
#S6, BUS Atm address
S6=:47:00:23:00:00:00:03:03:00:01:00:02:01:00:20:ea:00:0a:e9:02 #viulu
#S6=0,0,170
#ELANNAME=&quot;asdf&quot;</pre>
<p>The configuration file contains each modules name in brackets followed by variable definitions for that module. The definitions are of form <i>variable=value, </i> where value can be either an integer, a truth value (True/False), a string enclosed in double quotes <i>(string) </i> or an ATM address in hexadecimal format. Variables that can be set are the debug/memdebug for each module and variables S1-S6 as defined in LE specification. </p>
<pre>S1=Address of the LES. This address is used in ATM 
 signalling.
S2=Type of the emulated LAN. Valid values is &quot;802.3&quot;.
S3=Maximum frame size. Valid value is 1516.
S4=Join Timeout. Time in seconds which LES waits for 
 LE_JOIN_REQUEST before tearing down a connection.
S5=Maximum frame Age. Currently not used.
S6=Address of the BUS. This address is used in ATM signalling.
ELANNAME= Name of the emulated LAN</pre>
<p><code>SIGHUP</code> causes restart of the server. All resources are released and server is started. <code>SIGUSR1</code> causes the server to dump its internal state. <code>SIGUSR2</code> shuts down the server (hopefully) gracefully.</p>
<h2>Options</h2>
<dl>
<dt>
<dt><code>-d&nbsp;<wbr></code><i>module</i></p>
<dd>
<dd>Set debugging messages on for a module. &quot;All&quot; sets debugging on for all modules.</p>
<dt><code>-m&nbsp;<wbr></code><i>module</i></p>
<dd>Set memory debugging messages on for a module. &quot;All&quot; sets debugging on for all modules.</p>
<dt><code>-f&nbsp;<wbr></code><i>configuration_file</i></p>
<dd>Use the specified configuration file instead of <code>.lanevars</code>.</dl>
<h2>Files</h2>
<dl>
<dt><code>.lanevars</code></p>
<dd>configuration file</dl>
<h2>Bugs</h2>
<p>Servers don&#8217;t establish point-to-multipoint connections to LE clients as the specification states, which means that some LE clients won&#8217;t work with these servers. </p>
<p> Supports only IEEE 802.3 / Ethernet type of ELANs. </p>
<p> This manual page is confusing.</p>
<h2>Author</h2>
<p>Marko Kiiskila, TUT &lt;carnil [at] cs.tut.fi&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-lecs/">lecs</a>(8), <a href="/docs/linux/man/8-atmsigd/">atmsigd</a>(8), <a href="/docs/linux/man/8-zeppelin/">zeppelin</a>(8) </p>
