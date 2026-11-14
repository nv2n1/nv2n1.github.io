---
title: "xkbgetxlibcontrols(3)"
name: "xkbgetxlibcontrols"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbgetxlibcontrols/"
description: "XkbGetXlibControls – Determines the current state of the Library Controls"
---

<p>XkbGetXlibControls &#8211; Determines the current state of the Library Controls </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>unsigned int XkbGetXlibControls</code> <code>(Display *</code><i>display</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; display</i></p>
<dd>
<dd>connection to X server</dl>
<h2>Description</h2>
<p><i>XkbGetXlibControls </i> returns the current state of the Library Controls as a bit mask that is an inclusive OR of the control masks from Table 1 for the controls that are enabled. For the optional compose processing controls, the fact that a control is enabled does not imply that it is actually implemented. </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=2>Table 1 Library Control Masks
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Library Control Mask</td>
<td>Value
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XkbLC_ForceLatin1Lookup</td>
<td>(1 &lt;&lt; 0)
</td>
</tr>
<tr VALIGN=top>
<td>XkbLC_ConsumeLookupMods</td>
<td>(1 &lt;&lt; 1)
</td>
</tr>
<tr VALIGN=top>
<td>XkbLC_AlwaysConsumeShiftAndLock</td>
<td>(1 &lt;&lt; 2)
</td>
</tr>
<tr VALIGN=top>
<td>XkbLC_IgnoreNewKeyboards</td>
<td>(1 &lt;&lt; 3)
</td>
</tr>
<tr VALIGN=top>
<td>XkbLC_ConsumeKeysOnComposeFail</td>
<td>(1 &lt;&lt; 29)
</td>
</tr>
<tr VALIGN=top>
<td>XkbLC_ComposeLED</td>
<td>(1 &lt;&lt; 30)
</td>
</tr>
<tr VALIGN=top>
<td>XkbLC_BeepOnComposeFail</td>
<td>(1 &lt;&lt; 31)
</td>
</tr>
<tr VALIGN=top>
<td>XkbLC_AllControls</td>
<td>(0xc0000007)
</td>
</tr>
</table>
