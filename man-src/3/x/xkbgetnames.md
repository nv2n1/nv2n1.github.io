---
title: "xkbgetnames(3)"
name: "xkbgetnames"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbgetnames/"
description: "XkbGetNames – Obtain symbolic names from the server"
---

<p>XkbGetNames &#8211; Obtain symbolic names from the server </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbGetNames</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>unsigned int </code><i>which</i><code>,</code> <code>XkbDescPtr </code><i>Xkb</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>
<dd>connection to the X server</p>
<dt><i>&#8211; which</i></p>
<dd>mask of names or map components to be updated</p>
<dt><i>&#8211; Xkb</i></p>
<dd>keyboard description to be updated</dl>
<h2>Description</h2>
<p><i>XkbGetNames </i> retrieves symbolic names for the components of the keyboard extension from the X server. The <i>which </i> parameter specifies the name components to be updated in the <i>xkb </i> parameter, and is the bitwise inclusive OR of the valid names mask bits defined in Table 1. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=4>Table 1 Symbolic Names Masks
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Mask Bit</td>
<td>Value</td>
<td>Keyboard</td>
<td>Field
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>Component</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XkbKeycodesNameMask</td>
<td>(1&lt;&lt;0)</td>
<td>Xkb-&gt;names</td>
<td>keycodes
</td>
</tr>
<tr VALIGN=top>
<td>XkbGeometryNameMask</td>
<td>(1&lt;&lt;1)</td>
<td>Xkb-&gt;names</td>
<td>geometry
</td>
</tr>
<tr VALIGN=top>
<td>XkbSymbolsNameMask</td>
<td>(1&lt;&lt;2)</td>
<td>Xkb-&gt;names</td>
<td>symbols
</td>
</tr>
<tr VALIGN=top>
<td>XkbPhysSymbolsNameMask</td>
<td>(1&lt;&lt;3)</td>
<td>Xkb-&gt;names</td>
<td>phys_symbols
</td>
</tr>
<tr VALIGN=top>
<td>XkbTypesNameMask</td>
<td>(1&lt;&lt;4)</td>
<td>Xkb-&gt;names</td>
<td>type
</td>
</tr>
<tr VALIGN=top>
<td>XkbCompatNameMask</td>
<td>(1&lt;&lt;5)</td>
<td>Xkb-&gt;names</td>
<td>compat
</td>
</tr>
<tr VALIGN=top>
<td>XkbKeyTypeNamesMask</td>
<td>(1&lt;&lt;6)</td>
<td>Xkb-&gt;map</td>
<td>type[*].name
</td>
</tr>
<tr VALIGN=top>
<td>XkbKTLevelNamesMask</td>
<td>(1&lt;&lt;7)</td>
<td>Xkb-&gt;map</td>
<td>type[*].lvl_names[*]
</td>
</tr>
<tr VALIGN=top>
<td>XkbIndicatorNamesMask</td>
<td>(1&lt;&lt;8)</td>
<td>Xkb-&gt;names</td>
<td>indicators[*]
</td>
</tr>
<tr VALIGN=top>
<td>XkbKeyNamesMask</td>
<td>(1&lt;&lt;9)</td>
<td>Xkb-&gt;names</td>
<td>keys[*], num_keys
</td>
</tr>
<tr VALIGN=top>
<td>XkbKeyAliasesMask</td>
<td>(1&lt;&lt;10)</td>
<td>Xkb-&gt;names</td>
<td>key_aliases[*], num_key_aliases
</td>
</tr>
<tr VALIGN=top>
<td>XkbVirtualModNamesMask</td>
<td>(1&lt;&lt;11)</td>
<td>Xkb-&gt;names</td>
<td>vmods[*]
</td>
</tr>
<tr VALIGN=top>
<td>XkbGroupNamesMask</td>
<td>(1&lt;&lt;12)</td>
<td>Xkb-&gt;names</td>
<td>groups[*]
</td>
</tr>
<tr VALIGN=top>
<td>XkbRGNamesMask</td>
<td>(1&lt;&lt;13)</td>
<td>Xkb-&gt;names</td>
<td>radio_groups[*], num_rg
</td>
</tr>
<tr VALIGN=top>
<td>XkbComponentNamesMask</td>
<td>(0x3f)</td>
<td>Xkb-&gt;names</td>
<td>keycodes,
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td></td>
<td>geometry,
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td></td>
<td>symbols,
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td></td>
<td>physical symbols,
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td></td>
<td>types, and
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td></td>
<td>compatibility map
</td>
</tr>
<tr VALIGN=top>
<td>XkbAllNamesMask</td>
<td>(0x3fff)</td>
<td>Xkb-&gt;names</td>
<td>all name components
</td>
</tr>
</table>
<p> If the <i>names </i> field of the keyboard description <i>xkb </i> is NULL, <i>XkbGetNames </i> allocates and initializes the <i>names </i> component of the keyboard description before obtaining the values specified by <i>which. </i> If the <i>names field of </i> <i>xkb </i> is not NULL, <i>XkbGetNames </i> obtains the values specified by <i>which </i> and copies them into the keyboard description <i>Xkb.</i> </p>
<p> If the <i>map </i> component of the <i>xkb </i> parameter is NULL, <i>XkbGetNames </i> does not retrieve type or shift level names, even if XkbKeyTypeNamesMask or XkbKTLevelNamesMask are set in <i>which.</i> </p>
<p> <i>XkbGetNames </i> can return Success, or BadAlloc, BadLength, BadMatch, and BadImplementation errors. </p>
<p> To free symbolic names, use <i>XkbFreeNames.</i></p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage</p>
<dt><code>BadImplementation</code></p>
<dd>Invalid reply from server</p>
<dt><code>BadLength</code></p>
<dd>The length of a request is shorter or longer than that required to minimally contain the arguments</p>
<dt><code>BadMatch</code></p>
<dd>A compatible version of Xkb was not available in the server or an argument has correct type and range, but is otherwise invalid</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbfreenames/">XkbFreeNames</a></code>(3)</p>
