---
title: "std__atomic_flag_base(3)"
name: "std__atomic_flag_base"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__atomic_flag_base/"
description: "std::__atomic_flag_base –"
---

<p>std::__atomic_flag_base &#8211;</p>
<h2>Synopsis</h2>
<p> Inherited by <code>std::atomic_flag</code>.</p>
<h3>Public Attributes</h3>
<p>__atomic_flag_data_type <code>_M_i</code></p>
<h2>Detailed Description</h2>
<p>Base type for atomic_flag. </p>
<p> Base type is POD with data, allowing atomic_flag to derive from it and meet the standard layout type requirement. In addition to compatibilty with a C interface, this allows different implementations of atomic_flag to use the same atomic operation functions, via a standard conversion to the __atomic_flag_base argument. </p>
<p> Definition at line 261 of file atomic_base.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
