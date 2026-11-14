---
title: "xmselectionboxgetchild(3)"
name: "xmselectionboxgetchild"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmselectionboxgetchild/"
description: "XmSelectionBoxGetChild — A SelectionBox function that is used to access a component"
---

<p><code>XmSelectionBoxGetChild</code> &#8212; A SelectionBox function that is used to access a component</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/SelectioB.h&gt;
<code>Widget XmSelectionBoxGetChild</code>(
<code>Widget widget</code>,
<code>unsigned char child</code>);</pre>
<h2>Description</h2>
<p><code>XmSelectionBoxGetChild</code> is used to access a component within a SelectionBox. The parameters given to the function are the SelectionBox widget and a value indicating which component to access. </p>
<p> NOTE: This routine is obsolete and exists for compatibility with previous releases. Instead of calling <code>XmSelectionBoxGetChild</code>, you should call <code>XtNameToWidget</code> as described in the <code><a href="/docs/linux/man/3-xmselectionbox/">XmSelectionBox</a></code>(3) reference page.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the SelectionBox widget ID.</p>
<dt><i>child</i></p>
<dd>Specifies a component within the SelectionBox. The following values are legal for this parameter:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd><code>XmDIALOG_APPLY_BUTTON</code></p>
<dt> &bull;</p>
<dd><code>XmDIALOG_CANCEL_BUTTON</code></p>
<dt> &bull;</p>
<dd><code>XmDIALOG_DEFAULT_BUTTON</code></p>
<dt> &bull;</p>
<dd><code>XmDIALOG_HELP_BUTTON</code></p>
<dt> &bull;</p>
<dd><code>XmDIALOG_LIST</code></p>
<dt> &bull;</p>
<dd><code>XmDIALOG_LIST_LABEL</code></p>
<dt> &bull;</p>
<dd><code>XmDIALOG_OK_BUTTON</code></p>
<dt> &bull;</p>
<dd><code>XmDIALOG_SELECTION_LABEL</code></p>
<dt> &bull;</p>
<dd><code>XmDIALOG_SEPARATOR</code></p>
<dt> &bull;</p>
<dd><code>XmDIALOG_TEXT</code></p>
<dt> &bull;</p>
<dd><code>XmDIALOG_WORK_AREA</code></dl>
</dl>
</dl>
<p> For a complete definition of SelectionBox and its associated resources, see <code><a href="/docs/linux/man/3-xmselectionbox/">XmSelectionBox</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the widget ID of the specified SelectionBox component. An application should not assume that the returned widget will be of any particular class.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmselectionbox/">XmSelectionBox</a></code>(3).</p>
