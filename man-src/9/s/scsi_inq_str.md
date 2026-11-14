---
title: "scsi_inq_str(9)"
name: "scsi_inq_str"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_inq_str/"
description: "scsi_inq_str – print INQUIRY data from min to max index, strip trailing whitespace"
---

<p>scsi_inq_str &#8211; print INQUIRY data from min to max index, strip trailing whitespace</p>
<h2>Synopsis</h2>
<pre><code>unsigned char *scsi_inq_str(unsigned char *buf, unsigned char *inq, unsigned first, unsigned end);</code></pre>
<h2>Arguments</h2>
<p><i>buf</i></p>
<dl>
<dd>
<dd>Output buffer with at least end-first+1 bytes of space</dl>
<p> <i>inq</i></p>
<dl>
<dd>Inquiry buffer (input)</dl>
<p> <i>first</i></p>
<dl>
<dd>Offset of string into inq</dl>
<p> <i>end</i></p>
<dl>
<dd>Index after last character in inq</dl>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
