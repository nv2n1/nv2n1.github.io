---

title: "perl573delta(1)"
name: "perl573delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl573delta/"
description: "perl573delta – what’s new for perl v5.7.3"
---

<p> perl573delta - what&#8217;s new for perl v5.7.3 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.7.2 release and the 5.7.3 release. </p>
<p> (To view the differences between the 5.6.0 release and the 5.7.0 release, see perl570delta. To view the differences between the 5.7.0 release and the 5.7.1 release, see perl571delta. To view the differences between the 5.7.1 release and the 5.7.2 release, see perl572delta.)  </p>
<h2>Changes</h2>
<p> This is just a selected list of some of the more notable changes. The numbers refer to the Perl repository change numbers; see Changes58 (or Changes in Perl 5.8.1). In addition to these changes, lots of work took place in integrating threads, PerlIO, and Unicode; general code cleanup; and last but not least porting to non-Unix lands such as Win32, <font SIZE="-1">VMS</font>, Cygwin, <font SIZE="-1">DJGPP</font>, <font SIZE="-1">VOS</font>, MacOS Classic, and <font SIZE="-1">EBCDIC</font>. </p>
<dl>
<dt>11362</dt>
<dd> <p> add <font SIZE="-1">LC_MESSAGES</font> to <font SIZE="-1">POSIX</font> :locale_h export tag </p>
 </dd>
<dt>11371</dt>
<dd> <p> add <font SIZE="-1">DEL</font> to [:cntrl:] </p>
 </dd>
<dt>11375</dt>
<dd> <p> make h2ph understand constants like 1234L and 5678LL </p>
 </dd>
<dt>11405</dt>
<dd> <p> Win32: fix bugs in handling of the virtualized environment </p>
 </dd>
<dt>11410</dt>
<dd> <p> fix a bug in the security taint checking of <i>open()</i> </p>
 </dd>
<dt>11423</dt>
<dd> <p> make perl <i>fork()</i> safe even on platforms that don&#8217;t have <i>pthread_atfork()</i> </p>
 </dd>
<dt>11459</dt>
<dd> <p> make switching optimization and debugging levels during Perl builds easier via the <font SIZE="-1">OPTIMIZE</font> environment variable </p>
 </dd>
<dt>11475</dt>
<dd> <p> make <i>split()</i>&#8216;s unused captures to be undef, not &#8216;&#8216; </p>
 </dd>
<dt>11485</dt>
<dd> <p> Search::Dict: allow transforming lines before comparing </p>
 </dd>
<dt>11490</dt>
<dd> <p> allow installing extra modules or bundles when building Perl </p>
 </dd>
<dt>11516</dt>
<dd> <p> add -Wall in cflags when compiling with gcc to weed out dubious C practices </p>
 </dd>
<dt>11541</dt>
<dd> <p> pluggable optimizer </p>
 </dd>
<dt>11549</dt>
<dd> <p> WinCE: integrate the port </p>
 </dd>
<dt>11589</dt>
<dd> <p> Win32: 4-arg select was broken </p>
 </dd>
<dt>11594</dt>
<dd> <p> introduce the perlivp utility for verifying the Perl installation (<font SIZE="-1">IVP</font> = Installation Verification Procedure) </p>
 </dd>
<dt>11623</dt>
<dd> <p> rename lib/unicode to lib/unicore to avoid case-insensitivity problems with lib/Unicode </p>
 </dd>
<dt>111631</dt>
<dd> <p> remove Time::Piece </p>
 </dd>
<dt>11643</dt>
<dd> <p> document that use utf8 is not the right way most of the time </p>
 </dd>
<dt>11656</dt>
<dd> <p> allow building perl with -DUSE_UTF8_SCRIPTS which makes <font SIZE="-1">UTF-8</font> the default script encoding (not the default since that would break all scripts having legacy eight-bit data in them) </p>
 </dd>
<dt>11725</dt>
<dd> <p> division preserving 64-bit integers </p>
 </dd>
<dt>11743</dt>
<dd> <p> document the coderef-in-@INC feature </p>
 </dd>
<dt>11794</dt>
<dd> <p> modulo (%) preserving 64-bit integers </p>
 </dd>
<dt>11825</dt>
<dd> <p> update to Unicode 3.1.1 </p>
 </dd>
<dt>11865</dt>
<dd> <p> add the \[$@%&amp;*] prototype support </p>
 </dd>
<dt>11874</dt>
<dd> <p> <i>oct()</i> and <i>hex()</i> in glorious 64 bit </p>
 </dd>
<dt>11877</dt>
<dd> <p> Class::Struct: allow recursive classes </p>
 </dd>
<dt>11993</dt>
<dd> <p> fix unpack U to be the reverse of pack U </p>
 </dd>
<dt>12056</dt>
<dd> <p> <font SIZE="-1">VMS:</font> waitpid enhancements </p>
 </dd>
<dt>12180</dt>
<dd> <p> unpack(``Z*Z*&#8216;&#8216;, pack(``Z*Z*&#8216;&#8216;, ..)) was broken </p>
 </dd>
<dt>12243</dt>
<dd> <p> Devel::Peek: display <font SIZE="-1">UTF-8</font> SVs also as \x{...} </p>
 </dd>
<dt>12288</dt>
<dd> <p> Data::Dumper: option to sort hashes </p>
 </dd>
<dt>12542</dt>
<dd> <p> add perlpodspec </p>
 </dd>
<dt>12652</dt>
<dd> <p> threadsafe DynaLoader, re, Opcode, File::Glob, and B </p>
 </dd>
<dt>12756</dt>
<dd> <p> support BeOS better </p>
 </dd>
<dt>12874</dt>
<dd> <p> read-only hashes (user-level interface is Hash::Util) </p>
 </dd>
<dt>13162</dt>
<dd> <p> add Devel::PPPort </p>
 </dd>
<dt>13179</dt>
<dd> <p> add the sort pragma </p>
 </dd>
<dt>13326</dt>
<dd> <p> <font SIZE="-1">VMS:</font> fix perl -P </p>
 </dd>
<dt>13358</dt>
<dd> <p> add perlpacktut </p>
 </dd>
<dt>13452</dt>
<dd> <p> SUPER-UX: add hints file </p>
 </dd>
<dt>13575</dt>
<dd> <p> Win32: non-blocking waitpid(-1,WNOHANG) </p>
 </dd>
<dt>13684</dt>
<dd> <p> introduce the -t option for gentler taint checking </p>
 </dd>
<dt>14694</dt>
<dd> <p> add the if pragma </p>
 </dd>
<dt>14832</dt>
<dd> <p> implement IV/UV/NV/long double un/packing with j/J/F/D </p>
 </dd>
<dt>14854</dt>
<dd> <p> document the new taint behaviour of exec <font SIZE="-1">LIST</font> and system <font SIZE="-1">LIST</font> </p>
 </dd></dl>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://bugs.perl.org.">http://bugs.perl.org.</a> There may also be information at <a rel="nofollow" href="http://www.perl.com/,">http://www.perl.com/,</a> the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <code>&quot;perl -V&quot;</code>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team.  </p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information.  </p>
<h2>HISTORY</h2>
<p> Written by Jarkko Hietaniemi &lt;<i>jhi [at] iki.fi</i>&gt;, with many contributions from The Perl Porters and Perl Users submitting feedback and patches. </p>
<p> Send omissions or corrections to &lt;<i>perlbug [at] perl.org</i>&gt;. </p>
