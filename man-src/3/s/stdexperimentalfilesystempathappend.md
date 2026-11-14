---
title: "stdexperimentalfilesystempathappend(3)"
name: "stdexperimentalfilesystempathappend"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystempathappend/"
description: "std::experimental::filesystem::path::append, – std::experimental::filesystem::path::append,"
---

<p>std::experimental::filesystem::path::append, &#8211; std::experimental::filesystem::path::append,</p>
<h2>Synopsis</h2>
<pre><code>path &amp;operator/=(const path &amp;p);
(1)(filesystem TS)

    template &lt;class Source&gt;
    (2)(filesystem TS)

        path &amp;
        operator/=(const Source &amp;source);

template &lt;class Source&gt;
(3)(filesystem TS)

    path &amp;append(const Source &amp;source);

template &lt;class InputIt&gt;
(4)(filesystem TS)

    path &amp;append(InputIt first, InputIt last);</code></pre>
<p>1)&nbsp;<wbr>First, appends the preferred directory separator to this, except if any of the<br />
following conditions is true:<br />
*&nbsp;<wbr>the separator would be redundant&nbsp;<wbr>(*this already ends with a separator)<br />
*&nbsp;<wbr>*this is empty, or adding it would turn a relative path to an absolute path in<br />
some other way<br />
*&nbsp;<wbr>p is an empty path.<br />
*&nbsp;<wbr>p.native()&nbsp;<wbr>begins with a directory separator.<br />
Then, appends p.native()&nbsp;<wbr>to the pathname maintained by&nbsp;<wbr>*this<br />
2,3)&nbsp;<wbr>Same as&nbsp;<wbr><code>(1)</code>, but accepts any std::basic_string, null-terminated multicharacter<br />
string, or an input iterator pointing to a null-terminated multicharacter sequence.<br />
4)&nbsp;<wbr>Same as&nbsp;<wbr><code>(1)</code>, but accepts any iterator pair that designates a multicharacter<br />
string. </p>
<h2>Parameters</h2>
<p>p&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; pathname to append<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>std::basic_string, null-terminated multicharacter string, or an input<br />
source&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; iterator pointing to a null-terminated multicharacter sequence, which<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>represents a path name&nbsp;<wbr>(either in portable or in native format)<br />
first, last&nbsp;<wbr>&nbsp;<wbr>&#8211; pair of LegacyInputIterators that specify a multicharacter sequence<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>that represents a path name</p>
<h2>Type requirements</h2>
<p>&#8211;<br />
InputIt must meet the requirements of LegacyInputIterator.<br />
&#8211;<br />
The value type of InputIt must be one of the encoded character types&nbsp;<wbr>(char, wchar_t,<br />
char16_t and char32_t)</p>
<h2>Return value</h2>
<p>*this </p>
<h2>Exceptions</h2>
<p>May throw filesystem_error on underlying OS API errors or std::bad_alloc if memory<br />
allocation fails.</p>
<h2>Example</h2>
<p>// Run this code #include &lt;iostream&gt;</p>
<p>#include &lt;experimental/filesystem&gt;</p>
<p>namespace fs = std::experimental::filesystem;</p>
<p>int main()<br />
{<br />
    fs::path p1 = &quot;C:&quot;;<br />
    p1 /= &quot;Users&quot;; // does not insert a separator<br />
                   // &quot;C:Users&quot; is a relative path in Windows<br />
                   // adding directory separator would turn it to an absolute path<br />
    std::cout &lt;&lt; &quot;\&quot;C:\&quot; / \&quot;Users\&quot; == &quot; &lt;&lt; p1 &lt;&lt; &#8216;
&#8217;;<br />
    p1 /= &quot;batman&quot;; // inserts fs::path::preferred_separator, &#8216;\&#8217; on Windows<br />
    std::cout &lt;&lt; &quot;\&quot;C:\&quot; / \&quot;Users\&quot; / \&quot;batman\&quot; == &quot; &lt;&lt; p1 &lt;&lt; &#8216;
&#8217;;<br />
}</p>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&quot;C:&quot;&nbsp;<wbr>/&nbsp;<wbr>&quot;Users&quot;&nbsp;<wbr>==&nbsp;<wbr>&quot;C:Users&quot;<br />
&nbsp;<wbr>&quot;C:&quot;&nbsp;<wbr>/&nbsp;<wbr>&quot;Users&quot;&nbsp;<wbr>/&nbsp;<wbr>&quot;batman&quot;&nbsp;<wbr>==&nbsp;<wbr>&quot;C:Usersatman&quot;</p>
<h2>See also</h2>
<pre><code>concat     concatenates two paths without introducing a directory separator

operator+= (public member function)

operator/  concatenates two paths with a directory separator
(function)
</code></pre>
