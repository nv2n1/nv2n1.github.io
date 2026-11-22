---
title: "xtaddconverter(3)"
name: "xtaddconverter"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtaddconverter/"
description: "XtAppAddConverter, XtAddConverter – register resource converter"
---

<p>XtAppAddConverter, XtAddConverter &#8211; register resource converter </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtAppAddConverter(XtAppContext <i>app_context</i>, const char *<i>from_type</i>, const char *<i>to_type</i>, XtConverter <i>converter</i>, XtConvertArgList <i>convert_args</i>, Cardinal <i>num_args</i>);</dd>
<dd>void XtAddConverter(const char *<i>from_type</i>, const char *<i>to_type</i>, XtConverter <i>converter</i>, XtConvertArgList <i>convert_args</i>, Cardinal <i>num_args</i>);</dd></dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>app_context</i></dt>
<dd>Specifies the application context.</dd>
<dt><i>converter</i></dt>
<dd>Specifies the type converter procedure.</dd>
<dt><i>convert_args</i></dt>
<dd>Specifies how to compute the additional arguments to the converter or NULL.</dd>
<dt><i>from_type</i></dt>
<dd>Specifies the source type.</dd>
<dt><i>num_args</i></dt>
<dd>Specifies the number of additional arguments to the converter or zero.</dd>
<dt><i>to_type</i></dt>
<dd>Specifies the destination type.</dd></dl>
<h2>Description</h2>
<p><code>XtAppAddConverter</code> is equivalent in function to <code>XtAppSetTypeConverter</code> with <i>cache_type</i> equal to <code>XtCacheAll</code> for old-format type converters. It has been superseded by <code>XtAppSetTypeConverter</code>. </p>
<p> <code>XtAddConverter</code> is equivalent in function to <code>XtSetTypeConverter</code> with <i>cache_type</i> equal to <code>XtCacheAll</code> for old-format type converters. It has been superseded by <code>XtSetTypeConverter</code>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtconvert/">XtConvert</a>(3), <a href="/docs/linux/man/3-xtstringconversionwarning/">XtStringConversionWarning</a>(3)<br/>
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br/>
 <i>Xlib &#8211; C Language X Interface</i></p>
