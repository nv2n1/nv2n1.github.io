---
title: "blktool(8)"
name: "blktool"
section: "8"
letter: "b"
url: "/docs/linux/man/8-blktool/"
description: "blktool – Display or change block device settings"
---

<p>blktool &#8211; Display or change block device settings</p>
<h2>Synopsis</h2>
<p><code>blktool [options]</code> <i>device</i> [<code>N</code>&nbsp;<wbr><code>acoustic-mgmt</code>] <code>blktool [options]</code> <i>device</i> [<code>N</code>&nbsp;<wbr><code>block-sz</code>] <code>blktool [options]</code> <i>device</i> [<code>bus-id</code>&nbsp;<wbr>] <code>blktool [options]</code> <i>device</i> [<code>N</code>&nbsp;<wbr><code>bus-state</code>] <code>blktool [options]</code> <i>device</i> [<code>class</code>&nbsp;<wbr>] <code>blktool [options]</code> <i>device</i> [<code>N</code>&nbsp;<wbr><code>cd-speed</code>] <code>blktool [options]</code> <i>device</i> [<code>defect-mgmt</code>&nbsp;<wbr><code>off</code>|<code>on</code>] <code>blktool [options]</code> <i>device</i> [<code>dev-keep-settings</code>&nbsp;<wbr><code>off</code>|<code>on</code>] <code>blktool [options]</code> <i>device</i> [<code>dev-read-ahead</code>&nbsp;<wbr><code>off</code>|<code>on</code>] <code>blktool [options]</code> <i>device</i> [<code>dma</code>&nbsp;<wbr><code>off</code>|<code>on</code>] <code>blktool [options]</code> <i>device</i> [<code>geometry</code>&nbsp;<wbr>] <code>blktool [options]</code> <i>device</i> [<code>N</code>&nbsp;<wbr><code>i2o-rcache</code>] <code>blktool [options]</code> <i>device</i> [<code>N</code>&nbsp;<wbr><code>i2o-wcache</code>] <code>blktool [options]</code> <i>device</i> [<code>id</code>&nbsp;<wbr>] <code>blktool [options]</code> <i>device</i> [<code>keep-settings</code>&nbsp;<wbr><code>off</code>|<code>on</code>] <code>blktool [options]</code> <i>device</i> [<code>media</code>&nbsp;<wbr><code>unlock</code>|<code>lock</code>] <code>blktool [options]</code> <i>device</i> [<code>N</code>&nbsp;<wbr><code>multiple-count</code>] <code>blktool [options]</code> <i>device</i> [<code>no-write-err</code>&nbsp;<wbr><code>off</code>|<code>on</code>] <code>blktool [options]</code> <i>device</i> [<code>pio-data</code>&nbsp;<wbr><code>16-bit</code>|<code>32-bit</code>] <code>blktool [options]</code> <i>device</i> [<code>N</code>&nbsp;<wbr><code>pio-mode</code>] <code>blktool [options]</code> <i>device</i> [<code>N</code>&nbsp;<wbr><code>pm-mode</code>] <code>blktool [options]</code> <i>device</i> [<code>N</code>&nbsp;<wbr><code>queue-depth</code>] <code>blktool [options]</code> <i>device</i> [<code>N</code>&nbsp;<wbr><code>read-ahead</code>] <code>blktool [options]</code> <i>device</i> [<code>readonly</code>&nbsp;<wbr><code>off</code>|<code>on</code>] <code>blktool [options]</code> <i>device</i> [<code>reread-part</code>&nbsp;<wbr>] <code>blktool [options]</code> <i>device</i> [<code>reset</code>&nbsp;<wbr>] <code>blktool [options]</code> <i>device</i> [<code>sector-sz</code>&nbsp;<wbr>] <code>blktool [options]</code> <i>device</i> [<code>sleep</code>&nbsp;<wbr>] <code>blktool [options]</code> <i>device</i> [<code>standby</code>&nbsp;<wbr>] <code>blktool [options]</code> <i>device</i> [<code>unmask-irq</code>&nbsp;<wbr><code>off</code>|<code>on</code>] <code>blktool [options]</code> <i>device</i> [<code>version</code>&nbsp;<wbr>] <code>blktool [options]</code> [<code>version</code>&nbsp;<wbr>] <code>blktool [options]</code> <i>device</i> [<code>wcache</code>&nbsp;<wbr><code>off</code>|<code>on</code>] </p>
<h2>Description</h2>
<p><code>blktool</code> is used for querying and/or changing settings of a block device. <i>device</i> is the name of the block device to query or modify. </p>
<h2>Options</h2>
<dl>
<dt><code>-f</code></dt>
<dd>For a few commands, blktool will flush the buffers of the block device out to disk, before performing the requested command. Specify this option, &quot;force&quot;, disables any flushing blktool would attempt to do. </dd>
<dt><code>-t class</code></dt>
<dd>where class is one of &#8216;ide&#8217;, &#8216;ata&#8217;, &#8216;scsi&#8217;, &#8216;i2o&#8217;, or &#8216;auto&#8217; to override the default auto-detection of device class. </dd>
</dl>
<h2>Commands</h2>
<dl>
<dt><code>acoustic-mgmt</code></dt>
<dd>Query or set underlying device&#8217;s acoustic level. </dd>
<dt><code>block-sz</code></dt>
<dd>Query or set device block size. </dd>
<dt><code>bus-id </code></dt>
<dd>Query device bus id. </dd>
<dt><code>bus-state</code></dt>
<dd>Query or set device bus state (0 off, 1 on, 2 tristate) </dd>
<dt><code>class</code></dt>
<dd>Query the detected (or overridden, via -t) device class. Typically this will result in &#8216;ATA&#8217; or &#8216;SCSI&#8217; for most devices. Detection is based on device major; thus your SATA device may appear as </dd>
<dt><code>cd-speed</code></dt>
<dd>Set CD-ROM device speed (in Kbytes/sec). </dd>
<dt><code>defect-mgmt</code></dt>
<dd>Toggle underlying device&#8217;s defect management (obsolete). </dd>
<dt><code>dev-keep-settings</code></dt>
<dd>Toggle underlying device&#8217;s revert-to-defaults-on-reset feature. </dd>
<dt><code>dev-read-ahead</code></dt>
<dd>Toggle underlying device&#8217;s read-ahead feature. </dd>
<dt><code>dma</code></dt>
<dd>Toggle DMA data transfer. Omitting the on/off argument will print the current state. </dd>
<dt><code>geometry</code></dt>
<dd>Query device geometry (cylinders / heads / sectors / etc.). </dd>
<dt><code>i2o-rcache</code></dt>
<dd>Query or set an I2O block device&#8217;s read cache. </dd>
<dt><code>i2o-wcache</code></dt>
<dd>Query or set an I2O block device&#8217;s write cache. </dd>
<dt><code>id </code></dt>
<dd>Query IDENTIFY [PACKET] DEVICE data. </dd>
<dt><code>keep-settings</code></dt>
<dd>Keep settings across device resets. Omitting the on/off argument will print the current state. </dd>
<dt><code>media</code></dt>
<dd>Lock in (or unlock) a removeable device. </dd>
<dt><code>multiple-count</code></dt>
<dd>Set multiple count for use in READ/WRITE MULTIPLE commands. </dd>
<dt><code>no-write-err</code></dt>
<dd>Toggle ignore-write-errors flag. Omitting the on/off argument will print the current state. </dd>
<dt><code>pio-data</code></dt>
<dd>ATA PIO data transfer via 16-bit or 32-bit I/O. Omitting the on/off argument will print the current state. </dd>
<dt><code>pio-mode</code></dt>
<dd>Set underlying ATA device&#8217;s PIO data transfer mode. </dd>
<dt><code>pm-mode</code></dt>
<dd>Set underlying device&#8217;s Advanced Power Management mode. </dd>
<dt><code>queued-depth</code></dt>
<dd>Query or set underlying device&#8217;s queue depth. </dd>
<dt><code>read-ahead</code></dt>
<dd>Query or set block device read-ahead (in units of sectors). </dd>
<dt><code>readonly</code></dt>
<dd>Toggle block device read-only setting. Omitting the on/off argument will print the current state. </dd>
<dt><code>reread-part</code></dt>
<dd>Re-read partition table. </dd>
<dt><code>reset</code></dt>
<dd>Execute device reset. </dd>
<dt><code>sector-sz</code></dt>
<dd>Query device sector size. </dd>
<dt><code>sleep </code></dt>
<dd>Put device to sleep immediately. </dd>
<dt><code>standby</code></dt>
<dd>Put device in standby mode. </dd>
<dt><code>unmask-irq</code></dt>
<dd>Toggle unmasked irqs. Omitting the on/off argument will print the current state. </dd>
<dt><code>version</code></dt>
<dd>Print version number and exit. </dd>
<dt><code>wcache</code></dt>
<dd>Toggle underlying device&#8217;s writeback cache. </dd>
</dl>
<h2>Bugs</h2>
<p>Inevitably there are some. Please report any you find. </p>
<h2>Author</h2>
<p><code>blktool</code> was written by Jeff Garzik.</p>
<h2>Availability</h2>
<p><code>blktool</code> is available over the Web on the SourceForge site at <a rel="nofollow" href="http://sourceforge.net/projects/gkernel/">http://sourceforge.net/projects/gkernel/</a></p>
