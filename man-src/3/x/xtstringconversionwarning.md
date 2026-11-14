---
title: "xtstringconversionwarning(3)"
name: "xtstringconversionwarning"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtstringconversionwarning/"
description: "XtStringConversionWarning – issue a conversion warning message"
---

<p>XtStringConversionWarning &#8211; issue a conversion warning message </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtStringConversionWarning(const char *<i>src</i>, const char *<i>dst_type</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>src</i></p>
<dd>Specifies the string that could not be converted.</p>
<dt><i>dst_type</i></p>
<dd>Specifies the name of the type to which the string could not be converted.</dl>
<h2>Description</h2>
<p>The <code>XtStringConversionWarning</code> function issues a warning message with name &#8220;conversionError&#8221;, type &#8220;string&#8221;, class &#8220;XtToolkitError&#8221;, and the default message string &#8220;Cannot convert &quot;<i>src</i>&quot; to type <i>dst_type</i>&#8221;. </p>
<p> <code>XtStringConversionWarning</code> has been replaced by <code>XtDisplayStringConversionWarning</code>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtappaddconverter/">XtAppAddConverter</a>(3), <a href="//www.systutorials.com/docs/linux/man/3t-XtAppErrorMsg/">XtAppErrorMsg</a>(3t), <a href="/docs/linux/man/3-xtconvert/">XtConvert</a>(3), <a href="/docs/linux/man/3-xtdisplaystringconversionwarning/">XtDisplayStringConversionWarning</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
