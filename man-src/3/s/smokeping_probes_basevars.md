---
title: "smokeping_probes_basevars(3)"
name: "smokeping_probes_basevars"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_probes_basevars/"
---

Smokeping::probes::basevars - Another Base Class for implementing SmokePing Probes 

<h2>Overview</h2>Like Smokeping::probes::base, but supports host-specific variables for the probe.
<h2>Synopsis</h2><pre> *** Probes ***
 +basevars
 offset = 50%
 pings = 20
 step = 300
 # [...]
 *** Targets ***
 probe = basevars # if this should be the default probe
 # [...]
 + mytarget
 # probe = basevars # if the default probe is something else
 host = my.host</pre><h2>Description</h2>Provides the method `targets' that returns a list of hashes. The hashes contain the entries:
<dl COMPACT><dt>addr
<dd>The address of the target.
<dt>vars
<dd>A hash containing variables defined in the corresponding config section.
<dt>tree
<dd>The unique index that `probe::base' uses for targets. 

 There's also the method 'vars' that returns the abovementioned hash corresponding to the 'tree' index parameter.</dl><h2>Variables</h2>Supported probe-specific variables:
<dl COMPACT><dt>offset
<dd>If you run many probes concurrently you may want to prevent them from hitting your network all at the same time. Using the probe-specific offset parameter you can change the point in time when each probe will be run. Offset is specified in % of total interval, or alternatively as 'random', and the offset from the 'General' section is used if nothing is specified here. Note that this does <font SIZE="-1">NOT</font> influence the rrds itself, it is just a matter of when data acqusition is initiated. (This variable is only applicable if the variable 'concurrentprobes' is set in the 'General' section.) 

 Example value: 50%
<dt>pings
<dd>How many pings should be sent to each target, if different from the global value specified in the Database section. Note that the number of pings in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change this parameter afterwards, you'll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. 

 Example value: 20
<dt>step
<dd>Duration of the base interval that this probe should use, if different from the one specified in the 'Database' section. Note that the step in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change the step parameter afterwards, you'll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. (This variable is only applicable if the variable 'concurrentprobes' is set in the 'General' section.) 

 Example value: 300</dl><h2>Authors</h2>Niko Tyni &lt;ntyni [at] iki.fi&gt;
<h2>Bugs</h2>Uses `Smokeping::probes::base' internals too much to be a derived class, but I didn't want to touch the base class directly.
<h2>See Also</h2>Smokeping::probes::base, Smokeping::probes::EchoPing
