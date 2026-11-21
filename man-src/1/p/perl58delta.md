---
title: "perl58delta(1)"
name: "perl58delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl58delta/"
description: "perl58delta – what is new for perl v5.8.0"
---
<h2 class="name">NAME</h2>
<p> perl58delta - what is new for perl v5.8.0 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.6.0 release and the 5.8.0 release. </p>
<p> Many of the bug fixes in 5.8.0 were already seen in the 5.6.1 maintenance release since the two releases were kept closely coordinated (while 5.8.0 was still called 5.7.something). </p>
<p> Changes that were integrated into the 5.6.1 release are marked <code>&quot;[561]&quot;</code>. Many of these changes have been further developed since 5.6.1 was released, those are marked <code>&quot;[561+]&quot;</code>. </p>
<p> You can see the list of changes in the 5.6.1 release (both from the 5.005_03 release and the 5.6.0 release) by reading perl561delta.  </p>
<h2>Highlights In 5.8.0</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> Better Unicode support </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> New <font SIZE="-1">IO</font> Implementation </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> New Thread Implementation </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Better Numeric Accuracy </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Safe Signals </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Many New Modules </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> More Extensive Regression Testing </p>
 </dd></dl>
<h2>Incompatible Changes</h2>
<h3>Binary Incompatibility</h3>
<p> <code>Perl 5.8 is not binary compatible with earlier releases of Perl.</code> </p>
<p> <code>You have to recompile your </code><font SIZE="-1"><code>XS</code></font><code> modules.</code> </p>
<p> (Pure Perl modules should continue to work.) </p>
<p> The major reason for the discontinuity is the new <font SIZE="-1">IO</font> architecture called PerlIO. PerlIO is the default configuration because without it many new features of Perl 5.8 cannot be used. In other words: you just have to recompile your modules containing <font SIZE="-1">XS</font> code, sorry about that. </p>
<p> In future releases of Perl, non-PerlIO aware <font SIZE="-1">XS</font> modules may become completely unsupported. This shouldn&#8217;t be too difficult for module authors, however: PerlIO has been designed as a drop-in replacement (at the source code level) for the stdio interface. </p>
<p> Depending on your platform, there are also other reasons why we decided to break binary compatibility, please read on.  </p>
<h3>64-bit platforms and malloc</h3>
<p> If your pointers are 64 bits wide, the Perl malloc is no longer being used because it does not work well with 8-byte pointers. Also, usually the system mallocs on such platforms are much better optimized for such large memory models than the Perl malloc. Some memory-hungry Perl applications like the <font SIZE="-1">PDL</font> don&#8217;t work well with Perl&#8217;s malloc. Finally, other applications than Perl (such as mod_perl) tend to prefer the system malloc. Such platforms include Alpha and 64-bit <font SIZE="-1">HPPA, MIPS, PPC,</font> and Sparc.  </p>
<font SIZE="-1"></font><h3>AIX Dynaloading</h3>
<p> The <font SIZE="-1">AIX</font> dynaloading now uses in <font SIZE="-1">AIX</font> releases 4.3 and newer the native dlopen interface of <font SIZE="-1">AIX</font> instead of the old emulated interface. This change will probably break backward compatibility with compiled modules. The change was made to make Perl more compliant with other applications like mod_perl which are using the <font SIZE="-1">AIX</font> native interface.  </p>
<h3>Attributes for my variables now handled at run-time</h3>
<p> The <code>&quot;my EXPR : ATTRS&quot;</code> syntax now applies variable attributes at run-time. (Subroutine and <code>&quot;our&quot;</code> variables still get attributes applied at compile-time.) See attributes for additional details. In particular, however, this allows variable attributes to be useful for <code>&quot;tie&quot;</code> interfaces, which was a deficiency of earlier releases. Note that the new semantics doesn&#8217;t work with the Attribute::Handlers module (as of version 0.76).  </p>
<font SIZE="-1"></font><h3>Socket Extension Dynamic in VMS</h3>
<p> The Socket extension is now dynamically loaded instead of being statically built in. This may or may not be a problem with ancient <font SIZE="-1">TCP/IP</font> stacks of <font SIZE="-1">VMS:</font> we do not know since we weren&#8217;t able to test Perl in such configurations.  </p>
<h3>IEEE-format Floating Point Default on OpenVMS Alpha</h3>
<p> Perl now uses <font SIZE="-1">IEEE</font> format (T_FLOAT) as the default internal floating point format on OpenVMS Alpha, potentially breaking binary compatibility with external libraries or existing data. G_FLOAT is still available as a configuration option. The default on <font SIZE="-1">VAX</font> (D_FLOAT) has not changed.  </p>
<h3>New Unicode Semantics (no more use utf8, almost)</h3>
<p> Previously in Perl 5.6 to use Unicode one would say ``use utf8&#8217;&#8216; and then the operations (like string concatenation) were Unicode-aware in that lexical scope. </p>
<p> This was found to be an inconvenient interface, and in Perl 5.8 the Unicode model has completely changed: now the ``Unicodeness&#8217;&#8216; is bound to the data itself, and for most of the time ``use utf8&#8217;&#8216; is not needed at all. The only remaining use of ``use utf8&#8217;&#8216; is when the Perl script itself has been written in the <font SIZE="-1">UTF-8</font> encoding of Unicode. (<font SIZE="-1">UTF-8</font> has not been made the default since there are many Perl scripts out there that are using various national eight-bit character sets, which would be illegal in <font SIZE="-1">UTF-8.</font>) </p>
<p> See perluniintro for the explanation of the current model, and utf8 for the current use of the utf8 pragma.  </p>
<h3>New Unicode Properties</h3>
<p> Unicode <i>scripts</i> are now supported. Scripts are similar to (and superior to) Unicode <i>blocks</i>. The difference between scripts and blocks is that scripts are the glyphs used by a language or a group of languages, while the blocks are more artificial groupings of (mostly) 256 characters based on the Unicode numbering. </p>
<p> In general, scripts are more inclusive, but not universally so. For example, while the script <code>&quot;Latin&quot;</code> includes all the Latin characters and their various diacritic-adorned versions, it does not include the various punctuation or digits (since they are not solely <code>&quot;Latin&quot;</code>). </p>
<p> A number of other properties are now supported, including <code>&quot;\p{L&amp;}&quot;</code>, <code>&quot;\p{Any}&quot;</code> <code>&quot;\p{Assigned}&quot;</code>, <code>&quot;\p{Unassigned}&quot;</code>, <code>&quot;\p{Blank}&quot;</code> [561] and <code>&quot;\p{SpacePerl}&quot;</code> [561] (along with their <code>&quot;\P{...}&quot;</code> versions, of course). See perlunicode for details, and more additions. </p>
<p> The <code>&quot;In&quot;</code> or <code>&quot;Is&quot;</code> prefix to names used with the <code>&quot;\p{...}&quot;</code> and <code>&quot;\P{...}&quot;</code> are now almost always optional. The only exception is that a <code>&quot;In&quot;</code> prefix is required to signify a Unicode block when a block name conflicts with a script name. For example, <code>&quot;\p{Tibetan}&quot;</code> refers to the script, while <code>&quot;\p{InTibetan}&quot;</code> refers to the block. When there is no name conflict, you can omit the <code>&quot;In&quot;</code> from the block name (e.g. <code>&quot;\p{BraillePatterns}&quot;</code>), but to be safe, it&#8217;s probably best to always use the <code>&quot;In&quot;</code>).  </p>
<font SIZE="-1"></font><font SIZE="-1"></font><h3>REF (...) Instead Of SCALAR (...)</h3>
<p> A reference to a reference now stringifies as ``<font SIZE="-1">REF</font>(0x81485ec)&#8216;&#8216; instead of ``<font SIZE="-1">SCALAR</font>(0x81485ec)&#8216;&#8216; in order to be more consistent with the return value of <code>ref()</code>.  </p>
<h3>pack/unpack D/F recycled</h3>
<p> The undocumented pack/unpack template letters D/F have been recycled for better use: now they stand for long double (if supported by the platform) and <font SIZE="-1">NV</font> (Perl internal floating point type). (They used to be aliases for d/f, but you never knew that.)  </p>
<code></code><h3>glob() now returns filenames in alphabetical order</h3>
<p> The list of filenames from <code>glob()</code> (or &lt;...&gt;) is now by default sorted alphabetically to be csh-compliant (which is what happened before in most Unix platforms). (<code>bsd_glob()</code> does still sort platform natively, <font SIZE="-1">ASCII</font> or <font SIZE="-1">EBCDIC,</font> unless <font SIZE="-1">GLOB_ALPHASORT</font> is specified.) [561]  </p>
<h3>Deprecations</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> The semantics of bless(<font SIZE="-1">REF, REF</font>) were unclear and until someone proves it to make some sense, it is forbidden. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The obsolete chat2 library that should never have been allowed to escape the laboratory has been decommissioned. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Using chdir(&quot;&quot;) or chdir(undef) instead of explicit <code>chdir()</code> is doubtful. A failure (think chdir(<code>some_function()</code>) can lead into unintended <code>chdir()</code> to the home directory, therefore this behaviour is deprecated. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The builtin <code>dump()</code> function has probably outlived most of its usefulness. The core-dumping functionality will remain in future available as an explicit call to <code>&quot;CORE::dump()&quot;</code>, but in future releases the behaviour of an unqualified <code>&quot;dump()&quot;</code> call may change. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The very dusty examples in the eg/ directory have been removed. Suggestions for new shiny examples welcome but the main issue is that the examples need to be documented, tested and (most importantly) maintained. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The (bogus) escape sequences \8 and \9 now give an optional warning (``Unrecognized escape passed through&#8217;&#8216;). There is no need to \-escape any <code>&quot;\w&quot;</code> character. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The *glob{<font SIZE="-1">FILEHANDLE</font>} is deprecated, use *glob{<font SIZE="-1">IO</font>} instead. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;package;&quot;</code> syntax (<code>&quot;package&quot;</code> without an argument) has been deprecated. Its semantics were never that clear and its implementation even less so. If you have used that feature to disallow all but fully qualified variables, <code>&quot;use strict;&quot;</code> instead. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The unimplemented <font SIZE="-1">POSIX</font> regex features [[.cc.]] and [[=c=]] are still recognised but now cause fatal errors. The previous behaviour of ignoring them by default and warning if requested was unacceptable since it, in a way, falsely promised that the features could be used. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In future releases, non-PerlIO aware <font SIZE="-1">XS</font> modules may become completely unsupported. Since PerlIO is a drop-in replacement for stdio at the source code level, this shouldn&#8217;t be that drastic a change. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Previous versions of perl and some readings of some sections of Camel <font SIZE="-1">III</font> implied that the <code>&quot;:raw&quot;</code> ``discipline&#8217;&#8216; was the inverse of <code>&quot;:crlf&quot;</code>. Turning off ``clrfness&#8217;&#8216; is no longer enough to make a stream truly binary. So the PerlIO <code>&quot;:raw&quot;</code> layer (or ``discipline&#8217;&#8216;, to use the Camel book&#8217;s older terminology) is now formally defined as being equivalent to binmode(<font SIZE="-1">FH</font>) - which is in turn defined as doing whatever is necessary to pass each byte as-is without any translation. In particular binmode(<font SIZE="-1">FH</font>) - and hence <code>&quot;:raw&quot;</code> - will now turn off both <font SIZE="-1">CRLF</font> and <font SIZE="-1">UTF-8</font> translation and remove other layers (e.g. :<code>encoding()</code>) which would modify byte stream. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The current user-visible implementation of pseudo-hashes (the weird use of the first array element) is deprecated starting from Perl 5.8.0 and will be removed in Perl 5.10.0, and the feature will be implemented differently. Not only is the current interface rather ugly, but the current implementation slows down normal array and hash use quite noticeably. The <code>&quot;fields&quot;</code> pragma interface will remain available. The <i>restricted hashes</i> interface is expected to be the replacement interface (see Hash::Util). If your existing programs depends on the underlying implementation, consider using Class::PseudoHash from <font SIZE="-1">CPAN.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The syntaxes <code>&quot;@a-&gt;[...]&quot;</code> and <code>&quot;%h-&gt;{...}&quot;</code> have now been deprecated. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> After years of trying, suidperl is considered to be too complex to ever be considered truly secure. The suidperl functionality is likely to be removed in a future release. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The 5.005 threads model (module <code>&quot;Thread&quot;</code>) is deprecated and expected to be removed in Perl 5.10. Multithreaded code should be migrated to the new ithreads model (see threads, threads::shared and perlthrtut). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The long deprecated uppercase aliases for the string comparison operators (<font SIZE="-1">EQ, NE, LT, LE, GE, GT</font>) have now been removed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The tr///C and tr///U features have been removed and will not return; the interface was a mistake. Sorry about that. For similar functionality, see pack(&#8216;U0&#8217;, ...) and pack(&#8216;C0&#8217;, ...). [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Earlier Perls treated ``sub foo (@bar)&#8216;&#8216; as equivalent to ``sub foo (@)&#8216;&#8216;. The prototypes are now checked better at compile-time for invalid syntax. An optional warning is generated (``Illegal character in prototype...&#8216;&#8216;) but this may be upgraded to a fatal error in a future release. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;exec LIST&quot;</code> and <code>&quot;system LIST&quot;</code> operations now produce warnings on tainted data and in some future release they will produce fatal errors. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The existing behaviour when localising tied arrays and hashes is wrong, and will be changed in a future release, so do not rely on the existing behaviour. See ``Localising Tied Arrays and Hashes Is Broken&#8217;&#8216;. </p>
 </dd></dl>
<h2>Core Enhancements</h2>
<h3>Unicode Overhaul</h3>
<p> Unicode in general should be now much more usable than in Perl 5.6.0 (or even in 5.6.1). Unicode can be used in hash keys, Unicode in regular expressions should work now, Unicode in tr/// should work now, Unicode in I/O should work now. See perluniintro for introduction and perlunicode for details. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The Unicode Character Database coming with Perl has been upgraded to Unicode 3.2.0. For more information, see <a rel="nofollow" href="http://www.unicode.org/">http://www.unicode.org/</a> . [561+] (5.6.1 has <font SIZE="-1">UCD 3.0.1.</font>) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> For developers interested in enhancing Perl&#8217;s Unicode capabilities: almost all the <font SIZE="-1">UCD</font> files are included with the Perl distribution in the <i>lib/unicore</i> subdirectory. The most notable omission, for space considerations, is the Unihan database. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The properties \p{Blank} and \p{SpacePerl} have been added. ``Blank&#8217;&#8216; is like C <code>isblank()</code>, that is, it contains only ``horizontal whitespace&#8217;&#8216; (the space character is, the newline isn&#8217;t), and the ``SpacePerl&#8217;&#8216; is the Unicode equivalent of <code>&quot;\s&quot;</code> (\p{Space} isn&#8217;t, since that includes the vertical tabulator character, whereas <code>&quot;\s&quot;</code> doesn&#8217;t.) </p>
<p> See ``New Unicode Properties&#8217;&#8216; earlier in this document for additional information on changes with Unicode properties. </p>
 </dd></dl>
<h3>PerlIO is Now The Default</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">IO</font> is now by default done via PerlIO rather than system&#8217;s ``stdio&#8217;&#8216;. PerlIO allows ``layers&#8217;&#8216; to be ``pushed&#8217;&#8216; onto a file handle to alter the handle&#8217;s behaviour. Layers can be specified at open time via 3-arg form of open: </p>
<pre><code>   open($fh,'&gt;:crlf :utf8', $path) || ...
</code></pre>
<p> or on already opened handles via extended <code>&quot;binmode&quot;</code>: </p>
<pre><code>   binmode($fh,':encoding(iso-8859-7)');
</code></pre>
<p> The built-in layers are: unix (low level read/write), stdio (as in previous Perls), perlio (re-implementation of stdio buffering in a portable manner), crlf (does <font SIZE="-1">CRLF</font> &lt;=&gt; ``\n&#8217;&#8216; translation as on Win32, but available on any platform). A mmap layer may be available if platform supports it (mostly Unixes). </p>
<p> Layers to be applied by default may be specified via the &#8216;open&#8217; pragma. </p>
<p> See ``Installation and Configuration Improvements&#8217;&#8216; for the effects of PerlIO on your architecture name. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> If your platform supports <code>fork()</code>, you can use the list form of <code>&quot;open&quot;</code> for pipes. For example: </p>
<pre><code>    open KID_PS, &quot;-|&quot;, &quot;ps&quot;, &quot;aux&quot; or die $!;
</code></pre>
<p> forks the <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1) command (without spawning a shell, as there are more than three arguments to <code>open()</code>), and reads its standard output via the <code>&quot;KID_PS&quot;</code> filehandle. See perlipc. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File handles can be marked as accepting Perl&#8217;s internal encoding of Unicode (<font SIZE="-1">UTF-8</font> or UTF-EBCDIC depending on platform) by a pseudo layer ``:utf8&#8217;&#8216; : </p>
<pre><code>   open($fh,&quot;&gt;:utf8&quot;,&quot;Uni.txt&quot;);
</code></pre>
<p> Note for <font SIZE="-1">EBCDIC</font> users: the pseudo layer ``:utf8&#8217;&#8216; is erroneously named for you since it&#8217;s not <font SIZE="-1">UTF-8</font> what you will be getting but instead UTF-EBCDIC. See perlunicode, utf8, and <a rel="nofollow" href="http://www.unicode.org/unicode/reports/tr16/">http://www.unicode.org/unicode/reports/tr16/</a> for more information. In future releases this naming may change. See perluniintro for more information about <font SIZE="-1">UTF-8.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> If your environment variables (<font SIZE="-1">LC_ALL, LC_CTYPE, LANG</font>) look like you want to use <font SIZE="-1">UTF-8</font> (any of the variables match <code>&quot;/utf-?8/i&quot;</code>), your <font SIZE="-1">STDIN, STDOUT, STDERR</font> handles and the default open layer (see open) are marked as <font SIZE="-1">UTF-8.</font> (This feature, like other new features that combine Unicode and I/O, work only if you are using PerlIO, but that&#8217;s the default.) </p>
<p> Note that after this Perl really does assume that everything is <font SIZE="-1">UTF-8:</font> for example if some input handle is not, Perl will probably very soon complain about the input data like this ``Malformed <font SIZE="-1">UTF-8 ...&#8216;&#8216;</font> since any old eight-bit data is not legal <font SIZE="-1">UTF-8.</font> </p>
<p> Note for code authors: if you want to enable your users to use <font SIZE="-1">UTF-8</font> as their default encoding but in your code still have eight-bit I/O streams (such as images or zip files), you need to explicitly <code>open()</code> or <code>binmode()</code> with <code>&quot;:bytes&quot;</code> (see ``open&#8217;&#8216; in perlfunc and ``binmode&#8217;&#8216; in perlfunc), or you can just use <code>&quot;binmode(FH)&quot;</code> (nice for pre-5.8.0 backward compatibility). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File handles can translate character encodings from/to Perl&#8217;s internal Unicode form on read/write via the ``:<code>encoding()</code>&#8216;&#8216; layer. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File handles can be opened to ``in memory&#8217;&#8216; files held in Perl scalars via: </p>
<pre><code>   open($fh,'&gt;', \$variable) || ...
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Anonymous temporary files are available without need to &#8216;use FileHandle&#8217; or other module via </p>
<pre><code>   open($fh,&quot;+&gt;&quot;, undef) || ...
</code></pre>
<p> That is a literal undef, not an undefined value. </p>
 </dd></dl>
<h3>ithreads</h3>
<p> The new interpreter threads (``ithreads&#8217;&#8216; for short) implementation of multithreading, by Arthur Bergman, replaces the old ``5.005 threads&#8217;&#8216; implementation. In the ithreads model any data sharing between threads must be explicit, as opposed to the model where data sharing was implicit. See threads and threads::shared, and perlthrtut. </p>
<p> As a part of the ithreads implementation Perl will also use any necessary and detectable reentrant libc interfaces.  </p>
<h3>Restricted Hashes</h3>
<p> A restricted hash is restricted to a certain set of keys, no keys outside the set can be added. Also individual keys can be restricted so that the key cannot be deleted and the value cannot be changed. No new syntax is involved: the Hash::Util module is the interface.  </p>
<h3>Safe Signals</h3>
<p> Perl used to be fragile in that signals arriving at inopportune moments could corrupt Perl&#8217;s internal state. Now Perl postpones handling of signals until it&#8217;s safe (between opcodes). </p>
<p> This change may have surprising side effects because signals no longer interrupt Perl instantly. Perl will now first finish whatever it was doing, like finishing an internal operation (like <code>sort()</code>) or an external operation (like an I/O operation), and only then look at any arrived signals (and before starting the next operation). No more corrupt internal state since the current operation is always finished first, but the signal may take more time to get heard. Note that breaking out from potentially blocking operations should still work, though.  </p>
<h3>Understanding of Numbers</h3>
<p> In general a lot of fixing has happened in the area of Perl&#8217;s understanding of numbers, both integer and floating point. Since in many systems the standard number parsing functions like <code>&quot;strtoul()&quot;</code> and <code>&quot;atof()&quot;</code> seem to have bugs, Perl tries to work around their deficiencies. This results hopefully in more accurate numbers. </p>
<p> Perl now tries internally to use integer values in numeric conversions and basic arithmetics (+ - * /) if the arguments are integers, and tries also to keep the results stored internally as integers. This change leads to often slightly faster and always less lossy arithmetics. (Previously Perl always preferred floating point numbers in its math.)  </p>
<h3>Arrays now always interpolate into double-quoted strings [561]</h3>
<p> In double-quoted strings, arrays now interpolate, no matter what. The behavior in earlier versions of perl 5 was that arrays would interpolate into strings if the array had been mentioned before the string was compiled, and otherwise Perl would raise a fatal compile-time error. In versions 5.000 through 5.003, the error was </p>
<pre><code>        Literal @example now requires backslash
</code></pre>
<p> In versions 5.004_01 through 5.6.0, the error was </p>
<pre><code>        In string, @example now must be written as \@example
</code></pre>
<p> The idea here was to get people into the habit of writing <code>&quot;fred\@example.com&quot;</code> when they wanted a literal <code>&quot;@&quot;</code> sign, just as they have always written <code>&quot;Give me back my \$5&quot;</code> when they wanted a literal <code>&quot;$&quot;</code> sign. </p>
<p> Starting with 5.6.1, when Perl now sees an <code>&quot;@&quot;</code> sign in a double-quoted string, it <i>always</i> attempts to interpolate an array, regardless of whether or not the array has been used or declared already. The fatal error has been downgraded to an optional warning: </p>
<pre><code>        Possible unintended interpolation of @example in string
</code></pre>
<p> This warns you that <code>&quot;fred [at] example.com&quot;</code> is going to turn into <code>&quot;fred.com&quot;</code> if you don&#8217;t backslash the <code>&quot;@&quot;</code>. See <a rel="nofollow" href="http://perl.plover.com/at-error.html">http://perl.plover.com/at-error.html</a> for more details about the history here.  </p>
<h3>Miscellaneous Changes</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">AUTOLOAD</font> is now lvaluable, meaning that you can add the :lvalue attribute to <font SIZE="-1">AUTOLOAD</font> subroutines and you can assign to the <font SIZE="-1">AUTOLOAD</font> return value. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>$Config</code>{byteorder} (and corresponding <font SIZE="-1">BYTEORDER</font> in config.h) was previously wrong in platforms if sizeof(long) was 4, but sizeof(<font SIZE="-1">IV</font>) was 8. The byteorder was only sizeof(long) bytes long (1234 or 4321), but now it is correctly sizeof(<font SIZE="-1">IV</font>) bytes long, (12345678 or 87654321). (This problem didn&#8217;t affect Windows platforms.) </p>
<p> Also, <code>$Config</code>{byteorder} is now computed dynamically---this is more robust with ``fat binaries&#8217;&#8216; where an executable image contains binaries for more than one binary platform, and when cross-compiling. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;perl -d:Module=arg,arg,arg&quot;</code> now works (previously one couldn&#8217;t pass in multiple arguments.) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;do&quot;</code> followed by a bareword now ensures that this bareword isn&#8217;t a keyword (to avoid a bug where <code>&quot;do q(foo.pl)&quot;</code> tried to call a subroutine called <code>&quot;q&quot;</code>). This means that for example instead of <code>&quot;do format()&quot;</code> you must write <code>&quot;do &amp;format()&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The builtin <code>dump()</code> now gives an optional warning <code>&quot;dump() better written as CORE::dump()&quot;</code>, meaning that by default <code>&quot;dump(...)&quot;</code> is resolved as the builtin <code>dump()</code> which dumps core and aborts, not as (possibly) user-defined <code>&quot;sub dump&quot;</code>. To call the latter, qualify the call as <code>&quot;&amp;dump(...)&quot;</code>. (The whole <code>dump()</code> feature is to considered deprecated, and possibly removed/changed in future releases.) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>chomp()</code> and <code>chop()</code> are now overridable. Note, however, that their prototype (as given by <code>&quot;prototype(&quot;CORE::chomp&quot;)&quot;</code> is undefined, because it cannot be expressed and therefore one cannot really write replacements to override these builtins. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">END</font> blocks are now run even if you exit/die in a <font SIZE="-1">BEGIN</font> block. Internally, the execution of <font SIZE="-1">END</font> blocks is now controlled by PL_exit_flags &amp; <font SIZE="-1">PERL_EXIT_DESTRUCT_END.</font> This enables the new behaviour for Perl embedders. This will default in 5.10. See perlembed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Formats now support zero-padded decimal fields. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Although ``you shouldn&#8217;t do that&#8217;&#8216;, it was possible to write code that depends on Perl&#8217;s hashed key order (Data::Dumper does this). The new algorithm ``One-at-a-Time&#8217;&#8216; produces a different hashed key order. More details are in ``Performance Enhancements&#8217;&#8216;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> lstat(<font SIZE="-1">FILEHANDLE</font>) now gives a warning because the operation makes no sense. In future releases this may become a fatal error. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Spurious syntax errors generated in certain situations, when <code>glob()</code> caused File::Glob to be loaded for the first time, have been fixed. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Lvalue subroutines can now return <code>&quot;undef&quot;</code> in list context. However, the lvalue subroutine feature still remains experimental. [561+] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A lost warning ``Can&#8217;t declare ... dereference in my&#8217;&#8216; has been restored (Perl had it earlier but it became lost in later releases.) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new special regular expression variable has been introduced: <code>$^N</code>, which contains the most-recently closed group (submatch). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;no Module;&quot;</code> does not produce an error even if Module does not have an <code>unimport()</code> method. This parallels the behavior of <code>&quot;use&quot;</code> vis-a-vis <code>&quot;import&quot;</code>. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The numerical comparison operators return <code>&quot;undef&quot;</code> if either operand is a NaN. Previously the behaviour was unspecified. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;our&quot;</code> can now have an experimental optional attribute <code>&quot;unique&quot;</code> that affects how global variables are shared among multiple interpreters, see ``our&#8217;&#8216; in perlfunc. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The following builtin functions are now overridable: <code>each()</code>, <code>keys()</code>, <code>pop()</code>, <code>push()</code>, <code>shift()</code>, <code>splice()</code>, <code>unshift()</code>. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;pack() / unpack()&quot;</code> can now group template letters with <code>&quot;()&quot;</code> and then apply repetition/count modifiers on the groups. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;pack() / unpack()&quot;</code> can now process the Perl internal numeric types: IVs, UVs, NVs--- and also long doubles, if supported by the platform. The template letters are <code>&quot;j&quot;</code>, <code>&quot;J&quot;</code>, <code>&quot;F&quot;</code>, and <code>&quot;D&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;pack(&#8216;U0a*&#8216;, ...)&quot;</code> can now be used to force a string to <font SIZE="-1">UTF-8.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> my __PACKAGE__ <code>$obj</code> now works. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>POSIX::sleep()</code> now returns the number of <i>unslept</i> seconds (as the <font SIZE="-1">POSIX</font> standard says), as opposed to <code>CORE::sleep()</code> which returns the number of slept seconds. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>printf()</code> and <code>sprintf()</code> now support parameter reordering using the <code>&quot;%\d+\$&quot;</code> and <code>&quot;*\d+\$&quot;</code> syntaxes. For example </p>
<pre><code>    printf &quot;%2\$s %1\$s\n&quot;, &quot;foo&quot;, &quot;bar&quot;;
</code></pre>
<p> will print ``bar foo\n&#8217;&#8216;. This feature helps in writing internationalised software, and in general when the order of the parameters can vary. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The (\&amp;) prototype now works properly. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> prototype(\[$@%&amp;]) is now available to implicitly create references (useful for example if you want to emulate the <code>tie()</code> interface). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new command-line option, <code>&quot;-t&quot;</code> is available. It is the little brother of <code>&quot;-T&quot;</code>: instead of dying on taint violations, lexical warnings are given. <code>This is only meant as a temporary debugging aid while securing the code of old legacy applications. This is not a substitute for -T.</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In other taint news, the <code>&quot;exec LIST&quot;</code> and <code>&quot;system LIST&quot;</code> have now been considered too risky (think <code>&quot;exec @ARGV&quot;</code>: it can start any program with any arguments), and now the said forms cause a warning under lexical warnings. You should carefully launder the arguments to guarantee their validity. In future releases of Perl the forms will become fatal errors so consider starting laundering now. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Tied hash interfaces are now required to have the <font SIZE="-1">EXISTS</font> and <font SIZE="-1">DELETE</font> methods (either own or inherited). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> If tr/// is just counting characters, it doesn&#8217;t attempt to modify its target. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>untie()</code> will now call an <font SIZE="-1"><code>UNTIE</code></font><code>()</code> hook if it exists. See perltie for details. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ``utime&#8217;&#8216; in perlfunc now supports <code>&quot;utime undef, undef, @files&quot;</code> to change the file timestamps to the current time. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The rules for allowing underscores (underbars) in numeric constants have been relaxed and simplified: now you can have an underscore simply <code>between digits</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Rather than relying on C&#8217;s argv[0] (which may not contain a full pathname) where possible $^X is now set by asking the operating system. (eg by reading <i>/proc/self/exe</i> on Linux, <i>/proc/curproc/file</i> on FreeBSD) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new variable, <code>&quot;${^TAINT}&quot;</code>, indicates whether taint mode is enabled. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> You can now override the <code>readline()</code> builtin, and this overrides also the &lt;<font SIZE="-1">FILEHANDLE</font>&gt; angle bracket operator. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The command-line options -s and -F are now recognized on the shebang (#!) line. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Use of the <code>&quot;/c&quot;</code> match modifier without an accompanying <code>&quot;/g&quot;</code> modifier elicits a new warning: <code>&quot;Use of /c modifier is meaningless without /g&quot;</code>. </p>
<p> Use of <code>&quot;/c&quot;</code> in substitutions, even with <code>&quot;/g&quot;</code>, elicits <code>&quot;Use of /c modifier is meaningless in s///&quot;</code>. </p>
<p> Use of <code>&quot;/g&quot;</code> with <code>&quot;split&quot;</code> elicits <code>&quot;Use of /g modifier is meaningless in split&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Support for the <code>&quot;CLONE&quot;</code> special subroutine had been added. With ithreads, when a new thread is created, all Perl data is cloned, however non-Perl data cannot be cloned automatically. In <code>&quot;CLONE&quot;</code> you can do whatever you need to do, like for example handle the cloning of non-Perl data, if necessary. <code>&quot;CLONE&quot;</code> will be executed once for every package that has it defined or inherited. It will be called in the context of the new thread, so all modifications are made in the new area. </p>
<p> See perlmod </p>
 </dd></dl>
<h2>Modules and Pragmata</h2>
<h3>New Modules and Pragmata</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Attribute::Handlers&quot;</code>, originally by Damian Conway and now maintained by Arthur Bergman, allows a class to define attribute handlers. </p>
<pre><code>    package MyPack;
    use Attribute::Handlers;
    sub Wolf :ATTR(SCALAR) { print &quot;howl!\n&quot; }
    # later, in some package using or inheriting from MyPack...
    my MyPack $Fluffy : Wolf; # the attribute handler Wolf will be called
</code></pre>
<p> Both variables and routines can have attribute handlers. Handlers can be specific to type (<font SIZE="-1">SCALAR, ARRAY, HASH,</font> or <font SIZE="-1">CODE</font>), or specific to the exact compilation phase (<font SIZE="-1">BEGIN, CHECK, INIT,</font> or <font SIZE="-1">END</font>). See Attribute::Handlers. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;B::Concise&quot;</code>, by Stephen McCamant, is a new compiler backend for walking the Perl syntax tree, printing concise info about ops. The output is highly customisable. See B::Concise. [561+] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The new bignum, bigint, and bigrat pragmas, by Tels, implement transparent bignum support (using the Math::BigInt, Math::BigFloat, and Math::BigRat backends). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Class::ISA&quot;</code>, by Sean Burke, is a module for reporting the search path for a class&#8217;s <font SIZE="-1">ISA</font> tree. See Class::ISA. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Cwd&quot;</code> now has a split personality: if possible, an <font SIZE="-1">XS</font> extension is used, (this will hopefully be faster, more secure, and more robust) but if not possible, the familiar Perl implementation is used. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Devel::PPPort&quot;</code>, originally by Kenneth Albanowski and now maintained by Paul Marquess, has been added. It is primarily used by <code>&quot;h2xs&quot;</code> to enhance portability of <font SIZE="-1">XS</font> modules between different versions of Perl. See Devel::PPPort. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Digest&quot;</code>, frontend module for calculating digests (checksums), from Gisle Aas, has been added. See Digest. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Digest::MD5&quot;</code> for calculating <font SIZE="-1">MD5</font> digests (checksums) as defined in <font SIZE="-1">RFC 1321,</font> from Gisle Aas, has been added. See Digest::MD5. </p>
<pre><code>    use Digest::MD5 'md5_hex';
    $digest = md5_hex(&quot;Thirsty Camel&quot;);
    print $digest, &quot;\n&quot;; # 01d19d9d2045e005c3f1b80e8b164de1
</code></pre>
<p> <font SIZE="-1">NOTE:</font> the <code>&quot;MD5&quot;</code> backward compatibility module is deliberately not included since its further use is discouraged. </p>
<p> See also PerlIO::via::QuotedPrint. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Encode&quot;</code>, originally by Nick Ing-Simmons and now maintained by Dan Kogai, provides a mechanism to translate between different character encodings. Support for Unicode, <font SIZE="-1">ISO-8859-1,</font> and <font SIZE="-1">ASCII</font> are compiled in to the module. Several other encodings (like the rest of the <font SIZE="-1">ISO-8859,</font> CP*/Win*, Mac, <font SIZE="-1">KOI8-R,</font> three variants <font SIZE="-1">EBCDIC,</font> Chinese, Japanese, and Korean encodings) are included and can be loaded at runtime. (For space considerations, the largest Chinese encodings have been separated into their own <font SIZE="-1">CPAN</font> module, Encode::HanExtra, which Encode will use if available). See Encode. </p>
<p> Any encoding supported by Encode module is also available to the ``:<code>encoding()</code>&#8216;&#8216; layer if PerlIO is used. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Hash::Util&quot;</code> is the interface to the new <i>restricted hashes</i> feature. (Implemented by Jeffrey Friedl, Nick Ing-Simmons, and Michael Schwern.) See Hash::Util. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;I18N::Langinfo&quot;</code> can be used to query locale information. See I18N::Langinfo. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;I18N::LangTags&quot;</code>, by Sean Burke, has functions for dealing with RFC3066-style language tags. See I18N::LangTags. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;ExtUtils::Constant&quot;</code>, by Nicholas Clark, is a new tool for extension writers for generating <font SIZE="-1">XS</font> code to import C header constants. See ExtUtils::Constant. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Filter::Simple&quot;</code>, by Damian Conway, is an easy-to-use frontend to Filter::Util::Call. See Filter::Simple. </p>
<pre><code>    # in MyFilter.pm:
    package MyFilter;
    use Filter::Simple sub {
        while (my ($from, $to) = splice @_, 0, 2) {
                s/$from/$to/g;
        }
    };
    1;
    # in user's code:
    use MyFilter qr/red/ =&gt; 'green';
    print &quot;red\n&quot;; # this code is filtered, will print &quot;green\n&quot;
    print &quot;bored\n&quot;; # this code is filtered, will print &quot;bogreen\n&quot;
    no MyFilter;
    print &quot;red\n&quot;; # this code is not filtered, will print &quot;red\n&quot;
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;File::Temp&quot;</code>, by Tim Jenness, allows one to create temporary files and directories in an easy, portable, and secure way. See File::Temp. [561+] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Filter::Util::Call&quot;</code>, by Paul Marquess, provides you with the framework to write <i>source filters</i> in Perl. For most uses, the frontend Filter::Simple is to be preferred. See Filter::Util::Call. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;if&quot;</code>, by Ilya Zakharevich, is a new pragma for conditional inclusion of modules. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> libnet, by Graham Barr, is a collection of perl5 modules related to network programming. See Net::FTP, Net::NNTP, Net::Ping (not part of libnet, but related), Net::POP3, Net::SMTP, and Net::Time. </p>
<p> Perl installation leaves libnet unconfigured; use <i>libnetcfg</i> to configure it. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;List::Util&quot;</code>, by Graham Barr, is a selection of general-utility list subroutines, such as <code>sum()</code>, <code>min()</code>, <code>first()</code>, and <code>shuffle()</code>. See List::Util. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Locale::Constants&quot;</code>, <code>&quot;Locale::Country&quot;</code>, <code>&quot;Locale::Currency&quot;</code> <code>&quot;Locale::Language&quot;</code>, and Locale::Script, by Neil Bowers, have been added. They provide the codes for various locale standards, such as ``fr&#8217;&#8216; for France, ``usd&#8217;&#8216; for <font SIZE="-1">US</font> Dollar, and ``ja&#8217;&#8216; for Japanese. </p>
<pre><code>    use Locale::Country;
    $country = code2country('jp'); # $country gets 'Japan'
    $code = country2code('Norway'); # $code gets 'no'
</code></pre>
<p> See Locale::Constants, Locale::Country, Locale::Currency, and Locale::Language. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Locale::Maketext&quot;</code>, by Sean Burke, is a localization framework. See Locale::Maketext, and Locale::Maketext::TPJ13. The latter is an article about software localization, originally published in The Perl Journal #13, and republished here with kind permission. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Math::BigRat&quot;</code> for big rational numbers, to accompany Math::BigInt and Math::BigFloat, from Tels. See Math::BigRat. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Memoize&quot;</code> can make your functions faster by trading space for time, from Mark-Jason Dominus. See Memoize. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;MIME::Base64&quot;</code>, by Gisle Aas, allows you to encode data in base64, as defined in <font SIZE="-1">RFC 2045</font> - <i></i><font SIZE="-1"><i>MIME</i></font><i> (Multipurpose Internet Mail Extensions)</i>. </p>
<pre><code>    use MIME::Base64;
    $encoded = encode_base64('Aladdin:open sesame');
    $decoded = decode_base64($encoded);
    print $encoded, &quot;\n&quot;; # &quot;QWxhZGRpbjpvcGVuIHNlc2FtZQ==&quot;
</code></pre>
<p> See MIME::Base64. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;MIME::QuotedPrint&quot;</code>, by Gisle Aas, allows you to encode data in quoted-printable encoding, as defined in <font SIZE="-1">RFC 2045</font> - <i></i><font SIZE="-1"><i>MIME</i></font><i> (Multipurpose Internet Mail Extensions)</i>. </p>
<pre><code>    use MIME::QuotedPrint;
    $encoded = encode_qp(&quot;\xDE\xAD\xBE\xEF&quot;);
    $decoded = decode_qp($encoded);
    print $encoded, &quot;\n&quot;; # &quot;=DE=AD=BE=EF\n&quot;
    print $decoded, &quot;\n&quot;; # &quot;\xDE\xAD\xBE\xEF\n&quot;
</code></pre>
<p> See also PerlIO::via::QuotedPrint. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;NEXT&quot;</code>, by Damian Conway, is a pseudo-class for method redispatch. See <font SIZE="-1">NEXT</font>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;open&quot;</code> is a new pragma for setting the default I/O layers for <code>open()</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;PerlIO::scalar&quot;</code>, by Nick Ing-Simmons, provides the implementation of <font SIZE="-1">IO</font> to ``in memory&#8217;&#8216; Perl scalars as discussed above. It also serves as an example of a loadable PerlIO layer. Other future possibilities include PerlIO::Array and PerlIO::Code. See PerlIO::scalar. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;PerlIO::via&quot;</code>, by Nick Ing-Simmons, acts as a PerlIO layer and wraps PerlIO layer functionality provided by a class (typically implemented in Perl code). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;PerlIO::via::QuotedPrint&quot;</code>, by Elizabeth Mattijsen, is an example of a <code>&quot;PerlIO::via&quot;</code> class: </p>
<pre><code>    use PerlIO::via::QuotedPrint;
    open($fh,&quot;&gt;:via(QuotedPrint)&quot;,$path);
</code></pre>
<p> This will automatically convert everything output to <code>$fh</code> to Quoted-Printable. See PerlIO::via and PerlIO::via::QuotedPrint. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Pod::ParseLink&quot;</code>, by Russ Allbery, has been added, to parse L&lt;&gt; links in pods as described in the new perlpodspec. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Pod::Text::Overstrike&quot;</code>, by Joe Smith, has been added. It converts <font SIZE="-1">POD</font> data to formatted overstrike text. See Pod::Text::Overstrike. [561+] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Scalar::Util&quot;</code> is a selection of general-utility scalar subroutines, such as <code>blessed()</code>, <code>reftype()</code>, and <code>tainted()</code>. See Scalar::Util. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;sort&quot;</code> is a new pragma for controlling the behaviour of <code>sort()</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Storable&quot;</code> gives persistence to Perl data structures by allowing the storage and retrieval of Perl data to and from files in a fast and compact binary format. Because in effect Storable does serialisation of Perl data structures, with it you can also clone deep, hierarchical datastructures. Storable was originally created by Raphael Manfredi, but it is now maintained by Abhijit Menon-Sen. Storable has been enhanced to understand the two new hash features, Unicode keys and restricted hashes. See Storable. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Switch&quot;</code>, by Damian Conway, has been added. Just by saying </p>
<pre><code>    use Switch;
</code></pre>
<p> you have <code>&quot;switch&quot;</code> and <code>&quot;case&quot;</code> available in Perl. </p>
<pre><code>    use Switch;
    switch ($val) {
                case 1 { print &quot;number 1&quot; }
                case &quot;a&quot; { print &quot;string a&quot; }
                case [1..10,42] { print &quot;number in list&quot; }
                case (@array) { print &quot;number in list&quot; }
                case /\w+/ { print &quot;pattern&quot; }
                case qr/\w+/ { print &quot;pattern&quot; }
                case (%hash) { print &quot;entry in hash&quot; }
                case (\%hash) { print &quot;entry in hash&quot; }
                case (\&amp;sub) { print &quot;arg to subroutine&quot; }
                else { print &quot;previous case not true&quot; }
    }
</code></pre>
<p> See Switch. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Test::More&quot;</code>, by Michael Schwern, is yet another framework for writing test scripts, more extensive than Test::Simple. See Test::More. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Test::Simple&quot;</code>, by Michael Schwern, has basic utilities for writing tests. See Test::Simple. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Text::Balanced&quot;</code>, by Damian Conway, has been added, for extracting delimited text sequences from strings. </p>
<pre><code>    use Text::Balanced 'extract_delimited';
    ($a, $b) = extract_delimited(&quot;'never say never', he never said&quot;, &quot;'&quot;, '');
</code></pre>
<p> <code>$a</code> will be ``&#8216;never say never&#8217;&#8216;&#8216;, <code>$b</code> will be &#8216;, he never said&#8217;. </p>
<p> In addition to <code>extract_delimited()</code>, there are also <code>extract_bracketed()</code>, <code>extract_quotelike()</code>, <code>extract_codeblock()</code>, <code>extract_variable()</code>, <code>extract_tagged()</code>, <code>extract_multiple()</code>, <code>gen_delimited_pat()</code>, and <code>gen_extract_tagged()</code>. With these, you can implement rather advanced parsing algorithms. See Text::Balanced. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;threads&quot;</code>, by Arthur Bergman, is an interface to interpreter threads. Interpreter threads (ithreads) is the new thread model introduced in Perl 5.6 but only available as an internal interface for extension writers (and for Win32 Perl for <code>&quot;fork()&quot;</code> emulation). See threads, threads::shared, and perlthrtut. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;threads::shared&quot;</code>, by Arthur Bergman, allows data sharing for interpreter threads. See threads::shared. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Tie::File&quot;</code>, by Mark-Jason Dominus, associates a Perl array with the lines of a file. See Tie::File. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Tie::Memoize&quot;</code>, by Ilya Zakharevich, provides on-demand loaded hashes. See Tie::Memoize. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Tie::RefHash::Nestable&quot;</code>, by Edward Avis, allows storing hash references (unlike the standard Tie::RefHash) The module is contained within Tie::RefHash. See Tie::RefHash. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Time::HiRes&quot;</code>, by Douglas E. Wegscheid, provides high resolution timing (ualarm, usleep, and gettimeofday). See Time::HiRes. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Unicode::UCD&quot;</code> offers a querying interface to the Unicode Character Database. See Unicode::UCD. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Unicode::Collate&quot;</code>, by <font SIZE="-1">SADAHIRO</font> Tomoyuki, implements the <font SIZE="-1">UCA</font> (Unicode Collation Algorithm) for sorting Unicode strings. See Unicode::Collate. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Unicode::Normalize&quot;</code>, by <font SIZE="-1">SADAHIRO</font> Tomoyuki, implements the various Unicode normalization forms. See Unicode::Normalize. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;XS::APItest&quot;</code>, by Tim Jenness, is a test extension that exercises <font SIZE="-1">XS</font> APIs. Currently only <code>&quot;printf()&quot;</code> is tested: how to output various basic data types from <font SIZE="-1">XS.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;XS::Typemap&quot;</code>, by Tim Jenness, is a test extension that exercises <font SIZE="-1">XS</font> typemaps. Nothing gets installed, but the code is worth studying for extension writers. </p>
 </dd></dl>
<h3>Updated And Improved Modules and Pragmata</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> The following independently supported modules have been updated to the newest versions from <font SIZE="-1">CPAN: CGI, CPAN,</font> DB_File, File::Spec, File::Temp, Getopt::Long, Math::BigFloat, Math::BigInt, the podlators bundle (Pod::Man, Pod::Text), Pod::LaTeX [561+], Pod::Parser, Storable, Term::ANSIColor, Test, Text-Tabs+Wrap. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>attributes::reftype()</code> now works on tied arguments. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> AutoLoader can now be disabled with <code>&quot;no AutoLoader;&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> B::Deparse has been significantly enhanced by Robin Houston. It can now deparse almost all of the standard test suite (so that the tests still succeed). There is a make target ``test.deparse&#8217;&#8216; for trying this out. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Carp now has better interface documentation, and the <code>@CARP_NOT</code> interface has been added to get optional control over where errors are reported independently of <code>@ISA</code>, by Ben Tilly. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Class::Struct can now define the classes in compile time. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Class::Struct now assigns the array/hash element if the accessor is called with an array/hash element as the <code>sole</code> argument. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The return value of <code>Cwd::fastcwd()</code> is now tainted. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Data::Dumper now has an option to sort hashes. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Data::Dumper now has an option to dump code references using B::Deparse. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> DB_File now supports newer Berkeley <font SIZE="-1">DB</font> versions, among other improvements. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Devel::Peek now has an interface for the Perl memory statistics (this works only if you are using perl&#8217;s malloc, and if you have compiled with debugging). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The English module can now be used without the infamous performance hit by saying </p>
<pre><code>        use English '-no_match_vars';
</code></pre>
<p> (Assuming, of course, that you don&#8217;t need the troublesome variables <code>&quot;$`&quot;</code>, <code>$&amp;</code>, or <code>&quot;$&#8216;&quot;</code>.) Also, introduced <code>@LAST_MATCH_START</code> and <code>@LAST_MATCH_END</code> English aliases for <code>&quot;@-&quot;</code> and <code>&quot;@+&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::MakeMaker has been significantly cleaned up and fixed. The enhanced version has also been backported to earlier releases of Perl and submitted to <font SIZE="-1">CPAN</font> so that the earlier releases can enjoy the fixes. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The arguments of <code>WriteMakefile()</code> in Makefile.PL are now checked for sanity much more carefully than before. This may cause new warnings when modules are being installed. See ExtUtils::MakeMaker for more details. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::MakeMaker now uses File::Spec internally, which hopefully leads to better portability. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fcntl, Socket, and Sys::Syslog have been rewritten by Nicholas Clark to use the new-style constant dispatch section (see ExtUtils::Constant). This means that they will be more robust and hopefully faster. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Find now <code>chdir()</code>s correctly when chasing symbolic links. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Find now has pre- and post-processing callbacks. It also correctly changes directories when chasing symbolic links. Callbacks (naughtily) exiting with ``next;&#8216;&#8216; instead of ``return;&#8216;&#8216; now work. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Find is now (again) reentrant. It also has been made more portable. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The warnings issued by File::Find now belong to their own category. You can enable/disable them with <code>&quot;use/no warnings &#8216;File::Find&#8217;;&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>File::Glob::glob()</code> has been renamed to <code>File::Glob::bsd_glob()</code> because the name clashes with the builtin <code>glob()</code>. The older name is still available for compatibility, but is deprecated. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Glob now supports <code>&quot;GLOB_LIMIT&quot;</code> constant to limit the size of the returned list of filenames. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> IPC::Open3 now allows the use of numeric file descriptors. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> IO::Socket now has an <code>atmark()</code> method, which returns true if the socket is positioned at the out-of-band mark. The method is also exportable as a <code>sockatmark()</code> function. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> IO::Socket::INET failed to open the specified port if the service name was not known. It now correctly uses the supplied port number as is. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> IO::Socket::INET has support for the ReusePort option (if your platform supports it). The Reuse option now has an alias, ReuseAddr. For clarity, you may want to prefer ReuseAddr. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> IO::Socket::INET now supports a value of zero for <code>&quot;LocalPort&quot;</code> (usually meaning that the operating system will make one up.) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> &#8216;use lib&#8217; now works identically to <code>@INC</code>. Removing directories with &#8216;no lib&#8217; now works. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Math::BigFloat and Math::BigInt have undergone a full rewrite by Tels. They are now magnitudes faster, and they support various bignum libraries such as <font SIZE="-1">GMP</font> and <font SIZE="-1">PARI</font> as their backends. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Math::Complex handles inf, NaN etc., better. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Net::Ping has been considerably enhanced by Rob Brown: multihoming is now supported, Win32 functionality is better, there is now time measuring functionality (optionally high-resolution using Time::HiRes), and there is now ``external&#8217;&#8216; protocol which uses Net::Ping::External module which runs your external ping utility and parses the output. A version of Net::Ping::External is available in <font SIZE="-1">CPAN.</font> </p>
<p> Note that some of the Net::Ping tests are disabled when running under the Perl distribution since one cannot assume one or more of the following: enabled echo port at localhost, full Internet connectivity, or sympathetic firewalls. You can set the environment variable PERL_TEST_Net_Ping to ``1&#8217;&#8216; (one) before running the Perl test suite to enable all the Net::Ping tests. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>POSIX::sigaction()</code> is now much more flexible and robust. You can now install coderef handlers, &#8216;<font SIZE="-1">DEFAULT</font>&#8216;, and &#8216;<font SIZE="-1">IGNORE</font>&#8216; handlers, installing new handlers was not atomic. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In Safe, <code>%INC</code> is now localised in a Safe compartment so that use/require work. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In SDBM_File on DOSish platforms, some keys went missing because of lack of support for files with ``holes&#8217;&#8216;. A workaround for the problem has been added. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In Search::Dict one can now have a pre-processing hook for the lines being searched. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The Shell module now has an <font SIZE="-1">OO</font> interface. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In Sys::Syslog there is now a failover mechanism that will go through alternative connection mechanisms until the message is successfully logged. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The Test module has been significantly enhanced. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>Time::Local::timelocal()</code> does not handle fractional seconds anymore. The rationale is that neither does <code>localtime()</code>, and <code>timelocal()</code> and <code>localtime()</code> are supposed to be inverses of each other. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The vars pragma now supports declaring fully qualified variables. (Something that <code>&quot;our()&quot;</code> does not and will not support.) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;utf8::&quot;</code> name space (as in the pragma) provides various Perl-callable functions to provide low level access to Perl&#8217;s internal Unicode representation. At the moment only <code>length()</code> has been implemented. </p>
 </dd></dl>
<h2>Utility Changes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> Emacs perl mode (emacs/cperl-mode.el) has been updated to version 4.31. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>emacs/e2ctags.pl</i> is now much faster. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;enc2xs&quot;</code> is a tool for people adding their own encodings to the Encode module. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;h2ph&quot;</code> now supports C trigraphs. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;h2xs&quot;</code> now produces a template <font SIZE="-1">README.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;h2xs&quot;</code> now uses <code>&quot;Devel::PPPort&quot;</code> for better portability between different versions of Perl. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;h2xs&quot;</code> uses the new ExtUtils::Constant module which will affect newly created extensions that define constants. Since the new code is more correct (if you have two constants where the first one is a prefix of the second one, the first constant <code>never</code> got defined), less lossy (it uses integers for integer constant, as opposed to the old code that used floating point numbers even for integer constants), and slightly faster, you might want to consider regenerating your extension code (the new scheme makes regenerating easy). h2xs now also supports C trigraphs. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;libnetcfg&quot;</code> has been added to configure libnet. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;perlbug&quot;</code> is now much more robust. It also sends the bug report to perl.org, not perl.com. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;perlcc&quot;</code> has been rewritten and its user interface (that is, command line) is much more like that of the Unix C compiler, cc. (The perlbc tools has been removed. Use <code>&quot;perlcc -B&quot;</code> instead.) <code>Note that perlcc is still considered very experimental and unsupported.</code> [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;perlivp&quot;</code> is a new Installation Verification Procedure utility for running any time after installing Perl. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;piconv&quot;</code> is an implementation of the character conversion utility <code>&quot;iconv&quot;</code>, demonstrating the new Encode module. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;pod2html&quot;</code> now allows specifying a cache directory. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;pod2html&quot;</code> now produces <font SIZE="-1">XHTML 1.0.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;pod2html&quot;</code> now understands <font SIZE="-1">POD</font> written using different line endings (PC-like <font SIZE="-1">CRLF</font> versus Unix-like <font SIZE="-1">LF</font> versus MacClassic-like <font SIZE="-1">CR</font>). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;s2p&quot;</code> has been completely rewritten in Perl. (It is in fact a full implementation of sed in Perl: you can use the sed functionality by using the <code>&quot;psed&quot;</code> utility.) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;xsubpp&quot;</code> now understands <font SIZE="-1">POD</font> documentation embedded in the *.xs files. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;xsubpp&quot;</code> now supports the <font SIZE="-1">OUT</font> keyword. </p>
 </dd></dl>
<h2>New Documentation</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> perl56delta details the changes between the 5.005 release and the 5.6.0 release. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlclib documents the internal replacements for standard C library functions. (Interesting only for extension writers and Perl core hackers.) [561+] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perldebtut is a Perl debugging tutorial. [561+] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlebcdic contains considerations for running Perl on <font SIZE="-1">EBCDIC</font> platforms. [561+] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlintro is a gentle introduction to Perl. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perliol documents the internals of PerlIO with layers. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlmodstyle is a style guide for writing modules. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlnewmod tells about writing and submitting a new module. [561+] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlpacktut is a <code>pack()</code> tutorial. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlpod has been rewritten to be clearer and to record the best practices gathered over the years. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlpodspec is a more formal specification of the pod format, mainly of interest for writers of pod applications, not to people writing in pod. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlretut is a regular expression tutorial. [561+] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlrequick is a regular expressions quick-start guide. Yes, much quicker than perlretut. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perltodo has been updated. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perltootc has been renamed as perltooc (to not to conflict with perltoot in filesystems restricted to ``8.3&#8217;&#8216; names). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perluniintro is an introduction to using Unicode in Perl. (perlunicode is more of a detailed reference and background information) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlutil explains the command line utilities packaged with the Perl distribution. [561+] </p>
 </dd></dl>
<p> The following platform-specific documents are available before the installation as <font SIZE="-1">README.</font><i>platform</i>, and after the installation as perl <i>platform</i>: </p>
<pre><code>    perlaix perlamiga perlapollo perlbeos perlbs2000
    perlce perlcygwin perldgux perldos perlepoc perlfreebsd perlhpux
    perlhurd perlirix perlmachten perlmacos perlmint perlmpeix
    perlnetware perlos2 perlos390 perlplan9 perlqnx perlsolaris
    perltru64 perluts perlvmesa perlvms perlvos perlwin32
</code></pre>
<p> These documents usually detail one or more of the following subjects: configuring, building, testing, installing, and sometimes also using Perl on the said platform. </p>
<p> Eastern Asian Perl users are now welcomed in their own languages: <font SIZE="-1">README</font>.jp (Japanese), <font SIZE="-1">README</font>.ko (Korean), <font SIZE="-1">README</font>.cn (simplified Chinese) and <font SIZE="-1">README</font>.tw (traditional Chinese), which are written in normal pod but encoded in EUC-JP, EUC-KR, EUC-CN and Big5. These will get installed as </p>
<pre><code>   perljp perlko perlcn perltw
</code></pre>
<dl>
<dt>&bull;</dt>
<dd> <p> The documentation for the POSIX-BC platform is called ``<font SIZE="-1">BS2000&#8217;&#8216;,</font> to avoid confusion with the Perl <font SIZE="-1">POSIX</font> module. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The documentation for the WinCE platform is called perlce (<font SIZE="-1">README</font>.ce in the source code kit), to avoid confusion with the perlwin32 documentation on 8.3-restricted filesystems. </p>
 </dd></dl>
<h2>Performance Enhancements</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>map()</code> could get pathologically slow when the result list it generates is larger than the source list. The performance has been improved for common scenarios. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>sort()</code> is also fully reentrant, in the sense that the sort function can itself call <code>sort()</code>. This did not work reliably in previous releases. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>sort()</code> has been changed to use primarily mergesort internally as opposed to the earlier quicksort. For very small lists this may result in slightly slower sorting times, but in general the speedup should be at least 20%. Additional bonuses are that the worst case behaviour of <code>sort()</code> is now better (in computer science terms it now runs in time O(N log N), as opposed to quicksort&#8217;s Theta(N**2) worst-case run time behaviour), and that <code>sort()</code> is now stable (meaning that elements with identical keys will stay ordered as they were before the sort). See the <code>&quot;sort&quot;</code> pragma for information. </p>
<p> The story in more detail: suppose you want to serve yourself a little slice of Pi. </p>
<pre><code>    @digits = ( 3,1,4,1,5,9 );
</code></pre>
<p> A numerical sort of the digits will yield (1,1,3,4,5,9), as expected. Which <code>1</code> comes first is hard to know, since one <code>1</code> looks pretty much like any other. You can regard this as totally trivial, or somewhat profound. However, if you just want to sort the even digits ahead of the odd ones, then what will </p>
<pre><code>    sort { ($a % 2) &lt;=&gt; ($b % 2) } @digits;
</code></pre>
<p> yield? The only even digit, <code>4</code>, will come first. But how about the odd numbers, which all compare equal? With the quicksort algorithm used to implement Perl 5.6 and earlier, the order of ties is left up to the sort. So, as you add more and more digits of Pi, the order in which the sorted even and odd digits appear will change. and, for sufficiently large slices of Pi, the quicksort algorithm in Perl 5.8 won&#8217;t return the same results even if reinvoked with the same input. The justification for this rests with quicksort&#8217;s worst case behavior. If you run </p>
<pre><code>   sort { $a &lt;=&gt; $b } ( 1 .. $N , 1 .. $N );
</code></pre>
<p> (something you might approximate if you wanted to merge two sorted arrays using sort), doubling <code>$N</code> doesn&#8217;t just double the quicksort time, it <i>quadruples</i> it. Quicksort has a worst case run time that can grow like N**2, so-called <i>quadratic</i> behaviour, and it can happen on patterns that may well arise in normal use. You won&#8217;t notice this for small arrays, but you <i>will</i> notice it with larger arrays, and you may not live long enough for the sort to complete on arrays of a million elements. So the 5.8 quicksort scrambles large arrays before sorting them, as a statistical defence against quadratic behaviour. But that means if you sort the same large array twice, ties may be broken in different ways. </p>
<p> Because of the unpredictability of tie-breaking order, and the quadratic worst-case behaviour, quicksort was <i>almost</i> replaced completely with a stable mergesort. <i>Stable</i> means that ties are broken to preserve the original order of appearance in the input array. So </p>
<pre><code>    sort { ($a % 2) &lt;=&gt; ($b % 2) } (3,1,4,1,5,9);
</code></pre>
<p> will yield (4,3,1,1,5,9), guaranteed. The even and odd numbers appear in the output in the same order they appeared in the input. Mergesort has worst case O(N log N) behaviour, the best value attainable. And, ironically, this mergesort does particularly well where quicksort goes quadratic: mergesort sorts (1..$N, 1..$N) in O(N) time. But quicksort was rescued at the last moment because it is faster than mergesort on certain inputs and platforms. For example, if you really <i>don&#8217;t</i> care about the order of even and odd digits, quicksort will run in O(N) time; it&#8217;s very good at sorting many repetitions of a small number of distinct elements. The quicksort divide and conquer strategy works well on platforms with relatively small, very fast, caches. Eventually, the problem gets whittled down to one that fits in the cache, from which point it benefits from the increased memory speed. </p>
<p> Quicksort was rescued by implementing a sort pragma to control aspects of the sort. The <code>stable</code> subpragma forces stable behaviour, regardless of algorithm. The <code>_quicksort</code> and <code>_mergesort</code> subpragmas are heavy-handed ways to select the underlying implementation. The leading <code>&quot;_&quot;</code> is a reminder that these subpragmas may not survive beyond 5.8. More appropriate mechanisms for selecting the implementation exist, but they wouldn&#8217;t have arrived in time to save quicksort. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Hashes now use Bob Jenkins ``One-at-a-Time&#8217;&#8216; hashing key algorithm ( <a rel="nofollow" href="http://burtleburtle.net/bob/hash/doobs.html">http://burtleburtle.net/bob/hash/doobs.html</a> ). This algorithm is reasonably fast while producing a much better spread of values than the old hashing algorithm (originally by Chris Torek, later tweaked by Ilya Zakharevich). Hash values output from the algorithm on a hash of all 3-char printable <font SIZE="-1">ASCII</font> keys comes much closer to passing the <font SIZE="-1">DIEHARD</font> random number generation tests. According to perlbench, this change has not affected the overall speed of Perl. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>unshift()</code> should now be noticeably faster. </p>
 </dd></dl>
<h2>Installation and Configuration Improvements</h2>
<h3>Generic Improvements</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">INSTALL</font> now explains how you can configure Perl to use 64-bit integers even on non-64-bit platforms. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Policy.sh policy change: if you are reusing a Policy.sh file (see <font SIZE="-1">INSTALL</font>) and you use Configure -Dprefix=/foo/bar and in the old Policy <code>$prefix</code> eq <code>$siteprefix</code> and <code>$prefix</code> eq <code>$vendorprefix</code>, all of them will now be changed to the new prefix, /foo/bar. (Previously only <code>$prefix</code> changed.) If you do not like this new behaviour, specify prefix, siteprefix, and vendorprefix explicitly. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new optional location for Perl libraries, otherlibdirs, is available. It can be used for example for vendor add-ons without disturbing Perl&#8217;s own library directories. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In many platforms, the vendor-supplied &#8216;cc&#8217; is too stripped-down to build Perl (basically, &#8216;cc&#8217; doesn&#8217;t do <font SIZE="-1">ANSI C</font>). If this seems to be the case and &#8216;cc&#8217; does not seem to be the <font SIZE="-1">GNU C</font> compiler &#8216;gcc&#8217;, an automatic attempt is made to find and use &#8216;gcc&#8217; instead. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> gcc needs to closely track the operating system release to avoid build problems. If Configure finds that gcc was built for a different operating system release than is running, it now gives a clearly visible warning that there may be trouble ahead. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Since Perl 5.8 is not binary-compatible with previous releases of Perl, Configure no longer suggests including the 5.005 modules in <code>@INC</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Configure <code>&quot;-S&quot;</code> can now run non-interactively. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Configure support for pdp11-style memory models has been removed due to obsolescence. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> configure.gnu now works with options with whitespace in them. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> installperl now outputs everything to <font SIZE="-1">STDERR.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Because PerlIO is now the default on most platforms, ``-perlio&#8217;&#8216; doesn&#8217;t get appended to the <code>$Config</code>{archname} (also known as $^O) anymore. Instead, if you explicitly choose not to use perlio (Configure command line option -Uuseperlio), you will get ``-stdio&#8217;&#8216; appended. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Another change related to the architecture name is that ``-64all&#8217;&#8216; (-Duse64bitall, or ``maximally 64-bit&#8217;&#8216;) is appended only if your pointers are 64 bits wide. (To be exact, the use64bitall is ignored.) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In <font SIZE="-1">AFS</font> installations, one can configure the root of the <font SIZE="-1">AFS</font> to be somewhere else than the default <i>/afs</i> by using the Configure parameter <code>&quot;-Dafsroot=/some/where/else&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">APPLLIB_EXP,</font> a lesser-known configuration-time definition, has been documented. It can be used to prepend site-specific directories to Perl&#8217;s default search path (@INC); see <font SIZE="-1">INSTALL</font> for information. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The version of Berkeley <font SIZE="-1">DB</font> used when the Perl (and, presumably, the DB_File extension) was built is now available as <code>@Config{qw(db_version_major db_version_minor db_version_patch)}</code> from Perl and as <code>&quot;DB_VERSION_MAJOR_CFG DB_VERSION_MINOR_CFG DB_VERSION_PATCH_CFG&quot;</code> from C. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Building Berkeley <font SIZE="-1">DB3</font> for compatibility modes for <font SIZE="-1">DB, NDBM,</font> and <font SIZE="-1">ODBM</font> has been documented in <font SIZE="-1">INSTALL.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> If you have <font SIZE="-1">CPAN</font> access (either network or a local copy such as a CD-ROM) you can during specify extra modules to Configure to build and install with Perl using the -Dextras=... option. See <font SIZE="-1">INSTALL</font> for more details. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In addition to config.over, a new override file, config.arch, is available. This file is supposed to be used by hints file writers for architecture-wide changes (as opposed to config.over which is for site-wide changes). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> If your file system supports symbolic links, you can build Perl outside of the source directory by </p>
<pre><code>        mkdir perl/build/directory
        cd perl/build/directory
        sh /path/to/perl/source/Configure -Dmksymlinks ...
</code></pre>
<p> This will create in perl/build/directory a tree of symbolic links pointing to files in /path/to/perl/source. The original files are left unaffected. After Configure has finished, you can just say </p>
<pre><code>        make all test
</code></pre>
<p> and Perl will be built and tested, all in perl/build/directory. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> For Perl developers, several new make targets for profiling and debugging have been added; see perlhack. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Use of the <i>gprof</i> tool to profile Perl has been documented in perlhack. There is a make target called ``perl.gprof&#8217;&#8216; for generating a gprofiled Perl executable. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> If you have <font SIZE="-1">GCC 3,</font> there is a make target called ``perl.gcov&#8217;&#8216; for creating a gcoved Perl executable for coverage analysis. See perlhack. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> If you are on <font SIZE="-1">IRIX</font> or Tru64 platforms, new profiling/debugging options have been added; see perlhack for more information about pixie and Third Degree. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>&bull;</dt>
<dd> <p> Guidelines of how to construct minimal Perl installations have been added to <font SIZE="-1">INSTALL.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The Thread extension is now not built at all under ithreads (<code>&quot;Configure -Duseithreads&quot;</code>) because it wouldn&#8217;t work anyway (the Thread extension requires being Configured with <code>&quot;-Duse5005threads&quot;</code>). </p>
<p> <code>Note that the 5.005 threads are unsupported and deprecated: if you have code written for the old threads you should migrate it to the new ithreads model.</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The Gconvert macro ($Config{d_Gconvert}) used by perl for stringifying floating-point numbers is now more picky about using sprintf %.*g rules for the conversion. Some platforms that used to use gcvt may now resort to the slower sprintf. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The obsolete method of making a special (e.g., debugging) flavor of perl by saying </p>
<pre><code>        make LIBPERL=libperld.a
</code></pre>
<p> has been removed. Use -DDEBUGGING instead. </p>
 </dd></dl>
<h3>New Or Improved Platforms</h3>
<p> For the list of platforms known to support Perl, see ``Supported Platforms&#8217;&#8216; in perlport. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">AIX</font> dynamic loading should be now better supported. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">AIX</font> should now work better with gcc, threads, and 64-bitness. Also the long doubles support in <font SIZE="-1">AIX</font> should be better now. See perlaix. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> AtheOS ( <a rel="nofollow" href="http://www.atheos.cx/">http://www.atheos.cx/</a> ) is a new platform. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> BeOS has been reclaimed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <font SIZE="-1">DG/UX</font> platform now supports 5.005-style threads. See perldgux. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The DYNIX/ptx platform (also known as dynixptx) is supported at or near osvers 4.5.2. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">EBCDIC</font> platforms (z/OS (also known as <font SIZE="-1">OS/390</font>), POSIX-BC, and <font SIZE="-1">VM/ESA</font>) have been regained. Many test suite tests still fail and the co-existence of Unicode and <font SIZE="-1">EBCDIC</font> isn&#8217;t quite settled, but the situation is much better than with Perl 5.6. See perlos390, perlbs2000 (for POSIX-BC), and perlvmesa for more information. (<code>Note:</code> support for <font SIZE="-1">VM/ESA</font> was removed in Perl v5.18.0. The relevant information was in <i></i><font SIZE="-1"><i>README</i></font><i>.vmesa</i>) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Building perl with -Duseithreads or -Duse5005threads now works under HP-UX 10.20 (previously it only worked under 10.30 or later). You will need a thread library package installed. See <font SIZE="-1">README</font>.hpux. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Mac <font SIZE="-1">OS</font> Classic is now supported in the mainstream source package (MacPerl has of course been available since perl 5.004 but now the source code bases of standard Perl and MacPerl have been synchronised) [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Mac <font SIZE="-1">OS X</font> (or Darwin) should now be able to build Perl even on <font SIZE="-1">HFS+</font> filesystems. (The case-insensitivity used to confuse the Perl build process.) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">NCR</font> MP-RAS is now supported. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> All the NetBSD specific patches (except for the installation specific ones) have been merged back to the main distribution. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> NetWare from Novell is now supported. See perlnetware. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> NonStop-UX is now supported. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">NEC</font> SUPER-UX is now supported. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> All the OpenBSD specific patches (except for the installation specific ones) have been merged back to the main distribution. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl has been tested with the <font SIZE="-1">GNU</font> pth userlevel thread package ( <a rel="nofollow" href="http://www.gnu.org/software/pth/pth.html">http://www.gnu.org/software/pth/pth.html</a> ). All thread tests of Perl now work, but not without adding some <code>yield()</code>s to the tests, so while pth (and other userlevel thread implementations) can be considered to be ``working&#8217;&#8216; with Perl ithreads, keep in mind the possible non-preemptability of the underlying thread implementation. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Stratus <font SIZE="-1">VOS</font> is now supported using Perl&#8217;s native build method (Configure). This is the recommended method to build Perl on <font SIZE="-1">VOS.</font> The older methods, which build miniperl, are still available. See perlvos. [561+] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The Amdahl <font SIZE="-1">UTS</font> Unix mainframe platform is now supported. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> WinCE is now supported. See perlce. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> z/OS (formerly known as <font SIZE="-1">OS/390,</font> formerly known as <font SIZE="-1">MVS OE</font>) now has support for dynamic loading. This is not selected by default, however, you must specify -Dusedl in the arguments of Configure. [561] </p>
 </dd></dl>
<h2>Selected Bug Fixes</h2>
<p> Numerous memory leaks and uninitialized memory accesses have been hunted down. Most importantly, anonymous subs used to leak quite a bit. [561] </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The autouse pragma didn&#8217;t work for Multi::Part::Function::Names. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>caller()</code> could cause core dumps in certain situations. Carp was sometimes affected by this problem. In particular, <code>caller()</code> now returns a subroutine name of <code>&quot;(unknown)&quot;</code> for subroutines that have been removed from the symbol table. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> chop(@list) in list context returned the characters chopped in reverse order. This has been reversed to be in the right order. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Configure no longer includes the <font SIZE="-1">DBM</font> libraries (dbm, gdbm, db, ndbm) when building the Perl binary. The only exception to this is SunOS 4.x, which needs them. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The behaviour of non-decimal but numeric string constants such as ``0x23&#8217;&#8216; was platform-dependent: in some platforms that was seen as 35, in some as 0, in some as a floating point number (don&#8217;t ask). This was caused by Perl&#8217;s using the operating system libraries in a situation where the result of the string to number conversion is undefined: now Perl consistently handles such strings as zero in numeric contexts. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Several debugger fixes: exit code now reflects the script exit code, condition <code>&quot;0&quot;</code> now treated correctly, the <code>&quot;d&quot;</code> command now checks line number, <code>$.</code> no longer gets corrupted, and all debugger output now goes correctly to the socket if RemotePort is set. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The debugger (perl5db.pl) has been modified to present a more consistent commands interface, via (CommandSet=580). perl5db.t was also added to test the changes, and as a placeholder for further tests. </p>
<p> See perldebug. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The debugger has a new <code>&quot;dumpDepth&quot;</code> option to control the maximum depth to which nested structures are dumped. The <code>&quot;x&quot;</code> command has been extended so that <code>&quot;x N EXPR&quot;</code> dumps out the value of <i></i><font SIZE="-1"><i>EXPR</i></font><i></i> to a depth of at most <i>N</i> levels. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The debugger can now show lexical variables if you have the <font SIZE="-1">CPAN</font> module PadWalker installed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The order of DESTROYs has been made more predictable. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl 5.6.0 could emit spurious warnings about redefinition of <code>dl_error()</code> when statically building extensions into perl. This has been corrected. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> dprofpp -R didn&#8217;t work. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>*foo{FORMAT}</code> now works. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Infinity is now recognized as a number. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> UNIVERSAL::isa no longer caches methods incorrectly. (This broke the Tk extension with 5.6.0.) [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Lexicals I: lexicals outside an eval &quot;`` weren&#8217;t resolved correctly inside a subroutine definition inside the eval &#8216;&#8216;`` if they were not already referenced in the top level of the eval&#8217;&#8216;&quot;ed code. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Lexicals <font SIZE="-1">II:</font> lexicals leaked at file scope into subroutines that were declared before the lexicals. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Lexical warnings now propagating correctly between scopes and into <code>&quot;eval &quot;...&quot;&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;use warnings qw(FATAL all)&quot;</code> did not work as intended. This has been corrected. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>warnings::enabled()</code> now reports the state of $^W correctly if the caller isn&#8217;t using lexical warnings. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Line renumbering with eval and <code>&quot;#line&quot;</code> now works. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed numerous memory leaks, especially in eval &quot;&quot;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Localised tied variables no longer leak memory </p>
<pre><code>    use Tie::Hash;
    tie my %tied_hash =&gt; 'Tie::StdHash';
    ...
    # Used to leak memory every time local() was called;
    # in a loop, this added up.
    local($tied_hash{Foo}) = 1;
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Localised hash elements (and <code>%ENV</code>) are correctly unlocalised to not exist, if they didn&#8217;t before they were localised. </p>
<pre><code>    use Tie::Hash;
    tie my %tied_hash =&gt; 'Tie::StdHash';
    ...
    # Nothing has set the FOO element so far
    { local $tied_hash{FOO} = 'Bar' }
    # This used to print, but not now.
    print &quot;exists!\n&quot; if exists $tied_hash{FOO};
</code></pre>
<p> As a side effect of this fix, tied hash interfaces <code>must</code> define the <font SIZE="-1">EXISTS</font> and <font SIZE="-1">DELETE</font> methods. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>mkdir()</code> now ignores trailing slashes in the directory name, as mandated by <font SIZE="-1">POSIX.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Some versions of glibc have a broken <code>modfl()</code>. This affects builds with <code>&quot;-Duselongdouble&quot;</code>. This version of Perl detects this brokenness and has a workaround for it. The glibc release 2.2.2 is known to have fixed the <code>modfl()</code> bug. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Modulus of unsigned numbers now works (4063328477 % 65535 used to return 27406, instead of 27047). [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Some ``not a number&#8217;&#8216; warnings introduced in 5.6.0 eliminated to be more compatible with 5.005. Infinity is now recognised as a number. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Numeric conversions did not recognize changes in the string value properly in certain circumstances. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Attributes (such as :shared) didn&#8217;t work with <code>our()</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>our()</code> variables will not cause bogus ``Variable will not stay shared&#8217;&#8216; warnings. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ``our&#8217;&#8216; variables of the same name declared in two sibling blocks resulted in bogus warnings about ``redeclaration&#8217;&#8216; of the variables. The problem has been corrected. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> pack ``Z&#8217;&#8216; now correctly terminates the string with ``\0&#8217;&#8216;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fix password routines which in some shadow password platforms (e.g. HP-UX) caused <code>getpwent()</code> to return every other entry. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <font SIZE="-1">PERL5OPT</font> environment variable (for passing command line arguments to Perl) didn&#8217;t work for more than a single group of options. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">PERL5OPT</font> with embedded spaces didn&#8217;t work. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>printf()</code> no longer resets the numeric locale to ``C&#8217;&#8216;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;qw(a\\b)&quot;</code> now parses correctly as <code>&#8216;a\\b&#8217;</code>: that is, as three characters, not four. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>pos()</code> did not return the correct value within s///ge in earlier versions. This is now handled correctly. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Printing quads (64-bit integers) with printf/sprintf now works without the q L ll prefixes (assuming you are on a quad-capable platform). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Regular expressions on references and overloaded scalars now work. [561+] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Right-hand side magic (<font SIZE="-1">GMAGIC</font>) could in many cases such as string concatenation be invoked too many times. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>scalar()</code> now forces scalar context even when used in void context. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">SOCKS</font> support is now much more robust. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>sort()</code> arguments are now compiled in the right wantarray context (they were accidentally using the context of the <code>sort()</code> itself). The comparison block is now run in scalar context, and the arguments to be sorted are always provided list context. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Changed the <font SIZE="-1">POSIX</font> character class <code>&quot;[[:space:]]&quot;</code> to include the (very rarely used) vertical tab character. Added a new POSIX-ish character class <code>&quot;[[:blank:]]&quot;</code> which stands for horizontal whitespace (currently, the space and the tab). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The tainting behaviour of <code>sprintf()</code> has been rationalized. It does not taint the result of floating point formats anymore, making the behaviour consistent with that of string interpolation. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Some cases of inconsistent taint propagation (such as within hash values) have been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <font SIZE="-1">RE</font> engine found in Perl 5.6.0 accidentally pessimised certain kinds of simple pattern matches. These are now handled better. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Regular expression debug output (whether through <code>&quot;use re &#8216;debug&#8217;&quot;</code> or via <code>&quot;-Dr&quot;</code>) now looks better. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Multi-line matches like <code>&quot;&quot;a\nxb\n&quot; =~ /(?!\A)x/m&quot;</code> were flawed. The bug has been fixed. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Use of $&amp; could trigger a core dump under some situations. This is now avoided. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The regular expression captured submatches ($1, <code>$2</code>, ...) are now more consistently unset if the match fails, instead of leaving false data lying around in them. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>readline()</code> on files opened in ``slurp&#8217;&#8216; mode could return an extra &quot;&quot; (blank line) at the end in certain situations. This has been corrected. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Autovivification of symbolic references of special variables described in perlvar (as in <code>&quot;${$num}&quot;</code>) was accidentally disabled. This works again now. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Sys::Syslog ignored the <code>&quot;LOG_AUTH&quot;</code> constant. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>$AUTOLOAD</code>, <code>sort()</code>, <code>lock()</code>, and spawning subprocesses in multiple threads simultaneously are now thread-safe. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Tie::Array&#8217;s <font SIZE="-1">SPLICE</font> method was broken. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Allow a read-only string on the left-hand side of a non-modifying tr///. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> If <code>&quot;STDERR&quot;</code> is tied, warnings caused by <code>&quot;warn&quot;</code> and <code>&quot;die&quot;</code> now correctly pass to it. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Several Unicode fixes. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> BOMs (byte order marks) at the beginning of Perl files (scripts, modules) should now be transparently skipped. <font SIZE="-1">UTF-16</font> and <font SIZE="-1">UCS-2</font> encoded Perl files should now be read correctly. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The character tables have been updated to Unicode 3.2.0. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Comparing with utf8 data does not magically upgrade non-utf8 data into utf8. (This was a problem for example if you were mixing data from I/O and Unicode data: your output might have got magically encoded as <font SIZE="-1">UTF-8.</font>) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Generating illegal Unicode code points such as U+FFFE, or the <font SIZE="-1">UTF-16</font> surrogates, now also generates an optional warning. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;IsAlnum&quot;</code>, <code>&quot;IsAlpha&quot;</code>, and <code>&quot;IsWord&quot;</code> now match titlecase. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Concatenation with the <code>&quot;.&quot;</code> operator or via variable interpolation, <code>&quot;eq&quot;</code>, <code>&quot;substr&quot;</code>, <code>&quot;reverse&quot;</code>, <code>&quot;quotemeta&quot;</code>, the <code>&quot;x&quot;</code> operator, substitution with <code>&quot;s///&quot;</code>, single-quoted <font SIZE="-1">UTF-8,</font> should now work. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;tr///&quot;</code> operator now works. Note that the <code>&quot;tr///CU&quot;</code> functionality has been removed (but see pack(&#8216;U0&#8217;, ...)). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;eval &quot;v200&quot;&quot;</code> now works. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl 5.6.0 parsed m/\x{ab}/ incorrectly, leading to spurious warnings. This has been corrected. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Zero entries were missing from the Unicode classes such as <code>&quot;IsDigit&quot;</code>. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>&bull;</dt>
<dd> <p> Large unsigned numbers (those above 2**31) could sometimes lose their unsignedness, causing bogus results in arithmetic operations. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The Perl parser has been stress tested using both random input and Markov chain input and the few found crashes and lockups have been fixed. </p>
 </dd></dl>
<h3>Platform Specific Changes and Fixes</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">BSDI 4</font>.* </p>
<p> Perl now works on post-4.0 BSD/OSes. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> All BSDs </p>
<p> Setting <code>$0</code> now works (as much as possible; see perlvar for details). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Cygwin </p>
<p> Numerous updates; currently synchronised with Cygwin 1.3.10. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Previously DYNIX/ptx had problems in its Configure probe for non-blocking I/O. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">EPOC</font> </p>
<p> <font SIZE="-1">EPOC</font> now better supported. See <font SIZE="-1">README</font>.epoc. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> FreeBSD 3.* </p>
<p> Perl now works on post-3.0 FreeBSDs. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> HP-UX </p>
<p> <font SIZE="-1">README</font>.hpux updated; <code>&quot;Configure -Duse64bitall&quot;</code> now works; now uses HP-UX malloc instead of Perl malloc. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">IRIX</font> </p>
<p> Numerous compilation flag and hint enhancements; accidental mixing of 32-bit and 64-bit libraries (a doomed attempt) made much harder. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Linux </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Long doubles should now work (see <font SIZE="-1">INSTALL</font>). [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Linux previously had problems related to sockaddrlen when using <code>accept()</code>, <code>recvfrom()</code> (in Perl: <code>recv()</code>), <code>getpeername()</code>, and <code>getsockname()</code>. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>&bull;</dt>
<dd> <p> Mac <font SIZE="-1">OS</font> Classic </p>
<p> Compilation of the standard Perl distribution in Mac <font SIZE="-1">OS</font> Classic should now work if you have the Metrowerks development environment and the missing Mac-specific toolkit bits. Contact the macperl mailing list for details. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> MPE/iX </p>
<p> MPE/iX update after Perl 5.6.0. See <font SIZE="-1">README</font>.mpeix. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> NetBSD/threads: try installing the <font SIZE="-1">GNU</font> pth (should be in the packages collection, or <a rel="nofollow" href="http://www.gnu.org/software/pth/">http://www.gnu.org/software/pth/</a>), and Configure with -Duseithreads. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> NetBSD/sparc </p>
<p> Perl now works on NetBSD/sparc. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">OS/2</font> </p>
<p> Now works with usethreads (see <font SIZE="-1">INSTALL</font>). [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Solaris </p>
<p> 64-bitness using the Sun Workshop compiler now works. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Stratus <font SIZE="-1">VOS</font> </p>
<p> The native build method requires at least <font SIZE="-1">VOS</font> Release 14.5.0 and <font SIZE="-1">GNU C<font SIZE="-2">++</font>/GNU</font> Tools 2.0.1 or later. The Perl pack function now maps overflowed values to +infinity and underflowed values to -infinity. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Tru64 (aka Digital <font SIZE="-1">UNIX,</font> aka <font SIZE="-1">DEC OSF/1</font>) </p>
<p> The operating system version letter now recorded in <code>$Config</code>{osvers}. Allow compiling with gcc (previously explicitly forbidden). Compiling with gcc still not recommended because buggy code results, even with gcc 2.95.2. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unicos </p>
<p> Fixed various alignment problems that lead into core dumps either during build or later; no longer dies on math errors at runtime; now using full quad integers (64 bits), previously was using only 46 bit integers for speed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">VMS</font> </p>
<p> See ``Socket Extension Dynamic in <font SIZE="-1">VMS&#8217;&#8216;</font> and ``IEEE-format Floating Point Default on OpenVMS Alpha&#8217;&#8216; for important changes not otherwise listed here. </p>
<p> <code>chdir()</code> now works better despite a <font SIZE="-1">CRT</font> bug; now works with <font SIZE="-1">MULTIPLICITY</font> (see <font SIZE="-1">INSTALL</font>); now works with Perl&#8217;s malloc. </p>
<p> The tainting of <code>%ENV</code> elements via <code>&quot;keys&quot;</code> or <code>&quot;values&quot;</code> was previously unimplemented. It now works as documented. </p>
<p> The <code>&quot;waitpid&quot;</code> emulation has been improved. The worst bug (now fixed) was that a pid of -1 would cause a wildcard search of all processes on the system. </p>
<p> POSIX-style signals are now emulated much better on <font SIZE="-1">VMS</font> versions prior to 7.0. </p>
<p> The <code>&quot;system&quot;</code> function and backticks operator have improved functionality and better error handling. [561] </p>
<p> File access tests now use current process privileges rather than the user&#8217;s default privileges, which could sometimes result in a mismatch between reported access and actual access. This improvement is only available on <font SIZE="-1">VMS</font> v6.0 and later. </p>
<p> There is a new <code>&quot;kill&quot;</code> implementation based on <code>&quot;sys$sigprc&quot;</code> that allows older <font SIZE="-1">VMS</font> systems (pre-7.0) to use <code>&quot;kill&quot;</code> to send signals rather than simply force exit. This implementation also allows later systems to call <code>&quot;kill&quot;</code> from within a signal handler. </p>
<p> Iterative logical name translations are now limited to 10 iterations in imitation of <font SIZE="-1">SHOW LOGICAL</font> and other OpenVMS facilities. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Windows </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Signal handling now works better than it used to. It is now implemented using a Windows message loop, and is therefore less prone to random crashes. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>fork()</code> emulation is now more robust, but still continues to have a few esoteric bugs and caveats. See perlfork for details. [561+] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A failed (pseudo)fork now returns undef and sets errno to <font SIZE="-1">EAGAIN.</font> [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The following modules now work on Windows: </p>
<pre><code>    ExtUtils::Embed [561]
    IO::Pipe
    IO::Poll
    Net::Ping
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>IO::File::new_tmpfile()</code> is no longer limited to 32767 invocations per-process. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Better <code>chdir()</code> return value for a non-existent directory. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Compiling perl using the 64-bit Platform <font SIZE="-1">SDK</font> tools is now supported. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>Win32::SetChildShowWindow()</code> builtin can be used to control the visibility of windows created by child processes. See Win32 for details. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Non-blocking waits for child processes (or pseudo-processes) are supported via <code>&quot;waitpid($pid, &amp;POSIX::WNOHANG)&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The behavior of <code>system()</code> with multiple arguments has been rationalized. Each unquoted argument will be automatically quoted to protect whitespace, and any existing whitespace in the arguments will be preserved. This improves the portability of system(@args) by avoiding the need for Windows <code>&quot;cmd&quot;</code> shell specific quoting in perl programs. </p>
<p> Note that this means that some scripts that may have relied on earlier buggy behavior may no longer work correctly. For example, <code>&quot;system(&quot;nmake /nologo&quot;, @args)&quot;</code> will now attempt to run the file <code>&quot;nmake /nologo&quot;</code> and will fail when such a file isn&#8217;t found. On the other hand, perl will now execute code such as <code>&quot;system(&quot;c:/Program Files/MyApp/foo.exe&quot;, @args)&quot;</code> correctly. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The perl header files no longer suppress common warnings from the Microsoft Visual C<font SIZE="-2">++</font> compiler. This means that additional warnings may now show up when compiling <font SIZE="-1">XS</font> code. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Borland C<font SIZE="-2">++</font> v5.5 is now a supported compiler that can build Perl. However, the generated binaries continue to be incompatible with those generated by the other supported compilers (<font SIZE="-1">GCC</font> and Visual C<font SIZE="-2">++</font>). [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Duping socket handles with open(F, ``&gt;&amp;MYSOCK&#8217;&#8216;) now works under Windows 9x. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Current directory entries in <code>%ENV</code> are now correctly propagated to child processes. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> New <code>%ENV</code> entries now propagate to subprocesses. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>Win32::GetCwd()</code> correctly returns C:\ instead of C: when at the drive root. Other bugs in <code>chdir()</code> and <code>Cwd::cwd()</code> have also been fixed. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The makefiles now default to the features enabled in ActiveState ActivePerl (a popular Win32 binary distribution). [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">HTML</font> files will now be installed in c:\perl\html instead of c:\perl\lib\pod\html </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">REG_EXPAND_SZ</font> keys are now allowed in registry settings used by perl. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Can now <code>send()</code> from all threads, not just the first one. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::MakeMaker now uses <code>$ENV</code>{<font SIZE="-1">LIB</font>} to search for libraries. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Less stack reserved per thread so that more threads can run concurrently. (Still 16M per thread.) [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;File::Spec-&gt;tmpdir()&quot;</code> now prefers C:/temp over /tmp (works better when perl is running as service). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Better <font SIZE="-1">UNC</font> path handling under ithreads. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>wait()</code>, <code>waitpid()</code>, and backticks now return the correct exit status under Windows 9x. [561] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A socket handle leak in <code>accept()</code> has been fixed. [561] </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
</dl>
<h2>New or Changed Diagnostics</h2>
<p> Please see perldiag for more details. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Ambiguous range in the transliteration operator (like a-z-9) now gives a warning. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> chdir(&quot;&quot;) and chdir(undef) now give a deprecation warning because they cause a possible unintentional chdir to the home directory. Say <code>chdir()</code> if you really mean that. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Two new debugging options have been added: if you have compiled your Perl with debugging, you can use the -DT [561] and -DR options to trace tokenising and to add reference counts to displaying variables, respectively. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The lexical warnings category ``deprecated&#8217;&#8216; is no longer a sub-category of the ``syntax&#8217;&#8216; category. It is now a top-level category in its own right. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unadorned <code>dump()</code> will now give a warning suggesting to use explicit <code>CORE::dump()</code> if that&#8217;s what really is meant. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The ``Unrecognized escape&#8217;&#8216; warning has been extended to include <code>&quot;\8&quot;</code>, <code>&quot;\9&quot;</code>, and <code>&quot;\_&quot;</code>. There is no need to escape any of the <code>&quot;\w&quot;</code> characters. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> All regular expression compilation error messages are now hopefully easier to understand both because the error message now comes before the failed regex and because the point of failure is now clearly marked by a <code>&quot;&lt;-- HERE&quot;</code> marker. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Various I/O (and socket) functions like <code>binmode()</code>, <code>close()</code>, and so forth now more consistently warn if they are used illogically either on a yet unopened or on an already closed filehandle (or socket). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Using <code>lstat()</code> on a filehandle now gives a warning. (It&#8217;s a non-sensical thing to do.) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;-M&quot;</code> and <code>&quot;-m&quot;</code> options now warn if you didn&#8217;t supply the module name. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> If you in <code>&quot;use&quot;</code> specify a required minimum version, modules matching the name and but not defining a <code>$VERSION</code> will cause a fatal failure. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Using negative offset for <code>vec()</code> in lvalue context is now a warnable offense. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Odd number of arguments to overload::constant now elicits a warning. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Odd number of elements in anonymous hash now elicits a warning. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The various ``opened only for&#8217;&#8216;, ``on closed&#8217;&#8216;, ``never opened&#8217;&#8216; warnings drop the <code>&quot;main::&quot;</code> prefix for filehandles in the <code>&quot;main&quot;</code> package, for example <code>&quot;STDIN&quot;</code> instead of <code>&quot;main::STDIN&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Subroutine prototypes are now checked more carefully, you may get warnings for example if you have used non-prototype characters. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> If an attempt to use a (non-blessed) reference as an array index is made, a warning is given. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;push @a;&quot;</code> and <code>&quot;unshift @a;&quot;</code> (with no values to push or unshift) now give a warning. This may be a problem for generated and eval&#8217;ed code. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> If you try to ``pack&#8217;&#8216; in perlfunc a number less than 0 or larger than 255 using the <code>&quot;C&quot;</code> format you will get an optional warning. Similarly for the <code>&quot;c&quot;</code> format and a number less than -128 or more than 127. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> pack <code>&quot;P&quot;</code> format now demands an explicit size. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> unpack <code>&quot;w&quot;</code> now warns of unterminated compressed integers. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Warnings relating to the use of PerlIO have been added. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Certain regex modifiers such as <code>&quot;(?o)&quot;</code> make sense only if applied to the entire regex. You will get an optional warning if you try to do otherwise. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Variable length lookbehind has not yet been implemented, trying to use it will tell that. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Using arrays or hashes as references (e.g. <code>&quot;%foo-&gt;{bar}&quot;</code> has been deprecated for a while. Now you will get an optional warning. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Warnings relating to the use of the new restricted hashes feature have been added. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Self-ties of arrays and hashes are not supported and fatal errors will happen even at an attempt to do so. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Using <code>&quot;sort&quot;</code> in scalar context now issues an optional warning. This didn&#8217;t do anything useful, as the sort was not performed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Using the /g modifier in <code>split()</code> is meaningless and will cause a warning. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Using <code>splice()</code> past the end of an array now causes a warning. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Malformed Unicode encodings (<font SIZE="-1">UTF-8</font> and <font SIZE="-1">UTF-16</font>) cause a lot of warnings, as does trying to use <font SIZE="-1">UTF-16</font> surrogates (which are unimplemented). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Trying to use Unicode characters on an I/O stream without marking the stream&#8217;s encoding (using <code>open()</code> or <code>binmode()</code>) will cause ``Wide character&#8217;&#8216; warnings. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Use of v-strings in use/require causes a (backward) portability warning. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Warnings relating to the use interpreter threads and their shared data have been added. </p>
 </dd></dl>
<h2>Changed Internals</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> PerlIO is now the default. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlapi.pod (a companion to perlguts) now attempts to document the internal <font SIZE="-1">API.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> You can now build a really minimal perl called microperl. Building microperl does not require even running Configure; <code>&quot;make -f Makefile.micro&quot;</code> should be enough. Beware: microperl makes many assumptions, some of which may be too bold; the resulting executable may crash or otherwise misbehave in wondrous ways. For careful hackers only. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Added <code>rsignal()</code>, <code>whichsig()</code>, <code>do_join()</code>, op_clear, op_null, <code>ptr_table_clear()</code>, <code>ptr_table_free()</code>, <code>sv_setref_uv()</code>, and several <font SIZE="-1">UTF-8</font> interfaces to the publicised <font SIZE="-1">API.</font> For the full list of the available APIs see perlapi. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Made possible to propagate customised exceptions via <code>croak()</code>ing. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Now xsubs can have attributes just like subs. (Well, at least the built-in attributes.) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> dTHR and djSP have been obsoleted; the former removed (because it&#8217;s a no-op) and the latter replaced with dSP. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">PERL_OBJECT</font> has been completely removed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <font SIZE="-1">MAGIC</font> constants (e.g. <code>&#8216;P&#8217;</code>) have been macrofied (e.g. <code>&quot;PERL_MAGIC_TIED&quot;</code>) for better source code readability and maintainability. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The regex compiler now maintains a structure that identifies nodes in the compiled bytecode with the corresponding syntactic features of the original regex expression. The information is attached to the new <code>&quot;offsets&quot;</code> member of the <code>&quot;struct regexp&quot;</code>. See perldebguts for more complete information. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The C code has been made much more <code>&quot;gcc -Wall&quot;</code> clean. Some warning messages still remain in some platforms, so if you are compiling with gcc you may see some warnings about dubious practices. The warnings are being worked on. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>perly.c</i>, <i>sv.c</i>, and <i>sv.h</i> have now been extensively commented. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Documentation on how to use the Perl source repository has been added to <i>Porting/repository.pod</i>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> There are now several profiling make targets. </p>
 </dd></dl>
<h2>Security Vulnerability Closed [561]</h2>
<p> (This change was already made in 5.7.0 but bears repeating here.) (5.7.0 came out before 5.6.1: the development branch 5.7 released earlier than the maintenance branch 5.6) </p>
<p> A potential security vulnerability in the optional suidperl component of Perl was identified in August 2000. suidperl is neither built nor installed by default. As of November 2001 the only known vulnerable platform is Linux, most likely all Linux distributions. <font SIZE="-1">CERT</font> and various vendors and distributors have been alerted about the vulnerability. See <a rel="nofollow" href="http://www.cpan.org/src/5.0/sperl-2000-08-05/sperl-2000-08-05.txt">http://www.cpan.org/src/5.0/sperl-2000-08-05/sperl-2000-08-05.txt</a> for more information. </p>
<p> The problem was caused by Perl trying to report a suspected security exploit attempt using an external program, /bin/mail. On Linux platforms the /bin/mail program had an undocumented feature which when combined with suidperl gave access to a root shell, resulting in a serious compromise instead of reporting the exploit attempt. If you don&#8217;t have /bin/mail, or if you have &#8216;safe setuid scripts&#8217;, or if suidperl is not installed, you are safe. </p>
<p> The exploit attempt reporting feature has been completely removed from Perl 5.8.0 (and the maintenance release 5.6.1, and it was removed also from all the Perl 5.7 releases), so that particular vulnerability isn&#8217;t there anymore. However, further security vulnerabilities are, unfortunately, always possible. The suidperl functionality is most probably going to be removed in Perl 5.10. In any case, suidperl should only be used by security experts who know exactly what they are doing and why they are using suidperl instead of some other solution such as sudo ( see <a rel="nofollow" href="http://www.courtesan.com/sudo/">http://www.courtesan.com/sudo/</a> ).  </p>
<h2>New Tests</h2>
<p> Several new tests have been added, especially for the <i>lib</i> and <i>ext</i> subsections. There are now about 69 000 individual tests (spread over about 700 test scripts), in the regression suite (5.6.1 has about 11 700 tests, in 258 test scripts) The exact numbers depend on the platform and Perl configuration used. Many of the new tests are of course introduced by the new modules, but still in general Perl is now more thoroughly tested. </p>
<p> Because of the large number of tests, running the regression suite will take considerably longer time than it used to: expect the suite to take up to 4-5 times longer to run than in perl 5.6. On a really fast machine you can hope to finish the suite in about 6-8 minutes (wallclock time). </p>
<p> The tests are now reported in a different order than in earlier Perls. (This happens because the test scripts from under t/lib have been moved to be closer to the library/extension they are testing.)  </p>
<h2>Known Problems</h2>
<h3>The Compiler Suite Is Still Very Experimental</h3>
<p> The compiler suite is slowly getting better but it continues to be highly experimental. Use in production environments is discouraged.  </p>
<h3>Localising Tied Arrays and Hashes Is Broken</h3>
<pre><code>    local %tied_array;
</code></pre>
<p> doesn&#8217;t work as one would expect: the old value is restored incorrectly. This will be changed in a future release, but we don&#8217;t know yet what the new semantics will exactly be. In any case, the change will break existing code that relies on the current (ill-defined) semantics, so just avoid doing this in general.  </p>
<h3>Building Extensions Can Fail Because Of Largefiles</h3>
<p> Some extensions like mod_perl are known to have issues with `largefiles&#8217;, a change brought by Perl 5.6.0 in which file offsets default to 64 bits wide, where supported. Modules may fail to compile at all, or they may compile and work incorrectly. Currently, there is no good solution for the problem, but Configure now provides appropriate non-largefile ccflags, ldflags, libswanted, and libs in the <code>%Config</code> hash (e.g., <code>$Config</code>{ccflags_nolargefiles}) so the extensions that are having problems can try configuring themselves without the largefileness. This is admittedly not a clean solution, and the solution may not even work at all. One potential failure is whether one can (or, if one can, whether it&#8217;s a good idea to) link together at all binaries with different ideas about file offsets; all this is platform-dependent.  </p>
<h3>Modifying $_ Inside for(..)</h3>
<pre><code>   for (1..5) { $_++ }
</code></pre>
<p> works without complaint. It shouldn&#8217;t. (You should be able to modify only lvalue elements inside the loops.) You can see the correct behaviour by replacing the 1..5 with 1, 2, 3, 4, 5.  </p>
<h3>mod_perl 1.26 Doesn't Build With Threaded Perl</h3>
<p> Use mod_perl 1.27 or higher.  </p>
<h3>lib/ftmp-security tests warn 'system possibly insecure'</h3>
<p> Don&#8217;t panic. Read the &#8216;make test&#8217; section of <font SIZE="-1">INSTALL</font> instead.  </p>
<font SIZE="-1"></font><h3>libwww-perl ( LWP ) fails base/date #51</h3>
<p> Use libwww-perl 5.65 or later.  </p>
<font SIZE="-1"></font><h3>PDL failing some tests</h3>
<p> Use <font SIZE="-1">PDL 2.3.4</font> or later.  </p>
<h3>Perl_get_sv</h3>
<p> You may get errors like &#8216;Undefined symbol ``Perl_get_sv&#8217;&#8216;&#8216; or ``can&#8217;t resolve symbol &#8216;Perl_get_sv&#8217;&#8216;&#8216;, or the symbol may be ``Perl_sv_2pv&#8217;&#8216;. This probably means that you are trying to use an older shared Perl library (or extensions linked with such) with Perl 5.8.0 executable. Perl used to have such a subroutine, but that is no more the case. Check your shared library path, and any shared Perl libraries in those directories. </p>
<p> Sometimes this problem may also indicate a partial Perl 5.8.0 installation, see ``Mac <font SIZE="-1">OS X</font> dyld undefined symbols&#8217;&#8216; for an example and how to deal with it.  </p>
<h3>Self-tying Problems</h3>
<p> Self-tying of arrays and hashes is broken in rather deep and hard-to-fix ways. As a stop-gap measure to avoid people from getting frustrated at the mysterious results (core dumps, most often), it is forbidden for now (you will get a fatal error even from an attempt). </p>
<p> A change to self-tying of globs has caused them to be recursively referenced (see: ``Two-Phased Garbage Collection&#8217;&#8216; in perlobj). You will now need an explicit untie to destroy a self-tied glob. This behaviour may be fixed at a later date. </p>
<p> Self-tying of scalars and <font SIZE="-1">IO</font> thingies works.  </p>
<h3>ext/threads/t/libc</h3>
<p> If this test fails, it indicates that your libc (C library) is not threadsafe. This particular test stress tests the <code>localtime()</code> call to find out whether it is threadsafe. See perlthrtut for more information.  </p>
<h3>Failure of Thread (5.005-style) tests</h3>
<p> <code>Note that support for 5.005-style threading is deprecated, experimental and practically unsupported. In 5.10, it is expected to be removed. You should migrate your code to ithreads.</code> </p>
<p> The following tests are known to fail due to fundamental problems in the 5.005 threading implementation. These are not new failures---Perl 5.005_0x has the same bugs, but didn&#8217;t have these tests. </p>
<pre><code> ../ext/B/t/xref.t 255 65280 14 12 85.71% 3-14
 ../ext/List/Util/t/first.t 255 65280 7 4 57.14% 2 5-7
 ../lib/English.t 2 512 54 2 3.70% 2-3
 ../lib/FileCache.t 5 1 20.00% 5
 ../lib/Filter/Simple/t/data.t 6 3 50.00% 1-3
 ../lib/Filter/Simple/t/filter_only. 9 3 33.33% 1-2 5
 ../lib/Math/BigInt/t/bare_mbf.t 1627 4 0.25% 8 11 1626-1627
 ../lib/Math/BigInt/t/bigfltpm.t 1629 4 0.25% 10 13 1628-
                                                                    1629
 ../lib/Math/BigInt/t/sub_mbf.t 1633 4 0.24% 8 11 1632-1633
 ../lib/Math/BigInt/t/with_sub.t 1628 4 0.25% 9 12 1627-1628
 ../lib/Tie/File/t/31_autodefer.t 255 65280 65 32 49.23% 34-65
 ../lib/autouse.t 10 1 10.00% 4
 op/flip.t 15 1 6.67% 15
</code></pre>
<p> These failures are unlikely to get fixed as 5.005-style threads are considered fundamentally broken. (Basically what happens is that competing threads can corrupt shared global state, one good example being regular expression engine&#8217;s state.)  </p>
<h3>Timing problems</h3>
<p> The following tests may fail intermittently because of timing problems, for example if the system is heavily loaded. </p>
<pre><code>    t/op/alarm.t
    ext/Time/HiRes/HiRes.t
    lib/Benchmark.t
    lib/Memoize/t/expmod_t.t
    lib/Memoize/t/speed.t
</code></pre>
<p> In case of failure please try running them manually, for example </p>
<pre><code>    ./perl -Ilib ext/Time/HiRes/HiRes.t
</code></pre>
<h3>Tied/Magical Array/Hash Elements Do Not Autovivify</h3>
<p> For normal arrays <code>&quot;$foo = \$bar[1]&quot;</code> will assign <code>&quot;undef&quot;</code> to <code>$bar[1]</code> (assuming that it didn&#8217;t exist before), but for tied/magical arrays and hashes such autovivification does not happen because there is currently no way to catch the reference creation. The same problem affects slicing over non-existent indices/keys of a tied/magical array/hash.  </p>
<h3>Unicode in package/class and subroutine names does not work</h3>
<p> One can have Unicode in identifier names, but not in package/class or subroutine names. While some limited functionality towards this does exist as of Perl 5.8.0, that is more accidental than designed; use of Unicode for the said purposes is unsupported. </p>
<p> One reason of this unfinishedness is its (currently) inherent unportability: since both package names and subroutine names may need to be mapped to file and directory names, the Unicode capability of the filesystem becomes important--- and there unfortunately aren&#8217;t portable answers.  </p>
<h2>Platform Specific Problems</h2>
<font SIZE="-1"></font><h3>AIX</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> If using the <font SIZE="-1">AIX</font> native make command, instead of just ``make&#8217;&#8216; issue ``make all&#8217;&#8216;. In some setups the former has been known to spuriously also try to run ``make install&#8217;&#8216;. Alternatively, you may want to use <font SIZE="-1">GNU</font> make. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In <font SIZE="-1">AIX 4.2,</font> Perl extensions that use C<font SIZE="-2">++</font> functions that use statics may have problems in that the statics are not getting initialized. In newer <font SIZE="-1">AIX</font> releases, this has been solved by linking Perl with the libC_r library, but unfortunately in <font SIZE="-1">AIX 4.2</font> the said library has an obscure bug where the various functions related to time (such as <code>time()</code> and <code>gettimeofday()</code>) return broken values, and therefore in <font SIZE="-1">AIX 4.2</font> Perl is not linked against libC_r. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> vac 5.0.0.0 May Produce Buggy Code For Perl </p>
<p> The <font SIZE="-1">AIX C</font> compiler vac version 5.0.0.0 may produce buggy code, resulting in a few random tests failing when run as part of ``make test&#8217;&#8216;, but when the failing tests are run by hand, they succeed. We suggest upgrading to at least vac version 5.0.1.0, that has been known to compile Perl correctly. ``lslpp -L|grep vac.C&#8217;&#8216; will tell you the vac version. See <font SIZE="-1">README</font>.aix. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> If building threaded Perl, you may get compilation warning from pp_sys.c: </p>
<pre><code>  &quot;pp_sys.c&quot;, line 4651.39: 1506-280 (W) Function argument assignment between types &quot;unsigned char*&quot; and &quot;const void*&quot; is not allowed.
</code></pre>
<p> This is harmless; it is caused by the <code>getnetbyaddr()</code> and <code>getnetbyaddr_r()</code> having slightly different types for their first argument. </p>
 </dd></dl>
<h3>Alpha systems with old gccs fail several tests</h3>
<p> If you see op/pack, op/pat, op/regexp, or ext/Storable tests failing in a Linux/alpha or *BSD/Alpha, it&#8217;s probably time to upgrade your gcc. gccs prior to 2.95.3 are definitely not good enough, and gcc 3.1 may be even better. (RedHat Linux/alpha with gcc 3.1 reported no problems, as did Linux 2.4.18 with gcc 2.95.4.) (In Tru64, it is preferable to use the bundled C compiler.)  </p>
<h3>AmigaOS</h3>
<p> Perl 5.8.0 doesn&#8217;t build in AmigaOS. It broke at some point during the ithreads work and we could not find Amiga experts to unbreak the problems. Perl 5.6.1 still works for AmigaOS (as does the 5.7.2 development release).  </p>
<h3>BeOS</h3>
<p> The following tests fail on 5.8.0 Perl in BeOS Personal 5.03: </p>
<pre><code> t/op/lfs............................FAILED at test 17
 t/op/magic..........................FAILED at test 24
 ext/Fcntl/t/syslfs..................FAILED at test 17
 ext/File/Glob/t/basic...............FAILED at test 3
 ext/POSIX/t/sigaction...............FAILED at test 13
 ext/POSIX/t/waitpid.................FAILED at test 1
</code></pre>
<p> (<code>Note:</code> more information was available in <i></i><font SIZE="-1"><i>README</i></font><i>.beos</i> until support for BeOS was removed in Perl v5.18.0)  </p>
<h3>Cygwin unable to remap</h3>
<p> For example when building the Tk extension for Cygwin, you may get an error message saying ``unable to remap&#8217;&#8216;. This is known problem with Cygwin, and a workaround is detailed in here: <a rel="nofollow" href="http://sources.redhat.com/ml/cygwin/2001-12/msg00894.html">http://sources.redhat.com/ml/cygwin/2001-12/msg00894.html</a>  </p>
<font SIZE="-1"></font><h3>Cygwin ndbm tests fail on FAT</h3>
<p> One can build but not install (or test the build of) the NDBM_File on <font SIZE="-1">FAT</font> filesystems. Installation (or build) on <font SIZE="-1">NTFS</font> works fine. If one attempts the test on a <font SIZE="-1">FAT</font> install (or build) the following failures are expected: </p>
<pre><code> ../ext/NDBM_File/ndbm.t 13 3328 71 59 83.10% 1-2 4 16-71
 ../ext/ODBM_File/odbm.t 255 65280 ?? ?? % ??
 ../lib/AnyDBM_File.t 2 512 12 2 16.67% 1 4
 ../lib/Memoize/t/errors.t 0 139 11 5 45.45% 7-11
 ../lib/Memoize/t/tie_ndbm.t 13 3328 4 4 100.00% 1-4
 run/fresh_perl.t 97 1 1.03% 91
</code></pre>
<p> NDBM_File fails and ODBM_File just coredumps. </p>
<p> If you intend to run only on <font SIZE="-1">FAT</font> (or if using AnyDBM_File on <font SIZE="-1">FAT</font>), run Configure with the -Ui_ndbm and -Ui_dbm options to prevent NDBM_File and ODBM_File being built.  </p>
<font SIZE="-1"></font><h3>DJGPP Failures</h3>
<pre><code> t/op/stat............................FAILED at test 29
 lib/File/Find/t/find.................FAILED at test 1
 lib/File/Find/t/taint................FAILED at test 1
 lib/h2xs.............................FAILED at test 15
 lib/Pod/t/eol........................FAILED at test 1
 lib/Test/Harness/t/strap-analyze.....FAILED at test 8
 lib/Test/Harness/t/test-harness......FAILED at test 23
 lib/Test/Simple/t/exit...............FAILED at test 1
</code></pre>
<p> The above failures are known as of 5.8.0 with native builds with long filenames, but there are a few more if running under dosemu because of limitations (and maybe bugs) of dosemu: </p>
<pre><code> t/comp/cpp...........................FAILED at test 3
 t/op/inccode.........................(crash)
</code></pre>
<p> and a few lib/ExtUtils tests, and several hundred Encode/t/Aliases.t failures that work fine with long filenames. So you really might prefer native builds and long filenames.  </p>
<h3>FreeBSD built with ithreads coredumps reading large directories</h3>
<p> This is a known bug in FreeBSD 4.5&#8217;s <code>readdir_r()</code>, it has been fixed in FreeBSD 4.6 (see perlfreebsd (<font SIZE="-1">README</font>.freebsd)).  </p>
<font SIZE="-1"></font><h3>FreeBSD Failing locale Test 117 For ISO 8859-15 Locales</h3>
<p> The <font SIZE="-1">ISO 8859-15</font> locales may fail the locale test 117 in FreeBSD. This is caused by the characters \xFF (y with diaeresis) and \xBE (Y with diaeresis) not behaving correctly when being matched case-insensitively. Apparently this problem has been fixed in the latest FreeBSD releases. ( <a rel="nofollow" href="http://www.freebsd.org/cgi/query-pr.cgi?pr=34308">http://www.freebsd.org/cgi/query-pr.cgi?pr=34308</a> )  </p>
<font SIZE="-1"></font><h3>IRIX fails ext/List/Util/t/shuffle.t or Digest::MD5</h3>
<p> <font SIZE="-1">IRIX</font> with MIPSpro 7.3.1.2m or 7.3.1.3m compiler may fail the List::Util test ext/List/Util/t/shuffle.t by dumping core. This seems to be a compiler error since if compiled with gcc no core dump ensues, and no failures have been seen on the said test on any other platform. </p>
<p> Similarly, building the Digest::MD5 extension has been known to fail with ``*** Termination code 139 (bu21)&#8216;&#8216;. </p>
<p> The cure is to drop optimization level (Configure -Doptimize=-O2).  </p>
<h3>HP-UX lib/posix Subtest 9 Fails When LP64-Configured</h3>
<p> If perl is configured with -Duse64bitall, the successful result of the subtest 10 of lib/posix may arrive before the successful result of the subtest 9, which confuses the test harness so much that it thinks the subtest 9 failed.  </p>
<h3>Linux with glibc 2.2.5 fails t/op/int subtest #6 with -Duse64bitint</h3>
<p> This is a known bug in the glibc 2.2.5 with long long integers. ( <a rel="nofollow" href="http://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=65612">http://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=65612</a> )  </p>
<h3>Linux With Sfio Fails op/misc Test 48</h3>
<p> No known fix.  </p>
<font SIZE="-1"></font><h3>Mac OS X</h3>
<p> Please remember to set your environment variable <font SIZE="-1">LC_ALL</font> to ``C&#8217;&#8216; (setenv <font SIZE="-1">LC_ALL C</font>) before running ``make test&#8217;&#8216; to avoid a lot of warnings about the broken locales of Mac <font SIZE="-1">OS X.</font> </p>
<p> The following tests are known to fail in Mac <font SIZE="-1">OS X 10.1.5</font> because of buggy (old) implementations of Berkeley <font SIZE="-1">DB</font> included in Mac <font SIZE="-1">OS X:</font> </p>
<pre><code> Failed Test Stat Wstat Total Fail Failed List of Failed
 -------------------------------------------------------------------------
 ../ext/DB_File/t/db-btree.t 0 11 ?? ?? % ??
 ../ext/DB_File/t/db-recno.t 149 3 2.01% 61 63 65
</code></pre>
<p> If you are building on a <font SIZE="-1">UFS</font> partition, you will also probably see t/op/stat.t subtest #9 fail. This is caused by Darwin&#8217;s <font SIZE="-1">UFS</font> not supporting inode change time. </p>
<p> Also the ext/POSIX/t/posix.t subtest #10 fails but it is skipped for now because the failure is Apple&#8217;s fault, not Perl&#8217;s (blocked signals are lost). </p>
<p> If you Configure with ithreads, ext/threads/t/libc.t will fail. Again, this is not Perl&#8217;s fault--- the libc of Mac <font SIZE="-1">OS X</font> is not threadsafe (in this particular test, the <code>localtime()</code> call is found to be threadunsafe.)  </p>
<font SIZE="-1"></font><h3>Mac OS X dyld undefined symbols</h3>
<p> If after installing Perl 5.8.0 you are getting warnings about missing symbols, for example </p>
<pre><code>    dyld: perl Undefined symbols
    _perl_sv_2pv
    _perl_get_sv
</code></pre>
<p> you probably have an old pre-Perl-5.8.0 installation (or parts of one) in /Library/Perl (the undefined symbols used to exist in pre-5.8.0 Perls). It seems that for some reason ``make install&#8217;&#8216; doesn&#8217;t always completely overwrite the files in /Library/Perl. You can move the old Perl shared library out of the way like this: </p>
<pre><code>    cd /Library/Perl/darwin/CORE
    mv libperl.dylib libperlold.dylib
</code></pre>
<p> and then reissue ``make install&#8217;&#8216;. Note that the above of course is extremely disruptive for anything using the /usr/local/bin/perl. If that doesn&#8217;t help, you may have to try removing all the .bundle files from beneath /Library/Perl, and again ``make install&#8217;&#8216;-ing.  </p>
<font SIZE="-1"></font><h3>OS/2 Test Failures</h3>
<p> The following tests are known to fail on <font SIZE="-1">OS/2</font> (for clarity only the failures are shown, not the full error messages): </p>
<pre><code> ../lib/ExtUtils/t/Mkbootstrap.t 1 256 18 1 5.56% 8
 ../lib/ExtUtils/t/Packlist.t 1 256 34 1 2.94% 17
 ../lib/ExtUtils/t/basic.t 1 256 17 1 5.88% 14
 lib/os2_process.t 2 512 227 2 0.88% 174 209
 lib/os2_process_kid.t 227 2 0.88% 174 209
 lib/rx_cmprt.t 255 65280 18 3 16.67% 16-18
</code></pre>
<h3>op/sprintf tests 91, 129, and 130</h3>
<p> The op/sprintf tests 91, 129, and 130 are known to fail on some platforms. Examples include any platform using sfio, and Compaq/Tandem&#8217;s NonStop-UX. </p>
<p> Test 91 is known to fail on <font SIZE="-1">QNX6</font> (nto), because <code>&quot;sprintf &#8216;%e&#8217;,0&quot;</code> incorrectly produces <code>0.000000e+0</code> instead of <code>0.000000e+00</code>. </p>
<p> For tests 129 and 130, the failing platforms do not comply with the <font SIZE="-1">ANSI C</font> Standard: lines 19ff on page 134 of <font SIZE="-1">ANSI X3.159 1989,</font> to be exact. (They produce something other than ``1&#8217;&#8216; and ``-1&#8217;&#8216; when formatting 0.6 and -0.6 using the printf format ``%.0f&#8217;&#8216;; most often, they produce ``0&#8217;&#8216; and ``-0&#8217;&#8216;.)  </p>
<font SIZE="-1"></font><h3>SCO</h3>
<p> The socketpair tests are known to be unhappy in <font SIZE="-1">SCO 3</font>.2v5.0.4: </p>
<pre><code> ext/Socket/socketpair.t...............FAILED tests 15-45
</code></pre>
<h3>Solaris 2.5</h3>
<p> In case you are still using Solaris 2.5 (aka SunOS 5.5), you may experience failures (the test core dumping) in lib/locale.t. The suggested cure is to upgrade your Solaris.  </p>
<h3>Solaris x86 Fails Tests With -Duse64bitint</h3>
<p> The following tests are known to fail in Solaris x86 with Perl configured to use 64 bit integers: </p>
<pre><code> ext/Data/Dumper/t/dumper.............FAILED at test 268
 ext/Devel/Peek/Peek..................FAILED at test 7
</code></pre>
<font SIZE="-1"></font><h3>SUPER-UX ( NEC SX )</h3>
<p> The following tests are known to fail on SUPER-UX: </p>
<pre><code> op/64bitint...........................FAILED tests 29-30, 32-33, 35-36
 op/arith..............................FAILED tests 128-130
 op/pack...............................FAILED tests 25-5625
 op/pow................................
 op/taint..............................# msgsnd failed
 ../ext/IO/lib/IO/t/io_poll............FAILED tests 3-4
 ../ext/IPC/SysV/ipcsysv...............FAILED tests 2, 5-6
 ../ext/IPC/SysV/t/msg.................FAILED tests 2, 4-6
 ../ext/Socket/socketpair..............FAILED tests 12
 ../lib/IPC/SysV.......................FAILED tests 2, 5-6
 ../lib/warnings.......................FAILED tests 115-116, 118-119
</code></pre>
<p> The op/pack failure (``Cannot compress negative numbers at op/pack.t line 126&#8217;&#8216;) is serious but as of yet unsolved. It points at some problems with the signedness handling of the C compiler, as do the 64bitint, arith, and pow failures. Most of the rest point at problems with SysV <font SIZE="-1">IPC.</font>  </p>
<h3>Term::ReadKey not working on Win32</h3>
<p> Use Term::ReadKey 2.20 or later.  </p>
<h3>UNICOS/mk</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> During Configure, the test </p>
<pre><code>    Guessing which symbols your C compiler and preprocessor define...
</code></pre>
<p> will probably fail with error messages like </p>
<pre><code>    CC-20 cc: ERROR File = try.c, Line = 3
      The identifier &quot;bad&quot; is undefined.
      bad switch yylook 79bad switch yylook 79bad switch yylook 79bad switch yylook 79#ifdef A29K
      ^
    CC-65 cc: ERROR File = try.c, Line = 3
      A semicolon is expected at this point.
</code></pre>
<p> This is caused by a bug in the awk utility of UNICOS/mk. You can ignore the error, but it does cause a slight problem: you cannot fully benefit from the h2ph utility (see h2ph) that can be used to convert C headers to Perl libraries, mainly used to be able to access from Perl the constants defined using C preprocessor, cpp. Because of the above error, parts of the converted headers will be invisible. Luckily, these days the need for h2ph is rare. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> If building Perl with interpreter threads (ithreads), the <code>getgrent()</code>, <code>getgrnam()</code>, and <code>getgrgid()</code> functions cannot return the list of the group members due to a bug in the multithreaded support of UNICOS/mk. What this means is that in list context the functions will return only three values, not four. </p>
 </dd></dl>
<font SIZE="-1"></font><h3>UTS</h3>
<p> There are a few known test failures. (<code>Note:</code> the relevant information was available in <i></i><font SIZE="-1"><i>README</i></font><i>.uts</i> until support for <font SIZE="-1">UTS</font> was removed in Perl v5.18.0)  </p>
<font SIZE="-1"></font><h3>VOS (Stratus)</h3>
<p> When Perl is built using the native build process on <font SIZE="-1">VOS</font> Release 14.5.0 and <font SIZE="-1">GNU C<font SIZE="-2">++</font>/GNU</font> Tools 2.0.1, all attempted tests either pass or result in <font SIZE="-1">TODO</font> (ignored) failures.  </p>
<font SIZE="-1"></font><h3>VMS</h3>
<p> There should be no reported test failures with a default configuration, though there are a number of tests marked <font SIZE="-1">TODO</font> that point to areas needing further debugging and/or porting work.  </p>
<h3>Win32</h3>
<p> In multi-CPU boxes, there are some problems with the I/O buffering: some output may appear twice.  </p>
<h3>XML::Parser not working</h3>
<p> Use XML::Parser 2.31 or later.  </p>
<font SIZE="-1"></font><h3>z/OS ( OS/390 )</h3>
<p> z/OS has rather many test failures but the situation is actually much better than it was in 5.6.0; it&#8217;s just that so many new modules and tests have been added. </p>
<pre><code> Failed Test Stat Wstat Total Fail Failed List of Failed
 ---------------------------------------------------------------------------
 ../ext/Data/Dumper/t/dumper.t 357 8 2.24% 311 314 325 327
                                                              331 333 337 339
 ../ext/IO/lib/IO/t/io_unix.t 5 4 80.00% 2-5
 ../ext/Storable/t/downgrade.t 12 3072 169 12 7.10% 14-15 46-47 78-79
                                                              110-111 150 161
 ../lib/ExtUtils/t/Constant.t 121 30976 48 48 100.00% 1-48
 ../lib/ExtUtils/t/Embed.t 9 9 100.00% 1-9
 op/pat.t 922 7 0.76% 665 776 785 832-
                                                              834 845
 op/sprintf.t 224 3 1.34% 98 100 136
 op/tr.t 97 5 5.15% 63 71-74
 uni/fold.t 780 6 0.77% 61 169 196 661
                                                              710-711
</code></pre>
<p> The failures in dumper.t and downgrade.t are problems in the tests, those in io_unix and sprintf are problems in the <font SIZE="-1">USS</font> (<font SIZE="-1">UDP</font> sockets and printf formats). The pat, tr, and fold failures are genuine Perl problems caused by <font SIZE="-1">EBCDIC</font> (and in the pat and fold cases, combining that with Unicode). The Constant and Embed are probably problems in the tests (since they test Perl&#8217;s ability to build extensions, and that seems to be working reasonably well.)  </p>
<font SIZE="-1"></font><h3>Unicode Support on EBCDIC Still Spotty</h3>
<p> Though mostly working, Unicode support still has problem spots on <font SIZE="-1">EBCDIC</font> platforms. One such known spot are the <code>&quot;\p{}&quot;</code> and <code>&quot;\P{}&quot;</code> regular expression constructs for code points less than 256: the <code>&quot;pP&quot;</code> are testing for Unicode code points, not knowing about <font SIZE="-1">EBCDIC.</font>  </p>
<h3>Seen In Perl 5.7 But Gone Now</h3>
<p> <code>&quot;Time::Piece&quot;</code> (previously known as <code>&quot;Time::Object&quot;</code>) was removed because it was felt that it didn&#8217;t have enough value in it to be a core module. It is still a useful module, though, and is available from the <font SIZE="-1">CPAN.</font> </p>
<p> Perl 5.8 unfortunately does not build anymore on AmigaOS; this broke accidentally at some point. Since there are not that many Amiga developers available, we could not get this fixed and tested in time for 5.8.0. Perl 5.6.1 still works for AmigaOS (as does the 5.7.2 development release). </p>
<p> The <code>&quot;PerlIO::Scalar&quot;</code> and <code>&quot;PerlIO::Via&quot;</code> (capitalised) were renamed as <code>&quot;PerlIO::scalar&quot;</code> and <code>&quot;PerlIO::via&quot;</code> (all lowercase) just before 5.8.0. The main rationale was to have all core PerlIO layers to have all lowercase names. The ``plugins&#8217;&#8216; are named as usual, for example <code>&quot;PerlIO::via::QuotedPrint&quot;</code>. </p>
<p> The <code>&quot;threads::shared::queue&quot;</code> and <code>&quot;threads::shared::semaphore&quot;</code> were renamed as <code>&quot;Thread::Queue&quot;</code> and <code>&quot;Thread::Semaphore&quot;</code> just before 5.8.0. The main rationale was to have thread modules to obey normal naming, <code>&quot;Thread::&quot;</code> (the <code>&quot;threads&quot;</code> and <code>&quot;threads::shared&quot;</code> themselves are more pragma-like, they affect compile-time, so they stay lowercase).  </p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://bugs.perl.org/">http://bugs.perl.org/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.com/">http://www.perl.com/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <code>&quot;perl -V&quot;</code>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team.  </p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information.  </p>
<h2>HISTORY</h2>
<p> Written by Jarkko Hietaniemi &lt;<i>jhi [at] iki.fi</i>&gt;. </p>
