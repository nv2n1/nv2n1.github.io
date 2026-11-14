---
title: "stdiostream_category(3)"
name: "stdiostream_category"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdiostream_category/"
---

std::iostream_category - std::iostream_category

<h2>Synopsis</h2>

Defined in header &lt;ios&gt; 
const std::error_category&amp; iostream_category() noexcept; <i>(since C++11)</i> <pre><code>Obtains a reference to the static error category object for iostream errors. The object is required to override the virtual function error_category::name() to return a pointer to the string &quot;iostream&quot;. It is used to identify error codes provided in the exceptions of type std::ios_base::failure.
</code></pre>

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

A reference to the static object of unspecified runtime type, derived from std::error_category. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;fstream&gt;
int main()

{
    std::ifstream f(&quot;doesn't exist&quot;);
    try {
        f.exceptions(f.failbit);
    } catch (const std::ios_base::failure &amp;e) {
        std::cout &lt;&lt; &quot;Caught an ios_base::failure.\n&quot;
                  &lt;&lt; &quot;Error code: &quot; &lt;&lt; e.code().value()
                  &lt;&lt; &quot; (&quot; &lt;&lt; e.code().message() &lt;&lt; &quot;)\n&quot;
                  &lt;&lt; &quot;Error category: &quot; &lt;&lt; e.code().category().name() &lt;&lt; '\n';
    }
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Caught an ios_base::failure. 
&nbsp;<wbr>&nbsp;Error code: 1 (unspecified iostream_category error) 
&nbsp;<wbr>&nbsp;Error category: iostream

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;stream exception 
failure <i>(public member class of std::ios_base)</i> 
io_errc the IO stream error codes 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(enum)</i> 
<i>(C++11)</i> 
