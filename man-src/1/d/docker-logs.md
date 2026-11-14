---
title: "docker-logs(1)"
name: "docker-logs"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-logs/"
description: "docker-logs – Fetch the logs of a container"
---

<h2 class="name">NAME</h2>
<p> docker-logs &#8211; Fetch the logs of a container </p>
<h2>SYNOPSIS</h2>
<p> <code>docker logs [OPTIONS] CONTAINER</code> </p>
<h2>DESCRIPTION</h2>
<p> Alias for docker container logs. </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;details</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Show extra details provided to logs</p>
<p> <code>-f</code>, <code>&#8211;follow</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Follow log output</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for logs</p>
<p> <code>&#8211;since</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Show logs since timestamp (e.g. 2013-01-02T13:23:37Z) or relative (e.g. 42m for 42 minutes)</p>
<p> <code>-n</code>, <code>&#8211;tail</code>=&quot;all&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Number of lines to show from the end of the logs</p>
<p> <code>-t</code>, <code>&#8211;timestamps</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Show timestamps</p>
<p> <code>&#8211;until</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Show logs before a timestamp (e.g. 2013-01-02T13:23:37Z) or relative (e.g. 42m for 42 minutes)</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker/">docker</a>(1)</code> </p>
<h2>Index</h2>
