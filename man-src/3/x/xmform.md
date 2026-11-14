---
title: "xmform(3)"
name: "xmform"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmform/"
description: "XmForm — The Form widget class"
---

<p><code>XmForm</code> &#8212; The Form widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Form.h&gt;</pre>
<h2>Description</h2>
<p>Form is a container widget with no input semantics of its own. Constraints are placed on children of the Form to define attachments for each of the child&#8217;s four sides. These attachments can be to the Form, to another child widget or gadget, to a relative position within the Form, or to the initial position of the child. The attachments determine the layout behavior of the Form when resizing occurs. </p>
<p> The default value for <code>XmNinitialFocus</code> is the value of <code>XmNdefaultButton</code>. </p>
<p> Following are some important considerations in using a Form:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd>Every child must have an attachment on either the left or the right. If initialization or <code>XtSetValues</code> leaves a widget without such an attachment, the result depends upon the value of <code>XmNrubberPositioning</code>.</p>
<dd>If <code>XmNrubberPositioning</code> is False, the child is given an <code>XmNleftAttachment</code> of <code>XmATTACH_FORM</code> and an <code>XmNleftOffset</code> equal to its current <i>x</i> value.</p>
<dd>If <code>XmNrubberPositioning</code> is True, the child is given an <code>XmNleftAttachment</code> of <code>XmATTACH_POSITION</code> and an <code>XmNleftPosition</code> proportional to the current <i>x</i> value divided by the width of the Form.</p>
<dd>In either case, if the child has not been previously given an <i>x</i> value, its <i>x</i> value is taken to be 0 (zero), which places the child at the left side of the Form.</p>
<dt> &bull;</p>
<dd>If you want to create a child without any attachments, and then later (for example, after creating and managing it, but before realizing it) give it a right attachment through <code>XtSetValues</code>, you must set its <code>XmNleftAttachment</code> to <code>XmATTACH_NONE</code> at the same time.</p>
<dt> &bull;</p>
<dd>The <code>XmNresizable</code> resource controls only whether a geometry request by the child will be granted. It has no effect on whether the child&#8217;s size can be changed because of changes in geometry of the Form or of other children.</p>
<dt> &bull;</p>
<dd>Every child has a preferred width, based on geometry requests it makes (whether they are granted or not).</p>
<dt> &bull;</p>
<dd>If a child has attachments on both the left and the right sides, its size is completely controlled by the Form. It can be shrunk below its preferred width or enlarged above it, if necessary, due to other constraints. In addition, the child&#8217;s geometry requests to change its own width may be refused.</p>
<dt> &bull;</p>
<dd>If a child has attachments on only its left or right side, it will always be at its preferred width (if resizable, otherwise at is current width). This may cause it to be clipped by the Form or by other children.</p>
<dt> &bull;</p>
<dd>If a child&#8217;s left (or right) attachment is set to <code>XmATTACH_SELF</code>, its corresponding left (or right) offset is forced to 0 (zero). The attachment is then changed to <code>XmATTACH_POSITION</code>, with a position that corresponds to the <i>x</i> value of the child&#8217;s left (or right) edge. To fix the position of a side at a specific <i>x</i> value, use <code>XmATTACH_FORM</code> or <code>XmATTACH_OPPOSITE_FORM</code> with the <i>x</i> value as the left (or right) offset.</p>
<dt> &bull;</p>
<dd>Unmapping a child has no effect on the Form except that the child is not mapped.</p>
<dt> &bull;</p>
<dd>Unmanaging a child unmaps it. If no other child is attached to it, or if all children attached to it and all children recursively attached to them are also all unmanaged, all of those children are treated as if they did not exist in determining the size of the Form.</p>
<dt> &bull;</p>
<dd>When using <code>XtSetValues</code> to change the <code>XmNx</code> resource of a child, you must simultaneously set its left attachment to either <code>XmATTACH_SELF</code> or <code>XmATTACH_NONE</code>. Otherwise, the request is not granted. If <code>XmNresizable</code> is False, the request is granted only if the child&#8217;s size can remain the same.</p>
<dt> &bull;</p>
<dd>A left (or right) attachment of <code>XmATTACH_WIDGET</code>, where <code>XmNleftWidget</code> (or <code>XmNrightWidget</code>) is NULL, acts like an attachment of <code>XmATTACH_FORM</code>.</p>
<dt> &bull;</p>
<dd>If an attachment is made to a widget that is not a child of the Form, but an ancestor of the widget is a child of the Form, the attachment is made to the ancestor.</dl>
<p> All these considerations are true of top and bottom attachments as well, with top acting like left, bottom acting like right, <i>y</i> acting like <i>x</i>, and height acting like width.</p>
<h3>Classes</h3>
<p>Form inherits behavior, resources, and traits from <code>Core</code>, <code>Composite</code>, <code>Constraint</code>, <code>XmManager</code>, and <code>XmBulletinBoard</code>. </p>
<p> The class pointer is <code>xmFormWidgetClass</code>. </p>
<p> The class name is <code>XmForm</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmForm Resource Set</code>
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
<td>XmNfractionBase</td>
<td>XmCMaxValue</td>
<td>int</td>
<td>100</td>
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
<td>XmNhorizontalSpacing</td>
<td>XmCSpacing</td>
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
<td>XmNrubberPositioning</td>
<td>XmCRubberPositioning</td>
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
<td>XmNverticalSpacing</td>
<td>XmCSpacing</td>
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
<dt><code>XmNfractionBase</code></p>
<dd>Specifies the denominator used in calculating the relative position of a child widget using <code>XmATTACH_POSITION</code> constraints. The value must not be 0 (zero).</p>
<dd>If the value of a child&#8217;s <code>XmNleftAttachment</code> (or <code>XmNrightAttachment</code>) is <code>XmATTACH_POSITION</code>, the position of the left (or right) side of the child is relative to the left side of the Form and is a fraction of the width of the Form. This fraction is the value of the child&#8217;s <code>XmNleftPosition</code> (or <code>XmNrightPosition</code>) resource divided by the value of the Form&#8217;s <code>XmNfractionBase</code>.</p>
<dd>If the value of a child&#8217;s <code>XmNtopAttachment</code> (or <code>XmNbottomAttachment</code>) is <code>XmATTACH_POSITION</code>, the position of the top (or bottom) side of the child is relative to the top side of the Form and is a fraction of the height of the Form. This fraction is the value of the child&#8217;s <code>XmNtopPosition</code> (or <code>XmNbottomPosition</code>) resource divided by the value of the Form&#8217;s <code>XmNfractionBase</code>.</p>
<dt><code>XmNhorizontalSpacing</code></p>
<dd>Specifies the offset for right and left attachments. This resource is only used if no offset resource is specified (when attaching to a widget), or if no margin resource is specified (when attaching to the Form).</p>
<dt><code>XmNrubberPositioning</code></p>
<dd>Indicates the default near (left) and top attachments for a child of the Form. (Note that whether this resource actually applies to the left or right side of the child and its attachment depends on the value of the <code>XmNlayoutDirection</code>.)</p>
<dd>The default left attachment is applied whenever initialization or <code>XtSetValues</code> leaves the child without either a left or right attachment. The default top attachment is applied whenever initialization or <code>XtSetValues</code> leaves the child without either a top or bottom attachment.</p>
<dd>If this Boolean resource is set to False, <code>XmNleftAttachment</code> and <code>XmNtopAttachment</code> default to <code>XmATTACH_FORM</code>, <code>XmNleftOffset</code> defaults to the current <i>x</i> value of the left side of the child, and <code>XmNtopOffset</code> defaults to the current <i>y</i> value of the child. The effect is to position the child according to its absolute distance from the left or top side of the Form.</p>
<dd>If this resource is set to True, <code>XmNleftAttachment</code> and <code>XmNtopAttachment</code> default to <code>XmATTACH_POSITION</code>, <code>XmNleftPosition</code> defaults to a value proportional to the current <i>x</i> value of the left side of the child divided by the width of the Form, and <code>XmNtopPosition</code> defaults to a value proportional to the current <i>y</i> value of the child divided by the height of the Form. The effect is to position the child relative to the left or top side of the Form and in proportion to the width or height of the Form.</p>
<dt><code>XmNverticalSpacing</code></p>
<dd>Specifies the offset for top and bottom attachments. This resource is only used if no offset resource is specified (when attaching to a widget), or if no margin resource is specified (when attaching to the Form).</p>
<dd>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmForm Constraint Resource Set</code>
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
<td>XmNbottomAttachment</td>
<td>XmCAttachment</td>
<td>unsigned char</td>
<td>XmATTACH_NONE</td>
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
<td>XmNbottomOffset</td>
<td>XmCOffset</td>
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
<td>XmNbottomPosition</td>
<td>XmCPosition</td>
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
<td>XmNbottomWidget</td>
<td>XmCWidget</td>
<td>Widget</td>
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
<td>XmNleftAttachment</td>
<td>XmCAttachment</td>
<td>unsigned char</td>
<td>XmATTACH_NONE</td>
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
<td>XmNleftOffset</td>
<td>XmCOffset</td>
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
<td>XmNleftPosition</td>
<td>XmCPosition</td>
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
<td>XmNleftWidget</td>
<td>XmCWidget</td>
<td>Widget</td>
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
<td>XmNresizable</td>
<td>XmCBoolean</td>
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
<td>XmNrightAttachment</td>
<td>XmCAttachment</td>
<td>unsigned char</td>
<td>XmATTACH_NONE</td>
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
<td>XmNrightOffset</td>
<td>XmCOffset</td>
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
<td>XmNrightPosition</td>
<td>XmCPosition</td>
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
<td>XmNrightWidget</td>
<td>XmCWidget</td>
<td>Widget</td>
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
<td>XmNtopAttachment</td>
<td>XmCAttachment</td>
<td>unsigned char</td>
<td>XmATTACH_NONE</td>
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
<td>XmNtopOffset</td>
<td>XmCOffset</td>
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
<td>XmNtopPosition</td>
<td>XmCPosition</td>
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
<td>XmNtopWidget</td>
<td>XmCWidget</td>
<td>Widget</td>
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
</table>
</table>
<dt><code>XmNbottomAttachment</code></p>
<dd>Specifies attachment of the bottom side of the child. It can have the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmATTACH_NONE</code></p>
<dd>Do not attach the bottom side of the child.</p>
<dt><code>XmATTACH_FORM</code></p>
<dd>Attach the bottom side of the child to the bottom side of the Form.</p>
<dt><code>XmATTACH_OPPOSITE_FORM</code></p>
<dd>Attach the bottom side of the child to the top side of the Form. <code>XmNbottomOffset</code> can be used to determine the visibility of the child.</p>
<dt><code>XmATTACH_WIDGET</code></p>
<dd>Attach the bottom side of the child to the top side of the widget or gadget specified in the <code>XmNbottomWidget</code> resource. If <code>XmNbottomWidget</code> is NULL, <code>XmATTACH_WIDGET</code> is replaced by <code>XmATTACH_FORM</code>, and the child is attached to the bottom side of the Form.</p>
<dt><code>XmATTACH_OPPOSITE_WIDGET</code></p>
<dd>Attach the bottom side of the child to the bottom side of the widget or gadget specified in the <code>XmNbottomWidget</code> resource.</p>
<dt><code>XmATTACH_POSITION</code></p>
<dd>Attach the bottom side of the child to a position that is relative to the top side of the Form and in proportion to the height of the Form. This position is determined by the <code>XmNbottomPosition</code> and <code>XmNfractionBase</code> resources.</p>
<dt><code>XmATTACH_SELF</code></p>
<dd>Attach the bottom side of the child to a position that is proportional to the current <i>y</i> value of the bottom of the child divided by the height of the Form. This position is determined by the <code>XmNbottomPosition</code> and <code>XmNfractionBase</code> resources. <code>XmNbottomPosition</code> is set to a value proportional to the current <i>y</i> value of the bottom of the child divided by the height of the Form.</dl>
</dl>
<dt><code>XmNbottomOffset</code></p>
<dd>Specifies the constant offset between the bottom side of the child and the object to which it is attached. The relationship established remains, regardless of any resizing operations that occur. When this resource is explicitly set, the value of <code>XmNverticalSpacing</code> is ignored.</p>
<dt><code>XmNbottomPosition</code></p>
<dd>This resource is used to determine the position of the bottom side of the child when the child&#8217;s <code>XmNbottomAttachment</code> is set to <code>XmATTACH_POSITION</code>. In this case the position of the bottom side of the child is relative to the top side of the Form and is a fraction of the height of the Form. This fraction is the value of the child&#8217;s <code>XmNbottomPosition</code> resource divided by the value of the Form&#8217;s <code>XmNfractionBase</code>. For example, if the child&#8217;s <code>XmNbottomPosition</code> is 50, the Form&#8217;s <code>XmNfractionBase</code> is 100, and the Form&#8217;s height is 200, the position of the bottom side of the child is 100.</p>
<dt><code>XmNbottomWidget</code></p>
<dd>Specifies the widget or gadget to which the bottom side of the child is attached. This resource is used if the <code>XmNbottomAttachment</code> resource is set to either <code>XmATTACH_WIDGET</code> or <code>XmATTACH_OPPOSITE_WIDGET</code>.</p>
<dd>A string-to-widget resource converter is automatically installed for use with this resource. With this converter, the widget that is to be the value of the resource must exist at the time the widget that has the resource is created.</p>
<dt><code>XmNleftAttachment</code></p>
<dd>Specifies attachment of the near (left) side of the child. (Note that whether this resource actually applies to the left or right side of the child and its attachment depends on the value of the <code>XmNlayoutDirection</code> resource.) It can have the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmATTACH_NONE</code></p>
<dd>Do not attach the left side of the child. If <code>XmNrightAttachment</code> is also <code>XmATTACH_NONE</code>, this value is ignored and the child is given a default left attachment.</p>
<dt><code>XmATTACH_FORM</code></p>
<dd>Attach the left side of the child to the left side of the Form.</p>
<dt><code>XmATTACH_OPPOSITE_FORM</code></p>
<dd>Attach the left side of the child to the right side of the Form. <code>XmNleftOffset</code> can be used to determine the visibility of the child.</p>
<dt><code>XmATTACH_WIDGET</code></p>
<dd>Attach the left side of the child to the right side of the widget or gadget specified in the <code>XmNleftWidget</code> resource. If <code>XmNleftWidget</code> is NULL, <code>XmATTACH_WIDGET</code> is replaced by <code>XmATTACH_FORM</code>, and the child is attached to the left side of the Form.</p>
<dt><code>XmATTACH_OPPOSITE_WIDGET</code></p>
<dd>Attach the left side of the child to the left side of the widget or gadget specified in the <code>XmNleftWidget</code> resource.</p>
<dt><code>XmATTACH_POSITION</code></p>
<dd>Attach the left side of the child to a position that is relative to the left side of the Form and in proportion to the width of the Form. This position is determined by the <code>XmNleftPosition</code> and <code>XmNfractionBase</code> resources.</p>
<dt><code>XmATTACH_SELF</code></p>
<dd>Attach the left side of the child to a position that is proportional to the current <i>x</i> value of the left side of the child divided by the width of the Form. This position is determined by the <code>XmNleftPosition</code> and <code>XmNfractionBase</code> resources. <code>XmNleftPosition</code> is set to a value proportional to the current <i>x</i> value of the left side of the child divided by the width of the Form.</dl>
</dl>
<dt><code>XmNleftOffset</code></p>
<dd>Specifies the constant offset between the near (left) side of the child and the object to which it is attached. (Note that whether this resource actually applies to the left or right side of the child and its attachment depends on the value of the <code>XmNlayoutDirection</code> resource.) The relationship established remains, regardless of any resizing operations that occur. When this resource is explicitly set, the value of <code>XmNhorizontalSpacing</code> is ignored.</p>
<dt><code>XmNleftPosition</code></p>
<dd>This resource is used to determine the position of the near (left) side of the child when the child&#8217;s <code>XmNleftAttachment</code> is set to <code>XmATTACH_POSITION</code>. (Note that whether this resource actually applies to the left or right side of the child and its attachment depends on the value of the <code>XmNlayoutDirection</code> resource.)</p>
<dd>In this case, the position of the left side of the child is relative to the left side of the Form and is a fraction of the width of the Form. This fraction is the value of the child&#8217;s <code>XmNleftPosition</code> resource divided by the value of the Form&#8217;s <code>XmNfractionBase</code>. For example, if the child&#8217;s <code>XmNleftPosition</code> is 50, the Form&#8217;s <code>XmNfractionBase</code> is 100, and the Form&#8217;s width is 200, the position of the left side of the child is 100.</p>
<dt><code>XmNleftWidget</code></p>
<dd>Specifies the widget or gadget to which the near (left) side of the child is attached. (Note that whether this resource actually applies to the left or right side of the child and its attachment depends on the value of the <code>XmNlayoutDirection</code> resource.) The <code>XmNleftWidget</code> resource is used if the <code>XmNleftAttachment</code> resource is set to either <code>XmATTACH_WIDGET</code> or <code>XmATTACH_OPPOSITE_WIDGET</code>.</p>
<dd>A string-to-widget resource converter is automatically installed for use with this resource. With this converter, the widget that is to be the value of the resource must exist at the time the widget that has the resource is created.</p>
<dt><code>XmNresizable</code></p>
<dd>This Boolean resource specifies whether or not a child&#8217;s request for a new size is (conditionally) granted by the Form. If this resource is set to True the request is granted if possible. If this resource is set to False the request is always refused.</p>
<dd>If a child has both left and right attachments, its width is completely controlled by the Form, regardless of the value of the child&#8217;s <code>XmNresizable</code> resource. If a child has a left or right attachment but not both, the child&#8217;s <code>XmNwidth</code> is used in setting its width if the value of the child&#8217;s <code>XmNresizable</code> resource is True. These conditions are also true for top and bottom attachments, with height acting like width.</p>
<dt><code>XmNrightAttachment</code></p>
<dd>Specifies attachment of the far (right) side of the child. (Note that whether this resource actually applies to the left or right side of the child and its attachment depends on the value of the <code>XmNlayoutDirection</code> resource.) It can have the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmATTACH_NONE</code></p>
<dd>Do not attach the right side of the child.</p>
<dt><code>XmATTACH_FORM</code></p>
<dd>Attach the right side of the child to the right side of the Form.</p>
<dt><code>XmATTACH_OPPOSITE_FORM</code></p>
<dd>Attach the right side of the child to the left side of the Form. <code>XmNrightOffset</code> can be used to determine the visibility of the child.</p>
<dt><code>XmATTACH_WIDGET</code></p>
<dd>Attach the right side of the child to the left side of the widget or gadget specified in the <code>XmNrightWidget</code> resource. If <code>XmNrightWidget</code> is NULL, <code>XmATTACH_WIDGET</code> is replaced by <code>XmATTACH_FORM</code>, and the child is attached to the right side of the Form.</p>
<dt><code>XmATTACH_OPPOSITE_WIDGET</code></p>
<dd>Attach the right side of the child to the right side of the widget or gadget specified in the <code>XmNrightWidget</code> resource.</p>
<dt><code>XmATTACH_POSITION</code></p>
<dd>Attach the right side of the child to a position that is relative to the left side of the Form and in proportion to the width of the Form. This position is determined by the <code>XmNrightPosition</code> and <code>XmNfractionBase</code> resources.</p>
<dt><code>XmATTACH_SELF</code></p>
<dd>Attach the right side of the child to a position that is proportional to the current <i>x</i> value of the right side of the child divided by the width of the Form. This position is determined by the <code>XmNrightPosition</code> and <code>XmNfractionBase</code> resources. <code>XmNrightPosition</code> is set to a value proportional to the current <i>x</i> value of the right side of the child divided by the width of the Form.</dl>
</dl>
<dt><code>XmNrightOffset</code></p>
<dd>Specifies the constant offset between the far (right) side of the child and the object to which it is attached. (Note that whether this resource actually applies to the left or right side of the child and its attachment depends on the value of the <code>XmNlayoutDirection</code> resource.) The relationship established remains, regardless of any resizing operations that occur. When this resource is explicitly set, the value of <code>XmNhorizontalSpacing</code> is ignored.</p>
<dt><code>XmNrightPosition</code></p>
<dd>This resource is used to determine the position of the far (right) side of the child when the child&#8217;s <code>XmNrightAttachment</code> is set to <code>XmATTACH_POSITION</code>. (Note that whether this resource actually applies to the left or right side of the child and its attachment depends on the value of the <code>XmNlayoutDirection</code> resource.)</p>
<dd>In this case the position of the right side of the child is relative to the left side of the Form and is a fraction of the width of the Form. This fraction is the value of the child&#8217;s <code>XmNrightPosition</code> resource divided by the value of the Form&#8217;s <code>XmNfractionBase</code>. For example, if the child&#8217;s <code>XmNrightPosition</code> is 50, the Form&#8217;s <code>XmNfractionBase</code> is 100, and the Form&#8217;s width is 200, the position of the right side of the child is 100.</p>
<dt><code>XmNrightWidget</code></p>
<dd>Specifies the widget or gadget to which the far (right) side of the child is attached. (Note that whether this resource actually applies to the left or right side of the child and its attachment depends on the value of the <code>XmNlayoutDirection</code> resource.) The <code>XmNrightWidget</code> resource is used if the <code>XmNrightAttachment</code> resource is set to either <code>XmATTACH_WIDGET</code> or <code>XmATTACH_OPPOSITE_WIDGET</code>.</p>
<dd>A string-to-widget resource converter is automatically installed for use with this resource. With this converter, the widget that is to be the value of the resource must exist at the time the widget that has the resource is created.</p>
<dt><code>XmNtopAttachment</code></p>
<dd>Specifies attachment of the top side of the child. It can have following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmATTACH_NONE</code></p>
<dd>Do not attach the top side of the child. If the <code>XmNbottomAttachment</code> resource is also <code>XmATTACH_NONE</code>, this value is ignored and the child is given a default top attachment.</p>
<dt><code>XmATTACH_FORM</code></p>
<dd>Attach the top side of the child to the top side of the Form.</p>
<dt><code>XmATTACH_OPPOSITE_FORM</code></p>
<dd>Attach the top side of the child to the bottom side of the Form. <code>XmNtopOffset</code> can be used to determine the visibility of the child.</p>
<dt><code>XmATTACH_WIDGET</code></p>
<dd>Attach the top side of the child to the bottom side of the widget or gadget specified in the <code>XmNtopWidget</code> resource. If <code>XmNtopWidget</code> is NULL, <code>XmATTACH_WIDGET</code> is replaced by <code>XmATTACH_FORM</code> and the child is attached to the top side of the Form.</p>
<dt><code>XmATTACH_OPPOSITE_WIDGET</code></p>
<dd>Attach the top side of the child to the top side of the widget or gadget specified in the <code>XmNtopWidget</code> resource.</p>
<dt><code>XmATTACH_POSITION</code></p>
<dd>Attach the top side of the child to a position that is relative to the top side of the Form and in proportion to the height of the Form. This position is determined by the <code>XmNtopPosition</code> and <code>XmNfractionBase</code> resources.</p>
<dt><code>XmATTACH_SELF</code></p>
<dd>Attach the top side of the child to a position that is proportional to the current <i>y</i> value of the child divided by the height of the Form. This position is determined by the <code>XmNtopPosition</code> and <code>XmNfractionBase</code> resources. <code>XmNtopPosition</code> is set to a value proportional to the current <i>y</i> value of the child divided by the height of the Form.</dl>
</dl>
<dt><code>XmNtopOffset</code></p>
<dd>Specifies the constant offset between the top side of the child and the object to which it is attached. The relationship established remains, regardless of any resizing operations that occur. When this resource is explicitly set, the value of <code>XmNverticalSpacing</code> is ignored.</p>
<dt><code>XmNtopPosition</code></p>
<dd>This resource is used to determine the position of the top side of the child when the child&#8217;s <code>XmNtopAttachment</code> is set to <code>XmATTACH_POSITION</code>. In this case, the position of the top side of the child is relative to the top side of the Form and is a fraction of the height of the Form. This fraction is the value of the child&#8217;s <code>XmNtopPosition</code> resource divided by the value of the Form&#8217;s <code>XmNfractionBase</code>. For example, if the child&#8217;s <code>XmNtopPosition</code> is 50, the Form&#8217;s <code>XmNfractionBase</code> is 100, and the Form&#8217;s height is 200, the position of the top side of the child is 100.</p>
<dt><code>XmNtopWidget</code></p>
<dd>Specifies the widget or gadget to which the top side of the child is attached. This resource is used if <code>XmNtopAttachment</code> is set to a value of either <code>XmATTACH_WIDGET</code> or <code>XmATTACH_OPPOSITE_WIDGET</code>.</p>
<dd>A string-to-widget resource converter is automatically installed for use with this resource. With this converter, the widget that is to be the value of the resource must exist at the time the widget that has the resource is created.</dl>
<h3>Inherited Resources</h3>
<p>Form inherits behavior and resources from the superclasses described in the following tables. For a complete description of each resource, refer to the reference page for that superclass. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmBulletinBoard Resource Set</code>
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
<td>XmNallowOverlap</td>
<td>XmCAllowOverlap</td>
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
<td>XmNautoUnmanage</td>
<td>XmCAutoUnmanage</td>
<td>Boolean</td>
<td>True</td>
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
<td>XmNbuttonFontList</td>
<td>XmCButtonFontList</td>
<td>XmFontList</td>
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
<td>XmNbuttonRenderTable</td>
<td>XmCButtonRenderTable</td>
<td>XmRenderTable</td>
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
<td>XmNcancelButton</td>
<td>XmCWidget</td>
<td>Widget</td>
<td>NULL</td>
<td>SG
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
<td>XmNdefaultButton</td>
<td>XmCWidget</td>
<td>Widget</td>
<td>NULL</td>
<td>SG
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
<td>XmNdefaultPosition</td>
<td>XmCDefaultPosition</td>
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
<td>XmNdialogStyle</td>
<td>XmCDialogStyle</td>
<td>unsigned char</td>
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
<td>XmNdialogTitle</td>
<td>XmCDialogTitle</td>
<td>XmString</td>
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
<td>XmNfocusCallback</td>
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
<td>XmNlabelFontList</td>
<td>XmCLabelFontList</td>
<td>XmFontList</td>
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
<td>XmNlabelRenderTable</td>
<td>XmCLabelRenderTable</td>
<td>XmRenderTable</td>
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
<td>XmNmapCallback</td>
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
<td>XmNmarginHeight</td>
<td>XmCMarginHeight</td>
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
<td>XmNmarginWidth</td>
<td>XmCMarginWidth</td>
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
<td>XmNnoResize</td>
<td>XmCNoResize</td>
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
<td>XmNresizePolicy</td>
<td>XmCResizePolicy</td>
<td>unsigned char</td>
<td>XmRESIZE_ANY</td>
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
<td>XmNshadowType</td>
<td>XmCShadowType</td>
<td>unsigned char</td>
<td>XmSHADOW_OUT</td>
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
<td>XmNtextFontList</td>
<td>XmCTextFontList</td>
<td>XmFontList</td>
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
<td>XmNtextRenderTable</td>
<td>XmCTextRenderTable</td>
<td>XmRenderTable</td>
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
<td>XmNtextTranslations</td>
<td>XmCTranslations</td>
<td>XtTranslations</td>
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
<td>XmNunmapCallback</td>
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
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmManager Resource Set</code>
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
<td>XmNbottomShadowColor</td>
<td>XmCBottomShadowColor</td>
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
<td>XmNbottomShadowPixmap</td>
<td>XmCBottomShadowPixmap</td>
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
<td>XmNforeground</td>
<td>XmCForeground</td>
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
<td>XmNhelpCallback</td>
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
<td>XmNhighlightColor</td>
<td>XmCHighlightColor</td>
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
<td>XmNhighlightPixmap</td>
<td>XmCHighlightPixmap</td>
<td>Pixmap</td>
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
<td>XmNinitialFocus</td>
<td>XmCInitialFocus</td>
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
<td>XmNlayoutDirection</td>
<td>XmCLayoutDirection</td>
<td>XmDirection</td>
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
<td>XmNnavigationType</td>
<td>XmCNavigationType</td>
<td>XmNavigationType</td>
<td>XmTAB_GROUP</td>
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
<td>XmNpopupHandlerCallback</td>
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
<td>XmNshadowThickness</td>
<td>XmCShadowThickness</td>
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
<td>XmNstringDirection</td>
<td>XmCStringDirection</td>
<td>XmStringDirection</td>
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
<td>XmNtopShadowColor</td>
<td>XmCTopShadowColor</td>
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
<td>XmNtopShadowPixmap</td>
<td>XmCTopShadowPixmap</td>
<td>Pixmap</td>
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
<td>XmNtraversalOn</td>
<td>XmCTraversalOn</td>
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
<td>XmNunitType</td>
<td>XmCUnitType</td>
<td>unsigned char</td>
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
<td>XmNuserData</td>
<td>XmCUserData</td>
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
</table>
</table>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>Composite Resource Set</code>
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
<td>XmNchildren</td>
<td>XmCReadOnly</td>
<td>WidgetList</td>
<td>NULL</td>
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
<td>XmNinsertPosition</td>
<td>XmCInsertPosition</td>
<td>XtOrderProc</td>
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
<td>XmNnumChildren</td>
<td>XmCReadOnly</td>
<td>Cardinal</td>
<td>0</td>
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
</table>
</table>
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
<td>N/A
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
<h3>Translations</h3>
<p>XmForm inherits translations from XmBulletinBoard.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-composite/">Composite</a></code>(3), <code><a href="/docs/linux/man/3-constraint/">Constraint</a></code>(3), <code><a href="/docs/linux/man/3-core/">Core</a></code>(3), <code><a href="/docs/linux/man/3-xmbulletinboard/">XmBulletinBoard</a></code>(3), <code>XmCreateForm</code>, <code><a href="/docs/linux/man/3-xmcreateformdialog/">XmCreateFormDialog</a></code>(3), <code><a href="/docs/linux/man/3-xmmanager/">XmManager</a></code>(3), <code>XmVaCreateForm</code>, and <code>XmVaCreateManagedForm</code>.</p>
