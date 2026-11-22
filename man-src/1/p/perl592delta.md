---

title: "perl592delta(1)"
name: "perl592delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl592delta/"
description: "perl592delta – what is new for perl v5.9.2"
---

<p> perl592delta &#8211; what is new for perl v5.9.2 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.9.1 and the 5.9.2 development releases. See perl590delta and perl591delta for the differences between 5.8.0 and 5.9.1.</p>
<h2>Incompatible Changes</h2>
<h3>Packing and UTF-8 strings</h3>
<p> The semantics of <i>pack()</i> and <i>unpack()</i> regarding UTF-8-encoded data has been changed. Processing is now by default character per character instead of byte per byte on the underlying encoding. Notably, code that used things like <tt>&quot;pack(&quot;a*&quot;, $string)&quot;</tt> to see through the encoding of string will now simply get back the original <tt>$string</tt>. Packed strings can also get upgraded during processing when you store upgraded characters. You can get the old behaviour by using <tt>&quot;use bytes&quot;</tt>. </p>
<p> To be consistent with <i>pack()</i>, the <tt>&quot;C0&quot;</tt> in <i>unpack()</i> templates indicates that the data is to be processed in character mode, i.e. character by character; on the contrary, <tt>&quot;U0&quot;</tt> in <i>unpack()</i> indicates UTF-8 mode, where the packed string is processed in its UTF-8-encoded Unicode form on a byte by byte basis. This is reversed with regard to perl 5.8.X. </p>
<p> Moreover, <tt>&quot;C0&quot;</tt> and <tt>&quot;U0&quot;</tt> can also be used in <i>pack()</i> templates to specify respectively character and byte modes. </p>
<p> <tt>&quot;C0&quot;</tt> and <tt>&quot;U0&quot;</tt> in the middle of a pack or unpack format now switch to the specified encoding mode, honoring parens grouping. Previously, parens were ignored. </p>
<p> Also, there is a new <i>pack()</i> character format, <tt>&quot;W&quot;</tt>, which is intended to replace the old <tt>&quot;C&quot;</tt>. <tt>&quot;C&quot;</tt> is kept for unsigned chars coded as bytes in the strings internal representation. <tt>&quot;W&quot;</tt> represents unsigned (logical) character values, which can be greater than 255. It is therefore more robust when dealing with potentially UTF-8-encoded data (as <tt>&quot;C&quot;</tt> will wrap values outside the range 0..255, and not respect the string encoding). </p>
<p> In practice, that means that pack formats are now encoding-neutral, except <tt>&quot;C&quot;</tt>. </p>
<p> For consistency, <tt>&quot;A&quot;</tt> in <i>unpack()</i> format now trims all Unicode whitespace from the end of the string. Before perl 5.9.2, it used to strip only the classical ASCII space characters.</p>
<h3>Miscellaneous</h3>
<p> The internal dump output has been improved, so that non-printable characters such as newline and backspace are output in <tt>&quot;</tt>\x&quot;</code> notation, rather than octal. </p>
<p> The <code>-C</code> option can no longer be used on the <code>&quot;#!&quot;</code> line. It wasn&#8217;t working there anyway.  </p>
<h2>Core Enhancements</h2>
<h3>Malloc wrapping</h3>
<p> Perl can now be built to detect attempts to assign pathologically large chunks of memory. Previously such assignments would suffer from integer wrap-around during size calculations causing a misallocation, which would crash perl, and could theoretically be used for ``stack smashing&#8217;&#8216; attacks. The wrapping defaults to enabled on platforms where we know it works (most AIX configurations, BSDi, Darwin, DEC OSF/1, FreeBSD, HP-UX, GNU Linux, OpenBSD, Solaris, VMS and most Win32 compilers) and defaults to disabled on other platforms.  </p>
<h3>Unicode Character Database 4.0.1</h3>
<p> The copy of the Unicode Character Database included in Perl 5.9 has been updated to 4.0.1 from 4.0.0.  </p>
<h3>suidperl less insecure</h3>
<p> Paul Szabo has analysed and patched <code>&quot;suidperl&quot;</code> to remove existing known insecurities. Currently there are no known holes in <code>&quot;suidperl&quot;</code>, but previous experience shows that we cannot be confident that these were the last. You may no longer invoke the set uid perl directly, so to preserve backwards compatibility with scripts that invoke #!/usr/bin/suidperl the only set uid binary is now <code>&quot;sperl5.9.&quot;</code><i>n</i> (<code>&quot;sperl5.9.2&quot;</code> for this release). <code>&quot;suidperl&quot;</code> is installed as a hard link to <code>&quot;perl&quot;</code>; both <code>&quot;suidperl&quot;</code> and <code>&quot;perl&quot;</code> will invoke <code>&quot;sperl5.9.2&quot;</code> automatically the set uid binary, so this change should be completely transparent. </p>
<p> For new projects the core perl team would strongly recommend that you use dedicated, single purpose security tools such as <code>&quot;sudo&quot;</code> in preference to <code>&quot;suidperl&quot;</code>.  </p>
<h3>PERLIO_DEBUG</h3>
<p> The <code>&quot;PERLIO_DEBUG&quot;</code> environment variable has no longer any effect for setuid scripts and for scripts run with <code>-T</code>. </p>
<p> Moreover, with a thread-enabled perl, using <code>&quot;PERLIO_DEBUG&quot;</code> could lead to an internal buffer overflow. This has been fixed.  </p>
<h3>Formats</h3>
<p> In addition to bug fixes, <code>&quot;format&quot;</code>&#8216;s features have been enhanced. See perlform.  </p>
<h3>Unicode Character Classes</h3>
<p> Perl&#8217;s regular expression engine now contains support for matching on the intersection of two Unicode character classes. You can also now refer to user-defined character classes from within other user defined character classes.  </p>
<i></i><i></i><h3>Byte-order modifiers for pack() and unpack()</h3>
<p> There are two new byte-order modifiers, <code>&quot;&gt;&quot;</code> (big-endian) and <code>&quot;&lt;&quot;</code> (little-endian), that can be appended to most <i>pack()</i> and <i>unpack()</i> template characters and groups to force a certain byte-order for that type or group. See ``pack&#8217;&#8216; in perlfunc and perlpacktut for details.  </p>
<i></i><h3>Byte count feature in pack()</h3>
<p> A new <i>pack()</i> template character, <code>&quot;.&quot;</code>, returns the number of characters read so far.  </p>
<h3>New variables</h3>
<p> A new variable, ${^RE_DEBUG_FLAGS}, controls what debug flags are in effect for the regular expression engine when running under <code>&quot;use re &quot;debug&quot;&quot;</code>. See re for details. </p>
<p> A new variable ${^UTF8LOCALE} indicates where a UTF-8 locale was detected by perl at startup.  </p>
<h2>Modules and Pragmata</h2>
<h3>New modules</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;encoding::warnings&quot;</code>, by Audrey Tang, is a module to emit warnings whenever an ASCII character string containing high-bit bytes is implicitly converted into UTF-8. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Module::CoreList&quot;</code>, by Richard Clamp, is a small handy module that tells you what versions of core modules ship with any versions of Perl 5. It comes with a command-line frontend, <code>&quot;corelist&quot;</code>. </p>
 </dd></dl>
<h3>Updated And Improved Modules and Pragmata</h3>
<p> Dual-lived modules have been updated to be kept up-to-date with respect to CPAN. </p>
<p> The dual-lived modules which contain an <code>&quot;_&quot;</code> in their version number are actually <i>ahead</i> of the corresponding CPAN release. </p>
<dl>
<dt>B::Concise</dt>
<dd> <p> <code>&quot;B::Concise&quot;</code> was significantly improved. </p>
 </dd>
<dt>Socket</dt>
<dd> <p> There is experimental support for Linux abstract Unix domain sockets. </p>
 </dd>
<dt>Sys::Syslog</dt>
<dd> <p> <code>&quot;syslog()&quot;</code> can now use numeric constants for facility names and priorities, in addition to strings. </p>
 </dd>
<dt>threads</dt>
<dd> <p> Detached threads are now also supported on Windows. </p>
 </dd></dl>
<h2>Utility Changes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;corelist&quot;</code> utility is now installed with perl (see ``New modules&#8217;&#8216; above). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;h2ph&quot;</code> and <code>&quot;h2xs&quot;</code> have been made a bit more robust with regard to ``modern&#8217;&#8216; C code. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Several bugs have been fixed in <code>&quot;find2perl&quot;</code>, regarding <code>&quot;-exec&quot;</code> and <code>&quot;-eval&quot;</code>. Also the options <code>&quot;-path&quot;</code>, <code>&quot;-ipath&quot;</code> and <code>&quot;-iname&quot;</code> have been added. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The Perl debugger can now save all debugger commands for sourcing later; notably, it can now emulate stepping backwards, by restarting and rerunning all bar the last command from a saved command history. </p>
<p> It can also display the parent inheritance tree of a given class. </p>
<p> Perl has a new -dt command-line flag, which enables threads support in the debugger. </p>
 </dd></dl>
<h2>Performance Enhancements</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> Unicode case mappings (<code>&quot;/i&quot;</code>, <code>&quot;lc&quot;</code>, <code>&quot;uc&quot;</code>, etc) are faster. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;@a = sort @a&quot;</code> was optimized to do in-place sort. Likewise, <code>&quot;reverse sort ...&quot;</code> is now optimized to sort in reverse, avoiding the generation of a temporary intermediate list. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unnecessary assignments are optimised away in </p>
<pre><code>  my $s = undef;
  my @a = ();
  my %h = ();
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;map&quot;</code> in scalar context is now optimized. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The regexp engine now implements the trie optimization : it&#8217;s able to factor out common prefixes and suffixes in regular expressions. A new special variable, ${^RE_TRIE_MAXBUF}, has been added to fine-tune this optimization. </p>
 </dd></dl>
<h2>Installation and Configuration Improvements</h2>
<p> Run-time customization of <code>@INC</code> can be enabled by passing the <code>&quot;-Dusesitecustomize&quot;</code> flag to configure. When enabled, this will make perl run <i></i>$sitelibexp <i>/sitecustomize.pl</i> before anything else. This script can then be set up to add additional entries to <code>@INC</code>. </p>
<p> There is alpha support for relocatable <code>@INC</code> entries. </p>
<p> Perl should build on Interix and on GNU/kFreeBSD.  </p>
<h2>Selected Bug Fixes</h2>
<p> Most of those bugs were reported in the perl 5.8.x maintenance track. Notably, quite a few utf8 bugs were fixed, and several memory leaks were suppressed. The perl58Xdelta manpages have more details on them. </p>
<p> Development-only bug fixes include : </p>
<p> <code>$Foo::_</code> was wrongly forced as <code>$main::_</code>.  </p>
<h2>New or Changed Diagnostics</h2>
<p> A new warning, <code>&quot;!=~ should be !~&quot;</code>, is emitted to prevent this misspelling of the non-matching operator. </p>
<p> The warning <i>Newline in left-justified string</i> has been removed. </p>
<p> The error <i>Too late for ``-T&#8217;&#8216; option</i> has been reformulated to be more descriptive. </p>
<p> There is a new compilation error, <i>Illegal declaration of subroutine</i>, for an obscure case of syntax errors. </p>
<p> The diagnostic output of Carp has been changed slightly, to add a space after the comma between arguments. This makes it much easier for tools such as web browsers to wrap it, but might confuse any automatic tools which perform detailed parsing of Carp output. </p>
<p> <code>&quot;perl -V&quot;</code> has several improvements, making it more useable from shell scripts to get the value of configuration variables. See perlrun for details.  </p>
<h2>Changed Internals</h2>
<p> The perl core has been refactored and reorganised in several places. In short, this release will not be binary compatible with any previous perl release.  </p>
<h2>Known Problems</h2>
<p> For threaded builds, <i>ext/threads/shared/t/wait.t</i> has been reported to fail some tests on HP-UX 10.20. </p>
<p> Net::Ping might fail some tests on HP-UX 11.00 with the latest OS upgrades. </p>
<p> <i>t/io/dup.t</i>, <i>t/io/open.t</i> and <i>lib/ExtUtils/t/Constant.t</i> fail some tests on some BSD flavours.  </p>
<h2>Plans for the next release</h2>
<p> The current plan for perl 5.9.3 is to add CPANPLUS as a core module. More regular expression optimizations are also in the works. </p>
<p> It is planned to release a development version of perl more frequently, i.e. each time something major changes.  </p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://bugs.perl.org/">http://bugs.perl.org/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <code>&quot;perl -V&quot;</code>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team.  </p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for exhaustive details on what changed. </p>
<p> The <i></i><i>INSTALL</i><i></i> file for how to build Perl. </p>
<p> The <i></i><i>README</i><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
