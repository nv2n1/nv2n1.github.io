---
title: "scsi_dev_info_list_add(9)"
name: "scsi_dev_info_list_add"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_dev_info_list_add/"
description: "scsi_dev_info_list_add – add one dev_info list entry."
---

<p>scsi_dev_info_list_add &#8211; add one dev_info list entry.</p>
<h2>Synopsis</h2>
<pre><code>int scsi_dev_info_list_add(int compatible, char *vendor, char *model, char *strflags, int flags);</code></pre>
<h2>Arguments</h2>
<p><i>compatible</i></p>
<dl>
<dd>
<dd>if true, null terminate short strings. Otherwise space pad.</dl>
<p> <i>vendor</i></p>
<dl>
<dd>vendor string</dl>
<p> <i>model</i></p>
<dl>
<dd>model (product) string</dl>
<p> <i>strflags</i></p>
<dl>
<dd>integer string</dl>
<p> <i>flags</i></p>
<dl>
<dd>if strflags NULL, use this flag value</dl>
<h2>Description</h2>
<p>Create and add one dev_info entry for <i>vendor</i>, <i>model</i>, <i>strflags</i> or <i>flag</i>. If <i>compatible</i>, add to the tail of the list, do not space pad, and set devinfo-&gt;compatible. The scsi_static_device_list entries are added with <i>compatible</i> 1 and <i>clfags</i> NULL.</p>
<h2>Return</h2>
<p>0 OK, -error on failure.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
