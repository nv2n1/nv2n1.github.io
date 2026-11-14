---
title: "xuninstallcolormap(3)"
name: "xuninstallcolormap"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xuninstallcolormap/"
description: "XInstallColormap, XUninstallColormap, XListInstalledColormaps – control colormaps"
---

<p>XInstallColormap, XUninstallColormap, XListInstalledColormaps &#8211; control colormaps </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XInstallColormap(Display *<i>display</i>, Colormap <i>colormap</i>);</p>
<dd>int XUninstallColormap(Display *<i>display</i>, Colormap <i>colormap</i>);</p>
<dd>Colormap *XListInstalledColormaps(Display *<i>display</i>, Window <i>w</i>, int *<i>num_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>colormap</i></p>
<dd>Specifies the colormap.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>num_return</i></p>
<dd>Returns the number of currently installed colormaps.</p>
<dt><i>w</i></p>
<dd>Specifies the window that determines the screen.</dl>
<h2>Description</h2>
<p>The <code>XInstallColormap</code> function installs the specified colormap for its associated screen. All windows associated with this colormap immediately display with true colors. You associated the windows with this colormap when you created them by calling <code>XCreateWindow</code>, <code>XCreateSimpleWindow</code>, <code>XChangeWindowAttributes</code>, or <code>XSetWindowColormap</code>. </p>
<p> If the specified colormap is not already an installed colormap, the X server generates a <code>ColormapNotify</code> event on each window that has that colormap. In addition, for every other colormap that is installed as a result of a call to <code>XInstallColormap</code>, the X server generates a <code>ColormapNotify</code> event on each window that has that colormap. </p>
<p> <code>XInstallColormap</code> can generate a <code>BadColor</code> error. </p>
<p> The <code>XUninstallColormap</code> function removes the specified colormap from the required list for its screen. As a result, the specified colormap might be uninstalled, and the X server might implicitly install or uninstall additional colormaps. Which colormaps get installed or uninstalled is server dependent except that the required list must remain installed. </p>
<p> If the specified colormap becomes uninstalled, the X server generates a <code>ColormapNotify</code> event on each window that has that colormap. In addition, for every other colormap that is installed or uninstalled as a result of a call to <code>XUninstallColormap</code>, the X server generates a <code>ColormapNotify</code> event on each window that has that colormap. </p>
<p> <code>XUninstallColormap</code> can generate a <code>BadColor</code> error. </p>
<p> The <code>XListInstalledColormaps</code> function returns a list of the currently installed colormaps for the screen of the specified window. The order of the colormaps in the list is not significant and is no explicit indication of the required list. When the allocated list is no longer needed, free it by using <code>XFree</code>. </p>
<p> <code>XListInstalledColormaps</code> can generate a <code>BadWindow</code> error.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadColor</code></p>
<dd>A value for a Colormap argument does not name a defined Colormap.</p>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xchangewindowattributes/">XChangeWindowAttributes</a>(3), <a href="/docs/linux/man/3-xcreatecolormap/">XCreateColormap</a>(3), <a href="/docs/linux/man/3-xcreatewindow/">XCreateWindow</a>(3), <a href="/docs/linux/man/3-xfree/">XFree</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
