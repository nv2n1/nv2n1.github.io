---
title: "perl589delta(1)"
name: "perl589delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl589delta/"
description: "perl589delta – what is new for perl v5.8.9"
---

<h2 class="name">NAME</h2>
<p> perl589delta &#8211; what is new for perl v5.8.9 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.8.8 release and the 5.8.9 release.</p>
<h2>Notice</h2>
<p> The 5.8.9 release will be the last significant release of the 5.8.x series. Any future releases of 5.8.x will likely only be to deal with security issues, and platform build failures. Hence you should look to migrating to 5.10.x, if you have not started already. See &#8220;Known Problems&#8221; for more information.</p>
<h2>Incompatible Changes</h2>
<p> A particular construction in the source code of extensions written in C<font SIZE="-2">++</font> may need changing. See &#8220;Changed Internals&#8221; for more details. All extensions written in C, most written in C<font SIZE="-2">++</font>, and all existing compiled extensions are unaffected. This was necessary to improve C<font SIZE="-2">++</font> support. </p>
<p> Other than this, there are no changes intentionally incompatible with 5.8.8. If any exist, they are bugs and reports are welcome.</p>
<h2>Core Enhancements</h2>
<h3>Unicode Character Database 5.1.0.</h3>
<p> The copy of the Unicode Character Database included in Perl 5.8 has been updated to 5.1.0 from 4.1.0. See &lt;<a rel="nofollow" href="http://www.unicode.org/versions/Unicode5.1.0/#NotableChanges">http://www.unicode.org/versions/Unicode5.1.0/#NotableChanges</a>&gt; for the notable changes.</p>
<h3>stat and -X on directory handles</h3>
<p> It is now possible to call <tt>&quot;stat&quot;</tt> and the <tt>&quot;-X&quot;</tt> filestat operators on directory handles. As both directory and file handles are barewords, there can be ambiguities over which was intended. In these situations the file handle semantics are preferred. Both also treat <tt>*FILE{IO}</tt> filehandles like <tt>*FILE</tt> filehandles.</p>
<h3>Source filters in @INC</h3>
<p> It&#8217;s possible to enhance the mechanism of subroutine hooks in <tt>@INC</tt> by adding a source filter on top of the filehandle opened and returned by the hook. This feature was planned a long time ago, but wasn&#8217;t quite working until now. See &#8220;require&#8221; in perlfunc for details. (Nicholas Clark)</p>
<h3>Exceptions in constant folding</h3>
<p> The constant folding routine is now wrapped in an exception handler, and if folding throws an exception (such as attempting to evaluate 0/0), perl now retains the current optree, rather than aborting the whole program. Without this change, programs would not compile if they had expressions that happened to generate exceptions, even though those expressions were in code that could never be reached at runtime. (Nicholas Clark, Dave Mitchell)</p>
<h3>no VERSION</h3>
<p> You can now use <tt>&quot;no&quot;</tt> followed by a version number to specify that you want to use a version of perl older than the specified one.</p>
<h3>Improved internal <font SIZE="-1">UTF-8</font> caching code</h3>
<p> The code that caches calculated <font SIZE="-1">UTF-8</font> byte offsets for character offsets for a string has been re-written. Several bugs have been located and eliminated, and the code now makes better use of the information it has, so should be faster. In particular, it doesn&#8217;t scan to the end of a string before calculating an offset within the string, which should speed up some operations on long strings. It is now possible to disable the caching code at run time, to verify that it is not the cause of suspected problems.</p>
<h3>Runtime relocatable installations</h3>
<p> There is now <i>Configure</i> support for creating a perl tree that is relocatable at run time. see &#8220;Relocatable installations&#8221;.</p>
<h3>New internal variables</h3>
<dl>
<dt>&quot;${^CHILD_ERROR_NATIVE}&quot;</dt>
<dd> This variable gives the native status returned by the last pipe close, backtick command, successful call to <tt>&quot;wait&quot;</tt> or <tt>&quot;waitpid&quot;</tt>, or from the <tt>&quot;system&quot;</tt> operator. See perlvar for details. (Contributed by Gisle Aas.)</dd>
<dt>&quot;${^UTF8CACHE}&quot;</dt>
<dd> This variable controls the state of the internal <font SIZE="-1">UTF-8</font> offset caching code. 1 for on (the default), 0 for off, -1 to debug the caching code by checking all its results against linear scans, and panicking on any discrepancy.</dd></dl>
<h3>readpipe is now overridable</h3>
<p> The built-in function <tt>&quot;readpipe&quot;</tt> is now overridable. Overriding it permits also to override its operator counterpart, <tt>&quot;qx//&quot;</tt> (also known as <tt>&quot;``&quot;</tt>).</p>
<h3>simple exception handling macros</h3>
<p> Perl 5.8.9 (and 5.10.0 onwards) now provides a couple of macros to do very basic exception handling in <font SIZE="-1">XS</font> modules. You can use these macros if you call code that may <tt>&quot;croak&quot;</tt>, but you need to do some cleanup before giving control back to Perl. See &#8220;Exception Handling&#8221; in perlguts for more details.</p>
<h3>-D option enhancements</h3>
<dl>
<dt>&bull;</dt>
<dd> <tt>&quot;-Dq&quot;</tt> suppresses the <i></i><font SIZE="-1"><i>EXECUTING&#8230;</i></font><i></i> message when running under <tt>&quot;-D&quot;</tt></dd>
<dt>&bull;</dt>
<dd> <tt>&quot;-Dl&quot;</tt> logs runops loop entry and exit, and jump level popping.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;-Dv&quot;</tt> displays the process id as part of the trace output.</dd></dl>
<h3>XS-assisted <font SIZE="-1">SWASHGET</font></h3>
<p> Some pure-perl code that the regexp engine was using to retrieve Unicode properties and transliteration mappings has been reimplemented in <font SIZE="-1">XS</font> for faster execution. (<font SIZE="-1">SADAHIRO</font> Tomoyuki)</p>
<h3>Constant subroutines</h3>
<p> The interpreter internals now support a far more memory efficient form of inlineable constants. Storing a reference to a constant value in a symbol table is equivalent to a full typeglob referencing a constant subroutine, but using about 400 bytes less memory. This proxy constant subroutine is automatically upgraded to a real typeglob with subroutine if necessary. The approach taken is analogous to the existing space optimisation for subroutine stub declarations, which are stored as plain scalars in place of the full typeglob. </p>
<p> However, to aid backwards compatibility of existing code, which (wrongly) does not expect anything other than typeglobs in symbol tables, nothing in core uses this feature, other than the regression tests. </p>
<p> Stubs for prototyped subroutines have been stored in symbol tables as plain strings, and stubs for unprototyped subroutines as the number -1, since 5.005, so code which assumes that the core only places typeglobs in symbol tables has been making incorrect assumptions for over 10 years.</p>
<h2>New Platforms</h2>
<p> Compile support added for:</p>
<dl>
<dt>&bull;</dt>
<dd> DragonFlyBSD</dd>
<dt>&bull;</dt>
<dd> MidnightBSD</dd>
<dt>&bull;</dt>
<dd> MirOS <font SIZE="-1">BSD</font></dd>
<dt>&bull;</dt>
<dd> <font SIZE="-1">RISC OS</font></dd>
<dt>&bull;</dt>
<dd> Cray XT4/Catamount</dd></dl>
<h2>Modules and Pragmata</h2>
<h3>New Modules</h3>
<dl>
<dt>&bull;</dt>
<dd> <tt>&quot;Module::Pluggable&quot;</tt> is a simple framework to create modules that accept pluggable sub-modules. The bundled version is 3.8</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Module::CoreList&quot;</tt> is a hash of hashes that is keyed on perl version as indicated in <tt>$]</tt>. The bundled version is 2.17</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Win32API::File&quot;</tt> now available in core on Microsoft Windows. The bundled version is 0.1001_01</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Devel::InnerPackage&quot;</tt> finds all the packages defined by a single file. It is part of the <tt>&quot;Module::Pluggable&quot;</tt> distribution. The bundled version is 0.3</dd></dl>
<h3>Updated Modules</h3>
<dl>
<dt>&bull;</dt>
<dd> <tt>&quot;attributes&quot;</tt> upgraded to version 0.09</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;AutoLoader&quot;</tt> upgraded to version 5.67</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;AutoSplit&quot;</tt> upgraded to 1.06</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;autouse&quot;</tt> upgraded to version 1.06</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;B&quot;</tt> upgraded from 1.09_01 to 1.19</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> provides new pad related abstraction macros <tt>&quot;B::NV::COP_SEQ_RANGE_LOW&quot;</tt>, <tt>&quot;B::NV::COP_SEQ_RANGE_HIGH&quot;</tt>, <tt>&quot;B::NV::PARENT_PAD_INDEX&quot;</tt>, <tt>&quot;B::NV::PARENT_FAKELEX_FLAGS&quot;</tt>, which hides the difference in storage in 5.10.0 and later.</dd>
<dt>&bull;</dt>
<dd> provides <tt>&quot;B::sub_generation&quot;</tt>, which exposes <tt>&quot;PL_sub_generation&quot;</tt></dd>
<dt>&bull;</dt>
<dd> provides <tt>&quot;B::GV::isGV_with_GP&quot;</tt>, which on pre-5.10 perls always returns true.</dd>
<dt>&bull;</dt>
<dd> New type <tt>&quot;B::HE&quot;</tt> added with methods <tt>&quot;VAL&quot;</tt>, <tt>&quot;HASH&quot;</tt> and <tt>&quot;SVKEY_force&quot;</tt></dd>
<dt>&bull;</dt>
<dd> The <tt>&quot;B::GVf_IMPORTED_CV&quot;</tt> flag is now set correctly when a proxy constant subroutine is imported.</dd>
<dt>&bull;</dt>
<dd> bugs fixed in the handling of <tt>&quot;PMOP&quot;</tt>s.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;B::BM::PREVIOUS&quot;</tt> returns now <tt>&quot;U32&quot;</tt>, not <tt>&quot;U16&quot;</tt>. <tt>&quot;B::CV::START&quot;</tt> and <tt>&quot;B:CV::ROOT&quot;</tt> return now <tt>&quot;NULL&quot;</tt> on an <font SIZE="-1">XSUB,</font> <tt>&quot;B::CV::XSUB&quot;</tt> and <tt>&quot;B::CV::XSUBANY&quot;</tt> return 0 on a non-XSUB.</dd></dl>
</dl>
<dl>
</dl>
<dt>&bull;</dt>
<dd> <tt>&quot;B::C&quot;</tt> upgraded to 1.05</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;B::Concise&quot;</tt> upgraded to 0.76</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> new option <tt>&quot;-src&quot;</tt> causes the rendering of each statement (starting with the nextstate <font SIZE="-1">OP</font>) to be preceded by the first line of source code that generates it.</dd>
<dt>&bull;</dt>
<dd> new option <tt>&quot;-stash=&quot;somepackage&quot;&quot;</tt>, <tt>&quot;require&quot;</tt>s &#8220;somepackage&#8221;, and then renders each function defined in its namespace.</dd>
<dt>&bull;</dt>
<dd> now has documentation of detailed hint symbols.</dd></dl>
</dl>
<dl>
</dl>
<dt>&bull;</dt>
<dd> <tt>&quot;B::Debug&quot;</tt> upgraded to version 1.05</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;B::Deparse&quot;</tt> upgraded to version 0.87</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> properly deparse <tt>&quot;print readpipe $x, $y&quot;</tt>.</dd>
<dt>&bull;</dt>
<dd> now handles <tt>&quot;''-&gt;()&quot;</tt>, <tt>&quot;::()&quot;</tt>, <tt>&quot;sub :: {}&quot;</tt>, <i>etc.</i> correctly [<font SIZE="-1">RT</font> #43010]. All bugs in parsing these kinds of syntax are now fixed: </dd>
<pre><code>
perl - MO = Deparse - e '"my %h = "-&gt;()' perl - MO = Deparse - e '::-&gt;()' perl - MO = Deparse - e 'sub :: {}' perl - MO = Deparse - e 'package a; sub a::b::c {}' perl - MO = Deparse - e 'sub the::main::road {}'
</code></pre>
<dt>&bull;</dt>
<dd> does <code>not</code> deparse <tt>$^H{v_string}</tt>, which is automatically set by the internals.</dd></dl>
</dl>
<dl>
</dl>
<dt>&bull;</dt>
<dd> <tt>&quot;B::Lint&quot;</tt> upgraded to version 1.11</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;B::Terse&quot;</tt> upgraded to version 1.05</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;base&quot;</tt> upgraded to version 2.13</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> loading a module via base.pm would mask a global <tt>$SIG{__DIE__}</tt> in that module.</dd>
<dt>&bull;</dt>
<dd> push all classes at once in <tt>@ISA</tt></dd></dl>
</dl>
<dl>
</dl>
<dt>&bull;</dt>
<dd> <tt>&quot;Benchmark&quot;</tt> upgraded to version 1.10</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;bigint&quot;</tt> upgraded to 0.23</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;bignum&quot;</tt> upgraded to 0.23</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;bigrat&quot;</tt> upgraded to 0.23</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;blib&quot;</tt> upgraded to 0.04</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Carp&quot;</tt> upgraded to version 1.10 </dd>
<p> The argument backtrace code now shows <tt>&quot;undef&quot;</tt> as <tt>&quot;undef&quot;</tt>, instead of a string <i>&#8220;undef&#8221;</i>.</p>
<dt>&bull;</dt>
<dd> <tt>&quot;CGI&quot;</tt> upgraded to version 3.42</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;charnames&quot;</tt> upgraded to 1.06</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;constant&quot;</tt> upgraded to version 1.17</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;CPAN&quot;</tt> upgraded to version 1.9301</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Cwd&quot;</tt> upgraded to version 3.29 with some platform specific improvements (including for <font SIZE="-1">VMS</font>).</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Data::Dumper&quot;</tt> upgraded to version 2.121_17</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> Fixes hash iterator current position with the pure Perl version [<font SIZE="-1">RT</font> #40668]</dd>
<dt>&bull;</dt>
<dd> Performance enhancements, which will be most evident on platforms where repeated calls to C&#8217;s <tt>&quot;realloc()&quot;</tt> are slow, such as Win32.</dd></dl>
</dl>
<dl>
</dl>
<dt>&bull;</dt>
<dd> <tt>&quot;DB_File&quot;</tt> upgraded to version 1.817</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;DB_Filter&quot;</tt> upgraded to version 0.02</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Devel::DProf&quot;</tt> upgraded to version 20080331.00</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Devel::Peek&quot;</tt> upgraded to version 1.04</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Devel::PPPort&quot;</tt> upgraded to version 3.14</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;diagnostics&quot;</tt> upgraded to version 1.16</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Digest&quot;</tt> upgraded to version 1.15</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Digest::MD5&quot;</tt> upgraded to version 2.37</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;DirHandle&quot;</tt> upgraded to version 1.02</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> now localises <tt>$.</tt>, <tt>$@</tt>, <tt>$!</tt>, <tt>$^E</tt>, and <tt>$?</tt> before closing the directory handle to suppress leaking any side effects of warnings about it already being closed.</dd></dl>
</dl>
<dl>
</dl>
<dt>&bull;</dt>
<dd> <tt>&quot;DynaLoader&quot;</tt> upgraded to version 1.09 </dd>
<p> <tt>&quot;DynaLoader&quot;</tt> can now dynamically load a loadable object from a file with a non-default file extension.</p>
<dt>&bull;</dt>
<dd> <tt>&quot;Encode&quot;</tt> upgraded to version 2.26 </dd>
<p> <tt>&quot;Encode::Alias&quot;</tt> includes a fix for encoding &#8220;646&#8221; on Solaris (better known as <font SIZE="-1">ASCII</font>).</p>
<dt>&bull;</dt>
<dd> <tt>&quot;English&quot;</tt> upgraded to version 1.03</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Errno&quot;</tt> upgraded to version 1.10</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Exporter&quot;</tt> upgraded to version 5.63</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;ExtUtils::Command&quot;</tt> upgraded to version 1.15</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;ExtUtils::Constant&quot;</tt> upgraded to version 0.21</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;ExtUtils::Embed&quot;</tt> upgraded to version 1.28</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;ExtUtils::Install&quot;</tt> upgraded to version 1.50_01</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;ExtUtils::Installed&quot;</tt> upgraded to version 1.43</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;ExtUtils::MakeMaker&quot;</tt> upgraded to version 6.48</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> support for <tt>&quot;INSTALLSITESCRIPT&quot;</tt> and <tt>&quot;INSTALLVENDORSCRIPT&quot;</tt> configuration.</dd></dl>
</dl>
<dl>
</dl>
<dt>&bull;</dt>
<dd> <tt>&quot;ExtUtils::Manifest&quot;</tt> upgraded to version 1.55</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;ExtUtils::ParseXS&quot;</tt> upgraded to version 2.19</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Fatal&quot;</tt> upgraded to version 1.06</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> allows built-ins in <tt>&quot;CORE::GLOBAL&quot;</tt> to be made fatal.</dd></dl>
</dl>
<dl>
</dl>
<dt>&bull;</dt>
<dd> <tt>&quot;Fcntl&quot;</tt> upgraded to version 1.06</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;fields&quot;</tt> upgraded to version 2.12</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;File::Basename&quot;</tt> upgraded to version 2.77</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;FileCache&quot;</tt> upgraded to version 1.07</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;File::Compare&quot;</tt> upgraded to 1.1005</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;File::Copy&quot;</tt> upgraded to 2.13</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> now uses 3-arg open.</dd></dl>
</dl>
<dl>
</dl>
<dt>&bull;</dt>
<dd> <tt>&quot;File::DosGlob&quot;</tt> upgraded to 1.01</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;File::Find&quot;</tt> upgraded to version 1.13</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;File::Glob&quot;</tt> upgraded to version 1.06</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> fixes spurious results with brackets inside braces.</dd></dl>
</dl>
<dl>
</dl>
<dt>&bull;</dt>
<dd> <tt>&quot;File::Path&quot;</tt> upgraded to version 2.07_02</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;File::Spec&quot;</tt> upgraded to version 3.29</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> improved handling of bad arguments.</dd>
<dt>&bull;</dt>
<dd> some platform specific improvements (including for <font SIZE="-1">VMS</font> and Cygwin), with an optimisation on <tt>&quot;abs2rel&quot;</tt> when handling both relative arguments.</dd></dl>
</dl>
<dl>
</dl>
<dt>&bull;</dt>
<dd> <tt>&quot;File::stat&quot;</tt> upgraded to version 1.01</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;File::Temp&quot;</tt> upgraded to version 0.20</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;filetest&quot;</tt> upgraded to version 1.02</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Filter::Util::Call&quot;</tt> upgraded to version 1.07</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Filter::Simple&quot;</tt> upgraded to version 0.83</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;FindBin&quot;</tt> upgraded to version 1.49</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;GDBM_File&quot;</tt> upgraded to version 1.09</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Getopt::Long&quot;</tt> upgraded to version 2.37</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Getopt::Std&quot;</tt> upgraded to version 1.06</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Hash::Util&quot;</tt> upgraded to version 0.06</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;if&quot;</tt> upgraded to version 0.05</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;IO&quot;</tt> upgraded to version 1.23 </dd>
<p> Reduced number of calls to <tt>&quot;getpeername&quot;</tt> in <tt>&quot;IO::Socket&quot;</tt></p>
<dt>&bull;</dt>
<dd> <tt>&quot;IPC::Open&quot;</tt> upgraded to version 1.03</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;IPC::Open3&quot;</tt> upgraded to version 1.03</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;IPC::SysV&quot;</tt> upgraded to version 2.00</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;lib&quot;</tt> upgraded to version 0.61</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> avoid warning about loading <i>.par</i> files.</dd></dl>
</dl>
<dl>
</dl>
<dt>&bull;</dt>
<dd> <tt>&quot;libnet&quot;</tt> upgraded to version 1.22</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;List::Util&quot;</tt> upgraded to 1.19</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Locale::Maketext&quot;</tt> upgraded to 1.13</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Math::BigFloat&quot;</tt> upgraded to version 1.60</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Math::BigInt&quot;</tt> upgraded to version 1.89</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Math::BigRat&quot;</tt> upgraded to version 0.22</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> implements new <tt>&quot;as_float&quot;</tt> method.</dd></dl>
</dl>
<dl>
</dl>
<dt>&bull;</dt>
<dd> <tt>&quot;Math::Complex&quot;</tt> upgraded to version 1.54.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Math::Trig&quot;</tt> upgraded to version 1.18.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;NDBM_File&quot;</tt> upgraded to version 1.07</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> improve <i>g++</i> handling for systems using <font SIZE="-1">GDBM</font> compatibility headers.</dd></dl>
</dl>
<dl>
</dl>
<dt>&bull;</dt>
<dd> <tt>&quot;Net::Ping&quot;</tt> upgraded to version 2.35</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;NEXT&quot;</tt> upgraded to version 0.61</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> fix several bugs with <tt>&quot;NEXT&quot;</tt> when working with <tt>&quot;AUTOLOAD&quot;</tt>, <tt>&quot;eval&quot;</tt> block, and within overloaded stringification.</dd></dl>
</dl>
<dl>
</dl>
<dt>&bull;</dt>
<dd> <tt>&quot;ODBM_File&quot;</tt> upgraded to 1.07</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;open&quot;</tt> upgraded to 1.06</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;ops&quot;</tt> upgraded to 1.02</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;PerlIO::encoding&quot;</tt> upgraded to version 0.11</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;PerlIO::scalar&quot;</tt> upgraded to version 0.06</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> [<font SIZE="-1">RT</font> #40267] <tt>&quot;PerlIO::scalar&quot;</tt> doesn&#8217;t respect readonly-ness.</dd></dl>
</dl>
<dl>
</dl>
<dt>&bull;</dt>
<dd> <tt>&quot;PerlIO::via&quot;</tt> upgraded to version 0.05</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Pod::Html&quot;</tt> upgraded to version 1.09</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Pod::Parser&quot;</tt> upgraded to version 1.35</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Pod::Usage&quot;</tt> upgraded to version 1.35</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;POSIX&quot;</tt> upgraded to version 1.15</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> <tt>&quot;POSIX&quot;</tt> constants that duplicate those in <tt>&quot;Fcntl&quot;</tt> are now imported from <tt>&quot;Fcntl&quot;</tt> and re-exported, rather than being duplicated by <tt>&quot;POSIX&quot;</tt></dd>
<dt>&bull;</dt>
<dd> <tt>&quot;POSIX::remove&quot;</tt> can remove empty directories.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;POSIX::setlocale&quot;</tt> safer to call multiple times.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;POSIX::SigRt&quot;</tt> added, which provides access to <font SIZE="-1">POSIX</font> realtime signal functionality on systems that support it.</dd></dl>
</dl>
<dl>
</dl>
<dt>&bull;</dt>
<dd> <tt>&quot;re&quot;</tt> upgraded to version 0.06_01</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Safe&quot;</tt> upgraded to version 2.16</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Scalar::Util&quot;</tt> upgraded to 1.19</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;SDBM_File&quot;</tt> upgraded to version 1.06</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;SelfLoader&quot;</tt> upgraded to version 1.17</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Shell&quot;</tt> upgraded to version 0.72</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;sigtrap&quot;</tt> upgraded to version 1.04</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Socket&quot;</tt> upgraded to version 1.81</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> this fixes an optimistic use of <tt>&quot;gethostbyname&quot;</tt></dd></dl>
</dl>
<dl>
</dl>
<dt>&bull;</dt>
<dd> <tt>&quot;Storable&quot;</tt> upgraded to 2.19</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Switch&quot;</tt> upgraded to version 2.13</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Sys::Syslog&quot;</tt> upgraded to version 0.27</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Term::ANSIColor&quot;</tt> upgraded to version 1.12</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Term::Cap&quot;</tt> upgraded to version 1.12</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Term::ReadLine&quot;</tt> upgraded to version 1.03</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Test::Builder&quot;</tt> upgraded to version 0.80</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Test::Harness&quot;</tt> upgraded version to 2.64</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> this makes it able to handle newlines.</dd></dl>
</dl>
<dl>
</dl>
<dt>&bull;</dt>
<dd> <tt>&quot;Test::More&quot;</tt> upgraded to version 0.80</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Test::Simple&quot;</tt> upgraded to version 0.80</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Text::Balanced&quot;</tt> upgraded to version 1.98</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Text::ParseWords&quot;</tt> upgraded to version 3.27</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Text::Soundex&quot;</tt> upgraded to version 3.03</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Text::Tabs&quot;</tt> upgraded to version 2007.1117</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Text::Wrap&quot;</tt> upgraded to version 2006.1117</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Thread&quot;</tt> upgraded to version 2.01</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Thread::Semaphore&quot;</tt> upgraded to version 2.09</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Thread::Queue&quot;</tt> upgraded to version 2.11</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> added capability to add complex structures (e.g., hash of hashes) to queues.</dd>
<dt>&bull;</dt>
<dd> added capability to dequeue multiple items at once.</dd>
<dt>&bull;</dt>
<dd> added new methods to inspect and manipulate queues: <tt>&quot;peek&quot;</tt>, <tt>&quot;insert&quot;</tt> and <tt>&quot;extract&quot;</tt></dd></dl>
</dl>
<dl>
</dl>
<dt>&bull;</dt>
<dd> <tt>&quot;Tie::Handle&quot;</tt> upgraded to version 4.2</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Tie::Hash&quot;</tt> upgraded to version 1.03</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Tie::Memoize&quot;</tt> upgraded to version 1.1</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> <tt>&quot;Tie::Memoize::EXISTS&quot;</tt> now correctly caches its results.</dd></dl>
</dl>
<dl>
</dl>
<dt>&bull;</dt>
<dd> <tt>&quot;Tie::RefHash&quot;</tt> upgraded to version 1.38</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Tie::Scalar&quot;</tt> upgraded to version 1.01</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Tie::StdHandle&quot;</tt> upgraded to version 4.2</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Time::gmtime&quot;</tt> upgraded to version 1.03</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Time::Local&quot;</tt> upgraded to version 1.1901</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Time::HiRes&quot;</tt> upgraded to version 1.9715 with various build improvements (including <font SIZE="-1">VMS</font>) and minor platform-specific bug fixes (including for HP-UX 11 ia64).</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;threads&quot;</tt> upgraded to 1.71</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> new thread state information methods: <tt>&quot;is_running&quot;</tt>, <tt>&quot;is_detached&quot;</tt> and <tt>&quot;is_joinable&quot;</tt>. <tt>&quot;list&quot;</tt> method enhanced to return running or joinable threads.</dd>
<dt>&bull;</dt>
<dd> new thread signal method: <tt>&quot;kill&quot;</tt></dd>
<dt>&bull;</dt>
<dd> added capability to specify thread stack size.</dd>
<dt>&bull;</dt>
<dd> added capability to control thread exiting behavior. Added a new <tt>&quot;exit&quot;</tt> method.</dd></dl>
</dl>
<dl>
</dl>
<dt>&bull;</dt>
<dd> <tt>&quot;threads::shared&quot;</tt> upgraded to version 1.27</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> smaller and faster implementation that eliminates one internal structure and the consequent level of indirection.</dd>
<dt>&bull;</dt>
<dd> user locks are now stored in a safer manner.</dd>
<dt>&bull;</dt>
<dd> new function <tt>&quot;shared_clone&quot;</tt> creates a copy of an object leaving shared elements as-is and deep-cloning non-shared elements.</dd>
<dt>&bull;</dt>
<dd> added new <tt>&quot;is_shared&quot;</tt> method.</dd></dl>
</dl>
<dl>
</dl>
<dt>&bull;</dt>
<dd> <tt>&quot;Unicode::Normalize&quot;</tt> upgraded to version 1.02</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Unicode::UCD&quot;</tt> upgraded to version 0.25</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;warnings&quot;</tt> upgraded to version 1.05_01</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;Win32&quot;</tt> upgraded to version 0.38</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> added new function <tt>&quot;GetCurrentProcessId&quot;</tt> which returns the regular Windows process identifier of the current process, even when called from within a fork.</dd></dl>
</dl>
<dl>
</dl>
<dt>&bull;</dt>
<dd> <tt>&quot;XSLoader&quot;</tt> upgraded to version 0.10</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;XS::APItest&quot;</tt> and <tt>&quot;XS::Typemap&quot;</tt> are for internal use only and hence no longer installed. Many more tests have been added to <tt>&quot;XS::APItest&quot;</tt>.</dd></dl>
<h2>Utility Changes</h2>
<h3>debugger upgraded to version 1.31</h3>
<dl>
<dt>&bull;</dt>
<dd> Andreas König contributed two functions to save and load the debugger history.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;NEXT::AUTOLOAD&quot;</tt> no longer emits warnings under the debugger.</dd>
<dt>&bull;</dt>
<dd> The debugger should now correctly find tty the device on <font SIZE="-1">OS X 10.5</font> and <font SIZE="-1">VMS</font> when the program <tt>&quot;fork&quot;</tt>s.</dd>
<dt>&bull;</dt>
<dd> <font SIZE="-1">LVALUE</font> subs now work inside the debugger.</dd></dl>
<h3><i>perlthanks</i></h3>
<p> Perl 5.8.9 adds a new utility <i>perlthanks</i>, which is a variant of <i>perlbug</i>, but for sending non-bug-reports to the authors and maintainers of Perl. Getting nothing but bug reports can become a bit demoralising &#8211; we&#8217;ll see if this changes things.</p>
<h3><i>perlbug</i></h3>
<p> <i>perlbug</i> now checks if you&#8217;re reporting about a non-core module and suggests you report it to the <font SIZE="-1">CPAN</font> author instead.</p>
<h3><i>h2xs</i></h3>
<dl>
<dt>&bull;</dt>
<dd> won&#8217;t define an empty string as a constant [<font SIZE="-1">RT</font> #25366]</dd>
<dt>&bull;</dt>
<dd> has examples for <tt>&quot;h2xs -X&quot;</tt></dd></dl>
<h3><i>h2ph</i></h3>
<dl>
<dt>&bull;</dt>
<dd> now attempts to deal sensibly with the difference in path implications between <tt>&quot;&quot;</tt> and <tt>&quot;&lt;&gt;&quot;</tt> quoting in <tt>&quot;#include&quot;</tt> statements.</dd>
<dt>&bull;</dt>
<dd> now generates correct code for <tt>&quot;#if defined A || defined B&quot;</tt> [<font SIZE="-1">RT</font> #39130]</dd></dl>
<h2>New Documentation</h2>
<p> As usual, the documentation received its share of corrections, clarifications and other nitfixes. More <tt>&quot;&quot;</tt> tags were added for indexing. </p>
<p> perlunitut is a tutorial written by Juerd Waalboer on Unicode-related terminology and how to correctly handle Unicode in Perl scripts. </p>
<p> perlunicode is updated in section user defined properties. </p>
<p> perluniintro has been updated in the example of detecting data that is not valid in particular encoding. </p>
<p> perlcommunity provides an overview of the Perl Community along with further resources. </p>
<p> <font SIZE="-1">CORE</font> documents the pseudo-namespace for Perl&#8217;s core routines.</p>
<h2>Changes to Existing Documentation</h2>
<p> perlglossary adds <i>deprecated modules and features</i> and <i>to be dropped modules</i>. </p>
<p> perlhack has been updated and added resources on smoke testing. </p>
<p> The Perl FAQs (<i>perlfaq1</i>..<i>perlfaq9</i>) have been updated. </p>
<p> perlcheat is updated with better details on <tt>&quot;\w&quot;</tt>, <tt>&quot;\d&quot;</tt>, and <tt>&quot;\s&quot;</tt>. </p>
<p> perldebug is updated with information on how to call the debugger. </p>
<p> perldiag documentation updated with <i>subroutine with an ampersand</i> on the argument to <tt>&quot;exists&quot;</tt> and <tt>&quot;delete&quot;</tt> and also several terminology updates on warnings. </p>
<p> perlfork documents the limitation of <tt>&quot;exec&quot;</tt> inside pseudo-processes. </p>
<p> perlfunc:</p>
<dl>
<dt>&bull;</dt>
<dd> Documentation is fixed in section <tt>&quot;caller&quot;</tt> and <tt>&quot;pop&quot;</tt>.</dd>
<dt>&bull;</dt>
<dd> Function <tt>&quot;alarm&quot;</tt> now mentions <tt>&quot;Time::HiRes::ualarm&quot;</tt> in preference to <tt>&quot;select&quot;</tt>.</dd>
<dt>&bull;</dt>
<dd> Regarding precedence in <tt>&quot;-X&quot;</tt>, filetest operators are the same as unary operators, but not regarding parsing and parentheses (spotted by Eirik Berg Hanssen).</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;reverse&quot;</tt> function documentation received scalar context examples.</dd></dl>
<p> perllocale documentation is adjusted for number localization and <tt>&quot;POSIX::setlocale&quot;</tt> to fix Debian bug #379463. </p>
<p> perlmodlib is updated with <tt>&quot;CPAN::API::HOWTO&quot;</tt> and <tt>&quot;Sys::Syslog::win32::Win32&quot;</tt> </p>
<p> perlre documentation updated to reflect the differences between <tt>&quot;[[:xxxxx:]]&quot;</tt> and <tt>&quot;\p{IsXxxxx}&quot;</tt> matches. Also added section on <tt>&quot;/g&quot;</tt> and <tt>&quot;/c&quot;</tt> modifiers. </p>
<p> perlreguts describe the internals of the regular expressions engine. It has been contributed by Yves Orton. </p>
<p> perlrebackslash describes all perl regular expression backslash and escape sequences. </p>
<p> perlrecharclass describes the syntax and use of character classes in Perl Regular Expressions. </p>
<p> perlrun is updated to clarify on the hash seed <i></i><font SIZE="-1"><i>PERL_HASH_SEED</i></font><i></i>. Also more information in options <tt>&quot;-x&quot;</tt> and <tt>&quot;-u&quot;</tt>. </p>
<p> perlsub example is updated to use a lexical variable for <tt>&quot;opendir&quot;</tt> syntax. </p>
<p> perlvar fixes confusion about real <font SIZE="-1">GID</font> <tt>$(</tt> and effective <font SIZE="-1">GID</font> <tt>$)</tt>. </p>
<p> Perl thread tutorial example is fixed in section &#8220;Queues: Passing Data Around&#8221; in perlthrtut and perlthrtut. </p>
<p> perlhack documentation extensively improved by Jarkko Hietaniemi and others. </p>
<p> perltoot provides information on modifying <tt>@UNIVERSAL::ISA</tt>. </p>
<p> perlport documentation extended to include different <tt>&quot;kill(-9, ...)&quot;</tt> semantics on Windows. It also clearly states <tt>&quot;dump&quot;</tt> is not supported on Win32 and cygwin. </p>
<p> <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> has been updated and modernised.</p>
<h2>Performance Enhancements</h2>
<dl>
<dt>&bull;</dt>
<dd> The default since perl 5.000 has been for perl to create an empty scalar with every new typeglob. The increased use of lexical variables means that most are now unused. Thanks to Nicholas Clark&#8217;s efforts, Perl can now be compiled with <tt>&quot;-DPERL_DONT_CREATE_GVSV&quot;</tt> to avoid creating these empty scalars. This will significantly decrease the number of scalars allocated for all configurations, and the number of scalars that need to be copied for ithread creation. Whilst this option is binary compatible with existing perl installations, it does change a long-standing assumption about the internals, hence it is not enabled by default, as some third party code may rely on the old behaviour. </dd>
<p> We would recommend testing with this configuration on new deployments of perl, particularly for multi-threaded servers, to see whether all third party code is compatible with it, as this configuration may give useful performance improvements. For existing installations we would not recommend changing to this configuration unless thorough testing is performed before deployment.</p>
<dt>&bull;</dt>
<dd> <tt>&quot;diagnostics&quot;</tt> no longer uses <tt>$&amp;</tt>, which results in large speedups for regexp matching in all code using it.</dd>
<dt>&bull;</dt>
<dd> Regular expressions classes of a single character are now treated the same as if the character had been used as a literal, meaning that code that uses char-classes as an escaping mechanism will see a speedup. (Yves Orton)</dd>
<dt>&bull;</dt>
<dd> Creating anonymous array and hash references (ie. <tt>&quot;[]&quot;</tt> and <tt>&quot;{}&quot;</tt>) now incurs no more overhead than creating an anonymous list or hash. Nicholas Clark provided changes with a saving of two ops and one stack push, which was measured as a slightly better than 5% improvement for these operations.</dd>
<dt>&bull;</dt>
<dd> Many calls to <tt>&quot;strlen()&quot;</tt> have been eliminated, either because the length was already known, or by adopting or enhancing APIs that pass lengths. This has been aided by the adoption of a <tt>&quot;my_sprintf()&quot;</tt> wrapper, which returns the correct C89 value &#8211; the length of the formatted string. Previously we could not rely on the return value of <tt>&quot;sprintf()&quot;</tt>, because on some ancient but extant platforms it still returns <tt>&quot;char *&quot;</tt>.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;index&quot;</tt> is now faster if the search string is stored in <font SIZE="-1">UTF-8</font> but only contains characters in the Latin-1 range.</dd>
<dt>&bull;</dt>
<dd> The Unicode swatch cache inside the regexp engine is now used. (the lookup had a key mismatch, present since the initial implementation). [<font SIZE="-1">RT</font> #42839]</dd></dl>
<h2>Installation and Configuration Improvements</h2>
<h3>Relocatable installations</h3>
<p> There is now <i>Configure</i> support for creating a relocatable perl tree. If you <i>Configure</i> with <tt>&quot;-Duserelocatableinc&quot;</tt>, then the paths in <tt>@INC</tt> (and everything else in <tt>%Config</tt>) can be optionally located via the path of the <i>perl</i> executable. </p>
<p> At start time, if any paths in <tt>@INC</tt> or <tt>&quot;Config&quot;</tt> that <i>Configure</i> marked as relocatable (by starting them with <tt>&quot;.../&quot;</tt>), then they are prefixed the directory of <tt>$^X</tt>. This allows the relocation can be configured on a per-directory basis, although the default with <tt>&quot;-Duserelocatableinc&quot;</tt> is that everything is relocated. The initial install is done to the original configured prefix.</p>
<h3>Configuration improvements</h3>
<p> <i>Configure</i> is now better at removing temporary files. Tom Callaway (from RedHat) also contributed patches that complete the set of flags passed to the compiler and the linker, in particular that <tt>&quot;-fPIC&quot;</tt> is now enabled on Linux. It will also croak when your <i>/dev/null</i> isn&#8217;t a device. </p>
<p> A new configuration variable <tt>&quot;d_pseudofork&quot;</tt> has been to <i>Configure</i>, and is available as <tt>$Config{d_pseudofork}</tt> in the <tt>&quot;Config&quot;</tt> module. This distinguishes real <tt>&quot;fork&quot;</tt> support from the pseudofork emulation used on Windows platforms. </p>
<p> <i>Config.pod</i> and <i>config.sh</i> are now placed correctly for cross-compilation. </p>
<p> <tt>$Config{useshrplib}</tt> is now &#8216;true&#8217; rather than &#8216;yes&#8217; when using a shared perl library.</p>
<h3>Compilation improvements</h3>
<p> Parallel makes should work properly now, although there may still be problems if <tt>&quot;make test&quot;</tt> is instructed to run in parallel. </p>
<p> Many compilation warnings have been cleaned up. A very stubborn compiler warning in <tt>&quot;S_emulate_eaccess()&quot;</tt> was killed after six attempts. <i>g++</i> support has been tuned, especially for FreeBSD. </p>
<p> <i>mkppport</i> has been integrated, and all <i>ppport.h</i> files in the core will now be autogenerated at build time (and removed during cleanup).</p>
<h3>Installation improvements.</h3>
<p> <i>installman</i> now works with <tt>&quot;-Duserelocatableinc&quot;</tt> and <tt>&quot;DESTDIR&quot;</tt>. </p>
<p> <i>installperl</i> no longer installs:</p>
<dl>
<dt>&bull;</dt>
<dd> static library files of statically linked extensions when a shared perl library is being used. (They are not needed. See &#8220;Windows&#8221; below).</dd>
<dt>&bull;</dt>
<dd> <i></i><font SIZE="-1"><i>SIGNATURE</i></font><i></i> and <i>PAUSE*.pub</i> (<font SIZE="-1">CPAN</font> files)</dd>
<dt>&bull;</dt>
<dd> <i></i><font SIZE="-1"><i>NOTES</i></font><i></i> and <i></i><font SIZE="-1"><i>PATCHING</i></font><i></i> (ExtUtils files)</dd>
<dt>&bull;</dt>
<dd> <i>perlld</i> and <i>ld2</i> (Cygwin files)</dd></dl>
<h3>Platform Specific Changes</h3>
<p> There are improved hints for <font SIZE="-1">AIX,</font> Cygwin, <font SIZE="-1">DEC/OSF,</font> FreeBSD, <font SIZE="-1">HP/UX,</font> Irix 6 Linux, MachTen, NetBSD, <font SIZE="-1">OS/390, QNX, SCO,</font> Solaris, SunOS, System V Release 5.x (UnixWare 7, OpenUNIX 8), Ultrix, <font SIZE="-1">UMIPS,</font> uts and <font SIZE="-1">VOS.</font> </p>
<p> <i>FreeBSD</i></p>
<dl>
<dt>&bull;</dt>
<dd> Drop <tt>&quot;-std=c89&quot;</tt> and <tt>&quot;-ansi&quot;</tt> if using <tt>&quot;long long&quot;</tt> as the main integral type, else in FreeBSD 6.2 (and perhaps other releases), system headers do not declare some functions required by perl.</dd></dl>
<p> <i>Solaris</i></p>
<dl>
<dt>&bull;</dt>
<dd> Starting with Solaris 10, we do not want versioned shared libraries, because those often indicate a private use only library. These problems could often be triggered when SUNWbdb (Berkeley <font SIZE="-1">DB</font>) was installed. Hence if Solaris 10 is detected set <tt>&quot;ignore_versioned_solibs=y&quot;</tt>.</dd></dl>
<p> <i></i><font SIZE="-1"><i>VMS</i></font><i></i></p>
<dl>
<dt>&bull;</dt>
<dd> Allow <font SIZE="-1">IEEE</font> math to be deselected on OpenVMS I64 (but it remains the default).</dd>
<dt>&bull;</dt>
<dd> Record <font SIZE="-1">IEEE</font> usage in <tt>&quot;config.h&quot;</tt></dd>
<dt>&bull;</dt>
<dd> Help older <font SIZE="-1">VMS</font> compilers by using <tt>&quot;ccflags&quot;</tt> when building <tt>&quot;munchconfig.exe&quot;</tt>.</dd>
<dt>&bull;</dt>
<dd> Don&#8217;t try to build old <tt>&quot;Thread&quot;</tt> extension on <font SIZE="-1">VMS</font> when <tt>&quot;-Duseithreads&quot;</tt> has been chosen.</dd>
<dt>&bull;</dt>
<dd> Passing a raw string of &#8220;NaN&#8221; to <i>nawk</i> causes a core dump &#8211; so the string has been changed to &#8220;*NaN*&#8221;</dd>
<dt>&bull;</dt>
<dd> <i>t/op/stat.t</i> tests will now test hard links on <font SIZE="-1">VMS</font> if they are supported.</dd></dl>
<p> <i>Windows</i></p>
<dl>
<dt>&bull;</dt>
<dd> When using a shared perl library <i>installperl</i> no longer installs static library files, import library files and export library files (of statically linked extensions) and empty bootstrap files (of dynamically linked extensions). This fixes a problem building PAR-Packer on Win32 with a debug build of perl.</dd>
<dt>&bull;</dt>
<dd> Various improvements to the win32 build process, including support for Visual C<font SIZE="-2">++</font> 2005 Express Edition (aka Visual C<font SIZE="-2">++</font> 8.x).</dd>
<dt>&bull;</dt>
<dd> <i>perl.exe</i> will now have an icon if built with MinGW or Borland.</dd>
<dt>&bull;</dt>
<dd> Improvements to the perl-static.exe build process.</dd>
<dt>&bull;</dt>
<dd> Add Win32 makefile option to link all extensions statically.</dd>
<dt>&bull;</dt>
<dd> The <i>WinCE</i> directory has been merged into the <i>Win32</i> directory.</dd>
<dt>&bull;</dt>
<dd> <tt>&quot;setlocale&quot;</tt> tests have been re-enabled for Windows <font SIZE="-1">XP</font> onwards.</dd></dl>
<h2>Selected Bug Fixes</h2>
<h3>Unicode</h3>
<p> Many many bugs related to the internal Unicode implementation (<font SIZE="-1">UTF-8</font>) have been fixed. In particular, long standing bugs related to returning Unicode via <tt>&quot;tie&quot;</tt>, overloading or <tt>$@</tt> are now gone, some of which were never reported. </p>
<p> <tt>&quot;unpack&quot;</tt> will internally convert the string back from <font SIZE="-1">UTF-8</font> on numeric types. This is a compromise between the full consistency now in 5.10, and the current behaviour, which is often used as a &#8220;feature&#8221; on string types. </p>
<p> Using <tt>&quot;:crlf&quot;</tt> and <tt>&quot;UTF-16&quot;</tt> <font SIZE="-1">IO</font> layers together will now work. </p>
<p> Fixed problems with <tt>&quot;split&quot;</tt>, Unicode <tt>&quot;/\s+/&quot;</tt> and <tt>&quot;/</tt> \0/&quot;</code>. </p>
<p> Fixed bug <font SIZE="-1">RT</font> #40641 &#8211; encoding of Unicode characters in regular expressions. </p>
<p> Fixed a bug where using certain patterns in a regexp led to a panic. [<font SIZE="-1">RT</font> #45337] </p>
<p> Perl no longer segfaults (due to infinite internal recursion) if the locale&#8217;s character is not <font SIZE="-1">UTF-8</font> [<font SIZE="-1">RT</font> #41442]: </p>
<pre><code>    use open ':locale';
    print STDERR &quot;\x{201e}&quot;; # &amp;bdquo;
</code></pre>
<h3>PerlIO</h3>
<p> Inconsistencies have been fixed in the reference counting PerlIO uses to keep track of Unix file descriptors, and the <font SIZE="-1">API</font> used by <font SIZE="-1">XS</font> code to manage getting and releasing <code>&quot;FILE *&quot;</code>s  </p>
<h3>Magic</h3>
<p> Several bugs have been fixed in Magic, the internal system used to implement features such as <code>&quot;tie&quot;</code>, tainting and threads sharing. </p>
<p> <code>&quot;undef @array&quot;</code> on a tied array now correctly calls the <code>&quot;CLEAR&quot;</code> method. </p>
<p> Some of the bitwise ops were not checking whether their arguments were magical before using them. [<font SIZE="-1">RT</font> #24816] </p>
<p> Magic is no longer invoked twice by the expression <code>&quot;\&amp;$x&quot;</code> </p>
<p> A bug with assigning large numbers and tainting has been resolved. [<font SIZE="-1">RT</font> #40708] </p>
<p> A new entry has been added to the <font SIZE="-1">MAGIC</font> vtable &#8211; <code>&quot;svt_local&quot;</code>. This is used when copying magic to the new value during <code>&quot;local&quot;</code>, allowing certain problems with localising shared variables to be resolved. </p>
<p> For the implementation details, see ``Magic Virtual Tables&#8217;&#8216; in perlguts.  </p>
<h3>Reblessing overloaded objects now works</h3>
<p> Internally, perl object-ness is on the referent, not the reference, even though methods can only be called via a reference. However, the original implementation of overloading stored flags related to overloading on the reference, relying on the flags being copied when the reference was copied, or set at the creation of a new reference. This manifests in a bug &#8211; if you rebless an object from a class that has overloading, into one that does not, then any other existing references think that they (still) point to an overloaded object, choose these C code paths, and then throw errors. Analogously, blessing into an overloaded class when other references exist will result in them not using overloading. </p>
<p> The implementation has been fixed for 5.10, but this fix changes the semantics of flag bits, so is not binary compatible, so can&#8217;t be applied to 5.8.9. However, 5.8.9 has a work-around that implements the same bug fix. If the referent has multiple references, then all the other references are located and corrected. A full search is avoided whenever possible by scanning lexicals outwards from the current subroutine, and the argument stack. </p>
<p> A certain well known Linux vendor applied incomplete versions of this bug fix to their <i>/usr/bin/perl</i> and then prematurely closed bug reports about performance issues without consulting back upstream. This not being enough, they then proceeded to ignore the necessary fixes to these unreleased changes for 11 months, until massive pressure was applied by their long-suffering paying customers, catalysed by the failings being featured on a prominent blog and Slashdot.  </p>
<h3>strict now propagates correctly into string evals</h3>
<p> Under 5.8.8 and earlier: </p>
<pre><code>    $ perl5.8.8 -e 'use strict; eval &quot;use foo bar&quot; or die $@'
    Can't locate foo.pm in @INC (@INC contains: ... .) at (eval 1) line 2.
    BEGIN failed--compilation aborted at (eval 1) line 2.
</code></pre>
<p> Under 5.8.9 and later: </p>
<pre><code>    $ perl5.8.9 -e 'use strict; eval &quot;use foo bar&quot; or die $@'
    Bareword &quot;bar&quot; not allowed while &quot;strict subs&quot; in use at (eval 1) line 1.
</code></pre>
<p> This may cause problems with programs that parse the error message and rely on the buggy behaviour.  </p>
<h3>Other fixes</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> The tokenizer no longer treats <code>&quot;=cute&quot;</code> (and other words beginning with <code>&quot;=cut&quot;</code>) as a synonym for <code>&quot;=cut&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Calling <code>&quot;CORE::require&quot;</code> </p>
<p> <code>&quot;CORE::require&quot;</code> and <code>&quot;CORE::do&quot;</code> were always parsed as <code>&quot;require&quot;</code> and <code>&quot;do&quot;</code> when they were overridden. This is now fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Stopped memory leak on long <i>/etc/groups</i> entries. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;while (my $x ...) { ...; redo }&quot;</code> shouldn&#8217;t <code>&quot;undef $x&quot;</code>. </p>
<p> In the presence of <code>&quot;my&quot;</code> in the conditional of a <code>&quot;while()&quot;</code>, <code>&quot;until()&quot;</code>, or <code>&quot;for(;;)&quot;</code> loop, we now add an extra scope to the body so that <code>&quot;redo&quot;</code> doesn&#8217;t <code>&quot;undef&quot;</code> the lexical. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;encoding&quot;</code> pragma now correctly ignores anything following an <code>&quot;@&quot;</code> character in the <code>&quot;LC_ALL&quot;</code> and <code>&quot;LANG&quot;</code> environment variables. [<font SIZE="-1">RT</font> # 49646] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A segfault observed with some <i>gcc</i> 3.3 optimisations is resolved. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A possible segfault when <code>&quot;unpack&quot;</code> used in scalar context with <code>&quot;()&quot;</code> groups is resolved. [<font SIZE="-1">RT</font> #50256] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Resolved issue where <code>$!</code> could be changed by a signal handler interrupting a <code>&quot;system&quot;</code> call. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed bug <font SIZE="-1">RT</font> #37886, symbolic dereferencing was allowed in the argument of <code>&quot;defined&quot;</code> even under the influence of <code>&quot;use strict &#8216;refs&#8217;&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed bug <font SIZE="-1">RT</font> #43207, where <code>&quot;lc&quot;</code>/<code>&quot;uc&quot;</code> inside <code>&quot;sort&quot;</code> affected the return value. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed bug <font SIZE="-1">RT</font> #45607, where <code>&quot;*{&quot;BONK&quot;} = \&amp;{&quot;BONK&quot;}&quot;</code> didn&#8217;t work correctly. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed bug <font SIZE="-1">RT</font> #35878, croaking from a <font SIZE="-1">XSUB</font> called via <code>&quot;goto &amp;xsub&quot;</code> corrupts perl internals. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed bug <font SIZE="-1">RT</font> #32539, <i>DynaLoader.o</i> is moved into <i>libperl.so</i> to avoid the need to statically link DynaLoader into the stub perl executable. With this <i>libperl.so</i> provides everything needed to get a functional embedded perl interpreter to run. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fix bug <font SIZE="-1">RT</font> #36267 so that assigning to a tied hash doesn&#8217;t change the underlying hash. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fix bug <font SIZE="-1">RT</font> #6006, regexp replaces using large replacement variables fail some of the time, <i>i.e.</i> when substitution contains something like <code>&quot;${10}&quot;</code> (note the bracket) instead of just <code>$10</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fix bug <font SIZE="-1">RT</font> #45053, <code>&quot;Perl_newCONSTSUB()&quot;</code> is now thread safe. </p>
 </dd></dl>
<h3>Platform Specific Fixes</h3>
<p> <i>Darwin / MacOS X</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Various improvements to 64 bit builds. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Mutex protection added in <code>&quot;PerlIOStdio_close()&quot;</code> to avoid race conditions. Hopefully this fixes failures in the threads tests <i>free.t</i> and <i>blocks.t</i>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Added forked terminal support to the debugger, with the ability to update the window title. </p>
 </dd></dl>
<p> <i></i><font SIZE="-1"><i>OS/2</i></font><i></i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> A build problem with specifying <code>&quot;USE_MULTI&quot;</code> and <code>&quot;USE_ITHREADS&quot;</code> but without <code>&quot;USE_IMP_SYS&quot;</code> has been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;OS2::REXX&quot;</code> upgraded to version 1.04 </p>
 </dd></dl>
<p> <i>Tru64</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Aligned floating point build policies for <i>cc</i> and <i>gcc</i>. </p>
 </dd></dl>
<p> <i>RedHat Linux</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Revisited a patch from 5.6.1 for <font SIZE="-1">RH7.2</font> for Intel&#8217;s <i>icc</i> [<font SIZE="-1">RT</font> #7916], added an additional check for <code>$Config{gccversion}</code>. </p>
 </dd></dl>
<p> <i>Solaris/i386</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Use <code>&quot;-DPTR_IS_LONG&quot;</code> when using 64 bit integers </p>
 </dd></dl>
<p> <i></i><font SIZE="-1"><i>VMS</i></font><i></i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Fixed <code>&quot;PerlIO::Scalar&quot;</code> in-memory file record-style reads. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> pipe shutdown at process exit should now be more robust. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Bugs in <font SIZE="-1">VMS</font> exit handling tickled by <code>&quot;Test::Harness&quot;</code> 2.64 have been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fix <code>&quot;fcntl()&quot;</code> locking capability test in <i>configure.com</i>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Replaced <code>&quot;shrplib=&#8216;define&#8217;&quot;</code> with <code>&quot;useshrplib=&#8216;true&#8217;&quot;</code> on <font SIZE="-1">VMS.</font> </p>
 </dd></dl>
<p> <i>Windows</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;File::Find&quot;</code> used to fail when the target directory is a bare drive letter and <code>&quot;no_chdir&quot;</code> is 1 (the default is 0). [<font SIZE="-1">RT</font> #41555] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A build problem with specifying <code>&quot;USE_MULTI&quot;</code> and <code>&quot;USE_ITHREADS&quot;</code> but without <code>&quot;USE_IMP_SYS&quot;</code> has been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The process id is no longer truncated to 16 bits on some Windows platforms ( <a rel="nofollow" href="http://bugs.activestate.com/show_bug.cgi?id=72443">http://bugs.activestate.com/show_bug.cgi?id=72443</a> ) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed bug <font SIZE="-1">RT</font> #54828 in <i>perlio.c</i> where calling <code>&quot;binmode&quot;</code> on Win32 and Cygwin may cause a segmentation fault. </p>
 </dd></dl>
<h3>Smaller fixes</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> It is now possible to overload <code>&quot;eq&quot;</code> when using <code>&quot;nomethod&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Various problems using <code>&quot;overload&quot;</code> with 64 bit integers corrected. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The reference count of <code>&quot;PerlIO&quot;</code> file descriptors is now correctly handled. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On <font SIZE="-1">VMS,</font> escaped dots will be preserved when converted to Unix syntax. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;keys %+&quot;</code> no longer throws an <code>&#8216;ambiguous&#8217;</code> warning. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Using <code>&quot;#!perl -d&quot;</code> could trigger an assertion, which has been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Don&#8217;t stringify tied code references in <code>@INC</code> when calling <code>&quot;require&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Code references in <code>@INC</code> report the correct file name when <code>&quot;__FILE__&quot;</code> is used. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Width and precision in sprintf didn&#8217;t handle characters above 255 correctly. [<font SIZE="-1">RT</font> #40473] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> List slices with indices out of range now work more consistently. [<font SIZE="-1">RT</font> #39882] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A change introduced with perl 5.8.1 broke the parsing of arguments of the form <code>&quot;-foo=bar&quot;</code> with the <code>&quot;-s&quot;</code> on the &lt;#!&gt; line. This has been fixed. See <a rel="nofollow" href="http://bugs.activestate.com/show_bug.cgi?id=43483">http://bugs.activestate.com/show_bug.cgi?id=43483</a> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;tr///&quot;</code> is now threadsafe. Previously it was storing a swash inside its <font SIZE="-1">OP,</font> rather than in a pad. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>pod2html</i> labels anchors more consistently and handles nested definition lists better. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;threads&quot;</code> cleanup veto has been extended to include <code>&quot;perl_free()&quot;</code> and <code>&quot;perl_destruct()&quot;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On some systems, changes to <code>$ENV{TZ}</code> would not always be respected by the underlying calls to <code>&quot;localtime_r()&quot;</code>. Perl now forces the inspection of the environment on these systems. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The special variable <code>$^R</code> is now more consistently set when executing regexps using the <code>&quot;(?{...})&quot;</code> construct. In particular, it will still be set even if backreferences or optional sub-patterns <code>&quot;(?:...)?&quot;</code> are used. </p>
 </dd></dl>
<h2>New or Changed Diagnostics</h2>
<h3>panic: sv_chop %s</h3>
<p> This new fatal error occurs when the C routine <code>&quot;Perl_sv_chop()&quot;</code> was passed a position that is not within the scalar&#8217;s string buffer. This is caused by buggy <font SIZE="-1">XS</font> code, and at this point recovery is not possible.  </p>
<h3>Maximal count of pending signals (%s) exceeded</h3>
<p> This new fatal error occurs when the perl process has to abort due to too many pending signals, which is bound to prevent perl from being able to handle further incoming signals safely.  </p>
<h3>panic: attempt to call %s in %s</h3>
<p> This new fatal error occurs when the <font SIZE="-1">ACL</font> version file test operator is used where it is not available on the current platform. Earlier checks mean that it should never be possible to get this.  </p>
<font SIZE="-1"></font><h3>FETCHSIZE returned a negative value</h3>
<p> New error indicating that a tied array has claimed to have a negative number of elements.  </p>
<h3>Can't upgrade %s (%d) to %d</h3>
<p> Previously the internal error from the <font SIZE="-1">SV</font> upgrade code was the less informative <i>Can&#8217;t upgrade that kind of scalar</i>. It now reports the current internal type, and the new type requested.  </p>
<font SIZE="-1"></font><font SIZE="-1"></font><h3>%s argument is not a HASH or ARRAY element or a subroutine</h3>
<p> This error, thrown if an invalid argument is provided to <code>&quot;exists&quot;</code> now correctly includes ``or a subroutine&#8217;&#8216;. [<font SIZE="-1">RT</font> #38955]  </p>
<h3>Cannot make the non-overridable builtin %s fatal</h3>
<p> This error in <code>&quot;Fatal&quot;</code> previously did not show the name of the builtin in question (now represented by <code>%s</code> above).  </p>
<h3>Unrecognized character '%s' in column %d</h3>
<p> This error previously did not state the column.  </p>
<h3>Offset outside string</h3>
<p> This can now also be generated by a <code>&quot;seek&quot;</code> on a file handle using <code>&quot;PerlIO::scalar&quot;</code>.  </p>
<font SIZE="-1"></font><h3>Invalid escape in the specified encoding in regexp; marked by <-- HERE in m/%s/</h3>
<p> New error, introduced as part of the fix to <font SIZE="-1">RT</font> #40641 to handle encoding of Unicode characters in regular expression comments.  </p>
<h3>Your machine doesn't support dump/undump.</h3>
<p> A more informative fatal error issued when calling <code>&quot;dump&quot;</code> on Win32 and Cygwin. (Given that the purpose of <code>&quot;dump&quot;</code> is to abort with a core dump, and core dumps can&#8217;t be produced on these platforms, this is more useful than silently exiting.)  </p>
<h2>Changed Internals</h2>
<p> The perl sources can now be compiled with a C<font SIZE="-2">++</font> compiler instead of a C compiler. A necessary implementation details is that under C<font SIZE="-2">++</font>, the macro <code>&quot;XS&quot;</code> used to define XSUBs now includes an <code>&quot;extern &quot;C&quot;&quot;</code> definition. A side effect of this is that <code>C<font SIZE="-2">++</font></code> code that used the construction </p>
<pre><code>    typedef XS(SwigPerlWrapper);
</code></pre>
<p> now needs to be written </p>
<pre><code>    typedef XSPROTO(SwigPerlWrapper);
</code></pre>
<p> using the new <code>&quot;XSPROTO&quot;</code> macro, in order to compile. C extensions are unaffected, although C extensions are encouraged to use <code>&quot;XSPROTO&quot;</code> too. This change was present in the 5.10.0 release of perl, so any actively maintained code that happened to use this construction should already have been adapted. Code that needs changing will fail with a compilation error. </p>
<p> <code>&quot;set&quot;</code> magic on localizing/assigning to a magic variable will now only trigger for <i>container magics</i>, i.e. it will for <code>%ENV</code> or <code>%SIG</code> but not for <code>$#array</code>. </p>
<p> The new <font SIZE="-1">API</font> macro <code>&quot;newSVpvs()&quot;</code> can be used in place of constructions such as <code>&quot;newSVpvn(&quot;ISA&quot;, 3)&quot;</code>. It takes a single string constant, and at C compile time determines its length. </p>
<p> The new <font SIZE="-1">API</font> function <code>&quot;Perl_newSV_type()&quot;</code> can be used as a more efficient replacement of the common idiom </p>
<pre><code>    sv = newSV(0);
    sv_upgrade(sv, type);
</code></pre>
<p> Similarly <code>&quot;Perl_newSVpvn_flags()&quot;</code> can be used to combine <code>&quot;Perl_newSVpv()&quot;</code> with <code>&quot;Perl_sv_2mortal()&quot;</code> or the equivalent <code>&quot;Perl_sv_newmortal()&quot;</code> with <code>&quot;Perl_sv_setpvn()&quot;</code> </p>
<p> Two new macros <code>&quot;mPUSHs()&quot;</code> and <code>&quot;mXPUSHs()&quot;</code> are added, to make it easier to push mortal SVs onto the stack. They were then used to fix several bugs where values on the stack had not been mortalised. </p>
<p> A <code>&quot;Perl_signbit()&quot;</code> function was added to test the sign of an <code>&quot;NV&quot;</code>. It maps to the system one when available. </p>
<p> <code>&quot;Perl_av_reify()&quot;</code>, <code>&quot;Perl_lex_end()&quot;</code>, <code>&quot;Perl_mod()&quot;</code>, <code>&quot;Perl_op_clear()&quot;</code>, <code>&quot;Perl_pop_return()&quot;</code>, <code>&quot;Perl_qerror()&quot;</code>, <code>&quot;Perl_setdefout()&quot;</code>, <code>&quot;Perl_vivify_defelem()&quot;</code> and <code>&quot;Perl_yylex()&quot;</code> are now visible to extensions. This was required to allow <code>&quot;Data::Alias&quot;</code> to work on Windows. </p>
<p> <code>&quot;Perl_find_runcv()&quot;</code> is now visible to perl core extensions. This was required to allow <code>&quot;Sub::Current&quot;</code> to work on Windows. </p>
<p> <code>&quot;ptr_table*&quot;</code> functions are now available in unthreaded perl. <code>&quot;Storable&quot;</code> takes advantage of this. </p>
<p> There have been many small cleanups made to the internals. In particular, <code>&quot;Perl_sv_upgrade()&quot;</code> has been simplified considerably, with a straight-through code path that uses <code>&quot;memset()&quot;</code> and <code>&quot;memcpy()&quot;</code> to initialise the new body, rather than assignment via multiple temporary variables. It has also benefited from simplification and de-duplication of the arena management code. </p>
<p> A lot of small improvements in the code base were made due to reports from the Coverity static code analyzer. </p>
<p> Corrected use and documentation of <code>&quot;Perl_gv_stashpv()&quot;</code>, <code>&quot;Perl_gv_stashpvn()&quot;</code>, <code>&quot;Perl_gv_stashsv()&quot;</code> functions (last parameter is a bitmask, not boolean). </p>
<p> <code>&quot;PERL_SYS_INIT&quot;</code>, <code>&quot;PERL_SYS_INIT3&quot;</code> and <code>&quot;PERL_SYS_TERM&quot;</code> macros have been changed into functions. </p>
<p> <code>&quot;PERLSYS_TERM&quot;</code> no longer requires a context. <code>&quot;PerlIO_teardown()&quot;</code> is now called without a context, and debugging output in this function has been disabled because that required that an interpreter was present, an invalid assumption at termination time. </p>
<p> All compile time options which affect binary compatibility have been grouped together into a global variable (<code>&quot;PL_bincompat_options&quot;</code>). </p>
<p> The values of <code>&quot;PERL_REVISION&quot;</code>, <code>&quot;PERL_VERSION&quot;</code> and <code>&quot;PERL_SUBVERSION&quot;</code> are now baked into global variables (and hence into any shared perl library). Additionally under <code>&quot;MULTIPLICITY&quot;</code>, the perl executable now records the size of the interpreter structure (total, and for this version). Coupled with <code>&quot;PL_bincompat_options&quot;</code> this will allow 5.8.10 (and later), when compiled with a shared perl library, to perform sanity checks in <code>&quot;main()&quot;</code> to verify that the shared library is indeed binary compatible. </p>
<p> Symbolic references can now have embedded NULs. The new public function <code>&quot;Perl_get_cvn_flags()&quot;</code> can be used in extensions if you have to handle them.  </p>
<h3>Macro cleanups</h3>
<p> The core code, and <font SIZE="-1">XS</font> code in <i>ext</i> that is not dual-lived on <font SIZE="-1">CPAN,</font> no longer uses the macros <code>&quot;PL_na&quot;</code>, <code>&quot;NEWSV()&quot;</code>, <code>&quot;Null()&quot;</code>, <code>&quot;Nullav&quot;</code>, <code>&quot;Nullcv&quot;</code>, <code>&quot;Nullhv&quot;</code>, <code>&quot;Nullhv&quot;</code> <i>etc</i>. Their use is discouraged in new code, particularly <code>&quot;PL_na&quot;</code>, which is a small performance hit.  </p>
<h2>New Tests</h2>
<p> Many modules updated from <font SIZE="-1">CPAN</font> incorporate new tests. Some core specific tests have been added: </p>
<dl>
<dt>ext/DynaLoader/t/DynaLoader.t</dt>
<dd> <p> Tests for the <code>&quot;DynaLoader&quot;</code> module. </p>
 </dd>
<dt>t/comp/fold.t</dt>
<dd> <p> Tests for compile-time constant folding. </p>
 </dd>
<dt>t/io/pvbm.t</dt>
<dd> <p> Tests incorporated from 5.10.0 which check that there is no unexpected interaction between the internal types <code>&quot;PVBM&quot;</code> and <code>&quot;PVGV&quot;</code>. </p>
 </dd>
<dt>t/lib/proxy_constant_subs.t</dt>
<dd> <p> Tests for the new form of constant subroutines. </p>
 </dd>
<dt>t/op/attrhand.t</dt>
<dd> <p> Tests for <code>&quot;Attribute::Handlers&quot;</code>. </p>
 </dd>
<dt>t/op/dbm.t</dt>
<dd> <p> Tests for <code>&quot;dbmopen&quot;</code>. </p>
 </dd>
<dt>t/op/inccode-tie.t</dt>
<dd> <p> Calls all tests in <i>t/op/inccode.t</i> after first tying <code>@INC</code>. </p>
 </dd>
<dt>t/op/incfilter.t</dt>
<dd> <p> Tests for source filters returned from code references in <code>@INC</code>. </p>
 </dd>
<dt>t/op/kill0.t</dt>
<dd> <p> Tests for <font SIZE="-1">RT</font> #30970. </p>
 </dd>
<dt>t/op/qrstack.t</dt>
<dd> <p> Tests for <font SIZE="-1">RT</font> #41484. </p>
 </dd>
<dt>t/op/qr.t</dt>
<dd> <p> Tests for the <code>&quot;qr//&quot;</code> construct. </p>
 </dd>
<dt>t/op/regexp_qr_embed.t</dt>
<dd> <p> Tests for the <code>&quot;qr//&quot;</code> construct within another regexp. </p>
 </dd>
<dt>t/op/regexp_qr.t</dt>
<dd> <p> Tests for the <code>&quot;qr//&quot;</code> construct. </p>
 </dd>
<dt>t/op/rxcode.t</dt>
<dd> <p> Tests for <font SIZE="-1">RT</font> #32840. </p>
 </dd>
<dt>t/op/studytied.t</dt>
<dd> <p> Tests for <code>&quot;study&quot;</code> on tied scalars. </p>
 </dd>
<dt>t/op/substT.t</dt>
<dd> <p> Tests for <code>&quot;subst&quot;</code> run under <code>&quot;-T&quot;</code> mode. </p>
 </dd>
<dt>t/op/symbolcache.t</dt>
<dd> <p> Tests for <code>&quot;undef&quot;</code> and <code>&quot;delete&quot;</code> on stash entries that are bound to subroutines or methods. </p>
 </dd>
<dt>t/op/upgrade.t</dt>
<dd> <p> Tests for <code>&quot;Perl_sv_upgrade()&quot;</code>. </p>
 </dd>
<dt>t/mro/package_aliases.t</dt>
<dd> <p> <font SIZE="-1">MRO</font> tests for <code>&quot;isa&quot;</code> and package aliases. </p>
 </dd>
<dt>t/pod/twice.t</dt>
<dd> <p> Tests for calling <code>&quot;Pod::Parser&quot;</code> twice. </p>
 </dd>
<dt>t/run/cloexec.t</dt>
<dd> <p> Tests for inheriting file descriptors across <code>&quot;exec&quot;</code> (close-on-exec). </p>
 </dd>
<dt>t/uni/cache.t</dt>
<dd> <p> Tests for the <font SIZE="-1">UTF-8</font> caching code. </p>
 </dd>
<dt>t/uni/chr.t</dt>
<dd> <p> Test that strange encodings do not upset <code>&quot;Perl_pp_chr()&quot;</code>. </p>
 </dd>
<dt>t/uni/greek.t</dt>
<dd> <p> Tests for <font SIZE="-1">RT</font> #40641. </p>
 </dd>
<dt>t/uni/latin2.t</dt>
<dd> <p> Tests for <font SIZE="-1">RT</font> #40641. </p>
 </dd>
<dt>t/uni/overload.t</dt>
<dd> <p> Tests for returning Unicode from overloaded values. </p>
 </dd>
<dt>t/uni/tie.t</dt>
<dd> <p> Tests for returning Unicode from tied variables. </p>
 </dd></dl>
<h2>Known Problems</h2>
<p> There are no known new bugs. </p>
<p> However, programs that rely on bugs that have been fixed will have problems. Also, many bug fixes present in 5.10.0 can&#8217;t be back-ported to the 5.8.x branch, because they require changes that are binary incompatible, or because the code changes are too large and hence too risky to incorporate. </p>
<p> We have only limited volunteer labour, and the maintenance burden is getting increasingly complex. Hence this will be the last significant release of the 5.8.x series. Any future releases of 5.8.x will likely only be to deal with security issues, and platform build failures. Hence you should look to migrating to 5.10.x, if you have not started already. Alternatively, if business requirements constrain you to continue to use 5.8.x, you may wish to consider commercial support from firms such as ActiveState.  </p>
<h2>Platform Specific Notes</h2>
<h3>Win32</h3>
<p> <code>&quot;readdir()&quot;</code>, <code>&quot;cwd()&quot;</code>, <code>$^X</code> and <code>@INC</code> now use the alternate (short) filename if the long name is outside the current codepage (Jan Dubois). </p>
<p> <i>Updated Modules</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Win32&quot;</code> upgraded to version 0.38. Now has a documented &#8216;WinVista&#8217; response from <code>&quot;GetOSName&quot;</code> and support for Vista&#8217;s privilege elevation in <code>&quot;IsAdminUser&quot;</code>. Support for Unicode characters in path names. Improved cygwin and Win64 compatibility. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Win32API&quot;</code> updated to 0.1001_01 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;killpg()&quot;</code> support added to <code>&quot;MSWin32&quot;</code> (Jan Dubois). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;File::Spec::Win32&quot;</code> upgraded to version 3.2701 </p>
 </dd></dl>
<font SIZE="-1"></font><h3>OS/2</h3>
<p> <i>Updated Modules</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;OS2::Process&quot;</code> upgraded to 1.03 </p>
<p> Ilya Zakharevich has added and documented several <code>&quot;Window*&quot;</code> and <code>&quot;Clipbrd*&quot;</code> functions. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;OS2::REXX::DLL&quot;</code>, <code>&quot;OS2::REXX&quot;</code> updated to version 1.03 </p>
 </dd></dl>
<font SIZE="-1"></font><h3>VMS</h3>
<p> <i>Updated Modules</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;DCLsym&quot;</code> upgraded to version 1.03 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Stdio&quot;</code> upgraded to version 2.4 </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;VMS::XSSymSet&quot;</code> upgraded to 1.1. </p>
 </dd></dl>
<h2>Obituary</h2>
<p> Nick Ing-Simmons, long time Perl hacker, author of the <code>&quot;Tk&quot;</code> and <code>&quot;Encode&quot;</code> modules, <i>perlio.c</i> in the core, and 5.003_02 pumpking, died of a heart attack on 25th September 2006. He will be missed.  </p>
<h2>Acknowledgements</h2>
<p> Some of the work in this release was funded by a <font SIZE="-1">TPF</font> grant. </p>
<p> Steve Hay worked behind the scenes working out the causes of the differences between core modules, their <font SIZE="-1">CPAN</font> releases, and previous core releases, and the best way to rectify them. He doesn&#8217;t want to do it again. I know this feeling, and I&#8217;m very glad he did it this time, instead of me. </p>
<p> Paul Fenwick assembled a team of 18 volunteers, who broke the back of writing this document. In particular, Bradley Dean, Eddy Tan, and Vincent Pit provided half the team&#8217;s contribution. </p>
<p> Schwern verified the list of updated module versions, correcting quite a few errors that I (and everyone else) had missed, both wrongly stated module versions, and changed modules that had not been listed. </p>
<p> The crack Berlin-based <font SIZE="-1">QA</font> team of Andreas König and Slaven Rezic tirelessly re-built snapshots, tested most everything <font SIZE="-1">CPAN</font> against them, and then identified the changes responsible for any module regressions, ensuring that several show-stopper bugs were stomped before the first release candidate was cut. </p>
<p> The other core committers contributed most of the changes, and applied most of the patches sent in by the hundreds of contributors listed in <i></i><font SIZE="-1"><i>AUTHORS</i></font><i></i>. </p>
<p> And obviously, Larry Wall, without whom we wouldn&#8217;t have Perl.  </p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://bugs.perl.org.">http://bugs.perl.org.</a> There may also be information at <a rel="nofollow" href="http://www.perl.org,">http://www.perl.org,</a> the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <code>&quot;perl -V&quot;</code>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. You can browse and search the Perl 5 bugs at <a rel="nofollow" href="http://bugs.perl.org/">http://bugs.perl.org/</a> </p>
<p> If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who will be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on <font SIZE="-1">CPAN.</font>  </p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
