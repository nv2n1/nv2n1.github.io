---
title: "struct_erw(9)"
name: "struct_erw"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_erw/"
description: "struct_erw – extended report word"
---

<p>struct_erw &#8211; extended report word</p>
<h2>Synopsis</h2>
<pre><code>struct erw {
    __u32 res0 : 3;
    __u32 auth : 1;
    __u32 pvrf : 1;
    __u32 cpt : 1;
    __u32 fsavf : 1;
    __u32 cons : 1;
    __u32 scavf : 1;
    __u32 fsaf : 1;
    __u32 scnt : 6;
    __u32 res16 : 16;
};</code></pre>
<h2>Members</h2>
<p>res0</p>
<dl>
<dd>reserved</dl>
<p> auth</p>
<dl>
<dd>authorization check</dl>
<p> pvrf</p>
<dl>
<dd>path-verification-required flag</dl>
<p> cpt</p>
<dl>
<dd>channel-path timeout</dl>
<p> fsavf</p>
<dl>
<dd>failing storage address validity flag</dl>
<p> cons</p>
<dl>
<dd>concurrent sense</dl>
<p> scavf</p>
<dl>
<dd>secondary ccw address validity flag</dl>
<p> fsaf</p>
<dl>
<dd>failing storage address format</dl>
<p> scnt</p>
<dl>
<dd>sense count, if <i>cons</i> == <code>1</code></dl>
<p> res16</p>
<dl>
<dd>reserved</dl>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
