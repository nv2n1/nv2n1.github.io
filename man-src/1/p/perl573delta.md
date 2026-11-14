---
title: "perl573delta(1)"
name: "perl573delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl573delta/"
description: "perl573delta – what’s new for perl v5.7.3"
---

<h2 class="name">NAME</h2>
<p> perl573delta &#8211; what&#8217;s new for perl v5.7.3 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.7.2 release and the 5.7.3 release. </p>
<p> (To view the differences between the 5.6.0 release and the 5.7.0 release, see perl570delta. To view the differences between the 5.7.0 release and the 5.7.1 release, see perl571delta. To view the differences between the 5.7.1 release and the 5.7.2 release, see perl572delta.)</p>
<h2>Changes</h2>
<p> This is just a selected list of some of the more notable changes. The numbers refer to the Perl repository change numbers; see Changes58 (or Changes in Perl 5.8.1). In addition to these changes, lots of work took place in integrating threads, PerlIO, and Unicode; general code cleanup; and last but not least porting to non-Unix lands such as Win32, <font SIZE="-1">VMS</font>, Cygwin, <font SIZE="-1">DJGPP</font>, <font SIZE="-1">VOS</font>, MacOS Classic, and <font SIZE="-1">EBCDIC</font>.</p>
<dl>
<dt>11362</p>
<dd> add <font SIZE="-1">LC_MESSAGES</font> to <font SIZE="-1">POSIX</font> :locale_h export tag</p>
<dt>11371</p>
<dd> add <font SIZE="-1">DEL</font> to [:cntrl:]</p>
<dt>11375</p>
<dd> make h2ph understand constants like 1234L and 5678LL</p>
<dt>11405</p>
<dd> Win32: fix bugs in handling of the virtualized environment</p>
<dt>11410</p>
<dd> fix a bug in the security taint checking of <i>open()</i></p>
<dt>11423</p>
<dd> make perl <i>fork()</i> safe even on platforms that don&#8217;t have <i>pthread_atfork()</i></p>
<dt>11459</p>
<dd> make switching optimization and debugging levels during Perl builds easier via the <font SIZE="-1">OPTIMIZE</font> environment variable</p>
<dt>11475</p>
<dd> make <i>split()</i>&#8216;s unused captures to be undef, not &#8221;</p>
<dt>11485</p>
<dd> Search::Dict: allow transforming lines before comparing</p>
<dt>11490</p>
<dd> allow installing extra modules or bundles when building Perl</p>
<dt>11516</p>
<dd> add -Wall in cflags when compiling with gcc to weed out dubious C practices</p>
<dt>11541</p>
<dd> pluggable optimizer</p>
<dt>11549</p>
<dd> WinCE: integrate the port</p>
<dt>11589</p>
<dd> Win32: 4-arg select was broken</p>
<dt>11594</p>
<dd> introduce the perlivp utility for verifying the Perl installation (<font SIZE="-1">IVP</font> = Installation Verification Procedure)</p>
<dt>11623</p>
<dd> rename lib/unicode to lib/unicore to avoid case-insensitivity problems with lib/Unicode</p>
<dt>111631</p>
<dd> remove Time::Piece</p>
<dt>11643</p>
<dd> document that use utf8 is not the right way most of the time</p>
<dt>11656</p>
<dd> allow building perl with -DUSE_UTF8_SCRIPTS which makes <font SIZE="-1">UTF-8</font> the default script encoding (not the default since that would break all scripts having legacy eight-bit data in them)</p>
<dt>11725</p>
<dd> division preserving 64-bit integers</p>
<dt>11743</p>
<dd> document the coderef-in-@INC feature</p>
<dt>11794</p>
<dd> modulo (%) preserving 64-bit integers</p>
<dt>11825</p>
<dd> update to Unicode 3.1.1</p>
<dt>11865</p>
<dd> add the \[$@%&amp;*] prototype support</p>
<dt>11874</p>
<dd> <i>oct()</i> and <i>hex()</i> in glorious 64 bit</p>
<dt>11877</p>
<dd> Class::Struct: allow recursive classes</p>
<dt>11993</p>
<dd> fix unpack U to be the reverse of pack U</p>
<dt>12056</p>
<dd> <font SIZE="-1">VMS:</font> waitpid enhancements</p>
<dt>12180</p>
<dd> unpack(&#8220;Z*Z*&#8221;, pack(&#8220;Z*Z*&#8221;, ..)) was broken</p>
<dt>12243</p>
<dd> Devel::Peek: display <font SIZE="-1">UTF-8</font> SVs also as 
