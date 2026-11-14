---
title: "xkballoccontrols(3)"
name: "xkballoccontrols"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkballoccontrols/"
description: "XkbAllocControls – Allocates an XkbControlsRec structure in the XkbDescRec"
---

<p>XkbAllocControls &#8211; Allocates an XkbControlsRec structure in the XkbDescRec </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbAllocControls</code> <code>(XkbDescPtr </code><i>xkb</i><code>,</code> <code>unsigned int </code><i>which</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; xkb</i></p>
<dd>
<dd>Xkb description in which to allocate ctrls rec</p>
<dt><i>&#8211; which</i></p>
<dd>mask of components of ctrls to allocate</dl>
<h2>Description</h2>
<p>The need to allocate an XkbControlsRec structure seldom arises; Xkb creates one when an application calls <i>XkbGetControls </i> or a related function. For those situations where there is not an XkbControlsRec structure allocated in the XkbDescRec, allocate one by calling <i>XkbAllocControls.</i> </p>
<p> <i>XkbAllocControls </i> allocates the <i>ctrls </i> field of the <i>xkb </i> parameter, initializes all fields to zero, and returns Success. If the <i>ctrls </i> field is not NULL, <i>XkbAllocControls </i> simply returns Success. If <i>xkb </i> is NULL, <i>XkbAllocControls </i> reports a BadMatch error. If the <i>ctrls </i> field could not be allocated, it reports a BadAlloc error. </p>
<p> The <i>which </i> mask specifies the individual fields of the <i>ctrls </i> structure to be allocated and can contain any of the valid masks defined in Table 1. (SHOULD THIS COMMENT BE LEFT IN????) Because none of the currently existing controls have any structures associated with them, which is currently of little practical value in this call. </p>
<p> Table 1 shows the actual values for the individual mask bits used to select controls for modification and to enable and disable the control. Note that the same mask bit is used to specify general modifications to the parameters used to configure the control (which), and to enable and disable the control (enabled_ctrls). The anomalies in the table (no &quot;ok&quot; in column) are for controls that have no configurable attributes; and for controls that are not boolean controls and therefore cannot be enabled or disabled. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=4>Table 1 Controls Mask Bits
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Mask Bit</td>
<td>which or</td>
<td>enabled</td>
<td>Value
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>changed_ctrls</td>
<td>_ctrls</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=4>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XkbRepeatKeysMask</td>
<td>ok</td>
<td>ok</td>
<td>(1L&lt;&lt;0)
</td>
</tr>
<tr VALIGN=top>
<td>XkbSlowKeysMask</td>
<td>ok</td>
<td>ok</td>
<td>(1L&lt;&lt;1)
</td>
</tr>
<tr VALIGN=top>
<td>XkbBounceKeysMask</td>
<td>ok</td>
<td>ok</td>
<td>(1L&lt;&lt;2)
</td>
</tr>
<tr VALIGN=top>
<td>XkbStickyKeysMask</td>
<td>ok</td>
<td>ok</td>
<td>(1L&lt;&lt;3)
</td>
</tr>
<tr VALIGN=top>
<td>XkbMouseKeysMask</td>
<td>ok</td>
<td>ok</td>
<td>(1L&lt;&lt;4)
</td>
</tr>
<tr VALIGN=top>
<td>XkbMouseKeysAccelMask</td>
<td>ok</td>
<td>ok</td>
<td>(1L&lt;&lt;5)
</td>
</tr>
<tr VALIGN=top>
<td>XkbAccessXKeysMask</td>
<td>ok</td>
<td>ok</td>
<td>(1L&lt;&lt;6)
</td>
</tr>
<tr VALIGN=top>
<td>XkbAccessXTimeoutMask</td>
<td>ok</td>
<td>ok</td>
<td>(1L&lt;&lt;7)
</td>
</tr>
<tr VALIGN=top>
<td>XkbAccessXFeedbackMask</td>
<td>ok</td>
<td>ok</td>
<td>(1L&lt;&lt;8)
</td>
</tr>
<tr VALIGN=top>
<td>XkbAudibleBellMask</td>
<td></td>
<td>ok</td>
<td>(1L&lt;&lt;9)
</td>
</tr>
<tr VALIGN=top>
<td>XkbOverlay1Mask</td>
<td></td>
<td>ok</td>
<td>(1L&lt;&lt;10)
</td>
</tr>
<tr VALIGN=top>
<td>XkbOverlay2Mask</td>
<td></td>
<td>ok</td>
<td>(1L&lt;&lt;11)
</td>
</tr>
<tr VALIGN=top>
<td>XkbIgnoreGroupLockMask</td>
<td></td>
<td>ok</td>
<td>(1L&lt;&lt;12)
</td>
</tr>
<tr VALIGN=top>
<td>XkbGroupsWrapMask</td>
<td>ok</td>
<td></td>
<td>(1L&lt;&lt;27)
</td>
</tr>
<tr VALIGN=top>
<td>XkbInternalModsMask</td>
<td>ok</td>
<td></td>
<td>(1L&lt;&lt;28)
</td>
</tr>
<tr VALIGN=top>
<td>XkbIgnoreLockModsMask</td>
<td>ok</td>
<td></td>
<td>(1L&lt;&lt;29)
</td>
</tr>
<tr VALIGN=top>
<td>XkbPerKeyRepeatMask</td>
<td>ok</td>
<td></td>
<td>(1L&lt;&lt;30)
</td>
</tr>
<tr VALIGN=top>
<td>XkbControlsEnabledMask</td>
<td>ok</td>
<td></td>
<td>(1L&lt;&lt;31)
</td>
</tr>
<tr VALIGN=top>
<td>XkbAccessXOptionsMask</td>
<td>ok</td>
<td>ok</td>
<td>(XkbStickyKeysMask |
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td></td>
<td>XkbAccessXFeedbackMask)
</td>
</tr>
<tr VALIGN=top>
<td>XkbAllBooleanCtrlsMask</td>
<td></td>
<td>ok</td>
<td>(0x00001FFF)
</td>
</tr>
<tr VALIGN=top>
<td>XkbAllControlsMask</td>
<td>ok</td>
<td></td>
<td>(0xF8001FFF)
</td>
</tr>
</table>
<h2>Return Values</h2>
<dl COMPACT>
<dt>SUCCESS</p>
<dd>allocates the ctrls field of the xkb parameter, initializes all fields to zero </p>
<p> the ctrls field is not NULL</dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage</p>
<dt><code>BadMatch</code></p>
<dd>A compatible version of Xkb was not available in the server or an argument has correct type and range, but is otherwise invalid</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbgetcontrols/">XkbGetControls</a></code>(3)</p>
