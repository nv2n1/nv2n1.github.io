---
title: "xkblockmodifiers(3)"
name: "xkblockmodifiers"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkblockmodifiers/"
description: "XkbLockModifiers – Locks and unlocks any of the eight real keyboard modifiers"
---

<p>XkbLockModifiers &#8211; Locks and unlocks any of the eight real keyboard modifiers </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbLockModifiers</code> <code>(Display *</code><i>display</i><code>,</code> <code>unsigned int </code><i>device_spec</i><code>,</code> <code>unsigned int </code><i>affect</i><code>,</code> <code>unsigned int </code><i>values</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>
<dd>connection to the X server</p>
<dt><i>device_spec</i></p>
<dd>device ID, or XkbUseCoreKbd</p>
<dt><i>affect</i></p>
<dd>mask of real modifiers whose lock state is to change</p>
<dt><i>values</i></p>
<dd>1 =&gt; lock, 0 =&gt; unlock; only for modifiers selected by affect</dl>
<h2>Description</h2>
<p><i>XkbLockModifiers </i> sends a request to the server to lock the real modifiers selected by both <i>affect </i> and <i>values</i> and to unlock the real modifiers selected by <i>affect, </i> but not selected by <i>values. XkbLockModifiers </i> does not wait for a reply from the server. It returns True if the request was sent, and False otherwise. </p>
<p> The functions in this section that change the use of modifiers use a mask in the parameter affect. It is a bitwise inclusive OR of the legal modifier masks: </p>
<table>
<tr VALIGN=top>
<td ALIGN=center>Table 1 Real Modifier Masks
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Mask
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>ShiftMask
</td>
</tr>
<tr VALIGN=top>
<td>LockMask
</td>
</tr>
<tr VALIGN=top>
<td>ControlMask
</td>
</tr>
<tr VALIGN=top>
<td>Mod1Mask
</td>
</tr>
<tr VALIGN=top>
<td>Mod2Mask
</td>
</tr>
<tr VALIGN=top>
<td>Mod3Mask
</td>
</tr>
<tr VALIGN=top>
<td>Mod4Mask
</td>
</tr>
<tr VALIGN=top>
<td>Mod5Mask
</td>
</tr>
</table>
<h2>Return Values</h2>
<dl COMPACT>
<dt>True</p>
<dd>The <i>XkbLockModifiers </i> function returns True if a request is sent to the server to lock the real modifiers selected by both <i>affect </i> and <i>values</i> and to unlock the real modifiers selected by <i>affect, </i> but not selected by <i>values.</i></p>
<dt>False</p>
<dd>The <i>XkbLockModifiers </i> function returns False if the request was not sent. </p>
</dl>
