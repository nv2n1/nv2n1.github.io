---
title: "perl5005delta(1)"
name: "perl5005delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5005delta/"
description: "perl5005delta – what’s new for perl5.005"
---

<h2 class="name">NAME</h2>
<p> perl5005delta &#8211; what&#8217;s new for perl5.005 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.004 release and this one.</p>
<h2>About the new versioning system</h2>
<p> Perl is now developed on two tracks: a maintenance track that makes small, safe updates to released production versions with emphasis on compatibility; and a development track that pursues more aggressive evolution. Maintenance releases (which should be considered production quality) have subversion numbers that run from <tt>1</tt> to <tt>49</tt>, and development releases (which should be considered &#8220;alpha&#8221; quality) run from <tt>50</tt> to <tt>99</tt>. </p>
<p> Perl 5.005 is the combined product of the new dual-track development scheme.</p>
<h2>Incompatible Changes</h2>
<h3><font SIZE="-1">WARNING:</font> This version is not binary compatible with Perl 5.004.</h3>
<p> Starting with Perl 5.004_50 there were many deep and far-reaching changes to the language internals. If you have dynamically loaded extensions that you built under perl 5.003 or 5.004, you can continue to use them with 5.004, but you will need to rebuild and reinstall those extensions to use them 5.005. See <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> for detailed instructions on how to upgrade.</p>
<h3>Default installation structure has changed</h3>
<p> The new Configure defaults are designed to allow a smooth upgrade from 5.004 to 5.005, but you should read <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> for a detailed discussion of the changes in order to adapt them to your system.</p>
<h3>Perl Source Compatibility</h3>
<p> When none of the experimental features are enabled, there should be very few user-visible Perl source compatibility issues. </p>
<p> If threads are enabled, then some caveats apply. <tt>@_</tt> and <tt>$_</tt> become lexical variables. The effect of this should be largely transparent to the user, but there are some boundary conditions under which user will need to be aware of the issues. For example, <tt>&quot;local(@_)&quot;</tt> results in a &#8220;Can&#8217;t localize lexical variable <tt>@_</tt> &#8230;&#8221; message. This may be enabled in a future version. </p>
<p> Some new keywords have been introduced. These are generally expected to have very little impact on compatibility. See &quot;New <tt>&quot;INIT&quot;</tt> keyword&quot;, &quot;New <tt>&quot;lock&quot;</tt> keyword&quot;, and &quot;New <tt>&quot;qr//&quot;</tt> operator&quot;. </p>
<p> Certain barewords are now reserved. Use of these will provoke a warning if you have asked for them with the <tt>&quot;-w&quot;</tt> switch. See &quot;<tt>&quot;our&quot;</tt> is now a reserved word&quot;.</p>
<h3>C Source Compatibility</h3>
<p> There have been a large number of changes in the internals to support the new features in this release.</p>
<dl>
<dt>&bull;</p>
<dd> Core sources now require <font SIZE="-1">ANSI C</font> compiler </p>
<p> An <font SIZE="-1">ANSI C</font> compiler is now <code>required</code> to build perl. See <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i>.</p>
<dt>&bull;</p>
<dd> All Perl global variables must now be referenced with an explicit prefix </p>
<p> All Perl global variables that are visible for use by extensions now have a <tt>&quot;PL_&quot;</tt> prefix. New extensions should <tt>&quot;not&quot;</tt> refer to perl globals by their unqualified names. To preserve sanity, we provide limited backward compatibility for globals that are being widely used like <tt>&quot;sv_undef&quot;</tt> and <tt>&quot;na&quot;</tt> (which should now be written as <tt>&quot;PL_sv_undef&quot;</tt>, <tt>&quot;PL_na&quot;</tt> etc.) </p>
<p> If you find that your <font SIZE="-1">XS</font> extension does not compile anymore because a perl global is not visible, try adding a <tt>&quot;PL_&quot;</tt> prefix to the global and rebuild. </p>
<p> It is strongly recommended that all functions in the Perl <font SIZE="-1">API</font> that don&#8217;t begin with <tt>&quot;perl&quot;</tt> be referenced with a <tt>&quot;Perl_&quot;</tt> prefix. The bare function names without the <tt>&quot;Perl_&quot;</tt> prefix are supported with macros, but this support may cease in a future release. </p>
<p> See perlapi.</p>
<dt>&bull;</p>
<dd> Enabling threads has source compatibility issues </p>
<p> Perl built with threading enabled requires extensions to use the new <tt>&quot;dTHR&quot;</tt> macro to initialize the handle to access per-thread data. If you see a compiler error that talks about the variable <tt>&quot;thr&quot;</tt> not being declared (when building a module that has <font SIZE="-1">XS</font> code), you need to add <tt>&quot;dTHR;&quot;</tt> at the beginning of the block that elicited the error. </p>
<p> The <font SIZE="-1">API</font> function <tt>&quot;perl_get_sv(&quot;@&quot;,GV_ADD)&quot;</tt> should be used instead of directly accessing perl globals as <tt>&quot;GvSV(errgv)&quot;</tt>. The <font SIZE="-1">API</font> call is backward compatible with existing perls and provides source compatibility with threading is enabled. </p>
<p> See &#8220;C Source Compatibility&#8221; for more information.</dl>
<h3>Binary Compatibility</h3>
<p> This version is <font SIZE="-1">NOT</font> binary compatible with older versions. All extensions will need to be recompiled. Further binaries built with threads enabled are incompatible with binaries built without. This should largely be transparent to the user, as all binary incompatible configurations have their own unique architecture name, and extension binaries get installed at unique locations. This allows coexistence of several configurations in the same directory hierarchy. See <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i>.</p>
<h3>Security fixes may affect compatibility</h3>
<p> A few taint leaks and taint omissions have been corrected. This may lead to &#8220;failure&#8221; of scripts that used to work with older versions. Compiling with -DINCOMPLETE_TAINTS provides a perl with minimal amounts of changes to the tainting behavior. But note that the resulting perl will have known insecurities. </p>
<p> Oneliners with the <tt>&quot;-e&quot;</tt> switch do not create temporary files anymore.</p>
<h3>Relaxed new mandatory warnings introduced in 5.004</h3>
<p> Many new warnings that were introduced in 5.004 have been made optional. Some of these warnings are still present, but perl&#8217;s new features make them less often a problem. See &#8220;New Diagnostics&#8221;.</p>
<h3>Licensing</h3>
<p> Perl has a new Social Contract for contributors. See <i>Porting/Contract</i>. </p>
<p> The license included in much of the Perl documentation has changed. Most of the Perl documentation was previously under the implicit <font SIZE="-1">GNU</font> General Public License or the Artistic License (at the user&#8217;s choice). Now much of the documentation unambiguously states the terms under which it may be distributed. Those terms are in general much less restrictive than the <font SIZE="-1">GNU GPL.</font> See perl and the individual perl manpages listed therein.</p>
<h2>Core Changes</h2>
<h3>Threads</h3>
<p> <font SIZE="-1">WARNING:</font> Threading is considered an <code>experimental</code> feature. Details of the implementation may change without notice. There are known limitations and some bugs. These are expected to be fixed in future versions. </p>
<p> See <i></i><font SIZE="-1"><i>README</i></font><i>.threads</i>.</p>
<h3>Compiler</h3>
<p> <font SIZE="-1">WARNING:</font> The Compiler and related tools are considered <code>experimental</code>. Features may change without notice, and there are known limitations and bugs. Since the compiler is fully external to perl, the default configuration will build and install it. </p>
<p> The Compiler produces three different types of transformations of a perl program. The C backend generates C code that captures perl&#8217;s state just before execution begins. It eliminates the compile-time overheads of the regular perl interpreter, but the run-time performance remains comparatively the same. The <font SIZE="-1">CC</font> backend generates optimized C code equivalent to the code path at run-time. The <font SIZE="-1">CC</font> backend has greater potential for big optimizations, but only a few optimizations are implemented currently. The Bytecode backend generates a platform independent bytecode representation of the interpreter&#8217;s state just before execution. Thus, the Bytecode back end also eliminates much of the compilation overhead of the interpreter. </p>
<p> The compiler comes with several valuable utilities. </p>
<p> <tt>&quot;B::Lint&quot;</tt> is an experimental module to detect and warn about suspicious code, especially the cases that the <tt>&quot;-w&quot;</tt> switch does not detect. </p>
<p> <tt>&quot;B::Deparse&quot;</tt> can be used to demystify perl code, and understand how perl optimizes certain constructs. </p>
<p> <tt>&quot;B::Xref&quot;</tt> generates cross reference reports of all definition and use of variables, subroutines and formats in a program. </p>
<p> <tt>&quot;B::Showlex&quot;</tt> show the lexical variables used by a subroutine or file at a glance. </p>
<p> <tt>&quot;perlcc&quot;</tt> is a simple frontend for compiling perl. </p>
<p> See <tt>&quot;ext/B/README&quot;</tt>, B, and the respective compiler modules.</p>
<h3>Regular Expressions</h3>
<p> Perl&#8217;s regular expression engine has been seriously overhauled, and many new constructs are supported. Several bugs have been fixed. </p>
<p> Here is an itemized summary:</p>
<dl>
<dt>Many new and improved optimizations</p>
<dd> Changes in the <font SIZE="-1">RE</font> engine: </p>
<pre><code>
Unneeded nodes removed;
Substrings merged together;
New types of nodes to process(SUBEXPR) * and similar expressions
                                         quickly,
    used if the SUBEXPR has no side effects and matches
    strings of the same length;
        Better optimizations by lookup for constant substrings;
        Better search for constants substrings anchored by $ ;
</code></pre>
<p> Changes in Perl code using <font SIZE="-1">RE</font> engine: </p>
<p>More optimizations to s / longer / short / ;<br />
study() was not working;<br />
/ blah / may be optimized to an analogue of index() if $ &amp;$` $&#8217; not seen; Unneeded copying of matched &#8211; against string removed;<br />
Only matched part of the string is copying if $` $&#8217; were not seen;</p>
<dt>Many bug fixes</p>
<dd> Note that only the major bug fixes are listed here. See <i>Changes</i> for others. </p>
<p>        Backtracking might not restore start of $3.<br />
        No feedback if max count for * or + on &#8220;complex&#8221; subexpression<br />
            was reached, similarly (but at compile time) for {3,34567}<br />
        Primitive restrictions on max count introduced to decrease a<br />
            possibility of a segfault;<br />
        (ZERO &#8211; LENGTH) * could segfault;<br />
        (ZERO &#8211; LENGTH) * was prohibited;<br />
        Long REs were not allowed;<br />
        / RE / g could skip matches at the same position after a zero &#8211; length match;</p>
<dt>New regular expression constructs</p>
<dd> The following new syntax elements are supported: </p>
<pre>
        (?&lt;=RE)
        (?&lt;!RE)
        (?{ CODE })
        (?i-x)
        (?i:RE)
        (?(COND)YES_RE|NO_RE)
        (?&gt;RE)
        \z
</pre>
<dt>New operator for precompiled regular expressions</p>
<dd> See &quot;New <tt>&quot;qr//&quot;</tt> operator&quot;.</p>
<dt>Other improvements</p>
<dd>
Better debugging output(possibly with colors),<br />
    even from non &#8211; debugging Perl;<br />
RE engine code now looks like C, not like assembler;<br />
Behaviour of RE modifiable by `use re&#8217; directive; Improved documentation;<br />
Test suite significantly extended;<br />
Syntax<br />
    [:^upper:] etc., reserved inside character classes;</p>
<dt>Incompatible changes</p>
<dd>
<pre>
        (?i) localized inside enclosing group;
        $( is not interpolated into RE any more;
        /RE/g may match at the same position (with non-zero length)
            after a zero-length match (bug fix).
</pre>
</dl>
<p> See perlre and perlop.</p>
<h3>Improved <code>malloc()</code></h3>
<p> See banner at the beginning of <tt>&quot;malloc.c&quot;</tt> for details.</p>
<h3>Quicksort is internally implemented</h3>
<p> Perl now contains its own highly optimized <code>qsort()</code> routine. The new <code>qsort()</code> is resistant to inconsistent comparison functions, so Perl&#8217;s <tt>&quot;sort()&quot;</tt> will not provoke coredumps any more when given poorly written sort subroutines. (Some C library <tt>&quot;qsort()&quot;</tt>s that were being used before used to have this problem.) In our testing, the new <tt>&quot;qsort()&quot;</tt> required the minimal number of pair-wise compares on average, among all known <tt>&quot;qsort()&quot;</tt> implementations. </p>
<p> See <tt>&quot;perlfunc/sort&quot;</tt>.</p>
<h3>Reliable signals</h3>
<p> Perl&#8217;s signal handling is susceptible to random crashes, because signals arrive asynchronously, and the Perl runtime is not reentrant at arbitrary times. </p>
<p> However, one experimental implementation of reliable signals is available when threads are enabled. See <tt>&quot;Thread::Signal&quot;</tt>. Also see <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> for how to build a Perl capable of threads.</p>
<h3>Reliable stack pointers</h3>
<p> The internals now reallocate the perl stack only at predictable times. In particular, magic calls never trigger reallocations of the stack, because all reentrancy of the runtime is handled using a &#8220;stack of stacks&#8221;. This should improve reliability of cached stack pointers in the internals and in XSUBs.</p>
<h3>More generous treatment of carriage returns</h3>
<p> Perl used to complain if it encountered literal carriage returns in scripts. Now they are mostly treated like whitespace within program text. Inside string literals and here documents, literal carriage returns are ignored if they occur paired with linefeeds, or get interpreted as whitespace if they stand alone. This behavior means that literal carriage returns in files should be avoided. You can get the older, more compatible (but less generous) behavior by defining the preprocessor symbol <tt>&quot;PERL_STRICT_CR&quot;</tt> when building perl. Of course, all this has nothing whatever to do with how escapes like <tt>&quot;&quot;</tt> are handled within strings. </p>
<p> Note that this doesn&#8217;t somehow magically allow you to keep all text files in <font SIZE="-1">DOS</font> format. The generous treatment only applies to files that perl itself parses. If your C compiler doesn&#8217;t allow carriage returns in files, you may still be unable to build modules that need a C compiler.</p>
<h3>Memory leaks</h3>
<p> <tt>&quot;substr&quot;</tt>, <tt>&quot;pos&quot;</tt> and <tt>&quot;vec&quot;</tt> don&#8217;t leak memory anymore when used in lvalue context. Many small leaks that impacted applications that embed multiple interpreters have been fixed.</p>
<h3>Better support for multiple interpreters</h3>
<p> The build-time option <tt>&quot;-DMULTIPLICITY&quot;</tt> has had many of the details reworked. Some previously global variables that should have been per-interpreter now are. With care, this allows interpreters to call each other. See the <tt>&quot;PerlInterp&quot;</tt> extension on <font SIZE="-1">CPAN.</font></p>
<h3>Behavior of <code>local()</code> on array and hash elements is now well-defined</h3>
<p> See &#8220;Temporary Values via <code>local()</code>&#8221; in perlsub.</p>
<h3>%! is transparently tied to the Errno module</h3>
<p> See perlvar, and Errno.</p>
<h3>Pseudo-hashes are supported</h3>
<p> See perlref.</p>
<h3>EXPR foreach EXPR is supported</h3>
<p> See perlsyn.</p>
<h3>Keywords can be globally overridden</h3>
<p> See perlsub.</p>
<h3>$^E is meaningful on Win32</h3>
<p> See perlvar.</p>
<h3>foreach (1..1000000) optimized</h3>
<p> <tt>&quot;foreach (1..1000000)&quot;</tt> is now optimized into a counting loop. It does not try to allocate a 1000000-size list anymore.</p>
<h3>Foo:: can be used as implicitly quoted package name</h3>
<p> Barewords caused unintuitive behavior when a subroutine with the same name as a package happened to be defined. Thus, <tt>&quot;new Foo @args&quot;</tt>, use the result of the call to <tt>&quot;Foo()&quot;</tt> instead of <tt>&quot;Foo&quot;</tt> being treated as a literal. The recommended way to write barewords in the indirect object slot is <tt>&quot;new Foo:: @args&quot;</tt>. Note that the method <tt>&quot;new()&quot;</tt> is called with a first argument of <tt>&quot;Foo&quot;</tt>, not <tt>&quot;Foo::&quot;</tt> when you do that.</p>
<h3>exists $Foo::{Bar::} tests existence of a package</h3>
<p> It was impossible to test for the existence of a package without actually creating it before. Now <tt>&quot;exists $Foo::{Bar::}&quot;</tt> can be used to test if the <tt>&quot;Foo::Bar&quot;</tt> namespace has been created.</p>
<h3>Better locale support</h3>
<p> See perllocale.</p>
<h3>Experimental support for 64-bit platforms</h3>
<p> Perl5 has always had 64-bit support on systems with 64-bit longs. Starting with 5.005, the beginnings of experimental support for systems with 32-bit long and 64-bit &#8216;long long&#8217; integers has been added. If you add -DUSE_LONG_LONG to your ccflags in config.sh (or manually define it in perl.h) then perl will be built with &#8216;long long&#8217; support. There will be many compiler warnings, and the resultant perl may not work on all systems. There are many other issues related to third-party extensions and libraries. This option exists to allow people to work on those issues.</p>
<h3><code>prototype()</code> returns useful results on builtins</h3>
<p> See &#8220;prototype&#8221; in perlfunc.</p>
<h3>Extended support for exception handling</h3>
<p> <tt>&quot;die()&quot;</tt> now accepts a reference value, and <tt>$@</tt> gets set to that value in exception traps. This makes it possible to propagate exception objects. This is an undocumented <code>experimental</code> feature.</p>
<h3>Re-blessing in <font SIZE="-1"><code>DESTROY</code></font><code>()</code> supported for chaining <font SIZE="-1"><code>DESTROY</code></font><code>()</code> methods</h3>
<p> See &#8220;Destructors&#8221; in perlobj.</p>
<h3>All printf format conversions are handled internally</h3>
<p> See &#8220;printf&#8221; in perlfunc.</p>
<h3>New INIT keyword</h3>
<p> <tt>&quot;INIT&quot;</tt> subs are like <tt>&quot;BEGIN&quot;</tt> and <tt>&quot;END&quot;</tt>, but they get run just before the perl runtime begins execution. e.g., the Perl Compiler makes use of <tt>&quot;INIT&quot;</tt> blocks to initialize and resolve pointers to XSUBs.</p>
<h3>New lock keyword</h3>
<p> The <tt>&quot;lock&quot;</tt> keyword is the fundamental synchronization primitive in threaded perl. When threads are not enabled, it is currently a noop. </p>
<p> To minimize impact on source compatibility this keyword is &#8220;weak&#8221;, i.e., any user-defined subroutine of the same name overrides it, unless a <tt>&quot;use Thread&quot;</tt> has been seen.</p>
<h3>New qr// operator</h3>
<p> The <tt>&quot;qr//&quot;</tt> operator, which is syntactically similar to the other quote-like operators, is used to create precompiled regular expressions. This compiled form can now be explicitly passed around in variables, and interpolated in other regular expressions. See perlop.</p>
<h3>our is now a reserved word</h3>
<p> Calling a subroutine with the name <tt>&quot;our&quot;</tt> will now provoke a warning when using the <tt>&quot;-w&quot;</tt> switch.</p>
<h3>Tied arrays are now fully supported</h3>
<p> See Tie::Array.</p>
<h3>Tied handles support is better</h3>
<p> Several missing hooks have been added. There is also a new base class for <font SIZE="-1">TIEARRAY</font> implementations. See Tie::Array.</p>
<h3>4th argument to substr</h3>
<p> <code>substr()</code> can now both return and replace in one operation. The optional 4th argument is the replacement string. See &#8220;substr&#8221; in perlfunc.</p>
<h3>Negative <font SIZE="-1">LENGTH</font> argument to splice</h3>
<p> <code>splice()</code> with a negative <font SIZE="-1">LENGTH</font> argument now work similar to what the <font SIZE="-1">LENGTH</font> did for <code>substr()</code>. Previously a negative <font SIZE="-1">LENGTH</font> was treated as 0. See &#8220;splice&#8221; in perlfunc.</p>
<h3>Magic lvalues are now more magical</h3>
<p> When you say something like <tt>&quot;substr($x, 5) = &quot;hi&quot;&quot;</tt>, the scalar returned by <code>substr()</code> is special, in that any modifications to it affect <tt>$x</tt>. (This is called a &#8216;magic lvalue&#8217; because an &#8216;lvalue&#8217; is something on the left side of an assignment.) Normally, this is exactly what you would expect to happen, but Perl uses the same magic if you use <code>substr()</code>, <code>pos()</code>, or <code>vec()</code> in a context where they might be modified, like taking a reference with <tt>&quot;\&quot;</tt> or as an argument to a sub that modifies <tt>@_</tt>. In previous versions, this &#8216;magic&#8217; only went one way, but now changes to the scalar the magic refers to ($x in the above example) affect the magic lvalue too. For instance, this code now acts differently: </p>
<p>$x = &#8220;hello&#8221;;<br />
sub printit<br />
{<br />
    $x = &#8220;g&#8217;bye&#8221;;<br />
    print $_[0], &#8220;
&#8221;;<br />
}<br />
printit(substr($x, 0, 5));</p>
<p> In previous versions, this would print &#8220;hello&#8221;, but it now prints &#8220;g&#8217;bye&#8221;.</p>
<h3>&lt;&gt; now reads in records</h3>
<p> If <tt>$/</tt> is a reference to an integer, or a scalar that holds an integer, &lt;&gt; will read in records instead of lines. For more info, see &#8220;$/&#8221; in perlvar.</p>
<h2>Supported Platforms</h2>
<p> Configure has many incremental improvements. Site-wide policy for building perl can now be made persistent, via Policy.sh. Configure also records the command-line arguments used in <i>config.sh</i>.</p>
<h3>New Platforms</h3>
<p> BeOS is now supported. See <i></i><font SIZE="-1"><i>README</i></font><i>.beos</i>. </p>
<p> <font SIZE="-1">DOS</font> is now supported under the <font SIZE="-1">DJGPP</font> tools. See <i></i><font SIZE="-1"><i>README</i></font><i>.dos</i> (installed as perldos on some systems). </p>
<p> MiNT is now supported. See <i></i><font SIZE="-1"><i>README</i></font><i>.mint</i>. </p>
<p> MPE/iX is now supported. See <font SIZE="-1">README</font>.mpeix. </p>
<p> <font SIZE="-1">MVS</font> (aka <font SIZE="-1">OS390,</font> aka Open Edition) is now supported. See <i></i><font SIZE="-1"><i>README</i></font><i>.os390</i> (installed as perlos390 on some systems). </p>
<p> Stratus <font SIZE="-1">VOS</font> is now supported. See <i></i><font SIZE="-1"><i>README</i></font><i>.vos</i>.</p>
<h3>Changes in existing support</h3>
<p> Win32 support has been vastly enhanced. Support for Perl Object, a C<font SIZE="-2">++</font> encapsulation of Perl. <font SIZE="-1">GCC</font> and <font SIZE="-1">EGCS</font> are now supported on Win32. See <i></i><font SIZE="-1"><i>README</i></font><i>.win32</i>, aka perlwin32. </p>
<p> <font SIZE="-1">VMS</font> configuration system has been rewritten. See <i></i><font SIZE="-1"><i>README</i></font><i>.vms</i> (installed as <i>README_vms</i> on some systems). </p>
<p> The hints files for most Unix platforms have seen incremental improvements.</p>
<h2>Modules and Pragmata</h2>
<h3>New Modules</h3>
<dl>
<dt>B</p>
<dd> Perl compiler and tools. See B.</p>
<dt>Data::Dumper</p>
<dd> A module to pretty print Perl data. See Data::Dumper.</p>
<dt>Dumpvalue</p>
<dd> A module to dump perl values to the screen. See Dumpvalue.</p>
<dt>Errno</p>
<dd> A module to look up errors more conveniently. See Errno.</p>
<dt>File::Spec</p>
<dd> A portable <font SIZE="-1">API</font> for file operations.</p>
<dt>ExtUtils::Installed</p>
<dd> Query and manage installed modules.</p>
<dt>ExtUtils::Packlist</p>
<dd> Manipulate .packlist files.</p>
<dt>Fatal</p>
<dd> Make functions/builtins succeed or die.</p>
<dt>IPC::SysV</p>
<dd> Constants and other support infrastructure for System V <font SIZE="-1">IPC</font> operations in perl.</p>
<dt>Test</p>
<dd> A framework for writing test suites.</p>
<dt>Tie::Array</p>
<dd> Base class for tied arrays.</p>
<dt>Tie::Handle</p>
<dd> Base class for tied handles.</p>
<dt>Thread</p>
<dd> Perl thread creation, manipulation, and support.</p>
<dt>attrs</p>
<dd> Set subroutine attributes.</p>
<dt>fields</p>
<dd> Compile-time class fields.</p>
<dt>re</p>
<dd> Various pragmata to control behavior of regular expressions.</dl>
<h3>Changes in existing modules</h3>
<dl>
<dt>Benchmark</p>
<dd> You can now run tests for <i>x</i> seconds instead of guessing the right number of tests to run. </p>
<p> Keeps better time.</p>
<dt>Carp</p>
<dd> Carp has a new function <code>cluck()</code>. <code>cluck()</code> warns, like <code>carp()</code>, but also adds a stack backtrace to the error message, like <code>confess()</code>.</p>
<dt><font SIZE="-1">CGI</font></p>
<dd> <font SIZE="-1">CGI</font> has been updated to version 2.42.</p>
<dt>Fcntl</p>
<dd> More Fcntl constants added: F_SETLK64, F_SETLKW64, O_LARGEFILE for large (more than 4G) file access (the 64-bit support is not yet working, though, so no need to get overly excited), Free/Net/OpenBSD locking behaviour flags F_FLOCK, F_POSIX, Linux F_SHLCK, and O_ACCMODE: the mask of O_RDONLY, O_WRONLY, and O_RDWR.</p>
<dt>Math::Complex</p>
<dd> The accessors methods Re, Im, arg, abs, rho, theta, methods can ($z-&gt;<code>Re()</code>) now also act as mutators ($z-&gt;<code><a href="/docs/linux/man/3-re/">Re</a></code>(3)).</p>
<dt>Math::Trig</p>
<dd> A little bit of radial trigonometry (cylindrical and spherical) added, for example the great circle distance.</p>
<dt><font SIZE="-1">POSIX</font></p>
<dd> <font SIZE="-1">POSIX</font> now has its own platform-specific hints files.</p>
<dt>DB_File</p>
<dd> DB_File supports version 2.x of Berkeley <font SIZE="-1">DB.</font> See <tt>&quot;ext/DB_File/Changes&quot;</tt>.</p>
<dt>MakeMaker</p>
<dd> MakeMaker now supports writing empty makefiles, provides a way to specify that site <code>umask()</code> policy should be honored. There is also better support for manipulation of .packlist files, and getting information about installed modules. </p>
<p> Extensions that have both architecture-dependent and architecture-independent files are now always installed completely in the architecture-dependent locations. Previously, the shareable parts were shared both across architectures and across perl versions and were therefore liable to be overwritten with newer versions that might have subtle incompatibilities.</p>
<dt><font SIZE="-1">CPAN</font></p>
<dd> See perlmodinstall and <font SIZE="-1">CPAN</font>.</p>
<dt>Cwd</p>
<dd> Cwd::cwd is faster on most platforms.</dl>
<h2>Utility Changes</h2>
<p> <tt>&quot;h2ph&quot;</tt> and related utilities have been vastly overhauled. </p>
<p> <tt>&quot;perlcc&quot;</tt>, a new experimental front end for the compiler is available. </p>
<p> The crude <font SIZE="-1">GNU</font> <tt>&quot;configure&quot;</tt> emulator is now called <tt>&quot;configure.gnu&quot;</tt> to avoid trampling on <tt>&quot;Configure&quot;</tt> under case-insensitive filesystems. </p>
<p> <tt>&quot;perldoc&quot;</tt> used to be rather slow. The slower features are now optional. In particular, case-insensitive searches need the <tt>&quot;-i&quot;</tt> switch, and recursive searches need <tt>&quot;-r&quot;</tt>. You can set these switches in the <tt>&quot;PERLDOC&quot;</tt> environment variable to get the old behavior.</p>
<h2>Documentation Changes</h2>
<p> Config.pm now has a glossary of variables. </p>
<p> <i>Porting/patching.pod</i> has detailed instructions on how to create and submit patches for perl. </p>
<p> perlport specifies guidelines on how to write portably. </p>
<p> perlmodinstall describes how to fetch and install modules from <tt>&quot;CPAN&quot;</tt> sites. </p>
<p> Some more Perl traps are documented now. See perltrap. </p>
<p> perlopentut gives a tutorial on using <code>open()</code>. </p>
<p> perlreftut gives a tutorial on references. </p>
<p> perlthrtut gives a tutorial on threads.</p>
<h2>New Diagnostics</h2>
<dl>
<dt>Ambiguous call resolved as CORE::%s(), qualify as such or use &amp;</p>
<dd> (W) A subroutine you have declared has the same name as a Perl keyword, and you have used the name without qualification for calling one or the other. Perl decided to call the builtin because the subroutine is not imported. </p>
<p> To force interpretation as a subroutine call, either put an ampersand before the subroutine name, or qualify the name with its package. Alternatively, you can import the subroutine (or pretend that it&#8217;s imported with the <tt>&quot;use subs&quot;</tt> pragma). </p>
<p> To silently interpret it as the Perl operator, use the <tt>&quot;CORE::&quot;</tt> prefix on the operator (e.g. <tt>&quot;CORE::log($x)&quot;</tt>) or by declaring the subroutine to be an object method (see &#8220;attrs&#8221;).</p>
<dt>Bad index while coercing array into hash</p>
<dd> (F) The index looked up in the hash found as the 0&#8217;th element of a pseudo-hash is not legal. Index values must be at 1 or greater. See perlref.</p>
<dt>Bareword &quot;%s&quot; refers to nonexistent package</p>
<dd> (W) You used a qualified bareword of the form <tt>&quot;Foo::&quot;</tt>, but the compiler saw no other uses of that namespace before that point. Perhaps you need to predeclare a package?</p>
<dt>Can&#8217;t call method &quot;%s&quot; on an undefined value</p>
<dd> (F) You used the syntax of a method call, but the slot filled by the object reference or package name contains an undefined value. Something like this will reproduce the error: </p>
<p>$BADREF = 42;<br />
process $BADREF 1, 2, 3;<br />
$BADREF-&gt;process(1, 2, 3);</p>
<dt>Can&#8217;t check filesystem of script &quot;%s&quot; for nosuid</p>
<dd> (P) For some reason you can&#8217;t check the filesystem of the script for nosuid.</p>
<dt>Can&#8217;t coerce array into hash</p>
<dd> (F) You used an array where a hash was expected, but the array has no information on how to map from keys to array indices. You can do that only with arrays that have a hash reference at index 0.</p>
<dt>Can&#8217;t goto subroutine from an eval-string</p>
<dd> (F) The &#8220;goto subroutine&#8221; call can&#8217;t be used to jump out of an eval &#8220;string&#8221;. (You can use it to jump out of an eval {<font SIZE="-1">BLOCK</font>}, but you probably don&#8217;t want to.)</p>
<dt>Can&#8217;t localize pseudo-hash element</p>
<dd> (F) You said something like <tt>&quot;local $ar-&gt;{'key'}&quot;</tt>, where <tt>$ar</tt> is a reference to a pseudo-hash. That hasn&#8217;t been implemented yet, but you can get a similar effect by localizing the corresponding array element directly: <tt>&quot;local $ar-&gt;[$ar-&gt;[0]{'key'}]&quot;</tt>.</p>
<dt>Can&#8217;t use %%! because Errno.pm is not available</p>
<dd> (F) The first time the %! hash is used, perl automatically loads the Errno.pm module. The Errno module is expected to tie the %! hash to provide symbolic names for <tt>$!</tt> errno values.</p>
<dt>Cannot find an opnumber for &quot;%s&quot;</p>
<dd> (F) A string of a form <tt>&quot;CORE::word&quot;</tt> was given to <code>prototype()</code>, but there is no builtin with the name <tt>&quot;word&quot;</tt>.</p>
<dt>Character class syntax [. .] is reserved for future extensions</p>
<dd> (W) Within regular expression character classes ([]) the syntax beginning with &#8220;[.&#8221; and ending with &#8220;.]&#8221; is reserved for future extensions. If you need to represent those character sequences inside a regular expression character class, just quote the square brackets with the backslash: &#8220;\[.&#8221; and &#8220;.\]&#8221;.</p>
<dt>Character class syntax [: :] is reserved for future extensions</p>
<dd> (W) Within regular expression character classes ([]) the syntax beginning with &#8220;[:&#8221; and ending with &#8220;:]&#8221; is reserved for future extensions. If you need to represent those character sequences inside a regular expression character class, just quote the square brackets with the backslash: &#8220;\[:&#8221; and &#8220;:\]&#8221;.</p>
<dt>Character class syntax [= =] is reserved for future extensions</p>
<dd> (W) Within regular expression character classes ([]) the syntax beginning with &#8220;[=&#8221; and ending with &#8220;=]&#8221; is reserved for future extensions. If you need to represent those character sequences inside a regular expression character class, just quote the square brackets with the backslash: &#8220;\[=&#8221; and &#8220;=\]&#8221;.</p>
<dt>%s: Eval-group in insecure regular expression</p>
<dd> (F) Perl detected tainted data when trying to compile a regular expression that contains the <tt>&quot;(?{ ... })&quot;</tt> zero-width assertion, which is unsafe. See &#8220;(?{ code })&#8221; in perlre, and perlsec.</p>
<dt>%s: Eval-group not allowed, use re &#8216;eval&#8217;</p>
<dd> (F) A regular expression contained the <tt>&quot;(?{ ... })&quot;</tt> zero-width assertion, but that construct is only allowed when the <tt>&quot;use re 'eval'&quot;</tt> pragma is in effect. See &#8220;(?{ code })&#8221; in perlre.</p>
<dt>%s: Eval-group not allowed at run time</p>
<dd> (F) Perl tried to compile a regular expression containing the <tt>&quot;(?{ ... })&quot;</tt> zero-width assertion at run time, as it would when the pattern contains interpolated values. Since that is a security risk, it is not allowed. If you insist, you may still do this by explicitly building the pattern from an interpolated string at run time and using that in an <code>eval()</code>. See &#8220;(?{ code })&#8221; in perlre.</p>
<dt>Explicit blessing to &#8221; (assuming package main)</p>
<dd> (W) You are blessing a reference to a zero length string. This has the effect of blessing the reference into the package main. This is usually not what you want. Consider providing a default target package, e.g. bless($ref, <tt>$p</tt> || &#8216;MyPackage&#8217;);</p>
<dt>Illegal hex digit ignored</p>
<dd> (W) You may have tried to use a character other than 0 &#8211; 9 or A &#8211; F in a hexadecimal number. Interpretation of the hexadecimal number stopped before the illegal character.</p>
<dt>No such array field</p>
<dd> (F) You tried to access an array as a hash, but the field name used is not defined. The hash at index 0 should map all valid field names to array indices for that to work.</p>
<dt>No such field &quot;%s&quot; in variable %s of type %s</p>
<dd> (F) You tried to access a field of a typed variable where the type does not know about the field name. The field names are looked up in the <tt>%FIELDS</tt> hash in the type package at compile time. The <tt>%FIELDS</tt> hash is usually set up with the &#8216;fields&#8217; pragma.</p>
<dt>Out of memory during ridiculously large request</p>
<dd> (F) You can&#8217;t allocate more than 2^31+&#8220;small amount&#8221; bytes. This error is most likely to be caused by a typo in the Perl program. e.g., <tt>$arr[time]</tt> instead of <tt>$arr[$time]</tt>.</p>
<dt>Range iterator outside integer range</p>
<dd> (F) One (or both) of the numeric arguments to the range operator &#8220;..&#8221; are outside the range which can be represented by integers internally. One possible workaround is to force Perl to use magical string increment by prepending &#8220;0&#8221; to your numbers.</p>
<dt>Recursive inheritance detected while looking for method &#8216;%s&#8217; %s</p>
<dd> (F) More than 100 levels of inheritance were encountered while invoking a method. Probably indicates an unintended loop in your inheritance hierarchy.</p>
<dt>Reference found where even-sized list expected</p>
<dd> (W) You gave a single reference where Perl was expecting a list with an even number of elements (for assignment to a hash). This usually means that you used the anon hash constructor when you meant to use parens. In any case, a hash requires key/value <code>pairs</code>. </p>
<pre><code>
% hash = {
    one = &gt; 1,
    two = &gt; 2,
};
#WRONG % hash = [qw / an anon array / ];
#WRONG % hash = (one = &gt; 1, two = &gt; 2, );
#right % hash = qw(one 1 two 2);
#also fine
</code></pre>
<dt>Undefined value assigned to typeglob</p>
<dd> (W) An undefined value was assigned to a typeglob, a la <tt>&quot;*foo = undef&quot;</tt>. This does nothing. It&#8217;s possible that you really mean <tt>&quot;undef *foo&quot;</tt>.</p>
<dt>Use of reserved word &quot;%s&quot; is deprecated</p>
<dd> (D) The indicated bareword is a reserved word. Future versions of perl may use it as a keyword, so you&#8217;re better off either explicitly quoting the word in a manner appropriate for its context of use, or using a different name altogether. The warning can be suppressed for subroutine names by either adding a <tt>&quot;&amp;&quot;</tt> prefix, or using a package qualifier, e.g. <tt>&quot;&amp;our()&quot;</tt>, or <tt>&quot;Foo::our()&quot;</tt>.</p>
<dt>perl: warning: Setting locale failed.</p>
<dd> (S) The whole warning message will look something like: </p>
<pre>
       perl: warning: Setting locale failed.
       perl: warning: Please check that your locale settings:
               LC_ALL = &quot;En_US&quot;,
               LANG = (unset)
           are supported and installed on your system.
       perl: warning: Falling back to the standard locale (&quot;C&quot;).
</pre>
<p> Exactly what were the failed locale settings varies. In the above the settings were that the <font SIZE="-1">LC_ALL</font> was &#8220;En_US&#8221; and the <font SIZE="-1">LANG</font> had no value. This error means that Perl detected that you and/or your system administrator have set up the so-called variable system but Perl could not use those settings. This was not dead serious, fortunately: there is a &#8220;default locale&#8221; called &#8220;C&#8221; that Perl can and will use, the script will be run. Before you really fix the problem, however, you will get the same error message each time you run Perl. How to really fix the problem can be found in &#8220;<font SIZE="-1">LOCALE PROBLEMS&#8221;</font> in perllocale.</dl>
<h2>Obsolete Diagnostics</h2>
<dl>
<dt>Can&#8217;t <code>mktemp()</code></p>
<dd> (F) The <code>mktemp()</code> routine failed for some reason while trying to process a <code>-e</code> switch. Maybe your /tmp partition is full, or clobbered. </p>
<p> Removed because <code>-e</code> doesn&#8217;t use temporary files any more.</p>
<dt>Can&#8217;t write to temp file for <code>-e</code>: %s</p>
<dd> (F) The write routine failed for some reason while trying to process a <code>-e</code> switch. Maybe your /tmp partition is full, or clobbered. </p>
<p> Removed because <code>-e</code> doesn&#8217;t use temporary files any more.</p>
<dt>Cannot open temporary file</p>
<dd> (F) The create routine failed for some reason while trying to process a <code>-e</code> switch. Maybe your /tmp partition is full, or clobbered. </p>
<p> Removed because <code>-e</code> doesn&#8217;t use temporary files any more.</p>
<dt>regexp too big</p>
<dd> (F) The current implementation of regular expressions uses shorts as address offsets within a string. Unfortunately this means that if the regular expression compiles to longer than 32767, it&#8217;ll blow up. Usually when you want a regular expression this big, there is a better way to do it with multiple statements. See perlre.</dl>
<h2>Configuration Changes</h2>
<p> You can use &#8220;Configure -Uinstallusrbinperl&#8221; which causes installperl to skip installing perl also as /usr/bin/perl. This is useful if you prefer not to modify /usr/bin for some reason or another but harmful because many scripts assume to find Perl in /usr/bin/perl.</p>
<h2>BUGS</h2>
<p> If you find what you think is a bug, you might check the headers of recently posted articles in the comp.lang.perl.misc newsgroup. There may also be information at <a rel="nofollow" href="http://www.perl.com/perl/">http://www.perl.com/perl/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Make sure you trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to &lt;<i>perlbug [at] perl.com</i>&gt; to be analysed by the Perl porting team.</p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information.</p>
<h2>HISTORY</h2>
<p> Written by Gurusamy Sarathy &lt;<i>gsar [at] activestate.com</i>&gt;, with many contributions from The Perl Porters. </p>
<p> Send omissions or corrections to &lt;<i>perlbug [at] perl.com</i>&gt;. </p>
<h2>Index</h2>
<dt><a href="#lbAN">Core Changes</a></p>
<dd>
<dt><a href="#lbBX">Supported Platforms</a></p>
<dd>
<dt><a href="#lbCA">Modules and Pragmata</a></p>
<dd>
<dt><a href="#lbCD">Utility Changes</a></p>
<dd>
<dt><a href="#lbCE">Documentation Changes</a></p>
<dd>
<dt><a href="#lbCF">New Diagnostics</a></p>
<dd>
<dt><a href="#lbCG">Obsolete Diagnostics</a></p>
<dd>
<dt><a href="#lbCH">Configuration Changes</a></p>
<dd>
<dt><a href="#lbCI">BUGS</a></p>
<dd>
<dt><a href="#lbCJ">SEE ALSO</a></p>
<dd>
<dt><a href="#lbCK">HISTORY</a></p>
<dd></dl>
