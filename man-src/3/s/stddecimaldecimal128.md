---
title: "stddecimaldecimal128(3)"
name: "stddecimaldecimal128"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stddecimaldecimal128/"
description: "std::decimal::decimal128 –"
---

<p>std::decimal::decimal128 &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Types</h3>
<p>typedef float __decfloat128 <code>__attribute__</code> ((mode(TD)))</p>
<h3>Public Member Functions</h3>
<pre><code>decimal128 (decimal32 d32)



decimal128 (decimal64 d64)



decimal128 (float __r)



decimal128 (double __r)



decimal128 (long double __r)



decimal128 (int __z)



decimal128 (unsigned int __z)



decimal128 (long __z)



decimal128 (unsigned long __z)



decimal128 (long long __z)



decimal128 (unsigned long long __z)



decimal128 (__decfloat128 __z)



__decfloat128 __getval (void)



void __setval (__decfloat128 __x)



decimal128 &amp; operator*= (decimal32 __rhs)



decimal128 &amp; operator*= (decimal64 __rhs)



decimal128 &amp; operator*= (decimal128 __rhs)



decimal128 &amp; operator*= (int __rhs)



decimal128 &amp; operator*= (unsigned int __rhs)



decimal128 &amp; operator*= (long __rhs)



decimal128 &amp; operator*= (unsigned long __rhs)



decimal128 &amp; operator*= (unsigned long long __rhs)



decimal128 &amp; operator*= (long long __rhs)



decimal128 &amp; operator++ ()



decimal128 operator++ (int)



decimal128 &amp; operator+= (int __rhs)



decimal128 &amp; operator+= (decimal32 __rhs)



decimal128 &amp; operator+= (decimal64 __rhs)



decimal128 &amp; operator+= (decimal128 __rhs)



decimal128 &amp; operator+= (unsigned int __rhs)



decimal128 &amp; operator+= (long __rhs)



decimal128 &amp; operator+= (unsigned long __rhs)



decimal128 &amp; operator+= (long long __rhs)



decimal128 &amp; operator+= (unsigned long long __rhs)



decimal128 &amp; operator-- ()



decimal128 operator-- (int)



decimal128 &amp; operator-= (long __rhs)



decimal128 &amp; operator-= (int __rhs)



decimal128 &amp; operator-= (long long __rhs)



decimal128 &amp; operator-= (unsigned long long __rhs)



decimal128 &amp; operator-= (unsigned long __rhs)



decimal128 &amp; operator-= (decimal128 __rhs)



decimal128 &amp; operator-= (unsigned int __rhs)



decimal128 &amp; operator-= (decimal32 __rhs)



decimal128 &amp; operator-= (decimal64 __rhs)



decimal128 &amp; operator/= (decimal32 __rhs)



decimal128 &amp; operator/= (long long __rhs)



decimal128 &amp; operator/= (unsigned long long __rhs)



decimal128 &amp; operator/= (unsigned long __rhs)



decimal128 &amp; operator/= (decimal64 __rhs)



decimal128 &amp; operator/= (unsigned int __rhs)



decimal128 &amp; operator/= (decimal128 __rhs)



decimal128 &amp; operator/= (long __rhs)



decimal128 &amp; operator/= (int __rhs)</code></pre>
<h2>Detailed Description</h2>
<p>3.2.4 Class decimal128. </p>
<p> Definition at line 393 of file decimal.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>std::decimal::decimal128::decimal128 (__decfloat128__z) [inline]</h3>
<p>Conforming extension: Conversion from scalar decimal type. </p>
<p> Definition at line 418 of file decimal.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
