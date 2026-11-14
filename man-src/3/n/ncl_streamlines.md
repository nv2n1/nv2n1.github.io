---
title: "ncl_streamlines(3)"
name: "ncl_streamlines"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_streamlines/"
---

Streamlines - Utility for plotting a streamline representation of field flow data given two arrays containing the vector field components on a uniform grid.

<h2>Synopsis</h2>

The following two calls are the minimum required to create a streamline field flow plot using the current interface:
<dl><dt>&bull;
<dd>STINIT - Performs initialization tasks required before STREAM may be called to create a streamline field flow plot. Information about the input data arrays is copied into internal common block variables and the coordinate system mappings and boundaries are established.
<dt>&bull;
<dd>STREAM - Plots a streamline representation of field flow data, based on conditions established by STINIT and the current values of a set of user-modifiable internal parameters associated with the Streamlines utility.</dl>
 

 All user-modifiable internal parameters have default values; only those which are to have values different from the default need to be set. The routines used to set Streamlines parameters are as follows:
<dl><dt>&bull;
<dd>STRSET - Resets all parameters to their initial default values.
<dt>&bull;
<dd>STSETI - Sets the value of an internal parameter of type INTEGER.
<dt>&bull;
<dd>STSETR - Sets the value of an internal parameter of type REAL.</dl>
 

 In general, once a parameter is given a value by a call to one of these routines, it retains that value until a similar call resets it. Retrieve the value of an internal parameter by calling one of the following routines:
<dl><dt>&bull;
<dd>STGETI - Gets the current value of an internal parameter of type INTEGER.
<dt>&bull;
<dd>STGETR - Gets the current value of an internal parameter of type REAL.</dl>
 

 Streamlines supports two obsolete routines for compatibility with old NCAR Graphics codes. The compatibility mode parameter, CPM, offers a number of options that allow considerable flexibility in making the transition to the new version of the utility. When writing new code you are encouraged not to use these entry points, since they provide less capability than the standard Streamlines interface, and may eventually be phased out.
<dl><dt>&bull;
<dd>STRMLN - The principal entry point prior to Version 3.2, now a front end to the STINIT/STREAM interface.
<dt>&bull;
<dd>EZSTRM - Front end to STRMLN: a simpler interface for standard situations, when detailed control of the plot is not required.</dl>

<h2>C-Binding Synopsis</h2>

c_stinit 
 c_stream 
 c_strset 
 c_stseti 
 c_stsetr 
 c_stgeti 
 c_stgetr 
 c_strmln 
 c_ezstrm

<h2>User-Modifiable Internal Routines</h2>

The following routines are not to be called directly. However, you may modify them in order to customize the behavior of Streamlines. Three routines (STUMXY, STUIXY, and STUMTA) are provided to support user-defined mapping transformations. The fourth (STUMSL) allows you to tailor streamline masking to your requirements.
<dl><dt>&bull;
<dd>STUIXY - User modifiable routine that inversely maps a single point on the streamline from user to data coordinate space.
<dt>&bull;
<dd>STUMSL - Default name for a user-definable external subroutine used to draw masked streamlines. The default version of the routine draws any polyline all of whose area identifiers are greater than or equal to zero.
<dt>&bull;
<dd>STUMTA - Given the coordinates of a point on the streamline in data, user, and NDC space, and the interpolated, normalized components of the vector at the point relative to data coordinate space, the user-modifiable routine STUMTA finds the directional angle of the streamline relative to NDC space at the point.
<dt>&bull;
<dd>STUMXY - User modifiable routine that maps a single point on the streamline from data to user coordinate space.</dl>

<h2>Access</h2>

To use Streamlines, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>Messages</h2>

In this section are listed, in alphabetical order, all the error messages that may be written by Streamlines. Each error message begins with the name of the Streamlines routine in which an error has been detected, followed by a dash, followed by the error message itself. These error messages are written by a call to the error-handling support routine SETER, with a final argument indicating that the error is fatal and that execution should be terminated.
<dl><dt>STGETI OR STGETR - PARAMETER NAME NOT KNOWN - x
<dd>The given parameter name ('x') is not a legal parameter name known to Streamlines.
<dt>STGETI OR STGETR - PARAMETER NAME TOO SHORT - x
<dd>The parameter name (&quot;x&quot;) is less than three characters long.
<dt>STINIT - U AND/OR V ARRAY DIMENSIONS EXCEEDED
<dd>The STINIT input argument, M, specifying the number of array elements to use along the first dimension of the U and V arrays, exceeds the actual first dimension of U and/or V, as specified by the input arguments LU and LV.
<dt>STREAM - TOO MANY AREA GROUPS
<dd>The area map passed as the argument, IAM, to STREAM contains more area groups than allowed by the Streamlines utility, currently 64. This error can occur only if the mask to area map parameter, MSK, has a value greater than 0, specifying that streamlines are to be drawn masked to an area map.
<dt>STREAM - INVALID AREA MAP
<dd>The area map passed as the argument, IAM, to STREAM is judged to be invalid because it contains a negative value for the number of area groups. This error can occur only if the mask to area map parameter, MSK, has a value greater than 0, specifying that streamlines are to be drawn masked to an area map.
<dt>STSETI OR STSETR - PARAMETER NAME NOT KNOWN - x
<dd>The given parameter name ('x') is not a legal parameter name known to Streamlines.
<dt>STSETI OR STSETR - PARAMETER NAME TOO SHORT - x
<dd>The parameter name (&quot;x&quot;) is less than three characters long.
<dt>STSETI OR STSETR - PARAMETER VALUE OUT OF RANGE - x
<dd>An attempt has been made to set the parameter named 'x' to a value outside the range allowed by the Streamlines utility.</dl>

<h2>See Also</h2>

Online: stgetc, stgeti, stgetr, stinit, stream, streamlines_params, strset, stsetc, stseti, stsetr, stuixy, stumsl, stumta, stumxy, ncarg_cbind. 

 Hardcopy: NCAR Graphics Fundamentals, UNIX Version

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 The use of this Software is governed by a License Agreement.
