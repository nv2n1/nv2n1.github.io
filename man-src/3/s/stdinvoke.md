---
title: "stdinvoke(3)"
name: "stdinvoke"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdinvoke/"
---

std::invoke - std::invoke

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;functional&gt;

template&lt; class F, class... Args&gt;                                                          (since C++17)

std::invoke_result_t&lt;F, Args...&gt; invoke(F&amp;&amp; f, Args&amp;&amp;... args) noexcept(/* see below */);</code></pre> 
Invoke the Callable object f with the parameters args. As by INVOKE(std::forward&lt;F&gt;(f), std::forward&lt;Args&gt;(args)...). 
where INVOKE(f, t1, t2, ..., tN) is defined as follows: 
* If f is a pointer_to_member_function of class T: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If std::is_base_of&lt;T, std::decay_t&lt;decltype(t1)&gt;&gt;::value is true, then INVOKE(f, t1, t2, ..., tN) is equivalent to (t1.*f)(t2, ..., tN) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If std::decay_t&lt;decltype(t1)&gt; is a specialization of std::reference_wrapper, then INVOKE(f, t1, t2, ..., tN) is equivalent to (t1.get().*f)(t2, ..., tN) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If t1 does not satisfy the previous items, then INVOKE(f, t1, t2, ..., tN) is equivalent to ((*t1).*f)(t2, ..., tN). 
* Otherwise, if N == 1 and f is a pointer_to_data_member of class T: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If std::is_base_of&lt;T, std::decay_t&lt;decltype(t1)&gt;&gt;::value is true, then INVOKE(f, t1) is equivalent to t1.*f 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If std::decay_t&lt;decltype(t1)&gt; is a specialization of std::reference_wrapper, then INVOKE(f, t1) is equivalent to t1.get().*f 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If t1 does not satisfy the previous items, then INVOKE(f, t1) is equivalent to (*t1).*f 
* Otherwise, INVOKE(f, t1, t2, ..., tN) is equivalent to f(t1, t2, ..., tN) (that is, f is a FunctionObject) 

<h2>Parameters</h2>

f - Callable object to be invoked 
args - arguments to pass to f

<h2>Exceptions</h2>

noexcept specification: 
noexcept(std::is_nothrow_invocable_v&lt;F, Args...&gt;)

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;namespace detail { 
&nbsp;<wbr>&nbsp;template &lt;class T&gt; 
&nbsp;<wbr>&nbsp;struct is_reference_wrapper : std::false_type {}; 
&nbsp;<wbr>&nbsp;template &lt;class U&gt; 
&nbsp;<wbr>&nbsp;struct is_reference_wrapper&lt;std::reference_wrapper&lt;U&gt;&gt; : std::true_type {}; 
&nbsp;<wbr>&nbsp;template &lt;class T&gt; 
&nbsp;<wbr>&nbsp;constexpr bool is_reference_wrapper_v = is_reference_wrapper&lt;T&gt;::value; 

 
&nbsp;<wbr>&nbsp;template &lt;class T, class Type, class T1, class... Args&gt; 
&nbsp;<wbr>&nbsp;decltype(auto) INVOKE(Type T::* f, T1&amp;&amp; t1, Args&amp;&amp;... args) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if constexpr (std::is_member_function_pointer_v&lt;decltype(f)&gt;) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if constexpr (std::is_base_of_v&lt;T, std::decay_t&lt;T1&gt;&gt;) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return (std::forward&lt;T1&gt;(t1).*f)(std::forward&lt;Args&gt;(args)...); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;else if constexpr (is_reference_wrapper_v&lt;std::decay_t&lt;T1&gt;&gt;) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return (t1.get().*f)(std::forward&lt;Args&gt;(args)...); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;else 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return ((*std::forward&lt;T1&gt;(t1)).*f)(std::forward&lt;Args&gt;(args)...); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} else { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;static_assert(std::is_member_object_pointer_v&lt;decltype(f)&gt;); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;static_assert(sizeof...(args) == 0); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if constexpr (std::is_base_of_v&lt;T, std::decay_t&lt;T1&gt;&gt;) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::forward&lt;T1&gt;(t1).*f; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;else if constexpr (is_reference_wrapper_v&lt;std::decay_t&lt;T1&gt;&gt;) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return t1.get().*f; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;else 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return (*std::forward&lt;T1&gt;(t1)).*f; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;} 

 
&nbsp;<wbr>&nbsp;template &lt;class F, class... Args&gt; 
&nbsp;<wbr>&nbsp;decltype(auto) INVOKE(F&amp;&amp; f, Args&amp;&amp;... args) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::forward&lt;F&gt;(f)(std::forward&lt;Args&gt;(args)...); 
&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;} // namespace detail 

 
&nbsp;<wbr>&nbsp;template&lt; class F, class... Args&gt; 
&nbsp;<wbr>&nbsp;std::invoke_result_t&lt;F, Args...&gt; invoke(F&amp;&amp; f, Args&amp;&amp;... args) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;noexcept(std::is_nothrow_invocable_v&lt;F, Args...&gt;) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return detail::INVOKE(std::forward&lt;F&gt;(f), std::forward&lt;Args&gt;(args)...); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;functional&gt;

#include &lt;iostream&gt;
struct Foo {
    Foo(int num)
        : num_(num)
    {
    }
    void print_add(int i) const
    {
        std::cout &lt;&lt; num_ + i &lt;&lt; '\n';
    }
    int num_;
};
void print_num(int i)

{
    std::cout &lt;&lt; i &lt;&lt; '\n';
}
struct PrintNum {
    void operator()(int i) const
    {
        std::cout &lt;&lt; i &lt;&lt; '\n';
    }
};
int main()

{
    // invoke a free function
    std::invoke(print_num, -9);
    // invoke a lambda
    std::invoke([]() { print_num(42); });
    // invoke a member function
    const Foo foo(314159);
    std::invoke(&amp;Foo::print_add, foo, 1);
    // invoke (access) a data member
    std::cout &lt;&lt; &quot;num_: &quot; &lt;&lt; std::invoke(&amp;Foo::num_, foo) &lt;&lt; '\n';
    // invoke a function object
    std::invoke(PrintNum(), 18);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;-9 
&nbsp;<wbr>&nbsp;42 
&nbsp;<wbr>&nbsp;314160 
&nbsp;<wbr>&nbsp;num_: 314159 
&nbsp;<wbr>&nbsp;18

<h2>See also</h2>

mem_fn creates a function object out of a pointer to a member 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
result_of 
invoke_result deduces the result type of invoking a callable object with a set of arguments 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i>(removed in C++20) 
<i>(C++17)</i> 
is_invocable 
is_invocable_r checks if a type can be invoked (as if by std::invoke) with the given argument types 
is_nothrow_invocable <i>(class template)</i> 
is_nothrow_invocable_r 
<i>(C++17)</i> 
apply calls a function with a tuple of arguments 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
