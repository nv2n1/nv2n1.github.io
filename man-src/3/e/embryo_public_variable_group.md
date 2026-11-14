---
title: "embryo_public_variable_group(3)"
name: "embryo_public_variable_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-embryo_public_variable_group/"
description: "Public Variable Access Functions – In an Embryo program, a global variable can be declared public, as described in Scope."
---

<p>Public Variable Access Functions &#8211; In an Embryo program, a global variable can be declared public, as described in <code>Scope</code>. </p>
<h3>Functions</h3>
<p>EAPI Embryo_Cell <code>embryo_program_variable_find</code> (Embryo_Program *ep, const char *name)<br />
 <i>Retrieves the location of the public variable in the given program with the given name. </i><br />
 EAPI int <code>embryo_program_variable_count_get</code> (Embryo_Program *ep)<br />
 <i>Retrieves the number of public variables in the given program. </i><br />
 EAPI Embryo_Cell <code>embryo_program_variable_get</code> (Embryo_Program *ep, int num)<br />
 <i>Retrieves the location of the public variable in the given program with the given identifier. </i></p>
<h2>Detailed Description</h2>
<p>In an Embryo program, a global variable can be declared public, as described in <code>Scope</code>. </p>
<p> The functions here allow the host program to access these public variables.</p>
<h2>Function Documentation</h2>
<h3>EAPI int embryo_program_variable_count_get (Embryo_Program * ep)</h3>
<p>Retrieves the number of public variables in the given program. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ep</i> The given program.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The number of public variables.</dl>
<h3>EAPI Embryo_Cell embryo_program_variable_find (Embryo_Program * ep, const char * name)</h3>
<p>Retrieves the location of the public variable in the given program with the given name. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ep</i> The given program.<br />
 <i>name</i> The given name.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The address of the variable if found. EMBRYO_CELL_NONE otherwise.</dl>
<p> References EMBRYO_CELL_NONE.</p>
<h3>EAPI Embryo_Cell embryo_program_variable_get (Embryo_Program * ep, int num)</h3>
<p>Retrieves the location of the public variable in the given program with the given identifier. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ep</i> The given program.<br />
 <i>num</i> The identifier of the public variable.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The virtual machine address of the variable if found. EMBRYO_CELL_NONE otherwise.</dl>
<p> References EMBRYO_CELL_NONE.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Embryo from the source code.</p>
