---
title: "smokeping_probes_iosping(3)"
name: "smokeping_probes_iosping"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_probes_iosping/"
---

Smokeping::probes::IOSPing - Cisco IOS Probe for SmokePing 

<h2>Synopsis</h2><pre> *** Probes ***
 +IOSPing
 binary = /usr/bin/rsh # mandatory
 forks = 5
 offset = 50%
 packetsize = 56
 step = 300
 timeout = 15
 # The following variables can be overridden in each target section
 ioshost = my.cisco.router # mandatory
 iosint = Ethernet 1/0
 iosuser = admin
 pings = 5
 # [...]
 *** Targets ***
 probe = IOSPing # if this should be the default probe
 # [...]
 + mytarget
 # probe = IOSPing # if the default probe is something else
 host = my.host
 ioshost = my.cisco.router # mandatory
 iosint = Ethernet 1/0
 iosuser = admin
 pings = 5</pre><h2>Description</h2>Integrates Cisco IOS as a probe into smokeping. Uses the rsh / remsh protocol to run a ping from an IOS device.
<h2>Variables</h2>Supported probe-specific variables:
<dl COMPACT><dt>binary
</dt><dd>The binary option specifies the path of the binary to be used to connect to the IOS device. Commonly used binaries are /usr/bin/rsh and /usr/bin/remsh, although any script or binary should work if can be called as 
 <pre> /path/to/binary [ -l user ] router ping</pre>to produce the IOS ping dialog on stdin &amp; stdout. 
 Example value: /usr/bin/rsh 
 This setting is mandatory.
</dd><dt>forks
</dt><dd>Run this many concurrent processes at maximum 
 Example value: 5 
 Default value: 5
</dd><dt>offset
</dt><dd>If you run many probes concurrently you may want to prevent them from hitting your network all at the same time. Using the probe-specific offset parameter you can change the point in time when each probe will be run. Offset is specified in % of total interval, or alternatively as 'random', and the offset from the 'General' section is used if nothing is specified here. Note that this does NOT influence the rrds itself, it is just a matter of when data acqusition is initiated. (This variable is only applicable if the variable 'concurrentprobes' is set in the 'General' section.) 
 Example value: 50%
</dd><dt>packetsize
</dt><dd>The (optional) packetsize option lets you configure the packetsize for the pings sent. 
 Default value: 56
</dd><dt>step
</dt><dd>Duration of the base interval that this probe should use, if different from the one specified in the 'Database' section. Note that the step in the RRD files is fixed when they are originally generated, and if you change the step parameter afterwards, you'll have to delete the old RRD files or somehow convert them. (This variable is only applicable if the variable 'concurrentprobes' is set in the 'General' section.) 
 Example value: 300
</dd><dt>timeout
</dt><dd>How long a single 'ping' takes at maximum 
 Example value: 15 
 Default value: 5</dd></dl>
 

 Supported target-specific variables:
<dl COMPACT><dt>ioshost
</dt><dd>The ioshost option specifies the IOS device which should be used for the ping. 
 Example value: my.cisco.router 
 This setting is mandatory.
</dd><dt>iosint
</dt><dd>The (optional) iosint option allows you to specify the source address or interface in the IOS device. The value should be an IP address or an interface name such as ``Ethernet 1/0''. If this option is omitted, the IOS device will pick the IP address of the outbound interface to use. 
 Example value: Ethernet 1/0
</dd><dt>iosuser
</dt><dd>The (optional) iosuser option allows you to specify the remote username the IOS device. If this option is omitted, the username defaults to the default user used by the remsh command (usually the user running the remsh command, ie the user running SmokePing). 
 Example value: admin
</dd><dt>pings
</dt><dd>How many pings should be sent to each target, if different from the global value specified in the Database section. Note that the number of pings in the RRD files is fixed when they are originally generated, and if you change this parameter afterwards, you'll have to delete the old RRD files or somehow convert them. 
 Example value: 5</dd></dl><h2>Authors</h2>Paul J Murphy &lt;paul [at] murph.org&gt; 

 based on Smokeping::probes::FPing by 

 Tobias Oetiker &lt;tobi [at] oetiker.ch&gt;
<h2>Notes</h2><h3>IOS Configuration</h3>The IOS device must have rsh enabled and an appropriate trust defined, eg: 

 <pre> !
 ip rcmd rsh-enable
 ip rcmd remote-host smoke 192.168.1.2 smoke enable
 !</pre>Some IOS devices have a maximum of 5 VTYs available, so be careful not to hit a limit with the 'forks' variable.
<h3>Password authentication</h3>It is not possible to use password authentication with rsh or remsh due to fundamental limitations of the protocol.
<h3>Ping packet size</h3>The FPing manpage has the following to say on the topic of ping packet size: 

 Number of bytes of ping data to send. The minimum size (normally 12) allows room for the data that fping needs to do its work (sequence number, timestamp). The reported received data size includes the IP header (normally 20 bytes) and ICMP header (8 bytes), so the minimum total size is 40 bytes. Default is 56, as in ping. Maximum is the theoretical maximum IP datagram size (64K), though most systems limit this to a smaller, system-dependent number.
