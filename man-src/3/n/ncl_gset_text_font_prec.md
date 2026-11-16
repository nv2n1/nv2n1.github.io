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
<dt>text_font_prec.font</dt>
<dd>(Gint, Input) Specifies the text font to be used in subsequent calls to the gtext output primitive. Options are:</dd>
<dl COMPACT>
<dd>
</dd><dl COMPACT>
<dt> 1</dt>
<dd>ASCII font (default)</dd>
<dt> -2</dt>
<dd>Hershey cartographic Roman</dd>
<dt> -3</dt>
<dd>Hershey cartographic Greek</dd>
<dt> -4</dt>
<dd>Hershey simplex Roman</dd>
<dt> -5</dt>
<dd>Hershey simplex Greek</dd>
<dt> -6</dt>
<dd>Hershey simplex script</dd>
<dt> -7</dt>
<dd>Hershey complex Roman</dd>
<dt> -8</dt>
<dd>Hershey complex Greek</dd>
<dt> -9</dt>
<dd>Hershey complex script</dd>
<dt>-10</dt>
<dd>Hershey complex italic</dd>
<dt>-11</dt>
<dd>Hershey complex Cyrillic</dd>
<dt>-12</dt>
<dd>Hershey duplex Roman</dd>
<dt>-13</dt>
<dd>Hershey triplex Roman</dd>
<dt>-14</dt>
<dd>Hershey triplex italic</dd>
<dt>-15</dt>
<dd>Hershey Gothic German</dd>
<dt>-16</dt>
<dd>Hershey Gothic English</dd>
<dt>-17</dt>
<dd>Hershey Gothic Italian</dd>
<dt>-18</dt>
<dd>Hershey math symbols</dd>
<dt>-19</dt>
<dd>Hershey symbol set 1</dd>
<dt>-20</dt>
<dd>Hershey symbol set 2 </dd>
<p> The Hershey fonts are not standardized by GKS but are locally implemented in NCAR GKS-0A. GKS requires that such locally implemented fonts be assigned negative font numbers. To view the Hershey fonts, look at the plots produced from the PLOTCHAR example (execute &quot;ncargex epltch&quot; to get a metafile) and examine the plot titled &quot;PLCHHQ &#8211; FONTCAP DATABASES ADDED 6/90&quot;. The font numbers there are the absolute values of the value for text_font_prec.font described here (PLOTCHAR has no need to follow the structures that GKS imposes on font names for gset_text_font_prec).</dl>
</dl>
<dt>text_font_prec.prec</dt>
<dd>(Input) Gives the precision used in subsequent calls to the gtext output primitive for font type text_font_prec.font. Options are:</dd>
<dl COMPACT>
<dd>
</dd><dl COMPACT>
<dt>GPREC_STRING</dt>
<dd>String precision (good). This is the GKS default.</dd>
<dt>GPREC_CHAR</dt>
<dd>Character precision (better).</dd>
<dt>GPREC_STROKE</dt>
<dd>Stroke precision (best). This is the default for NCAR GSK-0A.</dd></dl>
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
