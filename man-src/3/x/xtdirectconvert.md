---
title: "xtdirectconvert(3)"
name: "xtdirectconvert"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtdirectconvert/"
description: "XtConvert, XtDirectConvert – invoke resource converters"
---

<p>XtConvert, XtDirectConvert &#8211; invoke resource converters </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtConvert(Widget <i>w</i>, const char *<i>from_type</i>, XrmValuePtr <i>from</i>, const char *<i>to_type</i>, XrmValuePtr <i>to_return</i>);</p>
<dd>void XtDirectConvert(XtConverter <i>converter</i>, XrmValuePtr <i>args</i>, Cardinal <i>num_args</i>, XrmValuePtr <i>from</i>, XrmValuePtr <i>to_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>args</i></p>
<dd>Specifies the argument list that contains the additional arguments needed to perform the conversion (often NULL).</p>
<dt><i>converter</i></p>
<dd>Specifies the conversion procedure that is to be called.</p>
<dt><i>from</i></p>
<dd>Specifies the value to be converted.</p>
<dt><i>from_type</i></p>
<dd>Specifies the source type.</p>
<dt><i>num_args</i></p>
<dd>Specifies the number of additional arguments (often zero).</p>
<dt><i>to_type</i></p>
<dd>Specifies the destination type.</p>
<dt><i>to_return</i></p>
<dd>Returns the converted value.</p>
<dt><i>w</i></p>
<dd>Specifies the widget to use for additional arguments (if any are needed).</dl>
<h2>Description</h2>
<p>The <code>XtConvert</code> function looks up the type converter registered to convert from_type to to_type, computes any additional arguments needed, and then calls <code>XtDirectConvert</code>. <code>XtConvert</code> has been replaced by <code>XtConvertAndStore</code>. </p>
<p> The <code>XtDirectConvert</code> function looks in the converter cache to see if this conversion procedure has been called with the specified arguments. If so, it returns a descriptor for information stored in the cache; otherwise, it calls the converter and enters the result in the cache. </p>
<p> Before calling the specified converter, <code>XtDirectConvert</code> sets the return value size to zero and the return value address to NULL. To determine if the conversion was successful, the client should check to_return.address for non-NULL. <code>XtDirectConvert</code> has been replaced by <code>XtCallConverter</code>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtappaddconverter/">XtAppAddConverter</a>(3), <a href="/docs/linux/man/3-xtstringconversionwarning/">XtStringConversionWarning</a>(3), <a href="/docs/linux/man/3-xtconvertandstore/">XtConvertAndStore</a>(3), <a href="/docs/linux/man/3-xtcallconverter/">XtCallConverter</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
