---
title: "perlvar(1)"
name: "perlvar"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlvar/"
description: "perlvar – Perl predefined variables"
---

<h2 class="name">NAME</h2>
<p> perlvar &#8211; Perl predefined variables </p>
<h2>DESCRIPTION</h2>
<h3>The Syntax of Variable Names</h3>
<p> Variable names in Perl can have several formats. Usually, they must begin with a letter or underscore, in which case they can be arbitrarily long (up to an internal limit of 251 characters) and may contain letters, digits, underscores, or the special sequence <tt>&quot;::&quot;</tt> or <tt>&quot;'&quot;</tt>. In this case, the part before the last <tt>&quot;::&quot;</tt> or <tt>&quot;'&quot;</tt> is taken to be a <i>package qualifier</i>; see perlmod. A Unicode letter that is not <font SIZE="-1">ASCII</font> is not considered to be a letter unless <tt>&quot;use utf8&quot;</tt> is in effect, and somewhat more complicated rules apply; see &#8220;Identifier parsing&#8221; in perldata for details. </p>
<p> Perl variable names may also be a sequence of digits, a single punctuation character, or the two-character sequence: <tt>&quot;^&quot;</tt> (caret or <font SIZE="-1">CIRCUMFLEX ACCENT</font>) followed by any one of the characters <tt>&quot;[][A-Z^_?\]&quot;</tt>. These names are all reserved for special uses by Perl; for example, the all-digits names are used to hold data captured by backreferences after a regular expression match. </p>
<p> Since Perl v5.6.0, Perl variable names may also be alphanumeric strings preceded by a caret. These must all be written in the form <tt>&quot;${^Foo}&quot;</tt>; the braces are not optional. <tt>&quot;${^Foo}&quot;</tt> denotes the scalar variable whose name is considered to be a control-<tt>&quot;F&quot;</tt> followed by two <tt>&quot;o&quot;</tt>&#8216;s. These variables are reserved for future special uses by Perl, except for the ones that begin with <tt>&quot;^_&quot;</tt> (caret-underscore). No name that begins with <tt>&quot;^_&quot;</tt> will acquire a special meaning in any future version of Perl; such names may therefore be used safely in programs. <tt>$^_</tt> itself, however, <i>is</i> reserved. </p>
<p> Perl identifiers that begin with digits or punctuation characters are exempt from the effects of the <tt>&quot;package&quot;</tt> declaration and are always forced to be in package <tt>&quot;main&quot;</tt>; they are also exempt from <tt>&quot;strict 'vars'&quot;</tt> errors. A few other names are also exempt in these ways: </p>
<pre>
    ENV      STDIN
    INC      STDOUT
    ARGV     STDERR
    ARGVOUT
    SIG
</pre>
<p> In particular, the special <tt>&quot;${^_XYZ}&quot;</tt> variables are always taken to be in package <tt>&quot;main&quot;</tt>, regardless of any <tt>&quot;package&quot;</tt> declarations presently in scope.</p>
<h2>SPECIAL VARIABLES</h2>
<p> The following names have special meaning to Perl. Most punctuation names have reasonable mnemonics, or analogs in the shells. Nevertheless, if you wish to use long variable names, you need only say: </p>
<pre>
    use English;
</pre>
<p> at the top of your program. This aliases all the short names to the long names in the current package. Some even have medium names, generally borrowed from <code>awk</code>. For more info, please see English. </p>
<p> Before you continue, note the sort order for variables. In general, we first list the variables in case-insensitive, almost-lexigraphical order (ignoring the <tt>&quot;{&quot;</tt> or <tt>&quot;^&quot;</tt> preceding words, as in <tt>&quot;${^UNICODE}&quot;</tt> or <tt>$^T</tt>), although <tt>$_</tt> and <tt>@_</tt> move up to the top of the pile. For variables with the same identifier, we list it in order of scalar, array, hash, and bareword.</p>
<h3>General Variables</h3>
<dl>
<dt>$ARG</p>
<dd>
<dt>$_</p>
<dd> The default input and pattern-searching space. The following pairs are equivalent: </p>
<pre><code>
while (&lt;&gt;) {
    ...
}
#equivalent only in while !while (defined($_ = &lt;&gt;)){... } / ^Subject : /
                                                    $_ = ~ / ^Subject : /
                                                             tr / a -
                                                         z / A - Z / $_ = ~tr / a - z / A - Z / chomp chomp($_)
</code></pre>
<p> Here are the places where Perl will assume <tt>$_</tt> even if you don&#8217;t use it:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> The following functions use <tt>$_</tt> as a default argument: </p>
<p> abs, alarm, chomp, chop, chr, chroot, cos, defined, eval, evalbytes, exp, fc, glob, hex, int, lc, lcfirst, length, log, lstat, mkdir, oct, ord, pos, print, printf, quotemeta, readlink, readpipe, ref, require, reverse (in scalar context only), rmdir, say, sin, split (for its second argument), sqrt, stat, study, uc, ucfirst, unlink, unpack.</p>
<dt>&bull;</p>
<dd> All file tests (<tt>&quot;-f&quot;</tt>, <tt>&quot;-d&quot;</tt>) except for <tt>&quot;-t&quot;</tt>, which defaults to <font SIZE="-1">STDIN.</font> See &#8220;-X&#8221; in perlfunc</p>
<dt>&bull;</p>
<dd> The pattern matching operations <tt>&quot;m//&quot;</tt>, <tt>&quot;s///&quot;</tt> and <tt>&quot;tr///&quot;</tt> (aka <tt>&quot;y///&quot;</tt>) when used without an <tt>&quot;=~&quot;</tt> operator.</p>
<dt>&bull;</p>
<dd> The default iterator variable in a <tt>&quot;foreach&quot;</tt> loop if no other variable is supplied.</p>
<dt>&bull;</p>
<dd> The implicit iterator variable in the <tt>&quot;grep()&quot;</tt> and <tt>&quot;map()&quot;</tt> functions.</p>
<dt>&bull;</p>
<dd> The implicit variable of <tt>&quot;given()&quot;</tt>.</p>
<dt>&bull;</p>
<dd> The default place to put the next value or input record when a <tt>&quot;&lt;FH&gt;&quot;</tt>, <tt>&quot;readline&quot;</tt>, <tt>&quot;readdir&quot;</tt> or <tt>&quot;each&quot;</tt> operation&#8217;s result is tested by itself as the sole criterion of a <tt>&quot;while&quot;</tt> test. Outside a <tt>&quot;while&quot;</tt> test, this will not happen.</dl>
</dl>
<dl>
<dt>
<dd>
<p> <tt>$_</tt> is a global variable. </p>
<p> However, between perl v5.10.0 and v5.24.0, it could be used lexically by writing <tt>&quot;my $_&quot;</tt>. Making <tt>$_</tt> refer to the global <tt>$_</tt> in the same scope was then possible with <tt>&quot;our $_&quot;</tt>. This experimental feature was removed and is now a fatal error, but you may encounter it in older code. </p>
<p> Mnemonic: underline is understood in certain operations.</dl>
<dt>@ARG</p>
<dd>
<dt>@_</p>
<dd> Within a subroutine the array <tt>@_</tt> contains the parameters passed to that subroutine. Inside a subroutine, <tt>@_</tt> is the default array for the array operators <tt>&quot;pop&quot;</tt> and <tt>&quot;shift&quot;</tt>. </p>
<p> See perlsub.</p>
<dt>$LIST_SEPARATOR</p>
<dd>
<dt>$&quot;</p>
<dd> When an array or an array slice is interpolated into a double-quoted string or a similar context such as <tt>&quot;/.../&quot;</tt>, its elements are separated by this value. Default is a space. For example, this: </p>
<pre>
    print &quot;The array is: @array
&quot;;
</pre>
<p> is equivalent to this: </p>
<pre>
    print &quot;The array is: &quot; . join($&quot;, @array) . &quot;
&quot;;
</pre>
<p> Mnemonic: works in double-quoted context.</p>
<dt>$PROCESS_ID</p>
<dd>
<dt>$PID</p>
<dd>
<dt>$$</p>
<dd> The process number of the Perl running this script. Though you <i>can</i> set this variable, doing so is generally discouraged, although it can be invaluable for some testing purposes. It will be reset automatically across <tt>&quot;fork()&quot;</tt> calls. </p>
<p> Note for Linux and Debian GNU/kFreeBSD users: Before Perl v5.16.0 perl would emulate <font SIZE="-1">POSIX</font> semantics on Linux systems using LinuxThreads, a partial implementation of <font SIZE="-1">POSIX</font> Threads that has since been superseded by the Native <font SIZE="-1">POSIX</font> Thread Library (<font SIZE="-1">NPTL</font>). </p>
<p> LinuxThreads is now obsolete on Linux, and caching <tt>&quot;getpid()&quot;</tt> like this made embedding perl unnecessarily complex (since you&#8217;d have to manually update the value of $$), so now <tt>$$</tt> and <tt>&quot;getppid()&quot;</tt> will always return the same values as the underlying C library. </p>
<p> Debian GNU/kFreeBSD systems also used LinuxThreads up until and including the 6.0 release, but after that moved to FreeBSD thread semantics, which are POSIX-like. </p>
<p> To see if your system is affected by this discrepancy check if <tt>&quot;getconf GNU_LIBPTHREAD_VERSION | grep -q NPTL&quot;</tt> returns a false value. <font SIZE="-1">NTPL</font> threads preserve the <font SIZE="-1">POSIX</font> semantics. </p>
<p> Mnemonic: same as shells.</p>
<dt>$PROGRAM_NAME</p>
<dd>
<dt>$0</p>
<dd> Contains the name of the program being executed. </p>
<p> On some (but not all) operating systems assigning to <tt>$0</tt> modifies the argument area that the <tt>&quot;ps&quot;</tt> program sees. On some platforms you may have to use special <tt>&quot;ps&quot;</tt> options or a different <tt>&quot;ps&quot;</tt> to see the changes. Modifying the <tt>$0</tt> is more useful as a way of indicating the current program state than it is for hiding the program you&#8217;re running. </p>
<p> Note that there are platform-specific limitations on the maximum length of <tt>$0</tt>. In the most extreme case it may be limited to the space occupied by the original <tt>$0</tt>. </p>
<p> In some platforms there may be arbitrary amount of padding, for example space characters, after the modified name as shown by <tt>&quot;ps&quot;</tt>. In some platforms this padding may extend all the way to the original length of the argument area, no matter what you do (this is the case for example with Linux 2.2). </p>
<p> Note for <font SIZE="-1">BSD</font> users: setting <tt>$0</tt> does not completely remove &#8220;perl&#8221; from the <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1) output. For example, setting <tt>$0</tt> to <tt>&quot;foobar&quot;</tt> may result in <tt>&quot;perl: foobar (perl)&quot;</tt> (whether both the <tt>&quot;perl: &quot;</tt> prefix and the &#8220; (perl)&#8221; suffix are shown depends on your exact <font SIZE="-1">BSD</font> variant and version). This is an operating system feature, Perl cannot help it. </p>
<p> In multithreaded scripts Perl coordinates the threads so that any thread may modify its copy of the <tt>$0</tt> and the change becomes visible to <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1) (assuming the operating system plays along). Note that the view of <tt>$0</tt> the other threads have will not change since they have their own copies of it. </p>
<p> If the program has been given to perl via the switches <tt>&quot;-e&quot;</tt> or <tt>&quot;-E&quot;</tt>, <tt>$0</tt> will contain the string <tt>&quot;-e&quot;</tt>. </p>
<p> On Linux as of perl v5.14.0 the legacy process name will be set with <tt><a href="/docs/linux/man/2-prctl/">prctl</a>(2)</tt>, in addition to altering the <font SIZE="-1">POSIX</font> name via <tt>&quot;argv[0]&quot;</tt> as perl has done since version 4.000. Now system utilities that read the legacy process name such as ps, top and killall will recognize the name you set when assigning to <tt>$0</tt>. The string you supply will be cut off at 16 bytes, this is a limitation imposed by Linux. </p>
<p> Mnemonic: same as <code>sh</code> and <code>ksh</code>.</p>
<dt>$REAL_GROUP_ID</p>
<dd>
<dt>$GID</p>
<dd>
<dt>$(</p>
<dd> The real gid of this process. If you are on a machine that supports membership in multiple groups simultaneously, gives a space separated list of groups you are in. The first number is the one returned by <tt>&quot;getgid()&quot;</tt>, and the subsequent ones by <tt>&quot;getgroups()&quot;</tt>, one of which may be the same as the first number. </p>
<p> However, a value assigned to <tt>$(</tt> must be a single number used to set the real gid. So the value given by <tt>$(</tt> should <i>not</i> be assigned back to <tt>$(</tt> without being forced numeric, such as by adding zero. Note that this is different to the effective gid (<tt>$)</tt>) which does take a list. </p>
<p> You can change both the real gid and the effective gid at the same time by using <tt>&quot;POSIX::setgid()&quot;</tt>. Changes to <tt>$(</tt> require a check to <tt>$!</tt> to detect any possible errors after an attempted change. </p>
<p> Mnemonic: parentheses are used to <i>group</i> things. The real gid is the group you <i>left</i>, if you&#8217;re running setgid.</p>
<dt>$EFFECTIVE_GROUP_ID</p>
<dd>
<dt>$EGID</p>
<dd>
<dt>$)</p>
<dd> The effective gid of this process. If you are on a machine that supports membership in multiple groups simultaneously, gives a space separated list of groups you are in. The first number is the one returned by <tt>&quot;getegid()&quot;</tt>, and the subsequent ones by <tt>&quot;getgroups()&quot;</tt>, one of which may be the same as the first number. </p>
<p> Similarly, a value assigned to <tt>$)</tt> must also be a space-separated list of numbers. The first number sets the effective gid, and the rest (if any) are passed to <tt>&quot;setgroups()&quot;</tt>. To get the effect of an empty list for <tt>&quot;setgroups()&quot;</tt>, just repeat the new effective gid; that is, to force an effective gid of 5 and an effectively empty <tt>&quot;setgroups()&quot;</tt> list, say <tt>&quot; $) = &quot;5 5&quot; &quot;</tt>. </p>
<p> You can change both the effective gid and the real gid at the same time by using <tt>&quot;POSIX::setgid()&quot;</tt> (use only a single numeric argument). Changes to <tt>$)</tt> require a check to <tt>$!</tt> to detect any possible errors after an attempted change. </p>
<p> <tt>$&lt;</tt>, <tt>$&gt;</tt>, <tt>$(</tt> and <tt>$)</tt> can be set only on machines that support the corresponding <i>set[re][ug]</i>id()<i></i> routine. <tt>$(</tt> and <tt>$)</tt> can be swapped only on machines supporting <tt>&quot;setregid()&quot;</tt>. </p>
<p> Mnemonic: parentheses are used to <i>group</i> things. The effective gid is the group that&#8217;s <i>right</i> for you, if you&#8217;re running setgid.</p>
<dt>$REAL_USER_ID</p>
<dd>
<dt>$UID</p>
<dd>
<dt>$&lt;</p>
<dd> The real uid of this process. You can change both the real uid and the effective uid at the same time by using <tt>&quot;POSIX::setuid()&quot;</tt>. Since changes to <tt>$&lt;</tt> require a system call, check <tt>$!</tt> after a change attempt to detect any possible errors. </p>
<p> Mnemonic: it&#8217;s the uid you came <i>from</i>, if you&#8217;re running setuid.</p>
<dt>$EFFECTIVE_USER_ID</p>
<dd>
<dt>$EUID</p>
<dd>
<dt>$&gt;</p>
<dd> The effective uid of this process. For example: </p>
<pre>
    $&lt; = $&gt;;            # set real to effective uid
    ($&lt;,$&gt;) = ($&gt;,$&lt;);  # swap real and effective uids
</pre>
<p> You can change both the effective uid and the real uid at the same time by using <tt>&quot;POSIX::setuid()&quot;</tt>. Changes to <tt>$&gt;</tt> require a check to <tt>$!</tt> to detect any possible errors after an attempted change. </p>
<p> <tt>$&lt;</tt> and <tt>$&gt;</tt> can be swapped only on machines supporting <tt>&quot;setreuid()&quot;</tt>. </p>
<p> Mnemonic: it&#8217;s the uid you went <i>to</i>, if you&#8217;re running setuid.</p>
<dt>$SUBSCRIPT_SEPARATOR</p>
<dd>
<dt>$SUBSEP</p>
<dd>
<dt>$;</p>
<dd> The subscript separator for multidimensional array emulation. If you refer to a hash element as </p>
<pre>
    $foo{$x,$y,$z}
</pre>
<p> it really means </p>
<pre>
    $foo{join($;, $x, $y, $z)}
</pre>
<p> But don&#8217;t put </p>
<pre>
    @foo{$x,$y,$z}      # a slice--note the @
</pre>
<p> which means </p>
<p>($foo{$x}, $foo{$y}, $foo{$z})</p>
<p> Default is &#8220;&#8221;, the same as <font SIZE="-1">SUBSEP</font> in <code>awk</code>. If your keys contain binary data there might not be any safe value for <tt>$;</tt>. </p>
<p> Consider using &#8220;real&#8221; multidimensional arrays as described in perllol. </p>
<p> Mnemonic: comma (the syntactic subscript separator) is a semi-semicolon.</p>
<dt>$a</p>
<dd>
<dt>$b</p>
<dd> Special package variables when using <tt>&quot;sort()&quot;</tt>, see &#8220;sort&#8221; in perlfunc. Because of this specialness <tt>$a</tt> and <tt>$b</tt> don&#8217;t need to be declared (using <tt>&quot;use vars&quot;</tt>, or <tt>&quot;our()&quot;</tt>) even when using the <tt>&quot;strict 'vars'&quot;</tt> pragma. Don&#8217;t lexicalize them with <tt>&quot;my $a&quot;</tt> or <tt>&quot;my $b&quot;</tt> if you want to be able to use them in the <tt>&quot;sort()&quot;</tt> comparison block or function.</p>
<dt>%ENV</p>
<dd> The hash <tt>%ENV</tt> contains your current environment. Setting a value in <tt>&quot;ENV&quot;</tt> changes the environment for any child processes you subsequently <tt>&quot;fork()&quot;</tt> off. </p>
<p> As of v5.18.0, both keys and values stored in <tt>%ENV</tt> are stringified. </p>
<p>my $foo = 1;<br />
$ENV{&#8216;bar&#8217;} = \$foo;<br />
if (ref $ENV{&#8216;bar&#8217;}) {<br />
    say &#8220;Pre 5.18.0 Behaviour&#8221;;<br />
} else {<br />
    say &#8220;Post 5.18.0 Behaviour&#8221;;<br />
}</p>
<p> Previously, only child processes received stringified values: </p>
<p>my $foo = 1;<br />
$ENV{&#8216;bar&#8217;} = \$foo;<br />
#Always printed &#8216;non ref&#8217;<br />
system($ ^ X, &#8216;-e&#8217;,<br />
       q / print(ref $ENV{&#8216;bar&#8217;} ? &#8216;ref&#8217; : &#8216;non ref&#8217;) /);</p>
<p> This happens because you can&#8217;t really share arbitrary data structures with foreign processes.</p>
<dt>$OLD_PERL_VERSION</p>
<dd>
<dt>$]</p>
<dd> The revision, version, and subversion of the Perl interpreter, represented as a decimal of the form 5.XXXYYY, where <font SIZE="-1">XXX</font> is the version / 1e3 and <font SIZE="-1">YYY</font> is the subversion / 1e6. For example, Perl v5.10.1 would be &#8220;5.010001&#8221;. </p>
<p> This variable can be used to determine whether the Perl interpreter executing a script is in the right range of versions: </p>
<pre>
    warn &quot;No PerlIO!
&quot; if $] lt '5.008';
</pre>
<p> When comparing <tt>$]</tt>, string comparison operators are <code>highly recommended</code>. The inherent limitations of binary floating point representation can sometimes lead to incorrect comparisons for some numbers on some architectures. </p>
<p> See also the documentation of <tt>&quot;use VERSION&quot;</tt> and <tt>&quot;require VERSION&quot;</tt> for a convenient way to fail if the running Perl interpreter is too old. </p>
<p> See &#8220;$^V&#8221; for a representation of the Perl version as a version object, which allows more flexible string comparisons. </p>
<p> The main advantage of <tt>$]</tt> over <tt>$^V</tt> is that it works the same on any version of Perl. The disadvantages are that it can&#8217;t easily be compared to versions in other formats (e.g. literal v-strings, &#8220;v1.2.3&#8221; or version objects) and numeric comparisons can occasionally fail; it&#8217;s good for string literal version checks and bad for comparing to a variable that hasn&#8217;t been sanity-checked. </p>
<p> The <tt>$OLD_PERL_VERSION</tt> form was added in Perl v5.20.0 for historical reasons but its use is discouraged. (If your reason to use <tt>$]</tt> is to run code on old perls then referring to it as <tt>$OLD_PERL_VERSION</tt> would be self-defeating.) </p>
<p> Mnemonic: Is this version of perl in the right bracket?</p>
<dt>$SYSTEM_FD_MAX</p>
<dd>
<dt>$^F</p>
<dd> The maximum system file descriptor, ordinarily 2. System file descriptors are passed to <tt>&quot;exec()&quot;</tt>ed processes, while higher file descriptors are not. Also, during an <tt>&quot;open()&quot;</tt>, system file descriptors are preserved even if the <tt>&quot;open()&quot;</tt> fails (ordinary file descriptors are closed before the <tt>&quot;open()&quot;</tt> is attempted). The close-on-exec status of a file descriptor will be decided according to the value of <tt>$^F</tt> when the corresponding file, pipe, or socket was opened, not the time of the <tt>&quot;exec()&quot;</tt>.</p>
<dt>@F</p>
<dd> The array <tt>@F</tt> contains the fields of each line read in when autosplit mode is turned on. See perlrun for the <code>-a</code> switch. This array is package-specific, and must be declared or given a full package name if not in package main when running under <tt>&quot;strict 'vars'&quot;</tt>.</p>
<dt>@INC</p>
<dd> The array <tt>@INC</tt> contains the list of places that the <tt>&quot;do EXPR&quot;</tt>, <tt>&quot;require&quot;</tt>, or <tt>&quot;use&quot;</tt> constructs look for their library files. It initially consists of the arguments to any <code>-I</code> command-line switches, followed by the default Perl library, probably <i>/usr/local/lib/perl</i>. Prior to Perl 5.26, <tt>&quot;.&quot;</tt> -which represents the current directory, was included in <tt>@INC</tt>; it has been removed. This change in behavior is documented in <tt>&quot;PERL_USE_UNSAFE_INC&quot;</tt> and it is not recommended that <tt>&quot;.&quot;</tt> be re-added to <tt>@INC</tt>. If you need to modify <tt>@INC</tt> at runtime, you should use the <tt>&quot;use lib&quot;</tt> pragma to get the machine-dependent library properly loaded as well: </p>
<pre>
    use lib '/mypath/libdir/';
    use SomeMod;
</pre>
<p> You can also insert hooks into the file inclusion system by putting Perl code directly into <tt>@INC</tt>. Those hooks may be subroutine references, array references or blessed objects. See &#8220;require&#8221; in perlfunc for details.</p>
<dt>%INC</p>
<dd> The hash <tt>%INC</tt> contains entries for each filename included via the <tt>&quot;do&quot;</tt>, <tt>&quot;require&quot;</tt>, or <tt>&quot;use&quot;</tt> operators. The key is the filename you specified (with module names converted to pathnames), and the value is the location of the file found. The <tt>&quot;require&quot;</tt> operator uses this hash to determine whether a particular file has already been included. </p>
<p> If the file was loaded via a hook (e.g. a subroutine reference, see &#8220;require&#8221; in perlfunc for a description of these hooks), this hook is by default inserted into <tt>%INC</tt> in place of a filename. Note, however, that the hook may have set the <tt>%INC</tt> entry by itself to provide some more specific info.</p>
<dt>$INPLACE_EDIT</p>
<dd>
<dt>$^I</p>
<dd> The current value of the inplace-edit extension. Use <tt>&quot;undef&quot;</tt> to disable inplace editing. </p>
<p> Mnemonic: value of <code>-i</code> switch.</p>
<dt>@ISA</p>
<dd> Each package contains a special array called <tt>@ISA</tt> which contains a list of that class&#8217;s parent classes, if any. This array is simply a list of scalars, each of which is a string that corresponds to a package name. The array is examined when Perl does method resolution, which is covered in perlobj. </p>
<p> To load packages while adding them to <tt>@ISA</tt>, see the parent pragma. The discouraged base pragma does this as well, but should not be used except when compatibility with the discouraged fields pragma is required.</p>
<dt>$^M</p>
<dd> By default, running out of memory is an untrappable, fatal error. However, if suitably built, Perl can use the contents of <tt>$^M</tt> as an emergency memory pool after <tt>&quot;die()&quot;</tt>ing. Suppose that your Perl were compiled with <tt>&quot;-DPERL_EMERGENCY_SBRK&quot;</tt> and used Perl&#8217;s malloc. Then </p>
<pre>
    $^M = 'a' x (1 &lt;&lt; 16);
</pre>
<p> would allocate a 64K buffer for use in an emergency. See the <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file in the Perl distribution for information on how to add custom C compilation flags when compiling perl. To discourage casual use of this advanced feature, there is no English long name for this variable. </p>
<p> This variable was added in Perl 5.004.</p>
<dt>$OSNAME</p>
<dd>
<dt>$^O</p>
<dd> The name of the operating system under which this copy of Perl was built, as determined during the configuration process. For examples see &#8220;<font SIZE="-1">PLATFORMS&#8221;</font> in perlport. </p>
<p> The value is identical to <tt>$Config{'osname'}</tt>. See also Config and the <code>-V</code> command-line switch documented in perlrun. </p>
<p> In Windows platforms, <tt>$^O</tt> is not very helpful: since it is always <tt>&quot;MSWin32&quot;</tt>, it doesn&#8217;t tell the difference between 95/98/ME/NT/2000/XP/CE/.NET. Use <tt>&quot;Win32::GetOSName()&quot;</tt> or <code>Win32::GetOSVersion()</code> (see Win32 and perlport) to distinguish between the variants. </p>
<p> This variable was added in Perl 5.003.</p>
<dt>%SIG</p>
<dd> The hash <tt>%SIG</tt> contains signal handlers for signals. For example: </p>
<p>sub handler<br />
{<br />
# 1st argument is signal name my($sig) = @_;<br />
    print &#8220;Caught a SIG$sig&#8211;shutting down
&#8221;;<br />
    close(LOG);<br />
    exit(0);<br />
}<br />
$SIG{&#8216;INT&#8217;} = \&amp; handler;<br />
$SIG{&#8216;QUIT&#8217;} = \&amp; handler;<br />
&#8230; $SIG{&#8216;INT&#8217;} = &#8216;DEFAULT&#8217;;<br />
#restore default action<br />
    $SIG{&#8216;QUIT&#8217; } = &#8216;IGNORE&#8217;;<br />
#ignore SIGQUIT</p>
<p> Using a value of <tt>'IGNORE'</tt> usually has the effect of ignoring the signal, except for the <tt>&quot;CHLD&quot;</tt> signal. See perlipc for more about this special case. </p>
<p> Here are some other examples: </p>
<p>$SIG{&#8220;PIPE&#8221;} = &#8220;Plumber&#8221;;<br />
#assumes main::Plumber(not<br />
#recommended)<br />
                       $SIG{&#8220;PIPE&#8221;} = \&amp; Plumber;<br />
                       #just fine; assume current<br />
#Plumber<br />
                                       $SIG{&#8220;PIPE&#8221;} = *Plumber;<br />
                       #somewhat esoteric<br />
                           $SIG{&#8220;PIPE&#8221;} = Plumber();<br />
                       #oops, what did Plumber()<br />
#return ? ?</p>
<p> Be sure not to use a bareword as the name of a signal handler, lest you inadvertently call it. </p>
<p> If your system has the <tt>&quot;sigaction()&quot;</tt> function then signal handlers are installed using it. This means you get reliable signal handling. </p>
<p> The default delivery policy of signals changed in Perl v5.8.0 from immediate (also known as &#8220;unsafe&#8221;) to deferred, also known as &#8220;safe signals&#8221;. See perlipc for more information. </p>
<p> Certain internal hooks can be also set using the <tt>%SIG</tt> hash. The routine indicated by <tt>$SIG{__WARN__}</tt> is called when a warning message is about to be printed. The warning message is passed as the first argument. The presence of a <tt>&quot;__WARN__&quot;</tt> hook causes the ordinary printing of warnings to <tt>&quot;STDERR&quot;</tt> to be suppressed. You can use this to save warnings in a variable, or turn warnings into fatal errors, like this: </p>
<p>local $SIG{__WARN__} = sub{die $_[0]};<br />
eval $proggie;</p>
<p> As the <tt>'IGNORE'</tt> hook is not supported by <tt>&quot;__WARN__&quot;</tt>, you can disable warnings using the empty subroutine: </p>
<p>local $SIG{__WARN__} = sub{};</p>
<p> The routine indicated by <tt>$SIG{__DIE__}</tt> is called when a fatal exception is about to be thrown. The error message is passed as the first argument. When a <tt>&quot;__DIE__&quot;</tt> hook routine returns, the exception processing continues as it would have in the absence of the hook, unless the hook routine itself exits via a <tt>&quot;goto &amp;sub&quot;</tt>, a loop exit, or a <tt>&quot;die()&quot;</tt>. The <tt>&quot;__DIE__&quot;</tt> handler is explicitly disabled during the call, so that you can die from a <tt>&quot;__DIE__&quot;</tt> handler. Similarly for <tt>&quot;__WARN__&quot;</tt>. </p>
<p> The <tt>$SIG{__DIE__}</tt> hook is called even inside an <tt>&quot;eval()&quot;</tt>. It was never intended to happen this way, but an implementation glitch made this possible. This used to be deprecated, as it allowed strange action at a distance like rewriting a pending exception in <tt>$@</tt>. Plans to rectify this have been scrapped, as users found that rewriting a pending exception is actually a useful feature, and not a bug. </p>
<p> <tt>&quot;__DIE__&quot;</tt>/<tt>&quot;__WARN__&quot;</tt> handlers are very special in one respect: they may be called to report (probable) errors found by the parser. In such a case the parser may be in inconsistent state, so any attempt to evaluate Perl code from such a handler will probably result in a segfault. This means that warnings or errors that result from parsing Perl should be used with extreme caution, like this: </p>
<p>require Carp if defined $ ^ S;<br />
Carp::confess(&#8220;Something wrong&#8221;) if defined &amp;Carp::confess;<br />
die &#8220;Something wrong, but could not load Carp to give &#8221;<br />
    .&#8221;backtrace&#8230;
	&#8221;<br />
    .&#8221;To see backtrace try starting Perl with -MCarp switch&#8221;;</p>
<p> Here the first line will load <tt>&quot;Carp&quot;</tt> <i>unless</i> it is the parser who called the handler. The second line will print backtrace and die if <tt>&quot;Carp&quot;</tt> was available. The third line will be executed only if <tt>&quot;Carp&quot;</tt> was not available. </p>
<p> Having to even think about the <tt>$^S</tt> variable in your exception handlers is simply wrong. <tt>$SIG{__DIE__}</tt> as currently implemented invites grievous and difficult to track down errors. Avoid it and use an <tt>&quot;END{}&quot;</tt> or CORE::GLOBAL::die override instead. </p>
<p> See &#8220;die&#8221; in perlfunc, &#8220;warn&#8221; in perlfunc, &#8220;eval&#8221; in perlfunc, and warnings for additional information.</p>
<dt>$BASETIME</p>
<dd>
<dt>$^T</p>
<dd> The time at which the program began running, in seconds since the epoch (beginning of 1970). The values returned by the <code>-M</code>, <code>-A</code>, and <code>-C</code> filetests are based on this value.</p>
<dt>$PERL_VERSION</p>
<dd>
<dt>$^V</p>
<dd> The revision, version, and subversion of the Perl interpreter, represented as a version object. </p>
<p> This variable first appeared in perl v5.6.0; earlier versions of perl will see an undefined value. Before perl v5.10.0 <tt>$^V</tt> was represented as a v-string rather than a version object. </p>
<p> <tt>$^V</tt> can be used to determine whether the Perl interpreter executing a script is in the right range of versions. For example: </p>
<pre>
    warn &quot;Hashes not randomized!
&quot; if !$^V or $^V lt v5.8.1
</pre>
<p> While version objects overload stringification, to portably convert <tt>$^V</tt> into its string representation, use <tt>&quot;sprintf()&quot;</tt>&#8216;s <tt>&quot;%vd&quot;</tt> conversion, which works for both v-strings or version objects: </p>
<pre>
    printf &quot;version is v%vd
&quot;, $^V;  # Perl's version
</pre>
<p> See the documentation of <tt>&quot;use VERSION&quot;</tt> and <tt>&quot;require VERSION&quot;</tt> for a convenient way to fail if the running Perl interpreter is too old. </p>
<p> See also <tt>&quot;$]&quot;</tt> for a decimal representation of the Perl version. </p>
<p> The main advantage of <tt>$^V</tt> over <tt>$]</tt> is that, for Perl v5.10.0 or later, it overloads operators, allowing easy comparison against other version representations (e.g. decimal, literal v-string, &#8220;v1.2.3&#8221;, or objects). The disadvantage is that prior to v5.10.0, it was only a literal v-string, which can&#8217;t be easily printed or compared, whereas the behavior of <tt>$]</tt> is unchanged on all versions of Perl. </p>
<p> Mnemonic: use ^V for a version object.</p>
<dt>${^WIN32_SLOPPY_STAT}</p>
<dd> If this variable is set to a true value, then <tt>&quot;stat()&quot;</tt> on Windows will not try to open the file. This means that the link count cannot be determined and file attributes may be out of date if additional hardlinks to the file exist. On the other hand, not opening the file is considerably faster, especially for files on network drives. </p>
<p> This variable could be set in the <i>sitecustomize.pl</i> file to configure the local Perl installation to use &#8220;sloppy&#8221; <tt>&quot;stat()&quot;</tt> by default. See the documentation for <code>-f</code> in perlrun for more information about site customization. </p>
<p> This variable was added in Perl v5.10.0.</p>
<dt>$EXECUTABLE_NAME</p>
<dd>
<dt>$^X</p>
<dd> The name used to execute the current copy of Perl, from C&#8217;s <tt>&quot;argv[0]&quot;</tt> or (where supported) <i>/proc/self/exe</i>. </p>
<p> Depending on the host operating system, the value of <tt>$^X</tt> may be a relative or absolute pathname of the perl program file, or may be the string used to invoke perl but not the pathname of the perl program file. Also, most operating systems permit invoking programs that are not in the <font SIZE="-1">PATH</font> environment variable, so there is no guarantee that the value of <tt>$^X</tt> is in <font SIZE="-1">PATH.</font> For <font SIZE="-1">VMS,</font> the value may or may not include a version number. </p>
<p> You usually can use the value of <tt>$^X</tt> to re-invoke an independent copy of the same perl that is currently running, e.g., </p>
<pre>
    @first_run = `$^X -le &quot;print int rand 100 for 1..100&quot;`;
</pre>
<p> But recall that not all operating systems support forking or capturing of the output of commands, so this complex statement may not be portable. </p>
<p> It is not safe to use the value of <tt>$^X</tt> as a path name of a file, as some operating systems that have a mandatory suffix on executable files do not require use of the suffix when invoking a command. To convert the value of <tt>$^X</tt> to a path name, use the following statements: </p>
<p>#Build up a set of file names(not command names).<br />
use Config;<br />
my $this_perl = $ ^ X;<br />
if ($ ^ O ne &#8216;VMS&#8217;) {<br />
    $this_perl.= $Config{_exe} unless $this_perl = ~m / $Config{_exe} $ / i;<br />
}</p>
<p> Because many operating systems permit anyone with read access to the Perl program file to make a copy of it, patch the copy, and then execute the copy, the security-conscious Perl programmer should take care to invoke the installed copy of perl, not the copy referenced by <tt>$^X</tt>. The following statements accomplish this goal, and produce a pathname that can be invoked as a command or referenced as a file. </p>
<p>use Config;<br />
my $secure_perl_path = $Config{perlpath};<br />
if ($ ^ O ne &#8216;VMS&#8217;) {<br />
    $secure_perl_path.= $Config{_exe} unless $secure_perl_path = ~m / $Config{_exe} $ / i;<br />
}
</dl>
<h3>Variables related to regular expressions</h3>
<p> Most of the special variables related to regular expressions are side effects. Perl sets these variables when it has a successful match, so you should check the match result before using them. For instance: </p>
<p>if (/ P(A) TT(ER) N /) {<br />
    print &#8220;I found $1 and $2
&#8221;;<br />
}</p>
<p> These variables are read-only and dynamically-scoped, unless we note otherwise. </p>
<p> The dynamic nature of the regular expression variables means that their value is limited to the block that they are in, as demonstrated by this bit of code: </p>
<p>my $outer = &#8216;Wallace and Grommit&#8217;;<br />
my $inner = &#8216;Mutt and Jeff&#8217;;<br />
my $pattern = qr / (\S +) and (\S +) / ;<br />
sub show_n{print &#8220;\$1 is $1; \$2 is $2
&#8221;}<br />
{<br />
OUTER:<br />
    show_n() if $outer = ~m / $pattern / ;<br />
INNER : {<br />
    show_n() if $inner = ~m / $pattern / ;<br />
}<br />
    show_n();<br />
}</p>
<p> The output shows that while in the <tt>&quot;OUTER&quot;</tt> block, the values of <tt>$1</tt> and <tt>$2</tt> are from the match against <tt>$outer</tt>. Inside the <tt>&quot;INNER&quot;</tt> block, the values of <tt>$1</tt> and <tt>$2</tt> are from the match against <tt>$inner</tt>, but only until the end of the block (i.e. the dynamic scope). After the <tt>&quot;INNER&quot;</tt> block completes, the values of <tt>$1</tt> and <tt>$2</tt> return to the values for the match against <tt>$outer</tt> even though we have not made another match: </p>
<pre>
    $1 is Wallace; $2 is Grommit
    $1 is Mutt; $2 is Jeff
    $1 is Wallace; $2 is Grommit
</pre>
<p> <i>Performance issues</i> </p>
<p> Traditionally in Perl, any use of any of the three variables <tt>&quot;$`&quot;</tt>, <tt>$&amp;</tt> or <tt>&quot;$'&quot;</tt> (or their <tt>&quot;use English&quot;</tt> equivalents) anywhere in the code, caused all subsequent successful pattern matches to make a copy of the matched string, in case the code might subsequently access one of those variables. This imposed a considerable performance penalty across the whole program, so generally the use of these variables has been discouraged. </p>
<p> In Perl 5.6.0 the <tt>&quot;@-&quot;</tt> and <tt>&quot;@+&quot;</tt> dynamic arrays were introduced that supply the indices of successful matches. So you could for example do this: </p>
<p>$str = ~ / pattern / ;<br />
print $`, $ &amp;, $&#8217;; # bad: performance hit print #good : no performance hit substr($str, 0, $ &#8211; [0]),<br />
                                                        substr($str, $ &#8211; [0], $ + [0] &#8211; $ &#8211; [0]),<br />
                                                        substr($str, $ + [0]);</p>
<p> In Perl 5.10.0 the <tt>&quot;/p&quot;</tt> match operator flag and the <tt>&quot;${^PREMATCH}&quot;</tt>, <tt>&quot;${^MATCH}&quot;</tt>, and <tt>&quot;${^POSTMATCH}&quot;</tt> variables were introduced, that allowed you to suffer the penalties only on patterns marked with <tt>&quot;/p&quot;</tt>. </p>
<p> In Perl 5.18.0 onwards, perl started noting the presence of each of the three variables separately, and only copied that part of the string required; so in </p>
<pre>
    $`; $&amp;; &quot;abcdefgh&quot; =~ /d/
</pre>
<p> perl would only copy the &#8220;abcd&#8221; part of the string. That could make a big difference in something like </p>
<pre>
    $str = 'x' x 1_000_000;
    $&amp;; # whoops
    $str =~ /x/g # one char copied a million times, not a million chars
</pre>
<p> In Perl 5.20.0 a new copy-on-write system was enabled by default, which finally fixes all performance issues with these three variables, and makes them safe to use anywhere. </p>
<p> The <tt>&quot;Devel::NYTProf&quot;</tt> and <tt>&quot;Devel::FindAmpersand&quot;</tt> modules can help you find uses of these problematic match variables in your code.</p>
<dl>
<dt>$&lt;<i>digits</i>&gt; ($1, $2, &#8230;)</p>
<dd> Contains the subpattern from the corresponding set of capturing parentheses from the last successful pattern match, not counting patterns matched in nested blocks that have been exited already. </p>
<p> Note there is a distinction between a capture buffer which matches the empty string a capture buffer which is optional. Eg, <tt>&quot;(x?)&quot;</tt> and <tt>&quot;(x)?&quot;</tt> The latter may be undef, the former not. </p>
<p> These variables are read-only and dynamically-scoped. </p>
<p> Mnemonic: like \digits.</p>
<dt>@{^CAPTURE}</p>
<dd> An array which exposes the contents of the capture buffers, if any, of the last successful pattern match, not counting patterns matched in nested blocks that have been exited already. </p>
<p> Note that the 0 index of @{^CAPTURE} is equivalent to <tt>$1</tt>, the 1 index is equivalent to <tt>$2</tt>, etc. </p>
<p>if (&#8220;foal&#8221; = ~ / (.)(.)(.)(.) /) {<br />
    print join &#8220;-&#8220;, @{^CAPTURE};<br />
}</p>
<p> should output &#8220;f-o-a-l&#8221;. </p>
<p> See also &quot;$&lt;<i>digits</i>&gt; ($1, <tt>$2</tt>, &#8230;)&quot;, &#8220;%{^CAPTURE}&#8221; and &#8220;%{^CAPTURE_ALL}&#8221;. </p>
<p> Note that unlike most other regex magic variables there is no single letter equivalent to <tt>&quot;@{^CAPTURE}&quot;</tt>. </p>
<p> This variable was added in 5.25.7</p>
<dt>$MATCH</p>
<dd>
<dt>$&amp;</p>
<dd> The string matched by the last successful pattern match (not counting any matches hidden within a <font SIZE="-1">BLOCK</font> or <tt>&quot;eval()&quot;</tt> enclosed by the current <font SIZE="-1">BLOCK</font>). </p>
<p> See &#8220;Performance issues&#8221; above for the serious performance implications of using this variable (even once) in your code. </p>
<p> This variable is read-only and dynamically-scoped. </p>
<p> Mnemonic: like <tt>&quot;&amp;&quot;</tt> in some editors.</p>
<dt>${^MATCH}</p>
<dd> This is similar to <tt>$&amp;</tt> (<tt>$MATCH</tt>) except that it does not incur the performance penalty associated with that variable. </p>
<p> See &#8220;Performance issues&#8221; above. </p>
<p> In Perl v5.18 and earlier, it is only guaranteed to return a defined value when the pattern was compiled or executed with the <tt>&quot;/p&quot;</tt> modifier. In Perl v5.20, the <tt>&quot;/p&quot;</tt> modifier does nothing, so <tt>&quot;${^MATCH}&quot;</tt> does the same thing as <tt>$MATCH</tt>. </p>
<p> This variable was added in Perl v5.10.0. </p>
<p> This variable is read-only and dynamically-scoped.</p>
<dt>$PREMATCH</p>
<dd>
<dt>$`</p>
<dd> The string preceding whatever was matched by the last successful pattern match, not counting any matches hidden within a <font SIZE="-1">BLOCK</font> or <tt>&quot;eval&quot;</tt> enclosed by the current <font SIZE="-1">BLOCK.</font> </p>
<p> See &#8220;Performance issues&#8221; above for the serious performance implications of using this variable (even once) in your code. </p>
<p> This variable is read-only and dynamically-scoped. </p>
<p> Mnemonic: <tt>&quot;`&quot;</tt> often precedes a quoted string.</p>
<dt>${^PREMATCH}</p>
<dd> This is similar to <tt>&quot;$`&quot;</tt> ($PREMATCH) except that it does not incur the performance penalty associated with that variable. </p>
<p> See &#8220;Performance issues&#8221; above. </p>
<p> In Perl v5.18 and earlier, it is only guaranteed to return a defined value when the pattern was compiled or executed with the <tt>&quot;/p&quot;</tt> modifier. In Perl v5.20, the <tt>&quot;/p&quot;</tt> modifier does nothing, so <tt>&quot;${^PREMATCH}&quot;</tt> does the same thing as <tt>$PREMATCH</tt>. </p>
<p> This variable was added in Perl v5.10.0. </p>
<p> This variable is read-only and dynamically-scoped.</p>
<dt>$POSTMATCH</p>
<dd>
<dt>$&#8217;</p>
<dd> The string following whatever was matched by the last successful pattern match (not counting any matches hidden within a <font SIZE="-1">BLOCK</font> or <tt>&quot;eval()&quot;</tt> enclosed by the current <font SIZE="-1">BLOCK</font>). Example: </p>
<pre>
    local $_ = 'abcdefghi';
    /def/;
    print &quot;$`:$&amp;:$'
&quot;;         # prints abc:def:ghi
</pre>
<p> See &#8220;Performance issues&#8221; above for the serious performance implications of using this variable (even once) in your code. </p>
<p> This variable is read-only and dynamically-scoped. </p>
<p> Mnemonic: <tt>&quot;'&quot;</tt> often follows a quoted string.</p>
<dt>${^POSTMATCH}</p>
<dd> This is similar to <tt>&quot;$'&quot;</tt> (<tt>$POSTMATCH</tt>) except that it does not incur the performance penalty associated with that variable. </p>
<p> See &#8220;Performance issues&#8221; above. </p>
<p> In Perl v5.18 and earlier, it is only guaranteed to return a defined value when the pattern was compiled or executed with the <tt>&quot;/p&quot;</tt> modifier. In Perl v5.20, the <tt>&quot;/p&quot;</tt> modifier does nothing, so <tt>&quot;${^POSTMATCH}&quot;</tt> does the same thing as <tt>$POSTMATCH</tt>. </p>
<p> This variable was added in Perl v5.10.0. </p>
<p> This variable is read-only and dynamically-scoped.</p>
<dt>$LAST_PAREN_MATCH</p>
<dd>
<dt>$+</p>
<dd> The text matched by the highest used capture group of the last successful search pattern. It is logically equivalent to the highest numbered capture variable (<tt>$1</tt>, <tt>$2</tt>, &#8230;) which has a defined value. </p>
<p> This is useful if you don&#8217;t know which one of a set of alternative patterns matched. For example: </p>
<pre>
    /Version: (.*)|Revision: (.*)/ &amp;&amp; ($rev = $+);
</pre>
<p> This variable is read-only and dynamically-scoped. </p>
<p> Mnemonic: be positive and forward looking.</p>
<dt>$LAST_SUBMATCH_RESULT</p>
<dd>
<dt>$^N</p>
<dd> The text matched by the used group most-recently closed (i.e. the group with the rightmost closing parenthesis) of the last successful search pattern. This is subtly different from <tt>$+</tt>. For example in </p>
<pre>
    &quot;ab&quot; =~ /^((.)(.))$/
</pre>
<p> we have </p>
<pre>
    $1,$^N   have the value &quot;ab&quot;
    $2       has  the value &quot;a&quot;
    $3,$+    have the value &quot;b&quot;
</pre>
<p> This is primarily used inside <tt>&quot;(?{...})&quot;</tt> blocks for examining text recently matched. For example, to effectively capture text to a variable (in addition to <tt>$1</tt>, <tt>$2</tt>, etc.), replace <tt>&quot;(...)&quot;</tt> with </p>
<pre>
    (?:(...)(?{ $var = $^N }))
</pre>
<p> By setting and then using <tt>$var</tt> in this way relieves you from having to worry about exactly which numbered set of parentheses they are. </p>
<p> This variable was added in Perl v5.8.0. </p>
<p> Mnemonic: the (possibly) Nested parenthesis that most recently closed.</p>
<dt>@LAST_MATCH_END</p>
<dd>
<dt>@+</p>
<dd> This array holds the offsets of the ends of the last successful submatches in the currently active dynamic scope. <tt>$+[0]</tt> is the offset into the string of the end of the entire match. This is the same value as what the <tt>&quot;pos&quot;</tt> function returns when called on the variable that was matched against. The <i>n</i>th element of this array holds the offset of the <i>n</i>th submatch, so <tt>$+[1]</tt> is the offset past where <tt>$1</tt> ends, <tt>$+[2]</tt> the offset past where <tt>$2</tt> ends, and so on. You can use <tt>$#+</tt> to determine how many subgroups were in the last successful match. See the examples given for the <tt>&quot;@-&quot;</tt> variable. </p>
<p> This variable was added in Perl v5.6.0.</p>
<dt>%{^CAPTURE}</p>
<dd>
<dt>%LAST_PAREN_MATCH</p>
<dd>
<dt>%+</p>
<dd> Similar to <tt>&quot;@+&quot;</tt>, the <tt>&quot;%+&quot;</tt> hash allows access to the named capture buffers, should they exist, in the last successful match in the currently active dynamic scope. </p>
<p> For example, <tt>$+{foo}</tt> is equivalent to <tt>$1</tt> after the following match: </p>
<pre>
    'foo' =~ /(?&lt;foo&gt;foo)/;
</pre>
<p> The keys of the <tt>&quot;%+&quot;</tt> hash list only the names of buffers that have captured (and that are thus associated to defined values). </p>
<p> If multiple distinct capture groups have the same name, then <tt>$+{NAME}</tt> will refer to the leftmost defined group in the match. </p>
<p> The underlying behaviour of <tt>&quot;%+&quot;</tt> is provided by the Tie::Hash::NamedCapture module. </p>
<p> <code>Note:</code> <tt>&quot;%-&quot;</tt> and <tt>&quot;%+&quot;</tt> are tied views into a common internal hash associated with the last successful regular expression. Therefore mixing iterative access to them via <tt>&quot;each&quot;</tt> may have unpredictable results. Likewise, if the last successful match changes, then the results may be surprising. </p>
<p> This variable was added in Perl v5.10.0. The <tt>&quot;%{^CAPTURE}&quot;</tt> alias was added in 5.25.7. </p>
<p> This variable is read-only and dynamically-scoped.</p>
<dt>@LAST_MATCH_START</p>
<dd>
<dt>@-</p>
<dd> <tt>&quot;$-[0]&quot;</tt> is the offset of the start of the last successful match. <tt>&quot;$-[</tt>n<tt>]&quot;</tt> is the offset of the start of the substring matched by <i>n</i>-th subpattern, or undef if the subpattern did not match. </p>
<p> Thus, after a match against <tt>$_</tt>, <tt>$&amp;</tt> coincides with <tt>&quot;substr $_, $-[0], $+[0] - $-[0]&quot;</tt>. Similarly, $<i>n</i> coincides with <tt>&quot;substr $_, $-[n], $+[n] - $-[n]&quot;</tt> if <tt>&quot;$-[n]&quot;</tt> is defined, and $+ coincides with <tt>&quot;substr $_, $-[$#-], $+[$#-] - $-[$#-]&quot;</tt>. One can use <tt>&quot;$#-&quot;</tt> to find the last matched subgroup in the last successful match. Contrast with <tt>$#+</tt>, the number of subgroups in the regular expression. Compare with <tt>&quot;@+&quot;</tt>. </p>
<p> This array holds the offsets of the beginnings of the last successful submatches in the currently active dynamic scope. <tt>&quot;$-[0]&quot;</tt> is the offset into the string of the beginning of the entire match. The <i>n</i>th element of this array holds the offset of the <i>n</i>th submatch, so <tt>&quot;$-[1]&quot;</tt> is the offset where <tt>$1</tt> begins, <tt>&quot;$-[2]&quot;</tt> the offset where <tt>$2</tt> begins, and so on. </p>
<p> After a match against some variable <tt>$var</tt>:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&quot;$`&quot; is the same as &quot;substr($var, 0, $-[0])&quot;</p>
<dd>
<dt>$&amp; is the same as &quot;substr($var, $-[0], $+[0] &#8211; $-[0])&quot;</p>
<dd>
<dt>&quot;$&#8217;&quot; is the same as &quot;substr($var, $+[0])&quot;</p>
<dd>
<dt>$1 is the same as &quot;substr($var, $-[1], $+[1] &#8211; $-[1])&quot;</p>
<dd>
<dt>$2 is the same as &quot;substr($var, $-[2], $+[2] &#8211; $-[2])&quot;</p>
<dd>
<dt>$3 is the same as &quot;substr($var, $-[3], $+[3] &#8211; $-[3])&quot;</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> This variable was added in Perl v5.6.0.</dl>
<dt>%{^CAPTURE_ALL}</p>
<dd>
<dt>%-</p>
<dd> Similar to <tt>&quot;%+&quot;</tt>, this variable allows access to the named capture groups in the last successful match in the currently active dynamic scope. To each capture group name found in the regular expression, it associates a reference to an array containing the list of values captured by all buffers with that name (should there be several of them), in the order where they appear. </p>
<p> Here&#8217;s an example: </p>
<p>    if (&#8216;1234&#8217; =~ /(?&lt;A&gt;1)(?&lt;B&gt;2)(?&lt;A&gt;3)(?&lt;B&gt;4)/) {<br />
        foreach<br />
            my $bufname(sort keys % -)<br />
            {<br />
                my $ary = $ &#8211; {$bufname};<br />
                foreach<br />
                    my $idx(0.. $ #$ary)<br />
                    {<br />
                        print &#8220;\$-{$bufname}[$idx] : &#8220;,<br />
                            (defined($ary-&gt;[$idx])<br />
                                 ? &#8220;&#8216;$ary-&gt;[$idx]'&#8221;<br />
                                 : &#8220;undef&#8221;),<br />
                            &#8220;
&#8221;;<br />
                    }<br />
            }<br />
    }</p>
<p> would print out: </p>
<p>$ &#8211; {A}[0] : &#8216;1&#8217; $ &#8211; {A}[1] : &#8216;3&#8217; $ &#8211; {B}[0] : &#8216;2&#8217; $ &#8211; {B}[1] : &#8216;4&#8217;</p>
<p> The keys of the <tt>&quot;%-&quot;</tt> hash correspond to all buffer names found in the regular expression. </p>
<p> The behaviour of <tt>&quot;%-&quot;</tt> is implemented via the Tie::Hash::NamedCapture module. </p>
<p> <code>Note:</code> <tt>&quot;%-&quot;</tt> and <tt>&quot;%+&quot;</tt> are tied views into a common internal hash associated with the last successful regular expression. Therefore mixing iterative access to them via <tt>&quot;each&quot;</tt> may have unpredictable results. Likewise, if the last successful match changes, then the results may be surprising. </p>
<p> This variable was added in Perl v5.10.0. The <tt>&quot;%{^CAPTURE_ALL}&quot;</tt> alias was added in 5.25.7. </p>
<p> This variable is read-only and dynamically-scoped.</p>
<dt>$LAST_REGEXP_CODE_RESULT</p>
<dd>
<dt>$^R</p>
<dd> The result of evaluation of the last successful <tt>&quot;(?{ code })&quot;</tt> regular expression assertion (see perlre). May be written to. </p>
<p> This variable was added in Perl 5.005.</p>
<dt>${^RE_COMPILE_RECURSION_LIMIT}</p>
<dd> The current value giving the maximum number of open but unclosed parenthetical groups there may be at any point during a regular expression compilation. The default is currently 1000 nested groups. You may adjust it depending on your needs and the amount of memory available. </p>
<p> This variable was added in Perl v5.30.0.</p>
<dt>${^RE_DEBUG_FLAGS}</p>
<dd> The current value of the regex debugging flags. Set to 0 for no debug output even when the <tt>&quot;re 'debug'&quot;</tt> module is loaded. See re for details. </p>
<p> This variable was added in Perl v5.10.0.</p>
<dt>${^RE_TRIE_MAXBUF}</p>
<dd> Controls how certain regex optimisations are applied and how much memory they utilize. This value by default is 65536 which corresponds to a 512kB temporary cache. Set this to a higher value to trade memory for speed when matching large alternations. Set it to a lower value if you want the optimisations to be as conservative of memory as possible but still occur, and set it to a negative value to prevent the optimisation and conserve the most memory. Under normal situations this variable should be of no interest to you. </p>
<p> This variable was added in Perl v5.10.0.</dl>
<h3>Variables related to filehandles</h3>
<p> Variables that depend on the currently selected filehandle may be set by calling an appropriate object method on the <tt>&quot;IO::Handle&quot;</tt> object, although this is less efficient than using the regular built-in variables. (Summary lines below for this contain the word <font SIZE="-1">HANDLE.</font>) First you must say </p>
<pre>
    use IO::Handle;
</pre>
<p> after which you may use either </p>
<pre>
    method HANDLE EXPR
</pre>
<p> or more safely, </p>
<pre>
    HANDLE-&gt;method(EXPR)
</pre>
<p> Each method returns the old value of the <tt>&quot;IO::Handle&quot;</tt> attribute. The methods each take an optional <font SIZE="-1">EXPR,</font> which, if supplied, specifies the new value for the <tt>&quot;IO::Handle&quot;</tt> attribute in question. If not supplied, most methods do nothing to the current value&#8212;except for <tt>&quot;autoflush()&quot;</tt>, which will assume a 1 for you, just to be different. </p>
<p> Because loading in the <tt>&quot;IO::Handle&quot;</tt> class is an expensive operation, you should learn how to use the regular built-in variables. </p>
<p> A few of these variables are considered &#8220;read-only&#8221;. This means that if you try to assign to this variable, either directly or indirectly through a reference, you&#8217;ll raise a run-time exception. </p>
<p> You should be very careful when modifying the default values of most special variables described in this document. In most cases you want to localize these variables before changing them, since if you don&#8217;t, the change may affect other modules which rely on the default values of the special variables that you have changed. This is one of the correct ways to read the whole file at once: </p>
<p>open my $fh, &#8220;&lt;&#8220;, &#8220;foo&#8221; or die $ !;<br />
local $ / ;<br />
#enable localized slurp mode<br />
    my $content = &lt; $fh&gt;;<br />
close $fh;</p>
<p> But the following code is quite bad: </p>
<p>open my $fh, &#8220;&lt;&#8220;, &#8220;foo&#8221; or die $ !;<br />
undef $ / ;<br />
#enable slurp mode<br />
    my $content = &lt; $fh&gt;;<br />
close $fh;</p>
<p> since some other module, may want to read data from some file in the default &#8220;line mode&#8221;, so if the code we have just presented has been executed, the global value of <tt>$/</tt> is now changed for any other code running inside the same Perl interpreter. </p>
<p> Usually when a variable is localized you want to make sure that this change affects the shortest scope possible. So unless you are already inside some short <tt>&quot;{}&quot;</tt> block, you should create one yourself. For example: </p>
<p>my $content = &#8221;;<br />
open my $fh, &#8220;&lt;&#8220;, &#8220;foo&#8221; or die $ !;<br />
{<br />
    local $ / ;<br />
    $content = &lt;$fh&gt;;<br />
}<br />
close $fh;</p>
<p> Here is an example of how your own code can go broken: </p>
<p>for (1..3) {<br />
    $\ = &#8220;
&#8221;;<br />
    nasty_break();<br />
    print &#8220;$_&#8221;;<br />
}<br />
sub nasty_break<br />
{<br />
    $\ = &#8220;&#8221;;<br />
#do something with $_<br />
}</p>
<p> You probably expect this code to print the equivalent of </p>
<pre>
    &quot;1
2
3
&quot;
</pre>
<p> but instead you get: </p>
<pre>
    &quot;123&quot;
</pre>
<p> Why? Because <tt>&quot;nasty_break()&quot;</tt> modifies <tt>&quot;$\&quot;</tt> without localizing it first. The value you set in <tt>&quot;nasty_break()&quot;</tt> is still there when you return. The fix is to add <tt>&quot;local()&quot;</tt> so the value doesn&#8217;t leak out of <tt>&quot;nasty_break()&quot;</tt>: </p>
<pre>
    local $\ = &quot;&quot;;
</pre>
<p> It&#8217;s easy to notice the problem in such a short example, but in more complicated code you are looking for trouble if you don&#8217;t localize changes to the special variables.</p>
<dl>
<dt>$ARGV</p>
<dd> Contains the name of the current file when reading from <tt>&quot;&lt;&gt;&quot;</tt>.</p>
<dt>@ARGV</p>
<dd> The array <tt>@ARGV</tt> contains the command-line arguments intended for the script. <tt>$#ARGV</tt> is generally the number of arguments minus one, because <tt>$ARGV[0]</tt> is the first argument, <i>not</i> the program&#8217;s command name itself. See &#8220;$0&#8221; for the command name.</p>
<dt><font SIZE="-1">ARGV</font></p>
<dd> The special filehandle that iterates over command-line filenames in <tt>@ARGV</tt>. Usually written as the null filehandle in the angle operator <tt>&quot;&lt;&gt;&quot;</tt>. Note that currently <tt>&quot;ARGV&quot;</tt> only has its magical effect within the <tt>&quot;&lt;&gt;&quot;</tt> operator; elsewhere it is just a plain filehandle corresponding to the last file opened by <tt>&quot;&lt;&gt;&quot;</tt>. In particular, passing <tt>&quot;\*ARGV&quot;</tt> as a parameter to a function that expects a filehandle may not cause your function to automatically read the contents of all the files in <tt>@ARGV</tt>.</p>
<dt><font SIZE="-1">ARGVOUT</font></p>
<dd> The special filehandle that points to the currently open output file when doing edit-in-place processing with <code>-i</code>. Useful when you have to do a lot of inserting and don&#8217;t want to keep modifying <tt>$_</tt>. See perlrun for the <code>-i</code> switch.</p>
<dt>IO::Handle-&gt;output_field_separator( <font SIZE="-1">EXPR</font> )</p>
<dd>
<dt>$OUTPUT_FIELD_SEPARATOR</p>
<dd>
<dt>$OFS</p>
<dd>
<dt>$,</p>
<dd> The output field separator for the print operator. If defined, this value is printed between each of print&#8217;s arguments. Default is <tt>&quot;undef&quot;</tt>. </p>
<p> You cannot call <tt>&quot;output_field_separator()&quot;</tt> on a handle, only as a static method. See IO::Handle. </p>
<p> Mnemonic: what is printed when there is a &#8220;,&#8221; in your print statement.</p>
<dt><font SIZE="-1">HANDLE-</font>&gt;input_line_number( <font SIZE="-1">EXPR</font> )</p>
<dd>
<dt>$INPUT_LINE_NUMBER</p>
<dd>
<dt>$NR</p>
<dd>
<dt>$.</p>
<dd> Current line number for the last filehandle accessed. </p>
<p> Each filehandle in Perl counts the number of lines that have been read from it. (Depending on the value of <tt>$/</tt>, Perl&#8217;s idea of what constitutes a line may not match yours.) When a line is read from a filehandle (via <tt>&quot;readline()&quot;</tt> or <tt>&quot;&lt;&gt;&quot;</tt>), or when <tt>&quot;tell()&quot;</tt> or <tt>&quot;seek()&quot;</tt> is called on it, <tt>$.</tt> becomes an alias to the line counter for that filehandle. </p>
<p> You can adjust the counter by assigning to <tt>$.</tt>, but this will not actually move the seek pointer. <i>Localizing </i>$.<i> will not localize the filehandle&#8217;s line count</i>. Instead, it will localize perl&#8217;s notion of which filehandle <tt>$.</tt> is currently aliased to. </p>
<p> <tt>$.</tt> is reset when the filehandle is closed, but <code>not</code> when an open filehandle is reopened without an intervening <tt>&quot;close()&quot;</tt>. For more details, see &#8220;I/O Operators&#8221; in perlop. Because <tt>&quot;&lt;&gt;&quot;</tt> never does an explicit close, line numbers increase across <tt>&quot;ARGV&quot;</tt> files (but see examples in &#8220;eof&#8221; in perlfunc). </p>
<p> You can also use <tt>&quot;HANDLE-&gt;input_line_number(EXPR)&quot;</tt> to access the line counter for a given filehandle without having to worry about which handle you last accessed. </p>
<p> Mnemonic: many programs use &#8220;.&#8221; to mean the current line number.</p>
<dt>IO::Handle-&gt;input_record_separator( <font SIZE="-1">EXPR</font> )</p>
<dd>
<dt>$INPUT_RECORD_SEPARATOR</p>
<dd>
<dt>$RS</p>
<dd>
<dt>$/</p>
<dd> The input record separator, newline by default. This influences Perl&#8217;s idea of what a &#8220;line&#8221; is. Works like <code>awk</code>&#8216;s <font SIZE="-1">RS</font> variable, including treating empty lines as a terminator if set to the null string (an empty line cannot contain any spaces or tabs). You may set it to a multi-character string to match a multi-character terminator, or to <tt>&quot;undef&quot;</tt> to read through the end of file. Setting it to <tt>&quot;

&quot;</tt> means something slightly different than setting to <tt>&quot;&quot;</tt>, if the file contains consecutive empty lines. Setting to <tt>&quot;&quot;</tt> will treat two or more consecutive empty lines as a single empty line. Setting to <tt>&quot;

&quot;</tt> will blindly assume that the next input character belongs to the next paragraph, even if it&#8217;s a newline. </p>
<p>local $ / ;<br />
#enable &#8220;slurp&#8221; mode<br />
    local $_ = &lt; FH&gt;;<br />
#whole file now here<br />
        s /
[ 	] + / / g;</p>
<p> Remember: the value of <tt>$/</tt> is a string, not a regex. <code>awk</code> has to be better for something. :-) </p>
<p> Setting <tt>$/</tt> to an empty string &#8212; the so-called <i>paragraph mode</i> &#8212; merits special attention. When <tt>$/</tt> is set to <tt>&quot;&quot;</tt> and the entire file is read in with that setting, any sequence of consecutive newlines <tt>&quot;

&quot;</tt> at the beginning of the file is discarded. With the exception of the final record in the file, each sequence of characters ending in two or more newlines is treated as one record and is read in to end in exactly two newlines. If the last record in the file ends in zero or one consecutive newlines, that record is read in with that number of newlines. If the last record ends in two or more consecutive newlines, it is read in with two newlines like all preceding records. </p>
<p> Suppose we wrote the following string to a file: </p>
<p>my $string = &#8220;


&#8221;;<br />
$string.= &#8220;alpha beta
gamma delta


&#8221;;<br />
$string.= &#8220;epsilon zeta eta

&#8221;;<br />
$string.= &#8220;theta
&#8221;;<br />
my $file = &#8216;simple_file.txt&#8217;;<br />
open my $OUT, &#8216;&gt;&#8217;, $file or die;<br />
print $OUT $string;<br />
close $OUT or die;</p>
<p> Now we read that file in paragraph mode: </p>
<p>local $ / = &#8220;&#8221;;<br />
#paragraph mode<br />
    open my $IN,<br />
    &#8216;&lt;&#8216;, $file or die;<br />
my @records = &lt;$IN&gt;;<br />
close $IN or die;</p>
<p> <tt>@records</tt> will consist of these 3 strings: </p>
<pre>
    (
      &quot;alpha beta
gamma delta

&quot;,
      &quot;epsilon zeta eta

&quot;,
      &quot;theta
&quot;,
    )
</pre>
<p> Setting <tt>$/</tt> to a reference to an integer, scalar containing an integer, or scalar that&#8217;s convertible to an integer will attempt to read records instead of lines, with the maximum record size being the referenced integer number of characters. So this: </p>
<pre>
    local $/ = \32768; # or \&quot;32768&quot;, or \$var_containing_32768
    open my $fh, &quot;&lt;&quot;, $myfile or die $!;
    local $_ = &lt;$fh&gt;;
</pre>
<p> will read a record of no more than 32768 characters from <tt>$fh</tt>. If you&#8217;re not reading from a record-oriented file (or your <font SIZE="-1">OS</font> doesn&#8217;t have record-oriented files), then you&#8217;ll likely get a full chunk of data with every read. If a record is larger than the record size you&#8217;ve set, you&#8217;ll get the record back in pieces. Trying to set the record size to zero or less is deprecated and will cause $/ to have the value of &#8220;undef&#8221;, which will cause reading in the (rest of the) whole file. </p>
<p> As of 5.19.9 setting <tt>$/</tt> to any other form of reference will throw a fatal exception. This is in preparation for supporting new ways to set <tt>$/</tt> in the future. </p>
<p> On <font SIZE="-1">VMS</font> only, record reads bypass PerlIO layers and any associated buffering, so you must not mix record and non-record reads on the same filehandle. Record mode mixes with line mode only when the same buffering layer is in use for both modes. </p>
<p> You cannot call <tt>&quot;input_record_separator()&quot;</tt> on a handle, only as a static method. See IO::Handle. </p>
<p> See also &#8220;Newlines&#8221; in perlport. Also see &#8220;$.&#8221;. </p>
<p> Mnemonic: / delimits line boundaries when quoting poetry.</p>
<dt>IO::Handle-&gt;output_record_separator( <font SIZE="-1">EXPR</font> )</p>
<dd>
<dt>$OUTPUT_RECORD_SEPARATOR</p>
<dd>
<dt>$ORS</p>
<dd>
<dt>$\</p>
<dd> The output record separator for the print operator. If defined, this value is printed after the last of print&#8217;s arguments. Default is <tt>&quot;undef&quot;</tt>. </p>
<p> You cannot call <tt>&quot;output_record_separator()&quot;</tt> on a handle, only as a static method. See IO::Handle. </p>
<p> Mnemonic: you set <tt>&quot;$\&quot;</tt> instead of adding &#8220;
&#8221; at the end of the print. Also, it&#8217;s just like <tt>$/</tt>, but it&#8217;s what you get &#8220;back&#8221; from Perl.</p>
<dt><font SIZE="-1">HANDLE-</font>&gt;autoflush( <font SIZE="-1">EXPR</font> )</p>
<dd>
<dt>$OUTPUT_AUTOFLUSH</p>
<dd>
<dt>$|</p>
<dd> If set to nonzero, forces a flush right away and after every write or print on the currently selected output channel. Default is 0 (regardless of whether the channel is really buffered by the system or not; <tt>$|</tt> tells you only whether you&#8217;ve asked Perl explicitly to flush after each write). <font SIZE="-1">STDOUT</font> will typically be line buffered if output is to the terminal and block buffered otherwise. Setting this variable is useful primarily when you are outputting to a pipe or socket, such as when you are running a Perl program under <code>rsh</code> and want to see the output as it&#8217;s happening. This has no effect on input buffering. See &#8220;getc&#8221; in perlfunc for that. See &#8220;select&#8221; in perlfunc on how to select the output channel. See also IO::Handle. </p>
<p> Mnemonic: when you want your pipes to be piping hot.</p>
<dt>${^LAST_FH}</p>
<dd> This read-only variable contains a reference to the last-read filehandle. This is set by <tt>&quot;&lt;HANDLE&gt;&quot;</tt>, <tt>&quot;readline&quot;</tt>, <tt>&quot;tell&quot;</tt>, <tt>&quot;eof&quot;</tt> and <tt>&quot;seek&quot;</tt>. This is the same handle that <tt>$.</tt> and <tt>&quot;tell&quot;</tt> and <tt>&quot;eof&quot;</tt> without arguments use. It is also the handle used when Perl appends &#8220;, &lt;<font SIZE="-1">STDIN</font>&gt; line 1&#8221; to an error or warning message. </p>
<p> This variable was added in Perl v5.18.0.</dl>
<p> <i>Variables related to formats</i> </p>
<p> The special variables for formats are a subset of those for filehandles. See perlform for more information about Perl&#8217;s formats.</p>
<dl>
<dt>$ACCUMULATOR</p>
<dd>
<dt>$^A</p>
<dd> The current value of the <tt>&quot;write()&quot;</tt> accumulator for <tt>&quot;format()&quot;</tt> lines. A format contains <tt>&quot;formline()&quot;</tt> calls that put their result into <tt>$^A</tt>. After calling its format, <tt>&quot;write()&quot;</tt> prints out the contents of <tt>$^A</tt> and empties. So you never really see the contents of <tt>$^A</tt> unless you call <tt>&quot;formline()&quot;</tt> yourself and then look at it. See perlform and &#8220;formline <font SIZE="-1">PICTURE,LIST&#8221;</font> in perlfunc.</p>
<dt>IO::Handle-&gt;format_formfeed(<font SIZE="-1">EXPR</font>)</p>
<dd>
<dt>$FORMAT_FORMFEED</p>
<dd>
<dt>$^L</p>
<dd> What formats output as a form feed. The default is <tt>&quot;&quot;</tt>. </p>
<p> You cannot call <tt>&quot;format_formfeed()&quot;</tt> on a handle, only as a static method. See IO::Handle.</p>
<dt><font SIZE="-1">HANDLE-</font>&gt;format_page_number(<font SIZE="-1">EXPR</font>)</p>
<dd>
<dt>$FORMAT_PAGE_NUMBER</p>
<dd>
<dt>$%</p>
<dd> The current page number of the currently selected output channel. </p>
<p> Mnemonic: <tt>&quot;%&quot;</tt> is page number in <code>nroff</code>.</p>
<dt><font SIZE="-1">HANDLE-</font>&gt;format_lines_left(<font SIZE="-1">EXPR</font>)</p>
<dd>
<dt>$FORMAT_LINES_LEFT</p>
<dd>
<dt>$-</p>
<dd> The number of lines left on the page of the currently selected output channel. </p>
<p> Mnemonic: lines_on_page &#8211; lines_printed.</p>
<dt>IO::Handle-&gt;format_line_break_characters <font SIZE="-1">EXPR</font></p>
<dd>
<dt>$FORMAT_LINE_BREAK_CHARACTERS</p>
<dd>
<dt>$:</p>
<dd> The current set of characters after which a string may be broken to fill continuation fields (starting with <tt>&quot;^&quot;</tt>) in a format. The default is &#8220; 
-&#8221;, to break on a space, newline, or a hyphen. </p>
<p> You cannot call <tt>&quot;format_line_break_characters()&quot;</tt> on a handle, only as a static method. See IO::Handle. </p>
<p> Mnemonic: a &#8220;colon&#8221; in poetry is a part of a line.</p>
<dt><font SIZE="-1">HANDLE-</font>&gt;format_lines_per_page(<font SIZE="-1">EXPR</font>)</p>
<dd>
<dt>$FORMAT_LINES_PER_PAGE</p>
<dd>
<dt>$=</p>
<dd> The current page length (printable lines) of the currently selected output channel. The default is 60. </p>
<p> Mnemonic: = has horizontal lines.</p>
<dt><font SIZE="-1">HANDLE-</font>&gt;format_top_name(<font SIZE="-1">EXPR</font>)</p>
<dd>
<dt>$FORMAT_TOP_NAME</p>
<dd>
<dt>$^</p>
<dd> The name of the current top-of-page format for the currently selected output channel. The default is the name of the filehandle with <tt>&quot;_TOP&quot;</tt> appended. For example, the default format top name for the <tt>&quot;STDOUT&quot;</tt> filehandle is <tt>&quot;STDOUT_TOP&quot;</tt>. </p>
<p> Mnemonic: points to top of page.</p>
<dt><font SIZE="-1">HANDLE-</font>&gt;format_name(<font SIZE="-1">EXPR</font>)</p>
<dd>
<dt>$FORMAT_NAME</p>
<dd>
<dt>$~</p>
<dd> The name of the current report format for the currently selected output channel. The default format name is the same as the filehandle name. For example, the default format name for the <tt>&quot;STDOUT&quot;</tt> filehandle is just <tt>&quot;STDOUT&quot;</tt>. </p>
<p> Mnemonic: brother to <tt>$^</tt>.</dl>
<h3>Error Variables</h3>
<p> The variables <tt>$@</tt>, <tt>$!</tt>, <tt>$^E</tt>, and <tt>$?</tt> contain information about different types of error conditions that may appear during execution of a Perl program. The variables are shown ordered by the &#8220;distance&#8221; between the subsystem which reported the error and the Perl process. They correspond to errors detected by the Perl interpreter, C library, operating system, or an external program, respectively. </p>
<p> To illustrate the differences between these variables, consider the following Perl expression, which uses a single-quoted string. After execution of this statement, perl may have set all four special error variables: </p>
<p>eval q<br />
{<br />
    open my $pipe, &#8220;/cdrom/install |&#8221; or die $ !;<br />
    my @res = &lt;$pipe&gt;;<br />
    close $pipe or die &#8220;bad pipe: $?, $!&#8221;;<br />
};</p>
<p> When perl executes the <tt>&quot;eval()&quot;</tt> expression, it translates the <tt>&quot;open()&quot;</tt>, <tt>&quot;&lt;PIPE&gt;&quot;</tt>, and <tt>&quot;close&quot;</tt> calls in the C run-time library and thence to the operating system kernel. perl sets <tt>$!</tt> to the C library&#8217;s <tt>&quot;errno&quot;</tt> if one of these calls fails. </p>
<p> <tt>$@</tt> is set if the string to be <tt>&quot;eval&quot;</tt>-ed did not compile (this may happen if <tt>&quot;open&quot;</tt> or <tt>&quot;close&quot;</tt> were imported with bad prototypes), or if Perl code executed during evaluation <tt>&quot;die()&quot;</tt>d. In these cases the value of <tt>$@</tt> is the compile error, or the argument to <tt>&quot;die&quot;</tt> (which will interpolate <tt>$!</tt> and <tt>$?</tt>). (See also Fatal, though.) </p>
<p> Under a few operating systems, <tt>$^E</tt> may contain a more verbose error indicator, such as in this case, &#8220;<font SIZE="-1">CDROM</font> tray not closed.&#8221; Systems that do not support extended error messages leave <tt>$^E</tt> the same as <tt>$!</tt>. </p>
<p> Finally, <tt>$?</tt> may be set to a non-0 value if the external program <i>/cdrom/install</i> fails. The upper eight bits reflect specific error conditions encountered by the program (the program&#8217;s <tt>&quot;exit()&quot;</tt> value). The lower eight bits reflect mode of failure, like signal death and core dump information. See <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2) for details. In contrast to <tt>$!</tt> and <tt>$^E</tt>, which are set only if an error condition is detected, the variable <tt>$?</tt> is set on each <tt>&quot;wait&quot;</tt> or pipe <tt>&quot;close&quot;</tt>, overwriting the old value. This is more like <tt>$@</tt>, which on every <tt>&quot;eval()&quot;</tt> is always set on failure and cleared on success. </p>
<p> For more details, see the individual descriptions at <tt>$@</tt>, <tt>$!</tt>, <tt>$^E</tt>, and <tt>$?</tt>.</p>
<dl>
<dt>${^CHILD_ERROR_NATIVE}</p>
<dd> The native status returned by the last pipe close, backtick (<tt>&quot;``&quot;</tt>) command, successful call to <tt>&quot;wait()&quot;</tt> or <tt>&quot;waitpid()&quot;</tt>, or from the <tt>&quot;system()&quot;</tt> operator. On POSIX-like systems this value can be decoded with the <font SIZE="-1">WIFEXITED, WEXITSTATUS, WIFSIGNALED, WTERMSIG, WIFSTOPPED, WSTOPSIG</font> and <font SIZE="-1">WIFCONTINUED</font> functions provided by the <font SIZE="-1">POSIX</font> module. </p>
<p> Under <font SIZE="-1">VMS</font> this reflects the actual <font SIZE="-1">VMS</font> exit status; i.e. it is the same as <tt>$?</tt> when the pragma <tt>&quot;use vmsish 'status'&quot;</tt> is in effect. </p>
<p> This variable was added in Perl v5.10.0.</p>
<dt>$EXTENDED_OS_ERROR</p>
<dd>
<dt>$^E</p>
<dd> Error information specific to the current operating system. At the moment, this differs from <tt>&quot;$!&quot;</tt> under only <font SIZE="-1">VMS, OS/2,</font> and Win32 (and for MacPerl). On all other platforms, <tt>$^E</tt> is always just the same as <tt>$!</tt>. </p>
<p> Under <font SIZE="-1">VMS,</font> <tt>$^E</tt> provides the <font SIZE="-1">VMS</font> status value from the last system error. This is more specific information about the last system error than that provided by <tt>$!</tt>. This is particularly important when <tt>$!</tt> is set to <font SIZE="-1"><code>EVMSERR</code></font>. </p>
<p> Under <font SIZE="-1">OS/2,</font> <tt>$^E</tt> is set to the error code of the last call to <font SIZE="-1">OS/2 API</font> either via <font SIZE="-1">CRT,</font> or directly from perl. </p>
<p> Under Win32, <tt>$^E</tt> always returns the last error information reported by the Win32 call <tt>&quot;GetLastError()&quot;</tt> which describes the last error from within the Win32 <font SIZE="-1">API.</font> Most Win32-specific code will report errors via <tt>$^E</tt>. <font SIZE="-1">ANSI C</font> and Unix-like calls set <tt>&quot;errno&quot;</tt> and so most portable Perl code will report errors via <tt>$!</tt>. </p>
<p> Caveats mentioned in the description of <tt>&quot;$!&quot;</tt> generally apply to <tt>$^E</tt>, also. </p>
<p> This variable was added in Perl 5.003. </p>
<p> Mnemonic: Extra error explanation.</p>
<dt>$EXCEPTIONS_BEING_CAUGHT</p>
<dd>
<dt>$^S</p>
<dd> Current state of the interpreter. </p>
<p>$ ^ S State&#8211; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -undef Parsing module, eval, or main program true(1) Executing an eval<br />
                                                                                                                false(0) Otherwise</p>
<p> The first state may happen in <tt>$SIG{__DIE__}</tt> and <tt>$SIG{__WARN__}</tt> handlers. </p>
<p> The English name <tt>$EXCEPTIONS_BEING_CAUGHT</tt> is slightly misleading, because the <tt>&quot;undef&quot;</tt> value does not indicate whether exceptions are being caught, since compilation of the main program does not catch exceptions. </p>
<p> This variable was added in Perl 5.004.</p>
<dt>$WARNING</p>
<dd>
<dt>$^W</p>
<dd> The current value of the warning switch, initially true if <code>-w</code> was used, false otherwise, but directly modifiable. </p>
<p> See also warnings. </p>
<p> Mnemonic: related to the <code>-w</code> switch.</p>
<dt>${^WARNING_BITS}</p>
<dd> The current set of warning checks enabled by the <tt>&quot;use warnings&quot;</tt> pragma. It has the same scoping as the <tt>$^H</tt> and <tt>&quot;%^H&quot;</tt> variables. The exact values are considered internal to the warnings pragma and may change between versions of Perl. </p>
<p> This variable was added in Perl v5.6.0.</p>
<dt>$OS_ERROR</p>
<dd>
<dt>$ERRNO</p>
<dd>
<dt>$!</p>
<dd> When referenced, <tt>$!</tt> retrieves the current value of the C <tt>&quot;errno&quot;</tt> integer variable. If <tt>$!</tt> is assigned a numerical value, that value is stored in <tt>&quot;errno&quot;</tt>. When referenced as a string, <tt>$!</tt> yields the system error string corresponding to <tt>&quot;errno&quot;</tt>. </p>
<p> Many system or library calls set <tt>&quot;errno&quot;</tt> if they fail, to indicate the cause of failure. They usually do <code>not</code> set <tt>&quot;errno&quot;</tt> to zero if they succeed. This means <tt>&quot;errno&quot;</tt>, hence <tt>$!</tt>, is meaningful only <i>immediately</i> after a <code>failure</code>: </p>
<p>if (open my $fh, &#8220;&lt;&#8220;, $filename) {<br />
#Here $ !is meaningless.<br />
    &#8230;<br />
} else {<br />
#ONLY here is $ !meaningful.<br />
    &#8230;<br />
#Already here $ !might be meaningless.<br />
}<br />
#Since here we might have either success or failure,<br />
#$ !is meaningless.</p>
<p> Here, <i>meaningless</i> means that <tt>$!</tt> may be unrelated to the outcome of the <tt>&quot;open()&quot;</tt> operator. Assignment to <tt>$!</tt> is similarly ephemeral. It can be used immediately before invoking the <tt>&quot;die()&quot;</tt> operator, to set the exit value, or to inspect the system error string corresponding to error <i>n</i>, or to restore <tt>$!</tt> to a meaningful state. </p>
<p> Mnemonic: What just went bang?</p>
<dt>%OS_ERROR</p>
<dd>
<dt>%ERRNO</p>
<dd>
<dt>%!</p>
<dd> Each element of <tt>&quot;%!&quot;</tt> has a true value only if <tt>$!</tt> is set to that value. For example, <tt>$!{ENOENT}</tt> is true if and only if the current value of <tt>$!</tt> is <tt>&quot;ENOENT&quot;</tt>; that is, if the most recent error was &#8220;No such file or directory&#8221; (or its moral equivalent: not all operating systems give that exact error, and certainly not all languages). The specific true value is not guaranteed, but in the past has generally been the numeric value of <tt>$!</tt>. To check if a particular key is meaningful on your system, use <tt>&quot;exists $!{the_key}&quot;</tt>; for a list of legal keys, use <tt>&quot;keys %!&quot;</tt>. See Errno for more information, and also see &#8220;$!&#8221;. </p>
<p> This variable was added in Perl 5.005.</p>
<dt>$CHILD_ERROR</p>
<dd>
<dt>$?</p>
<dd> The status returned by the last pipe close, backtick (<tt>&quot;``&quot;</tt>) command, successful call to <tt>&quot;wait()&quot;</tt> or <tt>&quot;waitpid()&quot;</tt>, or from the <tt>&quot;system()&quot;</tt> operator. This is just the 16-bit status word returned by the traditional Unix <tt>&quot;wait()&quot;</tt> system call (or else is made up to look like it). Thus, the exit value of the subprocess is really (<tt>&quot;$? &gt;&gt; 8&quot;</tt>), and <tt>&quot;$? &amp; 127&quot;</tt> gives which signal, if any, the process died from, and <tt>&quot;$? &amp; 128&quot;</tt> reports whether there was a core dump. </p>
<p> Additionally, if the <tt>&quot;h_errno&quot;</tt> variable is supported in C, its value is returned via <tt>$?</tt> if any <tt>&quot;gethost*()&quot;</tt> function fails. </p>
<p> If you have installed a signal handler for <tt>&quot;SIGCHLD&quot;</tt>, the value of <tt>$?</tt> will usually be wrong outside that handler. </p>
<p> Inside an <tt>&quot;END&quot;</tt> subroutine <tt>$?</tt> contains the value that is going to be given to <tt>&quot;exit()&quot;</tt>. You can modify <tt>$?</tt> in an <tt>&quot;END&quot;</tt> subroutine to change the exit status of your program. For example: </p>
<p>END<br />
{<br />
    $ ? = 1 if $ ? == 255;<br />
#die would make it 255<br />
}</p>
<p> Under <font SIZE="-1">VMS,</font> the pragma <tt>&quot;use vmsish 'status'&quot;</tt> makes <tt>$?</tt> reflect the actual <font SIZE="-1">VMS</font> exit status, instead of the default emulation of <font SIZE="-1">POSIX</font> status; see &#8220;$?&#8221; in perlvms for details. </p>
<p> Mnemonic: similar to <code>sh</code> and <code>ksh</code>.</p>
<dt>$EVAL_ERROR</p>
<dd>
<dt>$@</p>
<dd> The Perl error from the last <tt>&quot;eval&quot;</tt> operator, i.e. the last exception that was caught. For <tt>&quot;eval BLOCK&quot;</tt>, this is either a runtime error message or the string or reference <tt>&quot;die&quot;</tt> was called with. The <tt>&quot;eval STRING&quot;</tt> form also catches syntax errors and other compile time exceptions. </p>
<p> If no error occurs, <tt>&quot;eval&quot;</tt> sets <tt>$@</tt> to the empty string. </p>
<p> Warning messages are not collected in this variable. You can, however, set up a routine to process warnings by setting <tt>$SIG{__WARN__}</tt> as described in &#8220;%SIG&#8221;. </p>
<p> Mnemonic: Where was the error &#8220;at&#8221;?</dl>
<h3>Variables related to the interpreter state</h3>
<p> These variables provide information about the current interpreter state.</p>
<dl>
<dt>$COMPILING</p>
<dd>
<dt>$^C</p>
<dd> The current value of the flag associated with the <code>-c</code> switch. Mainly of use with <code>-MO=&#8230;</code> to allow code to alter its behavior when being compiled, such as for example to <tt>&quot;AUTOLOAD&quot;</tt> at compile time rather than normal, deferred loading. Setting <tt>&quot;$^C = 1&quot;</tt> is similar to calling <tt>&quot;B::minus_c&quot;</tt>. </p>
<p> This variable was added in Perl v5.6.0.</p>
<dt>$DEBUGGING</p>
<dd>
<dt>$^D</p>
<dd> The current value of the debugging flags. May be read or set. Like its command-line equivalent, you can use numeric or symbolic values, e.g. <tt>&quot;$^D = 10&quot;</tt> or <tt>&quot;$^D = &quot;st&quot;&quot;</tt>. See &quot;<code>-D</code><i>number</i>&quot; in perlrun. The contents of this variable also affects the debugger operation. See &#8220;Debugger Internals&#8221; in perldebguts. </p>
<p> Mnemonic: value of <code>-D</code> switch.</p>
<dt>${^ENCODING}</p>
<dd> This variable is no longer supported. </p>
<p> It used to hold the <i>object reference</i> to the <tt>&quot;Encode&quot;</tt> object that was used to convert the source code to Unicode. </p>
<p> Its purpose was to allow your non-ASCII Perl scripts not to have to be written in <font SIZE="-1">UTF-8</font>; this was useful before editors that worked on <font SIZE="-1">UTF-8</font> encoded text were common, but that was long ago. It caused problems, such as affecting the operation of other modules that weren&#8217;t expecting it, causing general mayhem. </p>
<p> If you need something like this functionality, it is recommended that use you a simple source filter, such as Filter::Encoding. </p>
<p> If you are coming here because code of yours is being adversely affected by someone&#8217;s use of this variable, you can usually work around it by doing this: </p>
<pre>
 local ${^ENCODING};
</pre>
<p> near the beginning of the functions that are getting broken. This undefines the variable during the scope of execution of the including function. </p>
<p> This variable was added in Perl 5.8.2 and removed in 5.26.0. Setting it to anything other than <tt>&quot;undef&quot;</tt> was made fatal in Perl 5.28.0.</p>
<dt>${^GLOBAL_PHASE}</p>
<dd> The current phase of the perl interpreter. </p>
<p> Possible values are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><font SIZE="-1">CONSTRUCT</font></p>
<dd> The <tt>&quot;PerlInterpreter*&quot;</tt> is being constructed via <tt>&quot;perl_construct&quot;</tt>. This value is mostly there for completeness and for use via the underlying C variable <tt>&quot;PL_phase&quot;</tt>. It&#8217;s not really possible for Perl code to be executed unless construction of the interpreter is finished.</p>
<dt><font SIZE="-1">START</font></p>
<dd> This is the global compile-time. That includes, basically, every <tt>&quot;BEGIN&quot;</tt> block executed directly or indirectly from during the compile-time of the top-level program. </p>
<p> This phase is not called &#8220;<font SIZE="-1">BEGIN&#8221;</font> to avoid confusion with <tt>&quot;BEGIN&quot;</tt>-blocks, as those are executed during compile-time of any compilation unit, not just the top-level program. A new, localised compile-time entered at run-time, for example by constructs as <tt>&quot;eval &quot;use SomeModule&quot;&quot;</tt> are not global interpreter phases, and therefore aren&#8217;t reflected by <tt>&quot;${^GLOBAL_PHASE}&quot;</tt>.</p>
<dt><font SIZE="-1">CHECK</font></p>
<dd> Execution of any <tt>&quot;CHECK&quot;</tt> blocks.</p>
<dt><font SIZE="-1">INIT</font></p>
<dd> Similar to &#8220;<font SIZE="-1">CHECK&#8221;,</font> but for <tt>&quot;INIT&quot;</tt>-blocks, not <tt>&quot;CHECK&quot;</tt> blocks.</p>
<dt><font SIZE="-1">RUN</font></p>
<dd> The main run-time, i.e. the execution of <tt>&quot;PL_main_root&quot;</tt>.</p>
<dt><font SIZE="-1">END</font></p>
<dd> Execution of any <tt>&quot;END&quot;</tt> blocks.</p>
<dt><font SIZE="-1">DESTRUCT</font></p>
<dd> Global destruction.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Also note that there&#8217;s no value for UNITCHECK-blocks. That&#8217;s because those are run for each compilation unit individually, and therefore is not a global interpreter phase. </p>
<p> Not every program has to go through each of the possible phases, but transition from one phase to another can only happen in the order described in the above list. </p>
<p> An example of all of the phases Perl code can see: </p>
<p>BEGIN{print &#8220;compile-time: ${^GLOBAL_PHASE}
&#8221;} INIT{print &#8220;init-time: ${^GLOBAL_PHASE}
&#8221;} CHECK{print &#8220;check-time: ${^GLOBAL_PHASE}
&#8221;}<br />
{<br />
    package Print::Phase;<br />
    sub new<br />
    {<br />
        my($class, $time) = @_;<br />
        return bless \$time, $class;<br />
    }<br />
    sub DESTROY<br />
    {<br />
        my $self = shift;<br />
        print &#8220;$$self: ${^GLOBAL_PHASE}
&#8221;;<br />
    }<br />
}<br />
print &#8220;run-time: ${^GLOBAL_PHASE}
&#8221;;<br />
my $runtime = Print::Phase-&gt;new (<br />
    &#8220;lexical variables are garbage collected before END&#8221;);<br />
END{print &#8220;end-time: ${^GLOBAL_PHASE}
&#8221;} our $destruct = Print::Phase-&gt;new (<br />
    &#8220;package variables are garbage collected after END&#8221;);</p>
<p> This will print out </p>
<pre>
    compile-time: START
    check-time: CHECK
    init-time: INIT
    run-time: RUN
    lexical variables are garbage collected before END: RUN
    end-time: END
    package variables are garbage collected after END: DESTRUCT
</pre>
<p> This variable was added in Perl 5.14.0.</dl>
<dt>$^H</p>
<dd> <font SIZE="-1">WARNING:</font> This variable is strictly for internal use only. Its availability, behavior, and contents are subject to change without notice. </p>
<p> This variable contains compile-time hints for the Perl interpreter. At the end of compilation of a <font SIZE="-1">BLOCK</font> the value of this variable is restored to the value when the interpreter started to compile the <font SIZE="-1">BLOCK.</font> </p>
<p> When perl begins to parse any block construct that provides a lexical scope (e.g., eval body, required file, subroutine body, loop body, or conditional block), the existing value of <tt>$^H</tt> is saved, but its value is left unchanged. When the compilation of the block is completed, it regains the saved value. Between the points where its value is saved and restored, code that executes within <font SIZE="-1">BEGIN</font> blocks is free to change the value of <tt>$^H</tt>. </p>
<p> This behavior provides the semantic of lexical scoping, and is used in, for instance, the <tt>&quot;use strict&quot;</tt> pragma. </p>
<p> The contents should be an integer; different bits of it are used for different pragmatic flags. Here&#8217;s an example: </p>
<p>sub add_100{$ ^ H |= 0x100} sub foo<br />
{<br />
    BEGIN{add_100()} bar-&gt;baz($boon);<br />
}</p>
<p> Consider what happens during execution of the <font SIZE="-1">BEGIN</font> block. At this point the <font SIZE="-1">BEGIN</font> block has already been compiled, but the body of <tt>&quot;foo()&quot;</tt> is still being compiled. The new value of <tt>$^H</tt> will therefore be visible only while the body of <tt>&quot;foo()&quot;</tt> is being compiled. </p>
<p> Substitution of <tt>&quot;BEGIN { add_100() }&quot;</tt> block with: </p>
<p>BEGIN<br />
{<br />
    require strict;<br />
    strict-&gt;import(&#8216;vars&#8217;)<br />
}</p>
<p> demonstrates how <tt>&quot;use strict 'vars'&quot;</tt> is implemented. Here&#8217;s a conditional version of the same lexical pragma: </p>
<pre><code>
BEGIN
{
    require strict;
    strict-&gt;import('vars') if $condition
}
</code></pre>
<p> This variable was added in Perl 5.003.</p>
<dt>%^H</p>
<dd> The <tt>&quot;%^H&quot;</tt> hash provides the same scoping semantic as <tt>$^H</tt>. This makes it useful for implementation of lexically scoped pragmas. See perlpragma. All the entries are stringified when accessed at runtime, so only simple values can be accommodated. This means no pointers to objects, for example. </p>
<p> When putting items into <tt>&quot;%^H&quot;</tt>, in order to avoid conflicting with other users of the hash there is a convention regarding which keys to use. A module should use only keys that begin with the module&#8217;s name (the name of its main package) and a &#8220;/&#8221; character. For example, a module <tt>&quot;Foo::Bar&quot;</tt> should use keys such as <tt>&quot;Foo::Bar/baz&quot;</tt>. </p>
<p> This variable was added in Perl v5.6.0.</p>
<dt>${^OPEN}</p>
<dd> An internal variable used by PerlIO. A string in two parts, separated by a <tt>&quot;
