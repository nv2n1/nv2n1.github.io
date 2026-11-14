---
title: "ata_host_resume(9)"
name: "ata_host_resume"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_host_resume/"
description: "ata_host_resume – resume host"
---

<p>ata_host_resume &#8211; resume host</p>
<h2>Synopsis</h2>
<pre><code>void ata_host_resume(struct ata_host *host);</code></pre>
<h2>Arguments</h2>
<p><i>host</i></p>
<dl>
<dd>
<dd>host to resume</dl>
<h2>Description</h2>
<p>Resume <i>host</i>. Actual operation is performed by port resume.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
