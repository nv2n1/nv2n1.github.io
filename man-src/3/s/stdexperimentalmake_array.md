---
title: "stdexperimentalmake_array(3)"
name: "stdexperimentalmake_array"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalmake_array/"
---

std::experimental::make_array - std::experimental::make_array

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / array&gt;

    template &lt;class D = void, class... Types&gt;
    (library fundamentals TS v2)

        constexpr std::array&lt;VT /* see below */, sizeof...(Types)&gt; make_array(Types &amp;&amp;...t);</code></pre> 
Creates a std::array whose size is equal to the number of arguments and whose elements are initialized from the corresponding arguments. Returns std::array&lt;VT, sizeof...(Types)&gt;{std::forward&lt;Types&gt;(t)...} 
If D is void, then the deduced type VT is std::common_type_t&lt;Types...&gt;. Otherwise, it is D. 
If D is void and any of std::decay_t&lt;Types&gt;... is a specialization of std::reference_wrapper, the program is ill-formed. 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;namespace details { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;template&lt;class&gt; struct is_ref_wrapper : std::false_type {}; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;template&lt;class T&gt; struct is_ref_wrapper&lt;std::reference_wrapper&lt;T&gt;&gt; : std::true_type {}; 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;template&lt;class T&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;using not_ref_wrapper = std::negation&lt;is_ref_wrapper&lt;std::decay_t&lt;T&gt;&gt;&gt;; 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;template &lt;class D, class...&gt; struct return_type_helper { using type = D; }; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;template &lt;class... Types&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct return_type_helper&lt;void, Types...&gt; : std::common_type&lt;Types...&gt; { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;static_assert(std::conjunction_v&lt;not_ref_wrapper&lt;Types&gt;...&gt;, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;Types cannot contain reference_wrappers when D is void&quot;); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}; 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;template &lt;class D, class... Types&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;using return_type = std::array&lt;typename return_type_helper&lt;D, Types...&gt;::type, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sizeof...(Types)&gt;; 
&nbsp;<wbr>&nbsp;} 

 
&nbsp;<wbr>&nbsp;template &lt; class D = void, class... Types&gt; 
&nbsp;<wbr>&nbsp;constexpr details::return_type&lt;D, Types...&gt; make_array(Types&amp;&amp;... t) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return {std::forward&lt;Types&gt;(t)... }; 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;experimental/array&gt;

#include &lt;iostream&gt;

#include &lt;type_traits&gt;
int main()

{
    decltype(auto) arr = std::experimental::make_array(1, 2, 3, 4, 5);
    bool is_array_of_5_ints = std::is_same&lt;decltype(arr), std::array&lt;int, 5&gt;&gt;::value;
    std::cout &lt;&lt; &quot;Returns an array of five ints? &quot;;
    std::cout &lt;&lt; std::boolalpha &lt;&lt; is_array_of_5_ints &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Returns an array of five ints? true

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Creates a std::array object from a built-in array 
to_array <i>(function template)</i> 
