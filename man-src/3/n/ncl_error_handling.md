---
title: "ncl_error_handling(3)"
name: "ncl_error_handling"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_error_handling/"
---

Error_handling - A set of routines for error handling in NCAR Graphics. 

<h2>Synopsis</h2>ENTSR - Enters recovery mode. 
 EPRIN - Prints the current error message. 
 ERROF - Turns off the internal error flag. 
 FDUM - A dump routine - the default version just RETURNS. 
 ICFELL - Checks for an outstanding error condition. 
 ICLOEM - Computes the real length of its character-string argument (ignoring blanks on the end) 
 NERRO - Gets the current value of the internal error flag. 
 RETSR - Restores a previous value of the internal error flag. 
 SEMESS - Gets a specified portion of the current error message. 
 SETER - Called by NCAR Graphics routines to report error conditions.
<h2>C-Binding Synopsis</h2>#include &lt;ncarg/ncargC.h&gt; 

 c_entsr 
 c_eprin 
 c_errof 
 c_icfell 
 c_icloem 
 c_nerro 
 c_retsr 
 c_semess 
 c_seter 

<h2>Using Seter In Ncar Graphics</h2>There are specific conventions for the use of SETER within NCAR Graphics, as follows:
<dl COMPACT><dt> -
<dd>All detectable errors shall be recoverable, in the sense described above. (That is, in every call to SETER, the final argument shall be a 1, rather than a 2.) This is by request of the folks doing NCAR Interactive, who rightly consider STOPs in the utilities undesirable. The idea is to let the user decide what is to be done about the various error conditions.
<dt> -
<dd>Whenever an NCAR Graphics routine calls a lower-level routine that might detect an error and call SETER, it should subsequently use ICFELL to check the error state; if a recoverable error has occurred, it should first do required clean-up chores, if possible, and then pass control back to the routine that called it. In all such uses of ICFELL, the first argument should be the name of the routine referencing ICFELL and the second argument should be a new number for the error, reflecting the position of the reference to the lower-level routine in the upper-level routine.
<dt> -
<dd>Any NCAR Graphics routine that can be called by a user and that can potentially yield a call to SETER must immediately check the error state and, if that error state is non-zero, return control without doing anything else. This is most conveniently done using a reference to ICFELL; see the second example in the &quot;Usage&quot; section of the description of ICFELL. All such references should have a first argument of the form 'XXXXXX - UNCLEARED PRIOR ERROR', where &quot;XXXXXX&quot; is the name of the routine in which the reference occurs, and a second argument equal to &quot;1&quot;.
<dt> -
<dd>It is recommended that, within a given utility routine, the error numbers in references to SETER and ICFELL should start at 1 and increment by 1. These numbers generally have no intrinsic meaning in and of themselves: they are merely intended to allow a consultant to find the reference that generated a given error.
<dt> -
<dd>NCAR Graphics routines are not required to turn recovery mode on before calling a lower-level routine that might call SETER (which was the convention in the PORT library, as described in the PORT document). Instead, the assumption is that it is the responsibility of the user of NCAR Graphics to set recovery mode if he/she desires to do recovery. Since, by default, recovery mode is turned off, all NCAR Graphics calls to SETER will be treated as fatal: the error message will be printed and execution will be terminated. Once the user turns recovery mode on, however, no NCAR Graphics error will be treated in this way except for one that the user fails to recover from.</dl>
 

 Note: These conventions are being adopted as of December 2, 1993, and represent a goal for the future. The current situation is somewhat muddled: In some utilities, all SETER calls are fatal ones. In other utilities, some SETER calls are fatal and some are not. In other utilities, no SETER calls are fatal. In general, errors at a lower level are not detected and passed back up the call chain. Users have complained (and rightly so) that error recovery is, in general, not possible; observance of these conventions should help to fix the situation. 

 Further note: As of March 30, 1994, the situation has improved markedly. CONPACK and all utilities referenced by it have been updated to follow the guidelines given above and work is proceeding on other utilities. 

 There is one sticky area in which questions remains to be answered: Sometimes, when an error condition occurs during execution of a utility routine that has changed the internal state of GKS or SPPS, it has not been possible to restore the state of those packages to exactly what it was before that routine was entered. In some cases, better bookkeeping would allow restoration to be done; in other cases, though, restoration would involve calling a routine that could generate a call to SETER, which would cause a STOP. In the latter cases, I have not yet worked out a good solution. For the moment, therefore, the situation is this: if you call an NCAR Graphics utility with recovery mode turned on and, when you get control back, you find that an error has occurred, you must be prepared to deal with the possibility that at least the following things might been changed: 1) the current SET call; 2) the current polyline color index; 3) the current polymarker color index; 4) the current text color index; 5) the current fill area color index; 6) the current dash pattern.
<h2>Access</h2>To use the Error_handling C or Fortran routines, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order. 

<h2>See Also</h2>Online: entsr, eprin, errof, fdum, icfell, icloem, nerro, retsr, semess, seter, ncarg_cbind
<h2>Copyright</h2>Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
