---
title: "srp_start_tl_fail_timers(9)"
name: "srp_start_tl_fail_timers"
section: "9"
letter: "s"
url: "/docs/linux/man/9-srp_start_tl_fail_timers/"
description: "srp_start_tl_fail_timers – start the transport layer failure timers"
---

<p>srp_start_tl_fail_timers &#8211; start the transport layer failure timers</p>
<h2>Synopsis</h2>
<pre><code>void srp_start_tl_fail_timers(struct srp_rport *rport);</code></pre>
<h2>Arguments</h2>
<p><i>rport</i></p>
<dl>
<dd>
<dd>SRP target port.</dl>
<h2>Description</h2>
<p>Start the transport layer fast I/O failure and device loss timers. Do not modify a timer that was already started.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
