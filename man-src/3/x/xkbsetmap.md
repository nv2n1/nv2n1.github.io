---
title: "xkbsetmap(3)"
name: "xkbsetmap"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbsetmap/"
description: "XkbSetMap – Send a complete new set of values for entire components to the server."
---

<p>XkbSetMap &#8211; Send a complete new set of values for entire components to the server. </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbSetMap</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>unsigned int </code><i>which</i><code>,</code> <code>XkbDescPtr </code><i>xkb</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>
<dd>connection to X server</p>
<dt><i>&#8211; which</i></p>
<dd>mask selecting subcomponents to update</p>
<dt><i>&#8211; xkb</i></p>
<dd>description from which new values are taken</dl>
<h2>Description</h2>
<p>There are two ways to make changes to map components: either change a local copy of the keyboard map and call <i>XkbSetMap </i> to send the modified map to the server, or, to reduce network traffic, use an XkbMapChangesRec structure and call <i>XkbChangeMap.</i> </p>
<p> Use <i>XkbSetMap </i> to send a complete new set of values for entire components (for example, all symbols, all actions, and so on) to the server. The <i>which </i> parameter specifies the components to be sent to the server, and is a bitwise inclusive OR of the masks listed in Table 1. The <i>xkb </i> parameter is a pointer to an XkbDescRec structure and contains the information to be copied to the server. For each bit set in the <i>which </i> parameter, <i>XkbSetMap </i> takes the corresponding structure values from the <i>xkb </i> parameter and sends it to the server specified by <i>dpy. </i> </p>
<p> If any components specified by <i>which </i> are not present in the <i>xkb </i> parameter, <i>XkbSetMap </i> returns False. Otherwise, it sends the update request to the server and returns True. <i>XkbSetMap </i> can generate BadAlloc, BadLength, and BadValue protocol errors. </p>
<p> Key types, symbol maps, and actions are all interrelated; changes in one require changes in the others. Xkb provides functions to make it easier to edit these components and handle the interdependencies. Table 1 lists these helper functions and provides a pointer to where they are defined. </p>
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
<p> The <i>changed </i> field identifies the map components that have changed in an XkbDescRec structure and may contain any of the bits in Table 1, which are also shown in Table 2. Every 1 bit in <i>changed </i> also identifies which other fields in the XkbMapChangesRec structure contain valid values, as indicated in Table 2. The <i>min_key_code </i> and <i>max_key_code </i> fields are for reference only; they are ignored on any requests sent to the server and are always updated by the server whenever it returns the data for an XkbMapChangesRec. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3>Table 2 XkbMapChangesRec Masks
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Valid</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>Mask</td>
<td>XkbMapChangesRec</td>
<td>XkbDescRec Field Containing
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Fields</td>
<td>Changed Data
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XkbKeyTypesMask</td>
<td>first_type,</td>
<td>map-&gt;type[first_type] ..
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>num_types</td>
<td>map-&gt;type[first_type + num_types &#8211; 1]
</td>
</tr>
<tr VALIGN=top>
<td>XkbKeySymsMask</td>
<td>first_key_sym,</td>
<td>map-&gt;key_sym_map[first_key_sym] ..
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>num_key_syms</td>
<td>map-&gt;key_sym_map[first_key_sym +
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>num_key_syms &#8211; 1]
</td>
</tr>
<tr VALIGN=top>
<td>XkbModifierMapMask</td>
<td>first_modmap_key,</td>
<td>map-&gt;modmap[first_modmap_key] ..
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>num_modmap_keys</td>
<td>map-&gt;modmap[first_modmap_key +
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>num_modmap_keys-1]
</td>
</tr>
<tr VALIGN=top>
<td>XkbExplicitComponentsMask</td>
<td>first_key_explicit,</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>server-&gt;explicit[first_key_explicit] ..</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>num_key_explicit</td>
<td>server-&gt;explicit[first_key_explicit +
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>num_key_explicit &#8211; 1]
</td>
</tr>
<tr VALIGN=top>
<td>XkbKeyActionsMask</td>
<td>first_key_act,</td>
<td>server-&gt;key_acts[first_key_act] ..
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>num_key_acts</td>
<td>server-&gt;key_acts[first_key_act +
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>num_key_acts &#8211; 1]
</td>
</tr>
<tr VALIGN=top>
<td>XkbKeyBehaviorsMask</td>
<td>first_key_behavior,</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>server-&gt;behaviors[first_key_behavior] ..</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>num_key_behaviors</td>
<td>server-&gt;behaviors[first_key_behavior +
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>num_key_behaviors &#8211; 1]
</td>
</tr>
<tr VALIGN=top>
<td>XkbVirtualModsMask</td>
<td>vmods</td>
<td>server-&gt;vmods[*]
</td>
</tr>
<tr VALIGN=top>
<td>XkbVirtualModMapMask</td>
<td>first_vmodmap_key,</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>server-&gt;vmodmap[first_vmodmap_key]</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>num_vmodmap_keys</td>
<td> ..
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>server-&gt;vmodmap[first_vmodmap_key
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>+ num_vmodmap_keys &#8211; 1]
</td>
</tr>
</table>
<h2>Return Values</h2>
<dl COMPACT>
<dt>True</p>
<dd>The <i>XkbSetMap </i> function returns True all components specified by <i>which </i> are present in the <i>xkb </i> parameter.</p>
<dt>False</p>
<dd>The <i>XkbSetMap </i> function returns False if any component specified by <i>which </i> is not present in the <i>xkb </i> parameter.</dl>
<h2>Structures</h2>
<p>Use the XkbMapChangesRec structure to identify and track partial modifications to the mapping components and to reduce the amount of traffic between the server and clients. </p>
<pre>typedef struct _XkbMapChanges {
 unsigned short changed; /* identifies valid components in structure */
 KeyCode min_key_code; /* lowest numbered keycode for device */
 KeyCode max_key_code; /* highest numbered keycode for device */
 unsigned char first_type; /* index of first key type modified */
 unsigned char num_types; /* # types modified */
 KeyCode first_key_sym; /* first key whose key_sym_map changed */
 unsigned char num_key_syms; /* # key_sym_map entries changed */
 KeyCode first_key_act; /* first key whose key_acts entry changed */
 unsigned char num_key_acts; /* # key_acts entries changed */
 KeyCode first_key_behavior; /* first key whose behaviors changed */
 unsigned char num_key_behaviors; /* # behaviors entries changed */
 KeyCode first_key_explicit; /* first key whose explicit entry changed */
 unsigned char num_key_explicit; /* # explicit entries changed */
 KeyCode first_modmap_key; /* first key whose modmap entry changed */
 unsigned char num_modmap_keys; /* # modmap entries changed */
 KeyCode first_vmodmap_key; /* first key whose vmodmap changed */
 unsigned char num_vmodmap_keys; /* # vmodmap entries changed */
 unsigned char pad1; /* reserved */
 unsigned short vmods; /* mask indicating which vmods changed */
} XkbMapChangesRec,*XkbMapChangesPtr;</pre>
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
<p> Each structure component has a corresponding mask bit that is used in function calls to indicate that the structure should be manipulated in some manner, such as allocating it or freeing it. These masks and their relationships to the fields in the XkbDescRec are shown in Table 3. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3>Table 3 Mask Bits for XkbDescRec
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
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage</p>
<dt><code>BadLength</code></p>
<dd>The length of a request is shorter or longer than that required to minimally contain the arguments</p>
<dt><code>BadValue</code></p>
<dd>An argument is out of range</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbchangemap/">XkbChangeMap</a></code>(3), <code><a href="/docs/linux/man/3-xkbchangetypesofkey/">XkbChangeTypesOfKey</a></code>(3), <code><a href="/docs/linux/man/3-xkbcopykeytype/">XkbCopyKeyType</a></code>(3), <code><a href="/docs/linux/man/3-xkbcopykeytypes/">XkbCopyKeyTypes</a></code>(3), <code><a href="/docs/linux/man/3-xkbgetkeyactions/">XkbGetKeyActions</a></code>(3), <code><a href="/docs/linux/man/3-xkbgetkeybehaviors/">XkbGetKeyBehaviors</a></code>(3), <code><a href="/docs/linux/man/3-xkbgetkeyexplicitcomponents/">XkbGetKeyExplicitComponents</a></code>(3), <code><a href="/docs/linux/man/3-xkbgetkeymodifiermap/">XkbGetKeyModifierMap</a></code>(3), <code><a href="/docs/linux/man/3-xkbgetkeysyms/">XkbGetKeySyms</a></code>(3), <code><a href="/docs/linux/man/3-xkbgetkeytypes/">XkbGetKeyTypes</a></code>(3), <code><a href="/docs/linux/man/3-xkbresizekeyactions/">XkbResizeKeyActions</a></code>(3), <code><a href="/docs/linux/man/3-xkbresizekeysyms/">XkbResizeKeySyms</a></code>(3), <code><a href="/docs/linux/man/3-xkbresizekeytype/">XkbResizeKeyType</a></code>(3), <code><a href="/docs/linux/man/3-xkbgetvirtualmodmap/">XkbGetVirtualModMap</a></code>(3), <code><a href="/docs/linux/man/3-xkbgetvirtualmods/">XkbGetVirtualMods</a></code>(3)</p>
