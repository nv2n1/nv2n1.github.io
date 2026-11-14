---
title: "eom(1)"
name: "eom"
section: "1"
letter: "e"
url: "/docs/linux/man/1-eom/"
description: "eom – The Eye of MATE Image Viewer"
---

<h2 class="name">NAME</h2>
<p> eom &#8211; The Eye of MATE Image Viewer </p>
<h2>SYNOPSIS</h2>
<p> <code>eom [&#8211;fullscreen] [&#8211;disable-image-collection] [&#8211;slide-show] [&#8211;new instance] [FILES&#8230;]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>eom</code> or the Eye of MATE is the official image viewer for the MATE Desktop Environment. It aims to be simplistic, lightweight, and easy to use. The Eye of MATE may also be used to perform basic tasks like image flipping and rotation. </p>
<p> Eye of MATE features a flexible plugin system which can be used to dynamically add new advanced features to <code>eom</code> itself. <code>eom</code> uses the gdk-pixbuf library, it can handle large images, zoom, and scroll with low memory usage. </p>
<p> This manual page briefly documents the <code>eom</code> command.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>filename(s)&#8230;</code></p>
<dd> Specifies the image to open when <code>eom</code> starts. If this is not specified, <code>eom</code> will start with a blank window and you may open a file from the menu or by using the shortcut CTRL+O. <code>eom</code> also supports handling of remote files.</p>
<dt><code>&#8211;display=DISPLAY</code></p>
<dd> X display to use.</p>
<dt><code>-f, &#8211;fullscreen</code></p>
<dd> Start <code>eom</code> in fullscreen mode.</p>
<dt><code>-c, &#8211;disable-image-collection</code></p>
<dd> Disable image collection viewer.</p>
<dt><code>-s, &#8211;slide-show</code></p>
<dd> Open in slideshow mode.</p>
<dt><code>-n, &#8211;new-instance</code></p>
<dd> Start a new instance instead of reusing an existing window.</p>
<dt><code>&#8211;version</code></p>
<dd> Output version information and exit.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Print standard command line options.</p>
<dt><code>&#8211;help-all</code></p>
<dd> Print all command line options.</dl>
<p> This program also accepts the standard GTK options.</p>
<h2>EXAMPLES</h2>
<p> <code>eom -f <a rel="nofollow" href="http://mate-desktop.org/assets/img/icons/mate.png">http://mate-desktop.org/assets/img/icons/mate.png</a></code></p>
<dl>
<dt>
<dd> Open the referenced file in fullscreen mode.</dl>
<p> <code>eom -s /usr/share/eom/icons/hicolor/scalable/actions</code></p>
<dl>
<dt>
<dd> Open the images in the referenced directory in slideshow mode.</dl>
<h2>BUGS</h2>
<h3>Should you encounter any bugs, they may be reported at:</h3>
<p> <a rel="nofollow" href="http://github.com/mate-desktop/eom/issues">http://github.com/mate-desktop/eom/issues</a></p>
<h2>AUTHORS</h2>
<h3>This Manual Page has been written for the MATE Desktop Environment by:</h3>
<p> Scott Balneaves &lt;sbalneav [at] mate-desktop.org&gt; (2013) Adam Erdman &lt;hekel [at] archlinux.info&gt; (2014)</p>
<h2>SEE ALSO</h2>
<h3>Eye of MATE documentation can be found from the Help menu, or by pressing the F1 key.</h3>
<p> Further information may also be available at: <a rel="nofollow" href="http://wiki.mate-desktop.org/docs">http://wiki.mate-desktop.org/docs</a> </p>
<h2>Index</h2>
