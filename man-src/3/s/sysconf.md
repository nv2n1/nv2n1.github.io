---
title: "sysconf(3)"
name: "sysconf"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sysconf/"
description: "sysconf – get configuration information at run time"
---

<p>sysconf &#8211; get configuration information at run time</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;unistd.h&gt;

long sysconf(int name);</code></pre>
<h2>Description</h2>
<p>POSIX allows an application to test at compile or run time whether certain options are supported, or what the value is of certain configurable constants or limits. </p>
<p> At compile time this is done by including <i>&lt;unistd.h&gt;</i> and/or <i>&lt;limits.h&gt;</i> and testing the value of certain macros. </p>
<p> At run time, one can ask for numerical values using the present function <code>sysconf</code>(). One can ask for numerical values that may depend on the filesystem in which a file resides using <code><a href="/docs/linux/man/3-fpathconf/">fpathconf</a></code>(3) and <code><a href="/docs/linux/man/3-pathconf/">pathconf</a></code>(3). One can ask for string values using <code><a href="/docs/linux/man/3-confstr/">confstr</a></code>(3). </p>
<p> The values obtained from these functions are system configuration constants. They do not change during the lifetime of a process. </p>
<p> For options, typically, there is a constant <code>_POSIX_FOO</code> that may be defined in <i>&lt;unistd.h&gt;</i>. If it is undefined, one should ask at run time. If it is defined to -1, then the option is not supported. If it is defined to 0, then relevant functions and headers exist, but one has to ask at run time what degree of support is available. If it is defined to a value other than -1 or 0, then the option is supported. Usually the value (such as 200112L) indicates the year and month of the POSIX revision describing the option. Glibc uses the value 1 to indicate support as long as the POSIX revision has not been published yet. The <code>sysconf</code>() argument will be <code>_SC_FOO</code>. For a list of options, see <code><a href="/docs/linux/man/7-posixoptions/">posixoptions</a></code>(7). </p>
<p> For variables or limits, typically, there is a constant <code>_FOO</code>, maybe defined in <i>&lt;limits.h&gt;</i>, or <code>_POSIX_FOO</code>, maybe defined in <i>&lt;unistd.h&gt;</i>. The constant will not be defined if the limit is unspecified. If the constant is defined, it gives a guaranteed value, and a greater value might actually be supported. If an application wants to take advantage of values which may change between systems, a call to <code>sysconf</code>() can be made. The <code>sysconf</code>() argument will be <code>_SC_FOO</code>.</p>
<h3>POSIX.1 variables</h3>
<p>We give the name of the variable, the name of the <code>sysconf</code>() argument used to inquire about its value, and a short description. </p>
<p> First, the POSIX.1 compatible values.</p>
<dl>
<dt><code>ARG_MAX</code> &#8211; <code>_SC_ARG_MAX</code></p>
<dd>The maximum length of the arguments to the <code><a href="/docs/linux/man/3-exec/">exec</a></code>(3) family of functions. Must not be less than <code>_POSIX_ARG_MAX</code> (4096).</p>
<dt><code>CHILD_MAX</code> &#8211; <code>_SC_CHILD_MAX</code></p>
<dd>The maximum number of simultaneous processes per user ID. Must not be less than <code>_POSIX_CHILD_MAX</code> (25).</p>
<dt><code>HOST_NAME_MAX</code> &#8211; <code>_SC_HOST_NAME_MAX</code></p>
<dd>Maximum length of a hostname, not including the terminating null byte, as returned by <code><a href="/docs/linux/man/2-gethostname/">gethostname</a></code>(2). Must not be less than <code>_POSIX_HOST_NAME_MAX</code> (255).</p>
<dt><code>LOGIN_NAME_MAX</code> &#8211; <code>_SC_LOGIN_NAME_MAX</code></p>
<dd>Maximum length of a login name, including the terminating null byte. Must not be less than <code>_POSIX_LOGIN_NAME_MAX</code> (9).</p>
<dt><code>NGROUPS_MAX</code> &#8211; <code>_SC_NGROUPS_MAX</code></p>
<dd>Maximum number of supplementary group IDs.</p>
<dt>clock ticks &#8211; <code>_SC_CLK_TCK</code></p>
<dd>The number of clock ticks per second. The corresponding variable is obsolete. It was of course called <code>CLK_TCK</code>. (Note: the macro <code>CLOCKS_PER_SEC</code> does not give information: it must equal 1000000.)</p>
<dt><code>OPEN_MAX</code> &#8211; <code>_SC_OPEN_MAX</code></p>
<dd>The maximum number of files that a process can have open at any time. Must not be less than <code>_POSIX_OPEN_MAX</code> (20).</p>
<dt><code>PAGESIZE</code> &#8211; <code>_SC_PAGESIZE</code></p>
<dd>Size of a page in bytes. Must not be less than 1.</p>
<dt><code>PAGE_SIZE</code> &#8211; <code>_SC_PAGE_SIZE</code></p>
<dd>A synonym for <code>PAGESIZE</code>/<code>_SC_PAGESIZE</code>. (Both <code>PAGESIZE</code> and <code>PAGE_SIZE</code> are specified in POSIX.)</p>
<dt><code>RE_DUP_MAX</code> &#8211; <code>_SC_RE_DUP_MAX</code></p>
<dd>The number of repeated occurrences of a BRE permitted by <code><a href="/docs/linux/man/3-regexec/">regexec</a></code>(3) and <code><a href="/docs/linux/man/3-regcomp/">regcomp</a></code>(3). Must not be less than <code>_POSIX2_RE_DUP_MAX</code> (255).</p>
<dt><code>STREAM_MAX</code> &#8211; <code>_SC_STREAM_MAX</code></p>
<dd>The maximum number of streams that a process can have open at any time. If defined, it has the same value as the standard C macro <code>FOPEN_MAX</code>. Must not be less than <code>_POSIX_STREAM_MAX</code> (8).</p>
<dt><code>SYMLOOP_MAX</code> &#8211; <code>_SC_SYMLOOP_MAX</code></p>
<dd>The maximum number of symbolic links seen in a pathname before resolution returns <code>ELOOP</code>. Must not be less than <code>_POSIX_SYMLOOP_MAX</code> (8).</p>
<dt><code>TTY_NAME_MAX</code> &#8211; <code>_SC_TTY_NAME_MAX</code></p>
<dd>The maximum length of terminal device name, including the terminating null byte. Must not be less than <code>_POSIX_TTY_NAME_MAX</code> (9).</p>
<dt><code>TZNAME_MAX</code> &#8211; <code>_SC_TZNAME_MAX</code></p>
<dd>The maximum number of bytes in a timezone name. Must not be less than <code>_POSIX_TZNAME_MAX</code> (6).</p>
<dt><code>_POSIX_VERSION</code> &#8211; <code>_SC_VERSION</code></p>
<dd>indicates the year and month the POSIX.1 standard was approved in the format <code>YYYYMML</code>; the value <code>199009L</code> indicates the Sept. 1990 revision.</dl>
<h3>POSIX.2 variables</h3>
<p>Next, the POSIX.2 values, giving limits for utilities.</p>
<dl>
<dt><code>BC_BASE_MAX</code> &#8211; <code>_SC_BC_BASE_MAX</code></p>
<dd>indicates the maximum <i>obase</i> value accepted by the <code><a href="/docs/linux/man/1-bc/">bc</a></code>(1) utility.</p>
<dt><code>BC_DIM_MAX</code> &#8211; <code>_SC_BC_DIM_MAX</code></p>
<dd>indicates the maximum value of elements permitted in an array by <code><a href="/docs/linux/man/1-bc/">bc</a></code>(1).</p>
<dt><code>BC_SCALE_MAX</code> &#8211; <code>_SC_BC_SCALE_MAX</code></p>
<dd>indicates the maximum <i>scale</i> value allowed by <code><a href="/docs/linux/man/1-bc/">bc</a></code>(1).</p>
<dt><code>BC_STRING_MAX</code> &#8211; <code>_SC_BC_STRING_MAX</code></p>
<dd>indicates the maximum length of a string accepted by <code><a href="/docs/linux/man/1-bc/">bc</a></code>(1).</p>
<dt><code>COLL_WEIGHTS_MAX</code> &#8211; <code>_SC_COLL_WEIGHTS_MAX</code></p>
<dd>indicates the maximum numbers of weights that can be assigned to an entry of the <code>LC_COLLATE order</code> keyword in the locale definition file.</p>
<dt><code>EXPR_NEST_MAX</code> &#8211; <code>_SC_EXPR_NEST_MAX</code></p>
<dd>is the maximum number of expressions which can be nested within parentheses by <code><a href="/docs/linux/man/1-expr/">expr</a></code>(1).</p>
<dt><code>LINE_MAX</code> &#8211; <code>_SC_LINE_MAX</code></p>
<dd>The maximum length of a utility&#8217;s input line, either from standard input or from a file. This includes space for a trailing newline.</p>
<dt><code>RE_DUP_MAX</code> &#8211; <code>_SC_RE_DUP_MAX</code></p>
<dd>The maximum number of repeated occurrences of a regular expression when the interval notation <code>\{m,n\}</code> is used.</p>
<dt><code>POSIX2_VERSION</code> &#8211; <code>_SC_2_VERSION</code></p>
<dd>indicates the version of the POSIX.2 standard in the format of YYYYMML.</p>
<dt><code>POSIX2_C_DEV</code> &#8211; <code>_SC_2_C_DEV</code></p>
<dd>indicates whether the POSIX.2 C language development facilities are supported.</p>
<dt><code>POSIX2_FORT_DEV</code> &#8211; <code>_SC_2_FORT_DEV</code></p>
<dd>indicates whether the POSIX.2 FORTRAN development utilities are supported.</p>
<dt><code>POSIX2_FORT_RUN</code> &#8211; <code>_SC_2_FORT_RUN</code></p>
<dd>indicates whether the POSIX.2 FORTRAN run-time utilities are supported.</p>
<dt><code>_POSIX2_LOCALEDEF</code> &#8211; <code>_SC_2_LOCALEDEF</code></p>
<dd>indicates whether the POSIX.2 creation of locales via <code><a href="/docs/linux/man/1-localedef/">localedef</a></code>(1) is supported.</p>
<dt><code>POSIX2_SW_DEV</code> &#8211; <code>_SC_2_SW_DEV</code></p>
<dd>indicates whether the POSIX.2 software development utilities option is supported.</dl>
<p> These values also exist, but may not be standard.</p>
<dl>
<dt> &#8211; <code>_SC_PHYS_PAGES</code></p>
<dd>The number of pages of physical memory. Note that it is possible for the product of this value and the value of <code>_SC_PAGESIZE</code> to overflow.</p>
<dt> &#8211; <code>_SC_AVPHYS_PAGES</code></p>
<dd>The number of currently available pages of physical memory.</p>
<dt> &#8211; <code>_SC_NPROCESSORS_CONF</code></p>
<dd>The number of processors configured. See also <code><a href="/docs/linux/man/3-get_nprocs_conf/">get_nprocs_conf</a></code>(3).</p>
<dt> &#8211; <code>_SC_NPROCESSORS_ONLN</code></p>
<dd>The number of processors currently online (available). See also <code><a href="/docs/linux/man/3-get_nprocs_conf/">get_nprocs_conf</a></code>(3).</dl>
<h2>Return Value</h2>
<p>The return value of <code>sysconf</code>() is one of the following:</p>
<dl>
<dt>*</p>
<dd>On error, -1 is returned and <i>errno</i> is set to indicate the cause of the error (for example, <code>EINVAL</code>, indicating that <i>name</i> is invalid).</p>
<dt>*</p>
<dd>If <i>name</i> corresponds to a maximum or minimum limit, and that limit is indeterminate, -1 is returned and <i>errno</i> is not changed. (To distinguish an indeterminate limit from an error, set <i>errno</i> to zero before the call, and then check whether <i>errno</i> is nonzero when -1 is returned.)</p>
<dt>*</p>
<dd>If <i>name</i> corresponds to an option, a positive value is returned if the option is supported, and -1 is returned if the option is not supported.</p>
<dt>*</p>
<dd>Otherwise, the current value of the option or limit is returned. This value will not be more restrictive than the corresponding value that was described to the application in <i>&lt;unistd.h&gt;</i> or <i>&lt;limits.h&gt;</i> when the application was compiled.</dl>
<h2>Errors</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd><i>name</i> is invalid.</dl>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>sysconf</code>() </td>
<td>Thread safety</td>
<td>MT-Safe env
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Bugs</h2>
<p>It is difficult to use <code>ARG_MAX</code> because it is not specified how much of the argument space for <code><a href="/docs/linux/man/3-exec/">exec</a></code>(3) is consumed by the user&#8217;s environment variables. </p>
<p> Some returned values may be huge; they are not suitable for allocating memory.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-bc/">bc</a></code>(1), <code><a href="/docs/linux/man/1-expr/">expr</a></code>(1), <code><a href="/docs/linux/man/1-getconf/">getconf</a></code>(1), <code><a href="/docs/linux/man/1-locale/">locale</a></code>(1), <code><a href="/docs/linux/man/3-confstr/">confstr</a></code>(3), <code><a href="/docs/linux/man/3-fpathconf/">fpathconf</a></code>(3), <code><a href="/docs/linux/man/3-pathconf/">pathconf</a></code>(3), <code><a href="/docs/linux/man/7-posixoptions/">posixoptions</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
