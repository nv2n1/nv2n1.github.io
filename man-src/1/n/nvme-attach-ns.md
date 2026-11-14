---
title: "nvme-attach-ns(1)"
name: "nvme-attach-ns"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nvme-attach-ns/"
---

<h2 class="name">NAME</h2>
 

 nvme-attach-ns - Send NVMe attach namespace, return result. 

<h2>SYNOPSIS</h2>

 

 <pre><code>
nvme attach - ns&lt;device&gt;[--namespace - id = &lt;nsid&gt; | -n&lt;nsid&gt;]
                        [--controllers = &lt;ctrl - list, &gt; | -c&lt;ctrl - list, &gt;]
</code></pre>

<h2>DESCRIPTION</h2>

 

 For the NVMe device given, sends the nvme namespace attach command for the provided namespace identifier, attaching to the provided list of controller identifiers.

<h2>OPTIONS</h2>

 

 -n &lt;nsid&gt;, --namespace-id=&lt;nsid&gt;
<dl>
<dt>
<dd> The namespace identifier to attach.</dl>
 

 -c &lt;ctrl-list,&gt;, -controllers=&lt;ctrl-list,&gt;
<dl>
<dt>
<dd> The comma separated list of controller identifiers to attach the namesapce too.</dl>

<h2>EXAMPLES</h2>

 

 No examples yet.

<h2>NVME</h2>

 

 Part of the nvme-user suite 

<h2>Index</h2>


