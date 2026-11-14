---
title: "perl58delta(1)"
name: "perl58delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl58delta/"
description: "perl58delta – what is new for perl v5.8.0"
---

<h2 class="name">NAME</h2>
<p> perl58delta &#8211; what is new for perl v5.8.0 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.6.0 release and the 5.8.0 release. </p>
<p> Many of the bug fixes in 5.8.0 were already seen in the 5.6.1 maintenance release since the two releases were kept closely coordinated (while 5.8.0 was still called 5.7.something). </p>
<p> Changes that were integrated into the 5.6.1 release are marked <tt>&quot;[561]&quot;</tt>. Many of these changes have been further developed since 5.6.1 was released, those are marked <tt>&quot;[561+]&quot;</tt>. </p>
<p> You can see the list of changes in the 5.6.1 release (both from the 5.005_03 release and the 5.6.0 release) by reading perl561delta.</p>
<h2>Highlights In 5.8.0</h2>
<dl>
<dt>&bull;</p>
<dd> Better Unicode support</p>
<dt>&bull;</p>
<dd> New <font SIZE="-1">IO</font> Implementation</p>
<dt>&bull;</p>
<dd> New Thread Implementation</p>
<dt>&bull;</p>
<dd> Better Numeric Accuracy</p>
<dt>&bull;</p>
<dd> Safe Signals</p>
<dt>&bull;</p>
<dd> Many New Modules</p>
<dt>&bull;</p>
<dd> More Extensive Regression Testing</dl>
<h2>Incompatible Changes</h2>
<h3>Binary Incompatibility</h3>
<p> <code>Perl 5.8 is not binary compatible with earlier releases of Perl.</code> </p>
<p> <code>You have to recompile your </code><font SIZE="-1"><code>XS</code></font><code> modules.</code> </p>
<p> (Pure Perl modules should continue to work.) </p>
<p> The major reason for the discontinuity is the new <font SIZE="-1">IO</font> architecture called PerlIO. PerlIO is the default configuration because without it many new features of Perl 5.8 cannot be used. In other words: you just have to recompile your modules containing <font SIZE="-1">XS</font> code, sorry about that. </p>
<p> In future releases of Perl, non-PerlIO aware <font SIZE="-1">XS</font> modules may become completely unsupported. This shouldn&#8217;t be too difficult for module authors, however: PerlIO has been designed as a drop-in replacement (at the source code level) for the stdio interface. </p>
<p> Depending on your platform, there are also other reasons why we decided to break binary compatibility, please read on.</p>
<h3>64-bit platforms and malloc</h3>
<p> If your pointers are 64 bits wide, the Perl malloc is no longer being used because it does not work well with 8-byte pointers. Also, usually the system mallocs on such platforms are much better optimized for such large memory models than the Perl malloc. Some memory-hungry Perl applications like the <font SIZE="-1">PDL</font> don&#8217;t work well with Perl&#8217;s malloc. Finally, other applications than Perl (such as mod_perl) tend to prefer the system malloc. Such platforms include Alpha and 64-bit <font SIZE="-1">HPPA, MIPS, PPC,</font> and Sparc.</p>
<h3><font SIZE="-1">AIX</font> Dynaloading</h3>
<p> The <font SIZE="-1">AIX</font> dynaloading now uses in <font SIZE="-1">AIX</font> releases 4.3 and newer the native dlopen interface of <font SIZE="-1">AIX</font> instead of the old emulated interface. This change will probably break backward compatibility with compiled modules. The change was made to make Perl more compliant with other applications like mod_perl which are using the <font SIZE="-1">AIX</font> native interface.</p>
<h3>Attributes for my variables now handled at run-time</h3>
<p> The <tt>&quot;my EXPR : ATTRS&quot;</tt> syntax now applies variable attributes at run-time. (Subroutine and <tt>&quot;our&quot;</tt> variables still get attributes applied at compile-time.) See attributes for additional details. In particular, however, this allows variable attributes to be useful for <tt>&quot;tie&quot;</tt> interfaces, which was a deficiency of earlier releases. Note that the new semantics doesn&#8217;t work with the Attribute::Handlers module (as of version 0.76).</p>
<h3>Socket Extension Dynamic in <font SIZE="-1">VMS</font></h3>
<p> The Socket extension is now dynamically loaded instead of being statically built in. This may or may not be a problem with ancient <font SIZE="-1">TCP/IP</font> stacks of <font SIZE="-1">VMS:</font> we do not know since we weren&#8217;t able to test Perl in such configurations.</p>
<h3>IEEE-format Floating Point Default on OpenVMS Alpha</h3>
<p> Perl now uses <font SIZE="-1">IEEE</font> format (T_FLOAT) as the default internal floating point format on OpenVMS Alpha, potentially breaking binary compatibility with external libraries or existing data. G_FLOAT is still available as a configuration option. The default on <font SIZE="-1">VAX</font> (D_FLOAT) has not changed.</p>
<h3>New Unicode Semantics (no more use utf8, almost)</h3>
<p> Previously in Perl 5.6 to use Unicode one would say &#8220;use utf8&#8221; and then the operations (like string concatenation) were Unicode-aware in that lexical scope. </p>
<p> This was found to be an inconvenient interface, and in Perl 5.8 the Unicode model has completely changed: now the &#8220;Unicodeness&#8221; is bound to the data itself, and for most of the time &#8220;use utf8&#8221; is not needed at all. The only remaining use of &#8220;use utf8&#8221; is when the Perl script itself has been written in the <font SIZE="-1">UTF-8</font> encoding of Unicode. (<font SIZE="-1">UTF-8</font> has not been made the default since there are many Perl scripts out there that are using various national eight-bit character sets, which would be illegal in <font SIZE="-1">UTF-8.</font>) </p>
<p> See perluniintro for the explanation of the current model, and utf8 for the current use of the utf8 pragma.</p>
<h3>New Unicode Properties</h3>
<p> Unicode <i>scripts</i> are now supported. Scripts are similar to (and superior to) Unicode <i>blocks</i>. The difference between scripts and blocks is that scripts are the glyphs used by a language or a group of languages, while the blocks are more artificial groupings of (mostly) 256 characters based on the Unicode numbering. </p>
<p> In general, scripts are more inclusive, but not universally so. For example, while the script <tt>&quot;Latin&quot;</tt> includes all the Latin characters and their various diacritic-adorned versions, it does not include the various punctuation or digits (since they are not solely <tt>&quot;Latin&quot;</tt>). </p>
<p> A number of other properties are now supported, including <tt>&quot;\p{L&amp;}&quot;</tt>, <tt>&quot;\p{Any}&quot;</tt> <tt>&quot;\p{Assigned}&quot;</tt>, <tt>&quot;\p{Unassigned}&quot;</tt>, <tt>&quot;\p{Blank}&quot;</tt> [561] and <tt>&quot;\p{SpacePerl}&quot;</tt> [561] (along with their <tt>&quot;\P{...}&quot;</tt> versions, of course). See perlunicode for details, and more additions. </p>
<p> The <tt>&quot;In&quot;</tt> or <tt>&quot;Is&quot;</tt> prefix to names used with the <tt>&quot;\p{...}&quot;</tt> and <tt>&quot;\P{...}&quot;</tt> are now almost always optional. The only exception is that a <tt>&quot;In&quot;</tt> prefix is required to signify a Unicode block when a block name conflicts with a script name. For example, <tt>&quot;\p{Tibetan}&quot;</tt> refers to the script, while <tt>&quot;\p{InTibetan}&quot;</tt> refers to the block. When there is no name conflict, you can omit the <tt>&quot;In&quot;</tt> from the block name (e.g. <tt>&quot;\p{BraillePatterns}&quot;</tt>), but to be safe, it&#8217;s probably best to always use the <tt>&quot;In&quot;</tt>).</p>
<h3><font SIZE="-1">REF</font>(&#8230;) Instead Of <font SIZE="-1">SCALAR</font>(&#8230;)</h3>
<p> A reference to a reference now stringifies as &#8220;<font SIZE="-1">REF</font>(0x81485ec)&#8221; instead of &#8220;<font SIZE="-1">SCALAR</font>(0x81485ec)&#8221; in order to be more consistent with the return value of <code>ref()</code>.</p>
<h3>pack/unpack D/F recycled</h3>
<p> The undocumented pack/unpack template letters D/F have been recycled for better use: now they stand for long double (if supported by the platform) and <font SIZE="-1">NV</font> (Perl internal floating point type). (They used to be aliases for d/f, but you never knew that.)</p>
<h3><code>glob()</code> now returns filenames in alphabetical order</h3>
<p> The list of filenames from <code>glob()</code> (or &lt;&#8230;&gt;) is now by default sorted alphabetically to be csh-compliant (which is what happened before in most Unix platforms). (<code>bsd_glob()</code> does still sort platform natively, <font SIZE="-1">ASCII</font> or <font SIZE="-1">EBCDIC,</font> unless <font SIZE="-1">GLOB_ALPHASORT</font> is specified.) [561]</p>
<h3>Deprecations</h3>
<dl>
<dt>&bull;</p>
<dd> The semantics of bless(<font SIZE="-1">REF, REF</font>) were unclear and until someone proves it to make some sense, it is forbidden.</p>
<dt>&bull;</p>
<dd> The obsolete chat2 library that should never have been allowed to escape the laboratory has been decommissioned.</p>
<dt>&bull;</p>
<dd> Using chdir(&quot;&quot;) or chdir(undef) instead of explicit <code>chdir()</code> is doubtful. A failure (think chdir(<code>some_function()</code>) can lead into unintended <code>chdir()</code> to the home directory, therefore this behaviour is deprecated.</p>
<dt>&bull;</p>
<dd> The builtin <code>dump()</code> function has probably outlived most of its usefulness. The core-dumping functionality will remain in future available as an explicit call to <tt>&quot;CORE::dump()&quot;</tt>, but in future releases the behaviour of an unqualified <tt>&quot;dump()&quot;</tt> call may change.</p>
<dt>&bull;</p>
<dd> The very dusty examples in the eg/ directory have been removed. Suggestions for new shiny examples welcome but the main issue is that the examples need to be documented, tested and (most importantly) maintained.</p>
<dt>&bull;</p>
<dd> The (bogus) escape sequences \8 and \9 now give an optional warning (&#8220;Unrecognized escape passed through&#8221;). There is no need to \-escape any <tt>&quot;\w&quot;</tt> character.</p>
<dt>&bull;</p>
<dd> The *glob{<font SIZE="-1">FILEHANDLE</font>} is deprecated, use *glob{<font SIZE="-1">IO</font>} instead.</p>
<dt>&bull;</p>
<dd> The <tt>&quot;package;&quot;</tt> syntax (<tt>&quot;package&quot;</tt> without an argument) has been deprecated. Its semantics were never that clear and its implementation even less so. If you have used that feature to disallow all but fully qualified variables, <tt>&quot;use strict;&quot;</tt> instead.</p>
<dt>&bull;</p>
<dd> The unimplemented <font SIZE="-1">POSIX</font> regex features [[.cc.]] and [[=c=]] are still recognised but now cause fatal errors. The previous behaviour of ignoring them by default and warning if requested was unacceptable since it, in a way, falsely promised that the features could be used.</p>
<dt>&bull;</p>
<dd> In future releases, non-PerlIO aware <font SIZE="-1">XS</font> modules may become completely unsupported. Since PerlIO is a drop-in replacement for stdio at the source code level, this shouldn&#8217;t be that drastic a change.</p>
<dt>&bull;</p>
<dd> Previous versions of perl and some readings of some sections of Camel <font SIZE="-1">III</font> implied that the <tt>&quot;:raw&quot;</tt> &#8220;discipline&#8221; was the inverse of <tt>&quot;:crlf&quot;</tt>. Turning off &#8220;clrfness&#8221; is no longer enough to make a stream truly binary. So the PerlIO <tt>&quot;:raw&quot;</tt> layer (or &#8220;discipline&#8221;, to use the Camel book&#8217;s older terminology) is now formally defined as being equivalent to binmode(<font SIZE="-1">FH</font>) &#8211; which is in turn defined as doing whatever is necessary to pass each byte as-is without any translation. In particular binmode(<font SIZE="-1">FH</font>) &#8211; and hence <tt>&quot;:raw&quot;</tt> &#8211; will now turn off both <font SIZE="-1">CRLF</font> and <font SIZE="-1">UTF-8</font> translation and remove other layers (e.g. :<code>encoding()</code>) which would modify byte stream.</p>
<dt>&bull;</p>
<dd> The current user-visible implementation of pseudo-hashes (the weird use of the first array element) is deprecated starting from Perl 5.8.0 and will be removed in Perl 5.10.0, and the feature will be implemented differently. Not only is the current interface rather ugly, but the current implementation slows down normal array and hash use quite noticeably. The <tt>&quot;fields&quot;</tt> pragma interface will remain available. The <i>restricted hashes</i> interface is expected to be the replacement interface (see Hash::Util). If your existing programs depends on the underlying implementation, consider using Class::PseudoHash from <font SIZE="-1">CPAN.</font></p>
<dt>&bull;</p>
<dd> The syntaxes <tt>&quot;@a-&gt;[...]&quot;</tt> and <tt>&quot;%h-&gt;{...}&quot;</tt> have now been deprecated.</p>
<dt>&bull;</p>
<dd> After years of trying, suidperl is considered to be too complex to ever be considered truly secure. The suidperl functionality is likely to be removed in a future release.</p>
<dt>&bull;</p>
<dd> The 5.005 threads model (module <tt>&quot;Thread&quot;</tt>) is deprecated and expected to be removed in Perl 5.10. Multithreaded code should be migrated to the new ithreads model (see threads, threads::shared and perlthrtut).</p>
<dt>&bull;</p>
<dd> The long deprecated uppercase aliases for the string comparison operators (<font SIZE="-1">EQ, NE, LT, LE, GE, GT</font>) have now been removed.</p>
<dt>&bull;</p>
<dd> The tr///C and tr///U features have been removed and will not return; the interface was a mistake. Sorry about that. For similar functionality, see pack(&#8216;U0&#8217;, &#8230;) and pack(&#8216;C0&#8217;, &#8230;). [561]</p>
<dt>&bull;</p>
<dd> Earlier Perls treated &#8220;sub foo (@bar)&#8221; as equivalent to &#8220;sub foo (@)&#8221;. The prototypes are now checked better at compile-time for invalid syntax. An optional warning is generated (&#8220;Illegal character in prototype&#8230;&#8221;) but this may be upgraded to a fatal error in a future release.</p>
<dt>&bull;</p>
<dd> The <tt>&quot;exec LIST&quot;</tt> and <tt>&quot;system LIST&quot;</tt> operations now produce warnings on tainted data and in some future release they will produce fatal errors.</p>
<dt>&bull;</p>
<dd> The existing behaviour when localising tied arrays and hashes is wrong, and will be changed in a future release, so do not rely on the existing behaviour. See &#8220;Localising Tied Arrays and Hashes Is Broken&#8221;.</dl>
<h2>Core Enhancements</h2>
<h3>Unicode Overhaul</h3>
<p> Unicode in general should be now much more usable than in Perl 5.6.0 (or even in 5.6.1). Unicode can be used in hash keys, Unicode in regular expressions should work now, Unicode in tr/// should work now, Unicode in I/O should work now. See perluniintro for introduction and perlunicode for details.</p>
<dl>
<dt>&bull;</p>
<dd> The Unicode Character Database coming with Perl has been upgraded to Unicode 3.2.0. For more information, see <a rel="nofollow" href="http://www.unicode.org/">http://www.unicode.org/</a> . [561+] (5.6.1 has <font SIZE="-1">UCD 3.0.1.</font>)</p>
<dt>&bull;</p>
<dd> For developers interested in enhancing Perl&#8217;s Unicode capabilities: almost all the <font SIZE="-1">UCD</font> files are included with the Perl distribution in the <i>lib/unicore</i> subdirectory. The most notable omission, for space considerations, is the Unihan database.</p>
<dt>&bull;</p>
<dd> The properties \p{Blank} and \p{SpacePerl} have been added. &#8220;Blank&#8221; is like C <code>isblank()</code>, that is, it contains only &#8220;horizontal whitespace&#8221; (the space character is, the newline isn&#8217;t), and the &#8220;SpacePerl&#8221; is the Unicode equivalent of <tt>&quot;\s&quot;</tt> (\p{Space} isn&#8217;t, since that includes the vertical tabulator character, whereas <tt>&quot;\s&quot;</tt> doesn&#8217;t.) </p>
<p> See &#8220;New Unicode Properties&#8221; earlier in this document for additional information on changes with Unicode properties.</dl>
<h3>PerlIO is Now The Default</h3>
<dl>
<dt>&bull;</p>
<dd> <font SIZE="-1">IO</font> is now by default done via PerlIO rather than system&#8217;s &#8220;stdio&#8221;. PerlIO allows &#8220;layers&#8221; to be &#8220;pushed&#8221; onto a file handle to alter the handle&#8217;s behaviour. Layers can be specified at open time via 3-arg form of open: </p>
<pre>
   open($fh,'&gt;:crlf :utf8', $path) || ...
</pre>
<p> or on already opened handles via extended <tt>&quot;binmode&quot;</tt>: </p>
<pre>
   binmode($fh,':encoding(iso-8859-7)');
</pre>
<p> The built-in layers are: unix (low level read/write), stdio (as in previous Perls), perlio (re-implementation of stdio buffering in a portable manner), crlf (does <font SIZE="-1">CRLF</font> &lt;=&gt; &#8220;
&#8221; translation as on Win32, but available on any platform). A mmap layer may be available if platform supports it (mostly Unixes). </p>
<p> Layers to be applied by default may be specified via the &#8216;open&#8217; pragma. </p>
<p> See &#8220;Installation and Configuration Improvements&#8221; for the effects of PerlIO on your architecture name.</p>
<dt>&bull;</p>
<dd> If your platform supports <code>fork()</code>, you can use the list form of <tt>&quot;open&quot;</tt> for pipes. For example: </p>
<pre>
    open KID_PS, &quot;-|&quot;, &quot;ps&quot;, &quot;aux&quot; or die $!;
</pre>
<p> forks the <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1) command (without spawning a shell, as there are more than three arguments to <code>open()</code>), and reads its standard output via the <tt>&quot;KID_PS&quot;</tt> filehandle. See perlipc.</p>
<dt>&bull;</p>
<dd> File handles can be marked as accepting Perl&#8217;s internal encoding of Unicode (<font SIZE="-1">UTF-8</font> or UTF-EBCDIC depending on platform) by a pseudo layer &#8220;:utf8&#8221; : </p>
<pre>
   open($fh,&quot;&gt;:utf8&quot;,&quot;Uni.txt&quot;);
</pre>
<p> Note for <font SIZE="-1">EBCDIC</font> users: the pseudo layer &#8220;:utf8&#8221; is erroneously named for you since it&#8217;s not <font SIZE="-1">UTF-8</font> what you will be getting but instead UTF-EBCDIC. See perlunicode, utf8, and <a rel="nofollow" href="http://www.unicode.org/unicode/reports/tr16/">http://www.unicode.org/unicode/reports/tr16/</a> for more information. In future releases this naming may change. See perluniintro for more information about <font SIZE="-1">UTF-8.</font></p>
<dt>&bull;</p>
<dd> If your environment variables (<font SIZE="-1">LC_ALL, LC_CTYPE, LANG</font>) look like you want to use <font SIZE="-1">UTF-8</font> (any of the variables match <tt>&quot;/utf-?8/i&quot;</tt>), your <font SIZE="-1">STDIN, STDOUT, STDERR</font> handles and the default open layer (see open) are marked as <font SIZE="-1">UTF-8.</font> (This feature, like other new features that combine Unicode and I/O, work only if you are using PerlIO, but that&#8217;s the default.) </p>
<p> Note that after this Perl really does assume that everything is <font SIZE="-1">UTF-8:</font> for example if some input handle is not, Perl will probably very soon complain about the input data like this &#8220;Malformed <font SIZE="-1">UTF-8 &#8230;&#8221;</font> since any old eight-bit data is not legal <font SIZE="-1">UTF-8.</font> </p>
<p> Note for code authors: if you want to enable your users to use <font SIZE="-1">UTF-8</font> as their default encoding but in your code still have eight-bit I/O streams (such as images or zip files), you need to explicitly <code>open()</code> or <code>binmode()</code> with <tt>&quot;:bytes&quot;</tt> (see &#8220;open&#8221; in perlfunc and &#8220;binmode&#8221; in perlfunc), or you can just use <tt>&quot;binmode(FH)&quot;</tt> (nice for pre-5.8.0 backward compatibility).</p>
<dt>&bull;</p>
<dd> File handles can translate character encodings from/to Perl&#8217;s internal Unicode form on read/write via the &#8220;:<code>encoding()</code>&#8221; layer.</p>
<dt>&bull;</p>
<dd> File handles can be opened to &#8220;in memory&#8221; files held in Perl scalars via: </p>
<pre>
   open($fh,'&gt;', \$variable) || ...
</pre>
<dt>&bull;</p>
<dd> Anonymous temporary files are available without need to &#8216;use FileHandle&#8217; or other module via </p>
<pre>
   open($fh,&quot;+&gt;&quot;, undef) || ...
</pre>
<p> That is a literal undef, not an undefined value.</dl>
<h3>ithreads</h3>
<p> The new interpreter threads (&#8220;ithreads&#8221; for short) implementation of multithreading, by Arthur Bergman, replaces the old &#8220;5.005 threads&#8221; implementation. In the ithreads model any data sharing between threads must be explicit, as opposed to the model where data sharing was implicit. See threads and threads::shared, and perlthrtut. </p>
<p> As a part of the ithreads implementation Perl will also use any necessary and detectable reentrant libc interfaces.</p>
<h3>Restricted Hashes</h3>
<p> A restricted hash is restricted to a certain set of keys, no keys outside the set can be added. Also individual keys can be restricted so that the key cannot be deleted and the value cannot be changed. No new syntax is involved: the Hash::Util module is the interface.</p>
<h3>Safe Signals</h3>
<p> Perl used to be fragile in that signals arriving at inopportune moments could corrupt Perl&#8217;s internal state. Now Perl postpones handling of signals until it&#8217;s safe (between opcodes). </p>
<p> This change may have surprising side effects because signals no longer interrupt Perl instantly. Perl will now first finish whatever it was doing, like finishing an internal operation (like <code>sort()</code>) or an external operation (like an I/O operation), and only then look at any arrived signals (and before starting the next operation). No more corrupt internal state since the current operation is always finished first, but the signal may take more time to get heard. Note that breaking out from potentially blocking operations should still work, though.</p>
<h3>Understanding of Numbers</h3>
<p> In general a lot of fixing has happened in the area of Perl&#8217;s understanding of numbers, both integer and floating point. Since in many systems the standard number parsing functions like <tt>&quot;strtoul()&quot;</tt> and <tt>&quot;atof()&quot;</tt> seem to have bugs, Perl tries to work around their deficiencies. This results hopefully in more accurate numbers. </p>
<p> Perl now tries internally to use integer values in numeric conversions and basic arithmetics (+ &#8211; * /) if the arguments are integers, and tries also to keep the results stored internally as integers. This change leads to often slightly faster and always less lossy arithmetics. (Previously Perl always preferred floating point numbers in its math.)</p>
<h3>Arrays now always interpolate into double-quoted strings [561]</h3>
<p> In double-quoted strings, arrays now interpolate, no matter what. The behavior in earlier versions of perl 5 was that arrays would interpolate into strings if the array had been mentioned before the string was compiled, and otherwise Perl would raise a fatal compile-time error. In versions 5.000 through 5.003, the error was </p>
<pre>
        Literal @example now requires backslash
</pre>
<p> In versions 5.004_01 through 5.6.0, the error was </p>
<pre>
        In string, @example now must be written as \@example
</pre>
<p> The idea here was to get people into the habit of writing <tt>&quot;fred\@example.com&quot;</tt> when they wanted a literal <tt>&quot;@&quot;</tt> sign, just as they have always written <tt>&quot;Give me back my \$5&quot;</tt> when they wanted a literal <tt>&quot;$&quot;</tt> sign. </p>
<p> Starting with 5.6.1, when Perl now sees an <tt>&quot;@&quot;</tt> sign in a double-quoted string, it <i>always</i> attempts to interpolate an array, regardless of whether or not the array has been used or declared already. The fatal error has been downgraded to an optional warning: </p>
<pre>
        Possible unintended interpolation of @example in string
</pre>
<p> This warns you that <tt>&quot;fred [at] example.com&quot;</tt> is going to turn into <tt>&quot;fred.com&quot;</tt> if you don&#8217;t backslash the <tt>&quot;@&quot;</tt>. See <a rel="nofollow" href="http://perl.plover.com/at-error.html">http://perl.plover.com/at-error.html</a> for more details about the history here.</p>
<h3>Miscellaneous Changes</h3>
<dl>
<dt>&bull;</p>
<dd> <font SIZE="-1">AUTOLOAD</font> is now lvaluable, meaning that you can add the :lvalue attribute to <font SIZE="-1">AUTOLOAD</font> subroutines and you can assign to the <font SIZE="-1">AUTOLOAD</font> return value.</p>
<dt>&bull;</p>
<dd> The <tt>$Config</tt>{byteorder} (and corresponding <font SIZE="-1">BYTEORDER</font> in config.h) was previously wrong in platforms if sizeof(long) was 4, but sizeof(<font SIZE="-1">IV</font>) was 8. The byteorder was only sizeof(long) bytes long (1234 or 4321), but now it is correctly sizeof(<font SIZE="-1">IV</font>) bytes long, (12345678 or 87654321). (This problem didn&#8217;t affect Windows platforms.) </p>
<p> Also, <tt>$Config</tt>{byteorder} is now computed dynamically&#8212;this is more robust with &#8220;fat binaries&#8221; where an executable image contains binaries for more than one binary platform, and when cross-compiling.</p>
<dt>&bull;</p>
<dd> <tt>&quot;perl -d:Module=arg,arg,arg&quot;</tt> now works (previously one couldn&#8217;t pass in multiple arguments.)</p>
<dt>&bull;</p>
<dd> <tt>&quot;do&quot;</tt> followed by a bareword now ensures that this bareword isn&#8217;t a keyword (to avoid a bug where <tt>&quot;do q(foo.pl)&quot;</tt> tried to call a subroutine called <tt>&quot;q&quot;</tt>). This means that for example instead of <tt>&quot;do format()&quot;</tt> you must write <tt>&quot;do &amp;format()&quot;</tt>.</p>
<dt>&bull;</p>
<dd> The builtin <code>dump()</code> now gives an optional warning <tt>&quot;dump() better written as CORE::dump()&quot;</tt>, meaning that by default <tt>&quot;dump(...)&quot;</tt> is resolved as the builtin <code>dump()</code> which dumps core and aborts, not as (possibly) user-defined <tt>&quot;sub dump&quot;</tt>. To call the latter, qualify the call as <tt>&quot;&amp;dump(...)&quot;</tt>. (The whole <code>dump()</code> feature is to considered deprecated, and possibly removed/changed in future releases.)</p>
<dt>&bull;</p>
<dd> <code>chomp()</code> and <code>chop()</code> are now overridable. Note, however, that their prototype (as given by <tt>&quot;prototype(&quot;CORE::chomp&quot;)&quot;</tt> is undefined, because it cannot be expressed and therefore one cannot really write replacements to override these builtins.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">END</font> blocks are now run even if you exit/die in a <font SIZE="-1">BEGIN</font> block. Internally, the execution of <font SIZE="-1">END</font> blocks is now controlled by PL_exit_flags &amp; <font SIZE="-1">PERL_EXIT_DESTRUCT_END.</font> This enables the new behaviour for Perl embedders. This will default in 5.10. See perlembed.</p>
<dt>&bull;</p>
<dd> Formats now support zero-padded decimal fields.</p>
<dt>&bull;</p>
<dd> Although &#8220;you shouldn&#8217;t do that&#8221;, it was possible to write code that depends on Perl&#8217;s hashed key order (Data::Dumper does this). The new algorithm &#8220;One-at-a-Time&#8221; produces a different hashed key order. More details are in &#8220;Performance Enhancements&#8221;.</p>
<dt>&bull;</p>
<dd> lstat(<font SIZE="-1">FILEHANDLE</font>) now gives a warning because the operation makes no sense. In future releases this may become a fatal error.</p>
<dt>&bull;</p>
<dd> Spurious syntax errors generated in certain situations, when <code>glob()</code> caused File::Glob to be loaded for the first time, have been fixed. [561]</p>
<dt>&bull;</p>
<dd> Lvalue subroutines can now return <tt>&quot;undef&quot;</tt> in list context. However, the lvalue subroutine feature still remains experimental. [561+]</p>
<dt>&bull;</p>
<dd> A lost warning &#8220;Can&#8217;t declare &#8230; dereference in my&#8221; has been restored (Perl had it earlier but it became lost in later releases.)</p>
<dt>&bull;</p>
<dd> A new special regular expression variable has been introduced: <tt>$^N</tt>, which contains the most-recently closed group (submatch).</p>
<dt>&bull;</p>
<dd> <tt>&quot;no Module;&quot;</tt> does not produce an error even if Module does not have an <code>unimport()</code> method. This parallels the behavior of <tt>&quot;use&quot;</tt> vis-a-vis <tt>&quot;import&quot;</tt>. [561]</p>
<dt>&bull;</p>
<dd> The numerical comparison operators return <tt>&quot;undef&quot;</tt> if either operand is a NaN. Previously the behaviour was unspecified.</p>
<dt>&bull;</p>
<dd> <tt>&quot;our&quot;</tt> can now have an experimental optional attribute <tt>&quot;unique&quot;</tt> that affects how global variables are shared among multiple interpreters, see &#8220;our&#8221; in perlfunc.</p>
<dt>&bull;</p>
<dd> The following builtin functions are now overridable: <code>each()</code>, <code>keys()</code>, <code>pop()</code>, <code>push()</code>, <code>shift()</code>, <code>splice()</code>, <code>unshift()</code>. [561]</p>
<dt>&bull;</p>
<dd> <tt>&quot;pack() / unpack()&quot;</tt> can now group template letters with <tt>&quot;()&quot;</tt> and then apply repetition/count modifiers on the groups.</p>
<dt>&bull;</p>
<dd> <tt>&quot;pack() / unpack()&quot;</tt> can now process the Perl internal numeric types: IVs, UVs, NVs&#8212; and also long doubles, if supported by the platform. The template letters are <tt>&quot;j&quot;</tt>, <tt>&quot;J&quot;</tt>, <tt>&quot;F&quot;</tt>, and <tt>&quot;D&quot;</tt>.</p>
<dt>&bull;</p>
<dd> <tt>&quot;pack('U0a*', ...)&quot;</tt> can now be used to force a string to <font SIZE="-1">UTF-8.</font></p>
<dt>&bull;</p>
<dd> my __PACKAGE__ <tt>$obj</tt> now works. [561]</p>
<dt>&bull;</p>
<dd> <code>POSIX::sleep()</code> now returns the number of <i>unslept</i> seconds (as the <font SIZE="-1">POSIX</font> standard says), as opposed to <code>CORE::sleep()</code> which returns the number of slept seconds.</p>
<dt>&bull;</p>
<dd> <code>printf()</code> and <code>sprintf()</code> now support parameter reordering using the <tt>&quot;%\d+\$&quot;</tt> and <tt>&quot;*\d+\$&quot;</tt> syntaxes. For example </p>
<pre>
    printf &quot;%2\$s %1\$s
&quot;, &quot;foo&quot;, &quot;bar&quot;;
</pre>
<p> will print &#8220;bar foo
&#8221;. This feature helps in writing internationalised software, and in general when the order of the parameters can vary.</p>
<dt>&bull;</p>
<dd> The (\&amp;) prototype now works properly. [561]</p>
<dt>&bull;</p>
<dd> prototype(\[$@%&amp;]) is now available to implicitly create references (useful for example if you want to emulate the <code>tie()</code> interface).</p>
<dt>&bull;</p>
<dd> A new command-line option, <tt>&quot;-t&quot;</tt> is available. It is the little brother of <tt>&quot;-T&quot;</tt>: instead of dying on taint violations, lexical warnings are given. <code>This is only meant as a temporary debugging aid while securing the code of old legacy applications. This is not a substitute for -T.</code></p>
<dt>&bull;</p>
<dd> In other taint news, the <tt>&quot;exec LIST&quot;</tt> and <tt>&quot;system LIST&quot;</tt> have now been considered too risky (think <tt>&quot;exec @ARGV&quot;</tt>: it can start any program with any arguments), and now the said forms cause a warning under lexical warnings. You should carefully launder the arguments to guarantee their validity. In future releases of Perl the forms will become fatal errors so consider starting laundering now.</p>
<dt>&bull;</p>
<dd> Tied hash interfaces are now required to have the <font SIZE="-1">EXISTS</font> and <font SIZE="-1">DELETE</font> methods (either own or inherited).</p>
<dt>&bull;</p>
<dd> If tr/// is just counting characters, it doesn&#8217;t attempt to modify its target.</p>
<dt>&bull;</p>
<dd> <code>untie()</code> will now call an <font SIZE="-1"><code>UNTIE</code></font><code>()</code> hook if it exists. See perltie for details. [561]</p>
<dt>&bull;</p>
<dd> &#8220;utime&#8221; in perlfunc now supports <tt>&quot;utime undef, undef, @files&quot;</tt> to change the file timestamps to the current time.</p>
<dt>&bull;</p>
<dd> The rules for allowing underscores (underbars) in numeric constants have been relaxed and simplified: now you can have an underscore simply <code>between digits</code>.</p>
<dt>&bull;</p>
<dd> Rather than relying on C&#8217;s argv[0] (which may not contain a full pathname) where possible $^X is now set by asking the operating system. (eg by reading <i>/proc/self/exe</i> on Linux, <i>/proc/curproc/file</i> on FreeBSD)</p>
<dt>&bull;</p>
<dd> A new variable, <tt>&quot;${^TAINT}&quot;</tt>, indicates whether taint mode is enabled.</p>
<dt>&bull;</p>
<dd> You can now override the <code>readline()</code> builtin, and this overrides also the &lt;<font SIZE="-1">FILEHANDLE</font>&gt; angle bracket operator.</p>
<dt>&bull;</p>
<dd> The command-line options -s and -F are now recognized on the shebang (#!) line.</p>
<dt>&bull;</p>
<dd> Use of the <tt>&quot;/c&quot;</tt> match modifier without an accompanying <tt>&quot;/g&quot;</tt> modifier elicits a new warning: <tt>&quot;Use of /c modifier is meaningless without /g&quot;</tt>. </p>
<p> Use of <tt>&quot;/c&quot;</tt> in substitutions, even with <tt>&quot;/g&quot;</tt>, elicits <tt>&quot;Use of /c modifier is meaningless in s///&quot;</tt>. </p>
<p> Use of <tt>&quot;/g&quot;</tt> with <tt>&quot;split&quot;</tt> elicits <tt>&quot;Use of /g modifier is meaningless in split&quot;</tt>.</p>
<dt>&bull;</p>
<dd> Support for the <tt>&quot;CLONE&quot;</tt> special subroutine had been added. With ithreads, when a new thread is created, all Perl data is cloned, however non-Perl data cannot be cloned automatically. In <tt>&quot;CLONE&quot;</tt> you can do whatever you need to do, like for example handle the cloning of non-Perl data, if necessary. <tt>&quot;CLONE&quot;</tt> will be executed once for every package that has it defined or inherited. It will be called in the context of the new thread, so all modifications are made in the new area. </p>
<p> See perlmod</dl>
<h2>Modules and Pragmata</h2>
<h3>New Modules and Pragmata</h3>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;Attribute::Handlers&quot;</tt>, originally by Damian Conway and now maintained by Arthur Bergman, allows a class to define attribute handlers. </p>
<pre><code>
package MyPack;
use Attribute::Handlers;
sub Wolf : ATTR(SCALAR){print "howl!
"}
#later, in some package using or inheriting from MyPack...
           my MyPack $Fluffy : Wolf;
#the attribute handler Wolf will be called
</code></pre>
<p> Both variables and routines can have attribute handlers. Handlers can be specific to type (<font SIZE="-1">SCALAR, ARRAY, HASH,</font> or <font SIZE="-1">CODE</font>), or specific to the exact compilation phase (<font SIZE="-1">BEGIN, CHECK, INIT,</font> or <font SIZE="-1">END</font>). See Attribute::Handlers.</p>
<dt>&bull;</p>
<dd> <tt>&quot;B::Concise&quot;</tt>, by Stephen McCamant, is a new compiler backend for walking the Perl syntax tree, printing concise info about ops. The output is highly customisable. See B::Concise. [561+]</p>
<dt>&bull;</p>
<dd> The new bignum, bigint, and bigrat pragmas, by Tels, implement transparent bignum support (using the Math::BigInt, Math::BigFloat, and Math::BigRat backends).</p>
<dt>&bull;</p>
<dd> <tt>&quot;Class::ISA&quot;</tt>, by Sean Burke, is a module for reporting the search path for a class&#8217;s <font SIZE="-1">ISA</font> tree. See Class::ISA.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Cwd&quot;</tt> now has a split personality: if possible, an <font SIZE="-1">XS</font> extension is used, (this will hopefully be faster, more secure, and more robust) but if not possible, the familiar Perl implementation is used.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Devel::PPPort&quot;</tt>, originally by Kenneth Albanowski and now maintained by Paul Marquess, has been added. It is primarily used by <tt>&quot;h2xs&quot;</tt> to enhance portability of <font SIZE="-1">XS</font> modules between different versions of Perl. See Devel::PPPort.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Digest&quot;</tt>, frontend module for calculating digests (checksums), from Gisle Aas, has been added. See Digest.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Digest::MD5&quot;</tt> for calculating <font SIZE="-1">MD5</font> digests (checksums) as defined in <font SIZE="-1">RFC 1321,</font> from Gisle Aas, has been added. See Digest::MD5. </p>
<p>use Digest::MD5 &#8216;md5_hex&#8217;;<br />
$digest = md5_hex(&#8220;Thirsty Camel&#8221;);<br />
print $digest, &#8220;
&#8221;;<br />
# 01d19d9d2045e005c3f1b80e8b164de1</p>
<p> <font SIZE="-1">NOTE:</font> the <tt>&quot;MD5&quot;</tt> backward compatibility module is deliberately not included since its further use is discouraged. </p>
<p> See also PerlIO::via::QuotedPrint.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Encode&quot;</tt>, originally by Nick Ing-Simmons and now maintained by Dan Kogai, provides a mechanism to translate between different character encodings. Support for Unicode, <font SIZE="-1">ISO-8859-1,</font> and <font SIZE="-1">ASCII</font> are compiled in to the module. Several other encodings (like the rest of the <font SIZE="-1">ISO-8859,</font> CP*/Win*, Mac, <font SIZE="-1">KOI8-R,</font> three variants <font SIZE="-1">EBCDIC,</font> Chinese, Japanese, and Korean encodings) are included and can be loaded at runtime. (For space considerations, the largest Chinese encodings have been separated into their own <font SIZE="-1">CPAN</font> module, Encode::HanExtra, which Encode will use if available). See Encode. </p>
<p> Any encoding supported by Encode module is also available to the &#8220;:<code>encoding()</code>&#8221; layer if PerlIO is used.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Hash::Util&quot;</tt> is the interface to the new <i>restricted hashes</i> feature. (Implemented by Jeffrey Friedl, Nick Ing-Simmons, and Michael Schwern.) See Hash::Util.</p>
<dt>&bull;</p>
<dd> <tt>&quot;I18N::Langinfo&quot;</tt> can be used to query locale information. See I18N::Langinfo.</p>
<dt>&bull;</p>
<dd> <tt>&quot;I18N::LangTags&quot;</tt>, by Sean Burke, has functions for dealing with RFC3066-style language tags. See I18N::LangTags.</p>
<dt>&bull;</p>
<dd> <tt>&quot;ExtUtils::Constant&quot;</tt>, by Nicholas Clark, is a new tool for extension writers for generating <font SIZE="-1">XS</font> code to import C header constants. See ExtUtils::Constant.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Filter::Simple&quot;</tt>, by Damian Conway, is an easy-to-use frontend to Filter::Util::Call. See Filter::Simple. </p>
<p>#in MyFilter.pm:<br />
package MyFilter;<br />
use Filter::Simple sub<br />
{<br />
    while (my($from, $to) = splice @_, 0, 2) {<br />
        s / $from / $to / g;<br />
    }<br />
};<br />
1;<br />
#in user&#8217;s code:<br />
use MyFilter qr / red / = &gt; &#8216;green&#8217;;<br />
print &#8220;red
&#8221;;<br />
#this code is filtered, will print &#8220;green
&#8221; print &#8220;bored
&#8221;;<br />
#this code is filtered, will print &#8220;bogreen
&#8221; no MyFilter;<br />
print &#8220;red
&#8221;;<br />
#this code is not filtered, will print &#8220;red
&#8221;</p>
<dt>&bull;</p>
<dd> <tt>&quot;File::Temp&quot;</tt>, by Tim Jenness, allows one to create temporary files and directories in an easy, portable, and secure way. See File::Temp. [561+]</p>
<dt>&bull;</p>
<dd> <tt>&quot;Filter::Util::Call&quot;</tt>, by Paul Marquess, provides you with the framework to write <i>source filters</i> in Perl. For most uses, the frontend Filter::Simple is to be preferred. See Filter::Util::Call.</p>
<dt>&bull;</p>
<dd> <tt>&quot;if&quot;</tt>, by Ilya Zakharevich, is a new pragma for conditional inclusion of modules.</p>
<dt>&bull;</p>
<dd> libnet, by Graham Barr, is a collection of perl5 modules related to network programming. See Net::FTP, Net::NNTP, Net::Ping (not part of libnet, but related), Net::POP3, Net::SMTP, and Net::Time. </p>
<p> Perl installation leaves libnet unconfigured; use <i>libnetcfg</i> to configure it.</p>
<dt>&bull;</p>
<dd> <tt>&quot;List::Util&quot;</tt>, by Graham Barr, is a selection of general-utility list subroutines, such as <code>sum()</code>, <code>min()</code>, <code>first()</code>, and <code>shuffle()</code>. See List::Util.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Locale::Constants&quot;</tt>, <tt>&quot;Locale::Country&quot;</tt>, <tt>&quot;Locale::Currency&quot;</tt> <tt>&quot;Locale::Language&quot;</tt>, and Locale::Script, by Neil Bowers, have been added. They provide the codes for various locale standards, such as &#8220;fr&#8221; for France, &#8220;usd&#8221; for <font SIZE="-1">US</font> Dollar, and &#8220;ja&#8221; for Japanese. </p>
<p>use Locale::Country;<br />
$country = code2country(&#8216;jp&#8217;);<br />
#$country gets &#8216;Japan&#8217; $code = country2code(&#8216;Norway&#8217;);<br />
#$code gets &#8216;no&#8217;</p>
<p> See Locale::Constants, Locale::Country, Locale::Currency, and Locale::Language.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Locale::Maketext&quot;</tt>, by Sean Burke, is a localization framework. See Locale::Maketext, and Locale::Maketext::TPJ13. The latter is an article about software localization, originally published in The Perl Journal #13, and republished here with kind permission.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Math::BigRat&quot;</tt> for big rational numbers, to accompany Math::BigInt and Math::BigFloat, from Tels. See Math::BigRat.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Memoize&quot;</tt> can make your functions faster by trading space for time, from Mark-Jason Dominus. See Memoize.</p>
<dt>&bull;</p>
<dd> <tt>&quot;MIME::Base64&quot;</tt>, by Gisle Aas, allows you to encode data in base64, as defined in <font SIZE="-1">RFC 2045</font> &#8211; <i></i><font SIZE="-1"><i>MIME</i></font><i> (Multipurpose Internet Mail Extensions)</i>. </p>
<p>use MIME::Base64;<br />
$encoded = encode_base64(&#8216;Aladdin:open sesame&#8217;);<br />
$decoded = decode_base64($encoded);<br />
print $encoded, &#8220;
&#8221;;<br />
#&#8221;QWxhZGRpbjpvcGVuIHNlc2FtZQ==&#8221;</p>
<p> See MIME::Base64.</p>
<dt>&bull;</p>
<dd> <tt>&quot;MIME::QuotedPrint&quot;</tt>, by Gisle Aas, allows you to encode data in quoted-printable encoding, as defined in <font SIZE="-1">RFC 2045</font> &#8211; <i></i><font SIZE="-1"><i>MIME</i></font><i> (Multipurpose Internet Mail Extensions)</i>. </p>
<p>use MIME::QuotedPrint;<br />
$encoded = encode_qp(&#8220;ޭ��&#8221;);<br />
$decoded = decode_qp($encoded);<br />
print $encoded, &#8220;
&#8221;;<br />
#&#8221;=DE=AD=BE=EF
&#8221; print $decoded, &#8220;
&#8221;;<br />
#&#8221;ޭ��
&#8221;</p>
<p> See also PerlIO::via::QuotedPrint.</p>
<dt>&bull;</p>
<dd> <tt>&quot;NEXT&quot;</tt>, by Damian Conway, is a pseudo-class for method redispatch. See <font SIZE="-1">NEXT</font>.</p>
<dt>&bull;</p>
<dd> <tt>&quot;open&quot;</tt> is a new pragma for setting the default I/O layers for <code>open()</code>.</p>
<dt>&bull;</p>
<dd> <tt>&quot;PerlIO::scalar&quot;</tt>, by Nick Ing-Simmons, provides the implementation of <font SIZE="-1">IO</font> to &#8220;in memory&#8221; Perl scalars as discussed above. It also serves as an example of a loadable PerlIO layer. Other future possibilities include PerlIO::Array and PerlIO::Code. See PerlIO::scalar.</p>
<dt>&bull;</p>
<dd> <tt>&quot;PerlIO::via&quot;</tt>, by Nick Ing-Simmons, acts as a PerlIO layer and wraps PerlIO layer functionality provided by a class (typically implemented in Perl code).</p>
<dt>&bull;</p>
<dd> <tt>&quot;PerlIO::via::QuotedPrint&quot;</tt>, by Elizabeth Mattijsen, is an example of a <tt>&quot;PerlIO::via&quot;</tt> class: </p>
<pre>
    use PerlIO::via::QuotedPrint;
    open($fh,&quot;&gt;:via(QuotedPrint)&quot;,$path);
</pre>
<p> This will automatically convert everything output to <tt>$fh</tt> to Quoted-Printable. See PerlIO::via and PerlIO::via::QuotedPrint.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Pod::ParseLink&quot;</tt>, by Russ Allbery, has been added, to parse L&lt;&gt; links in pods as described in the new perlpodspec.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Pod::Text::Overstrike&quot;</tt>, by Joe Smith, has been added. It converts <font SIZE="-1">POD</font> data to formatted overstrike text. See Pod::Text::Overstrike. [561+]</p>
<dt>&bull;</p>
<dd> <tt>&quot;Scalar::Util&quot;</tt> is a selection of general-utility scalar subroutines, such as <code>blessed()</code>, <code>reftype()</code>, and <code>tainted()</code>. See Scalar::Util.</p>
<dt>&bull;</p>
<dd> <tt>&quot;sort&quot;</tt> is a new pragma for controlling the behaviour of <code>sort()</code>.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Storable&quot;</tt> gives persistence to Perl data structures by allowing the storage and retrieval of Perl data to and from files in a fast and compact binary format. Because in effect Storable does serialisation of Perl data structures, with it you can also clone deep, hierarchical datastructures. Storable was originally created by Raphael Manfredi, but it is now maintained by Abhijit Menon-Sen. Storable has been enhanced to understand the two new hash features, Unicode keys and restricted hashes. See Storable.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Switch&quot;</tt>, by Damian Conway, has been added. Just by saying </p>
<pre>
    use Switch;
</pre>
<p> you have <tt>&quot;switch&quot;</tt> and <tt>&quot;case&quot;</tt> available in Perl. </p>
<p>use Switch;<br />
switch ($val) {<br />
                case 1          { print &#8220;number 1&#8221; }<br />
                case &#8220;a&#8221;        { print &#8220;string a&#8221; }<br />
                case [1..10,42] { print &#8220;number in list&#8221; }<br />
                case (@array)   { print &#8220;number in list&#8221; }<br />
                case /\w+/      { print &#8220;pattern&#8221; }<br />
                case qr/\w+/    { print &#8220;pattern&#8221; }<br />
                case (%hash)    { print &#8220;entry in hash&#8221; }<br />
                case (\%hash)   { print &#8220;entry in hash&#8221; }<br />
                case (\&amp;sub)    { print &#8220;arg to subroutine&#8221; }<br />
                else            { print &#8220;previous case not true&#8221; }<br />
    }</p>
<p> See Switch.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Test::More&quot;</tt>, by Michael Schwern, is yet another framework for writing test scripts, more extensive than Test::Simple. See Test::More.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Test::Simple&quot;</tt>, by Michael Schwern, has basic utilities for writing tests. See Test::Simple.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Text::Balanced&quot;</tt>, by Damian Conway, has been added, for extracting delimited text sequences from strings. </p>
<p>use Text::Balanced &#8216;extract_delimited&#8217;;<br />
($a, $b) = extract_delimited(&#8220;&#8216;never say never&#8217;, he never said&#8221;, &#8220;&#8216;&#8221;, &#8221;);</p>
<p> <tt>$a</tt> will be &#8220;&#8217;never say never&#8221;&#8217;, <tt>$b</tt> will be &#8216;, he never said&#8217;. </p>
<p> In addition to <code>extract_delimited()</code>, there are also <code>extract_bracketed()</code>, <code>extract_quotelike()</code>, <code>extract_codeblock()</code>, <code>extract_variable()</code>, <code>extract_tagged()</code>, <code>extract_multiple()</code>, <code>gen_delimited_pat()</code>, and <code>gen_extract_tagged()</code>. With these, you can implement rather advanced parsing algorithms. See Text::Balanced.</p>
<dt>&bull;</p>
<dd> <tt>&quot;threads&quot;</tt>, by Arthur Bergman, is an interface to interpreter threads. Interpreter threads (ithreads) is the new thread model introduced in Perl 5.6 but only available as an internal interface for extension writers (and for Win32 Perl for <tt>&quot;fork()&quot;</tt> emulation). See threads, threads::shared, and perlthrtut.</p>
<dt>&bull;</p>
<dd> <tt>&quot;threads::shared&quot;</tt>, by Arthur Bergman, allows data sharing for interpreter threads. See threads::shared.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Tie::File&quot;</tt>, by Mark-Jason Dominus, associates a Perl array with the lines of a file. See Tie::File.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Tie::Memoize&quot;</tt>, by Ilya Zakharevich, provides on-demand loaded hashes. See Tie::Memoize.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Tie::RefHash::Nestable&quot;</tt>, by Edward Avis, allows storing hash references (unlike the standard Tie::RefHash) The module is contained within Tie::RefHash. See Tie::RefHash.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Time::HiRes&quot;</tt>, by Douglas E. Wegscheid, provides high resolution timing (ualarm, usleep, and gettimeofday). See Time::HiRes.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Unicode::UCD&quot;</tt> offers a querying interface to the Unicode Character Database. See Unicode::UCD.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Unicode::Collate&quot;</tt>, by <font SIZE="-1">SADAHIRO</font> Tomoyuki, implements the <font SIZE="-1">UCA</font> (Unicode Collation Algorithm) for sorting Unicode strings. See Unicode::Collate.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Unicode::Normalize&quot;</tt>, by <font SIZE="-1">SADAHIRO</font> Tomoyuki, implements the various Unicode normalization forms. See Unicode::Normalize.</p>
<dt>&bull;</p>
<dd> <tt>&quot;XS::APItest&quot;</tt>, by Tim Jenness, is a test extension that exercises <font SIZE="-1">XS</font> APIs. Currently only <tt>&quot;printf()&quot;</tt> is tested: how to output various basic data types from <font SIZE="-1">XS.</font></p>
<dt>&bull;</p>
<dd> <tt>&quot;XS::Typemap&quot;</tt>, by Tim Jenness, is a test extension that exercises <font SIZE="-1">XS</font> typemaps. Nothing gets installed, but the code is worth studying for extension writers.</dl>
<h3>Updated And Improved Modules and Pragmata</h3>
<dl>
<dt>&bull;</p>
<dd> The following independently supported modules have been updated to the newest versions from <font SIZE="-1">CPAN: CGI, CPAN,</font> DB_File, File::Spec, File::Temp, Getopt::Long, Math::BigFloat, Math::BigInt, the podlators bundle (Pod::Man, Pod::Text), Pod::LaTeX [561+], Pod::Parser, Storable, Term::ANSIColor, Test, Text-Tabs+Wrap.</p>
<dt>&bull;</p>
<dd> <code>attributes::reftype()</code> now works on tied arguments.</p>
<dt>&bull;</p>
<dd> AutoLoader can now be disabled with <tt>&quot;no AutoLoader;&quot;</tt>.</p>
<dt>&bull;</p>
<dd> B::Deparse has been significantly enhanced by Robin Houston. It can now deparse almost all of the standard test suite (so that the tests still succeed). There is a make target &#8220;test.deparse&#8221; for trying this out.</p>
<dt>&bull;</p>
<dd> Carp now has better interface documentation, and the <tt>@CARP_NOT</tt> interface has been added to get optional control over where errors are reported independently of <tt>@ISA</tt>, by Ben Tilly.</p>
<dt>&bull;</p>
<dd> Class::Struct can now define the classes in compile time.</p>
<dt>&bull;</p>
<dd> Class::Struct now assigns the array/hash element if the accessor is called with an array/hash element as the <code>sole</code> argument.</p>
<dt>&bull;</p>
<dd> The return value of <code>Cwd::fastcwd()</code> is now tainted.</p>
<dt>&bull;</p>
<dd> Data::Dumper now has an option to sort hashes.</p>
<dt>&bull;</p>
<dd> Data::Dumper now has an option to dump code references using B::Deparse.</p>
<dt>&bull;</p>
<dd> DB_File now supports newer Berkeley <font SIZE="-1">DB</font> versions, among other improvements.</p>
<dt>&bull;</p>
<dd> Devel::Peek now has an interface for the Perl memory statistics (this works only if you are using perl&#8217;s malloc, and if you have compiled with debugging).</p>
<dt>&bull;</p>
<dd> The English module can now be used without the infamous performance hit by saying </p>
<pre>
        use English '-no_match_vars';
</pre>
<p> (Assuming, of course, that you don&#8217;t need the troublesome variables <tt>&quot;$`&quot;</tt>, <tt>$&amp;</tt>, or <tt>&quot;$'&quot;</tt>.) Also, introduced <tt>@LAST_MATCH_START</tt> and <tt>@LAST_MATCH_END</tt> English aliases for <tt>&quot;@-&quot;</tt> and <tt>&quot;@+&quot;</tt>.</p>
<dt>&bull;</p>
<dd> ExtUtils::MakeMaker has been significantly cleaned up and fixed. The enhanced version has also been backported to earlier releases of Perl and submitted to <font SIZE="-1">CPAN</font> so that the earlier releases can enjoy the fixes.</p>
<dt>&bull;</p>
<dd> The arguments of <code>WriteMakefile()</code> in Makefile.PL are now checked for sanity much more carefully than before. This may cause new warnings when modules are being installed. See ExtUtils::MakeMaker for more details.</p>
<dt>&bull;</p>
<dd> ExtUtils::MakeMaker now uses File::Spec internally, which hopefully leads to better portability.</p>
<dt>&bull;</p>
<dd> Fcntl, Socket, and Sys::Syslog have been rewritten by Nicholas Clark to use the new-style constant dispatch section (see ExtUtils::Constant). This means that they will be more robust and hopefully faster.</p>
<dt>&bull;</p>
<dd> File::Find now <code>chdir()</code>s correctly when chasing symbolic links. [561]</p>
<dt>&bull;</p>
<dd> File::Find now has pre- and post-processing callbacks. It also correctly changes directories when chasing symbolic links. Callbacks (naughtily) exiting with &#8220;next;&#8221; instead of &#8220;return;&#8221; now work.</p>
<dt>&bull;</p>
<dd> File::Find is now (again) reentrant. It also has been made more portable.</p>
<dt>&bull;</p>
<dd> The warnings issued by File::Find now belong to their own category. You can enable/disable them with <tt>&quot;use/no warnings 'File::Find';&quot;</tt>.</p>
<dt>&bull;</p>
<dd> <code>File::Glob::glob()</code> has been renamed to <code>File::Glob::bsd_glob()</code> because the name clashes with the builtin <code>glob()</code>. The older name is still available for compatibility, but is deprecated. [561]</p>
<dt>&bull;</p>
<dd> File::Glob now supports <tt>&quot;GLOB_LIMIT&quot;</tt> constant to limit the size of the returned list of filenames.</p>
<dt>&bull;</p>
<dd> IPC::Open3 now allows the use of numeric file descriptors.</p>
<dt>&bull;</p>
<dd> IO::Socket now has an <code>atmark()</code> method, which returns true if the socket is positioned at the out-of-band mark. The method is also exportable as a <code>sockatmark()</code> function.</p>
<dt>&bull;</p>
<dd> IO::Socket::INET failed to open the specified port if the service name was not known. It now correctly uses the supplied port number as is. [561]</p>
<dt>&bull;</p>
<dd> IO::Socket::INET has support for the ReusePort option (if your platform supports it). The Reuse option now has an alias, ReuseAddr. For clarity, you may want to prefer ReuseAddr.</p>
<dt>&bull;</p>
<dd> IO::Socket::INET now supports a value of zero for <tt>&quot;LocalPort&quot;</tt> (usually meaning that the operating system will make one up.)</p>
<dt>&bull;</p>
<dd> &#8216;use lib&#8217; now works identically to <tt>@INC</tt>. Removing directories with &#8216;no lib&#8217; now works.</p>
<dt>&bull;</p>
<dd> Math::BigFloat and Math::BigInt have undergone a full rewrite by Tels. They are now magnitudes faster, and they support various bignum libraries such as <font SIZE="-1">GMP</font> and <font SIZE="-1">PARI</font> as their backends.</p>
<dt>&bull;</p>
<dd> Math::Complex handles inf, NaN etc., better.</p>
<dt>&bull;</p>
<dd> Net::Ping has been considerably enhanced by Rob Brown: multihoming is now supported, Win32 functionality is better, there is now time measuring functionality (optionally high-resolution using Time::HiRes), and there is now &#8220;external&#8221; protocol which uses Net::Ping::External module which runs your external ping utility and parses the output. A version of Net::Ping::External is available in <font SIZE="-1">CPAN.</font> </p>
<p> Note that some of the Net::Ping tests are disabled when running under the Perl distribution since one cannot assume one or more of the following: enabled echo port at localhost, full Internet connectivity, or sympathetic firewalls. You can set the environment variable PERL_TEST_Net_Ping to &#8220;1&#8221; (one) before running the Perl test suite to enable all the Net::Ping tests.</p>
<dt>&bull;</p>
<dd> <code>POSIX::sigaction()</code> is now much more flexible and robust. You can now install coderef handlers, &#8216;<font SIZE="-1">DEFAULT</font>&#8216;, and &#8216;<font SIZE="-1">IGNORE</font>&#8216; handlers, installing new handlers was not atomic.</p>
<dt>&bull;</p>
<dd> In Safe, <tt>%INC</tt> is now localised in a Safe compartment so that use/require work.</p>
<dt>&bull;</p>
<dd> In SDBM_File on DOSish platforms, some keys went missing because of lack of support for files with &#8220;holes&#8221;. A workaround for the problem has been added.</p>
<dt>&bull;</p>
<dd> In Search::Dict one can now have a pre-processing hook for the lines being searched.</p>
<dt>&bull;</p>
<dd> The Shell module now has an <font SIZE="-1">OO</font> interface.</p>
<dt>&bull;</p>
<dd> In Sys::Syslog there is now a failover mechanism that will go through alternative connection mechanisms until the message is successfully logged.</p>
<dt>&bull;</p>
<dd> The Test module has been significantly enhanced.</p>
<dt>&bull;</p>
<dd> <code>Time::Local::timelocal()</code> does not handle fractional seconds anymore. The rationale is that neither does <code>localtime()</code>, and <code>timelocal()</code> and <code>localtime()</code> are supposed to be inverses of each other.</p>
<dt>&bull;</p>
<dd> The vars pragma now supports declaring fully qualified variables. (Something that <tt>&quot;our()&quot;</tt> does not and will not support.)</p>
<dt>&bull;</p>
<dd> The <tt>&quot;utf8::&quot;</tt> name space (as in the pragma) provides various Perl-callable functions to provide low level access to Perl&#8217;s internal Unicode representation. At the moment only <code>length()</code> has been implemented.</dl>
<h2>Utility Changes</h2>
<dl>
<dt>&bull;</p>
<dd> Emacs perl mode (emacs/cperl-mode.el) has been updated to version 4.31.</p>
<dt>&bull;</p>
<dd> <i>emacs/e2ctags.pl</i> is now much faster.</p>
<dt>&bull;</p>
<dd> <tt>&quot;enc2xs&quot;</tt> is a tool for people adding their own encodings to the Encode module.</p>
<dt>&bull;</p>
<dd> <tt>&quot;h2ph&quot;</tt> now supports C trigraphs.</p>
<dt>&bull;</p>
<dd> <tt>&quot;h2xs&quot;</tt> now produces a template <font SIZE="-1">README.</font></p>
<dt>&bull;</p>
<dd> <tt>&quot;h2xs&quot;</tt> now uses <tt>&quot;Devel::PPPort&quot;</tt> for better portability between different versions of Perl.</p>
<dt>&bull;</p>
<dd> <tt>&quot;h2xs&quot;</tt> uses the new ExtUtils::Constant module which will affect newly created extensions that define constants. Since the new code is more correct (if you have two constants where the first one is a prefix of the second one, the first constant <code>never</code> got defined), less lossy (it uses integers for integer constant, as opposed to the old code that used floating point numbers even for integer constants), and slightly faster, you might want to consider regenerating your extension code (the new scheme makes regenerating easy). h2xs now also supports C trigraphs.</p>
<dt>&bull;</p>
<dd> <tt>&quot;libnetcfg&quot;</tt> has been added to configure libnet.</p>
<dt>&bull;</p>
<dd> <tt>&quot;perlbug&quot;</tt> is now much more robust. It also sends the bug report to perl.org, not perl.com.</p>
<dt>&bull;</p>
<dd> <tt>&quot;perlcc&quot;</tt> has been rewritten and its user interface (that is, command line) is much more like that of the Unix C compiler, cc. (The perlbc tools has been removed. Use <tt>&quot;perlcc -B&quot;</tt> instead.) <code>Note that perlcc is still considered very experimental and unsupported.</code> [561]</p>
<dt>&bull;</p>
<dd> <tt>&quot;perlivp&quot;</tt> is a new Installation Verification Procedure utility for running any time after installing Perl.</p>
<dt>&bull;</p>
<dd> <tt>&quot;piconv&quot;</tt> is an implementation of the character conversion utility <tt>&quot;iconv&quot;</tt>, demonstrating the new Encode module.</p>
<dt>&bull;</p>
<dd> <tt>&quot;pod2html&quot;</tt> now allows specifying a cache directory.</p>
<dt>&bull;</p>
<dd> <tt>&quot;pod2html&quot;</tt> now produces <font SIZE="-1">XHTML 1.0.</font></p>
<dt>&bull;</p>
<dd> <tt>&quot;pod2html&quot;</tt> now understands <font SIZE="-1">POD</font> written using different line endings (PC-like <font SIZE="-1">CRLF</font> versus Unix-like <font SIZE="-1">LF</font> versus MacClassic-like <font SIZE="-1">CR</font>).</p>
<dt>&bull;</p>
<dd> <tt>&quot;s2p&quot;</tt> has been completely rewritten in Perl. (It is in fact a full implementation of sed in Perl: you can use the sed functionality by using the <tt>&quot;psed&quot;</tt> utility.)</p>
<dt>&bull;</p>
<dd> <tt>&quot;xsubpp&quot;</tt> now understands <font SIZE="-1">POD</font> documentation embedded in the *.xs files. [561]</p>
<dt>&bull;</p>
<dd> <tt>&quot;xsubpp&quot;</tt> now supports the <font SIZE="-1">OUT</font> keyword.</dl>
<h2>New Documentation</h2>
<dl>
<dt>&bull;</p>
<dd> perl56delta details the changes between the 5.005 release and the 5.6.0 release.</p>
<dt>&bull;</p>
<dd> perlclib documents the internal replacements for standard C library functions. (Interesting only for extension writers and Perl core hackers.) [561+]</p>
<dt>&bull;</p>
<dd> perldebtut is a Perl debugging tutorial. [561+]</p>
<dt>&bull;</p>
<dd> perlebcdic contains considerations for running Perl on <font SIZE="-1">EBCDIC</font> platforms. [561+]</p>
<dt>&bull;</p>
<dd> perlintro is a gentle introduction to Perl.</p>
<dt>&bull;</p>
<dd> perliol documents the internals of PerlIO with layers.</p>
<dt>&bull;</p>
<dd> perlmodstyle is a style guide for writing modules.</p>
<dt>&bull;</p>
<dd> perlnewmod tells about writing and submitting a new module. [561+]</p>
<dt>&bull;</p>
<dd> perlpacktut is a <code>pack()</code> tutorial.</p>
<dt>&bull;</p>
<dd> perlpod has been rewritten to be clearer and to record the best practices gathered over the years.</p>
<dt>&bull;</p>
<dd> perlpodspec is a more formal specification of the pod format, mainly of interest for writers of pod applications, not to people writing in pod.</p>
<dt>&bull;</p>
<dd> perlretut is a regular expression tutorial. [561+]</p>
<dt>&bull;</p>
<dd> perlrequick is a regular expressions quick-start guide. Yes, much quicker than perlretut. [561]</p>
<dt>&bull;</p>
<dd> perltodo has been updated.</p>
<dt>&bull;</p>
<dd> perltootc has been renamed as perltooc (to not to conflict with perltoot in filesystems restricted to &#8220;8.3&#8221; names).</p>
<dt>&bull;</p>
<dd> perluniintro is an introduction to using Unicode in Perl. (perlunicode is more of a detailed reference and background information)</p>
<dt>&bull;</p>
<dd> perlutil explains the command line utilities packaged with the Perl distribution. [561+]</dl>
<p> The following platform-specific documents are available before the installation as <font SIZE="-1">README.</font><i>platform</i>, and after the installation as perl<i>platform</i>: </p>
<pre>
    perlaix perlamiga perlapollo perlbeos perlbs2000
    perlce perlcygwin perldgux perldos perlepoc perlfreebsd perlhpux
    perlhurd perlirix perlmachten perlmacos perlmint perlmpeix
    perlnetware perlos2 perlos390 perlplan9 perlqnx perlsolaris
    perltru64 perluts perlvmesa perlvms perlvos perlwin32
</pre>
<p> These documents usually detail one or more of the following subjects: configuring, building, testing, installing, and sometimes also using Perl on the said platform. </p>
<p> Eastern Asian Perl users are now welcomed in their own languages: <font SIZE="-1">README</font>.jp (Japanese), <font SIZE="-1">README</font>.ko (Korean), <font SIZE="-1">README</font>.cn (simplified Chinese) and <font SIZE="-1">README</font>.tw (traditional Chinese), which are written in normal pod but encoded in EUC-JP, EUC-KR, EUC-CN and Big5. These will get installed as </p>
<pre>
   perljp perlko perlcn perltw
</pre>
<dl>
<dt>&bull;</p>
<dd> The documentation for the POSIX-BC platform is called &#8220;<font SIZE="-1">BS2000&#8221;,</font> to avoid confusion with the Perl <font SIZE="-1">POSIX</font> module.</p>
<dt>&bull;</p>
<dd> The documentation for the WinCE platform is called perlce (<font SIZE="-1">README</font>.ce in the source code kit), to avoid confusion with the perlwin32 documentation on 8.3-restricted filesystems.</dl>
<h2>Performance Enhancements</h2>
<dl>
<dt>&bull;</p>
<dd> <code>map()</code> could get pathologically slow when the result list it generates is larger than the source list. The performance has been improved for common scenarios. [561]</p>
<dt>&bull;</p>
<dd> <code>sort()</code> is also fully reentrant, in the sense that the sort function can itself call <code>sort()</code>. This did not work reliably in previous releases. [561]</p>
<dt>&bull;</p>
<dd> <code>sort()</code> has been changed to use primarily mergesort internally as opposed to the earlier quicksort. For very small lists this may result in slightly slower sorting times, but in general the speedup should be at least 20%. Additional bonuses are that the worst case behaviour of <code>sort()</code> is now better (in computer science terms it now runs in time O(N log N), as opposed to quicksort&#8217;s Theta(N**2) worst-case run time behaviour), and that <code>sort()</code> is now stable (meaning that elements with identical keys will stay ordered as they were before the sort). See the <tt>&quot;sort&quot;</tt> pragma for information. </p>
<p> The story in more detail: suppose you want to serve yourself a little slice of Pi. </p>
<pre>
    @digits = ( 3,1,4,1,5,9 );
</pre>
<p> A numerical sort of the digits will yield (1,1,3,4,5,9), as expected. Which <tt>1</tt> comes first is hard to know, since one <tt>1</tt> looks pretty much like any other. You can regard this as totally trivial, or somewhat profound. However, if you just want to sort the even digits ahead of the odd ones, then what will </p>
<pre>
    sort { ($a % 2) &lt;=&gt; ($b % 2) } @digits;
</pre>
<p> yield? The only even digit, <tt>4</tt>, will come first. But how about the odd numbers, which all compare equal? With the quicksort algorithm used to implement Perl 5.6 and earlier, the order of ties is left up to the sort. So, as you add more and more digits of Pi, the order in which the sorted even and odd digits appear will change. and, for sufficiently large slices of Pi, the quicksort algorithm in Perl 5.8 won&#8217;t return the same results even if reinvoked with the same input. The justification for this rests with quicksort&#8217;s worst case behavior. If you run </p>
<p>sort{$a &lt;=&gt; $b}(1..$N, 1..$N);</p>
<p> (something you might approximate if you wanted to merge two sorted arrays using sort), doubling <tt>$N</tt> doesn&#8217;t just double the quicksort time, it <i>quadruples</i> it. Quicksort has a worst case run time that can grow like N**2, so-called <i>quadratic</i> behaviour, and it can happen on patterns that may well arise in normal use. You won&#8217;t notice this for small arrays, but you <i>will</i> notice it with larger arrays, and you may not live long enough for the sort to complete on arrays of a million elements. So the 5.8 quicksort scrambles large arrays before sorting them, as a statistical defence against quadratic behaviour. But that means if you sort the same large array twice, ties may be broken in different ways. </p>
<p> Because of the unpredictability of tie-breaking order, and the quadratic worst-case behaviour, quicksort was <i>almost</i> replaced completely with a stable mergesort. <i>Stable</i> means that ties are broken to preserve the original order of appearance in the input array. So </p>
<pre>
    sort { ($a % 2) &lt;=&gt; ($b % 2) } (3,1,4,1,5,9);
</pre>
<p> will yield (4,3,1,1,5,9), guaranteed. The even and odd numbers appear in the output in the same order they appeared in the input. Mergesort has worst case O(N log N) behaviour, the best value attainable. And, ironically, this mergesort does particularly well where quicksort goes quadratic: mergesort sorts (1..$N, 1..$N) in O(N) time. But quicksort was rescued at the last moment because it is faster than mergesort on certain inputs and platforms. For example, if you really <i>don&#8217;t</i> care about the order of even and odd digits, quicksort will run in O(N) time; it&#8217;s very good at sorting many repetitions of a small number of distinct elements. The quicksort divide and conquer strategy works well on platforms with relatively small, very fast, caches. Eventually, the problem gets whittled down to one that fits in the cache, from which point it benefits from the increased memory speed. </p>
<p> Quicksort was rescued by implementing a sort pragma to control aspects of the sort. The <code>stable</code> subpragma forces stable behaviour, regardless of algorithm. The <code>_quicksort</code> and <code>_mergesort</code> subpragmas are heavy-handed ways to select the underlying implementation. The leading <tt>&quot;_&quot;</tt> is a reminder that these subpragmas may not survive beyond 5.8. More appropriate mechanisms for selecting the implementation exist, but they wouldn&#8217;t have arrived in time to save quicksort.</p>
<dt>&bull;</p>
<dd> Hashes now use Bob Jenkins &#8220;One-at-a-Time&#8221; hashing key algorithm ( <a rel="nofollow" href="http://burtleburtle.net/bob/hash/doobs.html">http://burtleburtle.net/bob/hash/doobs.html</a> ). This algorithm is reasonably fast while producing a much better spread of values than the old hashing algorithm (originally by Chris Torek, later tweaked by Ilya Zakharevich). Hash values output from the algorithm on a hash of all 3-char printable <font SIZE="-1">ASCII</font> keys comes much closer to passing the <font SIZE="-1">DIEHARD</font> random number generation tests. According to perlbench, this change has not affected the overall speed of Perl.</p>
<dt>&bull;</p>
<dd> <code>unshift()</code> should now be noticeably faster.</dl>
<h2>Installation and Configuration Improvements</h2>
<h3>Generic Improvements</h3>
<dl>
<dt>&bull;</p>
<dd> <font SIZE="-1">INSTALL</font> now explains how you can configure Perl to use 64-bit integers even on non-64-bit platforms.</p>
<dt>&bull;</p>
<dd> Policy.sh policy change: if you are reusing a Policy.sh file (see <font SIZE="-1">INSTALL</font>) and you use Configure -Dprefix=/foo/bar and in the old Policy <tt>$prefix</tt> eq <tt>$siteprefix</tt> and <tt>$prefix</tt> eq <tt>$vendorprefix</tt>, all of them will now be changed to the new prefix, /foo/bar. (Previously only <tt>$prefix</tt> changed.) If you do not like this new behaviour, specify prefix, siteprefix, and vendorprefix explicitly.</p>
<dt>&bull;</p>
<dd> A new optional location for Perl libraries, otherlibdirs, is available. It can be used for example for vendor add-ons without disturbing Perl&#8217;s own library directories.</p>
<dt>&bull;</p>
<dd> In many platforms, the vendor-supplied &#8216;cc&#8217; is too stripped-down to build Perl (basically, &#8216;cc&#8217; doesn&#8217;t do <font SIZE="-1">ANSI C</font>). If this seems to be the case and &#8216;cc&#8217; does not seem to be the <font SIZE="-1">GNU C</font> compiler &#8216;gcc&#8217;, an automatic attempt is made to find and use &#8216;gcc&#8217; instead.</p>
<dt>&bull;</p>
<dd> gcc needs to closely track the operating system release to avoid build problems. If Configure finds that gcc was built for a different operating system release than is running, it now gives a clearly visible warning that there may be trouble ahead.</p>
<dt>&bull;</p>
<dd> Since Perl 5.8 is not binary-compatible with previous releases of Perl, Configure no longer suggests including the 5.005 modules in <tt>@INC</tt>.</p>
<dt>&bull;</p>
<dd> Configure <tt>&quot;-S&quot;</tt> can now run non-interactively. [561]</p>
<dt>&bull;</p>
<dd> Configure support for pdp11-style memory models has been removed due to obsolescence. [561]</p>
<dt>&bull;</p>
<dd> configure.gnu now works with options with whitespace in them.</p>
<dt>&bull;</p>
<dd> installperl now outputs everything to <font SIZE="-1">STDERR.</font></p>
<dt>&bull;</p>
<dd> Because PerlIO is now the default on most platforms, &#8220;-perlio&#8221; doesn&#8217;t get appended to the <tt>$Config</tt>{archname} (also known as $^O) anymore. Instead, if you explicitly choose not to use perlio (Configure command line option -Uuseperlio), you will get &#8220;-stdio&#8221; appended.</p>
<dt>&bull;</p>
<dd> Another change related to the architecture name is that &#8220;-64all&#8221; (-Duse64bitall, or &#8220;maximally 64-bit&#8221;) is appended only if your pointers are 64 bits wide. (To be exact, the use64bitall is ignored.)</p>
<dt>&bull;</p>
<dd> In <font SIZE="-1">AFS</font> installations, one can configure the root of the <font SIZE="-1">AFS</font> to be somewhere else than the default <i>/afs</i> by using the Configure parameter <tt>&quot;-Dafsroot=/some/where/else&quot;</tt>.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">APPLLIB_EXP,</font> a lesser-known configuration-time definition, has been documented. It can be used to prepend site-specific directories to Perl&#8217;s default search path (@INC); see <font SIZE="-1">INSTALL</font> for information.</p>
<dt>&bull;</p>
<dd> The version of Berkeley <font SIZE="-1">DB</font> used when the Perl (and, presumably, the DB_File extension) was built is now available as <tt>@Config{qw(db_version_major db_version_minor db_version_patch)}</tt> from Perl and as <tt>&quot;DB_VERSION_MAJOR_CFG DB_VERSION_MINOR_CFG DB_VERSION_PATCH_CFG&quot;</tt> from C.</p>
<dt>&bull;</p>
<dd> Building Berkeley <font SIZE="-1">DB3</font> for compatibility modes for <font SIZE="-1">DB, NDBM,</font> and <font SIZE="-1">ODBM</font> has been documented in <font SIZE="-1">INSTALL.</font></p>
<dt>&bull;</p>
<dd> If you have <font SIZE="-1">CPAN</font> access (either network or a local copy such as a CD-ROM) you can during specify extra modules to Configure to build and install with Perl using the -Dextras=&#8230; option. See <font SIZE="-1">INSTALL</font> for more details.</p>
<dt>&bull;</p>
<dd> In addition to config.over, a new override file, config.arch, is available. This file is supposed to be used by hints file writers for architecture-wide changes (as opposed to config.over which is for site-wide changes).</p>
<dt>&bull;</p>
<dd> If your file system supports symbolic links, you can build Perl outside of the source directory by </p>
<pre>
        mkdir perl/build/directory
        cd perl/build/directory
        sh /path/to/perl/source/Configure -Dmksymlinks ...
</pre>
<p> This will create in perl/build/directory a tree of symbolic links pointing to files in /path/to/perl/source. The original files are left unaffected. After Configure has finished, you can just say </p>
<pre>
        make all test
</pre>
<p> and Perl will be built and tested, all in perl/build/directory. [561]</p>
<dt>&bull;</p>
<dd> For Perl developers, several new make targets for profiling and debugging have been added; see perlhack.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Use of the <i>gprof</i> tool to profile Perl has been documented in perlhack. There is a make target called &#8220;perl.gprof&#8221; for generating a gprofiled Perl executable.</p>
<dt>&bull;</p>
<dd> If you have <font SIZE="-1">GCC 3,</font> there is a make target called &#8220;perl.gcov&#8221; for creating a gcoved Perl executable for coverage analysis. See perlhack.</p>
<dt>&bull;</p>
<dd> If you are on <font SIZE="-1">IRIX</font> or Tru64 platforms, new profiling/debugging options have been added; see perlhack for more information about pixie and Third Degree.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> Guidelines of how to construct minimal Perl installations have been added to <font SIZE="-1">INSTALL.</font></p>
<dt>&bull;</p>
<dd> The Thread extension is now not built at all under ithreads (<tt>&quot;Configure -Duseithreads&quot;</tt>) because it wouldn&#8217;t work anyway (the Thread extension requires being Configured with <tt>&quot;-Duse5005threads&quot;</tt>). </p>
<p> <code>Note that the 5.005 threads are unsupported and deprecated: if you have code written for the old threads you should migrate it to the new ithreads model.</code></p>
<dt>&bull;</p>
<dd> The Gconvert macro ($Config{d_Gconvert}) used by perl for stringifying floating-point numbers is now more picky about using sprintf %.*g rules for the conversion. Some platforms that used to use gcvt may now resort to the slower sprintf.</p>
<dt>&bull;</p>
<dd> The obsolete method of making a special (e.g., debugging) flavor of perl by saying </p>
<pre>
        make LIBPERL=libperld.a
</pre>
<p> has been removed. Use -DDEBUGGING instead.</dl>
<h3>New Or Improved Platforms</h3>
<p> For the list of platforms known to support Perl, see &#8220;Supported Platforms&#8221; in perlport.</p>
<dl>
<dt>&bull;</p>
<dd> <font SIZE="-1">AIX</font> dynamic loading should be now better supported.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">AIX</font> should now work better with gcc, threads, and 64-bitness. Also the long doubles support in <font SIZE="-1">AIX</font> should be better now. See perlaix.</p>
<dt>&bull;</p>
<dd> AtheOS ( <a rel="nofollow" href="http://www.atheos.cx/">http://www.atheos.cx/</a> ) is a new platform.</p>
<dt>&bull;</p>
<dd> BeOS has been reclaimed.</p>
<dt>&bull;</p>
<dd> The <font SIZE="-1">DG/UX</font> platform now supports 5.005-style threads. See perldgux.</p>
<dt>&bull;</p>
<dd> The DYNIX/ptx platform (also known as dynixptx) is supported at or near osvers 4.5.2.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">EBCDIC</font> platforms (z/OS (also known as <font SIZE="-1">OS/390</font>), POSIX-BC, and <font SIZE="-1">VM/ESA</font>) have been regained. Many test suite tests still fail and the co-existence of Unicode and <font SIZE="-1">EBCDIC</font> isn&#8217;t quite settled, but the situation is much better than with Perl 5.6. See perlos390, perlbs2000 (for POSIX-BC), and perlvmesa for more information. (<code>Note:</code> support for <font SIZE="-1">VM/ESA</font> was removed in Perl v5.18.0. The relevant information was in <i></i><font SIZE="-1"><i>README</i></font><i>.vmesa</i>)</p>
<dt>&bull;</p>
<dd> Building perl with -Duseithreads or -Duse5005threads now works under HP-UX 10.20 (previously it only worked under 10.30 or later). You will need a thread library package installed. See <font SIZE="-1">README</font>.hpux. [561]</p>
<dt>&bull;</p>
<dd> Mac <font SIZE="-1">OS</font> Classic is now supported in the mainstream source package (MacPerl has of course been available since perl 5.004 but now the source code bases of standard Perl and MacPerl have been synchronised) [561]</p>
<dt>&bull;</p>
<dd> Mac <font SIZE="-1">OS X</font> (or Darwin) should now be able to build Perl even on <font SIZE="-1">HFS+</font> filesystems. (The case-insensitivity used to confuse the Perl build process.)</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">NCR</font> MP-RAS is now supported. [561]</p>
<dt>&bull;</p>
<dd> All the NetBSD specific patches (except for the installation specific ones) have been merged back to the main distribution.</p>
<dt>&bull;</p>
<dd> NetWare from Novell is now supported. See perlnetware.</p>
<dt>&bull;</p>
<dd> NonStop-UX is now supported. [561]</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">NEC</font> SUPER-UX is now supported.</p>
<dt>&bull;</p>
<dd> All the OpenBSD specific patches (except for the installation specific ones) have been merged back to the main distribution.</p>
<dt>&bull;</p>
<dd> Perl has been tested with the <font SIZE="-1">GNU</font> pth userlevel thread package ( <a rel="nofollow" href="http://www.gnu.org/software/pth/pth.html">http://www.gnu.org/software/pth/pth.html</a> ). All thread tests of Perl now work, but not without adding some <code>yield()</code>s to the tests, so while pth (and other userlevel thread implementations) can be considered to be &#8220;working&#8221; with Perl ithreads, keep in mind the possible non-preemptability of the underlying thread implementation.</p>
<dt>&bull;</p>
<dd> Stratus <font SIZE="-1">VOS</font> is now supported using Perl&#8217;s native build method (Configure). This is the recommended method to build Perl on <font SIZE="-1">VOS.</font> The older methods, which build miniperl, are still available. See perlvos. [561+]</p>
<dt>&bull;</p>
<dd> The Amdahl <font SIZE="-1">UTS</font> Unix mainframe platform is now supported. [561]</p>
<dt>&bull;</p>
<dd> WinCE is now supported. See perlce.</p>
<dt>&bull;</p>
<dd> z/OS (formerly known as <font SIZE="-1">OS/390,</font> formerly known as <font SIZE="-1">MVS OE</font>) now has support for dynamic loading. This is not selected by default, however, you must specify -Dusedl in the arguments of Configure. [561]</dl>
<h2>Selected Bug Fixes</h2>
<p> Numerous memory leaks and uninitialized memory accesses have been hunted down. Most importantly, anonymous subs used to leak quite a bit. [561]</p>
<dl>
<dt>&bull;</p>
<dd> The autouse pragma didn&#8217;t work for Multi::Part::Function::Names.</p>
<dt>&bull;</p>
<dd> <code>caller()</code> could cause core dumps in certain situations. Carp was sometimes affected by this problem. In particular, <code>caller()</code> now returns a subroutine name of <tt>&quot;(unknown)&quot;</tt> for subroutines that have been removed from the symbol table.</p>
<dt>&bull;</p>
<dd> chop(@list) in list context returned the characters chopped in reverse order. This has been reversed to be in the right order. [561]</p>
<dt>&bull;</p>
<dd> Configure no longer includes the <font SIZE="-1">DBM</font> libraries (dbm, gdbm, db, ndbm) when building the Perl binary. The only exception to this is SunOS 4.x, which needs them. [561]</p>
<dt>&bull;</p>
<dd> The behaviour of non-decimal but numeric string constants such as &#8220;0x23&#8221; was platform-dependent: in some platforms that was seen as 35, in some as 0, in some as a floating point number (don&#8217;t ask). This was caused by Perl&#8217;s using the operating system libraries in a situation where the result of the string to number conversion is undefined: now Perl consistently handles such strings as zero in numeric contexts.</p>
<dt>&bull;</p>
<dd> Several debugger fixes: exit code now reflects the script exit code, condition <tt>&quot;0&quot;</tt> now treated correctly, the <tt>&quot;d&quot;</tt> command now checks line number, <tt>$.</tt> no longer gets corrupted, and all debugger output now goes correctly to the socket if RemotePort is set. [561]</p>
<dt>&bull;</p>
<dd> The debugger (perl5db.pl) has been modified to present a more consistent commands interface, via (CommandSet=580). perl5db.t was also added to test the changes, and as a placeholder for further tests. </p>
<p> See perldebug.</p>
<dt>&bull;</p>
<dd> The debugger has a new <tt>&quot;dumpDepth&quot;</tt> option to control the maximum depth to which nested structures are dumped. The <tt>&quot;x&quot;</tt> command has been extended so that <tt>&quot;x N EXPR&quot;</tt> dumps out the value of <i></i><font SIZE="-1"><i>EXPR</i></font><i></i> to a depth of at most <i>N</i> levels.</p>
<dt>&bull;</p>
<dd> The debugger can now show lexical variables if you have the <font SIZE="-1">CPAN</font> module PadWalker installed.</p>
<dt>&bull;</p>
<dd> The order of DESTROYs has been made more predictable.</p>
<dt>&bull;</p>
<dd> Perl 5.6.0 could emit spurious warnings about redefinition of <code>dl_error()</code> when statically building extensions into perl. This has been corrected. [561]</p>
<dt>&bull;</p>
<dd> dprofpp -R didn&#8217;t work.</p>
<dt>&bull;</p>
<dd> <tt>*foo{FORMAT}</tt> now works.</p>
<dt>&bull;</p>
<dd> Infinity is now recognized as a number.</p>
<dt>&bull;</p>
<dd> UNIVERSAL::isa no longer caches methods incorrectly. (This broke the Tk extension with 5.6.0.) [561]</p>
<dt>&bull;</p>
<dd> Lexicals I: lexicals outside an eval &quot;&#8220; weren&#8217;t resolved correctly inside a subroutine definition inside the eval &#8221;&#8220; if they were not already referenced in the top level of the eval&#8221;&quot;ed code.</p>
<dt>&bull;</p>
<dd> Lexicals <font SIZE="-1">II:</font> lexicals leaked at file scope into subroutines that were declared before the lexicals.</p>
<dt>&bull;</p>
<dd> Lexical warnings now propagating correctly between scopes and into <tt>&quot;eval &quot;...&quot;&quot;</tt>.</p>
<dt>&bull;</p>
<dd> <tt>&quot;use warnings qw(FATAL all)&quot;</tt> did not work as intended. This has been corrected. [561]</p>
<dt>&bull;</p>
<dd> <code>warnings::enabled()</code> now reports the state of $^W correctly if the caller isn&#8217;t using lexical warnings. [561]</p>
<dt>&bull;</p>
<dd> Line renumbering with eval and <tt>&quot;#line&quot;</tt> now works. [561]</p>
<dt>&bull;</p>
<dd> Fixed numerous memory leaks, especially in eval &quot;&quot;.</p>
<dt>&bull;</p>
<dd> Localised tied variables no longer leak memory </p>
<p>use Tie::Hash;<br />
tie my % tied_hash = &gt; &#8216;Tie::StdHash&#8217;;<br />
&#8230;<br />
#Used to leak memory every time local() was called;<br />
#in a loop, this added up.<br />
    local($tied_hash{Foo}) = 1;</p>
<dt>&bull;</p>
<dd> Localised hash elements (and <tt>%ENV</tt>) are correctly unlocalised to not exist, if they didn&#8217;t before they were localised. </p>
<p>use Tie::Hash;<br />
tie my % tied_hash = &gt; &#8216;Tie::StdHash&#8217;;<br />
&#8230;<br />
#Nothing has set the FOO element so far<br />
    {local $tied_hash{FOO} = &#8216;Bar&#8217;}<br />
#This used to print, but not now.<br />
print &#8220;exists!
&#8221; if exists $tied_hash{FOO};</p>
<p> As a side effect of this fix, tied hash interfaces <code>must</code> define the <font SIZE="-1">EXISTS</font> and <font SIZE="-1">DELETE</font> methods.</p>
<dt>&bull;</p>
<dd> <code>mkdir()</code> now ignores trailing slashes in the directory name, as mandated by <font SIZE="-1">POSIX.</font></p>
<dt>&bull;</p>
<dd> Some versions of glibc have a broken <code>modfl()</code>. This affects builds with <tt>&quot;-Duselongdouble&quot;</tt>. This version of Perl detects this brokenness and has a workaround for it. The glibc release 2.2.2 is known to have fixed the <code>modfl()</code> bug.</p>
<dt>&bull;</p>
<dd> Modulus of unsigned numbers now works (4063328477 % 65535 used to return 27406, instead of 27047). [561]</p>
<dt>&bull;</p>
<dd> Some &#8220;not a number&#8221; warnings introduced in 5.6.0 eliminated to be more compatible with 5.005. Infinity is now recognised as a number. [561]</p>
<dt>&bull;</p>
<dd> Numeric conversions did not recognize changes in the string value properly in certain circumstances. [561]</p>
<dt>&bull;</p>
<dd> Attributes (such as :shared) didn&#8217;t work with <code>our()</code>.</p>
<dt>&bull;</p>
<dd> <code>our()</code> variables will not cause bogus &#8220;Variable will not stay shared&#8221; warnings. [561]</p>
<dt>&bull;</p>
<dd> &#8220;our&#8221; variables of the same name declared in two sibling blocks resulted in bogus warnings about &#8220;redeclaration&#8221; of the variables. The problem has been corrected. [561]</p>
<dt>&bull;</p>
<dd> pack &#8220;Z&#8221; now correctly terminates the string with &#8220;
