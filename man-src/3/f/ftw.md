---
title: "ftw(3)"
name: "ftw"
section: "3"
letter: "f"
url: "/docs/linux/man/3-ftw/"
description: "ftw, nftw – file tree walk"
---

<h2 class="name">NAME</h2>
<p> ftw, nftw &#8211; file tree walk </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ftw.h&gt;
int nftw(const char *dirpath,
         int (*fn)(const char *fpath, const struct stat *sb,
                   int typeflag, struct FTW *ftwbuf),
         int nopenfd, int flags);
#include &lt;ftw.h&gt;
int ftw(const char *dirpath,
        int (*fn)(const char *fpath, const struct stat *sb,
                  int typeflag),
        int nopenfd);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>nftw</code>(): _XOPEN_SOURCE &gt;= 500</p>
<h2>DESCRIPTION</h2>
<p> <code>nftw</code>() walks through the directory tree that is located under the directory <i>dirpath</i>, and calls <i>fn</i>() once for each entry in the tree. By default, directories are handled before the files and subdirectories they contain (preorder traversal). </p>
<p> To avoid using up all of the calling process&#8217;s file descriptors, <i>nopenfd</i> specifies the maximum number of directories that <code>nftw</code>() will hold open simultaneously. When the search depth exceeds this, <code>nftw</code>() will become slower because directories have to be closed and reopened. <code>nftw</code>() uses at most one file descriptor for each level in the directory tree. </p>
<p> For each entry found in the tree, <code>nftw</code>() calls <i>fn</i>() with four arguments: <i>fpath</i>, <i>sb</i>, <i>typeflag</i>, and <i>ftwbuf</i>. <i>fpath</i> is the pathname of the entry, and is expressed either as a pathname relative to the calling process&#8217;s current working directory at the time of the call to <code>nftw</code>(), if <i>dirpath</i> was expressed as a relative pathname, or as an absolute pathname, if <i>dirpath</i> was expressed as an absolute pathname. <i>sb</i> is a pointer to the <i>stat</i> structure returned by a call to <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) for <i>fpath</i>. </p>
<p> The <i>typeflag</i> argument passed to <i>fn</i>() is an integer that has one of the following values:</p>
<dl>
<dt><code>FTW_F</code></p>
<dd> <i>fpath</i> is a regular file.</p>
<dt><code>FTW_D</code></p>
<dd> <i>fpath</i> is a directory.</p>
<dt><code>FTW_DNR</code></p>
<dd> <i>fpath</i> is a directory which can&#8217;t be read.</p>
<dt><code>FTW_DP</code></p>
<dd> <i>fpath</i> is a directory, and <code>FTW_DEPTH</code> was specified in <i>flags</i>. (If <code>FTW_DEPTH</code> was not specified in <i>flags</i>, then directories will always be visited with <i>typeflag</i> set to <code>FTW_D</code>.) All of the files and subdirectories within <i>fpath</i> have been processed.</p>
<dt><code>FTW_NS</code></p>
<dd> The <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) call failed on <i>fpath</i>, which is not a symbolic link. The probable cause for this is that the caller had read permission on the parent directory, so that the filename <i>fpath</i> could be seen, but did not have execute permission, so that the file could not be reached for <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2). The contents of the buffer pointed to by <i>sb</i> are undefined.</p>
<dt><code>FTW_SL</code></p>
<dd> <i>fpath</i> is a symbolic link, and <code>FTW_PHYS</code> was set in <i>flags</i>.</p>
<dt><code>FTW_SLN</code></p>
<dd> <i>fpath</i> is a symbolic link pointing to a nonexistent file. (This occurs only if <code>FTW_PHYS</code> is not set.) In this case the <i>sb</i> argument passed to <i>fn</i>() contains information returned by performing <code><a href="/docs/linux/man/2-lstat/">lstat</a></code>(2) on the &quot;dangling&quot; symbolic link. (But see BUGS.)</dl>
<p> The fourth argument (<i>ftwbuf</i>) that <code>nftw</code>() supplies when calling <i>fn</i>() is a pointer to a structure of type <i>FTW</i>: </p>
<p> struct FTW {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int base;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int level; }; </p>
<p> <i>base</i> is the offset of the filename (i.e., basename component) in the pathname given in <i>fpath</i>. <i>level</i> is the depth of <i>fpath</i> in the directory tree, relative to the root of the tree (<i>dirpath</i>, which has depth 0). </p>
<p> To stop the tree walk, <i>fn</i>() returns a nonzero value; this value will become the return value of <code>nftw</code>(). As long as <i>fn</i>() returns 0, <code>nftw</code>() will continue either until it has traversed the entire tree, in which case it will return zero, or until it encounters an error (such as a <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) failure), in which case it will return -1. </p>
<p> Because <code>nftw</code>() uses dynamic data structures, the only safe way to exit out of a tree walk is to return a nonzero value from <i>fn</i>(). To allow a signal to terminate the walk without causing a memory leak, have the handler set a global flag that is checked by <i>fn</i>(). <i>Don&#8217;t</i> use <code><a href="/docs/linux/man/3-longjmp/">longjmp</a></code>(3) unless the program is going to terminate. </p>
<p> The <i>flags</i> argument of <code>nftw</code>() is formed by ORing zero or more of the following flags:</p>
<dl>
<dt><code>FTW_ACTIONRETVAL</code> (since glibc 2.3.3)</p>
<dd> If this glibc-specific flag is set, then <code>nftw</code>() handles the return value from <i>fn</i>() differently. <i>fn</i>() should return one of the following values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>FTW_CONTINUE</code></p>
<dd> Instructs <code>nftw</code>() to continue normally.</p>
<dt><code>FTW_SKIP_SIBLINGS</code></p>
<dd> If <i>fn</i>() returns this value, then siblings of the current entry will be skipped, and processing continues in the parent.</p>
<dt><code>FTW_SKIP_SUBTREE</code></p>
<dd> If <i>fn</i>() is called with an entry that is a directory (<i>typeflag</i> is <code>FTW_D</code>), this return value will prevent objects within that directory from being passed as arguments to <i>fn</i>(). <code>nftw</code>() continues processing with the next sibling of the directory.</p>
<dt><code>FTW_STOP</code></p>
<dd> Causes <code>nftw</code>() to return immediately with the return value <code>FTW_STOP</code>.</dl>
<p> Other return values could be associated with new actions in the future; <i>fn</i>() should not return values other than those listed above. </p>
<p> The feature test macro <code>_GNU_SOURCE</code> must be defined (before including <i>any</i> header files) in order to obtain the definition of <code>FTW_ACTIONRETVAL</code> from <i>&lt;ftw.h&gt;</i>.</dl>
<dt><code>FTW_CHDIR</code></p>
<dd> If set, do a <code><a href="/docs/linux/man/2-chdir/">chdir</a></code>(2) to each directory before handling its contents. This is useful if the program needs to perform some action in the directory in which <i>fpath</i> resides. (Specifying this flag has no effect on the pathname that is passed in the <i>fpath</i> argument of <i>fn</i>.)</p>
<dt><code>FTW_DEPTH</code></p>
<dd> If set, do a post-order traversal, that is, call <i>fn</i>() for the directory itself <i>after</i> handling the contents of the directory and its subdirectories. (By default, each directory is handled <i>before</i> its contents.)</p>
<dt><code>FTW_MOUNT</code></p>
<dd> If set, stay within the same filesystem (i.e., do not cross mount points).</p>
<dt><code>FTW_PHYS</code></p>
<dd> If set, do not follow symbolic links. (This is what you want.) If not set, symbolic links are followed, but no file is reported twice.</p>
<dt>
<dd> If <code>FTW_PHYS</code> is not set, but <code>FTW_DEPTH</code> is set, then the function <i>fn</i>() is never called for a directory that would be a descendant of itself.</dl>
<h3>ftw()</h3>
<p> <code>ftw</code>() is an older function that offers a subset of the functionality of <code>nftw</code>(). The notable differences are as follows:</p>
<dl>
<dt>*</p>
<dd> <code>ftw</code>() has no <i>flags</i> argument. It behaves the same as when <code>nftw</code>() is called with <i>flags</i> specified as zero.</p>
<dt>*</p>
<dd> The callback function, <i>fn</i>(), is not supplied with a fourth argument.</p>
<dt>*</p>
<dd> The range of values that is passed via the <i>typeflag</i> argument supplied to <i>fn</i>() is smaller: just <code>FTW_F</code>, <code>FTW_D</code>, <code>FTW_DNR</code>, <code>FTW_NS</code>, and (possibly) <code>FTW_SL</code>.</dl>
<h2>RETURN VALUE</h2>
<p> These functions return 0 on success, and -1 if an error occurs. </p>
<p> If <i>fn</i>() returns nonzero, then the tree walk is terminated and the value returned by <i>fn</i>() is returned as the result of <code>ftw</code>() or <code>nftw</code>(). </p>
<p> If <code>nftw</code>() is called with the <code>FTW_ACTIONRETVAL</code> flag, then the only nonzero value that should be used by <i>fn</i>() to terminate the tree walk is <code>FTW_STOP</code>, and that value is returned as the result of <code>nftw</code>().</p>
<h2>VERSIONS</h2>
<p> <code>nftw</code>() is available under glibc since version 2.1.</p>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>nftw</code>() </td>
<td>Thread safety</td>
<td>MT-Safe cwd
</td>
</tr>
<tr VALIGN=top>
<td> <code>ftw</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4, SUSv1. POSIX.1-2008 marks <code>ftw</code>() as obsolete.</p>
<h2>NOTES</h2>
<p> POSIX.1-2008 notes that the results are unspecified if <i>fn</i> does not preserve the current working directory. </p>
<p> The function <code>nftw</code>() and the use of <code>FTW_SL</code> with <code>ftw</code>() were introduced in SUSv1. </p>
<p> In some implementations (e.g., glibc), <code>ftw</code>() will never use <code>FTW_SL</code>, on other systems <code>FTW_SL</code> occurs only for symbolic links that do not point to an existing file, and again on other systems <code>ftw</code>() will use <code>FTW_SL</code> for each symbolic link. If <i>fpath</i> is a symbolic link and <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) failed, POSIX.1-2008 states that it is undefined whether <code>FTW_NS</code> or <code>FTW_SL</code> is passed in <i>typeflag</i>. For predictable results, use <code>nftw</code>().</p>
<h2>BUGS</h2>
<p> According to POSIX.1-2008, when the <i>typeflag</i> argument passed to <i>fn</i>() contains <code>FTW_SLN</code>, the buffer pointed to by <i>sb</i> should contain information about the dangling symbolic link (obtained by calling <code><a href="/docs/linux/man/2-lstat/">lstat</a></code>(2) on the link). Early glibc versions correctly followed the POSIX specification on this point. However, as a result of a regression introduced in glibc 2.4, the contents of the buffer pointed to by <i>sb</i> were undefined when <code>FTW_SLN</code> is passed in <i>typeflag</i>. (More precisely, the contents of the buffer were left unchanged in this case.) This regression was eventually fixed in glibc 2.30, so that the glibc implementation (once more) follows the POSIX specification.</p>
<h2>EXAMPLES</h2>
<p> The following program traverses the directory tree under the path named in its first command-line argument, or under the current directory if no argument is supplied. It displays various information about each file. The second command-line argument can be used to specify characters that control the value assigned to the <i>flags</i> argument when calling <code>nftw</code>().</p>
<h3>Program source</h3>
<p> #define _XOPEN_SOURCE 500 #include &lt;ftw.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;string.h&gt; #include &lt;stdint.h&gt; </p>
<p> static int display_info(const char *fpath, const struct stat *sb,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int tflag, struct FTW&nbsp;*ftwbuf) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%-3s&nbsp;%2d&nbsp;&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(tflag&nbsp;==&nbsp;FTW_D)&nbsp;?&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;d&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;:&nbsp;(tflag&nbsp;==&nbsp;FTW_DNR)&nbsp;?&nbsp;&quot;dnr&quot;&nbsp;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(tflag&nbsp;==&nbsp;FTW_DP)&nbsp;?&nbsp;<wbr>&nbsp;&quot;dp&quot;&nbsp;<wbr>&nbsp;:&nbsp;(tflag&nbsp;==&nbsp;FTW_F)&nbsp;?&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;f&quot;&nbsp;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(tflag&nbsp;==&nbsp;FTW_NS)&nbsp;?&nbsp;<wbr>&nbsp;&quot;ns&quot;&nbsp;<wbr>&nbsp;:&nbsp;(tflag&nbsp;==&nbsp;FTW_SL)&nbsp;?&nbsp;<wbr>&nbsp;&quot;sl&quot;&nbsp;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(tflag&nbsp;==&nbsp;FTW_SLN)&nbsp;?&nbsp;&quot;sln&quot;&nbsp;:&nbsp;&quot;???&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ftwbuf-&gt;level); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(tflag&nbsp;==&nbsp;FTW_NS)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&#8212;&#8212;-&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;else<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%7jd&quot;,&nbsp;(intmax_t)&nbsp;sb-&gt;st_size); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;%-40s&nbsp;%d&nbsp;%s
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fpath, ftwbuf-&gt;base, fpath&nbsp;+&nbsp;ftwbuf-&gt;base); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return 0;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;To tell nftw()&nbsp;to continue&nbsp;*/ } </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int flags&nbsp;=&nbsp;0; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;&gt;&nbsp;2&nbsp;&amp;&amp;&nbsp;strchr(argv[2],&nbsp;&#8216;d&#8217;)&nbsp;!=&nbsp;NULL)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;flags |=&nbsp;FTW_DEPTH;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;&gt;&nbsp;2&nbsp;&amp;&amp;&nbsp;strchr(argv[2],&nbsp;&#8216;p&#8217;)&nbsp;!=&nbsp;NULL)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;flags |=&nbsp;FTW_PHYS; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(nftw((argc&nbsp;&lt;&nbsp;2)&nbsp;?&nbsp;&quot;.&quot;&nbsp;: argv[1], display_info, 20, flags)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;nftw&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), <code><a href="/docs/linux/man/3-fts/">fts</a></code>(3), <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
