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
<dt>&bull;</p>
<dd> Although &#8220;you shouldn&#8217;t do that&#8221;, it was possible to write code that depends on Perl&#8217;s hashed key order (Data::Dumper does this). The new algorithm &#8220;One-at-a-Time&#8221; produces a different hashed key order. More details are in &#8220;Performance Enhancements&#8221;.</p>
<dt>&bull;</p>
<dd> The list of filenames from <i>glob()</i> (or &lt;&#8230;&gt;) is now by default sorted alphabetically to be csh-compliant. (<i>bsd_glob()</i> does still sort platform natively, <font SIZE="-1">ASCII</font> or <font SIZE="-1">EBCDIC</font>, unless <font SIZE="-1">GLOB_ALPHASORT</font> is specified.)</dl>
<h2>Core Enhancements</h2>
<h3><font SIZE="-1">AUTOLOAD</font> Is Now Lvaluable</h3>
<p> <font SIZE="-1">AUTOLOAD</font> is now lvaluable, meaning that you can add the :lvalue attribute to <font SIZE="-1">AUTOLOAD</font> subroutines and you can assign to the <font SIZE="-1">AUTOLOAD</font> return value.</p>
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
<dd> File handles can be marked as accepting Perl&#8217;s internal encoding of Unicode (<font SIZE="-1">UTF-8</font> or UTF-EBCDIC depending on platform) by a pseudo layer &#8220;:utf8&#8221; : </p>
<pre>
   open($fh,&quot;&gt;:utf8&quot;,&quot;Uni.txt&quot;);
</pre>
<p> Note for <font SIZE="-1">EBCDIC</font> users: the pseudo layer &#8220;:utf8&#8221; is erroneously named for you since it&#8217;s not <font SIZE="-1">UTF-8</font> what you will be getting but instead UTF-EBCDIC. See perlunicode, utf8, and <a rel="nofollow" href="http://www.unicode.org/unicode/reports/tr16/">http://www.unicode.org/unicode/reports/tr16/</a> for more information. In future releases this naming may change.</p>
<dt>&bull;</p>
<dd> File handles can translate character encodings from/to Perl&#8217;s internal Unicode form on read/write via the &#8220;:<i>encoding()</i>&#8221; layer.</p>
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
<p> That is a literal undef, not an undefined value.</p>
<dt>&bull;</p>
<dd> The list form of <tt>&quot;open&quot;</tt> is now implemented for pipes (at least on Unix): </p>
<pre>
   open($fh,&quot;-|&quot;, 'cat', '/etc/motd')
</pre>
<p> creates a pipe, and runs the equivalent of exec(&#8216;cat&#8217;, &#8216;/etc/motd&#8217;) in the child process.</p>
<dt>&bull;</p>
<dd> The following builtin functions are now overridable: <i>chop()</i>, <i>chomp()</i>, <i>each()</i>, <i>keys()</i>, <i>pop()</i>, <i>push()</i>, <i>shift()</i>, <i>splice()</i>, <i>unshift()</i>.</p>
<dt>&bull;</p>
<dd> Formats now support zero-padded decimal fields.</p>
<dt>&bull;</p>
<dd> Perl now tries internally to use integer values in numeric conversions and basic arithmetics (+ &#8211; * /) if the arguments are integers, and tries also to keep the results stored internally as integers. This change leads into often slightly faster and always less lossy arithmetics. (Previously Perl always preferred floating point numbers in its math.)</p>
<dt>&bull;</p>
<dd> The <i>printf()</i> and <i>sprintf()</i> now support parameter reordering using the <tt>&quot;%\d+\$&quot;</tt> and <tt>&quot;*\d+\$&quot;</tt> syntaxes. For example </p>
<pre>
    print &quot;%2\$s %1\$s
&quot;, &quot;foo&quot;, &quot;bar&quot;;
</pre>
<p> will print &#8220;bar foo
&#8221;; This feature helps in writing internationalised software.</p>
<dt>&bull;</p>
<dd> Unicode in general should be now much more usable. Unicode can be used in hash keys, Unicode in regular expressions should work now, Unicode in tr/// should work now (though tr/// seems to be a particularly tricky to get right, so you have been warned)</p>
<dt>&bull;</p>
<dd> The Unicode Character Database coming with Perl has been upgraded to Unicode 3.1. For more information, see <a rel="nofollow" href="http://www.unicode.org/">http://www.unicode.org/</a> , and <a rel="nofollow" href="http://www.unicode.org/unicode/reports/tr27/">http://www.unicode.org/unicode/reports/tr27/</a> </p>
<p> For developers interested in enhancing Perl&#8217;s Unicode capabilities: almost all the <font SIZE="-1">UCD</font> files are included with the Perl distribution in the lib/unicode subdirectory. The most notable omission, for space considerations, is the Unihan database.</p>
<dt>&bull;</p>
<dd> The Unicode character classes \p{Blank} and \p{SpacePerl} have been added. &#8220;Blank&#8221; is like C <i>isblank()</i>, that is, it contains only &#8220;horizontal whitespace&#8221; (the space character is, the newline isn&#8217;t), and the &#8220;SpacePerl&#8221; is the Unicode equivalent of <tt>&quot;\s&quot;</tt> (\p{Space} isn&#8217;t, since that includes the vertical tabulator character, whereas <tt>&quot;\s&quot;</tt> doesn&#8217;t.)</dl>
<h3>Signals Are Now Safe</h3>
<p> Perl used to be fragile in that signals arriving at inopportune moments could corrupt Perl&#8217;s internal state.</p>
<h2>Modules and Pragmata</h2>
<h3>New Modules</h3>
<dl>
<dt>&bull;</p>
<dd> B::Concise, by Stephen McCamant, is a new compiler backend for walking the Perl syntax tree, printing concise info about ops. The output is highly customisable. </p>
<p> See B::Concise for more information.</p>
<dt>&bull;</p>
<dd> Class::ISA, by Sean Burke, for reporting the search path for a class&#8217;s <font SIZE="-1">ISA</font> tree, has been added. </p>
<p> See Class::ISA for more information.</p>
<dt>&bull;</p>
<dd> Cwd has now a split personality: if possible, an extension is used, (this will hopefully be both faster and more secure and robust) but if not possible, the familiar Perl library implementation is used.</p>
<dt>&bull;</p>
<dd> Digest, a frontend module for calculating digests (checksums), from Gisle Aas, has been added. </p>
<p> See Digest for more information.</p>
<dt>&bull;</p>
<dd> Digest::MD5 for calculating <font SIZE="-1">MD5</font> digests (checksums), by Gisle Aas, has been added. </p>
<pre><code>
use Digest::MD5 'md5_hex';
$digest = md5_hex("Thirsty Camel");
print $digest, "
";
# 01d19d9d2045e005c3f1b80e8b164de1
</code></pre>
<p> <font SIZE="-1">NOTE:</font> the <font SIZE="-1">MD5</font> backward compatibility module is deliberately not included since its use is discouraged. </p>
<p> See Digest::MD5 for more information.</p>
<dt>&bull;</p>
<dd> Encode, by Nick Ing-Simmons, provides a mechanism to translate between different character encodings. Support for Unicode, ISO-8859-*, <font SIZE="-1">ASCII</font>, CP*, <font SIZE="-1">KOI8-R</font>, and three variants of <font SIZE="-1">EBCDIC</font> are compiled in to the module. Several other encodings (like Japanese, Chinese, and MacIntosh encodings) are included and will be loaded at runtime. </p>
<p> Any encoding supported by Encode module is also available to the &#8220;:<i>encoding()</i>&#8221; layer if PerlIO is used. </p>
<p> See Encode for more information.</p>
<dt>&bull;</p>
<dd> Filter::Simple is an easy-to-use frontend to Filter::Util::Call, from Damian Conway. </p>
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
<dt>&bull;</p>
<dd> Filter::Util::Call, by Paul Marquess, provides you with the framework to write <i>Source Filters</i> in Perl. For most uses the frontend Filter::Simple is to be preferred. See Filter::Util::Call for more information.</p>
<dt>&bull;</p>
<dd> Locale::Constants, Locale::Country, Locale::Currency, and Locale::Language, from Neil Bowers, have been added. They provide the codes for various locale standards, such as &#8220;fr&#8221; for France, &#8220;usd&#8221; for <font SIZE="-1">US</font> Dollar, and &#8220;jp&#8221; for Japanese. </p>
<p>use Locale::Country;<br />
$country = code2country(&#8216;jp&#8217;);<br />
#$country gets &#8216;Japan&#8217; $code = country2code(&#8216;Norway&#8217;);<br />
#$code gets &#8216;no&#8217;</p>
<p> See Locale::Constants, Locale::Country, Locale::Currency, and Locale::Language for more information.</p>
<dt>&bull;</p>
<dd> MIME::Base64, by Gisle Aas, allows you to encode data in base64. </p>
<p>use MIME::Base64;<br />
$encoded = encode_base64(&#8216;Aladdin:open sesame&#8217;);<br />
$decoded = decode_base64($encoded);<br />
print $encoded, &#8220;
&#8221;;<br />
#&#8221;QWxhZGRpbjpvcGVuIHNlc2FtZQ==&#8221;</p>
<p> See MIME::Base64 for more information.</p>
<dt>&bull;</p>
<dd> MIME::QuotedPrint, by Gisle Aas, allows you to encode data in quoted-printable encoding. </p>
<p>use MIME::QuotedPrint;<br />
$encoded = encode_qp(&#8220;Smiley in Unicode: 
