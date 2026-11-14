---
title: "ncl_agsetc(3)"
name: "ncl_agsetc"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_agsetc/"
---

AGSETC - Allows a user program to (in effect) store a character string as the value of a specified single parameter. 

<h2>Synopsis</h2>CALL AGSETC (TPGN,CUSR)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_agsetc (char *tpgn, char *cusr)
<h2>Description</h2><dl COMPACT><dt>TPGN
<dd>(an input expression of type CHARACTER) is a parameter identifier, as described for AGSETP, above. The specified parameter must be one of those which intrinsically have values of type character: 'LINE/END.', 'LABEL/NAME.', 'LINE/ TEXT.', or 'DASH/PATTERN/n.'
<dt>CUSR
<dd>(an input expression of type CHARACTER) is the desired character string.
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>If 'LINE/END.' is being set, only the first character of CUSR will be used.
<dt>&bull;
<dd>If 'LABEL/NAME.' is being set, the length of the string CUSR will be taken to be &quot;MAX(1,LEN(CUSR))&quot;.
<dt>&bull;
<dd>If the text of a label is being set, CUSR must either be of the exact length specified by 'LINE/MAXIMUM.' (40 characters, by default) or shorter; if shorter, it must be terminated by the character defined by 'LINE/END.' (default: a '$').
<dt>&bull;
<dd>If a dash pattern is being set, the length of CUSR will be taken to be the minimum of &quot;LEN(CUSR)&quot; and the value specified by 'DASH/LENGTH.'.</dl></dl>
</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>This routine allows you to set the current value of Autograph parameters. For a complete list of parameters available in this utility, see the autograph_params man page.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: agex05, agex06, agex07, agex08, agex09, agex13, tagupw, tautog, fagaxlbl, fagovrvw.
<h2>Access</h2>To use AGSETC or c_agsetc, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order. To get smoother curves, drawn using spline interpolation, also load libdashsmth.o. Or, you can use the ncargf77 command to compile your program and load the above libraries, then, to get smoother curves, use the -dashsmth option.
<h2>Messages</h2>See the autograph man page for a description of all Autograph error messages and/or informational messages.
<h2>See Also</h2>Online: autograph, autograph_params, agback, agbnch, agchax, agchcu, agchil, agchnl, agcurv, agdshn, aggetc, aggetf, aggeti, aggetp, aggetr, agpwrt, agrstr, agsave, agsetf, agseti, agsetp, agsetr, agstup, agutol, anotat, displa, ezmxy, ezmy, ezxy, ezy 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
