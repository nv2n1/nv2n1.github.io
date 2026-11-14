---
title: "ndctl-disable-namespace(1)"
name: "ndctl-disable-namespace"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ndctl-disable-namespace/"
description: "ndctl-disable-namespace – disable the given namespace(s)"
---

<h2 class="name">NAME</h2>
<p> ndctl-disable-namespace &#8211; disable the given namespace(s) </p>
<h2>SYNOPSIS</h2>
<pre>
<i>ndctl disable-namespace</i> &lt;namespace&gt; [&lt;options&gt;]
</pre>
<h2>DESCRIPTION</h2>
<p> A REGION, after resolving DPA aliasing and LABEL specified boundaries, surfaces one or more &quot;namespace&quot; devices. The arrival of a &quot;namespace&quot; device currently triggers either the nd_blk or nd_pmem driver to load and register a disk/block device.</p>
<h2>OPTIONS</h2>
<p> &lt;namespace&gt;</p>
<dl>
<dt>
<dd> A <i>namespaceX.Y</i> device name. The keyword <i>all</i> can be specified to carry out the operation on every namespace in the system, optionally filtered by region (see &#8211;region=option)</dl>
<p> -r, &#8211;region=</p>
<dl>
<dt>
<dd> A <i>regionX</i> device name, or a region id number. The keyword <i>all</i> can be specified to carry out the operation on every region in the system, optionally filtered by bus id (see &#8211;bus= option).</dl>
<p> -b, &#8211;bus=</p>
<dl>
<dt>
<dd> Enforce that the operation only be carried on devices that are attached to the given bus. Where <i>bus</i> can be a provider name or a bus id number.</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> Emit debug messages for the namespace operation</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ndctl-disable-namespace/">ndctl-disable-namespace</a></code>(1) </p>
<h2>Index</h2>
