---
title: "stdthrow_with_nested(3)"
name: "stdthrow_with_nested"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdthrow_with_nested/"
---

std::throw_with_nested - std::throw_with_nested

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;exception&gt;

    template &lt;class T&gt;
    (since C++ 11)

        [[noreturn]] void throw_with_nested(T &amp;&amp;t);</code></pre> 
If std::decay&lt;T&gt;::type is a non-final non-union class type that is neither std::nested_exception nor derived from std::nested_exception, throws an exception of an unspecified type that is publicly derived from both std::nested_exception and from std::decay&lt;T&gt;::type, and constructed from std::forward&lt;T&gt;(t). The default constructor of the nested_exception base class calls std::current_exception, capturing the currently handled exception object, if any, in a std::exception_ptr. 
Otherwise, throws std::forward&lt;T&gt;(t). 
Requires that std::decay&lt;T&gt;::type is CopyConstructible 

<h2>Parameters</h2>

t - the exception object to throw

<h2>Return value</h2>

<i>(none)</i> 

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
rethrow_if_nested throws the exception from a std::nested_exception 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
