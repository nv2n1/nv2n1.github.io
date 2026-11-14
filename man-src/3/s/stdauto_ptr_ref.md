---
title: "stdauto_ptr_ref(3)"
name: "stdauto_ptr_ref"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdauto_ptr_ref/"
description: "std::auto_ptr_ref< _Tp1 > –"
---

<p>std::auto_ptr_ref&lt; _Tp1 &gt; &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Member Functions</h3>
<p><code>auto_ptr_ref</code> (_Tp1 *__p)</p>
<h3>Public Attributes</h3>
<p>_Tp1 * <code>_M_ptr</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _Tp1&gt;struct std::auto_ptr_ref&lt; _Tp1 &gt;</h3>
<p>A wrapper class to provide auto_ptr with reference semantics. For example, an auto_ptr can be assigned (or constructed from) the result of a function which returns an auto_ptr by value. </p>
<p> All the auto_ptr_ref stuff should happen behind the scenes. </p>
<p> Definition at line 48 of file auto_ptr.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
