---
title: "libc(7)"
name: "libc"
section: "7"
letter: "l"
url: "/docs/linux/man/7-libc/"
description: "libc – overview of standard C libraries on Linux"
---

<p>libc &#8211; overview of standard C libraries on Linux</p>
<h2>Description</h2>
<p>The term &quot;libc&quot; is commonly used as a shorthand for the &quot;standard C library&quot;, a library of standard functions that can be used by all C programs (and sometimes by programs in other languages). Because of some history (see below), use of the term &quot;libc&quot; to refer to the standard C library is somewhat ambiguous on Linux.</p>
<h3>glibc</h3>
<p>By far the most widely used C library on Linux is the GNU C Library often referred to as <i>glibc</i>. This is the C library that is nowadays used in all major Linux distributions. It is also the C library whose details are documented in the relevant pages of the <i>man-pages</i> project (primarily in Section 3 of the manual). Documentation of glibc is also available in the glibc manual, available via the command <i>info libc</i>. Release 1.0 of glibc was made in September 1992. (There were earlier 0.x releases.) The next major release of glibc was 2.0, at the beginning of 1997. </p>
<p> The pathname <i>/lib/libc.so.6</i> (or something similar) is normally a symbolic link that points to the location of the glibc library, and executing this pathname will cause glibc to display various information about the version installed on your system.</p>
<h3>Linux libc</h3>
<p>In the early to mid 1990s, there was for a while <i>Linux libc</i>, a fork of glibc 1.x created by Linux developers who felt that glibc development at the time was not sufficing for the needs of Linux. Often, this library was referred to (ambiguously) as just &quot;libc&quot;. Linux libc released major versions 2, 3, 4, and 5, as well as many minor versions of those releases. Linux libc4 was the last version to use the a.out binary format, and the first version to provide (primitive) shared library support. Linux libc 5 was the first version to support the ELF binary format; this version used the shared library soname <i>libc.so.5</i>. For a while, Linux libc was the standard C library in many Linux distributions. </p>
<p> However, notwithstanding the original motivations of the Linux libc effort, by the time glibc 2.0 was released (in 1997), it was clearly superior to Linux libc, and all major Linux distributions that had been using Linux libc soon switched back to glibc. To avoid any confusion with Linux libc versions, glibc 2.0 and later used the shared library soname <i>libc.so.6</i>. </p>
<p> Since the switch from Linux libc to glibc 2.0 occurred long ago, <i>man-pages</i> no longer takes care to document Linux libc details. Nevertheless, the history is visible in vestiges of information about Linux libc that remain in a few manual pages, in particular, references to <i>libc4</i> and <i>libc5</i>.</p>
<h3>Other C libraries</h3>
<p>There are various other less widely used C libraries for Linux. These libraries are generally smaller than glibc, both in terms of features and memory footprint, and often intended for building small binaries, perhaps targeted at development for embedded Linux systems. Among such libraries are <i>uClibc</i> <i>dietlibc</i> and <i>musl libc</i> Details of these libraries are covered by the <i>man-pages</i> project, where they are known.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-syscalls/">syscalls</a></code>(2), <code><a href="/docs/linux/man/3-getauxval/">getauxval</a></code>(3), <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5), <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7), <code><a href="/docs/linux/man/7-man-pages/">man-pages</a></code>(7), <code><a href="/docs/linux/man/7-standards/">standards</a></code>(7), <code><a href="/docs/linux/man/7-vdso/">vdso</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
