---
title: "smokeping_probes_ssh(3)"
name: "smokeping_probes_ssh"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_probes_ssh/"
description: "Smokeping::probes::SSH – Secure Shell Probe for SmokePing"
---

<p>Smokeping::probes::SSH &#8211; Secure Shell Probe for SmokePing </p>
<h2>Synopsis</h2>
<pre> *** Probes ***
 +SSH
 binary = /usr/bin/ssh-keyscan # mandatory
 forks = 5
 offset = 50%
 step = 300
 timeout = 15
 # The following variables can be overridden in each target section
 keytype = dsa
 pings = 5
 port = 5000
 # [...]
 *** Targets ***
 probe = SSH # if this should be the default probe
 # [...]
 + mytarget
 # probe = SSH # if the default probe is something else
 host = my.host
 keytype = dsa
 pings = 5
 port = 5000</pre>
<h2>Description</h2>
<p>Integrates ssh-keyscan as a probe into smokeping. The variable <code>binary</code> must point to your copy of the ssh-keyscan program. If it is not installed on your system yet, you should install openssh &gt;= 3.8p1 </p>
<p> The Probe asks the given host n-times for it&#8217;s public key, where n is the amount specified in the config File. </p>
<p> As part of the initialization, the probe asks 127.0.0.1 for it&#8217;s public key and tries to parse the output. Make sure you have <font SIZE="-1">SSH</font> running on the localhost as well.</p>
<h2>Variables</h2>
<p>Supported probe-specific variables:</p>
<dl COMPACT>
<dt>binary</p>
<dd>The location of your ssh-keyscan binary. </p>
<p> Example value: /usr/bin/ssh-keyscan </p>
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
<dt>keytype</p>
<dd>Type of key, used in ssh-keyscan -t <i>keytype</i> </p>
<p> Example value: dsa </p>
<p> Default value: rsa</p>
<dt>pings</p>
<dd>How many pings should be sent to each target, if different from the global value specified in the Database section. Note that the number of pings in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change this parameter afterwards, you&#8217;ll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. </p>
<p> Example value: 5</p>
<dt>port</p>
<dd>Port to use when testing the ssh connection -p <i>port</i> </p>
<p> Example value: 5000 </p>
<p> Default value: 22</dl>
<h2>Authors</h2>
<p>Christian Recktenwald &lt;smokeping-contact [at] citecs.de&gt;</p>
