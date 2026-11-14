---
title: "perl583delta(1)"
name: "perl583delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl583delta/"
description: "perl583delta – what is new for perl v5.8.3"
---

<h2 class="name">NAME</h2>
<p> perl583delta &#8211; what is new for perl v5.8.3 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.8.2 release and the 5.8.3 release. </p>
<p> If you are upgrading from an earlier release such as 5.6.1, first read the perl58delta, which describes differences between 5.6.0 and 5.8.0, and the perl581delta and perl582delta, which describe differences between 5.8.0, 5.8.1 and 5.8.2</p>
<h2>Incompatible Changes</h2>
<p> There are no changes incompatible with 5.8.2.</p>
<h2>Core Enhancements</h2>
<p> A <tt>&quot;SCALAR&quot;</tt> method is now available for tied hashes. This is called when a tied hash is used in scalar context, such as </p>
<pre>
    if (%tied_hash) {
        ...
    }
</pre>
<p> The old behaviour was that <tt>%tied_hash</tt> would return whatever would have been returned for that hash before the hash was tied (so usually 0). The new behaviour in the absence of a <font SIZE="-1">SCALAR</font> method is to return <font SIZE="-1">TRUE</font> if in the middle of an <tt>&quot;each&quot;</tt> iteration, and otherwise call <font SIZE="-1">FIRSTKEY</font> to check if the hash is empty (making sure that a subsequent <tt>&quot;each&quot;</tt> will also begin by calling <font SIZE="-1">FIRSTKEY</font>). Please see &#8220;<font SIZE="-1">SCALAR&#8221;</font> in perltie for the full details and caveats.</p>
<h2>Modules and Pragmata</h2>
<dl>
<dt><font SIZE="-1">CGI</font></p>
<dd>
<dt>Cwd</p>
<dd>
<dt>Digest</p>
<dd>
<dt>Digest::MD5</p>
<dd>
<dt>Encode</p>
<dd>
<dt>File::Spec</p>
<dd>
<dt>FindBin</p>
<dd> A function <tt>&quot;again&quot;</tt> is provided to resolve problems where modules in different directories wish to use FindBin.</p>
<dt>List::Util</p>
<dd> You can now weaken references to read only values.</p>
<dt>Math::BigInt</p>
<dd>
<dt>PodParser</p>
<dd>
<dt>Pod::Perldoc</p>
<dd>
<dt><font SIZE="-1">POSIX</font></p>
<dd>
<dt>Unicode::Collate</p>
<dd>
<dt>Unicode::Normalize</p>
<dd>
<dt>Test::Harness</p>
<dd>
<dt>threads::shared</p>
<dd> <tt>&quot;cond_wait&quot;</tt> has a new two argument form. <tt>&quot;cond_timedwait&quot;</tt> has been added.</dl>
<h2>Utility Changes</h2>
<p> <tt>&quot;find2perl&quot;</tt> now assumes <tt>&quot;-print&quot;</tt> as a default action. Previously, it needed to be specified explicitly. </p>
<p> A new utility, <tt>&quot;prove&quot;</tt>, makes it easy to run an individual regression test at the command line. <tt>&quot;prove&quot;</tt> is part of Test::Harness, which users of earlier Perl versions can install from <font SIZE="-1">CPAN.</font></p>
<h2>New Documentation</h2>
<p> The documentation has been revised in places to produce more standard manpages. </p>
<p> The documentation for the special code blocks (<font SIZE="-1">BEGIN, CHECK, INIT, END</font>) has been improved.</p>
<h2>Installation and Configuration Improvements</h2>
<p> Perl now builds on OpenVMS I64</p>
<h2>Selected Bug Fixes</h2>
<p> Using <code>substr()</code> on a <font SIZE="-1">UTF8</font> string could cause subsequent accesses on that string to return garbage. This was due to incorrect <font SIZE="-1">UTF8</font> offsets being cached, and is now fixed. </p>
<p> <code>join()</code> could return garbage when the same <code>join()</code> statement was used to process 8 bit data having earlier processed <font SIZE="-1">UTF8</font> data, due to the flags on that statement&#8217;s temporary workspace not being reset correctly. This is now fixed. </p>
<p> <tt>&quot;$a .. $b&quot;</tt> will now work as expected when either <tt>$a</tt> or <tt>$b</tt> is <tt>&quot;undef&quot;</tt> </p>
<p> Using Unicode keys with tied hashes should now work correctly. </p>
<p> Reading $^E now preserves $!. Previously, the C code implementing $^E did not preserve <tt>&quot;errno&quot;</tt>, so reading $^E could cause <tt>&quot;errno&quot;</tt> and therefore <tt>$!</tt> to change unexpectedly. </p>
<p> Reentrant functions will (once more) work with C<font SIZE="-2">++</font>. 5.8.2 introduced a bugfix which accidentally broke the compilation of Perl extensions written in C<font SIZE="-2">++</font></p>
<h2>New or Changed Diagnostics</h2>
<p> The fatal error &#8220;<font SIZE="-1">DESTROY</font> created new reference to dead object&#8221; is now documented in perldiag.</p>
<h2>Changed Internals</h2>
<p> The hash code has been refactored to reduce source duplication. The external interface is unchanged, and aside from the bug fixes described above, there should be no change in behaviour. </p>
<p> <tt>&quot;hv_clear_placeholders&quot;</tt> is now part of the perl <font SIZE="-1">API</font> </p>
<p> Some C macros have been tidied. In particular macros which create temporary local variables now name these variables more defensively, which should avoid bugs where names clash. </p>
<p> &lt;signal.h&gt; is now always included.</p>
<h2>Configuration and Building</h2>
<p> <tt>&quot;Configure&quot;</tt> now invokes callbacks regardless of the value of the variable they are called for. Previously callbacks were only invoked in the <tt>&quot;case $variable $define)&quot;</tt> branch. This change should only affect platform maintainers writing configuration hints files.</p>
<h2>Platform Specific Problems</h2>
<p> The regression test ext/threads/shared/t/wait.t fails on early RedHat 9 and HP-UX 10.20 due to bugs in their threading implementations. RedHat users should see <a rel="nofollow" href="https://rhn.redhat.com/errata/RHBA-2003-136.html">https://rhn.redhat.com/errata/RHBA-2003-136.html</a> and consider upgrading their glibc.</p>
<h2>Known Problems</h2>
<p> Detached threads aren&#8217;t supported on Windows yet, as they may lead to memory access violation problems. </p>
<p> There is a known race condition opening scripts in <tt>&quot;suidperl&quot;</tt>. <tt>&quot;suidperl&quot;</tt> is neither built nor installed by default, and has been deprecated since perl 5.8.0. You are advised to replace use of suidperl with tools such as sudo ( <a rel="nofollow" href="http://www.courtesan.com/sudo/">http://www.courtesan.com/sudo/</a> ) </p>
<p> We have a backlog of unresolved bugs. Dealing with bugs and bug reports is unglamorous work; not something ideally suited to volunteer labour, but that is all that we have. </p>
<p> The perl5 development team are implementing changes to help address this problem, which should go live in early 2004.</p>
<h2>Future Directions</h2>
<p> Code freeze for the next maintenance release (5.8.4) is on March 31st 2004, with release expected by mid April. Similarly 5.8.5&#8217;s freeze will be at the end of June, with release by mid July.</p>
<h2>Obituary</h2>
<p> Iain &#8216;Spoon&#8217; Truskett, Perl hacker, author of perlreref and contributor to <font SIZE="-1">CPAN,</font> died suddenly on 29th December 2003, aged 24. He will be missed.</p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://bugs.perl.org.">http://bugs.perl.org.</a> There may also be information at <a rel="nofollow" href="http://www.perl.org,">http://www.perl.org,</a> the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. You can browse and search the Perl 5 bugs at <a rel="nofollow" href="http://bugs.perl.org/">http://bugs.perl.org/</a></p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
<h2>Index</h2>
