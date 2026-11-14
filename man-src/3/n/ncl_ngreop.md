---
title: "ncl_ngreop(3)"
name: "ncl_ngreop"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ngreop/"
---

NGREOP - reopen an existing NCAR Graphics metafile for appending.

<h2>Synopsis</h2>

CALL NGREOP(WKID, CONID, ITYPE, FNAME, IOPT, IAT, RAT, 
 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>NCOLRS, NSTART, CTAB)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 
 #include &lt;ncarg/gks.h&gt; 

 void c_ngsrat(int wkid, int conid, int itype, char *fname, 
 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>int iopt, int&nbsp;<wbr>*iat, float&nbsp;<wbr>*rat, int ncolrs,&nbsp;<wbr> 
 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>int nstart, Gcolr_rep&nbsp;<wbr>*ctab)

<h2>Description</h2>

<dl><dt>WKID
<dd>(an input variable of type INTEGER) specifying the workstation identifier that the reopened metafile will subsequently be known by. This does not have to be the same as the worksttion identifier used to create the original metafile.
<dt>CONID
<dd>(an input variable of type INTEGER) specifying the connection identifier.
<dt>ITYPE
<dd>(an input variable of type INTEGER) specifying the workstation type. Currently the only valid value is &quot;1&quot;. This subroutine may be augmented to accommodate PostScript files in the future.
<dt>FNAME
<dd>(an input variable of type CHARACTER) specifying the filename of the metafile being opened for appending.
<dt>IOPT
<dd>(an input variable of type INTEGER) specifying the desired action:
<dt> = 0
<dd>reestablish the color table only (using the color table in argument CTAB described below). The attributes of the reopened workstation will be set to default values and may well be out of sync with the current GKS attributes.
<dt> = 1
<dd>reestablish the color table and GKS state (the GKS state as supplied in arguments IAT and RAT described below). The state values will not be flushed to the metafile.
<dt> = 2
<dd>reestablish the color table and GKS state and flush the GKS state values to the metafile.
<dt> = 3
<dd>reestablish the color table and flush the current GKS state values to the metafile (not the values in IAT and RAT). values to the metafile.
<dd>If IOPT equals 1 or 2, then IAT and RAT must be supplied, otherwise not.
<dt>IAT
<dd>(an input array of type INTEGER dimensioned for 14) that contains GKS integer state variables as follows:
<dd>IAT( 1) = Clip indicator
<dd>IAT( 2) = Line type
<dd>IAT( 3) = Polyline color index
<dd>IAT( 4) = Marker type
<dd>IAT( 5) = Polymarker color index
<dd>IAT( 6) = Text font
<dd>IAT( 7) = Text precision
<dd>IAT( 8) = Text color index
<dd>IAT( 9) = Text path
<dd>IAT(10) = Text horizontal alignment
<dd>IAT(11) = Text vertical alignment
<dd>IAT(12) = Fill area interior style
<dd>IAT(13) = Fill are style index
<dd>IAT(14) = Fill area color index
<dt>RAT
<dd>(an input array of type REAL dimensioned for 7) that contains REAL GKS attribute settings as follows:
<dd>RAT( 1) = Linewidth scale factor
<dd>RAT( 2) = Marker scale factor
<dd>RAT( 3) = Character expansion factor
<dd>RAT( 4) = Character spacing
<dd>RAT( 5) = Character height in world coordinates
<dd>RAT( 6) = Character up vector, X component in world coordinates
<dd>RAT( 7) = Character up vector, Y component in world coordinates
<dt>NCOLRS
<dd>(an input variable of type INTEGER) that specifies the number of colors in the color table supplied in argument CTAB, described below. NCOLRS can be 0 .
<dt>NSTART
<dd>(an input variable of type INTEGER) that specifies the color index associated with the first color in the color table CTAB (all other color indices are filled in in sequence). For example, if NCOLRS = 3 and NSTART = 4, then the color values defined in CTAB would be used to define color indices 4, 5, and 6.
<dt>CTAB
<dd>(in the FORTRAN version of this routine, a two-dimensional input array of type REAL dimensioned CTAB(3,NCOLRS); in the C version of this routine, a one-dimensional input array of type Gcolr_rep dimensioned ctab[ncolrs]) that specifies a color table used to initialize the reopened metafile. This color table does not necessarily have to agree with the color table in effect when the original metafile was created.</dl>

<h2>Usage</h2>

The most common usage of NGREOP would be in conjunction with usage of NGSRAT and NGMFTC. NGMFTC would be used to temporarily close a metafile and NGSRAT used to save the state of the GKS primitive attributes at the time of the close. To reopen the temporarily closed metafile you would call NGREOP with the attribute settings previously saved and a setting of IOPT of 2. NGMFTC can be used to temporarily close a metafile any time after it has been opened, even in the middle of a picture. 

 NGREOP only reopens the metafile and does not activate it. It will be necessary to call GACWK before sending graphics primitives to the reopened metafile. 

 NGREOP can also be used to reopen a previously created metafile - either created in an independent job step, or in the same job step.

<h2>Examples</h2>

The following sequence: <pre> CALL <a HREF="//www.systutorials.com/docs/linux/man/1-NGMFTC/">NGMFTC</a>(1)
 CALL NGSRAT(2, IAT, RAT)
 ... do stuff
 CALL NGREOP(CALL NGREOP(1, 2, 1, 'gmeta1', 2, IAT, RAT, 
 NCOLS, 0, CTAB)</pre>would temporarily close the metafile with workstation ID of 1 (in this case a metafile with name &quot;gmeta1&quot;) and save the GKS state variables at the time of the close. Then the call to NGREOP would reopen the metafile for appending. 

 Use the ncargex command to see the following relevant example: pgkex27.

<h2>Access</h2>

To use NGREOP or c_ngreop, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>Messages</h2>

NGREOP issues the same messages as those issued by GOPWK.

<h2>See Also</h2>

Online: ngmftc(3NCARG), ngsrat(3NCARG), 

 Online URL: <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/gks/gkshome.html">http://ngwww.ucar.edu/ngdoc/ng/gks/gkshome.html</a>

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
