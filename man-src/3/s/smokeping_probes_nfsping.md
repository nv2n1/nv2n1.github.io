---
title: "smokeping_probes_nfsping(3)"
name: "smokeping_probes_nfsping"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_probes_nfsping/"
description: "Smokeping::probes::NFSping – NFSping Probe for SmokePing"
---

<p>Smokeping::probes::NFSping &#8211; NFSping Probe for SmokePing </p>
<h2>Synopsis</h2>
<pre> *** Probes ***
 +NFSping
 binary = /usr/local/bin/nfsping # mandatory
 blazemode = true
 hostinterval = 1.5
 mininterval = 0.001
 offset = 50%
 pings = 20
 step = 300
 timeout = 1.5
 # [...]
 *** Targets ***
 probe = NFSping # if this should be the default probe
 # [...]
 + mytarget
 # probe = NFSping # if the default probe is something else
 host = my.host</pre>
<h2>Description</h2>
<p>Integrates NFSping as a probe into smokeping. The variable <code>binary</code> must point to your copy of the NFSping program. </p>
<p> NFSping can be downloaded from: </p>
<p> &lt;<a rel="nofollow" href="https://github.com/mprovost/NFSping">https://github.com/mprovost/NFSping</a>&gt; </p>
<p> In <code>blazemode</code>, NFSping sends one more ping than requested, and discards the first <font SIZE="-1">RTT</font> value returned as it&#8217;s likely to be an outlier.</p>
<h2>Variables</h2>
<p>Supported probe-specific variables:</p>
<dl COMPACT>
<dt>binary</p>
<dd>The location of your nfsping binary. </p>
<p> Example value: /usr/local/bin/nfsping </p>
<p> This setting is mandatory.</p>
<dt>blazemode</p>
<dd>Send an extra ping and then discard the first answer since the first is bound to be an outlier. </p>
<p> Example value: true</p>
<dt>hostinterval</p>
<dd>The nfsping &#8220;-p&#8221; parameter, but in (possibly fractional) seconds rather than milliseconds, for consistency with other Smokeping probes. This parameter sets the time that nfsping waits between successive packets to an individual target. </p>
<p> Example value: 1.5</p>
<dt>mininterval</p>
<dd>The nfsping &#8220;-i&#8221; parameter, but in (probably fractional) seconds rather than milliseconds, for consistency with other Smokeping probes. This is the interval between pings to successive targets. </p>
<p> Example value: 0.001 </p>
<p> Default value: 0.01</p>
<dt>offset</p>
<dd>If you run many probes concurrently you may want to prevent them from hitting your network all at the same time. Using the probe-specific offset parameter you can change the point in time when each probe will be run. Offset is specified in % of total interval, or alternatively as &#8216;random&#8217;, and the offset from the &#8216;General&#8217; section is used if nothing is specified here. Note that this does <font SIZE="-1">NOT</font> influence the rrds itself, it is just a matter of when data acqusition is initiated. (This variable is only applicable if the variable &#8216;concurrentprobes&#8217; is set in the &#8216;General&#8217; section.) </p>
<p> Example value: 50%</p>
<dt>pings</p>
<dd>How many pings should be sent to each target, if different from the global value specified in the Database section. Note that the number of pings in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change this parameter afterwards, you&#8217;ll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. </p>
<p> Example value: 20</p>
<dt>step</p>
<dd>Duration of the base interval that this probe should use, if different from the one specified in the &#8216;Database&#8217; section. Note that the step in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change the step parameter afterwards, you&#8217;ll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. (This variable is only applicable if the variable &#8216;concurrentprobes&#8217; is set in the &#8216;General&#8217; section.) </p>
<p> Example value: 300</p>
<dt>timeout</p>
<dd>The nfsping &#8220;-t&#8221; parameter, but in (possibly fractional) seconds rather than milliseconds, for consistency with other Smokeping probes. </p>
<p> Example value: 1.5</dl>
<h2>Authors</h2>
<p>Tobias Oetiker &lt;tobi [at] oetiker.ch&gt; Matt Provost &lt;mprovost [at] termcap.net&gt;</p>
