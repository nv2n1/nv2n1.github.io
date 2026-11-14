---
title: "ncl_agchil(3)"
name: "ncl_agchil"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_agchil/"
---

AGCHIL - Provides a way for the user to change the color, intensity, text style, etc., of the informational labels. 

<h2>Synopsis</h2>SUBROUTINE AGCHIL (IFLG,LBNM,LNNO)
<h2>Description</h2><dl COMPACT><dt>IFLG
<dd>(an input expression of type INTEGER) is zero if a particular object is about to be drawn, non-zero if it has just been drawn.
<dt>LBNM
<dd>(an input expression of type CHARACTER) is the name of the label being drawn.
<dt>LNNO
<dd>(an input expression of type INTEGER) is the number of the line being drawn.</dl><h2>Usage</h2>This routine is not called by the user program, but by Autograph itself, just before and just after each informational-label line is drawn. The default version does nothing. The user may supply his own version to change the appearance of selected lines of text. 

 Note: A user version of AGCHIL should not call any other Autograph routine.
<h2>Access</h2>To use AGCHIL, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: autograph, agback, agbnch, agchax, agchcu, agchnl, agcurv, agdshn, aggetc, aggetf, aggeti, aggetp, aggetr, agpwrt, agrstr, agsave, agsetc, agsetf, agseti, agsetp, agsetr, agstup, agutol, anotat, displa, ezmxy, ezmy, ezxy, ezy 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
