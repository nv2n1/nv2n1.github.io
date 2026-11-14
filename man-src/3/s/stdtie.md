---
title: "stdtie(3)"
name: "stdtie"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtie/"
---

std::tie - std::tie

<h2>Synopsis</h2>

Defined in header &lt;tuple&gt; 
template&lt; class... Types &gt; <i>(since C++11)</i> 
tuple&lt;Types&amp;...&gt; tie( Types&amp;... args ) noexcept; (constexpr since C++14) 
Creates a tuple of lvalue references to its arguments or instances of std::ignore. 

<h2>Parameters</h2>

args - zero or more lvalue arguments to construct the tuple from

<h2>Return value</h2>

A std::tuple object containing lvalue references. 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;namespace detail { 
&nbsp;<wbr>&nbsp;struct ignore_t { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;template &lt;typename T&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;const ignore_t&amp; operator=(const T&amp;) const { return *this; } 
&nbsp;<wbr>&nbsp;}; 
&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;const detail::ignore_t ignore; 

 
&nbsp;<wbr>&nbsp;template &lt;typename... Args&gt; 
&nbsp;<wbr>&nbsp;auto tie(Args&amp;... args) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::tuple&lt;Args&amp;...&gt;(args...); 
&nbsp;<wbr>&nbsp;}

<h2>Notes</h2>

std::tie may be used to unpack a std::pair because std::tuple has a converting_assignment from pairs: <pre><code>bool result;

std::tie(std::ignore, result) = set.insert(value);

</code></pre>

<h2>Example</h2>

std::tie can be used to introduce lexicographical comparison to a struct or to unpack a tuple: 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;set&gt;

#include &lt;tuple&gt;
struct S {
    int n;
    std::string s;
    float d;
    bool operator&lt;(const S &amp;rhs) const
    {
        // compares n to rhs.n,
        // then s to rhs.s,
        // then d to rhs.d
        return std::tie(n, s, d) &lt; std::tie(rhs.n, rhs.s, rhs.d);
    }
};
int main()

{
    std::set&lt;S&gt; set_of_s; // S is LessThanComparable
    S value{42, &quot;Test&quot;, 3.14};
    std::set&lt;S&gt;::iterator iter;
    bool inserted;
    // unpacks the return value of insert into iter and inserted
    std::tie(iter, inserted) = set_of_s.insert(value);
    if (inserted)
        std::cout &lt;&lt; &quot;Value was inserted successfully\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Value was inserted successfully

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a tuple object of the type defined by the argument types 
make_tuple <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a tuple of rvalue references 
forward_as_tuple <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a tuple by concatenating any number of tuples 
tuple_cat <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;placeholder to skip an element when unpacking a tuple using tie 
ignore (constant) 
