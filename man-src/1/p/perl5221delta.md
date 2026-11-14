---
title: "perl5221delta(1)"
name: "perl5221delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5221delta/"
description: "perl5221delta – what is new for perl v5.22.1"
---

<h2 class="name">NAME</h2>
<p> perl5221delta &#8211; what is new for perl v5.22.1 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.22.0 release and the 5.22.1 release. </p>
<p> If you are upgrading from an earlier release such as 5.20.0, first read perl5220delta, which describes differences between 5.20.0 and 5.22.0.</p>
<h2>Incompatible Changes</h2>
<p> There are no changes intentionally incompatible with 5.20.0 other than the following single exception, which we deemed to be a sensible change to make in order to get the new <tt>&quot;{wb}&quot;</tt> and (in particular) <tt>&quot;{sb}&quot;</tt> features sane before people decided they&#8217;re worthless because of bugs in their Perl 5.22.0 implementation and avoided them in the future. If any others exist, they are bugs, and we request that you submit a report. See &#8220;Reporting Bugs&#8221; below.</p>
<h3>Bounds Checking Constructs</h3>
<p> Several bugs, including a segmentation fault, have been fixed with the bounds checking constructs (introduced in Perl 5.22) <tt>&quot;{gcb}&quot;</tt>, <tt>&quot;{sb}&quot;</tt>, <tt>&quot;{wb}&quot;</tt>, <tt>&quot;\B{gcb}&quot;</tt>, <tt>&quot;\B{sb}&quot;</tt>, and <tt>&quot;\B{wb}&quot;</tt>. All the <tt>&quot;\B{}&quot;</tt> ones now match an empty string; none of the <tt>&quot;{}&quot;</tt> ones do. [perl #126319] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126319">https://rt.perl.org/Ticket/Display.html?id=126319</a>&gt;</p>
<h2>Modules and Pragmata</h2>
<h3>Updated Modules and Pragmata</h3>
<dl>
<dt>&bull;</p>
<dd> Module::CoreList has been upgraded from version 5.20150520 to 5.20151213.</p>
<dt>&bull;</p>
<dd> PerlIO::scalar has been upgraded from version 0.22 to 0.23.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">POSIX</font> has been upgraded from version 1.53 to 1.53_01. </p>
<p> If <tt>&quot;POSIX::strerror&quot;</tt> was passed <tt>$!</tt> as its argument then it accidentally cleared <tt>$!</tt>. This has been fixed. [perl #126229] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126229">https://rt.perl.org/Ticket/Display.html?id=126229</a>&gt;</p>
<dt>&bull;</p>
<dd> Storable has been upgraded from version 2.53 to 2.53_01.</p>
<dt>&bull;</p>
<dd> warnings has been upgraded from version 1.32 to 1.34. </p>
<p> The <tt>&quot;warnings::enabled&quot;</tt> example now actually uses <tt>&quot;warnings::enabled&quot;</tt>. [perl #126051] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126051">https://rt.perl.org/Ticket/Display.html?id=126051</a>&gt;</p>
<dt>&bull;</p>
<dd> Win32 has been upgraded from version 0.51 to 0.52. </p>
<p> This has been updated for Windows 8.1, 10 and 2012 R2 Server.</dl>
<h2>Documentation</h2>
<h3>Changes to Existing Documentation</h3>
<p> <i>perltie</i></p>
<dl>
<dt>&bull;</p>
<dd> The usage of <tt>&quot;FIRSTKEY&quot;</tt> and <tt>&quot;NEXTKEY&quot;</tt> has been clarified.</dl>
<p> <i>perlvar</i></p>
<dl>
<dt>&bull;</p>
<dd> The specific true value of <tt>$!{E...}</tt> is now documented, noting that it is subject to change and not guaranteed.</dl>
<h2>Diagnostics</h2>
<p> The following additions or changes have been made to diagnostic output, including warnings and fatal error messages. For the complete list of diagnostic messages, see perldiag.</p>
<h3>Changes to Existing Diagnostics</h3>
<dl>
<dt>&bull;</p>
<dd> The <tt>&quot;printf&quot;</tt> and <tt>&quot;sprintf&quot;</tt> builtins are now more careful about the warnings they emit: argument reordering now disables the &#8220;redundant argument&#8221; warning in all cases. [perl #125469] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=125469">https://rt.perl.org/Ticket/Display.html?id=125469</a>&gt;</dl>
<h2>Configuration and Compilation</h2>
<dl>
<dt>&bull;</p>
<dd> Using the <tt>&quot;NO_HASH_SEED&quot;</tt> define in combination with the default hash algorithm <tt>&quot;PERL_HASH_FUNC_ONE_AT_A_TIME_HARD&quot;</tt> resulted in a fatal error while compiling the interpreter, since Perl 5.17.10. This has been fixed.</p>
<dt>&bull;</p>
<dd> Configuring with ccflags containing quotes (e.g. <tt>&quot;-Accflags='-DAPPLLIB_EXP=\&quot;/usr/libperl\&quot;'&quot;</tt>) was broken in Perl 5.22.0 but has now been fixed again. [perl #125314] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=125314">https://rt.perl.org/Ticket/Display.html?id=125314</a>&gt;</dl>
<h2>Platform Support</h2>
<h3>Platform-Specific Notes</h3>
<dl>
<dt><font SIZE="-1">IRIX</font></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Under some circumstances <font SIZE="-1">IRIX</font> stdio <code>fgetc()</code> and <code>fread()</code> set the errno to <tt>&quot;ENOENT&quot;</tt>, which made no sense according to either <font SIZE="-1">IRIX</font> or <font SIZE="-1">POSIX</font> docs. Errno is now cleared in such cases. [perl #123977] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123977">https://rt.perl.org/Ticket/Display.html?id=123977</a>&gt;</p>
<dt>&bull;</p>
<dd> Problems when multiplying long doubles by infinity have been fixed. [perl #126396] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126396">https://rt.perl.org/Ticket/Display.html?id=126396</a>&gt;</p>
<dt>&bull;</p>
<dd> All tests pass now on <font SIZE="-1">IRIX</font> with the default build configuration.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;qr/(?[ () ])/&quot;</tt> no longer segfaults, giving a syntax error message instead. [perl #125805] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=125805">https://rt.perl.org/Ticket/Display.html?id=125805</a>&gt;</p>
<dt>&bull;</p>
<dd> Regular expression possessive quantifier Perl 5.20 regression now fixed. <tt>&quot;qr/&quot;</tt><i></i><font SIZE="-1"><i>PAT</i></font><i></i><tt>&quot;{&quot;</tt><i>min</i>,<i>max</i><tt>&quot;}+&quot;</tt><tt>&quot;/&quot;</tt> is supposed to behave identically to <tt>&quot;qr/(?&gt;&quot;</tt><i></i><font SIZE="-1"><i>PAT</i></font><i></i><tt>&quot;{&quot;</tt><i>min</i>,<i>max</i><tt>&quot;})/&quot;</tt>. Since Perl 5.20, this didn&#8217;t work if <i>min</i> and <i>max</i> were equal. [perl #125825] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=125825">https://rt.perl.org/Ticket/Display.html?id=125825</a>&gt;</p>
<dt>&bull;</p>
<dd> Certain syntax errors in &#8220;Extended Bracketed Character Classes&#8221; in perlrecharclass caused panics instead of the proper error message. This has now been fixed. [perl #126481] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126481">https://rt.perl.org/Ticket/Display.html?id=126481</a>&gt;</p>
<dt>&bull;</p>
<dd> <tt>&quot;BEGIN &lt;&gt;&quot;</tt> no longer segfaults and properly produces an error message. [perl #125341] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=125341">https://rt.perl.org/Ticket/Display.html?id=125341</a>&gt;</p>
<dt>&bull;</p>
<dd> A regression from Perl 5.20 has been fixed, in which some syntax errors in <tt>&quot;(?[...])&quot;</tt> constructs within regular expression patterns could cause a segfault instead of a proper error message. [perl #126180] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126180">https://rt.perl.org/Ticket/Display.html?id=126180</a>&gt;</p>
<dt>&bull;</p>
<dd> Another problem with <tt>&quot;(?[...])&quot;</tt> constructs has been fixed wherein things like <tt>&quot;
