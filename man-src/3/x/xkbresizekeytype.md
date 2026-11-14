---
title: "xkbresizekeytype(3)"
name: "xkbresizekeytype"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbresizekeytype/"
description: "XkbResizeKeyType – Change the number of levels in a key type"
---

<p>XkbResizeKeyType &#8211; Change the number of levels in a key type </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbResizeKeyType</code> <code>(XkbDescPtr </code><i>xkb</i><code>,</code> <code>int </code><i>type_ndx</i><code>,</code> <code>int </code><i>map_count</i><code>,</code> <code>Bool </code><i>want_preserve</i><code>,</code> <code>int </code><i>new_num_lvls</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; xkb</i></p>
<dd>
<dd>keyboard description containing client map to update</p>
<dt><i>&#8211; type_ndx</i></p>
<dd>index in xkb-&gt;map-&gt;types of type to change</p>
<dt><i>&#8211; map_count</i></p>
<dd>total # of map entries needed for the type</p>
<dt><i>&#8211; want_preserve</i></p>
<dd>True =&gt; list of preserved modifiers is necessary</p>
<dt><i>&#8211; new_num_lvls</i></p>
<dd>new max # of levels for type</dl>
<h2>Description</h2>
<p><i>XkbResizeKeyType </i> changes the type specified by <i>xkb-&gt;map-&gt;types[type_ndx], </i> and reallocates the symbols and actions bound to all keys that use the type, if necessary. <i>XkbResizeKeyType </i> updates only the local copy of the types in <i>xkb; </i> to update the server&#8217;s copy for the physical device, use <i>XkbSetMap </i> or <i>XkbChangeMap </i> after calling <i>XkbResizeKeyType.</i> </p>
<p> The <i>map_count </i> parameter specifies the total number of map entries needed for the type, and can be zero or greater. If <i>map_count </i> is zero, <i>XkbResizeKeyType </i> frees the existing <i>map </i> and <i>preserve </i> entries for the type if they exist and sets them to NULL. </p>
<p> The <i>want_preserve </i> parameter specifies whether a <i>preserve </i> list for the key should be created. If <i>want_preserve </i> is True, the <i>preserve </i> list with <i>map_count </i> entries is allocated or reallocated if it already exists. Otherwise, if <i>want_preserve </i> is False, the <i>preserve </i> field is freed if necessary and set to NULL. </p>
<p> The <i>new_num_lvls </i> parameter specifies the new maximum number of shift levels for the type and is used to calculate and resize the symbols and actions bound to all keys that use the type. </p>
<p> If <i>type_ndx </i> does not specify a legal type, <i>new_num_lvls </i> is less than 1, or the <i>map_count </i> is less than zero, <i>XkbResizeKeyType </i> returns BadValue. If <i>XkbResizeKeyType </i> encounters any problems with allocation, it returns BadAlloc. Otherwise, it returns Success.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>Success</p>
<dd>The <i>XkbResizeKeyType </i> function returns Success if <i>type_ndx </i> specifies a legal type, <i>new_num_lvls </i> is greater than zero and <i>map_count </i> is positive.</dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage</p>
<dt><code>BadValue</code></p>
<dd>An argument is out of range</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbchangemap/">XkbChangeMap</a></code>(3), <code><a href="/docs/linux/man/3-xkbsetmap/">XkbSetMap</a></code>(3)</p>
