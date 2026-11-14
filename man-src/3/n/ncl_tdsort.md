---
title: "ncl_tdsort(3)"
name: "ncl_tdsort"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_tdsort/"
---

TDSORT - A generic sorting routine, normally used indirectly (by calling the routine TDOTRI).

<h2>Synopsis</h2>

CALL TDSORT (RWRK, NRWK, IORD, IWRK)

<h2>C-Binding Synopsis</h2>

#include &lt;ncarg/ncargC.h&gt; 

 void c_tdsort(float *rwrk, int nwrk, int iord, int *iwrk)

<h2>Description</h2>

This is an internal routine used for sorting. Originally, it was not intended that a user should call this routine directly, but doing so will do no harm. Given an array of NRWK reals in an array RWRK and an &quot;ordering flag&quot; IORD, TDSORT returns a permutation vector IWRK such that, for every I and J such that 1.LE.I.LE.J.LE.NWRK, if IORD is zero, then RWRK(IWRK(I)).LE.RWRK(IWRK(J)), else RWRK(IWRK(I)).GE.RWRK(IWRK(J)). 

 The arguments of TDSORT are as follows:
<dl><dt>RWRK
<dd>(an input array, of type REAL, dimensioned NWRK) - an array of NWRK real numbers that are to be sorted. The contents of RWRK are returned unchanged; the ordering is as specified by the contents of the array IWRK.
<dt>NWRK
<dd>(an input expression of type INTEGER) - the dimension of RWRK (and of IWRK).
<dt>IORD
<dd>(an input expression of type INTEGER) - if IORD is zero, the desired ordering is from smallest numeric value to largest; otherwise, the desired ordering is from largest value to smallest.
<dt>IWRK
<dd>(an output array of type INTEGER, dimensioned at least NWRK) - returned containing a permutation of the integers from 1 to NWRK.</dl>

<h2>C-Binding Description</h2>

The C-binding argument descriptions are the same as the FORTRAN argument descriptions.

<h2>Access</h2>

To use TDSORT or c_tdsort, load the NCAR Graphics libraries ncarg, ncarg_gks, and ncarg_c, preferably in that order.

<h2>See Also</h2>

Online: tdclrs, tdctri, tddtri, tdgeti, tdgetr, tdgrds, tdgrid, tdgtrs, tdinit, tditri, tdlbla, tdlbls, tdline, tdlnpa, tdmtri, tdotri, tdpack, tdpack_params, tdpara, tdplch, tdprpa, tdprpi, tdprpt, tdseti, tdsetr, tdstri, tdstrs

<h2>Copyright</h2>

Copyright (C) 1987-2009 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
