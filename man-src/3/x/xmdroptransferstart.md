---
title: "xmdroptransferstart(3)"
name: "xmdroptransferstart"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdroptransferstart/"
description: "XmDropTransferStart — A Drag and Drop function that initiates a drop transfer"
---

<p><code>XmDropTransferStart</code> &#8212; A Drag and Drop function that initiates a drop transfer</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DragDrop.h&gt;
<code>Widget XmDropTransferStart</code>(
<code>Widget widget</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmDropTransferStart</code> initiates a drop transfer and uses the specified argument list to initialize an <code>XmDropTransfer</code> object. The DropTransfer object can be manipulated with <code>XtSetValues</code> and <code>XtGetValues</code> until the last call to the <code>XmNtransferProc</code> procedure is made. After that point, the result of using the widget pointer is undefined. The DropTransfer object is freed by the toolkit when a transfer is complete.</p>
<dl COMPACT>
<dt><i>widget</i></dt>
<dd>Specifies the ID of the DragContext widget associated with the transaction</dd>
<dt><i>arglist</i></dt>
<dd>Specifies the argument list</dd>
<dt><i>argcount</i></dt>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>)</dd></dl>
<p> For a complete definition of DropTransfer and its associated resources, see <code><a href="/docs/linux/man/3-xmdroptransfer/">XmDropTransfer</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the ID of the DropTransfer widget.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmdragcontext/">XmDragContext</a></code>(3), <code><a href="/docs/linux/man/3-xmdroptransfer/">XmDropTransfer</a></code>(3), and <code><a href="/docs/linux/man/3-xmdroptransferadd/">XmDropTransferAdd</a></code>(3).</p>
