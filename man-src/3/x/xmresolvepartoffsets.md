---
title: "xmresolvepartoffsets(3)"
name: "xmresolvepartoffsets"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmresolvepartoffsets/"
description: "XmResolvePartOffsets — A function that allows writing of upward-compatible applications and widgets"
---

<p><code>XmResolvePartOffsets</code> &#8212; A function that allows writing of upward-compatible applications and widgets</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>void XmResolvePartOffsets</code>(
<code>WidgetClass widget_class</code>,
<code>XmOffsetPtr * offset</code>);</pre>
<h2>Description</h2>
<p>The use of offset records requires one extra global variable per widget class. The variable consists of a pointer to an array of offsets into the widget record for each part of the widget structure. The <code>XmResolvePartOffsets</code> function allocates the offset records needed by an application to guarantee upward-compatible access to widget instance records by applications and widgets. These offset records are used by the widget to access all of the widget&#8217;s variables. A widget needs to take the steps described in the following paragraphs. </p>
<p> Instead of creating a resource list, the widget creates an offset resource list. To accomplish this, use the <code>XmPartResource</code> structure and the <code>XmPartOffset</code> macro. The <code>XmPartResource</code> data structure looks just like a resource list, but instead of having one integer for its offset, it has two shorts. This structure is put into the class record as if it were a normal resource list. Instead of using <code>XtOffset</code> for the offset, the widget uses <code>XmPartOffset</code>. </p>
<pre><tt>XmPartResource resources[] = {
 { BarNxyz, BarCXyz, XmRBoolean,
 sizeof(Boolean), XmPartOffset(Bar,xyz),
 XmRImmediate, (XtPointer)False }
};</tt></pre>
<p>Instead of putting the widget size in the class record, the widget puts the widget part size in the same field. </p>
<p> Instead of putting <code>XtVersion</code> in the class record, the widget puts <code>XtVersionDontCheck</code> in the class record. </p>
<p> The widget defines a variable, of type <code>XmOffsetPtr</code>, to point to the offset record. This can be part of the widget&#8217;s class record or a separate global variable. </p>
<p> In class initialization, the widget calls <code>XmResolvePartOffsets</code>, passing it a pointer to contain the address of the offset record and the class record. This does several things:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd>Adds the superclass (which, by definition, has already been initialized) size field to the part size field</p>
<dt> &bull;</p>
<dd>Allocates an array based upon the number of superclasses</p>
<dt> &bull;</p>
<dd>Fills in the offsets of all the widget parts with the appropriate values, determined by examining the size fields of all superclass records</p>
<dt> &bull;</p>
<dd>Uses the part offset array to modify the offset entries in the resource list to be real offsets, in place</dl>
<p> The widget defines a constant that will be the index to its part structure in the offsets array. The value should be 1 greater than the index of the widget&#8217;s superclass. Constants defined for all <code>Xm</code> widgets can be found in <code>XmP.h</code>. </p>
<pre><tt>#define BarIndex (XmBulletinBIndex + 1)</tt></pre>
<p>Instead of accessing fields directly, the widget must always go through the offset table. The <code>XmField</code> macro helps you access these fields. Because the <code>XmPartOffset</code> and <code>XmField</code> macros concatenate things together, you must ensure that there is no space after the part argument. For example, the following macros do not work because of the space after the part (Label) argument: </p>
<pre><tt>XmField(w, offset, Label, text, char *)
XmPartOffset(Label, text)</tt></pre>
<p>Therefore, you must not have any spaces after the part (Label) argument, as illustrated here: </p>
<pre><tt>XmField(w, offset, Label, text, char *)</tt></pre>
<p>You can define macros for each field to make this easier. Assume an integer field <i>xyz</i>: </p>
<pre><tt>#define BarXyz(w) (*(int *)(((char *) w) + \
 offset[BarIndex] + XtOffset(BarPart,xyz)))</tt></pre>
<p>The parameters for <code>XmResolvePartOffsets</code> are</p>
<dl COMPACT>
<dt><i>widget_class</i></p>
<dd>Specifies the widget class pointer for the created widget</p>
<dt><i>offset</i></p>
<dd>Returns the offset record</dl>
<h2>Related Information</h2>
<p><code><a href="/docs/linux/man/3-xmresolveallpartoffsets/">XmResolveAllPartOffsets</a></code>(3).</p>
