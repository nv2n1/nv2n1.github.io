---
title: "embryo_program_data_group(3)"
name: "embryo_program_data_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-embryo_program_data_group/"
description: "Program Data Functions – Functions that set and retrieve data associated with the given program."
---

<p>Program Data Functions &#8211; Functions that set and retrieve data associated with the given program. </p>
<h3>Functions</h3>
<p>EAPI void <code>embryo_program_data_set</code> (Embryo_Program *ep, void *data)<br />
 <i>Sets the data associated to the given program. </i><br />
 EAPI void * <code>embryo_program_data_get</code> (Embryo_Program *ep)<br />
 <i>Retrieves the data associated to the given program. </i></p>
<h2>Detailed Description</h2>
<p>Functions that set and retrieve data associated with the given program.</p>
<h2>Function Documentation</h2>
<h3>EAPI void* embryo_program_data_get (Embryo_Program * ep)</h3>
<p>Retrieves the data associated to the given program. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ep</i> The given program.</dl>
<h3>EAPI void embryo_program_data_set (Embryo_Program * ep, void * data)</h3>
<p>Sets the data associated to the given program. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ep</i> The given program.<br />
 <i>data</i> New bytecode data.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Embryo from the source code.</p>
