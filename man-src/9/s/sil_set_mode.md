---
title: "sil_set_mode(9)"
name: "sil_set_mode"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sil_set_mode/"
description: "sil_set_mode – wrap set_mode functions"
---

<p>sil_set_mode &#8211; wrap set_mode functions</p>
<h2>Synopsis</h2>
<pre><code>int sil_set_mode(struct ata_link *link, struct ata_device **r_failed);</code></pre>
<h2>Arguments</h2>
<p><i>link</i></p>
<dl>
<dd>
<dd>link to set up</dl>
<p> <i>r_failed</i></p>
<dl>
<dd>returned device when we fail</dl>
<h2>Description</h2>
<p>Wrap the libata method for device setup as after the setup we need to inspect the results and do some configuration work</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
