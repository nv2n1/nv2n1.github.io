---
title: "xkbsetcompatmap(3)"
name: "xkbsetcompatmap"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbsetcompatmap/"
description: "XkbSetCompatMap – Modify the server’s compatibility map"
---

<p>XkbSetCompatMap &#8211; Modify the server&#8217;s compatibility map </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbSetCompatMap</code> <code>(Display *</code><i>display</i><code>,</code> <code>unsigned int </code><i>which</i><code>,</code> <code>XkbDescPtr </code><i>xkb</i><code>,</code> <code>Bool </code><i>update_actions</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; display</i></p>
<dd>
<dd>connection to server</p>
<dt><i>&#8211; which</i></p>
<dd>mask of compat map components to set</p>
<dt><i>&#8211; xkb</i></p>
<dd>source for compat map components</p>
<dt><i>&#8211; update_actions</i></p>
<dd>True =&gt; apply to server&#8217;s keyboard map</dl>
<h2>Description</h2>
<p>To modify the server&#8217;s compatibility map, first modify a local copy of the Xkb compatibility map, then call <i>XkbSetCompatMap. </i> You may allocate a new compatibility map for this purpose using <i>XkbAllocCompatMap. </i> You may also use a compatibility map from another server, although you need to adjust the <i>device_spec </i> field in the XkbDescRec accordingly. Note that symbol interpretations in a compatibility map ( <i>sym_interpret, </i> the vector of XkbSymInterpretRec structures) are also allocated using this same function. </p>
<p> <i>XkbSetCompatMap </i> copies compatibility map information from the keyboard description in <i>xkb </i> to the server specified in <i>display</i> <i>device_spec </i> field of <i>xkb. </i> Unless you have specifically modified this field, it is the default keyboard device. <i>which </i> specifies the compatibility map components to be set, and is an inclusive OR of the bits shown in Table 1. </p>
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
<p> After updating its compatibility map for the specified device, if <i>update_actions </i> is True, the server applies the new compatibility map to its entire keyboard for the device to generate a new set of key semantics, compatibility state, and a new core keyboard map. If <i>update_actions </i> is False, the new compatibility map is not used to generate any modifications to the current device semantics, state, or core keyboard map. One reason for not applying the compatibility map immediately would be if one server was being configured to match another on a piecemeal basis; the map should not be applied until everything is updated. To force an update at a later time, use <i>XkbSetCompatMap </i> specifying <i>which </i> as zero and <i>update_actions </i> as True. </p>
<p> <i>XkbSetCompatMap </i> returns True if successful and False if unsuccessful. The server may report problems it encounters when processing the request subsequently via protocol errors.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>True</p>
<dd>The <i>XkbSetCompatMap </i> function returns True if successful.</p>
<dt>False</p>
<dd>The <i>XkbSetCompatMap </i> function returns False if unsuccessful.</dl>
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
<p> The XkbSymInterpretRec structure specifies a symbol interpretation: </p>
<pre> typedef struct {
 KeySym sym; /* keysym of interest or NULL */
 unsigned char flags; /* XkbSI_AutoRepeat, XkbSI_LockingKey */
 unsigned char match; /* specifies how mods is interpreted */
 unsigned char mods; /* modifier bits, correspond to eight real modifiers */
 unsigned char virtual_mod; /* 1 modifier to add to key virtual mod map */
 XkbAnyAction act; /* action to bind to symbol position on key */
 } XkbSymInterpretRec,*XkbSymInterpretPtr;</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkballoccompatmap/">XkbAllocCompatMap</a></code>(3)</p>
