---
title: "struct_irb(9)"
name: "struct_irb"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_irb/"
description: "struct_irb – interruption response block"
---

<p>struct_irb &#8211; interruption response block</p>
<h2>Synopsis</h2>
<pre><code>struct irb {
    union scsw scsw;
    union esw;
    __u8 ecw[32];
};</code></pre>
<h2>Members</h2>
<p>scsw</p>
<dl>
<dd>subchannel status word</dl>
<p> esw</p>
<dl>
<dd>extended status word</dl>
<p> ecw[32]</p>
<dl>
<dd>extended control word</dl>
<h2>Description</h2>
<p>The irb that is handed to the device driver when an interrupt occurs. For solicited interrupts, the common I/O layer already performs checks whether a field is valid; a field not being valid is always passed as <code>0</code>. If a unit check occurred, <i>ecw</i> may contain sense data; this is retrieved by the common I/O layer itself if the device doesn&#8217;t support concurrent sense (so that the device driver never needs to perform basic sene itself). For unsolicited interrupts, the irb is passed as-is (expect for sense data, if applicable).</p>
<h2>Author</h2>
<p><code>Cornelia Huck</code> &lt;cornelia.huck [at] de.ibm.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
