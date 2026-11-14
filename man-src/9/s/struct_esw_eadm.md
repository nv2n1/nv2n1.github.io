---
title: "struct_esw_eadm(9)"
name: "struct_esw_eadm"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_esw_eadm/"
description: "struct_esw_eadm – EADM Subchannel Extended Status Word (ESW)"
---

<p>struct_esw_eadm &#8211; EADM Subchannel Extended Status Word (ESW)</p>
<h2>Synopsis</h2>
<pre><code>struct esw_eadm {
    __u32 sublog;
    struct erw_eadm erw;
};</code></pre>
<h2>Members</h2>
<p>sublog</p>
<dl>
<dd>subchannel logout</dl>
<p> erw</p>
<dl>
<dd>extended report word</dl>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
