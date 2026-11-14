---
title: "stdends(3)"
name: "stdends"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdends/"
---

std::ends - std::ends

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;ostream&gt;

template&lt; class CharT, class Traits &gt;

std::basic_ostream&lt;CharT, Traits&gt;&amp; ends( std::basic_ostream&lt;CharT, Traits&gt;&amp; os );</code></pre> 
Inserts a null character into the output sequence os as if by calling os.put(CharT()). 
This is an output-only I/O manipulator, it may be called with an expression such as out &lt;&lt; std::ends for any out of type std::basic_ostream. 

<h2>Notes</h2>

This manipulator is typically used with std::ostrstream, when the associated output buffer needs to be null-terminated to be processed as a C string. 
Unlike std::endl, this manipulator does not flush the stream. 

<h2>Parameters</h2>

os - reference to output stream

<h2>Return value</h2>

os (reference to the stream after insertion of the null character) 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;cstdio&gt;

#include &lt;strstream&gt;

int main()

{
    std::ostrstream oss;
    oss &lt;&lt; &quot;Sample text: &quot; &lt;&lt; 42 &lt;&lt; std::ends;
    std::printf(&quot;%s\n&quot;, oss.str());
    oss.freeze(false); // enable memory deallocation
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Sample text: 42

<h2>See also</h2>

ostrstream implements character array output operations 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
(deprecated in C++98) 
