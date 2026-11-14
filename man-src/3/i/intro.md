---
title: "intro(3)"
name: "intro"
section: "3"
letter: "i"
url: "/docs/linux/man/3-intro/"
description: "intro – introduction to library functions"
---

<h2 class="name">NAME</h2>
<p> intro &#8211; introduction to library functions </p>
<h2>DESCRIPTION</h2>
<p> Section 3 of the manual describes all library functions excluding the library functions (system call wrappers) described in Section 2, which implement system calls. </p>
<p> Many of the functions described in the section are part of the Standard C Library (<i>libc</i>). Some functions are part of other libraries (e.g., the math library, <i>libm</i>, or the real-time library, <i>librt</i>) in which case the manual page will indicate the linker option needed to link against the required library (e.g., <i>-lm</i> and <i>-lrt</i>, respectively, for the aforementioned libraries). </p>
<p> In some cases, the programmer must define a feature test macro in order to obtain the declaration of a function from the header file specified in the man page SYNOPSIS section. (Where required, these feature test macros must be defined before including <i>any</i> header files.) In such cases, the required macro is described in the man page. For further information on feature test macros, see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7).</p>
<h2>CONFORMING TO</h2>
<p> Certain terms and abbreviations are used to indicate UNIX variants and standards to which calls in this section conform. See <code><a href="/docs/linux/man/7-standards/">standards</a></code>(7).</p>
<h2>NOTES</h2>
<h3>Authors and copyright conditions</h3>
<p> Look at the header of the manual page source for the author(s) and copyright conditions. Note that these can be different from page to page!</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-intro/">intro</a></code>(2), <code><a href="/docs/linux/man/3-errno/">errno</a></code>(3), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7), <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7), <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7), <code><a href="/docs/linux/man/7-libc/">libc</a></code>(7), <code><a href="/docs/linux/man/7-math_error/">math_error</a></code>(7), <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7), <code><a href="/docs/linux/man/7-standards/">standards</a></code>(7), <code><a href="/docs/linux/man/7-system_data_types/">system_data_types</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
