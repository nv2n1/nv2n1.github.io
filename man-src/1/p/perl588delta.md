---
title: "perl588delta(1)"
name: "perl588delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl588delta/"
description: "perl588delta – what is new for perl v5.8.8"
---

<h2 class="name">NAME</h2>
<p> perl588delta &#8211; what is new for perl v5.8.8 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.8.7 release and the 5.8.8 release.</p>
<h2>Incompatible Changes</h2>
<p> There are no changes intentionally incompatible with 5.8.7. If any exist, they are bugs and reports are welcome.</p>
<h2>Core Enhancements</h2>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;chdir&quot;</tt>, <tt>&quot;chmod&quot;</tt> and <tt>&quot;chown&quot;</tt> can now work on filehandles as well as filenames, if the system supports respectively <tt>&quot;fchdir&quot;</tt>, <tt>&quot;fchmod&quot;</tt> and <tt>&quot;fchown&quot;</tt>, thanks to a patch provided by Gisle Aas.</dl>
<h2>Modules and Pragmata</h2>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;Attribute::Handlers&quot;</tt> upgraded to version 0.78_02</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Documentation typo fix</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;attrs&quot;</tt> upgraded to version 1.02</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Internal cleanup only</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;autouse&quot;</tt> upgraded to version 1.05</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Simplified implementation</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;B&quot;</tt> upgraded to version 1.09_01</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> The inheritance hierarchy of the <tt>&quot;B::&quot;</tt> modules has been corrected; <tt>&quot;B::NV&quot;</tt> now inherits from <tt>&quot;B::SV&quot;</tt> (instead of <tt>&quot;B::IV&quot;</tt>).</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;blib&quot;</tt> upgraded to version 1.03</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Documentation typo fix</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;ByteLoader&quot;</tt> upgraded to version 0.06</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Internal cleanup</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;CGI&quot;</tt> upgraded to version 3.15</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Extraneous &#8220;?&#8221; from <tt>&quot;self_url()&quot;</tt> removed</p>
<dt>&bull;</p>
<dd> <tt>&quot;scrolling_list()&quot;</tt> select attribute fixed</p>
<dt>&bull;</p>
<dd> <tt>&quot;virtual_port&quot;</tt> now works properly with the https protocol</p>
<dt>&bull;</p>
<dd> <tt>&quot;upload_hook()&quot;</tt> and <tt>&quot;append()&quot;</tt> now works in function-oriented mode</p>
<dt>&bull;</p>
<dd> <tt>&quot;POST_MAX&quot;</tt> doesn&#8217;t cause the client to hang any more</p>
<dt>&bull;</p>
<dd> Automatic tab indexes are now disabled and new <tt>&quot;-tabindex&quot;</tt> pragma has been added to turn automatic indexes back on</p>
<dt>&bull;</p>
<dd> <tt>&quot;end_form()&quot;</tt> doesn&#8217;t emit empty (and non-validating) <tt>&quot;&lt;div&gt;&quot;</tt></p>
<dt>&bull;</p>
<dd> <tt>&quot;CGI::Carp&quot;</tt> works better in certain mod_perl configurations</p>
<dt>&bull;</p>
<dd> Setting <tt>$CGI::TMPDIRECTORY</tt> is now effective</p>
<dt>&bull;</p>
<dd> Enhanced documentation</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;charnames&quot;</tt> upgraded to version 1.05</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;viacode()&quot;</tt> now accept hex strings and has been optimized.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;CPAN&quot;</tt> upgraded to version 1.76_02</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> 1 minor bug fix for Win32</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Cwd&quot;</tt> upgraded to version 3.12</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;canonpath()&quot;</tt> on Win32 now collapses <i>foo\..</i> sections correctly.</p>
<dt>&bull;</p>
<dd> Improved behaviour on Symbian <font SIZE="-1">OS.</font></p>
<dt>&bull;</p>
<dd> Enhanced documentation and typo fixes</p>
<dt>&bull;</p>
<dd> Internal cleanup</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Data::Dumper&quot;</tt> upgraded to version 2.121_08</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> A problem where <tt>&quot;Data::Dumper&quot;</tt> would sometimes update the iterator state of hashes has been fixed</p>
<dt>&bull;</p>
<dd> Numeric labels now work</p>
<dt>&bull;</p>
<dd> Internal cleanup</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;DB&quot;</tt> upgraded to version 1.01</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> A problem where the state of the regexp engine would sometimes get clobbered when running under the debugger has been fixed.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;DB_File&quot;</tt> upgraded to version 1.814</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Adds support for Berkeley <font SIZE="-1">DB 4.4.</font></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Devel::DProf&quot;</tt> upgraded to version 20050603.00</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Internal cleanup</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Devel::Peek&quot;</tt> upgraded to version 1.03</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Internal cleanup</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Devel::PPPort&quot;</tt> upgraded to version 3.06_01</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;--compat-version&quot;</tt> argument checking has been improved</p>
<dt>&bull;</p>
<dd> Files passed on the command line are filtered by default</p>
<dt>&bull;</p>
<dd> <tt>&quot;--nofilter&quot;</tt> option to override the filtering has been added</p>
<dt>&bull;</p>
<dd> Enhanced documentation</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;diagnostics&quot;</tt> upgraded to version 1.15</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Documentation typo fix</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Digest&quot;</tt> upgraded to version 1.14</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> The constructor now knows which module implements <font SIZE="-1">SHA-224</font></p>
<dt>&bull;</p>
<dd> Documentation tweaks and typo fixes</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Digest::MD5&quot;</tt> upgraded to version 2.36</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;XSLoader&quot;</tt> is now used for faster loading</p>
<dt>&bull;</p>
<dd> Enhanced documentation including <font SIZE="-1">MD5</font> weaknesses discovered lately</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Dumpvalue&quot;</tt> upgraded to version 1.12</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Documentation fix</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;DynaLoader&quot;</tt> upgraded but unfortunately we&#8217;re not able to increment its version number :-(</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Implements <tt>&quot;dl_unload_file&quot;</tt> on Win32</p>
<dt>&bull;</p>
<dd> Internal cleanup</p>
<dt>&bull;</p>
<dd> <tt>&quot;XSLoader&quot;</tt> 0.06 incorporated; small optimisation for calling <tt>&quot;bootstrap_inherit()&quot;</tt> and documentation enhancements.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Encode&quot;</tt> upgraded to version 2.12</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> A coderef is now acceptable for <tt>&quot;CHECK&quot;</tt>!</p>
<dt>&bull;</p>
<dd> 3 new characters added to the <font SIZE="-1">ISO-8859-7</font> encoding</p>
<dt>&bull;</p>
<dd> New encoding <tt>&quot;MIME-Header-ISO_2022_JP&quot;</tt> added</p>
<dt>&bull;</p>
<dd> Problem with partial characters and <tt>&quot;encoding(utf-8-strict)&quot;</tt> fixed.</p>
<dt>&bull;</p>
<dd> Documentation enhancements and typo fixes</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;English&quot;</tt> upgraded to version 1.02</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> the <tt>$COMPILING</tt> variable has been added</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;ExtUtils::Constant&quot;</tt> upgraded to version 0.17</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Improved compatibility with older versions of perl</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;ExtUtils::MakeMaker&quot;</tt> upgraded to version 6.30 (was 6.17)</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Too much to list here; see &lt;<a rel="nofollow" href="http://search.cpan.org/dist/ExtUtils-MakeMaker/Changes">http://search.cpan.org/dist/ExtUtils-MakeMaker/Changes</a>&gt;</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;File::Basename&quot;</tt> upgraded to version 2.74, with changes contributed by Michael Schwern.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Documentation clarified and errors corrected.</p>
<dt>&bull;</p>
<dd> <tt>&quot;basename&quot;</tt> now strips trailing path separators before processing the name.</p>
<dt>&bull;</p>
<dd> <tt>&quot;basename&quot;</tt> now returns <tt>&quot;/&quot;</tt> for parameter <tt>&quot;/&quot;</tt>, to make <tt>&quot;basename&quot;</tt> consistent with the shell utility of the same name.</p>
<dt>&bull;</p>
<dd> The suffix is no longer stripped if it is identical to the remaining characters in the name, again for consistency with the shell utility.</p>
<dt>&bull;</p>
<dd> Some internal code cleanup.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;File::Copy&quot;</tt> upgraded to version 2.09</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Copying a file onto itself used to fail.</p>
<dt>&bull;</p>
<dd> Moving a file between file systems now preserves the access and modification time stamps</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;File::Find&quot;</tt> upgraded to version 1.10</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Win32 portability fixes</p>
<dt>&bull;</p>
<dd> Enhanced documentation</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;File::Glob&quot;</tt> upgraded to version 1.05</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Internal cleanup</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;File::Path&quot;</tt> upgraded to version 1.08</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;mkpath&quot;</tt> now preserves <tt>&quot;errno&quot;</tt> when <tt>&quot;mkdir&quot;</tt> fails</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;File::Spec&quot;</tt> upgraded to version 3.12</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;File::Spec-&gt;rootdir()&quot;</tt> now returns <tt>&quot;\&quot;</tt> on Win32, instead of <tt>&quot;/&quot;</tt></p>
<dt>&bull;</p>
<dd> <tt>$^O</tt> could sometimes become tainted. This has been fixed.</p>
<dt>&bull;</p>
<dd> <tt>&quot;canonpath&quot;</tt> on Win32 now collapses <tt>&quot;foo/..&quot;</tt> (or <tt>&quot;foo\..&quot;</tt>) sections correctly, rather than doing the &#8220;misguided&#8221; work it was previously doing. Note that <tt>&quot;canonpath&quot;</tt> on Unix still does <code>not</code> collapse these sections, as doing so would be incorrect.</p>
<dt>&bull;</p>
<dd> Some documentation improvements</p>
<dt>&bull;</p>
<dd> Some internal code cleanup</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;FileCache&quot;</tt> upgraded to version 1.06</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <font SIZE="-1">POD</font> formatting errors in the documentation fixed</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Filter::Simple&quot;</tt> upgraded to version 0.82</p>
<dt>&bull;</p>
<dd> <tt>&quot;FindBin&quot;</tt> upgraded to version 1.47</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Now works better with directories where access rights are more restrictive than usual.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;GDBM_File&quot;</tt> upgraded to version 1.08</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Internal cleanup</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Getopt::Long&quot;</tt> upgraded to version 2.35</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;prefix_pattern&quot;</tt> has now been complemented by a new configuration option <tt>&quot;long_prefix_pattern&quot;</tt> that allows the user to specify what prefix patterns should have long option style semantics applied.</p>
<dt>&bull;</p>
<dd> Options can now take multiple values at once (experimental)</p>
<dt>&bull;</p>
<dd> Various bug fixes</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;if&quot;</tt> upgraded to version 0.05</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Give more meaningful error messages from <tt>&quot;if&quot;</tt> when invoked with a condition in list context.</p>
<dt>&bull;</p>
<dd> Restore backwards compatibility with earlier versions of perl</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;IO&quot;</tt> upgraded to version 1.22</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Enhanced documentation</p>
<dt>&bull;</p>
<dd> Internal cleanup</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;IPC::Open2&quot;</tt> upgraded to version 1.02</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Enhanced documentation</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;IPC::Open3&quot;</tt> upgraded to version 1.02</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Enhanced documentation</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;List::Util&quot;</tt> upgraded to version 1.18 (was 1.14)</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Fix pure-perl version of <tt>&quot;refaddr&quot;</tt> to avoid blessing an un-blessed reference</p>
<dt>&bull;</p>
<dd> Use <tt>&quot;XSLoader&quot;</tt> for faster loading</p>
<dt>&bull;</p>
<dd> Fixed various memory leaks</p>
<dt>&bull;</p>
<dd> Internal cleanup and portability fixes</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Math::Complex&quot;</tt> upgraded to version 1.35</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;atan2(0, i)&quot;</tt> now works, as do all the (computable) complex argument cases</p>
<dt>&bull;</p>
<dd> Fixes for certain bugs in <tt>&quot;make&quot;</tt> and <tt>&quot;emake&quot;</tt></p>
<dt>&bull;</p>
<dd> Support returning the <i>k</i>th root directly</p>
<dt>&bull;</p>
<dd> Support <tt>&quot;[2,-3pi/8]&quot;</tt> in <tt>&quot;emake&quot;</tt></p>
<dt>&bull;</p>
<dd> Support <tt>&quot;inf&quot;</tt> for <tt>&quot;make&quot;</tt>/<tt>&quot;emake&quot;</tt></p>
<dt>&bull;</p>
<dd> Document <tt>&quot;make&quot;</tt>/<tt>&quot;emake&quot;</tt> more visibly</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Math::Trig&quot;</tt> upgraded to version 1.03</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Add more great circle routines: <tt>&quot;great_circle_waypoint&quot;</tt> and <tt>&quot;great_circle_destination&quot;</tt></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;MIME::Base64&quot;</tt> upgraded to version 3.07</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Use <tt>&quot;XSLoader&quot;</tt> for faster loading</p>
<dt>&bull;</p>
<dd> Enhanced documentation</p>
<dt>&bull;</p>
<dd> Internal cleanup</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;NDBM_File&quot;</tt> upgraded to version 1.06</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Enhanced documentation</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;ODBM_File&quot;</tt> upgraded to version 1.06</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Documentation typo fixed</p>
<dt>&bull;</p>
<dd> Internal cleanup</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Opcode&quot;</tt> upgraded to version 1.06</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Enhanced documentation</p>
<dt>&bull;</p>
<dd> Internal cleanup</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;open&quot;</tt> upgraded to version 1.05</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Enhanced documentation</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;overload&quot;</tt> upgraded to version 1.04</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Enhanced documentation</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;PerlIO&quot;</tt> upgraded to version 1.04</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;PerlIO::via&quot;</tt> iterate over layers properly now</p>
<dt>&bull;</p>
<dd> <tt>&quot;PerlIO::scalar&quot;</tt> understands <tt>&quot;$/ = &quot;&quot;&quot;</tt> now</p>
<dt>&bull;</p>
<dd> <tt>&quot;encoding(utf-8-strict)&quot;</tt> with partial characters now works</p>
<dt>&bull;</p>
<dd> Enhanced documentation</p>
<dt>&bull;</p>
<dd> Internal cleanup</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Pod::Functions&quot;</tt> upgraded to version 1.03</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Documentation typos fixed</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Pod::Html&quot;</tt> upgraded to version 1.0504</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <font SIZE="-1">HTML</font> output will now correctly link to <tt>&quot;=item&quot;</tt>s on the same page, and should be valid <font SIZE="-1">XHTML.</font></p>
<dt>&bull;</p>
<dd> Variable names are recognized as intended</p>
<dt>&bull;</p>
<dd> Documentation typos fixed</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Pod::Parser&quot;</tt> upgraded to version 1.32</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Allow files that start with <tt>&quot;=head&quot;</tt> on the first line</p>
<dt>&bull;</p>
<dd> Win32 portability fix</p>
<dt>&bull;</p>
<dd> Exit status of <tt>&quot;pod2usage&quot;</tt> fixed</p>
<dt>&bull;</p>
<dd> New <tt>&quot;-noperldoc&quot;</tt> switch for <tt>&quot;pod2usage&quot;</tt></p>
<dt>&bull;</p>
<dd> Arbitrary <font SIZE="-1">URL</font> schemes now allowed</p>
<dt>&bull;</p>
<dd> Documentation typos fixed</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;POSIX&quot;</tt> upgraded to version 1.09</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Documentation typos fixed</p>
<dt>&bull;</p>
<dd> Internal cleanup</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;re&quot;</tt> upgraded to version 0.05</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Documentation typo fixed</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Safe&quot;</tt> upgraded to version 2.12</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Minor documentation enhancement</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;SDBM_File&quot;</tt> upgraded to version 1.05</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Documentation typo fixed</p>
<dt>&bull;</p>
<dd> Internal cleanup</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Socket&quot;</tt> upgraded to version 1.78</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Internal cleanup</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Storable&quot;</tt> upgraded to version 2.15</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> This includes the <tt>&quot;STORABLE_attach&quot;</tt> hook functionality added by Adam Kennedy, and more frugal memory requirements when storing under <tt>&quot;ithreads&quot;</tt>, by using the <tt>&quot;ithreads&quot;</tt> cloning tracking code.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Switch&quot;</tt> upgraded to version 2.10_01</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Documentation typos fixed</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Sys::Syslog&quot;</tt> upgraded to version 0.13</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Now provides numeric macros and meaningful <tt>&quot;Exporter&quot;</tt> tags.</p>
<dt>&bull;</p>
<dd> No longer uses <tt>&quot;Sys::Hostname&quot;</tt> as it may provide useless values in unconfigured network environments, so instead uses <tt>&quot;INADDR_LOOPBACK&quot;</tt> directly.</p>
<dt>&bull;</p>
<dd> <tt>&quot;syslog()&quot;</tt> now uses local timestamp.</p>
<dt>&bull;</p>
<dd> <tt>&quot;setlogmask()&quot;</tt> now behaves like its C counterpart.</p>
<dt>&bull;</p>
<dd> <tt>&quot;setlogsock()&quot;</tt> will now <tt>&quot;croak()&quot;</tt> as documented.</p>
<dt>&bull;</p>
<dd> Improved error and warnings messages.</p>
<dt>&bull;</p>
<dd> Improved documentation.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Term::ANSIColor&quot;</tt> upgraded to version 1.10</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Fixes a bug in <tt>&quot;colored&quot;</tt> when <tt>$EACHLINE</tt> is set that caused it to not color lines consisting solely of 0 (literal zero).</p>
<dt>&bull;</p>
<dd> Improved tests.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Term::ReadLine&quot;</tt> upgraded to version 1.02</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Documentation tweaks</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Test::Harness&quot;</tt> upgraded to version 2.56 (was 2.48)</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> The <tt>&quot;Test::Harness&quot;</tt> timer is now off by default.</p>
<dt>&bull;</p>
<dd> Now shows elapsed time in milliseconds.</p>
<dt>&bull;</p>
<dd> Various bug fixes</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Test::Simple&quot;</tt> upgraded to version 0.62 (was 0.54)</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;is_deeply()&quot;</tt> no longer fails to work for many cases</p>
<dt>&bull;</p>
<dd> Various minor bug fixes</p>
<dt>&bull;</p>
<dd> Documentation enhancements</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Text::Tabs&quot;</tt> upgraded to version 2005.0824</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Provides a faster implementation of <tt>&quot;expand&quot;</tt></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Text::Wrap&quot;</tt> upgraded to version 2005.082401</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Adds <tt>$Text::Wrap::separator2</tt>, which allows you to preserve existing newlines but add line-breaks with some other string.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;threads&quot;</tt> upgraded to version 1.07</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;threads&quot;</tt> will now honour <tt>&quot;no warnings 'threads'&quot;</tt></p>
<dt>&bull;</p>
<dd> A thread&#8217;s interpreter is now freed after <tt>&quot;$t-&gt;join()&quot;</tt> rather than after <tt>&quot;undef $t&quot;</tt>, which should fix some <tt>&quot;ithreads&quot;</tt> memory leaks. (Fixed by Dave Mitchell)</p>
<dt>&bull;</p>
<dd> Some documentation typo fixes.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;threads::shared&quot;</tt> upgraded to version 0.94</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Documentation changes only</p>
<dt>&bull;</p>
<dd> Note: An improved implementation of <tt>&quot;threads::shared&quot;</tt> is available on <font SIZE="-1">CPAN</font> &#8211; this will be merged into 5.8.9 if it proves stable.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Tie::Hash&quot;</tt> upgraded to version 1.02</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Documentation typo fixed</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Time::HiRes&quot;</tt> upgraded to version 1.86 (was 1.66)</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;clock_nanosleep()&quot;</tt> and <tt>&quot;clock()&quot;</tt> functions added</p>
<dt>&bull;</p>
<dd> Support for the <font SIZE="-1">POSIX</font> <tt>&quot;clock_gettime()&quot;</tt> and <tt>&quot;clock_getres()&quot;</tt> has been added</p>
<dt>&bull;</p>
<dd> Return <tt>&quot;undef&quot;</tt> or an empty list if the C <tt>&quot;gettimeofday()&quot;</tt> function fails</p>
<dt>&bull;</p>
<dd> Improved <tt>&quot;nanosleep&quot;</tt> detection</p>
<dt>&bull;</p>
<dd> Internal cleanup</p>
<dt>&bull;</p>
<dd> Enhanced documentation</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Unicode::Collate&quot;</tt> upgraded to version 0.52</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Now implements <font SIZE="-1">UCA</font> Revision 14 (based on Unicode 4.1.0).</p>
<dt>&bull;</p>
<dd> <tt>&quot;Unicode::Collate-&gt;new&quot;</tt> method no longer overwrites user&#8217;s <tt>$_</tt></p>
<dt>&bull;</p>
<dd> Enhanced documentation</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Unicode::UCD&quot;</tt> upgraded to version 0.24</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Documentation typos fixed</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;User::grent&quot;</tt> upgraded to version 1.01</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Documentation typo fixed</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;utf8&quot;</tt> upgraded to version 1.06</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Documentation typos fixed</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;vmsish&quot;</tt> upgraded to version 1.02</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Documentation typos fixed</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;warnings&quot;</tt> upgraded to version 1.05</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Gentler messing with <tt>&quot;Carp::&quot;</tt> internals</p>
<dt>&bull;</p>
<dd> Internal cleanup</p>
<dt>&bull;</p>
<dd> Documentation update</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Win32&quot;</tt> upgraded to version 0.2601</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Provides Windows Vista support to <tt>&quot;Win32::GetOSName&quot;</tt></p>
<dt>&bull;</p>
<dd> Documentation enhancements</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;XS::Typemap&quot;</tt> upgraded to version 0.02</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Internal cleanup</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h2>Utility Changes</h2>
<h3>h2xs enhancements</h3>
<p> <tt>&quot;h2xs&quot;</tt> implements new option <tt>&quot;--use-xsloader&quot;</tt> to force use of <tt>&quot;XSLoader&quot;</tt> even in backwards compatible modules. </p>
<p> The handling of authors&#8217; names that had apostrophes has been fixed. </p>
<p> Any enums with negative values are now skipped.</p>
<h3>perlivp enhancements</h3>
<p> <tt>&quot;perlivp&quot;</tt> implements new option <tt>&quot;-a&quot;</tt> and will not check for <i>*.ph</i> files by default any more. Use the <tt>&quot;-a&quot;</tt> option to run <i>all</i> tests.</p>
<h2>New Documentation</h2>
<p> The perlglossary manpage is a glossary of terms used in the Perl documentation, technical and otherwise, kindly provided by O&#8217;Reilly Media, inc.</p>
<h2>Performance Enhancements</h2>
<dl>
<dt>&bull;</p>
<dd> Weak reference creation is now <i><a href="/docs/linux/man/1-o/">O</a>(1)</i> rather than <i><a href="/docs/linux/man/n-o/">O</a>(n)</i>, courtesy of Nicholas Clark. Weak reference deletion remains <i><a href="/docs/linux/man/n-o/">O</a>(n)</i>, but if deletion only happens at program exit, it may be skipped completely.</p>
<dt>&bull;</p>
<dd> Salvador Fandiño provided improvements to reduce the memory usage of <tt>&quot;sort&quot;</tt> and to speed up some cases.</p>
<dt>&bull;</p>
<dd> Jarkko Hietaniemi and Andy Lester worked to mark as much data as possible in the C source files as <tt>&quot;static&quot;</tt>, to increase the proportion of the executable file that the operating system can share between process, and thus reduce real memory usage on multi-user systems.</dl>
<h2>Installation and Configuration Improvements</h2>
<p> Parallel makes should work properly now, although there may still be problems if <tt>&quot;make test&quot;</tt> is instructed to run in parallel. </p>
<p> Building with Borland&#8217;s compilers on Win32 should work more smoothly. In particular Steve Hay has worked to side step many warnings emitted by their compilers and at least one C compiler internal error. </p>
<p> <tt>&quot;Configure&quot;</tt> will now detect <tt>&quot;clearenv&quot;</tt> and <tt>&quot;unsetenv&quot;</tt>, thanks to a patch from Alan Burlison. It will also probe for <tt>&quot;futimes&quot;</tt> and whether <tt>&quot;sprintf&quot;</tt> correctly returns the length of the formatted string, which will both be used in perl 5.8.9. </p>
<p> There are improved hints for next-3.0, vmesa, <font SIZE="-1">IX,</font> Darwin, Solaris, Linux, <font SIZE="-1">DEC/OSF,</font> HP-UX and MPE/iX </p>
<p> Perl extensions on Windows now can be statically built into the Perl <font SIZE="-1">DLL,</font> thanks to a work by Vadim Konovalov. (This improvement was actually in 5.8.7, but was accidentally omitted from perl587delta).</p>
<h2>Selected Bug Fixes</h2>
<h3>no warnings &#8216;category&#8217; works correctly with -w</h3>
<p> Previously when running with warnings enabled globally via <tt>&quot;-w&quot;</tt>, selective disabling of specific warning categories would actually turn off all warnings. This is now fixed; now <tt>&quot;no warnings 'io';&quot;</tt> will only turn off warnings in the <tt>&quot;io&quot;</tt> class. Previously it would erroneously turn off all warnings. </p>
<p> This bug fix may cause some programs to start correctly issuing warnings.</p>
<h3>Remove over-optimisation</h3>
<p> Perl 5.8.4 introduced a change so that assignments of <tt>&quot;undef&quot;</tt> to a scalar, or of an empty list to an array or a hash, were optimised away. As this could cause problems when <tt>&quot;goto&quot;</tt> jumps were involved, this change has been backed out.</p>
<h3><code>sprintf()</code> fixes</h3>
<p> Using the <code>sprintf()</code> function with some formats could lead to a buffer overflow in some specific cases. This has been fixed, along with several other bugs, notably in bounds checking. </p>
<p> In related fixes, it was possible for badly written code that did not follow the documentation of <tt>&quot;Sys::Syslog&quot;</tt> to have formatting vulnerabilities. <tt>&quot;Sys::Syslog&quot;</tt> has been changed to protect people from poor quality third party code.</p>
<h3>Debugger and Unicode slowdown</h3>
<p> It had been reported that running under perl&#8217;s debugger when processing Unicode data could cause unexpectedly large slowdowns. The most likely cause of this was identified and fixed by Nicholas Clark.</p>
<h3>Smaller fixes</h3>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;FindBin&quot;</tt> now works better with directories where access rights are more restrictive than usual.</p>
<dt>&bull;</p>
<dd> Several memory leaks in ithreads were closed. An improved implementation of <tt>&quot;threads::shared&quot;</tt> is available on <font SIZE="-1">CPAN</font> &#8211; this will be merged into 5.8.9 if it proves stable.</p>
<dt>&bull;</p>
<dd> Trailing spaces are now trimmed from <tt>$!</tt> and <tt>$^E</tt>.</p>
<dt>&bull;</p>
<dd> Operations that require perl to read a process&#8217;s list of groups, such as reads of <tt>$(</tt> and <tt>$)</tt>, now dynamically allocate memory rather than using a fixed sized array. The fixed size array could cause C stack exhaustion on systems configured to use large numbers of groups.</p>
<dt>&bull;</p>
<dd> <tt>&quot;PerlIO::scalar&quot;</tt> now works better with non-default <tt>$/</tt> settings.</p>
<dt>&bull;</p>
<dd> You can now use the <tt>&quot;x&quot;</tt> operator to repeat a <tt>&quot;qw//&quot;</tt> list. This used to raise a syntax error.</p>
<dt>&bull;</p>
<dd> The debugger now traces correctly execution in eval(&quot;&quot;)uated code that contains #line directives.</p>
<dt>&bull;</p>
<dd> The value of the <tt>&quot;open&quot;</tt> pragma is no longer ignored for three-argument opens.</p>
<dt>&bull;</p>
<dd> The optimisation of <tt>&quot;for (reverse @a)&quot;</tt> introduced in perl 5.8.6 could misbehave when the array had undefined elements and was used in <font SIZE="-1">LVALUE</font> context. Dave Mitchell provided a fix.</p>
<dt>&bull;</p>
<dd> Some case insensitive matches between <font SIZE="-1">UTF-8</font> encoded data and 8 bit regexps, and vice versa, could give malformed character warnings. These have been fixed by Dave Mitchell and Yves Orton.</p>
<dt>&bull;</p>
<dd> <tt>&quot;lcfirst&quot;</tt> and <tt>&quot;ucfirst&quot;</tt> could corrupt the string for certain cases where the length <font SIZE="-1">UTF-8</font> encoding of the string in lower case, upper case or title case differed. This was fixed by Nicholas Clark.</p>
<dt>&bull;</p>
<dd> Perl will now use the C library calls <tt>&quot;unsetenv&quot;</tt> and <tt>&quot;clearenv&quot;</tt> if present to delete keys from <tt>%ENV</tt> and delete <tt>%ENV</tt> entirely, thanks to a patch from Alan Burlison.</dl>
<h2>New or Changed Diagnostics</h2>
<h3>Attempt to set length of freed array</h3>
<p> This is a new warning, produced in situations such as this: </p>
<pre><code>
$r = do
{
    my @a;
    \$ #a
};
$$r = 503;
</code></pre>
<h3>Non-string passed as bitmask</h3>
<p> This is a new warning, produced when number has been passed as an argument to <code>select()</code>, instead of a bitmask. </p>
<pre><code>
#Wrong, will now warn
$rin = fileno(STDIN);
($nfound, $timeleft) = select($rout = $rin, undef, undef, $timeout);

#Should be
$rin = '';
vec($rin, fileno(STDIN), 1) = 1;
($nfound, $timeleft) = select($rout = $rin, undef, undef, $timeout);
</code></pre>
<h3>Search pattern not terminated or ternary operator parsed as search pattern</h3>
<p> This syntax error indicates that the lexer couldn&#8217;t find the final delimiter of a <tt>&quot;?PATTERN?&quot;</tt> construct. Mentioning the ternary operator in this error message makes it easier to diagnose syntax errors.</p>
<h2>Changed Internals</h2>
<p> There has been a fair amount of refactoring of the <tt>&quot;C&quot;</tt> source code, partly to make it tidier and more maintainable. The resulting object code and the <tt>&quot;perl&quot;</tt> binary may well be smaller than 5.8.7, in particular due to a change contributed by Dave Mitchell which reworked the warnings code to be significantly smaller. Apart from being smaller and possibly faster, there should be no user-detectable changes. </p>
<p> Andy Lester supplied many improvements to determine which function parameters and local variables could actually be declared <tt>&quot;const&quot;</tt> to the C compiler. Steve Peters provided new <tt>*_set</tt> macros and reworked the core to use these rather than assigning to macros in <font SIZE="-1">LVALUE</font> context. </p>
<p> Dave Mitchell improved the lexer debugging output under <tt>&quot;-DT&quot;</tt> </p>
<p> Nicholas Clark changed the string buffer allocation so that it is now rounded up to the next multiple of 4 (or 8 on platforms with 64 bit pointers). This should reduce the number of calls to <tt>&quot;realloc&quot;</tt> without actually using any extra memory. </p>
<p> The <tt>&quot;HV&quot;</tt>&#8216;s array of <tt>&quot;HE*&quot;</tt>s is now allocated at the correct (minimal) size, thanks to another change by Nicholas Clark. Compile with <tt>&quot;-DPERL_USE_LARGE_HV_ALLOC&quot;</tt> to use the old, sloppier, default. </p>
<p> For <font SIZE="-1">XS</font> or embedding debugging purposes, if perl is compiled with <tt>&quot;-DDEBUG_LEAKING_SCALARS_FORK_DUMP&quot;</tt> in addition to <tt>&quot;-DDEBUG_LEAKING_SCALARS&quot;</tt> then a child process is <tt>&quot;fork&quot;</tt>ed just before global destruction, which is used to display the values of any scalars found to have leaked at the end of global destruction. Without this, the scalars have already been freed sufficiently at the point of detection that it is impossible to produce any meaningful dump of their contents. This feature was implemented by the indefatigable Nicholas Clark, based on an idea by Mike Giroux.</p>
<h2>Platform Specific Problems</h2>
<p> The optimiser on HP-UX 11.23 (Itanium 2) is currently partly disabled (scaled down to +O1) when using <font SIZE="-1">HP</font> C-ANSI-C; the cause of problems at higher optimisation levels is still unclear. </p>
<p> There are a handful of remaining test failures on <font SIZE="-1">VMS,</font> mostly due to test fixes and minor module tweaks with too many dependencies to integrate into this release from the development stream, where they have all been corrected. The following is a list of expected failures with the patch number of the fix where that is known: </p>
<pre>
    ext/Devel/PPPort/t/ppphtest.t  #26913
    ext/List/Util/t/p_tainted.t    #26912
    lib/ExtUtils/t/PL_FILES.t      #26813
    lib/ExtUtils/t/basic.t         #26813
    t/io/fs.t
    t/op/cmp.t
</pre>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://bugs.perl.org.">http://bugs.perl.org.</a> There may also be information at <a rel="nofollow" href="http://www.perl.org,">http://www.perl.org,</a> the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. You can browse and search the Perl 5 bugs at <a rel="nofollow" href="http://bugs.perl.org/">http://bugs.perl.org/</a></p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
<h2>Index</h2>
<dt><a href="#lbAS">New or Changed Diagnostics</a></p>
<dd>
<dt><a href="#lbAW">Changed Internals</a></p>
<dd>
<dt><a href="#lbAX">Platform Specific Problems</a></p>
<dd>
<dt><a href="#lbAY">Reporting Bugs</a></p>
<dd>
<dt><a href="#lbAZ">SEE ALSO</a></p>
<dd></dl>
