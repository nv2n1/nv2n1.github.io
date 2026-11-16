---
title: "smokeping_probes_echopinghttp(3)"
name: "smokeping_probes_echopinghttp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_probes_echopinghttp/"
---

Smokeping::probes::EchoPingHttp - an 

<a HREF="/docs/linux/man/1-echoping/">echoping</a>(1) probe for SmokePing
<h2>Overview</h2>Measures <font SIZE="-1">HTTP</font> roundtrip times (web servers and caches) for SmokePing.
<h2>Synopsis</h2><pre> *** Probes ***
 +EchoPingHttp
 binary = /usr/bin/echoping
 forks = 5
 offset = 50%
 step = 300
 # The following variables can be overridden in each target section
 accept_redirects = yes
 extraopts = -some-letter-the-author-did-not-think-of
 ignore_cache = yes
 ipversion = 4
 pings = 5
 port = 80
 priority = 6
 revalidate_data = no
 timeout = 20
 tos = 0xa0
 url = /
 waittime = 1
 # [...]
 *** Targets ***
 probe = EchoPingHttp # if this should be the default probe
 # [...]
 + mytarget
 # probe = EchoPingHttp # if the default probe is something else
 host = my.host
 accept_redirects = yes
 extraopts = -some-letter-the-author-did-not-think-of
 ignore_cache = yes
 ipversion = 4
 pings = 5
 port = 80
 priority = 6
 revalidate_data = no
 timeout = 20
 tos = 0xa0
 url = /
 waittime = 1</pre><h2>Variables</h2>Supported probe-specific variables:
<dl COMPACT><dt>binary
</dt><dd>The location of your echoping binary. 
 Default value: /usr/bin/echoping
</dd><dt>forks
</dt><dd>Run this many concurrent processes at maximum 
 Example value: 5 
 Default value: 5
</dd><dt>offset
</dt><dd>If you run many probes concurrently you may want to prevent them from hitting your network all at the same time. Using the probe-specific offset parameter you can change the point in time when each probe will be run. Offset is specified in % of total interval, or alternatively as 'random', and the offset from the 'General' section is used if nothing is specified here. Note that this does <font SIZE="-1">NOT</font> influence the rrds itself, it is just a matter of when data acqusition is initiated. (This variable is only applicable if the variable 'concurrentprobes' is set in the 'General' section.) 
 Example value: 50%
</dd><dt>step
</dt><dd>Duration of the base interval that this probe should use, if different from the one specified in the 'Database' section. Note that the step in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change the step parameter afterwards, you'll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. (This variable is only applicable if the variable 'concurrentprobes' is set in the 'General' section.) 
 Example value: 300</dd></dl>
 

 Supported target-specific variables:
<dl COMPACT><dt>accept_redirects
</dt><dd>The <i><a HREF="/docs/linux/man/1-echoping/">echoping</a></i>(1) ``-R'' option: Accept <font SIZE="-1">HTTP </font> status codes 3xx (redirections) as normal responses instead of treating them as errors. Note that this option is only available starting with Echoping 6. 
 Enabled if the value is anything other than 'no' or '0'. 
 Example value: yes
</dd><dt>extraopts
</dt><dd>Any extra options specified here will be passed unmodified to <i><a HREF="/docs/linux/man/1-echoping/">echoping</a></i>(1). 
 Example value: -some-letter-the-author-did-not-think-of
</dd><dt>ignore_cache
</dt><dd>The <i><a HREF="/docs/linux/man/1-echoping/">echoping</a></i>(1) ``-A'' option: force the proxy to ignore the cache. Enabled if the value is anything other than 'no' or '0'. 
 Example value: yes
</dd><dt>ipversion
</dt><dd>The <font SIZE="-1">IP</font> protocol used. Possible values are ``4'' and ``6''. Passed to <i><a HREF="/docs/linux/man/1-echoping/">echoping</a></i>(1) as the ``-4'' or ``-6'' options. 
 Example value: 4
</dd><dt>pings
</dt><dd>How many pings should be sent to each target, if different from the global value specified in the Database section. Note that the number of pings in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change this parameter afterwards, you'll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. 
 Example value: 5
</dd><dt>port
</dt><dd>The <font SIZE="-1">TCP</font> port to use. 
 Example value: 80
</dd><dt>priority
</dt><dd>The ``-p'' <i><a HREF="/docs/linux/man/1-echoping/">echoping</a></i>(1) option. 
 Example value: 6
</dd><dt>revalidate_data
</dt><dd>The <i><a HREF="/docs/linux/man/1-echoping/">echoping</a></i>(1) ``-a'' option: force the proxy to revalidate data with original server. Enabled if the value is anything other than 'no' or '0'. 
 Example value: no
</dd><dt>timeout
</dt><dd>The ``-t'' <i><a HREF="/docs/linux/man/1-echoping/">echoping</a></i>(1) option. 
 Example value: 20 
 Default value: 10
</dd><dt>tos
</dt><dd>The ``-P'' <i><a HREF="/docs/linux/man/1-echoping/">echoping</a></i>(1) option. 
 Example value: 0xa0
</dd><dt>url
</dt><dd>The <font SIZE="-1">URL</font> to be requested from the web server or cache. Can be either relative (/...) for web servers or absolute (<a rel="nofollow" HREF="http://...)">http://...)</a> for caches. 
 Default value: /
</dd><dt>waittime
</dt><dd>The ``-w'' <i><a HREF="/docs/linux/man/1-echoping/">echoping</a></i>(1) option. 
 Example value: 1</dd></dl><h2>Authors</h2>Niko Tyni &lt;ntyni [at] iki.fi&gt;
<h2>Notes</h2>You should consider setting a lower value for the <tt>&quot;pings&quot;</tt> variable than the default 20, as repetitive <font SIZE="-1">URL</font> fetching may be quite heavy on the server. 

 The <i>fill</i>, <i>size</i> and <i>udp</i> EchoPing variables are not valid for EchoPingHttp.
<h2>See Also</h2>Smokeping::probes::EchoPing, Smokeping::probes::EchoPingHttps
