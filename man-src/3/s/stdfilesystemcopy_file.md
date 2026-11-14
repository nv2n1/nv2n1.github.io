---
title: "stdfilesystemcopy_file(3)"
name: "stdfilesystemcopy_file"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemcopy_file/"
description: "std::filesystem::copy_file – std::filesystem::copy_file"
---

<p>std::filesystem::copy_file &#8211; std::filesystem::copy_file</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;filesystem&gt;

    bool copy_file(const std::filesystem::path &amp;from,

                   const std::filesystem::path &amp;to);

bool copy_file(const std::filesystem::path &amp;from, (1)(since C++ 17)

                                                      const std::filesystem::path &amp;to,

               std::error_code &amp;ec);

bool copy_file(const std::filesystem::path &amp;from,

               const std::filesystem::path &amp;to,

               std::filesystem::copy_options options);

bool copy_file(const std::filesystem::path &amp;from, (2)(since C++ 17)

                                                      const std::filesystem::path &amp;to,

               std::filesystem::copy_options options,

               std::error_code &amp;ec);</code></pre>
<p>1) The default, equivalent to <code>(2)</code> with copy_options::none used as options<br />
2) Copies a single file from from to to, using the copy options indicated by options. The behavior is undefined if there is more than one option in any of the copy_options option group present in options (even in the groups not relevant to copy_file)<br />
* If !is_regular_file(from) (either because the source file doesn&#8217;t exist or because it is not a regular file), report an error<br />
* Otherwise, if the destination file does not exist,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* copies the contents and the attributes of the file to which from resolves to the file to which to resolves (symlinks are followed)<br />
* Otherwise, if the destination file already exists&#8230;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* Report an error if any of the following is true:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* to and from are the same as determined by equivalent(from,_to);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* to is not a regular file as determined by !is_regular_file(to)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* none of the copy_file control options are set in options<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* Otherwise, if copy_options::skip_existing is set in options, do nothing<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* Otherwise, if copy_options::overwrite_existing is set in options, copy the contents and the attributes of the file to which from resolves to the file to which to resolves<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* Otherwise, if copy_options::update_existing is set in options, only copy the file if from is newer than to, as defined by last_write_time()<br />
The non-throwing overloads return false if an error occurs. </p>
<h2>Parameters</h2>
<p>from &#8211; path to the source file<br />
to &#8211; path to the target file<br />
ec &#8211; out-parameter for error reporting in the non-throwing overload</p>
<h2>Return value</h2>
<p>true if the file was copied, false otherwise. </p>
<h2>Exceptions</h2>
<p>The overload that does not take a std::error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with from as the first path argument, to as the second path argument, and the OS error code as the error code argument. The overload taking a std::error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. Any overload not marked noexcept may throw std::bad_alloc if memory allocation fails.</p>
<h2>Notes</h2>
<p>The functions involve at most one direct or indirect call to status(to) (used both to determine if the file exists, and, for copy_options::update_existing option, its last write time)<br />
Error is reported when copy_file is used to copy a directory: use copy for that.<br />
copy_file follows symlinks: use copy_symlink or copy with copy_options::copy_symlinks for that.<br />
Defect reports<br />
The following behavior-changing defect reports were applied retroactively to previously published C++ standards.<br />
DR Applied to Behavior as published Correct behavior<br />
LWG_3014 C++17 error_code overload marked noexcept but can allocate memory noexcept removed </p>
<h2>Examples</h2>
<p>// Run this code </p>
<pre><code>#include &lt;fstream&gt;

#include &lt;iostream&gt;

#include &lt;filesystem&gt;

namespace fs = std::filesystem;
int main()

{
    fs::create_directory(&quot;sandbox&quot;);
    std::ofstream(&quot;sandbox/file1.txt&quot;).put('a');
    fs::copy_file(&quot;sandbox/file1.txt&quot;, &quot;sandbox/file2.txt&quot;);
    // now there are two files in sandbox:
    std::cout &lt;&lt; &quot;file1.txt holds : &quot;
              &lt;&lt; std::ifstream(&quot;sandbox/file1.txt&quot;).rdbuf() &lt;&lt; '
';
    std::cout &lt;&lt; &quot;file2.txt holds : &quot;
              &lt;&lt; std::ifstream(&quot;sandbox/file2.txt&quot;).rdbuf() &lt;&lt; '
';
    // fail to copy directory
    fs::create_directory(&quot;sandbox/abc&quot;);
    try {
        fs::copy_file(&quot;sandbox/abc&quot;, &quot;sandbox/def&quot;);
    } catch (fs::filesystem_error &amp;e) {
        std::cout &lt;&lt; &quot;Could not copy sandbox/abc: &quot; &lt;&lt; e.what() &lt;&lt; '
';
    }
    fs::remove_all(&quot;sandbox&quot;);
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;file1.txt holds : a<br />
&nbsp;<wbr>&nbsp;file2.txt holds : a<br />
&nbsp;<wbr>&nbsp;Could not copy sandbox/abc: copy_file: Is a directory: &quot;sandbox/abc&quot;, &quot;sandbox/def&quot;</p>
<h2>See also</h2>
<p>copy_options specifies semantics of copy operations<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(enum)</i><br />
<i>(C++17)</i><br />
copy_symlink copies a symbolic link<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i><br />
copy copies files or directories<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++17)</i> </p>
