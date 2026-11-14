---
title: "stdcompare_3way(3)"
name: "stdcompare_3way"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcompare_3way/"
---

std::compare_3way - std::compare_3way

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;algorithm&gt;

    template &lt;class T, class U&gt;
    (since C++ 20)

        constexpr auto compare_3way(const T &amp;a, const U &amp;b);</code></pre> 
Compares two values using three-way comparison and produces a result of the strongest applicable comparison category type.

<h2>In detail:</h2>

* If the expression a &lt;=&gt; b is well-formed, returns its result 
* Otherwise, if the expressions a == b and a &lt; b are both well-formed and convertible to bool, 

 

 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* if a == b equals true, returns std::strong_ordering::equal 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* otherwise, if a &lt; b equals true, returns std::strong_ordering::less 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* otherwise, returns std::strong_ordering::greater 

 

 

 
* Otherwise, if the expression a == b is well-formed and convertible to bool (but a &lt; b is not), 

 

 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* if a == b equals true, returns std::strong_equality::equal 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* otherwise, returns std::strong_equality::nonequal 

 

 

 
* Otherwise (if neither a &lt;=&gt; b nor a == b are well-formed), the function is defined as deleted.

<h2>Parameters</h2>

a, b - the values to compare

<h2>Return value</h2>

As defined above. 

<h2>Notes</h2>

This function is useful in generic programming, since it uses &lt; and == as fallbacks when &lt;=&gt; is not available. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;compare&gt;

#include &lt;algorithm&gt;
// does not support &lt;=&gt;

struct Rational_1 {
    int num;
    int den; // &gt; 0
};
inline constexpr bool operator&lt;(Rational_1 lhs, Rational_1 rhs)

{
    return lhs.num * rhs.den &lt; rhs.num * lhs.den;
}
inline constexpr bool operator==(Rational_1 lhs, Rational_1 rhs)

{
    return lhs.num * rhs.den == rhs.num * lhs.den;
}
// supports &lt;=&gt;

struct Rational_2 {
    int num;
    int den; // &gt; 0
};
inline constexpr std::weak_ordering operator&lt;=&gt;(Rational_2 lhs, Rational_2 rhs)

{
    return lhs.num * rhs.den &lt;=&gt; rhs.num * lhs.den;
}
void print(std::weak_ordering value)

{
    if (value == 0)
        std::cout &lt;&lt; &quot;equal&quot;;
    else if (value &lt; 0)
        std::cout &lt;&lt; &quot;less&quot;;
    else
        std::cout &lt;&lt; &quot;greater&quot;;
    std::cout &lt;&lt; &quot;\n&quot;;
}
int main()

{
    Rational_1 a{1, 2};
    Rational_1 b{3, 4};

    //  print(a &lt;=&gt; b);                //doesn't work
    print(std::compare_3way(a, b)); // works, defaults to &lt; and ==
    Rational_2 c{6, 5};
    Rational_2 d{8, 7};
    print(c &lt;=&gt; d);                 // works
    print(std::compare_3way(c, d)); // works
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;less 
&nbsp;<wbr>&nbsp;greater 
&nbsp;<wbr>&nbsp;greater

<h2>See also</h2>

lexicographical_compare_3way compares two ranges using three-way comparison 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(C++20) 
strong_equality the result type of 3-way comparison that supports only equality/inequality and is substitutable 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
(C++20) 
weak_equality the result type of 3-way comparison that supports only equality/inequality and is not substitutable 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
(C++20) 
strong_ordering the result type of 3-way comparison that supports all 6 operators and is substitutable 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
(C++20) 
weak_ordering the result type of 3-way comparison that supports all 6 operators and is not substitutable 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
(C++20) 
partial_ordering the result type of 3-way comparison that supports all 6 operators, is not substitutable, and allows incomparable values 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
(C++20) 
