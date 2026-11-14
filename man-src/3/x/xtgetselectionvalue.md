---
title: "xtgetselectionvalue(3)"
name: "xtgetselectionvalue"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtgetselectionvalue/"
description: "XtGetSelectionValue, XtGetSelectionValues – obtain selection values"
---

<p>XtGetSelectionValue, XtGetSelectionValues &#8211; obtain selection values </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtGetSelectionValue(Widget <i>w</i>, Atom <i>selection</i>, Atom <i>target</i>, XtSelectionCallbackProc <i>callback</i>, XtPointer <i>client_data</i>, Time <i>time</i>);</p>
<dd>void XtGetSelectionValues(Widget <i>w</i>, Atom <i>selection</i>, Atom *<i>targets</i>, int <i>count</i>, XtSelectionCallbackProc <i>callback</i>, XtPointer *<i>client_data</i>, Time <i>time</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>callback</i></p>
<dd>Specifies the callback procedure that is to be called when the selection value has been obtained.</p>
<dt><i>client_data</i></p>
<dd>Specifies the argument that is to be passed to the specified procedure when it is called.</p>
<dt><i>client_data</i></p>
<dd>Specifies the client data (one for each target type) that is passed to the callback procedure when it is called for that target.</p>
<dt><i>count</i></p>
<dd>Specifies the length of the targets and client_data lists.</p>
<dt><i>selection</i></p>
<dd>Specifies the particular selection desired (that is, primary or secondary).</p>
<dt><i>target</i></p>
<dd>Specifies the type of the information that is needed about the selection.</p>
<dt><i>targets</i></p>
<dd>Specifies the types of information that is needed about the selection.</p>
<dt><i>time</i></p>
<dd>Specifies the timestamp that indicates when the selection value is desired.</p>
<dt><i>w</i></p>
<dd>Specifies the widget that is making the request.</dl>
<h2>Description</h2>
<p>The <code>XtGetSelectionValue</code> function requests the value of the selection that has been converted to the target type. The specified callback will be called some time after <code>XtGetSelectionValue</code> is called; in fact, it may be called before or after <code>XtGetSelectionValue</code> returns. </p>
<p> The <code>XtGetSelectionValues</code> function is similar to <code>XtGetSelectionValue</code> except that it takes a list of target types and a list of client data and obtains the current value of the selection converted to each of the targets. The effect is as if each target were specified in a separate call to <code>XtGetSelectionValue</code>. The callback is called once with the corresponding client data for each target. <code>XtGetSelectionValues</code> does guarantee that all the conversions will use the same selection value because the ownership of the selection cannot change in the middle of the list, as would be when calling <code>XtGetSelectionValue</code> repeatedly.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtappgetselectiontimeout/">XtAppGetSelectionTimeout</a>(3), <a href="/docs/linux/man/3-xtownselection/">XtOwnSelection</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
