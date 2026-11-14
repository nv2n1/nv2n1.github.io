---
title: "xkblibraryversion(3)"
name: "xkblibraryversion"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkblibraryversion/"
description: "XkbLibraryVersion – Determines the compatibility of a library at runtime."
---

<p>XkbLibraryVersion &#8211; Determines the compatibility of a library at runtime. </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbLibraryVersion</code> <code>(int *</code><i>lib_major_in_out</i><code>,</code> <code>int *</code><i>lib_minor_in_out</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>lib_major_in_out</i></p>
<dd>
<dd>Specifies and returns the major Xkb library version.</p>
<dt><i>lib_minor_in_out</i></p>
<dd>Specifies and returns the minor Xkb library version.</dl>
<h2>Description</h2>
<p>If an application is dynamically linked, both the X server and the client-side X library must contain the Xkb extension in order for the client to use the Xkb extension capabilities. Therefore a dynamically linked application must check both the library and the server for compatibility before using Xkb function calls. A properly written program must check for compatibility between the version of the Xkb library that is dynamically loaded and the one used when the application was built. It must then check the server version for compatibility with the version of Xkb in the library. </p>
<p> If your application is statically linked, you must still check for server compatibility and may check library compatibility. (It is possible to compile against one set of header files and link against a different, incompatible, version of the library, although this should not normally occur.) </p>
<p> Pass the symbolic value XkbMajorVersion in <i>lib_major_in_out </i> and XkbMinorVersion in <i>lib_minor_in_out. </i> These arguments represent the version of the library used at compile time. The <i>XkbLibraryVersion </i> function backfills the major and minor version numbers of the library used at run time in <i>lib_major_in_out and </i> <i>lib_minor_in_out. </i> If the versions of the compile time and run time libraries are compatible, <i>XkbLibraryVersion </i> returns True, otherwise, it returns False. </p>
<p> In addition, in order to use the Xkb extension, you must ensure that the extension is present in the server and that the server supports the version of the extension expected by the client. Use <i>XkbQueryExtension </i> to do this, as described in the next section.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>True</p>
<dd>The <i>XkbLibraryVersion </i> returns True if the versions of the compile time and run time libraries are compatible.</p>
<dt>False</p>
<dd>The <i>XkbLibraryVersion </i> returns False if the versions of the compile time and run time libraries are not compatible.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbmajorversion/">XkbMajorVersion</a></code>(3), <code><a href="/docs/linux/man/3-xkbminorversion/">XkbMinorVersion</a></code>(3), <code><a href="/docs/linux/man/3-xkbqueryextension/">XkbQueryExtension</a></code>(3)</p>
