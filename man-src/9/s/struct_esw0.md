---
title: "struct_esw0(9)"
name: "struct_esw0"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_esw0/"
description: "struct_esw0 – Format 0 Extended Status Word (ESW)"
---

<p>struct_esw0 &#8211; Format 0 Extended Status Word (ESW)</p>
<h2>Synopsis</h2>
<pre><code>struct esw0 {
    struct sublog sublog;
    struct erw erw;
    __u32 faddr[2];
    __u32 saddr;
};</code></pre>
<h2>Members</h2>
<p>sublog</p>
<dl>
<dd>subchannel logout</dl>
<p> erw</p>
<dl>
<dd>extended report word</dl>
<p> faddr[2]</p>
<dl>
<dd>failing storage address</dl>
<p> saddr</p>
<dl>
<dd>secondary ccw address</dl>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
