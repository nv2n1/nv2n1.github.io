---
title: "xmdragcontext(3)"
name: "xmdragcontext"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdragcontext/"
description: "XmDragContext — The DragContext widget class"
---

<p><code>XmDragContext</code> &#8212; The DragContext widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DragDrop.h&gt;</pre>
<h2>Description</h2>
<p>DragContexts are special widgets used in drag and drop transactions. A DragContext is implemented as a widget, but a client does not explicitly create a DragContext widget. Instead, a client initiates a drag and drop transaction by calling <code>XmDragStart</code>, and this routine initializes and returns a DragContext widget. There is a unique DragContext for each drag operation. The toolkit frees a DragContext when a transaction is complete; therefore, an application programmer should not explicitly destroy a DragContext. </p>
<p> Initiator and receiver clients both use DragContexts to track the state of a transaction. When the initiator and receiver of a transaction are in the same client, they share the same DragContext instance. If they are in different clients, there are two separate DragContexts. In this case, the initiator calls <code>XmDragStart</code> and the toolkit provides a DragContext for the receiver client. The only resources pertinent to the receiver are <code>XmNexportTargets</code> and <code>XmNnumExportTargets</code>. These can both be passed as arguments to the <code>XmDropSiteRetrieve</code> function to obtain information about the current drop site. </p>
<p> In general, in order to receive data, a drop site must share at least one target type and operation in common with a drag source. The DragContext resource, <code>XmNexportTargets</code>, identifies the selection targets for the drag source. These export targets are compared with the <code>XmNimportTargets</code> resource list specified by a drop site. The DragContext resource, <code>XmNdragOperations</code>, identifies the valid operations that can be applied to the source data by the initiator. The drop site counterpart resource is <code>XmNdropSiteOperations</code>, which indicates a drop site&#8217;s supported operations. </p>
<p> A client uses DragIcon widgets to define the drag-over animation effects associated with a given drag and drop transaction. An initiator specifies a set of drag icons, selects a blending model, and sets foreground and background cursor colors with DragContext resources. </p>
<p> The type of drag-over visual used to represent a drag operation depends on the drag protocol style. In preregister mode, the server is grabbed, and either a cursor or a pixmap may be used as a drag-over visual. In dynamic mode, drag-over visuals must be implemented with the X cursor. If the resulting drag protocol style is Drop Only or None and the <code>XmNdragInitiatorProtocolStyle</code> is <code>XmDRAG_DYNAMIC</code> or <code>XmDRAG_PREFER_DYNAMIC</code>, then a dynamic visual style (cursor) is used. Otherwise, a preregister visual style is used.</p>
<h3>Classes</h3>
<p>DragContext inherits behavior and resources from <code>Core</code>. </p>
<p> The class pointer is <code>xmDragContextClass</code>. </p>
<p> The class name is <code>XmDragContext</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using XtSetValues (S), retrieved by using XtGetValues (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmDragContext Resource Set</code>
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
<td>XmNblendModel</td>
<td>XmCBlendModel</td>
<td>unsigned char</td>
<td>XmBLEND_ALL</td>
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
<td>XmNclientData</td>
<td>XmCClientData</td>
<td>XtPointer</td>
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
<td>XmNconvertProc</td>
<td>XmCConvertProc</td>
<td>XtConvertSelectionIncrProc</td>
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
<td>XmNcursorBackground</td>
<td>XmCCursorBackground</td>
<td>Pixel</td>
<td>dynamic</td>
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
<td>XmNcursorForeground</td>
<td>XmCCursorForeground</td>
<td>Pixel</td>
<td>dynamic</td>
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
<td>XmNdragDropFinishCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
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
<td>XmNdragMotionCallback</td>
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
<tr VALIGN=top>
<td>XmNdragOperations</td>
<td>XmCDragOperations</td>
<td>unsigned char</td>
<td>XmDROP_COPY | XmDROP_MOVE</td>
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
<tr VALIGN=top>
<td>XmNdropFinishCallback</td>
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
<tr VALIGN=top>
<td>XmNdropSiteEnterCallback</td>
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
<tr VALIGN=top>
<td>XmNdropSiteLeaveCallback</td>
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
<tr VALIGN=top>
<td>XmNdropStartCallback</td>
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
<tr VALIGN=top>
<td>XmNexportTargets</td>
<td>XmCExportTargets</td>
<td>Atom *</td>
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
<td>XmNinvalidCursorForeground</td>
<td>XmCCursorForeground</td>
<td>Pixel</td>
<td>dynamic</td>
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
<td>XmNnoneCursorForeground</td>
<td>XmCCursorForeground</td>
<td>Pixel</td>
<td>dynamic</td>
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
<td>XmNnumExportTargets</td>
<td>XmCNumExportTargets</td>
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
<td>XmNoperationChangedCallback</td>
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
<tr VALIGN=top>
<td>XmNoperationCursorIcon</td>
<td>XmCOperationCursorIcon</td>
<td>Widget</td>
<td>dynamic</td>
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
<td>XmNsourceCursorIcon</td>
<td>XmCSourceCursorIcon</td>
<td>Widget</td>
<td>dynamic</td>
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
<td>XmNsourcePixmapIcon</td>
<td>XmCSourcePixmapIcon</td>
<td>Widget</td>
<td>dynamic</td>
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
<td>XmNstateCursorIcon</td>
<td>XmCStateCursorIcon</td>
<td>Widget</td>
<td>dynamic</td>
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
<td>XmNtopLevelEnterCallback</td>
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
<tr VALIGN=top>
<td>XmNtopLevelLeaveCallback</td>
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
<tr VALIGN=top>
<td>XmNvalidCursorForeground</td>
<td>XmCCursorForeground</td>
<td>Pixel</td>
<td>dynamic</td>
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
<dt><code>XmNblendModel</code></p>
<dd>Specifies which combination of DragIcons are blended to produce a drag-over visual.</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmBLEND_ALL</code></p>
<dd>Blends all three DragIcons: the source, state and operation icons. The icons are layered from top to bottom with the operation icon on top and the source icon on the bottom. The hotspot is derived from the state icon.</p>
<dt><code>XmBLEND_STATE_SOURCE</code></p>
<dd>Blends the state and source icons only. The hotspot is derived from the state icon.</p>
<dt><code>XmBLEND_JUST_SOURCE</code></p>
<dd>Specifies that only the source icon is used, which the initiator updates as required.</p>
<dt><code>XmBLEND_NONE</code></p>
<dd>Specifies that no drag-over visual is generated. The client tracks the drop site status through callback routines and updates the drag-over visuals as necessary.</dl>
</dl>
<dt><code>XmNclientData</code></p>
<dd>Specifies the client data to be passed to <code>XmNconvertProc</code> when it is invoked.</p>
<dt><code>XmNconvertProc</code></p>
<dd>If <code>XmNincremental</code> is True, specifies a procedure of type <code>XtConvertSelectionIncrProc</code> that converts the source data to the format(s) requested by the receiver client. The <i>widget</i> argument passed to this procedure is the DragContext widget. The selection atom passed is _MOTIF_DROP. If <code>XmNincremental</code> is False, the procedure is an <code>XtConvertSelectionProc</code>, and should ignore the <i>max_length</i>, <i>client_data</i>, and <i>request_id</i> arguments and should handle the conversion atomically. Data returned by <code>XmNconvertProc</code> must be allocated using <code>XtMalloc</code>, and will be freed automatically by the toolkit after the transfer. For additional information on selection conversion procedures, see <i>X Toolkit Intrinsics&#8212;C Language Interface</i>.</p>
<dt><code>XmNcursorBackground</code></p>
<dd>Specifies the background pixel value of the cursor.</p>
<dt><code>XmNcursorForeground</code></p>
<dd>Specifies the foreground pixel value of the cursor when the state icon is not blended. This resource defaults to the foreground color of the widget passed to the <code>XmDragStart</code> function.</p>
<dt><code>XmNdragDropFinishCallback</code></p>
<dd>Specifies the list of callbacks that are called when the transaction is completed. The type of the structure whose address is passed to this callback is <code>XmDragDropFinishCallbackStruct</code>. The reason sent by the callback is <code>XmCR_DRAG_DROP_FINISH</code>.</p>
<dt><code>XmNdragMotionCallback</code></p>
<dd>Specifies the list of callbacks that are invoked when the pointer moves. The type of structure whose address is passed to this callback is <code>XmDragMotionCallbackStruct</code>. The reason sent by the callback is <code>XmCR_DRAG_MOTION</code>.</p>
<dt><code>XmNdragOperations</code></p>
<dd>Specifies the set of valid operations associated with an initiator client for a drag transaction. This resource is a bit mask that is formed by combining one or more of the following values using a bitwise operation such as inclusive OR (|): <code>XmDROP_COPY</code>, <code>XmDROP_LINK</code>, <code>XmDROP_MOVE</code>. The value <code>XmDROP_NOOP</code> for this resource indicates that no operations are valid. For Text and TextField widgets, this resource is set to <code>XmDROP_COPY</code> | <code>XmDROP_MOVE</code>; for List widgets, it is set to <code>XmDROP_COPY</code>.</p>
<dt><code>XmNdropFinishCallback</code></p>
<dd>Specifies the list of callbacks that are invoked when the drop is completed. The type of the structure whose address is passed to this callback is <code>XmDropFinishCallbackStruct</code>. The reason sent by the callback is <code>XmCR_DROP_FINISH</code>.</p>
<dt><code>XmNdropSiteEnterCallback</code></p>
<dd>Specifies the list of callbacks that are invoked when the pointer enters a drop site. The type of the structure whose address is passed to this callback is <code>XmDropSiteEnterCallbackStruct</code>. The reason sent by the callback is <code>XmCR_DROP_SITE_ENTER</code>.</p>
<dt><code>XmNdropSiteLeaveCallback</code></p>
<dd>Specifies the list of callbacks that are invoked when the pointer leaves a drop site. The type of the structure whose address is passed to this callback is <code>XmDropSiteLeaveCallbackStruct</code>. The reason sent by the callback is <code>XmCR_DROP_SITE_LEAVE</code>.</p>
<dt><code>XmNdropStartCallback</code></p>
<dd>Specifies the list of callbacks that are invoked when a drop is initiated. The type of the structure whose address is passed to this callback is <code>XmDropStartCallbackStruct</code>. The reason sent by the callback is <code>XmCR_DROP_START</code>.</p>
<dt><code>XmNexportTargets</code></p>
<dd>Specifies the list of target atoms associated with this source. This resource identifies the selection targets this source can be converted to.</p>
<dt><code>XmNincremental</code></p>
<dd>Specifies a Boolean value that indicates whether the transfer on the initiator side uses the Xt incremental selection transfer mechanism described in <i>X Toolkit Intrinsics&#8212;C Language Interface</i>. If the value is True, the initiator uses incremental transfer; if the value is False, the initiator uses atomic transfer.</p>
<dt><code>XmNinvalidCursorForeground</code></p>
<dd>Specifies the foreground pixel value of the cursor when the state is invalid. This resource defaults to the value of the <code>XmNcursorForeground</code> resource.</p>
<dt><code>XmNnoneCursorForeground</code></p>
<dd>Specifies the foreground pixel value of the cursor when the state is none. This resource defaults to the value of the <code>XmNcursorForeground</code> resource.</p>
<dt><code>XmNnumExportTargets</code></p>
<dd>Specifies the number of entries in the list of export targets.</p>
<dt><code>XmNoperationChangedCallback</code></p>
<dd>Specifies the list of callbacks that are invoked when the drag is started and when the user requests that a different operation be applied to the drop. The type of the structure whose address is passed to this callback is <code>XmOperationChangedCallbackStruct</code>. The reason sent by the callback is <code>XmCR_OPERATION_CHANGED</code>.</p>
<dt><code>XmNoperationCursorIcon</code></p>
<dd>Specifies the cursor icon used to designate the type of operation performed by the drag transaction. If NULL, <code>XmScreen</code> resources provide default icons for copy, link, and move operations.</p>
<dt><code>XmNsourceCursorIcon</code></p>
<dd>Specifies the cursor icon used to represent the source when a dynamic visual style is used. If NULL, the <code>XmNdefaultSourceCursorIcon</code> resource of <code>XmScreen</code> provides a default cursor icon.</p>
<dt><code>XmNsourcePixmapIcon</code></p>
<dd>Specifies the pixmap icon used to represent the source when a preregister visual style is used. The icon is used in conjunction with the colormap of the widget passed to <code>XmDragStart</code>. If NULL, <code>XmNsourceCursorIcon</code> is used.</p>
<dt><code>XmNstateCursorIcon</code></p>
<dd>Specifies the cursor icon used to designate the state of a drop site. If NULL, <code>XmScreen</code> resources provide default icons for a valid, invalid, and no drop site condition.</p>
<dt><code>XmNtopLevelEnterCallback</code></p>
<dd>Specifies the list of callbacks that are called when the pointer enters a top-level window or root window (due to changing screens). The type of the structure whose address is passed to this callback is <code>XmTopLevelEnterCallbackStruct</code>. The reason sent by the callback is <code>XmCR_TOP_LEVEL_ENTER</code>.</p>
<dt><code>XmNtopLevelLeaveCallback</code></p>
<dd>Specifies the list of callbacks that are called when the pointer leaves a top level window or the root window (due to changing screens). The type of the structure whose address is passed to this callback is <code>XmTopLevelLeaveCallbackStruct</code>. The reason sent by the callback is <code>XmCR_TOP_LEVEL_LEAVE</code>.</p>
<dt><code>XmNvalidCursorForeground</code></p>
<dd>Specifies the foreground pixel value of the cursor designated as a valid cursor icon.</dl>
<h3>Inherited Resources</h3>
<p>DragContext inherits behavior and resources from the superclass described in the following table. For a complete description of each resource, refer to the <code>Core</code> reference page. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>Core Resource Set</code>
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
<td>XmNaccelerators</td>
<td>XmCAccelerators</td>
<td>XtAccelerators</td>
<td>dynamic</td>
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
<td>XmNancestorSensitive</td>
<td>XmCSensitive</td>
<td>Boolean</td>
<td>dynamic</td>
<td>G
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
<td>XmNbackground</td>
<td>XmCBackground</td>
<td>Pixel</td>
<td>dynamic</td>
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
<td>XmNbackgroundPixmap</td>
<td>XmCPixmap</td>
<td>Pixmap</td>
<td>XmUNSPECIFIED_PIXMAP</td>
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
<td>XmNborderColor</td>
<td>XmCBorderColor</td>
<td>Pixel</td>
<td>XtDefaultForeground</td>
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
<td>XmNborderPixmap</td>
<td>XmCPixmap</td>
<td>Pixmap</td>
<td>XmUNSPECIFIED_PIXMAP</td>
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
<td>XmNborderWidth</td>
<td>XmCBorderWidth</td>
<td>Dimension</td>
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
<td>XmNcolormap</td>
<td>XmCColormap</td>
<td>Colormap</td>
<td>dynamic</td>
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
<td>XmNdepth</td>
<td>XmCDepth</td>
<td>int</td>
<td>dynamic</td>
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
<tr VALIGN=top>
<td>XmNheight</td>
<td>XmCHeight</td>
<td>Dimension</td>
<td>dynamic</td>
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
<td>XmNinitialResourcesPersistent</td>
<td>XmCInitialResourcesPersistent</td>
<td>Boolean</td>
<td>True</td>
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
<tr VALIGN=top>
<td>XmNmappedWhenManaged</td>
<td>XmCMappedWhenManaged</td>
<td>Boolean</td>
<td>True</td>
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
<td>XmNscreen</td>
<td>XmCScreen</td>
<td>Screen *</td>
<td>dynamic</td>
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
<td>XmNsensitive</td>
<td>XmCSensitive</td>
<td>Boolean</td>
<td>True</td>
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
<td>XmNtranslations</td>
<td>XmCTranslations</td>
<td>XtTranslations</td>
<td>dynamic</td>
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
<td>XmNwidth</td>
<td>XmCWidth</td>
<td>Dimension</td>
<td>dynamic</td>
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
<td>XmNx</td>
<td>XmCPosition</td>
<td>Position</td>
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
<td>XmNy</td>
<td>XmCPosition</td>
<td>Position</td>
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
</table>
</table>
<h3>Callback Information</h3>
<p>Each of the DragContext callbacks has an associated callback structure. </p>
<p> A pointer to the following structure is passed to the <code>XmNdragDropFinishCallback</code> callback: </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent *<i>event</i>;
 Time <i>timeStamp</i>;
}XmDragDropFinishCallbackStruct, *XmDragDropFinishCallback;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback</p>
<dt><code>timeStamp</code></p>
<dd>Specifies the time at which either the drag or the drop was completed</dl>
<p> A pointer to the following structure is passed to callbacks for <code>XmNdragMotionCallback</code>: </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent *<i>event</i>;
 Time <i>timeStamp</i>;
 unsigned char <i>operation</i>;
 unsigned char <i>operations</i>;
 unsigned char <i>dropSiteStatus</i>;
 Position <i>x</i>;
 Position <i>y</i>;
}XmDragMotionCallbackStruct, *XmDragMotionCallback;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked.</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback.</p>
<dt><code>timeStamp</code></p>
<dd>Specifies the timestamp of the logical event.</p>
<dt><i>operation</i></p>
<dd>Identifies an operation.</p>
<dd>If the toolkit has just called a DropSite&#8217;s <code>XmNdragProc</code>, the toolkit initializes <i>operation</i> to the value of the <i>operation</i> member of the <code>XmDragProcCallbackStruct</code> at the time the DropSite&#8217;s <code>XmNdragProc</code> returns.</p>
<dd>If the toolkit has not called an <code>XmNdragProc</code> and the pointer is within an active drop site, the toolkit initializes <i>operation</i> by selecting an operation from the bitwise AND of the initial value of the <i>operations</i> member and the value of the DropSite&#8217;s <code>XmNdropSiteOperations</code> resource. The toolkit searches this set first for <code>XmDROP_MOVE</code>, then for <code>XmDROP_COPY</code>, then for <code>XmDROP_LINK</code>, and initializes <i>operation</i> to the first operation it finds in the set. If the toolkit finds none of these operations in the set, it initializes <i>operation</i> to <code>XmDROP_NOOP</code>.</p>
<dd>If the toolkit has not called an <code>XmNdragProc</code> and the pointer is not within an active drop site, the toolkit initializes <i>operation</i> by selecting an operation from the initial value of the <i>operations</i> member. The toolkit searches this set first for <code>XmDROP_MOVE</code>, then for <code>XmDROP_COPY</code>, then for <code>XmDROP_LINK</code>, and initializes <i>operation</i> to the first operation it finds in the set. If the toolkit finds none of these operations in the set, it initializes <i>operation</i> to <code>XmDROP_NOOP</code>.</p>
<dt><i>operations</i></p>
<dd>Indicates the set of operations supported for the source data.</p>
<dd>If the toolkit has just called a DropSite&#8217;s <code>XmNdragProc</code>, the toolkit initializes <i>operations</i> to the bitwise AND of the DropSite&#8217;s <code>XmNdropOperations</code> and the value of the <i>operations</i> member of the <code>XmDragProcCallbackStruct</code> at the time the DropSite&#8217;s <code>XmNdragProc</code> returns. If the resulting set of operations is empty, the toolkit initializes <i>operations</i> to <code>XmDROP_NOOP</code>.</p>
<dd>If the toolkit has not called an <code>XmNdragProc</code> and the user does not select an operation (by pressing a modifier key), the toolkit initializes <i>operations</i> to the value of the DragContext&#8217;s <code>XmNdragOperations</code> resource.</p>
<dd>If the toolkit has not called an <code>XmNdragProc</code> and the user does select an operation, the toolkit initializes <i>operations</i> to the bitwise AND of the corresponding operation and the value of the DragContext&#8217;s <code>XmNdragOperations</code> resource. If the resulting set of operations is empty, the toolkit initializes <i>operations</i> to <code>XmDROP_NOOP</code>.</p>
<dt><code>dropSiteStatus</code></p>
<dd>Indicates whether or not a drop site is valid.</p>
<dd>If the toolkit has just called a DropSite&#8217;s <code>XmNdragProc</code>, the toolkit initializes <code>dropSiteStatus</code> to the value of the <code>dropSiteStatus</code> member of the <code>XmDragProcCallbackStruct</code> at the time the DropSite&#8217;s <code>XmNdragProc</code> returns.</p>
<dd>If the toolkit has not called an <code>XmNdragProc</code>, it initializes <code>dropSiteStatus</code> as follows: the toolkit initializes <code>dropSiteStatus</code> to <code>XmNO_DROP_SITE</code> if the pointer is over an inactive drop site or is not over a drop site. The toolkit initializes <code>dropSiteStatus</code> to <code>XmDROP_SITE_VALID</code> if all the following conditions are met:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd>The pointer is over an active drop site.</p>
<dt> &bull;</p>
<dd>The DragContext&#8217;s <code>XmNexportTargets</code> and the DropSite&#8217;s <code>XmNimportTargets</code> are compatible.</p>
<dt> &bull;</p>
<dd>The initial value of the <i>operation</i> member is not <code>XmDROP_NOOP</code>.</dl>
</dl>
<dd>Otherwise, the toolkit initializes <code>dropSiteStatus</code> to <code>XmDROP_SITE_INVALID</code>.</dl>
<p> A pointer to the following structure is passed for the <code>XmNdropFinishCallback</code> callback: </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent *<i>event</i>;
 Time <i>timeStamp</i>;
 unsigned char <i>operation</i>;
 unsigned char <i>operations</i>;
 unsigned char <i>dropSiteStatus</i>;
 unsigned char <i>dropAction</i>;
 unsigned char <i>completionStatus</i>;
}XmDropFinishCallbackStruct, *XmDropFinishCallback;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked.</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback.</p>
<dt><code>timeStamp</code></p>
<dd>Specifies the time at which the drop was completed.</p>
<dt><i>operation</i></p>
<dd>Identifies an operation.</p>
<dd>If the pointer is over an active drop site when the drop begins, the toolkit initializes <i>operation</i> to the value of the <i>operation</i> member of the <code>XmDropProcCallbackStruct</code> at the time the DropSite&#8217;s <code>XmNdropProc</code> returns.</p>
<dd>If the pointer is not over an active drop site when the drop begins, the toolkit initializes <i>operation</i> by selecting an operation from the initial value of the <i>operations</i> member. The toolkit searches this set first for <code>XmDROP_MOVE</code>, then for <code>XmDROP_COPY</code>, then for <code>XmDROP_LINK</code>, and initializes <i>operation</i> to the first operation it finds in the set. If it finds none of these operations in the set, it initializes <i>operation</i> to <code>XmDROP_NOOP</code>.</p>
<dt><i>operations</i></p>
<dd>Indicates the set of operations supported for the source data.</p>
<dd>If the pointer is over an active drop site when the drop begins, the toolkit initializes <i>operations</i> to the bitwise AND of the DropSite&#8217;s <code>XmNdropOperations</code> and the value of the <i>operations</i> member of the <code>XmDropProcCallbackStruct</code> at the time the DropSite&#8217;s <code>XmNdropProc</code> returns. If the resulting set of operations is empty, the toolkit initializes <i>operations</i> to <code>XmDROP_NOOP</code>.</p>
<dd>If the pointer is not over an active drop site when the drop begins and if the user does not select an operation (by pressing a modifier key), the toolkit initializes <i>operations</i> to the value of the DragContext&#8217;s <code>XmNdragOperations</code> resource.</p>
<dd>If the pointer is not over an active drop site when the drop begins and if the user does select an operation, the toolkit initializes <i>operations</i> to the bitwise AND of the corresponding operation and the value of the DragContext&#8217;s <code>XmNdragOperations</code> resource. If the resulting set of operations is empty, the toolkit initializes <i>operations</i> to <code>XmDROP_NOOP</code>.</p>
<dt><code>dropSiteStatus</code></p>
<dd>Indicates whether or not a drop site is valid.</p>
<dd>If the pointer is over an active drop site when the drop begins, the toolkit initializes <code>dropSiteStatus</code> to the value of the <code>dropSiteStatus</code> member of the <code>XmDropProcCallbackStruct</code> at the time the DropSite&#8217;s <code>XmNdropProc</code> returns.</p>
<dd>If the pointer is not over an active drop site when the drop begins, the toolkit initializes <code>dropSiteStatus</code> to <code>XmNO_DROP_SITE</code>.</p>
<dt><code>dropAction</code></p>
<dd>Identifies the drop action. The values are <code>XmDROP</code>, <code>XmDROP_CANCEL</code>, <code>XmDROP_HELP</code>, and <code>XmDROP_INTERRUPT</code>. The <code>XmDROP_INTERRUPT</code> value is currently unsupported; if specified, it will be interpreted as an <code>XmDROP_CANCEL</code>.</p>
<dt><code>completionStatus</code></p>
<dd>An IN/OUT member that indicates the status of the drop action. After the last callback procedure has returned, the final value of this member determines what visual transition effects will be applied. There are two values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmDROP_SUCCESS</code></p>
<dd>The drop was successful.</p>
<dt><code>XmDROP_FAILURE</code></p>
<dd>The drop was unsuccessful.</dl>
</dl>
</dl>
<p> A pointer to the following structure is passed to callbacks for <code>XmNdropSiteEnterCallback</code>: </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent *<i>event</i>;
 Time <i>timeStamp</i>;
 unsigned char <i>operation</i>;
 unsigned char <i>operations</i>;
 unsigned char <i>dropSiteStatus</i>;
 Position <i>x</i>;
 Position <i>y</i>;
}XmDropSiteEnterCallbackStruct, *XmDropSiteEnterCallback;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked.</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback.</p>
<dt><code>timeStamp</code></p>
<dd>Specifies the time the crossing event occurred.</p>
<dt><i>operation</i></p>
<dd>Identifies an operation.</p>
<dd>If the toolkit has just called a DropSite&#8217;s <code>XmNdragProc</code>, the toolkit initializes <i>operation</i> to the value of the <i>operation</i> member of the <code>XmDragProcCallbackStruct</code> at the time the DropSite&#8217;s <code>XmNdragProc</code> returns.</p>
<dd>If the toolkit has not called an <code>XmNdragProc</code>, it initializes <i>operation</i> by selecting an operation from the bitwise AND of the initial value of the <i>operations</i> member and the value of the DropSite&#8217;s <code>XmNdropSiteOperations</code> resource. The toolkit searches this set first for <code>XmDROP_MOVE</code>, then for <code>XmDROP_COPY</code>, then for <code>XmDROP_LINK</code>, and initializes <i>operation</i> to the first operation it finds in the set. If the toolkit finds none of these operations in the set, it initializes <i>operation</i> to <code>XmDROP_NOOP</code>.</p>
<dt><i>operations</i></p>
<dd>Indicates the set of operations supported for the source data.</p>
<dd>If the toolkit has just called a DropSite&#8217;s <code>XmNdragProc</code>, the toolkit initializes <i>operations</i> to the bitwise AND of the DropSite&#8217;s <code>XmNdropOperations</code> and the value of the <i>operations</i> member of the <code>XmDragProcCallbackStruct</code> at the time the DropSite&#8217;s <code>XmNdragProc</code> returns. If the resulting set of operations is empty, the toolkit initializes <i>operations</i> to <code>XmDROP_NOOP</code>.</p>
<dd>If the toolkit has not called an <code>XmNdragProc</code> and the user does not select an operation (by pressing a modifier key), the toolkit initializes <i>operations</i> to the value of the DragContext&#8217;s <code>XmNdragOperations</code> resource.</p>
<dd>If the toolkit has not called an <code>XmNdragProc</code> and the user does select an operation, the toolkit initializes <i>operations</i> to the bitwise AND of the corresponding operation and the value of the DragContext&#8217;s <code>XmNdragOperations</code> resource. If the resulting set of operations is empty, the toolkit initializes <i>operations</i> to <code>XmDROP_NOOP</code>.</p>
<dt><code>dropSiteStatus</code></p>
<dd>Indicates whether or not a drop site is valid.</p>
<dd>If the toolkit has just called a DropSite&#8217;s <code>XmNdragProc</code>, the toolkit initializes <code>dropSiteStatus</code> to the value of the <code>dropSiteStatus</code> member of the <code>XmDragProcCallbackStruct</code> at the time the DropSite&#8217;s <code>XmNdragProc</code> returns.</p>
<dd>If the toolkit has not called <code>XmNdragProc</code>, it initializes <code>dropSiteStatus</code> to <code>XmDROP_SITE_VALID</code> if the DragContext&#8217;s <code>XmNexportTargets</code> and the DropSite&#8217;s <code>XmNimportTargets</code> are compatible and if the initial value of the <i>operation</i> member is not <code>XmDROP_NOOP</code>. Otherwise, the toolkit initializes <code>dropSiteStatus</code> to <code>XmDROP_SITE_INVALID</code>.</p>
<dt><i>x</i></p>
<dd>Indicates the x-coordinate of the pointer in root window coordinates.</p>
<dt><i>y</i></p>
<dd>Indicates the y-coordinate of the pointer in root window coordinates.</dl>
<p> A pointer to the following structure is passed to callbacks for <code>XmNdropSiteLeaveCallback</code>: </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent *<i>event</i>;
 Time <i>timeStamp</i>;
}XmDropSiteLeaveCallbackStruct, *XmDropSiteLeaveCallback;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback</p>
<dt><code>timeStamp</code></p>
<dd>Specifies the timestamp of the logical event</dl>
<p> A pointer to the following structure is passed for the <code>XmNdropStartCallback</code> callback: </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent *<i>event</i>;
 Time <i>timeStamp</i>;
 unsigned char <i>operation</i>;
 unsigned char <i>operations</i>;
 unsigned char <i>dropSiteStatus</i>;
 unsigned char <i>dropAction</i>;
 Position <i>x</i>;
 Position <i>y</i>;
}XmDropStartCallbackStruct, *XmDropStartCallback;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked.</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback.</p>
<dt><code>timeStamp</code></p>
<dd>Specifies the time at which the drag was completed.</p>
<dt><i>operation</i></p>
<dd>Identifies an operation.</p>
<dd>If the pointer is over an active drop site when the drop begins, the toolkit initializes <i>operation</i> to the value of the <i>operation</i> member of the <code>XmDropProcCallbackStruct</code> at the time the DropSite&#8217;s <code>XmNdropProc</code> returns.</p>
<dd>If the pointer is not over an active drop site when the drop begins, the toolkit initializes <i>operation</i> by selecting an operation from the initial value of the <i>operations</i> member. The toolkit searches this set first for <code>XmDROP_MOVE</code>, then for <code>XmDROP_COPY</code>, then for <code>XmDROP_LINK</code>, and initializes <i>operation</i> to the first operation it finds in the set. If it finds none of these operations in the set, it initializes <i>operation</i> to <code>XmDROP_NOOP</code>.</p>
<dt><i>operations</i></p>
<dd>Indicates the set of operations supported for the source data.</p>
<dd>If the pointer is over an active drop site when the drop begins, the toolkit initializes <i>operations</i> to the bitwise AND of the DropSite&#8217;s <code>XmNdropOperations</code> and the value of the <i>operations</i> member of the <code>XmDropProcCallbackStruct</code> at the time the DropSite&#8217;s <code>XmNdropProc</code> returns. If the resulting set of operations is empty, the toolkit initializes <i>operations</i> to <code>XmDROP_NOOP</code>.</p>
<dd>If the pointer is not over an active drop site when the drop begins and if the user does not select an operation (by pressing a modifier key), the toolkit initializes <i>operations</i> to the value of the DragContext&#8217;s <code>XmNdragOperations</code> resource.</p>
<dd>If the pointer is not over an active drop site when the drop begins and if the user does select an operation, the toolkit initializes <i>operations</i> to the bitwise AND of the corresponding operation and the value of the DragContext&#8217;s <code>XmNdragOperations</code> resource. If the resulting set of operations is empty, the toolkit initializes <i>operations</i> to <code>XmDROP_NOOP</code>.</p>
<dt><code>dropSiteStatus</code></p>
<dd>Indicates whether or not a drop site is valid.</p>
<dd>If the pointer is over an active drop site when the drop begins, the toolkit initializes <code>dropSiteStatus</code> to the value of the <code>dropSiteStatus</code> member of the <code>XmDropProcCallbackStruct</code> at the time the DropSite&#8217;s <code>XmNdropProc</code> returns.</p>
<dd>If the pointer is not over an active drop site when the drop begins, the toolkit initializes <code>dropSiteStatus</code> to <code>XmNO_DROP_SITE</code>.</p>
<dd>This field is invalid if the <code>dropAction</code> field is set to <code>XmDROP_CANCEL</code>.</p>
<dt><code>dropAction</code></p>
<dd>An IN/OUT member that identifies the drop action. The values are <code>XmDROP</code>, <code>XmDROP_CANCEL</code>, <code>XmDROP_HELP</code>, and <code>XmDROP_INTERRUPT</code>. The value of <code>dropAction</code> can be modified to change the action actually initiated. The value <code>XmDROP_INTERRUPT</code> is currently unsupported; if specified, it will be interpreted as an <code>XmDROP_CANCEL</code>.</p>
<dt><i>x</i></p>
<dd>Indicates the x-coordinate of the pointer in root window coordinates.</p>
<dt><i>y</i></p>
<dd>Indicates the y-coordinate of the pointer in root window coordinates.</dl>
<p> A pointer to the following structure is passed to the <code>XmNoperationChangedCallback</code> callback: </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent *<i>event</i>;
 Time <i>timeStamp</i>;
 unsigned char <i>operation</i>;
 unsigned char <i>operations</i>;
 unsigned char <i>dropSiteStatus</i>;
}XmOperationChangedCallbackStruct, *XmOperationChangedCallback;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked.</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback.</p>
<dt><code>timeStamp</code></p>
<dd>Specifies the time at which the crossing event occurred.</p>
<dt><i>operation</i></p>
<dd>Identifies an operation.</p>
<dd>If the toolkit has just called a DropSite&#8217;s <code>XmNdragProc</code>, the toolkit initializes <i>operation</i> to the value of the <i>operation</i> member of the <code>XmDragProcCallbackStruct</code> at the time the DropSite&#8217;s <code>XmNdragProc</code> returns.</p>
<dd>If the toolkit has not called an <code>XmNdragProc</code>, and the pointer is within an active drop site, the toolkit initializes <i>operation</i> by selecting an operation from the bitwise AND of the initial value of the <i>operations</i> member and the value of the DropSite&#8217;s <code>XmNdropSiteOperations</code> resource. The toolkit searches this set first for <code>XmDROP_MOVE</code>, then for <code>XmDROP_COPY</code>, then for <code>XmDROP_LINK</code>, and initializes <i>operation</i> to the first operation it finds in the set. If the toolkit finds none of these operations in the set, it initializes <i>operation</i> to <code>XmDROP_NOOP</code>.</p>
<dd>If the toolkit has not called an <code>XmNdragProc</code>, and the pointer is not within an active drop site, the toolkit initializes <i>operation</i> by selecting an operation from the initial value of the <i>operations</i> member. The toolkit searches this set first for <code>XmDROP_MOVE</code>, then for <code>XmDROP_COPY</code>, then for <code>XmDROP_LINK</code>, and initializes <i>operation</i> to the first operation it finds in the set. If the toolkit finds none of these operations in the set, it initializes <i>operation</i> to <code>XmDROP_NOOP</code>.</p>
<dt><i>operations</i></p>
<dd>Indicates the set of operations supported for the source data.</p>
<dd>If the toolkit has just called a DropSite&#8217;s <code>XmNdragProc</code>, the toolkit initializes <i>operations</i> to the bitwise AND of the DropSite&#8217;s <code>XmNdropOperations</code> and the value of the <i>operations</i> member of the <code>XmDragProcCallbackStruct</code> at the time the DropSite&#8217;s <code>XmNdragProc</code> returns. If the resulting set of operations is empty, the toolkit initializes <i>operations</i> to <code>XmDROP_NOOP</code>.</p>
<dd>If the toolkit has not called an <code>XmNdragProc</code>, and the user does not select an operation (by pressing a modifier key), the toolkit initializes <i>operations</i> to the value of the DragContext&#8217;s <code>XmNdragOperations</code> resource.</p>
<dd>If the toolkit has not called an <code>XmNdragProc</code>, and the user does select an operation, the toolkit initializes <i>operations</i> to the bitwise AND of the corresponding operation and the value of the DragContext&#8217;s <code>XmNdragOperations</code> resource. If the resulting set of operations is empty, the toolkit initializes <i>operations</i> to <code>XmDROP_NOOP</code>.</p>
<dt><code>dropSiteStatus</code></p>
<dd>Indicates whether or not a drop site is valid.</p>
<dd>If the toolkit has just called a DropSite&#8217;s <code>XmNdragProc</code>, the toolkit initializes <code>dropSiteStatus</code> to the value of the <code>dropSiteStatus</code> member of the <code>XmDragProcCallbackStruct</code> at the time the DropSite&#8217;s <code>XmNdragProc</code> returns.</p>
<dd>If the toolkit has not called an <code>XmNdragProc</code> it initializes <code>dropSiteStatus</code> to <code>XmNO_DROP_SITE</code> if the pointer is over an inactive drop site or is not over a drop site. The toolkit initializes <code>dropSiteStatus</code> to <code>XmDROP_SITE_VALID</code> if all the following conditions are met:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd>The pointer is over an active drop site</p>
<dt> &bull;</p>
<dd>The DragContext&#8217;s <code>XmNexportTargets</code> and the DropSite&#8217;s <code>XmNimportTargets</code> are compatible</p>
<dt> &bull;</p>
<dd>The initial value of the <i>operation</i> member is not <code>XmDROP_NOOP</code></dl>
</dl>
<dd>Otherwise, the toolkit initializes <code>dropSiteStatus</code> to <code>XmDROP_SITE_INVALID</code>.</dl>
<p> A pointer to the following structure is passed to callbacks for <code>XmNtopLevelEnterCallback</code>: </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent *<i>event</i>;
 Time <i>timeStamp</i>;
 Screen <i>screen</i>;
 Window <i>window</i>;
 Position <i>x</i>;
 Position <i>y</i>;
 unsigned char <i>dragProtocolStyle</i>;
}XmTopLevelEnterCallbackStruct, *XmTopLevelEnterCallback;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked.</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback.</p>
<dt><code>timeStamp</code></p>
<dd>Specifies the timestamp of the logical event.</p>
<dt><i>screen</i></p>
<dd>Specifies the screen associated with the top-level window or root window being entered.</p>
<dt><i>window</i></p>
<dd>Specifies the ID of the top-level window or root window being entered.</p>
<dt><i>x</i></p>
<dd>Indicates the x-coordinate of the pointer in root window coordinates.</p>
<dt><i>y</i></p>
<dd>Indicates the y-coordinate of the pointer in root window coordinates.</p>
<dt><code>dragProtocolStyle</code></p>
<dd>Specifies the protocol style adopted by the initiator. The values are <code>XmDRAG_DROP_ONLY</code>, <code>XmDRAG_DYNAMIC</code>, <code>XmDRAG_NONE</code>, and <code>XmDRAG_PREREGISTER</code>.</dl>
<p> A pointer to the following structure is passed to callbacks for <code>XmNtopLevelLeaveCallback</code>: </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent *<i>event</i>;
 Time <i>timeStamp</i>;
 Screen <i>screen</i>;
 Window <i>window</i>;
}XmTopLevelLeaveCallbackStruct, *XmTopLevelLeaveCallback;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback</p>
<dt><code>timeStamp</code></p>
<dd>Specifies the timestamp of the logical event</p>
<dt><i>screen</i></p>
<dd>Specifies a screen associated with the top-level window or root window being left</p>
<dt><i>window</i></p>
<dd>Specifies the ID of the top-level window or root window being left</dl>
<h3>Translations</h3>
<p>The XmDragContext translations are described in the following list. The following key names are listed in the X standard key event translation table syntax. This format is the one used by Motif to specify the widget actions corresponding to a given key. A brief overview of the format is provided under <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3). For a complete description of the format, please refer to the X Toolkit Instrinsics Documentation.</p>
<dl COMPACT>
<dt><code>Button1&lt;Enter&gt;</code>:</p>
<dd>DragMotion()</p>
<dt><code>Button1&lt;Leave&gt;</code>:</p>
<dd>DragMotion()</p>
<dt><code>Button1&lt;Motion&gt;</code>:</p>
<dd>DragMotion()</p>
<dt><code>Button2&lt;Enter&gt;</code>:</p>
<dd>DragMotion()</p>
<dt><code>Button2&lt;Leave&gt;</code>:</p>
<dd>DragMotion()</p>
<dt><code>Button2&lt;Motion&gt;</code>:</p>
<dd>DragMotion()</p>
<dt><code>&lt;Btn2Up&gt;</code>:</p>
<dd>FinishDrag()</p>
<dt><code>&lt;Btn1Up&gt;</code>:</p>
<dd>FinishDrag()</p>
<dt><code>&lt;Key&gt;</code><code>Return</code>:</p>
<dd>FinishDrag()</p>
<dt><code>&lt;Key&gt;</code><code>&lt;osfActivate&gt;</code>:</p>
<dd>FinishDrag()</p>
<dt><code>&lt;BtnDown&gt;</code>:</p>
<dd>IgnoreButtons()</p>
<dt><code>&lt;BtnUp&gt;</code>:</p>
<dd>IgnoreButtons()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfCancel&gt;</code>:</p>
<dd>CancelDrag()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfHelp&gt;</code>:</p>
<dd>HelpDrag()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfUp&gt;</code>:</p>
<dd>DragKey(<code>Up</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfDown&gt;</code>:</p>
<dd>DragKey(<code>Down</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfLeft&gt;</code>:</p>
<dd>DragKey(<code>Left</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfRight&gt;</code>:</p>
<dd>DragKey(<code>Right</code>)</p>
<dt><code>:&lt;KeyUp&gt;</code>:</p>
<dd>DragKey(<code>Update</code>)</p>
<dt><code>:&lt;KeyDown&gt;</code>:</p>
<dd>DragKey(<code>Update</code>)</dl>
<h3>Action Routines</h3>
<p>The XmDragContext action routines are</p>
<dl COMPACT>
<dt>CancelDrag():</p>
<dd>Cancels the drag operation and frees the associated DragContext.</p>
<dt>DragKey(<code>String</code><code>)</code></p>
<dd>If the value of <code>String</code> is <code>Left</code>, <code>Right</code>, <code>Up</code>, or <code>Down</code>, this action moves the dragged object in the corresponding location. Any other values of <code>String</code> are ignored.</p>
<dt>DragMotion():</p>
<dd>Drags the selected data as the pointer is moved.</p>
<dt>FinishDrag():</p>
<dd>Finishes the drag operation and starts the drop operation.</p>
<dt>HelpDrag():</p>
<dd>Initiates a conditional drop that enables the receiver to provide help information to the user. The user can cancel or continue the drop operation in response to this information.</dl>
<h3>Virtual Bindings</h3>
<p>The bindings for virtual keys are vendor specific. For information about bindings for virtual buttons and keys, see <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3).</p>
<h2>Related Information</h2>
<p><code><a href="/docs/linux/man/3-core/">Core</a></code>(3), <code><a href="/docs/linux/man/3-xmdisplay/">XmDisplay</a></code>(3), <code><a href="/docs/linux/man/3-xmdragcancel/">XmDragCancel</a></code>(3), <code><a href="/docs/linux/man/3-xmdragicon/">XmDragIcon</a></code>(3), <code><a href="/docs/linux/man/3-xmdragstart/">XmDragStart</a></code>(3), <code><a href="/docs/linux/man/3-xmdropsite/">XmDropSite</a></code>(3), <code><a href="/docs/linux/man/3-xmdroptransfer/">XmDropTransfer</a></code>(3), and <code><a href="/docs/linux/man/3-xmscreen/">XmScreen</a></code>(3).</p>
