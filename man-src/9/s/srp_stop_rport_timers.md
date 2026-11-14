---
title: "srp_stop_rport_timers(9)"
name: "srp_stop_rport_timers"
section: "9"
letter: "s"
url: "/docs/linux/man/9-srp_stop_rport_timers/"
description: "srp_stop_rport_timers – stop the transport layer recovery timers"
---

<p>srp_stop_rport_timers &#8211; stop the transport layer recovery timers</p>
<h2>Synopsis</h2>
<pre><code>void srp_stop_rport_timers(struct srp_rport *rport);</code></pre>
<h2>Arguments</h2>
<p><i>rport</i></p>
<dl>
<dd>
<dd>SRP remote port for which to stop the timers.</dl>
<h2>Description</h2>
<p>Must be called after <code>srp_remove_host</code> and <code>scsi_remove_host</code>. The caller must hold a reference on the rport (rport-&gt;dev) and on the SCSI host (rport-&gt;dev.parent).</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
