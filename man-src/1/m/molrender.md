---
title: "molrender(1)"
name: "molrender"
section: "1"
letter: "m"
url: "/docs/linux/man/1-molrender/"
---

<h2 class="name">NAME</h2>
 

 molrender - The molrender program reads a molecule from an input file and can render it in a variety of ways. 

 The output is an OOGL file that the Geomview program can read and display.

<h2>Running molrender</h2>

 

 

 If you have wish installed, tkmolrender script can be run to bring up a simple GUI to let you set up the molrender options. Otherwise, molrender can be run directly and takes the following command line options: 

<dl>
<dt>-model
<dd> Must be followed by one of ball, stick, or connolly
<dt>-render
<dd> Must be followed by the argument oogl
<dt>-pdb
<dd> Indicates that the input is a PDB file
<dt>-keyval
<dd> Indicates that the input is a KeyVal input
<dt>-keyword
<dd> Must be followed by keyword to read in a KeyVal input
<dt>-level
<dd> Must be Followed by an integer which is the sphere subdivision level</dl>
 

 

<h2>License</h2>

 

 

 molrender is open-source software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. 

<h2>Warranty</h2>

 

 

 molrender is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. 

<h2>Index</h2>


