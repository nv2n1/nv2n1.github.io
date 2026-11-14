---
title: "xkbgetcontrols(3)"
name: "xkbgetcontrols"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbgetcontrols/"
description: "XkbGetControls – Finds the current state of Xkb server controls"
---

<p>XkbGetControls &#8211; Finds the current state of Xkb server controls </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbGetControls</code> <code>(Display *</code><i>display</i><code>,</code> <code>unsigned long </code><i>which</i><code>,</code> <code>XkbDescPtr </code><i>xkb</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; display</i></p>
<dd>
<dd>connection to X server</p>
<dt><i>&#8211; which</i></p>
<dd>mask of controls requested</p>
<dt><i>&#8211; xkb</i></p>
<dd>keyboard description for controls information</dl>
<h2>Description</h2>
<p><i>XkbGetControls </i> queries the server for the requested control information, waits for a reply, and then copies the server&#8217;s values for the requested information into the <i>ctrls </i> structure of the <i>xkb </i> argument. Only those components specified by the <i>which </i> parameter are copied. Valid values for <i>which </i> are any combination of the masks listed in Table 1 that have &quot;ok&quot; in the <i>which </i> column. </p>
<p> Table 1 shows the actual values for the individual mask bits used to select controls for modification and to enable and disable the control. Note that the same mask bit is used to specify general modifications to the parameters used to configure the control (which), and to enable and disable the control (enabled_ctrls). The anomalies in Table 1 (no &quot;ok&quot; in column) are for controls that have no configurable attributes; and for controls that are not boolean controls and therefore cannot be enabled or disabled. </p>
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
<p> If <i>xkb-&gt;ctrls </i> is NULL, <i>XkbGetControls </i> allocates and initializes it before obtaining the values specified by <i>which. </i> If <i>xkb-&gt;ctrls </i> is not NULL, <i>XkbGetControls </i> modifies only those portions of <i>xkb-&gt;ctrls </i> corresponding to the values specified by <i>which.</i> </p>
<p> <i>XkbGetControls </i> returns Success if successful; otherwise, it returns BadAlloc if it cannot obtain sufficient storage, BadMatch if <i>xkb </i> is NULL or <i>which </i> is empty, or BadImplementation. </p>
<p> To free the <i>ctrls </i> member of a keyboard description, use <i>XkbFreeControls.</i> </p>
<p> The <i>num_groups </i> field in the <i>ctrls </i> structure is always filled in by <i>XkbGetControls, </i> regardless of which bits are selected by <i>which.</i></p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>Success</p>
<dd>The <i>XkbGetControls </i> function returns Success if successful.</dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage</p>
<dt><code>BadImplementation</code></p>
<dd>Invalid reply from server</p>
<dt><code>BadMatch</code></p>
<dd>A compatible version of Xkb was not available in the server or an argument has correct type and range, but is otherwise invalid </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbfreecontrols/">XkbFreeControls</a></code>(3)</p>
