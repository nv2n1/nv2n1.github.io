---
title: "ncl_labelbar(3)"
name: "ncl_labelbar"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_labelbar/"
---

Labelbar - Creates a labeled, filled, rectangular bar to serve as a key for a filled plot. 

<h2>Synopsis</h2>LBLBAR - Produces a complete label bar. 

 LBGETI - Retrieves current integer parameter values. 

 LBGETR - Retrieves current real parameter values. 

 LBSETI - Sets integer parameter values. 

 LBSETR - Sets real parameter values.
<h2>C-Binding Synopsis</h2>c_lblbar 
 c_lbgeti 
 c_lbgetr 
 c_lbfill 
 c_lbseti 
 c_lbsetr
<h2>User-Modifiable Internal Routines</h2>LBFILL - Fills label bars.
<h2>Access</h2>To use Labelbar routines, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.
<h2>Messages</h2>Various error conditions can occur in Labelbar. Each of these results in a call to the error-handling routine SETER, with a final argument indicating that the error is recoverable; by default, an error message is printed and execution is terminated, but, if you turn on error recovery (as described in the &quot;man&quot; page for &quot;error_handling&quot;), you can get control back. 

 The error messages are as follows; all should be more or less self-explanatory. 

 LBGETI - UNCLEARED PRIOR ERROR 
 LBGETR - PARAMETER NAME NOT KNOWN - X 
 LBGETR - PARAMETER NAME TOO SHORT - X 
 LBGETR - UNCLEARED PRIOR ERROR 
 LBLBAR - ERROR EXIT FROM GQFACI 
 LBLBAR - ERROR EXIT FROM GQLWSC 
 LBLBAR - ERROR EXIT FROM GQPLCI 
 LBLBAR - ERROR EXIT FROM GQTXCI 
 LBLBAR - UNCLEARED PRIOR ERROR 
 LBSETI - UNCLEARED PRIOR ERROR 
 LBSETR - PARAMETER NAME NOT KNOWN - X 
 LBSETR - PARAMETER NAME TOO SHORT - X 
 LBSETR - UNCLEARED PRIOR ERROR 

 All of these should be more or less self-explanatory. Those that complain of an error exit from a GKS routine probably imply that GKS has somehow been put in the wrong state. Others will result from using an incorrect internal-parameter name in a call to one of the parameter-access routines. (The &quot;X&quot; will be replaced by the offending name.)
<h2>See Also</h2>Online: labelbar_params, lbfill, lbgeti, lbgetr, lblbar, lbseti, lbsetr, ncarg_cbind 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
