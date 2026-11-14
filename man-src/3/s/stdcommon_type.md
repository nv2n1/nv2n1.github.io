---
title: "stdcommon_type(3)"
name: "stdcommon_type"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcommon_type/"
---

std::common_type - std::common_type

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class... T&gt;
    (since C++ 11)

        struct common_type;</code></pre> 
Determines the common type among all types T..., that is the type all T... can be implicitly converted to. If such a type exists (as determined according to the rules below), the member type names that type. Otherwise, there is no member type. 
* If sizeof...(T) is zero, there is no member type. 
* If sizeof...(T) is one (i.e., T... contains only one type T0), the member type names the same type as std::common_type&lt;T0, T0&gt;::type if it exists; otherwise there is no member type. 
* If sizeof...(T) is two (i.e., T... contains exactly two types T1 and T2), *If applying std::decay to at least one of T1 and T2 produces a different type, the member type names the same type as std::common_type&lt;std::decay&lt;T1&gt;::type, std::decay&lt;T2&gt;::type&gt;::type, if it exists;
if not, there is no member type.
      * Otherwise, if there is a user specialization for std::common_type&lt;T1, T2&gt;, that specialization is used;
*Otherwise, if std::decay&lt;decltype(false ? std::declval&lt;T1&gt;() : std::declval&lt;T2&gt;())&gt;::type is a valid type, the member type denotes that type;
 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* Otherwise, if std::decay&lt;decltype(false ? std::declval&lt;const T1 &amp;&gt;() : std::declval&lt;const T2 &amp;&gt;())&gt;::type is a valid type, the member type denotes that type; <i>(since C++20)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* Otherwise, there is no member type. 
* If sizeof...(T) is greater than two (i.e., T... consists of the types T1, T2, R...), then if std::common_type&lt;T1, T2&gt;::type exists, the member type denotes std::common_type&lt;std::common_type&lt;T1, T2&gt;::type, R...&gt;::type if such a type exists. In all other cases, there is no member type. 
The types in the parameter pack T shall each be a complete type, (possibly cv-qualified) void, or an array of unknown bound. Otherwise, the behavior is undefined. 
If an instantiation of a template above depends, directly or indirectly, on an incomplete type, and that instantiation could yield a different result if that type were hypothetically completed, the behavior is undefined. 

<h2>Member types</h2>

Name Definition 
type the common type for all T...

<h2>Helper types</h2>

template&lt; class... T &gt; <i>(since C++14)</i> 
using common_type_t = typename common_type&lt;T...&gt;::type;

<h2>Specializations</h2>

Users may specialize common_type for types T1 and T2 if 

 
* At least one of T1 and T2 depends on a user-defined type, and 
* std::decay is an identity transformation for both T1 and T2. 

 
If such a specialization has a member named type, it must be a public and unambiguous member type that names a cv-unqualified non-reference type to which both T1 and T2 are explicitly convertible. Additionally, std::common_type&lt;T1, T2&gt;::type and std::common_type&lt;T2, T1&gt;::type must denote the same type. 
A program that adds common_type specializations in violation of these rules has undefined behavior. 
Note that the behavior of a program that adds a specialization to any other template from &lt;type_traits&gt; is undefined. 
The following specializations are already provided by the standard library: 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;specializes the std::common_type trait 
std::common_type&lt;std::chrono::duration&gt; <i>(class template specialization)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;specializes the std::common_type trait 
std::common_type&lt;std::chrono::time_point&gt; <i>(class template specialization)</i>

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;// primary template (used for zero types) 
&nbsp;<wbr>&nbsp;template &lt;class ...T&gt; 
&nbsp;<wbr>&nbsp;struct common_type {}; 

 
&nbsp;<wbr>&nbsp;//////// one type 
&nbsp;<wbr>&nbsp;template &lt;class T&gt; 
&nbsp;<wbr>&nbsp;struct common_type&lt;T&gt; : common_type&lt;T, T&gt; {}; 

 
&nbsp;<wbr>&nbsp;//////// two types 

 
&nbsp;<wbr>&nbsp;// default implementation for two types 
&nbsp;<wbr>&nbsp;template&lt;class T1, class T2&gt; 
&nbsp;<wbr>&nbsp;using cond_t = decltype(false ? std::declval&lt;T1&gt;() : std::declval&lt;T2&gt;()); 

 
&nbsp;<wbr>&nbsp;template&lt;class T1, class T2, class=void&gt; 
&nbsp;<wbr>&nbsp;struct common_type_2_default {}; 

 
&nbsp;<wbr>&nbsp;template&lt;class T1, class T2&gt; 
&nbsp;<wbr>&nbsp;struct common_type_2_default&lt;T1, T2, std::void_t&lt;cond_t&lt;T1, T2&gt;&gt;&gt; { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;using type = std::decay_t&lt;cond_t&lt;T1, T2&gt;&gt;; 
&nbsp;<wbr>&nbsp;}; 

 
&nbsp;<wbr>&nbsp;// dispatcher to decay the type before applying specializations 
&nbsp;<wbr>&nbsp;template&lt;class T1, class T2, class D1 = std::decay_t&lt;T1&gt;, class D2=std::decay_t&lt;T2&gt;&gt; 
&nbsp;<wbr>&nbsp;struct common_type_2_impl : common_type&lt;D1, D2&gt; {}; 

 
&nbsp;<wbr>&nbsp;template&lt;class D1, class D2&gt; 
&nbsp;<wbr>&nbsp;struct common_type_2_impl&lt;D1, D2, D1, D2&gt; : common_type_2_default&lt;D1, D2&gt; {}; 

 
&nbsp;<wbr>&nbsp;template &lt;class T1, class T2&gt; 
&nbsp;<wbr>&nbsp;struct common_type&lt;T1, T2&gt; : common_type_2_impl&lt;T1, T2&gt; { }; 

 
&nbsp;<wbr>&nbsp;//////// 3+ types 

 
&nbsp;<wbr>&nbsp;template&lt;class AlwaysVoid, class T1, class T2, class...R&gt; 
&nbsp;<wbr>&nbsp;struct common_type_multi_impl { }; 

 
&nbsp;<wbr>&nbsp;template&lt; class T1, class T2, class...R&gt; 
&nbsp;<wbr>&nbsp;struct common_type_multi_impl&lt;std::void_t&lt;common_type_t&lt;T1, T2&gt;&gt;, T1, T2, R...&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;: common_type&lt;common_type_t&lt;T1, T2&gt;, R...&gt; { }; 

 

 
&nbsp;<wbr>&nbsp;template &lt;class T1, class T2, class... R&gt; 
&nbsp;<wbr>&nbsp;struct common_type&lt;T1, T2, R...&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;: common_type_multi_impl&lt;void, T1, T2, R...&gt; { };

<h2>Notes</h2>

For arithmetic types not subject to promotion, the common type may be viewed as the type of the (possibly mixed-mode) arithmetic expression such as T0() + T1() + ... + Tn(). 
Defect reports 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 
DR Applied to Behavior as published Correct behavior 
LWG_2141 C++11 common_type&lt;int, int&gt;::type is int&amp;&amp; decayed result type 
LWG_2408 C++11 common_type is not SFINAE-friendly made SFINAE-friendly 
LWG_2460 C++11 common_type specializations are nearly impossible to write reduced number of specializations needed 

<h2>Examples</h2>

Demonstrates mixed-mode arithmetic on a user-defined class 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;type_traits&gt;
template &lt;class T&gt;

struct Number {
    T n;
};
template &lt;class T, class U&gt;

Number&lt;typename std::common_type&lt;T, U&gt;::type&gt; operator+(const Number&lt;T&gt; &amp;lhs,
                                                        const Number&lt;U&gt; &amp;rhs)

{
    return {lhs.n + rhs.n};
}
int main()

{
    Number&lt;int&gt; i1 = {1}, i2 = {2};
    Number&lt;double&gt; d1 = {2.3}, d2 = {3.5};
    std::cout &lt;&lt; &quot;i1i2: &quot; &lt;&lt; (i1 + i2).n &lt;&lt; &quot;\ni1d2: &quot; &lt;&lt; (i1 + d2).n &lt;&lt; '\n'
              &lt;&lt; &quot;d1i2: &quot; &lt;&lt; (d1 + i2).n &lt;&lt; &quot;\nd1d2: &quot; &lt;&lt; (d1 + d2).n &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;i1i2: 3 
&nbsp;<wbr>&nbsp;i1d2: 4.5 
&nbsp;<wbr>&nbsp;d1i2: 4.3 
&nbsp;<wbr>&nbsp;d1d2: 5.8
