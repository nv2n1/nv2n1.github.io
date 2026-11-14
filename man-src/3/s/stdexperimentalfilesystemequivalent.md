---
title: "stdexperimentalfilesystemequivalent(3)"
name: "stdexperimentalfilesystemequivalent"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemequivalent/"
---

std::experimental::filesystem::equivalent - std::experimental::filesystem::equivalent

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / filesystem&gt;

    bool equivalent(const path &amp;p1, const path &amp;p2);
(1)(filesystem TS)

    bool equivalent(const path &amp;p1, const path &amp;p2, error_code &amp;ec);</code></pre> 
Checks whether the paths p1 and p2 refer to the same file or directory and have the same file status as determined by status (symlinks are followed). 
If p1 or p2 does not exist or if their file type is not file, directory, or symlink (as determined by is_other), an error is reported. 
The non-throwing overload returns false on errors. 

<h2>Parameters</h2>

p1, p2 - paths to check for equivalence 
ec - out-parameter for error reporting in the non-throwing overload

<h2>Return value</h2>

true if the p1 and p2 refer to the same file or directory and their file status is the same. false otherwise. 

<h2>Exceptions</h2>

The overload that does not take a error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p1 as the first argument, p2 as the second argument, and the OS error code as the error code argument. std::bad_alloc may be thrown if memory allocation fails. The overload taking a error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. This overload has 
noexcept specification: 
noexcept

<h2>Notes</h2>

Two paths are considered to resolve to the same file system entity if st_dev and st_ino of their POSIX stat_structure, obtained as if by POSIX stat, are equal. (meaning, the files are locate on the same device at the same location) 
In particular, all hard links for the same file or directory are equivalent, and a symlink and its target on the same file system are equivalent. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cstdint&gt;

#include &lt;experimental/filesystem&gt;

namespace fs = std::experimental::filesystem;

int main()

{
    // hard link equivalency
    fs::path p1 = &quot;.&quot;;
    fs::path p2 = fs::current_path();
    if (fs::equivalent(p1, p2))
        std::cout &lt;&lt; p1 &lt;&lt; &quot; is equivalent to &quot; &lt;&lt; p2 &lt;&lt; '\n';
    // symlink equivalency
    fs::path p3 = &quot;/lib/libc.so.6&quot;;
    fs::path p4 = p3.parent_path() / fs::read_symlink(p3);
    if (fs::equivalent(p3, p4))
        std::cout &lt;&lt; p3 &lt;&lt; &quot; is equivalent to &quot; &lt;&lt; p4 &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;&quot;.&quot; is equivalent to &quot;/var/tmp/test&quot; 
&nbsp;<wbr>&nbsp;&quot;/lib/libc.so.6&quot; is equivalent to &quot;/lib/libc-2.12.so&quot;

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;determines file attributes 
status determines file attributes, checking the symlink target 
symlink_status <i>(function)</i> 
