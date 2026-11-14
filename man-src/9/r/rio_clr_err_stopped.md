---
title: "rio_clr_err_stopped(9)"
name: "rio_clr_err_stopped"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_clr_err_stopped/"
description: "rio_clr_err_stopped – Clears port Error-stopped states."
---

<p>rio_clr_err_stopped &#8211; Clears port Error-stopped states.</p>
<h2>Synopsis</h2>
<pre><code>int rio_clr_err_stopped(struct rio_dev *rdev, u32 pnum, u32 err_status);</code></pre>
<h2>Arguments</h2>
<p><i>rdev</i></p>
<dl>
<dd>
<dd>Pointer to RIO device control structure</dl>
<p> <i>pnum</i></p>
<dl>
<dd>Switch port number to clear errors</dl>
<p> <i>err_status</i></p>
<dl>
<dd>port error status (if 0 reads register from device)</dl>
<h2>Description</h2>
<p>TODO: Currently this routine is not compatible with recovery process specified for idt_gen3 RapidIO switch devices. It has to be reviewed to implement universal recovery process that is compatible full range off available devices. IDT gen3 switch driver now implements HW-specific error handler that issues soft port reset to the port to reset ERR_STOP bits and ackIDs.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
