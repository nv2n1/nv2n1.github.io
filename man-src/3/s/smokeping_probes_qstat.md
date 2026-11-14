---
title: "smokeping_probes_qstat(3)"
name: "smokeping_probes_qstat"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_probes_qstat/"
description: "Smokeping::probes::Qstat – Qstat Probe for SmokePing"
---

<p>Smokeping::probes::Qstat &#8211; Qstat Probe for SmokePing </p>
<h2>Synopsis</h2>
<pre> *** Probes ***
 +Qstat
 binary = /usr/bin/quakestatba # mandatory
 forks = 5
 game = nexuizs
 mininterval = 0.1
 offset = 50%
 port = 27970
 sourceaddress = 192.168.0.1
 sourceport = 9923-9943
 step = 300
 timeout = 15
 # The following variables can be overridden in each target section
 pings = 5
 # [...]
 *** Targets ***
 probe = Qstat # if this should be the default probe
 # [...]
 + mytarget
 # probe = Qstat # if the default probe is something else
 host = my.host
 pings = 5</pre>
<h2>Description</h2>
<p>Integrates Qstat as a probe into smokeping. The variable <code>binary</code> must point to your copy of the Qstat program. </p>
<p> Make sure to set your pings to 10, most Quake servers seem to throttle after 10 rapid pings. </p>
<p> Set the game parameter to one of the valid options to check a different type</p>
<h2>Variables</h2>
<p>Supported probe-specific variables:</p>
<dl COMPACT>
<dt>binary</p>
<dd>The location of your quakestat binary. </p>
<p> Example value: /usr/bin/quakestatba </p>
<p> This setting is mandatory.</p>
<dt>forks</p>
<dd>Run this many concurrent processes at maximum </p>
<p> Example value: 5 </p>
<p> Default value: 5</p>
<dt>game</p>
<dd>What game type to check, from the -default flag of quakestat </p>
<p> Example value: nexuizs </p>
<p> Default value: q3s</p>
<dt>mininterval</p>
<dd>The minimum amount of time between sending a ping packet to the target. </p>
<p> Example value: 0.1 </p>
<p> Default value: 0.5</p>
<dt>offset</p>
<dd>If you run many probes concurrently you may want to prevent them from hitting your network all at the same time. Using the probe-specific offset parameter you can change the point in time when each probe will be run. Offset is specified in % of total interval, or alternatively as &#8216;random&#8217;, and the offset from the &#8216;General&#8217; section is used if nothing is specified here. Note that this does <font SIZE="-1">NOT</font> influence the rrds itself, it is just a matter of when data acqusition is initiated. (This variable is only applicable if the variable &#8216;concurrentprobes&#8217; is set in the &#8216;General&#8217; section.) </p>
<p> Example value: 50%</p>
<dt>port</p>
<dd>The game server port to check. It can also be overriden by adding :port to the host parameter in the Target config. </p>
<p> Example value: 27970</p>
<dt>sourceaddress</p>
<dd>The quakestat &#8220;-srcip&#8221; parameter . From <i><a href="/docs/linux/man/1-quakestat/">quakestat</a></i>(1): </p>
<p> Send packets using this <font SIZE="-1">IP</font> address </p>
<p> Example value: 192.168.0.1</p>
<dt>sourceport</p>
<dd>The quakestat &#8220;-srcport&#8221; parameter . From <i><a href="/docs/linux/man/1-quakestat/">quakestat</a></i>(1): </p>
<p> Send packets from these network ports </p>
<p> Example value: 9923-9943</p>
<dt>step</p>
<dd>Duration of the base interval that this probe should use, if different from the one specified in the &#8216;Database&#8217; section. Note that the step in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change the step parameter afterwards, you&#8217;ll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. (This variable is only applicable if the variable &#8216;concurrentprobes&#8217; is set in the &#8216;General&#8217; section.) </p>
<p> Example value: 300</p>
<dt>timeout</p>
<dd>How long a single &#8216;ping&#8217; takes at maximum </p>
<p> Example value: 15 </p>
<p> Default value: 5</dl>
<p> Supported target-specific variables:</p>
<dl COMPACT>
<dt>pings</p>
<dd>How many pings should be sent to each target, if different from the global value specified in the Database section. Note that the number of pings in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change this parameter afterwards, you&#8217;ll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. </p>
<p> Example value: 5</dl>
<h2>Authors</h2>
<p>Walter Huf &lt;hufman [at] gmail.com&gt;</p>
