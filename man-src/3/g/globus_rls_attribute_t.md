---
title: "globus_rls_attribute_t(3)"
name: "globus_rls_attribute_t"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_rls_attribute_t/"
description: "globus_rls_attribute_t –"
---

<h2 class="name">NAME</h2>
<p> globus_rls_attribute_t &#8211; </p>
<p> Object (LFN or PFN) attribute type.</p>
<h2>SYNOPSIS</h2>
<h3>Data Fields</h3>
<p> char * <code>name</code> </p>
<p> <code>globus_rls_obj_type_t</code> <code>objtype</code> </p>
<p> <code>globus_rls_attr_type_t</code> <code>type</code> </p>
<p> union { </p>
<p> time_t <code>t</code> </p>
<p> double <code>d</code> </p>
<p> int <code>i</code> </p>
<p> char * <code>s</code> </p>
<p> } <code>val</code> </p>
<h2>Detailed Description</h2>
<p> Object (LFN or PFN) attribute type.</p>
<h2>Field Documentation</h2>
<h3>char* <code>globus_rls_attribute_t::name</code></h3>
<p> Attribute name.</p>
<h3><code>globus_rls_obj_type_t</code> <code>globus_rls_attribute_t::objtype</code></h3>
<p> Object type.</p>
<h3><code>globus_rls_attr_type_t</code> <code>globus_rls_attribute_t::type</code></h3>
<p> Attribute value type.</p>
<h3>time_t <code>globus_rls_attribute_t::t</code></h3>
<p> Date value (unix time).</p>
<h3>double <code>globus_rls_attribute_t::d</code></h3>
<p> Floating point value.</p>
<h3>int <code>globus_rls_attribute_t::i</code></h3>
<p> Integer value.</p>
<h3>char* <code>globus_rls_attribute_t::s</code></h3>
<p> String value.</p>
<h3>union { &#8230; } <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> <code>globus_rls_attribute_t::val</code></h3>
<p> Value of attribute (depends on type). </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus rls client from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAO">Author</a></p>
<dd></dl>
