---
title: "stddecimaldecimal64(3)"
name: "stddecimaldecimal64"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stddecimaldecimal64/"
description: "std::decimal::decimal64 –"
---

<p>std::decimal::decimal64 &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Types</h3>
<p>typedef float __decfloat64 <code>__attribute__</code> ((mode(DD)))</p>
<h3>Public Member Functions</h3>
<pre><code>decimal64 (decimal32 d32)



decimal64 (decimal128 d128)



decimal64 (float __r)



decimal64 (double __r)



decimal64 (long double __r)



decimal64 (int __z)



decimal64 (unsigned int __z)



decimal64 (long __z)



decimal64 (unsigned long __z)



decimal64 (long long __z)



decimal64 (unsigned long long __z)



decimal64 (__decfloat64 __z)



__decfloat64 __getval (void)



void __setval (__decfloat64 __x)



decimal64 &amp; operator*= (decimal32 __rhs)



decimal64 &amp; operator*= (decimal64 __rhs)



decimal64 &amp; operator*= (decimal128 __rhs)



decimal64 &amp; operator*= (int __rhs)



decimal64 &amp; operator*= (unsigned int __rhs)



decimal64 &amp; operator*= (long __rhs)



decimal64 &amp; operator*= (unsigned long __rhs)



decimal64 &amp; operator*= (unsigned long long __rhs)



decimal64 &amp; operator*= (long long __rhs)



decimal64 &amp; operator++ ()



decimal64 operator++ (int)



decimal64 &amp; operator+= (int __rhs)



decimal64 &amp; operator+= (decimal32 __rhs)



decimal64 &amp; operator+= (decimal64 __rhs)



decimal64 &amp; operator+= (decimal128 __rhs)



decimal64 &amp; operator+= (unsigned int __rhs)



decimal64 &amp; operator+= (long __rhs)



decimal64 &amp; operator+= (unsigned long __rhs)



decimal64 &amp; operator+= (long long __rhs)



decimal64 &amp; operator+= (unsigned long long __rhs)



decimal64 &amp; operator-- ()



decimal64 operator-- (int)



decimal64 &amp; operator-= (long __rhs)



decimal64 &amp; operator-= (int __rhs)



decimal64 &amp; operator-= (long long __rhs)



decimal64 &amp; operator-= (unsigned long long __rhs)



decimal64 &amp; operator-= (unsigned long __rhs)



decimal64 &amp; operator-= (decimal128 __rhs)



decimal64 &amp; operator-= (unsigned int __rhs)



decimal64 &amp; operator-= (decimal32 __rhs)



decimal64 &amp; operator-= (decimal64 __rhs)



decimal64 &amp; operator/= (decimal32 __rhs)



decimal64 &amp; operator/= (long long __rhs)



decimal64 &amp; operator/= (unsigned long long __rhs)



decimal64 &amp; operator/= (unsigned long __rhs)



decimal64 &amp; operator/= (decimal64 __rhs)



decimal64 &amp; operator/= (unsigned int __rhs)



decimal64 &amp; operator/= (decimal128 __rhs)



decimal64 &amp; operator/= (long __rhs)



decimal64 &amp; operator/= (int __rhs)</code></pre>
<h2>Detailed Description</h2>
<p>3.2.3 Class decimal64. </p>
<p> Definition at line 310 of file decimal.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>std::decimal::decimal64::decimal64 (__decfloat64__z) [inline]</h3>
<p>Conforming extension: Conversion from scalar decimal type. </p>
<p> Definition at line 334 of file decimal.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
