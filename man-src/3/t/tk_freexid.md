---
title: "tk_freexid(3)"
name: "tk_freexid"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_freexid/"
description: "Tk_FreeXId – make X resource identifier available for reuse"
---

<p>Tk_FreeXId &#8211; make X resource identifier available for reuse </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
<code>Tk_FreeXId(</code><i>display, id</i><code>)</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Display <i>*display</i> (in) Display for which <i>id</i> was allocated.</p>
<dd>XID <i>id</i> (in) Identifier of X resource (window, font, pixmap, cursor, graphics context, or colormap) that is no longer in use.
</dl>
<h2>Description</h2>
<p>The default allocator for resource identifiers provided by Xlib is very simple-minded and does not allow resource identifiers to be re-used. If a long-running application reaches the end of the resource id space, it will generate an X protocol error and crash. Tk replaces the default id allocator with its own allocator, which allows identifiers to be reused. In order for this to work, <code>Tk_FreeXId</code> must be called to tell the allocator about resources that have been freed. Tk automatically calls <code>Tk_FreeXId</code> whenever it frees a resource, so if you use procedures like <code>Tk_GetFont</code>, <code>Tk_GetGC</code>, and <code>Tk_GetPixmap</code> then you need not call <code>Tk_FreeXId</code>. However, if you allocate resources directly from Xlib, for example by calling <code>XCreatePixmap</code>, then you should call <code>Tk_FreeXId</code> when you call the corresponding Xlib free procedure, such as <code>XFreePixmap</code>. If you do not call <code>Tk_FreeXId</code> then the resource identifier will be lost, which could cause problems if the application runs long enough to lose all of the available identifiers.</p>
<h2>Keywords</h2>
<p>resource identifier</p>
