---
title: "sata_lpm_ignore_phy_events(9)"
name: "sata_lpm_ignore_phy_events"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sata_lpm_ignore_phy_events/"
description: "sata_lpm_ignore_phy_events – test if PHY event should be ignored"
---

<p>sata_lpm_ignore_phy_events &#8211; test if PHY event should be ignored</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool sata_lpm_ignore_phy_events(struct ata_link&nbsp;<wbr>*&nbsp;<wbr></code><i>link</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>link</i></p>
<dl>
<dd>
<dd>Link receiving the event</dl>
<h2>Description</h2>
<p>Test whether the received PHY event has to be ignored or not. </p>
<p> LOCKING: None:</p>
<h2>Return</h2>
<p>True if the event has to be ignored.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
