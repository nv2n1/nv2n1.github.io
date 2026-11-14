---
title: "stdremove(3)"
name: "stdremove"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdremove/"
---

std::remove - std::remove

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdio&gt;

    int remove(const char *fname);</code></pre> 
Deletes the file identified by character string pointed to by fname. 
If the file is currently open by the current or another process, the behavior of this function is implementation-defined (in particular, POSIX systems unlink the file name, although the file system space is not reclaimed even if this was the last hardlink to the file until the last running process closes the file, Windows does not allow the file to be deleted) 

<h2>Parameters</h2>

fname - pointer to a null-terminated string containing the path identifying the file to delete

<h2>Return value</h2>

0 upon success or non-zero value on error. 

<h2>Notes</h2>

POSIX_specifies many additional details for the behavior of this function. 
The standard library also defines a function template std::remove taking a pair of iterators and a value, this overload is one of the standard algorithms. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;fstream&gt;

#include &lt;cstdio&gt;

int main()

{
    bool ok = static_cast&lt;bool&gt;(std::ofstream(&quot;file1.txt&quot;).put('a')); // create file
    if (!ok) {
        std::perror(&quot;Error creating file1.txt&quot;);
        return 1;
    }
    std::cout &lt;&lt; std::ifstream(&quot;file1.txt&quot;).rdbuf() &lt;&lt; '\n'; // print file
    std::remove(&quot;file1.txt&quot;);                                // delete file
    bool failed = !std::ifstream(&quot;file1.txt&quot;);
    if (failed) {
        std::perror(&quot;Error opening deleted file&quot;);
        return 1;
    }
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;a 
&nbsp;<wbr>&nbsp;Error opening deleted file: No such file or directory

<h2>See also</h2>

remove removes a file or empty directory 
remove_all removes a file or directory and all its contents, recursively 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
<i>(C++17)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;renames a file 
rename <i>(function)</i> 
