---
title: "stdexperimentalfilesystemcopy_file(3)"
name: "stdexperimentalfilesystemcopy_file"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemcopy_file/"
description: "std::experimental::filesystem::copy_file – std::experimental::filesystem::copy_file"
---

<p>std::experimental::filesystem::copy_file &#8211; std::experimental::filesystem::copy_file</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;experimental / filesystem&gt;

    bool copy_file(const path &amp;from, const path &amp;to);
(1)(filesystem TS)

    bool copy_file(const path &amp;from, const path &amp;to, error_code &amp;ec);

bool copy_file(const path &amp;from, const path &amp;to, copy_options options);
(2)(filesystem TS)

    bool copy_file(const path &amp;from, const path &amp;to, copy_options options, error_code &amp;ec);</code></pre>
<p>1) The default, equivalent to <code>(2)</code> with copy_options::none used as options<br />
2) Copies a single file from from to to, using the copy options indicated by options. The behavior is undefined if there is more than one option in any of the copy_options option group present in options (even in the groups not relevant to copy_file)<br />
* If the destination file does not exist,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* copies the contents and the attributes of the file to which from resolves to the file to which to resolves (symlinks are followed)<br />
* Otherwise, if the destination file already exists&#8230;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If to and from are the same as determined by equivalent(from,_to), report an error<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* Otherwise, if none of the copy_file control options are set in options, report an error<br />
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
<p>The overload that does not take a error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with from as the first argument, to as the second argument, and the OS error code as the error code argument. std::bad_alloc may be thrown if memory allocation fails. The overload taking a error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. This overload has<br />
noexcept specification:<br />
noexcept</p>
<h2>Notes</h2>
<p>The functions involve at most one direct or indirect call to status(to) (used both to determine if the file exists, and, for copy_options::update_existing option, its last write time)<br />
Error is reported when copy_file is used to copy a directory: use copy for that.<br />
copy_file follows symlinks: use copy_symlink or copy with copy_options::copy_symlinks for that. </p>
<h2>Examples</h2>
<p>// Run this code </p>
<pre><code>#include &lt;fstream&gt;

#include &lt;iostream&gt;

#include &lt;experimental/filesystem&gt;

namespace fs = std::experimental::filesystem;
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
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;specifies semantics of copy operations<br />
copy_options <i>(enum)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies a symbolic link<br />
copy_symlink <i>(function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies files or directories<br />
copy <i>(function)</i> </p>
