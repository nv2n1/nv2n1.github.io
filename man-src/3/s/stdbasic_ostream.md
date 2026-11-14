---
title: "stdbasic_ostream(3)"
name: "stdbasic_ostream"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbasic_ostream/"
---

std::basic_ostream&lt;CharT,Traits&gt;::~basic_ostream - std::basic_ostream&lt;CharT,Traits&gt;::~basic_ostream

<h2>Synopsis</h2>

<pre><code>virtual ~basic_ostream();</code></pre> 
Destroys the basic_ostream object. This destructor does not perform any operation on the underlying streambuffer (rdbuf()): the destructors of the derived output streams such as std::basic_ofstream and std::basic_ostringstream are responsible for calling the destructors of the stream buffers. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;sstream&gt;

#include &lt;iostream&gt;

void add_words(std::streambuf *p)

{
    std::ostream buf(p); // buf shares the buffer with s
    buf &lt;&lt; &quot; is the answer&quot;;

} // calls the destructor of buf. p remains unaffected

int main()

{
    std::ostringstream s;
    s &lt;&lt; 42;
    add_words(s.rdbuf());
    s &lt;&lt; &quot;.&quot;;
    std::cout &lt;&lt; s.str() &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;42 is the answer.
