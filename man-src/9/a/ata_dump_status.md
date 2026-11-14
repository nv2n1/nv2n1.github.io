---
title: "ata_dump_status(9)"
name: "ata_dump_status"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_dump_status/"
description: "ata_dump_status – user friendly display of error info"
---

<p>ata_dump_status &#8211; user friendly display of error info</p>
<h2>Synopsis</h2>
<pre><code>void ata_dump_status(unsigned id, struct ata_taskfile *tf);</code></pre>
<h2>Arguments</h2>
<p><i>id</i></p>
<dl>
<dd>
<dd>id of the port in question</dl>
<p> <i>tf</i></p>
<dl>
<dd>ptr to filled out taskfile</dl>
<h2>Description</h2>
<p>Decode and dump the ATA error/status registers for the user so that they have some idea what really happened at the non make-believe layer. </p>
<p> LOCKING: inherited from caller</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
