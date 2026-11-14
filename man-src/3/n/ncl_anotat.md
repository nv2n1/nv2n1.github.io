---
title: "ncl_anotat(3)"
name: "ncl_anotat"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_anotat/"
---

ANOTAT - Changes the values of certain primary control parameters, purportedly having to do with &quot;annotation&quot; of a graph. 

<h2>Synopsis</h2>ANOTAT (XLAB,YLAB,LBAC,LSET,NDSH,DSHC)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_anotat(char *xlab, char *ylab, int lbac, int lset, \ 
 int ndsh, char *dshc[])
<h2>Description</h2><dl COMPACT><dt>XLAB
<dd>(an input expression of type CHARACTER) defines a new &quot;x-axis label&quot;. (If the first character of this expression is &quot;CHAR(0)&quot;, no new &quot;x-axis label&quot; is defined; the current one will continue to be used.) A character string defining a new X-axis label must either be of the exact length specified by the current value of 'LINE/MAXIMUM.' (default: 40 characters), or shorter; if shorter, it must be terminated by the character defined by the current value of 'LINE/END.' (default: a '$'). The string becomes the new text of line number -100 of the label 'B'.
<dt>YLAB
<dd>(an input expression of type CHARACTER) defines a new &quot;y-axis label&quot;. (If the first character of this expression is &quot;CHAR(0)&quot;, no new &quot;y-axis label&quot; is defined; the current one will continue to be used.) A character string defining a new Y-axis label must either be of the exact length specified by the current value of 'LINE/MAXIMUM.' (default: 40 characters), or shorter; if shorter, it must be terminated by the character defined by the current value of 'LINE/END.' (default: a '$'). The string becomes the new text of line number 100 of the label 'L'.
<dt>LBAC
<dd>(an input expression of type INTEGER), if non-zero, must have the integer value 1, 2, 3, or 4, the real equivalent of which is to become the new value of 'BACKGROUND.'. (If LBAC is zero, no change is to be made in the current value.) The value &quot;1&quot; specifies a perimeter background, the value &quot;2&quot; a grid background, the value &quot;3&quot; a half-axis background, and the value &quot;4&quot; no background at all. 

 See the discussion of 'BACKGROUND.', in the autograph_params man page.
<dt>LSET
<dd>(an input expression of type INTEGER), if non-zero, must have the absolute value 1, 2, 3, or 4, the real equivalent of which is to be stored (by means of a call to AGSETI) as the new value of 'SET.'. If LSET is zero, no change is to be made in the current value of 'SET.'. 

 See the discussion of 'SET.', in the autograph_params man page.
<dt>NDSH
<dd>(an input expression of type INTEGER), if zero, specifies that no change is to be made in the parameters which specify the dashed-line patterns to be used for curves.
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>If NDSH is non-zero, it specifies an integer value whose real equivalent is to be stored as the new value of 'DASH/ SELECTOR.' (which has the default value &quot;1.&quot;).
<dt>&bull;
<dd>If NDSH is negative, 'DASH/SELECTOR.' is set negative, forcing EZMY and EZMXY to use internally-defined &quot;alphabetic&quot; patterns for the MANY curves drawn (&quot;A&quot; for the first, &quot;B&quot; for the second, . . ., &quot;Z&quot; for the 26th, &quot;A&quot; for the 27th, etc.). The routines EZY and EZXY are unaffected.
<dt>&bull;
<dd>If NDSH is greater than zero, it must be less than or equal to 26, and the next argument, DSHC, must contain NDSH dashed-line patterns comprising the new &quot;user&quot; set of patterns. The fact that 'DASH/SELECTOR.' is set positive forces EZMY and EZMXY to use this set of patterns. (The routines EZY and EZXY always use the first pattern in this set.) The contents of the array DSHC are copied to storage local to Autograph and pointers to them are installed as the values of 'DASH/PATTERNS/1.', '.../2.', etc.</dl></dl><dd>See the discussion of 'DASH.', in the autograph_params man page.
<dt>DSHC
<dd>(an input array of type CHARACTER, dimensioned NDSH) is meaningful only when NDSH is greater than zero. In this case, it must be an array of NDSH character strings, each of the length specified by the current value of 'DASH/ LENGTH.'. Each character string represents a dashed-line pattern; dollar signs mean &quot;pen down&quot;, quotes mean &quot;pen up&quot;, and other characters mean &quot;draw me&quot;. 

 See the discussion of 'DASH.', in the autograph_params man page.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>This routine sets internal parameter values. For a complete list of parameters available in this utility, see the autograph_params man page.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: agex08, agex10, agex13, bnchmk, sprevx.
<h2>Access</h2>To use ANOTAT or c_anotat, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: autograph, autograph_params, agback, agbnch, agchax, agchcu, agchil, agchnl, agcurv, agdshn, aggetc, aggetf, aggeti, aggetp, aggetr, agpwrt, agrstr, agsave, agsetc, agsetf, agseti, agsetp, agsetr, agstup, agutol, displa, ezmxy, ezmy, ezxy, ezy
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
