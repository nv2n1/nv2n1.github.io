---
title: "ncl_ngmisc(3)"
name: "ncl_ngmisc"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_ngmisc/"
---

Ngmisc - A collection of miscellaneous NCAR Graphics routines.

<h2>Synopsis</h2>

NGDOTS - Draws filled circular dots at coordinate positions (X(I),Y(I),I=1,NUM) at size SIZE with color given by the color index ICOLOR. 

 NGGCOG - Returns the latitudes and longitudes of a set of points approximating a circle at a given point on the surface of the globe. 

 NGGETC - Retrieves values for character-valued parameters set by NGSETC. 

 NGGETI - Retrieves values for integer-valued parameters set by NGSETI. 

 NGGETR - Retrieves values for real-valued parameters set by NGSETR. 

 NGSETC - Sets values for character-valued parameters. 

 NGSETI - Sets values for integer-valued parameters. 

 NGSETR - Sets values for real-valued parameters. 

 NGGSOG - Returns the latitudes and longitudes of six points defining a five-pointed star at a given point on the surface of the globe. 

 NGPICT - Effects a break in the picture drawing sequence in a FORTRAN code using NCAR GKS. The actions taken depend on whether the designated workstation is a metafile or an output/input workstation. An option is provided for prompting the user when an output/input workstation is ready and waiting after a pause. 

 NGPSWK - Returns an integer workstation type for NCAR GKS PostScript workstation types. 

 NGRITD - Given the coordinates of a point, this routine performs a rotation of that point about a specified axis by a specified angle. 

 NGWSYM - Draws a symbol from the standard WMO/NOAA meteorological fonts by reference to the font name and symbol number within that font.

<h2>C-Binding Synopsis</h2>

c_ngdots 
 c_nggetc 
 c_nggeti 
 c_nggetr 
 c_nggcog 
 c_nggsog 
 c_ngpict 
 c_ngpswk 
 c_ngritd 
 c_ngsetc 
 c_ngseti 
 c_ngsetr 
 c_ngwsym

<h2>User-Modifiable Internal Routines</h2>

None.

<h2>Access</h2>

To use Ngmisc routines, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: NGDOTS(3NCARG), NGSETC(3NCARG), NGSETI(3NCARG), NGSETR(3NCARG), NGGCOG(3NCARG), NGGETC(3NCARG), NGGETI(3NCARG), NGGETR(3NCARG), NGGSOG(3NCARG), NGMISC_PARAMS(3NCARG), NGPICT(3NCARG), NGPSWK(3NCARG), NGRITD(3NCARG), NGWSYM(3NCARG)

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
