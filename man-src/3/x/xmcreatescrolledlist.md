---
title: "xmcreatescrolledlist(3)"
name: "xmcreatescrolledlist"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreatescrolledlist/"
description: "XmCreateScrolledList — The List ScrolledList convenience creation function"
---

<p><code>XmCreateScrolledList</code> &#8212; The List ScrolledList convenience creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/List.h&gt;
<code>Widget XmCreateScrolledList</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmCreateScrolledList</code> creates an instance of a List widget that is contained within a ScrolledWindow. The ScrolledWindow parent is created managed. All ScrolledWindow subarea widgets are automatically created by this function. The ID returned by this function is that of the List widget (not the ScrolledWindow widget). Use this widget ID for all operations on the List widget. Use the widget ID of the List widget&#8217;s parent for all operations on the ScrolledWindow. To obtain the ID of the ScrolledWindow widget associated with the List widget, use the Xt Intrinsics <code>XtParent</code> function. The name of the ScrolledWindow created by this function is formed by concatenating <code>SW</code> onto the end of the <i>name</i> specified in the parameter list. </p>
<p> All arguments to either the List or the ScrolledWindow widget can be specified at creation time using this function. Changes to initial position and size are sent only to the ScrolledWindow widget. Other resources are sent to the List or the ScrolledWindow widget as appropriate. Note that the result of providing the <code>XmNdestroyCallback</code> resource in the creation <i>arglist</i> is unspecified. The application should use the <code>XtAddCallback</code> function to add callbacks to the appropriate widget (List or ScrolledWindow) after creating it. </p>
<p> This function forces the following initial values for ScrolledWindow resources:</p>
<dl COMPACT>
<dt> &bull;</dt>
<dd><code>XmNscrollingPolicy</code> is set to <code>XmAPPLICATION_DEFINED</code>.</dd>
<dt> &bull;</dt>
<dd><code>XmNvisualPolicy</code> is set to <code>XmVARIABLE</code>.</dd>
<dt> &bull;</dt>
<dd><code>XmNscrollBarDisplayPolicy</code> is set to <code>XmSTATIC</code>. (No initial value is forced for the List&#8217;s <code>XmNscrollBarDisplayPolicy</code>.)</dd>
<dt> &bull;</dt>
<dd><code>XmNshadowThickness</code> is set to 0 (zero).</dd>
<dt><i>parent</i></dt>
<dd>Specifies the parent widget ID</dd>
<dt><i>name</i></dt>
<dd>Specifies the name of the created widget</dd>
<dt><i>arglist</i></dt>
<dd>Specifies the argument list</dd>
<dt><i>argcount</i></dt>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>)</dd></dl>
<p> For a complete definition of List and its associated resources, see <code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the List widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3) and <code><a href="/docs/linux/man/3-xmscrolledwindow/">XmScrolledWindow</a></code>(3).</p>
