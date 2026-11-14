---
title: "environ(7)"
name: "environ"
section: "7"
letter: "e"
url: "/docs/linux/man/7-environ/"
description: "environ – user environment"
---

<p>environ &#8211; user environment</p>
<h2>Synopsis</h2>
<pre><code>extern char **</code><i>environ</i><code>;</code></pre>
<h2>Description</h2>
<p>The variable <i>environ</i> points to an array of pointers to strings called the &quot;environment&quot;. The last pointer in this array has the value NULL. (This variable must be declared in the user program, but is declared in the header file <i>&lt;unistd.h&gt;</i> if the <code>_GNU_SOURCE</code> feature test macro is defined.) This array of strings is made available to the process by the <code><a href="/docs/linux/man/3-exec/">exec</a></code>(3) call that started the process. When a child process is created via <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), it inherits a <i>copy</i> of its parent&#8217;s environment. By convention the strings in <i>environ</i> have the form &quot;<i>name</i><code>=</code><i>value</i>&quot;. Common examples are:</p>
<dl>
<dt><code>USER</code></p>
<dd>The name of the logged-in user (used by some BSD-derived programs).</p>
<dt><code>LOGNAME</code></p>
<dd>The name of the logged-in user (used by some System-V derived programs).</p>
<dt><code>HOME</code></p>
<dd>A user&#8217;s login directory, set by <code><a href="/docs/linux/man/1-login/">login</a></code>(1) from the password file <code><a href="/docs/linux/man/5-passwd/">passwd</a></code>(5).</p>
<dt><code>LANG</code></p>
<dd>The name of a locale to use for locale categories when not overridden by <code>LC_ALL</code> or more specific environment variables such as <code>LC_COLLATE</code>, <code>LC_CTYPE</code>, <code>LC_MESSAGES</code>, <code>LC_MONETARY</code>, <code>LC_NUMERIC</code>, and <code>LC_TIME</code> (see <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7) for further details of the <code>LC_*</code> environment variables).</p>
<dt><code>PATH</code></p>
<dd>The sequence of directory prefixes that <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1) and many other programs apply in searching for a file known by an incomplete pathname. The prefixes are separated by &#8216;<code>:</code>&#8216;. (Similarly one has <code>CDPATH</code> used by some shells to find the target of a change directory command, <code>MANPATH</code> used by <code><a href="/docs/linux/man/1-man/">man</a></code>(1) to find manual pages, and so on)</p>
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
<p> Names may be placed in the shell&#8217;s environment by the <i>export</i> command in <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1), or by the <i>setenv</i> command if you use <code><a href="/docs/linux/man/1-csh/">csh</a></code>(1). The initial environment of the shell is populated in various ways, such as definitions from <i>/etc/environment</i> that are processed by <code><a href="/docs/linux/man/8-pam_env/">pam_env</a></code>(8) for all users at login time (on systems that employ <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8)). In addition, various shell initialization scripts, such as the system-wide <i>/etc/profile</i> script and per-user initializations script may include commands that add variables to the shell&#8217;s environment; see the manual page of your preferred shell for details. Bourne-style shells support the syntax </p>
<pre><code>NAME=value command</code></pre>
<p> to create an environment variable definition only in the scope of the process that executes <i>command</i>. Multiple variable definitions, separated by white space, may precede <i>command</i>. Arguments may also be placed in the environment at the point of an <code><a href="/docs/linux/man/3-exec/">exec</a></code>(3). A C program can manipulate its environment using the functions <code><a href="/docs/linux/man/3-getenv/">getenv</a></code>(3), <code><a href="/docs/linux/man/3-putenv/">putenv</a></code>(3), <code><a href="/docs/linux/man/3-setenv/">setenv</a></code>(3), and <code><a href="/docs/linux/man/3-unsetenv/">unsetenv</a></code>(3). Note that the behavior of many programs and library routines is influenced by the presence or value of certain environment variables. Examples include the following:</p>
<dl>
<dt>*</p>
<dd>The variables <code>LANG</code>, <code>LANGUAGE</code>, <code>NLSPATH</code>, <code>LOCPATH</code>, <code>LC_ALL</code>, <code>LC_MESSAGES</code>, and so on influence locale handling; see <code><a href="/docs/linux/man/3-catopen/">catopen</a></code>(3), <code><a href="/docs/linux/man/3-gettext/">gettext</a></code>(3), and <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7).</p>
<dt>*</p>
<dd><code>TMPDIR</code> influences the path prefix of names created by <code><a href="/docs/linux/man/3-tempnam/">tempnam</a></code>(3) and other routines, and the temporary directory used by <code><a href="/docs/linux/man/1-sort/">sort</a></code>(1) and other programs.</p>
<dt>*</p>
<dd><code>LD_LIBRARY_PATH</code>, <code>LD_PRELOAD</code>, and other <code>LD_*</code> variables influence the behavior of the dynamic loader/linker.</p>
<dt>*</p>
<dd><code>POSIXLY_CORRECT</code> makes certain programs and library routines follow the prescriptions of POSIX.</p>
<dt>*</p>
<dd>The behavior of <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) is influenced by <code>MALLOC_*</code> variables.</p>
<dt>*</p>
<dd>The variable <code>HOSTALIASES</code> gives the name of a file containing aliases to be used with <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3).</p>
<dt>*</p>
<dd><code>TZ</code> and <code>TZDIR</code> give timezone information used by <code><a href="/docs/linux/man/3-tzset/">tzset</a></code>(3) and through that by functions like <code><a href="/docs/linux/man/3-ctime/">ctime</a></code>(3), <code><a href="/docs/linux/man/3-localtime/">localtime</a></code>(3), <code><a href="/docs/linux/man/3-mktime/">mktime</a></code>(3), <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3). See also <code><a href="/docs/linux/man/8-tzselect/">tzselect</a></code>(8).</p>
<dt>*</p>
<dd><code>TERMCAP</code> gives information on how to address a given terminal (or gives the name of a file containing such information).</p>
<dt>*</p>
<dd><code>COLUMNS</code> and <code>LINES</code> tell applications about the window size, possibly overriding the actual size.</p>
<dt>*</p>
<dd><code>PRINTER</code> or <code>LPDEST</code> may specify the desired printer to use. See <code><a href="/docs/linux/man/1-lpr/">lpr</a></code>(1).</dl>
<h2>Notes</h2>
<p>The <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) <code>PR_SET_MM_ENV_START</code> and <code>PR_SET_MM_ENV_END</code> operations can be used to control the location of the process&#8217;s environment.</p>
<h2>Bugs</h2>
<p>Clearly there is a security risk here. Many a system command has been tricked into mischief by a user who specified unusual values for <code>IFS</code> or <code>LD_LIBRARY_PATH</code>. </p>
<p> There is also the risk of name space pollution. Programs like <i>make</i> and <i>autoconf</i> allow overriding of default utility names from the environment with similarly named variables in all caps. Thus one uses <code>CC</code> to select the desired C compiler (and similarly <code>MAKE</code>, <code>AR</code>, <code>AS</code>, <code>FC</code>, <code>LD</code>, <code>LEX</code>, <code>RM</code>, <code>YACC</code>, etc.). However, in some traditional uses such an environment variable gives options for the program instead of a pathname. Thus, one has <code>MORE</code>, <code>LESS</code>, and <code>GZIP</code>. Such usage is considered mistaken, and to be avoided in new programs. The authors of <i>gzip</i> should consider renaming their option to <code>GZIP_OPT</code>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-bash/">bash</a></code>(1), <code><a href="/docs/linux/man/1-csh/">csh</a></code>(1), <code><a href="/docs/linux/man/1-env/">env</a></code>(1), <code><a href="/docs/linux/man/1-login/">login</a></code>(1), <code><a href="/docs/linux/man/1-printenv/">printenv</a></code>(1), <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1), <code><a href="/docs/linux/man/1-tcsh/">tcsh</a></code>(1), <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), <code><a href="/docs/linux/man/3-clearenv/">clearenv</a></code>(3), <code><a href="/docs/linux/man/3-exec/">exec</a></code>(3), <code><a href="/docs/linux/man/3-getenv/">getenv</a></code>(3), <code><a href="/docs/linux/man/3-putenv/">putenv</a></code>(3), <code><a href="/docs/linux/man/3-setenv/">setenv</a></code>(3), <code><a href="/docs/linux/man/3-unsetenv/">unsetenv</a></code>(3), <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7), <code><a href="/docs/linux/man/8-ld-so/">ld.so</a></code>(8), <code><a href="/docs/linux/man/8-pam_env/">pam_env</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
