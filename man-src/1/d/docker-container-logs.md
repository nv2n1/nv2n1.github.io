---
title: "docker-container-logs(1)"
name: "docker-container-logs"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-container-logs/"
description: "docker-container-logs – Fetch the logs of a container"
---

<h2 class="name">NAME</h2>
<p> docker-container-logs &#8211; Fetch the logs of a container </p>
<h2>SYNOPSIS</h2>
<p> <code>docker container logs [OPTIONS] CONTAINER</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>docker container logs</code> command batch-retrieves whatever logs are present for a container at the time of execution. This does not guarantee execution order when combined with a docker run (i.e., your run may not have generated any logs at the time you execute docker container logs). </p>
<p> The <code>docker container logs &#8211;follow</code> command combines commands <code>docker container logs</code> and <code>docker attach</code>. It will first return all logs from the beginning and then continue streaming new output from the container&#8217;s stdout and stderr. </p>
<p> <code>Warning</code>: This command works only for the <code>json-file</code> or <code>journald</code> logging drivers. </p>
<p> The &#8211;since and &#8211;until options can be Unix timestamps, date formatted timestamps, or Go duration strings (e.g. 10m, 1h30m) computed relative to the client machine&#8217;s time. Supported formats for date formatted time stamps include RFC3339Nano, RFC3339, 2006-01-02T15:04:05, 2006-01-02T15:04:05.999999999, 2006-01-02Z07:00, and 2006-01-02. The local timezone on the client will be used if you do not provide either a Z or a +-00:00 timezone offset at the end of the timestamp. When providing Unix timestamps enter seconds[.nanoseconds], where seconds is the number of seconds that have elapsed since January 1, 1970 (midnight UTC/GMT), not counting leap seconds (aka Unix epoch or Unix time), and the optional .nanoseconds field is a fraction of a second no more than nine digits long. You can combine the &#8211;since or &#8211;until options with either or both of the &#8211;follow or &#8211;tail options. </p>
<p> The docker container logs &#8211;details command will add on extra attributes, such as environment variables and labels, provided to &#8211;log-opt when creating the container. </p>
<p> In order to retrieve logs before a specific point in time, run: </p>
<dl>
<dt>
<dd>
<pre><code>
$ docker run-- name test - d busybox sh - c "while true; do $(echo date); sleep 1; done" $ date Tue 14 Nov 2017 16 : 40 : 00 CET $ docker logs - f-- until = 2s test
    Tue 14 Nov 2017 16 : 40 : 00 CET
        Tue 14 Nov 2017 16 : 40 : 01 CET
            Tue 14 Nov 2017 16 : 40 : 02 CET
</code></pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>&#8211;details</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Show extra details provided to logs</p>
<p> <code>-f</code>, <code>&#8211;follow</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Follow log output</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for logs</p>
<p> <code>&#8211;since</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Show logs since timestamp (e.g. 2013-01-02T13:23:37Z) or relative (e.g. 42m for 42 minutes)</p>
<p> <code>-n</code>, <code>&#8211;tail</code>=&quot;all&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Number of lines to show from the end of the logs</p>
<p> <code>-t</code>, <code>&#8211;timestamps</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Show timestamps</p>
<p> <code>&#8211;until</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Show logs before a timestamp (e.g. 2013-01-02T13:23:37Z) or relative (e.g. 42m for 42 minutes)</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-container/">docker-container</a>(1)</code> </p>
<h2>Index</h2>
