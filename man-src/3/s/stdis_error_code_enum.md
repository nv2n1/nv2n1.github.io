---
title: "stdis_error_code_enum(3)"
name: "stdis_error_code_enum"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_error_code_enum/"
description: "std::is_error_code_enum<std::io_errc> – std::is_error_code_enum<std::io_errc>"
---

<p>std::is_error_code_enum&lt;std::io_errc&gt; &#8211; std::is_error_code_enum&lt;std::io_errc&gt;</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;ios&gt;

    template &lt;&gt;
    (since C++ 11)

        struct is_error_code_enum&lt;std::io_errc&gt; : public std::true_type {
};</code></pre>
<p>This specialization of std::is_error_code_enum informs other library components that values of type std::io_errc are enumerations that hold error codes, which makes them implicitly convertible and assignable to objects of type std::error_code.<br />
Inherited from std::integral_constant </p>
<h2>Member constants</h2>
<p>value true<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code></p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts the object to bool, returns value<br />
operator bool <i>(public member function)</i> </p>
<p>operator() returns value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public member function)</i><br />
<i>(C++14)</i></p>
<h2>Member types</h2>
<p>Type Definition<br />
value_type bool<br />
type std::integral_constant&lt;bool, value&gt;</p>
<h2>Example</h2>
<p>The comparison between e.code() and std::io_errc::stream compiles because std::is_error_code_enum&lt;std::io_errc&gt;::value == true<br />
 // Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;fstream&gt;

int main()

{
    std::ifstream f(&quot;doesn't exist&quot;);
    try {
        f.exceptions(f.failbit);
    } catch (const std::ios_base::failure &amp;e) {
        std::cout &lt;&lt; &quot;Caught an ios_base::failure.
&quot;;
        if (e.code() == std::io_errc::stream)
            std::cout &lt;&lt; &quot;The error code is std::io_errc::stream
&quot;;
    }
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;Caught an ios_base::failure.<br />
&nbsp;<wbr>&nbsp;The error code is std::io_errc::stream</p>
<h2>See also</h2>
<p>is_error_code_enum identifies a class as an error_code enumeration<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
error_code holds a platform-dependent error code<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i><br />
<i>(C++11)</i><br />
io_errc the IO stream error codes<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(enum)</i><br />
<i>(C++11)</i> </p>
