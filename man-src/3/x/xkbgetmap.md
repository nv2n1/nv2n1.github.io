---
title: "xkbgetmap(3)"
name: "xkbgetmap"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbgetmap/"
description: "XkbGetMap – Allocate an XkbDescRec structure and populate it with the server’s keyboard client map and server map"
---

<p>XkbGetMap &#8211; Allocate an XkbDescRec structure and populate it with the server&#8217;s keyboard client map and server map </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>XkbDescPtr XkbGetMap</code> <code>(Display *</code><i>display</i><code>,</code> <code>unsigned int </code><i>which</i><code>,</code> <code>unsigned int </code><i>device_spec</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; display</i></p>
<dd>
<dd>connection to X server</p>
<dt><i>&#8211; which</i></p>
<dd>mask selecting subcomponents to populate</p>
<dt><i>&#8211; device_spec</i></p>
<dd>device_id, or XkbUseCoreKbd</dl>
<h2>Description</h2>
<p>Xkb provides two functions to obtain the keyboard mapping components from the server. The first function, <i>XkbGetMap, </i> allocates an XkbDescRec structure, retrieves mapping components from the server, and stores them in the XkbDescRec structure it just allocated. The second function, <i>XkbGetUpdatedMap, </i> retrieves mapping components from the server and stores them in an XkbDescRec structure that has previously been allocated. </p>
<p> To allocate an XkbDescRec structure and populate it with the server&#8217;s keyboard client map and server map, use <i>XkbGetMap. XkbGetMap </i> is similar to <i>XkbGetKeyboard,</i> but is used only for obtaining the address of an XkbDescRec structure that is populated with keyboard mapping components. It allows finer control over which substructures of the keyboard mapping components are to be populated. <i>XkbGetKeyboard </i> always returns fully populated components, while <i>XkbGetMap </i> can be instructed to return a partially populated component. </p>
<p> The <i>which mask is a bitwise inclusive OR of the masks defined in Table 14.1. Only </i> those portions of the keyboard server map and the keyboard client maps that are specified in <i>which </i> are allocated and populated. </p>
<p> In addition to allocating and obtaining the server map and the client map, <i>XkbGetMap </i> also sets the <i>device_spec, </i> the <i>min_key_code, </i> and <i>max_key_code </i> fields of the keyboard description. </p>
<p> <i>XkbGetMap </i> is synchronous; it queries the server for the desired information, waits for a reply, and then returns. If successful, <i>XkbGetMap </i> returns a pointer to the XkbDescRec structure it allocated. If unsuccessful, <i>XkbGetMap </i> returns NULL. When unsuccessful, one of the following protocol errors is also generated: BadAlloc (unable to allocate the XkbDescRec structure), BadValue (some mask bits in <i>which </i> are undefined), or BadImplementation (a compatible version of the Xkb extension is not available in the server). To free the returned data, use <i>XkbFreeKeyboard.</i> </p>
<p> Xkb also provides convenience functions to get partial component definitions from the server. These functions are specified in the &quot;convenience functions&quot; column in Table 1. Refer to the sections listed in the table for more information on these functions. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5>Table 1 Xkb Mapping Component Masks
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5>and Convenience Functions
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Mask</td>
<td>Value</td>
<td>Map</td>
<td>Fields</td>
<td>Convenience
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Functions
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> XkbKeyTypesMask </td>
<td>(1&lt;&lt;0)</td>
<td>client</td>
<td> types<br />
 size_types<br />
 num_types </td>
<td> XkbGetKeyTypes<br />
 XkbResizeKeyType<br />
 XkbCopyKeyType<br />
 XkbCopyKeyTypes
</td>
</tr>
<tr VALIGN=top>
<td> XkbKeySymsMask </td>
<td>(1&lt;&lt;1)</td>
<td>client</td>
<td> syms<br />
 size_syms<br />
 num_syms<br />
 key_sym_map </td>
<td> XkbGetKeySyms<br />
 XkbResizeKeySyms<br />
 XkbChangeTypesOfKey
</td>
</tr>
<tr VALIGN=top>
<td> XkbModifierMapMask </td>
<td>(1&lt;&lt;2)</td>
<td>client</td>
<td>modmap</td>
<td> XkbGetKeyModifierMap
</td>
</tr>
<tr VALIGN=top>
<td> XkbExplicitComponentsMask </td>
<td>(1&lt;&lt;3)</td>
<td>server</td>
<td> explicit </td>
<td> XkbGetKeyExplicitComponents
</td>
</tr>
<tr VALIGN=top>
<td> XkbKeyActionsMask </td>
<td>(1&lt;&lt;4)</td>
<td>server</td>
<td> key_acts<br />
 acts<br />
 num_acts<br />
 size_acts </td>
<td> XkbGetKeyActions<br />
 XkbResizeKeyActions
</td>
</tr>
<tr VALIGN=top>
<td> XkbKeyBehaviorsMask </td>
<td>(1&lt;&lt;5)</td>
<td>server</td>
<td> behaviors </td>
<td> XkbGetKeyBehaviors
</td>
</tr>
<tr VALIGN=top>
<td> XkbVirtualModsMask </td>
<td>(1&lt;&lt;6)</td>
<td>server</td>
<td> vmods </td>
<td> XkbGetVirtualMods
</td>
</tr>
<tr VALIGN=top>
<td> XkbVirtualModMapMask </td>
<td>(1&lt;&lt;7)</td>
<td>server</td>
<td> vmodmap </td>
<td> XkbGetVirtualModMap
</td>
</tr>
</table>
<pre>Xkb defines combinations of these masks for convenience:
 
 #define XkbResizableInfoMask (XkbKeyTypesMask)
 #define XkbAllClientInfoMask (XkbKeyTypesMask | XkbKeySymsMask |
 XkbModifierMapMask)
 #define XkbAllServerInfoMask (XkbExplicitComponentsMask |
 XkbKeyActionsMask | 
 XkbKeyBehaviorsMask |
 XkbVirtualModsMask | 
 XkbVirtualModMapMask)
 #define XkbAllMapComponentsMask XkbAllClientInfoMask | 
 XkbAllServerInfoMask)</pre>
<p>Key types, symbol maps, and actions are all interrelated: changes in one require changes in the others. The convenience functions make it easier to edit these components and handle the interdependencies. </p>
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
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbchangetypesofkey/">XkbChangeTypesOfKey</a></code>(3), <code><a href="/docs/linux/man/3-xkbcopykeytype/">XkbCopyKeyType</a></code>(3), <code><a href="/docs/linux/man/3-xkbcopykeytypes/">XkbCopyKeyTypes</a></code>(3), <code><a href="/docs/linux/man/3-xkbfreeclientmap/">XkbFreeClientMap</a></code>(3), <code><a href="/docs/linux/man/3-xkbgetkeyactions/">XkbGetKeyActions</a></code>(3), <code><a href="/docs/linux/man/3-xkbgetkeybehaviors/">XkbGetKeyBehaviors</a></code>(3), <code><a href="/docs/linux/man/3-xkbgetkeyboard/">XkbGetKeyboard</a></code>(3), <code><a href="/docs/linux/man/3-xkbgetkeyexplicitcomponents/">XkbGetKeyExplicitComponents</a></code>(3), <code><a href="/docs/linux/man/3-xkbgetkeymodifiermap/">XkbGetKeyModifierMap</a></code>(3), <code><a href="/docs/linux/man/3-xkbgetkeysyms/">XkbGetKeySyms</a></code>(3), <code><a href="/docs/linux/man/3-xkbgetkeytypes/">XkbGetKeyTypes</a></code>(3), <code><a href="/docs/linux/man/3-xkbgetupdatedmap/">XkbGetUpdatedMap</a></code>(3), <code><a href="/docs/linux/man/3-xkbgetvirtualmodmap/">XkbGetVirtualModMap</a></code>(3), <code><a href="/docs/linux/man/3-xkbgetvirtualmods/">XkbGetVirtualMods</a></code>(3), <code><a href="/docs/linux/man/3-xkbresizekeyactions/">XkbResizeKeyActions</a></code>(3), <code><a href="/docs/linux/man/3-xkbresizekeysyms/">XkbResizeKeySyms</a></code>(3), <code><a href="/docs/linux/man/3-xkbresizekeytype/">XkbResizeKeyType</a></code>(3)</p>
