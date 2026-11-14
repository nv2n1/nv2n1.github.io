---
title: "ncl_conop4(3)"
name: "ncl_conop4"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_conop4/"
---

CONOP4 - sets option switches and specifys various CHARACTER parameters to be used by the Conran_family utility. 

<h2>Synopsis</h2>CONOP4 (IOPT,CHARS,NUMC,IFMT)
<h2>Description</h2><dl COMPACT><dt>IOPT
<dd>Character, input -- Selects an internal parameter and sets an option switch. The possibilities are: 

 
&nbsp;<wbr>&nbsp;<wbr>'DAS=ON',&nbsp;<wbr>'DAS=OFF',&nbsp;<wbr>'DAS=GTR',&nbsp;<wbr>'DAS=EQU',&nbsp;<wbr>'DAS=LSS', and&nbsp;<wbr>'DAS=ALL' 
 
&nbsp;<wbr>&nbsp;<wbr>'FMT=ON'&nbsp;<wbr>or&nbsp;<wbr>'FMT=OFF' 
 
&nbsp;<wbr>&nbsp;<wbr>'TLE=ON'&nbsp;<wbr>or&nbsp;<wbr>'TLE=OFF' 

 If the value of an IOPT option is 'OFF', then the next three arguments of the CONOP4 call, CHARS, NUMC, and IFMT can be given any dummy value. Option settings will be returned to their default values. 

 If an option is other than 'OFF', then the CHARS, NUMC, and IFMT arguments can be used to override the default settings of that option.
<dt>CHARS
<dd>Character, input -- A string of up to 64 characters.
<dt>NUMC
<dd>Integer, input -- The number of characters in string CHARS.
<dt>IFMT
<dd>Integer, input -- The maximum number of digits which can be printed by the output format loaded into CHARS when IOPT='FMT=ON'. IFMT is not used with any other value of IOPT. 

 The following options are defined by this subroutine:
<dt>DAS
<dd>This parameter determines which contours are represented by dashed lines. The dashed line pattern is set in argument CHARS. Arguments NUMC and IFMT are not used. They can assume any dummy value. 

 If IOPT='DAS=OFF', only solid lines are used. This is the default. 

 All solid lines: CALL CONOP4('DAS=OFF',' ',0,0) 

 To assign a specified line pattern to all contours: 

 CALL CONOP4('DAS=ALL',CHARS,0,0) 

 To assign a specified line pattern to selected contours: 

 Contour &gt; DBP: CALL CONOP4('DAS=GTR',CHARS,0,0) 

 Contour = DBP: CALL CONOP4('DAS=EQU',CHARS,0,0) 

 Contour &lt; DBP: CALL CONOP4('DAS=LSS',CHARS,0,0) 

 The breakpoint for changing the line pattern, parameter DBP, is set by a call to entry CONOP3. DBP = 0. is the default. See parameter DBP in &quot;man conop3&quot;. 

 If DAS has a value other than OFF, CHARS is a dashed line pattern described by a ten character string with a dollar sign ($) for solid and a single quote (') for blank. Recall that in FORTRAN 77, in a quoted string a single quote is represented by two single quotes (''). 

 Example: CALL CONOP4('DAS=GTR','$$$$$''$$$$',0,0)
<dt>FMT
<dd>A parameter which specifies a format for output of the data values. 

 If FMT=ON, the user must specify values for CHARS, NUMC, and IFMT. CHARS is an output print format. It has beginning and ending parenthesis as in (F8.2). NUMC is the number of characters in CHARS. It is 6 for (F8.2). IFMT is the maximum number of digits which can be printed by this format. It is 8 for an F8.2. 

 <pre>Example:
CHARS = '(F8.2)'
NUMC = 6
IFMT = 8
CALL CONOP4('FMT=ON',CHARS,NUMC,IFMT)</pre>Warning: IFMT cannot be greater than 10; however, CONRAN will not test for a valid format. Thus, a format which results in IFMT &gt; 10 will cause an undetected error. 

 If FMT=OFF, the default values are: CHARS='(G10.3)', NUMC=7, and IFMT=10, respectively. 

 To return to default settings use: 
 CALL CONOP4('FMT=OFF',' ',0,0)
<dt>TLE
<dd>The parameter to place a title at the top of the plot. CHARS contains the title, NUMC is the number of characters in the title and IFMT is not used. 

 Example: CALL CONOP4('TLE=ON','VECTOR REVIEW',13,0)</dl><h2>Usage</h2>CONOP4 is called to set parameters of type CHARACTER before entries CONRAN, CONRAS, or CONRAQ are called to generate the contour plots.
<h2>Examples</h2>Use the ncargex command to see pertinent examples tconaq, tconas and tconan.
<h2>Access</h2>To use CONOP4 load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the conran_family man page for a description of all Conran_family error messages and/or informational messages.
<h2>See Also</h2>Online: conran_family, conran_family_params, conran, conraq, conras, conop1, conop2, conop3, conpack, conpack_params Hardcopy: NCAR Graphics Contouring and Mapping Tutorial; NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
