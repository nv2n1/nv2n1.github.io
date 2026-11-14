---
title: "environ(5)"
name: "environ"
section: "5"
letter: "e"
url: "/docs/linux/man/5-environ/"
description: "environ – user environment"
---

<p>environ &#8211; user environment</p>
<h2>Synopsis</h2>
<pre><code>extern char **</code><i>environ</i><code>;</code>
<br></pre>
<h2>Description</h2>
<p>The variable <i>environ</i> points to an array of pointers to strings called the &quot;environment&quot;. The last pointer in this array has the value NULL. (This variable must be declared in the user program, but is declared in the header file <i>&lt;unistd.h&gt;</i> in case the header files came from libc4 or libc5, and in case they came from glibc and <code>_GNU_SOURCE</code> was defined.) This array of strings is made available to the process by the <code><a href="/docs/linux/man/3-exec/">exec</a></code>(3) call that started the process. </p>
<p> By convention the strings in <i>environ</i> have the form &quot;<i>name</i><code>=</code><i>value</i>&quot;. Common examples are:</p>
<dl>
<dt><code>USER</code></p>
<dd>The name of the logged-in user (used by some BSD-derived programs).</p>
<dt><code>LOGNAME</code></p>
<dd>The name of the logged-in user (used by some System-V derived programs).</p>
<dt><code>HOME</code></p>
<dd>A user&#8217;s login directory, set by <code><a href="/docs/linux/man/1-login/">login</a></code>(1) from the password file <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5).</p>
<dt><code>LANG</code></p>
<dd>The name of a locale to use for locale categories when not overridden by <code>LC_ALL</code> or more specific environment variables like <code>LC_COLLATE</code>, <code>LC_CTYPE</code>, <code>LC_MESSAGES</code>, <code>LC_MONETARY</code>, <code>LC_NUMERIC</code>, <code>LC_TIME</code>, cf. <code><a href="/docs/linux/man/5-locale/">locale</a></code>(5).</p>
<dt><code>PATH</code></p>
<dd>The sequence of directory prefixes that <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1) and many other programs apply in searching for a file known by an incomplete pathname. The prefixes are separated by &#8216;<code>:</code>&#8216;. (Similarly one has <code>CDPATH</code> used by some shells to find the target of a change directory command, <code>MANPATH</code> used by <code><a href="/docs/linux/man/1-man/">man</a></code>(1) to find manual pages, etc.)</p>
<dt><code>PWD</code></p>
<dd>The current working directory. Set by some shells.</p>
<dt><code>SHELL</code></p>
<dd>The pathname of the user&#8217;s login shell.</p>
<dt><code>TERM</code></p>
<dd>The terminal type for which output is to be prepared.</p>
<dt><code>PAGER</code></p>
<dd>The user&#8217;s preferred utility to display text files.</p>
<dt><code>EDITOR</code>/<code>VISUAL</code></p>
<dd>The user&#8217;s preferred utility to edit text files.</dl>
<p> Further names may be placed in the environment by the <i>export</i> command and &quot;name=value&quot; in <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1), or by the <i>setenv</i> command if you use <code><a href="/docs/linux/man/1-csh/">csh</a></code>(1). Arguments may also be placed in the environment at the point of an <code><a href="/docs/linux/man/3-exec/">exec</a></code>(3). A C program can manipulate its environment using the functions <code><a href="/docs/linux/man/3-getenv/">getenv</a></code>(3), <code><a href="/docs/linux/man/3-putenv/">putenv</a></code>(3), <code><a href="/docs/linux/man/3-setenv/">setenv</a></code>(3), and <code><a href="/docs/linux/man/3-unsetenv/">unsetenv</a></code>(3). </p>
<p> Note that the behavior of many programs and library routines is influenced by the presence or value of certain environment variables. A random collection: </p>
<p> The variables <code>LANG</code>, <code>LANGUAGE</code>, <code>NLSPATH</code>, <code>LOCPATH</code>, <code>LC_ALL</code>, <code>LC_MESSAGES</code>, etc. influence locale handling, cf. <code><a href="/docs/linux/man/5-locale/">locale</a></code>(5). </p>
<p> <code>TMPDIR</code> influences the path prefix of names created by <code><a href="/docs/linux/man/3-tmpnam/">tmpnam</a></code>(3) and other routines, the temporary directory used by <code><a href="/docs/linux/man/1-sort/">sort</a></code>(1) and other programs, etc. </p>
<p> <code>LD_LIBRARY_PATH</code>, <code>LD_PRELOAD</code> and other LD_* variables influence the behavior of the dynamic loader/linker. </p>
<p> <code>POSIXLY_CORRECT</code> makes certain programs and library routines follow the prescriptions of POSIX. </p>
<p> The behavior of <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) is influenced by <code>MALLOC_*</code> variables. </p>
<p> The variable <code>HOSTALIASES</code> gives the name of a file containing aliases to be used with <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3). </p>
<p> <code>TZ</code> and <code>TZDIR</code> give timezone information used by <code><a href="/docs/linux/man/3-tzset/">tzset</a></code>(3) and through that by functions like <code><a href="/docs/linux/man/3-ctime/">ctime</a></code>(3), <code><a href="/docs/linux/man/3-localtime/">localtime</a></code>(3), <code><a href="/docs/linux/man/3-mktime/">mktime</a></code>(3), <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3). See also <code><a href="/docs/linux/man/8-tzselect/">tzselect</a></code>(8). </p>
<p> <code>TERMCAP</code> gives information on how to address a given terminal (or gives the name of a file containing such information). </p>
<p> <code>COLUMNS</code> and <code>LINES</code> tell applications about the window size, possibly overriding the actual size. </p>
<p> <code>PRINTER</code> or <code>LPDEST</code> may specify the desired printer to use. See <code><a href="/docs/linux/man/1-lpr/">lpr</a></code>(1). </p>
<p> Etc.</p>
<h2>Bugs</h2>
<p>Clearly there is a security risk here. Many a system command has been tricked into mischief by a user who specified unusual values for <code>IFS</code> or <code>LD_LIBRARY_PATH</code>. </p>
<p> There is also the risk of name space pollution. Programs like <i>make</i> and <i>autoconf</i> allow overriding of default utility names from the environment with similarly named variables in all caps. Thus one uses <code>CC</code> to select the desired C compiler (and similarly <code>MAKE</code>, <code>AR</code>, <code>AS</code>, <code>FC</code>, <code>LD</code>, <code>LEX</code>, <code>RM</code>, <code>YACC</code>, etc.). However, in some traditional uses such an environment variable gives options for the program instead of a pathname. Thus, one has <code>MORE</code>, <code>LESS</code>, and <code>GZIP</code>. Such usage is considered mistaken, and to be avoided in new programs. The authors of <i>gzip</i> should consider renaming their option to <code>GZIP_OPT</code>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-bash/">bash</a></code>(1), <code><a href="/docs/linux/man/1-csh/">csh</a></code>(1), <code><a href="/docs/linux/man/1-login/">login</a></code>(1), <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1), <code><a href="/docs/linux/man/1-tcsh/">tcsh</a></code>(1), <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), <code><a href="/docs/linux/man/3-clearenv/">clearenv</a></code>(3), <code><a href="/docs/linux/man/3-exec/">exec</a></code>(3), <code><a href="/docs/linux/man/3-getenv/">getenv</a></code>(3), <code><a href="/docs/linux/man/3-putenv/">putenv</a></code>(3), <code><a href="/docs/linux/man/3-setenv/">setenv</a></code>(3), <code><a href="/docs/linux/man/3-unsetenv/">unsetenv</a></code>(3), <code><a href="/docs/linux/man/5-locale/">locale</a></code>(5)</p>
<h2>Colophon</h2>
<p>This page is part of release 3.35 of the Linux <i>man-pages</i> project. A description of the project, and information about reporting bugs, can be found at <a rel="nofollow" href="http://man7.org/linux/man-pages/.">http://man7.org/linux/man-pages/.</a> </p>
