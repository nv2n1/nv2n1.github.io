---
title: "xtreservepropertyatom(3)"
name: "xtreservepropertyatom"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtreservepropertyatom/"
description: "XtReservePropertyAtom, XtReleasePropertyAtom – maintain a cache of property atoms"
---

<p>XtReservePropertyAtom, XtReleasePropertyAtom &#8211; maintain a cache of property atoms </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>Atom XtReservePropertyAtom(Widget <i>w</i>);</p>
<dd>void XtReleasePropertyAtom(Widget <i>w</i>, Atom <i>atom</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>w</i></p>
<dd>Specifies the widget used to reserve the atom.</p>
<dt><i>atom</i></p>
<dd>Specifies the atom whose reservation is to be released.</dl>
<h2>Description</h2>
<p><code>XtReservePropertyAtom</code> returns an atom that may be used for properties in conjunction with conversion requests from widget <i>w</i>. The atom returned will be unique for the display of the widget specified.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
