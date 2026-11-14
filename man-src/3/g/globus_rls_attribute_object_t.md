---
title: "globus_rls_attribute_object_t(3)"
name: "globus_rls_attribute_object_t"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_rls_attribute_object_t/"
description: "globus_rls_attribute_object_t –"
---

<h2 class="name">NAME</h2>
<p> globus_rls_attribute_object_t &#8211; </p>
<p> <code>globus_rls_client_lrc_attr_search()</code> returns a list of these structures which include the object name (LFN or PFN) and attribute value found by the query.</p>
<h2>SYNOPSIS</h2>
<h3>Data Fields</h3>
<p> <code>globus_rls_attribute_t</code> <code>attr</code> </p>
<p> char * <code>key</code> </p>
<p> int <code>rc</code> </p>
<h2>Detailed Description</h2>
<p> <code>globus_rls_client_lrc_attr_search()</code> returns a list of these structures which include the object name (LFN or PFN) and attribute value found by the query.</p>
<h2>Field Documentation</h2>
<h3><code>globus_rls_attribute_t</code> <code>globus_rls_attribute_object_t::attr</code></h3>
<p> Attribute value.</p>
<h3>char* <code>globus_rls_attribute_object_t::key</code></h3>
<p> LFN or PFN.</p>
<h3>int <code>globus_rls_attribute_object_t::rc</code></h3>
<p> Result code, only used in bulk query. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus rls client from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAJ">Author</a></p>
<dd></dl>
