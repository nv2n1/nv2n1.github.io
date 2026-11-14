---
title: "ncl_fdum(3)"
name: "ncl_fdum"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_fdum/"
---

FDUM - A routine called when fatal errors occur. 

<h2>Synopsis</h2>CALL FDUM
<h2>Description</h2>This routine is not intended to be called by the user. It is called by SETER when a fatal error is being processed and a STOP is about to be executed. The default version of FDUM does nothing. A user-supplied replacement version may take some other (system-dependent or program-dependent) action which would be helpful in diagnosing what may have caused the error to occur. 

 FDUM has no arguments.
<h2>Examples</h2>Use the ncargex command to see the following relevant examples: tseter, arex02.
<h2>Access</h2>To use FDUM, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: entsr, eprin, errof, error_handling, icfell, icloem, nerro, retsr, semess, seter, ncarg_cbind
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
