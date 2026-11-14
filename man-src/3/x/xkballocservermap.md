---
title: "xkballocservermap(3)"
name: "xkballocservermap"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkballocservermap/"
description: "XkbAllocServerMap – Allocate and initialize an empty server map description record"
---

<p>XkbAllocServerMap &#8211; Allocate and initialize an empty server map description record </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbAllocServerMap</code> <code>(XkbDescPtr </code><i>xkb</i><code>,</code> <code>unsigned int </code><i>which</i><code>,</code> <code>unsigned int </code><i>count_acts</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; xkb</i></p>
<dd>
<dd>keyboard description in which to allocate server map</p>
<dt><i>&#8211; which</i></p>
<dd>mask selecting map components to allocate</p>
<dt><i>&#8211; count_acts</i></p>
<dd>value of num_acts field in map to be allocated</dl>
<h2>Description</h2>
<p><i>XkbAllocServerMap </i> allocates and initializes an empty server map in the <i>server </i> field of the keyboard description specified by <i>xkb. </i> The <i>which </i> parameter specifies the particular components of the server map structure to allocate, as specified in Table 1. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=2>Table 1 XkbAllocServerMap Masks
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Mask</td>
<td>Effect
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XkbExplicitComponentsMask</td>
<td> The min_key_code and max_key_code fields of the xkb parameter are used to allocate the explicit field of the server map.
</td>
</tr>
<tr VALIGN=top>
<td>XkbKeyActionsMask</td>
<td> The min_key_code and max_key_code fields of the xkb parameter are used to allocate the key_acts field of the server map. The count_acts parameter is used to allocate the acts field of the server map.
</td>
</tr>
<tr VALIGN=top>
<td>XkbKeyBehaviorsMask</td>
<td> The min_key_code and max_key_code fields of the xkb parameter are used to allocate the behaviors field of the server map.
</td>
</tr>
<tr VALIGN=top>
<td>XkbVirtualModMapMask</td>
<td> The min_key_code and max_key_code fields of the xkb parameter are used to allocate the vmodmap field of the server map.
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>
</td>
</tr>
</table>
<p> If the server map of the keyboard description is not NULL and any fields are already allocated in the server map, <i>XkbAllocServerMap </i> does not overwrite the existing values. The only exception is with the <i>acts </i> array. If the <i>count_acts </i> parameter is greater than the current <i>num_acts </i> field of the server map, <i>XkbAllocServerMap </i> resizes the <i>acts </i> array and resets the <i>num_acts </i> field accordingly. </p>
<p> If <i>XkbAllocServerMap </i> is successful, it returns Success. Otherwise, it can return either BadMatch or BadAlloc errors.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage</p>
<dt><code>BadMatch</code></p>
<dd>A compatible version of Xkb was not available in the server or an argument has correct type and range, but is otherwise invalid</p>
<dt><code>BadValue</code></p>
<dd>An argument is out of range</dl>
<h2>Notes</h2>
<p>The <i>min_key_code </i> and <i>max_key_code </i> fields of the <i>xkb </i> parameter must be legal values. If they are not valid, <i>XkbAllocServerMap </i> returns BadValue.</p>
