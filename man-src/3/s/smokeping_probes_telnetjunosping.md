---
title: "smokeping_probes_telnetjunosping(3)"
name: "smokeping_probes_telnetjunosping"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_probes_telnetjunosping/"
---

Smokeping::probes::TelnetJunOSPing - Juniper JunOS Probe for SmokePing 

<h2>Synopsis</h2><pre> *** Probes ***
 +TelnetJunOSPing
 forks = 5
 offset = 50%
 packetsize = 100
 step = 300
 timeout = 15
 # The following variables can be overridden in each target section
 junospass = password # mandatory
 junosuser = user # mandatory
 pings = 5
 psource = 192.168.2.129
 source = 192.168.2.1 # mandatory
 # [...]
 *** Targets ***
 probe = TelnetJunOSPing # if this should be the default probe
 # [...]
 + mytarget
 # probe = TelnetJunOSPing # if the default probe is something else
 host = my.host
 junospass = password # mandatory
 junosuser = user # mandatory
 pings = 5
 psource = 192.168.2.129
 source = 192.168.2.1 # mandatory</pre><h2>Description</h2>Integrates Juniper JunOS as a probe into smokeping. Uses the telnet protocol to run a ping from an JunOS device (source) to another device (host). This probe basically uses the ``extended ping'' of the Juniper JunOS. You have the option to specify which interface the ping is sourced from as well.
<h2>Variables</h2>Supported probe-specific variables:
<dl COMPACT><dt>forks
<dd>Run this many concurrent processes at maximum 

 Example value: 5 

 Default value: 5
<dt>offset
<dd>If you run many probes concurrently you may want to prevent them from hitting your network all at the same time. Using the probe-specific offset parameter you can change the point in time when each probe will be run. Offset is specified in % of total interval, or alternatively as 'random', and the offset from the 'General' section is used if nothing is specified here. Note that this does <font SIZE="-1">NOT</font> influence the rrds itself, it is just a matter of when data acqusition is initiated. (This variable is only applicable if the variable 'concurrentprobes' is set in the 'General' section.) 

 Example value: 50%
<dt>packetsize
<dd>The (optional) packetsize option lets you configure the packetsize for the pings sent. 

 Default value: 100
<dt>step
<dd>Duration of the base interval that this probe should use, if different from the one specified in the 'Database' section. Note that the step in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change the step parameter afterwards, you'll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. (This variable is only applicable if the variable 'concurrentprobes' is set in the 'General' section.) 

 Example value: 300
<dt>timeout
<dd>How long a single 'ping' takes at maximum 

 Example value: 15 

 Default value: 5</dl>
 

 Supported target-specific variables:
<dl COMPACT><dt>junospass
<dd>The junospass option allows you to specify the password for the username specified with the option junosuser. 

 Example value: password 

 This setting is mandatory.
<dt>junosuser
<dd>The junosuser option allows you to specify a username that has ping capability on the JunOS Device. 

 Example value: user 

 This setting is mandatory.
<dt>pings
<dd>How many pings should be sent to each target, if different from the global value specified in the Database section. Note that the number of pings in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change this parameter afterwards, you'll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. 

 Example value: 5
<dt>psource
<dd>The (optional) psource option specifies an alternate <font SIZE="-1">IP</font> address or Interface from which you wish to source your pings from. Routers can have many many <font SIZE="-1">IP</font> addresses, and interfaces. When you ping from a router you have the ability to choose which interface and/or which <font SIZE="-1">IP</font> address the ping is sourced from. Specifying an IP/interface does not necessarily specify the interface from which the ping will leave, but will specify which address the packet(s) appear to come from. If this option is left out the JunOS Device will source the packet automatically based on routing and/or metrics. If this doesn't make sense to you then just leave it out. 

 Example value: 192.168.2.129
<dt>source
<dd>The source option specifies the JunOS device to which we telnet. This is an <font SIZE="-1">IP</font> address of an JunOS Device that you/your server: <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1) Have the ability to telnet to
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>2) Have a valid username and password for
 

 Example value: 192.168.2.1 

 This setting is mandatory.</dl><h2>Authors</h2>S H A N &lt;shanali [at] yahoo.com&gt; 

 based <font SIZE="-1">HEAVILY</font> on Smokeping::probes::TelnetIOSPing by 

 John A Jackson &lt;geonjay [at] infoave.net&gt; 

 based on Smokeping::probes::JunOSPing by 

 Paul J Murphy &lt;paul [at] murph.org&gt; 

 based on Smokeping::probes::FPing by 

 Tobias Oetiker &lt;tobi [at] oetiker.ch&gt;
<h2>Notes</h2><h3>JunOS configuration</h3>The JunOS device should have a username/password configured, as well as the ability to connect to the <font SIZE="-1">VTY</font>(s). 

 Some JunOS devices have a maximum of 5 VTYs available, so be careful not to hit a limit with the 'forks' variable.
<h3>Requirements</h3>This module requires the Net::Telnet module for perl. This is usually included on most newer OSs which include perl.
<h3>Debugging</h3>There is some <font SIZE="-1">VERY</font> rudimentary debugging code built into this module (it's based on the debugging code written into Net::Telnet). It will log information into three files ``TIPreturn'', ``TIPoutlog'', and ``TIPdump''. These files will be written out into your current working directory (<font SIZE="-1">CWD</font>). You can change the names of these files to something with more meaning to you.
<h3>Password authentication</h3>You should be advised that the authentication method of telnet uses clear text transmissions...meaning that without proper network security measures someone could sniff your username and password off the network. I may attempt to incorporate <font SIZE="-1">SSH</font> in a future version of this module, but it is very doubtful. Right now <font SIZE="-1">SSH</font> adds a <font SIZE="-1">LOT</font> of processing overhead to a router, and isn't incredibly easy to implement in perl. 

 Having said this, don't be too scared of telnet. Remember, the original JunOSPing module used <font SIZE="-1">RSH,</font> which is even more scary to use from a security perspective.
<h3>Ping packet size</h3>The FPing manpage has the following to say on the topic of ping packet size: 

 Number of bytes of ping data to send. The minimum size (normally 12) allows room for the data that fping needs to do its work (sequence number, timestamp). The reported received data size includes the <font SIZE="-1">IP</font> header (normally 20 bytes) and <font SIZE="-1">ICMP</font> header (8 bytes), so the minimum total size is 40 bytes. Default is 56, as in ping. Maximum is the theoretical maximum <font SIZE="-1">IP</font> datagram size (64K), though most systems limit this to a smaller, system-dependent number.
