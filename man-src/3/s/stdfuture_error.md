---
title: "stdfuture_error(3)"
name: "stdfuture_error"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfuture_error/"
description: "std::future_error – std::future_error"
---

<p>std::future_error &#8211; std::future_error</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;future&gt;<br />
class future_error; <i>(since C++11)</i><br />
The class std::future_error defines an exception object that is thrown on failure by the functions in the thread library that deal with asynchronous execution and shared states (std::future, std::promise, etc). Similar to std::system_error, this exception carries an error code compatible with std::error_code.<br />
&nbsp;std-future error-inheritance.svg<br />
Inheritance diagram </p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a std::future_error object<br />
constructor <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the error code<br />
code <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the explanatory string specific to the error code<br />
what <i>(public member function)</i> </p>
<p>Inherited from std::logic_error </p>
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
<pre><code>#include &lt;future&gt;

#include &lt;iostream&gt;
int main()

{
    std::future&lt;int&gt; empty;
    try {
        int n = empty.get(); // The behavior is undefined, but
                             // some implementations throw std::future_error
    } catch (const std::future_error &amp;e) {
        std::cout &lt;&lt; &quot;Caught a future_error with code \&quot;&quot; &lt;&lt; e.code()
                  &lt;&lt; &quot;\&quot;
Message: \&quot;&quot; &lt;&lt; e.what() &lt;&lt; &quot;\&quot;
&quot;;
    }
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;Caught a future_error with code &quot;future:3&quot;<br />
&nbsp;<wbr>&nbsp;Message: &quot;No associated state&quot;</p>
<h2>See also</h2>
<p>future_errc identifies the future error codes<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(enum)</i><br />
<i>(C++11)</i> </p>
