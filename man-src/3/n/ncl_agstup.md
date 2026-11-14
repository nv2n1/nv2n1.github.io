---
title: "ncl_agstup(3)"
name: "ncl_agstup"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_agstup/"
---

AGSTUP - Performs &quot;set-up&quot; tasks required before AGBACK and AGCURV may be called. Basically, AGSTUP examines the current values of the primary control parameters for errors and computes from them and from its arguments the values of secondary control parameters. The primary and secondary control parameters together determine how the routines AGBACK and AGCURV will behave. 

<h2>Synopsis</h2>&nbsp;<wbr>CALL AGSTUP&nbsp;<wbr>(XDRA,NVIX,IIVX,NEVX,IIEX,YDRA,NVIY,IIVY, 
 + NEVY,IIEY)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_agstup (float *xdra, int nvix, int iivx, int nevx, \ 
 int iiex, float *ydra, int nviy, int iivy, int nevy, \ 
 int iiey)
<h2>Description</h2>The first five arguments of AGSTUP are meaningful only if at least one of 'X/MINIMUM.' and 'X/MAXIMUM.' has the value &quot;null 1&quot; or &quot;null 2&quot;, specifying that Autograph is to determine for itself the minimum and/or maximum X coordinate in the user's data. Similarly, the second five arguments are meaningful only if at least one of 'Y/ MINIMUM.' and 'Y/MAXIMUM.' has the value &quot;null 1&quot; or &quot;null 2&quot;.
<dl COMPACT><dt>XDRA
<dd>(an input array of type REAL, dimensioned as implied by the next four arguments) contains user X coordinates.
<dt>NVIX
<dd>(an input expression of type INTEGER) is the number of &quot;vectors&quot; of data from XDRA to be considered in computing the minimum and/or maximum X values.
<dt>IIVX
<dd>(an input expression of type INTEGER) is the index increment between two &quot;vectors&quot; in XDRA. The 1st element of the first vector is <a HREF="/docs/linux/man/1-xdra/">XDRA</a>(1), the 1st element of the second vector is XDRA(1+IIVX), the 1st element of the third vector is XDRA(1+IIVX*2), etc.
<dt>NEVX
<dd>(an input expression of type INTEGER) is the number of elements of each vector in XDRA to be considered in computing the minimum and/or maximum X values.
<dt>IIEX
<dd>(an input expression of type INTEGER) is the index increment between two consecutive elements of a vector in XDRA. The second element of the 1st vector is XDRA (1+IIEX), the third element of the 1st vector is XDRA(1+IIEX*2), etc. If IIEX has the value 0, the contents of XDRA are ignored completely; the minimum and maximum X values are considered to be &quot;1.&quot; and FLOAT(NEVX), respectively.
<dt>YDRA, NVIY, IIVY, NEVY, and IIEY
<dd>are used similarly, but define the user Y coordinates. 

 Some examples:</dl><h2></h2><table> <tr VALIGN=top><td>X array</td><td>Data to use</td><td>XDRA</td><td>NVIX</td><td>IIVX</td><td>NEVX</td><td>HEX</td><td>
</td></tr><tr VALIGN=top><td>-------</td><td>-----------</td><td>----</td><td>----</td><td>----</td><td>----</td><td>---</td><td>
</td></tr><tr VALIGN=top><td>X(100)</td><td>all data</td><td><a HREF="/docs/linux/man/1-x/">X</a>(1)</td><td>1</td><td>-</td><td>100</td><td>1</td><td>
</td></tr><tr VALIGN=top><td>
&nbsp;<wbr></td><td>(X(I),I=1,99,2)</td><td><a HREF="/docs/linux/man/1-x/">X</a>(1)</td><td>1</td><td>-</td><td>50</td><td>2</td><td>
</td></tr><tr VALIGN=top><td>
&nbsp;<wbr></td><td>(X(I),I=51,99,2)</td><td>X(51)</td><td>1</td><td>-</td><td>25</td><td>2</td><td>
</td></tr><tr VALIGN=top><td>X(10,10)</td><td>all data</td><td>X(1,1)</td><td>10</td><td>10</td><td>10</td><td>1</td><td>
</td></tr><tr VALIGN=top><td>
&nbsp;<wbr></td><td> </td><td>X(1,1)</td><td>1</td><td>-</td><td>100</td><td>1</td><td>
</td></tr><tr VALIGN=top><td>
&nbsp;<wbr></td><td>((X(I,J),I=1,10),J=1,6)</td><td>X(1,1)</td><td>6</td><td>10</td><td>10</td><td>1</td><td>
</td></tr><tr VALIGN=top><td>
&nbsp;<wbr></td><td> </td><td>X(1,1)</td><td>10</td><td>1</td><td>6</td><td>10</td><td>
</td></tr><tr VALIGN=top><td>
&nbsp;<wbr></td><td> </td><td>X(1,1)</td><td>-</td><td>60</td><td>1</td><td></td><td>
</td></tr><tr VALIGN=top><td>
&nbsp;<wbr></td><td>((X(I,J),I=3,7),J=3,9)</td><td>X(3,3)</td><td>7</td><td>10</td><td>5</td><td>1</td><td>
</td></tr><tr VALIGN=top><td>
&nbsp;<wbr></td><td> </td><td>X(3,3)</td><td>5</td><td>1</td><td>7</td><td>10</td><td>
</td></tr><tr VALIGN=top><td>
&nbsp;<wbr></td><td>((X(I,J),I=3,7,4),J=3,9,3)</td><td>X(3,3)</td><td>3</td><td>30</td><td>2</td><td>4</td><td>
</td></tr><tr VALIGN=top><td>none</td><td>1., 2., . . ., 62.</td><td>-</td><td>-</td><td>-</td><td>62</td><td>0</td><td>
</td></tr> </table> 

 Note: The character &quot;-&quot; is used above to indicate an argument which is ignored and may be given a dummy value. 

 Normally, the X and Y coordinate data tendered to AGSTUP are the same data which will later be used to draw curves. However, this need not be the case. For example, one could call AGSTUP with a two-word XDRA (setting NVIX=1, IIVX=1, NEVX=2, and IIEX=1) containing a desired minimum and maximum to be used, disregarding the real data. 

 If 'INVERT.' is given the value &quot;1.&quot; (in place of its default value &quot;0.&quot;), AGSTUP will behave as if its first five arguments had been interchanged with its last five, so that X-coordinate values refer to vertical distances, and Y-coordinate values to horizontal distances, on the graph. This parameter affects AGCURV in a similar manner, thus allowing one to plot &quot;X as a function of Y&quot;.
<h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: agex13, cbex01.
<h2>Access</h2>To use AGSTUP or c_agstup, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order. To get smoother curves, drawn using spline interpolation, also load libdashsmth.o. Or, you can use the ncargf77 command to compile your program and load the above libraries, then, to get smoother curves, use the -dashsmth option.
<h2>Messages</h2>See the autograph man page for a description of all Autograph error messages and/or informational messages.
<h2>See Also</h2>Online: autograph, agback, agbnch, agchax, agchcu, agchil, agchnl, agcurv, agdshn, aggetc, aggetf, aggeti, aggetp, aggetr, agpwrt, agrstr, agsave, agsetc, agsetf, agseti, agsetp, agsetr, agutol, anotat, displa, ezmxy, ezmy, ezxy, ezy 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
