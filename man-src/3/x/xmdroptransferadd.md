---
title: "xmdroptransferadd(3)"
name: "xmdroptransferadd"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdroptransferadd/"
description: "XmDropTransferAdd — A Drag and Drop function that enables additional drop transfer entries to be processed after initiating a drop transfer"
---

<p><code>XmDropTransferAdd</code> &#8212; A Drag and Drop function that enables additional drop transfer entries to be processed after initiating a drop transfer</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DragDrop.h&gt;
<code>void XmDropTransferAdd</code>(
<code>Widget drop_transfer</code>,
<code>XmDropTransferEntryRec *transfers</code>,
<code>Cardinal num_transfers</code>);</pre>
<h2>Description</h2>
<p><code>XmDropTransferAdd</code> identifies a list of additional drop transfer entries to be processed after a drop transfer is started.</p>
<dl COMPACT>
<dt><i>drop_transfer</i></p>
<dd>Specifies the ID of the DropTransfer widget returned by <code>XmDropTransferStart</code></p>
<dt><i>transfers</i></p>
<dd>Specifies the additional drop transfer entries that the receiver wants processed</p>
<dt><i>num_transfers</i></p>
<dd>Specifies the number of items in the <i>transfers</i> array</dl>
<p> For a complete definition of DropTransfer and its associated resources, see <code><a href="/docs/linux/man/3-xmdroptransfer/">XmDropTransfer</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmdragcontext/">XmDragContext</a></code>(3), <code><a href="/docs/linux/man/3-xmdroptransfer/">XmDropTransfer</a></code>(3), and <code><a href="/docs/linux/man/3-xmdroptransferstart/">XmDropTransferStart</a></code>(3).</p>
