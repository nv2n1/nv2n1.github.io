---
title: "cfg_value_t(3)"
name: "cfg_value_t"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cfg_value_t/"
description: "cfg_value_t – Data structure holding the value of a fundamental option value."
---

<h2 class="name">NAME</h2>
<p> cfg_value_t &#8211; Data structure holding the value of a fundamental option value. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;confuse.h&gt; </p>
<h3>Data Fields</h3>
<p> long int <code>number</code><br />
 <i>integer value </i><br />
 double <code>fpnumber</code><br />
 <i>floating point value </i><br />
 <code>cfg_bool_t</code> <code>boolean</code><br />
 <i>boolean value </i><br />
 char * <code>string</code><br />
 <i>string value </i><br />
 <code>cfg_t</code> * <code>section</code><br />
 <i>section value </i><br />
 void * <code>ptr</code><br />
 <i>user-defined value </i></p>
<h2>Detailed Description</h2>
<p> Data structure holding the value of a fundamental option value. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for confuse from the source code. </p>
<h2>Index</h2>
