---
title: "xkbsetptractionx(3)"
name: "xkbsetptractionx"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbsetptractionx/"
description: "XkbSetPtrActionX – Sets the high_XXX and low_XXX fields of act from the signed integer value x"
---

<p>XkbSetPtrActionX &#8211; Sets the high_XXX and low_XXX fields of act from the signed integer value x </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>void XkbSetPtrActionX</code> <code>(XkbPtrAction </code><i>act</i><code>,</code> <code>int </code><i>x</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; act</i></p>
<dd>
<dd>action in which to set X</p>
<dt><i>&#8211; x</i></p>
<dd>new value to set</dl>
<h2>Description</h2>
<p>Actions associated with the XkbPtrAction structure move the pointer when keys are pressed and released. </p>
<p> If the MouseKeys control is not enabled, KeyPress and KeyRelease events are treated as though the action is XkbSA_NoAction. </p>
<p> If the MouseKeys control is enabled, a server action of type XkbSA_MovePtr instructs the server to generate core pointer MotionNotify events rather than the usual KeyPress event, and the corresponding KeyRelease event disables any mouse keys timers that were created as a result of handling the XkbSA_MovePtr action. </p>
<p> The <i>type </i> field of the XkbPtrAction structure is always XkbSA_MovePtr. </p>
<p> The <i>flags </i> field is a bitwise inclusive OR of the masks shown in Table 1. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=2>Table 1 Pointer Action Types
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Action Type</td>
<td>Meaning
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XkbSA_NoAcceleration</td>
<td> If not set, and the MouseKeysAccel control is enabled, the KeyPress initiates a mouse keys timer for this key; every time the timer expires, the cursor moves.
</td>
</tr>
<tr VALIGN=top>
<td>XkbSA_MoveAbsoluteX</td>
<td> If set, the X portion of the structure specifies the new pointer X coordinate. Otherwise, the X portion is added to the current pointer X coordinate to determine the new pointer X coordinate.
</td>
</tr>
<tr VALIGN=top>
<td>XkbSA_MoveAbsoluteY</td>
<td> If set, the Y portion of the structure specifies the new pointer Y coordinate. Otherwise, the Y portion is added to the current pointer Y coordinate to determine the new pointer Y coordinate.
</td>
</tr>
</table>
<p> Each of the X and Y coordinates of the XkbPtrAction structure is composed of two signed 16-bit values, that is, the X coordinate is composed of <i>high_XXX </i> and <i>low_XXX, </i> and similarly for the Y coordinate. Xkb provides the following macros, to convert between a signed integer and two signed 16-bit values in XkbPtrAction structures.</p>
<h2>Structures</h2>
<pre> typedef struct _XkbPtrAction {
 unsigned char type; /* XkbSA_MovePtr */
 unsigned char flags; /* determines type of pointer motion */
 unsigned char high_XXX; /* x coordinate, high bits*/
 unsigned char low_XXX; /* y coordinate, low bits */
 unsigned char high_YYY; /* x coordinate, high bits */
 unsigned char low_YYY; /* y coordinate, low bits */
 } XkbPtrAction;</pre>
