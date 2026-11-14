---
title: "xkbnotenamechanges(3)"
name: "xkbnotenamechanges"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbnotenamechanges/"
description: "XkbNoteNameChanges – Note the changed names in a changes structure"
---

<p>XkbNoteNameChanges &#8211; Note the changed names in a changes structure </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>void XkbNoteNameChanges</code> <code>(XkbNameChangesPtr </code><i>old</i><code>,</code> <code>XkbNamesNotifyEvent *</code><i>new</i><code>,</code> <code>unsigned int </code><i>wanted</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; old</i></p>
<dd>
<dd>XkbNameChanges structure to be updated</p>
<dt><i>&#8211; new</i></p>
<dd>event from which changes are to be copied</p>
<dt><i>&#8211; wanted</i></p>
<dd>types of names for which changes are to be noted</dl>
<h2>Description</h2>
<p>When your application receives a XkbNamesNotify event, you can note the changed names in a changes structure using <i>XkbNoteNameChanges.</i> </p>
<p> The <i>wanted </i> parameter is the bitwise inclusive OR of the valid names mask bits shown in Table 1. <i>XkbNoteNameChanges </i> copies any changes that are reported in <i>new </i> and specified in <i>wanted </i> into the changes record specified by <i>old.</i> </p>
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
