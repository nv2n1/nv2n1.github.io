---
title: "struct_ccw1(9)"
name: "struct_ccw1"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_ccw1/"
description: "struct_ccw1 – channel command word"
---

<p>struct_ccw1 &#8211; channel command word</p>
<h2>Synopsis</h2>
<pre><code>struct ccw1 {
    __u8 cmd_code;
    __u8 flags;
    __u16 count;
    __u32 cda;
};</code></pre>
<h2>Members</h2>
<p>cmd_code</p>
<dl>
<dd>command code</dl>
<p> flags</p>
<dl>
<dd>flags, like IDA addressing, etc.</dl>
<p> count</p>
<dl>
<dd>byte count</dl>
<p> cda</p>
<dl>
<dd>data address</dl>
<h2>Description</h2>
<p>The ccw is the basic structure to build channel programs that perform operations with the device or the control unit. Only Format-1 channel command words are supported.</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
