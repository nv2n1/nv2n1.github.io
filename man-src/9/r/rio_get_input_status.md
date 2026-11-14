---
title: "rio_get_input_status(9)"
name: "rio_get_input_status"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_get_input_status/"
description: "rio_get_input_status – Sends a Link-Request/Input-Status control symbol and returns link-response (if requested)."
---

<p>rio_get_input_status &#8211; Sends a Link-Request/Input-Status control symbol and returns link-response (if requested).</p>
<h2>Synopsis</h2>
<pre><code>int rio_get_input_status(struct rio_dev *rdev, int pnum, u32 *lnkresp);</code></pre>
<h2>Arguments</h2>
<p><i>rdev</i></p>
<dl>
<dd>
<dd>RIO devive to issue Input-status command</dl>
<p> <i>pnum</i></p>
<dl>
<dd>Device port number to issue the command</dl>
<p> <i>lnkresp</i></p>
<dl>
<dd>Response from a link partner</dl>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
