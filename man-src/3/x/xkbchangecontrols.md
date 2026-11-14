---
title: "xkbchangecontrols(3)"
name: "xkbchangecontrols"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbchangecontrols/"
description: "XkbChangeControls – Provides a flexible method for updating the controls in a server to match those in the changed keyboard description"
---

<p>XkbChangeControls &#8211; Provides a flexible method for updating the controls in a server to match those in the changed keyboard description </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbChangeControls</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>XkbDescPtr </code><i>xkb</i><code>,</code> <code>XkbControlsChangesPtr </code><i>changes</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>
<dd>connection to X server</p>
<dt><i>&#8211; xkb</i></p>
<dd>keyboard description with changed xkb-&gt;ctrls</p>
<dt><i>&#8211; changes</i></p>
<dd>which parts of xkb-&gt;ctrls have changed</dl>
<h2>Description</h2>
<p>The XkbControlsChangesRec structure allows applications to track modifications to an XkbControlsRec structure and thereby reduce the amount of traffic sent to the server. The same XkbControlsChangesRec structure may be used in several successive modifications to the same XkbControlsRec structure, then subsequently used to cause all of the changes, and only the changes, to be propagated to the server. </p>
<p> The <i>changed_ctrls </i> field is a mask specifying which logical sets of data in the controls structure have been modified. In this context, modified means <i>set, </i> that is, if a value is set to the same value it previously contained, it has still been modified, and is noted as changed. Valid values for <i>changed_ctrls </i> are any combination of the masks listed in Table 1 that have &quot;ok&quot; in the <i>changed_ctrls </i> column. Setting a bit implies the corresponding data fields from the &quot;Relevant XkbControlsRec Data Fields&quot; column in Table 1 have been modified. The <i>enabled_ctrls_changes </i> field specifies which bits in the <i>enabled_ctrls </i> field have changed. If the number of keyboard groups has changed, the <i>num_groups_changed </i> field is set to True. </p>
<p> Table 1 shows the actual values for the individual mask bits used to select controls for modification and to enable and disable the control. Note that the same mask bit is used to specify general modifications to the parameters used to configure the control (which), and to enable and disable the control (enabled_ctrls). The anomalies in the table (no &quot;ok&quot; in column) are for controls that have no configurable attributes; and for controls that are not boolean controls and therefore cannot be enabled or disabled. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5>Table 1 Xkb Controls
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Control</td>
<td>Control</td>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Selection</td>
<td>Relevant</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>Mask (which</td>
<td>XkbControlsRec</td>
<td>Boolean Control</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>parameter)</td>
<td>DataFields</td>
<td>enabled_ctrls bit</td>
<td>Section
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> AccessXFeedback </td>
<td> XkbAccessXFeedbackMask </td>
<td> ax_options:<br />
&nbsp;<wbr>&nbsp;XkbAX_*FBMask </td>
<td> XkbAccessXFeedbackMask </td>
<td>10.6.3
</td>
</tr>
<tr VALIGN=top>
<td> AccessXKeys </td>
<td></td>
<td></td>
<td> XkbAccessXKeysMask </td>
<td>10.6.1
</td>
</tr>
<tr VALIGN=top>
<td> AccessXTimeout </td>
<td> XkbAccessXTimeoutMask </td>
<td> ax_timeout axt_opts_mask axt_opts_values axt_ctrls_mask axt_ctrls_values </td>
<td> XkbAccessXTimeoutMask </td>
<td>10.6.2
</td>
</tr>
<tr VALIGN=top>
<td> AudibleBell </td>
<td></td>
<td></td>
<td> XkbAudibleBellMask </td>
<td>9.2
</td>
</tr>
<tr VALIGN=top>
<td> AutoReset </td>
<td></td>
<td></td>
<td></td>
<td>10.1.2
</td>
</tr>
<tr VALIGN=top>
<td> BounceKeys </td>
<td> XkbBounceKeysMask </td>
<td>debounce_delay</td>
<td> XkbBounceKeysMask </td>
<td>10.6.7
</td>
</tr>
<tr VALIGN=top>
<td> Detectable- </td>
<td></td>
<td></td>
<td></td>
<td>10.3.3
</td>
</tr>
<tr VALIGN=top>
<td> Autorepeat </td>
<td></td>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td> EnabledControls </td>
<td> XkbControlsEnabledMask </td>
<td>enabled_ctrls</td>
<td> Non-Boolean Control </td>
<td>10.1.1
</td>
</tr>
<tr VALIGN=top>
<td> GroupsWrap </td>
<td> XkbGroupsWrapMask </td>
<td>groups_wrap</td>
<td> Non-Boolean Control </td>
<td>10.7.1
</td>
</tr>
<tr VALIGN=top>
<td> IgnoreGroupLock </td>
<td></td>
<td></td>
<td> XkbIgnoreGroupLockMask </td>
<td>10.7.3
</td>
</tr>
<tr VALIGN=top>
<td> IgnoreLockMods </td>
<td> XkbIgnoreLockModsMask </td>
<td>ignore_lock</td>
<td> Non-Boolean Control </td>
<td>5.1
</td>
</tr>
<tr VALIGN=top>
<td> InternalMods </td>
<td> XkbInternalModsMask </td>
<td>internal</td>
<td> Non-Boolean Control </td>
<td>5.1
</td>
</tr>
<tr VALIGN=top>
<td> MouseKeys </td>
<td> XkbMouseKeysMask </td>
<td>mk_dflt_btn</td>
<td> XkbMouseKeysMask </td>
<td>10.5.1
</td>
</tr>
<tr VALIGN=top>
<td> MouseKeysAccel </td>
<td> XkbMouseKeysAccelMask </td>
<td> mk_delay mk_interval mk_time_to_max mk_max_speed mk_curve </td>
<td> XkbMouseKeysAccelMask </td>
<td>10.5.2
</td>
</tr>
<tr VALIGN=top>
<td> Overlay1 </td>
<td></td>
<td></td>
<td> XkbOverlay1Mask </td>
<td>10.4
</td>
</tr>
<tr VALIGN=top>
<td> Overlay2 </td>
<td></td>
<td></td>
<td> XkbOverlay2Mask </td>
<td>10.4
</td>
</tr>
<tr VALIGN=top>
<td> PerKeyRepeat </td>
<td> XkbPerKeyRepeatMask </td>
<td>per_key_repeat</td>
<td> Non-Boolean Control </td>
<td>10.3.1
</td>
</tr>
<tr VALIGN=top>
<td> RepeatKeys </td>
<td> XkbRepeatKeysMask </td>
<td>repeat_delay</td>
<td> XkbRepeatKeysMask </td>
<td>10.3
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td></td>
<td>repeat_interval</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td> SlowKeys </td>
<td> XkbSlowKeysMask </td>
<td>slow_keys_delay</td>
<td> XkbSlowKeysMask </td>
<td>10.6.6
</td>
</tr>
<tr VALIGN=top>
<td> StickyKeys </td>
<td> XkbStickyKeysMask </td>
<td> ax_options:<br />
&nbsp;<wbr>&nbsp;XkbAX_TwoKeysMask<br />
&nbsp;<wbr>&nbsp;XkbAX_LatchToLockMask </td>
<td> XkbStickyKeysMask </td>
<td>10.6.8
</td>
</tr>
</table>
<p> Table 2 shows the actual values for the individual mask bits used to select controls for modification and to enable and disable the control. Note that the same mask bit is used to specify general modifications to the parameters used to configure the control (which), and to enable and disable the control (enabled_ctrls). The anomalies in the table (no &quot;ok&quot; in column) are for controls that have no configurable attributes; and for controls that are not boolean controls and therefore cannot be enabled or disabled. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=4>Table 2 Controls Mask Bits
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
<td></td>
<td>Value
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>changed</td>
<td>enabled</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>_ctrls</td>
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
<p> If you have an Xkb description with controls that have been modified and an XkbControlsChangesRec that describes the changes that have been made, the <i>XkbChangeControls </i> function provides a flexible method for updating the controls in a server to match those in the changed keyboard description. </p>
<p> <i>XkbChangeControls </i> copies any controls fields specified by <i>changes </i> from the keyboard description controls structure, <i>xkb-&gt;ctrls, </i> to the server specified by <i>dpy.</i></p>
<h2>Structures</h2>
<p>The XkbControlsChangesRec structure is defined as follows: </p>
<pre>typedef struct _XkbControlsChanges {
 unsigned int changed_ctrls; /* bits indicating changed control data 
*/
 unsigned int enabled_ctrls_changes; /* bits indicating enabled/disabled 
controls */
 Bool num_groups_changed; /* True if number of keyboard groups 
changed */
} XkbControlsChangesRec,*XkbControlsChangesPtr;</pre>
