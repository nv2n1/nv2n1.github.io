---
title: "stdexperimentalrangesinvoke(3)"
name: "stdexperimentalrangesinvoke"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesinvoke/"
---

std::experimental::ranges::invoke - std::experimental::ranges::invoke

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / ranges / functional&gt;

    template &lt;class F, class... Args&gt;
    (ranges TS)

        std::result_of_t&lt;F &amp;&amp; (Args &amp;&amp; ...)&gt; invoke(F &amp;&amp;f, Args &amp;&amp;...args);
Invoke the Callable object f with the parameters args, and return the result, as if by return INVOKE(std::forward&lt;F&gt;(f), std::forward&lt;Args&gt;(args)...);
, where INVOKE(f, t1, t2, ..., tN)
is defined as follows:</code></pre> 
* if f is a pointer_to_member_function of class T: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If std::is_base_of&lt;T, std::decay_t&lt;decltype(t1)&gt;&gt;::value is true, then INVOKE(f, t1, t2, ..., tN) is equivalent to (t1.*f)(t2, ..., tN) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* otherwise, INVOKE(f, t1, t2, ..., tN) is equivalent to ((*t1).*f)(t2, ..., tN). 
* otherwise, if N == 1 and f is a pointer_to_data_member of class T: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If std::is_base_of&lt;T, std::decay_t&lt;decltype(t1)&gt;&gt;::value is true, then INVOKE(f, t1) is equivalent to t1.*f 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* otherwise, then INVOKE(f, t1) is equivalent to (*t1).*f 
* otherwise, INVOKE(f, t1, t2, ..., tN) is equivalent to f(t1, t2, ..., tN) (that is, f is a FunctionObject) 

<h2>Parameters</h2>

f - Callable object to be invoked 
args - arguments to pass to f

<h2>See also</h2>

invoke invokes any Callable object with given arguments 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++17)</i> 
