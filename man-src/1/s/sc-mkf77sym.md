---
title: "sc-mkf77sym(1)"
name: "sc-mkf77sym"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sc-mkf77sym/"
---

<h2 class="name">NAME</h2>
 

 sc-mkf77sym - The sc-mkf77sym program is used to generate symbols for linking FORTRAN subroutines into MPQC.

<h2>Synopsis</h2>

 

 

 

 <pre>
sc-mkf77sym <i>input</i> <i>output</i>
</pre> 

 

<h2>Description</h2>

 

 

 sc-mkf77sym requires two arguments: the name of the input file and the name of the output file. The input file contains C preprocessor definitions of the form 'define F77_FUNC' where FUNC is the name of a FORTRAN 77 function. The output file assigns these definitions to the C symbol that will link with the FORTRAN 77 function. For example, if FORTRAN symbols are formed from the routine name by converting to lowercase and have appending an underscore, then the following input file: 

 

 <pre><code>
#define F77_DGEMM
</code></pre> 

 

 will result in the following ouput file: 

 

 <pre><code>
#define F77_DGEMM dgemm_
</code></pre> 

 

<h2>License</h2>

 

 

 sc-mkf77sym is open-source software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. 

<h2>Warranty</h2>

 

 

 sc-mkf77sym is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. 

<h2>Index</h2>


