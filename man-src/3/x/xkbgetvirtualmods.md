---
title: "xkbgetvirtualmods(3)"
name: "xkbgetvirtualmods"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbgetvirtualmods/"
description: "XkbGetVirtualMods – Obtain a subset of the virtual modifier bindings (the vmods array) in a keyboard description"
---

<p>XkbGetVirtualMods &#8211; Obtain a subset of the virtual modifier bindings (the vmods array) in a keyboard description </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbGetVirtualMods</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>unsigned int </code><i>which</i><code>,</code> <code>XkbDescPtr </code><i>xkb</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>
<dd>connection to server</p>
<dt><i>&#8211; which</i></p>
<dd>mask indicating virtual modifier bindings to get</p>
<dt><i>&#8211; xkb</i></p>
<dd>Xkb description where results will be placed</dl>
<h2>Description</h2>
<p><i>XkbGetVirtualMods </i> sends a request to the server to obtain the <i>vmods </i> entries for the virtual modifiers specified in the mask, <i>which, </i> and waits for a reply. </p>
<p> Virtual modifiers are named by converting their string name to an X Atom and storing the Atom in the <i>names.vmods </i> array in an XkbDescRec structure. The position of a name Atom in the <i>names.vmods </i> array defines the bit position used to represent the virtual modifier and also the index used when accessing virtual modifier information in arrays: the name in the i-th (0 relative) entry of <i>names.vmods </i> is the i-th virtual modifier, represented by the mask (1&lt;&lt;i). Throughout Xkb, various functions have a parameter that is a mask representing virtual modifier choices. In each case, the i-th bit (0 relative) of the mask represents the i-th virtual modifier. </p>
<p> To set the name of a virtual modifier, use <i>XkbSetNames, </i> using XkbVirtualModNamesMask in <i>which </i> and the name in the <i>xkb </i> argument; to retrieve indicator names, use <i>XkbGetNames.</i> </p>
<p> For each bit set in <i>which, XkbGetVirtualMods </i> updates the corresponding virtual modifier definition in the <i>server-&gt;vmods </i> array of <i>xkb. </i> The <i>xkb </i> parameter must be a pointer to a valid Xkb keyboard description. If successful, <i>XkbGetVirtualMods </i> returns Success. </p>
<p> <code>Virtual Modifier Names and Masks</code> </p>
<p> Virtual modifiers are named by converting their string name to an X Atom and storing the Atom in the <i>names.vmods </i> array in an XkbDescRec structure. The position of a name Atom in the <i>names.vmods </i> array defines the bit position used to represent the virtual modifier and also the index used when accessing virtual modifier information in arrays: the name in the i-th (0 relative) entry of <i>names.vmods </i> is the i-th virtual modifier, represented by the mask (1&lt;&lt;i). Throughout Xkb, various functions have a parameter that is a mask representing virtual modifier choices. In each case, the i-th bit (0 relative) of the mask represents the i-th virtual modifier. </p>
<p> To set the name of a virtual modifier, use <i>XkbSetNames, </i> using XkbVirtualModNamesMask in <i>which </i> and the name in the <i>xkb </i> argument; to retrieve indicator names, use <i>XkbGetNames.</i> </p>
<p> If the <i>server </i> map has not been allocated in the <i>xkb </i> parameter, <i>XkbGetVirtualMods </i> allocates and initializes it before obtaining the virtual modifier bindings. </p>
<p> If the server does not have a compatible version of Xkb, or the Xkb extension has not been properly initialized, <i>XkbGetVirtualMods </i> returns BadMatch. Any errors in allocation cause <i>XkbGetVirtualMods </i> to return BadAlloc.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>Success</p>
<dd>The <i>XkbGetVirtualMods </i> function returns Success when it successfully updates the corresponding virtual modifier definition in the <i>server-&gt;vmods </i> array of <i>xkb. </i></dl>
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
<p>The <i>display </i> field points to an X display structure. The <i>flags </i> field is private to the library: modifying <i>flags </i> may yield unpredictable results. The <i>device_spec </i> field specifies the device identifier of the keyboard input device, or XkbUseCoreKeyboard, which specifies the core keyboard device. The <i>min_key_code</i> and <i>max_key_code </i> fields specify the least and greatest keycode that can be returned by the keyboard. </p>
<p> Each structure component has a corresponding mask bit that is used in function calls to indicate that the structure should be manipulated in some manner, such as allocating it or freeing it. These masks and their relationships to the fields in the XkbDescRec are shown in Table 1. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3>Table 1 Mask Bits for XkbDescRec
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
<dt><code>BadMatch</code></p>
<dd>A compatible version of Xkb was not available in the server or an argument has correct type and range, but is otherwise invalid</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbgetnames/">XkbGetNames</a></code>(3), <code><a href="/docs/linux/man/3-xkbsetnames/">XkbSetNames</a></code>(3)</p>
