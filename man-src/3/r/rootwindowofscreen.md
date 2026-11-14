---
title: "rootwindowofscreen(3)"
name: "rootwindowofscreen"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rootwindowofscreen/"
description: "BlackPixelOfScreen, WhitePixelOfScreen, CellsOfScreen, DefaultColormapOfScreen, DefaultDepthOfScreen, DefaultGCOfScreen, DefaultVisualOfScreen, DoesBackingStore, DoesSaveUnders, DisplayOfScreen, XS..."
---

<p>BlackPixelOfScreen, WhitePixelOfScreen, CellsOfScreen, DefaultColormapOfScreen, DefaultDepthOfScreen, DefaultGCOfScreen, DefaultVisualOfScreen, DoesBackingStore, DoesSaveUnders, DisplayOfScreen, XScreenNumberOfScreen, EventMaskOfScreen, HeightOfScreen, HeightMMOfScreen, MaxCmapsOfScreen, MinCmapsOfScreen, PlanesOfScreen, RootWindowOfScreen, WidthOfScreen, WidthMMOfScreen &#8211; screen information functions and macros </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>unsigned long BlackPixelOfScreen(Screen *<i>screen</i>);</p>
<dd>unsigned long WhitePixelOfScreen(Screen *<i>screen</i>);</p>
<dd>int CellsOfScreen(Screen *<i>screen</i>);</p>
<dd>Colormap DefaultColormapOfScreen(Screen *<i>screen</i>);</p>
<dd>int DefaultDepthOfScreen(Screen *<i>screen</i>);</p>
<dd>GC DefaultGCOfScreen(Screen *<i>screen</i>);</p>
<dd>Visual *DefaultVisualOfScreen(Screen *<i>screen</i>);</p>
<dd>int DoesBackingStore(Screen *<i>screen</i>);</p>
<dd>Bool DoesSaveUnders(Screen *<i>screen</i>);</p>
<dd>Display *DisplayOfScreen(Screen *<i>screen</i>);</p>
<dd>int XScreenNumberOfScreen(Screen *<i>screen</i>);</p>
<dd>long EventMaskOfScreen(Screen *<i>screen</i>);</p>
<dd>int HeightOfScreen(Screen *<i>screen</i>);</p>
<dd>int HeightMMOfScreen(Screen *<i>screen</i>);</p>
<dd>int MaxCmapsOfScreen(Screen *<i>screen</i>);</p>
<dd>int MinCmapsOfScreen(Screen *<i>screen</i>);</p>
<dd>int PlanesOfScreen(Screen *<i>screen</i>);</p>
<dd>Window RootWindowOfScreen(Screen *<i>screen</i>);</p>
<dd>int WidthOfScreen(Screen *<i>screen</i>);</p>
<dd>int WidthMMOfScreen(Screen *<i>screen</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>screen</i></p>
<dd>Specifies the appropriate <code>Screen</code> structure.</dl>
<h2>Description</h2>
<p>The <code>BlackPixelOfScreen</code> macro returns the black pixel value of the specified screen. </p>
<p> The <code>WhitePixelOfScreen</code> macro returns the white pixel value of the specified screen. </p>
<p> The <code>CellsOfScreen</code> macro returns the number of colormap cells in the default colormap of the specified screen. </p>
<p> The <code>DefaultColormapOfScreen</code> macro returns the default colormap of the specified screen. </p>
<p> The <code>DefaultDepthOfScreen</code> macro returns the default depth of the root window of the specified screen. </p>
<p> The <code>DefaultGCOfScreen</code> macro returns the default GC of the specified screen, which has the same depth as the root window of the screen. </p>
<p> The <code>DefaultVisualOfScreen</code> macro returns the default visual of the specified screen. </p>
<p> The <code>DoesBackingStore</code> macro returns <code>WhenMapped</code>, <code>NotUseful</code>, or <code>Always</code>, which indicate whether the screen supports backing stores. </p>
<p> The <code>DoesSaveUnders</code> macro returns a Boolean value indicating whether the screen supports save unders. </p>
<p> The <code>DisplayOfScreen</code> macro returns the display of the specified screen. </p>
<p> The <code>XScreenNumberOfScreen</code> function returns the screen index number of the specified screen. </p>
<p> The <code>EventMaskOfScreen</code> macro returns the root event mask of the root window for the specified screen at connection setup. </p>
<p> The <code>HeightOfScreen</code> macro returns the height of the specified screen. </p>
<p> The <code>HeightMMOfScreen</code> macro returns the height of the specified screen in millimeters. </p>
<p> The <code>MaxCmapsOfScreen</code> macro returns the maximum number of installed colormaps supported by the specified screen. </p>
<p> The <code>MinCmapsOfScreen</code> macro returns the minimum number of installed colormaps supported by the specified screen. </p>
<p> The <code>PlanesOfScreen</code> macro returns the number of planes in the root window of the specified screen. </p>
<p> The <code>RootWindowOfScreen</code> macro returns the root window of the specified screen. </p>
<p> The <code>WidthOfScreen</code> macro returns the width of the specified screen. </p>
<p> The <code>WidthMMOfScreen</code> macro returns the width of the specified screen in millimeters.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-allplanes/">AllPlanes</a>(3), <a href="/docs/linux/man/3-imagebyteorder/">ImageByteOrder</a>(3), <a href="/docs/linux/man/3-iscursorkey/">IsCursorKey</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
