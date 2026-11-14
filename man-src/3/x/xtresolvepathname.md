---
title: "xtresolvepathname(3)"
name: "xtresolvepathname"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtresolvepathname/"
description: "XtResolvePathname – search for a file using standard substitution"
---

<p>XtResolvePathname &#8211; search for a file using standard substitution </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>char * XtResolvePathname(Display *<i>display</i>, const char *<i>type</i>, const char *<i>filename</i>, const char *<i>suffix</i>, const char *<i>path</i>, Substitution <i>substitutions</i>, Cardinal <i>num_substitutions</i>, XtFilePredicate <i>predicate</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the display to use to find the language for language substitutions.</p>
<dt><i>type</i></p>
<dd>
<dt><i>filename</i></p>
<dd>
<dt><i>suffix</i></p>
<dd>Specify values to substitute into the path.</p>
<dt><i>path</i></p>
<dd>Specifies the list of file specifications, or NULL.</p>
<dt><i>substitutions</i></p>
<dd>Specifies a list of additional substitutions to make into the path, or NULL.</p>
<dt><i>num_substitutions</i></p>
<dd>Specifies the number of entries in <i>substitutions</i>.</p>
<dt><i>predicate</i></p>
<dd>Specifies a procedure called to judge each potential file name, or NULL.</dl>
<h2>Description</h2>
<p>The substitutions specified by <code>XtResolvePathname</code> are determined from the value of the language string retrieved by <code>XtDisplayInitialize</code> for the specified display. To set the language for all applications specify &#8220;*xnlLanguage: <i>lang</i>&#8221; in the resource database. The format and content of the language string are implementation-defined. One suggested syntax is to compose the language string of three parts: a &#8220;language part&#8221;, a &#8220;territory part&#8221; and a &#8220;codeset part&#8221;. The manner in which this composition is accomplished is implementation-defined and the Intrinsics make no interpretation of the parts other than to use them in substitutions as described below. </p>
<p> <code>XtResolvePathname</code> calls <code>XtFindFile</code> with the following substitutions in addition to any passed by the caller and returns the value returned by <code>XtFindFile</code>:</p>
<dl COMPACT>
<dt>%N</p>
<dd>The value of the <i>filename</i> parameter, or the application&#8217;s class name if <i>filename</i> is NULL.</p>
<dt>%T</p>
<dd>The value of the <i>type</i> parameter.</p>
<dt>%S</p>
<dd>The value of the <i>suffix</i> parameter.</p>
<dt>%L</p>
<dd>The language string associated with the specified display.</p>
<dt>%l</p>
<dd>The language part of the display&#8217;s language string.</p>
<dt>%t</p>
<dd>The territory part of the display&#8217;s language string.</p>
<dt>%c</p>
<dd>The codeset part of the display&#8217;s language string.</p>
<dt>%C</p>
<dd>The customization string retrieved from the resource database associated with <i>display</i>.</p>
<dt>%D</p>
<dd>The value of the implementation-specific default path.</dl>
<p> If a path is passed to <code>XtResolvePathname</code>, it will be passed along to <code>XtFindFile</code>. If the <i>path</i> argument is NULL, the value of the <font SIZE="-1"><code>XFILESEARCHPATH</code></font> environment variable will be passed to <code>XtFindFile</code>. If <font SIZE="-1"><code>XFILESEARCHPATH</code></font> is not defined, an implementation-specific default path will be used which contains at least 6 entries. These entries must contain the following substitutions: </p>
<pre>1. %C, %N, %S, %T, %L or %C, %N, %S, %T, %l, %t, %c
2. %C, %N, %S, %T, %l
3. %C, %N, %S, %T
4. %N, %S, %T, %L or %N, %S, %T, %l, %t, %c
5. %N, %S, %T, %l
6. %N, %S, %T</pre>
<p>The order of these six entries within the path must be as given above. The order and use of substitutions within a given entry is implementation dependent. If the path begins with a colon, it will be preceded by %N%S. If the path includes two adjacent colons, <code>%N%S</code> will be inserted between them. </p>
<p> The <i>type</i> parameter is intended to be a category of files, usually being translated into a directory in the pathname. Possible values might include &#8220;app-defaults&#8221;, &#8220;help&#8221;, and &#8220;bitmap&#8221;. </p>
<p> The <i>suffix</i> parameter is intended to be appended to the file name. Possible values might include &#8220;.txt&#8221;, &#8220;.dat&#8221;, and &#8220;.bm&#8221;. </p>
<p> A suggested value for the default path on POSIX-based systems is</p>
<dl COMPACT>
<dd>/usr/lib/X11/%L/%T/%N%C%S:/usr/lib/X11/%l/%T/%N%C%S:\<br />
 /usr/lib/X11/%T/%N%C%S:/usr/lib/X11/%L/%T/%N%S:\<br />
 /usr/lib/X11/%l/%T/%N%S:/usr/lib/X11/%T/%N%S</dl>
<p> Using this example, if the user has specified a language, it will be used as a subdirectory of /usr/lib/X11 that will be searched for other files. If the desired file is not found there, the lookup will be tried again using just the language part of the specification. If the file is not there, it will be looked for in /usr/lib/X11. The <i>type</i> parameter is used as a subdirectory of the language directory or of /usr/lib/X11, and <i>suffix</i> is appended to the file name. </p>
<p> The %D substitution allows the addition of path elements to the implementation-specific default path, typically to allow additional directories to be searched without preventing resources in the system directories from being found. For example, a user installing resource files under a directory called &#8220;ourdir&#8221; might set <font SIZE="-1"><code>XFILESEARCHPATH</code></font> to</p>
<dl COMPACT>
<dd>%D:ourdir/%T/%N%C:ourdir/%T/%N</dl>
<p> The customization string is obtained by querying the resource database currently associated with the display (the database returned by <code>XrmGetDatabase</code>) for the resource <i>application_name</i>.customization, class <i>application_class</i>.Customization where <i>application_name</i> and <i>application_class</i> are the values returned by <code>XtGetApplicationNameAndClass</code>. If no value is specified in the database, the empty string is used. </p>
<p> It is the responsibility of the caller to free the returned string using <code>XtFree</code> when it is no longer needed.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
