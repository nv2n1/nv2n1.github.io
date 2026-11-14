---
title: "smokeping_probes_passwordchecker(3)"
name: "smokeping_probes_passwordchecker"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_probes_passwordchecker/"
description: "Smokeping::probes::passwordchecker – A Base Class for implementing SmokePing Probes"
---

<p>Smokeping::probes::passwordchecker &#8211; A Base Class for implementing SmokePing Probes </p>
<h2>Overview</h2>
<p>Like Smokeping::probes::basefork, but supports a probe-specific configuration file for storing passwords and a method for accessing them.</p>
<h2>Synopsis</h2>
<pre> *** Probes ***
 +passwordchecker
 forks = 5
 offset = 50%
 passwordfile = /some/place/secret
 step = 300
 timeout = 15
 # The following variables can be overridden in each target section
 pings = 5
 # [...]
 *** Targets ***
 probe = passwordchecker # if this should be the default probe
 # [...]
 + mytarget
 # probe = passwordchecker # if the default probe is something else
 host = my.host
 pings = 5</pre>
<h2>Description</h2>
<h3>synopsis with more detail</h3>
<p>SmokePing main configuration file: </p>
<pre> *** Probes ***
 + MyPasswordChecker
 # location of the file containing usernames and passwords
 passwordfile = /usr/share/smokeping/etc/passwords</pre>
<p>The specified password file: </p>
<pre> # host:username:password
 host1:joe:hardlyasecret
 # comments and whitespace lines are allowed
 host2:sue:notasecreteither</pre>
<h3>Actual description</h3>
<p>In implementing authentication probes, it might not be desirable to store the necessary cleartext passwords in the SmokePing main configuration file, since the latter must be readable both by the SmokePing daemon performing the probes and the <font SIZE="-1">CGI</font> that displays the results. If the passwords are stored in a different file, this file can be made readable by only the user the daemon runs as. This way we can be sure that nobody can trick the <font SIZE="-1">CGI</font> into displaying the passwords on the Web. </p>
<p> This module reads the passwords in at startup from the file specified in the probe-specific variable `passwordfile&#8217;. The passwords can later be accessed and modified by the <code>password</code> method, that needs the corresponding host and username as arguments.</p>
<h3>Password file format</h3>
<p>The password file format is simply one line for each triplet of host, username and password, separated from each other by colons (:). </p>
<p> Comment lines, starting with the `#&#8217; sign, are ignored, as well as empty lines.</p>
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
<dt>passwordfile</p>
<dd>Location of the file containing usernames and passwords. </p>
<p> Example value: /some/place/secret</p>
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
<h2>Bugs</h2>
<p>The need for storing cleartext passwords can be considered a bug in itself.</p>
<h2>See Also</h2>
<p>Smokeping::probes::basefork, Smokeping::probes::Radius, Smokeping::probes::LDAP</p>
