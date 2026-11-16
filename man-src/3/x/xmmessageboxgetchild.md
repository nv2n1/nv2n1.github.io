---
title: "xmmessageboxgetchild(3)"
name: "xmmessageboxgetchild"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmmessageboxgetchild/"
description: "XmMessageBoxGetChild — A MessageBox function that is used to access a component"
---

<p><code>XmMessageBoxGetChild</code> &#8212; A MessageBox function that is used to access a component</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/MessageB.h&gt;
<code>Widget XmMessageBoxGetChild</code>(
<code>Widget widget</code>,
<code>unsigned char child</code>);</pre>
<h2>Description</h2>
<p><code>XmMessageBoxGetChild</code> is used to access a component within a MessageBox. The parameters given to the function are the MessageBox widget and a value indicating which component to access. </p>
<p> NOTE: This routine is obsolete and exists for compatibility with previous releases. Instead of calling <code>XmMessageBoxGetChild</code>, you should call <code>XtNameToWidget</code> as described in the <code><a href="/docs/linux/man/3-xmmessagebox/">XmMessageBox</a></code>(3) reference page.</p>
<dl COMPACT>
<dt><i>widget</i></dt>
<dd>Specifies the MessageBox widget ID.</dd>
<dt><i>child</i></dt>
<dd>Specifies a component within the MessageBox. The following are legal values for this parameter:</dd>
<dl COMPACT>
<dd>
</dd><dl COMPACT>
<dt> &bull;</dt>
<dd><code>XmDIALOG_CANCEL_BUTTON</code></dd>
<dt> &bull;</dt>
<dd><code>XmDIALOG_DEFAULT_BUTTON</code></dd>
<dt> &bull;</dt>
<dd><code>XmDIALOG_HELP_BUTTON</code></dd>
<dt> &bull;</dt>
<dd><code>XmDIALOG_MESSAGE_LABEL</code></dd>
<dt> &bull;</dt>
<dd><code>XmDIALOG_OK_BUTTON</code></dd>
<dt> &bull;</dt>
<dd><code>XmDIALOG_SEPARATOR</code></dd>
<dt> &bull;</dt>
<dd><code>XmDIALOG_SYMBOL_LABEL</code></dd></dl>
</dl>
</dl>
<p> For a complete definition of MessageBox and its associated resources, see <code><a href="/docs/linux/man/3-xmmessagebox/">XmMessageBox</a></code>(3).</p>
<h2>Return</h2>
<p>Returns the widget ID of the specified MessageBox component. An application should not assume that the returned widget will be of any particular class.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmmessagebox/">XmMessageBox</a></code>(3).</p>
