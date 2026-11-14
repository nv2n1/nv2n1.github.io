---
title: "xkbqueryextension(3)"
name: "xkbqueryextension"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbqueryextension/"
description: "XkbQueryExtension – Determines the compatibility of a library at runtime."
---

<p>XkbQueryExtension &#8211; Determines the compatibility of a library at runtime. </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbQueryExtension</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>int *</code><i>opcode_rtrn</i><code>,</code> <code>int *</code><i>event_rtrn</i><code>,</code> <code>int *</code><i>error_rtrn</i><code>,</code> <code>int *</code><i>major_in_out</i><code>,</code> <code>int *</code><i>minor_in_out</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>dpy</i></p>
<dd>
<dd>connection to the X server</p>
<dt><i>opcode_rtrn</i></p>
<dd>backfilled with the major extension opcode</p>
<dt><i>event_rtrn</i></p>
<dd>backfilled with the extension base event code</p>
<dt><i>error_rtrn</i></p>
<dd>backfilled with the extension base error code</p>
<dt><i>major_in_out</i></p>
<dd>compile time lib major version in, server major version out</p>
<dt><i>minor_in_out</i></p>
<dd>compile time lib min version in, server minor version out</dl>
<h2>Description</h2>
<p>Call <i>XkbQueryExtension </i> to check for the presence and compatibility of the extension in the server and to initialize the extension. Because of potential version mismatches, you cannot use the generic extension mechanism functions ( <i>XQueryExtension </i> and <i>XInitExtension</i> ) for checking for the presence of, and initializing the Xkb extension.<br />
&nbsp; You must call <i>XkbQueryExtension </i> or <i>XkbOpenDisplay </i> before using any other Xkb library interfaces, unless such usage is explicitly allowed in the interface description in this document. The exceptions are: <i>XkbIgnoreExtension, XkbLibraryVersion, </i> and a handful of audible-bell functions. You should not use any other Xkb functions if the extension is not present or is uninitialized. In general, calls to Xkb library functions made prior to initializing the Xkb extension cause BadAccess protocol errors. </p>
<p> <i>XkbQueryExtension </i> both determines whether a compatible Xkb extension is present in the X server and initializes the extension when it is present. </p>
<p> The <i>XkbQueryExtension </i> function determines whether a compatible version of the X Keyboard Extension is present in the server. If a compatible extension is present, <i>XkbQueryExtension </i> returns True; otherwise, it returns False. </p>
<p> If a compatible version of Xkb is present, <i>XkbQueryExtension </i> initializes the extension. It backfills the major opcode for the keyboard extension in <i>opcode_rtrn, </i> the base event code in <i>event_rtrn, </i> the base error code in <i>error_rtrn, </i> and the major and minor version numbers of the extension in <i>major_in_out </i> and <i>minor_in_out. </i> The major opcode is reported in the <i>req_major </i> fields of some Xkb events. For a discussion of the base event code.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>True</p>
<dd>The <i>XkbQueryExtension </i> function returns True if it determines a compatible version of the X Keyboard Extension is present in the server.</p>
<dt>False</p>
<dd>The <i>XkbQueryExtension </i> function returns False if it determines a compatible version of the X Keyboard Extension is not present in the server.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbignoreextension/">XkbIgnoreExtension</a></code>(3), <code><a href="/docs/linux/man/3-xkblibraryversion/">XkbLibraryVersion</a></code>(3), <code><a href="/docs/linux/man/3-xkbopendisplay/">XkbOpenDisplay</a></code>(3)</p>
