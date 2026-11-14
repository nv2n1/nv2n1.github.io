---
title: "perl587delta(1)"
name: "perl587delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl587delta/"
description: "perl587delta – what is new for perl v5.8.7"
---

<h2 class="name">NAME</h2>
<p> perl587delta &#8211; what is new for perl v5.8.7 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.8.6 release and the 5.8.7 release.</p>
<h2>Incompatible Changes</h2>
<p> There are no changes incompatible with 5.8.6.</p>
<h2>Core Enhancements</h2>
<h3>Unicode Character Database 4.1.0</h3>
<p> The copy of the Unicode Character Database included in Perl 5.8 has been updated to 4.1.0 from 4.0.1. See &lt;<a rel="nofollow" href="http://www.unicode.org/versions/Unicode4.1.0/#NotableChanges">http://www.unicode.org/versions/Unicode4.1.0/#NotableChanges</a>&gt; for the notable changes.</p>
<h3>suidperl less insecure</h3>
<p> A pair of exploits in <tt>&quot;suidperl&quot;</tt> involving debugging code have been closed. </p>
<p> For new projects the core perl team strongly recommends that you use dedicated, single purpose security tools such as <tt>&quot;sudo&quot;</tt> in preference to <tt>&quot;suidperl&quot;</tt>.</p>
<h3>Optional site customization script</h3>
<p> The perl interpreter can be built to allow the use of a site customization script. By default this is not enabled, to be consistent with previous perl releases. To use this, add <tt>&quot;-Dusesitecustomize&quot;</tt> to the command line flags when running the <tt>&quot;Configure&quot;</tt> script. See also &#8220;-f&#8221; in perlrun.</p>
<h3>Config.pm is now much smaller.</h3>
<p> <tt>&quot;Config.pm&quot;</tt> is now about 3K rather than 32K, with the infrequently used code and <tt>%Config</tt> values loaded on demand. This is transparent to the programmer, but means that most code will save parsing and loading 29K of script (for example, code that uses <tt>&quot;File::Find&quot;</tt>).</p>
<h2>Modules and Pragmata</h2>
<dl>
<dt>&bull;</p>
<dd> B upgraded to version 1.09</p>
<dt>&bull;</p>
<dd> base upgraded to version 2.07</p>
<dt>&bull;</p>
<dd> bignum upgraded to version 0.17</p>
<dt>&bull;</p>
<dd> bytes upgraded to version 1.02</p>
<dt>&bull;</p>
<dd> Carp upgraded to version 1.04</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">CGI</font> upgraded to version 3.10</p>
<dt>&bull;</p>
<dd> Class::ISA upgraded to version 0.33</p>
<dt>&bull;</p>
<dd> Data::Dumper upgraded to version 2.121_02</p>
<dt>&bull;</p>
<dd> DB_File upgraded to version 1.811</p>
<dt>&bull;</p>
<dd> Devel::PPPort upgraded to version 3.06</p>
<dt>&bull;</p>
<dd> Digest upgraded to version 1.10</p>
<dt>&bull;</p>
<dd> Encode upgraded to version 2.10</p>
<dt>&bull;</p>
<dd> FileCache upgraded to version 1.05</p>
<dt>&bull;</p>
<dd> File::Path upgraded to version 1.07</p>
<dt>&bull;</p>
<dd> File::Temp upgraded to version 0.16</p>
<dt>&bull;</p>
<dd> IO::File upgraded to version 1.11</p>
<dt>&bull;</p>
<dd> IO::Socket upgraded to version 1.28</p>
<dt>&bull;</p>
<dd> Math::BigInt upgraded to version 1.77</p>
<dt>&bull;</p>
<dd> Math::BigRat upgraded to version 0.15</p>
<dt>&bull;</p>
<dd> overload upgraded to version 1.03</p>
<dt>&bull;</p>
<dd> PathTools upgraded to version 3.05</p>
<dt>&bull;</p>
<dd> Pod::HTML upgraded to version 1.0503</p>
<dt>&bull;</p>
<dd> Pod::Perldoc upgraded to version 3.14</p>
<dt>&bull;</p>
<dd> Pod::LaTeX upgraded to version 0.58</p>
<dt>&bull;</p>
<dd> Pod::Parser upgraded to version 1.30</p>
<dt>&bull;</p>
<dd> Symbol upgraded to version 1.06</p>
<dt>&bull;</p>
<dd> Term::ANSIColor upgraded to version 1.09</p>
<dt>&bull;</p>
<dd> Test::Harness upgraded to version 2.48</p>
<dt>&bull;</p>
<dd> Test::Simple upgraded to version 0.54</p>
<dt>&bull;</p>
<dd> Text::Wrap upgraded to version 2001.09293, to fix a bug when <code>wrap()</code> was called with a non-space separator.</p>
<dt>&bull;</p>
<dd> threads::shared upgraded to version 0.93</p>
<dt>&bull;</p>
<dd> Time::HiRes upgraded to version 1.66</p>
<dt>&bull;</p>
<dd> Time::Local upgraded to version 1.11</p>
<dt>&bull;</p>
<dd> Unicode::Normalize upgraded to version 0.32</p>
<dt>&bull;</p>
<dd> utf8 upgraded to version 1.05</p>
<dt>&bull;</p>
<dd> Win32 upgraded to version 0.24, which provides Win32::GetFileVersion</dl>
<h2>Utility Changes</h2>
<h3>find2perl enhancements</h3>
<p> <tt>&quot;find2perl&quot;</tt> has new options <tt>&quot;-iname&quot;</tt>, <tt>&quot;-path&quot;</tt> and <tt>&quot;-ipath&quot;</tt>.</p>
<h2>Performance Enhancements</h2>
<p> The internal pointer mapping hash used during ithreads cloning now uses an arena for memory allocation. In tests this reduced ithreads cloning time by about 10%.</p>
<h2>Installation and Configuration Improvements</h2>
<dl>
<dt>&bull;</p>
<dd> The Win32 &#8220;dmake&#8221; makefile.mk has been updated to make it compatible with the latest versions of dmake.</p>
<dt>&bull;</p>
<dd> <tt>&quot;PERL_MALLOC&quot;</tt>, <tt>&quot;DEBUG_MSTATS&quot;</tt>, <tt>&quot;PERL_HASH_SEED_EXPLICIT&quot;</tt> and <tt>&quot;NO_HASH_SEED&quot;</tt> should now work in Win32 makefiles.</dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</p>
<dd> The <code>socket()</code> function on Win32 has been fixed so that it is able to use transport providers which specify a protocol of 0 (meaning any protocol is allowed) once more. (This was broken in 5.8.6, and typically caused the use of <font SIZE="-1">ICMP</font> sockets to fail.)</p>
<dt>&bull;</p>
<dd> Another obscure bug involving <tt>&quot;substr&quot;</tt> and <font SIZE="-1">UTF-8</font> caused by bad internal offset caching has been identified and fixed.</p>
<dt>&bull;</p>
<dd> A bug involving the loading of <font SIZE="-1">UTF-8</font> tables by the regexp engine has been fixed &#8211; code such as <tt>&quot;&quot;
