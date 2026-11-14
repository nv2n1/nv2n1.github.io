---
title: "antlr3-apiclasses(3)"
name: "antlr3-apiclasses"
section: "3"
letter: "a"
url: "/docs/linux/man/3-antlr3-apiclasses/"
description: "API Classes –"
---

<h2 class="name">NAME</h2>
<p> API Classes &#8211; </p>
<p> The API classes are divided into the typdefs (and their underlying structs) that are the containers for each &#8216;object&#8217; within the ANTLR3C runtime, and their implementations (the functions that are installed by default in to these structures when you create them.</p>
<h3>Modules</h3>
<p> <code>API Typedefs and Structs</code> </p>
<p> <i>These structures (and the typedefs that you use to reference them and their pointers) are the C equivalent of objects. </i><br />
 <code>API Implementation functions</code> </p>
<p> <i>API implementation functions are the default implementation of each of the methods in a particular typedef structure. </i></p>
<h2>Detailed Description</h2>
<p> The API classes are divided into the typdefs (and their underlying structs) that are the containers for each &#8216;object&#8217; within the ANTLR3C runtime, and their implementations (the functions that are installed by default in to these structures when you create them. </p>
<p> ) </p>
<p> The typedefs contain data and function pointers, which together define the object. The implementation functions are the default implementations of the &#8216;methds&#8217; encapsulated by the typdef structures.You may override any of the methods once their objects are created by installing a pointer to your own function. Some of these methods create other &#8216;objects&#8217; (instances of typedef structures), which allows you install your own method and create your own implementation of these.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for ANTLR3C from the source code. </p>
<h2>Index</h2>
