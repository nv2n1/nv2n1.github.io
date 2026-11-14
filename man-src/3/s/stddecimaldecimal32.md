---
title: "stddecimaldecimal32(3)"
name: "stddecimaldecimal32"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stddecimaldecimal32/"
description: "std::decimal::decimal32 –"
---

<p>std::decimal::decimal32 &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Types</h3>
<p>typedef float __decfloat32 <code>__attribute__</code> ((mode(SD)))</p>
<h3>Public Member Functions</h3>
<pre><code>decimal32 (decimal64 __d64)



decimal32 (decimal128 __d128)



decimal32 (float __r)



decimal32 (double __r)



decimal32 (long double __r)



decimal32 (int __z)



decimal32 (unsigned int __z)



decimal32 (long __z)



decimal32 (unsigned long __z)



decimal32 (long long __z)



decimal32 (unsigned long long __z)



decimal32 (__decfloat32 __z)



__decfloat32 __getval (void)



void __setval (__decfloat32 __x)



decimal32 &amp; operator*= (decimal32 __rhs)



decimal32 &amp; operator*= (decimal64 __rhs)



decimal32 &amp; operator*= (decimal128 __rhs)



decimal32 &amp; operator*= (int __rhs)



decimal32 &amp; operator*= (unsigned int __rhs)



decimal32 &amp; operator*= (long __rhs)



decimal32 &amp; operator*= (unsigned long __rhs)



decimal32 &amp; operator*= (unsigned long long __rhs)



decimal32 &amp; operator*= (long long __rhs)



decimal32 &amp; operator++ ()



decimal32 operator++ (int)



decimal32 &amp; operator+= (int __rhs)



decimal32 &amp; operator+= (decimal32 __rhs)



decimal32 &amp; operator+= (decimal64 __rhs)



decimal32 &amp; operator+= (decimal128 __rhs)



decimal32 &amp; operator+= (unsigned int __rhs)



decimal32 &amp; operator+= (long __rhs)



decimal32 &amp; operator+= (unsigned long __rhs)



decimal32 &amp; operator+= (long long __rhs)



decimal32 &amp; operator+= (unsigned long long __rhs)



decimal32 &amp; operator-- ()



decimal32 operator-- (int)



decimal32 &amp; operator-= (long __rhs)



decimal32 &amp; operator-= (int __rhs)



decimal32 &amp; operator-= (long long __rhs)



decimal32 &amp; operator-= (unsigned long long __rhs)



decimal32 &amp; operator-= (unsigned long __rhs)



decimal32 &amp; operator-= (decimal128 __rhs)



decimal32 &amp; operator-= (unsigned int __rhs)



decimal32 &amp; operator-= (decimal32 __rhs)



decimal32 &amp; operator-= (decimal64 __rhs)



decimal32 &amp; operator/= (decimal32 __rhs)



decimal32 &amp; operator/= (long long __rhs)



decimal32 &amp; operator/= (unsigned long long __rhs)



decimal32 &amp; operator/= (unsigned long __rhs)



decimal32 &amp; operator/= (decimal64 __rhs)



decimal32 &amp; operator/= (unsigned int __rhs)



decimal32 &amp; operator/= (decimal128 __rhs)



decimal32 &amp; operator/= (long __rhs)



decimal32 &amp; operator/= (int __rhs)</code></pre>
<h2>Detailed Description</h2>
<p>3.2.2 Class decimal32. </p>
<p> Definition at line 227 of file decimal.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>std::decimal::decimal32::decimal32 (__decfloat32__z) [inline]</h3>
<p>Conforming extension: Conversion from scalar decimal type. </p>
<p> Definition at line 251 of file decimal.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
