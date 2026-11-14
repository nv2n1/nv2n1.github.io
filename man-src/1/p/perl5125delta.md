---
title: "perl5125delta(1)"
name: "perl5125delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5125delta/"
description: "perl5125delta – what is new for perl v5.12.5"
---

<h2 class="name">NAME</h2>
<p> perl5125delta &#8211; what is new for perl v5.12.5 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.12.4 release and the 5.12.5 release. </p>
<p> If you are upgrading from an earlier release such as 5.12.3, first read perl5124delta, which describes differences between 5.12.3 and 5.12.4.</p>
<h2>Security</h2>
<h3>Encode decode_xs n-byte heap-overflow (<font SIZE="-1">CVE-2011-2939</font>)</h3>
<p> A bug in <tt>&quot;Encode&quot;</tt> could, on certain inputs, cause the heap to overflow. This problem has been corrected. Bug reported by Robert Zacek.</p>
<h3>File::Glob::bsd_glob() memory error with <font SIZE="-1">GLOB_ALTDIRFUNC</font> (<font SIZE="-1">CVE-2011-2728</font>).</h3>
<p> Calling <tt>&quot;File::Glob::bsd_glob&quot;</tt> with the unsupported flag <font SIZE="-1">GLOB_ALTDIRFUNC</font> would cause an access violation / segfault. A Perl program that accepts a flags value from an external source could expose itself to denial of service or arbitrary code execution attacks. There are no known exploits in the wild. The problem has been corrected by explicitly disabling all unsupported flags and setting unused function pointers to null. Bug reported by Clément Lecigne.</p>
<h3>Heap buffer overrun in &#8216;x&#8217; string repeat operator (<font SIZE="-1">CVE-2012-5195</font>)</h3>
<p> Poorly written perl code that allows an attacker to specify the count to perl&#8217;s &#8216;x&#8217; string repeat operator can already cause a memory exhaustion denial-of-service attack. A flaw in versions of perl before 5.15.5 can escalate that into a heap buffer overrun; coupled with versions of glibc before 2.16, it possibly allows the execution of arbitrary code. </p>
<p> This problem has been fixed.</p>
<h2>Incompatible Changes</h2>
<p> There are no changes intentionally incompatible with 5.12.4. If any exist, they are bugs and reports are welcome.</p>
<h2>Modules and Pragmata</h2>
<h3>Updated Modules</h3>
<p> <i>B::Concise</i> </p>
<p> B::Concise no longer produces mangled output with the <code>-tree</code> option [perl #80632]. </p>
<p> <i>charnames</i> </p>
<p> A regression introduced in Perl 5.8.8 has been fixed, that caused <tt>charnames::viacode(0)</tt> to return <tt>&quot;undef&quot;</tt> instead of the string &#8220;<font SIZE="-1">NULL&#8221;</font> [perl #72624]. </p>
<p> <i>Encode has been upgraded from version 2.39 to version 2.39_01.</i> </p>
<p> See &#8220;Security&#8221;. </p>
<p> <i>File::Glob has been upgraded from version 1.07 to version 1.07_01.</i> </p>
<p> See &#8220;Security&#8221;. </p>
<p> <i>Unicode::UCD</i> </p>
<p> The documentation for the <tt>&quot;upper&quot;</tt> function now actually says &#8220;upper&#8221;, not &#8220;lower&#8221;. </p>
<p> <i>Module::CoreList</i> </p>
<p> Module::CoreList has been updated to version 2.50_02 to add data for this release.</p>
<h2>Changes to Existing Documentation</h2>
<h3>perlebcdic</h3>
<p> The perlebcdic document contains a helpful table to use in <tt>&quot;tr///&quot;</tt> to convert between <font SIZE="-1">EBCDIC</font> and Latin1/ASCII. Unfortunately, the table was the inverse of the one it describes. This has been corrected.</p>
<h3>perlunicode</h3>
<p> The section on User-Defined Case Mappings had some bad markup and unclear sentences, making parts of it unreadable. This has been rectified.</p>
<h3>perluniprops</h3>
<p> This document has been corrected to take non-ASCII platforms into account.</p>
<h2>Installation and Configuration Improvements</h2>
<h3>Platform Specific Changes</h3>
<dl>
<dt>Mac <font SIZE="-1">OS X</font></p>
<dd> There have been configuration and test fixes to make Perl build cleanly on Lion and Mountain Lion.</p>
<dt>NetBSD</p>
<dd> The NetBSD hints file was corrected to be compatible with NetBSD 6.*</dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;chop&quot;</tt> now correctly handles characters above &#8220;
