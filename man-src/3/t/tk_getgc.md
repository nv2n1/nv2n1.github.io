---
title: "tk_getgc(3)"
name: "tk_getgc"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_getgc/"
description: "Tk_GetGC, Tk_FreeGC – maintain database of read-only graphics contexts"
---

<p>Tk_GetGC, Tk_FreeGC &#8211; maintain database of read-only graphics contexts </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
GC
<code>Tk_GetGC</code>(<i>tkwin, valueMask, valuePtr</i>)
<code>Tk_FreeGC(</code><i>display, gc</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_Window <i>tkwin</i> (in) Token for window in which the graphics context will be used.</p>
<dd>unsigned long <i>valueMask</i> (in) Mask of bits (such as <code>GCForeground</code> or <code>GCStipple</code>) indicating which fields of <i>*valuePtr</i> are valid.</p>
<dd>XGCValues <i>*valuePtr</i> (in) Pointer to structure describing the desired values for the graphics context.</p>
<dd>Display <i>*display</i> (in) Display for which <i>gc</i> was allocated.</p>
<dd>GC <i>gc</i> (in) X identifier for graphics context that is no longer needed. Must have been allocated by <code>Tk_GetGC</code>. </p>
</dl>
<h2>Description</h2>
<p><code>Tk_GetGC</code> and <code>Tk_FreeGC</code> manage a collection of graphics contexts being used by an application. The procedures allow graphics contexts to be shared, thereby avoiding the server overhead that would be incurred if a separate GC were created for each use. <code>Tk_GetGC</code> takes arguments describing the desired graphics context and returns an X identifier for a GC that fits the description. The graphics context that is returned will have default values in all of the fields not specified explicitly by <i>valueMask</i> and <i>valuePtr</i>. </p>
<p> <code>Tk_GetGC</code> maintains a database of all the graphics contexts it has created. Whenever possible, a call to <code>Tk_GetGC</code> will return an existing graphics context rather than creating a new one. This approach can substantially reduce server overhead, so <code>Tk_GetGC</code> should generally be used in preference to the Xlib procedure <code>XCreateGC</code>, which creates a new graphics context on each call. </p>
<p> Since the return values of <code>Tk_GetGC</code> are shared, callers should never modify the graphics contexts returned by <code>Tk_GetGC</code>. If a graphics context must be modified dynamically, then it should be created by calling <code>XCreateGC</code> instead of <code>Tk_GetGC</code>. </p>
<p> When a graphics context is no longer needed, <code>Tk_FreeGC</code> should be called to release it. There should be exactly one call to <code>Tk_FreeGC</code> for each call to <code>Tk_GetGC</code>. When a graphics context is no longer in use anywhere (i.e. it has been freed as many times as it has been gotten) <code>Tk_FreeGC</code> will release it to the X server and delete it from the database. </p>
<h2>Keywords</h2>
<p>graphics context</p>
