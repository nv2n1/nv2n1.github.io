---
title: "xkbchangenames(3)"
name: "xkbchangenames"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbchangenames/"
description: "XkbChangeNames – _summary-line_"
---

<p>XkbChangeNames &#8211; _summary-line_ </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbChangeNames</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>unsigned int </code><i>which</i><code>,</code> <code>XkbDescPtr </code><i>Xkb</i><code>);</code><br />
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
<p><i>XkbChangeNames </i> provides a more flexible method for changing symbolic names than <i>XkbSetNames </i> and requires the use of an XkbNameChangesRec structure. </p>
<p> <i>XkbChangeNames </i> copies any names specified by <i>changes </i> from the keyboard description, <i>xkb, </i> to the X server specified by <i>dpy. XkbChangeNames </i> aborts and returns False if any illegal type names or type shift level names are specified by changes. </p>
<p> To change the symbolic names in the server, first modify a local copy of the keyboard description and then use either <i>XkbSetNames, </i> or, to save network traffic, use a XkbNameChangesRec structure and call <i>XkbChangeNames </i> to download the changes to the server. <i>XkbSetNames </i> and <i>XkbChangeNames </i> can generate BadAlloc, BadAtom, BadLength, BadMatch, and BadImplementation errors.</p>
<h2>Structures</h2>
<p>The XkbNameChangesRec allows applications to identify small modifications to the symbolic names and effectively reduces the amount of traffic sent to the server: </p>
<pre> typedef struct _XkbNameChanges {
 unsigned int changed; /* name components that have changed 
*/
 unsigned char first_type; /* first key type with a new name */
 unsigned char num_types; /* number of types with new names */
 unsigned char first_lvl; /* first key type with new level 
names */
 unsigned char num_lvls; /* number of key types with new level 
names */
 unsigned char num_aliases; /* if key aliases changed, total 
number of key aliases */
 unsigned char num_rg; /* if radio groups changed, total 
number of radio groups */
 unsigned char first_key; /* first key with a new name */
 unsigned char num_keys; /* number of keys with new names */
 unsigned short changed_vmods; /* mask of virtual modifiers for 
which names have changed */
 unsigned long changed_indicators; /* mask of indicators for which names 
were changed */
 unsigned char changed_groups; /* mask of groups for which names 
were changed */
 } XkbNameChangesRec, *XkbNameChangesPtr</pre>
<p>The <i>changed </i> field specifies the name components that have changed and is the bitwise inclusive OR of the valid names mask bits defined in Table 1. The rest of the fields in the structure specify the ranges that have changed for the various kinds of symbolic names, as shown in Table 2. </p>
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
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=4>Table 2 XkbNameChanges Fields
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Mask</td>
<td>Fields</td>
<td>Component</td>
<td>Field
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XkbKeyTypeNamesMask</td>
<td>first_type,</td>
<td>Xkb-&gt;map</td>
<td>type[*].name
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>num_types</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>XkbKTLevelNamesMask</td>
<td>first_lvl,</td>
<td>Xkb-&gt;map</td>
<td>type[*].lvl_names[*]
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>num_lvls</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>XkbKeyAliasesMask</td>
<td>num_aliases</td>
<td>Xkb-&gt;names</td>
<td>key_aliases[*]
</td>
</tr>
<tr VALIGN=top>
<td>XkbRGNamesMask</td>
<td>num_rg</td>
<td>Xkb-&gt;names</td>
<td>radio_groups[*]
</td>
</tr>
<tr VALIGN=top>
<td>XkbKeyNamesMask</td>
<td>first_key,</td>
<td>Xkb-&gt;names</td>
<td>keys[*]
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>num_keys</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>XkbVirtualModNamesMask</td>
<td>changed_vmods</td>
<td>Xkb-&gt;names</td>
<td>vmods[*]
</td>
</tr>
<tr VALIGN=top>
<td>XkbIndicatorNamesMask</td>
<td>changed_indicators</td>
<td>Xkb-&gt;names</td>
<td>indicators[*]
</td>
</tr>
<tr VALIGN=top>
<td>XkbGroupNamesMask</td>
<td>changed_groups</td>
<td>Xkb-&gt;names</td>
<td>groups[*]
</td>
</tr>
</table>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage</p>
<dt><code>BadAtom</code></p>
<dd>A name is neither a valid Atom or None</p>
<dt><code>BadImplementation</code></p>
<dd>Invalid reply from server</p>
<dt><code>BadLength</code></p>
<dd>The length of a request is shorter or longer than that required to minimally contain the arguments</p>
<dt><code>BadMatch</code></p>
<dd>A compatible version of Xkb was not available in the server or an argument has correct type and range, but is otherwise invalid</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbsetnames/">XkbSetNames</a></code>(3)</p>
