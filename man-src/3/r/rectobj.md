---
title: "rectobj(3)"
name: "rectobj"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rectobj/"
description: "RectObj — The RectObj widget class"
---

<p><code>RectObj</code> &#8212; The RectObj widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;</pre>
<h2>Description</h2>
<p>RectObj is never instantiated. Its sole purpose is as a supporting superclass for other widget classes.</p>
<h3>Classes</h3>
<p>RectObj inherits behavior and a resource from <code>Object</code>. </p>
<p> The class pointer is <code>rectObjClass</code>. </p>
<p> The class name is <code>RectObj</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>RectObj Resource Set</code>
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
<td>XmNborderWidth</td>
<td>XmCBorderWidth</td>
<td>Dimension</td>
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
<dl COMPACT>
<dt><code>XmNancestorSensitive</code></p>
<dd>Specifies whether the immediate parent of the gadget receives input events. Use the function <code>XtSetSensitive</code> if you are changing the argument to preserve data integrity (see <code>XmNsensitive</code>). The default is the bitwise AND of the parent&#8217;s <code>XmNsensitive</code> and <code>XmNancestorSensitive</code> resources.</p>
<dt><code>XmNborderWidth</code></p>
<dd>Specifies the width of the border placed around the RectObj&#8217;s rectangular display area.</p>
<dt><code>XmNheight</code></p>
<dd>Specifies the inside height (excluding the border) of the RectObj&#8217;s rectangular display area.</p>
<dt><code>XmNsensitive</code></p>
<dd>Determines whether a RectObj receives input events. If a RectObj is sensitive, the parent dispatches to the gadget all keyboard, mouse button, motion, window enter/leave, and focus events. Insensitive gadgets do not receive these events. Use the function <code>XtSetSensitive</code> to change the sensitivity argument. Using <code>XtSetSensitive</code> ensures that if a parent widget has <code>XmNsensitive</code> set to False, the ancestor-sensitive flag of all its children is appropriately set.</p>
<dt><code>XmNwidth</code></p>
<dd>Specifies the inside width (excluding the border) of the RectObj&#8217;s rectangular display area.</p>
<dt><code>XmNx</code></p>
<dd>Specifies the x-coordinate of the upper left outside corner of the RectObj&#8217;s rectangular display area. The value is relative to the upper left inside corner of the parent window.</p>
<dt><code>XmNy</code></p>
<dd>Specifies the y-coordinate of the upper left outside corner of the RectObj&#8217;s rectangular display area. The value is relative to the upper left inside corner of the parent window.</dl>
<h3>Inherited Resources</h3>
<p>RectObj inherits behavior and a resource from <code>Object</code>. For a description of this resource, refer to the <code>Object</code> reference page. </p>
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
<h3>Translations</h3>
<p>There are no translations for RectObj.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-object/">Object</a></code>(3).</p>
