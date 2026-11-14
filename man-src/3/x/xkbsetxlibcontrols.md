---
title: "xkbsetxlibcontrols(3)"
name: "xkbsetxlibcontrols"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbsetxlibcontrols/"
description: "XkbSetXlibControls – Changes the state of the Library Controls"
---

<p>XkbSetXlibControls &#8211; Changes the state of the Library Controls </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>unsigned int XkbSetXlibControls</code> <code>(Display *</code><i>display</i><code>,</code> <code>unsigned long </code><i>bits_to_change</i><code>,</code> <code>unsigned long </code><i>values_for_bits</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; display</i></p>
<dd>
<dd>connection to X server</p>
<dt><i>&#8211; bits_to_change</i></p>
<dd>selects controls to be modified</p>
<dt><i>&#8211; values_for_bits</i></p>
<dd>turns selected controls on (1) or off (0)</dl>
<h2>Description</h2>
<p><i>XkbSetXlibControls </i> modifies the state of the controls selected by <i>bits_to_change; </i> only the controls selected by <i>bits_to_change </i> are modified. If the bit corresponding to a control is on in <i>bits_to_change </i> and also on in <i>values_for_bits, </i> the control is enabled. If the bit corresponding to a control is on in <i>bits_to_change </i> but off in <i>values_for_bits, </i> the control is disabled. <i>bits_to_change </i> should be an inclusive OR of bits from Table 1. </p>
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
<h2>Return Values</h2>
<dl COMPACT>
<dt>(1 &lt;&lt; 0)</p>
<dd>XkbLC_ForceLatin1Lookup</p>
<dt>(1 &lt;&lt; 1)</p>
<dd>XkbLC_ConsumeLookupMods</p>
<dt>(1 &lt;&lt; 2)</p>
<dd>XkbLC_AlwaysConsumeShiftAndLock</p>
<dt>(1 &lt;&lt; 3)</p>
<dd>XkbLC_IgnoreNewKeyboards</p>
<dt>(1 &lt;&lt; 29)</p>
<dd>XkbLC_ConsumeKeysOnComposeFail</p>
<dt>(1 &lt;&lt; 30)</p>
<dd>XkbLC_ComposeLED</p>
<dt>(1 &lt;&lt; 31)</p>
<dd>XkbLC_BeepOnComposeFail</p>
<dt>(0xc0000007)</p>
<dd>XkbLC_AllControls </p>
</dl>
