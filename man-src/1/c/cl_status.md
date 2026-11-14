---
title: "cl_status(1)"
name: "cl_status"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cl_status/"
description: "cl_status – Check Status of the High-Availability Linux (Linux-HA) Subsystem"
---

<h2>NAME</h2>
<p> cl_status &#8211; Check Status of the High-Availability Linux (Linux-HA) Subsystem</p>
<h2>SYNOPSIS</h2>
<p> <code>cl_status</code> &lt;sub-command&gt;<i>[&lt;options&gt;] [&lt;parameters&gt;]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>cl_status</code> is used to check the status of the High-Availability Linux Subsystem </p>
<h2>SUB-COMMANDS</h2>
<dl>
<dt><code>hbstatus</code></p>
<dd> Indicate if heartbeat is running on the local system.</p>
<dt><code>listnodes</code></p>
<dd> List the nodes in the cluster</p>
<dt><code>nodetype</code> <i>TYPE</i></p>
<dd> List the nodes of the given type. Currently the available types are ping and normal.</p>
<dt><code>listhblinks</code> <i>NODENAME</i></p>
<dd> List the network interfaces used as heartbeat links. Nodename should be as per the ha.cf file for the cluster.</p>
<dt><code>hblinkstatus</code> <i>NODENAME LINKNAME</i></p>
<dd> Show the status of a heartbeat link. Nodename should be as per the ha.cf file for the cluster. Linkname should be as per the output of the listhblinks subcomand.</p>
<dt><code>clientstatus</code> <i>NODENAME CLIENTID [TIMEOUT]</i></p>
<dd> Show the status of heartbeat clients. Nodename and Client-ID should be as per the ha.cf file for the cluster. Timeout is in milliseconds, the default is 100ms.</p>
<dt><code>rscstatus</code></p>
<dd> Show the status of cluster resources. Status will be one of: local, foreign, all or none.</p>
<dt><code>hbparameter -p</code> <i>PARAMETERNAME</i></p>
<dd> Retrieve the value of cluster parameters. The parameters may be one of the following, however some parameters which have not been specified may not retrieved:</p>
<dl>
<dt>
<dd> apiauth, auto_failback, baud, debug, debugfile, deadping, deadtime, hbversion, hopfudge, initdead, keepalive, logfacility, logfile, msgfmt, nice_failback, node, normalpoll, stonith, udpport, warntime, watchdog</dl>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-m</code></p>
<dd> Make the output more human readable. The default output should be easier for scripts to parse. Available with all commands.</p>
<dt><code>-p</code></p>
<dd> List only &#8216;ping&#8217; nodes. Available with hbstatus sub-command.</p>
<dt><code>-n</code></p>
<dd> List only &#8216;normal&#8217; nodes. Available with hbstatus sub-command. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-heartbeat/">heartbeat</a>(8) </p>
<h2>DOCUMENTATION</h2>
<p> More information may be found at <a rel="nofollow" href="http://www.linux-ha.org/">http://www.linux-ha.org/</a> </p>
<h2>AUTHORS</h2>
<p> cl_status &#8211; Sun Jiang Dong &lt;sunjd [at] cn.ibm.com&gt;<br />
 linux-ha &#8211; Alan Robertson &lt;alanr [at] unix.sh&gt; <i>et al</i>.<br />
 man page &#8211; Horms &lt;horms [at] verge.net.au&gt; </p>
<h2>Index</h2>
