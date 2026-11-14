---
title: "ata_timing_cycle2mode(9)"
name: "ata_timing_cycle2mode"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_timing_cycle2mode/"
description: "ata_timing_cycle2mode – find xfer mode for the specified cycle duration"
---

<p>ata_timing_cycle2mode &#8211; find xfer mode for the specified cycle duration</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>u8 ata_timing_cycle2mode(unsigned int&nbsp;<wbr></code><i>xfer_shift</i><code>, int&nbsp;<wbr></code><i>cycle</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>xfer_shift</i></p>
<dl>
<dd>
<dd>ATA_SHIFT_* value for transfer type to examine.</dl>
<p> <i>cycle</i></p>
<dl>
<dd>cycle duration in ns</dl>
<h2>Description</h2>
<p>Return matching xfer mode for <i>cycle</i>. The returned mode is of the transfer type specified by <i>xfer_shift</i>. If <i>cycle</i> is too slow for <i>xfer_shift</i>, 0xff is returned. If <i>cycle</i> is faster than the fastest known mode, the fasted mode is returned. </p>
<p> LOCKING: None.</p>
<h2>Return</h2>
<p>Matching xfer_mode, 0xff if no match found.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
