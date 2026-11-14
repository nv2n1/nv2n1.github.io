---
title: "stdnested_exception(3)"
name: "stdnested_exception"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnested_exception/"
description: "std::nested_exception – std::nested_exception"
---

<p>std::nested_exception &#8211; std::nested_exception</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;exception&gt;<br />
class nested_exception; <i>(since C++11)</i><br />
std::nested_exception is a polymorphic mixin class which can capture and store the current exception, making it possible to nest exceptions of arbitrary types within each other. </p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a nested_exception<br />
constructor <i>(public member function)</i> </p>
<p>destructor destructs a nested exception<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual public member function)</i><br />
<code>[virtual]</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;replaces the contents of a nested_exception<br />
operator= <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;throws the stored exception<br />
rethrow_nested <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;obtains a pointer to the stored exception<br />
nested_ptr <i>(public member function)</i></p>
<h2>Non-member functions</h2>
<p>throw_with_nested throws its argument with std::nested_exception mixed in<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i> </p>
<p>rethrow_if_nested throws the exception from a std::nested_exception<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i></p>
<h2>Example</h2>
<p>Demonstrates construction and recursion through a nested exception object<br />
 // Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;stdexcept&gt;

#include &lt;exception&gt;

#include &lt;string&gt;

#include &lt;fstream&gt;
// prints the explanatory string of an exception. If the exception is nested,

// recurses to print the explanatory of the exception it holds

void print_exception(const std::exception &amp;e, int level = 0)

{
    std::cerr &lt;&lt; std::string(level, ' ') &lt;&lt; &quot;exception: &quot; &lt;&lt; e.what() &lt;&lt; '
';
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
<p>&nbsp;<wbr>&nbsp;exception: run() failed<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;exception: Couldn&#8217;t open nonexistent.file<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exception: basic_ios::clear</p>
<h2>See also</h2>
<p>exception_ptr shared pointer type for handling exception objects<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(typedef)</i><br />
<i>(C++11)</i><br />
throw_with_nested throws its argument with std::nested_exception mixed in<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i><br />
rethrow_if_nested throws the exception from a std::nested_exception<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i><br />
<i>(C++11)</i> </p>
