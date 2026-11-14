---
title: "docker-container-stats(1)"
name: "docker-container-stats"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-container-stats/"
description: "docker-container-stats – Display a live stream of container(s) resource usage statistics"
---

<h2 class="name">NAME</h2>
<p> docker-container-stats &#8211; Display a live stream of container(s) resource usage statistics </p>
<h2>SYNOPSIS</h2>
<p> <code>docker container stats [OPTIONS] [CONTAINER&#8230;]</code> </p>
<h2>DESCRIPTION</h2>
<p> Display a live stream of one or more containers&#8217; resource usage statistics </p>
<h2>Format</h2>
<p> Pretty-print containers statistics using a Go template.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Valid placeholders:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.Container &#8211; Container name or ID.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.Name &#8211; Container name.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.ID &#8211; Container ID.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.CPUPerc &#8211; CPU percentage.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.MemUsage &#8211; Memory usage.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.NetIO &#8211; Network IO.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.BlockIO &#8211; Block IO.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.MemPerc &#8211; Memory percentage&nbsp;(Not available on Windows).<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;.PIDs &#8211; Number of PIDs&nbsp;(Not available on Windows). </p>
<h2>EXAMPLES</h2>
<p> Running docker container stats on all running containers. </p>
<dl>
<dt>
<dd>
<pre>
$ docker container stats
CONTAINER           CPU %               MEM USAGE / LIMIT     MEM %               NET I/O             BLOCK I/O
1285939c1fd3        0.07%               796 KiB / 64 MiB        1.21%               788 B / 648 B       3.568 MB / 512 KB
9c76f7834ae2        0.07%               2.746 MiB / 64 MiB      4.29%               1.266 KB / 648 B    12.4 MB / 0 B
d1ea048f04e4        0.03%               4.583 MiB / 64 MiB      6.30%               2.854 KB / 648 B    27.7 MB / 0 B
</pre>
</dl>
<p> Running docker container stats on multiple containers by name and id. </p>
<dl>
<dt>
<dd>
<pre>
$ docker container stats fervent_panini 5acfcb1b4fd1
CONTAINER           CPU %               MEM USAGE/LIMIT     MEM %               NET I/O
5acfcb1b4fd1        0.00%               115.2 MiB/1.045 GiB   11.03%              1.422 kB/648 B
fervent_panini      0.02%               11.08 MiB/1.045 GiB   1.06%               648 B/648 B
</pre>
</dl>
<p> Running docker container stats with customized format on all (Running and Stopped) containers. </p>
<dl>
<dt>
<dd>
<pre><code>
$ docker container stats-- all-- format "table &#123;&#123;.ID}}	&#123;&#123;.Name}}	&#123;&#123;.CPUPerc}}	&#123;&#123;.MemUsage}}" CONTAINER ID NAME CPU % MEM USAGE / LIMIT c9dfa83f0317f87637d5b7e67aa4223337d947215c5a9947e697e4f7d3e0f834 ecstatic_noether 0.00 % 56KiB / 15.57GiB 8f92d01cf3b29b4f5fca4cd33d907e05def7af5a3684711b20a2369d211ec67f stoic_goodall 0.07 % 32.86MiB / 15.57GiB 38dd23dba00f307d53d040c1d18a91361bbdcccbf592315927d56cf13d8b7343 drunk_visvesvaraya 0.00 % 0B / 0B 5a8b07ec4cc52823f3cbfdb964018623c1ba307bce2c057ccdbde5f4f6990833 big_heisenberg 0.00 % 0B / 0B
</code></pre>
</dl>
<p> drunk_visvesvaraya and big_heisenberg are stopped containers in the above example. </p>
<h2>OPTIONS</h2>
<p> <code>-a</code>, <code>&#8211;all</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Show all containers (default shows just running)</p>
<p> <code>&#8211;format</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Pretty-print images using a Go template</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for stats</p>
<p> <code>&#8211;no-stream</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Disable streaming stats and only pull the first result</p>
<p> <code>&#8211;no-trunc</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Do not truncate output</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-container/">docker-container</a>(1)</code> </p>
<h2>Index</h2>
