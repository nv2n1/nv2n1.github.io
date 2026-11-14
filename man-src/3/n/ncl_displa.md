---
title: "ncl_displa(3)"
name: "ncl_displa"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_displa/"
---

DISPLA - Changes the values of certain primary control parameters purportedly having to do with the &quot;display&quot; of a graph. 

<h2>Synopsis</h2>CALL DISPLA(LFRA,LROW,LTYP)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_displa(int lfra, int lrow, int ltyp)
<h2>Description</h2><dl COMPACT><dt>LFRA
<dd>(an input expression of type INTEGER), if non-zero, must have an integer value, the real equivalent of which is to become the new value of 'FRAME.'. If LFRA is zero, no change is to be made in the current value of 'FRAME.'.
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>The default value of 'FRAME.' is &quot;1.&quot;, specifying that each of the routines EZY, EZXY, EZMY, and EZMXY is to do a frame advance after drawing a graph.
<dt>&bull;
<dd>The value &quot;2.&quot; specifies no frame advance.
<dt>&bull;
<dd>The value &quot;3.&quot; specifies a frame advance before drawing a graph.</dl></dl><dt>LROW
<dd>(an input expression of type INTEGER), if non-zero, must have an integer value, the real equivalent of which is to become the new value of 'ROW.'. If LROW is zero, no change is to be made in the current value of 'ROW.'. This parameter affects the way in which the routines EZMY and EZMXY interpret the arguments XDRA and YDRA, as follows:
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>If 'ROW.' is positive, the first subscript of YDRA is a point number and the second subscript is a curve number. If 'ROW.' is negative, the order of the subscripts is reversed (row-wise, rather than column-wise, storage).
<dt>&bull;
<dd>If the absolute value of 'ROW.' is &quot;1.&quot;, XDRA is singly-subscripted; its subscript is a point number. If the absolute value of 'ROW.' is &quot;2.&quot; or greater, XDRA is doubly-subscripted; the order of the subscripts is the same as for YDRA.</dl></dl><dd>The default value of 'ROW.' is &quot;1.&quot;, specifying that XDRA is singly-subscripted by point number and that YDRA is doubly-subscripted by point number and curve number, in that order.
<dt>LTYP
<dd>(an input expression of type INTEGER), if non-zero, is an integer specifying new values for 'X/LOGARITHMIC.' and 'Y/LOGARITHMIC.'. If LTYP is zero, no change is to be made in the current values.
<dl COMPACT><dd><dl COMPACT><dt>&bull;
<dd>The parameter 'X/LOGARITHMIC.' has the default value &quot;0.&quot;, specifying a linear mapping of user X coordinates onto the horizontal axis of the grid window; it may be given either of the two values &quot;-1.&quot; or &quot;+1.&quot; to specify a logarithmic mapping. The value &quot;-1.&quot; protects it from being reset as a side effect of setting 'SET.'. DISPLA generates the value &quot;0.&quot; or &quot;-1.&quot;.
<dt>&bull;
<dd>The parameter 'Y/LOGARITHMIC.' is defined similarly and affects the mapping of user Y coordinates onto the vertical axis of the grid window.</dl></dl><dd>A non-zero LTYP resets these values, as follows: 

 <table> <tr VALIGN=top><td ALIGN=center>LTYP</td><td>'X/LOGARITHMIC.'</td><td>'Y/LOGARITHMIC.'
</td></tr><tr VALIGN=top><td ALIGN=center>----</td><td>----------------</td><td>----------------
</td></tr><tr VALIGN=top><td ALIGN=center>1</td><td>linear</td><td>linear
</td></tr><tr VALIGN=top><td ALIGN=center>2</td><td>linear</td><td>logarithmic
</td></tr><tr VALIGN=top><td ALIGN=center>3</td><td>logarithmic</td><td>linear
</td></tr><tr VALIGN=top><td ALIGN=center>4</td><td>logarithmic</td><td>logarithmic
</td></tr> </table></dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Usage</h2>This routine sets internal parameter values. For a complete list of parameters available in this utility, see the autograph_params man page.
<h2>Examples</h2>Use the ncargex command to see the following relevant example: agex13. bnchmk, splogy, sprevx.
<h2>Access</h2>To use DISPLA or c_displa, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: autograph, autograph_params, agback, agbnch, agchax, agchcu, agchil, agchnl, agcurv, agdshn, aggetc, aggetf, aggeti, aggetp, aggetr, agpwrt, agrstr, agsave, agsetc, agsetf, agseti, agsetp, agsetr, agstup, agutol, anotat, ezmxy, ezmy, ezxy, ezy
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
