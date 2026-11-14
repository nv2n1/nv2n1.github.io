---
title: "std_weak_result_type(3)"
name: "std_weak_result_type"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std_weak_result_type/"
description: "std::_Weak_result_type< _Functor > –"
---

<p>std::_Weak_result_type&lt; _Functor &gt; &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>std::_Weak_result_type_impl&lt; remove_cv&lt; _Functor &gt;::type &gt;</code>. Inherited by std::_Bind&lt; _Functor(_Bound_args&#8230;)&gt;.</p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Functor&gt;struct std::_Weak_result_type&lt; _Functor &gt;</h3>
<p>Strip top-level cv-qualifiers from the function object and let _Weak_result_type_impl perform the real work. </p>
<p> Definition at line 184 of file functional.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
