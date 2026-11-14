---
title: "xmdragicon(3)"
name: "xmdragicon"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmdragicon/"
description: "XmDragIcon — The DragIcon widget class"
---

<p><code>XmDragIcon</code> &#8212; The DragIcon widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/DragDrop.h&gt;</pre>
<h2>Description</h2>
<p>A DragIcon is a component of the visual used to represent the source data in a drag and drop transaction. During a drag operation, a real or simulated X cursor provides drag-over visuals consisting of a static portion that represents the object being dragged, and dynamic cues that provide visual feedback during the drag operation. The visual is attained by blending together various <code>XmDragIcons</code> specified in the <code>XmDragContext</code> associated with the drag operation. </p>
<p> The static portion of the drag-over visual is the graphic representation that identifies the drag source. For example, when a user drags several items within a list, a DragIcon depicting a list might be supplied as the visual. The <code>XmDragContext</code> resources, <code>XmNsourceCursorIcon</code> or <code>XmNsourcePixmapIcon</code>, specify a DragIcon to use for the static portion of the visual. </p>
<p> A drag-over visual incorporates dynamic cues in order to provide visual feedback in response to the user&#8217;s actions. For instance, the drag-over visual might use different indicators to identify the type of operation (copy, link, or move) being performed. Dynamic cues could also alert the user that a drop site is valid or invalid as the pointer traverses the drop site. The <code>XmNoperationCursorIcon</code> and <code>XmNstateCursorIcon</code> resources of <code>XmDragContext</code> specify DragIcons for dynamic cues. </p>
<p> A drag-over visual typically consists of a source, operation and state DragIcon. The <code>XmNblendModel</code> resource of <code>XmDragContext</code> offers several options that determine which icons are blended to produce the drag-over visual. DragIcon resources control the relative position of the operation and state icons (if used). If a particular DragIcon is not specified, the toolkit uses the <code>XmScreen</code> default DragIcons. </p>
<p> An application initializes a DragIcon with the function <code>XmCreateDragIcon</code> or through entries in the resource database. If a pixmap and its mask (optional) are specified in the resource database, the toolkit converts the values in the X11 Bitmap file format and assigns values to the corresponding resources.</p>
<h3>Classes</h3>
<p>DragIcon inherits behavior and a resource from <code>Object</code>. </p>
<p> The class pointer is <code>xmDragIconObjectClass</code>. </p>
<p> The class name is <code>XmDragIcon</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmDragIcon Resource Set</code>
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
<td>XmNattachment</td>
<td>XmCAttachment</td>
<td>unsigned char</td>
<td>XmATTACH_NORTH_WEST</td>
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
<td>XmNdepth</td>
<td>XmCDepth</td>
<td>int</td>
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
<td>XmNheight</td>
<td>XmCHeight</td>
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
<td>XmNhotX</td>
<td>XmCHot</td>
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
<td>XmNhotY</td>
<td>XmCHot</td>
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
<td>XmNmask</td>
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
<td>XmNoffsetX</td>
<td>XmCOffset</td>
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
<td>XmNoffsetY</td>
<td>XmCOffset</td>
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
<td>XmNpixmap</td>
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
<td>XmNwidth</td>
<td>XmCWidth</td>
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
</table>
</table>
<dl COMPACT>
<dt><code>XmNattachment</code></p>
<dd>Specifies a relative location on the source icon for the attachment of the state or operation icon. The origin of the state and operation icons is aligned with the specified compass point on the source icon. The <code>XmNoffsetX</code> and <code>XmNoffsetY</code> resources can be used to further refine the icon positions. The possible values are</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmATTACH_NORTH_WEST</code></p>
<dd>Attaches the origin of the state or operation icon to the northwest point on the source icon.</p>
<dt><code>XmATTACH_NORTH</code></p>
<dd>Attaches the origin of the state or operation icon to the north point on the source icon.</p>
<dt><code>XmATTACH_NORTH_EAST</code></p>
<dd>Attaches the origin of the state or operation icon to the northeast point on the source icon.</p>
<dt><code>XmATTACH_EAST</code></p>
<dd>Attaches the origin of the state or operation icon to the east point on the source icon.</p>
<dt><code>XmATTACH_SOUTH_EAST</code></p>
<dd>Attaches the origin of the state or operation icon to the southeast point on the source icon.</p>
<dt><code>XmATTACH_SOUTH</code></p>
<dd>Attaches the origin of the state or operation icon to the south point on the source icon.</p>
<dt><code>XmATTACH_SOUTH_WEST</code></p>
<dd>Attaches the origin of the state or operation icon to the southwest point on the source icon.</p>
<dt><code>XmATTACH_WEST</code></p>
<dd>Attaches the origin of the state or operation icon to the west point on the source icon.</p>
<dt><code>XmATTACH_CENTER</code></p>
<dd>Attaches the origin of the state or operation icon to the center of the source icon. The <code>XmNoffsetX</code> and <code>XmNoffsetY</code> resources may be used to center the attached icon.</p>
<dt><code>XmATTACH_HOT</code></p>
<dd>Attaches the hotspot coordinates of a state or operation DragIcon to an x,y position on the source icon. The x,y coordinate is taken from the event passed to the <code>XmDragStart</code> function, and made relative to the widget passed as an argument to the same function.</dl>
</dl>
<dt><code>XmNdepth</code></p>
<dd>Specifies the depth of the pixmap.</p>
<dt><code>XmNheight</code></p>
<dd>Specifies the height of the pixmap.</p>
<dt><code>XmNhotX</code></p>
<dd>Specifies the x-coordinate of the hotspot of a cursor DragIcon in relation to the origin of the pixmap bounding box.</p>
<dt><code>XmNhotY</code></p>
<dd>Specifies the y-coordinate of the hotspot of a cursor DragIcon in relation to the origin of the pixmap bounding box.</p>
<dt><code>XmNmask</code></p>
<dd>Specifies a pixmap of depth 1 to use as the DragIcon mask pixmap.</p>
<dt><code>XmNoffsetX</code></p>
<dd>Specifies a horizontal offset (in pixels) of the origin of the state or operation icon relative to the attachment point on the source icon. A positive offset value moves the origin to the right; a negative value moves the origin to the left.</p>
<dt><code>XmNoffsetY</code></p>
<dd>Specifies a vertical offset (in pixels) of the origin of the state or operation icon relative to the attachment point on the source icon. A positive offset value moves the origin down; a negative value moves the origin up.</p>
<dt><code>XmNpixmap</code></p>
<dd>Specifies a pixmap to use as the DragIcon pixmap.</p>
<dt><code>XmNwidth</code></p>
<dd>Specifies the width of the pixmap.</dl>
<h3>Inherited Resources</h3>
<p>DragIcon inherits behavior and a resource from <code>Object</code>. For a complete description of this resource, refer to the <code>Object</code> reference page. </p>
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
<p><code><a href="/docs/linux/man/3-object/">Object</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatedragicon/">XmCreateDragIcon</a></code>(3), <code><a href="/docs/linux/man/3-xmdisplay/">XmDisplay</a></code>(3), <code><a href="/docs/linux/man/3-xmdragcontext/">XmDragContext</a></code>(3), <code><a href="/docs/linux/man/3-xmdropsite/">XmDropSite</a></code>(3), <code><a href="/docs/linux/man/3-xmdroptransfer/">XmDropTransfer</a></code>(3), and <code><a href="/docs/linux/man/3-xmscreen/">XmScreen</a></code>(3).</p>
