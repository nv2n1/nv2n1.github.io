---
title: "xtreleasegc(3)"
name: "xtreleasegc"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtreleasegc/"
description: "XtGetGC, XtReleaseGC – obtain and destroy a sharable GC"
---

<p>XtGetGC, XtReleaseGC &#8211; obtain and destroy a sharable GC </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>GC XtGetGC(Widget <i>w</i>, XtGCMask <i>value_mask</i>, XGCValues *<i>values</i>);</dd>
<dd>void XtReleaseGC(Widget <i>w</i>, GC <i>gc</i>);</dd></dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>gc</i></dt>
<dd>Specifies the GC to be deallocated.</dd>
<dt><i>values</i></dt>
<dd>Specifies the actual values for this GC.</dd>
<dt><i>value_mask</i></dt>
<dd>Specifies which fields of the values are specified.</dd>
<dt><i>w</i></dt>
<dd>Specifies the widget.</dd></dl>
<h2>Description</h2>
<p>The <code>XtGetGC</code> function returns a sharable, read-only GC. The parameters to this function are the same as those for <code>XCreateGC</code> except that a widget is passed instead of a display. <code>XtGetGC</code> shares only GCs in which all values in the GC returned by <code>XCreateGC</code> are the same. In particular, it does not use the value_mask provided to determine which fields of the GC a widget considers relevant. The value_mask is used only to tell the server which fields should be filled in with widget data and which it should fill in with default values. For further information about value_mask and values, see <code>XCreateGC</code> in the <i>Xlib &#8211; C Language X Interface</i>. </p>
<p> The <code>XtReleaseGC</code> function deallocate the specified shared GC.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br/>
 <i>Xlib &#8211; C Language X Interface</i></p>
