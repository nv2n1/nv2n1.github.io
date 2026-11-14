---
title: "smokeping_probes_anotherssh(3)"
name: "smokeping_probes_anotherssh"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_probes_anotherssh/"
---

Smokeping::probes::AnotherSSH - Another SSH probe 

<h2>Synopsis</h2><pre> *** Probes ***
 +AnotherSSH
 forks = 5
 offset = 50%
 step = 300
 # The following variables can be overridden in each target section
 greeting = SSH-Latency-Measurement-Sorry-for-this-logmessage
 interval = established
 mininterval = 0.5
 pings = 5
 port = 22
 timeout = 5
 # [...]
 *** Targets ***
 probe = AnotherSSH # if this should be the default probe
 # [...]
 + mytarget
 # probe = AnotherSSH # if the default probe is something else
 host = my.host
 greeting = SSH-Latency-Measurement-Sorry-for-this-logmessage
 interval = established
 mininterval = 0.5
 pings = 5
 port = 22
 timeout = 5</pre><h2>Description</h2>Latency measurement using <font SIZE="-1">SSH.</font> This generates Logfile messages on the other Host, so get permission from the owner first!
<h2>Variables</h2>Supported probe-specific variables:
<dl COMPACT><dt>forks
<dd>Run this many concurrent processes at maximum 

 Example value: 5 

 Default value: 5
<dt>offset
<dd>If you run many probes concurrently you may want to prevent them from hitting your network all at the same time. Using the probe-specific offset parameter you can change the point in time when each probe will be run. Offset is specified in % of total interval, or alternatively as 'random', and the offset from the 'General' section is used if nothing is specified here. Note that this does <font SIZE="-1">NOT</font> influence the rrds itself, it is just a matter of when data acqusition is initiated. (This variable is only applicable if the variable 'concurrentprobes' is set in the 'General' section.) 

 Example value: 50%
<dt>step
<dd>Duration of the base interval that this probe should use, if different from the one specified in the 'Database' section. Note that the step in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change the step parameter afterwards, you'll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. (This variable is only applicable if the variable 'concurrentprobes' is set in the 'General' section.) 

 Example value: 300</dl>
 

 Supported target-specific variables:
<dl COMPACT><dt>greeting
<dd>Greeting string to send to the <font SIZE="-1">SSH</font> Server. This will appear in the Logfile. Use this to make clear, who you are and what you are doing to avoid confusion. 

 Also, don't use something that is a valid version string. This probe assumes that the connection gets terminated because of protocol mismatch. 

 Default value: SSH-Latency-Measurement-Sorry-for-this-logmessage
<dt>interval
<dd>The interval to be measured. One of:
<dl COMPACT><dd><dl COMPACT><dt>connect
<dd>Interval between <i>connect()</i> and the greeting string from the host.
<dt>established
<dd>Interval between our greeting message and the end of the connection because of Protocol mismatch. This is the default.
<dt>complete
<dd>From <i>connect()</i> to the end of the connection.</dl></dl><dl COMPACT><dd>Default value: established</dl><dt>mininterval
<dd>Minimum interval between the start of two connection attempts in (possibly fractional) seconds. 

 Default value: 0.5
<dt>pings
<dd>How many pings should be sent to each target, if different from the global value specified in the Database section. Note that the number of pings in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change this parameter afterwards, you'll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. 

 Example value: 5
<dt>port
<dd>Connect to this port. 

 Default value: 22
<dt>timeout
<dd>Timeout for the connection. 

 Default value: 5</dl><h2>Authors</h2>Christoph Heine &lt;Christoph.Heine [at] HaDiKo.DE&gt;
