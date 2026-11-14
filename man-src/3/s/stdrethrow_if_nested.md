---
title: "stdrethrow_if_nested(3)"
name: "stdrethrow_if_nested"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrethrow_if_nested/"
---

std::rethrow_if_nested - std::rethrow_if_nested

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;exception&gt;

    template &lt;class E&gt;
    (since C++ 11)

        void rethrow_if_nested(const E &amp;e);</code></pre> 
If E is not a polymorphic class type, or if std::nested_exception is an inaccessible or ambiguous base class of E, there is no effect. 
Otherwise, performs if (auto p = dynamic_cast&lt;const std::nested_exception *&gt;(std::addressof(e)))
    p-&gt;rethrow_nested();


<h2>Parameters</h2>

e - the exception object to rethrow

<h2>Return value</h2>

<i>(none)</i> 

<h2>Notes</h2>

Unlike many related functions, this function is not intended to be called with a std::exception_ptr but rather an actual exception reference. 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;namespace details { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;template &lt;class E&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct can_dynamic_cast 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;: std::integral_constant&lt;bool, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::is_polymorphic&lt;E&gt;::value &amp;&amp; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(!std::is_base_of&lt;std::nested_exception, E&gt;::value || 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::is_convertible&lt;E*, std::nested_exception*&gt;::value) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&gt; { }; 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;template &lt;class T&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void rethrow_if_nested_impl(const T&amp; e, std::true_type) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if(auto nep = dynamic_cast&lt;const std::nested_exception*&gt;(std::addressof(e))) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nep-&gt;rethrow_nested(); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;template &lt;class T&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void rethrow_if_nested_impl(const T&amp;, std::false_type) { } 
&nbsp;<wbr>&nbsp;} 

 
&nbsp;<wbr>&nbsp;template &lt;class T&gt; 
&nbsp;<wbr>&nbsp;void rethrow_if_nested(const T&amp; t){ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;details::rethrow_if_nested_impl(t, details::can_dynamic_cast&lt;T&gt;()); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

Demonstrates construction and recursion through a nested exception object 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;stdexcept&gt;

#include &lt;exception&gt;

#include &lt;string&gt;

#include &lt;fstream&gt;
// prints the explanatory string of an exception. If the exception is nested,

// recurses to print the explanatory of the exception it holds

void print_exception(const std::exception &amp;e, int level = 0)

{
    std::cerr &lt;&lt; std::string(level, ' ') &lt;&lt; &quot;exception: &quot; &lt;&lt; e.what() &lt;&lt; '\n';
    try {
        std::rethrow_if_nested(e);
    } catch (const std::exception &amp;e) {
        print_exception(e, level + 1);
    } catch (...) {
    }
}
// sample function that catches an exception and wraps it in a nested exception

void open_file(const std::string &amp;s)

{
    try {
        std::ifstream file(s);
        file.exceptions(std::ios_base::failbit);
    } catch (...) {
        std::throw_with_nested(std::runtime_error(&quot;Couldn't open &quot; + s));
    }
}
// sample function that catches an exception and wraps it in a nested exception

void run()

{
    try {
        open_file(&quot;nonexistent.file&quot;);
    } catch (...) {
        std::throw_with_nested(std::runtime_error(&quot;run() failed&quot;));
    }
}
// runs the sample function above and prints the caught exception

int main()

{
    try {
        run();
    } catch (const std::exception &amp;e) {
        print_exception(e);
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;exception: run() failed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;exception: Couldn't open nonexistent.file 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exception: basic_ios::clear

<h2>See also</h2>

nested_exception a mixin type to capture and store current exceptions 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
<i>(C++11)</i> 
throw_with_nested throws its argument with std::nested_exception mixed in 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
