---
title: "stdfilesystemcopy(3)"
name: "stdfilesystemcopy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemcopy/"
description: "std::filesystem::copy – std::filesystem::copy"
---

<p>std::filesystem::copy &#8211; std::filesystem::copy</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;filesystem&gt;

    void copy(const std::filesystem::path &amp;from,

              const std::filesystem::path &amp;to);

void copy(const std::filesystem::path &amp;from, (1)(since C++ 17)

                                                 const std::filesystem::path &amp;to,

          std::error_code &amp;ec);

void copy(const std::filesystem::path &amp;from,

          const std::filesystem::path &amp;to,

          std::filesystem::copy_options options);

void copy(const std::filesystem::path &amp;from, (2)(since C++ 17)

                                                 const std::filesystem::path &amp;to,

          std::filesystem::copy_options options,

          std::error_code &amp;ec);</code></pre>
<p>Copies files and directories, with a variety of options<br />
1) The default, equivalent to <code>(2)</code> with copy_options::none used as options<br />
2) Copies the file or directory from to file or directory to, using the copy options indicated by options. The behavior is undefined if there is more than one option in any of the copy_options option group present in options (even in the copy_file group).<br />
The behavior is as follows:<br />
* First, before doing anything else, obtains type and permissions of from by no more than a single call to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* std::filesystem::symlink_status, if copy_options::skip_symlinks, copy_options::copy_symlinks, or copy_options::create_symlinks is present in options;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* std::filesystem::status otherwise.<br />
* If necessary, obtains the status of to, by no more than a single call to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* std::filesystem::symlink_status, if copy_options::skip_symlinks or copy_options::create_symlinks is present in options;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* std::filesystem::status otherwise (including the case where copy_options::copy_symlinks is present in options).<br />
* If either from or to has an implementation-defined file_type, the effects of this function are implementation-defined.<br />
* If from does not exist, reports an error.<br />
* If from and to are the same file as determined by std::filesystem::equivalent, reports an error<br />
* If either from or to is not a regular file, a directory, or a symlink, as determined by std::filesystem::is_other, reports an error<br />
* If from is a directory, but to is a regular file, reports an error<br />
* If from is a symbolic link, then<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If copy_options::skip_symlink is present in options, does nothing.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* Otherwise, if to does not exist and copy_options::copy_symlinks is present in options, then behaves as if copy_symlink(from, to)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* Otherwise, reports an error<br />
* Otherwise, if from is a regular file, then<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If copy_options::directories_only is present in options, does nothing<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* Otherwise, if copy_options::create_symlinks is present in options, creates a symlink to to. Note: from must be an absolute path unless to is in the current directory.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* Otherwise, if copy_options::create_hard_links is present in options, creates a hard link to to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* Otherwise, if to is a directory, then behaves as if copy_file(from, to/from.filename(), options) (creates a copy of from as a file in the directory to)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* Otherwise, behaves as if copy_file(from, to, options) (copies the file)<br />
* Otherwise, if from is a directory and copy_options::create_symlinks is set in options, reports an error with an error code equal to std::make_error_code(std::errc::is_a_directory).<br />
* Otherwise, if from is a directory and either options has copy_options::recursive or is copy_options::none, * If to does not exist, first executes create_directory(to, from) (creates the new directory with a copy of the old directory&#8217;s attributes)<br />
* Then, whether to already existed or was just created, iterates over the files contained in from as if by for (const std::filesystem::directory_entry&amp; x : std::filesystem::directory_iterator(from)) and for each directory entry, recursively calls copy(x.path(), to/x.path().filename(), options | in-recursive-copy), where in-recursive-copy is a special bit that has no other effect when set in options. (The sole purpose of setting this bit is to prevent recursive copying subdirectories if options is copy_options::none.)</p>
<p>* Otherwise does nothing </p>
<h2>Parameters</h2>
<p>from &#8211; path to the source file, directory, or symlink<br />
to &#8211; path to the target file, directory, or symlink<br />
ec &#8211; out-parameter for error reporting in the non-throwing overload</p>
<h2>Return value</h2>
<p><i>(none)</i> </p>
<h2>Exceptions</h2>
<p>The overload that does not take a std::error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with from as the first path argument, to as the second path argument, and the OS error code as the error code argument. The overload taking a std::error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. Any overload not marked noexcept may throw std::bad_alloc if memory allocation fails.</p>
<h2>Notes</h2>
<p>The default behavior when copying directories is the non-recursive copy: the files are copied, but not the subdirectories:<br />
&nbsp;<wbr>&nbsp;// Given<br />
&nbsp;<wbr>&nbsp;// /dir1 contains /dir1/file1, /dir1/file2, /dir1/dir2<br />
&nbsp;<wbr>&nbsp;// and /dir1/dir2 contains /dir1/dir2/file3<br />
&nbsp;<wbr>&nbsp;// After<br />
&nbsp;<wbr>&nbsp;std::filesystem::copy(&quot;/dir1&quot;, &quot;/dir3&quot;);<br />
&nbsp;<wbr>&nbsp;// /dir3 is created (with the attributes of /dir1)<br />
&nbsp;<wbr>&nbsp;// /dir1/file1 is copied to /dir3/file1<br />
&nbsp;<wbr>&nbsp;// /dir1/file2 is copied to /dir3/file2<br />
While with copy_options::recursive, the subdirectories are also copied, with their content, recursively.<br />
&nbsp;<wbr>&nbsp;// &#8230;but after<br />
&nbsp;<wbr>&nbsp;std::filesystem::copy(&quot;/dir1&quot;, &quot;/dir3&quot;, std::filesystem::copy_options::recursive);<br />
&nbsp;<wbr>&nbsp;// /dir3 is created (with the attributes of /dir1)<br />
&nbsp;<wbr>&nbsp;// /dir1/file1 is copied to /dir3/file1<br />
&nbsp;<wbr>&nbsp;// /dir1/file2 is copied to /dir3/file2<br />
&nbsp;<wbr>&nbsp;// /dir3/dir2 is created (with the attributes of /dir1/dir2)<br />
&nbsp;<wbr>&nbsp;// /dir1/dir2/file3 is copied to /dir3/dir2/file3<br />
Defect reports<br />
The following behavior-changing defect reports were applied retroactively to previously published C++ standards.<br />
DR Applied to Behavior as published Correct behavior<br />
LWG_3013 C++17 error_code overload marked noexcept but can allocate memory noexcept removed<br />
LWG_2682 C++17 attempting to create a symlink for a directory succeeds but does nothing reports an error </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;fstream&gt;

#include &lt;filesystem&gt;

namespace fs = std::filesystem;
int main()

{
    fs::create_directories(&quot;sandbox/dir/subdir&quot;);
    std::ofstream(&quot;sandbox/file1.txt&quot;).put('a');
    fs::copy(&quot;sandbox/file1.txt&quot;, &quot;sandbox/file2.txt&quot;); // copy file
    fs::copy(&quot;sandbox/dir&quot;, &quot;sandbox/dir2&quot;);            // copy directory (non-recursive)
    // sandbox holds 2 files and 2 directories, one of which has a subdirectory
    // sandbox/file1.txt
    // sandbox/file2.txt
    // sandbox/dir2
    // sandbox/dir
    //    sandbox/dir/subdir
    fs::copy(&quot;sandbox&quot;, &quot;sandbox/copy&quot;, fs::copy_options::recursive);
    // sandbox/copy holds copies of the above files and subdirectories
    fs::remove_all(&quot;sandbox&quot;);
}
</code></pre>
<h2>See also</h2>
<p>copy_options specifies semantics of copy operations<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(enum)</i><br />
<i>(C++17)</i><br />
copy_symlink copies a symbolic link<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i><br />
copy_file copies file contents<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i> </p>
