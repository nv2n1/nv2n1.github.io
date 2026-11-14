---
title: "smokeping_probes_ftptransfer(3)"
name: "smokeping_probes_ftptransfer"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_probes_ftptransfer/"
description: "Smokeping::probes::FTPtransfer – intrusive bandwidth probe"
---

<p>Smokeping::probes::FTPtransfer &#8211; intrusive bandwidth probe </p>
<h2>Overview</h2>
<p>This probe send and retrieve files to or from an ftp server. It will plot the bandwidth it could use.</p>
<h2>Synopsis</h2>
<pre> *** Probes ***
 +FTPtransfer
 destfile = path/to/destinationfile.xxx
 forks = 5
 min_interval = 1
 mode = get # mandatory
 offset = 50%
 passwordfile = /some/place/secret
 srcfile = src/path/mybig.pdf # mandatory
 step = 300
 timeout = 15 # mandatory
 # The following variables can be overridden in each target section
 localaddr = myhost-nat-if
 passive = yes
 password = test-password
 pings = 5
 port = 3255
 timeout = 10
 username = test-user
 # [...]
 *** Targets ***
 probe = FTPtransfer # if this should be the default probe
 # [...]
 + mytarget
 # probe = FTPtransfer # if the default probe is something else
 host = my.host
 localaddr = myhost-nat-if
 passive = yes
 password = test-password
 pings = 5
 port = 3255
 timeout = 10
 username = test-user</pre>
<h2>Description</h2>
<p>The probe uses the Net::FTP perl client to run performance tests using an <font SIZE="-1">FTP</font> server as a target. This probe is <code>intrusive</code> as it transfers real data. By using real data we get a fair shot at figuring out what a link is capable of when it comes to transfering actual files. </p>
<p> The password can be specified either (in order of precedence, with the latter overriding the former) in the probe-specific variable `password&#8217;, in an external file or in the target-specific variable `password&#8217;. The location of this external file is given in the probe-specific variable `passwordfile&#8217;. See <i><a href="//www.systutorials.com/docs/linux/man/3pm-Smokeping::probes::passwordchecker/">Smokeping::probes::passwordchecker</a></i>(3pm) for the format of this file (summary: colon-separated triplets of the form `&lt;host&gt;:&lt;username&gt;:&lt;password&gt;&#8217;) </p>
<p> The probe tries to be nice to the server and waits at least X seconds between starting filetransfers, where X is the value of the probe specific `min_interval&#8217; variable (1 by default). </p>
<p> Many variables can be specified either in the probe or in the target definition, the target-specific variable will override the prove-specific variable. </p>
<p> If your transfer takes a lot of time, you may want to make sure to set the <code>timeout</code> and <code>max_rtt</code> properly so that smokeping does not abort the transfers of limit the graph size.</p>
<h2>Variables</h2>
<p>Supported probe-specific variables:</p>
<dl COMPACT>
<dt>destfile</p>
<dd>Normally the destination filename is the same as the source filename (without the path). If you want keep files in different directories this may not work, and you have to specify destfile as well. </p>
<p> Example value: path/to/destinationfile.xxx</p>
<dt>forks</p>
<dd>Run this many concurrent processes at maximum </p>
<p> Example value: 5 </p>
<p> Default value: 5</p>
<dt>min_interval</p>
<dd>The minimum interval between each starting ftp sessions in seconds. </p>
<p> Default value: 1</p>
<dt>mode</p>
<dd>The ftp probe can be in either put or get mode. If it is in put mode then it will send a file to the ftp server. In get mode it will retrieve a file from the ftp server. </p>
<p> Example value: get </p>
<p> This setting is mandatory.</p>
<dt>offset</p>
<dd>If you run many probes concurrently you may want to prevent them from hitting your network all at the same time. Using the probe-specific offset parameter you can change the point in time when each probe will be run. Offset is specified in % of total interval, or alternatively as &#8216;random&#8217;, and the offset from the &#8216;General&#8217; section is used if nothing is specified here. Note that this does <font SIZE="-1">NOT</font> influence the rrds itself, it is just a matter of when data acqusition is initiated. (This variable is only applicable if the variable &#8216;concurrentprobes&#8217; is set in the &#8216;General&#8217; section.) </p>
<p> Example value: 50%</p>
<dt>passwordfile</p>
<dd>Location of the file containing usernames and passwords. </p>
<p> Example value: /some/place/secret</p>
<dt>srcfile</p>
<dd>The name of the source file. If the probe is in <code>put</code> mode, this file has to be on the local machine, if the probe is in <code>get</code> mode then this file should sit in the remote ftp account. </p>
<p> Example value: src/path/mybig.pdf </p>
<p> This setting is mandatory.</p>
<dt>step</p>
<dd>Duration of the base interval that this probe should use, if different from the one specified in the &#8216;Database&#8217; section. Note that the step in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change the step parameter afterwards, you&#8217;ll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. (This variable is only applicable if the variable &#8216;concurrentprobes&#8217; is set in the &#8216;General&#8217; section.) </p>
<p> Example value: 300</p>
<dt>timeout</p>
<dd>The timeout is the maximum amount of time you will allow the probe to transfer the file. If the probe does not succeed to transfer in the time specified, it will get killed and a &#8216;loss&#8217; will be loged. </p>
<p> Since FTPtransfer is an invasive probe you should make sure you do not load the link for more than a few seconds anyway. Smokeping curently has a hard limit of 180 seconds for any <font SIZE="-1">RTT.</font> </p>
<p> Example value: 15 </p>
<p> This setting is mandatory.</dl>
<p> Supported target-specific variables:</p>
<dl COMPACT>
<dt>localaddr</p>
<dd>The local address to be used when making connections </p>
<p> Example value: myhost-nat-if</p>
<dt>passive</p>
<dd>Use passive <font SIZE="-1">FTP</font> protocol </p>
<p> Example value: yes</p>
<dt>password</p>
<dd>The password for the user, if not present in the password file. </p>
<p> Example value: test-password</p>
<dt>pings</p>
<dd>How many pings should be sent to each target, if different from the global value specified in the Database section. Note that the number of pings in the <font SIZE="-1">RRD</font> files is fixed when they are originally generated, and if you change this parameter afterwards, you&#8217;ll have to delete the old <font SIZE="-1">RRD</font> files or somehow convert them. </p>
<p> Example value: 5</p>
<dt>port</p>
<dd>A non-standard <font SIZE="-1">FTP</font> port to be used </p>
<p> Example value: 3255</p>
<dt>timeout</p>
<dd>Timeout in seconds for the <font SIZE="-1">FTP</font> transfer to complete. </p>
<p> Example value: 10</p>
<dt>username</p>
<dd>The username to be tested. </p>
<p> Example value: test-user</dl>
<h2>Authors</h2>
<p>Tobias Oetiker &lt;tobi [at] oetiker.ch&gt; sponsored by Virtela</p>
<h2>Bugs</h2>
<p>This probe has the capability for saturating your links, so don&#8217;t use it unless you know what you are doing. </p>
<p> The FTPtransfer probe measures bandwidth, but we report the number of seconds it took to transfer the &#8216;reference&#8217; file. This is because curently the notion of <i>Round Trip Time</i> is at the core of the application. It would take some re-engineering to split this out in plugins and thus make it configurable &#8230;</p>
