---
title: "ncl_softfill(3)"
name: "ncl_softfill"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_softfill/"
---

Softfill - Fills a polygonal subset of the plotter frame.

<h2>Synopsis</h2>

SFSGFA - Can be made to fill polygons by calling the GKS routine GFA or by calling the lower-level Softfill routines SFWRLD and SFNORM. 

 SFWRLD - Fills polygons with parallel lines or with dots, polymarkers, or selected characters arrayed in a regular rectangular pattern. 

 SFNORM - Fills polygons with parallel lines or with dots, polymarkers, or selected characters arrayed in a regular rectangular pattern. 

 SFGETC - Retrieves the current character value of a specified internal parameter. 

 SFGETI - Retrieves the current integer value of a specified internal parameter. 

 SFGETP - Retrieves the current value of the dot pattern. 

 SFGETR - Retrieves the current real value of a specified internal parameter. 

 SFSETC - Sets the new character value of a specified internal parameter. 

 SFSETI - Sets the new integer value of a specified internal parameter. 

 SFSETP - Sets the new value of the dot pattern. 

 SFSETR - Sets the new real value of a specified internal parameter.

<h2>C-Binding Synopsis</h2>

c_sfsgfa 
 c_sfwrld 
 c_sfnorm 
 c_sfgetc 
 c_sfgeti 
 c_sfgetp 
 c_sfgetr 
 c_sfsetc 
 c_sfseti 
 c_sfsetp 
 c_sfsetr

<h2>User-Modifiable Internal Routines</h2>

None

<h2>Messages</h2>

Various error conditions can occur in Softfill. Each of these results in a call to the error-handling routine SETER, with a final argument indicating that the error is recoverable; by default, an error message is printed and execution is terminated, but, if you turn on error recovery (as described in the &quot;man&quot; page for &quot;error_handling&quot;), you can get control back. 

 The error messages are as follows; all should be more or less self-explanatory. 

 SFGETC - PARAMETER NAME NOT KNOWN - X 
 SFGETC - PARAMETER NAME TOO SHORT - X 
 SFGETC - UNCLEARED PRIOR ERROR 
 SFGETI - UNCLEARED PRIOR ERROR 
 SFGETP - UNCLEARED PRIOR ERROR 
 SFGETR - PARAMETER NAME NOT KNOWN - X 
 SFGETR - PARAMETER NAME TOO SHORT - X 
 SFGETR - UNCLEARED PRIOR ERROR 
 SFNORM - ARRAY DST IS TOO SMALL 
 SFNORM - ARRAY IND IS TOO SMALL 
 SFNORM - COORDINATE ARRAYS TOO SMALL 
 SFNORM - LOGIC ERROR - SEE SPECIALIST 
 SFNORM - UNCLEARED PRIOR ERROR 
 SFSETC - PARAMETER NAME NOT KNOWN - X 
 SFSETC - PARAMETER NAME TOO SHORT - X 
 SFSETC - UNCLEARED PRIOR ERROR 
 SFSETI - UNCLEARED PRIOR ERROR 
 SFSETP - UNCLEARED PRIOR ERROR 
 SFSETR - PARAMETER NAME NOT KNOWN - X 
 SFSETR - PARAMETER NAME TOO SHORT - X 
 SFSETR - UNCLEARED PRIOR ERROR 
 SFSGFA - ERROR EXIT FROM GQFACI 
 SFSGFA - ERROR EXIT FROM GQPLCI 
 SFSGFA - UNCLEARED PRIOR ERROR 
 SFWRLD - UNCLEARED PRIOR ERROR 

 The &quot;LOGIC ERROR&quot; in SFNORM should never occur; if it does, it indicates a compiler problem or some sort of tampering with the code of the package. Error messages that complain of an error exit from a GKS routine probably imply that GKS has somehow been put in the wrong state. In the messages that result from using an incorrect internal-parameter name in a call to one of the parameter-access routines, the &quot;X&quot; will be replaced by the offending name.

<h2>See Also</h2>

Online: softfill_params, sfgetc, sfgeti, sfgetp, sfgetr, sfsetc, sfseti, sfsetp, sfsetr, sfsgfa, sfwrld, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
