---
title: "spi_populate_tag_msg(9)"
name: "spi_populate_tag_msg"
section: "9"
letter: "s"
url: "/docs/linux/man/9-spi_populate_tag_msg/"
description: "spi_populate_tag_msg – place a tag message in a buffer"
---

<p>spi_populate_tag_msg &#8211; place a tag message in a buffer</p>
<h2>Synopsis</h2>
<pre><code>int spi_populate_tag_msg(unsigned char *msg, struct scsi_cmnd *cmd);</code></pre>
<h2>Arguments</h2>
<p><i>msg</i></p>
<dl>
<dd>
<dd>pointer to the area to place the tag</dl>
<p> <i>cmd</i></p>
<dl>
<dd>pointer to the scsi command for the tag</dl>
<h2>Notes</h2>
<p>designed to create the correct type of tag message for the particular request. Returns the size of the tag message. May return 0 if TCQ is disabled for this device.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
