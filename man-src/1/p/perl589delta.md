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
<dt>&quot;${^CHILD_ERROR_NATIVE}&quot;</p>
<dd> This variable gives the native status returned by the last pipe close, backtick command, successful call to <tt>&quot;wait&quot;</tt> or <tt>&quot;waitpid&quot;</tt>, or from the <tt>&quot;system&quot;</tt> operator. See perlvar for details. (Contributed by Gisle Aas.)</p>
<dt>&quot;${^UTF8CACHE}&quot;</p>
<dd> This variable controls the state of the internal <font SIZE="-1">UTF-8</font> offset caching code. 1 for on (the default), 0 for off, -1 to debug the caching code by checking all its results against linear scans, and panicking on any discrepancy.</dl>
<h3>readpipe is now overridable</h3>
<p> The built-in function <tt>&quot;readpipe&quot;</tt> is now overridable. Overriding it permits also to override its operator counterpart, <tt>&quot;qx//&quot;</tt> (also known as <tt>&quot;``&quot;</tt>).</p>
<h3>simple exception handling macros</h3>
<p> Perl 5.8.9 (and 5.10.0 onwards) now provides a couple of macros to do very basic exception handling in <font SIZE="-1">XS</font> modules. You can use these macros if you call code that may <tt>&quot;croak&quot;</tt>, but you need to do some cleanup before giving control back to Perl. See &#8220;Exception Handling&#8221; in perlguts for more details.</p>
<h3>-D option enhancements</h3>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;-Dq&quot;</tt> suppresses the <i></i><font SIZE="-1"><i>EXECUTING&#8230;</i></font><i></i> message when running under <tt>&quot;-D&quot;</tt></p>
<dt>&bull;</p>
<dd> <tt>&quot;-Dl&quot;</tt> logs runops loop entry and exit, and jump level popping.</p>
<dt>&bull;</p>
<dd> <tt>&quot;-Dv&quot;</tt> displays the process id as part of the trace output.</dl>
<h3>XS-assisted <font SIZE="-1">SWASHGET</font></h3>
<p> Some pure-perl code that the regexp engine was using to retrieve Unicode properties and transliteration mappings has been reimplemented in <font SIZE="-1">XS</font> for faster execution. (<font SIZE="-1">SADAHIRO</font> Tomoyuki)</p>
<h3>Constant subroutines</h3>
<p> The interpreter internals now support a far more memory efficient form of inlineable constants. Storing a reference to a constant value in a symbol table is equivalent to a full typeglob referencing a constant subroutine, but using about 400 bytes less memory. This proxy constant subroutine is automatically upgraded to a real typeglob with subroutine if necessary. The approach taken is analogous to the existing space optimisation for subroutine stub declarations, which are stored as plain scalars in place of the full typeglob. </p>
<p> However, to aid backwards compatibility of existing code, which (wrongly) does not expect anything other than typeglobs in symbol tables, nothing in core uses this feature, other than the regression tests. </p>
<p> Stubs for prototyped subroutines have been stored in symbol tables as plain strings, and stubs for unprototyped subroutines as the number -1, since 5.005, so code which assumes that the core only places typeglobs in symbol tables has been making incorrect assumptions for over 10 years.</p>
<h2>New Platforms</h2>
<p> Compile support added for:</p>
<dl>
<dt>&bull;</p>
<dd> DragonFlyBSD</p>
<dt>&bull;</p>
<dd> MidnightBSD</p>
<dt>&bull;</p>
<dd> MirOS <font SIZE="-1">BSD</font></p>
<dt>&bull;</p>
<dd> <font SIZE="-1">RISC OS</font></p>
<dt>&bull;</p>
<dd> Cray XT4/Catamount</dl>
<h2>Modules and Pragmata</h2>
<h3>New Modules</h3>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;Module::Pluggable&quot;</tt> is a simple framework to create modules that accept pluggable sub-modules. The bundled version is 3.8</p>
<dt>&bull;</p>
<dd> <tt>&quot;Module::CoreList&quot;</tt> is a hash of hashes that is keyed on perl version as indicated in <tt>$]</tt>. The bundled version is 2.17</p>
<dt>&bull;</p>
<dd> <tt>&quot;Win32API::File&quot;</tt> now available in core on Microsoft Windows. The bundled version is 0.1001_01</p>
<dt>&bull;</p>
<dd> <tt>&quot;Devel::InnerPackage&quot;</tt> finds all the packages defined by a single file. It is part of the <tt>&quot;Module::Pluggable&quot;</tt> distribution. The bundled version is 0.3</dl>
<h3>Updated Modules</h3>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;attributes&quot;</tt> upgraded to version 0.09</p>
<dt>&bull;</p>
<dd> <tt>&quot;AutoLoader&quot;</tt> upgraded to version 5.67</p>
<dt>&bull;</p>
<dd> <tt>&quot;AutoSplit&quot;</tt> upgraded to 1.06</p>
<dt>&bull;</p>
<dd> <tt>&quot;autouse&quot;</tt> upgraded to version 1.06</p>
<dt>&bull;</p>
<dd> <tt>&quot;B&quot;</tt> upgraded from 1.09_01 to 1.19</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> provides new pad related abstraction macros <tt>&quot;B::NV::COP_SEQ_RANGE_LOW&quot;</tt>, <tt>&quot;B::NV::COP_SEQ_RANGE_HIGH&quot;</tt>, <tt>&quot;B::NV::PARENT_PAD_INDEX&quot;</tt>, <tt>&quot;B::NV::PARENT_FAKELEX_FLAGS&quot;</tt>, which hides the difference in storage in 5.10.0 and later.</p>
<dt>&bull;</p>
<dd> provides <tt>&quot;B::sub_generation&quot;</tt>, which exposes <tt>&quot;PL_sub_generation&quot;</tt></p>
<dt>&bull;</p>
<dd> provides <tt>&quot;B::GV::isGV_with_GP&quot;</tt>, which on pre-5.10 perls always returns true.</p>
<dt>&bull;</p>
<dd> New type <tt>&quot;B::HE&quot;</tt> added with methods <tt>&quot;VAL&quot;</tt>, <tt>&quot;HASH&quot;</tt> and <tt>&quot;SVKEY_force&quot;</tt></p>
<dt>&bull;</p>
<dd> The <tt>&quot;B::GVf_IMPORTED_CV&quot;</tt> flag is now set correctly when a proxy constant subroutine is imported.</p>
<dt>&bull;</p>
<dd> bugs fixed in the handling of <tt>&quot;PMOP&quot;</tt>s.</p>
<dt>&bull;</p>
<dd> <tt>&quot;B::BM::PREVIOUS&quot;</tt> returns now <tt>&quot;U32&quot;</tt>, not <tt>&quot;U16&quot;</tt>. <tt>&quot;B::CV::START&quot;</tt> and <tt>&quot;B:CV::ROOT&quot;</tt> return now <tt>&quot;NULL&quot;</tt> on an <font SIZE="-1">XSUB,</font> <tt>&quot;B::CV::XSUB&quot;</tt> and <tt>&quot;B::CV::XSUBANY&quot;</tt> return 0 on a non-XSUB.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;B::C&quot;</tt> upgraded to 1.05</p>
<dt>&bull;</p>
<dd> <tt>&quot;B::Concise&quot;</tt> upgraded to 0.76</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> new option <tt>&quot;-src&quot;</tt> causes the rendering of each statement (starting with the nextstate <font SIZE="-1">OP</font>) to be preceded by the first line of source code that generates it.</p>
<dt>&bull;</p>
<dd> new option <tt>&quot;-stash=&quot;somepackage&quot;&quot;</tt>, <tt>&quot;require&quot;</tt>s &#8220;somepackage&#8221;, and then renders each function defined in its namespace.</p>
<dt>&bull;</p>
<dd> now has documentation of detailed hint symbols.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;B::Debug&quot;</tt> upgraded to version 1.05</p>
<dt>&bull;</p>
<dd> <tt>&quot;B::Deparse&quot;</tt> upgraded to version 0.87</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> properly deparse <tt>&quot;print readpipe $x, $y&quot;</tt>.</p>
<dt>&bull;</p>
<dd> now handles <tt>&quot;''-&gt;()&quot;</tt>, <tt>&quot;::()&quot;</tt>, <tt>&quot;sub :: {}&quot;</tt>, <i>etc.</i> correctly [<font SIZE="-1">RT</font> #43010]. All bugs in parsing these kinds of syntax are now fixed: </p>
<pre><code>
perl - MO = Deparse - e '"my %h = "-&gt;()' perl - MO = Deparse - e '::-&gt;()' perl - MO = Deparse - e 'sub :: {}' perl - MO = Deparse - e 'package a; sub a::b::c {}' perl - MO = Deparse - e 'sub the::main::road {}'
</code></pre>
<dt>&bull;</p>
<dd> does <code>not</code> deparse <tt>$^H{v_string}</tt>, which is automatically set by the internals.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;B::Lint&quot;</tt> upgraded to version 1.11</p>
<dt>&bull;</p>
<dd> <tt>&quot;B::Terse&quot;</tt> upgraded to version 1.05</p>
<dt>&bull;</p>
<dd> <tt>&quot;base&quot;</tt> upgraded to version 2.13</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> loading a module via base.pm would mask a global <tt>$SIG{__DIE__}</tt> in that module.</p>
<dt>&bull;</p>
<dd> push all classes at once in <tt>@ISA</tt></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Benchmark&quot;</tt> upgraded to version 1.10</p>
<dt>&bull;</p>
<dd> <tt>&quot;bigint&quot;</tt> upgraded to 0.23</p>
<dt>&bull;</p>
<dd> <tt>&quot;bignum&quot;</tt> upgraded to 0.23</p>
<dt>&bull;</p>
<dd> <tt>&quot;bigrat&quot;</tt> upgraded to 0.23</p>
<dt>&bull;</p>
<dd> <tt>&quot;blib&quot;</tt> upgraded to 0.04</p>
<dt>&bull;</p>
<dd> <tt>&quot;Carp&quot;</tt> upgraded to version 1.10 </p>
<p> The argument backtrace code now shows <tt>&quot;undef&quot;</tt> as <tt>&quot;undef&quot;</tt>, instead of a string <i>&#8220;undef&#8221;</i>.</p>
<dt>&bull;</p>
<dd> <tt>&quot;CGI&quot;</tt> upgraded to version 3.42</p>
<dt>&bull;</p>
<dd> <tt>&quot;charnames&quot;</tt> upgraded to 1.06</p>
<dt>&bull;</p>
<dd> <tt>&quot;constant&quot;</tt> upgraded to version 1.17</p>
<dt>&bull;</p>
<dd> <tt>&quot;CPAN&quot;</tt> upgraded to version 1.9301</p>
<dt>&bull;</p>
<dd> <tt>&quot;Cwd&quot;</tt> upgraded to version 3.29 with some platform specific improvements (including for <font SIZE="-1">VMS</font>).</p>
<dt>&bull;</p>
<dd> <tt>&quot;Data::Dumper&quot;</tt> upgraded to version 2.121_17</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Fixes hash iterator current position with the pure Perl version [<font SIZE="-1">RT</font> #40668]</p>
<dt>&bull;</p>
<dd> Performance enhancements, which will be most evident on platforms where repeated calls to C&#8217;s <tt>&quot;realloc()&quot;</tt> are slow, such as Win32.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;DB_File&quot;</tt> upgraded to version 1.817</p>
<dt>&bull;</p>
<dd> <tt>&quot;DB_Filter&quot;</tt> upgraded to version 0.02</p>
<dt>&bull;</p>
<dd> <tt>&quot;Devel::DProf&quot;</tt> upgraded to version 20080331.00</p>
<dt>&bull;</p>
<dd> <tt>&quot;Devel::Peek&quot;</tt> upgraded to version 1.04</p>
<dt>&bull;</p>
<dd> <tt>&quot;Devel::PPPort&quot;</tt> upgraded to version 3.14</p>
<dt>&bull;</p>
<dd> <tt>&quot;diagnostics&quot;</tt> upgraded to version 1.16</p>
<dt>&bull;</p>
<dd> <tt>&quot;Digest&quot;</tt> upgraded to version 1.15</p>
<dt>&bull;</p>
<dd> <tt>&quot;Digest::MD5&quot;</tt> upgraded to version 2.37</p>
<dt>&bull;</p>
<dd> <tt>&quot;DirHandle&quot;</tt> upgraded to version 1.02</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> now localises <tt>$.</tt>, <tt>$@</tt>, <tt>$!</tt>, <tt>$^E</tt>, and <tt>$?</tt> before closing the directory handle to suppress leaking any side effects of warnings about it already being closed.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;DynaLoader&quot;</tt> upgraded to version 1.09 </p>
<p> <tt>&quot;DynaLoader&quot;</tt> can now dynamically load a loadable object from a file with a non-default file extension.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Encode&quot;</tt> upgraded to version 2.26 </p>
<p> <tt>&quot;Encode::Alias&quot;</tt> includes a fix for encoding &#8220;646&#8221; on Solaris (better known as <font SIZE="-1">ASCII</font>).</p>
<dt>&bull;</p>
<dd> <tt>&quot;English&quot;</tt> upgraded to version 1.03</p>
<dt>&bull;</p>
<dd> <tt>&quot;Errno&quot;</tt> upgraded to version 1.10</p>
<dt>&bull;</p>
<dd> <tt>&quot;Exporter&quot;</tt> upgraded to version 5.63</p>
<dt>&bull;</p>
<dd> <tt>&quot;ExtUtils::Command&quot;</tt> upgraded to version 1.15</p>
<dt>&bull;</p>
<dd> <tt>&quot;ExtUtils::Constant&quot;</tt> upgraded to version 0.21</p>
<dt>&bull;</p>
<dd> <tt>&quot;ExtUtils::Embed&quot;</tt> upgraded to version 1.28</p>
<dt>&bull;</p>
<dd> <tt>&quot;ExtUtils::Install&quot;</tt> upgraded to version 1.50_01</p>
<dt>&bull;</p>
<dd> <tt>&quot;ExtUtils::Installed&quot;</tt> upgraded to version 1.43</p>
<dt>&bull;</p>
<dd> <tt>&quot;ExtUtils::MakeMaker&quot;</tt> upgraded to version 6.48</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> support for <tt>&quot;INSTALLSITESCRIPT&quot;</tt> and <tt>&quot;INSTALLVENDORSCRIPT&quot;</tt> configuration.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;ExtUtils::Manifest&quot;</tt> upgraded to version 1.55</p>
<dt>&bull;</p>
<dd> <tt>&quot;ExtUtils::ParseXS&quot;</tt> upgraded to version 2.19</p>
<dt>&bull;</p>
<dd> <tt>&quot;Fatal&quot;</tt> upgraded to version 1.06</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> allows built-ins in <tt>&quot;CORE::GLOBAL&quot;</tt> to be made fatal.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Fcntl&quot;</tt> upgraded to version 1.06</p>
<dt>&bull;</p>
<dd> <tt>&quot;fields&quot;</tt> upgraded to version 2.12</p>
<dt>&bull;</p>
<dd> <tt>&quot;File::Basename&quot;</tt> upgraded to version 2.77</p>
<dt>&bull;</p>
<dd> <tt>&quot;FileCache&quot;</tt> upgraded to version 1.07</p>
<dt>&bull;</p>
<dd> <tt>&quot;File::Compare&quot;</tt> upgraded to 1.1005</p>
<dt>&bull;</p>
<dd> <tt>&quot;File::Copy&quot;</tt> upgraded to 2.13</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> now uses 3-arg open.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;File::DosGlob&quot;</tt> upgraded to 1.01</p>
<dt>&bull;</p>
<dd> <tt>&quot;File::Find&quot;</tt> upgraded to version 1.13</p>
<dt>&bull;</p>
<dd> <tt>&quot;File::Glob&quot;</tt> upgraded to version 1.06</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> fixes spurious results with brackets inside braces.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;File::Path&quot;</tt> upgraded to version 2.07_02</p>
<dt>&bull;</p>
<dd> <tt>&quot;File::Spec&quot;</tt> upgraded to version 3.29</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> improved handling of bad arguments.</p>
<dt>&bull;</p>
<dd> some platform specific improvements (including for <font SIZE="-1">VMS</font> and Cygwin), with an optimisation on <tt>&quot;abs2rel&quot;</tt> when handling both relative arguments.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;File::stat&quot;</tt> upgraded to version 1.01</p>
<dt>&bull;</p>
<dd> <tt>&quot;File::Temp&quot;</tt> upgraded to version 0.20</p>
<dt>&bull;</p>
<dd> <tt>&quot;filetest&quot;</tt> upgraded to version 1.02</p>
<dt>&bull;</p>
<dd> <tt>&quot;Filter::Util::Call&quot;</tt> upgraded to version 1.07</p>
<dt>&bull;</p>
<dd> <tt>&quot;Filter::Simple&quot;</tt> upgraded to version 0.83</p>
<dt>&bull;</p>
<dd> <tt>&quot;FindBin&quot;</tt> upgraded to version 1.49</p>
<dt>&bull;</p>
<dd> <tt>&quot;GDBM_File&quot;</tt> upgraded to version 1.09</p>
<dt>&bull;</p>
<dd> <tt>&quot;Getopt::Long&quot;</tt> upgraded to version 2.37</p>
<dt>&bull;</p>
<dd> <tt>&quot;Getopt::Std&quot;</tt> upgraded to version 1.06</p>
<dt>&bull;</p>
<dd> <tt>&quot;Hash::Util&quot;</tt> upgraded to version 0.06</p>
<dt>&bull;</p>
<dd> <tt>&quot;if&quot;</tt> upgraded to version 0.05</p>
<dt>&bull;</p>
<dd> <tt>&quot;IO&quot;</tt> upgraded to version 1.23 </p>
<p> Reduced number of calls to <tt>&quot;getpeername&quot;</tt> in <tt>&quot;IO::Socket&quot;</tt></p>
<dt>&bull;</p>
<dd> <tt>&quot;IPC::Open&quot;</tt> upgraded to version 1.03</p>
<dt>&bull;</p>
<dd> <tt>&quot;IPC::Open3&quot;</tt> upgraded to version 1.03</p>
<dt>&bull;</p>
<dd> <tt>&quot;IPC::SysV&quot;</tt> upgraded to version 2.00</p>
<dt>&bull;</p>
<dd> <tt>&quot;lib&quot;</tt> upgraded to version 0.61</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> avoid warning about loading <i>.par</i> files.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;libnet&quot;</tt> upgraded to version 1.22</p>
<dt>&bull;</p>
<dd> <tt>&quot;List::Util&quot;</tt> upgraded to 1.19</p>
<dt>&bull;</p>
<dd> <tt>&quot;Locale::Maketext&quot;</tt> upgraded to 1.13</p>
<dt>&bull;</p>
<dd> <tt>&quot;Math::BigFloat&quot;</tt> upgraded to version 1.60</p>
<dt>&bull;</p>
<dd> <tt>&quot;Math::BigInt&quot;</tt> upgraded to version 1.89</p>
<dt>&bull;</p>
<dd> <tt>&quot;Math::BigRat&quot;</tt> upgraded to version 0.22</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> implements new <tt>&quot;as_float&quot;</tt> method.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Math::Complex&quot;</tt> upgraded to version 1.54.</p>
<dt>&bull;</p>
<dd> <tt>&quot;Math::Trig&quot;</tt> upgraded to version 1.18.</p>
<dt>&bull;</p>
<dd> <tt>&quot;NDBM_File&quot;</tt> upgraded to version 1.07</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> improve <i>g++</i> handling for systems using <font SIZE="-1">GDBM</font> compatibility headers.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Net::Ping&quot;</tt> upgraded to version 2.35</p>
<dt>&bull;</p>
<dd> <tt>&quot;NEXT&quot;</tt> upgraded to version 0.61</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> fix several bugs with <tt>&quot;NEXT&quot;</tt> when working with <tt>&quot;AUTOLOAD&quot;</tt>, <tt>&quot;eval&quot;</tt> block, and within overloaded stringification.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;ODBM_File&quot;</tt> upgraded to 1.07</p>
<dt>&bull;</p>
<dd> <tt>&quot;open&quot;</tt> upgraded to 1.06</p>
<dt>&bull;</p>
<dd> <tt>&quot;ops&quot;</tt> upgraded to 1.02</p>
<dt>&bull;</p>
<dd> <tt>&quot;PerlIO::encoding&quot;</tt> upgraded to version 0.11</p>
<dt>&bull;</p>
<dd> <tt>&quot;PerlIO::scalar&quot;</tt> upgraded to version 0.06</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> [<font SIZE="-1">RT</font> #40267] <tt>&quot;PerlIO::scalar&quot;</tt> doesn&#8217;t respect readonly-ness.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;PerlIO::via&quot;</tt> upgraded to version 0.05</p>
<dt>&bull;</p>
<dd> <tt>&quot;Pod::Html&quot;</tt> upgraded to version 1.09</p>
<dt>&bull;</p>
<dd> <tt>&quot;Pod::Parser&quot;</tt> upgraded to version 1.35</p>
<dt>&bull;</p>
<dd> <tt>&quot;Pod::Usage&quot;</tt> upgraded to version 1.35</p>
<dt>&bull;</p>
<dd> <tt>&quot;POSIX&quot;</tt> upgraded to version 1.15</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;POSIX&quot;</tt> constants that duplicate those in <tt>&quot;Fcntl&quot;</tt> are now imported from <tt>&quot;Fcntl&quot;</tt> and re-exported, rather than being duplicated by <tt>&quot;POSIX&quot;</tt></p>
<dt>&bull;</p>
<dd> <tt>&quot;POSIX::remove&quot;</tt> can remove empty directories.</p>
<dt>&bull;</p>
<dd> <tt>&quot;POSIX::setlocale&quot;</tt> safer to call multiple times.</p>
<dt>&bull;</p>
<dd> <tt>&quot;POSIX::SigRt&quot;</tt> added, which provides access to <font SIZE="-1">POSIX</font> realtime signal functionality on systems that support it.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;re&quot;</tt> upgraded to version 0.06_01</p>
<dt>&bull;</p>
<dd> <tt>&quot;Safe&quot;</tt> upgraded to version 2.16</p>
<dt>&bull;</p>
<dd> <tt>&quot;Scalar::Util&quot;</tt> upgraded to 1.19</p>
<dt>&bull;</p>
<dd> <tt>&quot;SDBM_File&quot;</tt> upgraded to version 1.06</p>
<dt>&bull;</p>
<dd> <tt>&quot;SelfLoader&quot;</tt> upgraded to version 1.17</p>
<dt>&bull;</p>
<dd> <tt>&quot;Shell&quot;</tt> upgraded to version 0.72</p>
<dt>&bull;</p>
<dd> <tt>&quot;sigtrap&quot;</tt> upgraded to version 1.04</p>
<dt>&bull;</p>
<dd> <tt>&quot;Socket&quot;</tt> upgraded to version 1.81</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> this fixes an optimistic use of <tt>&quot;gethostbyname&quot;</tt></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Storable&quot;</tt> upgraded to 2.19</p>
<dt>&bull;</p>
<dd> <tt>&quot;Switch&quot;</tt> upgraded to version 2.13</p>
<dt>&bull;</p>
<dd> <tt>&quot;Sys::Syslog&quot;</tt> upgraded to version 0.27</p>
<dt>&bull;</p>
<dd> <tt>&quot;Term::ANSIColor&quot;</tt> upgraded to version 1.12</p>
<dt>&bull;</p>
<dd> <tt>&quot;Term::Cap&quot;</tt> upgraded to version 1.12</p>
<dt>&bull;</p>
<dd> <tt>&quot;Term::ReadLine&quot;</tt> upgraded to version 1.03</p>
<dt>&bull;</p>
<dd> <tt>&quot;Test::Builder&quot;</tt> upgraded to version 0.80</p>
<dt>&bull;</p>
<dd> <tt>&quot;Test::Harness&quot;</tt> upgraded version to 2.64</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> this makes it able to handle newlines.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Test::More&quot;</tt> upgraded to version 0.80</p>
<dt>&bull;</p>
<dd> <tt>&quot;Test::Simple&quot;</tt> upgraded to version 0.80</p>
<dt>&bull;</p>
<dd> <tt>&quot;Text::Balanced&quot;</tt> upgraded to version 1.98</p>
<dt>&bull;</p>
<dd> <tt>&quot;Text::ParseWords&quot;</tt> upgraded to version 3.27</p>
<dt>&bull;</p>
<dd> <tt>&quot;Text::Soundex&quot;</tt> upgraded to version 3.03</p>
<dt>&bull;</p>
<dd> <tt>&quot;Text::Tabs&quot;</tt> upgraded to version 2007.1117</p>
<dt>&bull;</p>
<dd> <tt>&quot;Text::Wrap&quot;</tt> upgraded to version 2006.1117</p>
<dt>&bull;</p>
<dd> <tt>&quot;Thread&quot;</tt> upgraded to version 2.01</p>
<dt>&bull;</p>
<dd> <tt>&quot;Thread::Semaphore&quot;</tt> upgraded to version 2.09</p>
<dt>&bull;</p>
<dd> <tt>&quot;Thread::Queue&quot;</tt> upgraded to version 2.11</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> added capability to add complex structures (e.g., hash of hashes) to queues.</p>
<dt>&bull;</p>
<dd> added capability to dequeue multiple items at once.</p>
<dt>&bull;</p>
<dd> added new methods to inspect and manipulate queues: <tt>&quot;peek&quot;</tt>, <tt>&quot;insert&quot;</tt> and <tt>&quot;extract&quot;</tt></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Tie::Handle&quot;</tt> upgraded to version 4.2</p>
<dt>&bull;</p>
<dd> <tt>&quot;Tie::Hash&quot;</tt> upgraded to version 1.03</p>
<dt>&bull;</p>
<dd> <tt>&quot;Tie::Memoize&quot;</tt> upgraded to version 1.1</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> <tt>&quot;Tie::Memoize::EXISTS&quot;</tt> now correctly caches its results.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Tie::RefHash&quot;</tt> upgraded to version 1.38</p>
<dt>&bull;</p>
<dd> <tt>&quot;Tie::Scalar&quot;</tt> upgraded to version 1.01</p>
<dt>&bull;</p>
<dd> <tt>&quot;Tie::StdHandle&quot;</tt> upgraded to version 4.2</p>
<dt>&bull;</p>
<dd> <tt>&quot;Time::gmtime&quot;</tt> upgraded to version 1.03</p>
<dt>&bull;</p>
<dd> <tt>&quot;Time::Local&quot;</tt> upgraded to version 1.1901</p>
<dt>&bull;</p>
<dd> <tt>&quot;Time::HiRes&quot;</tt> upgraded to version 1.9715 with various build improvements (including <font SIZE="-1">VMS</font>) and minor platform-specific bug fixes (including for HP-UX 11 ia64).</p>
<dt>&bull;</p>
<dd> <tt>&quot;threads&quot;</tt> upgraded to 1.71</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> new thread state information methods: <tt>&quot;is_running&quot;</tt>, <tt>&quot;is_detached&quot;</tt> and <tt>&quot;is_joinable&quot;</tt>. <tt>&quot;list&quot;</tt> method enhanced to return running or joinable threads.</p>
<dt>&bull;</p>
<dd> new thread signal method: <tt>&quot;kill&quot;</tt></p>
<dt>&bull;</p>
<dd> added capability to specify thread stack size.</p>
<dt>&bull;</p>
<dd> added capability to control thread exiting behavior. Added a new <tt>&quot;exit&quot;</tt> method.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;threads::shared&quot;</tt> upgraded to version 1.27</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> smaller and faster implementation that eliminates one internal structure and the consequent level of indirection.</p>
<dt>&bull;</p>
<dd> user locks are now stored in a safer manner.</p>
<dt>&bull;</p>
<dd> new function <tt>&quot;shared_clone&quot;</tt> creates a copy of an object leaving shared elements as-is and deep-cloning non-shared elements.</p>
<dt>&bull;</p>
<dd> added new <tt>&quot;is_shared&quot;</tt> method.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;Unicode::Normalize&quot;</tt> upgraded to version 1.02</p>
<dt>&bull;</p>
<dd> <tt>&quot;Unicode::UCD&quot;</tt> upgraded to version 0.25</p>
<dt>&bull;</p>
<dd> <tt>&quot;warnings&quot;</tt> upgraded to version 1.05_01</p>
<dt>&bull;</p>
<dd> <tt>&quot;Win32&quot;</tt> upgraded to version 0.38</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> added new function <tt>&quot;GetCurrentProcessId&quot;</tt> which returns the regular Windows process identifier of the current process, even when called from within a fork.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> <tt>&quot;XSLoader&quot;</tt> upgraded to version 0.10</p>
<dt>&bull;</p>
<dd> <tt>&quot;XS::APItest&quot;</tt> and <tt>&quot;XS::Typemap&quot;</tt> are for internal use only and hence no longer installed. Many more tests have been added to <tt>&quot;XS::APItest&quot;</tt>.</dl>
<h2>Utility Changes</h2>
<h3>debugger upgraded to version 1.31</h3>
<dl>
<dt>&bull;</p>
<dd> Andreas König contributed two functions to save and load the debugger history.</p>
<dt>&bull;</p>
<dd> <tt>&quot;NEXT::AUTOLOAD&quot;</tt> no longer emits warnings under the debugger.</p>
<dt>&bull;</p>
<dd> The debugger should now correctly find tty the device on <font SIZE="-1">OS X 10.5</font> and <font SIZE="-1">VMS</font> when the program <tt>&quot;fork&quot;</tt>s.</p>
<dt>&bull;</p>
<dd> <font SIZE="-1">LVALUE</font> subs now work inside the debugger.</dl>
<h3><i>perlthanks</i></h3>
<p> Perl 5.8.9 adds a new utility <i>perlthanks</i>, which is a variant of <i>perlbug</i>, but for sending non-bug-reports to the authors and maintainers of Perl. Getting nothing but bug reports can become a bit demoralising &#8211; we&#8217;ll see if this changes things.</p>
<h3><i>perlbug</i></h3>
<p> <i>perlbug</i> now checks if you&#8217;re reporting about a non-core module and suggests you report it to the <font SIZE="-1">CPAN</font> author instead.</p>
<h3><i>h2xs</i></h3>
<dl>
<dt>&bull;</p>
<dd> won&#8217;t define an empty string as a constant [<font SIZE="-1">RT</font> #25366]</p>
<dt>&bull;</p>
<dd> has examples for <tt>&quot;h2xs -X&quot;</tt></dl>
<h3><i>h2ph</i></h3>
<dl>
<dt>&bull;</p>
<dd> now attempts to deal sensibly with the difference in path implications between <tt>&quot;&quot;</tt> and <tt>&quot;&lt;&gt;&quot;</tt> quoting in <tt>&quot;#include&quot;</tt> statements.</p>
<dt>&bull;</p>
<dd> now generates correct code for <tt>&quot;#if defined A || defined B&quot;</tt> [<font SIZE="-1">RT</font> #39130]</dl>
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
<dt>&bull;</p>
<dd> Documentation is fixed in section <tt>&quot;caller&quot;</tt> and <tt>&quot;pop&quot;</tt>.</p>
<dt>&bull;</p>
<dd> Function <tt>&quot;alarm&quot;</tt> now mentions <tt>&quot;Time::HiRes::ualarm&quot;</tt> in preference to <tt>&quot;select&quot;</tt>.</p>
<dt>&bull;</p>
<dd> Regarding precedence in <tt>&quot;-X&quot;</tt>, filetest operators are the same as unary operators, but not regarding parsing and parentheses (spotted by Eirik Berg Hanssen).</p>
<dt>&bull;</p>
<dd> <tt>&quot;reverse&quot;</tt> function documentation received scalar context examples.</dl>
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
<dt>&bull;</p>
<dd> The default since perl 5.000 has been for perl to create an empty scalar with every new typeglob. The increased use of lexical variables means that most are now unused. Thanks to Nicholas Clark&#8217;s efforts, Perl can now be compiled with <tt>&quot;-DPERL_DONT_CREATE_GVSV&quot;</tt> to avoid creating these empty scalars. This will significantly decrease the number of scalars allocated for all configurations, and the number of scalars that need to be copied for ithread creation. Whilst this option is binary compatible with existing perl installations, it does change a long-standing assumption about the internals, hence it is not enabled by default, as some third party code may rely on the old behaviour. </p>
<p> We would recommend testing with this configuration on new deployments of perl, particularly for multi-threaded servers, to see whether all third party code is compatible with it, as this configuration may give useful performance improvements. For existing installations we would not recommend changing to this configuration unless thorough testing is performed before deployment.</p>
<dt>&bull;</p>
<dd> <tt>&quot;diagnostics&quot;</tt> no longer uses <tt>$&amp;</tt>, which results in large speedups for regexp matching in all code using it.</p>
<dt>&bull;</p>
<dd> Regular expressions classes of a single character are now treated the same as if the character had been used as a literal, meaning that code that uses char-classes as an escaping mechanism will see a speedup. (Yves Orton)</p>
<dt>&bull;</p>
<dd> Creating anonymous array and hash references (ie. <tt>&quot;[]&quot;</tt> and <tt>&quot;{}&quot;</tt>) now incurs no more overhead than creating an anonymous list or hash. Nicholas Clark provided changes with a saving of two ops and one stack push, which was measured as a slightly better than 5% improvement for these operations.</p>
<dt>&bull;</p>
<dd> Many calls to <tt>&quot;strlen()&quot;</tt> have been eliminated, either because the length was already known, or by adopting or enhancing APIs that pass lengths. This has been aided by the adoption of a <tt>&quot;my_sprintf()&quot;</tt> wrapper, which returns the correct C89 value &#8211; the length of the formatted string. Previously we could not rely on the return value of <tt>&quot;sprintf()&quot;</tt>, because on some ancient but extant platforms it still returns <tt>&quot;char *&quot;</tt>.</p>
<dt>&bull;</p>
<dd> <tt>&quot;index&quot;</tt> is now faster if the search string is stored in <font SIZE="-1">UTF-8</font> but only contains characters in the Latin-1 range.</p>
<dt>&bull;</p>
<dd> The Unicode swatch cache inside the regexp engine is now used. (the lookup had a key mismatch, present since the initial implementation). [<font SIZE="-1">RT</font> #42839]</dl>
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
<dt>&bull;</p>
<dd> static library files of statically linked extensions when a shared perl library is being used. (They are not needed. See &#8220;Windows&#8221; below).</p>
<dt>&bull;</p>
<dd> <i></i><font SIZE="-1"><i>SIGNATURE</i></font><i></i> and <i>PAUSE*.pub</i> (<font SIZE="-1">CPAN</font> files)</p>
<dt>&bull;</p>
<dd> <i></i><font SIZE="-1"><i>NOTES</i></font><i></i> and <i></i><font SIZE="-1"><i>PATCHING</i></font><i></i> (ExtUtils files)</p>
<dt>&bull;</p>
<dd> <i>perlld</i> and <i>ld2</i> (Cygwin files)</dl>
<h3>Platform Specific Changes</h3>
<p> There are improved hints for <font SIZE="-1">AIX,</font> Cygwin, <font SIZE="-1">DEC/OSF,</font> FreeBSD, <font SIZE="-1">HP/UX,</font> Irix 6 Linux, MachTen, NetBSD, <font SIZE="-1">OS/390, QNX, SCO,</font> Solaris, SunOS, System V Release 5.x (UnixWare 7, OpenUNIX 8), Ultrix, <font SIZE="-1">UMIPS,</font> uts and <font SIZE="-1">VOS.</font> </p>
<p> <i>FreeBSD</i></p>
<dl>
<dt>&bull;</p>
<dd> Drop <tt>&quot;-std=c89&quot;</tt> and <tt>&quot;-ansi&quot;</tt> if using <tt>&quot;long long&quot;</tt> as the main integral type, else in FreeBSD 6.2 (and perhaps other releases), system headers do not declare some functions required by perl.</dl>
<p> <i>Solaris</i></p>
<dl>
<dt>&bull;</p>
<dd> Starting with Solaris 10, we do not want versioned shared libraries, because those often indicate a private use only library. These problems could often be triggered when SUNWbdb (Berkeley <font SIZE="-1">DB</font>) was installed. Hence if Solaris 10 is detected set <tt>&quot;ignore_versioned_solibs=y&quot;</tt>.</dl>
<p> <i></i><font SIZE="-1"><i>VMS</i></font><i></i></p>
<dl>
<dt>&bull;</p>
<dd> Allow <font SIZE="-1">IEEE</font> math to be deselected on OpenVMS I64 (but it remains the default).</p>
<dt>&bull;</p>
<dd> Record <font SIZE="-1">IEEE</font> usage in <tt>&quot;config.h&quot;</tt></p>
<dt>&bull;</p>
<dd> Help older <font SIZE="-1">VMS</font> compilers by using <tt>&quot;ccflags&quot;</tt> when building <tt>&quot;munchconfig.exe&quot;</tt>.</p>
<dt>&bull;</p>
<dd> Don&#8217;t try to build old <tt>&quot;Thread&quot;</tt> extension on <font SIZE="-1">VMS</font> when <tt>&quot;-Duseithreads&quot;</tt> has been chosen.</p>
<dt>&bull;</p>
<dd> Passing a raw string of &#8220;NaN&#8221; to <i>nawk</i> causes a core dump &#8211; so the string has been changed to &#8220;*NaN*&#8221;</p>
<dt>&bull;</p>
<dd> <i>t/op/stat.t</i> tests will now test hard links on <font SIZE="-1">VMS</font> if they are supported.</dl>
<p> <i>Windows</i></p>
<dl>
<dt>&bull;</p>
<dd> When using a shared perl library <i>installperl</i> no longer installs static library files, import library files and export library files (of statically linked extensions) and empty bootstrap files (of dynamically linked extensions). This fixes a problem building PAR-Packer on Win32 with a debug build of perl.</p>
<dt>&bull;</p>
<dd> Various improvements to the win32 build process, including support for Visual C<font SIZE="-2">++</font> 2005 Express Edition (aka Visual C<font SIZE="-2">++</font> 8.x).</p>
<dt>&bull;</p>
<dd> <i>perl.exe</i> will now have an icon if built with MinGW or Borland.</p>
<dt>&bull;</p>
<dd> Improvements to the perl-static.exe build process.</p>
<dt>&bull;</p>
<dd> Add Win32 makefile option to link all extensions statically.</p>
<dt>&bull;</p>
<dd> The <i>WinCE</i> directory has been merged into the <i>Win32</i> directory.</p>
<dt>&bull;</p>
<dd> <tt>&quot;setlocale&quot;</tt> tests have been re-enabled for Windows <font SIZE="-1">XP</font> onwards.</dl>
<h2>Selected Bug Fixes</h2>
<h3>Unicode</h3>
<p> Many many bugs related to the internal Unicode implementation (<font SIZE="-1">UTF-8</font>) have been fixed. In particular, long standing bugs related to returning Unicode via <tt>&quot;tie&quot;</tt>, overloading or <tt>$@</tt> are now gone, some of which were never reported. </p>
<p> <tt>&quot;unpack&quot;</tt> will internally convert the string back from <font SIZE="-1">UTF-8</font> on numeric types. This is a compromise between the full consistency now in 5.10, and the current behaviour, which is often used as a &#8220;feature&#8221; on string types. </p>
<p> Using <tt>&quot;:crlf&quot;</tt> and <tt>&quot;UTF-16&quot;</tt> <font SIZE="-1">IO</font> layers together will now work. </p>
<p> Fixed problems with <tt>&quot;split&quot;</tt>, Unicode <tt>&quot;/\s+/&quot;</tt> and <tt>&quot;/ 
