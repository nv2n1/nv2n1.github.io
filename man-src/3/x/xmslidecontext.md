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
<td ALIGN=center COLSPAN=5><font SIZE="-9"><code><br />
&nbsp;<wbr>XmSlideContext Resource Set</code></font>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9"><code>Name</code></font></td>
<td><font SIZE="-9"><code>Class</code></font></td>
<td><font SIZE="-9"><code>Type</code></font></td>
<td><font SIZE="-9"><code>Default</code></font></td>
<td><font SIZE="-9"><code>Access</code></font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNslideDestHeight</font></td>
<td><font SIZE="-9">XtCSlideDestHeight</font></td>
<td><font SIZE="-9">Dimension</font></td>
<td><font SIZE="-9">variable</font></td>
<td><font SIZE="-9">C</font>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNslideDestWidth</font></td>
<td><font SIZE="-9">XtCSlideDestWidth</font></td>
<td><font SIZE="-9">Dimension</font></td>
<td><font SIZE="-9">variable</font></td>
<td><font SIZE="-9">C</font>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNslideDestX</font></td>
<td><font SIZE="-9">XtCSlideDestX</font></td>
<td><font SIZE="-9">Position</font></td>
<td><font SIZE="-9">variable</font></td>
<td><font SIZE="-9">C</font>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNslideDestY</font></td>
<td><font SIZE="-9">XtCSlideDestY</font></td>
<td><font SIZE="-9">Position</font></td>
<td><font SIZE="-9">variable</font></td>
<td><font SIZE="-9">C</font>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNslideFinishCallback</font></td>
<td><font SIZE="-9">XtCCallback</font></td>
<td><font SIZE="-9">XtCallbackList</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">C</font>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNslideInterval</font></td>
<td><font SIZE="-9">XtCSlideInterval</font></td>
<td><font SIZE="-9">int</font></td>
<td><font SIZE="-9">5</font></td>
<td><font SIZE="-9">C</font>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNslideMotionCallback</font></td>
<td><font SIZE="-9">XtCCallback</font></td>
<td><font SIZE="-9">XtCallbackList</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">C</font>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNslideWidget</font></td>
<td><font SIZE="-9">XtCSlideWidget</font></td>
<td><font SIZE="-9">Widget</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">C</font>
</td>
</tr>
</table>
<p></center> </p>
<dl COMPACT>
<dt><i>XmNslideDestHeight</i></p>
<dd>If not specified, the current height of XmNslideWidget is used. </p>
<dt><i>XmNslideDestWidth</i></p>
<dd>If not specified, the current width of XmNslideWidget is used. </p>
<dt><i>XmNslideDestX</i></p>
<dd>If not specified, the current x of XmNslideWidget is used. </p>
<dt><i>XmNslideDestY</i></p>
<dd>If not specified, the current y of XmNslideWidget is used. </p>
<dt><i>XmNslideFinishCallback</i></p>
<dd>Specifies the list of callbacks that is called when the XmNslideWidget reaches it&#8217;s destination. </p>
<dt><i>XmNslideInterval</i></p>
<dd>The time between each geometry change. A value of 0 will set the destination values on the first iteration. </p>
<dt><i>XmNslideMotionCallback</i></p>
<dd>Specifies the list of callbacks that is called when the widget geometry changes. </p>
<dt><i>XmNslideWidget</i></p>
<dd>The widget to alter. This _must_ be specified during creation. </p>
</dl>
<h3>Inherited Resources</h3>
<p>SlideContext inherits behavior and resources from the following superclasses. For a complete description of each resource, refer to the man page for that superclass. </p>
<p> <center></p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><font SIZE="-9"><code><br />
&nbsp;<wbr>Object Resource Set</code></font>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9"><code>Name</code></font></td>
<td><font SIZE="-9"><code>Class</code></font></td>
<td><font SIZE="-9"><code>Type</code></font></td>
<td><font SIZE="-9"><code>Default</code></font></td>
<td><font SIZE="-9"><code>Access</code></font>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNdestroyCallback</font></td>
<td><font SIZE="-9">XmCCallback</font></td>
<td><font SIZE="-9">XtCallbackList</font></td>
<td><font SIZE="-9">NULL</font></td>
<td><font SIZE="-9">C</font>
</td>
</tr>
<tr VALIGN=top>
<td><font SIZE="-9">XmNscreen</font></td>
<td><font SIZE="-9">XmCScreen</font></td>
<td><font SIZE="-9">Screen *</font></td>
<td><font SIZE="-9">dynamic</font></td>
<td><font SIZE="-9">CG</font>
</td>
</tr>
</table>
<p></center> </p>
<h3>Behavior</h3>
<p>XmSlideContext behavior is described below: XmSlideContext installs an Xt timer that is called every XmNslideInterval miliseconds. At each call of the timer proc the XmNslideWidget geometry is adjusted such that the X/Y/Width/Height are 10 percent closer to the final values. The XmSlideContext is automatically destroyed when the XmNslideWidget reaches its destination. If the XmNslideWidget is destroyed before the slide is finished, the XmSlideContext is destroyed. </p>
<h3>Virtual Bindings</h3>
<p>The bindings for virtual keys are vendor specific. For information about bindings for virtual buttons and keys, see <i><a href="//www.systutorials.com/docs/linux/man/3X-VirtualBindings/">VirtualBindings</a>(3X)</i>.</p>
<h2>Related Information</h2>
<p><i><a href="//www.systutorials.com/docs/linux/man/3X-Object/">Object</a>(3X)</i>,</p>
