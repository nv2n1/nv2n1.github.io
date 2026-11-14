---
title: "ncl_conop2(3)"
name: "ncl_conop2"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_conop2/"
---

CONOP2 - sets option switches and specifys various INTEGER parameters to be used by the Conran_family utility. 

<h2>Synopsis</h2>CALL CONOP2 (IOPT, IVAL)
<h2>Description</h2><dl COMPACT><dt>IOPT
<dd>Character, input -- Selects an internal parameter and sets an option switch. The possibilities are: 

 <pre> 'INT=OFF', 'INT=ALL', 'INT=MAJ', 'INT=MIN', 'INT=LAB', 'INT=DAT'
 'LSZ=ON' or 'LSZ=OFF'
 'NCP=ON' or 'NCP=OFF'
 'SML=ON' or 'SML=OFF'
 'SPD=ON' or 'SPD=OFF'
 'SSZ=ON' or 'SSZ=OFF'
 'STL=ON' or 'STL=OFF'</pre><dt>IVAL
<dd>Integer, input -- Sets an internal parameter. 

 If IOPT is not 'OFF', then the IVAL argument is used to override the default setting of that option. 

 If IOPT is 'OFF', the IVAL argument can have any dummy value. Option settings will be returned to their default values. 

 The following options are defined by this subroutine:
<dt>INT
<dd>The parameter to determine the intensities of the contour lines and other parts of the plot. If INT=OFF, all intensities are set to the default values. If INT=ALL, all intensities are set to IVAL. If INT is set to one of the other possible options (MAJ, MIN, LAB or DAT), the intensity level for that option is set to IVAL. 

 If program set: CALL CONOP2('INT=OFF',0) 

 All the same: CALL CONOP2('INT=ALL',IVAL) 

 Major lines: CALL CONOP2('INT=MAJ',IVAL) 

 Minor lines: CALL CONOP2('INT=MIN',IVAL) 

 Title and message: CALL CONOP2('INT=LAB',IVAL) 

 Data values: CALL CONOP2('INT=DAT',IVAL) 

 Note: 'INT=DAT' relates to the plotted data values and the plotted maximums and minimums. 

 Note: IVAL is the intensity desired. IVAL values range from 0 to 255. 

 Example: CALL CONOP2('INT=ALL',110)
<dt>LSZ
<dd>This parameter determines the label size. (Does not apply to entry CONRAQ.) The value of LSZ is the desired length in NDCs multiplied by 1023. If LSZ=ON, the label size is set to IVAL. If LSZ=OFF, the default label size is 9./1023. NDCs. 

 Example: CALL CONOP2('LSZ=ON',12)
<dt>NCP
<dd>The parameter to indicate the number of data points used for the partial derivative estimation. If NCP=OFF, IVAL is set to 4, which is the default value. If NCP=ON, the user must specify IVAL greater than or equal to 2. 

 Example: CALL CONOP2('NCP=ON',2) 

 Note: IVAL = number of data points used for estimation. Changing this value affects the contours produced and the size of input array IWK.
<dt>SML
<dd>The parameter to determine the size of minimum and maximum contour labels in integer scaled NDC units. (Does not apply to entry CONRAQ.) The value of SML is the desired length in NDCs multiplied by 1023. If SML=OFF, the default label size is 15./1023. NDCs. If SML=ON, the user must specify IVAL. 

 Example: CALL CONOP2('SML=ON',12)
<dt>SPD
<dd>The parameter for the size of the plotted input data values in integer scaled NDC units. If SPD=OFF, the default label size is 8./1023. NDCs. If SPD=ON, the user must specify IVAL. 

 Example: CALL CONOP2('SPD=ON',12)
<dt>SSZ
<dd>The parameter to determine the resolution (number of steps in each direction). If SSZ=ON, the user sets IVAL, or, if SSZ=OFF, the program will automatically set IVAL to the default value of 40. 

 Warning: The scratch array (7th argument in the CONRAN call) must be dimensioned IVAL**2 or larger. 

 <pre>Example:
 DIMENSION SCR(10000)
 CALL CONOP2('SSZ=ON',100)
 CALL CONRAN(XD,YD,ZD,NDP,WK,IWK,SCR)</pre>Note: IVAL is an integer specifying the density of the virtual grid. In most cases, the default value of 40 produces pleasing contours. For coarser but quicker contours, lower the value. For smoother contours at the expense of taking a longer time, raise the value. 

 Warning: For step sizes greater than 200 in CONRAN, the arrays PV in common block CONRA1 and ITLOC in common block CONRA9, must be expanded to about 10 more than IVAL.
<dt>STL
<dd>The parameter to determine the character size of the main title in integer scaled NDC units. If STL=OFF, the default label size is 16./1023. NDCs. If STL=ON, the user must specify IVAL. 

 Example: CALL CONOP2('STL=ON',14) 

 Note: When 30 or 40 characters are used for the title, the default size of 16 integer scaled NDC units works well. For longer titles, a smaller title size is required.</dl><h2>Usage</h2>CONOP2 is called to set parameters of type INTEGER before CONRAN, CONRAQ, or CONRAS are called to generate the contour plot.
<h2>Examples</h2>Use the command ncargex to see the following examples: tconaq, tconan, and tconas.
<h2>Access</h2>To use CONOP2 load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>See the conran_family man page for a description of all Conran_family error messages and/or informational messages.
<h2>See Also</h2>Online: conran_family, conran_family_params, conran, conraq, conras, conop1, conop3, conop4, conpack, conpack_params 

 Hardcopy: NCAR Graphics Contouring and Mapping Tutorial; NCAR Graphics Fundamentals, UNIX Version; User's Guide for NCAR GKS-0A Graphics
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
