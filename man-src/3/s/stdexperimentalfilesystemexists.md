---
title: "stdexperimentalfilesystemexists(3)"
name: "stdexperimentalfilesystemexists"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemexists/"
description: "std::experimental::filesystem::exists – std::experimental::filesystem::exists"
---

<p>std::experimental::filesystem::exists &#8211; std::experimental::filesystem::exists</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;experimental/filesystem&gt;<br />
bool exists( file_status s ) <code>(1)</code> (filesystem TS)<br />
bool exists( const path&amp; p ); <code>(2)</code> (filesystem TS)<br />
bool exists( const path&amp; p, error_code&amp; ec )<br />
Checks if the given file status or path corresponds to an existing file or directory.<br />
1) Equivalent to status_known(s) &amp;&amp; s.type() != file_type::not_found.<br />
2) Equivalent to exists(status(p)) or exists(status(p, ec)) (symlinks are followed). The non-throwing overload returns false if an error occurs. </p>
<h2>Parameters</h2>
<p>s &#8211; file status to check<br />
p &#8211; path to examine<br />
ec &#8211; out-parameter for error reporting in the non-throwing overload</p>
<h2>Return value</h2>
<p>true if the given path or file status corresponds to an existing file or directory, false otherwise. </p>
<h2>Exceptions</h2>
<p>1)<br />
noexcept specification:<br />
noexcept<br />
2) The overload that does not take a error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first argument and the OS error code as the error code argument. std::bad_alloc may be thrown if memory allocation fails. The overload taking a error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. This overload has<br />
noexcept specification:<br />
noexcept</p>
<h2>Notes</h2>
<p>The information provided by this function is usually also provided as a byproduct of directory iteration. During directory iteration, calling exists(*iterator) is less efficient than exists(iterator-&gt;status()) </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;fstream&gt;

#include &lt;cstdint&gt;

#include &lt;experimental/filesystem&gt;

namespace fs = std::experimental::filesystem;
void demo_exists(const fs::path &amp;p, fs::file_status s = fs::file_status{})

{
    std::cout &lt;&lt; p;
    if (fs::status_known(s) ? fs::exists(s) : fs::exists(p))
        std::cout &lt;&lt; &quot; exists
&quot;;
    else
        std::cout &lt;&lt; &quot; does not exist
&quot;;
}

int main()

{
    fs::create_directory(&quot;sandbox&quot;);
    std::ofstream(&quot;sandbox/file&quot;); // create regular file
    fs::create_symlink(&quot;non-existing&quot;, &quot;sandbox/symlink&quot;);
    demo_exists(&quot;sandbox&quot;);
    for (auto it = fs::directory_iterator(&quot;sandbox&quot;); it != fs::directory_iterator(); ++it)
        demo_exists(*it, it-&gt;status()); // use cached status from directory entry
    fs::remove_all(&quot;sandbox&quot;);
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;&quot;sandbox&quot; exists<br />
&nbsp;<wbr>&nbsp;&quot;sandbox/file&quot; exists<br />
&nbsp;<wbr>&nbsp;&quot;sandbox/symlink&quot; does not exist</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;determines file attributes<br />
status determines file attributes, checking the symlink target<br />
symlink_status <i>(function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;represents file type and permissions<br />
file_status <i>(class)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cached status of the file designated by this directory entry<br />
status cached symlink_status of the file designated by this directory entry<br />
symlink_status <i>(public member function of std::experimental::filesystem::directory_entry)</i> </p>
