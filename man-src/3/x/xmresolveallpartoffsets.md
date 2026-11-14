---
title: "xmresolveallpartoffsets(3)"
name: "xmresolveallpartoffsets"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmresolveallpartoffsets/"
description: "XmResolveAllPartOffsets — A function that allows writing of upward-compatible applications and widgets"
---

<p><code>XmResolveAllPartOffsets</code> &#8212; A function that allows writing of upward-compatible applications and widgets</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>void XmResolveAllPartOffsets</code>(
<code>WidgetClass widget_class</code>,
<code>XmOffsetPtr * offset</code>,
<code>XmOffsetPtr * constraint_offset</code>);</pre>
<h2>Description</h2>
<dl COMPACT>
<dd><code>Note: </p>
<p> This routine is obsolete and exists for compatibility with previous releases. You should call XmeResolvePartOffsets</code> instead.</dl>
<p> The use of offset records requires two extra global variables per widget class. The variables consist of pointers to arrays of offsets into the widget record and constraint record for each part of the widget structure. The <code>XmResolveAllPartOffsets</code> function allocates the offset records needed by an application to guarantee upward-compatible access to widget instance and constraint records by applications and widgets. These offset records are used by the widget to access all of the widget&#8217;s variables. A widget needs to take the steps described in the following paragraphs. </p>
<p> Instead of creating a resource list, the widget creates an offset resource list. To accomplish this, use the <code>XmPartResource</code> structure and the <code>XmPartOffset</code> macro. The <code>XmPartResource</code> data structure looks just like a resource list, but instead of having one integer for its offset, it has two shorts. This structure is put into the class record as if it were a normal resource list. Instead of using <code>XtOffset</code> for the offset, the widget uses <code>XmPartOffset</code>. </p>
<p> If the widget is a subclass of the Constraint class and it defines additional constraint resources, create an offset resource list for the constraint part as well. Instead of using <code>XtOffset</code> for the offset, the widget uses <code>XmConstraintPartOffset</code> in the constraint resource list. </p>
<pre><tt>XmPartResource resources[] = {
 { BarNxyz, BarCXyz, XmRBoolean, sizeof(Boolean),
 XmPartOffset(Bar,xyz), XmRImmediate, (XtPointer)False } };
XmPartResource constraints[] = {
 { BarNmaxWidth, BarNMaxWidth,
 XmRDimension, sizeof(Dimension),
 XmConstraintPartOffset(Bar,max_width),
 XmRImmediate, (XtPointer)100 } };</tt></pre>
<p>Instead of putting the widget size in the class record, the widget puts the widget part size in the same field. If the widget is a subclass of the Constraint class, instead of putting the widget constraint record size in the class record, the widget puts the widget constraint part size in the same field. </p>
<p> Instead of putting <code>XtVersion</code> in the class record, the widget puts <code>XtVersionDontCheck</code> in the class record. </p>
<p> Define a variable, of type <code>XmOffsetPtr</code>, to point to the offset record. If the widget is a subclass of the Constraint class, define a variable of type <code>XmOffsetPtr</code> to point to the constraint offset record. These can be part of the widget&#8217;s class record or separate global variables. </p>
<p> In class initialization, the widget calls <code>XmResolveAllPartOffsets</code>, passing it pointers to the class record, the address of the offset record, and the address of the constraint offset record. If the widget not is a subclass of the Constraint class, it should pass NULL as the address of the constraint offset record. This does several things:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd>Adds the superclass (which, by definition, has already been initialized) size field to the part size field</p>
<dt> &bull;</p>
<dd>If the widget is a subclass of the Constraint class, adds the superclass constraint size field to the constraint size field</p>
<dt> &bull;</p>
<dd>Allocates an array based upon the number of superclasses</p>
<dt> &bull;</p>
<dd>If the widget is a subclass of the constraint class, allocates an array for the constraint offset record</p>
<dt> &bull;</p>
<dd>Fills in the offsets of all the widget parts and constraint parts with the appropriate values, determined by examining the size fields of all superclass records</p>
<dt> &bull;</p>
<dd>Uses the part offset array to modify the offset entries in the resource list to be real offsets, in place</dl>
<p> The widget defines a constant that will be the index to its part structure in the offsets array. The value should be 1 greater than the index of the widget&#8217;s superclass. Constants defined for all <code>Xm</code> widgets can be found in <code>XmP.h</code>. </p>
<pre><tt>#define BarIndex (XmBulletinBIndex + 1)</tt></pre>
<p>Instead of accessing fields directly, the widget must always go through the offset table. The <code>XmField</code> and <code>XmConstraintField</code> macros help you access these fields. Because the <code>XmPartOffset</code>, <code>XmConstraintPartOffset</code>, <code>XmField</code>, and <code>XmConstraintField</code> macros concatenate things, you must ensure that there is no space after the part argument. For example, the following macros do not work because of the space after the part (Label) argument: </p>
<pre><tt>XmField(w, offset, Label, text, char *)
XmPartOffset(Label, text).</tt></pre>
<p>Therefore, you must not have any spaces after the part (Label) argument, as illustrated here: </p>
<pre><tt>XmField(w, offset, Label, text, char *)</tt></pre>
<p>You can define macros for each field to make this easier. Assume an integer field <i>xyz</i>: </p>
<pre><tt>#define BarXyz(w) (*(int *)(((char *) w) + \
 offset[BarIndex] + XtOffset(BarPart,xyz)))</tt></pre>
<p>For constraint field <i>max_width</i>: </p>
<pre><tt>#define BarMaxWidth(w) \
 XmConstraintField(w,constraint_offsets,Bar,max_width,Dimension)</tt></pre>
<p>The parameters for <code>XmResolveAllPartOffsets</code> are</p>
<dl COMPACT>
<dt><i>widget_class</i></p>
<dd>Specifies the widget class pointer for the created widget</p>
<dt><i>offset</i></p>
<dd>Returns the offset record</p>
<dt><i>constraint_offset</i></p>
<dd>Returns the constraint offset record</dl>
<h2>Related Information</h2>
<p><code><a href="/docs/linux/man/3-xmresolvepartoffsets/">XmResolvePartOffsets</a></code>(3).</p>
