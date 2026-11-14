---
title: "tcl_splitpath(3)"
name: "tcl_splitpath"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_splitpath/"
description: "Tcl_SplitPath, Tcl_JoinPath, Tcl_GetPathType – manipulate platform-dependent file paths"
---

<p>Tcl_SplitPath, Tcl_JoinPath, Tcl_GetPathType &#8211; manipulate platform-dependent file paths </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
<code>Tcl_SplitPath</code>(<i>path, argcPtr, argvPtr</i>)
char *
<code>Tcl_JoinPath</code>(<i>argc, argv, resultPtr</i>)
Tcl_PathType
<code>Tcl_GetPathType</code>(<i>path</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>const char <i>*path</i> (in) File path in a form appropriate for the current platform (see the <code>filename</code> manual entry for acceptable forms for path names).</p>
<dd>int <i>*argcPtr</i> (out) Filled in with number of path elements in <i>path</i>.</p>
<dd>const char <i>***argvPtr</i> (out) <i>*argvPtr</i> will be filled in with the address of an array of pointers to the strings that are the extracted elements of <i>path</i>. There will be <i>*argcPtr</i> valid entries in the array, followed by a NULL entry.</p>
<dd>int <i>argc</i> (in) Number of elements in <i>argv</i>.</p>
<dd>const char *const <i>*argv</i> (in) Array of path elements to merge together into a single path.</p>
<dd>Tcl_DString <i>*resultPtr</i> (in/out) A pointer to an initialized <code>Tcl_DString</code> to which the result of <code>Tcl_JoinPath</code> will be appended. </p>
</dl>
<h2>Description</h2>
<p>These procedures have been superceded by the objectified procedures in the <code>FileSystem</code> man page, which are more efficient. </p>
<p> These procedures may be used to disassemble and reassemble file paths in a platform independent manner: they provide C-level access to the same functionality as the <code>file split</code>, <code>file join</code>, and <code>file pathtype</code> commands. </p>
<p> <code>Tcl_SplitPath</code> breaks a path into its constituent elements, returning an array of pointers to the elements using <i>argcPtr</i> and <i>argvPtr</i>. The area of memory pointed to by <i>*argvPtr</i> is dynamically allocated; in addition to the array of pointers, it also holds copies of all the path elements. It is the caller&#8217;s responsibility to free all of this storage. For example, suppose that you have called <code>Tcl_SplitPath</code> with the following code:</p>
<dl COMPACT>
<dd>
<pre>int argc;
char *path;
char **argv;
...
Tcl_SplitPath(string, &amp;argc, &amp;argv);</pre>
</dl>
<p> Then you should eventually free the storage with a call like the following:</p>
<dl COMPACT>
<dd>
<pre>Tcl_Free((char *) argv);</pre>
</dl>
<p> <code>Tcl_JoinPath</code> is the inverse of <code>Tcl_SplitPath</code>: it takes a collection of path elements given by <i>argc</i> and <i>argv</i> and generates a result string that is a properly constructed path. The result string is appended to <i>resultPtr</i>. <i>ResultPtr</i> must refer to an initialized <code>Tcl_DString</code>. </p>
<p> If the result of <code>Tcl_SplitPath</code> is passed to <code>Tcl_JoinPath</code>, the result will refer to the same location, but may not be in the same form. This is because <code>Tcl_SplitPath</code> and <code>Tcl_JoinPath</code> eliminate duplicate path separators and return a normalized form for each platform. </p>
<p> <code>Tcl_GetPathType</code> returns the type of the specified <i>path</i>, where <code>Tcl_PathType</code> is one of <code>TCL_PATH_ABSOLUTE</code>, <code>TCL_PATH_RELATIVE</code>, or <code>TCL_PATH_VOLUME_RELATIVE</code>. See the <code>filename</code> manual entry for a description of the path types for each platform. </p>
<h2>Keywords</h2>
<p>file, filename, join, path, split, type</p>
