---
title: "ncl_agutol(3)"
name: "ncl_agutol"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_agutol/"
---

AGUTOL - Provides a way for the user to change the user-system-to-label-system mapping for one or more of the four axes. 

<h2>Synopsis</h2>SUBROUTINE AGUTOL (IAXS,FUNS,IDMA,VINP,VOTP)
<h2>Description</h2><dl COMPACT><dt>IAXS
<dd>(an input expression of type INTEGER) is the number of the axis. The values 1, 2, 3, and 4 imply the left, right, bottom, and top axes, respectively.
<dt>FUNS
<dd>(an input expression of type REAL) is the value of 'AXIS/s/FUNCTION.', which may be used to select the desired mapping function for the axis IAXS. It is recommended that the default value (zero) be used to specify the identity mapping. The value may be integral (&quot;1.&quot;, &quot;2.&quot;, etc.) and serve purely to select the code to be executed or it may be the value of an actual parameter in the equations defining the mapping.
<dt>IDMA
<dd>(an input expression of type INTEGER) specifies the direction of the mapping. A value greater than zero indicates that VINP is a value in the user system and that VOTP is to be a value in the label system, a value less than zero the opposite. The mappings in one direction must be the mathematical inverses of the mappings in the other direction.
<dt>VINP
<dd>(an input expression of type REAL) is an input value in one coordinate system.
<dt>VOTP
<dd>(an output variable of type REAL) is an output value in the other coordinate system.</dl><h2>Usage</h2>This routine is not called by the user program, but by Autograph itself. It defines the user-system-to-label-system mapping for all four axes. The default version makes the label system match the user system on all four axes. The user may supply his own version of this routine to change the mapping on one or more of the axes. Mappings defined by the subroutine must be continuous and monotonic. 

 Note: A user version of AGUTOL should not call any other Autograph routine.
<h2>Access</h2>To use AGUTOL, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: autograph, agback, agbnch, agchax, agchcu, agchil, agchnl, agcurv, agdshn, aggetc, aggetf, aggeti, aggetp, aggetr, agpwrt, agrstr, agsave, agsetc, agsetf, agseti, agsetp, agsetr, agstup, anotat, displa, ezmxy, ezmy, ezxy, ezy 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
