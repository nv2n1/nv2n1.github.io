---
title: "smokeping_probes_basefork(3)"
name: "smokeping_probes_basefork"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_probes_basefork/"
description: "Smokeping::probes::basefork – Yet Another Base Class for implementing SmokePing Probes"
---

<p>Smokeping::probes::basefork &#8211; Yet Another Base Class for implementing SmokePing Probes </p>
<h2>Overview</h2>
<p>Like Smokeping::probes::basevars, but supports the probe-specific property `forks&#8217; to determine how many processes should be run concurrently. The targets are pinged one at a time, and the number of pings sent can vary between targets.</p>
<h2>Synopsis</h2>
<pre> *** Probes ***
 +basefork
 forks = 5
 offset = 50%
 step = 300
 timeout = 15
 # The following variables can be overridden in each target section
 pings = 5
 # [...]
 *** Targets ***
 probe = basefork # if this should be the default probe
 # [...]
 + mytarget
 # probe = basefork # if the default probe is something else
 host = my.host
 pings = 5</pre>
<h2>Description</h2>
<p>Not all pinger programs support testing multiple hosts in a single go like <i><a href="/docs/linux/man/1-fping/">fping</a></i>(1). If the measurement takes long enough, there may be not enough time perform all the tests in the time available. For example, if the test takes 30 seconds, measuring ten hosts already fills up the SmokePing default five minute step. </p>
<p> Thus, it may be necessary to do some of the tests concurrently. This module defines the <code>ping</code> method that forks the requested number of concurrent processes and calls the <code>pingone</code> method that derived classes must provide. </p>
<p> The <code>pingone</code> method is called with one argument: a hash containing the target that is to be measured. The contents of the hash are described in <i><a href="//www.systutorials.com/docs/linux/man/3pm-Smokeping::probes::basevars/">Smokeping::probes::basevars</a></i>(3pm). </p>
<p> The number of concurrent processes is determined by the probe-specific variable `forks&#8217; and is 5 by default. If there are more targets than this value, another round of forks is done after the first processes are finished. This continues until all the targets have been tested. </p>
<p> The timeout in which each child has to finish is set to 5 seconds multiplied by the maximum number of &#8216;pings&#8217; of the targets. You can set the base timeout differently if you want to, using the timeout property of the probe in the master config file (this again will be multiplied by the maximum number of pings). The probe itself can also provide another default value if desired by modifying the _default value of the timeout variable. </p>
<p> If the child isn&#8217;t finished when the timeout occurs, it will be killed along with any processes it has started. </p>
<p> The number of pings sent can be specified in the target-specific variable &#8216;pings&#8217;.</p>
<h2>Variables</h2>
<p>Supported probe-specific variables:</p>
<dl COMPACT>
<dt>forks</p>
<dd>Run this many concurrent processes at maximum </p>
<p> Example value: 5 </p>
<p> Default value: 5</p>
<dt>offset</p>
<dd>If you run many probes concurrently you may want to prevent them from hitting your network all at the same time. Using the probe-specific offset parameter you can change the point in time when each probe will be run. Offset is specified in % of total interval, or alternatively as &#8216;random&#8217;, and the offset from the &#8216;General&#8217; section is used if nothing is specified here. Note that this does <font SIZE="-1">NOT</font> influence the rrds itself, it is just a matter of when data acqusition is initiated. (This variable is only applicable if the variable &#8216;concurrentprobes&#8217; is set in the &#8216;General&#8217; section.) </p>
<p> Example value: 50%</p>
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
<p>Niko Tyni &lt;ntyni [at] iki.fi&gt;</p>
<h2>See Also</h2>
<p>Smokeping::probes::basevars, Smokeping::probes::EchoPing</p>
