---
title: "smokeping_probes_echoping(3)"
name: "smokeping_probes_echoping"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_probes_echoping/"
---

Smokeping::probes::EchoPing - an 

<a HREF="/docs/linux/man/1-echoping/">echoping</a>(1) probe for SmokePing
<h2>Overview</h2>Measures <font SIZE="-1">TCP</font> or <font SIZE="-1">UDP</font> echo (port 7) roundtrip times for SmokePing. Can also be used as a base class for other <i><a HREF="/docs/linux/man/1-echoping/">echoping</a></i>(1) probes.
<h2>Synopsis</h2><pre> *** Probes ***
 +EchoPing
 binary = /usr/bin/echoping
 forks = 5
 offset = 50%
 step = 300
 # The following variables can be overridden in each target section
 extraopts = -some-letter-the-author-did-not-think-of
 fill = A
 ipversion = 4
 pings = 5
 priority = 6
 size = 510
 timeout = 1
 tos = 0xa0
 udp = no
 waittime = 1
 # [...]
 *** Targets ***
 probe = EchoPing # if this should be the default probe
 # [...]
 + mytarget
 # probe = EchoPing # if the default probe is something else
 host = my.host
 extraopts = -some-letter-the-author-did-not-think-of
 fill = A
 ipversion = 4
 pings = 5
 priority = 6
 size = 510
 timeout = 1
 tos = 0xa0
 udp = no
 waittime = 1</pre><h2>Description</h2>See <i><a HREF="/docs/linux/man/1-echoping/">echoping</a></i>(1) for details of the options below.
<h2>Variables</h2>Supported probe-specific variables:
<dl COMPACT><dt>binary
<dd>The location of your echoping binary. 

 Default value: /usr/bin/echoping
<dt>forks
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
<dl COMPACT><dt>extraopts
<dd>Any extra options specified here will be passed unmodified to <i><a HREF="/docs/linux/man/1-echoping/">echoping</a></i>(1). 

 Example value: -some-letter-the-author-did-not-think-of
<dt>fill
<dd>The ``-f'' <i><a HREF="/docs/linux/man/1-echoping/">echoping</a></i>(1) option. 

 Example value: A
<dt>ipversion
<dd>The <font SIZE="-1">IP</font> protocol used. Possible values are ``4'' and ``6''. Passed to <i><a HREF="/docs/linux/man/1-echoping/">echoping</a></i>(1) as the ``-4'' or ``-6'' options. 

 Example value: 4
<dt>pings
<dd>How many pings should be sent to each target, if different from the global value specified in the Database section. Note that the number of pings in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change this parameter afterwards, you'll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. 

 Example value: 5
<dt>priority
<dd>The ``-p'' <i><a HREF="/docs/linux/man/1-echoping/">echoping</a></i>(1) option. 

 Example value: 6
<dt>size
<dd>The ``-s'' <i><a HREF="/docs/linux/man/1-echoping/">echoping</a></i>(1) option. 

 Example value: 510
<dt>timeout
<dd>The ``-t'' <i><a HREF="/docs/linux/man/1-echoping/">echoping</a></i>(1) option. 

 Example value: 1 

 Default value: 5
<dt>tos
<dd>The ``-P'' <i><a HREF="/docs/linux/man/1-echoping/">echoping</a></i>(1) option. 

 Example value: 0xa0
<dt>udp
<dd>The ``-u'' <i><a HREF="/docs/linux/man/1-echoping/">echoping</a></i>(1) option. Values other than '0' and 'no' enable <font SIZE="-1">UDP.</font> 

 Example value: no
<dt>waittime
<dd>The ``-w'' <i><a HREF="/docs/linux/man/1-echoping/">echoping</a></i>(1) option. 

 Example value: 1</dl><h2>Authors</h2>Niko Tyni &lt;ntyni [at] iki.fi&gt;
<h2>Bugs</h2>Should we test the availability of the service at startup? After that it's too late to complain. 

 The location of the echoping binary should probably be a global variable instead of a probe-specific one. As things are, every EchoPing -derived probe has to declare it if the default (/usr/bin/echoping) isn't correct.
<h2>See Also</h2><i><a HREF="/docs/linux/man/1-echoping/">echoping</a></i>(1), Smokeping::probes::EchoPingHttp etc., &lt;<a rel="nofollow" HREF="http://echoping.sourceforge.net/">http://echoping.sourceforge.net/</a>&gt;
