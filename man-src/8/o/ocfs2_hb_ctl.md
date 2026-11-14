---
title: "ocfs2_hb_ctl(8)"
name: "ocfs2_hb_ctl"
section: "8"
letter: "o"
url: "/docs/linux/man/8-ocfs2_hb_ctl/"
description: "ocfs2_hb_ctl – Starts and stops the OCFS2 heartbeat on a given device."
---

<p>ocfs2_hb_ctl &#8211; Starts and stops the <i>OCFS2</i> heartbeat on a given device.</p>
<h2>Synopsis</h2>
<p><code>ocfs2_hb_ctl</code> <code>-S</code> <code>-d</code> <i>device</i> <i>service</i><br />
 <code>ocfs2_hb_ctl</code> <code>-S</code> <code>-u</code> <i>uuid</i> <i>service</i><br />
 <code>ocfs2_hb_ctl</code> <code>-K</code> <code>-d</code> <i>device</i> <i>service</i><br />
 <code>ocfs2_hb_ctl</code> <code>-K</code> <code>-u</code> <i>uuid</i> <i>service</i><br />
 <code>ocfs2_hb_ctl</code> <code>-I</code> <code>-d</code> <i>device</i><br />
 <code>ocfs2_hb_ctl</code> <code>-I</code> <code>-u</code> <i>uuid</i><br />
 <code>ocfs2_hb_ctl</code> <code>-P</code> <code>-d</code> <i>device</i> [<code>-n</code> <i>io_priority</i>]<br />
 <code>ocfs2_hb_ctl</code> <code>-P</code> <code>-u</code> <i>uuid</i> [<code>-n</code> <i>io_priority</i>]<br />
 <code>ocfs2_hb_ctl</code> <code>-h</code><i> </p>
<h2>Description</h2>
<p><code>ocfs2_hb_ctl</code> starts and stops the heartbeat on a <i>OCFS2</i> device. <code>Users are strongly urged not to use this tool directly</code>. It is automatically invoked by <i>mount.ocfs2</i> and other tools that require heartbeat notifications. The tools accepts devices to be specified by its name or its uuid. Service denotes the application that is requesting the heartbeat notification. </p>
<h2>Options</h2>
<dl>
<dt><code>-S</code></p>
<dd>Starts the heartbeat. </p>
<dt><code>-K</code></p>
<dd>Stops the heartbeat. </p>
<dt><code>-I</code></p>
<dd>Prints the heartbeat reference counts for that heartbeat region. </p>
<dt><code>-d</code></p>
<dd>Specify region by device name. </p>
<dt><code>-u</code></p>
<dd>Specify region by device uuid. </p>
<dt><code>-n</code></p>
<dd>Adjust IO priority for the heartbeat thread. This option calls the <code>ionice</code> tool to set its IO scheduling class to realtime with scheduling class data as provided. This option is usable only with the <code>O2CB</code> cluster stack. </p>
<dt><code>-h</code></p>
<dd>Displays help and exit. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mkfs-ocfs2/">mkfs.ocfs2</a>(8)</code> <code><a href="/docs/linux/man/8-fsck-ocfs2/">fsck.ocfs2</a>(8)</code> <code><a href="/docs/linux/man/8-tunefs-ocfs2/">tunefs.ocfs2</a>(8)</code> <code><a href="/docs/linux/man/8-mounted-ocfs2/">mounted.ocfs2</a>(8)</code> <code><a href="/docs/linux/man/8-ocfs2console/">ocfs2console</a>(8)</code> <code><a href="/docs/linux/man/8-debugfs-ocfs2/">debugfs.ocfs2</a>(8)</code> </p>
<h2>Authors</h2>
<p>Oracle Corporation</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2004, 2009 Oracle. All rights reserved.</p>
