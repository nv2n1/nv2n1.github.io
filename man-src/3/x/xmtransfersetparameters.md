---
title: "xmtransfersetparameters(3)"
name: "xmtransfersetparameters"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtransfersetparameters/"
description: "XmTransferSetParameters — A toolkit function that establishes parameters to be passed by the next call to XmTransferValue"
---

<p><code>XmTransferSetParameters</code> &#8212; A toolkit function that establishes parameters to be passed by the next call to XmTransferValue</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Transfer.h&gt;
<code>void XmTransferSetParameters</code>(
<code>XtPointer transfer_id</code>,
<code>XtPointer parm</code>,
<code>int parm_fmt</code>,
<code>unsigned long parm_length</code>,
<code>Atom parm_type</code>);</pre>
<h2>Description</h2>
<p><code>XmTransferSetParameters</code> establishes a parameter definition. Your application calls <code>XmTransferSetParameters</code> just before calling <code>XmTransferValue</code>, and only if <code>XmTransferValue</code> needs to transfer a value containing a parameter.</p>
<dl COMPACT>
<dt><code>transfer_id</code></p>
<dd>Specifies a unique indentifier for the data transfer operation. The value must be the same as the value of the <code>transfer_id</code> member of the <code>XmDestinationCallbackStruct</code> passed to the <code>XmNdestinationCallback</code> procedure.</p>
<dt><i>parm</i></p>
<dd>Specifies parameters to be passed to the conversion routine (and the <code>XmNconvertCallback</code> procedures, if any) of the widget that owns the selection. The type and length of parameters are target-specific. If the target takes no parameters, the value is NULL.</p>
<dt><i>parm_fmt</i></p>
<dd>Specifies whether the data in <i>parm</i> should be viewed as a list of 8-bit, 16-bit, or 32-bit quantities. Possible values are 0 (when <i>parm</i> is NULL), 8, 16, and 32.</p>
<dt><i>parm_length</i></p>
<dd>Specifies the number of elements of data in <i>parm</i>, where each element has the number of bits specified by <i>parm_fmt</i>. When <i>parm</i> is NULL, the value is 0.</p>
<dt><i>parm_type</i></p>
<dd>Specifies the type of <i>parm</i>.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtransfersendrequest/">XmTransferSendRequest</a></code>(3), <code><a href="/docs/linux/man/3-xmtransferstartrequest/">XmTransferStartRequest</a></code>(3), and <code><a href="/docs/linux/man/3-xmtransfervalue/">XmTransferValue</a></code>(3).</p>
