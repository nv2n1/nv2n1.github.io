---
title: "stdenable_if(3)"
name: "stdenable_if"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdenable_if/"
---

std::enable_if - std::enable_if

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;bool B, class T = void&gt;
    (since C++ 11)

        struct enable_if;</code></pre> 
If B is true, std::enable_if has a public member typedef type, equal to T; otherwise, there is no member typedef. 
This metafunction is a convenient way to leverage SFINAE to conditionally remove functions from overload_resolution based on type traits and to provide separate function overloads and specializations for different type traits. std::enable_if can be used as an additional function argument (not applicable to operator overloads), as a return type (not applicable to constructors and destructors), or as a class template or function template parameter. 

<h2>Member types</h2>

Type Definition 
type either T or no such member, depending on the value of B

<h2>Helper types</h2>

template&lt; bool B, class T = void &gt; <i>(since C++14)</i> 
using enable_if_t = typename enable_if&lt;B,T&gt;::type;

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt;bool B, class T = void&gt; 
&nbsp;<wbr>&nbsp;struct enable_if {}; 

 
&nbsp;<wbr>&nbsp;template&lt;class T&gt; 
&nbsp;<wbr>&nbsp;struct enable_if&lt;true, T&gt; { typedef T type; };

<h2>Notes</h2>

A common mistake is to declare two function templates that differ only in their default template arguments. This is illegal because default template arguments are not part of function template's signature, and declaring two different function templates with the same signature is illegal. struct X {
    enum { value1 = true,
           value2 = true };
};
template &lt;class T, std::enable_if_t&lt;T::value2, int&gt; = 0&gt;

void func()
{
} // #3 
Care should be taken when using enable_if in the type of a template non-type parameter of a namespace-scope function template. Some ABI specifications like the Itanium ABI do not include the instantiation-dependent portions of non-type template parameters in the mangling, meaning that specializations of two distinct function templates might end up with the same mangled name and be erroneously linked together. For example: 
&nbsp;<wbr>&nbsp;// first translation unit  
&nbsp;<wbr>&nbsp;template void func&lt;X&gt;(); // #2 
&nbsp;<wbr>&nbsp;// second translation unit struct X {
    enum { value1 = true,
           value2 = true };
};
template &lt;class T, std::enable_if_t&lt;T::value2, int&gt; = 0&gt;

void func()
{
} // #3 
&nbsp;<wbr>&nbsp;template void func&lt;X&gt;(); //#4 
The function templates #1 and #3 have different signatures and are distinct templates. Nonetheless, #2 and #4, despite being instantiations of different function templates, have the same mangled name in_the_Itanium_C++_ABI (_Z4funcI1XLi0EEvv), meaning that the linker will erroneously consider them to be the same entity. 

<h2>Example</h2>

// Run this code #include &lt;type_traits&gt;

#include &lt;iostream&gt;

#include &lt;string&gt;
namespace detail
{
struct inplace_t {
};
} // namespace detail

void *operator_new(std::size_t, void *p, detail::inplace_t)
{
    return p;
}
// #1, enabled via the return type

template &lt;class T, class... Args&gt;

typename std::enable_if&lt;std::is_trivially_constructible&lt;T, Args &amp;&amp;...&gt;::value&gt;::type
construct(T *t, Args &amp;&amp;...args)

{
    std::cout &lt;&lt; &quot;constructing trivially constructible T\n&quot;;
}
// #2

template &lt;class T, class... Args&gt;

std::enable_if_t&lt;!std::is_trivially_constructible&lt;T, Args &amp;&amp;...&gt;::value&gt; // Using helper type
construct(T *t, Args &amp;&amp;...args)

{
    std::cout &lt;&lt; &quot;constructing non-trivially constructible T\n&quot;;
    new (t, detail::inplace_t{}) T(args...);
}
// #3, enabled via a parameter

template &lt;class T&gt;

void destroy(
    T *t,
    typename std::enable_if&lt;
        std::is_trivially_destructible&lt;T&gt;::value&gt;::type * = 0

)
{
    std::cout &lt;&lt; &quot;destroying trivially destructible T\n&quot;;
}
// #4, enabled via a template parameter

template &lt;class T,
          typename std::enable_if&lt;
              !std::is_trivially_destructible&lt;T&gt;{} &amp;&amp;
                  (std::is_class&lt;T&gt;{} || std::is_union&lt;T&gt;{}),
              int&gt;::type = 0&gt;

void destroy(T *t)

{
    std::cout &lt;&lt; &quot;destroying non-trivially destructible T\n&quot;;
    t-&gt;~T();
}
// #5, enabled via a template parameter

template &lt;class T,

          typename = std::enable_if_t&lt;std::is_array&lt;T&gt;::value&gt;&gt;

void destroy(T *t) // note, function signature is unmodified

{
    for (std::size_t i = 0; i &lt; std::extent&lt;T&gt;::value; ++i) {
        destroy((*t)[i]);
    }
}

/*

template&lt;class T,

    typename = std::enable_if_t&lt;std::is_void&lt;T&gt;::value&gt; &gt;

void destroy(T* t){} // error: has the same signature with #5

*/ 
&nbsp;<wbr>&nbsp;// the partial specialization of A is enabled via a template parameter 
&nbsp;<wbr>&nbsp;template&lt;class T, class Enable = void&gt; 
&nbsp;<wbr>&nbsp;class A {}; // primary template 
&nbsp;<wbr>&nbsp;template&lt;class T&gt; 
&nbsp;<wbr>&nbsp;class A&lt;T, typename std::enable_if&lt;std::is_floating_point&lt;T&gt;::value&gt;::type&gt; { 
&nbsp;<wbr>&nbsp;}; // specialization for floating point types <pre><code>int main()

{
    std::aligned_union_t&lt;0, int, std::string&gt; u;
    construct(reinterpret_cast&lt;int *&gt;(&amp;u));
    destroy(reinterpret_cast&lt;int *&gt;(&amp;u));
    construct(reinterpret_cast&lt;std::string *&gt;(&amp;u), &quot;Hello&quot;);
    destroy(reinterpret_cast&lt;std::string *&gt;(&amp;u));
    A&lt;int&gt; a1;    // OK, matches the primary template
    A&lt;double&gt; a2; // OK, matches the partial specialization
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;constructing trivially constructible T 
&nbsp;<wbr>&nbsp;destroying trivially destructible T 
&nbsp;<wbr>&nbsp;constructing non-trivially constructible T 
&nbsp;<wbr>&nbsp;destroying non-trivially destructible T

<h2>See also</h2>

void_t void variadic alias template 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(alias template) 
<i>(C++17)</i> 
* static_assert 
* SFINAE 
