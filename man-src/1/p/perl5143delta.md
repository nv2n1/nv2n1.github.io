---
title: "perl5143delta(1)"
name: "perl5143delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5143delta/"
description: "perl5143delta – what is new for perl v5.14.3"
---

<h2 class="name">NAME</h2>
<p> perl5143delta &#8211; what is new for perl v5.14.3 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.14.2 release and the 5.14.3 release. </p>
<p> If you are upgrading from an earlier release such as 5.12.0, first read perl5140delta, which describes differences between 5.12.0 and 5.14.0.</p>
<h2>Core Enhancements</h2>
<p> No changes since 5.14.0.</p>
<h2>Security</h2>
<h3>Digest unsafe use of eval (<font SIZE="-1">CVE-2011-3597</font>)</h3>
<p> The <tt>&quot;Digest-&gt;new()&quot;</tt> function did not properly sanitize input before using it in an <code>eval()</code> call, which could lead to the injection of arbitrary Perl code. </p>
<p> In order to exploit this flaw, the attacker would need to be able to set the algorithm name used, or be able to execute arbitrary Perl code already. </p>
<p> This problem has been fixed.</p>
<h3>Heap buffer overrun in &#8216;x&#8217; string repeat operator (<font SIZE="-1">CVE-2012-5195</font>)</h3>
<p> Poorly written perl code that allows an attacker to specify the count to perl&#8217;s &#8216;x&#8217; string repeat operator can already cause a memory exhaustion denial-of-service attack. A flaw in versions of perl before 5.15.5 can escalate that into a heap buffer overrun; coupled with versions of glibc before 2.16, it possibly allows the execution of arbitrary code. </p>
<p> This problem has been fixed.</p>
<h2>Incompatible Changes</h2>
<p> There are no changes intentionally incompatible with 5.14.0. If any exist, they are bugs and reports are welcome.</p>
<h2>Deprecations</h2>
<p> There have been no deprecations since 5.14.0.</p>
<h2>Modules and Pragmata</h2>
<h3>New Modules and Pragmata</h3>
<p> None</p>
<h3>Updated Modules and Pragmata</h3>
<dl>
<dt>&bull;</p>
<dd> PerlIO::scalar was updated to fix a bug in which opening a filehandle to a glob copy caused assertion failures (under debugging) or hangs or other erratic behaviour without debugging.</p>
<dt>&bull;</p>
<dd> ODBM_File and NDBM_File were updated to allow building on GNU/Hurd.</p>
<dt>&bull;</p>
<dd> IPC::Open3 has been updated to fix a regression introduced in perl 5.12, which broke <tt>&quot;IPC::Open3::open3($in, $out, $err, '-')&quot;</tt>. [perl #95748]</p>
<dt>&bull;</p>
<dd> Digest has been upgraded from version 1.16 to 1.16_01. </p>
<p> See &#8220;Security&#8221;.</p>
<dt>&bull;</p>
<dd> Module::CoreList has been updated to version 2.49_04 to add data for this release.</dl>
<h3>Removed Modules and Pragmata</h3>
<p> None</p>
<h2>Documentation</h2>
<h3>New Documentation</h3>
<p> None</p>
<h3>Changes to Existing Documentation</h3>
<p> <i>perlcheat</i></p>
<dl>
<dt>&bull;</p>
<dd> perlcheat was updated to 5.14.</dl>
<h2>Configuration and Compilation</h2>
<dl>
<dt>&bull;</p>
<dd> h2ph was updated to search correctly gcc include directories on platforms such as Debian with multi-architecture support.</p>
<dt>&bull;</p>
<dd> In Configure, the test for procselfexe was refactored into a loop.</dl>
<h2>Platform Support</h2>
<h3>New Platforms</h3>
<p> None</p>
<h3>Discontinued Platforms</h3>
<p> None</p>
<h3>Platform-Specific Notes</h3>
<dl>
<dt>FreeBSD</p>
<dd> The FreeBSD hints file was corrected to be compatible with FreeBSD 10.0.</p>
<dt>Solaris and NetBSD</p>
<dd> Configure was updated for &#8220;procselfexe&#8221; support on Solaris and NetBSD.</p>
<dt>HP-UX</p>
<dd> <font SIZE="-1">README</font>.hpux was updated to note the existence of a broken header in HP-UX 11.00.</p>
<dt>Linux</p>
<dd> libutil is no longer used when compiling on Linux platforms, which avoids warnings being emitted. </p>
<p> The system gcc (rather than any other gcc which might be in the compiling user&#8217;s path) is now used when searching for libraries such as <tt>&quot;-lm&quot;</tt>.</p>
<dt>Mac <font SIZE="-1">OS X</font></p>
<dd> The locale tests were updated to reflect the behaviour of locales in Mountain Lion.</p>
<dt>GNU/Hurd</p>
<dd> Various build and test fixes were included for GNU/Hurd. </p>
<p> <font SIZE="-1">LFS</font> support was enabled in GNU/Hurd.</p>
<dt>NetBSD</p>
<dd> The NetBSD hints file was corrected to be compatible with NetBSD 6.*</dl>
<h2>Bug Fixes</h2>
<dl>
<dt>&bull;</p>
<dd> A regression has been fixed that was introduced in 5.14, in <tt>&quot;/i&quot;</tt> regular expression matching, in which a match improperly fails if the pattern is in <font SIZE="-1">UTF-8,</font> the target string is not, and a Latin-1 character precedes a character in the string that should match the pattern. [perl #101710]</p>
<dt>&bull;</p>
<dd> In case-insensitive regular expression pattern matching, no longer on <font SIZE="-1">UTF-8</font> encoded strings does the scan for the start of match only look at the first possible position. This caused matches such as <tt>&quot;&quot;f
