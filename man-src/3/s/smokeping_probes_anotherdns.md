---
title: "smokeping_probes_anotherdns(3)"
name: "smokeping_probes_anotherdns"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_probes_anotherdns/"
---

Smokeping::probes::AnotherDNS - Alternate DNS Probe 

<h2>Synopsis</h2><pre> *** Probes ***
 +AnotherDNS
 forks = 5
 offset = 50%
 step = 300
 # The following variables can be overridden in each target section
 ipversion = 4
 lookup = <a rel="nofollow" HREF="http://www.example.org">www.example.org</a>
 mininterval = 0.5
 pings = 5
 port = 53
 protocol = udp
 recordtype = A
 require_answers = 0
 require_noerror = 0
 timeout = 5
 # [...]
 *** Targets ***
 probe = AnotherDNS # if this should be the default probe
 # [...]
 + mytarget
 # probe = AnotherDNS # if the default probe is something else
 host = my.host
 ipversion = 4
 lookup = <a rel="nofollow" HREF="http://www.example.org">www.example.org</a>
 mininterval = 0.5
 pings = 5
 port = 53
 protocol = udp
 recordtype = A
 require_answers = 0
 require_noerror = 0
 timeout = 5</pre><h2>Description</h2>Like <font SIZE="-1">DNS,</font> but uses Net::DNS and Time::HiRes instead of dig. This probe does *not* retry the request three times before it is considerd ``lost'', like dig and other resolver do by default. If operating as caching Nameserver, <font SIZE="-1">BIND </font>(and maybe others) expect clients to retry the request if the answer is not in the cache. So, ask the nameserver for something that he is authoritative for if you want measure the network packet loss correctly. 

 If you have a really fast network and nameserver, you will notice that this probe reports the query time in microsecond resolution. :-)
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
<dl COMPACT><dt>ipversion
<dd>The <font SIZE="-1">IP</font> protocol used. Possible values are ``4'' and ``6''. Passed to <i><a HREF="/docs/linux/man/1-echoping/">echoping</a></i>(1) as the ``-4'' or ``-6'' options. 

 Example value: 4
<dt>lookup
<dd>Name of the host to look up in the dns. 

 Example value: <a rel="nofollow" HREF="http://www.example.org">www.example.org</a>
<dt>mininterval
<dd>Minimum time between sending two lookup queries in (possibly fractional) seconds. 

 Default value: 0.5
<dt>pings
<dd>How many pings should be sent to each target, if different from the global value specified in the Database section. Note that the number of pings in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change this parameter afterwards, you'll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. 

 Example value: 5
<dt>port
<dd>The <font SIZE="-1">UDP</font> Port to use. 

 Default value: 53
<dt>protocol
<dd>The Network Protocol to use. 

 Default value: udp
<dt>recordtype
<dd>Record type to look up. 

 Default value: A
<dt>require_answers
<dd>Only Count Answers with answer count &gt;= this value. 

 Default value: 0
<dt>require_noerror
<dd>Only Count Answers with Response Status <font SIZE="-1">NOERROR.</font> 

 Default value: 0
<dt>timeout
<dd>Timeout for a single request in seconds. 

 Default value: 5</dl><h2>Authors</h2>Christoph Heine &lt;Christoph.Heine [at] HaDiKo.DE&gt;
