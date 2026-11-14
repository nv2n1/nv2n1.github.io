---
title: "mat_vargetstructfieldnames(3)"
name: "mat_vargetstructfieldnames"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mat_vargetstructfieldnames/"
description: "Mat_VarGetStructFieldnames – Get the fieldnames of a structure variable."
---

<p><code>Mat_VarGetStructFieldnames</code> &#8211; Get the fieldnames of a structure variable.</p>
<h2>Synopsis</h2>
<p>Fd #include &lt;matio.h&gt; Ft char * const * Fo Mat_VarGetStructFieldnames Fa const matvar_t *matvar Fc</p>
<h2>Description</h2>
<p>The Fn Mat_VarGetStructFieldnames function returns the fieldnames of the structure variable Fa matvar.</p>
<h2>Return Values</h2>
<p>An array of fieldnames is returned of the variable is a valid structure variable. Otherwise NULL is returned. The Mat_VarGetNumberOfFields function returns the number of fields for the structure.</p>
<h2>See Also</h2>
<p>Mat_VarGetNumberOfFields3,</p>
