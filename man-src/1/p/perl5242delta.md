---
title: "perl5242delta(1)"
name: "perl5242delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5242delta/"
---

<h2 class="name">NAME</h2>
 

 perl5242delta - what is new for perl v5.24.2 

<h2>DESCRIPTION</h2>

 This document describes differences between the 5.24.1 release and the 5.24.2 release. 

 If you are upgrading from an earlier release such as 5.24.0, first read perl5241delta, which describes differences between 5.24.0 and 5.24.1.

<h2>Security</h2>

<h3>Improved handling of '.' in @INC in base.pm</h3>

 The handling of (the removal of) <tt>'.'</tt> in <tt>@INC</tt> in base has been improved. This resolves some problematic behaviour in the approach taken in Perl 5.24.1, which is probably best described in the following two threads on the Perl 5 Porters mailing list: &lt;<a rel="nofollow" HREF="http://www.nntp.perl.org/group/perl.perl5.porters/2016/08/msg238991.html">http://www.nntp.perl.org/group/perl.perl5.porters/2016/08/msg238991.html</a>&gt;, &lt;<a rel="nofollow" HREF="http://www.nntp.perl.org/group/perl.perl5.porters/2016/10/msg240297.html">http://www.nntp.perl.org/group/perl.perl5.porters/2016/10/msg240297.html</a>&gt;.

<h3>Escaped colons and relative paths in <font SIZE="-1">PATH</font></h3>

 On Unix systems, Perl treats any relative paths in the <font SIZE="-1">PATH</font> environment variable as tainted when starting a new process. Previously, it was allowing a backslash to escape a colon (unlike the <font SIZE="-1">OS</font>), consequently allowing relative paths to be considered safe if the <font SIZE="-1">PATH</font> was set to something like <tt>&quot;/\:.&quot;</tt>. The check has been fixed to treat <tt>&quot;.&quot;</tt> as tainted in that example.

<h2>Modules and Pragmata</h2>

<h3>Updated Modules and Pragmata</h3>

<dl>
<dt>&bull;
<dd> base has been upgraded from version 2.23 to 2.23_01.
<dt>&bull;
<dd> Module::CoreList has been upgraded from version 5.20170114_24 to 5.20170715_24.</dl>

<h2>Selected Bug Fixes</h2>

<dl>
<dt>&bull;
<dd> Fixed a crash with <tt>&quot;s///l&quot;</tt> where it thought it was dealing with <font SIZE="-1">UTF-8</font> when it wasn't. [perl #129038] &lt;<a rel="nofollow" HREF="https://rt.perl.org/Ticket/Display.html?id=129038">https://rt.perl.org/Ticket/Display.html?id=129038</a>&gt;</dl>

<h2>Acknowledgements</h2>

 Perl 5.24.2 represents approximately 6 months of development since Perl 5.24.1 and contains approximately 2,500 lines of changes across 53 files from 18 authors. 

 Excluding auto-generated files, documentation and release tools, there were approximately 960 lines of changes to 17 .pm, .t, .c and .h files. 

 Perl continues to flourish into its third decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.24.2: 

 Aaron Crane, Abigail, Aristotle Pagaltzis, Chris 'BinGOs' Williams, Dan Collins, David Mitchell, Eric Herman, Father Chrysostomos, James E Keenan, Karl Williamson, Lukas Mai, Renee Baecker, Ricardo Signes, Sawyer X, Stevan Little, Steve Hay, Tony Cook, Yves Orton. 

 The list above is almost certainly incomplete as it is automatically generated from version control history. In particular, it does not include the names of the (very much appreciated) contributors who reported issues to the Perl bug tracker. 

 Many of the changes included in this version originated in the <font SIZE="-1">CPAN</font> modules included in Perl's core. We're grateful to the entire <font SIZE="-1">CPAN</font> community for helping Perl to flourish. 

 For a more complete list of all of Perl's historical contributors, please see the <i></i><font SIZE="-1"><i>AUTHORS</i></font><i></i> file in the Perl source distribution.

<h2>Reporting Bugs</h2>

 If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at &lt;<a rel="nofollow" HREF="https://rt.perl.org/">https://rt.perl.org/</a>&gt; . There may also be information at &lt;<a rel="nofollow" HREF="http://www.perl.org/">http://www.perl.org/</a>&gt; , the Perl Home Page. 

 If you believe you have an unreported bug, please run the perlbug program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. 

 If the bug you are reporting has security implications which make it inappropriate to send to a publicly archived mailing list, then see ``<font SIZE="-1">SECURITY VULNERABILITY CONTACT INFORMATION''</font> in perlsec for details of how to report the issue.

<h2>SEE ALSO</h2>

 The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. 

 The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. 

 The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. 

 The <i>Artistic</i> and <i>Copying</i> files for copyright information. 

<h2>Index</h2>



<dt><a HREF="#lbAG">Modules and Pragmata</a>
<dd>


<dt><a HREF="#lbAI">Selected Bug Fixes</a>
<dd>
<dt><a HREF="#lbAJ">Acknowledgements</a>
<dd>
<dt><a HREF="#lbAK">Reporting Bugs</a>
<dd>
<dt><a HREF="#lbAL">SEE ALSO</a>
<dd></dl>
