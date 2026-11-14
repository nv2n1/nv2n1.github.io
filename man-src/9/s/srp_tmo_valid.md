---
title: "srp_tmo_valid(9)"
name: "srp_tmo_valid"
section: "9"
letter: "s"
url: "/docs/linux/man/9-srp_tmo_valid/"
description: "srp_tmo_valid – check timeout combination validity"
---

<p>srp_tmo_valid &#8211; check timeout combination validity</p>
<h2>Synopsis</h2>
<pre><code>int srp_tmo_valid(int reconnect_delay, int fast_io_fail_tmo, int dev_loss_tmo);</code></pre>
<h2>Arguments</h2>
<p><i>reconnect_delay</i></p>
<dl>
<dd>
<dd>Reconnect delay in seconds.</dl>
<p> <i>fast_io_fail_tmo</i></p>
<dl>
<dd>Fast I/O fail timeout in seconds.</dl>
<p> <i>dev_loss_tmo</i></p>
<dl>
<dd>Device loss timeout in seconds.</dl>
<h2>Description</h2>
<p>The combination of the timeout parameters must be such that SCSI commands are finished in a reasonable time. Hence do not allow the fast I/O fail timeout to exceed SCSI_DEVICE_BLOCK_MAX_TIMEOUT nor allow dev_loss_tmo to exceed that limit if failing I/O fast has been disabled. Furthermore, these parameters must be such that multipath can detect failed paths timely. Hence do not allow all three parameters to be disabled simultaneously.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
