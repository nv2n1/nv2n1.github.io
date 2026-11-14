---
title: "stdfilesystemcreate_directorystdfilesystemcreate_directories(3)"
name: "stdfilesystemcreate_directorystdfilesystemcreate_directories"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemcreate_directorystdfilesystemcreate_directories/"
description: "std::filesystem::create_directory,std::filesystem::create_directories – std::filesystem::create_directory,std::filesystem::create_directories"
---

<p>std::filesystem::create_directory,std::filesystem::create_directories &#8211; std::filesystem::create_directory,std::filesystem::create_directories</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;filesystem&gt;

    bool create_directory(const std::filesystem::path &amp;p);
(1)(since C++ 17)

    bool create_directory(const std::filesystem::path &amp;p, std::error_code &amp;ec) noexcept;

bool create_directory(const std::filesystem::path &amp;p,

                      const std::filesystem::path &amp;existing_p);

bool create_directory(const std::filesystem::path &amp;p, (2)(since C++ 17)

                                                          const std::filesystem::path &amp;existing_p,

                      std::error_code &amp;ec) noexcept;

bool create_directories(const std::filesystem::path &amp;p);
(3)(since C++ 17)

    bool create_directories(const std::filesystem::path &amp;p, std::error_code &amp;ec);</code></pre>
<p>1) Creates the directory p as if by POSIX mkdir() with a second argument of static_cast&lt;int&gt;(std::filesystem::perms::all) (the parent directory must already exist). If the function fails because p resolves to an existing directory, no error is reported. Otherwise on failure an error is reported.<br />
2) Same as <code>(1)</code>, except that the attributes of the new directory are copied from existing_p (which must be a directory that exists). It is OS-dependent which attributes are copied: on POSIX systems, the attributes are copied as if by<br />
&nbsp;<wbr>&nbsp;stat(existing_p.c_str(), &amp;attributes_stat)<br />
&nbsp;<wbr>&nbsp;mkdir(p.c_str(), attributes_stat.st_mode)<br />
On Windows OS, no attributes of existing_p are copied.<br />
3) Executes <code>(1)</code> for every element of p that does not already exist. If p already exists, the function does nothing (this condition is not treated as an error). </p>
<h2>Parameters</h2>
<p>p &#8211; the path to the new directory to create<br />
existing_p &#8211; the path to a directory to copy the attributes from<br />
ec &#8211; out-parameter for error reporting in the non-throwing overload</p>
<h2>Return value</h2>
<p>true if a directory was created for the directory p resolves to, false otherwise. </p>
<h2>Exceptions</h2>
<p>1,3) The overload that does not take a std::error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first path argument and the OS error code as the error code argument. The overload taking a std::error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. Any overload not marked noexcept may throw std::bad_alloc if memory allocation fails.<br />
2) The overload that does not take a std::error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first path argument, existing_p as the second path argument, and the OS error code as the error code argument. The overload taking a std::error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. Any overload not marked noexcept may throw std::bad_alloc if memory allocation fails.</p>
<h2>Notes</h2>
<p>The attribute-preserving overload <code>(2)</code> is implicitly invoked by copy() when recursively copying directories. Its equivalent in boost.filesystem is copy_directory (with argument order reversed)<br />
Defect reports<br />
The following behavior-changing defect reports were applied retroactively to previously published C++ standards.<br />
DR Applied to Behavior as published Correct behavior<br />
LWG_2935 C++17 error if target already exists but isn&#8217;t a directory not error<br />
LWG_3014 C++17 error_code overload of create_directories marked noexcept but can allocate memory noexcept removed<br />
P1164R1 C++17 creation failure caused by an existing non-directory file is not an error made error </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;fstream&gt;

#include &lt;cstdlib&gt;

#include &lt;filesystem&gt;

namespace fs = std::filesystem;
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
<p>create_symlink<br />
create_directory_symlink creates a symbolic link<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i><br />
<i>(C++17)</i><br />
copy copies files or directories<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i><br />
perms identifies file system permissions<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(enum)</i><br />
<i>(C++17)</i> </p>
