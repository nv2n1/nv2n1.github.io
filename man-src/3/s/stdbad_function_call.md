---
title: "stdbad_function_call(3)"
name: "stdbad_function_call"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbad_function_call/"
description: "std::bad_function_call – std::bad_function_call"
---

<p>std::bad_function_call &#8211; std::bad_function_call</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;functional&gt;<br />
class bad_function_call; <i>(since C++11)</i><br />
std::bad_function_call is the type of the exception thrown by std::function::operator() if the function wrapper has no target.<br />
&nbsp;std-bad function call-inheritance.svg<br />
Inheritance diagram </p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the bad_function_call object<br />
constructor <i>(public member function)</i> </p>
<p>&nbsp;std::bad_function_call::bad_function_call() </p>
<p>bad_function_call() noexcept; </p>
<p>Constructs a new instance of std::bad_function_call.</p>
<h2>Parameters</h2>
<p><i>(none)</i> </p>
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

#include &lt;functional&gt;
int main()

{
    std::function&lt;int()&gt; f = nullptr;
    try {
        f();
    } catch (const std::bad_function_call &amp;e) {
        std::cout &lt;&lt; e.what() &lt;&lt; '
';
    }
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;bad function call</p>
<h2>See also</h2>
<p>function wraps callable object of any type with specified function call signature<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i> </p>
