---
title: "glob(3)"
name: "glob"
section: "3"
letter: "g"
url: "/docs/linux/man/3-glob/"
description: "glob, globfree – find pathnames matching a pattern, free memory from glob()"
---

<h2 class="name">NAME</h2>
<p> glob, globfree &#8211; find pathnames matching a pattern, free memory from glob() </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;glob.h&gt;
int glob(const char *pattern, int flags,
         int (*errfunc)(const char *epath, int eerrno),
         glob_t *pglob);
void globfree(glob_t *pglob);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>glob</code>() function searches for all the pathnames matching <i>pattern</i> according to the rules used by the shell (see <code><a href="/docs/linux/man/7-glob/">glob</a></code>(7)). No tilde expansion or parameter substitution is done; if you want these, use <code><a href="/docs/linux/man/3-wordexp/">wordexp</a></code>(3). </p>
<p> The <code>globfree</code>() function frees the dynamically allocated storage from an earlier call to <code>glob</code>(). </p>
<p> The results of a <code>glob</code>() call are stored in the structure pointed to by <i>pglob</i>. This structure is of type <i>glob_t</i> (declared in <i>&lt;glob.h&gt;</i>) and includes the following elements defined by POSIX.2 (more may be present as an extension): </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;gl_pathc;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Count of paths matched so far&nbsp;<wbr>&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;**gl_pathv;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;List of matched pathnames.&nbsp;<wbr>&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;gl_offs;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Slots to reserve in&nbsp;<i>gl_pathv</i>.&nbsp;<wbr>&nbsp;*/ } glob_t; </p>
<p> Results are stored in dynamically allocated storage. </p>
<p> The argument <i>flags</i> is made up of the bitwise OR of zero or more the following symbolic constants, which modify the behavior of <code>glob</code>():</p>
<dl>
<dt><code>GLOB_ERR</code></p>
<dd> Return upon a read error (because a directory does not have read permission, for example). By default, <code>glob</code>() attempts carry on despite errors, reading all of the directories that it can.</p>
<dt><code>GLOB_MARK</code></p>
<dd> Append a slash to each path which corresponds to a directory.</p>
<dt><code>GLOB_NOSORT</code></p>
<dd> Don&#8217;t sort the returned pathnames. The only reason to do this is to save processing time. By default, the returned pathnames are sorted.</p>
<dt><code>GLOB_DOOFFS</code></p>
<dd> Reserve <i>pglob-&gt;gl_offs</i> slots at the beginning of the list of strings in <i>pglob-&gt;pathv</i>. The reserved slots contain null pointers.</p>
<dt><code>GLOB_NOCHECK</code></p>
<dd> If no pattern matches, return the original pattern. By default, <code>glob</code>() returns <code>GLOB_NOMATCH</code> if there are no matches.</p>
<dt><code>GLOB_APPEND</code></p>
<dd> Append the results of this call to the vector of results returned by a previous call to <code>glob</code>(). Do not set this flag on the first invocation of <code>glob</code>().</p>
<dt><code>GLOB_NOESCAPE</code></p>
<dd> Don&#8217;t allow backslash (&#8216;\&#8217;) to be used as an escape character. Normally, a backslash can be used to quote the following character, providing a mechanism to turn off the special meaning metacharacters.</dl>
<p> <i>flags</i> may also include any of the following, which are GNU extensions and not defined by POSIX.2:</p>
<dl>
<dt><code>GLOB_PERIOD</code></p>
<dd> Allow a leading period to be matched by metacharacters. By default, metacharacters can&#8217;t match a leading period.</p>
<dt><code>GLOB_ALTDIRFUNC</code></p>
<dd> Use alternative functions <i>pglob-&gt;gl_closedir</i>, <i>pglob-&gt;gl_readdir</i>, <i>pglob-&gt;gl_opendir</i>, <i>pglob-&gt;gl_lstat</i>, and <i>pglob-&gt;gl_stat</i> for filesystem access instead of the normal library functions.</p>
<dt><code>GLOB_BRACE</code></p>
<dd> Expand <code><a href="/docs/linux/man/1-csh/">csh</a></code>(1) style brace expressions of the form <code>{a,b}</code>. Brace expressions can be nested. Thus, for example, specifying the pattern &quot;{foo/{,cat,dog},bar}&quot; would return the same results as four separate <code>glob</code>() calls using the strings: &quot;foo/&quot;, &quot;foo/cat&quot;, &quot;foo/dog&quot;, and &quot;bar&quot;.</p>
<dt><code>GLOB_NOMAGIC</code></p>
<dd> If the pattern contains no metacharacters, then it should be returned as the sole matching word, even if there is no file with that name.</p>
<dt><code>GLOB_TILDE</code></p>
<dd> Carry out tilde expansion. If a tilde (&#8216;~&#8217;) is the only character in the pattern, or an initial tilde is followed immediately by a slash (&#8216;/&#8217;), then the home directory of the caller is substituted for the tilde. If an initial tilde is followed by a username (e.g., &quot;~andrea/bin&quot;), then the tilde and username are substituted by the home directory of that user. If the username is invalid, or the home directory cannot be determined, then no substitution is performed.</p>
<dt><code>GLOB_TILDE_CHECK</code></p>
<dd> This provides behavior similar to that of <code>GLOB_TILDE</code>. The difference is that if the username is invalid, or the home directory cannot be determined, then instead of using the pattern itself as the name, <code>glob</code>() returns <code>GLOB_NOMATCH</code> to indicate an error.</p>
<dt><code>GLOB_ONLYDIR</code></p>
<dd> This is a <i>hint</i> to <code>glob</code>() that the caller is interested only in directories that match the pattern. If the implementation can easily determine file-type information, then nondirectory files are not returned to the caller. However, the caller must still check that returned files are directories. (The purpose of this flag is merely to optimize performance when the caller is interested only in directories.)</dl>
<p> If <i>errfunc</i> is not NULL, it will be called in case of an error with the arguments <i>epath</i>, a pointer to the path which failed, and <i>eerrno</i>, the value of <i>errno</i> as returned from one of the calls to <code><a href="/docs/linux/man/3-opendir/">opendir</a></code>(3), <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3), or <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2). If <i>errfunc</i> returns nonzero, or if <code>GLOB_ERR</code> is set, <code>glob</code>() will terminate after the call to <i>errfunc</i>. </p>
<p> Upon successful return, <i>pglob-&gt;gl_pathc</i> contains the number of matched pathnames and <i>pglob-&gt;gl_pathv</i> contains a pointer to the list of pointers to matched pathnames. The list of pointers is terminated by a null pointer. </p>
<p> It is possible to call <code>glob</code>() several times. In that case, the <code>GLOB_APPEND</code> flag has to be set in <i>flags</i> on the second and later invocations. </p>
<p> As a GNU extension, <i>pglob-&gt;gl_flags</i> is set to the flags specified, <code>or</code>ed with <code>GLOB_MAGCHAR</code> if any metacharacters were found.</p>
<h2>RETURN VALUE</h2>
<p> On successful completion, <code>glob</code>() returns zero. Other possible returns are:</p>
<dl>
<dt><code>GLOB_NOSPACE</code></p>
<dd> for running out of memory,</p>
<dt><code>GLOB_ABORTED</code></p>
<dd> for a read error, and</p>
<dt><code>GLOB_NOMATCH</code></p>
<dd> for no found matches.</dl>
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
<td> <code>glob</code>() </td>
<td>Thread safety</td>
<td> MT-Unsafe race:utent env<br />
 sig:ALRM timer locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>globfree</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<p> In the above table, <i>utent</i> in <i>race:utent</i> signifies that if any of the functions <code><a href="/docs/linux/man/3-setutent/">setutent</a></code>(3), <code><a href="/docs/linux/man/3-getutent/">getutent</a></code>(3), or <code><a href="/docs/linux/man/3-endutent/">endutent</a></code>(3) are used in parallel in different threads of a program, then data races could occur. <code>glob</code>() calls those functions, so we use race:utent to remind users.</p>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, POSIX.2.</p>
<h2>NOTES</h2>
<p> The structure elements <i>gl_pathc</i> and <i>gl_offs</i> are declared as <i>size_t</i> in glibc 2.1, as they should be according to POSIX.2, but are declared as <i>int</i> in glibc 2.0.</p>
<h2>BUGS</h2>
<p> The <code>glob</code>() function may fail due to failure of underlying function calls, such as <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) or <code><a href="/docs/linux/man/3-opendir/">opendir</a></code>(3). These will store their error code in <i>errno</i>.</p>
<h2>EXAMPLES</h2>
<p> One example of use is the following code, which simulates typing </p>
<p> ls -l *.c ../*.c </p>
<p> in the shell: </p>
<p> glob_t globbuf; </p>
<p> globbuf.gl_offs = 2; glob(&quot;*.c&quot;, GLOB_DOOFFS, NULL, &amp;globbuf); glob(&quot;../*.c&quot;, GLOB_DOOFFS | GLOB_APPEND, NULL, &amp;globbuf); globbuf.gl_pathv[0] = &quot;ls&quot;; globbuf.gl_pathv[1] = &quot;-l&quot;; execvp(&quot;ls&quot;, &amp;globbuf.gl_pathv[0]);</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1), <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1), <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), <code><a href="/docs/linux/man/3-exec/">exec</a></code>(3), <code><a href="/docs/linux/man/3-fnmatch/">fnmatch</a></code>(3), <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), <code><a href="/docs/linux/man/3-opendir/">opendir</a></code>(3), <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3), <code><a href="/docs/linux/man/3-wordexp/">wordexp</a></code>(3), <code><a href="/docs/linux/man/7-glob/">glob</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
