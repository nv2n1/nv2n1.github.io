---

title: "sdot(3)"
name: "sdot"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdot/"
---

sdot.f - 

<h2>SYNOPSIS</h2>

 
 

<h3>Functions/Subroutines</h3>

 

 
 REAL function <b>sdot</b> (N, SX, INCX, SY, INCY) 
 <i></i><b>SDOT</b>

<h2>Function/Subroutine Documentation</h2>

 

<h3>REAL function sdot (integerN, real, dimension(*)SX, integerINCX, real, dimension(*)SY, integerINCY)</h3>

 

 

 <b>SDOT</b> <b>Purpose: </b>
<dl>
<dt>
</dt><dd> 
 <pre>
    SDOT forms the dot product of two vectors.
    uses unrolled loops for increments equal to one.
</pre> 
&nbsp;<wbr></dd></dl>
 

 <b>Author:</b>
<dl>
<dt>
</dt><dd> Univ. of Tennessee 
 Univ. of California Berkeley 
 Univ. of Colorado Denver 
 NAG Ltd.</dd></dl>
 

 <b>Date:</b>
<dl>
<dt>
</dt><dd> November 2011</dd></dl>
 

 <b>Further Details: </b>
<dl>
<dt>
</dt><dd> 
 <pre>
     jack dongarra, linpack, 3/11/78.
     modified 12/3/93, array(1) declarations changed to array(*)
</pre> 
&nbsp;<wbr></dd></dl>
 

 

 

 Definition at line 52 of file sdot.f.

<h2>Author</h2>

 

 Generated automatically by Doxygen for LAPACK from the source code.
