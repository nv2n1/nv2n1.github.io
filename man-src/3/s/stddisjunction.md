---
title: "stddisjunction(3)"
name: "stddisjunction"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stddisjunction/"
---

std::disjunction - std::disjunction

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class... B&gt;
    (1)(since C++ 17)

        struct disjunction;</code></pre> 
Forms the logical_disjunction of the type traits B..., effectively performing a logical OR on the sequence of traits. 
The specialization std::disjunction&lt;B1, ..., BN&gt; has a public and unambiguous base that is 
* if sizeof...(B) == 0, std::false_type; otherwise 
* the first type Bi in B1, ..., BN for which bool(Bi::value) == true, or BN if there is no such type. 
The member names of the base class, other than disjunction and operator=, are not hidden and are unambiguously available in disjunction. 
Disjunction is short-circuiting: if there is a template type argument Bi with bool(Bi::value) != false, then instantiating disjunction&lt;B1, ..., BN&gt;::value does not require the instantiation of Bj::value for j &gt; i 

<h2>Template parameters</h2>

B... - every template argument Bi for which Bi::value is instantiated must be usable as a base class and define member value that is convertible to bool 

 

 
Helper variable template 

 

 
template&lt;class... B&gt; <i>(since C++17)</i> 
inline constexpr bool disjunction_v = disjunction&lt;B...&gt;::value;

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt;class...&gt; struct disjunction : std::false_type { }; 
&nbsp;<wbr>&nbsp;template&lt;class B1&gt; struct disjunction&lt;B1&gt; : B1 { }; 
&nbsp;<wbr>&nbsp;template&lt;class B1, class... Bn&gt; 
&nbsp;<wbr>&nbsp;struct disjunction&lt;B1, Bn...&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;: std::conditional_t&lt;bool(B1::value), B1, disjunction&lt;Bn...&gt;&gt; { };

<h2>Notes</h2>

A specialization of disjunction does not necessarily inherit from of either std::true_type or std::false_type: it simply inherits from the first B whose ::value, explicitly converted to bool, is true, or from the very last B when all of them convert to false. For example, std::disjunction&lt;std::integral_constant&lt;int, 2&gt;, std::integral_constant&lt;int, 4&gt;&gt;::value is 2. 
The short-circuit instantiation differentiates disjunction from fold expressions: a fold expression like (... || Bs::value) instantiates every B in Bs, while std::disjunction_v&lt;Bs...&gt; stops instantiation once the value can be determined. This is particularly useful if the later type is expensive to instantiate or can cause a hard error when instantiated with the wrong type. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;type_traits&gt;

#include &lt;string&gt;
// checking if Foo is constructible from double will cause a hard error

struct Foo {
    template &lt;class T&gt;
    struct sfinae_unfriendly_check {
        static_assert(!std::is_same_v&lt;T, double&gt;);
    };
    template &lt;class T&gt;
    Foo(T, sfinae_unfriendly_check&lt;T&gt; = {});
};
template &lt;class... Ts&gt;

struct first_constructible {
    template &lt;class T, class... Args&gt;
    struct is_constructible_x : std::is_constructible&lt;T, Args...&gt; {
        using type = T;
    };
    struct fallback {
        static constexpr bool value = true;
        using type = void; // type to return if nothing is found
    };
    template &lt;class... Args&gt;
    using with = typename std::disjunction&lt;is_constructible_x&lt;Ts, Args...&gt;...,
                                           fallback&gt;::type;
};
// OK, is_constructible&lt;Foo, double&gt; not instantiated

static_assert(std::is_same_v&lt;first_constructible&lt;std::string, int, Foo&gt;::with&lt;double&gt;,
                             int&gt;);
static_assert(std::is_same_v&lt;first_constructible&lt;std::string, int&gt;::with&lt;&gt;, std::string&gt;);

static_assert(std::is_same_v&lt;first_constructible&lt;std::string, int&gt;::with&lt;const char *&gt;,
                             std::string&gt;);

static_assert(std::is_same_v&lt;first_constructible&lt;std::string, int&gt;::with&lt;void *&gt;, void&gt;);
int main()
{
}
</code></pre>

<h2>See also</h2>

negation logical NOT metafunction 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++17)</i> 
conjunction variadic logical AND metafunction 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++17)</i> 
