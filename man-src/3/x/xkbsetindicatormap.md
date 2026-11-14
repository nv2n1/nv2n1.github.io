---
title: "xkbsetindicatormap(3)"
name: "xkbsetindicatormap"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbsetindicatormap/"
description: "XkbSetIndicatorMap – Downloads the changes to the server based on modifications to a local copy of the keyboard description which will update the maps for one or more indicators"
---

<p>XkbSetIndicatorMap &#8211; Downloads the changes to the server based on modifications to a local copy of the keyboard description which will update the maps for one or more indicators </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Bool XkbSetIndicatorMap</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>unsigned int </code><i>which</i><code>,</code> <code>XkbDescPtr </code><i>desc</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>
<dd>connection to the X server</p>
<dt><i>&#8211; which</i></p>
<dd>mask of indicators to change</p>
<dt><i>&#8211; desc</i></p>
<dd>keyboard description from which the maps are taken</dl>
<h2>Description</h2>
<p>This section discusses the effects of explicitly changing indicators depending upon different settings in the indicator map. See Tables 1 and Table 2 for information on the effects of the indicator map fields when explicit changes are made. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3>Table 1 XkbIndicatorMapRec which_groups and groups,
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3>Indicator Drives Keyboard
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>which_groups</td>
<td>New State</td>
<td>Effect on Keyboard Group State
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XkbIM_UseNone</td>
<td>On or Off</td>
<td>No effect
</td>
</tr>
<tr VALIGN=top>
<td>XkbIM_UseBase</td>
<td>On or Off</td>
<td>No effect
</td>
</tr>
<tr VALIGN=top>
<td>XkbIM_UseLatched</td>
<td>On</td>
<td> The groups field is treated as a group mask. The keyboard group latch is changed to the lowest numbered group specified in groups; if groups is empty, the keyboard group latch is changed to zero.
</td>
</tr>
<tr VALIGN=top>
<td>XkbIM_UseLatched</td>
<td>Off</td>
<td> The groups field is treated as a group mask. If the indicator is explicitly extinguished, keyboard group latch is changed to the lowest numbered group not specified in groups; if groups is zero, the keyboard group latch is set to the index of the highest legal keyboard group.
</td>
</tr>
<tr VALIGN=top>
<td>XkbIM_UseLocked or</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>XkbIM_UseEffective</td>
<td>On</td>
<td> If the groups mask is empty, group is not changed; otherwise, the locked keyboard group is changed to the lowest numbered group specified in groups.
</td>
</tr>
<tr VALIGN=top>
<td>XkbIM_UseLocked or</td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>XkbIM_UseEffective</td>
<td>Off</td>
<td> Locked keyboard group is changed to the lowest numbered group that is not specified in the groups mask, or to Group1 if the groups mask contains all keyboard groups.
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>
</td>
</tr>
</table>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3>Table 2 XkbIndicatorMapRec which_mods and mods,
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=3>Indicator Drives Keyboard
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>which_mods</td>
<td>New State</td>
<td>Effect on Keyboard Modifiers
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XkbIM_UseNone or XkbIM_UseBase</td>
<td>On or Off</td>
<td>No Effect
</td>
</tr>
<tr VALIGN=top>
<td>XkbIM_UseLatched</td>
<td>On</td>
<td> Any modifiers specified in the mask field of mods are added to the latched modifiers.
</td>
</tr>
<tr VALIGN=top>
<td>XkbIM_UseLatched</td>
<td>Off</td>
<td> Any modifiers specified in the mask field of mods are removed from the latched modifiers.
</td>
</tr>
<tr VALIGN=top>
<td>XkbIM_UseLocked, XkbIM_UseCompat, or XkbIM_UseEffective</td>
<td>On</td>
<td> Any modifiers specified in the mask field of mods are added to the locked modifiers.
</td>
</tr>
<tr VALIGN=top>
<td>XkbIM_UseLocked</td>
<td>Off</td>
<td> Any modifiers specified in the mask field of mods are removed from the locked modifiers.
</td>
</tr>
<tr VALIGN=top>
<td>XkbIM_UseCompat or XkbIM_UseEffective</td>
<td>Off</td>
<td> Any modifiers specified in the mask field of mods are removed from both the locked and latched modifiers.
</td>
</tr>
</table>
<p> If XkbIM_LEDDrivesKB is set and XkbIM_NoExplicit is not, and if you call a function that updates the server&#8217;s image of the indicator map (such as <i>XkbSetIndicatorMap </i> or <i>XkbSetNamedIndicator),</i><br />
&nbsp;Xkb changes the keyboard state and controls to reflect the other fields of the&nbsp; indicator map. If you attempt to explicitly change the value of an indicator for which XkbIM_LEDDrivesKB is absent or for which XkbIM_NoExplicit is present, keyboard state or controls are unaffected.<br />
&nbsp; If neither XkbIM_NoAutomatic nor XkbIM_NoExplicit is set in an indicator map, Xkb honors any request to change the state of the indicator, but the new state might be immediately superseded by automatic changes to the indicator state if the keyboard state or controls change. </p>
<p> The effects of changing an indicator that drives the keyboard are cumulative; it is possible for a single change to affect keyboard group, modifiers, and controls simultaneously. </p>
<p> If you change an indicator for which both the XkbIM_LEDDrivesKB and XkbIM_NoAutomatic flags are specified, Xkb applies the keyboard changes specified in the other indicator map fields and changes the indicator to reflect the state that was explicitly requested. The indicator remains in the new state until it is explicitly changed again. </p>
<p> If the XkbIM_NoAutomatic flag is not set and XkbIM_LEDDrivesKB is set, Xkb applies the changes specified in the other indicator map fields and sets the state of the indicator to the values specified by the indicator map. Note that it is possible in this case for the indicator to end up in a different state than the one that was explicitly requested. For example, Xkb does not extinguish an indicator with <i>which_mods </i> of XkbIM_UseBase and <i>mods </i> of Shift if, at the time Xkb processes the request to extinguish the indicator, one of the Shift keys is physically depressed. </p>
<p> If you explicitly light an indicator for which XkbIM_LEDDrivesKB is set, Xkb enables all of the boolean controls specified in the <i>ctrls </i> field of its indicator map. Explicitly extinguishing such an indicator causes Xkb to disable all of the boolean controls specified in <i>ctrls. </i> </p>
<p> For each bit set in the <i>which </i> parameter, <i>XkbSetIndicatorMap </i> sends the corresponding indicator map from the <i>desc </i> parameter to the server.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbsetnamedindicator/">XkbSetNamedIndicator</a></code>(3)</p>
