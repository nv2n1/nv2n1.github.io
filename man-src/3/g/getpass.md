---
title: "getpass(3)"
name: "getpass"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getpass/"
description: "getpass – get a password"
---

<h2 class="name">NAME</h2>
<p> getpass &#8211; get a password </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>char *getpass(const char *</code><i>prompt</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>getpass</code>():</p>
<dl>
<dt>
<dd>
<dl>
<dt>Since glibc 2.2.2:</p>
<dd>
<pre><code>
_XOPEN_SOURCE &amp;&amp; !(_POSIX_C_SOURCE &amp; nbsp; &gt;= &amp;nbsp; 200112L) || /* Glibc since 2.19: */ _DEFAULT_SOURCE || /* Glibc versions &lt;= 2.19: */ _BSD_SOURCE
</code></pre>
<dt>Before glibc 2.2.2:</p>
<dd> none</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> This function is obsolete. Do not use it. If you want to read input without terminal echoing enabled, see the description of the <i>ECHO</i> flag in <code><a href="/docs/linux/man/3-termios/">termios</a></code>(3). </p>
<p> The <code>getpass</code>() function opens <i>/dev/tty</i> (the controlling terminal of the process), outputs the string <i>prompt</i>, turns off echoing, reads one line (the &quot;password&quot;), restores the terminal state and closes <i>/dev/tty</i> again.</p>
<h2>RETURN VALUE</h2>
<p> The function <code>getpass</code>() returns a pointer to a static buffer containing (the first <code>PASS_MAX</code> bytes of) the password without the trailing newline, terminated by a null byte (&#8216;
