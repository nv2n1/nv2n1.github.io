---
title: "perlopenbsd(1)"
name: "perlopenbsd"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlopenbsd/"
---

<h2 class="name">NAME</h2>
 

 perlopenbsd - Perl version 5 on OpenBSD systems 

<h2>DESCRIPTION</h2>

 This document describes various features of OpenBSD that will affect how Perl version 5 (hereafter just Perl) is compiled and/or runs.

<h3>OpenBSD core dumps from getprotobyname_r and getservbyname_r with ithreads</h3>

 When Perl is configured to use ithreads, it will use re-entrant library calls in preference to non-re-entrant versions. There is an incompatibility in OpenBSD's <tt>&quot;getprotobyname_r&quot;</tt> and <tt>&quot;getservbyname_r&quot;</tt> function in versions 3.7 and later that will cause a <font SIZE="-1">SEGV</font> when called without doing a <tt>&quot;bzero&quot;</tt> on their return structs prior to calling these functions. Current Perl's should handle this problem correctly. Older threaded Perls (5.8.6 or earlier) will run into this problem. If you want to run a threaded Perl on OpenBSD 3.7 or higher, you will need to upgrade to at least Perl 5.8.7.

<h2>AUTHOR</h2>

 Steve Peters &lt;steve [at] fisharerojo.org&gt; 

 Please report any errors, updates, or suggestions to <i>perlbug [at] perl.org</i>. 

<h2>Index</h2>


