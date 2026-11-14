---
title: "xkbsasetptrdfltvalue(3)"
name: "xkbsasetptrdfltvalue"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbsasetptrdfltvalue/"
description: "XkbSASetPtrDfltValue – Sets the valueXXX field of act from val"
---

<p>XkbSASetPtrDfltValue &#8211; Sets the valueXXX field of act from val </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>void XkbSASetPtrDfltValue</code> <code>(XkbAction </code><i>act</i><code>,</code> <code>int </code><i>val</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; act</i></p>
<dd>
<dd>action in which to set valueXXX</p>
<dt><i>&#8211; val</i></p>
<dd>value to set in valueXXX</dl>
<h2>Description</h2>
<p>Actions associated with the XkbPtrDfltAction structure change the mk_dflt_btn attribute of the MouseKeys control. </p>
<p> If the MouseKeys control is not enabled, KeyPress and KeyRelease events are treated as though the action is XkbSA_NoAction. Otherwise, this action changes the <i>mk_dflt_btn </i> attribute of the MouseKeys control. </p>
<p> The <i>type </i> field of the XkbPtrDfltAction structure should always be XkbSA_SetPtrDflt. </p>
<p> The <i>flags </i> field is composed of the bitwise inclusive OR of the values shown in Table 1 (currently there is only one value defined). </p>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=2>Table 1 Pointer Default Flags
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
<td>XkbSA_DfltBtnAbsolute</td>
<td> If set, the value field represents an absolute pointer button. Otherwise, the value field represents the amount to be added to the current default button.
</td>
</tr>
</table>
<p> The <i>affect </i> field specifies what changes as a result of this action. The only valid value for the <i>affect </i> field is XkbSA_AffectDfltBtn. </p>
<p> The <i>valueXXX </i> field is a signed character that represents the new button value for the <i>mk_dflt_btn </i> attribute of the MouseKeys control. If XkbSA_DfltBtnAbsolute is set in <i>flags, valueXXX </i> specifies the button to be used; otherwise, <i>valueXXX </i> specifies the amount to be added to the current default button. In either case, illegal button choices are wrapped back around into range. Xkb provides macros, to convert between the integer and signed character values in XkbPtrDfltAction structures.</p>
<h2>Structures</h2>
<pre> typedef struct _XkbPtrDfltAction {
 unsigned char type; /* XkbSA_SetPtrDflt */
 unsigned char flags; /* controls the pointer button number */
 unsigned char affect; /* XkbSA_AffectDfltBtn */
 char valueXXX; /* new default button member */
 } XkbPtrDfltAction;</pre>
