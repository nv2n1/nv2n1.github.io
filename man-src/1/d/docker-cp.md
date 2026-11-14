---
title: "docker-cp(1)"
name: "docker-cp"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-cp/"
description: "docker-cp – Copy files/folders between a container and the local filesystem"
---

<h2 class="name">NAME</h2>
<p> docker-cp &#8211; Copy files/folders between a container and the local filesystem </p>
<h2>SYNOPSIS</h2>
<p> <code>docker cp [OPTIONS] CONTAINER:SRC_PATH DEST_PATH|- <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>docker cp [OPTIONS] SRC_PATH|- CONTAINER:DEST_PATH</code></p>
<h2>DESCRIPTION</h2>
<p> Alias for docker container cp. </p>
<h2>OPTIONS</h2>
<p> <code>-a</code>, <code>&#8211;archive</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Archive mode (copy all uid/gid information)</p>
<p> <code>-L</code>, <code>&#8211;follow-link</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Always follow symbol link in SRC_PATH</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for cp</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker/">docker</a>(1)</code> </p>
<h2>Index</h2>
