---
title: "struct_ciw(9)"
name: "struct_ciw"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_ciw/"
description: "struct_ciw – command information word (CIW) layout"
---

<p>struct_ciw &#8211; command information word (CIW) layout</p>
<h2>Synopsis</h2>
<pre><code>struct ciw {
    __u32 et : 2;
    __u32 reserved : 2;
    __u32 ct : 4;
    __u32 cmd : 8;
    __u32 count : 16;
};</code></pre>
<h2>Members</h2>
<p>et</p>
<dl>
<dd>entry type</dl>
<p> reserved</p>
<dl>
<dd>reserved bits</dl>
<p> ct</p>
<dl>
<dd>command type</dl>
<p> cmd</p>
<dl>
<dd>command code</dl>
<p> count</p>
<dl>
<dd>command count</dl>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
