---
title: "xevi(3)"
name: "xevi"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xevi/"
description: "XeviQueryExtension, XeviQueryVersion, XeviGetVisualInfo – X Extended Visual Information functions"
---

<p>XeviQueryExtension, XeviQueryVersion, XeviGetVisualInfo &#8211; X Extended Visual Information functions </p>
<h2>Synopsis</h2>
<p>#include &lt;X11/extensions/XEVI.h&gt; </p>
<p> Bool XeviQueryExtension (Display *dpy); </p>
<p> Bool XeviQueryVersion (Display *dpy,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;*major_version_return,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;*minor_version_return); </p>
<p> int XeviGetVisualInfo (Display *dpy, VisualID *visual,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int n_visual, ExtendedVisualInfo&nbsp;**&nbsp;evi_return,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;*&nbsp;n_info_return);</p>
<h2>Description</h2>
<p>The X11 Extended Visual Information extension (EVI) allows a client to determine information about core X visuals beyond what the core protocol provides. </p>
<p> The EVI application programming library contains the interfaces described below. With the exception of <code>XeviQueryExtension,</code> if any of these routines are called with a display that does not support the extension, the ExtensionErrorHandler (which can be set with <code>XSetExtensionErrorHandler</code> and functions the same way as <code>XSetErrorHandler</code>) will be called and the function will then return. </p>
<p> <code>XeviQueryExtension</code> returns <code>True</code> if the Extended Visual Information extension is available on the given display. A client must call <code>XeviQueryExtension</code> before calling any other EVI function in order to negotiate a compatible protocol version; otherwise the client will get undefined behavior (EVI may or may not work). </p>
<p> <code>XeviQueryVersion</code> returns <code>True</code> if the request succeeded; the values of the major and minor protocol version supported by the server are returned in <i>major_version_return</i> and <i>minor_version_return.</i> </p>
<p> <code>XeviGetVisualInfo</code> returns a list of ExtendedVisualInfo structures that describe visual information beyond that supported by the core protocol. This includes layer information relevant for systems supporting overlays and/or underlay planes, and information that allows applications better to determine the level of hardware support for multiple colormaps. XeviGetVisualInfo returns <code>Success</code> if successful, or an X error otherwise. If the argument <i>visual</i> is NULL, then information for all visuals of all screens is returned. Otherwise, it&#8217;s a pointer to a list of visuals for which extended visual information is desired. <i>n_visual</i> is the number of elements in the array visual. <i>evi_return</i> returns a pointer to a list of ExtendedVisualInfo. When done, the client should free the list using XFree. <i>n_info_return</i> returns the number of elements in the array evi_return. </p>
<p> The <code>ExtendedVisualInfo</code> structure has the following fields: </p>
<pre>VisualID <i>core_visual_id</i>
int <i>screen</i>
int <i>level</i>
unsigned int <i>transparency_type</i>
unsigned int <i>transparency_value</i>
unsigned int <i>min_hw_colormaps</i>
unsigned int <i>max_hw_colormaps</i>
unsigned int <i>num_colormap_conflicts</i>
VisualID * <i>colormap_conflicts</i></pre>
<p>The combination of <i>core_visual_id</i> and <i>screen</i> number uniquely specify the visual being described. </p>
<p> <i>level</i> returns the level number for the visual, 0 for normal planes, &gt; 0 for overlays, &lt; 0 for underlays. </p>
<p> <i>transparency_type</i> returns the type of transparency supported by the visual. XEVI_TRANSPARENCY_NONE if there are no transparent pixels, XEVI_TRANSPARENCY_PIXEL if the visual supports a transparent pixel, XEVI_TRANSPARENCY_MASK if the visual supports transparent plane(s). </p>
<p> <i>transparency_value</i> returns the pixel/plane value to set for transparency if transparency_type isn&#8217;t XEVI_TRANSPARENCY_NONE. </p>
<p> <i>min_hw_colormaps</i> and <i>max_hw_colormaps</i> return the minimum and maximum number of hardware colormaps backing up the visual. </p>
<p> <i>num_colormap_conflicts</i> returns the number of elements in <i>colormap_conflicts.</i> This array returns a list of visuals that may cause conflicts in the use of the hardware colormap. For example, if a 12-bit hardware colormap is overloaded to support 8-bit colormaps, the corresponding 8-bit visuals would conflict with the 12-bit visuals. </p>
<h2>Errors</h2>
<p><code>XeviGetVisualInfo</code> will return <i>BadValue</i> if passed an illegal visual ID, <i>BadAccess</i> if the X server does not respond, <i>BadAlloc</i> if there is a memory allocation failure.</p>
