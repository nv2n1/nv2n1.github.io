---
title: "smokeping_probes_remotefping(3)"
name: "smokeping_probes_remotefping"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_probes_remotefping/"
description: "Smokeping::probes::RemoteFPing – Remote FPing Probe for SmokePing"
---

<p>Smokeping::probes::RemoteFPing &#8211; Remote FPing Probe for SmokePing </p>
<h2>Synopsis</h2>
<pre> *** Probes ***
 +RemoteFPing
 binary = /usr/bin/ssh # mandatory
 blazemode = true
 hostinterval = 1.5
 mininterval = 0.001
 offset = 50%
 packetsize = 5000
 pings = 20
 rbinary = /usr/bin/fping # mandatory
 rhost = my.pinger.host # mandatory
 ruser = foo
 sourceaddress = 192.168.0.1
 step = 300
 timeout = 1.5
 tos = 0x20
 usestdout = true
 # [...]
 *** Targets ***
 probe = RemoteFPing # if this should be the default probe
 # [...]
 + mytarget
 # probe = RemoteFPing # if the default probe is something else
 host = my.host</pre>
<h2>Description</h2>
<p>Integrates the remote execution of FPing via ssh/rsh into smokeping. The variable <code>binary</code> must point to your copy of the ssh/rsh program. The variable <code>rbinary</code> must point to your copy of the fping program at the remote end.</p>
<h2>Variables</h2>
<p>Supported probe-specific variables:</p>
<dl COMPACT>
<dt>binary</p>
<dd>This variable specifies the path of the remote shell program (usually ssh, rsh or remsh). Any other script or binary that can be called as </p>
<p> binary [ -l ruser ] rhost rbinary </p>
<p> may be used. </p>
<p> Example value: /usr/bin/ssh </p>
<p> This setting is mandatory.</p>
<dt>blazemode</p>
<dd>Send an extra ping and then discarge the first answer since the first is bound to be an outliner. </p>
<p> Example value: true</p>
<dt>hostinterval</p>
<dd>The fping &#8220;-p&#8221; parameter, but in (possibly fractional) seconds rather than milliseconds, for consistency with other Smokeping probes. From <i><a href="/docs/linux/man/1-fping/">fping</a></i>(1): </p>
<p> This parameter sets the time that fping waits between successive packets to an individual target. </p>
<p> Example value: 1.5</p>
<dt>mininterval</p>
<dd>The fping &#8220;-i&#8221; parameter, but in (probably fractional) seconds rather than milliseconds, for consistency with other Smokeping probes. From <i><a href="/docs/linux/man/1-fping/">fping</a></i>(1): </p>
<p> The minimum amount of time between sending a ping packet to any target. </p>
<p> Example value: 0.001 </p>
<p> Default value: 0.01</p>
<dt>offset</p>
<dd>If you run many probes concurrently you may want to prevent them from hitting your network all at the same time. Using the probe-specific offset parameter you can change the point in time when each probe will be run. Offset is specified in % of total interval, or alternatively as &#8216;random&#8217;, and the offset from the &#8216;General&#8217; section is used if nothing is specified here. Note that this does <font SIZE="-1">NOT</font> influence the rrds itself, it is just a matter of when data acqusition is initiated. (This variable is only applicable if the variable &#8216;concurrentprobes&#8217; is set in the &#8216;General&#8217; section.) </p>
<p> Example value: 50%</p>
<dt>packetsize</p>
<dd>The ping packet size (in the range of 12-64000 bytes). </p>
<p> Example value: 5000</p>
<dt>pings</p>
<dd>How many pings should be sent to each target, if different from the global value specified in the Database section. Note that the number of pings in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change this parameter afterwards, you&#8217;ll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. </p>
<p> Example value: 20</p>
<dt>rbinary</p>
<dd>The location of your fping binary. </p>
<p> Example value: /usr/bin/fping </p>
<p> This setting is mandatory.</p>
<dt>rhost</p>
<dd>The <code>rhost</code> option specifies the remote device from where fping will be launched. </p>
<p> Example value: my.pinger.host </p>
<p> This setting is mandatory.</p>
<dt>ruser</p>
<dd>The (optional) <code>ruser</code> option allows you to specify the remote user, if different from the one running the smokeping daemon. </p>
<p> Example value: foo</p>
<dt>sourceaddress</p>
<dd>The fping &#8220;-S&#8221; parameter . From <i><a href="/docs/linux/man/1-fping/">fping</a></i>(1): </p>
<p> Set source address. </p>
<p> Example value: 192.168.0.1</p>
<dt>step</p>
<dd>Duration of the base interval that this probe should use, if different from the one specified in the &#8216;Database&#8217; section. Note that the step in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change the step parameter afterwards, you&#8217;ll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. (This variable is only applicable if the variable &#8216;concurrentprobes&#8217; is set in the &#8216;General&#8217; section.) </p>
<p> Example value: 300</p>
<dt>timeout</p>
<dd>The fping &#8220;-t&#8221; parameter, but in (possibly fractional) seconds rather than milliseconds, for consistency with other Smokeping probes. Note that as Smokeping uses the fping &#8216;counting&#8217; mode (-C), this apparently only affects the last ping. </p>
<p> Example value: 1.5</p>
<dt>tos</p>
<dd>Set the type of service (<font SIZE="-1">TOS</font>) of outgoing <font SIZE="-1">ICMP</font> packets. You need at laeast fping-2.4b2_to3-ipv6 for this to work. Find a copy on <a rel="nofollow" href="http://www.smokeping.org">www.smokeping.org</a>/pub. </p>
<p> Example value: 0x20</p>
<dt>usestdout</p>
<dd>Listen for FPing output on stdout instead of stderr &#8230; (version 3.3+ sends its statistics on stdout). </p>
<p> Example value: true</dl>
<h2>Authors</h2>
<pre> Luis F Balbinot &lt;hades [at] inf.ufrgs.br&gt;
 Niko Tyni &lt;ntyni [at] iki.fi&gt;
 derived from Smokeping::probes::FPing by
 Tobias Oetiker &lt;tobi [at] oetiker.ch&gt;</pre>
<h2>Notes</h2>
<p>It is important to make sure that you can access the remote machine without a password prompt, otherwise this probe will not work properly. To test just try something like this: </p>
<pre> $ ssh foo [at] HostA.foobar.com fping HostB.barfoo.com</pre>
<p>The next thing you see must be fping&#8217;s output. </p>
<p> The <code>rhost</code>, <code>ruser</code> and <code>rbinary</code> variables used to be configured in the Targets section of the first target or its parents They were moved to the Probes section, because the variables aren&#8217;t really target-specific (all the targets are measured with the same parameters). The Targets sections aren&#8217;t recognized anymore.</p>
<h2>Bugs</h2>
<p>This functionality should be in a generic &#8216;remote execution&#8217; module so that it could be used for the other probes too.</p>
