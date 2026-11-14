---
title: "smokeping_probes_ldap(3)"
name: "smokeping_probes_ldap"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_probes_ldap/"
---

Smokeping::probes::LDAP - a LDAP probe for SmokePing 

<h2>Overview</h2>Measures <font SIZE="-1">LDAP</font> search latency for SmokePing
<h2>Synopsis</h2><pre> *** Probes ***
 +LDAP
 forks = 5
 offset = 50%
 passwordfile = /some/place/secret
 step = 300
 # The following variables can be overridden in each target section
 attrs = uid,someotherattr
 base = dc=foo,dc=bar
 binddn = uid=testuser,dc=foo,dc=bar
 filter = uid=testuser # mandatory
 mininterval = 1
 password = mypass
 pings = 5
 port = 389
 scope = one
 start_tls = 1
 timeout = 10
 version = 3
 # [...]
 *** Targets ***
 probe = LDAP # if this should be the default probe
 # [...]
 + mytarget
 # probe = LDAP # if the default probe is something else
 host = my.host
 attrs = uid,someotherattr
 base = dc=foo,dc=bar
 binddn = uid=testuser,dc=foo,dc=bar
 filter = uid=testuser # mandatory
 mininterval = 1
 password = mypass
 pings = 5
 port = 389
 scope = one
 start_tls = 1
 timeout = 10
 version = 3</pre><h2>Description</h2>This probe measures <font SIZE="-1">LDAP</font> query latency for SmokePing. The query is specified by the target-specific variable `filter' and, optionally, by the target-specific variable `base'. The attributes queried can be specified in the comma-separated list `attrs'. 

 The <font SIZE="-1">TCP</font> port of the <font SIZE="-1">LDAP</font> server and the <font SIZE="-1">LDAP</font> version to be used can be specified by the variables `port' and `version'. 

 The probe can issue the starttls command to convert the connection into encrypted mode, if so instructed by the `start_tls' variable. This requires the 'IO::Socket::SSL' perl module to be installed. 

 The probe can also optionally do an authenticated <font SIZE="-1">LDAP</font> bind, if the `binddn' variable is present. The password to be used can be specified by the target-specific variable `password' or in an external file. The location of this file is given in the probe-specific variable `passwordfile'. See <i><a HREF="//www.systutorials.com/docs/linux/man/3pm-Smokeping::probes::passwordchecker/">Smokeping::probes::passwordchecker</a></i>(3pm) for the format of this file (summary: colon-separated triplets of the form `&lt;host&gt;:&lt;bind-dn&gt;:&lt;password&gt;') 

 The probe tries to be nice to the server and does not send authentication requests more frequently than once every X seconds, where X is the value of the target-specific ``min_interval'' variable (1 by default).
<h2>Variables</h2>Supported probe-specific variables:
<dl COMPACT><dt>forks
<dd>Run this many concurrent processes at maximum 

 Example value: 5 

 Default value: 5
<dt>offset
<dd>If you run many probes concurrently you may want to prevent them from hitting your network all at the same time. Using the probe-specific offset parameter you can change the point in time when each probe will be run. Offset is specified in % of total interval, or alternatively as 'random', and the offset from the 'General' section is used if nothing is specified here. Note that this does <font SIZE="-1">NOT</font> influence the rrds itself, it is just a matter of when data acqusition is initiated. (This variable is only applicable if the variable 'concurrentprobes' is set in the 'General' section.) 

 Example value: 50%
<dt>passwordfile
<dd>Location of the file containing usernames and passwords. 

 Example value: /some/place/secret
<dt>step
<dd>Duration of the base interval that this probe should use, if different from the one specified in the 'Database' section. Note that the step in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change the step parameter afterwards, you'll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. (This variable is only applicable if the variable 'concurrentprobes' is set in the 'General' section.) 

 Example value: 300</dl>
 

 Supported target-specific variables:
<dl COMPACT><dt>attrs
<dd>The attributes queried. 

 Example value: uid,someotherattr
<dt>base
<dd>The base to be used in the <font SIZE="-1">LDAP</font> query 

 Example value: dc=foo,dc=bar
<dt>binddn
<dd>If present, authenticate the <font SIZE="-1">LDAP</font> bind with this <font SIZE="-1">DN.</font> 

 Example value: uid=testuser,dc=foo,dc=bar
<dt>filter
<dd>The actual search to be made 

 Example value: uid=testuser 

 This setting is mandatory.
<dt>mininterval
<dd>The minimum interval between each query sent, in (possibly fractional) second s. 

 Default value: 1
<dt>password
<dd>The password to be used, if not present in &lt;passwordfile&gt;. 

 Example value: mypass
<dt>pings
<dd>How many pings should be sent to each target, if different from the global value specified in the Database section. Note that the number of pings in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change this parameter afterwards, you'll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. 

 Example value: 5
<dt>port
<dd><font SIZE="-1">TCP</font> port of the <font SIZE="-1">LDAP</font> server 

 Example value: 389
<dt>scope
<dd>The scope of the query. Can be either 'base', 'one' or 'sub'. See the Net::LDAP documentation for details. 

 Example value: one 

 Default value: sub
<dt>start_tls
<dd>If true, encrypt the connection with the starttls command. Disabled by default. 

 Example value: 1
<dt>timeout
<dd><font SIZE="-1">LDAP</font> query timeout in seconds. 

 Example value: 10 

 Default value: 5
<dt>version
<dd>The <font SIZE="-1">LDAP</font> version to be used. 

 Example value: 3</dl><h2>Authors</h2>Niko Tyni &lt;ntyni [at] iki.fi&gt;
<h2>Bugs</h2>There should be a way of specifying <font SIZE="-1">TLS</font> options, such as the certificates involved etc. 

 The probe has an ugly way of working around the fact that the IO::Socket::SSL class complains if <i>start_tls()</i> is done more than once in the same program. But It Works For Me (tm).
