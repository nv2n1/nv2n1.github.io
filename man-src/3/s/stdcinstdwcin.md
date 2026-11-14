---
title: "stdcinstdwcin(3)"
name: "stdcinstdwcin"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcinstdwcin/"
description: "std::cin,std::wcin – std::cin,std::wcin"
---

<p>std::cin,std::wcin &#8211; std::cin,std::wcin</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;iostream&gt;<br />
extern std::istream cin; <code>(1)</code><br />
extern std::wistream wcin; <code>(2)</code><br />
The global objects std::cin and std::wcin control input from a stream buffer of implementation-defined type (derived from std::streambuf), associated with the standard C input stream stdin.<br />
These objects are guaranteed to be initialized during or before the first time an object of type std::ios_base::Init is constructed and are available for use in the constructors and destructors of static objects with ordered_initialization (as long as &lt;iostream&gt; is included before the object is defined).<br />
Unless sync_with_stdio(false) has been issued, it is safe to concurrently access these objects from multiple threads for both formatted and unformatted input.<br />
Once std::cin is constructed, std::cin.tie() returns &amp;std::cout, and likewise, std::wcin.tie() returns &amp;std::wcout. This means that any formatted input operation on std::cin forces a call to std::cout.flush() if any characters are pending for output. </p>
<h2>Notes</h2>
<p>The &#8216;c&#8217; in the name refers to &quot;character&quot; (stroustrup.com_FAQ); cin means &quot;character input&quot; and wcin means &quot;wide character input&quot; </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

struct Foo {
    int n;
    Foo()
    {
        std::cout &lt;&lt; &quot;Enter n: &quot;; // no flush needed
        std::cin &gt;&gt; n;
    }
};

Foo f; // static object

int main()

{
    std::cout &lt;&lt; &quot;f.n is &quot; &lt;&lt; f.n &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;Enter n: 10<br />
&nbsp;<wbr>&nbsp;f.n is 10</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;initializes standard stream objects<br />
Init <i>(public member class of std::ios_base)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;writes to the standard C output stream stdout<br />
cout (global object)<br />
wcout </p>
