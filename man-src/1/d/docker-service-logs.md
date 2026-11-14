---
title: "docker-service-logs(1)"
name: "docker-service-logs"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-service-logs/"
description: "docker-service-logs – Fetch the logs of a service or task"
---

<h2 class="name">NAME</h2>
<p> docker-service-logs &#8211; Fetch the logs of a service or task </p>
<h2>SYNOPSIS</h2>
<p> <code>docker service logs [OPTIONS] SERVICE|TASK</code> </p>
<h2>DESCRIPTION</h2>
<p> Fetch the logs of a service or task </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;details</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Show extra details provided to logs</p>
<p> <code>-f</code>, <code>&#8211;follow</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Follow log output</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for logs</p>
<p> <code>&#8211;no-resolve</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Do not map IDs to Names in output</p>
<p> <code>&#8211;no-task-ids</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Do not include task IDs in output</p>
<p> <code>&#8211;no-trunc</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Do not truncate output</p>
<p> <code>&#8211;raw</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Do not neatly format logs</p>
<p> <code>&#8211;since</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Show logs since timestamp (e.g. 2013-01-02T13:23:37Z) or relative (e.g. 42m for 42 minutes)</p>
<p> <code>-n</code>, <code>&#8211;tail</code>=&quot;all&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Number of lines to show from the end of the logs</p>
<p> <code>-t</code>, <code>&#8211;timestamps</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Show timestamps</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-service/">docker-service</a>(1)</code> </p>
<h2>Index</h2>
