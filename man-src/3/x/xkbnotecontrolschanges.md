---
title: "xkbnotecontrolschanges(3)"
name: "xkbnotecontrolschanges"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbnotecontrolschanges/"
description: "XkbNoteControlsChanges – Notes the changes in a changes structure when a client receives an XkbControlsNotify event"
---

<p>XkbNoteControlsChanges &#8211; Notes the changes in a changes structure when a client receives an XkbControlsNotify event </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>void XkbNoteControlsChanges</code> <code>(XkbControlsChangesPtr </code><i>changes</i><code>,</code> <code>XkbControlsNotifyEvent *</code><i>new</i><code>,</code> <code>unsigned int </code><i>wanted</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; changes</i></p>
<dd>
<dd>records changes indicated by new</p>
<dt><i>&#8211; new</i></p>
<dd>tells which things have changed</p>
<dt><i>&#8211; wanted</i></p>
<dd>tells which parts of new to record in changes</dl>
<h2>Description</h2>
<p>Whenever a field in the controls structure changes in the server&#8217;s keyboard description, the server sends an XkbControlsNotify event to all interested clients.To receive XkbControlsNotify events under all possible conditions, use <i>XkbSelectEvents </i> and pass XkbControlsNotifyMask in both <i>bits_to_change </i> and <i>values_for_bits.</i> </p>
<p> To receive XkbControlsNotify events only under certain conditions, use <i>XkbSelectEventDetails </i> using XkbControlsNotify as the <i>event_type </i> and specifying the desired state changes in <i>bits_to_change </i> and <i>values_for_bits </i> using mask bits from Table 1. </p>
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
<td>XkbAccessXFeedbackMask)</td>
<td></td>
<td></td>
<td>
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
<p> The <i>changed_ctrls </i> field specifies the controls components that have changed and consists of bits taken from the masks defined in Table 1 with &quot;ok&quot; in the <i>changed_ctrls </i> column. </p>
<p> The controls currently enabled in the server are reported in the <i>enabled_ctrls </i> field. If any controls were just enabled or disabled (that is, the contents of the <i>enabled_ctrls </i> field changed), they are flagged in the <i>enabled_ctrl_changes </i> field. The valid bits for these fields are the masks listed in Table 1 with &quot;ok&quot; in the <i>enabled_ctrls </i> column. The <i>num_groups </i> field reports the number of groups bound to the key belonging to the most number of groups and is automatically updated when the keyboard mapping changes. </p>
<p> If the change was caused by a request from a client, the <i>keycode </i> and <i>event_type </i> fields are set to zero and the <i>req_major </i> and <i>req_minor </i> fields identify the request. The <i>req_major value is the same as the major extension opcode. Otherwise,</i> <i>event_type </i> is set to the type of event that caused the change (one of KeyPress, KeyRelease, DeviceKeyPress, DeviceKeyRelease, ButtonPress or ButtonRelease), and <i>req_major </i> and <i>req_minor </i> are undefined. If <i>event_type </i> is KeyPress, KeyRelease, DeviceKeyPress, or DeviceKeyRelease, the <i>keycode </i> field is set to the key that caused the change. If <i>event_type </i> is ButtonPress or ButtonRelease, <i>keycode </i> contains the button number. </p>
<p> When a client receives an XkbControlsNotify event, it can note the changes in a changes structure using <i>XkbNoteControlsChanges.</i> </p>
<p> The <i>wanted </i> parameter is a bitwise inclusive OR of bits taken from the set of masks specified in Table 1 with &quot;ok&quot; in the <i>changed_ctrls </i> column. <i>XkbNoteControlsChanges </i> copies any changes reported in <i>new </i> and specified in <i>wanted </i> into the changes record specified by <i>old.</i></p>
<h2>Structures</h2>
<pre>The structure for the XkbControlsNotify event is defined as follows:
typedef struct {
 int type; /* Xkb extension base event code */
 unsigned long serial; /* X server serial number for event */
 Bool send_event; /* True =&gt; synthetically generated */
 Display * display; /* server connection where event generated */
 Time time; /* server time when event generated */
 int xkb_type; /* XkbCompatMapNotify */
 int device; /* Xkb device ID, will not be XkbUseCoreKbd */
 unsigned int changed_ctrls; /* bits indicating which controls data have changed*/
 unsigned int enabled_ctrls; /* controls currently enabled in server */
 unsigned int enabled_ctrl_changes; /* bits indicating enabled/disabled controls */
 int num_groups; /* current number of keyboard groups */
 KeyCode keycode; /* != 0 =&gt; keycode of key causing change */
 char event_type; /* Type of event causing change */
 char req_major; /* major event code of event causing change */
 char req_minor; /* minor event code of event causing change */
} XkbControlsNotifyEvent;</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbselecteventdetails/">XkbSelectEventDetails</a></code>(3), <code><a href="/docs/linux/man/3-xkbselectevents/">XkbSelectEvents</a></code>(3)</p>
