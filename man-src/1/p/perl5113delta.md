---
title: "perl5113delta(1)"
name: "perl5113delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5113delta/"
description: "perl5113delta – what is new for perl v5.11.3"
---

<h2 class="name">NAME</h2>
<p> perl5113delta &#8211; what is new for perl v5.11.3 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.11.2 release and the 5.11.3 release. </p>
<p> If you are upgrading from an earlier release such as 5.11.1, first read the perl5112delta, which describes differences between 5.11.1 and 5.11.2</p>
<h2>Incompatible Changes</h2>
<h3>Filehandles are blessed directly into IO::Handle, as FileHandle is merely a wrapper around IO::Handle.</h3>
<p> The previous behaviour was to bless Filehandles into FileHandle (an empty proxy class) if it was loaded into memory and otherwise to bless them into <tt>&quot;IO::Handle&quot;</tt>.</p>
<h2>Core Enhancements</h2>
<h3>Unicode version</h3>
<p> Perl is shipped with the latest Unicode version, 5.2, dated October 2009. See &lt;<a rel="nofollow" href="http://www.unicode.org/versions/Unicode5.2.0">http://www.unicode.org/versions/Unicode5.2.0</a>&gt; for details about this release of Unicode. See perlunicode for instructions on installing and using older versions of Unicode.</p>
<h3>Unicode properties</h3>
<p> Perl can now handle every Unicode character property. A new pod, perluniprops, lists all available non-Unihan character properties. By default the Unihan properties and certain others (deprecated and Unicode internal-only ones) are not exposed. See below for more details on these; there is also a section in the pod listing them, and why they are not exposed. </p>
<p> Perl now fully supports the Unicode compound-style of using <tt>&quot;=&quot;</tt> and <tt>&quot;:&quot;</tt> in writing regular expressions: <tt>&quot;\p{property=value}&quot;</tt> and <tt>&quot;\p{property:value}&quot;</tt> (both of which mean the same thing). </p>
<p> Perl now fully supports the Unicode loose matching rules for text between the braces in <tt>&quot;\p{...}&quot;</tt> constructs. In addition, Perl also allows underscores between digits of numbers. </p>
<p> All the Unicode-defined synonyms for properties and property values are now accepted. </p>
<p> <tt>&quot;qr/\X/&quot;</tt>, which matches a Unicode logical character, has been expanded to work better with various Asian languages. It now is defined as an <tt>&quot;extended grapheme cluster&quot;</tt>. (See &lt;<a rel="nofollow" href="http://www.unicode.org/reports/tr29/">http://www.unicode.org/reports/tr29/</a>&gt;). Anything matched previously that made sense will continue to be matched. But in addition:</p>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;\X&quot;</tt> will now not break apart a <tt>&quot;CR LF&quot;</tt> sequence.</p>
<dt>&bull;</p>
<dd> <tt>&quot;\X&quot;</tt> will now match a sequence including the <tt>&quot;ZWJ&quot;</tt> and <tt>&quot;ZWNJ&quot;</tt> characters.</p>
<dt>&bull;</p>
<dd> <tt>&quot;\X&quot;</tt> will now always match at least one character, including an initial mark. Marks generally come after a base character, but it is possible in Unicode to have them in isolation, and <tt>&quot;\X&quot;</tt> will now handle that case, for example at the beginning of a line or after a <tt>&quot;ZWSP&quot;</tt>. And this is the part where <tt>&quot;\X&quot;</tt> doesn&#8217;t match the things that it used to that don&#8217;t make sense. Formerly, for example, you could have the nonsensical case of an accented <font SIZE="-1">LF</font>.</p>
<dt>&bull;</p>
<dd> <tt>&quot;\X&quot;</tt> will now match a (Korean) Hangul syllable sequence, and the Thai and Lao exception cases.</dl>
<p> Otherwise, this change should be transparent for the non-affected languages. </p>
<p> <tt>&quot;\p{...}&quot;</tt> matches using the Canonical_Combining_Class property were completely broken in previous Perls. This is now fixed. </p>
<p> In previous Perls, the Unicode <tt>&quot;Decomposition_Type=Compat&quot;</tt> property and a Perl extension had the same name, which led to neither matching all the correct values (with more than 100 mistakes in one, and several thousand in the other). The Perl extension has now been renamed to be <tt>&quot;Decomposition_Type=Noncanonical&quot;</tt> (short: <tt>&quot;dt=noncanon&quot;</tt>). It has the same meaning as was previously intended, namely the union of all the non-canonical Decomposition types, with Unicode <tt>&quot;Compat&quot;</tt> being just one of those. </p>
<p> <tt>&quot;\p{Uppercase}&quot;</tt> and <tt>&quot;\p{Lowercase}&quot;</tt> have been brought into line with the Unicode definitions. This means they each match a few more characters than previously. </p>
<p> <tt>&quot;\p{Cntrl}&quot;</tt> now matches the same characters as <tt>&quot;\p{Control}&quot;</tt>. This means it no longer will match Private Use (gc=co), Surrogates (gc=cs), nor Format (gc=cf) code points. The Format code points represent the biggest possible problem. All but 36 of them are either officially deprecated or strongly discouraged from being used. Of those 36, likely the most widely used are the soft hyphen (U+00AD), and <font SIZE="-1">BOM</font>, <font SIZE="-1">ZWSP</font>, <font SIZE="-1">ZWNJ</font>, <font SIZE="-1">WJ</font>, and similar, plus Bi-directional controls. </p>
<p> <tt>&quot;\p{Alpha}&quot;</tt> now matches the same characters as <tt>&quot;\p{Alphabetic}&quot;</tt>. The Perl definition included a number of things that aren&#8217;t really alpha (all marks), while omitting many that were. As a direct consequence, the definitions of <tt>&quot;\p{Alnum}&quot;</tt> and <tt>&quot;\p{Word}&quot;</tt> which depend on Alpha also change. </p>
<p> <tt>&quot;\p{Word}&quot;</tt> also now doesn&#8217;t match certain characters it wasn&#8217;t supposed to, such as fractions. </p>
<p> <tt>&quot;\p{Print}&quot;</tt> no longer matches the line control characters: Tab, <font SIZE="-1">LF</font>, <font SIZE="-1">CR</font>, <font SIZE="-1">FF</font>, <font SIZE="-1">VT</font>, and <font SIZE="-1">NEL</font>. This brings it in line with the documentation. </p>
<p> <tt>&quot;\p{Decomposition_Type=Canonical}&quot;</tt> now includes the Hangul syllables. </p>
<p> The Numeric type property has been extended to include the Unihan characters. </p>
<p> There is a new Perl extension, the &#8216;Present_In&#8217;, or simply &#8216;In&#8217;, property. This is an extension of the Unicode Age property, but <tt>&quot;\p{In=5.0}&quot;</tt> matches any code point whose usage has been determined <i>as of</i> Unicode version 5.0. The <tt>&quot;\p{Age=5.0}&quot;</tt> only matches code points added in <i>precisely</i> version 5.0. </p>
<p> A number of properties did not have the correct values for unassigned code points. This is now fixed. The affected properties are Bidi_Class, East_Asian_Width, Joining_Type, Decomposition_Type, Hangul_Syllable_Type, Numeric_Type, and Line_Break. </p>
<p> The Default_Ignorable_Code_Point, ID_Continue, and ID_Start properties have been updated to their current Unicode definitions. </p>
<p> Certain properties that are supposed to be Unicode internal-only were erroneously exposed by previous Perls. Use of these in regular expressions will now generate, if enabled, a deprecated warning message. The properties are: Other_Alphabetic, Other_Default_Ignorable_Code_Point, Other_Grapheme_Extend, Other_ID_Continue, Other_ID_Start, Other_Lowercase, Other_Math, and Other_Uppercase. </p>
<p> An installation can now fairly easily change which Unicode properties Perl understands. As mentioned above, certain properties are by default turned off. These include all the Unihan properties (which should be accessible via the <font SIZE="-1">CPAN</font> module Unicode::Unihan) and any deprecated or Unicode internal-only property that Perl has never exposed. </p>
<p> The generated files in the <tt>&quot;lib/unicore/To&quot;</tt> directory are now more clearly marked as being stable, directly usable by applications. New hash entries in them give the format of the normal entries, which allows for easier machine parsing. Perl can generate files in this directory for any property, though most are suppressed. An installation can choose to change which get written. Instructions are in perluniprops.</p>
<h3>Regular Expressions</h3>
<p> U+0FFFF is now a legal character in regular expressions.</p>
<h2>Modules and Pragmata</h2>
<h3>Pragmata Changes</h3>
<dl>
<dt>&quot;constant&quot;</p>
<dd> Upgraded from version 1.19 to 1.20.</p>
<dt>&quot;diagnostics&quot;</p>
<dd> This pragma no longer suppresses <tt>&quot;Use of uninitialized value in range (or flip)&quot;</tt> warnings. [perl #71204]</p>
<dt>&quot;feature&quot;</p>
<dd> Upgraded from 1.13 to 1.14. Added the <tt>&quot;unicode_strings&quot;</tt> feature: </p>
<pre>
    use feature &quot;unicode_strings&quot;;
</pre>
<p> This pragma turns on Unicode semantics for the case-changing operations (uc/lc/ucfirst/lcfirst) on strings that don&#8217;t have the internal <font SIZE="-1">UTF-8</font> flag set, but that contain single-byte characters between 128 and 255.</p>
<dt>&quot;legacy&quot;</p>
<dd> The experimental <tt>&quot;legacy&quot;</tt> pragma, introduced in 5.11.2, has been removed, and its functionality replaced by the new feature pragma, <tt>&quot;use feature &quot;unicode_strings&quot;&quot;</tt>.</p>
<dt>&quot;threads&quot;</p>
<dd> Upgraded from version 1.74 to 1.75.</p>
<dt>&quot;warnings&quot;</p>
<dd> Upgraded from 1.07 to 1.08. Added new <tt>&quot;warnings::fatal_enabled()&quot;</tt> function.</dl>
<h3>Updated Modules</h3>
<dl>
<dt>&quot;Archive::Extract&quot;</p>
<dd> Upgraded from version 0.34 to 0.36.</p>
<dt>&quot;CPAN&quot;</p>
<dd> Upgraded from version 1.94_51 to 1.94_5301, which is 1.94_53 on <font SIZE="-1">CPAN</font> plus some local fixes for bleadperl. </p>
<p> Includes better bzip2 support, improved FirstTime experience with auto-selection of <font SIZE="-1">CPAN</font> mirrors, proper handling of modules removed from the Perl core, and an updated &#8216;cpan&#8217; utility script</p>
<dt>&quot;CPANPLUS&quot;</p>
<dd> Upgraded from version 0.89_09 to 0.90.</p>
<dt>&quot;Encode&quot;</p>
<dd> Upgraded from version 2.38 to 2.39.</p>
<dt>&quot;ExtUtils::MakeMaker&quot;</p>
<dd> Upgraded from version 6.55_02 to 6.56. Adds new <font SIZE="-1">BUILD_REQUIRES</font> key to indicate build-only prerequisites. Also adds support for mingw64 and the new &#8220;package <font SIZE="-1">NAME</font> <font SIZE="-1">VERSION</font>&#8221; syntax.</p>
<dt>&quot;File::Path&quot;</p>
<dd> Upgraded from version 2.08 to 2.08_01.</p>
<dt>&quot;Module::Build&quot;</p>
<dd> Upgraded from version 0.35_09 to 0.36. Compared to 0.35, this version has a new &#8216;installdeps&#8217; action, supports the <font SIZE="-1">PERL_MB_OPT</font> environment variable, adds a &#8216;share_dir&#8217; property for File::ShareDir support, support the &#8220;package <font SIZE="-1">NAME</font> <font SIZE="-1">VERSION</font>&#8221; syntax and has many other enhancements and bug fixes. The &#8216;passthrough&#8217; style of Module::Build::Compat has been deprecated.</p>
<dt>&quot;Module::CoreList&quot;</p>
<dd> Upgraded from version 2.23 to 2.24.</p>
<dt>&quot;POSIX&quot;</p>
<dd> Upgraded from version 1.18 to 1.19. Error codes for <tt>&quot;getaddrinfo()&quot;</tt> and <tt>&quot;getnameinfo()&quot;</tt> are now available.</p>
<dt>&quot;Pod::Simple&quot;</p>
<dd> Upgraded from version 3.10 to 3.13.</p>
<dt>&quot;Safe&quot;</p>
<dd> Upgraded from version 2.19 to 2.20.</dl>
<h2>Utility Changes</h2>
<dl>
<dt><i>perlbug</i></p>
<dd> No longer reports &#8220;Message sent&#8221; when it hasn&#8217;t actually sent the message</dl>
<h2>Changes to Existing Documentation</h2>
<p> The Pod specification (perlpodspec) has been updated to bring the specification in line with modern usage already supported by most Pod systems. A parameter string may now follow the format name in a &#8220;begin/end&#8221; region. Links to URIs with a text description are now allowed. The usage of <tt>&quot;L&lt;&quot;section&quot;&gt;&quot;</tt> has been marked as deprecated. </p>
<p> if.pm has been documented in &#8220;use&#8221; in perlfunc as a means to get conditional loading of modules despite the implicit <font SIZE="-1">BEGIN</font> block around <tt>&quot;use&quot;</tt>.</p>
<h2>Installation and Configuration Improvements</h2>
<h3>Testing improvements</h3>
<dl>
<dt>It&#8217;s now possible to override &quot;PERL5OPT&quot; and friends in <i>t/TEST</i></p>
<dd></dl>
<h3>Platform Specific Changes</h3>
<dl>
<dt>Win32</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Always add a manifest resource to <tt>&quot;perl.exe&quot;</tt> to specify the <tt>&quot;trustInfo&quot;</tt> settings for Windows Vista and later. Without this setting Windows will treat <tt>&quot;perl.exe&quot;</tt> as a legacy application and apply various heuristics like redirecting access to protected file system areas (like the &#8220;Program Files&#8221; folder) to the users &#8220;VirtualStore&#8221; instead of generating a proper &#8220;permission denied&#8221; error. </p>
<p> For <font SIZE="-1">VC8</font> and <font SIZE="-1">VC9</font> this manifest setting is automatically generated by the compiler/linker (together with the binding information for their respective runtime libraries); for all other compilers we need to embed the manifest resource explicitly in the external resource file. </p>
<p> This change also requests the Microsoft Common-Controls version 6.0 (themed controls introduced in Windows <font SIZE="-1">XP</font>) via the dependency list in the assembly manifest. For <font SIZE="-1">VC8</font> and <font SIZE="-1">VC9</font> this is specified using the <tt>&quot;/manifestdependency&quot;</tt> linker commandline option instead.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>cygwin</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>Enable IPv6 support on cygwin 1.7 and newer</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>OpenVMS</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>Make -UDEBUGGING the default on <font SIZE="-1">VMS</font> for 5.12.0.</p>
<dd> Like it has been everywhere else for ages and ages. Also make command-line selection of -UDEBUGGING and -DDEBUGGING work in configure.com; before the only way to turn it off was by saying no in answer to the interactive question.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</p>
<dd> Ensure that pp_qr returns a new regexp <font SIZE="-1">SV</font> each time. Resolves <font SIZE="-1">RT</font> #69852. </p>
<p> Instead of returning a(nother) reference to the (pre-compiled) regexp in the optree, use <i>reg_temp_copy()</i> to create a copy of it, and return a reference to that. This resolves issues about Regexp::DESTROY not being called in a timely fashion (the original bug tracked by <font SIZE="-1">RT</font> #69852), as well as bugs related to blessing regexps, and of assigning to regexps, as described in correspondence added to the ticket. </p>
<p> It transpires that we also need to undo the <i>SvPVX()</i> sharing when ithreads cloning a Regexp <font SIZE="-1">SV</font>, because mother_re is set to <font SIZE="-1">NULL</font>, instead of a cloned copy of the mother_re. This change might fix bugs with regexps and threads in certain other situations, but as yet neither tests nor bug reports have indicated any problems, so it might not actually be an edge case that it&#8217;s possible to reach.</p>
<dt>&bull;</p>
<dd> Several compilation errors and segfaults when perl was built with <tt>&quot;-Dmad&quot;</tt> were fixed.</p>
<dt>&bull;</p>
<dd> Fixes for lexer <font SIZE="-1">API</font> changes in 5.11.2 which broke NYTProf&#8217;s savesrc option.</p>
<dt>&bull;</p>
<dd> <i>-t</i> should only return <font SIZE="-1">TRUE</font> for file handles connected to a <font SIZE="-1">TTY</font> </p>
<p> The Microsoft C version of <i>isatty()</i> returns <font SIZE="-1">TRUE</font> for all character mode devices, including the /dev/null style &#8220;nul&#8221; device and printers like &#8220;lpt1&#8221;.</p>
<dt>&bull;</p>
<dd> Fixed a regression caused by commit fafafbaf which caused a panic during parameter passing [perl #70171]</p>
<dt>&bull;</p>
<dd> On systems which in-place edits without backup files, -i&#8217;*&#8217; now works as the documentation says it does [perl #70802]</p>
<dt>&bull;</p>
<dd> Saving and restoring magic flags no longer loses readonly flag.</p>
<dt>&bull;</p>
<dd> The malformed syntax <tt>&quot;grep EXPR LIST&quot;</tt> (note the missing comma) no longer causes abrupt and total failure.</p>
<dt>&bull;</p>
<dd> Regular expressions compiled with <tt>&quot;qr{}&quot;</tt> literals properly set <tt>&quot;$'&quot;</tt> when matching again.</p>
<dt>&bull;</p>
<dd> Using named subroutines with <tt>&quot;sort&quot;</tt> should no longer lead to bus errors [perl #71076]</p>
<dt>&bull;</p>
<dd> Numerous bugfixes catch small issues caused by the recently-added Lexer <font SIZE="-1">API</font>.</p>
<dt>&bull;</p>
<dd> Smart match against <tt>@_</tt> sometimes gave false negatives. [perl #71078]</p>
<dt>&bull;</p>
<dd> <tt>$@</tt> may now be assigned a read-only value (without error or busting the stack).</p>
<dt>&bull;</p>
<dd> <tt>&quot;sort&quot;</tt> called recursively from within an active comparison subroutine no longer causes a bus error if run multiple times. [perl #71076]</dl>
<h2>New or Changed Diagnostics</h2>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;split&quot;</tt> now warns when called in void context</p>
<dt>&bull;</p>
<dd> <tt>&quot;printf&quot;</tt>-style functions called with too few arguments will now issue the warning <tt>&quot;Missing argument in %s&quot;</tt> [perl #71000]</dl>
<h2>New Tests</h2>
<p> Many modules updated from <font SIZE="-1">CPAN</font> incorporate new tests.</p>
<dl>
<dt>t/comp/final_line_num.t</p>
<dd> See if line numbers are correct at <font SIZE="-1">EOF</font></p>
<dt>t/comp/form_scope.t</p>
<dd> See if format scoping works</p>
<dt>t/comp/line_debug.t</p>
<dd> See if @{&#8220;_&lt;$file&#8221;} works</p>
<dt>t/op/filetest_t.t</p>
<dd> See if -t file test works</p>
<dt>t/op/qr.t</p>
<dd> See if qr works</p>
<dt>t/op/utf8cache.t</p>
<dd> Tests malfunctions of utf8 cache</p>
<dt>t/re/uniprops.t</p>
<dd> Test unicode \p{} regex constructs</dl>
<h2>Deprecations</h2>
<p> The following items are now deprecated.</p>
<dl>
<dt>Use of &quot;goto&quot; to jump into a construct is deprecated</p>
<dd> Using <tt>&quot;goto&quot;</tt> to jump from an outer scope into an inner scope is now deprecated. This rare use case was causing problems in the implementation of scopes.</dl>
<h2>Acknowledgements</h2>
<p> Perl 5.11.3 represents approximately one month of development since Perl 5.11.2 and contains 61407 lines of changes across 396 files from 40 authors and committers: </p>
<p> Abigail, Alex Davies, Alexandr Ciornii, Andrew Rodland, Andy Dougherty, Bram, brian d foy, Chip Salzenberg, Chris Williams, Craig A. Berry, Daniel Frederick Crisman, David Golden, Dennis Kaarsemaker, Eric Brine, Father Chrysostomos, Gene Sullivan, Gerard Goossen, H. Merijn Brand, Hugo van der Sanden, Jan Dubois, Jerry D. Hedden, Jesse Vincent, Jim Cromie, Karl Williamson, Leon Brocard, Max Maischein, Michael Breen, Moritz Lenz, Nicholas Clark, Rafael Garcia-Suarez, Reini Urban, Ricardo Signes, Stepan Kasal, Steve Hay, Steve Peters, Tim Bunce, Tony Cook, Vincent Pit and Zefram. </p>
<p> Many of the changes included in this version originated in the <font SIZE="-1">CPAN</font> modules included in Perl&#8217;s core. We&#8217;re grateful to the entire <font SIZE="-1">CPAN</font> community for helping Perl to flourish.</p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://rt.perl.org/perlbug/">http://rt.perl.org/perlbug/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on <font SIZE="-1">CPAN</font>.</p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
<h2>Index</h2>
