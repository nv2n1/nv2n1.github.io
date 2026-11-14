---
title: "cfg_defvalue_t(3)"
name: "cfg_defvalue_t"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cfg_defvalue_t/"
description: "cfg_defvalue_t – Data structure holding the default value given by the initialization macros."
---

<h2 class="name">NAME</h2>
<p> cfg_defvalue_t &#8211; Data structure holding the default value given by the initialization macros. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;confuse.h&gt; </p>
<h3>Data Fields</h3>
<p> long int <code>number</code><br />
 <i>default integer value </i><br />
 double <code>fpnumber</code><br />
 <i>default floating point value </i><br />
 <code>cfg_bool_t</code> <code>boolean</code><br />
 <i>default boolean value </i><br />
 char * <code>string</code><br />
 <i>default string value </i><br />
 char * <code>parsed</code><br />
 <i>default value that is parsed by libConfuse, used for lists and functions </i></p>
<h2>Detailed Description</h2>
<p> Data structure holding the default value given by the initialization macros. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for confuse from the source code. </p>
<h2>Index</h2>
