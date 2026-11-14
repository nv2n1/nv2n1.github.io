---
title: "stdbasic_istream(3)"
name: "stdbasic_istream"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdbasic_istream/"
---

std::basic_istream&lt;CharT,Traits&gt;::~basic_istream - std::basic_istream&lt;CharT,Traits&gt;::~basic_istream

<h2>Synopsis</h2>

<pre><code>virtual ~basic_istream();</code></pre> 
Destructs the input stream. 

<h2>Notes</h2>

This destructor does not perform any operation on the underlying streambuffer (rdbuf()): the destructors of the derived input streams such as std::basic_ifstream and std::basic_istringstream are responsible for calling the destructors of the streambuffers. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;sstream&gt;

#include &lt;iostream&gt;
void print_stringbuf(std::streambuf *p)

{
    std::istream buf(p); // buf shares the buffer with s1
    int n;
    buf &gt;&gt; n;
    std::cout &lt;&lt; n;

} // calls the destructor of buf. p remains unaffected
int main()

{
    std::istringstream s1(&quot;10 20&quot;);
    print_stringbuf(s1.rdbuf());
    int n;
    s1 &gt;&gt; n;
    std::cout &lt;&lt; ',' &lt;&lt; n &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;10,20
