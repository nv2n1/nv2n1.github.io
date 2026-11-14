---
title: "xkblockgroup(3)"
name: "xkblockgroup"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkblockgroup/"
description: "XkbLockGroup – Locks the keysym group"
---

<p>XkbLockGroup &#8211; Locks the keysym group </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbLockGroup</code> <code>(Display *</code><i>display</i><code>,</code> <code>unsigned int </code><i>device_spec</i><code>,</code> <code>unsigned int </code><i>group</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>
<dd>connection to the X server</p>
<dt><i>device_spec</i></p>
<dd>device ID, or XkbUseCoreKbd</p>
<dt><i>group</i></p>
<dd>index of the keysym group to lock</dl>
<h2>Description</h2>
<p><i>XkbLockGroup </i> sends a request to the server to lock the specified <i>group </i> and does not wait for a reply. It returns True if the request was sent and False otherwise. </p>
<p> Reference the keysym group indices with these symbolic constants: </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=2>Table 1 Symbolic Group Names
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Symbolic Name</td>
<td>Value
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XkbGroup1Index</td>
<td>0
</td>
</tr>
<tr VALIGN=top>
<td>XkbGroup2Index</td>
<td>1
</td>
</tr>
<tr VALIGN=top>
<td>XkbGroup3Index</td>
<td>2
</td>
</tr>
<tr VALIGN=top>
<td>XkbGroup4Index</td>
<td>3
</td>
</tr>
</table>
<h2>Return Values</h2>
<dl COMPACT>
<dt>True</p>
<dd>The <i>XkbLockGroup</i> function returns True when a request was sent to the server to lock the specified <i>group</i> and does not wait for a reply.</p>
<dt>False</p>
<dd>The <i>XkbLockGroup</i> function returns False if the request was not sent. </p>
</dl>
