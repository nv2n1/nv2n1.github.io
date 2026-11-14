---
title: "struct_erw_eadm(9)"
name: "struct_erw_eadm"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_erw_eadm/"
description: "struct_erw_eadm – EADM Subchannel extended report word"
---

<p>struct_erw_eadm &#8211; EADM Subchannel extended report word</p>
<h2>Synopsis</h2>
<pre><code>struct erw_eadm {
    __u32 b : 1;
    __u32 r : 1;
};</code></pre>
<h2>Members</h2>
<p>b</p>
<dl>
<dd>aob error</dl>
<p> r</p>
<dl>
<dd>arsb error</dl>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
