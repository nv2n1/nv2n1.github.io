---
title: "perl584delta(1)"
name: "perl584delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl584delta/"
description: "perl584delta – what is new for perl v5.8.4"
---

<h2 class="name">NAME</h2>
<p> perl584delta &#8211; what is new for perl v5.8.4 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.8.3 release and the 5.8.4 release.</p>
<h2>Incompatible Changes</h2>
<p> Many minor bugs have been fixed. Scripts which happen to rely on previously erroneous behaviour will consider these fixes as incompatible changes :-) You are advised to perform sufficient acceptance testing on this release to satisfy yourself that this does not affect you, before putting this release into production. </p>
<p> The diagnostic output of Carp has been changed slightly, to add a space after the comma between arguments. This makes it much easier for tools such as web browsers to wrap it, but might confuse any automatic tools which perform detailed parsing of Carp output. </p>
<p> The internal dump output has been improved, so that non-printable characters such as newline and backspace are output in <tt>&quot;</tt>\x&quot;</code> notation, rather than octal. This might just confuse non-robust tools which parse the output of modules such as Devel::Peek.  </p>
<h2>Core Enhancements</h2>
<h3>Malloc wrapping</h3>
<p> Perl can now be built to detect attempts to assign pathologically large chunks of memory. Previously such assignments would suffer from integer wrap-around during size calculations causing a misallocation, which would crash perl, and could theoretically be used for ``stack smashing&#8217;&#8216; attacks. The wrapping defaults to enabled on platforms where we know it works (most <font SIZE="-1">AIX</font> configurations, BSDi, Darwin, <font SIZE="-1">DEC OSF/1,</font> FreeBSD, <font SIZE="-1">HP/UX, GNU</font> Linux, OpenBSD, Solaris, <font SIZE="-1">VMS</font> and most Win32 compilers) and defaults to disabled on other platforms.  </p>
<h3>Unicode Character Database 4.0.1</h3>
<p> The copy of the Unicode Character Database included in Perl 5.8 has been updated to 4.0.1 from 4.0.0.  </p>
<h3>suidperl less insecure</h3>
<p> Paul Szabo has analysed and patched <code>&quot;suidperl&quot;</code> to remove existing known insecurities. Currently there are no known holes in <code>&quot;suidperl&quot;</code>, but previous experience shows that we cannot be confident that these were the last. You may no longer invoke the set uid perl directly, so to preserve backwards compatibility with scripts that invoke #!/usr/bin/suidperl the only set uid binary is now <code>&quot;sperl5.8.&quot;</code><i>n</i> (<code>&quot;sperl5.8.4&quot;</code> for this release). <code>&quot;suidperl&quot;</code> is installed as a hard link to <code>&quot;perl&quot;</code>; both <code>&quot;suidperl&quot;</code> and <code>&quot;perl&quot;</code> will invoke <code>&quot;sperl5.8.4&quot;</code> automatically the set uid binary, so this change should be completely transparent. </p>
<p> For new projects the core perl team would strongly recommend that you use dedicated, single purpose security tools such as <code>&quot;sudo&quot;</code> in preference to <code>&quot;suidperl&quot;</code>.  </p>
<h3>format</h3>
<p> In addition to bug fixes, <code>&quot;format&quot;</code>&#8216;s features have been enhanced. See perlform  </p>
<h2>Modules and Pragmata</h2>
<p> The (mis)use of <code>&quot;/tmp&quot;</code> in core modules and documentation has been tidied up. Some modules available both within the perl core and independently from <font SIZE="-1">CPAN</font> (``dual-life modules&#8217;&#8216;) have not yet had these changes applied; the changes will be integrated into future stable perl releases as the modules are updated on <font SIZE="-1">CPAN.</font>  </p>
<h3>Updated modules</h3>
<dl>
<dt>Attribute::Handlers</dt>
<dd>  </dd>
<dt>B</dt>
<dd>  </dd>
<dt>Benchmark</dt>
<dd>  </dd>
<dt><font SIZE="-1">CGI</font></dt>
<dd>  </dd>
<dt>Carp</dt>
<dd>  </dd>
<dt>Cwd</dt>
<dd>  </dd>
<dt>Exporter</dt>
<dd>  </dd>
<dt>File::Find</dt>
<dd>  </dd>
<dt><font SIZE="-1">IO</font></dt>
<dd>  </dd>
<dt>IPC::Open3</dt>
<dd>  </dd>
<dt>Local::Maketext</dt>
<dd>  </dd>
<dt>Math::BigFloat</dt>
<dd>  </dd>
<dt>Math::BigInt</dt>
<dd>  </dd>
<dt>Math::BigRat</dt>
<dd>  </dd>
<dt>MIME::Base64</dt>
<dd>  </dd>
<dt>ODBM_File</dt>
<dd>  </dd>
<dt><font SIZE="-1">POSIX</font></dt>
<dd>  </dd>
<dt>Shell</dt>
<dd>  </dd>
<dt>Socket</dt>
<dd> <p> There is experimental support for Linux abstract Unix domain sockets. </p>
 </dd>
<dt>Storable</dt>
<dd>  </dd>
<dt>Switch</dt>
<dd> <p> Synced with its <font SIZE="-1">CPAN</font> version 2.10 </p>
 </dd>
<dt>Sys::Syslog</dt>
<dd> <p> <code>&quot;syslog()&quot;</code> can now use numeric constants for facility names and priorities, in addition to strings. </p>
 </dd>
<dt>Term::ANSIColor</dt>
<dd>  </dd>
<dt>Time::HiRes</dt>
<dd>  </dd>
<dt>Unicode::UCD</dt>
<dd>  </dd>
<dt>Win32</dt>
<dd> <p> Win32.pm/Win32.xs has moved from the libwin32 module to core Perl </p>
 </dd>
<dt>base</dt>
<dd>  </dd>
<dt>open</dt>
<dd>  </dd>
<dt>threads</dt>
<dd> <p> Detached threads are now also supported on Windows. </p>
 </dd>
<dt>utf8</dt>
<dd>  </dd></dl>
<h2>Performance Enhancements</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> Accelerated Unicode case mappings (<code>&quot;/i&quot;</code>, <code>&quot;lc&quot;</code>, <code>&quot;uc&quot;</code>, etc). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In place sort optimised (eg <code>&quot;@a = sort @a&quot;</code>) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unnecessary assignment optimised away in </p>
<pre><code>  my $s = undef;
  my @a = ();
  my %h = ();
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Optimised <code>&quot;map&quot;</code> in scalar context </p>
 </dd></dl>
<h2>Utility Changes</h2>
<p> The Perl debugger (<i>lib/perl5db.pl</i>) can now save all debugger commands for sourcing later, and can display the parent inheritance tree of a given class.  </p>
<h2>Installation and Configuration Improvements</h2>
<p> The build process on both <font SIZE="-1">VMS</font> and Windows has had several minor improvements made. On Windows Borland&#8217;s C compiler can now compile perl with PerlIO and/or <font SIZE="-1">USE_LARGE_FILES</font> enabled. </p>
<p> <code>&quot;perl.exe&quot;</code> on Windows now has a ``Camel&#8217;&#8216; logo icon. The use of a camel with the topic of Perl is a trademark of O&#8217;Reilly and Associates Inc., and is used with their permission (ie distribution of the source, compiling a Windows executable from it, and using that executable locally). Use of the supplied camel for anything other than a perl executable&#8217;s icon is specifically not covered, and anyone wishing to redistribute perl binaries <i>with</i> the icon should check directly with O&#8217;Reilly beforehand. </p>
<p> Perl should build cleanly on Stratus <font SIZE="-1">VOS</font> once more.  </p>
<h2>Selected Bug Fixes</h2>
<p> More utf8 bugs fixed, notably in how <code>&quot;chomp&quot;</code>, <code>&quot;chop&quot;</code>, <code>&quot;send&quot;</code>, and <code>&quot;syswrite&quot;</code> and interact with utf8 data. Concatenation now works correctly when <code>&quot;use bytes;&quot;</code> is in scope. </p>
<p> Pragmata are now correctly propagated into (?{...}) constructions in regexps. Code such as </p>
<pre><code>   my $x = qr{ ... (??{ $x }) ... };
</code></pre>
<p> will now (correctly) fail under use strict. (As the inner <code>$x</code> is and has always referred to <code>$::x</code>) </p>
<p> The ``const in void context&#8217;&#8216; warning has been suppressed for a constant in an optimised-away boolean expression such as <code>&quot;5 || print;&quot;</code> </p>
<p> <code>&quot;perl -i&quot;</code> could <code>&quot;fchmod(stdin)&quot;</code> by mistake. This is serious if stdin is attached to a terminal, and perl is running as root. Now fixed.  </p>
<h2>New or Changed Diagnostics</h2>
<p> <code>&quot;Carp&quot;</code> and the internal diagnostic routines used by <code>&quot;Devel::Peek&quot;</code> have been made clearer, as described in ``Incompatible Changes&#8217;&#8216;  </p>
<h2>Changed Internals</h2>
<p> Some bugs have been fixed in the hash internals. Restricted hashes and their place holders are now allocated and deleted at slightly different times, but this should not be visible to user code.  </p>
<h2>Future Directions</h2>
<p> Code freeze for the next maintenance release (5.8.5) will be on 30th June 2004, with release by mid July.  </p>
<h2>Platform Specific Problems</h2>
<p> This release is known not to build on Windows 95.  </p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://bugs.perl.org.">http://bugs.perl.org.</a> There may also be information at <a rel="nofollow" href="http://www.perl.org,">http://www.perl.org,</a> the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <code>&quot;perl -V&quot;</code>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. You can browse and search the Perl 5 bugs at <a rel="nofollow" href="http://bugs.perl.org/">http://bugs.perl.org/</a>  </p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
<h2>Index</h2>
