---
title: "xkballoccompatmap(3)"
name: "xkballoccompatmap"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkballoccompatmap/"
description: "XkbAllocCompatMap – Allocate a new compatibility map if you do not already have one available"
---

<p>XkbAllocCompatMap &#8211; Allocate a new compatibility map if you do not already have one available </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbAllocCompatMap</code> <code>(XkbDescPtr </code><i>xkb</i><code>,</code> <code>unsigned int </code><i>which</i><code>,</code> <code>unsigned int </code><i>num_si</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; xkb</i></p>
<dd>
<dd>keyboard description in which to allocate compat map</p>
<dt><i>&#8211; which</i></p>
<dd>mask of compatibility map components to allocate</p>
<dt><i>&#8211; num_si</i></p>
<dd>number of symbol interpretations to allocate</dl>
<h2>Description</h2>
<p><i>xkb </i> specifies the keyboard description for which compatibility maps are to be allocated. The compatibility map is the <i>compat </i> field in this structure. </p>
<p> <i>which </i> specifies the compatibility map components to be allocated (see XkbGetCompatMap). <i>which </i> is an inclusive OR of the bits shown in Table 1. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3>Table 1 Compatibility Map Component Masks
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Mask</td>
<td>Value</td>
<td>Affecting
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XkbSymInterpMask</td>
<td>(1&lt;&lt;0)</td>
<td>Symbol interpretations
</td>
</tr>
<tr VALIGN=top>
<td>XkbGroupCompatMask</td>
<td>(1&lt;&lt;1)</td>
<td>Group maps
</td>
</tr>
<tr VALIGN=top>
<td>XkbAllCompatMask</td>
<td>(0x3)</td>
<td>All compatibility map components
</td>
</tr>
</table>
<p> <i>num_si </i> specifies the total number of entries to allocate in the symbol interpretation vector <i>(xkb.compat.sym_interpret).</i> </p>
<p> <i>XkbAllocCompatMap </i> returns Success if successful, BadMatch if <i>xkb </i> is NULL, or BadAlloc if errors are encountered when attempting to allocate storage.</p>
<h2>Structures</h2>
<pre> typedef struct {
 KeySym sym; /* keysym of interest or NULL */
 unsigned char flags; /* XkbSI_AutoRepeat, XkbSI_LockingKey */
 unsigned char match; /* specifies how mods is interpreted */
 unsigned char mods; /* modifier bits, correspond to eight real modifiers */
 unsigned char virtual_mod; /* 1 modifier to add to key virtual mod map */
 XkbAnyAction act; /* action to bind to symbol position on key */
 } XkbSymInterpretRec,*XkbSymInterpretPtr;</pre>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage</p>
<dt><code>BadMatch</code></p>
<dd>A compatible version of Xkb was not available in the server or an argument has correct type and range, but is otherwise invalid</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbgetcompatmap/">XkbGetCompatMap</a></code>(3)</p>
<h2>Notes</h2>
<p>Note that symbol interpretations in a compatibility map (the <i>sym_interpret </i> vector of XkbSymInterpretRec structures) are also allocated using this same function. To ensure that there is sufficient space in the symbol interpretation vector for entries to be added, use <i>XkbAllocCompatMap </i> specifying <i>which </i> as XkbSymInterpretMask and the number of free symbol interpretations needed in <i>num_si.</i></p>
