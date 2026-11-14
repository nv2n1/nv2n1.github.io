---
title: "scsi_dev_info_list_find(9)"
name: "scsi_dev_info_list_find"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_dev_info_list_find/"
description: "scsi_dev_info_list_find – find a matching dev_info list entry."
---

<p>scsi_dev_info_list_find &#8211; find a matching dev_info list entry.</p>
<h2>Synopsis</h2>
<pre><code>struct scsi_dev_info_list *scsi_dev_info_list_find(const char *vendor, const char *model, int key);</code></pre>
<h2>Arguments</h2>
<p><i>vendor</i></p>
<dl>
<dd>
<dd>vendor string</dl>
<p> <i>model</i></p>
<dl>
<dd>model (product) string</dl>
<p> <i>key</i></p>
<dl>
<dd>specify list to use</dl>
<h2>Description</h2>
<p>Finds the first dev_info entry matching <i>vendor</i>, <i>model</i> in list specified by <i>key</i>.</p>
<h2>Return</h2>
<p>pointer to matching entry, or ERR_PTR on failure.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
