---
title: "tk_internatom(3)"
name: "tk_internatom"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_internatom/"
description: "Tk_InternAtom, Tk_GetAtomName – manage cache of X atoms"
---

<p>Tk_InternAtom, Tk_GetAtomName &#8211; manage cache of X atoms </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
Atom
<code>Tk_InternAtom(</code><i>tkwin, name</i>)
const char *
<code>Tk_GetAtomName(</code><i>tkwin, atom</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_Window <i>tkwin</i> (in) Token for window. Used to map atom or name relative to a particular display.</p>
<dd>const char <i>*name</i> (in) String name for which atom is desired.</p>
<dd>Atom <i>atom</i> (in) Atom for which corresponding string name is desired. </p>
</dl>
<h2>Description</h2>
<p>These procedures are similar to the Xlib procedures <code>XInternAtom</code> and <code>XGetAtomName</code>. <code>Tk_InternAtom</code> returns the atom identifier associated with string given by <i>name</i>; the atom identifier is only valid for the display associated with <i>tkwin</i>. <code>Tk_GetAtomName</code> returns the string associated with <i>atom</i> on <i>tkwin</i>&#8216;s display. The string returned by <code>Tk_GetAtomName</code> is in Tk&#8217;s storage: the caller need not free this space when finished with the string, and the caller should not modify the contents of the returned string. If there is no atom <i>atom</i> on <i>tkwin</i>&#8216;s display, then <code>Tk_GetAtomName</code> returns the string &#8220;?bad atom?&#8221;. </p>
<p> Tk caches the information returned by <code>Tk_InternAtom</code> and <code>Tk_GetAtomName</code> so that future calls for the same information can be serviced from the cache without contacting the server. Thus <code>Tk_InternAtom</code> and <code>Tk_GetAtomName</code> are generally much faster than their Xlib counterparts, and they should be used in place of the Xlib procedures. </p>
<h2>Keywords</h2>
<p>atom, cache, display</p>
