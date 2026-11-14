---
title: "proc_scsi_write(9)"
name: "proc_scsi_write"
section: "9"
letter: "p"
url: "/docs/linux/man/9-proc_scsi_write/"
description: "proc_scsi_write – handle writes to /proc/scsi/scsi"
---

<p>proc_scsi_write &#8211; handle writes to /proc/scsi/scsi</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ssize_t proc_scsi_write(struct file&nbsp;<wbr>*&nbsp;<wbr></code><i>file</i><code>, const char&nbsp;<wbr>__user&nbsp;<wbr>*&nbsp;<wbr></code><i>buf</i><code>, size_t&nbsp;<wbr></code><i>length</i><code>, loff_t&nbsp;<wbr>*&nbsp;<wbr></code><i>ppos</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>file</i></p>
<dl>
<dd>
<dd>not used</dl>
<p> <i>buf</i></p>
<dl>
<dd>buffer to write</dl>
<p> <i>length</i></p>
<dl>
<dd>length of buf, at most PAGE_SIZE</dl>
<p> <i>ppos</i></p>
<dl>
<dd>not used</dl>
<h2>Description</h2>
<p>this provides a legacy mechanism to add or remove devices by Host, Channel, ID, and Lun. To use, &#8220;echo &#8216;scsi add-single-device 0 1 2 3&#8217; &gt; /proc/scsi/scsi&#8221; or &#8220;echo &#8216;scsi remove-single-device 0 1 2 3&#8217; &gt; /proc/scsi/scsi&#8221; with &#8220;0 1 2 3&#8221; replaced by the Host, Channel, Id, and Lun.</p>
<h2>Note</h2>
<p>this seems to be aimed at parallel SCSI. Most modern busses (USB, SATA, Firewire, Fibre Channel, etc) dynamically assign these values to provide a unique identifier and nothing more.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
