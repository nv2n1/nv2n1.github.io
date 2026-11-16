---
title: "ncl_agchax(3)"
name: "ncl_agchax"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_agchax/"
---

AGCHAX - Provides a way for the user to change the color, intensity, line style, etc., of various portions of the axes. 

<h2>Synopsis</h2>SUBROUTINE AGCHAX (IFLG,IAXS,IPRT,VILS)
<h2>Description</h2><dl COMPACT><dt>IFLG
</dt><dd>(an input expression of type INTEGER) is zero if a particular object is about to be drawn, non-zero if it has just been drawn.
</dd><dt>IAXS
</dt><dd>(an input expression of type INTEGER) is the number of the axis being drawn. The values 1, 2, 3, and 4 indicate the left, right, bottom, and top axes, respectively.
</dd><dt>IPRT
</dt><dd>(an input expression of type INTEGER) indicates the part of the axis being drawn. Possible values are as follows:
</dd><dl COMPACT><dd></dd><dl COMPACT><dt>&bull;
</dt><dd>1 implies the line of the axis.
</dd><dt>&bull;
</dt><dd>2 implies a major tick
</dd><dt>&bull;
</dt><dd>3 implies a minor tick.
</dd><dt>&bull;
</dt><dd>4 implies the mantissa of a numeric label.
</dd><dt>&bull;
</dt><dd>5 implies the exponent of a numeric label.</dd></dl></dl><dt>VILS
</dt><dd>(an input expression of type REAL) is the value in the label system at the point where the part is being drawn. For IPRT = 1, VILS is zero.</dd></dl><h2>Usage</h2>This routine is not called by the user program, but by Autograph itself, just before and just after each of the objects making up an axis is drawn. The default version does nothing. The user may supply his own version to change the color, intensity, line style, etc. of selected portions of the axis. 

 Note: A user version of AGCHAX should not call any other Autograph routine.
<h2>Access</h2>To use AGCHAX, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: autograph, agback, agbnch, agchcu, agchil, agchnl, agcurv, agdshn, aggetc, aggetf, aggeti, aggetp, aggetr, agpwrt, agrstr, agsave, agsetc, agsetf, agseti, agsetp, agsetr, agstup, agutol, anotat, displa, ezmxy, ezmy, ezxy, ezy 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
