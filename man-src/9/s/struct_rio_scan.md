---
title: "struct_rio_scan(9)"
name: "struct_rio_scan"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_rio_scan/"
description: "struct_rio_scan – RIO enumeration and discovery operations"
---

<p>struct_rio_scan &#8211; RIO enumeration and discovery operations</p>
<h2>Synopsis</h2>
<pre><code>struct rio_scan {
    struct module *owner;
    int (*enumerate)(struct rio_mport *mport, u32 flags);
    int (*discover)(struct rio_mport *mport, u32 flags);
};</code></pre>
<h2>Members</h2>
<p>owner</p>
<dl>
<dd>The module owner of this structure</dl>
<p> enumerate</p>
<dl>
<dd>Callback to perform RapidIO fabric enumeration.</dl>
<p> discover</p>
<dl>
<dd>Callback to perform RapidIO fabric discovery.</dl>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
