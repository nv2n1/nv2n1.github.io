---
title: "smokeping_probes_sipsak(3)"
name: "smokeping_probes_sipsak"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_probes_sipsak/"
---

Smokeping::probes::SipSak - tests sip server 

<h2>Overview</h2>This probe sends <font SIZE="-1">OPTIONS</font> messages to a sip server testing the latency.
<h2>Synopsis</h2><pre> *** Probes ***
 +SipSak
 binary = /usr/bin/sipsak
 forks = 5
 offset = 50%
 step = 300
 timeout = 15
 # The following variables can be overridden in each target section
 keep_second = yes
 params = --numeric --password=mysecret
 pings = 5
 port = 5061
 user = nobody
 # [...]
 *** Targets ***
 probe = SipSak # if this should be the default probe
 # [...]
 + mytarget
 # probe = SipSak # if the default probe is something else
 host = my.host
 keep_second = yes
 params = --numeric --password=mysecret
 pings = 5
 port = 5061
 user = nobody</pre><h2>Description</h2>The probe uses the sipsak &lt;<a rel="nofollow" HREF="http://sipsak.org/">http://sipsak.org/</a>&gt; tool to measure sip server latency by sending an <font SIZE="-1">OPTIONS</font> message. 

 The sipsak command supports a large number of additional parameters to fine-tune its operation. Use the params variable to configure them.
<h2>Variables</h2>Supported probe-specific variables:
<dl COMPACT><dt>binary
<dd>The location of your echoping binary. 

 Default value: /usr/bin/sipsak
<dt>forks
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
<dl COMPACT><dt>keep_second
<dd>If <font SIZE="-1">OPTIONS</font> is actually implemented by the server, SipSak will receive two responses. If this option is set, the timeing from the second, final response will be counter 

 Example value: yes
<dt>params
<dd>additional sipsak options. The options will get split on space. 

 Example value: --numeric --password=mysecret
<dt>pings
<dd>How many pings should be sent to each target, if different from the global value specified in the Database section. Note that the number of pings in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change this parameter afterwards, you'll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. 

 Example value: 5
<dt>port
<dd>usa non-default port for the sip connection. 

 Example value: 5061
<dt>user
<dd>User to use for sip connection. 

 Example value: nobody</dl><h2>Authors</h2>Tobias Oetiker &lt;tobi [at] oetiker.ch&gt; sponsored by <font SIZE="-1">ANI</font> Networks
