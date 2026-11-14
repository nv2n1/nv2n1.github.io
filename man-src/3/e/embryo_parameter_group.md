---
title: "embryo_parameter_group(3)"
name: "embryo_parameter_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-embryo_parameter_group/"
description: "Function Parameter Functions – Functions that set parameters for the next function that is called."
---

<p>Function Parameter Functions &#8211; Functions that set parameters for the next function that is called. </p>
<h3>Functions</h3>
<p>EAPI int <code>embryo_parameter_cell_push</code> (Embryo_Program *ep, Embryo_Cell cell)<br />
 <i>Pushes an Embryo_Cell onto the function stack to use as a parameter for the next function that is called in the given program. </i><br />
 EAPI int <code>embryo_parameter_string_push</code> (Embryo_Program *ep, const char *str)<br />
 <i>Pushes a string onto the function stack to use as a parameter for the next function that is called in the given program. </i><br />
 EAPI int <code>embryo_parameter_cell_array_push</code> (Embryo_Program *ep, Embryo_Cell *cells, int num)<br />
 <i>Pushes an array of Embryo_Cells onto the function stack to be used as parameters for the next function that is called in the given program. </i></p>
<h2>Detailed Description</h2>
<p>Functions that set parameters for the next function that is called.</p>
<h2>Function Documentation</h2>
<h3>EAPI int embryo_parameter_cell_array_push (Embryo_Program * ep, Embryo_Cell * cells, int num)</h3>
<p>Pushes an array of Embryo_Cells onto the function stack to be used as parameters for the next function that is called in the given program. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ep</i> The given program.<br />
 <i>cells</i> The array of Embryo_Cells.<br />
 <i>num</i> The number of cells in cells.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if successful. 0 otherwise.</dl>
<p> References embryo_parameter_cell_push().</p>
<h3>EAPI int embryo_parameter_cell_push (Embryo_Program * ep, Embryo_Cell cell)</h3>
<p>Pushes an Embryo_Cell onto the function stack to use as a parameter for the next function that is called in the given program. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ep</i> The given program.<br />
 <i>cell</i> The Embryo_Cell to push onto the stack.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if successful. 0 otherwise.</dl>
<p> Referenced by embryo_parameter_cell_array_push().</p>
<h3>EAPI int embryo_parameter_string_push (Embryo_Program * ep, const char * str)</h3>
<p>Pushes a string onto the function stack to use as a parameter for the next function that is called in the given program. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ep</i> The given program.<br />
 <i>str</i> The string to push onto the stack.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if successful. 0 otherwise.</dl>
<p> References embryo_parameter_string_push(). </p>
<p> Referenced by embryo_parameter_string_push().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Embryo from the source code.</p>
