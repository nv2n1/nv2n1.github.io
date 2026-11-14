---
title: "ncl_gstxp(3)"
name: "ncl_gstxp"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_gstxp/"
---

GSTXP (Set text path) - sets the text paths or directions in which text is to be drawn.
<h2>Synopsis</h2>CALL GSTXP (TXP)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/gks.h&gt; 

 void gset_text_path(Gtext_path text_path);
<h2>Description</h2><dl COMPACT><dt>TXP
<dd>(Integer, Input) - Gives the direction in which a character string is to be drawn. Options are:
<dl COMPACT><dd><dl COMPACT><dt>0
<dd>Draw successive characters in the string such that character n+l appears to the right of character n. This is text path &quot;right&quot; and is the default.
<dt>1
<dd>Draw character n+1 to the left of character n. This is text path &quot;left&quot;.
<dt>2
<dd>Draw character n+1 above character n. This is text path &quot;up&quot;.
<dt>3
<dd>Draw character n+1 below character n. This is text path &quot;down&quot;.</dl>
 

 The right, left, up, and down directions are relative to the character up vector. The right text path direction is perpendicular to the up vector direction. Thus, to draw a text string at a 45 degree angle the character up vector would be (-1,1), and the text path would be right .</dl></dl><h2>Access</h2>To use GKS routines, load the NCAR GKS-0A library ncarg_gks.
<h2>See Also</h2>Online: gtx, gstxal, gstxfp, gschh, gschsp, gschup, gschxp, gscr, gstxci, gqtxp, gqtxal, gqtxfp, gqchh, gqchsp, gqchup, gqchxp, plotchar, gset_text_path 

 Hardcopy: User's Guide for NCAR GKS-0A Graphics; NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
