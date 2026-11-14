---
title: "smokeping_probes_skel(3)"
name: "smokeping_probes_skel"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_probes_skel/"
---

Smokeping::probes::skel - a skeleton for Smokeping Probes 

<h2>Synopsis</h2><pre> *** Probes ***
 +skel
 forks = 5
 offset = 50%
 step = 300
 timeout = 15
 # The following variables can be overridden in each target section
 pings = 5
 # [...]
 *** Targets ***
 probe = skel # if this should be the default probe
 # [...]
 + mytarget
 # probe = skel # if the default probe is something else
 host = my.host
 pings = 5</pre><h2>Description</h2>This is a non-functional module that is intended to act as a basis for creation of new probes. See the smokeping_extend document for more information.
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

 Example value: 300
<dt>timeout
<dd>How long a single 'ping' takes at maximum 

 Example value: 15 

 Default value: 5</dl>
 

 Supported target-specific variables:
<dl COMPACT><dt>pings
<dd>How many pings should be sent to each target, if different from the global value specified in the Database section. Note that the number of pings in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change this parameter afterwards, you'll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. 

 Example value: 5</dl><h2>Authors</h2><pre> Niko Tyni &lt;ntyni [at] iki.fi&gt;,</pre><h2>See Also</h2>smokeping_extend
