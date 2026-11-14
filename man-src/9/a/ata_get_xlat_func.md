---
title: "ata_get_xlat_func(9)"
name: "ata_get_xlat_func"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_get_xlat_func/"
description: "ata_get_xlat_func – check if SCSI to ATA translation is possible"
---

<p>ata_get_xlat_func &#8211; check if SCSI to ATA translation is possible</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ata_xlat_func_t ata_get_xlat_func(struct ata_device&nbsp;<wbr>*&nbsp;<wbr></code><i>dev</i><code>, u8&nbsp;<wbr></code><i>cmd</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>ATA device</dl>
<p> <i>cmd</i></p>
<dl>
<dd>SCSI command opcode to consider</dl>
<h2>Description</h2>
<p>Look up the SCSI command given, and determine whether the SCSI command is to be translated or simulated.</p>
<h2>Return</h2>
<p>Pointer to translation function if possible, <code>NULL</code> if not.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
