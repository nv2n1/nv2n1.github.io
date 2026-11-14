---
title: "scsi_dev_info_list_add_str(9)"
name: "scsi_dev_info_list_add_str"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_dev_info_list_add_str/"
description: "scsi_dev_info_list_add_str – parse dev_list and add to the scsi_dev_info_list."
---

<p>scsi_dev_info_list_add_str &#8211; parse dev_list and add to the scsi_dev_info_list.</p>
<h2>Synopsis</h2>
<pre><code>int scsi_dev_info_list_add_str(char *dev_list);</code></pre>
<h2>Arguments</h2>
<p><i>dev_list</i></p>
<dl>
<dd>
<dd>string of device flags to add</dl>
<h2>Description</h2>
<p>Parse dev_list, and add entries to the scsi_dev_info_list. dev_list is of the form &#8220;vendor:product:flag,vendor:product:flag&#8221;. dev_list is modified via strsep. Can be called for command line addition, for proc or mabye a sysfs interface.</p>
<h2>Return</h2>
<p>0 if OK, -error on failure.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
