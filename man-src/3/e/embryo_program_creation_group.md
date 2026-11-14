---
title: "embryo_program_creation_group(3)"
name: "embryo_program_creation_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-embryo_program_creation_group/"
description: "Program Creation and Destruction Functions – Functions that set up programs, and destroy them."
---

<p>Program Creation and Destruction Functions &#8211; Functions that set up programs, and destroy them. </p>
<h3>Functions</h3>
<p>EAPI Embryo_Program * <code>embryo_program_new</code> (void *data, int size)<br />
 <i>Creates a new Embryo program, with bytecode data that can be freed. </i><br />
 EAPI Embryo_Program * <code>embryo_program_const_new</code> (void *data, int size)<br />
 <i>Creates a new Embryo program, with bytecode data that cannot be freed. </i><br />
 EAPI Embryo_Program * <code>embryo_program_load</code> (char *file)<br />
 <i>Creates a new Embryo program based on the bytecode data stored in the given file. </i><br />
 EAPI void <code>embryo_program_free</code> (Embryo_Program *ep)<br />
 <i>Frees the given Embryo program. </i></p>
<h2>Detailed Description</h2>
<p>Functions that set up programs, and destroy them.</p>
<h2>Function Documentation</h2>
<h3>EAPI Embryo_Program* embryo_program_const_new (void * data, int size)</h3>
<p>Creates a new Embryo program, with bytecode data that cannot be freed. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> Pointer to the bytecode of the program.<br />
 <i>size</i> Number of bytes of bytecode.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A new Embryo program.</dl>
<h3>EAPI void embryo_program_free (Embryo_Program * ep)</h3>
<p>Frees the given Embryo program. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ep</i> The given program.</dl>
<h3>EAPI Embryo_Program* embryo_program_load (char * file)</h3>
<p>Creates a new Embryo program based on the bytecode data stored in the given file. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>file</i> Filename of the given file.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A new Embryo program.</dl>
<p> References embryo_program_new(), and embryo_swap_32().</p>
<h3>EAPI Embryo_Program* embryo_program_new (void * data, int size)</h3>
<p>Creates a new Embryo program, with bytecode data that can be freed. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>data</i> Pointer to the bytecode of the program.<br />
 <i>size</i> Number of bytes of bytecode.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A new Embryo program.</dl>
<p> Referenced by embryo_program_load().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Embryo from the source code.</p>
