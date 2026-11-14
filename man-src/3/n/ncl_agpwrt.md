---
title: "ncl_agpwrt(3)"
name: "ncl_agpwrt"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_agpwrt/"
---

AGPWRT - Provides a way for the user to change the style of all text strings drawn by Autograph. 

<h2>Synopsis</h2>SUBROUTINE AGPWRT (XPOS,YPOS,CHRS,NCHS,ISIZ,IORI,ICEN)
<h2>Description</h2><dl COMPACT><dt>XPOS
<dd>(an input expression of type REAL) is the X coordinate of a point relative to which the text string is to be positioned.
<dt>YPOS
<dd>(an input expression of type REAL) is the Y coordinate of a point relative to which the text string is to be positioned.
<dt>CHRS
<dd>(an input expression of type CHARACTER) is the text string to be drawn.
<dt>NCHS
<dd>(an input expression of type INTEGER) is the length of CHRS - the number of characters in the text string.
<dt>ISIZ
<dd>(an input expression of type INTEGER) specifies the size of the characters to be used. The values 0, 1, 2, and 3 imply character widths of 8, 12, 16, and 24 plotter units, respectively. Larger values specify the character width directly.
<dt>IORI
<dd>(an input expression of type INTEGER) is the orientation angle of the text string, measured in degrees counter-clockwise from a vector which is horizontal and pointing to the right.
<dt>ICEN
<dd>(an input expression of type INTEGER) is the centering option. The value &quot;-1&quot; implies that the text is to be written with (XPOS,YPOS) in the center of the left edge of the leftmost character, the value &quot;0&quot; that (XPOS,YPOS) is to be in the center of the entire string, and the value &quot;+1&quot; that (XPOS,YPOS) is to be in the center of the right edge of the rightmost character.</dl><h2>Usage</h2>This routine is not called by the user program, but by Autograph itself, to draw a numeric label or an informational label on the graph. The default version just calls the plot-package routine PWRIT. The user may supply a replacement version. 

 Note: A user version of AGPWRT should not call any other Autograph routine.
<h2>Access</h2>To use AGPWRT, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>See Also</h2>Online: autograph, agback, agbnch, agchax, agchcu, agchil, agchnl, agcurv, agdshn, aggetc, aggetf, aggeti, aggetp, aggetr, agrstr, agsave, agsetc, agsetf, agseti, agsetp, agsetr, agstup, agutol, anotat, displa, ezmxy, ezmy, ezxy, ezy 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
