---
title: "xtconvert(3)"
name: "xtconvert"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtconvert/"
description: "XtConvert, XtDirectConvert – invoke resource converters"
---

<p>XtConvert, XtDirectConvert &#8211; invoke resource converters </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtConvert(Widget <i>w</i>, const char *<i>from_type</i>, XrmValuePtr <i>from</i>, const char *<i>to_type</i>, XrmValuePtr <i>to_return</i>);</dd>
<dd>void XtDirectConvert(XtConverter <i>converter</i>, XrmValuePtr <i>args</i>, Cardinal <i>num_args</i>, XrmValuePtr <i>from</i>, XrmValuePtr <i>to_return</i>);</dd></dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>args</i></dt>
<dd>Specifies the argument list that contains the additional arguments needed to perform the conversion (often NULL).</dd>
<dt><i>converter</i></dt>
<dd>Specifies the conversion procedure that is to be called.</dd>
<dt><i>from</i></dt>
<dd>Specifies the value to be converted.</dd>
<dt><i>from_type</i></dt>
<dd>Specifies the source type.</dd>
<dt><i>num_args</i></dt>
<dd>Specifies the number of additional arguments (often zero).</dd>
<dt><i>to_type</i></dt>
<dd>Specifies the destination type.</dd>
<dt><i>to_return</i></dt>
<dd>Returns the converted value.</dd>
<dt><i>w</i></dt>
<dd>Specifies the widget to use for additional arguments (if any are needed).</dd></dl>
<h2>Description</h2>
<p>The <code>XtConvert</code> function looks up the type converter registered to convert from_type to to_type, computes any additional arguments needed, and then calls <code>XtDirectConvert</code>. <code>XtConvert</code> has been replaced by <code>XtConvertAndStore</code>. </p>
<p> The <code>XtDirectConvert</code> function looks in the converter cache to see if this conversion procedure has been called with the specified arguments. If so, it returns a descriptor for information stored in the cache; otherwise, it calls the converter and enters the result in the cache. </p>
<p> Before calling the specified converter, <code>XtDirectConvert</code> sets the return value size to zero and the return value address to NULL. To determine if the conversion was successful, the client should check to_return.address for non-NULL. <code>XtDirectConvert</code> has been replaced by <code>XtCallConverter</code>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtappaddconverter/">XtAppAddConverter</a>(3), <a href="/docs/linux/man/3-xtstringconversionwarning/">XtStringConversionWarning</a>(3), <a href="/docs/linux/man/3-xtconvertandstore/">XtConvertAndStore</a>(3), <a href="/docs/linux/man/3-xtcallconverter/">XtCallConverter</a>(3)<br/>
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br/>
 <i>Xlib &#8211; C Language X Interface</i></p>
