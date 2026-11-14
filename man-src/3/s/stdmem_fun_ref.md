---
title: "stdmem_fun_ref(3)"
name: "stdmem_fun_ref"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmem_fun_ref/"
description: "std::mem_fun_ref – std::mem_fun_ref"
---

<p>std::mem_fun_ref &#8211; std::mem_fun_ref</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;functional&gt;<br />
template&lt; class Res, class T &gt; <code>(1)</code> (deprecated in C++11)<br />
std::mem_fun_ref_t&lt;Res,T&gt; mem_fun_ref( Res (T::*f)() ); (removed in C++17)<br />
template&lt; class Res, class T &gt; <code>(1)</code> (deprecated in C++11)<br />
std::const_mem_fun_ref_t&lt;Res,T&gt; mem_fun_ref( Res (T::*f)() ); (removed in C++17)<br />
template&lt; class Res, class T, class Arg &gt; <code>(2)</code> (deprecated in C++11)<br />
std::mem_fun1_ref_t&lt;Res,T,Arg&gt; mem_fun_ref( Res (T::*f)(Arg) ); (removed in C++17)<br />
template&lt; class Res, class T, class Arg &gt; <code>(2)</code> (deprecated in C++11)<br />
std::const_mem_fun1_ref_t&lt;Res,T,Arg&gt; mem_fun_ref( S (T::*f)(Arg) ); (removed in C++17)<br />
Creates a member function wrapper object, deducing the target type from the template arguments. The wrapper object expects a reference to an object of type T as the first parameter to its operator().<br />
1) Effectively calls std::mem_fun_ref_t&lt;S,T&gt;(f) or std::const_mem_fun_ref_t&lt;S,T&gt;(f).<br />
2) Effectively calls std::mem_fun1_ref_t&lt;S,T&gt;(f) or std::const_mem_fun1_ref_t&lt;S,T&gt;(f).<br />
This function and the related types were deprecated in C++11 and removed in C++17 in favor of the more general std::mem_fn and std::bind, both of which create callable adapter-compatible function objects from member functions. </p>
<h2>Parameters</h2>
<p>f &#8211; pointer to a member function to create a wrapper for</p>
<h2>Return value</h2>
<p>A function object wrapping f. </p>
<h2>Exceptions</h2>
<p><i>(none)</i></p>
<h2>Notes</h2>
<p>The difference between std::mem_fun and std::mem_fun_ref is that the former produces an function wrapper that expects a pointer to an object, whereas the latter &#8212; a reference. </p>
<h2>Example</h2>
<p>uses std::mem_fun_ref to bind std::string&#8217;s member function .size()<br />
 // Run this code </p>
<pre><code>#include &lt;functional&gt;

#include &lt;vector&gt;

#include &lt;string&gt;

#include &lt;iterator&gt;

#include &lt;algorithm&gt;

#include &lt;iostream&gt;
int main()

{
    std::vector&lt;std::string&gt; v = {&quot;once&quot;, &quot;upon&quot;, &quot;a&quot;, &quot;time&quot;};
    std::transform(v.begin(), v.end(),
                   std::ostream_iterator&lt;std::size_t&gt;(std::cout, &quot; &quot;),
                   std::mem_fun_ref(&amp;std::string::size));
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;4 4 1 4</p>
<h2>See also</h2>
<p>mem_fun creates a wrapper from a pointer to member function, callable with a pointer to object<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
(deprecated in C++11)<br />
(removed in C++17) </p>
