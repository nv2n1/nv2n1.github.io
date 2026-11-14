---
title: "stdbinder2nd(3)"
name: "stdbinder2nd"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbinder2nd/"
description: "std::binder2nd< _Operation > –"
---

<p>std::binder2nd&lt; _Operation &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>std::unary_function&lt; _Operation::first_argument_type, _Operation::result_type &gt;</code>.</p>
<h3>Public Types</h3>
<p>typedef<br />
 _Operation::first_argument_type <code>argument_type</code>&quot; </p>
<p> typedef _Operation::result_type <code>result_type</code></p>
<h3>Public Member Functions</h3>
<p><code>binder2nd</code> (const _Operation &amp;__x, const typename _Operation::second_argument_type &amp;__y) </p>
<p> _Operation::result_type <code>operator()</code> (const typename _Operation::first_argument_type &amp;__x) const </p>
<p> _Operation::result_type <code>operator()</code> (typename _Operation::first_argument_type &amp;__x) const</p>
<h3>Protected Attributes</h3>
<p>_Operation <code>op</code> </p>
<p> _Operation::second_argument_type <code>value</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Operation&gt;class std::binder2nd&lt; _Operation &gt;</h3>
<p>One of the <code>binder functors</code>. </p>
<p> Definition at line 139 of file binders.h.</p>
<h2>Member Typedef Documentation</h2>
<h3>typedef _Operation::first_argument_type <code>std::unary_function</code>&lt; _Operation::first_argument_type , _Operation::result_type &gt;::<code>argument_type</code> [inherited]</h3>
<p>argument_type is the type of the argument </p>
<p> Definition at line 104 of file stl_function.h.</p>
<h3>typedef _Operation::result_type <code>std::unary_function</code>&lt; _Operation::first_argument_type , _Operation::result_type &gt;::<code>result_type</code> [inherited]</h3>
<p>result_type is the return type </p>
<p> Definition at line 107 of file stl_function.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
