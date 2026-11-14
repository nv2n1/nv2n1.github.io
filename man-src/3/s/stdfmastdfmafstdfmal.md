---
title: "stdfmastdfmafstdfmal(3)"
name: "stdfmastdfmafstdfmal"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfmastdfmafstdfmal/"
---

std::fma,std::fmaf,std::fmal - std::fma,std::fmaf,std::fmal

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cmath&gt;

    float fma(float x, float y, float z);
(1)(since C++ 11)

    float fmaf(float x, float y, float z);

double fma(double x, double y, double z);
(2)(since C++ 11)

    long double fma(long double x, long double y, long double z);
(3)(since C++ 11)

    long double fmal(long double x, long double y, long double z);

Promoted fma(Arithmetic1 x, Arithmetic2 y, Arithmetic3 z);    (4) (since C++11)

#define FP_FAST_FMA /* implementation-defined */ (5)(since C++ 11)

#define FP_FAST_FMAF /* implementation-defined */ (6)(since C++ 11)

#define FP_FAST_FMAL /* implementation-defined */ (7)(since C++ 11)
1-3) Computes (x*y) + z as if to infinite precision and rounded only once to fit the result type.

4) A set of overloads or a function template for all combinations of arguments of arithmetic_type not covered by 1-3). If any argument has integral_type, it is cast to double. If any other argument is long double, then the return type is long double, otherwise it is double.

5-7) If the macro constants FP_FAST_FMAF, FP_FAST_FMA, or FP_FAST_FMAL are defined, the function std::fma evaluates faster (in addition to being more precise) than the expression x*y+z for float, double, and long double arguments, respectively. If defined, these macros evaluate to integer 1.
</code></pre>

<h2>Parameters</h2>

x, y, z - values of floating-point or integral_types

<h2>Return value</h2>

If successful, returns the value of (x*y) + z as if calculated to infinite precision and rounded once to fit the result type (or, alternatively, calculated as a single ternary floating-point operation) 
If a range error due to overflow occurs, ±HUGE_VAL, ±HUGE_VALF, or ±HUGE_VALL is returned. 
If a range error due to underflow occurs, the correct value (after rounding) is returned. 

<h2>Error handling</h2>

Errors are reported as specified in math_errhandling. 
If the implementation supports IEEE floating-point arithmetic (IEC 60559), 

 
* If x is zero and y is infinite or if x is infinite and y is zero, and z is not a NaN, then NaN is returned and FE_INVALID is raised 
* If x is zero and y is infinite or if x is infinite and y is zero, and z is a NaN, then NaN is returned and FE_INVALID may be raised 
* If x*y is an exact infinity and z is an infinity with the opposite sign, NaN is returned and FE_INVALID is raised 
* If x or y are NaN, NaN is returned 
* If z is NaN, and x*y aren't 0*Inf or Inf*0, then NaN is returned (without FE_INVALID)

<h2>Notes</h2>

This operation is commonly implemented in hardware as fused_multiply-add CPU instruction. If supported by hardware, the appropriate FP_FAST_FMA* macros are expected to be defined, but many implementations make use of the CPU instruction even when the macros are not defined. 
POSIX_additionally_specifies that the situations specified to return FE_INVALID are domain errors. 
Due to its infinite intermediate precision, fma is a common building block of other correctly-rounded mathematical operations, such as std::sqrt or even the division (where not provided by the CPU, e.g. Itanium) 
As with all floating-point expressions, the expression (x*y) + z may be compiled as a fused multiply-add unless the #pragma STDC FP_CONTRACT is off. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;iomanip&gt;

#include &lt;cmath&gt;

#include &lt;cfenv&gt;

#pragma STDC FENV_ACCESS ON

int main()

{
    // demo the difference between fma and built-in operators
    double in = 0.1;
    std::cout &lt;&lt; &quot;0.1 double is &quot; &lt;&lt; std::setprecision(23) &lt;&lt; in
              &lt;&lt; &quot; (&quot; &lt;&lt; std::hexfloat &lt;&lt; in &lt;&lt; std::defaultfloat &lt;&lt; &quot;)\n&quot;
              &lt;&lt; &quot;0.1*10 is 1.0000000000000000555112 (0x8.0000000000002p-3), &quot;
              &lt;&lt; &quot;or 1.0 if rounded to double\n&quot;;
    double expr_result = 0.1 * 10 - 1;
    double fma_result = fma(0.1, 10, -1);
    std::cout &lt;&lt; &quot;0.1 * 10 - 1 = &quot; &lt;&lt; expr_result
              &lt;&lt; &quot; : 1 subtracted after intermediate rounding\n&quot;
              &lt;&lt; &quot;fma(0.1, 10, -1) = &quot; &lt;&lt; std::setprecision(6) &lt;&lt; fma_result &lt;&lt; &quot; (&quot;
              &lt;&lt; std::hexfloat &lt;&lt; fma_result &lt;&lt; std::defaultfloat &lt;&lt; &quot;)\n\n&quot;;
    // fma is used in double-double arithmetic
    double high = 0.1 * 10;
    double low = fma(0.1, 10, -high);
    std::cout &lt;&lt; &quot;in double-double arithmetic, 0.1 * 10 is representable as &quot;
              &lt;&lt; high &lt;&lt; &quot; + &quot; &lt;&lt; low &lt;&lt; &quot;\n\n&quot;;
    // error handling
    std::feclearexcept(FE_ALL_EXCEPT);
    std::cout &lt;&lt; &quot;fma(+Inf, 10, -Inf) = &quot; &lt;&lt; std::fma(INFINITY, 10, -INFINITY) &lt;&lt; '\n';
    if (std::fetestexcept(FE_INVALID))
        std::cout &lt;&lt; &quot;    FE_INVALID raised\n&quot;;
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;0.1 double is 0.10000000000000000555112 (0x1.999999999999ap-4) 
&nbsp;<wbr>&nbsp;0.1*10 is 1.0000000000000000555112 (0x8.0000000000002p-3), or 1.0 if rounded to double 
&nbsp;<wbr>&nbsp;0.1 * 10 - 1 = 0 : 1 subtracted after intermediate rounding 
&nbsp;<wbr>&nbsp;fma(0.1, 10, -1) = 5.55112e-17 (0x1p-54) 

 
&nbsp;<wbr>&nbsp;in double-double arithmetic, 0.1 * 10 is representable as 1 + 5.55112e-17 

 
&nbsp;<wbr>&nbsp;fma(+Inf, 10, -Inf) = -nan 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FE_INVALID raised

<h2>See also</h2>

remainder 
remainderf 
remainderl signed remainder of the division operation 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
remquo 
remquof 
remquol signed remainder as well as the three last bits of the division operation 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
