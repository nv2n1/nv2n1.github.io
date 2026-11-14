---
title: "stdexperimentalfilesystemread_symlink(3)"
name: "stdexperimentalfilesystemread_symlink"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemread_symlink/"
---

std::experimental::filesystem::read_symlink - std::experimental::filesystem::read_symlink

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / filesystem&gt;

    path read_symlink(const path &amp;p);
(filesystem TS)

    path read_symlink(const path &amp;p, error_code &amp;ec);</code></pre> 
If the path p refers to a symbolic link, returns a new path object which refers to the target of that symbolic link. 
It is an error if p does not refer to a symbolic link. 
The non-throwing overload returns an empty path on errors. 

<h2>Parameters</h2>

p - path to a symlink 
ec - out-parameter for error reporting in the non-throwing overload

<h2>Return value</h2>

The target of the symlink (which may not necessarily exist) 

<h2>Exceptions</h2>

The overload that does not take a error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first argument and the OS error code as the error code argument. std::bad_alloc may be thrown if memory allocation fails. The overload taking a error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. This overload has 
noexcept specification: 
noexcept

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;experimental/filesystem&gt;

namespace fs = std::experimental::filesystem;

int main()

{
    // on a typical Linux system, /lib/libc.so.6 is a symlink
    fs::path p = &quot;/lib/libc.so.6&quot;;
    if (exists(p) &amp;&amp; is_symlink(p))
        std::cout &lt;&lt; p &lt;&lt; &quot; -&gt; &quot; &lt;&lt; read_symlink(p) &lt;&lt; '\n';
    else
        std::cout &lt;&lt; p &lt;&lt; &quot; does not exist or is not a symlink\n&quot;;
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;&quot;/lib/libc.so.6&quot; -&gt; &quot;libc-2.12.so&quot;

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks whether the argument refers to a symbolic link 
is_symlink <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a symbolic link 
create_symlink <i>(function)</i> 
create_directory_symlink 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies a symbolic link 
copy_symlink <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;determines file attributes 
status determines file attributes, checking the symlink target 
symlink_status <i>(function)</i> 
