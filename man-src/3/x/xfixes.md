---
title: "xfixes(3)"
name: "xfixes"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xfixes/"
description: "XFixes – Augmented versions of core protocol requests"
---

<p>XFixes &#8211; Augmented versions of core protocol requests </p>
<h2>Syntax</h2>
<p>#include &lt;X11/extensions/Xfixes.h&gt; </p>
<pre>Bool XFixesQueryExtension (Display *<i>dpy</i>,
 int *<i>event_base_return</i>, int *<i>error_base_return</i>);
Status XFixesQueryVersion (Display *<i>dpy</i>,
 int *<i>major_version_return</i>,
 int *<i>minor_version_return</i>);
void XFixesChangeSaveSet (Display *dpy,
 Window <i>window</i>,
 int <i>mode</i>,
 int <i>target</i>,
 int <i>map</i>);</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>window</i></p>
<dd>Specifies which window.</p>
<dt><i>mode</i></p>
<dd>Specifies the save set operation (SetModeInsert/SetModeDelete).</p>
<dt><i>target</i></p>
<dd>Specifies the target when executing the save set (SaveSetNearest/SaveSetRoot). In SaveSetNearest mode, the save set member window will be reparented to the nearest window not owned by the save set client. In SaveSetRoot mode, the save set member window will be reparented to the root window.</p>
<dt><i>map</i></p>
<dd>Specifies the map mode (SaveSetMap/SaveSetUnmap) which selects whether the save setmember window will be mapped or unmapped during save set processing.</dl>
<h2>Description</h2>
<p><code>Xfixes</code> is a simple library designed to interface the X Fixes Extension. This extension provides application with work arounds for various limitations in the core protocol.</p>
<h2>Restrictions</h2>
<p><code>Xfixes</code> will remain upward compatible after the 1.0 release.</p>
<h2>Authors</h2>
<p>Keith Packard, member of the XFree86 Project, Inc. and HP, Owen Taylor, member of the Gnome Foundation and Redhat, Inc.</p>
