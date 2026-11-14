---
title: "atapi_cmd_type(9)"
name: "atapi_cmd_type"
section: "9"
letter: "a"
url: "/docs/linux/man/9-atapi_cmd_type/"
description: "atapi_cmd_type – Determine ATAPI command type from SCSI opcode"
---

<p>atapi_cmd_type &#8211; Determine ATAPI command type from SCSI opcode</p>
<h2>Synopsis</h2>
<pre><code>int atapi_cmd_type(u8 opcode);</code></pre>
<h2>Arguments</h2>
<p><i>opcode</i></p>
<dl>
<dd>
<dd>SCSI opcode</dl>
<h2>Description</h2>
<p>Determine ATAPI command type from <i>opcode</i>. </p>
<p> LOCKING: None.</p>
<h2>Return</h2>
<p>ATAPI_{READ|WRITE|READ_CD|PASS_THRU|MISC}</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
