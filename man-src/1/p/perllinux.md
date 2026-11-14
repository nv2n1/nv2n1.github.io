---
title: "perllinux(1)"
name: "perllinux"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perllinux/"
---

<h2 class="name">NAME</h2>
 

 perllinux - Perl version 5 on Linux systems 

<h2>DESCRIPTION</h2>

 This document describes various features of Linux that will affect how Perl version 5 (hereafter just Perl) is compiled and/or runs.

<h3>Experimental Support for Sun Studio Compilers for Linux <font SIZE="-1">OS</font></h3>

 Sun Microsystems has released a port of their Sun Studio compilers for Linux. As of November 2005, only an alpha version has been released. Until a release of these compilers is made, support for compiling Perl with these compiler experimental. 

 Also, some special instructions for building Perl with Sun Studio on Linux. Following the normal <tt>&quot;Configure&quot;</tt>, you have to run make as follows: 

 <pre>
    LDLOADLIBS=-lc make
</pre> 

 <tt>&quot;LDLOADLIBS&quot;</tt> is an environment variable used by the linker to link modules <tt>&quot;/ext&quot;</tt> modules to glibc. Currently, that environment variable is not getting populated by a combination of <tt>&quot;Config&quot;</tt> entries and <tt>&quot;ExtUtil::MakeMaker&quot;</tt>. While there may be a bug somewhere in Perl's configuration or <tt>&quot;ExtUtil::MakeMaker&quot;</tt> causing the problem, the most likely cause is an incomplete understanding of Sun Studio by this author. Further investigation is needed to get this working better.

<h2>AUTHOR</h2>

 Steve Peters &lt;steve [at] fisharerojo.org&gt; 

 Please report any errors, updates, or suggestions to <i>perlbug [at] perl.org</i>. 

<h2>Index</h2>



<dt><a HREF="#lbAE">AUTHOR</a>
<dd></dl>
