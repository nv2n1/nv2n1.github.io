---
title: "stdexperimentalfilesystemcurrent_path(3)"
name: "stdexperimentalfilesystemcurrent_path"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemcurrent_path/"
description: "std::experimental::filesystem::current_path – std::experimental::filesystem::current_path"
---

<p>std::experimental::filesystem::current_path &#8211; std::experimental::filesystem::current_path</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;experimental/filesystem&gt;<br />
path current_path(); <code>(1)</code> (filesystem TS)<br />
path current_path( error_code&amp; ec ); <code>(2)</code> (filesystem TS)<br />
void current_path( const path&amp; p ); <code>(3)</code> (filesystem TS)<br />
void current_path( const path&amp; p, error_code&amp; ec ); <code>(4)</code> (filesystem TS)<br />
Returns or changes the current path.<br />
1-2) Returns the absolute path of the current working directory, obtained as if by POSIX getcwd. <code>(2)</code> returns path() if error occurs.<br />
3-4) Changes the current working directory to p, as if by POSIX chdir. </p>
<h2>Parameters</h2>
<p>p &#8211; path to change the current working directory to<br />
ec &#8211; out-parameter for error reporting in the non-throwing overloads</p>
<h2>Return value</h2>
<p>1-2) Returns the current working directory.<br />
3-4) <i>(none)</i> </p>
<h2>Exceptions</h2>
<p>1-2) The overload that does not take a error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with the OS error code as the error code argument. std::bad_alloc may be thrown if memory allocation fails. The overload taking a error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. This overload has<br />
noexcept specification:<br />
noexcept<br />
3-4) The overload that does not take a error_code&amp; parameter throws filesystem_error on underlying OS API errors, constructed with p as the first argument and the OS error code as the error code argument. std::bad_alloc may be thrown if memory allocation fails. The overload taking a error_code&amp; parameter sets it to the OS API error code if an OS API call fails, and executes ec.clear() if no errors occur. This overload has<br />
noexcept specification:<br />
noexcept</p>
<h2>Notes</h2>
<p>The current working directory is the directory that is used as the starting location in path resolution for relative paths. Single current working directory is associated with entire process.<br />
The current working directory is a dangerous global state of the program. Behavior of various file input/output related functions are affected by the value of the current path. The current path may be unexpectedly changed by any component of the program, including various external libraries or other threads. </p>
<h2>See also</h2>
<p>&nbsp;This section is incomplete </p>
