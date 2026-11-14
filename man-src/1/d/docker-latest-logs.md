---
title: "docker-latest-logs(1)"
name: "docker-latest-logs"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest-logs/"
description: "docker-logs – Fetch the logs of a container"
---

<h2 class="name">NAME</h2>
<p> docker-logs &#8211; Fetch the logs of a container </p>
<h2>SYNOPSIS</h2>
<p> <code>docker logs</code> [<code>-f</code>|<code>&#8211;follow</code>] [<code>&#8211;help</code>] [<code>&#8211;since</code>[=<i>SINCE</i>]] [<code>-t</code>|<code>&#8211;timestamps</code>] [<code>&#8211;tail</code>[=<i>&quot;all&quot;</i>]] CONTAINER </p>
<h2>DESCRIPTION</h2>
<p> The <code>docker logs</code> command batch-retrieves whatever logs are present for a container at the time of execution. This does not guarantee execution order when combined with a docker run (i.e., your run may not have generated any logs at the time you execute docker logs). </p>
<p> The <code>docker logs &#8211;follow</code> command combines commands <code>docker logs</code> and <code>docker attach</code>. It will first return all logs from the beginning and then continue streaming new output from the container&#8217;s stdout and stderr. </p>
<p> <code>Warning</code>: This command works only for the <code>json-file</code> or <code>journald</code> logging drivers. </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> <code>&#8211;details</code>=<i>true</i>|<i>false</i><br />
Show extra details provided to logs </p>
<p> <code>-f</code>, <code>&#8211;follow</code>=<i>true</i>|<i>false</i><br />
Follow log output. The default is&nbsp;<wbr><i>false</i>. </p>
<p> <code>&#8211;since</code>=&quot;&quot;<br />
Show logs since timestamp </p>
<p> <code>-t</code>, <code>&#8211;timestamps</code>=<i>true</i>|<i>false</i><br />
Show timestamps. The default is&nbsp;<wbr><i>false</i>. </p>
<p> <code>&#8211;tail</code>=&quot;<i>all</i>&quot;<br />
Output the specified number of lines at the end of logs&nbsp;<wbr>(defaults to all logs) </p>
<p> The &#8211;since option can be Unix timestamps, date formatted timestamps, or Go duration strings (e.g. 10m, 1h30m) computed relative to the client machine&#8217;s time. Supported formats for date formatted time stamps include RFC3339Nano, RFC3339, 2006-01-02T15:04:05, 2006-01-02T15:04:05.999999999, 2006-01-02Z07:00, and 2006-01-02. The local timezone on the client will be used if you do not provide either a Z or a +-00:00 timezone offset at the end of the timestamp. When providing Unix timestamps enter seconds[.nanoseconds], where seconds is the number of seconds that have elapsed since January 1, 1970 (midnight UTC/GMT), not counting leap seconds (aka Unix epoch or Unix time), and the optional .nanoseconds field is a fraction of a second no more than nine digits long. You can combine the &#8211;since option with either or both of the &#8211;follow or &#8211;tail options. </p>
<p> The docker logs &#8211;details command will add on extra attributes, such as environment variables and labels, provided to &#8211;log-opt when creating the container. </p>
<h2>HISTORY</h2>
<p> April 2014, Originally compiled by William Henry (whenry at redhat dot com) based on docker.com source material and internal work. June 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; July 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; April 2015, updated by Ahmet Alp Balkan &lt;ahmetalpbalkan [at] gmail.com&gt; October 2015, updated by Mike Brown &lt;mikebrow [at] gmail.com&gt; </p>
<h2>Index</h2>
