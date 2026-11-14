---
title: "xkbsetignorelockmods(3)"
name: "xkbsetignorelockmods"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbsetignorelockmods/"
description: "XkbSetIgnoreLockMods – Sets the modifiers that, if locked, are not to be reported in matching events to passive grabs"
---

<p>XkbSetIgnoreLockMods &#8211; Sets the modifiers that, if locked, are not to be reported in matching events to passive grabs </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbSetIgnoreLockMods</code> <code>(Display *</code><i>display</i><code>,</code> <code>unsigned int </code><i>device_spec</i><code>,</code> <code>unsigned int </code><i>affect_real</i><code>,</code> <code>unsigned int </code><i>real_values</i><code>,</code> <code>unsigned int </code><i>affect_virtual</i><code>,</code> <code>unsigned int </code><i>virtual_values</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; display</i></p>
<dd>
<dd>connection to the X server</p>
<dt><i>&#8211; device_spec</i></p>
<dd>device ID, or XkbUseCoreKbd</p>
<dt><i>&#8211; affect_real</i></p>
<dd>mask of real modifiers affected by this call</p>
<dt><i>&#8211; real_values</i></p>
<dd>values for affected real modifiers (1=&gt;set, 0=&gt;unset)</p>
<dt><i>&#8211; affect_virtual</i></p>
<dd>mask of virtual modifiers affected by this call</p>
<dt><i>&#8211; virtual_values</i></p>
<dd>values for affected virtual modifiers (1=&gt;set, 0=&gt;unset)</dl>
<h2>Description</h2>
<p>The core protocol does not provide a way to exclude specific modifiers from grab calculations, with the result that locking modifiers sometimes have unanticipated side effects. </p>
<p> The IgnoreLockMods control specifies modifiers that should be excluded from grab calculations. These modifiers are also not reported in any core events except KeyPress and KeyRelease events that do not activate a passive grab and that do not occur while a grab is active. </p>
<p> Manipulate the IgnoreLockMods control via the <i>ignore_lock </i> field in the XkbControlsRec structure, then use <i>XkbSetControls </i> and <i>XkbGetControls </i> to query and change this control. Alternatively, use <i>XkbSetIgnoreLockMods.</i> </p>
<p> <i>XkbSetIgnoreLockMods </i> sends a request to the server to change the server&#8217;s IgnoreLockMods control. <i>affect_real </i> and <i>real_values </i> are masks of real modifier bits indicating which real modifiers are to be added and removed from the server&#8217;s IgnoreLockMods control. Modifiers selected by both <i>affect_real </i> and <i>real_values </i> are added to the server&#8217;s IgnoreLockMods control; those selected by <i>affect_real </i> but not by <i>real_values </i> are removed from the server&#8217;s IgnoreLockMods control. Valid values for <i>affect_real </i> and <i>real_values </i> consist of any combination of the eight core modifier bits: ShiftMask, LockMask, ControlMask, Mod1Mask &#8211; Mod5Mask. <i>affect_virtual </i> and <i>virtual_values </i> are masks of virtual modifier bits indicating which virtual modifiers are to be added and removed from the server&#8217;s IgnoreLockMods control. Modifiers selected by both <i>affect_virtual </i> and <i>virtual_values </i> are added to the server&#8217;s IgnoreLockMods control; those selected by <i>affect_virtual </i> but not by <i>virtual_values </i> are removed from the server&#8217;s IgnoreLockMods control. See below for a discussion of virtual modifier masks to use in <i>affect_virtual </i> and <i>virtual_values. XkbSetIgnoreLockMods </i> does not wait for a reply from the server. It returns True if the request was sent, and False otherwise. </p>
<p> Virtual modifiers are named by converting their string name to an X Atom and storing the Atom in the <i>names.vmods </i> array in an XkbDescRec structure. The position of a name Atom in the <i>names.vmods </i> array defines the bit position used to represent the virtual modifier and also the index used when accessing virtual modifier information in arrays: the name in the i-th (0 relative) entry of <i>names.vmods </i> is the i-th virtual modifier, represented by the mask (1&lt;&lt;i). Throughout Xkb, various functions have a parameter that is a mask representing virtual modifier choices. In each case, the i-th bit (0 relative) of the mask represents the i-th virtual modifier. </p>
<p> To set the name of a virtual modifier, use <i>XkbSetNames, </i> using XkbVirtualModNamesMask in <i>which </i> and the name in the <i>xkb </i> argument; to retrieve indicator names, use <i>XkbGetNames.</i></p>
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
<p>The display field points to an X display structure. The flags field is private to the library: modifying flags may yield unpredictable results. The device_spec field specifies the device identifier of the keyboard input device, or XkbUseCoreKeyboard, which specifies the core keyboard device. The min_key_code and max_key_code fields specify the least and greatest keycode that can be returned by the keyboard.<br />
&nbsp; Each structure component has a corresponding mask bit that is used in function calls to indicate that the structure should be manipulated in some manner, such as allocating it or freeing it. These masks and their relationships to the fields in the XkbDescRec are shown in Table 1. </p>
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
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbgetcontrols/">XkbGetControls</a></code>(3), <code><a href="/docs/linux/man/3-xkbgetnames/">XkbGetNames</a></code>(3), <code><a href="/docs/linux/man/3-xkbsetcontrols/">XkbSetControls</a></code>(3), <code><a href="/docs/linux/man/3-xkbsetnames/">XkbSetNames</a></code>(3)</p>
