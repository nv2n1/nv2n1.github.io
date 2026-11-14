---
title: "ncl_seter(3)"
name: "ncl_seter"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_seter/"
---

SETER - Called by NCAR Graphics routines when errors occur.

<h2>Synopsis</h2>

CALL SETER(MESSG,NERRF,ILEVL)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_seter(char *messg, int nerrf, int ilevl)

<h2>Description</h2>

The FORTRAN statement &quot;CALL SETER (MESSG,NERRF,ILEVL) is used to tell the error-handling package that an error has occurred. Exactly what happens as a result of such a call depends not only on the values of the arguments, but on the settings of two internal variables: the error flag, which says whether or not there was a prior error, and the recovery-mode flag, which says whether or not recovery mode is in effect.
<dl><dt> -
<dd>If the internal error flag is 0 (no prior error) and the internal recovery-mode flag is 2 (recovery mode not set, which is the default), SETER prints the error message MESSG, calls FDUM if and only if ILEVL = 2, and then STOPs.
<dt> -
<dd>If the internal error flag is 0 (no prior error) and the internal recovery-mode flag is 1 (recovery mode set), then what happens depends on the value of ILEVL: if ILEVL = 2 (fatal error), SETER prints the error message MESSG, calls FDUM, and STOPs, but, if ILEVL = 1 (recoverable error), SETER resets the internal error flag equal to NERRF, remembers the error message MESSG, and RETURNs. In the latter case, the user is expected to detect the fact that an error has occurred, take the necessary remedial action, and call ERROF to turn the internal error flag off.
<dt> -
<dd>If the internal error flag is non-zero (prior error), then the value of the internal recovery-mode flag will be 1 (recovery mode set); in this case, it doesn't make any difference what the value of ILEVL is: SETER prints both the remembered error message from the prior error and the new error message from MESSG, calls FDUM, and STOPs.</dl>
 

 The arguments of SETER are as follows: 

<dl><dt>MESSG
<dd>(an input variable or constant of type CHARACTER) is an error message describing the error that has occurred. This should be of the form &quot;XXXXXX - TEXT DESCRIBING THE ERROR&quot;, where &quot;XXXXXX&quot; is the name of the routine in which the error occurred, and it should not be more than 113 characters long.
<dt>NERRF
<dd>(an input expression of type INTEGER) is a non-zero error number in the range from -999 to +9999.
<dt>ILEVL
<dd>(an input expression of type INTEGER) is the &quot;error level&quot; - either a 1 or a 2, implying that the error described by MESSG and NERRF is recoverable or fatal, respectively.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Examples</h2>

Use the ncargex command to see the following relevant examples: tseter, arex02.

<h2>Access</h2>

To use SETER or c_seter, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: entsr, eprin, errof, error_handling, fdum, icfell, icloem, nerro, retsr, semess, ncarg_cbind

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
