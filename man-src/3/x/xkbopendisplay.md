---
title: "xkbopendisplay(3)"
name: "xkbopendisplay"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbopendisplay/"
description: "XkbOpenDisplay – Checks for a compatible version of the Xkb extension in both the library and the server, and initializes the extension for use."
---

<p>XkbOpenDisplay &#8211; Checks for a compatible version of the Xkb extension in both the library and the server, and initializes the extension for use. </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Display *XkbOpenDisplay</code> <code>(char *</code><i>display_name</i><code>,</code> <code>int *</code><i>event_rtrn</i><code>,</code> <code>int *</code><i>error_rtrn</i><code>,</code> <code>int *</code><i>major_in_out</i><code>,</code> <code>int *</code><i>minor_in_out</i><code>,</code> <code>int *</code><i>reason_rtrn</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display_name</i></p>
<dd>
<dd>hardware display name, which determines the display and communications domain to be used</p>
<dt><i>event_rtrn</i></p>
<dd>backfilled with the extension base event code</p>
<dt><i>error_rtrn</i></p>
<dd>backfilled with the extension base error code</p>
<dt><i>major_in_out</i></p>
<dd>compile time lib major version in, server major version out</p>
<dt><i>minor_in_out</i></p>
<dd>compile time lib min version in, server minor version out</p>
<dt><i>reason_rtrn</i></p>
<dd>backfilled with a status code</dl>
<h2>Description</h2>
<p>As a convenience, you can use the function <i>XkbOpenDisplay </i> to perform these three tasks at once: open a connection to an X server, check for a compatible version of the Xkb extension in both the library and the server, and initialize the extension for use. </p>
<p> <i>XkbOpenDisplay </i> is a convenience function that opens an X display connection and initializes the X keyboard extension. In all cases, upon return <i>reason_rtrn </i> contains a status value indicating success or the type of failure. If <i>major_in_out </i> and <i>minor_in_out </i> are not NULL, <i>XkbOpenDisplay </i> first calls <i>XkbLibraryVersion </i> to determine whether the client library is compatible, passing it the values pointed to by <i>major_in_out and </i> <i>minor_in_out. If the library is </i> incompatible, <i>XkbOpenDisplay backfills </i> <i>major_in_out </i> and <i>minor_in_out </i> with the major and minor extension versions of the library being used and returns NULL. If the library is compatible, <i>XkbOpenDisplay </i> next calls <i>XOpenDisplay </i> with the <i>display_name. </i> If this fails, the function returns NULL. If successful, <i>XkbOpenDisplay </i> calls <i>XkbQueryExtension </i> and backfills the major and minor Xkb server extension version numbers in <i>major_in_out and </i> <i>minor_in_out. If the server </i> extension version is not compatible with the library extension version or if the server extension is not present, <i>XkbOpenDisplay </i> closes the display and returns NULL. When successful, the function returns the display connection. </p>
<p> The possible values for reason_rtrn are: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>XkbOD_BadLibraryVersion indicates XkbLibraryVersion returned False.</p>
<dt>&bull;</p>
<dd>XkbOD_ConnectionRefused indicates the display could not be opened.</p>
<dt>&bull;</p>
<dd>XkbOD_BadServerVersion indicates the library and the server have incompatible extension versions.</p>
<dt>&bull;</p>
<dd>XkbOD_NonXkbServer indicates the extension is not present in the X server.</p>
<dt>&bull;</p>
<dd>XkbOD_Success indicates that the function succeeded.</dl>
<h2>Return Values</h2>
<dl COMPACT>
<dt>NULL</p>
<dd>The <i>XkbOpenDisplay </i> function returns NULL if the library is incompatible. </p>
<p> The <i>XkbOpenDisplay </i> function returns NULL if the call to <i>XOpenDisplay </i> with the <i>display_name</i> fails. </p>
<p> The <i>XkbOpenDisplay </i> function returns NULL and closes the display if the server extension version is not compatible with the library extension version or if the server extension is not present.</dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><font SIZE="-1">BadAccess</font></p>
<dd>The Xkb extension has not been properly initialized</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkblibraryversion/">XkbLibraryVersion</a></code>(3), <code><a href="/docs/linux/man/3-xkbqueryextension/">XkbQueryExtension</a></code>(3), <code><a href="/docs/linux/man/3-xopendisplay/">XOpenDisplay</a></code>(3)</p>
