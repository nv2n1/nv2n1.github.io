---
title: "z8530_interrupt(9)"
name: "z8530_interrupt"
section: "9"
letter: "z"
url: "/docs/linux/man/9-z8530_interrupt/"
description: "z8530_interrupt – Handle an interrupt from a Z8530"
---

<p>z8530_interrupt &#8211; Handle an interrupt from a Z8530</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>irqreturn_t z8530_interrupt(int&nbsp;<wbr></code><i>irq</i><code>, void&nbsp;<wbr>*&nbsp;<wbr></code><i>dev_id</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>irq</i></p>
<dl>
<dd>
<dd>Interrupt number</dl>
<p> <i>dev_id</i></p>
<dl>
<dd>The Z8530 device that is interrupting.</dl>
<h2>Description</h2>
<p>A Z85[2]30 device has stuck its hand in the air for attention. We scan both the channels on the chip for events and then call the channel specific call backs for each channel that has events. We have to use callback functions because the two channels can be in different modes. </p>
<p> Locking is done for the handlers. Note that locking is done at the chip level (the 5uS delay issue is per chip not per channel). c-&gt;lock for both channels points to dev-&gt;lock</p>
<h2>Author</h2>
<p><code>Alan Cox</code> &lt;alan [at] lxorguk.ukuu.org.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
