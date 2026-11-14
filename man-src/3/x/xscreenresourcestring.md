---
title: "xscreenresourcestring(3)"
name: "xscreenresourcestring"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xscreenresourcestring/"
description: "XResourceManagerString, XScreenResourceString – obtain server resource properties"
---

<p>XResourceManagerString, XScreenResourceString &#8211; obtain server resource properties </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>char *XResourceManagerString(Display *<i>display</i>);</p>
<dd>char *XScreenResourceString(Screen *<i>screen</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>screen</i></p>
<dd>Specifies the screen.</dl>
<h2>Description</h2>
<p>The <code>XResourceManagerString</code> function returns the RESOURCE_MANAGER property from the server&#8217;s root window of screen zero, which was returned when the connection was opened using <code>XOpenDisplay</code>. The property is converted from type STRING to the current locale. The conversion is identical to that produced by <code>XmbTextPropertyToTextList</code> for a single element STRING property. The returned string is owned by Xlib and should not be freed by the client. The property value must be in a format that is acceptable to <code>XrmGetStringDatabase</code>. If no property exists, NULL is returned. </p>
<p> The <code>XScreenResourceString</code> function returns the SCREEN_RESOURCES property from the root window of the specified screen. The property is converted from type STRING to the current locale. The conversion is identical to that produced by <code>XmbTextPropertyToTextList</code> for a single element STRING property. The property value must be in a format that is acceptable to <code>XrmGetStringDatabase</code>. If no property exists, NULL is returned. The caller is responsible for freeing the returned string by using <code>XFree</code>.</p>
<h2>See Also</h2>
<p><i>Xlib &#8211; C Language X Interface</i></p>
