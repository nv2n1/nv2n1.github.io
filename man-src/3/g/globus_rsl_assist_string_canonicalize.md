---
title: "globus_rsl_assist_string_canonicalize(3)"
name: "globus_rsl_assist_string_canonicalize"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_rsl_assist_string_canonicalize/"
description: "RSL Helper Functions –"
---

<h2 class="name">NAME</h2>
<p> RSL Helper Functions &#8211; </p>
<h3>Functions</h3>
<p> int <code>globus_rsl_assist_attributes_canonicalize</code> (globus_rsl_t *rsl)<br />
 <i>Canonicalize all attribute names in an RSL parse tree. </i><br />
 void <code>globus_rsl_assist_string_canonicalize</code> (char *ptr)<br />
 <i>Canonicalize an attribute name. </i></p>
<h2>Detailed Description</h2>
<p> The rsl_assist library provide a set of functions to canonicalize RSL parse trees or strings.</p>
<h2>Function Documentation</h2>
<h3>int globus_rsl_assist_attributes_canonicalize (globus_rsl_t *rsl)</h3>
<p> Canonicalize all attribute names in an RSL parse tree. The <code>globus_rsl_assist_attributes_canonicalize()</code> function performs an in-place canonicalization of the RSL parse tree pointed to by its <i>rsl</i> parameter. All relation attribute names will be changed so that they lower-case, with all internal underscore characters removed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>rsl</i> Pointer to the RSL parse tree to canonicalize.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> If <code>globus_rsl_assist_attributes_canonicalize()</code> is successful, it will ensure that all attribute names in the given RSL will be in canonical form and return GLOBUS_SUCCESS. If an error occurs, it will return GLOBUS_FAILURE.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_FAILURE</i> Failure</dl>
<h3>void globus_rsl_assist_string_canonicalize (char *ptr)</h3>
<p> Canonicalize an attribute name. The <code>globus_rsl_assist_string_canonicalize()</code> function modifies the NULL-terminated string pointed to by its <i>ptr</i> parameter so that it is in canonical form. The canonical form is all lower-case with all underscore characters removed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ptr</i> Pointer to the RSL string to modify in place.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> void</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_rsl from the source code. </p>
<h2>Index</h2>
