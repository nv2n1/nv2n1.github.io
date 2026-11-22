---
title: "xmslidecontext(3)"
name: "xmslidecontext"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmslidecontext/"
description: "XmSlideContext – The SlideContext widget class"
---

<p><i>XmSlideContext</i> &#8211; The SlideContext widget class </p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/SlideC.h&gt;</pre>
<h2>Description</h2>
<p>SlideContext can be used to change a widgets geometry over a period of time. </p>
<p> Next paragraph </p>
<p> Next paragraph</p>
<h3>Classes</h3>
<p>SlideContext inherits behavior and resources from the <i>Object</i> class. </p>
<p> The class pointer is <i>XmSlideContextWidgetClass</i>. </p>
<p> The class name is <i>XmSlideContext</i>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a .Xdefaults file, remove the <i>XmN</i> or <i>XmC</i> prefix and use the remaining letters. To specify one of the defined values for a resource in a .Xdefaults file, remove the <i>Xm</i> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <i>XtSetValues</i> (S), retrieved by using <i>XtGetValues</i> (G), or is not applicable (N/A). </p>
<p> <center></p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code><br/>
&nbsp;<wbr>XmSlideContext Resource Set</code>
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
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNslideDestHeight</td>
<td>XtCSlideDestHeight</td>
<td>Dimension</td>
<td>variable</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>XmNslideDestWidth</td>
<td>XtCSlideDestWidth</td>
<td>Dimension</td>
<td>variable</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>XmNslideDestX</td>
<td>XtCSlideDestX</td>
<td>Position</td>
<td>variable</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>XmNslideDestY</td>
<td>XtCSlideDestY</td>
<td>Position</td>
<td>variable</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>XmNslideFinishCallback</td>
<td>XtCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>XmNslideInterval</td>
<td>XtCSlideInterval</td>
<td>int</td>
<td>5</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>XmNslideMotionCallback</td>
<td>XtCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>XmNslideWidget</td>
<td>XtCSlideWidget</td>
<td>Widget</td>
<td>NULL</td>
<td>C
</td>
</tr>
</table>
<p></center> </p>
<dl COMPACT>
<dt><i>XmNslideDestHeight</i></dt>
<dd>If not specified, the current height of XmNslideWidget is used. </dd>
<dt><i>XmNslideDestWidth</i></dt>
<dd>If not specified, the current width of XmNslideWidget is used. </dd>
<dt><i>XmNslideDestX</i></dt>
<dd>If not specified, the current x of XmNslideWidget is used. </dd>
<dt><i>XmNslideDestY</i></dt>
<dd>If not specified, the current y of XmNslideWidget is used. </dd>
<dt><i>XmNslideFinishCallback</i></dt>
<dd>Specifies the list of callbacks that is called when the XmNslideWidget reaches it&#8217;s destination. </dd>
<dt><i>XmNslideInterval</i></dt>
<dd>The time between each geometry change. A value of 0 will set the destination values on the first iteration. </dd>
<dt><i>XmNslideMotionCallback</i></dt>
<dd>Specifies the list of callbacks that is called when the widget geometry changes. </dd>
<dt><i>XmNslideWidget</i></dt>
<dd>The widget to alter. This _must_ be specified during creation. </dd>
</dl>
<h3>Inherited Resources</h3>
<p>SlideContext inherits behavior and resources from the following superclasses. For a complete description of each resource, refer to the man page for that superclass. </p>
<p> <center></p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code><br/>
&nbsp;<wbr>Object Resource Set</code>
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
<td COLSPAN=5>
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
<td>XmNscreen</td>
<td>XmCScreen</td>
<td>Screen *</td>
<td>dynamic</td>
<td>CG
</td>
</tr>
</table>
<p></center> </p>
<h3>Behavior</h3>
<p>XmSlideContext behavior is described below: XmSlideContext installs an Xt timer that is called every XmNslideInterval miliseconds. At each call of the timer proc the XmNslideWidget geometry is adjusted such that the X/Y/Width/Height are 10 percent closer to the final values. The XmSlideContext is automatically destroyed when the XmNslideWidget reaches its destination. If the XmNslideWidget is destroyed before the slide is finished, the XmSlideContext is destroyed. </p>
<h3>Virtual Bindings</h3>
<p>The bindings for virtual keys are vendor specific. For information about bindings for virtual buttons and keys, see <i>VirtualBindings(3X)</i>.</p>
<h2>Related Information</h2>
<p><i>Object(3X)</i>,</p>
