---
title: "ncl_conop3(3)"
name: "ncl_conop3"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_conop3/"
---

CONOP3 - sets option switches and specifys various REAL parameters to be used by the Conran_family utility. 

<h2>Synopsis</h2>CALL CONOP3 (IOPT, ARRAY, LENA)
<h2>Description</h2><dl COMPACT><dt>IOPT
<dd>Character, input -- Selects an internal parameter and sets an option switch. The possibilities are: 

 <pre> 'CHL=ON' or 'CHL=OFF'
 'CIL=ON' or 'CIL=OFF'
 'CON=ON' or 'CON=OFF'
 'DBP=ON' or 'DBP=OFF'
 'SDC=ON' or 'SDC=OFF'
 'SLD=ON' or 'SLD=OFF'
 'TEN=ON' or 'TEN=OFF'</pre><dt>ARRAY
<dd>Real array, input -- Sets an internal parameter.
<dt>LENA
<dd>Integer, input -- The length of array ARRAY.
<dd>If an option is turned 'ON', then the remaining CONOP3 arguments can be used to override the default settings of that option. 

 If the option is 'OFF', then the remaining arguments of the CONOP3 call can be any dummy values. Option settings will be returned to their default values. 

 The following options are defined by this subroutine:
<dt>CHL
<dd>This parameter determines how the high and low contour values are set. These contour values may be set by the program or by the user. If CHL=OFF, the program examines the user's input data and determines both the high and low values. If CHL=ON, the user must specify the desired high (HI) and low (FLO) values. The default is CHL=OFF. 

 If program set: CALL CONOP3('CHL=OFF',0.,0) 

 If user set: CALL CONOP3('CHL=ON',ARRAY,2) where <a HREF="/docs/linux/man/1-array/">ARRAY</a>(1)=HI, <a HREF="/docs/linux/man/2-array/">ARRAY</a>(2)=FLO 

 Note: The values supplied for contour increment and contour high and low values assume unscaled data values. See the SDC parameter, below.
<dt>CIL
<dd>This parameter determines how the contour increment (CINC) is set. The increment is either calculated by the program (CIL=OFF) using the range of high and low values from the user's input data, or set by the user (CIL=ON). The default is CIL=OFF. 

 If program set: CALL CONOP3('CIL=OFF',0.,0) 

 If user set: CALL CONOP3('CIL=ON',CINC,1) 

 Note: By default, ('CIL=OFF') the program will examine the user's input data and determine the contour interval (CINC) at some appropriate range between the level of high and low values supplied, usually generating between 15 and 20 contour levels. 

 Example: CALL CONOP3('CIL=ON',10.,1) 
 will generate contours at increments of 10. units in user coordinates.
<dt>CON
<dd>This parameter determines how the contour levels are set. If CON=ON, the user must specify an array of contour values and the number of contour levels. A maximum of NCL=30 contour levels is permitted. If CON=OFF, NCL and the contour values are computed. The default is OFF. 

 If program set: CALL CONOP3('CON=OFF',0.,0) 

 If user set: CALL CONOP3('CON=ON',ARRAY,NCL) 

 Note: The real array (ARRAY) must have the contour levels ordered from smallest to largest. 

 Warning: It is illegal to use the CON option when either CIL or CHL are activated. If this is done, the option call that detected the error will not be executed.
<dt>DBP
<dd>This parameter determines how the dash pattern break point (BP) is set. (Does not apply to entry CONRAQ.) If DBP=ON, BP must be set by the user. If DBP=OFF, the program will set BP to 0. This is the default. 

 If program set: CALL CONOP3('DBP=OFF',0.,0) 

 If user set: CALL CONOP3('DBP=ON',BP,1) 

 Note: BP is a floating point number where the break for GTR and LSS contour dash patterns are defined. BP is assumed to be given relative to the untransformed contours. 

 To see how various dash line patterns can be assigned to various contours see parameter DBP in &quot;man conop4&quot;.
<dt>SDC
<dd>The parameter to determine how to scale the input data from which the contours are generated. (Does not apply to entry CONRAQ.) If SDC=ON, the scaling factor is set to <a HREF="/docs/linux/man/1-array/">ARRAY</a>(1). If SDC=OFF, the default scale factor of 1. is used. 

 If program set: CALL CONOP3('SDC=OFF',0.,0) 

 If user set: CALL CONOP3('SDC=ON',ARRAY,1) 

 Note: The data plotted on contour lines and the data plotted for relative minimums and maximums will be scaled by ARRAY.
<dt>SLD
<dd>Input a polygon to define the extent of area to be contoured. (Does not apply to entry CONRAQ.) When this option is activated, only those contours within the shield are drawn. The shield is a polygon specified by the user which must be given in the same coordinate range as the the data. It must define only one polygon. 

 To input a shield: 
&nbsp;<wbr>&nbsp;<wbr>CALL CONOP3('SLD=ON',ARRAY,LENA) 

 Otherwise: 
&nbsp;<wbr>&nbsp;<wbr>CALL CONOP3('SLD=OFF',0.,0) 

 Note: ARRAY is a real array LENA elements long. The first LENA/2 elements are X coordinates and the second LENA/2 elements are Y coordinates. This polygon must be closed, that is the first and last points in ARRAY must be the same. 

 <pre>Example:
 DIMENSION SHLD(10)
 DATA SHLD/ 7.,10.,10.,7.,7.,
1 7.,7.,10.,10.,7./
 CALL CONOP3 ('SLD=ON',SHLD,10)</pre><dt>TEN
<dd>The parameter to determine the tension factor applied when smoothing contour lines using splines under tension. (Does not apply to entry CONRAQ.) If user set, the allowed range is from greater than zero to 30. The higher the tension the less smoothing occurs. The default value (TEN=OFF) is 2.5. 

 If program set: CALL CONOP3('TEN=OFF',0.,0) 

 If user set: CALL CONOP3('TEN=ON',TENS,1) 

 Note: This option is not available in the standard version of CONRAN.</dl><h2>Usage</h2>CONOP3 is called to set parameters of type REAL before CONRAN, CONRAQ, or CONRAS are called to generate the contour plot.
<h2>Examples</h2>Use the command ncargex to see the following examples: tconaq, tconan, and tconas.
<h2>Access</h2>To use CONOP3 load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the conran_family man page for a description of all Conran_family error messages and/or informational messages.
<h2>See Also</h2>Online: conran_family, conran_family_params, conran, conraq, conras, conop1, conop2, conop4, conpack, conpack_params 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial; NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
