---
title: "xmtransferstartrequest(3)"
name: "xmtransferstartrequest"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtransferstartrequest/"
description: "XmTransferStartRequest — A toolkit function that begins a MULTIPLE transfer"
---

<p><code>XmTransferStartRequest</code> &#8212; A toolkit function that begins a MULTIPLE transfer</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Transfer.h&gt;
<code>void XmTransferStartRequest</code>(
<code>XtPointer transfer_id</code>);</pre>
<h2>Description</h2>
<p><code>XmTransferStartRequest</code> begins a <code>MULTIPLE</code> request. The <code>MULTIPLE</code> request may contain one or more calls to <code>XmTransferValue</code>. Your application concludes a <code>MULTIPLE</code> request by calling <code>XmTransferSendRequest</code>. </p>
<p> <code>XmTransferStartRequest</code> is typically called by a destination callback or by a transfer procedure.</p>
<dl COMPACT>
<dt><code>transfer_id</code></p>
<dd>Specifies a unique indentifier for the data transfer operation. You should use the <code>transfer_id</code> passed in the <code>XmDestinationCallbackStruct</code> or <code>XmSelectionCallbackStruct</code>.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtransfersetparameters/">XmTransferSetParameters</a></code>(3), <code><a href="/docs/linux/man/3-xmtransfersendrequest/">XmTransferSendRequest</a></code>(3), and <code><a href="/docs/linux/man/3-xmtransfervalue/">XmTransferValue</a></code>(3).</p>
