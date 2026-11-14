---
title: "stdbad_exception(3)"
name: "stdbad_exception"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbad_exception/"
description: "std::bad_exception – std::bad_exception"
---

<p>std::bad_exception &#8211; std::bad_exception</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;exception&gt;

class bad_exception;</code></pre>
<p>std::bad_exception is the type of the exception thrown by the C++ runtime in the following situations:<br />
1) If std::exception_ptr stores a copy of the caught exception and if the copy constructor of the exception object caught by std::current_exception throws an exception, the captured exception is an instance of std::bad_exception.<br />
2) If a dynamic_exception_specification is violated and std::unexpected throws or rethrows an exception that still violates the exception specification, but the exception specification allows std::bad_exception, std::bad_exception is thrown. <i>(until C++17)</i><br />
&nbsp;std-bad exception-inheritance.svg<br />
Inheritance diagram </p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs the bad_exception object<br />
constructor <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies the object<br />
operator= <i>(public member function)</i> </p>
<p>what returns the explanatory string<br />
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
<pre><code>#include &lt;iostream&gt;

#include &lt;exception&gt;

#include &lt;stdexcept&gt;
void my_unexp()
{
    throw;
}
void test() throw(std::bad_exception)

{
    throw std::runtime_error(&quot;test&quot;);
}
int main()

{
    std::set_unexpected(my_unexp);
    try {
        test();
    } catch (const std::bad_exception &amp;e) {
        std::cerr &lt;&lt; &quot;Caught &quot; &lt;&lt; e.what() &lt;&lt; '
';
    }
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;Caught std::bad_exception</p>
