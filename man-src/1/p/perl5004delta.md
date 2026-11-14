---
title: "perl5004delta(1)"
name: "perl5004delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5004delta/"
description: "perl5004delta – what’s new for perl5.004"
---

<h2 class="name">NAME</h2>
<p> perl5004delta &#8211; what&#8217;s new for perl5.004 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.003 release (as documented in <i>Programming Perl</i>, second edition&#8212;the Camel Book) and this one.</p>
<h2>Supported Environments</h2>
<p> Perl5.004 builds out of the box on Unix, Plan 9, LynxOS, <font SIZE="-1">VMS, OS/2, QNX,</font> AmigaOS, and Windows <font SIZE="-1">NT.</font> Perl runs on Windows 95 as well, but it cannot be built there, for lack of a reasonable command interpreter.</p>
<h2>Core Changes</h2>
<p> Most importantly, many bugs were fixed, including several security problems. See the <i>Changes</i> file in the distribution for details.</p>
<h3>List assignment to %ENV works</h3>
<p> <tt>&quot;%ENV = ()&quot;</tt> and <tt>&quot;%ENV = @list&quot;</tt> now work as expected (except on <font SIZE="-1">VMS</font> where it generates a fatal error).</p>
<h3>Change to Can&#8217;t locate Foo.pm in @INC error</h3>
<p> The error &#8220;Can&#8217;t locate Foo.pm in <tt>@INC</tt>&#8221; now lists the contents of <tt>@INC</tt> for easier debugging.</p>
<h3>Compilation option: Binary compatibility with 5.003</h3>
<p> There is a new Configure question that asks if you want to maintain binary compatibility with Perl 5.003. If you choose binary compatibility, you do not have to recompile your extensions, but you might have symbol conflicts if you embed Perl in another application, just as in the 5.003 release. By default, binary compatibility is preserved at the expense of symbol table pollution.</p>
<h3>$PERL5OPT environment variable</h3>
<p> You may now put Perl options in the <tt>$PERL5OPT</tt> environment variable. Unless Perl is running with taint checks, it will interpret this variable as if its contents had appeared on a &#8220;#!perl&#8221; line at the beginning of your script, except that hyphens are optional. <font SIZE="-1">PERL5OPT</font> may only be used to set the following switches: <code>-[DIMUdmw]</code>.</p>
<h3>Limitations on <code>-M</code>, <code>-m</code>, and <code>-T</code> options</h3>
<p> The <tt>&quot;-M&quot;</tt> and <tt>&quot;-m&quot;</tt> options are no longer allowed on the <tt>&quot;#!&quot;</tt> line of a script. If a script needs a module, it should invoke it with the <tt>&quot;use&quot;</tt> pragma. </p>
<p> The <code>-T</code> option is also forbidden on the <tt>&quot;#!&quot;</tt> line of a script, unless it was present on the Perl command line. Due to the way <tt>&quot;#!&quot;</tt> works, this usually means that <code>-T</code> must be in the first argument. Thus: </p>
<pre>
    #!/usr/bin/perl -T -w
</pre>
<p> will probably work for an executable script invoked as <tt>&quot;scriptname&quot;</tt>, while: </p>
<pre>
    #!/usr/bin/perl -w -T
</pre>
<p> will probably fail under the same conditions. (Non-Unix systems will probably not follow this rule.) But <tt>&quot;perl scriptname&quot;</tt> is guaranteed to fail, since then there is no chance of <code>-T</code> being found on the command line before it is found on the <tt>&quot;#!&quot;</tt> line.</p>
<h3>More precise warnings</h3>
<p> If you removed the <code>-w</code> option from your Perl 5.003 scripts because it made Perl too verbose, we recommend that you try putting it back when you upgrade to Perl 5.004. Each new perl version tends to remove some undesirable warnings, while adding new warnings that may catch bugs in your scripts.</p>
<h3>Deprecated: Inherited AUTOLOAD for non-methods</h3>
<p> Before Perl 5.004, <tt>&quot;AUTOLOAD&quot;</tt> functions were looked up as methods (using the <tt>@ISA</tt> hierarchy), even when the function to be autoloaded was called as a plain function (e.g. <tt>&quot;Foo::bar()&quot;</tt>), not a method (e.g. <tt>&quot;Foo-&gt;bar()&quot;</tt> or <tt>&quot;$obj-&gt;bar()&quot;</tt>). </p>
<p> Perl 5.005 will use method lookup only for methods&#8217; <tt>&quot;AUTOLOAD&quot;</tt>s. However, there is a significant base of existing code that may be using the old behavior. So, as an interim step, Perl 5.004 issues an optional warning when a non-method uses an inherited <tt>&quot;AUTOLOAD&quot;</tt>. </p>
<p> The simple rule is: Inheritance will not work when autoloading non-methods. The simple fix for old code is: In any module that used to depend on inheriting <tt>&quot;AUTOLOAD&quot;</tt> for non-methods from a base class named <tt>&quot;BaseClass&quot;</tt>, execute <tt>&quot;*AUTOLOAD = \&amp;BaseClass::AUTOLOAD&quot;</tt> during startup.</p>
<h3>Previously deprecated %OVERLOAD is no longer usable</h3>
<p> Using <tt>%OVERLOAD</tt> to define overloading was deprecated in 5.003. Overloading is now defined using the overload pragma. <tt>%OVERLOAD</tt> is still used internally but should not be used by Perl scripts. See overload for more details.</p>
<h3>Subroutine arguments created only when they&#8217;re modified</h3>
<p> In Perl 5.004, nonexistent array and hash elements used as subroutine parameters are brought into existence only if they are actually assigned to (via <tt>@_</tt>). </p>
<p> Earlier versions of Perl vary in their handling of such arguments. Perl versions 5.002 and 5.003 always brought them into existence. Perl versions 5.000 and 5.001 brought them into existence only if they were not the first argument (which was almost certainly a bug). Earlier versions of Perl never brought them into existence. </p>
<p> For example, given this code: </p>
<pre><code>
undef @a;
undef % a;
sub show{print $_[0]};
sub change{$_[0]++};
show($a[2]);
change($a{b});
</code></pre>
<p> After this code executes in Perl 5.004, <tt>$a</tt>{b} exists but <tt>$a</tt>[2] does not. In Perl 5.002 and 5.003, both <tt>$a</tt>{b} and <tt>$a</tt>[2] would have existed (but <tt>$a</tt>[2]&#8217;s value would have been undefined).</p>
<h3>Group vector changeable with $)</h3>
<p> The <tt>$)</tt> special variable has always (well, in Perl 5, at least) reflected not only the current effective group, but also the group list as returned by the <tt>&quot;getgroups()&quot;</tt> C function (if there is one). However, until this release, there has not been a way to call the <tt>&quot;setgroups()&quot;</tt> C function from Perl. </p>
<p> In Perl 5.004, assigning to <tt>$)</tt> is exactly symmetrical with examining it: The first number in its string value is used as the effective gid; if there are any numbers after the first one, they are passed to the <tt>&quot;setgroups()&quot;</tt> C function (if there is one).</p>
<h3>Fixed parsing of $$&lt;digit&gt;, &amp;$&lt;digit&gt;, etc.</h3>
<p> Perl versions before 5.004 misinterpreted any type marker followed by &#8220;$&#8221; and a digit. For example, &#8220;$$0&#8221; was incorrectly taken to mean &#8220;${$}0&#8221; instead of &#8220;${$0}&#8221;. This bug is (mostly) fixed in Perl 5.004. </p>
<p> However, the developers of Perl 5.004 could not fix this bug completely, because at least two widely-used modules depend on the old meaning of &#8220;$$0&#8221; in a string. So Perl 5.004 still interprets &#8220;$$&lt;digit&gt;&#8221; in the old (broken) way inside strings; but it generates this message as a warning. And in Perl 5.005, this special treatment will cease.</p>
<h3>Fixed localization of $&lt;digit&gt;, $&amp;, etc.</h3>
<p> Perl versions before 5.004 did not always properly localize the regex-related special variables. Perl 5.004 does localize them, as the documentation has always said it should. This may result in <tt>$1</tt>, <tt>$2</tt>, etc. no longer being set where existing programs use them.</p>
<h3>No resetting of $. on implicit close</h3>
<p> The documentation for Perl 5.0 has always stated that <tt>$.</tt> is <i>not</i> reset when an already-open file handle is reopened with no intervening call to <tt>&quot;close&quot;</tt>. Due to a bug, perl versions 5.000 through 5.003 <i>did</i> reset <tt>$.</tt> under that circumstance; Perl 5.004 does not.</p>
<h3>wantarray may return undef</h3>
<p> The <tt>&quot;wantarray&quot;</tt> operator returns true if a subroutine is expected to return a list, and false otherwise. In Perl 5.004, <tt>&quot;wantarray&quot;</tt> can also return the undefined value if a subroutine&#8217;s return value will not be used at all, which allows subroutines to avoid a time-consuming calculation of a return value if it isn&#8217;t going to be used.</p>
<h3>eval EXPR determines value of <font SIZE="-1">EXPR</font> in scalar context</h3>
<p> Perl (version 5) used to determine the value of <font SIZE="-1">EXPR</font> inconsistently, sometimes incorrectly using the surrounding context for the determination. Now, the value of <font SIZE="-1">EXPR</font> (before being parsed by eval) is always determined in a scalar context. Once parsed, it is executed as before, by providing the context that the scope surrounding the eval provided. This change makes the behavior Perl4 compatible, besides fixing bugs resulting from the inconsistent behavior. This program: </p>
<p>@a = qw(time now is time);<br />
print eval @a;<br />
print &#8216;|&#8217;, scalar eval @a;</p>
<p> used to print something like &#8220;timenowis881399109|4&#8221;, but now (and in perl4) prints &#8220;4|4&#8221;.</p>
<h3>Changes to tainting checks</h3>
<p> A bug in previous versions may have failed to detect some insecure conditions when taint checks are turned on. (Taint checks are used in setuid or setgid scripts, or when explicitly turned on with the <tt>&quot;-T&quot;</tt> invocation option.) Although it&#8217;s unlikely, this may cause a previously-working script to now fail, which should be construed as a blessing since that indicates a potentially-serious security hole was just plugged. </p>
<p> The new restrictions when tainting include:</p>
<dl>
<dt>No <code>glob()</code> or &lt;*&gt;</p>
<dd> These operators may spawn the C shell (csh), which cannot be made safe. This restriction will be lifted in a future version of Perl when globbing is implemented without the use of an external program.</p>
<dt>No spawning if tainted $CDPATH, $ENV, $BASH_ENV</p>
<dd> These environment variables may alter the behavior of spawned programs (especially shells) in ways that subvert security. So now they are treated as dangerous, in the manner of <tt>$IFS</tt> and <tt>$PATH</tt>.</p>
<dt>No spawning if tainted $TERM doesn&#8217;t look like a terminal name</p>
<dd> Some termcap libraries do unsafe things with <tt>$TERM</tt>. However, it would be unnecessarily harsh to treat all <tt>$TERM</tt> values as unsafe, since only shell metacharacters can cause trouble in <tt>$TERM</tt>. So a tainted <tt>$TERM</tt> is considered to be safe if it contains only alphanumerics, underscores, dashes, and colons, and unsafe if it contains other characters (including whitespace).</dl>
<h3>New Opcode module and revised Safe module</h3>
<p> A new Opcode module supports the creation, manipulation and application of opcode masks. The revised Safe module has a new <font SIZE="-1">API</font> and is implemented using the new Opcode module. Please read the new Opcode and Safe documentation.</p>
<h3>Embedding improvements</h3>
<p> In older versions of Perl it was not possible to create more than one Perl interpreter instance inside a single process without leaking like a sieve and/or crashing. The bugs that caused this behavior have all been fixed. However, you still must take care when embedding Perl in a C program. See the updated perlembed manpage for tips on how to manage your interpreters.</p>
<h3>Internal change: FileHandle class based on IO::* classes</h3>
<p> File handles are now stored internally as type IO::Handle. The FileHandle module is still supported for backwards compatibility, but it is now merely a front end to the IO::* modules, specifically IO::Handle, IO::Seekable, and IO::File. We suggest, but do not require, that you use the IO::* modules in new code. </p>
<p> In harmony with this change, <tt>*GLOB{FILEHANDLE}</tt> is now just a backward-compatible synonym for <tt>*GLOB{IO}</tt>.</p>
<h3>Internal change: PerlIO abstraction interface</h3>
<p> It is now possible to build Perl with <font SIZE="-1">AT&amp;T</font>&#8216;s sfio <font SIZE="-1">IO</font> package instead of stdio. See perlapio for more details, and the <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to use it.</p>
<h3>New and changed syntax</h3>
<dl>
<dt>$coderef-&gt;(<font SIZE="-1">PARAMS</font>)</p>
<dd> A subroutine reference may now be suffixed with an arrow and a (possibly empty) parameter list. This syntax denotes a call of the referenced subroutine, with the given parameters (if any). </p>
<p> This new syntax follows the pattern of <tt>&quot;$hashref-&gt;{FOO}&quot;</tt> and <tt>&quot;$aryref-&gt;[$foo]&quot;</tt>: You may now write <tt>&quot;&amp;$subref($foo)&quot;</tt> as <tt>&quot;$subref-&gt;($foo)&quot;</tt>. All these arrow terms may be chained; thus, <tt>&quot;&amp;{$table-&gt;{FOO}}($bar)&quot;</tt> may now be written <tt>&quot;$table-&gt;{FOO}-&gt;($bar)&quot;</tt>.</dl>
<h3>New and changed builtin constants</h3>
<dl>
<dt>__PACKAGE__</p>
<dd> The current package name at compile time, or the undefined value if there is no current package (due to a <tt>&quot;package;&quot;</tt> directive). Like <tt>&quot;__FILE__&quot;</tt> and <tt>&quot;__LINE__&quot;</tt>, <tt>&quot;__PACKAGE__&quot;</tt> does <i>not</i> interpolate into strings.</dl>
<h3>New and changed builtin variables</h3>
<dl>
<dt>$^E</p>
<dd> Extended error message on some platforms. (Also known as <tt>$EXTENDED_OS_ERROR</tt> if you <tt>&quot;use English&quot;</tt>).</p>
<dt>$^H</p>
<dd> The current set of syntax checks enabled by <tt>&quot;use strict&quot;</tt>. See the documentation of <tt>&quot;strict&quot;</tt> for more details. Not actually new, but newly documented. Because it is intended for internal use by Perl core components, there is no <tt>&quot;use English&quot;</tt> long name for this variable.</p>
<dt>$^M</p>
<dd> By default, running out of memory it is not trappable. However, if compiled for this, Perl may use the contents of <tt>$^M</tt> as an emergency pool after <code>die()</code>ing with this message. Suppose that your Perl were compiled with -DPERL_EMERGENCY_SBRK and used Perl&#8217;s malloc. Then </p>
<pre>
    $^M = 'a' x (1&lt;&lt;16);
</pre>
<p> would allocate a 64K buffer for use when in emergency. See the <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for information on how to enable this option. As a disincentive to casual use of this advanced feature, there is no <tt>&quot;use English&quot;</tt> long name for this variable.</dl>
<h3>New and changed builtin functions</h3>
<dl>
<dt>delete on slices</p>
<dd> This now works. (e.g. <tt>&quot;delete @ENV{'PATH', 'MANPATH'}&quot;</tt>)</p>
<dt>flock</p>
<dd> is now supported on more platforms, prefers fcntl to lockf when emulating, and always flushes before (un)locking.</p>
<dt>printf and sprintf</p>
<dd> Perl now implements these functions itself; it doesn&#8217;t use the C library function <code>sprintf()</code> any more, except for floating-point numbers, and even then only known flags are allowed. As a result, it is now possible to know which conversions and flags will work, and what they will do. </p>
<p> The new conversions in Perl&#8217;s <code>sprintf()</code> are: </p>
<pre>
   %i   a synonym for %d
   %p   a pointer (the address of the Perl value, in hexadecimal)
   %n   special: *stores* the number of characters output so far
        into the next variable in the parameter list
</pre>
<p> The new flags that go between the <tt>&quot;%&quot;</tt> and the conversion are: </p>
<pre>
   #    prefix octal with &quot;0&quot;, hex with &quot;0x&quot;
   h    interpret integer as C type &quot;short&quot; or &quot;unsigned short&quot;
   V    interpret integer as Perl's standard integer type
</pre>
<p> Also, where a number would appear in the flags, an asterisk (&#8220;*&#8221;) may be used instead, in which case Perl uses the next item in the parameter list as the given number (that is, as the field width or precision). If a field width obtained through &#8220;*&#8221; is negative, it has the same effect as the &#8216;-&#8216; flag: left-justification. </p>
<p> See &#8220;sprintf&#8221; in perlfunc for a complete list of conversion and flags.</p>
<dt>keys as an lvalue</p>
<dd> As an lvalue, <tt>&quot;keys&quot;</tt> allows you to increase the number of hash buckets allocated for the given hash. This can gain you a measure of efficiency if you know the hash is going to get big. (This is similar to pre-extending an array by assigning a larger number to $#array.) If you say </p>
<pre>
    keys %hash = 200;
</pre>
<p> then <tt>%hash</tt> will have at least 200 buckets allocated for it. These buckets will be retained even if you do <tt>&quot;%hash = ()&quot;</tt>; use <tt>&quot;undef %hash&quot;</tt> if you want to free the storage while <tt>%hash</tt> is still in scope. You can&#8217;t shrink the number of buckets allocated for the hash using <tt>&quot;keys&quot;</tt> in this way (but you needn&#8217;t worry about doing this by accident, as trying has no effect).</p>
<dt><code>my()</code> in Control Structures</p>
<dd> You can now use <code>my()</code> (with or without the parentheses) in the control expressions of control structures such as: </p>
<p>while (defined(my $line = &lt;&gt;)) {<br />
    $line = lc $line;<br />
}<br />
continue<br />
{<br />
    print $line;<br />
}<br />
    if ((my $answer = &lt;STDIN&gt;) =~ /^y(es)?$/i) {<br />
        user_agrees();<br />
    } elsif ($answer =~ /^n(o)?$/i)<br />
    {<br />
        user_disagrees();<br />
    }<br />
    else<br />
    {<br />
        chomp $answer;<br />
        die &#8220;`$answer&#8217; is neither `yes&#8217; nor `no'&#8221;;<br />
    }</p>
<p> Also, you can declare a foreach loop control variable as lexical by preceding it with the word &#8220;my&#8221;. For example, in: </p>
<p>foreach<br />
    my $i(1, 2, 3)<br />
    {<br />
        some_function();<br />
    }</p>
<p> <tt>$i</tt> is a lexical variable, and the scope of <tt>$i</tt> extends to the end of the loop, but not beyond it. </p>
<p> Note that you still cannot use <code>my()</code> on global punctuation variables such as <tt>$_</tt> and the like.</p>
<dt><code>pack()</code> and <code>unpack()</code></p>
<dd> A new format &#8216;w&#8217; represents a <font SIZE="-1">BER</font> compressed integer (as defined in <font SIZE="-1">ASN.1</font>). Its format is a sequence of one or more bytes, each of which provides seven bits of the total value, with the most significant first. Bit eight of each byte is set, except for the last byte, in which bit eight is clear. </p>
<p> If &#8216;p&#8217; or &#8216;P&#8217; are given undef as values, they now generate a <font SIZE="-1">NULL</font> pointer. </p>
<p> Both <code>pack()</code> and <code>unpack()</code> now fail when their templates contain invalid types. (Invalid types used to be ignored.)</p>
<dt><code>sysseek()</code></p>
<dd> The new <code>sysseek()</code> operator is a variant of <code>seek()</code> that sets and gets the file&#8217;s system read/write position, using the <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2) system call. It is the only reliable way to seek before using <code>sysread()</code> or <code>syswrite()</code>. Its return value is the new position, or the undefined value on failure.</p>
<dt>use <font SIZE="-1">VERSION</font></p>
<dd> If the first argument to <tt>&quot;use&quot;</tt> is a number, it is treated as a version number instead of a module name. If the version of the Perl interpreter is less than <font SIZE="-1">VERSION,</font> then an error message is printed and Perl exits immediately. Because <tt>&quot;use&quot;</tt> occurs at compile time, this check happens immediately during the compilation process, unlike <tt>&quot;require VERSION&quot;</tt>, which waits until runtime for the check. This is often useful if you need to check the current Perl version before <tt>&quot;use&quot;</tt>ing library modules which have changed in incompatible ways from older versions of Perl. (We try not to do this more than we have to.)</p>
<dt>use Module <font SIZE="-1">VERSION LIST</font></p>
<dd> If the <font SIZE="-1">VERSION</font> argument is present between Module and <font SIZE="-1">LIST,</font> then the <tt>&quot;use&quot;</tt> will call the <font SIZE="-1">VERSION</font> method in class Module with the given version as an argument. The default <font SIZE="-1">VERSION</font> method, inherited from the <font SIZE="-1">UNIVERSAL</font> class, croaks if the given version is larger than the value of the variable <tt>$Module::VERSION</tt>. (Note that there is not a comma after <font SIZE="-1">VERSION</font>!) </p>
<p> This version-checking mechanism is similar to the one currently used in the Exporter module, but it is faster and can be used with modules that don&#8217;t use the Exporter. It is the recommended method for new code.</p>
<dt>prototype(<font SIZE="-1">FUNCTION</font>)</p>
<dd> Returns the prototype of a function as a string (or <tt>&quot;undef&quot;</tt> if the function has no prototype). <font SIZE="-1">FUNCTION</font> is a reference to or the name of the function whose prototype you want to retrieve. (Not actually new; just never documented before.)</p>
<dt>srand</p>
<dd> The default seed for <tt>&quot;srand&quot;</tt>, which used to be <tt>&quot;time&quot;</tt>, has been changed. Now it&#8217;s a heady mix of difficult-to-predict system-dependent values, which should be sufficient for most everyday purposes. </p>
<p> Previous to version 5.004, calling <tt>&quot;rand&quot;</tt> without first calling <tt>&quot;srand&quot;</tt> would yield the same sequence of random numbers on most or all machines. Now, when perl sees that you&#8217;re calling <tt>&quot;rand&quot;</tt> and haven&#8217;t yet called <tt>&quot;srand&quot;</tt>, it calls <tt>&quot;srand&quot;</tt> with the default seed. You should still call <tt>&quot;srand&quot;</tt> manually if your code might ever be run on a pre-5.004 system, of course, or if you want a seed other than the default.</p>
<dt>$_ as Default</p>
<dd> Functions documented in the Camel to default to <tt>$_</tt> now in fact do, and all those that do are so documented in perlfunc.</p>
<dt>&quot;m//gc&quot; does not reset search position on failure</p>
<dd> The <tt>&quot;m//g&quot;</tt> match iteration construct has always reset its target string&#8217;s search position (which is visible through the <tt>&quot;pos&quot;</tt> operator) when a match fails; as a result, the next <tt>&quot;m//g&quot;</tt> match after a failure starts again at the beginning of the string. With Perl 5.004, this reset may be disabled by adding the &#8220;c&#8221; (for &#8220;continue&#8221;) modifier, i.e. <tt>&quot;m//gc&quot;</tt>. This feature, in conjunction with the <tt>&quot;\G&quot;</tt> zero-width assertion, makes it possible to chain matches together. See perlop and perlre.</p>
<dt>&quot;m//x&quot; ignores whitespace before ?*+{}</p>
<dd> The <tt>&quot;m//x&quot;</tt> construct has always been intended to ignore all unescaped whitespace. However, before Perl 5.004, whitespace had the effect of escaping repeat modifiers like &#8220;*&#8221; or &#8220;?&#8221;; for example, <tt>&quot;/a *b/x&quot;</tt> was (mis)interpreted as <tt>&quot;/a\*b/x&quot;</tt>. This bug has been fixed in 5.004.</p>
<dt>nested &quot;sub{}&quot; closures work now</p>
<dd> Prior to the 5.004 release, nested anonymous functions didn&#8217;t work right. They do now.</p>
<dt>formats work right on changing lexicals</p>
<dd> Just like anonymous functions that contain lexical variables that change (like a lexical index variable for a <tt>&quot;foreach&quot;</tt> loop), formats now work properly. For example, this silently failed before (printed only zeros), but is fine now: </p>
<p>my $i;<br />
foreach<br />
    $i(1..10)<br />
    {<br />
        write;<br />
    }<br />
format =<br />
    my i is @ #$i<br />
        .</p>
<p> However, it still fails (without a warning) if the foreach is within a subroutine: </p>
<p>my $i;<br />
sub foo<br />
{<br />
    foreach<br />
        $i(1..10)<br />
        {<br />
            write;<br />
        }<br />
}<br />
foo;<br />
format =<br />
    my i is @ #$i<br />
        .
</dl>
<h3>New builtin methods</h3>
<p> The <tt>&quot;UNIVERSAL&quot;</tt> package automatically contains the following methods that are inherited by all other classes:</p>
<dl>
<dt>isa(<font SIZE="-1">CLASS</font>)</p>
<dd> <tt>&quot;isa&quot;</tt> returns <i>true</i> if its object is blessed into a subclass of <tt>&quot;CLASS&quot;</tt> </p>
<p> <tt>&quot;isa&quot;</tt> is also exportable and can be called as a sub with two arguments. This allows the ability to check what a reference points to. Example: </p>
<p>use UNIVERSAL qw(isa);<br />
if (isa($ref, &#8216;ARRAY&#8217;)) {<br />
    &#8230;<br />
}</p>
<dt>can(<font SIZE="-1">METHOD</font>)</p>
<dd> <tt>&quot;can&quot;</tt> checks to see if its object has a method called <tt>&quot;METHOD&quot;</tt>, if it does then a reference to the sub is returned; if it does not then <i>undef</i> is returned.</p>
<dt><font SIZE="-1">VERSION</font>( [<font SIZE="-1">NEED</font>] )</p>
<dd> <tt>&quot;VERSION&quot;</tt> returns the version number of the class (package). If the <font SIZE="-1">NEED</font> argument is given then it will check that the current version (as defined by the <tt>$VERSION</tt> variable in the given package) not less than <font SIZE="-1">NEED</font>; it will die if this is not the case. This method is normally called as a class method. This method is called automatically by the <tt>&quot;VERSION&quot;</tt> form of <tt>&quot;use&quot;</tt>. </p>
<p>use A 1.2 qw(some imported subs);<br />
#implies:<br />
A-&gt;VERSION(1.2);
</dl>
<p> <font SIZE="-1"><code>NOTE:</code></font> <tt>&quot;can&quot;</tt> directly uses Perl&#8217;s internal code for method lookup, and <tt>&quot;isa&quot;</tt> uses a very similar method and caching strategy. This may cause strange effects if the Perl code dynamically changes <tt>@ISA</tt> in any package. </p>
<p> You may add other methods to the <font SIZE="-1">UNIVERSAL</font> class via Perl or <font SIZE="-1">XS</font> code. You do not need to <tt>&quot;use UNIVERSAL&quot;</tt> in order to make these methods available to your program. This is necessary only if you wish to have <tt>&quot;isa&quot;</tt> available as a plain subroutine in the current package.</p>
<h3><font SIZE="-1">TIEHANDLE</font> now supported</h3>
<p> See perltie for other kinds of <code>tie()</code>s.</p>
<dl>
<dt><font SIZE="-1">TIEHANDLE</font> classname, <font SIZE="-1">LIST</font></p>
<dd> This is the constructor for the class. That means it is expected to return an object of some sort. The reference can be used to hold some internal information. </p>
<p>sub TIEHANDLE<br />
{<br />
    print &#8220;&lt;shout&gt;
&#8221;;<br />
    my $i;<br />
    return bless \$i, shift;<br />
}</p>
<dt><font SIZE="-1">PRINT</font> this, <font SIZE="-1">LIST</font></p>
<dd> This method will be triggered every time the tied handle is printed to. Beyond its self reference it also expects the list that was passed to the print function. </p>
<p>sub PRINT<br />
{<br />
    $r = shift;<br />
    $$r++;<br />
    return print join(<br />
               $, = &gt; map { uc } @_),<br />
           $\;<br />
}</p>
<dt><font SIZE="-1">PRINTF</font> this, <font SIZE="-1">LIST</font></p>
<dd> This method will be triggered every time the tied handle is printed to with the <tt>&quot;printf()&quot;</tt> function. Beyond its self reference it also expects the format and list that was passed to the printf function. </p>
<p>sub PRINTF<br />
{<br />
    shift;<br />
    my $fmt = shift;<br />
    print sprintf($fmt, @_).&#8221;
&#8221;;<br />
}</p>
<dt><font SIZE="-1">READ</font> this <font SIZE="-1">LIST</font></p>
<dd> This method will be called when the handle is read from via the <tt>&quot;read&quot;</tt> or <tt>&quot;sysread&quot;</tt> functions. </p>
<p>sub READ<br />
{<br />
    $r = shift;<br />
    my($buf, $len, $offset) = @_;<br />
    print &#8220;READ called, \$buf=$buf, \$len=$len, \$offset=$offset&#8221;;<br />
}</p>
<dt><font SIZE="-1">READLINE</font> this</p>
<dd> This method will be called when the handle is read from. The method should return undef when there is no more data. </p>
<p>sub READLINE<br />
{<br />
    $r = shift;<br />
    return &#8220;PRINT called $$r times
&#8221;<br />
}</p>
<dt><font SIZE="-1">GETC</font> this</p>
<dd> This method will be called when the <tt>&quot;getc&quot;</tt> function is called. </p>
<p>sub GETC<br />
{<br />
    print &#8220;Don&#8217;t GETC, Get Perl&#8221;;<br />
    return &#8220;a&#8221;;<br />
}</p>
<dt><font SIZE="-1">DESTROY</font> this</p>
<dd> As with the other types of ties, this method will be called when the tied handle is about to be destroyed. This is useful for debugging and possibly for cleaning up. </p>
<pre>
    sub DESTROY {
        print &quot;&lt;/shout&gt;
&quot;;
    }
</pre>
</dl>
<h3>Malloc enhancements</h3>
<p> If perl is compiled with the malloc included with the perl distribution (that is, if <tt>&quot;perl -V:d_mymalloc&quot;</tt> is &#8216;define&#8217;) then you can print memory statistics at runtime by running Perl thusly: </p>
<pre>
  env PERL_DEBUG_MSTATS=2 perl your_script_here
</pre>
<p> The value of 2 means to print statistics after compilation and on exit; with a value of 1, the statistics are printed only on exit. (If you want the statistics at an arbitrary time, you&#8217;ll need to install the optional module Devel::Peek.) </p>
<p> Three new compilation flags are recognized by malloc.c. (They have no effect if perl is compiled with system <code>malloc()</code>.)</p>
<dl>
<dt>-DPERL_EMERGENCY_SBRK</p>
<dd> If this macro is defined, running out of memory need not be a fatal error: a memory pool can allocated by assigning to the special variable <tt>$^M</tt>. See &#8220;$^M&#8221;.</p>
<dt>-DPACK_MALLOC</p>
<dd> Perl memory allocation is by bucket with sizes close to powers of two. Because of these malloc overhead may be big, especially for data of size exactly a power of two. If <tt>&quot;PACK_MALLOC&quot;</tt> is defined, perl uses a slightly different algorithm for small allocations (up to 64 bytes long), which makes it possible to have overhead down to 1 byte for allocations which are powers of two (and appear quite often). </p>
<p> Expected memory savings (with 8-byte alignment in <tt>&quot;alignbytes&quot;</tt>) is about 20% for typical Perl usage. Expected slowdown due to additional malloc overhead is in fractions of a percent (hard to measure, because of the effect of saved memory on speed).</p>
<dt>-DTWO_POT_OPTIMIZE</p>
<dd> Similarly to <tt>&quot;PACK_MALLOC&quot;</tt>, this macro improves allocations of data with size close to a power of two; but this works for big allocations (starting with 16K by default). Such allocations are typical for big hashes and special-purpose scripts, especially image processing. </p>
<p> On recent systems, the fact that perl requires 2M from system for 1M allocation will not affect speed of execution, since the tail of such a chunk is not going to be touched (and thus will not require real memory). However, it may result in a premature out-of-memory error. So if you will be manipulating very large blocks with sizes close to powers of two, it would be wise to define this macro. </p>
<p> Expected saving of memory is 0-100% (100% in applications which require most memory in such 2**n chunks); expected slowdown is negligible.</dl>
<h3>Miscellaneous efficiency enhancements</h3>
<p> Functions that have an empty prototype and that do nothing but return a fixed value are now inlined (e.g. <tt>&quot;sub PI () { 3.14159 }&quot;</tt>). </p>
<p> Each unique hash key is only allocated once, no matter how many hashes have an entry with that key. So even if you have 100 copies of the same hash, the hash keys never have to be reallocated.</p>
<h2>Support for More Operating Systems</h2>
<p> Support for the following operating systems is new in Perl 5.004.</p>
<h3>Win32</h3>
<p> Perl 5.004 now includes support for building a &#8220;native&#8221; perl under Windows <font SIZE="-1">NT,</font> using the Microsoft Visual C<font SIZE="-2">++</font> compiler (versions 2.0 and above) or the Borland C<font SIZE="-2">++</font> compiler (versions 5.02 and above). The resulting perl can be used under Windows 95 (if it is installed in the same directory locations as it got installed in Windows <font SIZE="-1">NT</font>). This port includes support for perl extension building tools like ExtUtils::MakeMaker and h2xs, so that many extensions available on the Comprehensive Perl Archive Network (<font SIZE="-1">CPAN</font>) can now be readily built under Windows <font SIZE="-1">NT.</font> See <a rel="nofollow" href="http://www.perl.com/">http://www.perl.com/</a> for more information on <font SIZE="-1">CPAN</font> and <i></i><font SIZE="-1"><i>README</i></font><i>.win32</i> in the perl distribution for more details on how to get started with building this port. </p>
<p> There is also support for building perl under the Cygwin32 environment. Cygwin32 is a set of <font SIZE="-1">GNU</font> tools that make it possible to compile and run many Unix programs under Windows <font SIZE="-1">NT</font> by providing a mostly Unix-like interface for compilation and execution. See <i></i><font SIZE="-1"><i>README</i></font><i>.cygwin32</i> in the perl distribution for more details on this port and how to obtain the Cygwin32 toolkit.</p>
<h3>Plan 9</h3>
<p> See <i></i><font SIZE="-1"><i>README</i></font><i>.plan9</i> in the perl distribution.</p>
<h3><font SIZE="-1">QNX</font></h3>
<p> See <i></i><font SIZE="-1"><i>README</i></font><i>.qnx</i> in the perl distribution.</p>
<h3>AmigaOS</h3>
<p> See <i></i><font SIZE="-1"><i>README</i></font><i>.amigaos</i> in the perl distribution.</p>
<h2>Pragmata</h2>
<p> Six new pragmatic modules exist:</p>
<dl>
<dt>use autouse <font SIZE="-1">MODULE</font> =&gt; qw(sub1 sub2 sub3)</p>
<dd> Defers <tt>&quot;require MODULE&quot;</tt> until someone calls one of the specified subroutines (which must be exported by <font SIZE="-1">MODULE</font>). This pragma should be used with caution, and only when necessary.</p>
<dt>use blib</p>
<dd>
<dt>use blib &#8216;dir&#8217;</p>
<dd> Looks for MakeMaker-like <i>&#8216;blib&#8217;</i> directory structure starting in <i>dir</i> (or current directory) and working back up to five levels of parent directories. </p>
<p> Intended for use on command line with <code>-M</code> option as a way of testing arbitrary scripts against an uninstalled version of a package.</p>
<dt>use constant <font SIZE="-1">NAME</font> =&gt; <font SIZE="-1">VALUE</font></p>
<dd> Provides a convenient interface for creating compile-time constants, See &#8220;Constant Functions&#8221; in perlsub.</p>
<dt>use locale</p>
<dd> Tells the compiler to enable (or disable) the use of <font SIZE="-1">POSIX</font> locales for builtin operations. </p>
<p> When <tt>&quot;use locale&quot;</tt> is in effect, the current <font SIZE="-1">LC_CTYPE</font> locale is used for regular expressions and case mapping; <font SIZE="-1">LC_COLLATE</font> for string ordering; and <font SIZE="-1">LC_NUMERIC</font> for numeric formatting in printf and sprintf (but <code>not</code> in print). <font SIZE="-1">LC_NUMERIC</font> is always used in write, since lexical scoping of formats is problematic at best. </p>
<p> Each <tt>&quot;use locale&quot;</tt> or <tt>&quot;no locale&quot;</tt> affects statements to the end of the enclosing <font SIZE="-1">BLOCK</font> or, if not inside a <font SIZE="-1">BLOCK,</font> to the end of the current file. Locales can be switched and queried with <code>POSIX::setlocale()</code>. </p>
<p> See perllocale for more information.</p>
<dt>use ops</p>
<dd> Disable unsafe opcodes, or any named opcodes, when compiling Perl code.</p>
<dt>use vmsish</p>
<dd> Enable VMS-specific language features. Currently, there are three VMS-specific features available: &#8216;status&#8217;, which makes <tt>$?</tt> and <tt>&quot;system&quot;</tt> return genuine <font SIZE="-1">VMS</font> status values instead of emulating <font SIZE="-1">POSIX</font>; &#8216;exit&#8217;, which makes <tt>&quot;exit&quot;</tt> take a genuine <font SIZE="-1">VMS</font> status value instead of assuming that <tt>&quot;exit 1&quot;</tt> is an error; and &#8216;time&#8217;, which makes all times relative to the local time zone, in the <font SIZE="-1">VMS</font> tradition.</dl>
<h2>Modules</h2>
<h3>Required Updates</h3>
<p> Though Perl 5.004 is compatible with almost all modules that work with Perl 5.003, there are a few exceptions: </p>
<p>    Module   Required Version for Perl 5.004<br />
    &#8212;&#8212;   &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-<br />
    Filter   Filter-1.12<br />
    LWP      libwww-perl-5.08<br />
    Tk       Tk400.202 (-w makes noise)</p>
<p> Also, the majordomo mailing list program, version 1.94.1, doesn&#8217;t work with Perl 5.004 (nor with perl 4), because it executes an invalid regular expression. This bug is fixed in majordomo version 1.94.2.</p>
<h3>Installation directories</h3>
<p> The <i>installperl</i> script now places the Perl source files for extensions in the architecture-specific library directory, which is where the shared libraries for extensions have always been. This change is intended to allow administrators to keep the Perl 5.004 library directory unchanged from a previous version, without running the risk of binary incompatibility between extensions&#8217; Perl source and shared libraries.</p>
<h3>Module information summary</h3>
<p> Brand new modules, arranged by topic rather than strictly alphabetically: </p>
<p>    CGI.pm               Web server interface (&#8220;Common Gateway Interface&#8221;)<br />
    CGI/Apache.pm        Support for Apache&#8217;s Perl module<br />
    CGI/Carp.pm          Log server errors with helpful context<br />
    CGI/Fast.pm          Support for FastCGI (persistent server process)<br />
    CGI/Push.pm          Support for server push<br />
    CGI/Switch.pm        Simple interface for multiple server types<br />
    CPAN                 Interface to Comprehensive Perl Archive Network<br />
    CPAN::FirstTime      Utility for creating CPAN configuration file<br />
    CPAN::Nox            Runs CPAN while avoiding compiled extensions<br />
    IO.pm                Top-level interface to IO::* classes<br />
    IO/File.pm           IO::File extension Perl module<br />
    IO/Handle.pm         IO::Handle extension Perl module<br />
    IO/Pipe.pm           IO::Pipe extension Perl module<br />
    IO/Seekable.pm       IO::Seekable extension Perl module<br />
    IO/Select.pm         IO::Select extension Perl module<br />
    IO/Socket.pm         IO::Socket extension Perl module<br />
    Opcode.pm            Disable named opcodes when compiling Perl code<br />
    ExtUtils/Embed.pm    Utilities for embedding Perl in C programs<br />
    ExtUtils/testlib.pm  Fixes up @INC to use just-built extension<br />
    FindBin.pm           Find path of currently executing program<br />
    Class/Struct.pm      Declare struct-like datatypes as Perl classes<br />
    File/stat.pm         By-name interface to Perl&#8217;s builtin stat<br />
    Net/hostent.pm       By-name interface to Perl&#8217;s builtin gethost*<br />
    Net/netent.pm        By-name interface to Perl&#8217;s builtin getnet*<br />
    Net/protoent.pm      By-name interface to Perl&#8217;s builtin getproto*<br />
    Net/servent.pm       By-name interface to Perl&#8217;s builtin getserv*<br />
    Time/gmtime.pm       By-name interface to Perl&#8217;s builtin gmtime<br />
    Time/localtime.pm    By-name interface to Perl&#8217;s builtin localtime<br />
    Time/tm.pm           Internal object for Time::{gm,local}time<br />
    User/grent.pm        By-name interface to Perl&#8217;s builtin getgr*<br />
    User/pwent.pm        By-name interface to Perl&#8217;s builtin getpw*<br />
    Tie/RefHash.pm       Base class for tied hashes with references as keys<br />
    UNIVERSAL.pm         Base class for *ALL* classes</p>
<h3>Fcntl</h3>
<p> New constants in the existing Fcntl modules are now supported, provided that your operating system happens to support them: </p>
<pre>
    F_GETOWN F_SETOWN
    O_ASYNC O_DEFER O_DSYNC O_FSYNC O_SYNC
    O_EXLOCK O_SHLOCK
</pre>
<p> These constants are intended for use with the Perl operators <code>sysopen()</code> and <code>fcntl()</code> and the basic database modules like SDBM_File. For the exact meaning of these and other Fcntl constants please refer to your operating system&#8217;s documentation for <code>fcntl()</code> and <code>open()</code>. </p>
<p> In addition, the Fcntl module now provides these constants for use with the Perl operator <code>flock()</code>: </p>
<pre>
        LOCK_SH LOCK_EX LOCK_NB LOCK_UN
</pre>
<p> These constants are defined in all environments (because where there is no <code>flock()</code> system call, Perl emulates it). However, for historical reasons, these constants are not exported unless they are explicitly requested with the &#8220;:flock&#8221; tag (e.g. <tt>&quot;use Fcntl ':flock'&quot;</tt>).</p>
<h3><font SIZE="-1">IO</font></h3>
<p> The <font SIZE="-1">IO</font> module provides a simple mechanism to load all the <font SIZE="-1">IO</font> modules at one go. Currently this includes: </p>
<pre>
     IO::Handle
     IO::Seekable
     IO::File
     IO::Pipe
     IO::Socket
</pre>
<p> For more information on any of these modules, please see its respective documentation.</p>
<h3>Math::Complex</h3>
<p> The Math::Complex module has been totally rewritten, and now supports more operations. These are overloaded: </p>
<pre>
     + - * / ** &lt;=&gt; neg ~ abs sqrt exp log sin cos atan2 &quot;&quot; (stringify)
</pre>
<p> And these functions are now exported: </p>
<pre>
    pi i Re Im arg
    log10 logn ln cbrt root
    tan
    csc sec cot
    asin acos atan
    acsc asec acot
    sinh cosh tanh
    csch sech coth
    asinh acosh atanh
    acsch asech acoth
    cplx cplxe
</pre>
<h3>Math::Trig</h3>
<p> This new module provides a simpler interface to parts of Math::Complex for those who need trigonometric functions only for real numbers.</p>
<h3>DB_File</h3>
<p> There have been quite a few changes made to DB_File. Here are a few of the highlights:</p>
<dl>
<dt>&bull;</p>
<dd> Fixed a handful of bugs.</p>
<dt>&bull;</p>
<dd> By public demand, added support for the standard hash function <code>exists()</code>.</p>
<dt>&bull;</p>
<dd> Made it compatible with Berkeley <font SIZE="-1">DB 1.86.</font></p>
<dt>&bull;</p>
<dd> Made negative subscripts work with <font SIZE="-1">RECNO</font> interface.</p>
<dt>&bull;</p>
<dd> Changed the default flags from O_RDWR to O_CREAT|O_RDWR and the default mode from 0640 to 0666.</p>
<dt>&bull;</p>
<dd> Made DB_File automatically import the <code>open()</code> constants (O_RDWR, O_CREAT etc.) from Fcntl, if available.</p>
<dt>&bull;</p>
<dd> Updated documentation.</dl>
<p> Refer to the <font SIZE="-1">HISTORY</font> section in DB_File.pm for a complete list of changes. Everything after DB_File 1.01 has been added since 5.003.</p>
<h3>Net::Ping</h3>
<p> Major rewrite &#8211; support added for both udp echo and real icmp pings.</p>
<h3>Object-oriented overrides for builtin operators</h3>
<p> Many of the Perl builtins returning lists now have object-oriented overrides. These are: </p>
<pre>
    File::stat
    Net::hostent
    Net::netent
    Net::protoent
    Net::servent
    Time::gmtime
    Time::localtime
    User::grent
    User::pwent
</pre>
<p> For example, you can now say </p>
<p>use File::stat;<br />
use User::pwent;<br />
$his = (stat($filename)-&gt;st_uid == pwent($whoever)-&gt;pw_uid);</p>
<h2>Utility Changes</h2>
<h3>pod2html</h3>
<dl>
<dt>Sends converted <font SIZE="-1">HTML</font> to standard output</p>
<dd> The <i>pod2html</i> utility included with Perl 5.004 is entirely new. By default, it sends the converted <font SIZE="-1">HTML</font> to its standard output, instead of writing it to a file like Perl 5.003&#8217;s <i>pod2html</i> did. Use the <code>&#8211;outfile=FILENAME</code> option to write to a file.</dl>
<h3>xsubpp</h3>
<dl>
<dt>&quot;void&quot; XSUBs now default to returning nothing</p>
<dd> Due to a documentation/implementation bug in previous versions of Perl, XSUBs with a return type of <tt>&quot;void&quot;</tt> have actually been returning one value. Usually that value was the <font SIZE="-1">GV</font> for the <font SIZE="-1">XSUB,</font> but sometimes it was some already freed or reused value, which would sometimes lead to program failure. </p>
<p> In Perl 5.004, if an <font SIZE="-1">XSUB</font> is declared as returning <tt>&quot;void&quot;</tt>, it actually returns no value, i.e. an empty list (though there is a backward-compatibility exception; see below). If your <font SIZE="-1">XSUB</font> really does return an <font SIZE="-1">SV,</font> you should give it a return type of <tt>&quot;SV *&quot;</tt>. </p>
<p> For backward compatibility, <i>xsubpp</i> tries to guess whether a <tt>&quot;void&quot;</tt> <font SIZE="-1">XSUB</font> is really <tt>&quot;void&quot;</tt> or if it wants to return an <tt>&quot;SV *&quot;</tt>. It does so by examining the text of the <font SIZE="-1">XSUB:</font> if <i>xsubpp</i> finds what looks like an assignment to <tt>ST(0)</tt>, it assumes that the <font SIZE="-1">XSUB</font>&#8216;s return type is really <tt>&quot;SV *&quot;</tt>.</dl>
<h2>C Language API Changes</h2>
<dl>
<dt>&quot;gv_fetchmethod&quot; and &quot;perl_call_sv&quot;</p>
<dd> The <tt>&quot;gv_fetchmethod&quot;</tt> function finds a method for an object, just like in Perl 5.003. The <font SIZE="-1">GV</font> it returns may be a method cache entry. However, in Perl 5.004, method cache entries are not visible to users; therefore, they can no longer be passed directly to <tt>&quot;perl_call_sv&quot;</tt>. Instead, you should use the <tt>&quot;GvCV&quot;</tt> macro on the <font SIZE="-1">GV</font> to extract its <font SIZE="-1">CV,</font> and pass the <font SIZE="-1">CV</font> to <tt>&quot;perl_call_sv&quot;</tt>. </p>
<p> The most likely symptom of passing the result of <tt>&quot;gv_fetchmethod&quot;</tt> to <tt>&quot;perl_call_sv&quot;</tt> is Perl&#8217;s producing an &#8220;Undefined subroutine called&#8221; error on the <i>second</i> call to a given method (since there is no cache on the first call).</p>
<dt>&quot;perl_eval_pv&quot;</p>
<dd> A new function handy for eval&#8217;ing strings of Perl code inside C code. This function returns the value from the eval statement, which can be used instead of fetching globals from the symbol table. See perlguts, perlembed and perlcall for details and examples.</p>
<dt>Extended <font SIZE="-1">API</font> for manipulating hashes</p>
<dd> Internal handling of hash keys has changed. The old hashtable <font SIZE="-1">API</font> is still fully supported, and will likely remain so. The additions to the <font SIZE="-1">API</font> allow passing keys as <tt>&quot;SV*&quot;</tt>s, so that <tt>&quot;tied&quot;</tt> hashes can be given real scalars as keys rather than plain strings (nontied hashes still can only use strings as keys). New extensions must use the new hash access functions and macros if they wish to use <tt>&quot;SV*&quot;</tt> keys. These additions also make it feasible to manipulate <tt>&quot;HE*&quot;</tt>s (hash entries), which can be more efficient. See perlguts for details.</dl>
<h2>Documentation Changes</h2>
<p> Many of the base and library pods were updated. These new pods are included in section 1:</p>
<dl>
<dt>perldelta</p>
<dd> This document.</p>
<dt>perlfaq</p>
<dd> Frequently asked questions.</p>
<dt>perllocale</p>
<dd> Locale support (internationalization and localization).</p>
<dt>perltoot</p>
<dd> Tutorial on Perl <font SIZE="-1">OO</font> programming.</p>
<dt>perlapio</p>
<dd> Perl internal <font SIZE="-1">IO</font> abstraction interface.</p>
<dt>perlmodlib</p>
<dd> Perl module library and recommended practice for module creation. Extracted from perlmod (which is much smaller as a result).</p>
<dt>perldebug</p>
<dd> Although not new, this has been massively updated.</p>
<dt>perlsec</p>
<dd> Although not new, this has been massively updated.</dl>
<h2>New Diagnostics</h2>
<p> Several new conditions will trigger warnings that were silent before. Some only affect certain platforms. The following new warnings and errors outline these. These messages are classified as follows (listed in increasing order of desperation): </p>
<pre>
   (W) A warning (optional).
   (D) A deprecation (optional).
   (S) A severe warning (mandatory).
   (F) A fatal error (trappable).
   (P) An internal error you should never see (trappable).
   (X) A very fatal error (nontrappable).
   (A) An alien error message (not generated by Perl).
</pre>
<dl>
<dt>&quot;my&quot; variable %s masks earlier declaration in same scope</p>
<dd> (W) A lexical variable has been redeclared in the same scope, effectively eliminating all access to the previous instance. This is almost always a typographical error. Note that the earlier variable will still exist until the end of the scope or until all closure referents to it are destroyed.</p>
<dt>%s argument is not a <font SIZE="-1">HASH</font> element or slice</p>
<dd> (F) The argument to <code>delete()</code> must be either a hash element, such as </p>
<p>$foo{$bar} $ref-&gt;[12] -&gt; { &#8220;susie&#8221; }</p>
<p> or a hash slice, such as </p>
<p>@foo<br />
{<br />
    $bar, $baz, $xyzzy<br />
}<br />
@{$ref-&gt;[12]}<br />
{<br />
    &#8220;susie&#8221;, &#8220;queue&#8221;<br />
}</p>
<dt>Allocation too large: %lx</p>
<dd> (X) You can&#8217;t allocate more than 64K on an MS-DOS machine.</p>
<dt>Allocation too large</p>
<dd> (F) You can&#8217;t allocate more than 2^31+&#8220;small amount&#8221; bytes.</p>
<dt>Applying %s to %s will act on scalar(%s)</p>
<dd> (W) The pattern match (//), substitution (s///), and transliteration (tr///) operators work on scalar values. If you apply one of them to an array or a hash, it will convert the array or hash to a scalar value (the length of an array or the population info of a hash) and then work on that scalar value. This is probably not what you meant to do. See &#8220;grep&#8221; in perlfunc and &#8220;map&#8221; in perlfunc for alternatives.</p>
<dt>Attempt to free nonexistent shared string</p>
<dd> (P) Perl maintains a reference counted internal table of strings to optimize the storage and access of hash keys and other strings. This indicates someone tried to decrement the reference count of a string that can no longer be found in the table.</p>
<dt>Attempt to use reference as lvalue in substr</p>
<dd> (W) You supplied a reference as the first argument to <code>substr()</code> used as an lvalue, which is pretty strange. Perhaps you forgot to dereference it first. See &#8220;substr&#8221; in perlfunc.</p>
<dt>Bareword &quot;%s&quot; refers to nonexistent package</p>
<dd> (W) You used a qualified bareword of the form <tt>&quot;Foo::&quot;</tt>, but the compiler saw no other uses of that namespace before that point. Perhaps you need to predeclare a package?</p>
<dt>Can&#8217;t redefine active sort subroutine %s</p>
<dd> (F) Perl optimizes the internal handling of sort subroutines and keeps pointers into them. You tried to redefine one such sort subroutine when it was currently active, which is not allowed. If you really want to do this, you should write <tt>&quot;sort { &amp;func } @x&quot;</tt> instead of <tt>&quot;sort func @x&quot;</tt>.</p>
<dt>Can&#8217;t use bareword (&quot;%s&quot;) as %s ref while &quot;strict refs&quot; in use</p>
<dd> (F) Only hard references are allowed by &#8220;strict refs&#8221;. Symbolic references are disallowed. See perlref.</p>
<dt>Cannot resolve method `%s&#8217; overloading `%s&#8217; in package `%s&#8217;</p>
<dd> (P) Internal error trying to resolve overloading specified by a method name (as opposed to a subroutine reference).</p>
<dt>Constant subroutine %s redefined</p>
<dd> (S) You redefined a subroutine which had previously been eligible for inlining. See &#8220;Constant Functions&#8221; in perlsub for commentary and workarounds.</p>
<dt>Constant subroutine %s undefined</p>
<dd> (S) You undefined a subroutine which had previously been eligible for inlining. See &#8220;Constant Functions&#8221; in perlsub for commentary and workarounds.</p>
<dt>Copy method did not return a reference</p>
<dd> (F) The method which overloads &#8220;=&#8221; is buggy. See &#8220;Copy Constructor&#8221; in overload.</p>
<dt>Died</p>
<dd> (F) You passed <code>die()</code> an empty string (the equivalent of <tt>&quot;die &quot;&quot;&quot;</tt>) or you called it with no args and both <tt>$@</tt> and <tt>$_</tt> were empty.</p>
<dt>Exiting pseudo-block via %s</p>
<dd> (W) You are exiting a rather special block construct (like a sort block or subroutine) by unconventional means, such as a goto, or a loop control statement. See &#8220;sort&#8221; in perlfunc.</p>
<dt>Identifier too long</p>
<dd> (F) Perl limits identifiers (names for variables, functions, etc.) to 252 characters for simple names, somewhat more for compound names (like <tt>$A::B</tt>). You&#8217;ve exceeded Perl&#8217;s limits. Future versions of Perl are likely to eliminate these arbitrary limitations.</p>
<dt>Illegal character %s (carriage return)</p>
<dd> (F) A carriage return character was found in the input. This is an error, and not a warning, because carriage return characters can break multi-line strings, including here documents (e.g., <tt>&quot;print &lt;&lt;EOF;&quot;</tt>).</p>
<dt>Illegal switch in <font SIZE="-1">PERL5OPT:</font> %s</p>
<dd> (X) The <font SIZE="-1">PERL5OPT</font> environment variable may only be used to set the following switches: <code>-[DIMUdmw]</code>.</p>
<dt>Integer overflow in hex number</p>
<dd> (S) The literal hex number you have specified is too big for your architecture. On a 32-bit architecture the largest hex literal is 0xFFFFFFFF.</p>
<dt>Integer overflow in octal number</p>
<dd> (S) The literal octal number you have specified is too big for your architecture. On a 32-bit architecture the largest octal literal is 037777777777.</p>
<dt>internal error: glob failed</p>
<dd> (P) Something went wrong with the external program(s) used for <tt>&quot;glob&quot;</tt> and <tt>&quot;&lt;*.c&gt;&quot;</tt>. This may mean that your csh (C shell) is broken. If so, you should change all of the csh-related variables in config.sh: If you have tcsh, make the variables refer to it as if it were csh (e.g. <tt>&quot;full_csh='/usr/bin/tcsh'&quot;</tt>); otherwise, make them all empty (except that <tt>&quot;d_csh&quot;</tt> should be <tt>'undef'</tt>) so that Perl will think csh is missing. In either case, after editing config.sh, run <tt>&quot;./Configure -S&quot;</tt> and rebuild Perl.</p>
<dt>Invalid conversion in %s: &quot;%s&quot;</p>
<dd> (W) Perl does not understand the given format conversion. See &#8220;sprintf&#8221; in perlfunc.</p>
<dt>Invalid type in pack: &#8216;%s&#8217;</p>
<dd> (F) The given character is not a valid pack type. See &#8220;pack&#8221; in perlfunc.</p>
<dt>Invalid type in unpack: &#8216;%s&#8217;</p>
<dd> (F) The given character is not a valid unpack type. See &#8220;unpack&#8221; in perlfunc.</p>
<dt>Name &quot;%s::%s&quot; used only once: possible typo</p>
<dd> (W) Typographical errors often show up as unique variable names. If you had a good reason for having a unique name, then just mention it again somehow to suppress the message (the <tt>&quot;use vars&quot;</tt> pragma is provided for just this purpose).</p>
<dt>Null picture in formline</p>
<dd> (F) The first argument to formline must be a valid format picture specification. It was found to be empty, which probably means you supplied it an uninitialized value. See perlform.</p>
<dt>Offset outside string</p>
<dd> (F) You tried to do a read/write/send/recv operation with an offset pointing outside the buffer. This is difficult to imagine. The sole exception to this is that <tt>&quot;sysread()&quot;</tt>ing past the buffer will extend the buffer and zero pad the new area.</p>
<dt>Out of memory!</p>
<dd> (X|F) The <code>malloc()</code> function returned 0, indicating there was insufficient remaining memory (or virtual memory) to satisfy the request. </p>
<p> The request was judged to be small, so the possibility to trap it depends on the way Perl was compiled. By default it is not trappable. However, if compiled for this, Perl may use the contents of <tt>$^M</tt> as an emergency pool after <code>die()</code>ing with this message. In this case the error is trappable <i>once</i>.</p>
<dt>Out of memory during request for %s</p>
<dd> (F) The <code>malloc()</code> function returned 0, indicating there was insufficient remaining memory (or virtual memory) to satisfy the request. However, the request was judged large enough (compile-time default is 64K), so a possibility to shut down by trapping this error is granted.</p>
<dt>panic: frexp</p>
<dd> (P) The library function <code>frexp()</code> failed, making printf(&#8220;%f&#8221;) impossible.</p>
<dt>Possible attempt to put comments in <code>qw()</code> list</p>
<dd> (W) <code>qw()</code> lists contain items separated by whitespace; as with literal strings, comment characters are not ignored, but are instead treated as literal data. (You may have used different delimiters than the parentheses shown here; braces are also frequently used.) </p>
<p> You probably wrote something like this: </p>
<pre>
    @list = qw(
        a # a comment
        b # another comment
    );
</pre>
<p> when you should have written this: </p>
<pre>
    @list = qw(
        a
        b
    );
</pre>
<p> If you really want comments, build your list the old-fashioned way, with quotes and commas: </p>
<pre>
    @list = (
        'a',    # a comment
        'b',    # another comment
    );
</pre>
<dt>Possible attempt to separate words with commas</p>
<dd> (W) <code>qw()</code> lists contain items separated by whitespace; therefore commas aren&#8217;t needed to separate the items. (You may have used different delimiters than the parentheses shown here; braces are also frequently used.) </p>
<p> You probably wrote something like this: </p>
<pre>
    qw! a, b, c !;
</pre>
<p> which puts literal commas into some of the list items. Write it without commas if you don&#8217;t want them to appear in your data: </p>
<pre>
    qw! a b c !;
</pre>
<dt>Scalar value @%s{%s} better written as $%s{%s}</p>
<dd> (W) You&#8217;ve used a hash slice (indicated by @) to select a single element of a hash. Generally it&#8217;s better to ask for a scalar value (indicated by $). The difference is that <tt>$foo{&amp;bar}</tt> always behaves like a scalar, both when assigning to it and when evaluating its argument, while <tt>@foo{&amp;bar}</tt> behaves like a list when you assign to it, and provides a list context to its subscript, which can do weird things if you&#8217;re expecting only one subscript.</p>
<dt>Stub found while resolving method `%s&#8217; overloading `%s&#8217; in %s</p>
<dd> (P) Overloading resolution over <tt>@ISA</tt> tree may be broken by importing stubs. Stubs should never be implicitly created, but explicit calls to <tt>&quot;can&quot;</tt> may break this.</p>
<dt>Too late for &quot;<code>-T</code>&quot; option</p>
<dd> (X) The #! line (or local equivalent) in a Perl script contains the <code>-T</code> option, but Perl was not invoked with <code>-T</code> in its argument list. This is an error because, by the time Perl discovers a <code>-T</code> in a script, it&#8217;s too late to properly taint everything from the environment. So Perl gives up.</p>
<dt>untie attempted while %d inner references still exist</p>
<dd> (W) A copy of the object returned from <tt>&quot;tie&quot;</tt> (or <tt>&quot;tied&quot;</tt>) was still valid when <tt>&quot;untie&quot;</tt> was called.</p>
<dt>Unrecognized character %s</p>
<dd> (F) The Perl parser has no idea what to do with the specified character in your Perl script (or eval). Perhaps you tried to run a compressed script, a binary program, or a directory as a Perl program.</p>
<dt>Unsupported function fork</p>
<dd> (F) Your version of executable does not support forking. </p>
<p> Note that under some systems, like <font SIZE="-1">OS/2,</font> there may be different flavors of Perl executables, some of which may support fork, some not. Try changing the name you call Perl by to <tt>&quot;perl_&quot;</tt>, <tt>&quot;perl__&quot;</tt>, and so on.</p>
<dt>Use of &quot;$$&lt;digit&gt;&quot; to mean &quot;${$}&lt;digit&gt;&quot; is deprecated</p>
<dd> (D) Perl versions before 5.004 misinterpreted any type marker followed by &#8220;$&#8221; and a digit. For example, &#8220;$$0&#8221; was incorrectly taken to mean &#8220;${$}0&#8221; instead of &#8220;${$0}&#8221;. This bug is (mostly) fixed in Perl 5.004. </p>
<p> However, the developers of Perl 5.004 could not fix this bug completely, because at least two widely-used modules depend on the old meaning of &#8220;$$0&#8221; in a string. So Perl 5.004 still interprets &#8220;$$&lt;digit&gt;&#8221; in the old (broken) way inside strings; but it generates this message as a warning. And in Perl 5.005, this special treatment will cease.</p>
<dt>Value of %s can be &quot;0&quot;; test with <code>defined()</code></p>
<dd> (W) In a conditional expression, you used &lt;<font SIZE="-1">HANDLE</font>&gt;, &lt;*&gt; (glob), <tt>&quot;each()&quot;</tt>, or <tt>&quot;readdir()&quot;</tt> as a boolean value. Each of these constructs can return a value of &#8220;0&#8221;; that would make the conditional expression false, which is probably not what you intended. When using these constructs in conditional expressions, test their values with the <tt>&quot;defined&quot;</tt> operator.</p>
<dt>Variable &quot;%s&quot; may be unavailable</p>
<dd> (W) An inner (nested) <i>anonymous</i> subroutine is inside a <i>named</i> subroutine, and outside that is another subroutine; and the anonymous (innermost) subroutine is referencing a lexical variable defined in the outermost subroutine. For example: </p>
<pre><code>
sub outermost
{
    my $a;
    sub middle
    {
        sub
        {
            $a
        }
    }
}
</code></pre>
<p> If the anonymous subroutine is called or referenced (directly or indirectly) from the outermost subroutine, it will share the variable as you would expect. But if the anonymous subroutine is called or referenced when the outermost subroutine is not active, it will see the value of the shared variable as it was before and during the *first* call to the outermost subroutine, which is probably not what you want. </p>
<p> In these circumstances, it is usually best to make the middle subroutine anonymous, using the <tt>&quot;sub {}&quot;</tt> syntax. Perl has specific support for shared variables in nested anonymous subroutines; a named subroutine in between interferes with this feature.</p>
<dt>Variable &quot;%s&quot; will not stay shared</p>
<dd> (W) An inner (nested) <i>named</i> subroutine is referencing a lexical variable defined in an outer subroutine. </p>
<p> When the inner subroutine is called, it will probably see the value of the outer subroutine&#8217;s variable as it was before and during the *first* call to the outer subroutine; in this case, after the first call to the outer subroutine is complete, the inner and outer subroutines will no longer share a common value for the variable. In other words, the variable will no longer be shared. </p>
<p> Furthermore, if the outer subroutine is anonymous and references a lexical variable outside itself, then the outer and inner subroutines will <i>never</i> share the given variable. </p>
<p> This problem can usually be solved by making the inner subroutine anonymous, using the <tt>&quot;sub {}&quot;</tt> syntax. When inner anonymous subs that reference variables in outer subroutines are called or referenced, they are automatically rebound to the current values of such variables.</p>
<dt>Warning: something&#8217;s wrong</p>
<dd> (W) You passed <code>warn()</code> an empty string (the equivalent of <tt>&quot;warn &quot;&quot;&quot;</tt>) or you called it with no args and <tt>$_</tt> was empty.</p>
<dt>Ill-formed logical name |%s| in prime_env_iter</p>
<dd> (W) A warning peculiar to <font SIZE="-1">VMS.</font> A logical name was encountered when preparing to iterate over <tt>%ENV</tt> which violates the syntactic rules governing logical names. Since it cannot be translated normally, it is skipped, and will not appear in <tt>%ENV</tt>. This may be a benign occurrence, as some software packages might directly modify logical name tables and introduce nonstandard names, or it may indicate that a logical name table has been corrupted.</p>
<dt>Got an error from DosAllocMem</p>
<dd> (P) An error peculiar to <font SIZE="-1">OS/2.</font> Most probably you&#8217;re using an obsolete version of Perl, and this should not happen anyway.</p>
<dt>Malformed <font SIZE="-1">PERLLIB_PREFIX</font></p>
<dd> (F) An error peculiar to <font SIZE="-1">OS/2.</font> <font SIZE="-1">PERLLIB_PREFIX</font> should be of the form </p>
<pre>
    prefix1;prefix2
</pre>
<p> or </p>
<pre>
    prefix1 prefix2
</pre>
<p> with nonempty prefix1 and prefix2. If <tt>&quot;prefix1&quot;</tt> is indeed a prefix of a builtin library search path, prefix2 is substituted. The error may appear if components are not found, or are too long. See &#8220;<font SIZE="-1">PERLLIB_PREFIX&#8221;</font> in <i></i><font SIZE="-1"><i>README</i></font><i>.os2</i>.</p>
<dt><font SIZE="-1">PERL_SH_DIR</font> too long</p>
<dd> (F) An error peculiar to <font SIZE="-1">OS/2. PERL_SH_DIR</font> is the directory to find the <tt>&quot;sh&quot;</tt>-shell in. See &#8220;<font SIZE="-1">PERL_SH_DIR&#8221;</font> in <i></i><font SIZE="-1"><i>README</i></font><i>.os2</i>.</p>
<dt>Process terminated by SIG%s</p>
<dd> (W) This is a standard message issued by <font SIZE="-1">OS/2</font> applications, while *nix applications die in silence. It is considered a feature of the <font SIZE="-1">OS/2</font> port. One can easily disable this by appropriate sighandlers, see &#8220;Signals&#8221; in perlipc. See also &#8220;Process terminated by <font SIZE="-1">SIGTERM/SIGINT&#8221;</font> in <i></i><font SIZE="-1"><i>README</i></font><i>.os2</i>.</dl>
<h2>BUGS</h2>
<p> If you find what you think is a bug, you might check the headers of recently posted articles in the comp.lang.perl.misc newsgroup. There may also be information at <a rel="nofollow" href="http://www.perl.com/perl/">http://www.perl.com/perl/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Make sure you trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <tt>&quot;perl -V&quot;</tt>, will be sent off to &lt;<i>perlbug [at] perl.com</i>&gt; to be analysed by the Perl porting team.</p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. This file has been significantly updated for 5.004, so even veteran users should look through it. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Copying</i> file for copyright information.</p>
<h2>HISTORY</h2>
<p> Constructed by Tom Christiansen, grabbing material with permission from innumerable contributors, with kibitzing by more than a few Perl porters. </p>
<p> Last update: Wed May 14 11:14:09 <font SIZE="-1">EDT 1997</font> </p>
<h2>Index</h2>
<dt><a href="#lbBH">Support for More Operating Systems</a></p>
<dd>
<dt><a href="#lbBM">Pragmata</a></p>
<dd>
<dt><a href="#lbBN">Modules</a></p>
<dd>
<dt><a href="#lbBY">Utility Changes</a></p>
<dd>
<dt><a href="#lbCB">C Language API Changes</a></p>
<dd>
<dt><a href="#lbCC">Documentation Changes</a></p>
<dd>
<dt><a href="#lbCD">New Diagnostics</a></p>
<dd>
<dt><a href="#lbCE">BUGS</a></p>
<dd>
<dt><a href="#lbCF">SEE ALSO</a></p>
<dd>
<dt><a href="#lbCG">HISTORY</a></p>
<dd></dl>
