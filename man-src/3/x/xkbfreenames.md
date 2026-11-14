---
title: "xkbfreenames(3)"
name: "xkbfreenames"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbfreenames/"
description: "XkbFreeNames – Free symbolic names structures"
---

<p>XkbFreeNames &#8211; Free symbolic names structures </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>void XkbFreeNames</code> <code>(XkbDescPtr </code><i>xkb</i><code>,</code> <code>unsigned int </code><i>which</i><code>,</code> <code>Bool </code><i>free_map</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; xkb</i></p>
<dd>
<dd>keyboard description for which names are to be freed</p>
<dt><i>&#8211; which</i></p>
<dd>mask of names components to be freed</p>
<dt><i>&#8211; free_map</i></p>
<dd>True =&gt; XkbNamesRec structure itself should be freed</dl>
<h2>Description</h2>
<p>Do not free symbolic names structures directly using <i>free </i> or <i>XFree. </i> Use <i>XkbFreeNames </i> instead. </p>
<p> The <i>which </i> parameter is the bitwise inclusive OR of the valid names mask bits defined in Table 1. </p>
<p> Xkb provides several functions that work with symbolic names. Each of these functions uses a mask to specify individual fields of the structures described above. These masks and their relationships to the fields in a keyboard description are shown in Table 1. </p>
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
