---
title: "stdexperimentalfilesystemrecursive_directory_iteratordisable_recursion_pending(3)"
name: "stdexperimentalfilesystemrecursive_directory_iteratordisable_recursion_pending"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemrecursive_directory_iteratordisable_recursion_pending/"
---

std::experimental::filesystem::recursive_directory_iterator::disable_recursion_pending - std::experimental::filesystem::recursive_directory_iterator::disable_recursion_pending

<h2>Synopsis</h2>

<pre><code>void disable_recursion_pending();
(filesystem TS)</code></pre> 
Disables recursion to the currently referred subdirectory, if any. 
The call modifies the pending recursion flag on the iterator in such a way that the next time increment is called, the iterator will advance within the current directly even if it is currently referring to a subdirectory that hasn't been visited. 
The status of the pending recursion flag can be queried with recursion_pending(), which is false after this call. It is reset back to true after increment, and its initial value is also true. 
The behavior is undefined if *this is the end iterator. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

<i>(none)</i> 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Example</h2>

// Run this code <pre><code>#include &lt;fstream&gt;

#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;experimental/filesystem&gt;

namespace fs = std::experimental::filesystem;
int main()

{
    fs::create_directories(&quot;sandbox/a/b/c&quot;);
    fs::create_directories(&quot;sandbox/a/b/d/e&quot;);
    std::ofstream(&quot;sandbox/a/b/file1.txt&quot;);
    fs::create_symlink(&quot;a&quot;, &quot;sandbox/syma&quot;);
    for (auto i = fs::recursive_directory_iterator(&quot;sandbox&quot;);
         i != fs::recursive_directory_iterator();
         ++i) {
        std::cout &lt;&lt; std::string(i.depth(), ' ') &lt;&lt; *i;
        if (fs::is_symlink(i-&gt;symlink_status()))
            std::cout &lt;&lt; &quot; -&gt; &quot; &lt;&lt; fs::read_symlink(*i);
        std::cout &lt;&lt; '\n';
        // do not descend into &quot;b&quot;
        if (i-&gt;path().filename() == &quot;b&quot;)
            i.disable_recursion_pending();
    }
    fs::remove_all(&quot;sandbox&quot;);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;&quot;sandbox/a&quot; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;sandbox/a/b&quot; 
&nbsp;<wbr>&nbsp;&quot;sandbox/syma&quot; -&gt; &quot;a&quot;

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether the recursion is disabled for the current directory 
recursion_pending <i>(public member function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;advances to the next entry 
increment <i>(public member function)</i> 
operator++ 
