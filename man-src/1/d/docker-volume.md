---
title: "docker-volume(1)"
name: "docker-volume"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-volume/"
description: "docker-volume – Manage volumes"
---

<h2 class="name">NAME</h2>
<p> docker-volume &#8211; Manage volumes </p>
<h2>SYNOPSIS</h2>
<p> <code>docker volume COMMAND</code> </p>
<h2>DESCRIPTION</h2>
<p> The docker volume command has subcommands for managing data volumes. A data volume is a specially-designated directory that by-passes storage driver management. </p>
<p> Data volumes persist data independent of a container&#8217;s life cycle. When you delete a container, the Docker daemon does not delete any data volumes. You can share volumes across multiple containers. Moreover, you can share data volumes with other computing resources in your system. </p>
<p> To see help for a subcommand, use: </p>
<dl>
<dt>
<dd>
<pre>
docker volume COMMAND --help
</pre>
</dl>
<p> For full details on using docker volume visit Docker&#8217;s online documentation. </p>
<h2>OPTIONS</h2>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for volume</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker/">docker</a>(1)</code>, <code><a href="/docs/linux/man/1-docker-volume-create/">docker-volume-create</a>(1)</code>, <code><a href="/docs/linux/man/1-docker-volume-inspect/">docker-volume-inspect</a>(1)</code>, <code><a href="/docs/linux/man/1-docker-volume-ls/">docker-volume-ls</a>(1)</code>, <code><a href="/docs/linux/man/1-docker-volume-prune/">docker-volume-prune</a>(1)</code>, <code><a href="/docs/linux/man/1-docker-volume-rm/">docker-volume-rm</a>(1)</code> </p>
<h2>Index</h2>
