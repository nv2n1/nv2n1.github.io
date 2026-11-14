---
title: "stdexperimentalfilesystemcreate_directory(3)"
name: "stdexperimentalfilesystemcreate_directory"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemcreate_directory/"
description: "std::experimental::filesystem::create_directory,std::experimental::filesystem::create_directories – std::experimental::filesystem::create_directory,std::experimental::filesystem::create_directories"
---

<p>std::experimental::filesystem::create_directory,std::experimental::filesystem::create_directories &#8211; std::experimental::filesystem::create_directory,std::experimental::filesystem::create_directories</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;experimental / filesystem&gt;

    bool create_directory(const path &amp;p);
(1)(filesystem TS)

    bool create_directory(const path &amp;p, error_code &amp;ec);

bool create_directory(const path &amp;p, const path &amp;existing_p);
(2)(filesystem TS)

    bool create_directory(const path &amp;p, const path &amp;existing_p, error_code &amp;ec);

bool create_directories(const path &amp;p);
(3)(filesystem TS)

    bool create_directories(const path &amp;p, error_code &amp;ec);</code></pre>
<p>1) Creates the directory p as if by POSIX mkdir() with a second argument of static_cast&lt;int&gt;(fs::perms::all) (the parent directory must already exist). If p already exists and is already a directory, the function does nothing (this condition is not treated as an error).<br />
2) Same as <code>(1)</code>, except that the attributes of the new directory are copied from existing_p (which must be a directory that exists). It is OS-dependent which attributes are copied: on POSIX systems, the attributes are copied as if by<br />
&nbsp;<wbr>&nbsp;stat(existing_p.c_str(), &amp;attributes_stat)<br />
&nbsp;<wbr>&nbsp;mkdir(p.c_str(), attributes_stat.st_mode)<br />
On Windows OS, the attributes are copied as if by<br />
&nbsp;<wbr>&nbsp;CreateDirectoryExW(existing_p.c_str(), p.c_str(), 0)<br />
3) Executes <code>(1)</code> for every element of p that does not already exist.<br />
The non-throwing overloads return false if any error occurs. </p>
<h2>Parameters</h2>
<p>p &#8211; the path to the new directory to create<br />
existing_p &#8211; the path to a directory to copy the attributes from<br />
ec &#8211; out-parameter for error reporting in the non-throwing overload</p>
<h2>Return value</h2>
<p>1,2) true if directory creation is successful, false otherwise. </p>
<h2>Exceptions</h2>
<p>1,3) The overload that does not take a error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first argument and the OS error code as the error code argument. std::bad_alloc may be thrown if memory allocation fails. The overload taking a error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. This overload has<br />
noexcept specification:<br />
noexcept<br />
2) The overload that does not take a error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first argument, existing_p as the second argument, and the OS error code as the error code argument. std::bad_alloc may be thrown if memory allocation fails. The overload taking a error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. This overload has<br />
noexcept specification:<br />
noexcept</p>
<h2>Notes</h2>
<p>The attribute-preserving overload <code>(2)</code> is implicitly invoked by copy() when recursively copying directories. Its equivalent in boost.filesystem is copy_directory (with argument order reversed) </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;fstream&gt;

#include &lt;cstdlib&gt;

#include &lt;experimental/filesystem&gt;

namespace fs = std::experimental::filesystem;
int main()

{
    fs::create_directories(&quot;sandbox/1/2/a&quot;);
    fs::create_directory(&quot;sandbox/1/2/b&quot;);
    fs::permissions(&quot;sandbox/1/2/b&quot;, fs::perms::remove_perms | fs::perms::others_all);
    fs::create_directory(&quot;sandbox/1/2/c&quot;, &quot;sandbox/1/2/b&quot;);
    std::system(&quot;ls -l sandbox/1/2&quot;);
    fs::remove_all(&quot;sandbox&quot;);
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;drwxr-xr-x 2 user group 4096 Apr 15 09:33 a<br />
&nbsp;<wbr>&nbsp;drwxr-x&#8212; 2 user group 4096 Apr 15 09:33 b<br />
&nbsp;<wbr>&nbsp;drwxr-x&#8212; 2 user group 4096 Apr 15 09:33 c</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a symbolic link<br />
create_symlink <i>(function)</i><br />
create_directory_symlink<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies files or directories<br />
copy <i>(function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;identifies file system permissions<br />
perms <i>(enum)</i> </p>
