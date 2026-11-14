---
title: "stdsystem_error(3)"
name: "stdsystem_error"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsystem_error/"
description: "std::system_error – std::system_error"
---

<p>std::system_error &#8211; std::system_error</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;system_error&gt;<br />
class system_error; <i>(since C++11)</i><br />
std::system_error is the type of the exception thrown by various library functions (typically the functions that interface with the OS facilities, e.g. the constructor of std::thread) when the exception has an associated std::error_code, which may be reported.<br />
&nbsp;std-system error-inheritance.svg<br />
Inheritance diagram </p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the system_error object<br />
constructor <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns error code<br />
code <i>(public member function)</i> </p>
<p>what returns explanatory string<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual public member function)</i><br />
<code>[virtual]</code> </p>
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
<pre><code>#include &lt;thread&gt;

#include &lt;iostream&gt;

#include &lt;system_error&gt;
int main()

{
    try {
        std::thread().detach(); // attempt to detach a non-thread
    } catch (const std::system_error &amp;e) {
        std::cout &lt;&lt; &quot;Caught system_error with code &quot; &lt;&lt; e.code()
                  &lt;&lt; &quot; meaning &quot; &lt;&lt; e.what() &lt;&lt; '
';
    }
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;Caught system_error with code generic:22 meaning Invalid argument</p>
