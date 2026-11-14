---
title: "stdexperimentalto_array(3)"
name: "stdexperimentalto_array"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalto_array/"
---

std::experimental::to_array - std::experimental::to_array

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/array&gt;

template &lt;class T, std::size_t N&gt;                                  (library fundamentals TS v2)

constexpr std::array&lt;std::remove_cv_t&lt;T&gt;, N&gt; to_array(T (&amp;a)[N]);</code></pre> 
Creates a std::array from the built-in array a. The elements of the std::array are copy-initialized from the corresponding element of a. 

<h2>Parameters</h2>

a - the built-in array to be used to initialize the std::array

<h2>Return value</h2>

An std::array object whose elements are copy-initialized from the corresponding element of a. 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;namespace detail { 
&nbsp;<wbr>&nbsp;template &lt;class T, std::size_t N, std::size_t... I&gt; 
&nbsp;<wbr>&nbsp;constexpr std::array&lt;std::remove_cv_t&lt;T&gt;, N&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;to_array_impl(T (&amp;a)[N], std::index_sequence&lt;I...&gt;) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return { {a[I]...} }; 
&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;} 

 
&nbsp;<wbr>&nbsp;template &lt;class T, std::size_t N&gt; 
&nbsp;<wbr>&nbsp;constexpr std::array&lt;std::remove_cv_t&lt;T&gt;, N&gt; to_array(T (&amp;a)[N]) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return detail::to_array_impl(a, std::make_index_sequence&lt;N&gt;{}); 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;cstdlib&gt;

#include &lt;cassert&gt;

#include &lt;experimental/array&gt;

#include &lt;unistd.h&gt;
// mkstemp(3) that works

template &lt;std::size_t N&gt;

int tempfd(char const (&amp;tmpl)[N])

{
    auto s = std::experimental::to_array(tmpl);
    int fd = mkstemp(s.data());
    if (fd != -1)
        unlink(s.data());
    return fd;
}
int main()

{
    int fd = tempfd(&quot;/tmp/test.XXXXXX&quot;);
    int rt = close(fd);
    assert(rt == 0);
}
</code></pre>

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Creates a std::array object whose size and optionally element type are deduced from the arguments 
make_array <i>(function template)</i> 
