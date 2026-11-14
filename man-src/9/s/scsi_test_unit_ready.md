---
title: "scsi_test_unit_ready(9)"
name: "scsi_test_unit_ready"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_test_unit_ready/"
description: "scsi_test_unit_ready – test if unit is ready"
---

<p>scsi_test_unit_ready &#8211; test if unit is ready</p>
<h2>Synopsis</h2>
<pre><code>int scsi_test_unit_ready(struct scsi_device *sdev, int timeout, int retries, struct scsi_sense_hdr *sshdr_external);</code></pre>
<h2>Arguments</h2>
<p><i>sdev</i></p>
<dl>
<dd>
<dd>scsi device to change the state of.</dl>
<p> <i>timeout</i></p>
<dl>
<dd>command timeout</dl>
<p> <i>retries</i></p>
<dl>
<dd>number of retries before failing</dl>
<p> <i>sshdr_external</i></p>
<dl>
<dd>Optional pointer to struct scsi_sense_hdr for returning sense. Make sure that this is cleared before passing in.</dl>
<h2>Description</h2>
<p>Returns zero if unsuccessful or an error if TUR failed. For removable media, UNIT_ATTENTION sets -&gt;changed flag.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
