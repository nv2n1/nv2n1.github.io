---
title: "docker-deploy(1)"
name: "docker-deploy"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-deploy/"
description: "docker-deploy – Deploy a new stack or update an existing stack"
---

<h2 class="name">NAME</h2>
<p> docker-deploy &#8211; Deploy a new stack or update an existing stack </p>
<h2>SYNOPSIS</h2>
<p> <code>docker deploy [OPTIONS] STACK</code> </p>
<h2>DESCRIPTION</h2>
<p> Deploy a new stack or update an existing stack </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;bundle-file</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Path to a Distributed Application Bundle file </p>
<p> <code>-c</code>, <code>&#8211;compose-file</code>=[]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Path to a Compose file, or&nbsp;&quot;-&quot;&nbsp;to read from stdin </p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;help for deploy </p>
<p> <code>&#8211;namespace</code>=&quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Kubernetes namespace to use </p>
<p> <code>&#8211;prune</code>[=false]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Prune services that are no longer referenced </p>
<p> <code>&#8211;resolve-image</code>=&quot;always&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Query the registry to resolve image digest and supported platforms&nbsp;(&quot;always&quot;|&quot;changed&quot;|&quot;never&quot;) </p>
<p> <code>&#8211;with-registry-auth</code>[=false]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Send registry authentication details to Swarm agents </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker/">docker</a>(1)</code> </p>
<h2>Index</h2>
