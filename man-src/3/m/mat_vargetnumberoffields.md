---
title: "mat_vargetnumberoffields(3)"
name: "mat_vargetnumberoffields"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mat_vargetnumberoffields/"
description: "Mat_VarGetNumberOfFields – Get the number of fields for a structure variable."
---

<p><code>Mat_VarGetNumberOfFields</code> &#8211; Get the number of fields for a structure variable.</p>
<h2>Synopsis</h2>
<p>Fd #include &lt;matio.h&gt; Ft unsigned Fo Mat_VarGetNumberOfFields Fa const matvar_t *matvar Fc</p>
<h2>Description</h2>
<p>The Fn Mat_VarGetNumberOfFields function returns the number of fields for the structure variable Fa matvar.</p>
<h2>Return Values</h2>
<p>The number of fields will be returned on success, and 0 otherwise. Note also that a structure can validly contain 0 fields.</p>
<h2>See Also</h2>
<p>Mat_VarGetStructFieldnames3</p>
