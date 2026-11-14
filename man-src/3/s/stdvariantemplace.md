---
title: "stdvariantemplace(3)"
name: "stdvariantemplace"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdvariantemplace/"
---

std::variant&lt;Types...&gt;::emplace - std::variant&lt;Types...&gt;::emplace

<h2>Synopsis</h2>

<pre><code>template &lt;class T, class... Args&gt;                                                             (1) (since C++17)

T&amp; emplace(Args&amp;&amp;... args);

template &lt;class T, class U, class... Args&gt;                                                    (2) (since C++17)

T&amp; emplace(std::initializer_list&lt;U&gt; il, Args&amp;&amp;... args);

template &lt;size_t I, class... Args&gt;                                                            (3) (since C++17)

std::variant_alternative_t&lt;I, variant&gt;&amp; emplace(Args&amp;&amp;... args);

template &lt;size_t I, class U, class... Args&gt;                                                   (4) (since C++17)

std::variant_alternative_t&lt;I, variant&gt;&amp; emplace(std::initializer_list&lt;U&gt; il, Args&amp;&amp;... args);</code></pre> 
Creates a new value in-place, in an existing variant object 
1) Equivalent to emplace&lt;I&gt;(std::forward&lt;Args&gt;(args)...), where I is the zero-based index of T in Types.... This overload only participates in overload resolution if std::is_constructible_v&lt;T, Args...&gt; is true, and T occurs exactly once in Types... 
2) Equivalent to emplace&lt;I&gt;(il, std::forward&lt;Args&gt;(args)...), where I is the zero-based index of T in Types.... This overload only participates in overload resolution if std::is_constructible_v&lt;T, std::initializer_list&lt;U&gt;&amp;, Args...&gt; is true, and T occurs exactly once in Types... 
3) First, destroys the currently contained value (if any). Then direct-initializes the contained value as if constructing a value of type T_I with the arguments std::forward&lt;Args&gt;(args).... If an exception is thrown, *this may become valueless_by_exception. This overload only participates in overload resolution if std::is_constructible_v&lt;T_I, Args...&gt; is true. The behavior is undefined if I is not less than sizeof...(Types). 
4) First, destroys the currently contained value (if any). Then direct-initializes the contained value as if constructing a value of type T_I with the arguments il, std::forward&lt;Args&gt;(args).... If an exception is thrown, *this may become valueless_by_exception. This overload only participates in overload resolution if std::is_constructible_v&lt;T_I, initializer_list&lt;U&gt;&amp;, Args...&gt; is true. The behavior is undefined if I is not less than sizeof...(Types). 

<h2>Parameters</h2>

args - constructor arguments to use when constructing the new value 
il - initializer_list argument to use when constructing the new value

<h2>Return value</h2>

A reference to the new contained value. 

<h2>Exceptions</h2>

1-4) Any exception thrown during the initialization of the contained value.

<h2>Example</h2>

// Run this code #include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;variant&gt;
int main()

{
    std::variant&lt;std::string&gt; v1;
    v1.emplace&lt;0&gt;(&quot;abc&quot;); // OK
    std::cout &lt;&lt; std::get&lt;0&gt;(v1) &lt;&lt; '\n';
    v1.emplace&lt;std::string&gt;(&quot;def&quot;); // OK
    std::cout &lt;&lt; std::get&lt;0&gt;(v1) &lt;&lt; '\n';
    std::variant&lt;std::string, std::string&gt; v2;
    v2.emplace&lt;1&gt;(&quot;ghi&quot;); // OK
    std::cout &lt;&lt; std::get&lt;1&gt;(v2) &lt;&lt; '\n';
    // v2.emplace&lt;std::string&gt;(&quot;abc&quot;); -&gt; Error
}


<h2>Output:</h2>

&nbsp;<wbr>&nbsp;abc 
&nbsp;<wbr>&nbsp;def 
&nbsp;<wbr>&nbsp;ghi

<h2>See also</h2>

<pre><code>assigns a variant

operator= (public member function)




</code></pre>
