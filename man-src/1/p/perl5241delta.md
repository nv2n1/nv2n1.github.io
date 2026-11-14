---
title: "perl5241delta(1)"
name: "perl5241delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5241delta/"
description: "perl5241delta – what is new for perl v5.24.1"
---

<h2 class="name">NAME</h2>
<p> perl5241delta &#8211; what is new for perl v5.24.1 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.24.0 release and the 5.24.1 release. </p>
<p> If you are upgrading from an earlier release such as 5.22.0, first read perl5240delta, which describes differences between 5.22.0 and 5.24.0.</p>
<h2>Security</h2>
<h3><code>-Di</code> switch is now required for PerlIO debugging output</h3>
<p> Previously PerlIO debugging output would be sent to the file specified by the <tt>&quot;PERLIO_DEBUG&quot;</tt> environment variable if perl wasn&#8217;t running setuid and the <code>-T</code> or <code>-t</code> switches hadn&#8217;t been parsed yet. </p>
<p> If perl performed output at a point where it hadn&#8217;t yet parsed its switches this could result in perl creating or overwriting the file named by <tt>&quot;PERLIO_DEBUG&quot;</tt> even when the <code>-T</code> switch had been supplied. </p>
<p> Perl now requires the <code>-Di</code> switch to produce PerlIO debugging output. By default this is written to <tt>&quot;stderr&quot;</tt>, but can optionally be redirected to a file by setting the <tt>&quot;PERLIO_DEBUG&quot;</tt> environment variable. </p>
<p> If perl is running setuid or the <code>-T</code> switch was supplied <tt>&quot;PERLIO_DEBUG&quot;</tt> is ignored and the debugging output is sent to <tt>&quot;stderr&quot;</tt> as for any other <code>-D</code> switch.</p>
<h3>Core modules and tools no longer search <i>.</i> for optional modules</h3>
<p> The tools and many modules supplied in core no longer search the default current directory entry in <tt>@INC</tt> for optional modules. For example, Storable will remove the final <i>&#8220;.&#8221;</i> from <tt>@INC</tt> before trying to load Log::Agent. </p>
<p> This prevents an attacker injecting an optional module into a process run by another user where the current directory is writable by the attacker, e.g. the <i>/tmp</i> directory. </p>
<p> In most cases this removal should not cause problems, but difficulties were encountered with base, which treats every module name supplied as optional. These difficulties have not yet been resolved, so for this release there are no changes to base. We hope to have a fix for base in Perl 5.24.2. </p>
<p> To protect your own code from this attack, either remove the default <i>&#8220;.&#8221;</i> entry from <tt>@INC</tt> at the start of your script, so: </p>
<pre>
  #!/usr/bin/perl
  use strict;
  ...
</pre>
<p> becomes: </p>
<pre><code>
#!/ usr / bin / perl
BEGIN
{
    pop @INC if $INC[-1] eq '.'
}
use strict;
...
</code></pre>
<p> or for modules, remove <i>&#8220;.&#8221;</i> from a localized <tt>@INC</tt>, so: </p>
<pre>
  my $can_foo = eval { require Foo; }
</pre>
<p> becomes: </p>
<pre><code>
my $can_foo = eval
{
    local @INC = @INC;
    pop @INC if $INC[-1] eq '.';
    require Foo;
};
</code></pre>
<h2>Incompatible Changes</h2>
<p> Other than the security changes above there are no changes intentionally incompatible with Perl 5.24.0. If any exist, they are bugs, and we request that you submit a report. See &#8220;Reporting Bugs&#8221; below.</p>
<h2>Modules and Pragmata</h2>
<h3>Updated Modules and Pragmata</h3>
<dl>
<dt>&bull;</p>
<dd> Archive::Tar has been upgraded from version 2.04 to 2.04_01.</p>
<dt>&bull;</p>
<dd> bignum has been upgraded from version 0.42 to 0.42_01.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">CPAN</font> has been upgraded from version 2.11 to 2.11_01.</p>
<dt>&bull;</p>
<dd> Digest has been upgraded from version 1.17 to 1.17_01.</p>
<dt>&bull;</p>
<dd> Digest::SHA has been upgraded from version 5.95 to 5.95_01.</p>
<dt>&bull;</p>
<dd> Encode has been upgraded from version 2.80 to 2.80_01.</p>
<dt>&bull;</p>
<dd> ExtUtils::MakeMaker has been upgraded from version 7.10_01 to 7.10_02.</p>
<dt>&bull;</p>
<dd> File::Fetch has been upgraded from version 0.48 to 0.48_01.</p>
<dt>&bull;</p>
<dd> File::Spec has been upgraded from version 3.63 to 3.63_01.</p>
<dt>&bull;</p>
<dd> HTTP::Tiny has been upgraded from version 0.056 to 0.056_001.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">IO</font> has been upgraded from version 1.36 to 1.36_01.</p>
<dt>&bull;</p>
<dd> The IO-Compress modules have been upgraded from version 2.069 to 2.069_001.</p>
<dt>&bull;</p>
<dd> IPC::Cmd has been upgraded from version 0.92 to 0.92_01.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">JSON::PP</font> has been upgraded from version 2.27300 to 2.27300_01.</p>
<dt>&bull;</p>
<dd> Locale::Maketext has been upgraded from version 1.26 to 1.26_01.</p>
<dt>&bull;</p>
<dd> Locale::Maketext::Simple has been upgraded from version 0.21 to 0.21_01.</p>
<dt>&bull;</p>
<dd> Memoize has been upgraded from version 1.03 to 1.03_01.</p>
<dt>&bull;</p>
<dd> Module::CoreList has been upgraded from version 5.20160506 to 5.20170114_24.</p>
<dt>&bull;</p>
<dd> Net::Ping has been upgraded from version 2.43 to 2.43_01.</p>
<dt>&bull;</p>
<dd> Parse::CPAN::Meta has been upgraded from version 1.4417 to 1.4417_001.</p>
<dt>&bull;</p>
<dd> Pod::Html has been upgraded from version 1.22 to 1.2201.</p>
<dt>&bull;</p>
<dd> Pod::Perldoc has been upgraded from version 3.25_02 to 3.25_03.</p>
<dt>&bull;</p>
<dd> Storable has been upgraded from version 2.56 to 2.56_01.</p>
<dt>&bull;</p>
<dd> Sys::Syslog has been upgraded from version 0.33 to 0.33_01.</p>
<dt>&bull;</p>
<dd> Test has been upgraded from version 1.28 to 1.28_01.</p>
<dt>&bull;</p>
<dd> Test::Harness has been upgraded from version 3.36 to 3.36_01.</p>
<dt>&bull;</p>
<dd> XSLoader has been upgraded from version 0.21 to 0.22, fixing a security hole in which binary files could be loaded from a path outside of <tt>@INC</tt>. [perl #128528] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128528">https://rt.perl.org/Public/Bug/Display.html?id=128528</a>&gt;</dl>
<h2>Documentation</h2>
<h3>Changes to Existing Documentation</h3>
<p> <i>perlapio</i></p>
<dl>
<dt>&bull;</p>
<dd> The documentation of <tt>&quot;PERLIO_DEBUG&quot;</tt> has been updated.</dl>
<p> <i>perlrun</i></p>
<dl>
<dt>&bull;</p>
<dd> The new <code>-Di</code> switch has been documented, and the documentation of <tt>&quot;PERLIO_DEBUG&quot;</tt> has been updated.</dl>
<h2>Testing</h2>
<dl>
<dt>&bull;</p>
<dd> A new test script, <i>t/run/switchDx.t</i>, has been added to test that the new <code>-Di</code> switch is working correctly.</dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</p>
<dd> The change to hashbang redirection introduced in Perl 5.24.0, whereby perl would redirect to another interpreter (Perl 6) if it found a hashbang path which contains &#8220;perl&#8221; followed by &#8220;6&#8221;, has been reverted because it broke in cases such as <tt>&quot;#!/opt/perl64/bin/perl&quot;</tt>.</dl>
<h2>Acknowledgements</h2>
<p> Perl 5.24.1 represents approximately 8 months of development since Perl 5.24.0 and contains approximately 8,100 lines of changes across 240 files from 18 authors. </p>
<p> Excluding auto-generated files, documentation and release tools, there were approximately 2,200 lines of changes to 170 .pm, .t, .c and .h files. </p>
<p> Perl continues to flourish into its third decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.24.1: </p>
<p> Aaron Crane, Alex Vandiver, Aristotle Pagaltzis, Chad Granum, Chris &#8216;BinGOs&#8217; Williams, Craig A. Berry, Father Chrysostomos, James E Keenan, Jarkko Hietaniemi, Karen Etheridge, Leon Timmermans, Matthew Horsfall, Ricardo Signes, Sawyer X, Sébastien Aperghis-Tramoni, Stevan Little, Steve Hay, Tony Cook. </p>
<p> The list above is almost certainly incomplete as it is automatically generated from version control history. In particular, it does not include the names of the (very much appreciated) contributors who reported issues to the Perl bug tracker. </p>
<p> Many of the changes included in this version originated in the <font SIZE="-1">CPAN</font> modules included in Perl&#8217;s core. We&#8217;re grateful to the entire <font SIZE="-1">CPAN</font> community for helping Perl to flourish. </p>
<p> For a more complete list of all of Perl&#8217;s historical contributors, please see the <i></i><font SIZE="-1"><i>AUTHORS</i></font><i></i> file in the Perl source distribution.</p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the Perl bug database at &lt;<a rel="nofollow" href="https://rt.perl.org/">https://rt.perl.org/</a>&gt; . There may also be information at &lt;<a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a>&gt; , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the perlbug program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications which make it inappropriate to send to a publicly archived mailing list, then see &#8220;<font SIZE="-1">SECURITY VULNERABILITY CONTACT INFORMATION&#8221;</font> in perlsec for details of how to report the issue.</p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
<h2>Index</h2>
<dt><a href="#lbAG">Incompatible Changes</a></p>
<dd>
<dt><a href="#lbAH">Modules and Pragmata</a></p>
<dd>
<dt><a href="#lbAJ">Documentation</a></p>
<dd>
<dt><a href="#lbAL">Testing</a></p>
<dd>
<dt><a href="#lbAM">Selected Bug Fixes</a></p>
<dd>
<dt><a href="#lbAN">Acknowledgements</a></p>
<dd>
<dt><a href="#lbAO">Reporting Bugs</a></p>
<dd>
<dt><a href="#lbAP">SEE ALSO</a></p>
<dd></dl>
