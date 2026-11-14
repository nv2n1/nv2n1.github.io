---
title: "xkballocclientmap(3)"
name: "xkballocclientmap"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkballocclientmap/"
description: "XkbAllocClientMap – Allocate and initialize an empty client map description record"
---

<p>XkbAllocClientMap &#8211; Allocate and initialize an empty client map description record </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbAllocClientMap</code> <code>(XkbDescPtr </code><i>xkb</i><code>,</code> <code>unsigned int </code><i>which</i><code>,</code> <code>unsigned int </code><i>type_count</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; xkb</i></p>
<dd>
<dd>keyboard description in which to allocate client map</p>
<dt><i>&#8211; which</i></p>
<dd>mask selecting map components to allocate</p>
<dt><i>&#8211; type_count</i></p>
<dd>value of num_types field in map to be allocated</dl>
<h2>Description</h2>
<p>Calling <i>XkbGetMap </i> should be sufficient for most applications to get client and server maps. As a result, most applications do not need to directly allocate client and server maps. </p>
<p> If you change the number of key types or construct map components without loading the necessary components from the X server, do not allocate any map components directly using <i>malloc </i> or <i>Xmalloc. </i> Instead, use the Xkb allocators, <i>XkbAllocClientMap, </i> and <i>XkbAllocServerMap.</i> </p>
<p> Similarly, use the Xkb destructors, <i>XkbFreeClientMap, </i> and <i>XkbFreeServerMap </i> instead of <i>free </i> or <i>Xfree.</i> </p>
<p> <i>XkbAllocClientMap </i> allocates and initializes an empty client map in the <i>map </i> field of the keyboard description specified by <i>xkb. </i> The <i>which </i> parameter specifies the particular components of the client map structure to allocate and is a mask composed by a bitwise inclusive OR of one or more of the masks shown in Table 1. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=2>Table 1 XkbAllocClientMap Masks
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
<td>XkbKeyTypesMask</td>
<td> The type_count field specifies the number of entries to preallocate for the types field of the client map. If the type_count field is less than XkbNumRequiredTypes returns BadValue.
</td>
</tr>
<tr VALIGN=top>
<td>XkbKeySymsMask</td>
<td> The min_key_code and max_key_code fields of the xkb parameter are used to allocate the syms and key_sym_map fields of the client map. The fields are allocated to contain the maximum number of entries necessary for max_key_code &#8211; min_key_code + 1 keys.
</td>
</tr>
<tr VALIGN=top>
<td>XkbModifierMapMask</td>
<td> The min_key_code and max_key_code fields of the xkb parameter are used to allocate the modmap field of the client map. The field is allocated to contain the maximum number of entries necessary for max_key_code &#8211; min_key_code + 1 keys.
</td>
</tr>
</table>
<p> NOTE: The <i>min_key_code </i> and <i>max_key_code </i> fields of the <i>xkb </i> parameter must be legal values if the XkbKeySymsMask or XkbModifierMapMask masks are set in the <i>which </i> parameter. If they are not valid, <i>XkbAllocClientMap </i> returns BadValue. </p>
<p> If the client map of the keyboard description is not NULL, and any fields are already allocated in the client map, <i>XkbAllocClientMap </i> does not overwrite the existing values; it simply ignores that part of the request. The only exception is the <i>types </i> array. If <i>type_count </i> is greater than the current <i>num_types </i> field of the client map, <i>XkbAllocClientMap </i> resizes the <i>types </i> array and resets the <i>num_types </i> field accordingly. </p>
<p> If <i>XkbAllocClientMap </i> is successful, it returns Success. Otherwise, it can return either BadMatch, BadAlloc, or BadValue errors.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage</p>
<dt><code>BadMatch</code></p>
<dd>A compatible version of Xkb was not available in the server or an argument has correct type and range, but is otherwise invalid</p>
<dt><code>BadValue</code></p>
<dd>An argument is out of range</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkballocclientmap/">XkbAllocClientMap</a></code>(3), <code><a href="/docs/linux/man/3-xkballocservermap/">XkbAllocServerMap</a></code>(3), <code>XkbFreeClientMap,</code>(3), <code><a href="/docs/linux/man/3-xkbfreeservermap/">XkbFreeServerMap</a></code>(3), <code><a href="/docs/linux/man/3-xkbgetmap/">XkbGetMap</a></code>(3)</p>
