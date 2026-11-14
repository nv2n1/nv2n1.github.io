---
title: "stdfilesystempathbeginstdfilesystempathend(3)"
name: "stdfilesystempathbeginstdfilesystempathend"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystempathbeginstdfilesystempathend/"
description: "std::filesystem::path::begin,std::filesystem::path::end – std::filesystem::path::begin,std::filesystem::path::end"
---

<p>std::filesystem::path::begin,std::filesystem::path::end &#8211; std::filesystem::path::begin,std::filesystem::path::end</p>
<h2>Synopsis</h2>
<p>iterator begin() const; <code>(1)</code> <i>(since C++17)</i><br />
iterator end() const; <code>(2)</code> <i>(since C++17)</i><br />
1) Returns an iterator to the first element of the path. If the path is empty, the returned iterator is equal to end().<br />
2) Returns an iterator one past the last element of the path. Dereferencing this iterator is undefined behavior.<br />
The sequence denoted by this pair of iterators consists of the following:<br />
1) root-name (if any)<br />
2) root-directory (if any)<br />
3) sequence of file-names, omitting any directory separators<br />
4) If there is a directory separator after the last file-name in the path, the last element before the end iterator is an empty element. </p>
<h2>Parameters</h2>
<p><i>(none)</i></p>
<h2>Return value</h2>
<p>1) Iterator to the first element of the path.<br />
2) Iterator one past the end of the path </p>
<h2>Exceptions</h2>
<p><i>(none)</i></p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;filesystem&gt;

namespace fs = std::filesystem;

int main()

{
    fs::path p = &quot;C:\users\abcdef\AppData\Local\Temp\&quot;;
    std::cout &lt;&lt; &quot;Examining the path &quot; &lt;&lt; p &lt;&lt; &quot; through iterators gives
&quot;;
    for (auto &amp;e : p)
        std::cout &lt;&lt; e &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;Examining the path &quot;C:
