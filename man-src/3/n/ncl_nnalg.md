---
title: "ncl_nnalg(3)"
name: "ncl_nnalg"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ncl_nnalg/"
---

nnalg - a tool for displaying features of the Natgrid algorithm

<h2>Synopsis</h2>

nnalg algorithmic_data_file

<h2>Description</h2>

&quot;nnalg&quot; takes a single argument which is a the name of a special file created by the Fortran subroutine NATGRIDS or the C function c_natgrids in the Natgrid package. This file contains data appropriate for displaying various features of the Natgrid algorithm. By default, this file is not created. In order to create it, you need to set the parameter adf in the Natgrid package. You can additionally override the default file name of &quot;nnalg.dat&quot; by using the parameter alg. 

 To invoke &quot;nnalg&quot;, simply type the command: 

 nnalg data_file 

 By editing the data file, you have many options as to what is displayed and what the appearance of the plot looks like. 

 The features that can be displayed are: 

 
&nbsp;<wbr>&nbsp;<wbr>1. The input data points&nbsp;<wbr> 
 
&nbsp;<wbr>&nbsp;<wbr>2. The natural neighbor circumcircles&nbsp;<wbr> 
 
&nbsp;<wbr>&nbsp;<wbr>3. The Delaunay triangulation, derived from the natural 
&nbsp;<wbr>&nbsp;<wbr>neighbor circumcircles&nbsp;<wbr> 
&nbsp;<wbr>&nbsp;<wbr>4. The Voronoi polygons&nbsp;<wbr> 
 
&nbsp;<wbr>&nbsp;<wbr>5. The first order natural neighbors of a given&nbsp;<wbr> 
&nbsp;<wbr>&nbsp;<wbr>input point&nbsp;<wbr>(or points)&nbsp;<wbr> 
 
&nbsp;<wbr>&nbsp;<wbr>6. The second order natural neighbors of a given input 
&nbsp;<wbr>&nbsp;<wbr>point&nbsp;<wbr>(or points)&nbsp;<wbr> 

 The first four items in the above list are displayed in the default case.

<h2>Usage</h2>

What gets displayed by nnalg depends on values in the input data file which can be changed by manual editing.

<h2>See Also</h2>

natgrid 

 Complete documentation for nnalg is available at URL 
 <a rel="nofollow" HREF="http://ngwww.ucar.edu/ngdoc/ng/ngmath/natgrid/algorithm.html">http://ngwww.ucar.edu/ngdoc/ng/ngmath/natgrid/algorithm.html</a>

<h2>Copyright</h2>

Copyright (C) 2000 
 University Corporation for Atmospheric Research 
 

 The use of this Software is governed by a License Agreement.
