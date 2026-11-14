---
title: "xtgetselectionparameters(3)"
name: "xtgetselectionparameters"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtgetselectionparameters/"
description: "XtGetSelectionParameters – retrieve target parameters for a selection request with a single target"
---

<p>XtGetSelectionParameters &#8211; retrieve target parameters for a selection request with a single target </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtGetSelectionParameters(Widget <i>owner</i>, Atom <i>selection</i>, XtRequestId <i>request_id</i>, Atom *<i>type_return</i>, XtPointer *<i>value_return</i>, unsigned long *<i>length_return</i>, int *<i>format_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>owner</i></p>
<dd>Specifies the widget that owns the specified selection.</p>
<dt><i>selection</i></p>
<dd>Specifies the selection being processed.</p>
<dt><i>request_id</i></p>
<dd>Specifies the requestor id in the case of incremental selections, or NULL in the case of atomic transfers.</p>
<dt><i>type_return</i></p>
<dd>Specifies a pointer to an atom in which the property type of the parameters will be stored.</p>
<dt><i>value_return</i></p>
<dd>Specifies a pointer into which a pointer to the parameters are to be stored. A NULL will be stored if no parameters accompany the request.</p>
<dt><i>length_return</i></p>
<dd>Specifies a pointer into which the number of data elements in <i>value_return</i> of size indicated by <i>format_return</i> will be stored.</p>
<dt><i>format_return</i></p>
<dd>Specifies a pointer into which the size in bits of the parameter data in the elements of <i>value_return</i> will be stored.</dl>
<h2>Description</h2>
<p><code>XtGetSelectionParameters</code> may only be called from within an <code>XtConvertSelectionProc</code> or from within the last call to an <code>XtConvertSelectionIncrProc</code> with a new request_id.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtsetselectionparameters/">XtSetSelectionParameters</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
