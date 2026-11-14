---
title: "embryo_func_group(3)"
name: "embryo_func_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-embryo_func_group/"
description: "Function Functions – Functions that deal with Embryo program functions."
---

<p>Function Functions &#8211; Functions that deal with Embryo program functions. </p>
<h3>Functions</h3>
<p>EAPI void <code>embryo_program_native_call_add</code> (Embryo_Program *ep, const char *name, Embryo_Cell(*func)(Embryo_Program *ep, Embryo_Cell *params))<br />
 <i>Adds a native program call to the given Embryo program. </i><br />
 EAPI Embryo_Function <code>embryo_program_function_find</code> (Embryo_Program *ep, const char *name)<br />
 <i>Returns the function in the given program with the given name. </i></p>
<h2>Detailed Description</h2>
<p>Functions that deal with Embryo program functions.</p>
<h2>Function Documentation</h2>
<h3>EAPI Embryo_Function embryo_program_function_find (Embryo_Program * ep, const char * name)</h3>
<p>Returns the function in the given program with the given name. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ep</i> The given program.<br />
 <i>name</i> The given function name.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The function if successful. Otherwise, EMBRYO_FUNCTION_NONE.</dl>
<p> References EMBRYO_FUNCTION_NONE.</p>
<h3>EAPI void embryo_program_native_call_add (Embryo_Program * ep, const char * name, Embryo_Cell(*)(Embryo_Program *ep, Embryo_Cell *params) func)</h3>
<p>Adds a native program call to the given Embryo program. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ep</i> The given Embryo program.<br />
 <i>name</i> The name for the call used in the script.<br />
 <i>func</i> The function to use when the call is made.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Embryo from the source code.</p>
