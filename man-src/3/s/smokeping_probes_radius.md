---
title: "smokeping_probes_radius(3)"
name: "smokeping_probes_radius"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_probes_radius/"
---

Smokeping::probes::Radius - a RADIUS authentication probe for SmokePing 

<h2>Overview</h2>Measures <font SIZE="-1">RADIUS</font> authentication latency for SmokePing
<h2>Synopsis</h2><pre> *** Probes ***
 +Radius
 forks = 5
 offset = 50%
 passwordfile = /some/place/secret
 secretfile = /another/place/secret
 step = 300
 # The following variables can be overridden in each target section
 allowreject = true
 mininterval = 1
 nas_ip_address = 10.1.2.3
 password = test-password
 pings = 5
 port = 1645
 secret = test-secret
 timeout = 5
 username = test-user # mandatory
 # [...]
 *** Targets ***
 probe = Radius # if this should be the default probe
 # [...]
 + mytarget
 # probe = Radius # if the default probe is something else
 host = my.host
 allowreject = true
 mininterval = 1
 nas_ip_address = 10.1.2.3
 password = test-password
 pings = 5
 port = 1645
 secret = test-secret
 timeout = 5
 username = test-user # mandatory</pre><h2>Description</h2>This probe measures <font SIZE="-1">RADIUS </font>(<font SIZE="-1">RFC 2865</font>) authentication latency for SmokePing. 

 The username to be tested is specified in either the probe-specific or the target-specific variable `username', with the target-specific one overriding the probe-specific one. 

 The password can be specified either (in order of precedence, with the latter overriding the former) in the probe-specific variable `password', in an external file or in the target-specific variable `password'. The location of this file is given in the probe-specific variable `passwordfile'. See <i><a HREF="//www.systutorials.com/docs/linux/man/3pm-Smokeping::probes::passwordchecker/">Smokeping::probes::passwordchecker</a></i>(3pm) for the format of this file (summary: colon-separated triplets of the form `&lt;host&gt;:&lt;username&gt;:&lt;password&gt;') 

 The <font SIZE="-1">RADIUS</font> protocol requires a shared secret between the server and the client. This secret can be specified either (in order of precedence, with the latter overriding the former) in the probe-specific variable `secret', in an external file or in the target-specific variable `secret'. This external file is located by the probe-specific variable `secretfile', and it should contain whitespace-separated pairs of the form `&lt;host&gt; &lt;secret&gt;'. Comments and blank lines are <font SIZE="-1">OK.</font> 

 If the optional probe-specific variable `nas_ip_address' is specified, its value is inserted into the authentication requests as the `NAS-IP-Address' <font SIZE="-1">RADIUS</font> attribute. 

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
<dt>secretfile
<dd>A file containing the <font SIZE="-1">RADIUS</font> shared secrets for the targets. It should contain whitespace-separated pairs of the form `&lt;host&gt; &lt;secret&gt;'. Comments and blank lines are <font SIZE="-1">OK.</font> 

 Example value: /another/place/secret
<dt>step
<dd>Duration of the base interval that this probe should use, if different from the one specified in the 'Database' section. Note that the step in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change the step parameter afterwards, you'll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. (This variable is only applicable if the variable 'concurrentprobes' is set in the 'General' section.) 

 Example value: 300</dl>
 

 Supported target-specific variables:
<dl COMPACT><dt>allowreject
<dd>Treat ``reject'' responses as <font SIZE="-1">OK</font> 

 Example value: true
<dt>mininterval
<dd>The minimum interval between each authentication request sent, in (possibly fractional) seconds. 

 Default value: 1
<dt>nas_ip_address
<dd>The NAS-IP-Address <font SIZE="-1">RADIUS</font> attribute for the authentication requests. Not needed everywhere. 

 Example value: 10.1.2.3
<dt>password
<dd>The password for the user, if not present in the password file. 

 Example value: test-password
<dt>pings
<dd>How many pings should be sent to each target, if different from the global value specified in the Database section. Note that the number of pings in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change this parameter afterwards, you'll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. 

 Example value: 5
<dt>port
<dd>The <font SIZE="-1">RADIUS</font> port to be used 

 Example value: 1645
<dt>secret
<dd>The <font SIZE="-1">RADIUS</font> shared secret for the target, if not present in the secrets file. 

 Example value: test-secret
<dt>timeout
<dd>Timeout in seconds for the <font SIZE="-1">RADIUS</font> queries. 

 Default value: 5
<dt>username
<dd>The username to be tested. 

 Example value: test-user 

 This setting is mandatory.</dl><h2>Authors</h2>Niko Tyni &lt;ntyni [at] iki.fi&gt;
<h2>Bugs</h2>There should be a more general way of specifying <font SIZE="-1">RADIUS</font> attributes.
