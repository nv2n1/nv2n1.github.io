---
title: "mat_vargetstructs(3)"
name: "mat_vargetstructs"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mat_vargetstructs/"
description: "Mat_VarGetStructs – Index a structure variable using slices of each dimension"
---

<p><code>Mat_VarGetStructs</code> &#8211; Index a structure variable using slices of each dimension</p>
<h2>Synopsis</h2>
<p>Fd #include &lt;matio.h&gt; Ft matvar_t * Fo Mat_VarGetStructs Fa const matvar_t *matvar Fa int *start Fa int *stride Fa int *edge Fa int copy_fields Fc</p>
<h2>Description</h2>
<p>The Fn Mat_VarGetStructs function selects a subarray from a structure array Fa matvar. Each of the elements in the subarray contains all of the fields of the structure. The index of each dimension starts at the Fa start element in the array (0 being the first element), and reads every Fa stride values (1 being every element, 2 every other element, etc.). The total number of elements in the subarray is specified as Fa edge. The Fa copy_fields option specifies whether the fields of the original structure are copied for the new subarray. If set to 0, the returned structure array&#8217;s fields have the same pointer as the original array, and the <code>data</code> field of the subarray structure. The subarray is marked with the conserve memory flag indicating that the fields should not be free&#8217;d. They are free&#8217;d when the original structure is free&#8217;d.</p>
<h2>Return Values</h2>
<p>A subarray of the original structure array, or NULL if there is an error.</p>
<h2>See Also</h2>
<p>Mat_VarGetStructsLinear3,</p>
