---
title: "xtsettypeconverter(3)"
name: "xtsettypeconverter"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtsettypeconverter/"
description: "XtAppSetTypeConverter, XtSetTypeConverter – register resource converter"
---

<p>XtAppSetTypeConverter, XtSetTypeConverter &#8211; register resource converter </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtAppSetTypeConverter(XtAppContext <i>app_context</i>, const char *<i>from_type</i>, const char * <i>to_type</i>, XtTypeConverter <i>converter</i>, XtConvertArgList <i>convert_args</i>, Cardinal <i>num_args</i>, XtCacheType <i>cache_type</i>, XtDestructor <i>destructor</i>);</p>
<dd>void XtSetTypeConverter(const char *<i>from_type</i>, const char *<i>to_type</i>, XtTypeConverter <i>converter</i>, XtConvertArgList <i>convert_args</i>, Cardinal <i>num_args</i>, XtCacheType <i>cache_type</i>, XtDestructor <i>destructor</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>app_context</i></p>
<dd>Specifies the application context.</p>
<dt><i>converter</i></p>
<dd>Specifies the type converter procedure.</p>
<dt><i>convert_args</i></p>
<dd>Specifies how to compute the additional arguments to the converter or NULL.</p>
<dt><i>from_type</i></p>
<dd>Specifies the source type.</p>
<dt><i>num_args</i></p>
<dd>Specifies the number of additional arguments to the converter or zero.</p>
<dt><i>to_type</i></p>
<dd>Specifies the destination type.</p>
<dt><i>cache_type</i></p>
<dd>Specifies whether or not resources produced by this converter are sharable or display-specific and when they should be freed.</p>
<dt><i>destructor</i></p>
<dd>Specifies a destroy procedure for resources produced by this conversion, or NULL if no additional action is required to deallocate resources produced by the converter.</dl>
<h2>Description</h2>
<p><code>XtSetTypeConverter</code> registers the specified type converter and destructor in all application contexts created by the calling process, including any future application contexts that may be created. <code>XtAppSetTypeConverter</code> registers the specified type converter in the single application context specified. If the same <i>from_type</i> and <i>to_type</i> are specified in multiple calls to either function, the most recent overrides the previous ones.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
