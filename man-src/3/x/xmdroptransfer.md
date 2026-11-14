---
title: "xmdroptransfer(3)"
name: "xmdroptransfer"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdroptransfer/"
description: "XmDropTransfer — The DropTransfer widget class"
---

<p><code>XmDropTransfer</code> &#8212; The DropTransfer widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DragDrop.h&gt;</pre>
<h2>Description</h2>
<p>DropTransfer provides a set of resources that identifies the procedures and associated information required by the toolkit in order to process and complete a drop transaction. Clients should not explicitly create a DropTransfer widget. Instead, a client initiates a transfer by calling <code>XmDropTransferStart</code>, which initializes and returns a DropTransfer widget. If this function is called within an <code>XmNdropProc</code> callback, the actual transfers are initiated after the callback returns. Even if no data needs to be transferred, <code>XmDropTransferStart</code> needs to be called (typically with no arguments, or just setting <code>XmNtransferStatus</code>) to finish the drag and drop transaction. </p>
<p> The <code>XmNdropTransfers</code> resource specifies a transfer list that describes the requested target types for the source data. A transfer list is an array of <code>XmDropTransferEntryRec</code> structures, each of which identifies a target type. The transfer list is analogous to the MULTIPLE selections capability defined in the <i>Inter-Client Communication Conventions Manual</i> (ICCCM). </p>
<p> The DropTransfer resource, <code>XmNtransferProc</code>, specifies a transfer procedure of type XtSelectionCallbackProc that delivers the requested selection data. This procedure operates in conjunction with the underlying Xt selection capabilities and is called for each target in the transfer list. Additional target types can be requested after a transfer is initiated by calling the <code>XmDropTransferAdd</code> function.</p>
<h3>Structures</h3>
<p>An <code>XmDropTransferEntry</code> is a pointer to the following structure of type <code>XmDropTransferEntryRec</code>, which identifies a selection target associated with a given drop transaction: </p>
<pre>typedef struct
{
 XtPointer <i>client_data</i><code>;
 Atom</code> <i>target</i><code>;
} XmDropTransferEntryRec, *XmDropTransferEntry;</code></pre>
<dl COMPACT>
<dt><i>client_data</i></p>
<dd>Specifies any additional information required by this selection target</p>
<dt><i>target</i></p>
<dd>Specifies a selection target associated with the drop operation</dl>
<h3>Classes</h3>
<p>DropTransfer inherits behavior and a resource from <code>Object</code>. </p>
<p> The class pointer is <code>xmDropTransferObjectClass</code>. </p>
<p> The class name is <code>XmDropTransfer</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmDropTransfer Resource Set</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>Name</code></td>
<td><code>Class</code></td>
<td><code>Type</code></td>
<td><code>Default</code></td>
<td><code>Access</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNdropTransfers</td>
<td>XmCDropTransfers</td>
<td>XmDropTransferEntryRec *</td>
<td>NULL</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNincremental</td>
<td>XmCIncremental</td>
<td>Boolean</td>
<td>False</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNnumDropTransfers</td>
<td>XmCNumDropTransfers</td>
<td>Cardinal</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtransferProc</td>
<td>XmCTransferProc</td>
<td>XtSelectionCallbackProc</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtransferStatus</td>
<td>XmCTransferStatus</td>
<td>unsigned char</td>
<td>XmTRANSFER_SUCCESS</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
</table>
</table>
<dl COMPACT>
<dt><code>XmNdropTransfers</code></p>
<dd>Specifies the address of an array of drop transfer entry records. The drop transfer is complete when all the entries in the list have been processed.</p>
<dt><code>XmNincremental</code></p>
<dd>Specifies a Boolean value that indicates whether the transfer on the receiver side uses the Xt incremental selection transfer mechanism described in <i>X Toolkit Intrinsics&#8212;C Language Interface</i>. If the value is True, the receiver uses incremental transfer; if the value is False, the receiver uses atomic transfer.</p>
<dt><code>XmNnumDropTransfers</code></p>
<dd>Specifies the number of entries in <code>XmNdropTransfers</code>. If this resource is set to 0 at any time, the transfer is considered complete. The value of <code>XmNtransferStatus</code> determines the completion handshaking process.</p>
<dt><code>XmNtransferProc</code></p>
<dd>Specifies a procedure of type <code>XtSelectionCallbackProc</code> that delivers the requested selection values. The <i>widget</i> argument passed to this procedure is the DropTransfer widget. The selection atom passed is _MOTIF_DROP. For additional information on selection callback procedures, see <i>X Toolkit Intrinsics&#8212;C Language Interface</i>.</p>
<dt><code>XmNtransferStatus</code></p>
<dd>Specifies the current status of the drop transfer. The client updates this value when the transfer ends and communicates the value to the initiator. The possible values are</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmTRANSFER_SUCCESS</code></p>
<dd>The transfer succeeded.</p>
<dt><code>XmTRANSFER_FAILURE</code></p>
<dd>The transfer failed.</dl>
</dl>
</dl>
<h3>Inherited Resources</h3>
<p>DropTransfer inherits behavior and a resource from <code>Object</code>. For a complete description of this resource, refer to the <code>Object</code> reference page. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>Object Resource Set</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>Name</code></td>
<td><code>Class</code></td>
<td><code>Type</code></td>
<td><code>Default</code></td>
<td><code>Access</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNdestroyCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
</table>
</table>
<h2>Related Information</h2>
<p><code><a href="/docs/linux/man/3-object/">Object</a></code>(3), <code><a href="/docs/linux/man/3-xmdisplay/">XmDisplay</a></code>(3), <code><a href="/docs/linux/man/3-xmdragcontext/">XmDragContext</a></code>(3), <code><a href="/docs/linux/man/3-xmdragicon/">XmDragIcon</a></code>(3), <code><a href="/docs/linux/man/3-xmdropsite/">XmDropSite</a></code>(3), <code><a href="/docs/linux/man/3-xmdroptransferadd/">XmDropTransferAdd</a></code>(3), and <code><a href="/docs/linux/man/3-xmdroptransferstart/">XmDropTransferStart</a></code>(3).</p>
