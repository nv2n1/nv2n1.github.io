---
title: "xkbfreeservermap(3)"
name: "xkbfreeservermap"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbfreeservermap/"
description: "XkbFreeServerMap – Free memory used by the server member of an XkbDescRec structure"
---

<p>XkbFreeServerMap &#8211; Free memory used by the server member of an XkbDescRec structure </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>void XkbFreeServerMap</code> <code>(XkbDescPtr </code><i>xkb</i><code>,</code> <code>unsigned int </code><i>which</i><code>,</code> <code>Bool </code><i>free_all</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; xkb</i></p>
<dd>
<dd>keyboard description containing server map to free</p>
<dt><i>&#8211; which</i></p>
<dd>mask identifying components of map to free</p>
<dt><i>&#8211; free_all</i></p>
<dd>True =&gt; free all server map components and server itself</dl>
<h2>Description</h2>
<p>The <i>XkbFreeServerMap </i> function frees the specified components of server map in the XkbDescRec structure specified by the <i>xkb </i> parameter and sets the corresponding structure component values to NULL. The <i>which parameter specifies a combination of the server map masks and is a </i> bitwise inclusive OR of the masks listed in Table 1. If <i>free_all </i> is True, <i>which </i> is ignored and <i>XkbFreeServerMap </i> frees every non-NULL structure component in the server map, frees the XkbServerMapRec structure referenced by the <i>server </i> member of the <i>xkb </i> parameter, and sets the <i>server </i> member to NULL. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=2>Table 1 XkbAllocServerMap Masks
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
<td>XkbExplicitComponentsMask</td>
<td> The min_key_code and max_key_code fields of the xkb parameter are used to allocate the explicit field of the server map.
</td>
</tr>
<tr VALIGN=top>
<td>XkbKeyActionsMask</td>
<td> The min_key_code and max_key_code fields of the xkb parameter are used to allocate the key_acts field of the server map. The count_acts parameter is used to allocate the acts field of the server map.
</td>
</tr>
<tr VALIGN=top>
<td>XkbKeyBehaviorsMask</td>
<td> The min_key_code and max_key_code fields of the xkb parameter are used to allocate the behaviors field of the server map.
</td>
</tr>
<tr VALIGN=top>
<td>XkbVirtualModMapMask</td>
<td> The min_key_code and max_key_code fields of the xkb parameter are used to allocate the vmodmap field of the server map.
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>
</td>
</tr>
</table>
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
<p> The Xkb server map contains the information the server needs to interpret key events and is of type XkbServerMapRec: </p>
<pre>#define XkbNumVirtualMods 16
typedef struct { /* Server Map */
 unsigned short num_acts; /* # of occupied entries in acts */
 unsigned short size_acts; /* # of entries in acts */
 XkbAction * acts; /* linear 2d tables of key actions, 1 per keycode */
 XkbBehavior * behaviors; /* key behaviors,1 per keycode */
 unsigned short * key_acts; /* index into acts, 1 per keycode */
 unsigned char * explicit; /* explicit overrides of core remapping, 1 per key */
 unsigned char vmods[XkbNumVirtualMods]; /* real mods bound to virtual mods */
 unsigned short * vmodmap; /* virtual mods bound to key, 1 per keycode*/
} XkbServerMapRec, *XkbServerMapPtr;</pre>
