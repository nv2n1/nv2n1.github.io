---
title: "xkbgetkeyvirtualmodmap(3)"
name: "xkbgetkeyvirtualmodmap"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbgetkeyvirtualmodmap/"
description: "XkbGetKeyVirtualModMap – Obtain the virtual modifier map (the vmodmap array) for a subset of the keys in a keyboard description"
---

<p>XkbGetKeyVirtualModMap &#8211; Obtain the virtual modifier map (the vmodmap array) for a subset of the keys in a keyboard description </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbGetKeyVirtualModMap</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>unsigned int </code><i>first</i><code>,</code> <code>unsigned int </code><i>num</i><code>,</code> <code>XkbDescPtr </code><i>xkb</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>
<dd>connection to server</p>
<dt><i>&#8211; first</i></p>
<dd>keycode of first key to fetch</p>
<dt><i>&#8211; num</i></p>
<dd>number of keys for which virtual mod maps are desired</p>
<dt><i>&#8211; xkb</i></p>
<dd>Xkb description where results will be placed</dl>
<h2>Description</h2>
<p><i>XkbGetKeyVirutalModmap </i> sends a request to the server to obtain the virtual modifier mappings for <i>num </i> keys on the keyboard starting with key <i>first. </i> It waits for a reply and returns the virtual modifier mappings in the <i>server-&gt;vmodmap </i> array of <i>xkb. </i> If successful, <i>XkbGetKeyVirtualModMap </i> returns Success. The <i>xkb </i> parameter must be a pointer to a valid Xkb keyboard description. </p>
<p> If the <i>server </i> map in the <i>xkb </i> parameter has not been allocated, <i>XkbGetKeyVirtualModMap </i> allocates and initializes it before obtaining the virtual modifier mappings. </p>
<p> If the server does not have a compatible version of Xkb, or the Xkb extension has not been properly initialized, <i>XkbGetKeyVirtualModMap </i> returns BadMatch. If <i>num </i> is less than 1 or greater than XkbMaxKeyCount, <i>XkbGetKeyVirtualModMap </i> returns BadValue. If any allocation errors occur, <i>XkbGetKeyVirtualModMap </i> returns BadAlloc.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>Success</p>
<dd>The <i>XkbGetKeyVirutalModmap </i> function returns Success following a successful reply from the server to obtain the virtual modifier mappings for <i>num </i> keys on the keyboard starting with key <i>first. </i></dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage</p>
<dt><code>BadMatch</code></p>
<dd>A compatible version of Xkb was not available in the server or an argument has correct type and range, but is otherwise invalid</p>
<dt><code>BadValue</code></p>
<dd>An argument is out of range </p>
</dl>
