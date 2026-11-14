---
title: "xkbsaactionsetctrls(3)"
name: "xkbsaactionsetctrls"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbsaactionsetctrls/"
description: "XkbSAActionSetCtrls – Sets the ctrls0 through ctrls3 fields of act from ctrls"
---

<p>XkbSAActionSetCtrls &#8211; Sets the <i>ctrls0 </i> through <i>ctrls3</i> fields of <i>act</i> from <i>ctrls</i> </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>void XkbSAActionSetCtrls</code> <code>(XkbCtrlsAction </code><i>act</i><code>,</code> <code>unsigned int </code><i>ctrls</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; act</i></p>
<dd>
<dd>action in which to set ctrls0-ctrls3</p>
<dt><i>&#8211; ctrls</i></p>
<dd>value to set in ctrls0-ctrls3</dl>
<h2>Description</h2>
<p>Actions associated with the XkbCtrlsAction structure change the state of the boolean controls. </p>
<p> The <i>type </i> field can have any one of the values shown in Table 1. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=2>Table 1 Controls Action Types
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Type</td>
<td>Effect
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XkbSA_SetControls</td>
<td> A key press enables any boolean controls specified in the ctrls fields that were not already enabled at the time of the key press. A key release disables any controls enabled by the key press. This action can cause XkbControlsNotify events.
</td>
</tr>
<tr VALIGN=top>
<td>XkbSA_LockControls</td>
<td> If the XkbSA_LockNoLock bit is not set in the flags field, a key press enables any controls specified in the ctrls fields that were not already enabled at the time of the key press.<br />
 If the XkbSA_LockNoUnlock bit is not set in the flags field, a key release disables any controls specified in the ctrls fields that were not already disabled at the time of the key press.<br />
 This action can cause XkbControlsNotify events.
</td>
</tr>
</table>
<p> The <i>flags </i> field is composed of the bitwise inclusive OR of the masks shown in Table 2. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=2>Table 2 Control Action Flags
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
<td>XkbSA_LockNoLock</td>
<td> If set, and the action type is XkbSA_LockControls, the server only disables controls.
</td>
</tr>
<tr VALIGN=top>
<td>XkbSA_LockNoUnlock</td>
<td> If set, and the action type is XkbSA_LockControls, the server only enables controls.
</td>
</tr>
</table>
<p> The XkbSA_SetControls action implements a key that enables a boolean control when pressed and disables it when released. The XkbSA_LockControls action is used to implement a key that toggles the state of a boolean control each time it is pressed and released. The XkbSA_LockNoLock and XkbSA_LockNoUnlock flags allow modifying the toggling behavior to only unlock or only lock the boolean control. </p>
<p> The <i>ctrls0, ctrls1, ctrls2, </i> and <i>ctrls3 </i> fields represent the boolean controls in the <i>enabled_ctrls </i> field of the controls structure. Xkb macros, to convert between the two formats. </p>
<p> <i>XkbSAActionSetCtrls </i> sets the <i>ctrls0 </i> through <i>ctrls3 </i> fields of <i>act </i> from <i>ctrls.</i></p>
<h2>Structures</h2>
<pre> typedef struct _XkbCtrlsAction {
 unsigned char type; /* XkbSA_SetControls, XkbSA_LockControls */
 unsigned char flags; /* with type, controls enabling and disabling 
of controls */
 unsigned char ctrls3; /* ctrls0 through ctrls3 represent the boolean 
controls */
 unsigned char ctrls2; /* ctrls0 through ctrls3 represent the boolean 
controls */
 unsigned char ctrls1; /* ctrls0 through ctrls3 represent the boolean 
controls */
 unsigned char ctrls0; /* ctrls0 through ctrls3 represent the boolean 
controls */
 } XkbCtrlsAction;</pre>
