---
title: "stdios_basefailure(3)"
name: "stdios_basefailure"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdios_basefailure/"
description: "std::ios_base::failure – std::ios_base::failure"
---

<p>std::ios_base::failure &#8211; std::ios_base::failure</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;ios&gt;

class failure;</code></pre>
<p>The class std::ios_base::failure defines an exception object that is thrown on failure by the functions in the Input/Output library.<br />
std::ios_base::failure may be defined either as a member class of std::ios_base or as a synonym <i>(typedef)</i> for another class with equivalent functionality.<br />
<i>(since C++17)</i><br />
&nbsp;std-ios base-failure-2003-inheritance.svg <i>(until C++11)</i><br />
Inheritance diagram<br />
&nbsp;std-ios base-failure-inheritance.svg <i>(since C++11)</i><br />
Inheritance diagram </p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the exception object<br />
constructor <i>(public member function)</i> </p>
<p>&nbsp;std::ios_base::failure::failure </p>
<p>explicit failure( const std::string&amp; message ); <i>(until C++11)</i><br />
explicit failure( const std::string&amp; message, <i>(since C++11)</i><br />
const std::error_code&amp; ec = std::io_errc::stream );<br />
explicit failure( const char* message, <i>(since C++11)</i><br />
const std::error_code&amp; ec = std::io_errc::stream ); </p>
<p>Constructs the exception object using message as explanation string which can later be retrieved using what().</p>
<h2>Parameters</h2>
<p>message &#8211; explanatory string </p>
<p>Inherited from std::system_error</p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns error code<br />
code <i>(public member function of std::system_error)</i> </p>
<p>what returns explanatory string<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual public member function of std::system_error)</i><br />
<code>[virtual]</code> </p>
<p>Inherited from std::runtime_error </p>
<p>Inherited from std::exception</p>
<h2>Member functions</h2>
<p>destructor destroys the exception object<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual public member function of std::exception)</i><br />
<code>[virtual]</code> </p>
<p>what returns an explanatory string<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual public member function of std::exception)</i><br />
<code>[virtual]</code></p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;fstream&gt;

int main()

{
    std::ifstream f(&quot;doesn't exist&quot;);
    try {
        f.exceptions(f.failbit);
    } catch (const std::ios_base::failure &amp;e) {
        std::cout &lt;&lt; &quot;Caught an ios_base::failure.
&quot;
                  &lt;&lt; &quot;Explanatory string: &quot; &lt;&lt; e.what() &lt;&lt; '
'
                  &lt;&lt; &quot;Error code: &quot; &lt;&lt; e.code() &lt;&lt; '
';
    }
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;Caught an ios_base::failure.<br />
&nbsp;<wbr>&nbsp;Explanatory string: ios_base::clear: unspecified iostream_category error<br />
&nbsp;<wbr>&nbsp;Error code: iostream:1</p>
<h2>See also</h2>
<p>io_errc the IO stream error codes<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(enum)</i><br />
<i>(C++11)</i> </p>
