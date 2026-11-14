---
title: "ata_phys_link_online(9)"
name: "ata_phys_link_online"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_phys_link_online/"
description: "ata_phys_link_online – test whether the given link is online"
---

<p>ata_phys_link_online &#8211; test whether the given link is online</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool ata_phys_link_online(struct ata_link&nbsp;<wbr>*&nbsp;<wbr></code><i>link</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>link</i></p>
<dl>
<dd>
<dd>ATA link to test</dl>
<h2>Description</h2>
<p>Test whether <i>link</i> is online. Note that this function returns 0 if online status of <i>link</i> cannot be obtained, so ata_link_online(link) != !ata_link_offline(link). </p>
<p> LOCKING: None.</p>
<h2>Return</h2>
<p>True if the port online status is available and online.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
