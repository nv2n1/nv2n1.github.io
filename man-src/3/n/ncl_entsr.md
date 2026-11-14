---
title: "ncl_entsr(3)"
name: "ncl_entsr"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_entsr/"
---

ENTSR - Called by a user to set recovery mode in NCAR Graphics. 

<h2>Synopsis</h2>CALL ENTSR(IROLD,IRNEW)
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 void c_entsr(int *irold, int irnew)
<h2>Description</h2>The FORTRAN statement &quot;CALL ENTSR(IROLD,IRNEW)&quot; is normally used to enter recovery mode and save the previous value of the internal error-recovery flag, but it can also be used to exit from recovery mode and save the previous value of the flag, or to just get the value of the flag, without changing it. 

 If recovery mode is turned off by a call to ENTSR at a time when the internal error flag is non-zero, this is treated as a fatal error; the error message is printed, the dump routine FDUM is called, and a STOP is executed. 

 The arguments of ENTSR are as follows: 

<dl COMPACT><dt>IROLD
<dd>(an output variable of type INTEGER) - Receives the old value of the internal flag that indicates whether recovery mode is in effect or not. In the former case, the returned value will be a 1; in the latter case, it will be a 2. Normally, the value returned is saved for a later call to RETSR. 

<dt>IRNEW
<dd>(an input expression of type INTEGER) - Specifies what is to be done to the internal flag that indicates whether recovery mode is in effect or not. If IRNEW is a 1 or a 2, it becomes the new value of the internal recovery-mode flag: the value 1 turns recovery mode on and the value 2 turns it off. Other non-zero values are illegal, but, if IRNEW is zero, the state of the internal recovery-mode flag is not changed.</dl><h2>C-Binding Description</h2>The C-binding argument descriptions are the same as the FORTRAN argument descriptions.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: tseter, arex02.
<h2>Access</h2>To use ENTSR or c_entsr, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: eprin, errof, error_handling, fdum, icfell, icloem, nerro, retsr, semess, seter, ncarg_cbind
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
