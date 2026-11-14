---
title: "xkbsasetscreen(3)"
name: "xkbsasetscreen"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbsasetscreen/"
description: "XkbSASetScreen – Sets the screenXXX field of act from s"
---

<p>XkbSASetScreen &#8211; Sets the screenXXX field of act from s </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>void XkbSASetScreen</code> <code>(XkbSwitchScreenAction </code><i>act</i><code>,</code> <code>int </code><i>s</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; act</i></p>
<dd>
<dd>action in which to set screenXXX</p>
<dt><i>&#8211; s</i></p>
<dd>value to set in screenXXX</dl>
<h2>Description</h2>
<p>Actions associated with the XkbSwitchScreen action structure change the active screen on a multiscreen display. </p>
<p> The <i>type </i> field of the XkbSwitchScreenAction structure should always be XkbSA_SwitchScreen. </p>
<p> The <i>flags </i> field is composed of the bitwise inclusive OR of the masks shown in Table 1. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=2>Table 1 Switch Screen Action Flags
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Flag</td>
<td>Meaning
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XkbSA_SwitchAbsolute</td>
<td> If set, the screenXXX field represents the index of the new screen. Otherwise, it represents an offset from the current screen to the new screen.
</td>
</tr>
<tr VALIGN=top>
<td>XkbSA_SwitchApplication</td>
<td> If not set, the action should switch to another screen on the same server. Otherwise, it should switch to another X server or application that shares the same physical display.
</td>
</tr>
</table>
<p> The <i>screenXXX </i> field is a signed character value that represents either the relative or absolute screen index, depending on the state of the XkbSA_SwitchAbsolute bit in the <i>flags </i> field. Xkb provides the following macros to convert between the integer and signed character value for screen numbers in XkbSwitchScreenAction structures.</p>
<h2>Structures</h2>
<pre> typedef struct _XkbSwitchScreenAction {
 unsigned char type; /* XkbSA_SwitchScreen */
 unsigned char flags; /* controls screen switching */
 char screenXXX; /* screen number or delta */
 } XkbSwitchScreenAction;</pre>
<h2>Notes</h2>
<p>This action is optional. Servers are free to ignore the action or any of its flags if they do not support the requested behavior. If the action is ignored, it behaves like XkbSA_NoAction. Otherwise, key press and key release events do not generate an event.</p>
