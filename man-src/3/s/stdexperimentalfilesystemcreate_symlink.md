---
title: "stdexperimentalfilesystemcreate_symlink(3)"
name: "stdexperimentalfilesystemcreate_symlink"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemcreate_symlink/"
description: "std::experimental::filesystem::create_symlink,std::experimental::filesystem::create_directory_symlink – std::experimental::filesystem::create_symlink,std::experimental::filesystem::create_directory..."
---

<p>std::experimental::filesystem::create_symlink,std::experimental::filesystem::create_directory_symlink &#8211; std::experimental::filesystem::create_symlink,std::experimental::filesystem::create_directory_symlink</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;experimental / filesystem&gt;

    void create_symlink(const path &amp;target, const path &amp;link);
(1)(filesystem TS)

    void create_symlink(const path &amp;target, const path &amp;link, error_code &amp;ec);

void create_directory_symlink(const path &amp;target, const path &amp;link);
(2)(filesystem TS)

    void create_directory_symlink(const path &amp;target, const path &amp;link, error_code &amp;ec);</code></pre>
<p>Creates a symbolic link link with its target set to target as if by POSIX symlink(): the pathname target may be invalid or non-existing.<br />
Some operating systems require symlink creation to identify that the link is to a directory. Portable code should use <code>(2)</code> to create directory symlinks rather than <code>(1)</code>, even though there is no distinction on POSIX systems. </p>
<h2>Parameters</h2>
<p>target &#8211; path to point the symlink to, does not have to exist<br />
link &#8211; path of the new symbolic link<br />
ec &#8211; out-parameter for error reporting in the non-throwing overload</p>
<h2>Return value</h2>
<p><i>(none)</i> </p>
<h2>Exceptions</h2>
<p>The overload that does not take a error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with target as the first argument, link as the second argument, and the OS error code as the error code argument. std::bad_alloc may be thrown if memory allocation fails. The overload taking a error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. This overload has<br />
noexcept specification:<br />
noexcept</p>
<h2>Notes</h2>
<p>Some operating systems do not support symbolic links at all or support them only for regular files.<br />
Some file systems do not support symbolic links regardless of the operating system, for example the FAT system used on some memory cards and flash drives.<br />
Like a hard link, a symbolic link allows a file to have multiple logical names. The presence of a hard link guarantees the existence of a file, even after the original name has been removed. A symbolic link provides no such assurance; in fact, the file named by the target argument need not exist when the link is created. A symbolic link can cross file system boundaries. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;experimental/filesystem&gt;

namespace fs = std::experimental::filesystem;
int main()

{
    fs::create_directories(&quot;sandbox/subdir&quot;);
    fs::create_symlink(&quot;target&quot;, &quot;sandbox/sym1&quot;);
    fs::create_directory_symlink(&quot;subdir&quot;, &quot;sandbox/sym2&quot;);
    for (auto it = fs::directory_iterator(&quot;sandbox&quot;); it != fs::directory_iterator(); ++it)
        if (is_symlink(it-&gt;symlink_status()))
            std::cout &lt;&lt; *it &lt;&lt; &quot;-&gt;&quot; &lt;&lt; read_symlink(*it) &lt;&lt; '
';
    fs::remove_all(&quot;sandbox&quot;);
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;&quot;sandbox/sym1&quot;-&gt;&quot;target&quot;<br />
&nbsp;<wbr>&nbsp;&quot;sandbox/sym2&quot;-&gt;&quot;subdir&quot;</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;determines file attributes<br />
status determines file attributes, checking the symlink target<br />
symlink_status <i>(function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;obtains the target of a symbolic link<br />
read_symlink <i>(function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a hard link<br />
create_hard_link <i>(function)</i> </p>
