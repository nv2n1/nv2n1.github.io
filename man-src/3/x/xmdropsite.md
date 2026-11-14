---
title: "xmdropsite(3)"
name: "xmdropsite"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdropsite/"
description: "XmDropSite — The DropSite Registry"
---

<p><code>XmDropSite</code> &#8212; The DropSite Registry</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DragDrop.h&gt;</pre>
<h2>Description</h2>
<p>A client registers a widget or gadget as a drop site using the <code>XmDropSiteRegister</code> function. In addition, this routine defines the behavior and capabilities of a drop site by specifying appropriate resources. For example, the <code>XmNimportTargets</code> and <code>XmNnumImportTargets</code> resources identify respectively the selection target types and number of types supported by a drop site. The visual animation effects associated with a drop site are also described with DropSite resources. </p>
<p> Drop site animation effects that occur in response to the pointer entering a valid drop site are called drag-under effects. A receiver can select from several animation styles supplied by the toolkit or can provide customized animation effects. Drag-under effects supplied by the toolkit include border highlighting, shadow in/out drawing, and pixmap representation. </p>
<p> When a preregister drag protocol style is used, the toolkit generates drag-under visual effects based on the value of the <code>XmNanimationStyle</code> resource. In dynamic mode, if the drop site <code>XmNdragProc</code> resource is NULL, the toolkit also provides animation effects based on the <code>XmNanimationStyle</code> resource. Otherwise, if the <code>XmNdragProc</code> routine is specified, the receiver can either assume responsibility for animation effects (through the <code>XmNdragProc</code> routine) or rely on the toolkit to provide animation. An application can either handle all or none of the animation effects for a particular drop site. That is, an application should never do a partial job of animation on a particular drop site. </p>
<p> Drop sites may overlap. The initial stacking order corresponds to the order in which the drop sites were registered. When a drop site overlaps another drop site, the drag-under effects of the drop site underneath are clipped by the obscuring drop site(s). </p>
<p> The <code>XmDropSiteUpdate</code> routine sets resources for a widget that is registered as a drop site. <code>XmDropSiteRetrieve</code> gets drop site resource values previously specified for a registered widget. These routines are used instead of <code>XtSetValues</code> and <code>XtGetValues</code>.</p>
<h3>Classes</h3>
<p>XmDropSite does not inherit from any widget class.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XmDropSiteUpdate</code> (S), retrieved by using <code>XmDropSiteRetrieve</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmDropSite Resource Set</code>
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
<td>XmNanimationMask</td>
<td>XmCAnimationMask</td>
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
<td>XmNanimationPixmap</td>
<td>XmCAnimationPixmap</td>
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
<td>XmNanimationPixmapDepth</td>
<td>XmCAnimationPixmapDepth</td>
<td>int</td>
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
<td>XmNanimationStyle</td>
<td>XmCAnimationStyle</td>
<td>unsigned char</td>
<td>XmDRAG_UNDER_HIGHLIGHT</td>
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
<td>XmNdragProc</td>
<td>XmCDragProc</td>
<td>XtCallbackProc</td>
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
<td>XmNdropProc</td>
<td>XmCDropProc</td>
<td>XtCallbackProc</td>
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
<td>XmNdropRectangles</td>
<td>XmCDropRectangles</td>
<td>XRectangle *</td>
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
<td>XmNdropSiteActivity</td>
<td>XmCDropSiteActivity</td>
<td>unsigned char</td>
<td>XmDROP_SITE_ACTIVE</td>
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
<td>XmNdropSiteOperations</td>
<td>XmCDropSiteOperations</td>
<td>unsigned char</td>
<td>XmDROP_MOVE | XmDROP_COPY</td>
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
<td>XmNdropSiteType</td>
<td>XmCDropSiteType</td>
<td>unsigned char</td>
<td>XmDROP_SITE_SIMPLE</td>
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
<td>XmNimportTargets</td>
<td>XmCImportTargets</td>
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
<td>XmNnumDropRectangles</td>
<td>XmCNumDropRectangles</td>
<td>Cardinal</td>
<td>1</td>
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
<td>XmNnumImportTargets</td>
<td>XmCNumImportTargets</td>
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
</table>
</table>
<dl COMPACT>
<dt><code>XmNanimationMask</code></p>
<dd>Specifies a mask to use with the pixmap specified by <code>XmNanimationPixmap</code> when the animation style is <code>XmDRAG_UNDER_PIXMAP</code>.</p>
<dt><code>XmNanimationPixmap</code></p>
<dd>Specifies a pixmap for drag-under animation when the animation style is <code>XmDRAG_UNDER_PIXMAP</code>. The pixmap is drawn with its origin at the upper left corner of the bounding box of the drop site. If the drop site window is larger than the animation pixmap, the portion of the window not covered by the pixmap will be tiled with the window&#8217;s background color.</p>
<dt><code>XmNanimationPixmapDepth</code></p>
<dd>Specifies the depth of the pixmap specified by the <code>XmNanimationPixmap</code> resource. When the depth is 1, the colors are taken from the foreground and background of the drop site widget. For any other value, drop site animation occurs only if the <code>XmNanimationPixmapDepth</code> matches the depth of the drop site window. Colors are derived from the current colormap.</p>
<dt><code>XmNanimationStyle</code></p>
<dd>Specifies the drag-under animation style used when a drag enters a valid drop site. The possible values are</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmDRAG_UNDER_HIGHLIGHT</code></p>
<dd>The drop site uses highlighting effects.</p>
<dt><code>XmDRAG_UNDER_SHADOW_OUT</code></p>
<dd>The drop site uses an outset shadow.</p>
<dt><code>XmDRAG_UNDER_SHADOW_IN</code></p>
<dd>The drop site uses an inset shadow.</p>
<dt><code>XmDRAG_UNDER_PIXMAP</code></p>
<dd>The drop site uses the pixmap specified by <code>XmNanimationPixmap</code> to indicate that it can receive the drop.</p>
<dt><code>XmDRAG_UNDER_NONE</code></p>
<dd>The drop site does not use animation effects. A client using a dynamic protocol, may provide drag-under effects in its <code>XmNdragProc</code> routine.</dl>
</dl>
<dt><code>XmNdragProc</code></p>
<dd>Specifies the procedure that is invoked when the drop site receives a crossing, motion, or operation changed message. This procedure is called only when a dynamic protocol is used. The type of structure whose address is passed to this procedure is <code>XmDragProcCallbackStruct</code>. The reason sent to the procedure is one of the following:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd><code>XmCR_DROP_SITE_ENTER_MESSAGE</code></p>
<dt> &bull;</p>
<dd><code>XmCR_DROP_SITE_LEAVE_MESSAGE</code></p>
<dt> &bull;</p>
<dd><code>XmCR_DRAG_MOTION</code></p>
<dt> &bull;</p>
<dd><code>XmCR_OPERATION_CHANGED</code></dl>
</dl>
<dd>The drag procedure may change the values of some members of the <code>XmDragProcCallbackStruct</code> passed to it. After the drag procedure returns, the toolkit uses the final values in initializing some members of the callback structure passed to the appropriate callbacks of the initiator (the DragContext&#8217;s <code>XmNdropSiteEnterCallback</code>, <code>XmNdropSiteLeaveCallback</code>, <code>XmNdragMotionCallback</code>, or <code>XmNoperationChangedCallback</code> callbacks).</p>
<dt><code>XmNdropProc</code></p>
<dd>Specifies the procedure that is invoked when a drop (excluding a cancel or interrupt action) occurs on a drop site regardless of the status of the drop site. The type of the structure whose address is passed to this procedure is <code>XmDropProcCallbackStruct</code>. The reason sent to the procedure is <code>XmCR_DROP_MESSAGE</code>.</p>
<dd>The drop procedure may change the values of some members of the <code>XmDropProcCallbackStruct</code> passed to it. After the drop procedure returns, the toolkit uses the final values in initializing some members of the <code>XmDropStartCallbackStruct</code> passed to the initiator&#8217;s drop start callbacks (the DragContext&#8217;s <code>XmNdropStartCallback</code> callbacks).</p>
<dt><code>XmNdropRectangles</code></p>
<dd>Specifies a list of rectangles that describe the shape of a drop site. The locations of the rectangles are relative to the origin of the enclosing object. When <code>XmNdropRectangles</code> is NULL, the drop site is assumed to be the sensitive area of the enclosing widget. If <code>XmNdropSiteType</code> is <code>XmDROP_SITE_COMPOSITE</code>, this resource cannot be specified by the application.</p>
<dd>Retrieving this resource returns allocated memory that needs to be freed with the <code>XtFree</code> function.</p>
<dt><code>XmNdropSiteActivity</code></p>
<dd>Indicates whether a drop site is active or inactive. The values are <code>XmDROP_SITE_ACTIVE</code>, <code>XmDROP_SITE_INACTIVE</code>, and <code>XmDROP_SITE_IGNORE</code>. An active drop site can receive a drop, whereas an inactive drop site is dormant. An inactive drop site is treated as if it was not a registered drop site and any drag-under visuals associated with entering or leaving the drop site do not occur. However, it is still used for clipping drag-under effects. A value of <code>XmDROP_SITE_IGNORE</code> indicates that a drop site should be ignored for all purposes.</p>
<dt><code>XmNdropSiteOperations</code></p>
<dd>Specifies the set of valid operations associated with a drop site. This resource is a bit mask that is formed by combining one or more of the following values using a bitwise operation such as inclusive OR (|): <code>XmDROP_COPY</code>, <code>XmDROP_LINK</code>, and <code>XmDROP_MOVE</code>. The value <code>XmDROP_NOOP</code> for this resource indicates that no operations are valid.</p>
<dt><code>XmNdropSiteType</code></p>
<dd>Specifies the type of the drop site. The possible values are</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmDROP_SITE_SIMPLE</code></p>
<dd>The widget does not have any additional children that are registered as drop sites.</p>
<dt><code>XmDROP_SITE_COMPOSITE</code></p>
<dd>The widget will have children that are registered as drop sites.</dl>
</dl>
<dt><code>XmNimportTargets</code></p>
<dd>Specifies the list of target atoms that this drop site accepts.</p>
<dt><code>XmNnumDropRectangles</code></p>
<dd>Specifies the number of rectangles in the <code>XmNdropRectangles</code> list. If the drop site type is <code>XmDROP_SITE_COMPOSITE</code>, this resource can not be specified by the application.</p>
<dt><code>XmNnumImportTargets</code></p>
<dd>Specifies the number of atoms in the target atom list.</dl>
<h3>Callback Information</h3>
<p>A pointer to the following structure is passed to the <code>XmNdragProc</code> routine when the drop site receives crossing, motion, or operation changed messages: </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent *<i>event</i>;
 Time <i>timeStamp</i>;
 Widget <i>dragContext</i>;
 Position <i>x</i>;
 Position <i>y</i>;
 unsigned char <i>dropSiteStatus</i>;
 unsigned char <i>operation</i>;
 unsigned char <i>operations</i>;
 Boolean <i>animate</i>;
} XmDragProcCallbackStruct, *XmDragProcCallback;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked.</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback.</p>
<dt><code>timeStamp</code></p>
<dd>Specifies the timestamp of the logical event.</p>
<dt><i>dragContext</i></p>
<dd>Specifies the ID of the DragContext widget associated with the transaction.</p>
<dt><i>x</i></p>
<dd>Indicates the x-coordinate of the pointer relative to the drop site.</p>
<dt><i>y</i></p>
<dd>Indicates the y-coordinate of the pointer relative to the drop site.</p>
<dt><code>dropSiteStatus</code></p>
<dd>An IN/OUT member that indicates whether or not a drop site is valid.</p>
<dd>When <i>reason</i> is <code>XmCR_DROP_SITE_ENTER_MESSAGE</code> or <code>XmCR_OPERATION_CHANGED</code>, or <i>reason</i> is <code>XmCR_DRAG_MOTION</code> or <code>XmCR_DROP_SITE_LEAVE_MESSAGE</code> and the pointer is not in the same drop site as on the previous invocation of the drag procedure, the toolkit initializes <code>dropSiteStatus</code> to <code>XmDROP_SITE_VALID</code> if the DragContext&#8217;s <code>XmNexportTargets</code> and the DropSite&#8217;s <code>XmNimportTargets</code> are compatible and if the initial value of the <i>operation</i> member is not <code>XmDROP_NOOP</code>. Otherwise, the toolkit initializes <code>dropSiteStatus</code> to <code>XmDROP_SITE_INVALID</code>.</p>
<dd>When the <i>reason</i> is <code>XmCR_DRAG_MOTION</code> or <code>XmCR_DROP_SITE_LEAVE_MESSAGE</code> and the pointer is within the same drop site as on the previous invocation of the drag procedure, the toolkit initializes <code>dropSiteStatus</code> to the value of <code>dropSiteStatus</code> at the time the previous invocation of the drag procedure returns.</p>
<dd>The drag procedure may change the value of this member. After the drag procedure returns, the toolkit uses the final value in initializing the <code>dropSiteStatus</code> member of the callback struct passed to the appropriate callbacks of the initiator.</p>
<dt><i>operation</i></p>
<dd>An IN/OUT member that identifies an operation.</p>
<dd>The toolkit initializes <i>operation</i> by selecting an operation from the bitwise AND of the initial value of the <i>operations</i> member and the value of the DropSite&#8217;s <code>XmNdropSiteOperations</code> resource. The toolkit searches this set first for <code>XmDROP_MOVE</code>, then for <code>XmDROP_COPY</code>, then for <code>XmDROP_LINK</code>, and initializes <i>operation</i> to the first operation it finds in the set. If the toolkit finds none of these operations in the set, it initializes <i>operation</i> to <code>XmDROP_NOOP</code>.</p>
<dd>The drag procedure may change the value of this member. After the drag procedure returns, the toolkit uses the final value in initializing the <i>operation</i> member of the callback struct passed to the appropriate callbacks of the initiator.</p>
<dt><i>operations</i></p>
<dd>An IN/OUT member that indicates the set of operations supported for the source data.</p>
<dd>If the user does not select an operation (by pressing a modifier key), the toolkit initializes <i>operations</i> to the value of the DragContext&#8217;s <code>XmNdragOperations</code> resource. If the user does select an operation, the toolkit initializes <i>operations</i> to the bitwise AND of the corresponding operation and the value of the DragContext&#8217;s <code>XmNdragOperations</code> resource. If the resulting set of operations is empty, the toolkit initializes <i>operations</i> to <code>XmDROP_NOOP</code>.</p>
<dd>The drag procedure may change the value of this member. After the drag procedure returns, the toolkit uses the final value in initializing the <i>operations</i> member of the callback struct passed to the appropriate callbacks of the initiator.</p>
<dt><i>animate</i></p>
<dd>An OUT member that indicates whether the toolkit or the receiver client provides drag-under effects for a valid drop site. If <i>animate</i> is set to True, the toolkit provides drop site animation per the <code>XmNanimationStyle</code> resource value; if it is set to False, the receiver generates drag-under animation effects.</dl>
<p> A pointer to the following structure is passed to the <code>XmNdropProc</code> routine when the drop site receives a drop message: </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent *<i>event</i>;
 Time <i>timeStamp</i>;
 Widget <i>dragContext</i>;
 Position <i>x</i>;
 Position <i>y</i>;
 unsigned char <i>dropSiteStatus</i>;
 unsigned char <i>operation</i>;
 unsigned char <i>operations</i>;
 unsigned char <i>dropAction</i>;
} XmDropProcCallbackStruct, *XmDropProcCallback;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked.</p>
<dt><i>event</i></p>
<dd>Specifies the <code>XEvent</code> that triggered the callback.</p>
<dt><code>timeStamp</code></p>
<dd>Specifies the timestamp of the logical event.</p>
<dt><i>dragContext</i></p>
<dd>Specifies the ID of the DragContext widget associated with the transaction.</p>
<dt><i>x</i></p>
<dd>Indicates the x-coordinate of the pointer relative to the drop site.</p>
<dt><i>y</i></p>
<dd>Indicates the y-coordinate of the pointer relative to the drop site.</p>
<dt><code>dropSiteStatus</code></p>
<dd>An IN/OUT member that indicates whether or not a drop site is valid.</p>
<dd>The toolkit initializes <code>dropSiteStatus</code> to <code>XmDROP_SITE_VALID</code> if the DragContext&#8217;s <code>XmNexportTargets</code> and the DropSite&#8217;s <code>XmNimportTargets</code> are compatible and if the initial value of the <i>operation</i> member is not <code>XmDROP_NOOP</code>. Otherwise, the toolkit initializes <code>dropSiteStatus</code> to <code>XmDROP_SITE_INVALID</code>.</p>
<dd>The drop procedure may change the value of this member. After the drop procedure returns, the toolkit uses the final value in initializing the <code>dropSiteStatus</code> member of the <code>XmDropStartCallbackStruct</code> passed to the initiator&#8217;s drop start callbacks (the DragContext&#8217;s <code>XmNdropStartCallback</code> callbacks).</p>
<dt><i>operation</i></p>
<dd>An IN/OUT member that identifies an operation.</p>
<dd>The toolkit initializes <i>operation</i> by selecting an operation from the bitwise AND of the initial value of the <i>operations</i> member and the value of the DropSite&#8217;s <code>XmNdropSiteOperations</code> resource. The toolkit searches this set first for <code>XmDROP_MOVE</code>, then for <code>XmDROP_COPY</code>, then for <code>XmDROP_LINK</code>, and initializes <i>operation</i> to the first operation it finds in the set. If it finds none of these operations in the set, it initializes <i>operation</i> to <code>XmDROP_NOOP</code>.</p>
<dd>The drop procedure may change the value of this member. After the drop procedure returns, the toolkit uses the final value in initializing the <i>operation</i> member of the <code>XmDropStartCallbackStruct</code> passed to the initiator&#8217;s drop start callbacks (the DragContext&#8217;s <code>XmNdropStartCallback</code> callbacks).</p>
<dt><i>operations</i></p>
<dd>An IN/OUT member that indicates the set of operations supported for the source data.</p>
<dd>If the user does not select an operation (by pressing a modifier key), the toolkit initializes <i>operations</i> to the value of the DragContext&#8217;s <code>XmNdragOperations</code> resource. If the user does select an operation, the toolkit initializes <i>operations</i> to the bitwise AND of the corresponding operation and the value of the DragContext&#8217;s <code>XmNdragOperations</code> resource. If the resulting set of operations is empty, the toolkit initializes <i>operations</i> to <code>XmDROP_NOOP</code>.</p>
<dd>The drop procedure may change the value of this member. After the drop procedure returns, the toolkit uses the final value in initializing the <i>operations</i> member of the <code>XmDropStartCallbackStruct</code> passed to the initiator&#8217;s drop start callbacks (the DragContext&#8217;s <code>XmNdropStartCallback</code> callbacks).</p>
<dt><code>dropAction</code></p>
<dd>An IN/OUT member that identifies the action associated with the drop. The possible values are</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmDROP</code></p>
<dd>A drop was attempted. If the drop site is valid, drop transfer handling proceeds.</p>
<dt><code>XmDROP_HELP</code></p>
<dd>The user has requested help on the drop site.</dl>
</dl>
<dd>The drop procedure may change the value of this member. After the drop procedure returns, the toolkit uses the final value in initializing the <code>dropAction</code> member of the <code>XmDropStartCallbackStruct</code> passed to the initiator&#8217;s drop start callbacks (the DragContext&#8217;s <code>XmNdropStartCallback</code> callbacks).</dl>
<h2>Related Information</h2>
<p><code><a href="/docs/linux/man/3-xmdragcontext/">XmDragContext</a></code>(3), <code><a href="/docs/linux/man/3-xmdragicon/">XmDragIcon</a></code>(3), <code><a href="/docs/linux/man/3-xmdropsiteconfigurestackingorder/">XmDropSiteConfigureStackingOrder</a></code>(3), <code><a href="/docs/linux/man/3-xmdropsiteendupdate/">XmDropSiteEndUpdate</a></code>(3), <code><a href="/docs/linux/man/3-xmdropsitequerystackingorder/">XmDropSiteQueryStackingOrder</a></code>(3), <code><a href="/docs/linux/man/3-xmdropsiteregister/">XmDropSiteRegister</a></code>(3), <code><a href="/docs/linux/man/3-xmdropsitestartupdate/">XmDropSiteStartUpdate</a></code>(3), <code><a href="/docs/linux/man/3-xmdropsiteupdate/">XmDropSiteUpdate</a></code>(3), <code><a href="/docs/linux/man/3-xmdropsiteunregister/">XmDropSiteUnregister</a></code>(3), <code><a href="/docs/linux/man/3-xmdroptransfer/">XmDropTransfer</a></code>(3), and <code><a href="/docs/linux/man/3-xmtargetsarecompatible/">XmTargetsAreCompatible</a></code>(3).</p>
