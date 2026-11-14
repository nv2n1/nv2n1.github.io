---
title: "stdrename(3)"
name: "stdrename"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrename/"
---

std::rename - std::rename

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdio&gt;

    int rename(const char *old_filename, const char *new_filename);</code></pre> 
Changes the filename of a file. The file is identified by character string pointed to by old_filename. The new filename is identified by character string pointed to by new_filename. 
If new_filename exists, the behavior is implementation-defined. 

<h2>Parameters</h2>

old_filename - pointer to a null-terminated string containing the path identifying the file to rename 
new_filename - pointer to a null-terminated string containing the new path of the file

<h2>Return value</h2>

0 upon success or non-zero value on error. 

<h2>Notes</h2>

POSIX specifies many additional details on the semantics of this function, which are reproduced in C++ by std::experimental::filesystem::rename. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;fstream&gt;

#include &lt;cstdio&gt;

int main()

{
    bool ok{std::ofstream(&quot;from.txt&quot;).put('a')}; // create and write to file
    if (!ok) {
        std::perror(&quot;Error creating from.txt&quot;);
        return 1;
    }
    if (std::rename(&quot;from.txt&quot;, &quot;to.txt&quot;)) {
        std::perror(&quot;Error renaming&quot;);
        return 1;
    }
    std::cout &lt;&lt; std::ifstream(&quot;to.txt&quot;).rdbuf() &lt;&lt; '\n'; // print file
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;a

<h2>See also</h2>

rename moves or renames a file or directory 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;erases a file 
remove <i>(function)</i> 
