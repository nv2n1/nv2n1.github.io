---
title: "mat_varfree(3)"
name: "mat_varfree"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mat_varfree/"
description: "Mat_VarFree – Free a MAT variable structure"
---

<p><code>Mat_VarFree</code> &#8211; Free a MAT variable structure</p>
<h2>Synopsis</h2>
<p>Fd #include &lt;matio.h&gt; Ft void Fo Mat_VarRead Fa matvar_t *matvar Fc</p>
<h2>Description</h2>
<p>The Fn Mat_VarFree function free&#8217;s the memory used by a MAT variable structure. If the variable was no created with the <code>MAT_F_DONT_COPY_DATA</code> flag, the variable data is also free&#8217;d.</p>
<h2>See Also</h2>
<p>Mat_VarCreate3, Mat_VarCreateStruct3</p>
