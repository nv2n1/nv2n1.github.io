---
title: "xkbgetnamechanges(3)"
name: "xkbgetnamechanges"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbgetnamechanges/"
description: "XkbGetNameChanges – Update the local copy of the keyboard description with the actual values of the results of one or more calls to XkbNoteNameChanges"
---

<p>XkbGetNameChanges &#8211; Update the local copy of the keyboard description with the actual values of the results of one or more calls to <i>XkbNoteNameChanges</i> </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbGetNameChanges</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>XkbDescPtr </code><i>xkb</i><code>,</code> <code>XkbNameChangesPtr </code><i>changes</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>
<dd>connection to the X server</p>
<dt><i>&#8211; xkb</i></p>
<dd>keyboard description to which names are copied</p>
<dt><i>&#8211; changes</i></p>
<dd>names components to be obtained from the server</dl>
<h2>Description</h2>
<p><i>XkbGetNameChanges </i> examines the <i>changes </i> parameter, retrieves the necessary information from the server, and places the results into the <i>xkb </i> keyboard description. </p>
<p> <i>XkbGetNamesChanges </i> can generate BadAlloc, BadImplementation, and BadMatch errors.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage</p>
<dt><code>BadImplementation</code></p>
<dd>Invalid reply from server</p>
<dt><code>BadMatch</code></p>
<dd>A compatible version of Xkb was not available in the server or an argument has correct type and range, but is otherwise invalid</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbnotenamechanges/">XkbNoteNameChanges</a></code>(3)</p>
