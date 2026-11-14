---
title: "stdbetastdbetafstdbetal(3)"
name: "stdbetastdbetafstdbetal"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbetastdbetafstdbetal/"
description: "std::beta,std::betaf,std::betal – std::beta,std::betaf,std::betal"
---

<p>std::beta,std::betaf,std::betal &#8211; std::beta,std::betaf,std::betal</p>
<h2>Synopsis</h2>
<pre><code>double beta( double x, double y );

float betaf( float x, float y );                   (1) (since C++17)

long double betal( long double x, long double y );

Promoted beta( Arithmetic x, Arithmetic y );       (2) (since C++17)</code></pre>
<p>1) Computes the beta_function of x and y.<br />
2) A set of overloads or a function template for all combinations of arguments of arithmetic type not covered by <code>(1)</code>. If any argument has integral_type, it is cast to double. If any argument is long double, then the return type Promoted is also long double, otherwise the return type is always double. </p>
<h2>Parameters</h2>
<p>x, y &#8211; values of a floating-point or integral type</p>
<h2>Return value</h2>
<p>If no errors occur, value of the beta function of x and y, that is ∫1<br />
0tx-1<br />
(1-t)(y-1)<br />
dt, or, equivalently,<br />
Γ(x)Γ(y)<br />
Γ(x+y)<br />
is returned. </p>
<h2>Error handling</h2>
<p>Errors may be reported as specified in math_errhandling </p>
<p>* If any argument is NaN, NaN is returned and domain error is not reported<br />
* The function is only required to be defined where both x and y are greater than zero, and is allowed to report a domain error otherwise.</p>
<h2>Notes</h2>
<p>Implementations that do not support C++17, but support ISO_29124:2010, provide this function if __STDCPP_MATH_SPEC_FUNCS__ is defined by the implementation to a value at least 201003L and if the user defines __STDCPP_WANT_MATH_SPEC_FUNCS__ before including any standard library headers.<br />
Implementations that do not support ISO 29124:2010 but support TR 19768:2007 (TR1), provide this function in the header tr1/cmath and namespace std::tr1<br />
An implementation of this function is also available_in_boost.math<br />
beta(x, y) equals beta(y, x)<br />
When x and y are positive integers, beta(x,y) equals \(rac{(x-1)!(y-1)!}{(x+y-1)!}\)<br />
(x-1)!(y-1)!<br />
(x+y-1)!<br />
. Binomial coefficients can be expressed in terms of the beta function: \(inom{n}{k} = rac{1}{(n+1)B(n-k+1,k+1)}\)⎛</p>
<p>⎜</p>
<p>⎝n</p>
<p>k⎞</p>
<p>⎟</p>
<p>⎠=<br />
1<br />
(n+1)Β(n-k+1,k+1) </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;cmath&gt;

#include &lt;string&gt;

#include &lt;iostream&gt;

#include &lt;iomanip&gt;

double binom(int n, int k)
{
    return 1 / ((n + 1) * std::beta(n - k + 1, k + 1));
}

int main()

{
    std::cout &lt;&lt; &quot;Pascal's triangle:
&quot;;
    for (int n = 1; n &lt; 10; ++n) {
        std::cout &lt;&lt; std::string(20 - n * 2, ' ');
        for (int k = 1; k &lt; n; ++k)
            std::cout &lt;&lt; std::setw(3) &lt;&lt; binom(n, k) &lt;&lt; ' ';
        std::cout &lt;&lt; '
';
    }
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;Pascal&#8217;s triangle: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;3 3<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;4 6 4<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;5 10 10 5<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;6 15 20 15 6<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;7 21 35 35 21 7<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;8 28 56 70 56 28 8<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;9 36 84 126 126 84 36 9</p>
<h2>See also</h2>
<p>tgamma<br />
tgammaf<br />
tgammal gamma function<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
<h2>External links</h2>
<p>Weisstein,_Eric_W._&quot;Beta_Function.&quot; From MathWorld&#8211;A Wolfram Web Resource.</p>
