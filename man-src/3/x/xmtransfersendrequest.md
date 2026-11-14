---
title: "xmtransfersendrequest(3)"
name: "xmtransfersendrequest"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtransfersendrequest/"
description: "XmTransferSendRequest — A toolkit function that transfers a MULTIPLE request"
---

<p><code>XmTransferSendRequest</code> &#8212; A toolkit function that transfers a MULTIPLE request</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Transfer.h&gt;
<code>void XmTransferSendRequest</code>(
<code>XtPointer transfer_id</code>,
<code>Time time</code>);</pre>
<h2>Description</h2>
<p><code>XmTransferSendRequest</code> marks the end of a MULTIPLE request started by <code>XmTransferStartRequest</code>.</p>
<dl COMPACT>
<dt><code>transfer_id</code></p>
<dd>Specifies a unique indentifier for the data transfer operation.</p>
<dt><i>time</i></p>
<dd>Specifies the time of the <code>XEvent</code> that triggered the data transfer. You should typically set this field to <code>XtLastTimestampProcessed</code>.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtransfersetparameters/">XmTransferSetParameters</a></code>(3), <code><a href="/docs/linux/man/3-xmtransferstartrequest/">XmTransferStartRequest</a></code>(3), and <code><a href="/docs/linux/man/3-xmtransfervalue/">XmTransferValue</a></code>(3).</p>
