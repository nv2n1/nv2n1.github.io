---
title: "docker-stack-deploy(1)"
name: "docker-stack-deploy"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-stack-deploy/"
description: "docker-stack-deploy – Deploy a new stack or update an existing stack"
---

<h2 class="name">NAME</h2>
<p> docker-stack-deploy &#8211; Deploy a new stack or update an existing stack </p>
<h2>SYNOPSIS</h2>
<p> <code>docker stack deploy [OPTIONS] STACK</code> </p>
<h2>DESCRIPTION</h2>
<p> Deploy a new stack or update an existing stack </p>
<h2>OPTIONS</h2>
<p> <code>-c</code>, <code>&#8211;compose-file</code>=[] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Path to a Compose file, or &quot;-&quot; to read from stdin</p>
<p> <code>-h</code>, <code>&#8211;help</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>help for deploy</p>
<p> <code>&#8211;namespace</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Kubernetes namespace to use</p>
<p> <code>&#8211;prune</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Prune services that are no longer referenced</p>
<p> <code>&#8211;resolve-image</code>=&quot;always&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Query the registry to resolve image digest and supported platforms (&quot;always&quot;|&quot;changed&quot;|&quot;never&quot;)</p>
<p> <code>&#8211;with-registry-auth</code>[=false] <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Send registry authentication details to Swarm agents</p>
<h2>OPTIONS INHERITED FROM PARENT COMMANDS</h2>
<p> <code>&#8211;kubeconfig</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Kubernetes config file</p>
<p> <code>&#8211;orchestrator</code>=&quot;&quot; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Orchestrator to use (swarm|kubernetes|all)</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-docker-stack/">docker-stack</a>(1)</code> </p>
<h2>Index</h2>
