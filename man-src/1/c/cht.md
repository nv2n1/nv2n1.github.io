---
title: "cht(1)"
name: "cht"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cht/"
description: "cht – chemtool drawings analyzer"
---

<h2 class="name">NAME</h2>
<p> cht &#8211; chemtool drawings analyzer</p>
<h2>SYNOPSIS</h2>
<p> <code>cht</code> [<code>options</code>] <i>filename.cht</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>cht</code> is a commandline tool to derive the sum formula and molecular mass of the molecule depicted in a <code>chemtool </code> drawing file. It is also available from within <code>chemtool</code> to calculate these data for the current structure or a marked fragment of it. </p>
<p> <code>cht</code> currently recognizes the element symbols C, H, O, N, P, S, Si, B, Br, Cl, F, I, Al, As, Ba, Be, Bi, Ca, Cd, Co, Cr, Cs, Cu, Fe, Ga, Ge, In, K, Li, Mg, Mn, Na, Ni, Pb, Rb, Sb, Sc, Se, Sn, Sr, Te, Ti, Tl, V, Zn (that is, all main group elements except the noble gases, and the first row of transition metals) and the abbreviations Ac, Ade, Bn, Bu, iBu, tBu, Bz, BOC, Cyt, CE, DBAM, DMAM, DMTr, Et, Gua, Me, Ms, MOC, MOM, MMTr, Ph, Pr, iPr, Tf, Thy, Tol, Tr, Ts, TBDMS, TBDPS, TMS, TMTr, Ura, Z. </p>
<p> It can handle two levels of parentheses; e.g. P[OCH(CH_3)_2]_3. </p>
<p> When <code>cht</code> detects any duplicate (overlapping) bonds in the drawing file, it will prepend an exclamation mark to the calculated (and likely wrong) sum formula. </p>
<h2>OPTIONS</h2>
<p> <code>cht</code> understands the following options:</p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Displays brief help and list of options.</p>
<dt><code>-e, &#8211;exact</code></p>
<dd> Calculate exact mass for MS.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Be verbose.</p>
<dt><code>-d, &#8211;debug</code></p>
<dd> Be extremely verbose. </p>
</dl>
<h2>BUGS</h2>
<p> <code>cht</code> can misinterpret molecules that contain the &#8216;aromatic ring&#8217; symbol, as it uses a fixed search radius to identify the aromatic system that it denotes. It also does not handle the &#8216;partial double bond&#8217;, so you should avoid these two in drawings that you intend to use with <code>cht</code>. </p>
<p> A label that is offset from the corresponding bond end by more than five pixels is not recognized, so that the default CH2 or CH3 group enters the calculation in its place. </p>
<p> In general, one should check the plausibility of the generated sum formula wherever possible. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-chemtool/">chemtool</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> <code>Radek Liboska</code> </p>
<h2>Index</h2>
