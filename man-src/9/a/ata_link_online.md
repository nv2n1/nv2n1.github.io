---
title: "ata_link_online(9)"
name: "ata_link_online"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_link_online/"
description: "ata_link_online – test whether the given link is online"
---

<p>ata_link_online &#8211; test whether the given link is online</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool ata_link_online(struct ata_link&nbsp;<wbr>*&nbsp;<wbr></code><i>link</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>link</i></p>
<dl>
<dd>
<dd>ATA link to test</dl>
<h2>Description</h2>
<p>Test whether <i>link</i> is online. This is identical to <code>ata_phys_link_online</code> when there&#8217;s no slave link. When there&#8217;s a slave link, this function should only be called on the master link and will return true if any of M/S links is online. </p>
<p> LOCKING: None.</p>
<h2>Return</h2>
<p>True if the port online status is available and online.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
