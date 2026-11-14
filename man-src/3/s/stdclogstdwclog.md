---
title: "stdclogstdwclog(3)"
name: "stdclogstdwclog"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdclogstdwclog/"
description: "std::clog,std::wclog – std::clog,std::wclog"
---

<p>std::clog,std::wclog &#8211; std::clog,std::wclog</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;iostream&gt;<br />
extern std::ostream clog; <code>(1)</code><br />
extern std::wostream wclog; <code>(2)</code><br />
The global objects std::clog and std::wclog control output to a stream buffer of implementation-defined type (derived from std::streambuf), associated with the standard C output stream stderr, but, unlike std::cerr/std::wcerr, these streams are not automatically flushed and not automatically tie()&#8217;d with cout.<br />
These objects are guaranteed to be initialized during or before the first time an object of type std::ios_base::Init is constructed and are available for use in the constructors and destructors of static objects with ordered_initialization (as long as &lt;iostream&gt; is included before the object is defined).<br />
Unless sync_with_stdio(false) has been issued, it is safe to concurrently access these objects from multiple threads for both formatted and unformatted output. </p>
<h2>Notes</h2>
<p>The &#8216;c&#8217; in the name refers to &quot;character&quot; (stroustrup.com_FAQ); clog means &quot;character log&quot; and wclog means &quot;wide character log&quot; </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;
struct Foo {
    int n;
    Foo()
    {
        std::clog &lt;&lt; &quot;static constructor
&quot;;
    }
    ~Foo()
    {
        std::clog &lt;&lt; &quot;static destructor
&quot;;
    }
};</code></pre>
<p>&nbsp;<wbr>&nbsp;Foo f; // static object </p>
<pre><code>int main()

{
    std::clog &lt;&lt; &quot;main function
&quot;;
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;static constructor<br />
&nbsp;<wbr>&nbsp;main function<br />
&nbsp;<wbr>&nbsp;static destructor</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;initializes standard stream objects<br />
Init <i>(public member class of std::ios_base)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;writes to the standard C error stream stderr, unbuffered<br />
cerr (global object)<br />
wcerr<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;writes to the standard C output stream stdout<br />
cout (global object)<br />
wcout </p>
