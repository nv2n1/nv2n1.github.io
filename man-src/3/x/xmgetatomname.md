---
title: "xmgetatomname(3)"
name: "xmgetatomname"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmgetatomname/"
description: "XmGetAtomName — A function that returns the string representation for an atom"
---

<p><code>XmGetAtomName</code> &#8212; A function that returns the string representation for an atom</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
#include &lt;Xm/AtomMgr.h&gt;
<code>String XmGetAtomName</code>(
<code>Display * display</code>,
<code>Atom atom</code>);</pre>
<h2>Description</h2>
<p><code>XmGetAtomName</code> returns the string representation for an atom. It mirrors the <i>Xlib</i> interfaces for atom management but provides client-side caching. When and where caching is provided in <i>Xlib</i>, the routines will become pseudonyms for the <i>Xlib</i> routines.</p>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server</p>
<dt><i>atom</i></p>
<dd>Specifies the atom for the property name you want returned</dl>
<h2>Return</h2>
<p>Returns a string. The function allocates space to hold the returned string. The application is responsible for managing the allocated space. The application can recover the allocated space by calling <code>XFree</code>.</p>
