---
title: "stdregex_error(3)"
name: "stdregex_error"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdregex_error/"
description: "std::regex_error – std::regex_error"
---

<p>std::regex_error &#8211; std::regex_error</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;regex&gt;<br />
class regex_error; <i>(since C++11)</i><br />
Defines the type of exception object thrown to report errors in the regular expressions library.<br />
&nbsp;std-regex error-inheritance.svg<br />
Inheritance diagram </p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a regex_error object<br />
constructor <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gets the std::regex_constants::error_type for a regex_error<br />
code <i>(public member function)</i> </p>
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
<pre><code>#include &lt;regex&gt;

#include &lt;iostream&gt;
int main()

{
    try {
        std::regex re(&quot;[a-b][a&quot;);
    } catch (const std::regex_error &amp;e) {
        std::cout &lt;&lt; &quot;regex_error caught: &quot; &lt;&lt; e.what() &lt;&lt; '
';
        if (e.code() == std::regex_constants::error_brack) {
            std::cout &lt;&lt; &quot;The code was error_brack
&quot;;
        }
    }
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;regex_error caught: The expression contained mismatched [ and ].<br />
&nbsp;<wbr>&nbsp;The code was error_brack</p>
