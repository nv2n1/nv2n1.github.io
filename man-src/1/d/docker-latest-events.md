---
title: "docker-latest-events(1)"
name: "docker-latest-events"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest-events/"
description: "docker-events – Get real time events from the server"
---

<h2 class="name">NAME</h2>
<p> docker-events &#8211; Get real time events from the server </p>
<h2>SYNOPSIS</h2>
<p> <code>docker events</code> [<code>&#8211;help</code>] [<code>-f</code>|<code>&#8211;filter</code>[=<i>[]</i>]] [<code>&#8211;since</code>[=<i>SINCE</i>]] [<code>&#8211;until</code>[=<i>UNTIL</i>]] </p>
<h2>DESCRIPTION</h2>
<p> Get event information from the Docker daemon. Information can include historical information and real-time information. </p>
<p> Docker containers will report the following events: </p>
<dl>
<dt>
<dd>
<pre>
attach, commit, copy, create, destroy, detach, die, exec_create, exec_detach, exec_start, export, kill, oom, pause, rename, resize, restart, start, stop, top, unpause, update
</pre>
</dl>
<p> Docker images report the following events: </p>
<dl>
<dt>
<dd>
<pre>
delete, import, load, pull, push, save, tag, untag
</pre>
</dl>
<p> Docker volumes report the following events: </p>
<dl>
<dt>
<dd>
<pre>
create, mount, unmount, destroy
</pre>
</dl>
<p> Docker networks report the following events: </p>
<dl>
<dt>
<dd>
<pre>
create, connect, disconnect, destroy
</pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> <code>-f</code>, <code>&#8211;filter</code>=[]<br />
Provide filter values&nbsp;<wbr>(i.e.,&nbsp;<wbr>&#8216;event=stop&#8217;) </p>
<p> <code>&#8211;since</code>=&quot;&quot;<br />
Show all events created since timestamp </p>
<p> <code>&#8211;until</code>=&quot;&quot;<br />
Stream events until this timestamp </p>
<p> The &#8211;since and &#8211;until parameters can be Unix timestamps, date formatted timestamps, or Go duration strings (e.g. 10m, 1h30m) computed relative to the client machine&#8217;s time. If you do not provide the &#8211;since option, the command returns only new and/or live events. Supported formats for date formatted time stamps include RFC3339Nano, RFC3339, 2006-01-02T15:04:05, 2006-01-02T15:04:05.999999999, 2006-01-02Z07:00, and 2006-01-02. The local timezone on the client will be used if you do not provide either a Z or a +-00:00 timezone offset at the end of the timestamp. When providing Unix timestamps enter seconds[.nanoseconds], where seconds is the number of seconds that have elapsed since January 1, 1970 (midnight UTC/GMT), not counting leap seconds (aka Unix epoch or Unix time), and the optional .nanoseconds field is a fraction of a second no more than nine digits long. </p>
<h2>EXAMPLES</h2>
<h2>Listening for Docker events</h2>
<p> After running docker events a container 786d698004576 is started and stopped (The container name has been shortened in the output below): </p>
<dl>
<dt>
<dd>
<pre>
# docker events
2015-01-28T20:21:31.000000000-08:00 59211849bc10: (from whenry/testimage:latest) start
2015-01-28T20:21:31.000000000-08:00 59211849bc10: (from whenry/testimage:latest) die
2015-01-28T20:21:32.000000000-08:00 59211849bc10: (from whenry/testimage:latest) stop
</pre>
</dl>
<h2>Listening for events since a given date</h2>
<p> Again the output container IDs have been shortened for the purposes of this document: </p>
<dl>
<dt>
<dd>
<pre>
# docker events --since '2015-01-28'
2015-01-28T20:25:38.000000000-08:00 c21f6c22ba27: (from whenry/testimage:latest) create
2015-01-28T20:25:38.000000000-08:00 c21f6c22ba27: (from whenry/testimage:latest) start
2015-01-28T20:25:39.000000000-08:00 c21f6c22ba27: (from whenry/testimage:latest) create
2015-01-28T20:25:39.000000000-08:00 c21f6c22ba27: (from whenry/testimage:latest) start
2015-01-28T20:25:40.000000000-08:00 c21f6c22ba27: (from whenry/testimage:latest) die
2015-01-28T20:25:42.000000000-08:00 c21f6c22ba27: (from whenry/testimage:latest) stop
2015-01-28T20:25:45.000000000-08:00 c21f6c22ba27: (from whenry/testimage:latest) start
2015-01-28T20:25:45.000000000-08:00 c21f6c22ba27: (from whenry/testimage:latest) die
2015-01-28T20:25:46.000000000-08:00 c21f6c22ba27: (from whenry/testimage:latest) stop
</pre>
</dl>
<p> The following example outputs all events that were generated in the last 3 minutes, relative to the current time on the client machine: </p>
<dl>
<dt>
<dd>
<pre>
# docker events --since '3m'
2015-05-12T11:51:30.999999999Z07:00  4386fb97867d: (from ubuntu-1:14.04) die
2015-05-12T15:52:12.999999999Z07:00  4386fb97867d: (from ubuntu-1:14.04) stop
2015-05-12T15:53:45.999999999Z07:00  7805c1d35632: (from redis:2.8) die
2015-05-12T15:54:03.999999999Z07:00  7805c1d35632: (from redis:2.8) stop
</pre>
</dl>
<p> If you do not provide the &#8211;since option, the command returns only new and/or live events. </p>
<h2>HISTORY</h2>
<p> April 2014, Originally compiled by William Henry (whenry at redhat dot com) based on docker.com source material and internal work. June 2014, updated by Sven Dowideit &lt;SvenDowideit [at] home.org.au&gt; June 2015, updated by Brian Goff &lt;cpuguy83 [at] gmail.com&gt; October 2015, updated by Mike Brown &lt;mikebrow [at] gmail.com&gt; </p>
<h2>Index</h2>
