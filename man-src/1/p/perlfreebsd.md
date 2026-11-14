---
title: "perlfreebsd(1)"
name: "perlfreebsd"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlfreebsd/"
---

<h2 class="name">NAME</h2>
 

 perlfreebsd - Perl version 5 on FreeBSD systems 

<h2>DESCRIPTION</h2>

 This document describes various features of FreeBSD that will affect how Perl version 5 (hereafter just Perl) is compiled and/or runs.

<h3>FreeBSD core dumps from readdir_r with ithreads</h3>

 When perl is configured to use ithreads, it will use re-entrant library calls in preference to non-re-entrant versions. There is a bug in FreeBSD's <tt>&quot;readdir_r&quot;</tt> function in versions 4.5 and earlier that can cause a <font SIZE="-1">SEGV</font> when reading large directories. A patch for FreeBSD libc is available (see &lt;<a rel="nofollow" HREF="http://www.freebsd.org/cgi/query-pr.cgi?pr=misc/30631">http://www.freebsd.org/cgi/query-pr.cgi?pr=misc/30631</a>&gt; ) which has been integrated into FreeBSD 4.6.

<h3>$^X doesn't always contain a full path in FreeBSD</h3>

 perl sets <tt>$^X</tt> where possible to a full path by asking the operating system. On FreeBSD the full path of the perl interpreter is found by using <tt>&quot;sysctl&quot;</tt> with <tt>&quot;KERN_PROC_PATHNAME&quot;</tt> if that is supported, else by reading the symlink <i>/proc/curproc/file</i>. FreeBSD 7 and earlier has a bug where either approach sometimes returns an incorrect value (see &lt;<a rel="nofollow" HREF="http://www.freebsd.org/cgi/query-pr.cgi?pr=35703">http://www.freebsd.org/cgi/query-pr.cgi?pr=35703</a>&gt; ). In these cases perl will fall back to the old behaviour of using C's <tt>&quot;argv[0]&quot;</tt> value for <tt>$^X</tt>.

<h2>AUTHOR</h2>

 Nicholas Clark &lt;nick [at] ccl4.org&gt;, collating wisdom supplied by Slaven Rezic and Tim Bunce. 

 Please report any errors, updates, or suggestions to &lt;mailto:perlbug [at] perl.org&gt;. 

<h2>Index</h2>


