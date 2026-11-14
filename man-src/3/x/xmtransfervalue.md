---
title: "xmtransfervalue(3)"
name: "xmtransfervalue"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmtransfervalue/"
description: "XmTransferValue — A toolkit function that transfers data to a destination"
---

<p><code>XmTransferValue</code> &#8212; A toolkit function that transfers data to a destination</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>void XmTransferValue</code>(
<code>XtPointer transfer_id</code>,
<code>Atom target</code>,
<code>XtCallbackProc proc</code>,
<code>XtPointer client_data</code>,
<code>Time time</code>);</pre>
<h2>Description</h2>
<p><code>XmTransferValue</code> converts a selection, transferring any data from the selection owner, in the context of an already-initiated data transfer operation. An application can call this routine from an <code>XmNdestinationCallback</code> procedure or any function called as a result. </p>
<p> The caller of <code>XmTransferValue</code> supplies the target to which the selection is converted. The caller also supplies a callback procedure to handle the data that results from the conversion.</p>
<dl COMPACT>
<dt><code>transfer_id</code></p>
<dd>Specifies a unique indentifier for the data transfer operation. The value must be the same as the value of the <code>transfer_id</code> member of the <code>XmDestinationCallbackStruct</code> passed to the <code>XmNdestinationCallback</code> procedure.</p>
<dt><i>target</i></p>
<dd>Specifies the target to which the selection is to be converted.</p>
<dt><i>proc</i></p>
<dd>Specifies a callback procedure to be invoked when the selection has been converted and the data, if any, is available. This procedure is responsible for inserting or otherwise handling any data transferred. The procedure can also terminate the data transfer by calling <code>XmTransferDone</code>. The <i>proc</i> receives three arguments:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd>The widget that requested the conversion</p>
<dt> &bull;</p>
<dd>The value of the <i>client_data</i> argument</p>
<dt> &bull;</p>
<dd>A pointer to an <code>XmSelectionCallbackStruct</code></dl>
</dl>
<dd>This procedure can be called before or after <code>XmTransferValue</code> returns.</p>
<dt><i>client_data</i></p>
<dd>Specifies data to be passed to the callback procedure (the value of the <i>proc</i> argument) when the selection has been converted.</p>
<dt><i>time</i></p>
<dd>Specifies the time of the <code>XEvent</code> that triggered the data transfer. You should typically set this field to <code>XtLastTimestampProcessed</code>.</dl>
<p> The callback procedure (the value of the <i>proc</i> argument) receives a pointer to an <code>XmSelectionCallbackStruct</code>, which has the following definition: </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent *<i>event</i>;
 Atom <i>selection</i>;
 Atom <i>target</i>;
 Atom <i>type</i>;
 XtPointer <i>transfer_id</i>;
 int <i>flags</i>;
 int <i>remaining</i>;
 XtPointer <i>value</i>;
 unsigned long <i>length</i>;
 int <i>format</i>;
} XmSelectionCallbackStruct;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked.</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback. It can be NULL.</p>
<dt><i>selection</i></p>
<dd>Specifies the selection that has been converted.</p>
<dt><i>target</i></p>
<dd>Specifies the target to which <code>XmTransferValue</code> requested conversion. The value is the same as the value of the <i>target</i> argument to <code>XmTransferValue</code>.</p>
<dt><i>type</i></p>
<dd>Specifies the type of the selection value. This is not the target, but the type used to represent the target. The value <code>XT_CONVERT_FAIL</code> means that the selection owner did not respond to the conversion request within the Intrinsics selection timeout interval.</p>
<dt><code>transfer_id</code></p>
<dd>Specifies a unique indentifier for the data transfer operation. The value is the same as the value of the <code>transfer_id</code> argument to <code>XmTransferValue</code>.</p>
<dt><i>flags</i></p>
<dd>This member is currently unused. The value is always <code>XmSELECTION_DEFAULT</code>.</p>
<dt><i>remaining</i></p>
<dd>Indicates the number of transfers remaining for the operation specified by <code>transfer_id</code>.</p>
<dt><i>value</i></p>
<dd>Represents the data transferred by this request. The application is responsible for freeing the value by calling <code>XtFree</code>.</p>
<dt><i>length</i></p>
<dd>Indicates the number of elements of data in <i>value</i>, where each element has the size symbolized by <i>format</i>. If <i>value</i> is NULL, <i>length</i> is 0.</p>
<dt><i>format</i></p>
<dd>Indicates whether the data in <i>value</i> should be viewed as a list of <i>char</i>, <i>short</i>, or <i>long</i> quantities. Possible values are 8 (for a list of <i>char</i>), 16 (for a list of <i>short</i>), or 32 (for a list of <i>long</i>).</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmtransfersetparameters/">XmTransferSetParameters</a></code>(3), <code><a href="/docs/linux/man/3-xmtransfersendrequest/">XmTransferSendRequest</a></code>(3), and <code><a href="/docs/linux/man/3-xmtransferstartrequest/">XmTransferStartRequest</a></code>(3).</p>
