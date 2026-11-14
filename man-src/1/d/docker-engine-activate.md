---
title: "docker-engine-activate(1)"
name: "docker-engine-activate"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-engine-activate/"
description: "docker-engine-activate – Activate Enterprise Edition"
---

<h2 class="name">NAME</h2>
<p> docker-engine-activate &#8211; Activate Enterprise Edition </p>
<h2>SYNOPSIS</h2>
<p> <code>docker engine activate [OPTIONS]</code> </p>
<h2>DESCRIPTION</h2>
<p> Activate Enterprise Edition. </p>
<p> With this command you may apply an existing Docker enterprise license, or interactively download one from Docker. In the interactive exchange, you can sign up for a new trial, or download an existing license. If you are currently running a Community Edition engine, the daemon will be updated to the Enterprise Edition Docker engine with additional capabilities and long term support. </p>
<p> For more information about different Docker Enterprise license types visit </p>
<p> &lt;<a rel="nofollow" href="https://www.docker.com/licenses">https://www.docker.com/licenses</a>&gt; </p>
<p> For non-interactive scriptable deployments, download your license from </p>
<p> &lt;<a rel="nofollow" href="https://hub.docker.com/">https://hub.docker.com/</a>&gt; then specify the file with the &#8216;&#8211;license&#8217; flag. </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;containerd</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;override default location of containerd endpoint </p>
<p> <code>&#8211;display-only</code>[=false]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;only display license information and exit </p>
<p> <code>&#8211;engine-image</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Specify engine image </p>
<p> <code>&#8211;format</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Pretty-print licenses using a Go template </p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;help for activate </p>
<p> <code>&#8211;license</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;License File </p>
<p> <code>&#8211;quiet</code>[=false]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Only display available licenses by ID </p>
<p> <code>&#8211;registry-prefix</code>=&quot;docker.io/store/docker&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Override the default location where engine images are pulled </p>
<p> <code>&#8211;version</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Specify engine version&nbsp;(default is to use currently running version) </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-engine/">docker-engine</a>(1)</code> </p>
<h2>Index</h2>
