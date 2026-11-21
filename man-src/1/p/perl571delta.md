---
title: "perl571delta(1)"
name: "perl571delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl571delta/"
description: "perl571delta – what’s new for perl v5.7.1"
---

<h2 class="name">NAME</h2>
<p> perl571delta &#8211; what&#8217;s new for perl v5.7.1 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.7.0 release and the 5.7.1 release. </p>
<p> (To view the differences between the 5.6.0 release and the 5.7.0 release, see perl570delta.)</p>
<h2>Security Vulnerability Closed</h2>
<p> (This change was already made in 5.7.0 but bears repeating here.) </p>
<p> A potential security vulnerability in the optional suidperl component of Perl was identified in August 2000. suidperl is neither built nor installed by default. As of April 2001 the only known vulnerable platform is Linux, most likely all Linux distributions. <font SIZE="-1">CERT</font> and various vendors and distributors have been alerted about the vulnerability. See <a rel="nofollow" href="http://www.cpan.org/src/5.0/sperl-2000-08-05/sperl-2000-08-05.txt">http://www.cpan.org/src/5.0/sperl-2000-08-05/sperl-2000-08-05.txt</a> for more information. </p>
<p> The problem was caused by Perl trying to report a suspected security exploit attempt using an external program, /bin/mail. On Linux platforms the /bin/mail program had an undocumented feature which when combined with suidperl gave access to a root shell, resulting in a serious compromise instead of reporting the exploit attempt. If you don&#8217;t have /bin/mail, or if you have &#8216;safe setuid scripts&#8217;, or if suidperl is not installed, you are safe. </p>
<p> The exploit attempt reporting feature has been completely removed from all the Perl 5.7 releases (and will be gone also from the maintenance release 5.6.1), so that particular vulnerability isn&#8217;t there anymore. However, further security vulnerabilities are, unfortunately, always possible. The suidperl code is being reviewed and if deemed too risky to continue to be supported, it may be completely removed from future releases. In any case, suidperl should only be used by security experts who know exactly what they are doing and why they are using suidperl instead of some other solution such as sudo ( see <a rel="nofollow" href="http://www.courtesan.com/sudo/">http://www.courtesan.com/sudo/</a> ).</p>
<h2>Incompatible Changes</h2>
<dl>
<dt>&bull;</dt>
<dd> Although &#8220;you shouldn&#8217;t do that&#8221;, it was possible to write code that depends on Perl&#8217;s hashed key order (Data::Dumper does this). The new algorithm &#8220;One-at-a-Time&#8221; produces a different hashed key order. More details are in &#8220;Performance Enhancements&#8221;.</dd>
<dt>&bull;</dt>
<dd> The list of filenames from <i>glob()</i> (or &lt;&#8230;&gt;) is now by default sorted alphabetically to be csh-compliant. (<i>bsd_glob()</i> does still sort platform natively, <font SIZE="-1">ASCII</font> or <font SIZE="-1">EBCDIC</font>, unless <font SIZE="-1">GLOB_ALPHASORT</font> is specified.)</dd></dl>
<h2>Core Enhancements</h2>
<h3><font SIZE="-1">AUTOLOAD</font> Is Now Lvaluable</h3>
<p> <font SIZE="-1">AUTOLOAD</font> is now lvaluable, meaning that you can add the :lvalue attribute to <font SIZE="-1">AUTOLOAD</font> subroutines and you can assign to the <font SIZE="-1">AUTOLOAD</font> return value.</p>
<h3>PerlIO is Now The Default</h3>
<dl>
<dt>&bull;</dt>
<dd> <font SIZE="-1">IO</font> is now by default done via PerlIO rather than system&#8217;s &#8220;stdio&#8221;. PerlIO allows &#8220;layers&#8221; to be &#8220;pushed&#8221; onto a file handle to alter the handle&#8217;s behaviour. Layers can be specified at open time via 3-arg form of open: </dd>
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
<dt>&bull;</dt>
<dd> File handles can be marked as accepting Perl&#8217;s internal encoding of Unicode (<font SIZE="-1">UTF-8</font> or UTF-EBCDIC depending on platform) by a pseudo layer &#8220;:utf8&#8221; : </dd>
<pre>
   open($fh,&quot;&gt;:utf8&quot;,&quot;Uni.txt&quot;);
</pre>
<p> Note for <font SIZE="-1">EBCDIC</font> users: the pseudo layer &#8220;:utf8&#8221; is erroneously named for you since it&#8217;s not <font SIZE="-1">UTF-8</font> what you will be getting but instead UTF-EBCDIC. See perlunicode, utf8, and <a rel="nofollow" href="http://www.unicode.org/unicode/reports/tr16/">http://www.unicode.org/unicode/reports/tr16/</a> for more information. In future releases this naming may change.</p>
<dt>&bull;</dt>
<dd> File handles can translate character encodings from/to Perl&#8217;s internal Unicode form on read/write via the &#8220;:<i>encoding()</i>&#8221; layer.</dd>
<dt>&bull;</dt>
<dd> File handles can be opened to &#8220;in memory&#8221; files held in Perl scalars via: </dd>
<pre>
   open($fh,'&gt;', \$variable) || ...
</pre>
<dt>&bull;</dt>
<dd> Anonymous temporary files are available without need to &#8216;use FileHandle&#8217; or other module via </dd>
<pre>
   open($fh,&quot;+&gt;&quot;, undef) || ...
</pre>
<p> That is a literal undef, not an undefined value.</p>
<dt>&bull;</dt>
<dd> The list form of <tt>&quot;open&quot;</tt> is now implemented for pipes (at least on Unix): </dd>
<pre>
   open($fh,&quot;-|&quot;, 'cat', '/etc/motd')
</pre>
<p> creates a pipe, and runs the equivalent of exec(&#8216;cat&#8217;, &#8216;/etc/motd&#8217;) in the child process.</p>
<dt>&bull;</dt>
<dd> The following builtin functions are now overridable: <i>chop()</i>, <i>chomp()</i>, <i>each()</i>, <i>keys()</i>, <i>pop()</i>, <i>push()</i>, <i>shift()</i>, <i>splice()</i>, <i>unshift()</i>.</dd>
<dt>&bull;</dt>
<dd> Formats now support zero-padded decimal fields.</dd>
<dt>&bull;</dt>
<dd> Perl now tries internally to use integer values in numeric conversions and basic arithmetics (+ &#8211; * /) if the arguments are integers, and tries also to keep the results stored internally as integers. This change leads into often slightly faster and always less lossy arithmetics. (Previously Perl always preferred floating point numbers in its math.)</dd>
<dt>&bull;</dt>
<dd> The <i>printf()</i> and <i>sprintf()</i> now support parameter reordering using the <tt>&quot;%\d+\$&quot;</tt> and <tt>&quot;*\d+\$&quot;</tt> syntaxes. For example </dd>
<pre>
    print &quot;%2\$s %1\$s
&quot;, &quot;foo&quot;, &quot;bar&quot;;
</pre>
<p> will print &#8220;bar foo
&#8221;; This feature helps in writing internationalised software.</p>
<dt>&bull;</dt>
<dd> Unicode in general should be now much more usable. Unicode can be used in hash keys, Unicode in regular expressions should work now, Unicode in tr/// should work now (though tr/// seems to be a particularly tricky to get right, so you have been warned)</dd>
<dt>&bull;</dt>
<dd> The Unicode Character Database coming with Perl has been upgraded to Unicode 3.1. For more information, see <a rel="nofollow" href="http://www.unicode.org/">http://www.unicode.org/</a> , and <a rel="nofollow" href="http://www.unicode.org/unicode/reports/tr27/">http://www.unicode.org/unicode/reports/tr27/</a> </dd>
<p> For developers interested in enhancing Perl&#8217;s Unicode capabilities: almost all the <font SIZE="-1">UCD</font> files are included with the Perl distribution in the lib/unicode subdirectory. The most notable omission, for space considerations, is the Unihan database.</p>
<dt>&bull;</dt>
<dd> The Unicode character classes \p{Blank} and \p{SpacePerl} have been added. &#8220;Blank&#8221; is like C <i>isblank()</i>, that is, it contains only &#8220;horizontal whitespace&#8221; (the space character is, the newline isn&#8217;t), and the &#8220;SpacePerl&#8221; is the Unicode equivalent of <tt>&quot;\s&quot;</tt> (\p{Space} isn&#8217;t, since that includes the vertical tabulator character, whereas <tt>&quot;\s&quot;</tt> doesn&#8217;t.)</dd></dl>
<h3>Signals Are Now Safe</h3>
<p> Perl used to be fragile in that signals arriving at inopportune moments could corrupt Perl&#8217;s internal state.</p>
<h2>Modules and Pragmata</h2>
<h3>New Modules</h3>
<dl>
<dt>&bull;</dt>
<dd> B::Concise, by Stephen McCamant, is a new compiler backend for walking the Perl syntax tree, printing concise info about ops. The output is highly customisable. </dd>
<p> See B::Concise for more information.</p>
<dt>&bull;</dt>
<dd> Class::ISA, by Sean Burke, for reporting the search path for a class&#8217;s <font SIZE="-1">ISA</font> tree, has been added. </dd>
<p> See Class::ISA for more information.</p>
<dt>&bull;</dt>
<dd> Cwd has now a split personality: if possible, an extension is used, (this will hopefully be both faster and more secure and robust) but if not possible, the familiar Perl library implementation is used.</dd>
<dt>&bull;</dt>
<dd> Digest, a frontend module for calculating digests (checksums), from Gisle Aas, has been added. </dd>
<p> See Digest for more information.</p>
<dt>&bull;</dt>
<dd> Digest::MD5 for calculating <font SIZE="-1">MD5</font> digests (checksums), by Gisle Aas, has been added. </dd>
<pre><code>
use Digest::MD5 'md5_hex';
$digest = md5_hex("Thirsty Camel");
print $digest, "
";
# 01d19d9d2045e005c3f1b80e8b164de1
</code></pre>
<p> <font SIZE="-1">NOTE:</font> the <font SIZE="-1">MD5</font> backward compatibility module is deliberately not included since its use is discouraged. </p>
<p> See Digest::MD5 for more information.</p>
<dt>&bull;</dt>
<dd> Encode, by Nick Ing-Simmons, provides a mechanism to translate between different character encodings. Support for Unicode, ISO-8859-*, <font SIZE="-1">ASCII</font>, CP*, <font SIZE="-1">KOI8-R</font>, and three variants of <font SIZE="-1">EBCDIC</font> are compiled in to the module. Several other encodings (like Japanese, Chinese, and MacIntosh encodings) are included and will be loaded at runtime. </dd>
<p> Any encoding supported by Encode module is also available to the &#8220;:<i>encoding()</i>&#8221; layer if PerlIO is used. </p>
<p> See Encode for more information.</p>
<dt>&bull;</dt>
<dd> Filter::Simple is an easy-to-use frontend to Filter::Util::Call, from Damian Conway. </dd>
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
<p> See Filter::Simple for more information.</p>
<dt>&bull;</dt>
<dd> Filter::Util::Call, by Paul Marquess, provides you with the framework to write <i>Source Filters</i> in Perl. For most uses the frontend Filter::Simple is to be preferred. See Filter::Util::Call for more information.</dd>
<dt>&bull;</dt>
<dd> Locale::Constants, Locale::Country, Locale::Currency, and Locale::Language, from Neil Bowers, have been added. They provide the codes for various locale standards, such as &#8220;fr&#8221; for France, &#8220;usd&#8221; for <font SIZE="-1">US</font> Dollar, and &#8220;jp&#8221; for Japanese. </dd>
<p>use Locale::Country;<br />
$country = code2country(&#8216;jp&#8217;);<br />
#$country gets &#8216;Japan&#8217; $code = country2code(&#8216;Norway&#8217;);<br />
#$code gets &#8216;no&#8217;</p>
<p> See Locale::Constants, Locale::Country, Locale::Currency, and Locale::Language for more information.</p>
<dt>&bull;</dt>
<dd> MIME::Base64, by Gisle Aas, allows you to encode data in base64. </dd>
<p>use MIME::Base64;<br />
$encoded = encode_base64(&#8216;Aladdin:open sesame&#8217;);<br />
$decoded = decode_base64($encoded);<br />
print $encoded, &#8220;
&#8221;;<br />
#&#8221;QWxhZGRpbjpvcGVuIHNlc2FtZQ==&#8221;</p>
<p> See MIME::Base64 for more information.</p>
<dt>&bull;</dt>
<dd> MIME::QuotedPrint, by Gisle Aas, allows you to encode data in quoted-printable encoding. </dd>
<p>use MIME::QuotedPrint;<br />
$encoded = encode_qp(&#8220;Smiley in Unicode: \x{263a}&quot;); $decoded = decode_qp($encoded); print $encoded, &quot;\n&quot;; # &quot;Smiley in Unicode: =263A&quot; </code></pre>
 </p>
<p> MIME::QuotedPrint has been enhanced to provide the basic methods necessary to use it with PerlIO::Via as in : </p>
<pre><code>    use MIME::QuotedPrint;
    open($fh,&quot;&gt;Via(MIME::QuotedPrint)&quot;,$path)
</code></pre>
<p> See MIME::QuotedPrint for more information. </p>
<dt>&bull;</dt>
<dd> <p> PerlIO::Scalar, by Nick Ing-Simmons, provides the implementation of <font SIZE="-1">IO</font> to ``in memory&#8217;&#8216; Perl scalars as discussed above. It also serves as an example of a loadable layer. Other future possibilities include PerlIO::Array and PerlIO::Code. See PerlIO::Scalar for more information. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> PerlIO::Via, by Nick Ing-Simmons, acts as a PerlIO layer and wraps PerlIO layer functionality provided by a class (typically implemented in perl code). </p>
<pre><code>    use MIME::QuotedPrint;
    open($fh,&quot;&gt;Via(MIME::QuotedPrint)&quot;,$path)
</code></pre>
<p> This will automatically convert everything output to <code>$fh</code> to Quoted-Printable. See PerlIO::Via for more information. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pod::Text::Overstrike, by Joe Smith, has been added. It converts <font SIZE="-1">POD</font> data to formatted overstrike text. See Pod::Text::Overstrike for more information. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Switch from Damian Conway has been added. Just by saying </p>
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
<p> See Switch for more information. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Text::Balanced from Damian Conway has been added, for extracting delimited text sequences from strings. </p>
<pre><code>    use Text::Balanced 'extract_delimited';
    ($a, $b) = extract_delimited(&quot;'never say never', he never said&quot;, &quot;'&quot;, '');
</code></pre>
<p> <code>$a</code> will be ``&#8216;never say never&#8217;&#8216;&#8216;, <code>$b</code> will be &#8216;, he never said&#8217;. </p>
<p> In addition to <i>extract_delimited()</i> there are also <i>extract_bracketed()</i>, <i>extract_quotelike()</i>, <i>extract_codeblock()</i>, <i>extract_variable()</i>, <i>extract_tagged()</i>, <i>extract_multiple()</i>, <i>gen_delimited_pat()</i>, and <i>gen_extract_tagged()</i>. With these you can implement rather advanced parsing algorithms. See Text::Balanced for more information. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Tie::RefHash::Nestable, by Edward Avis, allows storing hash references (unlike the standard Tie::RefHash) The module is contained within Tie::RefHash. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> XS::Typemap, by Tim Jenness, is a test extension that exercises <font SIZE="-1">XS</font> typemaps. Nothing gets installed but for extension writers the code is worth studying. </p>
 </dd></dl>
<h3>Updated And Improved Modules and Pragmata</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> B::Deparse should be now more robust. It still far from providing a full round trip for any random piece of Perl code, though, and is under active development: expect more robustness in 5.7.2. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Class::Struct can now define the classes in compile time. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Math::BigFloat has undergone much fixing, and in addition the <i>fmod()</i> function now supports modulus operations. </p>
<p> ( The fixed Math::BigFloat module is also available in <font SIZE="-1">CPAN</font> for those who can&#8217;t upgrade their Perl: <a rel="nofollow" href="http://www.cpan.org/authors/id/J/JP/JPEACOCK/">http://www.cpan.org/authors/id/J/JP/JPEACOCK/</a> ) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Devel::Peek now has an interface for the Perl memory statistics (this works only if you are using perl&#8217;s malloc, and if you have compiled with debugging). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> IO::Socket has now <i>atmark()</i> method, which returns true if the socket is positioned at the out-of-band mark. The method is also exportable as a <i>sockatmark()</i> function. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> IO::Socket::INET has support for ReusePort option (if your platform supports it). The Reuse option now has an alias, ReuseAddr. For clarity you may want to prefer ReuseAddr. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Net::Ping has been enhanced. There is now ``external&#8217;&#8216; protocol which uses Net::Ping::External module which runs external <i><a href="/docs/linux/man/1-ping/">ping</a></i>(1) and parses the output. An alpha version of Net::Ping::External is available in <font SIZE="-1">CPAN</font> and in 5.7.2 the Net::Ping::External may be integrated to Perl. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;open&quot;</code> pragma allows layers other than ``:raw&#8217;&#8216; and ``:crlf&#8217;&#8216; when using PerlIO. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>POSIX::sigaction()</i> is now much more flexible and robust. You can now install coderef handlers, &#8216;<font SIZE="-1">DEFAULT</font>&#8216;, and &#8216;<font SIZE="-1">IGNORE</font>&#8216; handlers, installing new handlers was not atomic. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The Test module has been significantly enhanced. Its use is greatly recommended for module writers. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The utf8:: name space (as in the pragma) provides various Perl-callable functions to provide low level access to Perl&#8217;s internal Unicode representation. At the moment only <i>length()</i> has been implemented. </p>
 </dd></dl>
<p> The following modules have been upgraded from the versions at <font SIZE="-1">CPAN:</font> <font SIZE="-1">CPAN</font>, <font SIZE="-1">CGI</font>, DB_File, File::Temp, Getopt::Long, Pod::Man, Pod::Text, Storable, Text-Tabs+Wrap.  </p>
<h2>Performance Enhancements</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> Hashes now use Bob Jenkins ``One-at-a-Time&#8217;&#8216; hashing key algorithm ( <a rel="nofollow" href="http://burtleburtle.net/bob/hash/doobs.html">http://burtleburtle.net/bob/hash/doobs.html</a> ). This algorithm is reasonably fast while producing a much better spread of values than the old hashing algorithm (originally by Chris Torek, later tweaked by Ilya Zakharevich). Hash values output from the algorithm on a hash of all 3-char printable <font SIZE="-1">ASCII</font> keys comes much closer to passing the <font SIZE="-1">DIEHARD</font> random number generation tests. According to perlbench, this change has not affected the overall speed of Perl. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>unshift()</i> should now be noticeably faster. </p>
 </dd></dl>
<h2>Utility Changes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> h2xs now produces template <font SIZE="-1">README</font>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> s2p has been completely rewritten in Perl. (It is in fact a full implementation of sed in Perl.) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> xsubpp now supports <font SIZE="-1">OUT</font> keyword. </p>
 </dd></dl>
<h2>New Documentation</h2>
<h3>perlclib</h3>
<p> Internal replacements for standard C library functions. (Interesting only for extension writers and Perl core hackers.)  </p>
<h3>perliol</h3>
<p> Internals of PerlIO with layers.  </p>
<font SIZE="-1"></font><h3>README .aix</h3>
<p> Documentation on compiling Perl on <font SIZE="-1">AIX</font> has been added. <font SIZE="-1">AIX</font> has several different C compilers and getting the right patch level is essential. On install <font SIZE="-1">README</font>.aix will be installed as perlaix.  </p>
<font SIZE="-1"></font><h3>README .bs2000</h3>
<p> Documentation on compiling Perl on the POSIX-BC platform (an <font SIZE="-1">EBCDIC</font> mainframe environment) has been added. </p>
<p> This was formerly known as <font SIZE="-1">README</font>.posix-bc but the name was considered to be too confusing (it has nothing to do with the <font SIZE="-1">POSIX</font> module or the <font SIZE="-1">POSIX</font> standard). On install <font SIZE="-1">README</font>.bs2000 will be installed as perlbs2000.  </p>
<font SIZE="-1"></font><h3>README .macos</h3>
<p> In perl 5.7.1 (and in the 5.6.1) the MacPerl sources have been synchronised with the standard Perl sources. To compile MacPerl some additional steps are required, and this file documents those steps. On install <font SIZE="-1">README</font>.macos will be installed as perlmacos.  </p>
<font SIZE="-1"></font><h3>README .mpeix</h3>
<p> The <font SIZE="-1">README</font>.mpeix has been podified, which means that this information about compiling and using Perl on the MPE/iX miniframe platform will be installed as perlmpeix.  </p>
<font SIZE="-1"></font><h3>README .solaris</h3>
<p> <font SIZE="-1">README</font>.solaris has been created and Solaris wisdom from elsewhere in the Perl documentation has been collected there. On install <font SIZE="-1">README</font>.solaris will be installed as perlsolaris.  </p>
<font SIZE="-1"></font><h3>README .vos</h3>
<p> The <font SIZE="-1">README</font>.vos has been podified, which means that this information about compiling and using Perl on the Stratus <font SIZE="-1">VOS</font> miniframe platform will be installed as perlvos.  </p>
<h3>Porting/repository.pod</h3>
<p> Documentation on how to use the Perl source repository has been added.  </p>
<h2>Installation and Configuration Improvements</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> Because PerlIO is now the default on most platforms, ``-perlio&#8217;&#8216; doesn&#8217;t get appended to the <code>$Config</code>{archname} (also known as $^O) anymore. Instead, if you explicitly choose not to use perlio (Configure command line option -Uuseperlio), you will get ``-stdio&#8217;&#8216; appended. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Another change related to the architecture name is that ``-64all&#8217;&#8216; (-Duse64bitall, or ``maximally 64-bit&#8217;&#8216;) is appended only if your pointers are 64 bits wide. (To be exact, the use64bitall is ignored.) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">APPLLIB_EXP</font>, a less-know configuration-time definition, has been documented. It can be used to prepend site-specific directories to Perl&#8217;s default search path (@INC), see <font SIZE="-1">INSTALL</font> for information. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Building Berkeley <font SIZE="-1">DB3</font> for compatibility modes for <font SIZE="-1">DB</font>, <font SIZE="-1">NDBM</font>, and <font SIZE="-1">ODBM</font> has been documented in <font SIZE="-1">INSTALL</font>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> If you are on <font SIZE="-1">IRIX</font> or Tru64 platforms, new profiling/debugging options have been added, see perlhack for more information about pixie and Third Degree. </p>
 </dd></dl>
<h3>New Or Improved Platforms</h3>
<p> For the list of platforms known to support Perl, see ``Supported Platforms&#8217;&#8216; in perlport. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">AIX</font> dynamic loading should be now better supported. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> After a long pause, AmigaOS has been verified to be happy with Perl. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">EBCDIC</font> platforms (z/OS, also known as <font SIZE="-1">OS/390</font>, POSIX-BC, and <font SIZE="-1">VM/ESA</font>) have been regained. Many test suite tests still fail and the co-existence of Unicode and <font SIZE="-1">EBCDIC</font> isn&#8217;t quite settled, but the situation is much better than with Perl 5.6. See perlos390, perlbs2000 (for POSIX-BC), and perlvmesa for more information. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Building perl with -Duseithreads or -Duse5005threads now works under HP-UX 10.20 (previously it only worked under 10.30 or later). You will need a thread library package installed. See <font SIZE="-1">README</font>.hpux. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Mac <font SIZE="-1">OS</font> Classic (MacPerl has of course been available since perl 5.004 but now the source code bases of standard Perl and MacPerl have been synchronised) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">NCR</font> MP-RAS is now supported. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> NonStop-UX is now supported. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Amdahl <font SIZE="-1">UTS</font> is now supported. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> z/OS (formerly known as <font SIZE="-1">OS/390</font>, formerly known as <font SIZE="-1">MVS</font> <font SIZE="-1">OE</font>) has now support for dynamic loading. This is not selected by default, however, you must specify -Dusedl in the arguments of Configure. </p>
 </dd></dl>
<h3>Generic Improvements</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Configure no longer includes the <font SIZE="-1">DBM</font> libraries (dbm, gdbm, db, ndbm) when building the Perl binary. The only exception to this is SunOS 4.x, which needs them. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Some new Configure symbols, useful for extension writers: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>d_cmsghdr</dt>
<dd> <p> For struct cmsghdr. </p>
 </dd>
<dt>d_fcntl_can_lock</dt>
<dd> <p> Whether <i>fcntl()</i> can be used for file locking. </p>
 </dd>
<dt>d_fsync</dt>
<dd>  </dd>
<dt>d_getitimer</dt>
<dd>  </dd>
<dt>d_getpagsz</dt>
<dd> <p> For <i>getpagesize()</i>, though you should prefer POSIX::sysconf(_SC_PAGE_SIZE)) </p>
 </dd>
<dt>d_msghdr_s</dt>
<dd> <p> For struct msghdr. </p>
 </dd>
<dt>need_va_copy</dt>
<dd> <p> Whether one needs to use <i>Perl_va_copy()</i> to copy varargs. </p>
 </dd>
<dt>d_readv</dt>
<dd>  </dd>
<dt>d_recvmsg</dt>
<dd>  </dd>
<dt>d_sendmsg</dt>
<dd>  </dd>
<dt>sig_size</dt>
<dd> <p> The number of elements in an array needed to hold all the available signals. </p>
 </dd>
<dt>d_sockatmark</dt>
<dd>  </dd>
<dt>d_strtoq</dt>
<dd>  </dd>
<dt>d_u32align</dt>
<dd> <p> Whether one needs to access character data aligned by U32 sized pointers. </p>
 </dd>
<dt>d_ualarm</dt>
<dd>  </dd>
<dt>d_usleep</dt>
<dd>  </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>&bull;</dt>
<dd> <p> Removed Configure symbols: the <font SIZE="-1">PDP-11</font> memory model settings: huge, large, medium, models. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">SOCKS</font> support is now much more robust. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> If your file system supports symbolic links you can build Perl outside of the source directory by </p>
<pre><code>        mkdir perl/build/directory
        cd perl/build/directory
        sh /path/to/perl/source/Configure -Dmksymlinks ...
</code></pre>
<p> This will create in perl/build/directory a tree of symbolic links pointing to files in /path/to/perl/source. The original files are left unaffected. After Configure has finished you can just say </p>
<pre><code>        make all test
</code></pre>
<p> and Perl will be built and tested, all in perl/build/directory. </p>
 </dd></dl>
<h2>Selected Bug Fixes</h2>
<p> Numerous memory leaks and uninitialized memory accesses have been hunted down. Most importantly anonymous subs used to leak quite a bit. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> chop(@list) in list context returned the characters chopped in reverse order. This has been reversed to be in the right order. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The order of DESTROYs has been made more predictable. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>mkdir()</i> now ignores trailing slashes in the directory name, as mandated by <font SIZE="-1">POSIX</font>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Attributes (like :shared) didn&#8217;t work with <i>our()</i>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <font SIZE="-1">PERL5OPT</font> environment variable (for passing command line arguments to Perl) didn&#8217;t work for more than a single group of options. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The tainting behaviour of <i>sprintf()</i> has been rationalized. It does not taint the result of floating point formats anymore, making the behaviour consistent with that of string interpolation. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> All but the first argument of the <font SIZE="-1">IO</font> <i>syswrite()</i> method are now optional. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Tie::ARRAY <font SIZE="-1">SPLICE</font> method was broken. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>vec()</i> now tries to work with characters &lt;= 255 when possible, but it leaves higher character values in place. In that case, if <i>vec()</i> was used to modify the string, it is no longer considered to be utf8-encoded. </p>
 </dd></dl>
<h3>Platform Specific Changes and Fixes</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Linux previously had problems related to sockaddrlen when using <i>accept()</i>, <i>revcfrom()</i> (in Perl: <i>recv()</i>), <i>getpeername()</i>, and <i>getsockname()</i>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Previously DYNIX/ptx had problems in its Configure probe for non-blocking I/O. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Windows </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Borland C<font SIZE="-2">++</font> v5.5 is now a supported compiler that can build Perl. However, the generated binaries continue to be incompatible with those generated by the other supported compilers (<font SIZE="-1">GCC</font> and Visual C<font SIZE="-2">++</font>). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>Win32::GetCwd()</i> correctly returns C:\ instead of C: when at the drive root. Other bugs in <i>chdir()</i> and <i>Cwd::cwd()</i> have also been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Duping socket handles with open(F, ``&gt;&amp;MYSOCK&#8217;&#8216;) now works under Windows 9x. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">HTML</font> files will be installed in c:\perl\html instead of c:\perl\lib\pod\html </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The makefiles now provide a single switch to bulk-enable all the features enabled in ActiveState ActivePerl (a popular binary distribution). </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
</dl>
<h2>New or Changed Diagnostics</h2>
<p> Two new debugging options have been added: if you have compiled your Perl with debugging, you can use the -DT and -DR options to trace tokenising and to add reference counts to displaying variables, respectively. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> If an attempt to use a (non-blessed) reference as an array index is made, a warning is given. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;push @a;&quot;</code> and <code>&quot;unshift @a;&quot;</code> (with no values to push or unshift) now give a warning. This may be a problem for generated and eval&#8217;ed code. </p>
 </dd></dl>
<h2>Changed Internals</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> Some new APIs: <i>ptr_table_clear()</i>, <i>ptr_table_free()</i>, <i>sv_setref_uv()</i>. For the full list of the available APIs see perlapi. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> dTHR and djSP have been obsoleted; the former removed (because it&#8217;s a no-op) and the latter replaced with dSP. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl now uses system malloc instead of Perl malloc on all 64-bit platforms, and even in some not-always-64-bit platforms like <font SIZE="-1">AIX</font>, <font SIZE="-1">IRIX</font>, and Solaris. This change breaks backward compatibility but Perl&#8217;s malloc has problems with large address spaces and also the speed of vendors&#8217; malloc is generally better in large address space machines (Perl&#8217;s malloc is mostly tuned for space). </p>
 </dd></dl>
<h2>New Tests</h2>
<p> Many new tests have been added. The most notable is probably the lib/1_compile: it is very notable because running it takes quite a long time. It test compiles all the Perl modules in the distribution. Please be patient.  </p>
<h2>Known Problems</h2>
<p> Note that unlike other sections in this document (which describe changes since 5.7.0) this section is cumulative containing known problems for all the 5.7 releases.  </p>
<font SIZE="-1"></font><h3>AIX vac 5.0.0.0 May Produce Buggy Code For Perl</h3>
<p> The <font SIZE="-1">AIX</font> C compiler vac version 5.0.0.0 may produce buggy code, resulting in few random tests failing, but when the failing tests are run by hand, they succeed. We suggest upgrading to at least vac version 5.0.1.0, that has been known to compile Perl correctly. ``lslpp -L|grep vac.C&#8217;&#8216; will tell you the vac version.  </p>
<h3>lib/ftmp-security tests warn 'system possibly insecure'</h3>
<p> Don&#8217;t panic. Read <font SIZE="-1">INSTALL</font> &#8216;make test&#8217; section instead.  </p>
<h3>lib/io_multihomed Fails In LP64-Configured HP-UX</h3>
<p> The lib/io_multihomed test may hang in HP-UX if Perl has been configured to be 64-bit. Because other 64-bit platforms do not hang in this test, HP-UX is suspect. All other tests pass in 64-bit HP-UX. The test attempts to create and connect to ``multihomed&#8217;&#8216; sockets (sockets which have multiple <font SIZE="-1">IP</font> addresses).  </p>
<h3>Test lib/posix Subtest 9 Fails In LP64-Configured HP-UX</h3>
<p> If perl is configured with -Duse64bitall, the successful result of the subtest 10 of lib/posix may arrive before the successful result of the subtest 9, which confuses the test harness so much that it thinks the subtest 9 failed.  </p>
<h3>lib/b test 19</h3>
<p> The test fails on various platforms (<font SIZE="-1">PA64</font> and <font SIZE="-1">IA64</font> are known), but the exact cause is still being investigated.  </p>
<h3>Linux With Sfio Fails op/misc Test 48</h3>
<p> No known fix.  </p>
<font SIZE="-1"></font><h3>sigaction test 13 in VMS</h3>
<p> The test is known to fail; whether it&#8217;s because of <font SIZE="-1">VMS</font> of because of faulty test is not known.  </p>
<h3>sprintf tests 129 and 130</h3>
<p> The op/sprintf tests 129 and 130 are known to fail on some platforms. Examples include any platform using sfio, and Compaq/Tandem&#8217;s NonStop-UX. The failing platforms do not comply with the <font SIZE="-1">ANSI</font> C Standard, line 19ff on page 134 of <font SIZE="-1">ANSI</font> X3.159 1989 to be exact. (They produce something else than ``1&#8217;&#8216; and ``-1&#8217;&#8216; when formatting 0.6 and -0.6 using the printf format ``%.0f&#8217;&#8216;, most often they produce ``0&#8217;&#8216; and ``-0&#8217;&#8216;.)  </p>
<h3>Failure of Thread tests</h3>
<p> The subtests 19 and 20 of lib/thr5005.t test are known to fail due to fundamental problems in the 5.005 threading implementation. These are not new failures---Perl 5.005_0x has the same bugs, but didn&#8217;t have these tests. (Note that support for 5.005-style threading remains experimental.)  </p>
<h3>Localising a Tied Variable Leaks Memory</h3>
<pre><code>    use Tie::Hash;
    tie my %tie_hash =&gt; 'Tie::StdHash';
    ...
    local($tie_hash{Foo}) = 1; # leaks
</code></pre>
<p> Code like the above is known to leak memory every time the <i>local()</i> is executed.  </p>
<h3>Self-tying of Arrays and Hashes Is Forbidden</h3>
<p> Self-tying of arrays and hashes is broken in rather deep and hard-to-fix ways. As a stop-gap measure to avoid people from getting frustrated at the mysterious results (core dumps, most often) it is for now forbidden (you will get a fatal error even from an attempt).  </p>
<h3>Building Extensions Can Fail Because Of Largefiles</h3>
<p> Some extensions like mod_perl are known to have issues with `largefiles&#8217;, a change brought by Perl 5.6.0 in which file offsets default to 64 bits wide, where supported. Modules may fail to compile at all or compile and work incorrectly. Currently there is no good solution for the problem, but Configure now provides appropriate non-largefile ccflags, ldflags, libswanted, and libs in the <code>%Config</code> hash (e.g., <code>$Config</code>{ccflags_nolargefiles}) so the extensions that are having problems can try configuring themselves without the largefileness. This is admittedly not a clean solution, and the solution may not even work at all. One potential failure is whether one can (or, if one can, whether it&#8217;s a good idea) link together at all binaries with different ideas about file offsets, all this is platform-dependent.  </p>
<h3>The Compiler Suite Is Still Experimental</h3>
<p> The compiler suite is slowly getting better but is nowhere near working order yet.  </p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://bugs.perl.org/">http://bugs.perl.org/</a> There may also be information at <a rel="nofollow" href="http://www.perl.com/perl/">http://www.perl.com/perl/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <code>&quot;perl -V&quot;</code>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team.  </p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information.  </p>
<h2>HISTORY</h2>
<p> Written by Jarkko Hietaniemi &lt;<i>jhi [at] iki.fi</i>&gt;, with many contributions from The Perl Porters and Perl Users submitting feedback and patches. </p>
<p> Send omissions or corrections to &lt;<i>perlbug [at] perl.org</i>&gt;. </p>
<h2>Index</h2>
