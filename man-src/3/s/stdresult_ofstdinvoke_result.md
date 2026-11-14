---
title: "stdresult_ofstdinvoke_result(3)"
name: "stdresult_ofstdinvoke_result"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdresult_ofstdinvoke_result/"
description: "std::result_of,std::invoke_result – std::result_of,std::invoke_result"
---

<p>std::result_of,std::invoke_result &#8211; std::result_of,std::invoke_result</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;type_traits&gt;

template&lt; class &gt;

class result_of; // not defined            (since C++11)
(1) (deprecated in C++17)

template&lt; class F, class... ArgTypes &gt;     (removed in C++20)

class result_of&lt;F(ArgTypes...)&gt;;

template&lt; class F, class... ArgTypes&gt;  (2) (since C++17)

class invoke_result;</code></pre>
<p>Deduces the return type of an INVOKE expression at compile time.<br />
F must be a callable type, reference to function, or reference to callable type. Invoking F with ArgTypes&#8230; must be a well-formed expression. <i>(since C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(until C++14)</i><br />
F and all types in ArgTypes can be any complete type, array of unknown bound, or (possibly cv-qualified) void. <i>(since C++14)</i> </p>
<h2>Member types</h2>
<p>Member type Definition<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the return type of the Callable type F if invoked with the arguments ArgTypes&#8230;.<br />
type Only defined if F can be called with the arguments ArgTypes&#8230; in unevaluated context.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++14)</i></p>
<h2>Helper types</h2>
<p>template&lt; class T &gt; <i>(since C++14)</i><br />
using result_of_t = typename result_of&lt;T&gt;::type; <code>(1)</code> (deprecated in C++17)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(removed in C++20)<br />
template&lt; class F, class&#8230; ArgTypes&gt; <code>(2)</code> <i>(since C++17)</i><br />
using invoke_result_t = typename invoke_result&lt;F, ArgTypes&#8230;&gt;::type;</p>
<h2>Possible implementation</h2>
<p>&nbsp;<wbr>&nbsp;namespace detail {<br />
&nbsp;<wbr>&nbsp;template &lt;class T&gt;<br />
&nbsp;<wbr>&nbsp;struct is_reference_wrapper : std::false_type {};<br />
&nbsp;<wbr>&nbsp;template &lt;class U&gt;<br />
&nbsp;<wbr>&nbsp;struct is_reference_wrapper&lt;std::reference_wrapper&lt;U&gt;&gt; : std::true_type {}; </p>
<p>&nbsp;<wbr>&nbsp;template&lt;class T&gt;<br />
&nbsp;<wbr>&nbsp;struct invoke_impl {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;template&lt;class F, class&#8230; Args&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;static auto call(F&amp;&amp; f, Args&amp;&amp;&#8230; args)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-&gt; decltype(std::forward&lt;F&gt;(f)(std::forward&lt;Args&gt;(args)&#8230;));<br />
&nbsp;<wbr>&nbsp;}; </p>
<p>&nbsp;<wbr>&nbsp;template&lt;class B, class MT&gt;<br />
&nbsp;<wbr>&nbsp;struct invoke_impl&lt;MT B::*&gt; {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;template&lt;class T, class Td = typename std::decay&lt;T&gt;::type,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;class = typename std::enable_if&lt;std::is_base_of&lt;B, Td&gt;::value&gt;::type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;static auto get(T&amp;&amp; t) -&gt; T&amp;&amp;; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;template&lt;class T, class Td = typename std::decay&lt;T&gt;::type,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;class = typename std::enable_if&lt;is_reference_wrapper&lt;Td&gt;::value&gt;::type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;static auto get(T&amp;&amp; t) -&gt; decltype(t.get()); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;template&lt;class T, class Td = typename std::decay&lt;T&gt;::type,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;class = typename std::enable_if&lt;!std::is_base_of&lt;B, Td&gt;::value&gt;::type,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;class = typename std::enable_if&lt;!is_reference_wrapper&lt;Td&gt;::value&gt;::type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;static auto get(T&amp;&amp; t) -&gt; decltype(*std::forward&lt;T&gt;(t)); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;template&lt;class T, class&#8230; Args, class MT1,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;class = typename std::enable_if&lt;std::is_function&lt;MT1&gt;::value&gt;::type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;static auto call(MT1 B::*pmf, T&amp;&amp; t, Args&amp;&amp;&#8230; args)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-&gt; decltype((invoke_impl::get(std::forward&lt;T&gt;(t)).*pmf)(std::forward&lt;Args&gt;(args)&#8230;)); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;template&lt;class T&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;static auto call(MT B::*pmd, T&amp;&amp; t)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-&gt; decltype(invoke_impl::get(std::forward&lt;T&gt;(t)).*pmd);<br />
&nbsp;<wbr>&nbsp;}; </p>
<p>&nbsp;<wbr>&nbsp;template&lt;class F, class&#8230; Args, class Fd = typename std::decay&lt;F&gt;::type&gt;<br />
&nbsp;<wbr>&nbsp;auto INVOKE(F&amp;&amp; f, Args&amp;&amp;&#8230; args)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;-&gt; decltype(invoke_impl&lt;Fd&gt;::call(std::forward&lt;F&gt;(f), std::forward&lt;Args&gt;(args)&#8230;)); </p>
<p>&nbsp;<wbr>&nbsp;} // namespace detail </p>
<p>&nbsp;<wbr>&nbsp;// Minimal C++11 implementation:<br />
&nbsp;<wbr>&nbsp;template &lt;class&gt; struct result_of;<br />
&nbsp;<wbr>&nbsp;template &lt;class F, class&#8230; ArgTypes&gt;<br />
&nbsp;<wbr>&nbsp;struct result_of&lt;F(ArgTypes&#8230;)&gt; {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;using type = decltype(detail::INVOKE(std::declval&lt;F&gt;(), std::declval&lt;ArgTypes&gt;()&#8230;));<br />
&nbsp;<wbr>&nbsp;}; </p>
<p>&nbsp;<wbr>&nbsp;// Conforming C++14 implementation (is also a valid C++11 implementation):<br />
&nbsp;<wbr>&nbsp;namespace detail {<br />
&nbsp;<wbr>&nbsp;template &lt;typename AlwaysVoid, typename, typename&#8230;&gt;<br />
&nbsp;<wbr>&nbsp;struct invoke_result { };<br />
&nbsp;<wbr>&nbsp;template &lt;typename F, typename&#8230;Args&gt;<br />
&nbsp;<wbr>&nbsp;struct invoke_result&lt;decltype(void(detail::INVOKE(std::declval&lt;F&gt;(), std::declval&lt;Args&gt;()&#8230;))),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;F, Args&#8230;&gt; {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;using type = decltype(detail::INVOKE(std::declval&lt;F&gt;(), std::declval&lt;Args&gt;()&#8230;));<br />
&nbsp;<wbr>&nbsp;};<br />
&nbsp;<wbr>&nbsp;} // namespace detail </p>
<p>&nbsp;<wbr>&nbsp;template &lt;class&gt; struct result_of;<br />
&nbsp;<wbr>&nbsp;template &lt;class F, class&#8230; ArgTypes&gt;<br />
&nbsp;<wbr>&nbsp;struct result_of&lt;F(ArgTypes&#8230;)&gt; : detail::invoke_result&lt;void, F, ArgTypes&#8230;&gt; {}; </p>
<p>&nbsp;<wbr>&nbsp;template &lt;class F, class&#8230; ArgTypes&gt;<br />
&nbsp;<wbr>&nbsp;struct invoke_result : detail::invoke_result&lt;void, F, ArgTypes&#8230;&gt; {};</p>
<h2>Notes</h2>
<p>As formulated in C++11, the behavior of std::result_of is undefined when INVOKE(std::declval&lt;F&gt;(), std::declval&lt;ArgTypes&gt;()&#8230;) is ill-formed (e.g. when F is not a callable type at all). C++14 changes that to a SFINAE (when F is not callable, std::result_of&lt;F(ArgTypes&#8230;)&gt; simply doesn&#8217;t have the type member).<br />
The motivation behind std::result_of is to determine the result of invoking a Callable, in particular if that result type is different for different sets of arguments.<br />
F(Args&#8230;) is a function type with Args&#8230; being the argument types and F being the return type. As such, std::result_of suffers from several quirks that lead to its deprecation in favor of std::invoke_result in C++17:<br />
* F cannot be a function type or an array type (but can be a reference to them);<br />
* if any of the Args has type &quot;array of T&quot; or a function type T, it is automatically adjusted to T*;<br />
* neither F nor any of Args&#8230; can be an abstract class type;<br />
* if any of Args&#8230; has a top-level cv-qualifier, it is discarded;<br />
* none of Args&#8230; may be of type void.<br />
To avoid these quirks, result_of is often used with reference types as F and Args&#8230;. For example: template&lt;class F, class&#8230; Args&gt;</p>
<p>std::result_of_t&lt;F&amp;&amp;(Args&amp;&amp;&#8230;)&gt; // instead of std::result_of_t&lt;F(Args&#8230;)&gt;, which is wrong<br />
my_invoke(F&amp;&amp; f, Args&amp;&amp;&#8230; args) {<br />
    /* implementation */</p>
<p>}</p>
<h2>Examples</h2>
<p>// Run this code </p>
<pre><code>#include &lt;type_traits&gt;

#include &lt;iostream&gt;
struct S {
    double operator()(char, int &amp;);
    float operator()(int)
    {
        return 1.0;
    }
};
template &lt;class T&gt;

typename std::result_of&lt;T(int)&gt;::type f(T &amp;t)

{
    std::cout &lt;&lt; &quot;overload of f for callable T
&quot;;
    return t(0);
}
template &lt;class T, class U&gt;

int f(U u)

{
    std::cout &lt;&lt; &quot;overload of f for non-callable T
&quot;;
    return u;
}
int main()

{
    // the result of invoking S with char and int&amp; arguments is double
    std::result_of&lt;S(char, int &amp;)&gt;::type d = 3.14; // d has type double
    static_assert(std::is_same&lt;decltype(d), double&gt;::value, &quot;&quot;);
    // the result of invoking S with int argument is float
    std::result_of&lt;S(int)&gt;::type x = 3.14; // x has type float
    static_assert(std::is_same&lt;decltype(x), float&gt;::value, &quot;&quot;);
    // result_of can be used with a pointer to member function as follows
    struct C {
        double Func(char, int &amp;);
    };
    std::result_of&lt;decltype (&amp;C::Func)(C, char, int &amp;)&gt;::type g = 3.14;
    static_assert(std::is_same&lt;decltype(g), double&gt;::value, &quot;&quot;);
    f&lt;C&gt;(1); // may fail to compile in C++11; calls the non-callable overload in C++14
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;overload of f for non-callable T</p>
<h2>See also</h2>
<p>invoke invokes any Callable object with given arguments<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++17)</i><br />
is_invocable<br />
is_invocable_r checks if a type can be invoked (as if by std::invoke) with the given argument types<br />
is_nothrow_invocable <i>(class template)</i><br />
is_nothrow_invocable_r<br />
<i>(C++17)</i><br />
declval obtains a reference to its argument for use in unevaluated context<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i> </p>
