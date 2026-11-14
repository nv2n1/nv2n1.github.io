---
title: "stdws(3)"
name: "stdws"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdws/"
---

std::ws - std::ws

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;istream&gt;

template&lt; class CharT, class Traits &gt;

std::basic_istream&lt;CharT,Traits&gt;&amp; ws( std::basic_istream&lt;CharT, Traits&gt;&amp; is );</code></pre> 
Discards leading whitespace from an input stream. 
Behaves as an UnformattedInputFunction, except that is.gcount() is not modified. After constructing and checking the sentry object, extracts characters from the stream and discards them until any one of the following conditions occurs: 
* end of file condition occurs in the input sequence (in which case the function calls setstate(eofbit) but does not set failbit; this does not apply if the eofbit is already set on is prior to the call to ws, in which case the construction of the sentry object would set failbit). 
* the next available character c in the input sequence is not whitespace as determined by std::isspace(c, is.getloc()). The non-whitespace character is not extracted. 
This is an input-only I/O manipulator, it may be called with an expression such as in &gt;&gt; std::ws for any in of type std::basic_istream. 

<h2>Parameters</h2>

is - reference to input stream

<h2>Return value</h2>

is (reference to the stream after extraction of consecutive whitespace) 

<h2>Notes</h2>

If eofbit is set on the stream prior to the call, the construction of the sentry object will set failbit. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;istream&gt;

#include &lt;sstream&gt;

#include &lt;string&gt;
int main()

{
    std::istringstream s(&quot;     this is a test&quot;);
    std::string line;
    std::getline(s &gt;&gt; std::ws, line);
    std::cout &lt;&lt; &quot;ws + getline returns: \&quot;&quot; &lt;&lt; line &lt;&lt; &quot;\&quot;\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;ws + getline returns: &quot;this is a test&quot;

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;extracts and discards characters until the given character is found 
ignore <i>(public member function of std::basic_istream&lt;CharT,Traits&gt;)</i> 
