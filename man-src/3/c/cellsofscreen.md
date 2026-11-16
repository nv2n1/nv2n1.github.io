---
title: "cellsofscreen(3)"
name: "cellsofscreen"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cellsofscreen/"
description: "BlackPixelOfScreen, WhitePixelOfScreen, CellsOfScreen, DefaultColormapOfScreen, DefaultDepthOfScreen, DefaultGCOfScreen, DefaultVisualOfScreen, DoesBackingStore, DoesSaveUnders, DisplayOfScreen, XS..."
---

<p>BlackPixelOfScreen, WhitePixelOfScreen, CellsOfScreen, DefaultColormapOfScreen, DefaultDepthOfScreen, DefaultGCOfScreen, DefaultVisualOfScreen, DoesBackingStore, DoesSaveUnders, DisplayOfScreen, XScreenNumberOfScreen, EventMaskOfScreen, HeightOfScreen, HeightMMOfScreen, MaxCmapsOfScreen, MinCmapsOfScreen, PlanesOfScreen, RootWindowOfScreen, WidthOfScreen, WidthMMOfScreen &#8211; screen information functions and macros </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>unsigned long BlackPixelOfScreen(Screen *<i>screen</i>);</dd>
<dd>unsigned long WhitePixelOfScreen(Screen *<i>screen</i>);</dd>
<dd>int CellsOfScreen(Screen *<i>screen</i>);</dd>
<dd>Colormap DefaultColormapOfScreen(Screen *<i>screen</i>);</dd>
<dd>int DefaultDepthOfScreen(Screen *<i>screen</i>);</dd>
<dd>GC DefaultGCOfScreen(Screen *<i>screen</i>);</dd>
<dd>Visual *DefaultVisualOfScreen(Screen *<i>screen</i>);</dd>
<dd>int DoesBackingStore(Screen *<i>screen</i>);</dd>
<dd>Bool DoesSaveUnders(Screen *<i>screen</i>);</dd>
<dd>Display *DisplayOfScreen(Screen *<i>screen</i>);</dd>
<dd>int XScreenNumberOfScreen(Screen *<i>screen</i>);</dd>
<dd>long EventMaskOfScreen(Screen *<i>screen</i>);</dd>
<dd>int HeightOfScreen(Screen *<i>screen</i>);</dd>
<dd>int HeightMMOfScreen(Screen *<i>screen</i>);</dd>
<dd>int MaxCmapsOfScreen(Screen *<i>screen</i>);</dd>
<dd>int MinCmapsOfScreen(Screen *<i>screen</i>);</dd>
<dd>int PlanesOfScreen(Screen *<i>screen</i>);</dd>
<dd>Window RootWindowOfScreen(Screen *<i>screen</i>);</dd>
<dd>int WidthOfScreen(Screen *<i>screen</i>);</dd>
<dd>int WidthMMOfScreen(Screen *<i>screen</i>);</dd></dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>screen</i></dt>
<dd>Specifies the appropriate <code>Screen</code> structure.</dd></dl>
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
<p><a href="/docs/linux/man/3-allplanes/">AllPlanes</a>(3), ImageByteOrder(3), IsCursorKey(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
