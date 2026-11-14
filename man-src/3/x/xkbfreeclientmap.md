---
title: "xkbfreeclientmap(3)"
name: "xkbfreeclientmap"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbfreeclientmap/"
description: "XkbFreeClientMap – Free memory used by the client map member of an XkbDescRec structure"
---

<p>XkbFreeClientMap &#8211; Free memory used by the client map member of an XkbDescRec structure </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>void XkbFreeClientMap</code> <code>(XkbDescPtr </code><i>xkb</i><code>,</code> <code>unsigned int </code><i>which</i><code>,</code> <code>Bool </code><i>free_all</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; xkb</i></p>
<dd>
<dd>keyboard description containing client map to free</p>
<dt><i>&#8211; which</i></p>
<dd>mask identifying components of map to free</p>
<dt><i>&#8211; free_all</i></p>
<dd>True =&gt; free all client components and map itself</dl>
<h2>Description</h2>
<p><i>XkbFreeClientMap </i> frees the components of client map specified by <i>which </i> in the XkbDescRec structure specified by the <i>xkb </i> parameter and sets the corresponding structure component values to NULL. The <i>which </i> parameter specifies a combination of the client map masks shown in Table 1. </p>
<p> If <i>free_all </i> is True, <i>which </i> is ignored; <i>XkbFreeClientMap </i> frees every non-NULL structure component in the client map, frees the XkbClientMapRec structure referenced by the <i>map </i> member of the <i>xkb </i> parameter, and sets the <i>map </i> member to NULL. </p>
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
<p> NOTE: The <i>min_key_code </i> and <i>max_key_code </i> fields of the <i>xkb </i> parameter must be legal values if the XkbKeySymsMask or XkbModifierMapMask masks are set in the <i>which </i> parameter. If they are not valid, <i>XkbAllocClientMap </i> returns BadValue.</p>
<h2>Structures</h2>
<p>The complete description of an Xkb keyboard is given by an XkbDescRec. The component structures in the XkbDescRec represent the major Xkb components. </p>
<pre>typedef struct {
 struct _XDisplay * display; /* connection to X server */
 unsigned short flags; /* private to Xkb, do not modify */
 unsigned short device_spec; /* device of interest */
 KeyCode min_key_code; /* minimum keycode for device */
 KeyCode max_key_code; /* maximum keycode for device */
 XkbControlsPtr ctrls; /* controls */
 XkbServerMapPtr server; /* server keymap */
 XkbClientMapPtr map; /* client keymap */
 XkbIndicatorPtr indicators; /* indicator map */
 XkbNamesPtr names; /* names for all components */
 XkbCompatMapPtr compat; /* compatibility map */
 XkbGeometryPtr geom; /* physical geometry of keyboard */
} XkbDescRec, *XkbDescPtr;</pre>
<p>The <i>display </i> field points to an X display structure. The <i>flags field is private to the library: modifying </i> <i>flags </i> may yield unpredictable results. The <i>device_spec </i> field specifies the device identifier of the keyboard input device, or XkbUseCoreKeyboard, which specifies the core keyboard device. The <i>min_key_code</i> and <i>max_key_code </i> fields specify the least and greatest keycode that can be returned by the keyboard. </p>
<p> Each structure component has a corresponding mask bit that is used in function calls to indicate that the structure should be manipulated in some manner, such as allocating it or freeing it. These masks and their relationships to the fields in the XkbDescRec are shown in Table 2. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3>Table 2 Mask Bits for XkbDescRec
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Mask Bit</td>
<td>XkbDescRec Field</td>
<td>Value
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XkbControlsMask</td>
<td>ctrls</td>
<td>(1L&lt;&lt;0)
</td>
</tr>
<tr VALIGN=top>
<td>XkbServerMapMask</td>
<td>server</td>
<td>(1L&lt;&lt;1)
</td>
</tr>
<tr VALIGN=top>
<td>XkbIClientMapMask</td>
<td>map</td>
<td>(1L&lt;&lt;2)
</td>
</tr>
<tr VALIGN=top>
<td>XkbIndicatorMapMask</td>
<td>indicators</td>
<td>(1L&lt;&lt;3)
</td>
</tr>
<tr VALIGN=top>
<td>XkbNamesMask</td>
<td>names</td>
<td>(1L&lt;&lt;4)
</td>
</tr>
<tr VALIGN=top>
<td>XkbCompatMapMask</td>
<td>compat</td>
<td>(1L&lt;&lt;5)
</td>
</tr>
<tr VALIGN=top>
<td>XkbGeometryMask</td>
<td>geom</td>
<td>(1L&lt;&lt;6)
</td>
</tr>
<tr VALIGN=top>
<td>XkbAllComponentsMask</td>
<td>All Fields</td>
<td>(0x7f)
</td>
</tr>
</table>
<p> The <i>map </i> field of the complete Xkb keyboard description is a pointer to the Xkb client map, which is of type XkbClientMapRec: </p>
<pre> typedef struct { /* Client Map */
 unsigned char size_types; /* # occupied entries in types */
 unsigned char num_types; /* # entries in types */
 XkbKeyTypePtr types; /* vector of key types used by this keymap */
 unsigned short size_syms; /* length of the syms array */
 unsigned short num_syms; /* # entries in syms */
 KeySym * syms; /* linear 2d tables of keysyms, 1 per key */
 XkbSymMapPtr key_sym_map; /* 1 per keycode, maps keycode to syms */
 unsigned char * modmap; /* 1 per keycode, real mods bound to key */
} XkbClientMapRec, *XkbClientMapPtr;</pre>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadValue</code></p>
<dd>An argument is out of range</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkballocclientmap/">XkbAllocClientMap</a></code>(3)</p>
