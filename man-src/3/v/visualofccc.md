---
title: "visualofccc(3)"
name: "visualofccc"
section: "3"
letter: "v"
url: "/docs/linux/man/3-visualofccc/"
description: "DisplayOfCCC, VisualOfCCC, ScreenNumberOfCCC, ScreenWhitePointOfCCC, ClientWhitePointOfCCC – Color Conversion Context macros"
---

<p>DisplayOfCCC, VisualOfCCC, ScreenNumberOfCCC, ScreenWhitePointOfCCC, ClientWhitePointOfCCC &#8211; Color Conversion Context macros </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>Display *DisplayOfCCC(XcmsCCC <i>ccc</i>);</p>
<dd>Visual *VisualOfCCC(XcmsCCC <i>ccc</i>);</p>
<dd>int ScreenNumberOfCCC(XcmsCCC <i>ccc</i>);</p>
<dd>XcmsColor *ScreenWhitePointOfCCC(XcmsCCC <i>ccc</i>);</p>
<dd>XcmsColor *ClientWhitePointOfCCC(XcmsCCC <i>ccc</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>ccc</i></p>
<dd>Specifies the CCC.</dl>
<h2>Description</h2>
<p>The <code>DisplayOfCCC</code> macro returns the display associated with the specified CCC. </p>
<p> The <code>VisualOfCCC</code> macro returns the visual associated with the specified CCC. </p>
<p> The <code>ScreenNumberOfCCC</code> macro returns the number of the screen associated with the specified CCC. </p>
<p> The <code>ScreenWhitePointOfCCC</code> macro returns the screen white point of the screen associated with the specified CCC. </p>
<p> The <code>ClientWhitePointOfCCC</code> macro returns the client white point of the screen associated with the specified CCC.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcmscccofcolormap/">XcmsCCCOfColormap</a>(3), <a href="/docs/linux/man/3-xcmsconvertcolors/">XcmsConvertColors</a>(3), <a href="/docs/linux/man/3-xcmscreateccc/">XcmsCreateCCC</a>(3), <a href="/docs/linux/man/3-xcmsdefaultccc/">XcmsDefaultCCC</a>(3), <a href="/docs/linux/man/3-xcmssetwhitepoint/">XcmsSetWhitePoint</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
