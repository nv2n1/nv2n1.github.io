---
title: "stdfilesystemcurrent_path(3)"
name: "stdfilesystemcurrent_path"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemcurrent_path/"
description: "std::filesystem::current_path – std::filesystem::current_path"
---

<p>std::filesystem::current_path &#8211; std::filesystem::current_path</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;filesystem&gt;

    path current_path();
(1)(since C++ 17)

    path current_path(std::error_code &amp;ec);
(2)(since C++ 17)

    void current_path(const std::filesystem::path &amp;p);
(3)(since C++ 17)

    void current_path(const std::filesystem::path &amp;p, (4)(since C++ 17)

                                                          std::error_code &amp;ec) noexcept;</code></pre>
<p>Returns or changes the current path.<br />
1-2) Returns the absolute path of the current working directory, obtained as if (in native format) by POSIX getcwd. <code>(2)</code> returns path() if error occurs.<br />
3-4) Changes the current working directory to p, as if by POSIX chdir. </p>
<h2>Parameters</h2>
<p>p &#8211; path to change the current working directory to<br />
ec &#8211; out-parameter for error reporting in the non-throwing overloads</p>
<h2>Return value</h2>
<p>1-2) Returns the current working directory.<br />
3-4) <i>(none)</i> </p>
<h2>Exceptions</h2>
<p>1-2) The overload that does not take a std::error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with the OS error code as the error code argument. The overload taking a std::error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. Any overload not marked noexcept may throw std::bad_alloc if memory allocation fails.<br />
3-4) The overload that does not take a std::error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first path argument and the OS error code as the error code argument. The overload taking a std::error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. Any overload not marked noexcept may throw std::bad_alloc if memory allocation fails.</p>
<h2>Notes</h2>
<p>The current working directory is the directory, associated with the process, that is used as the starting location in pathname resolution for relative paths.<br />
The current path as returned by many operating systems is a dangerous global variable. It may be changed unexpectedly by third-party or system library functions, or by another thread. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;filesystem&gt;

namespace fs = std::filesystem;

int main()

{
    std::cout &lt;&lt; &quot;Current path is &quot; &lt;&lt; fs::current_path() &lt;&lt; '
';
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;Current path is &quot;D:/local/ConsoleApplication1&quot;</p>
