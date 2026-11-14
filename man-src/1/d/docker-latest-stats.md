---
title: "docker-latest-stats(1)"
name: "docker-latest-stats"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-latest-stats/"
description: "docker-stats – Display a live stream of one or more containers’ resource usage statistics"
---

<h2 class="name">NAME</h2>
<p> docker-stats &#8211; Display a live stream of one or more containers&#8217; resource usage statistics </p>
<h2>SYNOPSIS</h2>
<p> <code>docker stats</code> [<code>-a</code>|<code>&#8211;all</code>] [<code>&#8211;help</code>] [<code>&#8211;no-stream</code>] [CONTAINER&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> Display a live stream of one or more containers&#8217; resource usage statistics </p>
<h2>OPTIONS</h2>
<p> <code>-a</code>, <code>&#8211;all</code>=<i>true</i>|<i>false</i><br />
Show all containers. Only running containers are shown by default. The default is&nbsp;<wbr><i>false</i>. </p>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;<wbr>Print usage statement </p>
<p> <code>&#8211;no-stream</code>=<i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;<wbr>Disable streaming stats and only pull the first result, default setting is false. </p>
<h2>EXAMPLES</h2>
<p> Running docker stats on all running containers </p>
<dl>
<dt>
<dd>
<pre>
$ docker stats
CONTAINER           CPU %               MEM USAGE / LIMIT     MEM %               NET I/O             BLOCK I/O
1285939c1fd3        0.07%               796 KiB / 64 MiB        1.21%               788 B / 648 B       3.568 MB / 512 KB
9c76f7834ae2        0.07%               2.746 MiB / 64 MiB      4.29%               1.266 KB / 648 B    12.4 MB / 0 B
d1ea048f04e4        0.03%               4.583 MiB / 64 MiB      6.30%               2.854 KB / 648 B    27.7 MB / 0 B
</pre>
</dl>
<p> Running docker stats on multiple containers by name and id. </p>
<dl>
<dt>
<dd>
<pre>
$ docker stats fervent_panini 5acfcb1b4fd1
CONTAINER           CPU %               MEM USAGE/LIMIT     MEM %               NET I/O
5acfcb1b4fd1        0.00%               115.2 MiB/1.045 GiB   11.03%              1.422 kB/648 B
fervent_panini      0.02%               11.08 MiB/1.045 GiB   1.06%               648 B/648 B
</pre>
</dl>
<h2>Index</h2>
