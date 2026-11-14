---
title: "xkbgetkeytypes(3)"
name: "xkbgetkeytypes"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbgetkeytypes/"
description: "XkbGetKeyTypes – Obtain the list of available key types in the server’s keyboard mapping"
---

<p>XkbGetKeyTypes &#8211; Obtain the list of available key types in the server&#8217;s keyboard mapping </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbGetKeyTypes</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>unsigned int </code><i>first</i><code>,</code> <code>unsigned int </code><i>num</i><code>,</code> <code>XkbDescPtr </code><i>xkb</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>
<dd>connection to X server</p>
<dt><i>&#8211; first</i></p>
<dd>index to first type to get, 0 =&gt; 1st type</p>
<dt><i>&#8211; num</i></p>
<dd>number of key types to be returned</p>
<dt><i>&#8211; xkb</i></p>
<dd>keyboard description containing client map to update</dl>
<h2>Description</h2>
<p><i>XkbGetKeyTypes </i> queries the server for the desired types, waits for a reply, and returns the desired types in the <i>xkb-&gt;map-&gt;types. </i> If successful, it returns Success. </p>
<p> <i>XkbGetKeyTypes </i> returns BadAccess if the Xkb extension has not been properly initialized and BadValue if the combination of <i>first </i> and <i>num </i> results in numbers out of valid range. </p>
<p> <code>NOTE: </code> <i>XkbGetKeyTypes </i> is used to obtain descriptions of the key types themselves, not the key types bound to individual keys. To obtain the key types bound to an individual key, refer to the <i>key_sym_map </i> field of the client map.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAccess</code></p>
<dd>The Xkb extension has not been properly initialized</p>
<dt><code>BadValue</code></p>
<dd>An argument is out of range</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbkeytype/">XkbKeyType</a></code>(3), <code><a href="/docs/linux/man/3-xkbkeytypeindex/">XkbKeyTypeIndex</a></code>(3)</p>
