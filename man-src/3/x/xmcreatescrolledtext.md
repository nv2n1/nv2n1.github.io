---
title: "xmcreatescrolledtext(3)"
name: "xmcreatescrolledtext"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmcreatescrolledtext/"
description: "XmCreateScrolledText — The Text ScrolledText convenience creation function"
---

<p><code>XmCreateScrolledText</code> &#8212; The Text ScrolledText convenience creation function</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Text.h&gt;
<code>Widget XmCreateScrolledText</code>(
<code>Widget parent</code>,
<code>String name</code>,
<code>ArgList arglist</code>,
<code>Cardinal argcount</code>);</pre>
<h2>Description</h2>
<p><code>XmCreateScrolledText</code> creates an instance of a Text widget that is contained within a ScrolledWindow. The ScrolledWindow parent is created managed. All ScrolledWindow subarea widgets are automatically created by this function. The ID returned by this function is that of the Text widget (not the ScrolledWindow widget). Use this widget ID for all operations on the Text widget. Use the widget ID of the Text widget&#8217;s parent for all operations on the ScrolledWindow. To obtain the ID of the ScrolledWindow widget associated with the Text widget, use the Xt Intrinsics <code>XtParent</code> function. The name of the ScrolledWindow created by this function is formed by concatenating the letters <code>SW</code> onto the end of the <i>name</i> specified in the parameter list. </p>
<p> The Text widget defaults to single-line text edit; therefore, no ScrollBars are displayed. The Text resource <code>XmNeditMode</code> must be set to <code>XmMULTI_LINE_EDIT</code> to display the ScrollBars. The results of placing a Text widget inside a ScrolledWindow when the Text&#8217;s <code>XmNeditMode</code> is <code>XmSINGLE_LINE_EDIT</code> are undefined. </p>
<p> All arguments to either the Text or the ScrolledWindow widget can be specified at creation time with this function. Changes to initial position and size are sent only to the ScrolledWindow widget. Other resources are sent to the Text or the ScrolledWindow widget as appropriate. Note that the result of providing the <code>XmNdestroyCallback</code> resource in the creation <i>arglist</i> is unspecified. The application should use the <code>XtAddCallback</code> function to add callbacks to the appropriate widget (Text or ScrolledWindow) after creating it. </p>
<p> This function forces the following initial values for ScrolledWindow resources:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd><code>XmNscrollingPolicy</code> is set to <code>XmAPPLICATION_DEFINED</code>.</p>
<dt> &bull;</p>
<dd><code>XmNvisualPolicy</code> is set to <code>XmVARIABLE</code>.</p>
<dt> &bull;</p>
<dd><code>XmNscrollBarDisplayPolicy</code> is set to <code>XmSTATIC</code>.</p>
<dt> &bull;</p>
<dd><code>XmNshadowThickness</code> is set to 0 (zero).</p>
<dt><i>parent</i></p>
<dd>Specifies the parent widget ID</p>
<dt><i>name</i></p>
<dd>Specifies the name of the created widget</p>
<dt><i>arglist</i></p>
<dd>Specifies the argument list</p>
<dt><i>argcount</i></p>
<dd>Specifies the number of attribute/value pairs in the argument list (<i>arglist</i>)</dl>
<p> For a complete definition of Text and its associated resources, see <code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the Text widget ID.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmscrolledwindow/">XmScrolledWindow</a></code>(3) and <code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3).</p>
