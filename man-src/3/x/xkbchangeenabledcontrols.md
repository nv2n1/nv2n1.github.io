---
title: "xkbchangeenabledcontrols(3)"
name: "xkbchangeenabledcontrols"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbchangeenabledcontrols/"
description: "XkbChangeEnabledControls – Manipulates the EnabledControls control"
---

<p>XkbChangeEnabledControls &#8211; Manipulates the EnabledControls control </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbChangeEnabledControls</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>unsigned int </code><i>device_spec</i><code>,</code> <code>unsigned int </code><i>mask</i><code>,</code> <code>unsigned int </code><i>values</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>
<dd>connection to X server</p>
<dt><i>&#8211; device_spec</i></p>
<dd>&nbsp;keyboard device to modify</p>
<dt><i>&#8211; mask</i></p>
<dd>1 bit -&gt; controls to enable / disable</p>
<dt><i>&#8211; values</i></p>
<dd>1 bit =&gt; enable, 0 bit =&gt; disable</dl>
<h2>Description</h2>
<p>The EnabledControls control is a bit mask where each bit that is turned on means the corresponding control is enabled, and when turned off, disabled. It corresponds to the <i>enabled_ctrls </i> field of an XkbControlsRec structure (see STRUCTURES). The bits describing which controls are turned on or off are defined in Table 1. </p>
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
<p> The <i>mask </i> parameter specifies the boolean controls to be enabled or disabled, and the <i>values </i> mask specifies the new state for those controls. Valid values for both of these masks are composed of a bitwise inclusive OR of bits taken from the set of mask bits in Table 1, using only those masks with &quot;ok&quot; in the <i>enabled_ctrls </i> column. </p>
<p> If the X server does not support a compatible version of Xkb or the Xkb extension has not been properly initialized, <i>XkbChangeEnabledControls </i> returns False; otherwise, it sends the request to the X server and returns True. </p>
<p> Note that the EnabledControls control only enables and disables controls; it does not configure them. Some controls, such as the AudibleBell control, have no configuration attributes and are therefore manipulated solely by enabling and disabling them. Others, however, have additional attributes to configure their behavior. For example, the RepeatControl control uses <i>repeat_delay </i> and <i>repeat_interval </i> fields to describe the timing behavior of keys that repeat. The RepeatControl behavior is turned on or off depending on the value of the XkbRepeatKeysMask bit, but you must use other means, as described in this chapter, to configure its behavior in detail.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>True</p>
<dd>The X server supports a compatible version of Xkb.</p>
<dt>False</p>
<dd>The X server does not support a compatible version of Xkb or the Xkb extension has not been properly initialized.</dl>
<h2>Structures</h2>
<pre>The XkbControlsRec structure is defined as follows:
 #define XkbMaxLegalKeyCode 255
 #define XkbPerKeyBitArraySize ((XkbMaxLegalKeyCode+1)/8)
 
 
 typedef struct {
 unsigned char mk_dflt_btn; /* default button for keyboard driven mouse */
 unsigned char num_groups; /* number of keyboard groups */
 unsigned char groups_wrap; /* how to wrap out-of-bounds groups */
 XkbModsRec internal; /* defines server internal modifiers */
 XkbModsRec ignore_lock; /* modifiers to ignore when checking for grab */
 unsigned int enabled_ctrls; /* 1 bit =&gt; corresponding boolean control enabled */
 unsigned short repeat_delay; /* ms delay until first repeat */
 unsigned short repeat_interval; /* ms delay between repeats */
 unsigned short slow_keys_delay; /* ms minimum time key must be down to be ok */
 unsigned short debounce_delay; /* ms delay before key reactivated */
 unsigned short mk_delay; /* ms delay to second mouse motion event */
 unsigned short mk_interval; /* ms delay between repeat mouse events */
 unsigned short mk_time_to_max; /* # intervals until constant mouse move */
 unsigned short mk_max_speed; /* multiplier for maximum mouse speed */
 short mk_curve; /* determines mouse move curve type */
 unsigned short ax_options; /* 1 bit =&gt; Access X option enabled */
 unsigned short ax_timeout; /* seconds until Access X disabled */
 unsigned short axt_opts_mask; /* 1 bit =&gt; options to reset on Access X timeout */
 unsigned short axt_opts_values; /* 1 bit =&gt; turn option on, 0=&gt; off */
 unsigned int axt_ctrls_mask; /* which bits in enabled_ctrls to modify */
 unsigned int axt_ctrls_values; /* values for new bits in enabled_ctrls */
 unsigned char per_key_repeat[XkbPerKeyBitArraySize]; /* per key auto repeat */
 } XkbControlsRec, *XkbControlsPtr;</pre>
