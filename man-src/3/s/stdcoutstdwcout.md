---
title: "stdcoutstdwcout(3)"
name: "stdcoutstdwcout"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcoutstdwcout/"
description: "std::cout,std::wcout – std::cout,std::wcout"
---

<p>std::cout,std::wcout &#8211; std::cout,std::wcout</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;iostream&gt;<br />
extern std::ostream cout; <code>(1)</code><br />
extern std::wostream wcout; <code>(2)</code><br />
The global objects std::cout and std::wcout control output to a stream buffer of implementation-defined type (derived from std::streambuf), associated with the standard C output stream stdout.<br />
These objects are guaranteed to be initialized during or before the first time an object of type std::ios_base::Init is constructed and are available for use in the constructors and destructors of static objects with ordered_initialization (as long as &lt;iostream&gt; is included before the object is defined).<br />
Unless sync_with_stdio(false) has been issued, it is safe to concurrently access these objects from multiple threads for both formatted and unformatted output.<br />
Once initialized, std::cout is tie()&#8217;d to std::cin and std::wcout is tie()&#8217;d to std::wcin, meaning that any input operation on std::cin executes std::cout.flush() (via std::basic_istream::sentry&#8217;s constructor).<br />
Once initialized, std::cout is also tie()&#8217;d to std::cerr and std::wcout is tie()&#8217;d to std::wcerr, meaning that any output operation on std::cerr executes std::cout.flush() (via std::basic_ostream::sentry&#8217;s constructor) <i>(since C++11)</i> </p>
<h2>Notes</h2>
<p>The &#8216;c&#8217; in the name refers to &quot;character&quot; (stroustrup.com_FAQ); cout means &quot;character output&quot; and wcout means &quot;wide character output&quot; </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

struct Foo {
    int n;
    Foo()
    {
        std::cout &lt;&lt; &quot;static constructor
&quot;;
    }
    ~Foo()
    {
        std::cout &lt;&lt; &quot;static destructor
&quot;;
    }
};

Foo f; // static object

int main()

{
    std::cout &lt;&lt; &quot;main function
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
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;writes to the standard C error stream stderr<br />
clog (global object)<br />
wclog </p>
