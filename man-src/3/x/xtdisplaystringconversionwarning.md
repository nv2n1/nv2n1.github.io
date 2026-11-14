---
title: "xtdisplaystringconversionwarning(3)"
name: "xtdisplaystringconversionwarning"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtdisplaystringconversionwarning/"
description: "XtDisplayStringConversionWarning – issue a conversion warning message"
---

<p>XtDisplayStringConversionWarning &#8211; issue a conversion warning message </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtDisplayStringConversionWarning(Display* <i>display</i>, const char *<i>from_value</i>, const char *<i>to_type</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the display connection with which the conversion is associated.</p>
<dt><i>from_value</i></p>
<dd>Specifies the string that could not be converted.</p>
<dt><i>to_type</i></p>
<dd>Specifies the target representation type requested.</dl>
<h2>Description</h2>
<p>The <code>XtDisplayStringConversionWarning</code> function issues a warning message using <code>XtAppWarningMsg</code> with name &#8220;conversionError&#8221;, type &#8220;string&#8221;, class &#8220;XtToolkitError&#8221;, and the default message string &#8220;Cannot convert &quot;<i>from_value</i>&quot; to type <i>to_type</i>&#8221;. </p>
<p> To issue other types of warning or error messages, the type converter should use <code>XtAppWarningMsg</code> or <code>XtAppErrorMsg</code>.</p>
<h2>See Also</h2>
<p><a href="//www.systutorials.com/docs/linux/man/3t-XtAppWarningMsg/">XtAppWarningMsg</a>(3t)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
