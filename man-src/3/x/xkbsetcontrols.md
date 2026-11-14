---
title: "xkbsetcontrols(3)"
name: "xkbsetcontrols"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbsetcontrols/"
description: "XkbSetControls – Copies changes to the X server based on a modified ctrls structure in a local copy of the keyboard description"
---

<p>XkbSetControls &#8211; Copies changes to the X server based on a modified ctrls structure in a local copy of the keyboard description </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbSetControls</code> <code>(Display *</code><i>display</i><code>,</code> <code>unsigned long </code><i>which</i><code>,</code> <code>XkbDescPtr </code><i>xkb</i><code>);</code><br />
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
<p>For each bit that is set in the <i>which </i> parameter, <i>XkbSetControls </i> sends the corresponding values from the <i>xkb-&gt;ctrls </i> field to the server. Valid values for <i>which </i> are any combination of the masks listed in Table 1 that have &quot;ok&quot; in the <i>which </i> column. </p>
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
<p> If <i>xkb-&gt;ctrls </i> is NULL, the server does not support a compatible version of Xkb, or the Xkb extension has not been properly initialized, <i>XkbSetControls </i> returns False. Otherwise, it sends the request to the X server and returns True. </p>
<p> Note that changes to attributes of controls in the XkbControlsRec structure are apparent only when the associated control is enabled, although the corresponding values are still updated in the X server. For example, the <i>repeat_delay </i> and <i>repeat_interval </i> fields are ignored unless the RepeatKeys control is enabled (that is, the X server&#8217;s equivalent of <i>xkb-&gt;ctrls </i> has XkbRepeatKeyMask set in <i>enabled_ctrls). </i> It is permissible to modify the attributes of a control in one call to <i>XkbSetControls </i> and enable the control in a subsequent call. See <i>XkbChangeEnabledControls </i> for more information on enabling and disabling controls. </p>
<p> Note that the <i>enabled_ctrls </i> field is itself a control &#8211; the EnabledControls control. As such, to set a specific configuration of enabled and disabled boolean controls, you must set <i>enabled_ctrls </i> to the appropriate bits to enable only the controls you want and disable all others, then specify the XkbControlsEnabledMask in a call to <i>XkbSetControls. </i> </p>
<p> Because this is somewhat awkward if all you want to do is enable and disable controls, and not modify any of their attributes, a convenience function is also provided for this purpose, <i>XkbChangeEnabledControls.</i></p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>True</p>
<dd>The <i>XkbSetControls </i> function returns True when it sends the request to the X server.</p>
<dt>False</p>
<dd>The <i>XkbSetControls </i> function returns False when <i>xkb-&gt;ctrls </i> is NULL, the server does not support a compatible version of Xkb, or the Xkb extension has not been properly initialized.</dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage</p>
<dt><code>BadMatch</code></p>
<dd>A compatible version of Xkb was not available in the server or an argument has correct type and range, but is otherwise invalid</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbchangeenabledcontrols/">XkbChangeEnabledControls</a></code>(3), <code><a href="/docs/linux/man/3-xkbfreecontrols/">XkbFreeControls</a></code>(3)</p>
