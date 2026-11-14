---
title: "ncl_gset_text_font_prec(3)"
name: "ncl_gset_text_font_prec"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gset_text_font_prec/"
description: "gset_text_font_prec (Set text font and precision) – sets the text font and precision."
---

<p>gset_text_font_prec (Set text font and precision) &#8211; sets the text font and precision.</p>
<h2>Synopsis</h2>
<p>#include &lt;ncarg/gks.h&gt; </p>
<p> void gset_text_font_prec(const Gtext_font_prec *text_font_prec);</p>
<h2>Description</h2>
<dl COMPACT>
<dt>text_font_prec.font</p>
<dd>(Gint, Input) Specifies the text font to be used in subsequent calls to the gtext output primitive. Options are:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> 1</p>
<dd>ASCII font (default)</p>
<dt> -2</p>
<dd>Hershey cartographic Roman</p>
<dt> -3</p>
<dd>Hershey cartographic Greek</p>
<dt> -4</p>
<dd>Hershey simplex Roman</p>
<dt> -5</p>
<dd>Hershey simplex Greek</p>
<dt> -6</p>
<dd>Hershey simplex script</p>
<dt> -7</p>
<dd>Hershey complex Roman</p>
<dt> -8</p>
<dd>Hershey complex Greek</p>
<dt> -9</p>
<dd>Hershey complex script</p>
<dt>-10</p>
<dd>Hershey complex italic</p>
<dt>-11</p>
<dd>Hershey complex Cyrillic</p>
<dt>-12</p>
<dd>Hershey duplex Roman</p>
<dt>-13</p>
<dd>Hershey triplex Roman</p>
<dt>-14</p>
<dd>Hershey triplex italic</p>
<dt>-15</p>
<dd>Hershey Gothic German</p>
<dt>-16</p>
<dd>Hershey Gothic English</p>
<dt>-17</p>
<dd>Hershey Gothic Italian</p>
<dt>-18</p>
<dd>Hershey math symbols</p>
<dt>-19</p>
<dd>Hershey symbol set 1</p>
<dt>-20</p>
<dd>Hershey symbol set 2 </p>
<p> The Hershey fonts are not standardized by GKS but are locally implemented in NCAR GKS-0A. GKS requires that such locally implemented fonts be assigned negative font numbers. To view the Hershey fonts, look at the plots produced from the PLOTCHAR example (execute &quot;ncargex epltch&quot; to get a metafile) and examine the plot titled &quot;PLCHHQ &#8211; FONTCAP DATABASES ADDED 6/90&quot;. The font numbers there are the absolute values of the value for text_font_prec.font described here (PLOTCHAR has no need to follow the structures that GKS imposes on font names for gset_text_font_prec).</dl>
</dl>
<dt>text_font_prec.prec</p>
<dd>(Input) Gives the precision used in subsequent calls to the gtext output primitive for font type text_font_prec.font. Options are:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>GPREC_STRING</p>
<dd>String precision (good). This is the GKS default.</p>
<dt>GPREC_CHAR</p>
<dd>Character precision (better).</p>
<dt>GPREC_STROKE</p>
<dd>Stroke precision (best). This is the default for NCAR GSK-0A.</dl>
</dl>
</dl>
<h2>Usage</h2>
<p>If one accesses the Hershey fonts via gset_text_font_prec and gtext, then the characters are not stroked until viewing time. If one accesses the Hershey fonts via PLOTCHAR, then the characters are stroked by PLOTCHAR itself. This can make a significant difference in metafile sizes.</p>
<h2>Access</h2>
<p>To use the GKS C-binding routines, load the ncarg_gks and ncarg_c libraries.</p>
<h2>See Also</h2>
<p>Online: <code>gtext(3NCARG),</code> <code>gset_text_path(3NCARG),</code> <code>gset_text_align(3NCARG),</code> <code>gset_char_ht(3NCARG),</code> <code>gset_char_space(3NCARG),</code> <code>gset_char_up_vec(3NCARG),</code> <code>gset_char_expan(3NCARG),</code> <code>gset_colr_rep(3NCARG),</code> <code>gset_text_colr_ind(3NCARG),</code> <code>ginq_text_path(3NCARG),</code> <code>ginq_text_align(3NCARG),</code> <code>ginq_text_font_prec(3NCARG),</code> <code>ginq_char_ht(3NCARG),</code> <code>ginq_char_space(3NCARG),</code> <code>ginq_char_up_vec(3NCARG),</code> <code>ginq_char_expan(3NCARG),</code> <code>plotchar(3NCARG),</code> <code>gks(3NCARG),</code> <code>ncarg_gks_cbind(3NCARG),</code> </p>
<p> Hardcopy: User&#8217;s Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version</p>
<h2>Copyright</h2>
<p>Copyright (C) 1987-2009<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement.</p>
