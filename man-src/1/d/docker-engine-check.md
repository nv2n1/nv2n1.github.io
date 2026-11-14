---
title: "docker-engine-check(1)"
name: "docker-engine-check"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-engine-check/"
description: "docker-engine-check – Check for available engine updates"
---

<h2 class="name">NAME</h2>
<p> docker-engine-check &#8211; Check for available engine updates </p>
<h2>SYNOPSIS</h2>
<p> <code>docker engine check [OPTIONS]</code> </p>
<h2>DESCRIPTION</h2>
<p> Check for available engine updates </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;containerd</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;override default location of containerd endpoint </p>
<p> <code>&#8211;downgrades</code>[=false]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Report downgrades&nbsp;(default omits older versions) </p>
<p> <code>&#8211;engine-image</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Specify engine image&nbsp;(default uses the same image as currently running) </p>
<p> <code>&#8211;format</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Pretty-print updates using a Go template </p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;help for check </p>
<p> <code>&#8211;pre-releases</code>[=false]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Include pre-release versions </p>
<p> <code>-q</code>, <code>&#8211;quiet</code>[=false]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Only display available versions </p>
<p> <code>&#8211;registry-prefix</code>=&quot;docker.io/store/docker&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Override the existing location where engine images are pulled </p>
<p> <code>&#8211;upgrades</code>[=true]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Report available upgrades </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-engine/">docker-engine</a>(1)</code> </p>
<h2>Index</h2>
