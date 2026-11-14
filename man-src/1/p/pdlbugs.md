---
title: "pdlbugs(1)"
name: "pdlbugs"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdlbugs/"
description: "PDL::Bugs – How to diagnose and report PDL problems"
---

<p>PDL::Bugs &#8211; How to diagnose and report PDL problems </p>
<h2>Version</h2>
<p>version 1.0000</p>
<h2>Description</h2>
<p>This module explains how to get help with a <font SIZE="-1">PDL</font> problem and how, when, and where to submit a bug report. In the future it may be extended to provide some sort of automated bug reporting capability.</p>
<h2>If You Have A Pdl Problem</h2>
<p>The primary resource for support for the Perl Data Language is via the <font SIZE="-1">PDL</font> mailing lists. The perldl list is for general use and discussions and is the one to use for questions about problems with <font SIZE="-1">PDL</font> or <font SIZE="-1">PDL</font> use for computation. This <i>is almost always</i> the list to post to for <font SIZE="-1">PDL</font> problems. </p>
<p> The pdl-porters list is <i>specifically</i> for <font SIZE="-1">PDL</font> development and often contains discussions of a rather technical nature relating to <font SIZE="-1">PDL</font> internals. This is <i>not</i> the list for general <font SIZE="-1">PDL</font> discussion or questions. </p>
<pre> <a rel="nofollow" href="http://pdl.perl.org/?page=mailing-lists">http://pdl.perl.org/?page=mailing-lists</a></pre>
<p><font SIZE="-1"><code>NOTE</code></font>: Both perldl and pdl-porters are read by the <font SIZE="-1">PDL</font> developers so you don&#8217;t save time or increase the probability of response by posting to pdl-porters or by cross-posting to pdl-porters. Please stick to perldl list posts unless you want to talk <font SIZE="-1">PDL</font> implementation and development. </p>
<p> <font SIZE="-1"><code>NOTE</code></font>: There is also a <font SIZE="-1">PDL IRC</font> channel which can be useful for immediate questions if populated. However, it has the big disadvantage of not being easily searched or routinely read by all <font SIZE="-1">PDL</font> developers and users. As a result, if you get an answer there, it may be incorrect or incomplete depending on who happens to be chatting at the time. It is definitely not readily searchable.</p>
<h2>Reporting Bugs</h2>
<p>Please submit bug reports via the sourceforge bug tracker interface at </p>
<pre> <a rel="nofollow" href="http://sourceforge.net/p/pdl/bugs/">http://sourceforge.net/p/pdl/bugs/</a></pre>
<p>where you can review the previously submitted bug reports. Click on <tt>&quot;Create Ticket&quot;</tt> to generate a bug report. If you do not already have a sourceforge.net account, you will need to get one to submit the report: </p>
<pre> <a rel="nofollow" href="http://sourceforge.net/account/registration/">http://sourceforge.net/account/registration/</a></pre>
<p>Please provide a way for the <font SIZE="-1">PDL</font> developers to contact you regarding the problem. </p>
<p> Try to include any information you think might help someone isolate, reproduce, and fix your problem. </p>
<p> At a <i>minimum</i>, include the following information:</p>
<dl>
<dt>&bull;</p>
<dd><font SIZE="-1">PDL</font> version number (e.g. <font SIZE="-1">PDL-2.007</font>)</p>
<dt>&bull;</p>
<dd>Perl version information. Output from <tt>&quot;perl -v&quot;</tt> or <tt>&quot;perl -V&quot;</tt> (even better!)</p>
<dt>&bull;</p>
<dd>Your operating System. You can run the <tt>&quot;uname -a&quot;</tt> command on many unix systems</p>
<dt>&bull;</p>
<dd>The full output of <tt>&quot;perldl -V&quot;</tt> </p>
<p> If you are reporting a bug with an already installed <font SIZE="-1">PDL. </font> If the <font SIZE="-1">PDL</font> has compiled and built but not been installed, you may run <tt>&quot;perl -Mblib perldl -V&quot;</tt> from the top level of the <font SIZE="-1">PDL</font> build directory.</p>
<dt>&bull;</p>
<dd>The bug description and how to reproduce it. </p>
<p> Short examples using the <font SIZE="-1">PDL</font> shells, <tt>&quot;pdl2&quot;</tt> or <tt>&quot;perldl&quot;</tt>, are excellent! Don&#8217;t forget to include needed input data (as small as possible) so that the code can be run with a cut and paste.</dl>
<p> Other things that are often helpful:</p>
<dl>
<dt>&bull;</p>
<dd>Details about your operating environment that might be related to the problem</p>
<dt>&bull;</p>
<dd>Exact cut and pasted error or warning messages</p>
<dt>&bull;</p>
<dd>The shortest, clearest code you can manage to write which reproduces the bug described.</p>
<dt>&bull;</p>
<dd>A patch against the latest released version of this distribution which fixes this bug.</dl>
<p> Alternatively, send an e-mail report with the above information (including the output of <tt>&quot;perldl -V&quot;</tt>) to <tt>&quot;pdl-porters [at] jach.hawaii.edu&quot;</tt>. See </p>
<pre> <a rel="nofollow" href="http://pdl.perl.org/?page=mailing-lists">http://pdl.perl.org/?page=mailing-lists</a></pre>
<p>for info on how to subscribe to this list.</p>
<h2>Before You Send A Report</h2>
<p><font SIZE="-1">BEFORE</font> you report a bug make sure you got the latest release version of <font SIZE="-1">PDL,</font> always available from <font SIZE="-1">CPAN,</font> check </p>
<pre> <a rel="nofollow" href="http://search.cpan.org/search?dist=PDL">http://search.cpan.org/search?dist=PDL</a></pre>
<p>Also, you can check the <font SIZE="-1">FAQ</font> at </p>
<pre> <a rel="nofollow" href="http://pdl.perl.org/?docs=FAQ">http://pdl.perl.org/?docs=FAQ</a>&amp;title=PDL::FAQ</pre>
<p>and the mailing list archives for hints. You can find links to the searchable archives at </p>
<pre> <a rel="nofollow" href="http://pdl.perl.org/?page=mailing-lists">http://pdl.perl.org/?page=mailing-lists</a></pre>
<p>and there is a Google enable search box on the top right of &lt;<a rel="nofollow" href="http://pdl.perl.org">http://pdl.perl.org</a>&gt; which usually gives the best results.</p>
<h2>Patches</h2>
<p>Patches can be sent to the pdl-porters mailing list (see above) or can be directly submitted to the patch manager </p>
<pre> <a rel="nofollow" href="http://sourceforge.net/p/pdl/patches/">http://sourceforge.net/p/pdl/patches/</a></pre>
<p>Patches should be made against the latest released <font SIZE="-1">PDL</font> or, ideally, against the current git sources which you can browse and check out at </p>
<pre> <a href="git://git.code.sf.net/p/pdl/code">git://git.code.sf.net/p/pdl/code</a></pre>
<p>Thanks, The pdl-porters team.</p>
