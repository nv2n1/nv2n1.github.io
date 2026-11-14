---
title: "xmtransferdone(3)"
name: "xmtransferdone"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtransferdone/"
description: "XmTransferDone — A toolkit function that completes a data transfer"
---

<p><code>XmTransferDone</code> &#8212; A toolkit function that completes a data transfer</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>void XmTransferDone</code>(
<code>XtPointer transfer_id</code>,
<code>XmTransferStatus status</code>);</pre>
<h2>Description</h2>
<p><code>XmTransferDone</code> completes an already-initiated data transfer operation. An application can call this routine from an <code>XmNdestinationCallback</code> procedure or any function called as a result, including the selection procedures called as a result of calls to <code>XmTransferValue</code>. </p>
<p> The caller of <code>XmTransferDone</code> supplies an identifier for the transfer operation and an indication of the completion status. <code>XmTransferDone</code> causes any remaining transfers for the operation to be discarded.</p>
<dl COMPACT>
<dt><code>transfer_id</code></p>
<dd>Specifies a unique indentifier for the data transfer operation. The value must be the same as the value of the <code>transfer_id</code> member of the <code>XmDestinationCallbackStruct</code> passed to the <code>XmNdestinationCallback</code> procedure.</p>
<dt><i>status</i></p>
<dd>Specifies the completion status of the data transfer. Following are the possible values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmTRANSFER_DONE_SUCCEED</code></p>
<dd>The transfer was completed successfully. This status has the following additional effects:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd>For a move operation, the selection owner receives a request to convert the selection to the <code>DELETE</code> target.</p>
<dt> &bull;</p>
<dd>If a <code>TRANSACT</code> operation is in progress, the owner receives a request to commit the transaction.</p>
<dt> &bull;</p>
<dd>If a <code>PERSIST</code> or <code>_MOTIF_SNAPSHOT</code> operation is in progress, the owner receives a notification that the operation is finished.</p>
<dt> &bull;</p>
<dd>The widget class destination procedure is not called.</dl>
</dl>
<dt><code>XmTRANSFER_DONE_FAIL</code></p>
<dd>The transfer was completed unsuccessfully. This status has the following additional effects:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd>For a move operation, the selection owner does not receive a request to convert the selection to the <code>DELETE</code> target.</p>
<dt> &bull;</p>
<dd>For a drag and drop operation, the DropTransfer&#8217;s <code>XmNtransferStatus</code> is set to <code>XmTRANSFER_FAILURE</code>.</p>
<dt> &bull;</p>
<dd>If a <code>TRANSACT</code> operation is in progress, the owner receives a request to abort the transaction.</p>
<dt> &bull;</p>
<dd>If a <code>PERSIST</code> or <code>_MOTIF_SNAPSHOT</code> operation is in progress, the owner receives a notification that the operation is finished.</p>
<dt> &bull;</p>
<dd>The widget class destination procedure is not called.</dl>
</dl>
<dt><code>XmTRANSFER_DONE_CONTINUE</code></p>
<dd>This status has the same effect as <code>XmTRANSFER_DONE_SUCCEED</code>, except that if a <code>PERSIST</code> or <code>_MOTIF_SNAPSHOT</code> operation is in progress, the owner does not receive a notification that the operation is finished.</p>
<dt><code>XmTRANSFER_DONE_DEFAULT</code></p>
<dd>The widget class destination procedure is called. Further effects depend on the actions of that procedure.</dl>
</dl>
</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtransfersendrequest/">XmTransferSendRequest</a></code>(3), <code><a href="/docs/linux/man/3-xmtransferstartrequest/">XmTransferStartRequest</a></code>(3), <code><a href="/docs/linux/man/3-xmtransferstartrequest/">XmTransferStartRequest</a></code>(3), and <code><a href="/docs/linux/man/3-xmtransfervalue/">XmTransferValue</a></code>(3).</p>
