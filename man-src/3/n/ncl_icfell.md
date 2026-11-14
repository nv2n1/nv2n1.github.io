---
title: "ncl_icfell(3)"
name: "ncl_icfell"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_icfell/"
---

ICFELL - Called to check for existing error conditions and (perhaps) to update the current error message and error flag. 

<h2>Synopsis</h2>NERR = ICFELL(MESSG,NERRF)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 int c_icfell(char *messg, int nerrf)
<h2>Description</h2>ICFELL (which stands for &quot;I Check For Errors on Lower Level&quot;) is used to check for the occurrence of a recoverable error in a lower-level routine and (perhaps) to update the current internal error message and error flag. 

 The old value of the error flag is returned as the value of the function ICFELL. If that value is zero, nothing else has been done. If the value of ICFELL is non-zero, the following actions have been taken:
<dl COMPACT><dt> -
<dd>If MESSG is blank, the current error message has not been changed.
<dt> -
<dd>If MESSG is non-blank and its length is 6 or less, it should be the name of the routine referencing ICFELL; the current error message has been altered by prepending first a slash and then MESSG. (Note that, if an error occurs several levels deep, the effect of using ICFELL in this manner at each level is, effectively, to generate traceback information in the error message.)
<dt> -
<dd>If MESSG is non-blank and its length is 7 or greater, its value has become the new value of the current error message and the previous error message has been printed. This is intended for use at the beginning of an NCAR Graphics routine to check for an outstanding error that the user has not recovered from and to ensure that the message for the outstanding error gets printed.
<dt> -
<dd>If the expression NERRF has the value zero, the current error flag has not been changed.
<dt> -
<dd>If the expression NERRF has a non-zero value, the value of the current error flag has been made equal to that value.</dl>
 

 An example: Assume that the routine &quot;A&quot; calls the routine &quot;B&quot; and that &quot;B&quot; detects an error and calls SETER with error number &quot;32&quot; and error message &quot;B - ERROR HAS OCCURRED&quot;. If recovery mode is not in effect, SETER prints the error message and STOPs; if recovery mode is in effect, control returns from &quot;SETER&quot; to &quot;B&quot; and thence to &quot;A&quot;. At that point, the statement &quot;IF (ICFELL('A',13).NE.0) RETURN&quot; detects the fact that an error has occurred in &quot;B&quot; and results in a return from &quot;A&quot; to whatever routine called it. It also changes the current error message to read 'A/B - ERROR HAS OCCURRED' and changes the error number from &quot;32&quot; to &quot;13&quot;. 

 Another example: Assume that the NCAR Graphics routine &quot;A&quot; is called when recovery mode is set and that it detects an error, calls SETER, and RETURNs to the user. If the user neglects to check the error state and calls the routine &quot;B&quot; next, the statement &quot;IF (ICFELL('B - UNCLEARED PRIOR ERROR',1).NE.0) RETURN&quot; ensures that the error message from routine &quot;A&quot; will be printed, that it will be replaced by an error message referring to the routine &quot;B&quot;, and that &quot;B&quot; won't do anything else. 

 The arguments of ICFELL are as follows: 

<dl COMPACT><dt>MESSG
<dd>(an input variable or constant of type CHARACTER) - A character string saying what is to be done to the current error message (when an error has occurred). If MESSG is blank, no change is to be made in the current error message. If the length of MESSG is six characters or fewer, a slash is prepended to the current error message and then MESSG is prepended to that. If the length of MESSG is seven characters or more, MESSG is a complete new error message to be substituted for the current one; it should be of the form &quot;XXXXXX - TEXT DESCRIBING THE ERROR&quot;, where &quot;XXXXXX&quot; is the name of the routine in which the error occurred, and it should not be more than 113 characters long.
<dt>NERRF
<dd>(an input expression of type INTEGER) - A value in the range from -999 to +9999. If this value is zero, no change is made in the internal error flag; otherwise, it is the desired new value of that flag (when an error has occurred).</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: tseter, arex02.
<h2>Access</h2>To use ICFELL or c_icfell, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: entsr, eprin, errof, error_handling, fdum, icloem, nerro, retsr, semess, seter, ncarg_cbind
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
