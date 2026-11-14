---
title: "embryo_library_group(3)"
name: "embryo_library_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-embryo_library_group/"
description: "Library Maintenance Functions – Functions that start up and shutdown the Embryo library."
---

<p>Library Maintenance Functions &#8211; Functions that start up and shutdown the Embryo library. </p>
<h3>Functions</h3>
<p>EAPI int <code>embryo_init</code> (void)<br />
 <i>Initialises the Embryo library. </i><br />
 EAPI int <code>embryo_shutdown</code> (void)<br />
 <i>Shuts down the Embryo library. </i></p>
<h2>Detailed Description</h2>
<p>Functions that start up and shutdown the Embryo library.</p>
<h2>Function Documentation</h2>
<h3>EAPI int embryo_init (void)</h3>
<p>Initialises the Embryo library. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The number of times the library has been initialised without being shut down.</dl>
<h3>EAPI int embryo_shutdown (void)</h3>
<p>Shuts down the Embryo library. </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The number of times the library has been initialised without being shutdown.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Embryo from the source code.</p>
