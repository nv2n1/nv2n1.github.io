---
title: "xkbgetkeybehaviors(3)"
name: "xkbgetkeybehaviors"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbgetkeybehaviors/"
description: "XkbGetKeyBehaviors – Obtain the behaviors (the behaviors array) for a subset of the keys in a keyboard description from the server"
---

<p>XkbGetKeyBehaviors &#8211; Obtain the behaviors (the behaviors array) for a subset of the keys in a keyboard description from the server </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbGetKeyBehaviors</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>unsigned int </code><i>first</i><code>,</code> <code>unsigned int </code><i>num</i><code>,</code> <code>XkbDescPtr </code><i>xkb</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>
<dd>connection to server</p>
<dt><i>&#8211; first</i></p>
<dd>keycode of first key to get</p>
<dt><i>&#8211; num</i></p>
<dd>number of keys for which behaviors are desired</p>
<dt><i>&#8211; xkb</i></p>
<dd>Xkb description to contain the result</dl>
<h2>Description</h2>
<p><i>XkbGetKeyBehaviors </i> sends a request to the server to obtain the behaviors for <i>num </i> keys on the keyboard starting with the key whose keycode is <i>first. </i> It waits for a reply and returns the behaviors in the <i>server-&gt;behaviors </i> field of <i>xkb. </i> If successful, <i>XkbGetKeyBehaviors </i> returns Success. </p>
<p> If the <i>server </i> map in the <i>xkb </i> parameter has not been allocated, <i>XkbGetKeyBehaviors </i> allocates and initializes it before obtaining the actions. </p>
<p> If the server does not have a compatible version of Xkb, or the Xkb extension has not been properly initialized, <i>XkbGetKeyBehaviors </i> returns BadAccess. If <i>num </i> is less than 1 or greater than XkbMaxKeyCount, <i>XkbGetKeyBehaviors </i> returns BadValue. If any allocation errors occur, <i>XkbGetKeyBehaviors </i> returns BadAlloc.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAccess</code></p>
<dd>The Xkb extension has not been properly initialized</p>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage</p>
<dt><code>BadValue</code></p>
<dd>An argument is out of range </p>
</dl>
