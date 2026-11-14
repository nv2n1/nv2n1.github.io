---
title: "perl561delta(1)"
name: "perl561delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl561delta/"
description: "perl561delta – what’s new for perl v5.6.1"
---

<h2 class="name">NAME</h2>
<p> perl561delta &#8211; what&#8217;s new for perl v5.6.1 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.005 release and the 5.6.1 release.</p>
<h2>Summary of changes between 5.6.0 and 5.6.1</h2>
<p> This section contains a summary of the changes between the 5.6.0 release and the 5.6.1 release. More details about the changes mentioned here may be found in the <i>Changes</i> files that accompany the Perl source distribution. See perlhack for pointers to online resources where you can inspect the individual patches described by these changes.</p>
<h3>Security Issues</h3>
<p> suidperl will not run /bin/mail anymore, because some platforms have a /bin/mail that is vulnerable to buffer overflow attacks. </p>
<p> Note that suidperl is neither built nor installed by default in any recent version of perl. Use of suidperl is highly discouraged. If you think you need it, try alternatives such as sudo first. See <a rel="nofollow" href="http://www.courtesan.com/sudo/">http://www.courtesan.com/sudo/</a> .</p>
<h3>Core bug fixes</h3>
<p> This is not an exhaustive list. It is intended to cover only the significant user-visible changes.</p>
<dl>
<dt>&quot;UNIVERSAL::isa()&quot;</p>
<dd> A bug in the caching mechanism used by <tt>&quot;UNIVERSAL::isa()&quot;</tt> that affected base.pm has been fixed. The bug has existed since the 5.005 releases, but wasn&#8217;t tickled by base.pm in those releases.</p>
<dt>Memory leaks</p>
<dd> Various cases of memory leaks and attempts to access uninitialized memory have been cured. See &#8220;Known Problems&#8221; below for further issues.</p>
<dt>Numeric conversions</p>
<dd> Numeric conversions did not recognize changes in the string value properly in certain circumstances. </p>
<p> In other situations, large unsigned numbers (those above 2**31) could sometimes lose their unsignedness, causing bogus results in arithmetic operations. </p>
<p> Integer modulus on large unsigned integers sometimes returned incorrect values. </p>
<p> Perl 5.6.0 generated &#8220;not a number&#8221; warnings on certain conversions where previous versions didn&#8217;t. </p>
<p> These problems have all been rectified. </p>
<p> Infinity is now recognized as a number.</p>
<dt>qw(a\b)</p>
<dd> In Perl 5.6.0, qw(a\b) produced a string with two backslashes instead of one, in a departure from the behavior in previous versions. The older behavior has been reinstated.</p>
<dt><code>caller()</code></p>
<dd> <code>caller()</code> could cause core dumps in certain situations. Carp was sometimes affected by this problem.</p>
<dt>Bugs in regular expressions</p>
<dd> Pattern matches on overloaded values are now handled correctly. </p>
<p> Perl 5.6.0 parsed m/
