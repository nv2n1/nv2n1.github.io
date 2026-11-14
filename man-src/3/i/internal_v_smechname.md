---
title: "internal_v_smechname(3)"
name: "internal_v_smechname"
section: "3"
letter: "i"
url: "/docs/linux/man/3-internal_v_smechname/"
description: "internal_v_smechname – Internal names and mechanism names"
---

<h2 class="name">NAME</h2>
<p> internal_v_smechname &#8211; Internal names and mechanism names</p>
<h2>Name forms</h2>
<p> There are two name representations in GSS-API: Internal form and Contiguous string (&#8216;flat&#8217;) form. Functions <code>gss_export_name()</code> and <code>gss_import_name()</code> can be used to convert between the two forms. </p>
<dl>
<dt>&bull;</p>
<dd> The contiguous string form is described by an oid specificing the type and an octet string. A special form of the contiguous string form is the exported name object. The exported name defined for each mechanism, is something that can be stored and compared later. The exported name is what should be used for ACLs comparisons.</p>
<dt>&bull;</p>
<dd> The Internal form is opaque to the application programmer and is implementation-dependent.</p>
<dt>&bull;</p>
<dd> There is also a special form of the Internal Name (IN), and that is the Mechanism Name (MN). In the mechanism name all the generic information is stripped of and only contain the information for one mechanism. In GSS-API some function return MN and some require MN as input. Each of these function is marked up as such.</dl>
<p> Describe relationship between import_name, canonicalize_name, export_name and friends. </p>
<h2>Index</h2>
