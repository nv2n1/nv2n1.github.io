---
title: "stdexperimentalfilesystemtemp_directory_path(3)"
name: "stdexperimentalfilesystemtemp_directory_path"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemtemp_directory_path/"
---

std::experimental::filesystem::temp_directory_path - std::experimental::filesystem::temp_directory_path

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/filesystem&gt;

path temp_directory_path();                 (1) (filesystem TS)

path temp_directory_path( error_code&amp; ec );</code></pre> 
Returns the directory location suitable for temporary files. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

A directory suitable for temporary files. The path is guaranteed to exist and to be a directory. The overload that takes error_code&amp; argument returns an empty path on error. 

<h2>Exceptions</h2>

The overload that does not take a error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with path to be returned as the first argument and the OS error code as the error code argument. std::bad_alloc may be thrown if memory allocation fails. The overload taking a error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. This overload has 
noexcept specification: 
noexcept

<h2>Notes</h2>

On POSIX systems, the path may be the one specified in the environment variables TMPDIR, TMP, TEMP, TEMPDIR, and, if none of them are specified, the path &quot;/tmp&quot; is returned. 
On Windows systems, the path is typically the one returned by GetTempPath 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;experimental/filesystem&gt;

namespace fs = std::experimental::filesystem;

int main()

{
    std::cout &lt;&lt; &quot;Temp directory is &quot; &lt;&lt; fs::temp_directory_path() &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Temp directory is &quot;C:\Windows\TEMP\&quot;

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates and opens a temporary, auto-removing file 
tmpfile <i>(function)</i> 
