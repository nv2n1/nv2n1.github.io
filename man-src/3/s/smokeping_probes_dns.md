---
title: "smokeping_probes_dns(3)"
name: "smokeping_probes_dns"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_probes_dns/"
description: "Smokeping::probes::DNS – Name Service Probe for SmokePing"
---

<p>Smokeping::probes::DNS &#8211; Name Service Probe for SmokePing </p>
<h2>Synopsis</h2>
<pre> *** Probes ***
 +DNS
 binary = /usr/bin/dig # mandatory
 forks = 5
 offset = 50%
 step = 300
 timeout = 15
 # The following variables can be overridden in each target section
 lookup = <a rel="nofollow" href="http://www.example.org">www.example.org</a>
 pings = 5
 server = ns1.someisp.net
 # [...]
 *** Targets ***
 probe = DNS # if this should be the default probe
 # [...]
 + mytarget
 # probe = DNS # if the default probe is something else
 host = my.host
 lookup = <a rel="nofollow" href="http://www.example.org">www.example.org</a>
 pings = 5
 server = ns1.someisp.net</pre>
<h2>Description</h2>
<p>Integrates dig as a probe into smokeping. The variable <code>binary</code> must point to your copy of the dig program. If it is not installed on your system yet, you should install bind-utils &gt;= 9.0.0. </p>
<p> The Probe asks the given host n-times for it&#8217;s name. Where n is the amount specified in the config File.</p>
<h2>Variables</h2>
<p>Supported probe-specific variables:</p>
<dl COMPACT>
<dt>binary</p>
<dd>The location of your dig binary. </p>
<p> Example value: /usr/bin/dig </p>
<p> This setting is mandatory.</p>
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
<dt>lookup</p>
<dd>Name of the host to look up in the dns. </p>
<p> Example value: <a rel="nofollow" href="http://www.example.org">www.example.org</a></p>
<dt>pings</p>
<dd>How many pings should be sent to each target, if different from the global value specified in the Database section. Note that the number of pings in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change this parameter afterwards, you&#8217;ll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. </p>
<p> Example value: 5</p>
<dt>server</p>
<dd>Name of the dns server to use. </p>
<p> Example value: ns1.someisp.net</dl>
<h2>Authors</h2>
<pre> Igor Petrovski &lt;pigor [at] myrealbox.com&gt;,
 Carl Elkins &lt;carl [at] celkins.org.uk&gt;,
 Andre Stolze &lt;stolze [at] uni-muenster.de&gt;,
 Niko Tyni &lt;ntyni [at] iki.fi&gt;,
 Chris Poetzel&lt;cpoetzel [at] anl.gov&gt;</pre>
