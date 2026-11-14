---
title: "xtsetselectionparameters(3)"
name: "xtsetselectionparameters"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtsetselectionparameters/"
description: "XtSetSelectionParameters – specify target parameters for a selection request with a single target"
---

<p>XtSetSelectionParameters &#8211; specify target parameters for a selection request with a single target </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtSetSelectionParameters(Widget <i>requestor</i>, Atom <i>selection</i>, Atom <i>type</i>, XtPointer <i>value</i>, unsigned long <i>length</i>, int <i>format</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>requestor</i></p>
<dd>Specifies the widget making the request. Must be of class Core or any subclass thereof.</p>
<dt><i>selection</i></p>
<dd>Specifies the atom that names the selection.</p>
<dt><i>type</i></p>
<dd>Specifies the type of the property in which the parameters will be passed.</p>
<dt><i>value</i></p>
<dd>Specifies a pointer to the parameters.</p>
<dt><i>length</i></p>
<dd>Specifies the number of elements containing data in <i>value</i>, each element of a sized indicated by <i>format</i>.</p>
<dt><i>format</i></p>
<dd>Specifies the size in bits of the data in the elements of <i>value</i>.</dl>
<h2>Description</h2>
<p>The specified parameters will be copied and stored in a new property of the specified type and format on the requestor&#8217;s window. To initiate a selection request with a target and these parameters, a subsequent call to <code>XtGetSelectionValue</code> or to <code>XtGetSelectionValueIncremental</code> specifying the same requestor widget and selection atom will generate a <code>ConvertSelection</code> request referring referring to the property containing the parameters. If <code>XtSetSelectionParameters</code> is called more than once with the same widget and selection without a call to specify a request, the most recently specified parameters are used in the subsequent request. </p>
<p> The possible values of <i>format</i> may be 8, 16, or 32. If the <i>format</i> is 8, the elements of <i>value</i> are assumed to be sizeof(char); if 16, sizeof(short); if 32, sizeof(long). </p>
<p> To generate a MULTIPLE target request with parameters for any of the multiple targets of the selection request, precede individual calls to <code>XtGetSelectionValue</code> and <code>XtGetSelectionValueIncremental</code> with corresponding individual calls to <code>XtSetSelectionParameters</code>, and enclose these all within <code>XtCreateSelectionRequest</code> and <code>XtSendSelectionRequest</code>. <code>XtGetSelectionValues</code> and <code>XtGetSelectionValuesIncremental</code> cannot be used to make selection requests with parameterized targets.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtgetselectionparameters/">XtGetSelectionParameters</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
