---
title: "docker-context-update(1)"
name: "docker-context-update"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-context-update/"
description: "docker-context-update – Update a context"
---

<h2 class="name">NAME</h2>
<p> docker-context-update &#8211; Update a context </p>
<h2>SYNOPSIS</h2>
<p> <code>docker context update [OPTIONS] CONTEXT</code> </p>
<h2>DESCRIPTION</h2>
<p> Update a context </p>
<p> Docker endpoint config: </p>
<p> NAME DESCRIPTION from Copy named context&#8217;s Docker endpoint configuration host Docker endpoint on which to connect ca Trust certs signed only by this CA cert Path to TLS certificate file key Path to TLS key file skip-tls-verify Skip TLS certificate validation </p>
<p> Kubernetes endpoint config: </p>
<p> NAME DESCRIPTION from Copy named context&#8217;s Kubernetes endpoint configuration config-file Path to a Kubernetes config file context-override Overrides the context set in the kubernetes config file namespace-override Overrides the namespace set in the kubernetes config file </p>
<p> Example: </p>
<p> $ docker context update my-context &#8211;description &quot;some description&quot; &#8211;docker &quot;host=<a href="tcp://myserver:2376,ca=~/ca-file,cert=~/cert-file,key=~/key-file">tcp://myserver:2376,ca=~/ca-file,cert=~/cert-file,key=~/key-file</a>&quot; </p>
<h2>OPTIONS</h2>
<p> <code>&#8211;default-stack-orchestrator</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Default orchestrator for stack operations to use with this context (swarm|kubernetes|all)</p>
<p> <code>&#8211;description</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Description of the context</p>
<p> <code>&#8211;docker</code>=[] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>set the docker endpoint</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for update</p>
<p> <code>&#8211;kubernetes</code>=[] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>set the kubernetes endpoint</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-context/">docker-context</a>(1)</code> </p>
<h2>Index</h2>
