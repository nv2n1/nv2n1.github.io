---
title: "perl5136delta(1)"
name: "perl5136delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5136delta/"
description: "perl5136delta – what is new for perl v5.13.6"
---

<h2 class="name">NAME</h2>
<p> perl5136delta &#8211; what is new for perl v5.13.6 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.13.5 release and the 5.13.6 release. </p>
<p> If you are upgrading from an earlier release such as 5.13.4, first read perl5135delta, which describes differences between 5.13.4 and 5.13.5.</p>
<h2>Core Enhancements</h2>
<h3>(?^&#8230;) regex construct added to signify default modifiers</h3>
<p> A caret (also called a &#8220;circumflex accent&#8221;) <tt>&quot;^&quot;</tt> immediately following a <tt>&quot;(?&quot;</tt> in a regular expression now means that the subexpression is to not inherit the surrounding modifiers such as <tt>&quot;/i&quot;</tt>, but to revert to the Perl defaults. Any modifiers following the caret override the defaults. </p>
<p> The stringification of regular expressions now uses this notation. E.g., before, <tt>&quot;qr/hlagh/i&quot;</tt> would be stringified as <tt>&quot;(?i-xsm:hlagh)&quot;</tt>, but now it&#8217;s stringified as <tt>&quot;(?^i:hlagh)&quot;</tt>. </p>
<p> The main purpose of this is to allow tests that rely on the stringification to not have to change when new modifiers are added. See &#8220;Extended Patterns&#8221; in perlre.</p>
<h3>d, l, and u regex modifiers added</h3>
<p> These modifiers are currently only available within a <tt>&quot;(?...)&quot;</tt> construct. </p>
<p> The <tt>&quot;l&quot;</tt> modifier says to compile the regular expression as if it were in the scope of <tt>&quot;use locale&quot;</tt>, even if it is not. </p>
<p> The <tt>&quot;u&quot;</tt> modifier says to compile the regular expression as if it were in the scope of a <tt>&quot;use feature &quot;unicode_strings&quot;&quot;</tt> pragma. </p>
<p> The <tt>&quot;d&quot;</tt> modifier is used to override any <tt>&quot;use locale&quot;</tt> and <tt>&quot;use feature &quot;unicode_strings&quot;&quot;</tt> pragmas that are in effect at the time of compiling the regular expression. </p>
<p> See just below and &#8220;(?dlupimsx-imsx)&#8221; in perlre.</p>
<h3>use feature unicode_strings now applies to some regex matching</h3>
<p> Another chunk of the &#8220;The &#8221;Unicode Bug&quot;&quot; in perlunicode is fixed in this release. Now, regular expressions compiled within the scope of the &#8220;unicode_strings&#8221; feature will match the same whether or not the target string is encoded in utf8, with regard to <tt>&quot;\s&quot;</tt>, <tt>&quot;\w&quot;</tt>, <tt>&quot;&quot;</tt>, and their complements. Work is underway to add the <tt>&quot;[[:posix:]]&quot;</tt> character classes and case sensitive matching to the control of this feature, but was not complete in time for this dot release.</p>
<h3>\N{&#8230;} now handles Unicode named character sequences</h3>
<p> Unicode has a number of named character sequences, in which particular sequences of code points are given names. <tt>&quot;\N{...}&quot;</tt> now recognizes these. See charnames.</p>
<h3>New function charnames::string_vianame()</h3>
<p> This function is a run-time version of <tt>&quot;\N{...}&quot;</tt>, returning the string of characters whose Unicode name is its parameter. It can handle Unicode named character sequences, whereas the pre-existing <tt>&quot;charnames::vianame()&quot;</tt> cannot, as the latter returns a single code point. See charnames.</p>
<h3>Reentrant regular expression engine</h3>
<p> It is now safe to use regular expressions within <tt>&quot;(?{...})&quot;</tt> and <tt>&quot;(??{...})&quot;</tt> code blocks inside regular expressions. </p>
<p> These block are still experimental, however, and still have problems with lexical (<tt>&quot;my&quot;</tt>) variables, lexical pragmata and abnormal exiting.</p>
<h3>Custom per-subroutine check hooks</h3>
<p> <font SIZE="-1">XS</font> code in an extension module can now annotate a subroutine (whether implemented in <font SIZE="-1">XS</font> or in Perl) so that nominated <font SIZE="-1">XS</font> code will be called at compile time (specifically as part of op checking) to change the op tree of that subroutine. The compile-time check function (supplied by the extension module) can implement argument processing that can&#8217;t be expressed as a prototype, generate customised compile-time warnings, perform constant folding for a pure function, inline a subroutine consisting of sufficiently simple ops, replace the whole call with a custom op, and so on. This was previously all possible by hooking the <tt>&quot;entersub&quot;</tt> op checker, but the new mechanism makes it easy to tie the hook to a specific subroutine. See &#8220;cv_set_call_checker&#8221; in perlapi. </p>
<p> To help in writing custom check hooks, several subtasks within standard <tt>&quot;entersub&quot;</tt> op checking have been separated out and exposed in the <font SIZE="-1">API</font>.</p>
<h3>Return value of delete $+{&#8230;}</h3>
<p> Custom regular expression engines can now determine the return value of <tt>&quot;delete&quot;</tt> on an entry of <tt>&quot;%+&quot;</tt> or <tt>&quot;%-&quot;</tt>.</p>
<h3>keys, values work on arrays</h3>
<p> You can now use the <tt>&quot;keys&quot;</tt>, <tt>&quot;values&quot;</tt>, <tt>&quot;each&quot;</tt> builtin functions on arrays (previously you could only use them on hashes). See perlfunc for details. This is actually a change introduced in perl 5.12.0, but it was missed from that release&#8217;s perldelta.</p>
<h2>Incompatible Changes</h2>
<h3>Stringification of regexes has changed</h3>
<p> Default regular expression modifiers are now notated by using <tt>&quot;(?^...)&quot;</tt>. Code relying on the old stringification will fail. The purpose of this is so that when new modifiers are added, such code will not have to change (after this one time), as the stringification will automatically incorporate the new modifiers. </p>
<p> Code that needs to work properly with both old- and new-style regexes can avoid the whole issue by using (for Perls since 5.9.5): </p>
<pre><code>
use re qw(regexp_pattern);
my($pat, $mods) = regexp_pattern($re_ref);
</code></pre>
<p> where <tt>$re_ref</tt> is a reference to a compiled regular expression. Upon return, <tt>$mods</tt> will be a string containing all the non-default modifiers used when the regular expression was compiled, and <tt>$pattern</tt> the actual pattern. </p>
<p> If the actual stringification is important, or older Perls need to be supported, you can use something like the following: </p>
<pre>
    # Accept both old and new-style stringification
    my $modifiers = (qr/foobar/ =~ /\Q(?^/) ? '^' : '-xism';
</pre>
<p> And then use <tt>$modifiers</tt> instead of <tt>&quot;-xism&quot;</tt>.</p>
<h3>Regular expressions retain their localeness when interpolated</h3>
<p> Regular expressions compiled under <tt>&quot;use locale&quot;</tt> now retain this when interpolated into a new regular expression compiled outside a <tt>&quot;use locale&quot;</tt>, and vice-versa. </p>
<p> Previously, a regular expression interpolated into another one inherited the localeness of the surrounding one, losing whatever state it originally had. This is considered a bug fix, but may trip up code that has come to rely on the incorrect behavior.</p>
<h3>Directory handles not copied to threads</h3>
<p> On systems that do not have a <tt>&quot;fchdir&quot;</tt> function, newly-created threads no longer inherit directory handles from their parent threads. Such programs would probably have crashed anyway [perl #75154] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=75154">http://rt.perl.org/rt3/Public/Bug/Display.html?id=75154</a>&gt;.</p>
<h3>Negation treats strings differently from before</h3>
<p> The unary negation operator <tt>&quot;-&quot;</tt> now treats strings that look like numbers as numbers [perl #57706] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=57706">http://rt.perl.org/rt3/Public/Bug/Display.html?id=57706</a>&gt;.</p>
<h3>Negative zero</h3>
<p> Negative zero (-0.0), when converted to a string, now becomes &#8220;0&#8221; on all platforms. It used to become &#8220;-0&#8221; on some, but &#8220;0&#8221; on others. </p>
<p> If you still need to determine whether a zero is negative, use <tt>&quot;sprintf(&quot;%g&quot;, $zero) =~ /^-/&quot;</tt> or the Data::Float module on <font SIZE="-1">CPAN</font>.</p>
<h2>Performance Enhancements</h2>
<dl>
<dt>&bull;</p>
<dd> The bulk of the <tt>&quot;Tie::Hash::NamedCapture&quot;</tt> module used to be in the perl core. It has now been moved to an <font SIZE="-1">XS</font> module, to reduce the overhead for programs that do not use <tt>&quot;%+&quot;</tt> or <tt>&quot;%-&quot;</tt>.</p>
<dt>&bull;</p>
<dd> Eliminate <tt>&quot;PL_*&quot;</tt> accessor functions under ithreads. </p>
<p> When <tt>&quot;MULTIPLICITY&quot;</tt> was first developed, and interpreter state moved into an interpreter struct, thread and interpreter local <tt>&quot;PL_*&quot;</tt> variables were defined as macros that called accessor functions, returning the address of the value, outside of the perl core. The intent was to allow members within the interpreter struct to change size without breaking binary compatibility, so that bug fixes could be merged to a maintenance branch that necessitated such a size change. </p>
<p> However, some non-core code defines <tt>&quot;PERL_CORE&quot;</tt>, sometimes intentionally to bypass this mechanism for speed reasons, sometimes for other reasons but with the inadvertent side effect of bypassing this mechanism. As some of this code is widespread in production use, the result is that the core <code>can&#8217;t</code> change the size of members of the interpreter struct, as it will break such modules compiled against a previous release on that maintenance branch. The upshot is that this mechanism is redundant, and well-behaved code is penalised by it. Hence it can and should be removed.</dl>
<h2>Modules and Pragmata</h2>
<h3>Updated Modules and Pragmata</h3>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;Archive::Extract&quot;</tt> has been upgraded from version 0.42 to 0.44</p>
<dt>&bull;</p>
<dd> <tt>&quot;Carp&quot;</tt> has been upgraded from version 1.18 to 1.19. </p>
<p> It no longer autovivifies the <tt>*CORE::GLOBAL::caller</tt> glob, something it started doing in 1.18, which was released with perl 5.13.4 [perl #78082] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3//Public/Bug/Display.html?id=78082">http://rt.perl.org/rt3//Public/Bug/Display.html?id=78082</a>&gt;</p>
<dt>&bull;</p>
<dd> <tt>&quot;Compress::Raw::Bzip2&quot;</tt> has been upgraded from version 2.030 to 2.031 </p>
<p> Updated to use bzip2 1.0.6</p>
<dt>&bull;</p>
<dd> <tt>&quot;CPAN&quot;</tt> has been upgraded from version 1.94_57 to 1.94_61</p>
<dt>&bull;</p>
<dd> <tt>&quot;Data::Dumper&quot;</tt> has been upgraded from version 2.128 to 2.129. </p>
<p> <tt>&quot;Dumpxs&quot;</tt> no longer crashes with globs returned by <tt>*$io_ref</tt> [perl #72332] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3//Public/Bug/Display.html?id=72332">http://rt.perl.org/rt3//Public/Bug/Display.html?id=72332</a>&gt;.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Digest::MD5&quot;</tt> has been upgraded from version 2.40 to 2.51. </p>
<p> It is now safe to use this module in combination with threads.</p>
<dt>&bull;</p>
<dd> <tt>&quot;File::DosGlob&quot;</tt> has been upgraded from version 1.02 to 1.03. </p>
<p> It allows patterns containing literal parentheses (they no longer need to be escaped). On Windows, it no longer adds an extra <i>./</i> to the file names returned when the pattern is a relative glob with a drive specification, like <i>c:*.pl</i> [perl #71712] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3//Public/Bug/Display.html?id=71712">http://rt.perl.org/rt3//Public/Bug/Display.html?id=71712</a>&gt;.</p>
<dt>&bull;</p>
<dd> <tt>&quot;File::Find&quot;</tt> has been upgraded from version 1.17 to 1.18. </p>
<p> It improves handling of backslashes on Windows, so that paths such as <i>c:\dir\/file</i> are no longer generated [perl #71710] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3//Public/Bug/Display.html?id=71710">http://rt.perl.org/rt3//Public/Bug/Display.html?id=71710</a>&gt;.</p>
<dt>&bull;</p>
<dd> <tt>&quot;if&quot;</tt> has been upgraded from version 0.05 to 0.06</p>
<dt>&bull;</p>
<dd> <tt>&quot;IPC::Cmd&quot;</tt> has been upgraded from version 0.60 to 0.64</p>
<dt>&bull;</p>
<dd> <tt>&quot;IPC::Open3&quot;</tt> has been upgraded from version 1.06 to 1.07. </p>
<p> The internal <tt>&quot;xclose&quot;</tt> routine now knows how to handle file descriptors, as documented, so duplicating <font SIZE="-1">STDIN</font> in a child process using its file descriptor now works [perl #76474] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3//Public/Bug/Display.html?id=71710">http://rt.perl.org/rt3//Public/Bug/Display.html?id=71710</a>&gt;.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Locale::Codes&quot;</tt> has been upgraded from version 3.13 to 3.14.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Locale::Maketext&quot;</tt> has been upgraded from version 1.15 to 1.16. </p>
<p> It fixes an infinite loop in <tt>&quot;Locale::Maketext::Guts::_compile()&quot;</tt> when working with tainted values (<font SIZE="-1">CPAN</font> <font SIZE="-1">RT</font> #40727 &lt;<a rel="nofollow" href="https://rt.cpan.org/Public/Bug/Display.html?id=40727">https://rt.cpan.org/Public/Bug/Display.html?id=40727</a>&gt;). </p>
<p> <tt>&quot;-&gt;maketext&quot;</tt> calls will now backup and restore <tt>$@</tt> so that error messages are not suppressed (<font SIZE="-1">CPAN</font> <font SIZE="-1">RT</font> #34182 &lt;<a rel="nofollow" href="https://rt.cpan.org/Public/Bug/Display.html?id=34182">https://rt.cpan.org/Public/Bug/Display.html?id=34182</a>&gt;).</p>
<dt>&bull;</p>
<dd> <tt>&quot;Math::BigInt&quot;</tt> has been upgraded from version 1.95 to 1.97. </p>
<p> This prevents <tt>&quot;sqrt($int)&quot;</tt> from crashing under <tt>&quot;use bigrat;&quot;</tt> [perl #73534] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3//Public/Bug/Display.html?id=73534">http://rt.perl.org/rt3//Public/Bug/Display.html?id=73534</a>&gt;.</p>
<dt>&bull;</p>
<dd> <tt>&quot;NEXT&quot;</tt> has been upgraded from version 0.64 to 0.65.</p>
<dt>&bull;</p>
<dd> <tt>&quot;overload&quot;</tt> has been upgraded from version 1.10 to 1.11. </p>
<p> <tt>&quot;overload::Method&quot;</tt> can now handle subroutines that are themselves blessed into overloaded classes [perl #71998] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3//Public/Bug/Display.html?id=71998">http://rt.perl.org/rt3//Public/Bug/Display.html?id=71998</a>&gt;.</p>
<dt>&bull;</p>
<dd> <tt>&quot;PathTools&quot;</tt> has been upgraded from version 3.31_01 to 3.34.</p>
<dt>&bull;</p>
<dd> <tt>&quot;podlators&quot;</tt> has been upgraded from version 2.3.1 to 2.4.0</p>
<dt>&bull;</p>
<dd> <tt>&quot;sigtrap&quot;</tt> has been upgraded from version 1.04 to 1.05. </p>
<p> It no longer tries to modify read-only arguments when generating a backtrace [perl #72340] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3//Public/Bug/Display.html?id=72340">http://rt.perl.org/rt3//Public/Bug/Display.html?id=72340</a>&gt;.</p>
<dt>&bull;</p>
<dd> <tt>&quot;threads&quot;</tt> has been upgraded from version 1.77_03 to 1.81_01.</p>
<dt>&bull;</p>
<dd> <tt>&quot;threads::shared&quot;</tt> has been upgrade from version 1.33_03 to 1.34</p>
<dt>&bull;</p>
<dd> <tt>&quot;Unicode::Collate&quot;</tt> has been upgraded from version 0.59 to 0.63 </p>
<p> U::C::Locale newly supports locales: ar, be, bg, de__phonebook, hu, hy, kk, mk, nso, om, tn, vi, hr, ig, ru, sq, se, sr, to and uk</p>
<dt>&bull;</p>
<dd> <tt>&quot;Unicode::Normalize&quot;</tt> has been upgraded from version 1.06 to 1.07</p>
<dt>&bull;</p>
<dd> <tt>&quot;B::Deparse&quot;</tt> has been upgraded from version 0.98 to 0.99 </p>
<p> B::Deparse now properly handles the code that applies a conditional pattern match against implicit <tt>$_</tt> as it was fixed in [perl #20444] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3//Public/Bug/Display.html?id=20444">http://rt.perl.org/rt3//Public/Bug/Display.html?id=20444</a>&gt;.</p>
<dt>&bull;</p>
<dd> <tt>&quot;GDBM_File&quot;</tt> has been upgraded from version 1.10 to 1.11</dl>
<h2>Documentation</h2>
<h3>Changes to Existing Documentation</h3>
<p> <i>perlapi</i></p>
<dl>
<dt>&bull;</p>
<dd> The documentation for the <tt>&quot;SvTRUE&quot;</tt> macro was simply wrong in stating that get-magic is not processed. It has been corrected.</dl>
<h2>Diagnostics</h2>
<p> The following additions or changes have been made to diagnostic output, including warnings and fatal error messages. For the complete list of diagnostic messages, see perldiag.</p>
<h3>Changes to Existing Diagnostics</h3>
<dl>
<dt>&bull;</p>
<dd> The &#8216;Layer does not match this perl&#8217; error message has been replaced with these more helpful messages:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> PerlIO layer function table size (%d) does not match size expected by this perl (%d)</p>
<dt>&bull;</p>
<dd> PerlIO layer instance size (%d) does not match size expected by this perl (%d)</dl>
</dl>
<dl>
<dt>
<dd>
<p> [perl #73754] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3//Public/Bug/Display.html?id=73754">http://rt.perl.org/rt3//Public/Bug/Display.html?id=73754</a>&gt;</dl>
</dl>
<h2>Testing</h2>
<dl>
<dt>&bull;</p>
<dd> The script <i>t/op/threads-dirh.t</i> has been added, which tests interaction of threads and directory handles.</dl>
<h2>Platform Support</h2>
<h3>Platform-Specific Notes</h3>
<dl>
<dt><font SIZE="-1">IRIX</font></p>
<dd> Conversion of strings to floating-point numbers is now more accurate on <font SIZE="-1">IRIX</font> systems [perl #32380] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3//Public/Bug/Display.html?id=32380">http://rt.perl.org/rt3//Public/Bug/Display.html?id=32380</a>&gt;.</p>
<dt>Mac <font SIZE="-1">OS</font> X</p>
<dd> Early versions of Mac <font SIZE="-1">OS</font> X (Darwin) had buggy implementations of the <tt>&quot;setregid&quot;</tt>, <tt>&quot;setreuid&quot;</tt>, <tt>&quot;setrgid&quot;</tt> and <tt>&quot;setruid&quot;</tt> functions, so perl would pretend they did not exist. </p>
<p> These functions are now recognised on Mac <font SIZE="-1">OS</font> 10.5 (Leopard; Darwin 9) and higher, as they have been fixed [perl #72990] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3//Public/Bug/Display.html?id=72990">http://rt.perl.org/rt3//Public/Bug/Display.html?id=72990</a>&gt;.</p>
<dt>OpenVOS</p>
<dd> perl now builds again with OpenVOS (formerly known as Stratus <font SIZE="-1">VOS</font>) [perl #78132] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3//Public/Bug/Display.html?id=78132">http://rt.perl.org/rt3//Public/Bug/Display.html?id=78132</a>&gt;.</p>
<dt><font SIZE="-1">VMS</font></p>
<dd> The shortening of symbols longer than 31 characters in the C sources is now done by the compiler rather than by xsubpp (which could only do so for generated symbols in <font SIZE="-1">XS</font> code).</p>
<dt>Windows</p>
<dd> <tt>$Config{gccversion}</tt> is now set correctly when perl is built using the mingw64 compiler from &lt;<a rel="nofollow" href="http://mingw64.org">http://mingw64.org</a>&gt; [perl #73754] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3//Public/Bug/Display.html?id=73754">http://rt.perl.org/rt3//Public/Bug/Display.html?id=73754</a>&gt;. </p>
<p> The build process proceeds more smoothly with mingw and dmake when <i>C:\MSYSin</i> is in the <font SIZE="-1">PATH</font>, due to a <tt>&quot;Cwd&quot;</tt> fix.</dl>
<h2>Internal Changes</h2>
<dl>
<dt>&bull;</p>
<dd> See &#8220;Regular expressions retain their localeness when interpolated&#8221;, above.</p>
<dt>&bull;</p>
<dd> The <tt>&quot;sv_cmp_flags&quot;</tt>, <tt>&quot;sv_cmp_locale_flags&quot;</tt>, <tt>&quot;sv_eq_flags&quot;</tt> and <tt>&quot;sv_collxfrm_flags&quot;</tt> functions have been added. These are like their non-_flags counterparts, but allow one to specify whether get-magic is processed. </p>
<p> The <tt>&quot;sv_cmp&quot;</tt>, <tt>&quot;sv_cmp_locale&quot;</tt>, <tt>&quot;sv_eq&quot;</tt> and <tt>&quot;sv_collxfrm&quot;</tt> functions have been replaced with wrappers around the new functions.</p>
<dt>&bull;</p>
<dd> A new <tt>&quot;sv_2bool_flags&quot;</tt> function has been added. </p>
<p> This is like <tt>&quot;sv_2bool&quot;</tt>, but it lets the calling code decide whether get-magic is handled. <tt>&quot;sv_2bool&quot;</tt> is now a macro that calls the new function.</p>
<dt>&bull;</p>
<dd> A new macro, <tt>&quot;SvTRUE_nomg&quot;</tt>, has been added. </p>
<p> This is like <tt>&quot;SvTRUE&quot;</tt>, except that it does not process magic. It uses the new <tt>&quot;sv_2bool_flags&quot;</tt> function.</p>
<dt>&bull;</p>
<dd> <tt>&quot;sv_catsv_flags&quot;</tt> no longer calls <tt>&quot;mg_get&quot;</tt> on its second argument (the source string) if the flags passed to it do not include <font SIZE="-1">SV_GMAGIC</font>. So it now matches the documentation.</p>
<dt>&bull;</p>
<dd> A new interface has been added for custom check hooks on subroutines. See &#8220;Custom per-subroutine check hooks&#8221;, above.</p>
<dt>&bull;</p>
<dd> List op building functions have been added to the <font SIZE="-1">API</font>. See op_append_elem, op_append_list, and op_prepend_elem.</p>
<dt>&bull;</p>
<dd> The <font SIZE="-1">LINKLIST</font> macro, part of op building that constructs the execution-order op chain, has been added to the <font SIZE="-1">API</font>.</p>
<dt>&bull;</p>
<dd> Many functions ending with pvn now have equivalent pv/pvs/sv versions.</p>
<dt>&bull;</p>
<dd> The <tt>&quot;save_freeop&quot;</tt>, <tt>&quot;save_op&quot;</tt>, <tt>&quot;save_pushi32ptr&quot;</tt> and <tt>&quot;save_pushptrptr&quot;</tt> functions have been added to the <font SIZE="-1">API</font>.</p>
<dt>&bull;</p>
<dd> The new <font SIZE="-1">API</font> function <tt>&quot;parse_stmtseq()&quot;</tt> parses a sequence of statements, up to closing brace or <font SIZE="-1">EOF</font>.</dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</p>
<dd> A regular expression match in the right-hand side of a global substitution (<tt>&quot;s///g&quot;</tt>) that is in the same scope will no longer cause match variables to have the wrong values on subsequent iterations. This can happen when an array or hash subscript is interpolated in the right-hand side, as in <tt>&quot;s|(.)|@a{ print($1), /./ }|g&quot;</tt> [perl #19078] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3//Public/Bug/Display.html?id=19078">http://rt.perl.org/rt3//Public/Bug/Display.html?id=19078</a>&gt;.</p>
<dt>&bull;</p>
<dd> Constant-folding used to cause </p>
<pre>
  $text =~ ( 1 ? /phoo/ : /bear/)
</pre>
<p> to turn into </p>
<pre>
  $text =~ /phoo/
</pre>
<p> at compile time. Now it correctly matches against <tt>$_</tt> [perl #20444] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3//Public/Bug/Display.html?id=20444">http://rt.perl.org/rt3//Public/Bug/Display.html?id=20444</a>&gt;.</p>
<dt>&bull;</p>
<dd> Parsing Perl code (either with string <tt>&quot;eval&quot;</tt> or by loading modules) from within a <tt>&quot;UNITCHECK&quot;</tt> block no longer causes the interpreter to crash [perl #70614] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3//Public/Bug/Display.html?id=70614">http://rt.perl.org/rt3//Public/Bug/Display.html?id=70614</a>&gt;.</p>
<dt>&bull;</p>
<dd> When <tt>&quot;-d&quot;</tt> is used on the shebang (<tt>&quot;#!&quot;</tt>) line, the debugger now has access to the lines of the main program. In the past, this sometimes worked and sometimes did not, depending on what order things happened to be arranged in memory [perl #71806] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3//Public/Bug/Display.html?id=71806">http://rt.perl.org/rt3//Public/Bug/Display.html?id=71806</a>&gt;.</p>
<dt>&bull;</p>
<dd> The <tt>&quot;y///&quot;</tt> or <tt>&quot;tr///&quot;</tt> operator now calls get-magic (e.g., the <tt>&quot;FETCH&quot;</tt> method of a tie) on its left-hand side just once, not twice [perl #76814] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3//Public/Bug/Display.html?id=76814">http://rt.perl.org/rt3//Public/Bug/Display.html?id=76814</a>&gt;.</p>
<dt>&bull;</p>
<dd> String comparison (<tt>&quot;eq&quot;</tt>, <tt>&quot;ne&quot;</tt>, <tt>&quot;lt&quot;</tt>, <tt>&quot;gt&quot;</tt>, <tt>&quot;le&quot;</tt>, <tt>&quot;ge&quot;</tt> and <tt>&quot;cmp&quot;</tt>) and logical not (<tt>&quot;not&quot;</tt> and <tt>&quot;!&quot;</tt>) operators no longer call magic (e.g., tie methods) twice on their operands [perl #76814] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3//Public/Bug/Display.html?id=76814">http://rt.perl.org/rt3//Public/Bug/Display.html?id=76814</a>&gt;. </p>
<p> This bug was introduced in an earlier 5.13 release, and does not affect perl 5.12.</p>
<dt>&bull;</p>
<dd> When a tied (or other magic) variable is used as, or in, a regular expression, it no longer has its <tt>&quot;FETCH&quot;</tt> method called twice [perl #76814] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3//Public/Bug/Display.html?id=76814">http://rt.perl.org/rt3//Public/Bug/Display.html?id=76814</a>&gt;. </p>
<p> This bug was introduced in an earlier 5.13 release, and does not affect perl 5.12.</p>
<dt>&bull;</p>
<dd> The <tt>&quot;-C&quot;</tt> command line option can now be followed by other options [perl #72434] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3//Public/Bug/Display.html?id=72434">http://rt.perl.org/rt3//Public/Bug/Display.html?id=72434</a>&gt;.</p>
<dt>&bull;</p>
<dd> Assigning a glob to a <font SIZE="-1">PVLV</font> used to convert it to a plain string. Now it works correctly, and a <font SIZE="-1">PVLV</font> can hold a glob. This would happen when a nonexistent hash or array element was passed to a subroutine: </p>
<pre><code>
sub
{
    $_[0] = *foo
    } -&gt; ($hash{key});
#$_[0] would have been the string "*main::foo"
</code></pre>
<p> It also happened when a glob was assigned to, or returned from, an element of a tied array or hash [perl #36051] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3//Public/Bug/Display.html?id=36051">http://rt.perl.org/rt3//Public/Bug/Display.html?id=36051</a>&gt;.</p>
<dt>&bull;</p>
<dd> Creating a new thread when directory handles were open used to cause a crash, because the handles were not cloned, but simply passed to the new thread, resulting in a double free. </p>
<p> Now directory handles are cloned properly, on systems that have a <tt>&quot;fchdir&quot;</tt> function. On other systems, new threads simply do not inherit directory handles from their parent threads [perl #75154] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=75154">http://rt.perl.org/rt3/Public/Bug/Display.html?id=75154</a>&gt;.</p>
<dt>&bull;</p>
<dd> The regular expression parser no longer hangs when parsing <tt>&quot;\18&quot;</tt> and <tt>&quot;\88&quot;</tt>. </p>
<p> This bug was introduced in version 5.13.5 and did not affect earlier versions [perl #78058] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=78058">http://rt.perl.org/rt3/Public/Bug/Display.html?id=78058</a>&gt;.</p>
<dt>&bull;</p>
<dd> Subroutine redefinition works once more in the debugger [perl #48332] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=48332">http://rt.perl.org/rt3/Public/Bug/Display.html?id=48332</a>&gt;.</p>
<dt>&bull;</p>
<dd> The <tt>&quot;&amp;&quot;</tt> <tt>&quot;|&quot;</tt> <tt>&quot;^&quot;</tt> bitwise operators no longer coerce read-only arguments [perl #20661] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=20661">http://rt.perl.org/rt3/Public/Bug/Display.html?id=20661</a>&gt;.</p>
<dt>&bull;</p>
<dd> Stringifying a scalar containing -0.0 no longer has the affect of turning false into true [perl #45133] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=45133">http://rt.perl.org/rt3/Public/Bug/Display.html?id=45133</a>&gt;.</p>
<dt>&bull;</p>
<dd> Aliasing packages by assigning to globs or deleting packages by deleting their containing stash elements used to have erratic effects on method resolution, because the internal &#8216;isa&#8217; caches were not reset. This has been fixed.</p>
<dt>&bull;</p>
<dd> <tt>&quot;sort&quot;</tt> with a custom sort routine could crash if too many nested subroutine calls occurred from within the sort routine [perl #77930] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=77930">http://rt.perl.org/rt3/Public/Bug/Display.html?id=77930</a>&gt;. </p>
<p> This bug was introduced in an earlier 5.13 release, and did not affect perl 5.12.</p>
<dt>&bull;</p>
<dd> The <tt>&quot;eval_sv&quot;</tt> and <tt>&quot;eval_pv&quot;</tt> C functions now set <tt>$@</tt> correctly when there is a syntax error and no <tt>&quot;G_KEEPERR&quot;</tt> flag, and never set it if the <tt>&quot;G_KEEPERR&quot;</tt> flag is present [perl #3719] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=3719">http://rt.perl.org/rt3/Public/Bug/Display.html?id=3719</a>&gt;.</p>
<dt>&bull;</p>
<dd> Nested <tt>&quot;map&quot;</tt> and <tt>&quot;grep&quot;</tt> blocks no longer leak memory when processing large lists [perl #48004] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=48004">http://rt.perl.org/rt3/Public/Bug/Display.html?id=48004</a>&gt;.</p>
<dt>&bull;</p>
<dd> Malformed <tt>&quot;version&quot;</tt> objects no longer cause crashes [perl #78286] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=78286">http://rt.perl.org/rt3/Public/Bug/Display.html?id=78286</a>&gt;.</p>
<dt>&bull;</p>
<dd> The interpreter no longer crashes when freeing deeply-nested arrays of arrays. Hashes have not been fixed yet [perl #44225] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=44225">http://rt.perl.org/rt3/Public/Bug/Display.html?id=44225</a>&gt;.</p>
<dt>&bull;</p>
<dd> The mechanism for freeing objects in globs used to leave dangling pointers to freed SVs, meaning Perl users could see corrupted state during destruction. </p>
<p> Perl now only frees the affected slots of the <font SIZE="-1">GV</font>, rather than freeing the <font SIZE="-1">GV</font> itself. This makes sure that there are no dangling refs or corrupted state during destruction.</p>
<dt>&bull;</p>
<dd> The typeglob <tt>&quot;*,&quot;</tt>, which holds the scalar variable <tt>$,</tt> (output field separator), had the wrong reference count in child threads.</p>
<dt>&bull;</p>
<dd> <tt>&quot;splice&quot;</tt> now calls set-magic. This means that, for instance, changes made by <tt>&quot;splice @ISA&quot;</tt> are respected by method calls [perl #78400] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=78400">http://rt.perl.org/rt3/Public/Bug/Display.html?id=78400</a>&gt;.</p>
<dt>&bull;</p>
<dd> <tt>&quot;use v5.8&quot;</tt> no longer leaks memory [perl #78436] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=78436">http://rt.perl.org/rt3/Public/Bug/Display.html?id=78436</a>&gt;.</p>
<dt>&bull;</p>
<dd> The <font SIZE="-1">XS</font> multicall <font SIZE="-1">API</font> no longer causes subroutines to lose reference counts if called via the multicall interface from within those very subroutines. This affects modules like List::Util. Calling one of its functions with an active subroutine as the first argument could cause a crash [perl #78070] &lt;<a rel="nofollow" href="http://rt.perl.org/rt3/Public/Bug/Display.html?id=78070">http://rt.perl.org/rt3/Public/Bug/Display.html?id=78070</a>&gt;.</dl>
<h2>Errata</h2>
<dl>
<dt>&bull;</p>
<dd> Fixed a typo in perl5135delta regarding array slices and smart matching</dl>
<h2>Acknowledgements</h2>
<p> Perl 5.13.6 represents approximately one month of development since Perl 5.13.5 and contains 67920 lines of changes across 566 files from 47 authors and committers: </p>
<p> A. Sinan Unur, Aaron Crane, Alex Davies, Ali Polatel, Allen Smith, Andrew Rodland, Andy Dougherty, Ben Morrow, brian d foy, Casey West, Chip Salzenberg, Chris &#8216;BinGOs&#8217; Williams, Craig A. Berry, David Golden, David Mitchell, Eric Brine, Father Chrysostomos, Florian Ragwitz, George Greer, gregor herrmann, Jan Dubois, Jerry D. Hedden, Jesse Vincent, Joshua Pritikin, Karl Williamson, kmx, Michael G Schwern, Mike Kelly, Nicholas Clark, Paul Green, Rafael Garcia-Suarez, Renee Baecker, Ricardo Signes, Sisyphus, Slaven Rezic, Steffen Mu.ller, Steve Hay, Sullivan Beck, Tatsuhiko Miyagawa, Todd Rinaldo, Tony Cook, Tye McQueen, Vernon Lyon, Walt Mankowski, Zefram, Zsban Ambrus, var Arnfjo.rd<i>&#8211;</i> Bjarmason. </p>
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
