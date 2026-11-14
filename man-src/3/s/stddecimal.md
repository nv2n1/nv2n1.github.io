---
title: "stddecimal(3)"
name: "stddecimal"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stddecimal/"
description: "std::decimal –"
---

<p>std::decimal &#8211;</p>
<h2>Synopsis</h2>
<h3>Classes</h3>
<p>class <code>decimal128</code> </p>
<p> class <code>decimal32</code> </p>
<p> class <code>decimal64</code></p>
<h3>Functions</h3>
<pre><code>double decimal128_to_double (decimal128 __d)



float decimal128_to_float (decimal128 __d)



long double decimal128_to_long_double (decimal128 __d)



long long decimal128_to_long_long (decimal128 __d)



double decimal32_to_double (decimal32 __d)



float decimal32_to_float (decimal32 __d)



long double decimal32_to_long_double (decimal32 __d)



long long decimal32_to_long_long (decimal32 __d)



double decimal64_to_double (decimal64 __d)



float decimal64_to_float (decimal64 __d)



long double decimal64_to_long_double (decimal64 __d)



long long decimal64_to_long_long (decimal64 __d)



double decimal_to_double (decimal32 __d)



double decimal_to_double (decimal64 __d)



double decimal_to_double (decimal128 __d)



float decimal_to_float (decimal32 __d)



float decimal_to_float (decimal64 __d)



float decimal_to_float (decimal128 __d)



long double decimal_to_long_double (decimal32 __d)



long double decimal_to_long_double (decimal64 __d)



long double decimal_to_long_double (decimal128 __d)



long long decimal_to_long_long (decimal32 __d)



long long decimal_to_long_long (decimal64 __d)



long long decimal_to_long_long (decimal128 __d)



static decimal128 make_decimal128 (long long __coeff, int __exp)



static decimal128 make_decimal128 (unsigned long long __coeff, int __exp)



static decimal32 make_decimal32 (long long __coeff, int __exp)



static decimal32 make_decimal32 (unsigned long long __coeff, int __exp)



static decimal64 make_decimal64 (long long __coeff, int __exp)



static decimal64 make_decimal64 (unsigned long long __coeff, int __exp)



bool operator!= (decimal32 __lhs, decimal32 __rhs)



bool operator!= (decimal32 __lhs, decimal64 __rhs)



bool operator!= (decimal32 __lhs, decimal128 __rhs)



bool operator!= (decimal32 __lhs, int __rhs)



bool operator!= (decimal32 __lhs, unsigned int __rhs)



bool operator!= (decimal32 __lhs, long __rhs)



bool operator!= (decimal32 __lhs, unsigned long __rhs)



bool operator!= (decimal32 __lhs, long long __rhs)



bool operator!= (decimal32 __lhs, unsigned long long __rhs)



bool operator!= (int __lhs, decimal32 __rhs)



bool operator!= (unsigned int __lhs, decimal32 __rhs)



bool operator!= (long __lhs, decimal32 __rhs)



bool operator!= (unsigned long __lhs, decimal32 __rhs)



bool operator!= (long long __lhs, decimal32 __rhs)



bool operator!= (unsigned long long __lhs, decimal32 __rhs)



bool operator!= (decimal64 __lhs, decimal32 __rhs)



bool operator!= (decimal64 __lhs, decimal64 __rhs)



bool operator!= (decimal64 __lhs, decimal128 __rhs)



bool operator!= (decimal64 __lhs, int __rhs)



bool operator!= (decimal64 __lhs, unsigned int __rhs)



bool operator!= (decimal64 __lhs, long __rhs)



bool operator!= (decimal64 __lhs, unsigned long __rhs)



bool operator!= (decimal64 __lhs, long long __rhs)



bool operator!= (decimal64 __lhs, unsigned long long __rhs)



bool operator!= (int __lhs, decimal64 __rhs)



bool operator!= (unsigned int __lhs, decimal64 __rhs)



bool operator!= (long __lhs, decimal64 __rhs)



bool operator!= (unsigned long __lhs, decimal64 __rhs)



bool operator!= (long long __lhs, decimal64 __rhs)



bool operator!= (unsigned long long __lhs, decimal64 __rhs)



bool operator!= (decimal128 __lhs, decimal32 __rhs)



bool operator!= (decimal128 __lhs, decimal64 __rhs)



bool operator!= (decimal128 __lhs, decimal128 __rhs)



bool operator!= (decimal128 __lhs, int __rhs)



bool operator!= (decimal128 __lhs, unsigned int __rhs)



bool operator!= (decimal128 __lhs, long __rhs)



bool operator!= (decimal128 __lhs, unsigned long __rhs)



bool operator!= (decimal128 __lhs, long long __rhs)



bool operator!= (decimal128 __lhs, unsigned long long __rhs)



bool operator!= (int __lhs, decimal128 __rhs)



bool operator!= (unsigned int __lhs, decimal128 __rhs)



bool operator!= (long __lhs, decimal128 __rhs)



bool operator!= (unsigned long __lhs, decimal128 __rhs)



bool operator!= (long long __lhs, decimal128 __rhs)



bool operator!= (unsigned long long __lhs, decimal128 __rhs)



decimal32 operator* (decimal32 __lhs, decimal32 __rhs)



decimal32 operator* (decimal32 __lhs, unsigned int __rhs)



decimal32 operator* (decimal32 __lhs, int __rhs)



decimal32 operator* (decimal32 __lhs, unsigned long __rhs)



decimal32 operator* (decimal32 __lhs, long __rhs)



decimal32 operator* (decimal32 __lhs, long long __rhs)



decimal32 operator* (decimal32 __lhs, unsigned long long __rhs)



decimal32 operator* (int __lhs, decimal32 __rhs)



decimal32 operator* (unsigned int __lhs, decimal32 __rhs)



decimal32 operator* (long __lhs, decimal32 __rhs)



decimal32 operator* (unsigned long __lhs, decimal32 __rhs)



decimal32 operator* (long long __lhs, decimal32 __rhs)



decimal32 operator* (unsigned long long __lhs, decimal32 __rhs)



decimal64 operator* (decimal32 __lhs, decimal64 __rhs)



decimal64 operator* (decimal64 __lhs, decimal32 __rhs)



decimal64 operator* (decimal64 __lhs, decimal64 __rhs)



decimal64 operator* (decimal64 __lhs, int __rhs)



decimal64 operator* (decimal64 __lhs, unsigned int __rhs)



decimal64 operator* (decimal64 __lhs, long __rhs)



decimal64 operator* (decimal64 __lhs, unsigned long __rhs)



decimal64 operator* (decimal64 __lhs, long long __rhs)



decimal64 operator* (decimal64 __lhs, unsigned long long __rhs)



decimal64 operator* (int __lhs, decimal64 __rhs)



decimal64 operator* (unsigned int __lhs, decimal64 __rhs)



decimal64 operator* (long __lhs, decimal64 __rhs)



decimal64 operator* (unsigned long __lhs, decimal64 __rhs)



decimal64 operator* (long long __lhs, decimal64 __rhs)



decimal64 operator* (unsigned long long __lhs, decimal64 __rhs)



decimal128 operator* (decimal32 __lhs, decimal128 __rhs)



decimal128 operator* (decimal64 __lhs, decimal128 __rhs)



decimal128 operator* (decimal128 __lhs, decimal32 __rhs)



decimal128 operator* (decimal128 __lhs, decimal64 __rhs)



decimal128 operator* (decimal128 __lhs, decimal128 __rhs)



decimal128 operator* (decimal128 __lhs, int __rhs)



decimal128 operator* (decimal128 __lhs, unsigned int __rhs)



decimal128 operator* (decimal128 __lhs, long __rhs)



decimal128 operator* (decimal128 __lhs, unsigned long __rhs)



decimal128 operator* (decimal128 __lhs, long long __rhs)



decimal128 operator* (decimal128 __lhs, unsigned long long __rhs)



decimal128 operator* (int __lhs, decimal128 __rhs)



decimal128 operator* (unsigned int __lhs, decimal128 __rhs)



decimal128 operator* (long __lhs, decimal128 __rhs)



decimal128 operator* (unsigned long __lhs, decimal128 __rhs)



decimal128 operator* (long long __lhs, decimal128 __rhs)



decimal128 operator* (unsigned long long __lhs, decimal128 __rhs)



decimal32 operator+ (decimal32 __rhs)



decimal64 operator+ (decimal64 __rhs)



decimal128 operator+ (decimal128 __rhs)



decimal32 operator+ (decimal32 __lhs, decimal32 __rhs)



decimal32 operator+ (decimal32 __lhs, int __rhs)



decimal32 operator+ (decimal32 __lhs, unsigned int __rhs)



decimal32 operator+ (decimal32 __lhs, long __rhs)



decimal32 operator+ (decimal32 __lhs, unsigned long __rhs)



decimal32 operator+ (decimal32 __lhs, long long __rhs)



decimal32 operator+ (decimal32 __lhs, unsigned long long __rhs)



decimal32 operator+ (int __lhs, decimal32 __rhs)



decimal32 operator+ (unsigned int __lhs, decimal32 __rhs)



decimal32 operator+ (long __lhs, decimal32 __rhs)



decimal32 operator+ (unsigned long __lhs, decimal32 __rhs)



decimal32 operator+ (long long __lhs, decimal32 __rhs)



decimal32 operator+ (unsigned long long __lhs, decimal32 __rhs)



decimal64 operator+ (decimal32 __lhs, decimal64 __rhs)



decimal64 operator+ (decimal64 __lhs, decimal32 __rhs)



decimal64 operator+ (decimal64 __lhs, decimal64 __rhs)



decimal64 operator+ (unsigned long long __lhs, decimal64 __rhs)



decimal64 operator+ (decimal64 __lhs, int __rhs)



decimal64 operator+ (decimal64 __lhs, unsigned int __rhs)



decimal64 operator+ (decimal64 __lhs, long __rhs)



decimal64 operator+ (decimal64 __lhs, unsigned long __rhs)



decimal64 operator+ (decimal64 __lhs, long long __rhs)



decimal64 operator+ (decimal64 __lhs, unsigned long long __rhs)



decimal64 operator+ (int __lhs, decimal64 __rhs)



decimal64 operator+ (unsigned int __lhs, decimal64 __rhs)



decimal64 operator+ (long __lhs, decimal64 __rhs)



decimal64 operator+ (unsigned long __lhs, decimal64 __rhs)



decimal64 operator+ (long long __lhs, decimal64 __rhs)



decimal128 operator+ (decimal32 __lhs, decimal128 __rhs)



decimal128 operator+ (decimal64 __lhs, decimal128 __rhs)



decimal128 operator+ (decimal128 __lhs, decimal32 __rhs)



decimal128 operator+ (decimal128 __lhs, decimal64 __rhs)



decimal128 operator+ (decimal128 __lhs, decimal128 __rhs)



decimal128 operator+ (decimal128 __lhs, int __rhs)



decimal128 operator+ (decimal128 __lhs, unsigned int __rhs)



decimal128 operator+ (decimal128 __lhs, long __rhs)



decimal128 operator+ (decimal128 __lhs, unsigned long __rhs)



decimal128 operator+ (decimal128 __lhs, long long __rhs)



decimal128 operator+ (decimal128 __lhs, unsigned long long __rhs)



decimal128 operator+ (int __lhs, decimal128 __rhs)



decimal128 operator+ (unsigned int __lhs, decimal128 __rhs)



decimal128 operator+ (long __lhs, decimal128 __rhs)



decimal128 operator+ (unsigned long __lhs, decimal128 __rhs)



decimal128 operator+ (long long __lhs, decimal128 __rhs)



decimal128 operator+ (unsigned long long __lhs, decimal128 __rhs)



decimal32 operator- (decimal32 __rhs)



decimal64 operator- (decimal64 __rhs)



decimal128 operator- (decimal128 __rhs)



decimal32 operator- (decimal32 __lhs, decimal32 __rhs)



decimal32 operator- (decimal32 __lhs, int __rhs)



decimal32 operator- (decimal32 __lhs, unsigned int __rhs)



decimal32 operator- (decimal32 __lhs, long __rhs)



decimal32 operator- (decimal32 __lhs, unsigned long __rhs)



decimal32 operator- (decimal32 __lhs, long long __rhs)



decimal32 operator- (decimal32 __lhs, unsigned long long __rhs)



decimal32 operator- (int __lhs, decimal32 __rhs)



decimal32 operator- (unsigned int __lhs, decimal32 __rhs)



decimal32 operator- (long __lhs, decimal32 __rhs)



decimal32 operator- (unsigned long __lhs, decimal32 __rhs)



decimal32 operator- (long long __lhs, decimal32 __rhs)



decimal32 operator- (unsigned long long __lhs, decimal32 __rhs)



decimal64 operator- (decimal32 __lhs, decimal64 __rhs)



decimal64 operator- (decimal64 __lhs, decimal32 __rhs)



decimal64 operator- (decimal64 __lhs, decimal64 __rhs)



decimal64 operator- (decimal64 __lhs, int __rhs)



decimal64 operator- (decimal64 __lhs, unsigned int __rhs)



decimal64 operator- (decimal64 __lhs, long __rhs)



decimal64 operator- (decimal64 __lhs, unsigned long __rhs)



decimal64 operator- (decimal64 __lhs, long long __rhs)



decimal64 operator- (decimal64 __lhs, unsigned long long __rhs)



decimal64 operator- (int __lhs, decimal64 __rhs)



decimal64 operator- (unsigned int __lhs, decimal64 __rhs)



decimal64 operator- (long __lhs, decimal64 __rhs)



decimal64 operator- (unsigned long __lhs, decimal64 __rhs)



decimal64 operator- (long long __lhs, decimal64 __rhs)



decimal64 operator- (unsigned long long __lhs, decimal64 __rhs)



decimal128 operator- (decimal32 __lhs, decimal128 __rhs)



decimal128 operator- (decimal64 __lhs, decimal128 __rhs)



decimal128 operator- (decimal128 __lhs, decimal32 __rhs)



decimal128 operator- (decimal128 __lhs, decimal64 __rhs)



decimal128 operator- (decimal128 __lhs, decimal128 __rhs)



decimal128 operator- (decimal128 __lhs, int __rhs)



decimal128 operator- (decimal128 __lhs, unsigned int __rhs)



decimal128 operator- (decimal128 __lhs, long __rhs)



decimal128 operator- (decimal128 __lhs, unsigned long __rhs)



decimal128 operator- (decimal128 __lhs, long long __rhs)



decimal128 operator- (decimal128 __lhs, unsigned long long __rhs)



decimal128 operator- (int __lhs, decimal128 __rhs)



decimal128 operator- (unsigned int __lhs, decimal128 __rhs)



decimal128 operator- (long __lhs, decimal128 __rhs)



decimal128 operator- (unsigned long __lhs, decimal128 __rhs)



decimal128 operator- (long long __lhs, decimal128 __rhs)



decimal128 operator- (unsigned long long __lhs, decimal128 __rhs)



decimal32 operator/ (decimal32 __lhs, decimal32 __rhs)



decimal32 operator/ (decimal32 __lhs, int __rhs)



decimal32 operator/ (decimal32 __lhs, unsigned int __rhs)



decimal32 operator/ (decimal32 __lhs, long __rhs)



decimal32 operator/ (decimal32 __lhs, unsigned long __rhs)



decimal32 operator/ (decimal32 __lhs, long long __rhs)



decimal32 operator/ (decimal32 __lhs, unsigned long long __rhs)



decimal32 operator/ (int __lhs, decimal32 __rhs)



decimal32 operator/ (unsigned int __lhs, decimal32 __rhs)



decimal32 operator/ (long __lhs, decimal32 __rhs)



decimal32 operator/ (unsigned long __lhs, decimal32 __rhs)



decimal32 operator/ (long long __lhs, decimal32 __rhs)



decimal32 operator/ (unsigned long long __lhs, decimal32 __rhs)



decimal64 operator/ (decimal32 __lhs, decimal64 __rhs)



decimal64 operator/ (decimal64 __lhs, decimal32 __rhs)



decimal64 operator/ (decimal64 __lhs, decimal64 __rhs)



decimal64 operator/ (decimal64 __lhs, int __rhs)



decimal64 operator/ (decimal64 __lhs, unsigned int __rhs)



decimal64 operator/ (decimal64 __lhs, long __rhs)



decimal64 operator/ (decimal64 __lhs, unsigned long __rhs)



decimal64 operator/ (decimal64 __lhs, long long __rhs)



decimal64 operator/ (decimal64 __lhs, unsigned long long __rhs)



decimal64 operator/ (int __lhs, decimal64 __rhs)



decimal64 operator/ (unsigned int __lhs, decimal64 __rhs)



decimal64 operator/ (long __lhs, decimal64 __rhs)



decimal64 operator/ (unsigned long __lhs, decimal64 __rhs)



decimal64 operator/ (long long __lhs, decimal64 __rhs)



decimal64 operator/ (unsigned long long __lhs, decimal64 __rhs)



decimal128 operator/ (decimal32 __lhs, decimal128 __rhs)



decimal128 operator/ (decimal64 __lhs, decimal128 __rhs)



decimal128 operator/ (decimal128 __lhs, decimal32 __rhs)



decimal128 operator/ (decimal128 __lhs, decimal64 __rhs)



decimal128 operator/ (decimal128 __lhs, decimal128 __rhs)



decimal128 operator/ (decimal128 __lhs, long __rhs)



decimal128 operator/ (long long __lhs, decimal128 __rhs)



decimal128 operator/ (decimal128 __lhs, int __rhs)



decimal128 operator/ (decimal128 __lhs, unsigned int __rhs)



decimal128 operator/ (decimal128 __lhs, unsigned long __rhs)



decimal128 operator/ (decimal128 __lhs, long long __rhs)



decimal128 operator/ (decimal128 __lhs, unsigned long long __rhs)



decimal128 operator/ (int __lhs, decimal128 __rhs)



decimal128 operator/ (unsigned int __lhs, decimal128 __rhs)



decimal128 operator/ (long __lhs, decimal128 __rhs)



decimal128 operator/ (unsigned long __lhs, decimal128 __rhs)



decimal128 operator/ (unsigned long long __lhs, decimal128 __rhs)



bool operator&lt; (unsigned long __lhs, decimal32 __rhs)



bool operator&lt; (decimal32 __lhs, decimal32 __rhs)



bool operator&lt; (decimal32 __lhs, decimal64 __rhs)



bool operator&lt; (decimal32 __lhs, decimal128 __rhs)



bool operator&lt; (decimal32 __lhs, int __rhs)



bool operator&lt; (decimal32 __lhs, long __rhs)



bool operator&lt; (decimal32 __lhs, unsigned long __rhs)



bool operator&lt; (decimal32 __lhs, long long __rhs)



bool operator&lt; (int __lhs, decimal32 __rhs)



bool operator&lt; (long __lhs, decimal32 __rhs)



bool operator&lt; (decimal32 __lhs, unsigned long long __rhs)



bool operator&lt; (long long __lhs, decimal32 __rhs)



bool operator&lt; (unsigned long long __lhs, decimal32 __rhs)



bool operator&lt; (unsigned int __lhs, decimal32 __rhs)



bool operator&lt; (decimal32 __lhs, unsigned int __rhs)



bool operator&lt; (long __lhs, decimal64 __rhs)



bool operator&lt; (unsigned long __lhs, decimal64 __rhs)



bool operator&lt; (decimal64 __lhs, decimal64 __rhs)



bool operator&lt; (unsigned long long __lhs, decimal64 __rhs)



bool operator&lt; (long long __lhs, decimal64 __rhs)



bool operator&lt; (decimal64 __lhs, decimal32 __rhs)



bool operator&lt; (decimal64 __lhs, decimal128 __rhs)



bool operator&lt; (decimal64 __lhs, unsigned int __rhs)



bool operator&lt; (decimal64 __lhs, int __rhs)



bool operator&lt; (int __lhs, decimal64 __rhs)



bool operator&lt; (unsigned int __lhs, decimal64 __rhs)



bool operator&lt; (decimal64 __lhs, long long __rhs)



bool operator&lt; (decimal64 __lhs, long __rhs)



bool operator&lt; (decimal64 __lhs, unsigned long __rhs)



bool operator&lt; (decimal64 __lhs, unsigned long long __rhs)



bool operator&lt; (unsigned long __lhs, decimal128 __rhs)



bool operator&lt; (decimal128 __lhs, unsigned long long __rhs)



bool operator&lt; (decimal128 __lhs, unsigned int __rhs)



bool operator&lt; (unsigned long long __lhs, decimal128 __rhs)



bool operator&lt; (decimal128 __lhs, decimal32 __rhs)



bool operator&lt; (int __lhs, decimal128 __rhs)



bool operator&lt; (unsigned int __lhs, decimal128 __rhs)



bool operator&lt; (long long __lhs, decimal128 __rhs)



bool operator&lt; (long __lhs, decimal128 __rhs)



bool operator&lt; (decimal128 __lhs, unsigned long __rhs)



bool operator&lt; (decimal128 __lhs, int __rhs)



bool operator&lt; (decimal128 __lhs, decimal64 __rhs)



bool operator&lt; (decimal128 __lhs, long __rhs)



bool operator&lt; (decimal128 __lhs, decimal128 __rhs)



bool operator&lt; (decimal128 __lhs, long long __rhs)



bool operator== (decimal32 __lhs, unsigned long __rhs)



bool operator== (decimal32 __lhs, decimal128 __rhs)



bool operator== (decimal32 __lhs, decimal32 __rhs)



bool operator== (decimal32 __lhs, decimal64 __rhs)



bool operator== (decimal32 __lhs, int __rhs)



bool operator== (decimal32 __lhs, unsigned int __rhs)



bool operator== (decimal32 __lhs, long __rhs)



bool operator== (decimal32 __lhs, long long __rhs)



bool operator== (decimal32 __lhs, unsigned long long __rhs)



bool operator== (int __lhs, decimal32 __rhs)



bool operator== (unsigned int __lhs, decimal32 __rhs)



bool operator== (long __lhs, decimal32 __rhs)



bool operator== (unsigned long __lhs, decimal32 __rhs)



bool operator== (long long __lhs, decimal32 __rhs)



bool operator== (unsigned long long __lhs, decimal32 __rhs)



bool operator== (unsigned long long __lhs, decimal64 __rhs)



bool operator== (long __lhs, decimal64 __rhs)



bool operator== (decimal64 __lhs, long long __rhs)



bool operator== (decimal64 __lhs, unsigned int __rhs)



bool operator== (decimal64 __lhs, decimal128 __rhs)



bool operator== (long long __lhs, decimal64 __rhs)



bool operator== (decimal64 __lhs, int __rhs)



bool operator== (decimal64 __lhs, long __rhs)



bool operator== (decimal64 __lhs, decimal32 __rhs)



bool operator== (decimal64 __lhs, decimal64 __rhs)



bool operator== (decimal64 __lhs, unsigned long __rhs)



bool operator== (decimal64 __lhs, unsigned long long __rhs)



bool operator== (int __lhs, decimal64 __rhs)



bool operator== (unsigned int __lhs, decimal64 __rhs)



bool operator== (unsigned long __lhs, decimal64 __rhs)



bool operator== (int __lhs, decimal128 __rhs)



bool operator== (unsigned int __lhs, decimal128 __rhs)



bool operator== (long __lhs, decimal128 __rhs)



bool operator== (long long __lhs, decimal128 __rhs)



bool operator== (unsigned long long __lhs, decimal128 __rhs)



bool operator== (unsigned long __lhs, decimal128 __rhs)



bool operator== (decimal128 __lhs, decimal32 __rhs)



bool operator== (decimal128 __lhs, unsigned int __rhs)



bool operator== (decimal128 __lhs, unsigned long long __rhs)



bool operator== (decimal128 __lhs, unsigned long __rhs)



bool operator== (decimal128 __lhs, decimal128 __rhs)



bool operator== (decimal128 __lhs, long long __rhs)



bool operator== (decimal128 __lhs, decimal64 __rhs)



bool operator== (decimal128 __lhs, int __rhs)



bool operator== (decimal128 __lhs, long __rhs)



bool operator&gt; (unsigned int __lhs, decimal32 __rhs)



bool operator&gt; (long __lhs, decimal32 __rhs)



bool operator&gt; (decimal32 __lhs, decimal128 __rhs)



bool operator&gt; (decimal32 __lhs, long long __rhs)



bool operator&gt; (decimal32 __lhs, unsigned long long __rhs)



bool operator&gt; (decimal32 __lhs, unsigned long __rhs)



bool operator&gt; (decimal32 __lhs, decimal32 __rhs)



bool operator&gt; (decimal32 __lhs, decimal64 __rhs)



bool operator&gt; (decimal32 __lhs, long __rhs)



bool operator&gt; (unsigned long __lhs, decimal32 __rhs)



bool operator&gt; (unsigned long long __lhs, decimal32 __rhs)



bool operator&gt; (long long __lhs, decimal32 __rhs)



bool operator&gt; (decimal32 __lhs, unsigned int __rhs)



bool operator&gt; (int __lhs, decimal32 __rhs)



bool operator&gt; (decimal32 __lhs, int __rhs)



bool operator&gt; (decimal64 __lhs, unsigned long long __rhs)



bool operator&gt; (decimal64 __lhs, decimal32 __rhs)



bool operator&gt; (unsigned long __lhs, decimal64 __rhs)



bool operator&gt; (unsigned long long __lhs, decimal64 __rhs)



bool operator&gt; (long long __lhs, decimal64 __rhs)



bool operator&gt; (int __lhs, decimal64 __rhs)



bool operator&gt; (decimal64 __lhs, unsigned int __rhs)



bool operator&gt; (decimal64 __lhs, unsigned long __rhs)



bool operator&gt; (decimal64 __lhs, decimal128 __rhs)



bool operator&gt; (decimal64 __lhs, long __rhs)



bool operator&gt; (decimal64 __lhs, long long __rhs)



bool operator&gt; (decimal64 __lhs, decimal64 __rhs)



bool operator&gt; (decimal64 __lhs, int __rhs)



bool operator&gt; (long __lhs, decimal64 __rhs)



bool operator&gt; (unsigned int __lhs, decimal64 __rhs)



bool operator&gt; (decimal128 __lhs, decimal128 __rhs)



bool operator&gt; (int __lhs, decimal128 __rhs)



bool operator&gt; (decimal128 __lhs, unsigned long __rhs)



bool operator&gt; (unsigned long long __lhs, decimal128 __rhs)



bool operator&gt; (decimal128 __lhs, unsigned int __rhs)



bool operator&gt; (unsigned int __lhs, decimal128 __rhs)



bool operator&gt; (decimal128 __lhs, decimal32 __rhs)



bool operator&gt; (decimal128 __lhs, unsigned long long __rhs)



bool operator&gt; (decimal128 __lhs, long __rhs)



bool operator&gt; (unsigned long __lhs, decimal128 __rhs)



bool operator&gt; (decimal128 __lhs, int __rhs)



bool operator&gt; (long long __lhs, decimal128 __rhs)



bool operator&gt; (long __lhs, decimal128 __rhs)



bool operator&gt; (decimal128 __lhs, decimal64 __rhs)



bool operator&gt; (decimal128 __lhs, long long __rhs)



bool operator&gt;= (long long __lhs, decimal32 __rhs)



bool operator&gt;= (unsigned long __lhs, decimal32 __rhs)



bool operator&gt;= (decimal32 __lhs, decimal64 __rhs)



bool operator&gt;= (decimal32 __lhs, unsigned int __rhs)



bool operator&gt;= (decimal32 __lhs, decimal32 __rhs)



bool operator&gt;= (decimal32 __lhs, int __rhs)



bool operator&gt;= (decimal32 __lhs, decimal128 __rhs)



bool operator&gt;= (unsigned long long __lhs, decimal32 __rhs)



bool operator&gt;= (unsigned int __lhs, decimal32 __rhs)



bool operator&gt;= (long __lhs, decimal32 __rhs)



bool operator&gt;= (decimal32 __lhs, unsigned long long __rhs)



bool operator&gt;= (decimal32 __lhs, long long __rhs)



bool operator&gt;= (int __lhs, decimal32 __rhs)



bool operator&gt;= (decimal32 __lhs, long __rhs)



bool operator&gt;= (decimal32 __lhs, unsigned long __rhs)



bool operator&gt;= (unsigned long long __lhs, decimal64 __rhs)



bool operator&gt;= (decimal64 __lhs, unsigned long long __rhs)



bool operator&gt;= (decimal64 __lhs, long long __rhs)



bool operator&gt;= (decimal64 __lhs, decimal64 __rhs)



bool operator&gt;= (decimal64 __lhs, decimal32 __rhs)



bool operator&gt;= (decimal64 __lhs, unsigned int __rhs)



bool operator&gt;= (decimal64 __lhs, unsigned long __rhs)



bool operator&gt;= (decimal64 __lhs, decimal128 __rhs)



bool operator&gt;= (long __lhs, decimal64 __rhs)



bool operator&gt;= (decimal64 __lhs, long __rhs)



bool operator&gt;= (unsigned int __lhs, decimal64 __rhs)



bool operator&gt;= (decimal64 __lhs, int __rhs)



bool operator&gt;= (unsigned long __lhs, decimal64 __rhs)



bool operator&gt;= (int __lhs, decimal64 __rhs)



bool operator&gt;= (long long __lhs, decimal64 __rhs)



bool operator&gt;= (decimal128 __lhs, int __rhs)



bool operator&gt;= (int __lhs, decimal128 __rhs)



bool operator&gt;= (decimal128 __lhs, unsigned long __rhs)



bool operator&gt;= (long long __lhs, decimal128 __rhs)



bool operator&gt;= (decimal128 __lhs, decimal64 __rhs)



bool operator&gt;= (unsigned long __lhs, decimal128 __rhs)



bool operator&gt;= (decimal128 __lhs, decimal32 __rhs)



bool operator&gt;= (decimal128 __lhs, long __rhs)



bool operator&gt;= (decimal128 __lhs, unsigned int __rhs)



bool operator&gt;= (decimal128 __lhs, long long __rhs)



bool operator&gt;= (decimal128 __lhs, decimal128 __rhs)



bool operator&gt;= (unsigned int __lhs, decimal128 __rhs)



bool operator&gt;= (decimal128 __lhs, unsigned long long __rhs)



bool operator&gt;= (long __lhs, decimal128 __rhs)



bool operator&gt;= (unsigned long long __lhs, decimal128 __rhs)</code></pre>
<h2>Detailed Description</h2>
<p>ISO/IEC TR 24733 Decimal floating-point arithmetic.</p>
<h2>Function Documentation</h2>
<h3>long long std::decimal::decimal32_to_long_long (decimal32__d)</h3>
<p>Non-conforming extension: Conversion to integral type.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
