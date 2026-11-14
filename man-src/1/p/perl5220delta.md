---
title: "perl5220delta(1)"
name: "perl5220delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5220delta/"
description: "perl5220delta – what is new for perl v5.22.0"
---

<h2 class="name">NAME</h2>
<p> perl5220delta &#8211; what is new for perl v5.22.0 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.20.0 release and the 5.22.0 release. </p>
<p> If you are upgrading from an earlier release such as 5.18.0, first read perl5200delta, which describes differences between 5.18.0 and 5.20.0.</p>
<h2>Core Enhancements</h2>
<h3>New bitwise operators</h3>
<p> A new experimental facility has been added that makes the four standard bitwise operators (<tt>&quot;&amp; | ^ ~&quot;</tt>) treat their operands consistently as numbers, and introduces four new dotted operators (<tt>&quot;&amp;. |. ^. ~.&quot;</tt>) that treat their operands consistently as strings. The same applies to the assignment variants (<tt>&quot;&amp;= |= ^= &amp;.= |.= ^.=&quot;</tt>). </p>
<p> To use this, enable the &#8220;bitwise&#8221; feature and disable the &#8220;experimental::bitwise&#8221; warnings category. See &#8220;Bitwise String Operators&#8221; in perlop for details. [perl #123466] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123466">https://rt.perl.org/Ticket/Display.html?id=123466</a>&gt;.</p>
<h3>New double-diamond operator</h3>
<p> <tt>&quot;&lt;&lt;&gt;&gt;&quot;</tt> is like <tt>&quot;&lt;&gt;&quot;</tt> but uses three-argument <tt>&quot;open&quot;</tt> to open each file in <tt>@ARGV</tt>. This means that each element of <tt>@ARGV</tt> will be treated as an actual file name, and <tt>&quot;|foo&quot;</tt> won&#8217;t be treated as a pipe open.</p>
<h3>New  boundaries in regular expressions</h3>
<p> <i></i>&quot;qr/{gcb}/&quot;<i></i> </p>
<p> <tt>&quot;gcb&quot;</tt> stands for Grapheme Cluster Boundary. It is a Unicode property that finds the boundary between sequences of characters that look like a single character to a native speaker of a language. Perl has long had the ability to deal with these through the <tt>&quot;\X&quot;</tt> regular escape sequence. Now, there is an alternative way of handling these. See &#8220;{}, , \B{}, \B&#8221; in perlrebackslash for details. </p>
<p> <i></i>&quot;qr/{wb}/&quot;<i></i> </p>
<p> <tt>&quot;wb&quot;</tt> stands for Word Boundary. It is a Unicode property that finds the boundary between words. This is similar to the plain <tt>&quot;&quot;</tt> (without braces) but is more suitable for natural language processing. It knows, for example, that apostrophes can occur in the middle of words. See &#8220;{}, , \B{}, \B&#8221; in perlrebackslash for details. </p>
<p> <i></i>&quot;qr/{sb}/&quot;<i></i> </p>
<p> <tt>&quot;sb&quot;</tt> stands for Sentence Boundary. It is a Unicode property to aid in parsing natural language sentences. See &#8220;{}, , \B{}, \B&#8221; in perlrebackslash for details.</p>
<h3>Non-Capturing Regular Expression Flag</h3>
<p> Regular expressions now support a <tt>&quot;/n&quot;</tt> flag that disables capturing and filling in <tt>$1</tt>, <tt>$2</tt>, etc inside of groups: </p>
<pre>
  &quot;hello&quot; =~ /(hi|hello)/n; # $1 is not set
</pre>
<p> This is equivalent to putting <tt>&quot;?:&quot;</tt> at the beginning of every capturing group. </p>
<p> See &#8220;n&#8221; in perlre for more information.</p>
<h3>use re &#8216;strict&#8217;</h3>
<p> This applies stricter syntax rules to regular expression patterns compiled within its scope. This will hopefully alert you to typos and other unintentional behavior that backwards-compatibility issues prevent us from reporting in normal regular expression compilations. Because the behavior of this is subject to change in future Perl releases as we gain experience, using this pragma will raise a warning of category <tt>&quot;experimental::re_strict&quot;</tt>. See &#8216;strict&#8217; in re.</p>
<h3>Unicode 7.0 (with correction) is now supported</h3>
<p> For details on what is in this release, see &lt;<a rel="nofollow" href="http://www.unicode.org/versions/Unicode7.0.0/">http://www.unicode.org/versions/Unicode7.0.0/</a>&gt;. The version of Unicode 7.0 that comes with Perl includes a correction dealing with glyph shaping in Arabic (see &lt;<a rel="nofollow" href="http://www.unicode.org/errata/#current_errata">http://www.unicode.org/errata/#current_errata</a>&gt;).</p>
<h3>use locale can restrict which locale categories are affected</h3>
<p> It is now possible to pass a parameter to <tt>&quot;use locale&quot;</tt> to specify a subset of locale categories to be locale-aware, with the remaining ones unaffected. See &#8220;The &#8221;use locale&#8220; pragma&#8221; in perllocale for details.</p>
<h3>Perl now supports <font SIZE="-1">POSIX 2008</font> locale currency additions</h3>
<p> On platforms that are able to handle <font SIZE="-1">POSIX.1-2008,</font> the hash returned by <tt>&quot;POSIX::localeconv()&quot;</tt> includes the international currency fields added by that version of the <font SIZE="-1">POSIX</font> standard. These are <tt>&quot;int_n_cs_precedes&quot;</tt>, <tt>&quot;int_n_sep_by_space&quot;</tt>, <tt>&quot;int_n_sign_posn&quot;</tt>, <tt>&quot;int_p_cs_precedes&quot;</tt>, <tt>&quot;int_p_sep_by_space&quot;</tt>, and <tt>&quot;int_p_sign_posn&quot;</tt>.</p>
<h3>Better heuristics on older platforms for determining locale UTF-8ness</h3>
<p> On platforms that implement neither the C99 standard nor the <font SIZE="-1">POSIX 2001</font> standard, determining if the current locale is <font SIZE="-1">UTF-8</font> or not depends on heuristics. These are improved in this release.</p>
<h3>Aliasing via reference</h3>
<p> Variables and subroutines can now be aliased by assigning to a reference: </p>
<pre>
    \$c = \$d;
    \&amp;x = \&amp;y;
</pre>
<p> Aliasing can also be accomplished by using a backslash before a <tt>&quot;foreach&quot;</tt> iterator variable; this is perhaps the most useful idiom this feature provides: </p>
<pre>
    foreach \%hash (@array_of_hash_refs) { ... }
</pre>
<p> This feature is experimental and must be enabled via <tt>&quot;use feature 'refaliasing'&quot;</tt>. It will warn unless the <tt>&quot;experimental::refaliasing&quot;</tt> warnings category is disabled. </p>
<p> See &#8220;Assigning to References&#8221; in perlref</p>
<h3>prototype with no arguments</h3>
<p> <tt>&quot;prototype()&quot;</tt> with no arguments now infers <tt>$_</tt>. [perl #123514] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123514">https://rt.perl.org/Ticket/Display.html?id=123514</a>&gt;.</p>
<h3>New :const subroutine attribute</h3>
<p> The <tt>&quot;const&quot;</tt> attribute can be applied to an anonymous subroutine. It causes the new sub to be executed immediately whenever one is created (<i>i.e.</i> when the <tt>&quot;sub&quot;</tt> expression is evaluated). Its value is captured and used to create a new constant subroutine that is returned. This feature is experimental. See &#8220;Constant Functions&#8221; in perlsub.</p>
<h3>fileno now works on directory handles</h3>
<p> When the relevant support is available in the operating system, the <tt>&quot;fileno&quot;</tt> builtin now works on directory handles, yielding the underlying file descriptor in the same way as for filehandles. On operating systems without such support, <tt>&quot;fileno&quot;</tt> on a directory handle continues to return the undefined value, as before, but also sets <tt>$!</tt> to indicate that the operation is not supported. </p>
<p> Currently, this uses either a <tt>&quot;dd_fd&quot;</tt> member in the <font SIZE="-1">OS</font> <tt>&quot;DIR&quot;</tt> structure, or a <tt><a href="/docs/linux/man/3-dirfd/">dirfd</a>(3)</tt> function as specified by <font SIZE="-1">POSIX.1-2008.</font></p>
<h3>List form of pipe open implemented for Win32</h3>
<p> The list form of pipe: </p>
<pre>
  open my $fh, &quot;-|&quot;, &quot;program&quot;, @arguments;
</pre>
<p> is now implemented on Win32. It has the same limitations as <tt>&quot;system LIST&quot;</tt> on Win32, since the Win32 <font SIZE="-1">API</font> doesn&#8217;t accept program arguments as a list.</p>
<h3>Assignment to list repetition</h3>
<p> <tt>&quot;(...) x ...&quot;</tt> can now be used within a list that is assigned to, as long as the left-hand side is a valid lvalue. This allows <tt>&quot;(undef,undef,$foo) = that_function()&quot;</tt> to be written as <tt>&quot;((undef)x2, $foo) = that_function()&quot;</tt>.</p>
<h3>Infinity and NaN (not-a-number) handling improved</h3>
<p> Floating point values are able to hold the special values infinity, negative infinity, and NaN (not-a-number). Now we more robustly recognize and propagate the value in computations, and on output normalize them to the strings <tt>&quot;Inf&quot;</tt>, <tt>&quot;-Inf&quot;</tt>, and <tt>&quot;NaN&quot;</tt>. </p>
<p> See also the <font SIZE="-1">POSIX</font> enhancements.</p>
<h3>Floating point parsing has been improved</h3>
<p> Parsing and printing of floating point values has been improved. </p>
<p> As a completely new feature, hexadecimal floating point literals (like <tt>&quot;0x1.23p-4&quot;</tt>) are now supported, and they can be output with <tt>&quot;printf &quot;%a&quot;&quot;</tt>. See &#8220;Scalar value constructors&#8221; in perldata for more details.</p>
<h3>Packing infinity or not-a-number into a character is now fatal</h3>
<p> Before, when trying to pack infinity or not-a-number into a (signed) character, Perl would warn, and assumed you tried to pack <tt>0xFF</tt>; if you gave it as an argument to <tt>&quot;chr&quot;</tt>, <tt>&quot;U+FFFD&quot;</tt> was returned. </p>
<p> But now, all such actions (<tt>&quot;pack&quot;</tt>, <tt>&quot;chr&quot;</tt>, and <tt>&quot;print '%c'&quot;</tt>) result in a fatal error.</p>
<h3>Experimental C Backtrace <font SIZE="-1">API</font></h3>
<p> Perl now supports (via a C level <font SIZE="-1">API</font>) retrieving the C level backtrace (similar to what symbolic debuggers like gdb do). </p>
<p> The backtrace returns the stack trace of the C call frames, with the symbol names (function names), the object names (like &#8220;perl&#8221;), and if it can, also the source code locations (file:line). </p>
<p> The supported platforms are Linux and <font SIZE="-1">OS X</font> (some *BSD might work at least partly, but they have not yet been tested). </p>
<p> The feature needs to be enabled with <tt>&quot;Configure -Dusecbacktrace&quot;</tt>. </p>
<p> See &#8220;C backtrace&#8221; in perlhacktips for more information.</p>
<h2>Security</h2>
<h3>Perl is now compiled with -fstack-protector-strong if available</h3>
<p> Perl has been compiled with the anti-stack-smashing option <tt>&quot;-fstack-protector&quot;</tt> since 5.10.1. Now Perl uses the newer variant called <tt>&quot;-fstack-protector-strong&quot;</tt>, if available.</p>
<h3>The Safe module could allow outside packages to be replaced</h3>
<p> Critical bugfix: outside packages could be replaced. Safe has been patched to 2.38 to address this.</p>
<h3>Perl is now always compiled with -D_FORTIFY_SOURCE=2 if available</h3>
<p> The &#8216;code hardening&#8217; option called <tt>&quot;_FORTIFY_SOURCE&quot;</tt>, available in gcc 4.*, is now always used for compiling Perl, if available. </p>
<p> Note that this isn&#8217;t necessarily a huge step since in many platforms the step had already been taken several years ago: many Linux distributions (like Fedora) have been using this option for Perl, and <font SIZE="-1">OS X</font> has enforced the same for many years.</p>
<h2>Incompatible Changes</h2>
<h3>Subroutine signatures moved before attributes</h3>
<p> The experimental sub signatures feature, as introduced in 5.20, parsed signatures after attributes. In this release, following feedback from users of the experimental feature, the positioning has been moved such that signatures occur after the subroutine name (if any) and before the attribute list (if any).</p>
<h3>&amp; and \&amp; prototypes accepts only subs</h3>
<p> The <tt>&quot;&amp;&quot;</tt> prototype character now accepts only anonymous subs (<tt>&quot;sub {...}&quot;</tt>), things beginning with <tt>&quot;\&amp;&quot;</tt>, or an explicit <tt>&quot;undef&quot;</tt>. Formerly it erroneously also allowed references to arrays, hashes, and lists. [perl #4539] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=4539">https://rt.perl.org/Ticket/Display.html?id=4539</a>&gt;. [perl #123062] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123062">https://rt.perl.org/Ticket/Display.html?id=123062</a>&gt;. [perl #123062] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123475">https://rt.perl.org/Ticket/Display.html?id=123475</a>&gt;. </p>
<p> In addition, the <tt>&quot;\&amp;&quot;</tt> prototype was allowing subroutine calls, whereas now it only allows subroutines: <tt>&amp;foo</tt> is still permitted as an argument, while <tt>&quot;&amp;foo()&quot;</tt> and <tt>&quot;foo()&quot;</tt> no longer are. [perl #77860] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=77860">https://rt.perl.org/Ticket/Display.html?id=77860</a>&gt;.</p>
<h3>use encoding is now lexical</h3>
<p> The encoding pragma&#8217;s effect is now limited to lexical scope. This pragma is deprecated, but in the meantime, it could adversely affect unrelated modules that are included in the same program; this change fixes that.</p>
<h3>List slices returning empty lists</h3>
<p> List slices now return an empty list only if the original list was empty (or if there are no indices). Formerly, a list slice would return an empty list if all indices fell outside the original list; now it returns a list of <tt>&quot;undef&quot;</tt> values in that case. [perl #114498] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=114498">https://rt.perl.org/Ticket/Display.html?id=114498</a>&gt;.</p>
<h3>\N{} with a sequence of multiple spaces is now a fatal error</h3>
<p> E.g. <tt>&quot;\N{TOO  MANY SPACES}&quot;</tt> or <tt>&quot;\N{TRAILING SPACE }&quot;</tt>. This has been deprecated since v5.18.</p>
<h3>use UNIVERSAL &#8216;&#8230;&#8217; is now a fatal error</h3>
<p> Importing functions from <tt>&quot;UNIVERSAL&quot;</tt> has been deprecated since v5.12, and is now a fatal error. <tt>&quot;use UNIVERSAL&quot;</tt> without any arguments is still allowed.</p>
<h3>In double-quotish 
