---
title: "ndctl-read-labels(1)"
name: "ndctl-read-labels"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ndctl-read-labels/"
description: "ndctl-read-labels – read out the label area on a dimm or set of dimms"
---

<h2 class="name">NAME</h2>
<p> ndctl-read-labels &#8211; read out the label area on a dimm or set of dimms </p>
<h2>SYNOPSIS</h2>
<pre><code>
ndctl read - labels&lt;nmem0&gt;[&lt;nmem1&gt;..&lt;nmemN&gt;][&lt;options&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The namespace label area is a small persistent partition of capacity available on some NVDIMM devices. The label area is used to resolve aliasing between <i>pmem</i> and <i>blk</i> capacity by lineating namespace boundaries. This command dumps the raw binary data in a dimm&#8217;s label area to stdout or a file. In the multi-dimm case the data is concatenated.</p>
<h2>OPTIONS</h2>
<p> &lt;memory device(s)&gt;&#8230;</p>
<dl>
<dt>
<dd> One or more <i>nmemX</i> device names. The keyword <i>all</i> can be specified to operate on every dimm in the system, optionally filtered by bus id (see &#8211;bus= option).</dl>
<p> -b, &#8211;bus=</p>
<dl>
<dt>
<dd> Limit operation to memory devices (dimms) that are on the given bus. Where <i>bus</i> can be a provider name or a bus id number.</dl>
<p> -v</p>
<dl>
<dt>
<dd> Turn on verbose debug messages in the library (if ndctl was built with logging and debug enabled).</dl>
<p> -o</p>
<dl>
<dt>
<dd> output file</dl>
<p> -j, &#8211;json</p>
<dl>
<dt>
<dd> parse the label data into json assuming the <i>NVDIMM Namespace Specification</i> format.</dl>
<h2>SEE ALSO</h2>
<p> m[blue]<code>NVDIMM Namespace Specification</code>m[]<font SIZE="-2">[1]</font></p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> NVDIMM Namespace Specification</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://pmem.io/documents/NVDIMM_Namespace_Spec.pdf">http://pmem.io/documents/NVDIMM_Namespace_Spec.pdf</a></dl>
</dl>
<h2>Index</h2>
