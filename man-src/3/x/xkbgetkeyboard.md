---
title: "xkbgetkeyboard(3)"
name: "xkbgetkeyboard"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbgetkeyboard/"
description: "XkbGetKeyboard – Retrieves one or more components of a keyboard device description"
---

<p>XkbGetKeyboard &#8211; Retrieves one or more components of a keyboard device description </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>XkbDescPtr XkbGetKeyboard</code> <code>(Display *</code><i>display</i><code>,</code> <code>unsigned int </code><i>which</i><code>,</code> <code>unsigned int </code><i>device_spec</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>
<dd>connection to the X server</p>
<dt><i>device_spec</i></p>
<dd>device ID, or XkbUseCoreKbd</p>
<dt><i>bits_to_change</i></p>
<dd>determines events to be selected / deselected</p>
<dt><i>values_for_bits</i></p>
<dd>1=&gt;select, 0-&gt;deselect; for events in bits_to_change</dl>
<h2>Description</h2>
<p><i>XkbGetKeyboard </i> allocates and returns a pointer to a keyboard description. It queries the server for those components specified in the <i>which </i> parameter for device <i>device_spec </i> and copies the results to the XkbDescRec it allocated. The remaining fields in the keyboard description are set to NULL. The valid masks for <i>which </i> are those listed in Table 1. </p>
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
<td>(1L&lt;&lt;7)
</td>
</tr>
</table>
<p> <i>XkbGetKeyboard </i> is used to read the current description for one or more components of a keyboard device. It calls <i>XkbGetKeyboardByName </i> as follows: </p>
<p> <i>XkbGetKeyboardByName(dpy, device_spec, </i> NULL, <i>which, which, </i> False).</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><font SIZE="-1">BadAlloc</font></p>
<dd>Unable to allocate storage </p>
</dl>
