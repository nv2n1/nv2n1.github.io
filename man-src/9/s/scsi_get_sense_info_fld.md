---
title: "scsi_get_sense_info_fld(9)"
name: "scsi_get_sense_info_fld"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_get_sense_info_fld/"
description: "scsi_get_sense_info_fld – get information field from sense data (either fixed or descriptor format)"
---

<p>scsi_get_sense_info_fld &#8211; get information field from sense data (either fixed or descriptor format)</p>
<h2>Synopsis</h2>
<pre><code>int scsi_get_sense_info_fld(const u8 *sense_buffer, int sb_len, u64 *info_out);</code></pre>
<h2>Arguments</h2>
<p><i>sense_buffer</i></p>
<dl>
<dd>
<dd>byte array of sense data</dl>
<p> <i>sb_len</i></p>
<dl>
<dd>number of valid bytes in sense_buffer</dl>
<p> <i>info_out</i></p>
<dl>
<dd>pointer to 64 integer where 8 or 4 byte information field will be placed if found.</dl>
<h2>Description</h2>
<p>Return value: 1 if information field found, 0 if not found.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
