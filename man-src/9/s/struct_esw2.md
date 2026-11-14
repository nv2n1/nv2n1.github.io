---
title: "struct_esw2(9)"
name: "struct_esw2"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_esw2/"
description: "struct_esw2 – Format 2 Extended Status Word (ESW)"
---

<p>struct_esw2 &#8211; Format 2 Extended Status Word (ESW)</p>
<h2>Synopsis</h2>
<pre><code>struct esw2 {
    __u8 zero0;
    __u8 lpum;
    __u16 dcti;
    struct erw erw;
    __u32 zeros[3];
};</code></pre>
<h2>Members</h2>
<p>zero0</p>
<dl>
<dd>reserved zeros</dl>
<p> lpum</p>
<dl>
<dd>last path used mask</dl>
<p> dcti</p>
<dl>
<dd>device-connect-time interval</dl>
<p> erw</p>
<dl>
<dd>extended report word</dl>
<p> zeros[3]</p>
<dl>
<dd>three fullwords of zeros</dl>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
