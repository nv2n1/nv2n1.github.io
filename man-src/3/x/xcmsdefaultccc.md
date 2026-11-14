---
title: "xcmsdefaultccc(3)"
name: "xcmsdefaultccc"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcmsdefaultccc/"
description: "XcmsDefaultCCC – obtain the default CCC for a screen"
---

<p>XcmsDefaultCCC &#8211; obtain the default CCC for a screen </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>XcmsCCC XcmsDefaultCCC(Display *<i>display</i>, int <i>screen_number</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>screen_number</i></p>
<dd>Specifies the appropriate screen number on the host server.</dl>
<h2>Description</h2>
<p>The <code>XcmsDefaultCCC</code> function returns the default CCC for the specified screen. Its visual is the default visual of the screen. Its initial gamut compression and white point adjustment procedures as well as the associated client data are implementation specific.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-displayofccc/">DisplayOfCCC</a>(3), <a href="/docs/linux/man/3-xcmscccofcolormap/">XcmsCCCOfColormap</a>(3), <a href="/docs/linux/man/3-xcmsconvertcolors/">XcmsConvertColors</a>(3), <a href="/docs/linux/man/3-xcmscreateccc/">XcmsCreateCCC</a>(3), <a href="/docs/linux/man/3-xcmssetwhitepoint/">XcmsSetWhitePoint</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
