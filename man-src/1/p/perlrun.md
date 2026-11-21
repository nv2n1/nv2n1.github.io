---
title: "perlrun(1)"
name: "perlrun"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlrun/"
description: "perlrun – how to execute the Perl interpreter"
---

<h2>SYNOPSIS</h2>
<p> <code>perl</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[ <code>-sTtuUWX</code> ]<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[ <code>-hv</code> ] [ <code>-V</code>[:<i>configvar</i>] ]<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[ <code>-cw</code> ] [ <code>-d</code>[<code>t</code>][:<i>debugger</i>] ] [ <code>-D</code>[<i>number/list</i>] ]<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[ <code>-pna</code> ] [ <code>-F</code><i>pattern</i> ] [ <code>-l</code>[<i>octal</i>] ] [ <code>-0</code>[<i>octal/hexadecimal</i>] ]<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[ <code>-I</code><i>dir</i> ] [ <code>-m</code>[<code>&#8211;</code>]<i>module</i> ] [ <code>-M</code>[<code>&#8211;</code>]<i>&#8216;module&#8230;&#8217;</i> ] [ <code>-f</code> ]<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[ <code>-C [</code>number/list<code>] </code>]<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[ <code>-S</code> ]<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[ <code>-x</code>[<i>dir</i>] ]<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[ <code>-i</code>[<i>extension</i>] ]<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>[ [<code>-e</code>|<code>-E</code>] <i>&#8216;command&#8217;</i> ] [ <code>&#8212;</code> ] [ <i>programfile</i> ] [ <i>argument</i> ]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> The normal way to run a Perl program is by making it directly executable, or else by passing the name of the source file as an argument on the command line. (An interactive Perl environment is also possible&#8212;see perldebug for details on how to do that.) Upon startup, Perl looks for your program in one of the following places:</p>
<dl>
<dt>1.</dt>
<dd> Specified line by line via <code>-e</code> or <code>-E</code> switches on the command line.</dd>
<dt>2.</dt>
<dd> Contained in the file specified by the first filename on the command line. (Note that systems supporting the <tt>&quot;#!&quot;</tt> notation invoke interpreters this way. See &#8220;Location of Perl&#8221;.)</dd>
<dt>3.</dt>
<dd> Passed in implicitly via standard input. This works only if there are no filename arguments&#8212;to pass arguments to a STDIN-read program you must explicitly specify a &#8220;-&#8221; for the program name.</dd></dl>
<p> With methods 2 and 3, Perl starts parsing the input file from the beginning, unless you&#8217;ve specified a <code>-x</code> switch, in which case it scans for the first line starting with <tt>&quot;#!&quot;</tt> and containing the word &#8220;perl&#8221;, and starts there instead. This is useful for running a program embedded in a larger message. (In this case you would indicate the end of the program using the <tt>&quot;__END__&quot;</tt> token.) </p>
<p> The <tt>&quot;#!&quot;</tt> line is always examined for switches as the line is being parsed. Thus, if you&#8217;re on a machine that allows only one argument with the <tt>&quot;#!&quot;</tt> line, or worse, doesn&#8217;t even recognize the <tt>&quot;#!&quot;</tt> line, you still can get consistent switch behaviour regardless of how Perl was invoked, even if <code>-x</code> was used to find the beginning of the program. </p>
<p> Because historically some operating systems silently chopped off kernel interpretation of the <tt>&quot;#!&quot;</tt> line after 32 characters, some switches may be passed in on the command line, and some may not; you could even get a &#8220;-&#8221; without its letter, if you&#8217;re not careful. You probably want to make sure that all your switches fall either before or after that 32-character boundary. Most switches don&#8217;t actually care if they&#8217;re processed redundantly, but getting a &#8220;-&#8221; instead of a complete switch could cause Perl to try to execute standard input instead of your program. And a partial <code>-I</code> switch could also cause odd results. </p>
<p> Some switches do care if they are processed twice, for instance combinations of <code>-l</code> and <code>-0</code>. Either put all the switches after the 32-character boundary (if applicable), or replace the use of <code>-0</code><i>digits</i> by <tt>&quot;BEGIN{ $/ = &quot;</tt>\0digits&quot;; }&quot;</code>. </p>
<p> Parsing of the <code>&quot;#!&quot;</code> switches starts wherever ``perl&#8217;&#8216; is mentioned in the line. The sequences ``-*&#8216;&#8216; and ``- &#8216;&#8216; are specifically ignored so that you could, if you were so inclined, say </p>
<pre><code>    #!/bin/sh
    #! -*-perl-*-
    eval 'exec perl -x -wS $0 ${1+&quot;$@&quot;}'
        if 0;
</code></pre>
<p> to let Perl see the <code>-p</code> switch. </p>
<p> A similar trick involves the <i>env</i> program, if you have it. </p>
<pre><code>    #!/usr/bin/env perl
</code></pre>
<p> The examples above use a relative path to the perl interpreter, getting whatever version is first in the user&#8217;s path. If you want a specific version of Perl, say, perl5.14.1, you should place that directly in the <code>&quot;#!&quot;</code> line&#8217;s path. </p>
<p> If the <code>&quot;#!&quot;</code> line does not contain the word ``perl&#8217;&#8216; nor the word ``indir&#8217;&#8216;, the program named after the <code>&quot;#!&quot;</code> is executed instead of the Perl interpreter. This is slightly bizarre, but it helps people on machines that don&#8217;t do <code>&quot;#!&quot;</code>, because they can tell a program that their <font SIZE="-1">SHELL</font> is <i>/usr/bin/perl</i>, and Perl will then dispatch the program to the correct interpreter for them. </p>
<p> After locating your program, Perl compiles the entire program to an internal form. If there are any compilation errors, execution of the program is not attempted. (This is unlike the typical shell script, which might run part-way through before finding a syntax error.) </p>
<p> If the program is syntactically correct, it is executed. If the program runs off the end without hitting an <code>exit()</code> or <code>die()</code> operator, an implicit <code>exit(0)</code> is provided to indicate successful completion.  </p>
<h3>#! and quoting on non-Unix systems</h3>
<p> Unix&#8217;s <code>&quot;#!&quot;</code> technique can be simulated on other systems: </p>
<dl>
<dt><font SIZE="-1">OS/2</font></dt>
<dd> <p> Put </p>
<pre><code>    extproc perl -S -your_switches
</code></pre>
<p> as the first line in <code>&quot;*.cmd&quot;</code> file (<code>-S</code> due to a bug in cmd.exe&#8217;s `extproc&#8217; handling). </p>
 </dd>
<dt>MS-DOS</dt>
<dd> <p> Create a batch file to run your program, and codify it in <code>&quot;ALTERNATE_SHEBANG&quot;</code> (see the <i>dosish.h</i> file in the source distribution for more information). </p>
 </dd>
<dt>Win95/NT</dt>
<dd> <p> The Win95/NT installation, when using the ActiveState installer for Perl, will modify the Registry to associate the <i>.pl</i> extension with the perl interpreter. If you install Perl by other means (including building from the sources), you may have to modify the Registry yourself. Note that this means you can no longer tell the difference between an executable Perl program and a Perl library file. </p>
 </dd>
<dt><font SIZE="-1">VMS</font></dt>
<dd> <p> Put </p>
<pre><code> $ perl -mysw 'f$env(&quot;procedure&quot;)' 'p1' 'p2' 'p3' 'p4' 'p5' 'p6' 'p7' 'p8' !
 $ exit++ + ++$status != 0 and $exit = $status = undef;
</code></pre>
<p> at the top of your program, where <code>-mysw</code> are any command line switches you want to pass to Perl. You can now invoke the program directly, by saying <code>&quot;perl program&quot;</code>, or as a <font SIZE="-1">DCL</font> procedure, by saying <code>@program</code> (or implicitly via <i></i><font SIZE="-1"><i>DCL$PATH</i></font><i></i> by just using the name of the program). </p>
<p> This incantation is a bit much to remember, but Perl will display it for you if you say <code>&quot;perl &quot;-V:startperl&quot;&quot;</code>. </p>
 </dd></dl>
<p> Command-interpreters on non-Unix systems have rather different ideas on quoting than Unix shells. You&#8217;ll need to learn the special characters in your command-interpreter (<code>&quot;*&quot;</code>, <code>&quot;\&quot;</code> and <code>&quot;&quot;&quot;</code> are common) and how to protect whitespace and these characters to run one-liners (see -e below). </p>
<p> On some systems, you may have to change single-quotes to double ones, which you must <i>not</i> do on Unix or Plan 9 systems. You might also have to change a single % to a %%. </p>
<p> For example: </p>
<pre><code>    # Unix
    perl -e 'print &quot;Hello world\n&quot;'
    # MS-DOS, etc.
    perl -e &quot;print \&quot;Hello world\n\&quot;&quot;
    # VMS
    perl -e &quot;print &quot;&quot;Hello world\n&quot;&quot;&quot;
</code></pre>
<p> The problem is that none of this is reliable: it depends on the command and it is entirely possible neither works. If <i>4DOS</i> were the command shell, this would probably work better: </p>
<pre><code>    perl -e &quot;print &lt;Ctrl-x&gt;&quot;Hello world\n&lt;Ctrl-x&gt;&quot;&quot;
</code></pre>
<p> <font SIZE="-1"><code>CMD.EXE</code></font> in Windows <font SIZE="-1">NT</font> slipped a lot of standard Unix functionality in when nobody was looking, but just try to find documentation for its quoting rules. </p>
<p> There is no general solution to all of this. It&#8217;s just a mess.  </p>
<h3>Location of Perl</h3>
<p> It may seem obvious to say, but Perl is useful only when users can easily find it. When possible, it&#8217;s good for both <i>/usr/bin/perl</i> and <i>/usr/local/bin/perl</i> to be symlinks to the actual binary. If that can&#8217;t be done, system administrators are strongly encouraged to put (symlinks to) perl and its accompanying utilities into a directory typically found along a user&#8217;s <font SIZE="-1">PATH,</font> or in some other obvious and convenient place. </p>
<p> In this documentation, <code>&quot;#!/usr/bin/perl&quot;</code> on the first line of the program will stand in for whatever method works on your system. You are advised to use a specific path if you care about a specific version. </p>
<pre><code>    #!/usr/local/bin/perl5.14
</code></pre>
<p> or if you just want to be running at least version, place a statement like this at the top of your program: </p>
<pre><code>    use 5.014;
</code></pre>
<h3>Command Switches</h3>
<p> As with all standard commands, a single-character switch may be clustered with the following switch, if any. </p>
<pre><code>    #!/usr/bin/perl -spi.orig # same as -s -p -i.orig
</code></pre>
<p> A <code>&quot;--&quot;</code> signals the end of options and disables further option processing. Any arguments after the <code>&quot;--&quot;</code> are treated as filenames and arguments. </p>
<p> Switches include: </p>
<dl>
<dt><code>-0</code>[<i>octal/hexadecimal</i>]</dt>
<dd> <p> specifies the input record separator (<code>$/</code>) as an octal or hexadecimal number. If there are no digits, the null character is the separator. Other switches may precede or follow the digits. For example, if you have a version of <i>find</i> which can print filenames terminated by the null character, you can say this: </p>
<pre><code>    find . -name '*.orig' -print0 | perl -n0e unlink
</code></pre>
<p> The special value 00 will cause Perl to slurp files in paragraph mode. Any value 0400 or above will cause Perl to slurp files whole, but by convention the value 0777 is the one normally used for this purpose. </p>
<p> You can also specify the separator character using hexadecimal notation: <code>-0x</code><font SIZE="-1">HHH...</font>, where the <code>&quot;</code>H <code>&quot;</code> are valid hexadecimal digits. Unlike the octal form, this one may be used to specify any Unicode character, even those beyond 0xFF. So if you <i>really</i> want a record separator of 0777, specify it as <code>-0x1FF</code>. (This means that you cannot use the <code>-x</code> option with a directory name that consists of hexadecimal digits, or else Perl will think you have specified a hex number to <code>-0</code>.) </p>
 </dd>
<dt><code>-a</code></dt>
<dd> <p> turns on autosplit mode when used with a <code>-n</code> or <code>-p</code>. An implicit split command to the <code>@F</code> array is done as the first thing inside the implicit while loop produced by the <code>-n</code> or <code>-p</code>. </p>
<pre><code>    perl -ane 'print pop(@F), &quot;\n&quot;;'
</code></pre>
<p> is equivalent to </p>
<pre><code>    while (&lt;&gt;) {
        @F = split(' ');
        print pop(@F), &quot;\n&quot;;
    }
</code></pre>
<p> An alternate delimiter may be specified using <code>-F</code>. </p>
<p> <code>-a</code> implicitly sets <code>-n</code>. </p>
 </dd>
<dt><code>-C [</code>number/list <code>]</code></dt>
<dd> <p> The <code>-C</code> flag controls some of the Perl Unicode features. </p>
<p> As of 5.8.1, the <code>-C</code> can be followed either by a number or a list of option letters. The letters, their numeric values, and effects are as follows; listing the letters is equal to summing the numbers. </p>
<pre><code>    I 1 STDIN is assumed to be in UTF-8
    O 2 STDOUT will be in UTF-8
    E 4 STDERR will be in UTF-8
    S 7 I + O + E
    i 8 UTF-8 is the default PerlIO layer for input streams
    o 16 UTF-8 is the default PerlIO layer for output streams
    D 24 i + o
    A 32 the @ARGV elements are expected to be strings encoded
              in UTF-8
    L 64 normally the &quot;IOEioA&quot; are unconditional, the L makes
              them conditional on the locale environment variables
              (the LC_ALL, LC_CTYPE, and LANG, in the order of
              decreasing precedence) -- if the variables indicate
              UTF-8, then the selected &quot;IOEioA&quot; are in effect
    a 256 Set ${^UTF8CACHE} to -1, to run the UTF-8 caching
              code in debugging mode.
</code></pre>
<p> For example, <code>-COE</code> and <code>-C6</code> will both turn on UTF-8-ness on both <font SIZE="-1">STDOUT</font> and <font SIZE="-1">STDERR.</font> Repeating letters is just redundant, not cumulative nor toggling. </p>
<p> The <code>&quot;io&quot;</code> options mean that any subsequent <code>open()</code> (or similar I/O operations) in the current file scope will have the <code>&quot;:utf8&quot;</code> PerlIO layer implicitly applied to them, in other words, <font SIZE="-1">UTF-8</font> is expected from any input stream, and <font SIZE="-1">UTF-8</font> is produced to any output stream. This is just the default, with explicit layers in <code>open()</code> and with <code>binmode()</code> one can manipulate streams as usual. </p>
<p> <code>-C</code> on its own (not followed by any number or option list), or the empty string <code>&quot;&quot;</code> for the <code>&quot;PERL_UNICODE&quot;</code> environment variable, has the same effect as <code>-CSDL</code>. In other words, the standard I/O handles and the default <code>&quot;open()&quot;</code> layer are UTF-8-fied <i>but</i> only if the locale environment variables indicate a <font SIZE="-1">UTF-8</font> locale. This behaviour follows the <i>implicit</i> (and problematic) <font SIZE="-1">UTF-8</font> behaviour of Perl 5.8.0. (See ``<font SIZE="-1">UTF-8</font> no longer default under <font SIZE="-1">UTF-8</font> locales&#8217;&#8216; in perl581delta.) </p>
<p> You can use <code>-C0</code> (or <code>&quot;0&quot;</code> for <code>&quot;PERL_UNICODE&quot;</code>) to explicitly disable all the above Unicode features. </p>
<p> The read-only magic variable <code>&quot;${^UNICODE}&quot;</code> reflects the numeric value of this setting. This variable is set during Perl startup and is thereafter read-only. If you want runtime effects, use the three-arg <code>open()</code> (see ``open&#8217;&#8216; in perlfunc), the two-arg <code>binmode()</code> (see ``binmode&#8217;&#8216; in perlfunc), and the <code>&quot;open&quot;</code> pragma (see open). </p>
<p> (In Perls earlier than 5.8.1 the <code>-C</code> switch was a Win32-only switch that enabled the use of Unicode-aware ``wide system call&#8217;&#8216; Win32 APIs. This feature was practically unused, however, and the command line switch was therefore ``recycled&#8217;&#8216;.) </p>
<p> <code>Note:</code> Since perl 5.10.1, if the <code>-C</code> option is used on the <code>&quot;#!&quot;</code> line, it must be specified on the command line as well, since the standard streams are already set up at this point in the execution of the perl interpreter. You can also use <code>binmode()</code> to set the encoding of an I/O stream. </p>
 </dd>
<dt><code>-c</code></dt>
<dd> <p> causes Perl to check the syntax of the program and then exit without executing it. Actually, it <i>will</i> execute any <code>&quot;BEGIN&quot;</code>, <code>&quot;UNITCHECK&quot;</code>, or <code>&quot;CHECK&quot;</code> blocks and any <code>&quot;use&quot;</code> statements: these are considered as occurring outside the execution of your program. <code>&quot;INIT&quot;</code> and <code>&quot;END&quot;</code> blocks, however, will be skipped. </p>
 </dd>
<dt><code>-d</code></dt>
<dd>  </dd>
<dt><code>-dt</code></dt>
<dd> <p> runs the program under the Perl debugger. See perldebug. If <code>t</code> is specified, it indicates to the debugger that threads will be used in the code being debugged. </p>
 </dd>
<dt><code>-d:</code><i>MOD[=bar,baz]</i></dt>
<dd>  </dd>
<dt><code>-dt:</code><i>MOD[=bar,baz]</i></dt>
<dd> <p> runs the program under the control of a debugging, profiling, or tracing module installed as <code>&quot;Devel::</code>MOD <code>&quot;</code>. E.g., <code>-d:DProf</code> executes the program using the <code>&quot;Devel::DProf&quot;</code> profiler. As with the <code>-M</code> flag, options may be passed to the <code>&quot;Devel::</code>MOD <code>&quot;</code> package where they will be received and interpreted by the <code>&quot;Devel::</code>MOD <code>::import&quot;</code> routine. Again, like <code>-M</code>, use -<code>-d:-</code><font SIZE="-1">MOD</font> to call <code>&quot;Devel::</code>MOD <code>::unimport&quot;</code> instead of import. The comma-separated list of options must follow a <code>&quot;=&quot;</code> character. If <code>t</code> is specified, it indicates to the debugger that threads will be used in the code being debugged. See perldebug. </p>
 </dd>
<dt><code>-D</code><i>letters</i></dt>
<dd>  </dd>
<dt><code>-D</code><i>number</i></dt>
<dd> <p> sets debugging flags. This switch is enabled only if your perl binary has been built with debugging enabled: normal production perls won&#8217;t have been. </p>
<p> For example, to watch how perl executes your program, use <code>-Dtls</code>. Another nice value is <code>-Dx</code>, which lists your compiled syntax tree, and <code>-Dr</code> displays compiled regular expressions; the format of the output is explained in perldebguts. </p>
<p> As an alternative, specify a number instead of list of letters (e.g., <code>-D14</code> is equivalent to <code>-Dtls</code>): </p>
<pre><code>         1 p Tokenizing and parsing (with v, displays parse
               stack)
         2 s Stack snapshots (with v, displays all stacks)
         4 l Context (loop) stack processing
         8 t Trace execution
        16 o Method and overloading resolution
        32 c String/numeric conversions
        64 P Print profiling info, source file input state
       128 m Memory and SV allocation
       256 f Format processing
       512 r Regular expression parsing and execution
      1024 x Syntax tree dump
      2048 u Tainting checks
      4096 U Unofficial, User hacking (reserved for private,
               unreleased use)
     16384 X Scratchpad allocation
     32768 D Cleaning up
     65536 S Op slab allocation
    131072 T Tokenizing
    262144 R Include reference counts of dumped variables
               (eg when using -Ds)
    524288 J show s,t,P-debug (don't Jump over) on opcodes within
               package DB
   1048576 v Verbose: use in conjunction with other flags to
               increase the verbosity of the output. Is a no-op on
               many of the other flags
   2097152 C Copy On Write
   4194304 A Consistency checks on internal structures
   8388608 q quiet - currently only suppresses the &quot;EXECUTING&quot;
               message
  16777216 M trace smart match resolution
  33554432 B dump suBroutine definitions, including special
               Blocks like BEGIN
  67108864 L trace Locale-related info; what gets output is very
               subject to change
 134217728 i trace PerlIO layer processing. Set PERLIO_DEBUG to
               the filename to trace to.
</code></pre>
<p> All these flags require <code>-DDEBUGGING</code> when you compile the Perl executable (but see <code>&quot;:opd&quot;</code> in Devel::Peek or ``&#8216;debug&#8217; mode&#8217;&#8216; in re which may change this). See the <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file in the Perl source distribution for how to do this. </p>
<p> If you&#8217;re just trying to get a print out of each line of Perl code as it executes, the way that <code>&quot;sh -x&quot;</code> provides for shell scripts, you can&#8217;t use Perl&#8217;s <code>-D</code> switch. Instead do this </p>
<pre><code>  # If you have &quot;env&quot; utility
  env PERLDB_OPTS=&quot;NonStop=1 AutoTrace=1 frame=2&quot; perl -dS program
  # Bourne shell syntax
  $ PERLDB_OPTS=&quot;NonStop=1 AutoTrace=1 frame=2&quot; perl -dS program
  # csh syntax
  % (setenv PERLDB_OPTS &quot;NonStop=1 AutoTrace=1 frame=2&quot;; perl -dS program)
</code></pre>
<p> See perldebug for details and variations. </p>
 </dd>
<dt><code>-e</code><i>commandline</i></dt>
<dd> <p> may be used to enter one line of program. If <code>-e</code> is given, Perl will not look for a filename in the argument list. Multiple <code>-e</code> commands may be given to build up a multi-line script. Make sure to use semicolons where you would in a normal program. </p>
 </dd>
<dt><code>-E</code><i>commandline</i></dt>
<dd> <p> behaves just like <code>-e</code>, except that it implicitly enables all optional features (in the main compilation unit). See feature. </p>
 </dd>
<dt><code>-f</code></dt>
<dd> <p> Disable executing <i></i>$Config <i>{sitelib}/sitecustomize.pl</i> at startup. </p>
<p> Perl can be built so that it by default will try to execute <i></i>$Config <i>{sitelib}/sitecustomize.pl</i> at startup (in a <font SIZE="-1">BEGIN</font> block). This is a hook that allows the sysadmin to customize how Perl behaves. It can for instance be used to add entries to the <code>@INC</code> array to make Perl find modules in non-standard locations. </p>
<p> Perl actually inserts the following code: </p>
<pre><code>    BEGIN {
        do { local $!; -f &quot;$Config{sitelib}/sitecustomize.pl&quot;; }
            &amp;&amp; do &quot;$Config{sitelib}/sitecustomize.pl&quot;;
    }
</code></pre>
<p> Since it is an actual <code>&quot;do&quot;</code> (not a <code>&quot;require&quot;</code>), <i>sitecustomize.pl</i> doesn&#8217;t need to return a true value. The code is run in package <code>&quot;main&quot;</code>, in its own lexical scope. However, if the script dies, <code>$@</code> will not be set. </p>
<p> The value of <code>$Config{sitelib}</code> is also determined in C code and not read from <code>&quot;Config.pm&quot;</code>, which is not loaded. </p>
<p> The code is executed <i>very</i> early. For example, any changes made to <code>@INC</code> will show up in the output of `perl -V`. Of course, <code>&quot;END&quot;</code> blocks will be likewise executed very late. </p>
<p> To determine at runtime if this capability has been compiled in your perl, you can check the value of <code>$Config{usesitecustomize}</code>. </p>
 </dd>
<dt><code>-F</code><i>pattern</i></dt>
<dd> <p> specifies the pattern to split on for <code>-a</code>. The pattern may be surrounded by <code>&quot;//&quot;</code>, <code>&quot;&quot;</code>, or <code>&#8216;&#8216;</code>, otherwise it will be put in single quotes. You can&#8217;t use literal whitespace or <font SIZE="-1">NUL</font> characters in the pattern. </p>
<p> <code>-F</code> implicitly sets both <code>-a</code> and <code>-n</code>. </p>
 </dd>
<dt><code>-h</code></dt>
<dd> <p> prints a summary of the options. </p>
 </dd>
<dt><code>-i</code>[<i>extension</i>]</dt>
<dd> <p> specifies that files processed by the <code>&quot;&lt;&gt;&quot;</code> construct are to be edited in-place. It does this by renaming the input file, opening the output file by the original name, and selecting that output file as the default for <code>print()</code> statements. The extension, if supplied, is used to modify the name of the old file to make a backup copy, following these rules: </p>
<p> If no extension is supplied, and your system supports it, the original <i>file</i> is kept open without a name while the output is redirected to a new file with the original <i>filename</i>. When perl exits, cleanly or not, the original <i>file</i> is unlinked. </p>
<p> If the extension doesn&#8217;t contain a <code>&quot;*&quot;</code>, then it is appended to the end of the current filename as a suffix. If the extension does contain one or more <code>&quot;*&quot;</code> characters, then each <code>&quot;*&quot;</code> is replaced with the current filename. In Perl terms, you could think of this as: </p>
<pre><code>    ($backup = $extension) =~ s/\*/$file_name/g;
</code></pre>
<p> This allows you to add a prefix to the backup file, instead of (or in addition to) a suffix: </p>
<pre><code> $ perl -pi'orig_*' -e 's/bar/baz/' fileA # backup to
                                           # 'orig_fileA'
</code></pre>
<p> Or even to place backup copies of the original files into another directory (provided the directory already exists): </p>
<pre><code> $ perl -pi'old/*.orig' -e 's/bar/baz/' fileA # backup to
                                               # 'old/fileA.orig'
</code></pre>
<p> These sets of one-liners are equivalent: </p>
<pre><code> $ perl -pi -e 's/bar/baz/' fileA # overwrite current file
 $ perl -pi'*' -e 's/bar/baz/' fileA # overwrite current file
 $ perl -pi'.orig' -e 's/bar/baz/' fileA # backup to 'fileA.orig'
 $ perl -pi'*.orig' -e 's/bar/baz/' fileA # backup to 'fileA.orig'
</code></pre>
<p> From the shell, saying </p>
<pre><code>    $ perl -p -i.orig -e &quot;s/foo/bar/; ... &quot;
</code></pre>
<p> is the same as using the program: </p>
<pre><code>    #!/usr/bin/perl -pi.orig
    s/foo/bar/;
</code></pre>
<p> which is equivalent to </p>
<pre><code>    #!/usr/bin/perl
    $extension = '.orig';
    LINE: while (&lt;&gt;) {
        if ($ARGV ne $oldargv) {
            if ($extension !~ /\*/) {
                $backup = $ARGV . $extension;
            }
            else {
                ($backup = $extension) =~ s/\*/$ARGV/g;
            }
            rename($ARGV, $backup);
            open(ARGVOUT, &quot;&gt;$ARGV&quot;);
            select(ARGVOUT);
            $oldargv = $ARGV;
        }
        s/foo/bar/;
    }
    continue {
        print; # this prints to original filename
    }
    select(STDOUT);
</code></pre>
<p> except that the <code>-i</code> form doesn&#8217;t need to compare <code>$ARGV</code> to <code>$oldargv</code> to know when the filename has changed. It does, however, use <font SIZE="-1">ARGVOUT</font> for the selected filehandle. Note that <font SIZE="-1">STDOUT</font> is restored as the default output filehandle after the loop. </p>
<p> As shown above, Perl creates the backup file whether or not any output is actually changed. So this is just a fancy way to copy files: </p>
<pre><code>    $ perl -p -i'/some/file/path/*' -e 1 file1 file2 file3...
or
    $ perl -p -i'.orig' -e 1 file1 file2 file3...
</code></pre>
<p> You can use <code>&quot;eof&quot;</code> without parentheses to locate the end of each input file, in case you want to append to each file, or reset line numbering (see example in ``eof&#8217;&#8216; in perlfunc). </p>
<p> If, for a given file, Perl is unable to create the backup file as specified in the extension then it will skip that file and continue on with the next one (if it exists). </p>
<p> For a discussion of issues surrounding file permissions and <code>-i</code>, see ``Why does Perl let me delete read-only files? Why does -i clobber protected files? Isn&#8217;t this a bug in Perl?&#8216;&#8216; in perlfaq5. </p>
<p> You cannot use <code>-i</code> to create directories or to strip extensions from files. </p>
<p> Perl does not expand <code>&quot;~&quot;</code> in filenames, which is good, since some folks use it for their backup files: </p>
<pre><code>    $ perl -pi~ -e 's/foo/bar/' file1 file2 file3...
</code></pre>
<p> Note that because <code>-i</code> renames or deletes the original file before creating a new file of the same name, Unix-style soft and hard links will not be preserved. </p>
<p> Finally, the <code>-i</code> switch does not impede execution when no files are given on the command line. In this case, no backup is made (the original file cannot, of course, be determined) and processing proceeds from <font SIZE="-1">STDIN</font> to <font SIZE="-1">STDOUT</font> as might be expected. </p>
 </dd>
<dt><code>-I</code><i>directory</i></dt>
<dd> <p> Directories specified by <code>-I</code> are prepended to the search path for modules (<code>@INC</code>). </p>
 </dd>
<dt><code>-l</code>[<i>octnum</i>]</dt>
<dd> <p> enables automatic line-ending processing. It has two separate effects. First, it automatically chomps <code>$/</code> (the input record separator) when used with <code>-n</code> or <code>-p</code>. Second, it assigns <code>&quot;$\&quot;</code> (the output record separator) to have the value of <i>octnum</i> so that any print statements will have that separator added back on. If <i>octnum</i> is omitted, sets <code>&quot;$\&quot;</code> to the current value of <code>$/</code>. For instance, to trim lines to 80 columns: </p>
<pre><code>    perl -lpe 'substr($_, 80) = &quot;&quot;'
</code></pre>
<p> Note that the assignment <code>&quot;$\ = $/&quot;</code> is done when the switch is processed, so the input record separator can be different than the output record separator if the <code>-l</code> switch is followed by a <code>-0</code> switch: </p>
<pre><code>    gnufind / -print0 | perl -ln0e 'print &quot;found $_&quot; if -p'
</code></pre>
<p> This sets <code>&quot;$\&quot;</code> to newline and then sets <code>$/</code> to the null character. </p>
 </dd>
<dt><code>-m</code>[<code>-</code>]<i>module</i></dt>
<dd>  </dd>
<dt><code>-M</code>[<code>-</code>]<i>module</i></dt>
<dd>  </dd>
<dt><code>-M</code>[<code>-</code>]<i>&#8216;module ...&#8216;</i></dt>
<dd>  </dd>
<dt><code>-[mM]</code>[<code>-</code>]<i>module=arg[,arg]...</i></dt>
<dd> <p> <code>-m</code><i>module</i> executes <code>&quot;use&quot;</code> <i>module</i> <code>&quot;();&quot;</code> before executing your program. This loads the module, but does not call its <code>&quot;import&quot;</code> method, so does not import subroutines and does not give effect to a pragma. </p>
<p> <code>-M</code><i>module</i> executes <code>&quot;use&quot;</code> <i>module</i> <code>&quot;;&quot;</code> before executing your program. This loads the module and calls its <code>&quot;import&quot;</code> method, causing the module to have its default effect, typically importing subroutines or giving effect to a pragma. You can use quotes to add extra code after the module name, e.g., <code>&#8216;-M</code>MODULE <code> qw(foo bar)&#8216;</code>. </p>
<p> If the first character after the <code>-M</code> or <code>-m</code> is a dash (<code>-</code>) then the &#8216;use&#8217; is replaced with &#8216;no&#8217;. This makes no difference for <code>-m</code>. </p>
<p> A little builtin syntactic sugar means you can also say <code>-m</code><font SIZE="-1">MODULE</font><code>=foo,bar</code> or <code>-M</code><font SIZE="-1">MODULE</font><code>=foo,bar</code> as a shortcut for <code>&#8216;-M</code><font SIZE="-1">MODULE</font><code> qw(foo bar)&#8216;</code>. This avoids the need to use quotes when importing symbols. The actual code generated by <code>-M</code><font SIZE="-1">MODULE</font><code>=foo,bar</code> is <code>&quot;use module split(/,/,q{foo,bar})&quot;</code>. Note that the <code>&quot;=&quot;</code> form removes the distinction between <code>-m</code> and <code>-M</code>; that is, <code>-m</code><font SIZE="-1">MODULE</font><code>=foo,bar</code> is the same as <code>-M</code><font SIZE="-1">MODULE</font><code>=foo,bar</code>. </p>
<p> A consequence of the <code>&quot;split&quot;</code> formulation is that <code>-M</code><font SIZE="-1">MODULE</font><code>=number</code> never does a version check, unless <code>&quot;</code>MODULE <code>::import()&quot;</code> itself is set up to do a version check, which could happen for example if <i></i><font SIZE="-1"><i>MODULE</i></font><i></i> inherits from Exporter. </p>
 </dd>
<dt><code>-n</code></dt>
<dd> <p> causes Perl to assume the following loop around your program, which makes it iterate over filename arguments somewhat like <i>sed -n</i> or <i>awk</i>: </p>
<pre><code>  LINE:
    while (&lt;&gt;) {
        ... # your program goes here
    }
</code></pre>
<p> Note that the lines are not printed by default. See ``-p&#8217;&#8216; to have lines printed. If a file named by an argument cannot be opened for some reason, Perl warns you about it and moves on to the next file. </p>
<p> Also note that <code>&quot;&lt;&gt;&quot;</code> passes command line arguments to ``open&#8217;&#8216; in perlfunc, which doesn&#8217;t necessarily interpret them as file names. See perlop for possible security implications. </p>
<p> Here is an efficient way to delete all files that haven&#8217;t been modified for at least a week: </p>
<pre><code>    find . -mtime +7 -print | perl -nle unlink
</code></pre>
<p> This is faster than using the <code>-exec</code> switch of <i>find</i> because you don&#8217;t have to start a process on every filename found (but it&#8217;s not faster than using the <code>-delete</code> switch available in newer versions of <i>find</i>. It does suffer from the bug of mishandling newlines in pathnames, which you can fix if you follow the example under <code>-0</code>. </p>
<p> <code>&quot;BEGIN&quot;</code> and <code>&quot;END&quot;</code> blocks may be used to capture control before or after the implicit program loop, just as in <i>awk</i>. </p>
 </dd>
<dt><code>-p</code></dt>
<dd> <p> causes Perl to assume the following loop around your program, which makes it iterate over filename arguments somewhat like <i>sed</i>: </p>
<pre><code>  LINE:
    while (&lt;&gt;) {
        ... # your program goes here
    } continue {
        print or die &quot;-p destination: $!\n&quot;;
    }
</code></pre>
<p> If a file named by an argument cannot be opened for some reason, Perl warns you about it, and moves on to the next file. Note that the lines are printed automatically. An error occurring during printing is treated as fatal. To suppress printing use the <code>-n</code> switch. A <code>-p</code> overrides a <code>-n</code> switch. </p>
<p> <code>&quot;BEGIN&quot;</code> and <code>&quot;END&quot;</code> blocks may be used to capture control before or after the implicit loop, just as in <i>awk</i>. </p>
 </dd>
<dt><code>-s</code></dt>
<dd> <p> enables rudimentary switch parsing for switches on the command line after the program name but before any filename arguments (or before an argument of <code>--</code>). Any switch found there is removed from <code>@ARGV</code> and sets the corresponding variable in the Perl program. The following program prints ``1&#8217;&#8216; if the program is invoked with a <code>-xyz</code> switch, and ``abc&#8217;&#8216; if it is invoked with <code>-xyz=abc</code>. </p>
<pre><code>    #!/usr/bin/perl -s
    if ($xyz) { print &quot;$xyz\n&quot; }
</code></pre>
<p> Do note that a switch like <code>--help</code> creates the variable <code>&quot;${-help}&quot;</code>, which is not compliant with <code>&quot;use strict &quot;refs&quot;&quot;</code>. Also, when using this option on a script with warnings enabled you may get a lot of spurious ``used only once&#8217;&#8216; warnings. </p>
 </dd>
<dt><code>-S</code></dt>
<dd> <p> makes Perl use the <font SIZE="-1">PATH</font> environment variable to search for the program unless the name of the program contains path separators. </p>
<p> On some platforms, this also makes Perl append suffixes to the filename while searching for it. For example, on Win32 platforms, the ``.bat&#8217;&#8216; and ``.cmd&#8217;&#8216; suffixes are appended if a lookup for the original name fails, and if the name does not already end in one of those suffixes. If your Perl was compiled with <code>&quot;DEBUGGING&quot;</code> turned on, using the <code>-Dp</code> switch to Perl shows how the search progresses. </p>
<p> Typically this is used to emulate <code>&quot;#!&quot;</code> startup on platforms that don&#8217;t support <code>&quot;#!&quot;</code>. It&#8217;s also convenient when debugging a script that uses <code>&quot;#!&quot;</code>, and is thus normally found by the shell&#8217;s <code>$PATH</code> search mechanism. </p>
<p> This example works on many platforms that have a shell compatible with Bourne shell: </p>
<pre><code>    #!/usr/bin/perl
    eval 'exec /usr/bin/perl -wS $0 ${1+&quot;$@&quot;}'
            if $running_under_some_shell;
</code></pre>
<p> The system ignores the first line and feeds the program to <i>/bin/sh</i>, which proceeds to try to execute the Perl program as a shell script. The shell executes the second line as a normal shell command, and thus starts up the Perl interpreter. On some systems <code>$0</code> doesn&#8217;t always contain the full pathname, so the <code>-S</code> tells Perl to search for the program if necessary. After Perl locates the program, it parses the lines and ignores them because the variable <code>$running_under_some_shell</code> is never true. If the program will be interpreted by csh, you will need to replace <code>&quot;${1+&quot;$@&quot;}&quot;</code> with <code>$*</code>, even though that doesn&#8217;t understand embedded spaces (and such) in the argument list. To start up <i>sh</i> rather than <i>csh</i>, some systems may have to replace the <code>&quot;#!&quot;</code> line with a line containing just a colon, which will be politely ignored by Perl. Other systems can&#8217;t control that, and need a totally devious construct that will work under any of <i>csh</i>, <i>sh</i>, or Perl, such as the following: </p>
<pre><code>        eval '(exit $?0)' &amp;&amp; eval 'exec perl -wS $0 ${1+&quot;$@&quot;}'
        &amp; eval 'exec /usr/bin/perl -wS $0 $argv:q'
                if $running_under_some_shell;
</code></pre>
<p> If the filename supplied contains directory separators (and so is an absolute or relative pathname), and if that file is not found, platforms that append file extensions will do so and try to look for the file with those extensions added, one by one. </p>
<p> On DOS-like platforms, if the program does not contain directory separators, it will first be searched for in the current directory before being searched for on the <font SIZE="-1">PATH.</font> On Unix platforms, the program will be searched for strictly on the <font SIZE="-1">PATH.</font> </p>
 </dd>
<dt><code>-t</code></dt>
<dd> <p> Like <code>-T</code>, but taint checks will issue warnings rather than fatal errors. These warnings can now be controlled normally with <code>&quot;no warnings qw(taint)&quot;</code>. </p>
<p> <code>Note: This is not a substitute for </code>&quot;-T&quot;<code>!</code> This is meant to be used <i>only</i> as a temporary development aid while securing legacy code: for real production code and for new secure code written from scratch, always use the real <code>-T</code>. </p>
 </dd>
<dt><code>-T</code></dt>
<dd> <p> turns on ``taint&#8217;&#8216; so you can test them. Ordinarily these checks are done only when running setuid or setgid. It&#8217;s a good idea to turn them on explicitly for programs that run on behalf of someone else whom you might not necessarily trust, such as <font SIZE="-1">CGI</font> programs or any internet servers you might write in Perl. See perlsec for details. For security reasons, this option must be seen by Perl quite early; usually this means it must appear early on the command line or in the <code>&quot;#!&quot;</code> line for systems which support that construct. </p>
 </dd>
<dt><code>-u</code></dt>
<dd> <p> This switch causes Perl to dump core after compiling your program. You can then in theory take this core dump and turn it into an executable file by using the <i>undump</i> program (not supplied). This speeds startup at the expense of some disk space (which you can minimize by stripping the executable). (Still, a ``hello world&#8217;&#8216; executable comes out to about 200K on my machine.) If you want to execute a portion of your program before dumping, use the <code>&quot;CORE::dump()&quot;</code> function instead. Note: availability of <i>undump</i> is platform specific and may not be available for a specific port of Perl. </p>
 </dd>
<dt><code>-U</code></dt>
<dd> <p> allows Perl to do unsafe operations. Currently the only ``unsafe&#8217;&#8216; operations are attempting to unlink directories while running as superuser and running setuid programs with fatal taint checks turned into warnings. Note that warnings must be enabled along with this option to actually <i>generate</i> the taint-check warnings. </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> prints the version and patchlevel of your perl executable. </p>
 </dd>
<dt><code>-V</code></dt>
<dd> <p> prints summary of the major perl configuration values and the current values of <code>@INC</code>. </p>
 </dd>
<dt><code>-V:</code><i>configvar</i></dt>
<dd> <p> Prints to <font SIZE="-1">STDOUT</font> the value of the named configuration variable(s), with multiples when your <code>&quot;</code>configvar <code>&quot;</code> argument looks like a regex (has non-letters). For example: </p>
<pre><code>    $ perl -V:libc
        libc='/lib/libc-2.2.4.so';
    $ perl -V:lib.
        libs='-lnsl -lgdbm -ldb -ldl -lm -lcrypt -lutil -lc';
        libc='/lib/libc-2.2.4.so';
    $ perl -V:lib.*
        libpth='/usr/local/lib /lib /usr/lib';
        libs='-lnsl -lgdbm -ldb -ldl -lm -lcrypt -lutil -lc';
        lib_ext='.a';
        libc='/lib/libc-2.2.4.so';
        libperl='libperl.a';
        ....
</code></pre>
<p> Additionally, extra colons can be used to control formatting. A trailing colon suppresses the linefeed and terminator ``;&#8216;&#8216;, allowing you to embed queries into shell commands. (mnemonic: <font SIZE="-1">PATH</font> separator ``:&#8216;&#8216;.) </p>
<pre><code>    $ echo &quot;compression-vars: &quot; `perl -V:z.*: ` &quot; are here !&quot;
    compression-vars: zcat='' zip='zip' are here !
</code></pre>
<p> A leading colon removes the ``name=&#8216;&#8216; part of the response, this allows you to map to the name you need. (mnemonic: empty label) </p>
<pre><code>    $ echo &quot;goodvfork=&quot;`./perl -Ilib -V::usevfork`
    goodvfork=false;
</code></pre>
<p> Leading and trailing colons can be used together if you need positional parameter values without the names. Note that in the case below, the <code>&quot;PERL_API&quot;</code> params are returned in alphabetical order. </p>
<pre><code>    $ echo building_on `perl -V::osname: -V::PERL_API_.*:` now
    building_on 'linux' '5' '1' '9' now
</code></pre>
 </dd>
<dt><code>-w</code></dt>
<dd> <p> prints warnings about dubious constructs, such as variable names mentioned only once and scalar variables used before being set; redefined subroutines; references to undefined filehandles; filehandles opened read-only that you are attempting to write on; values used as a number that don&#8217;t <i>look</i> like numbers; using an array as though it were a scalar; if your subroutines recurse more than 100 deep; and innumerable other things. </p>
<p> This switch really just enables the global <code>$^W</code> variable; normally, the lexically scoped <code>&quot;use warnings&quot;</code> pragma is preferred. You can disable or promote into fatal errors specific warnings using <code>&quot;__WARN__&quot;</code> hooks, as described in perlvar and ``warn&#8217;&#8216; in perlfunc. See also perldiag and perltrap. A fine-grained warning facility is also available if you want to manipulate entire classes of warnings; see warnings. </p>
 </dd>
<dt><code>-W</code></dt>
<dd> <p> Enables all warnings regardless of <code>&quot;no warnings&quot;</code> or <code>$^W</code>. See warnings. </p>
 </dd>
<dt><code>-X</code></dt>
<dd> <p> Disables all warnings regardless of <code>&quot;use warnings&quot;</code> or <code>$^W</code>. See warnings. </p>
 </dd>
<dt><code>-x</code></dt>
<dd>  </dd>
<dt><code>-x</code><i>directory</i></dt>
<dd> <p> tells Perl that the program is embedded in a larger chunk of unrelated text, such as in a mail message. Leading garbage will be discarded until the first line that starts with <code>&quot;#!&quot;</code> and contains the string ``perl&#8217;&#8216;. Any meaningful switches on that line will be applied. </p>
<p> All references to line numbers by the program (warnings, errors, ...) will treat the <code>&quot;#!&quot;</code> line as the first line. Thus a warning on the 2nd line of the program, which is on the 100th line in the file will be reported as line 2, not as line 100. This can be overridden by using the <code>&quot;#line&quot;</code> directive. (See ``Plain Old Comments (Not!)&#8216;&#8216; in perlsyn) </p>
<p> If a directory name is specified, Perl will switch to that directory before running the program. The <code>-x</code> switch controls only the disposal of leading garbage. The program must be terminated with <code>&quot;__END__&quot;</code> if there is trailing garbage to be ignored; the program can process any or all of the trailing garbage via the <code>&quot;DATA&quot;</code> filehandle if desired. </p>
<p> The directory, if specified, must appear immediately following the <code>-x</code> with no intervening whitespace. </p>
 </dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1">HOME</font></dt>
<dd> <p> Used if <code>&quot;chdir&quot;</code> has no argument. </p>
 </dd>
<dt><font SIZE="-1">LOGDIR</font></dt>
<dd> <p> Used if <code>&quot;chdir&quot;</code> has no argument and <font SIZE="-1">HOME</font> is not set. </p>
 </dd>
<dt><font SIZE="-1">PATH</font></dt>
<dd> <p> Used in executing subprocesses, and in finding the program if <code>-S</code> is used. </p>
 </dd>
<dt><font SIZE="-1">PERL5LIB</font></dt>
<dd> <p> A list of directories in which to look for Perl library files before looking in the standard library. Any architecture-specific and version-specific directories, such as <i>version/archname/</i>, <i>version/</i>, or <i>archname/</i> under the specified locations are automatically included if they exist, with this lookup done at interpreter startup time. In addition, any directories matching the entries in <code>$Config{inc_version_list}</code> are added. (These typically would be for older compatible perl versions installed in the same directory tree.) </p>
<p> If <font SIZE="-1">PERL5LIB</font> is not defined, <font SIZE="-1">PERLLIB</font> is used. Directories are separated (like in <font SIZE="-1">PATH</font>) by a colon on Unixish platforms and by a semicolon on Windows (the proper path separator being given by the command <code>&quot;perl -V:</code>path_sep <code>&quot;</code>). </p>
<p> When running taint checks, either because the program was running setuid or setgid, or the <code>-T</code> or <code>-t</code> switch was specified, neither <font SIZE="-1">PERL5LIB</font> nor <font SIZE="-1">PERLLIB</font> is consulted. The program should instead say: </p>
<pre><code>    use lib &quot;/my/directory&quot;;
</code></pre>
 </dd>
<dt><font SIZE="-1">PERL5OPT</font></dt>
<dd> <p> Command-line options (switches). Switches in this variable are treated as if they were on every Perl command line. Only the <code>-[CDIMTUWdmtw]</code> switches are allowed. When running taint checks (either because the program was running setuid or setgid, or because the <code>-T</code> or <code>-t</code> switch was used), this variable is ignored. If <font SIZE="-1">PERL5OPT</font> begins with <code>-T</code>, tainting will be enabled and subsequent options ignored. If <font SIZE="-1">PERL5OPT</font> begins with <code>-t</code>, tainting will be enabled, a writable dot removed from <code>@INC</code>, and subsequent options honored. </p>
 </dd>
<dt><font SIZE="-1">PERLIO</font></dt>
<dd> <p> A space (or colon) separated list of PerlIO layers. If perl is built to use PerlIO system for <font SIZE="-1">IO</font> (the default) these layers affect Perl&#8217;s <font SIZE="-1">IO.</font> </p>
<p> It is conventional to start layer names with a colon (for example, <code>&quot;:perlio&quot;</code>) to emphasize their similarity to variable ``attributes&#8217;&#8216;. But the code that parses layer specification strings, which is also used to decode the <font SIZE="-1">PERLIO</font> environment variable, treats the colon as a separator. </p>
<p> An unset or empty <font SIZE="-1">PERLIO</font> is equivalent to the default set of layers for your platform; for example, <code>&quot;:unix:perlio&quot;</code> on Unix-like systems and <code>&quot;:unix:crlf&quot;</code> on Windows and other DOS-like systems. </p>
<p> The list becomes the default for <i>all</i> Perl&#8217;s <font SIZE="-1">IO.</font> Consequently only built-in layers can appear in this list, as external layers (such as <code>&quot;:encoding()&quot;</code>) need <font SIZE="-1">IO</font> in order to load them! See ``open pragma&#8217;&#8216; for how to add external encodings as defaults. </p>
<p> Layers it makes sense to include in the <font SIZE="-1">PERLIO</font> environment variable are briefly summarized below. For more details see PerlIO. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>:bytes</dt>
<dd> <p> A pseudolayer that turns the <code>&quot;:utf8&quot;</code> flag <i>off</i> for the layer below; unlikely to be useful on its own in the global <font SIZE="-1">PERLIO</font> environment variable. You perhaps were thinking of <code>&quot;:crlf:bytes&quot;</code> or <code>&quot;:perlio:bytes&quot;</code>. </p>
 </dd>
<dt>:crlf</dt>
<dd> <p> A layer which does <font SIZE="-1">CRLF</font> to <code>&quot;\n&quot;</code> translation distinguishing ``text&#8217;&#8216; and ``binary&#8217;&#8216; files in the manner of MS-DOS and similar operating systems. (It currently does <i>not</i> mimic MS-DOS as far as treating of Control-Z as being an end-of-file marker.) </p>
 </dd>
<dt>:mmap</dt>
<dd> <p> A layer that implements ``reading&#8217;&#8216; of files by using <i><a href="/docs/linux/man/2-mmap/">mmap</a></i>(2) to make an entire file appear in the process&#8217;s address space, and then using that as PerlIO&#8217;s ``buffer&#8217;&#8216;. </p>
 </dd>
<dt>:perlio</dt>
<dd> <p> This is a re-implementation of stdio-like buffering written as a PerlIO layer. As such it will call whatever layer is below it for its operations, typically <code>&quot;:unix&quot;</code>. </p>
 </dd>
<dt>:pop</dt>
<dd> <p> An experimental pseudolayer that removes the topmost layer. Use with the same care as is reserved for nitroglycerine. </p>
 </dd>
<dt>:raw</dt>
<dd> <p> A pseudolayer that manipulates other layers. Applying the <code>&quot;:raw&quot;</code> layer is equivalent to calling <code>&quot;binmode($fh)&quot;</code>. It makes the stream pass each byte as-is without translation. In particular, both <font SIZE="-1">CRLF</font> translation and intuiting <code>&quot;:utf8&quot;</code> from the locale are disabled. </p>
<p> Unlike in earlier versions of Perl, <code>&quot;:raw&quot;</code> is <i>not</i> just the inverse of <code>&quot;:crlf&quot;</code>: other layers which would affect the binary nature of the stream are also removed or disabled. </p>
 </dd>
<dt>:stdio</dt>
<dd> <p> This layer provides a PerlIO interface by wrapping system&#8217;s <font SIZE="-1">ANSI C</font> ``stdio&#8217;&#8216; library calls. The layer provides both buffering and <font SIZE="-1">IO.</font> Note that the <code>&quot;:stdio&quot;</code> layer does <i>not</i> do <font SIZE="-1">CRLF</font> translation even if that is the platform&#8217;s normal behaviour. You will need a <code>&quot;:crlf&quot;</code> layer above it to do that. </p>
 </dd>
<dt>:unix</dt>
<dd> <p> Low-level layer that calls <code>&quot;read&quot;</code>, <code>&quot;write&quot;</code>, <code>&quot;lseek&quot;</code>, etc. </p>
 </dd>
<dt>:utf8</dt>
<dd> <p> A pseudolayer that enables a flag in the layer below to tell Perl that output should be in utf8 and that input should be regarded as already in valid utf8 form. <font SIZE="-1"><code>WARNING:</code></font><code> It does not check for validity and as such should be handled with extreme caution for input, because security violations can occur with non-shortest </code><font SIZE="-1"><code>UTF-8</code></font><code> encodings, etc.</code> Generally <code>&quot;:encoding(UTF-8)&quot;</code> is the best option when reading <font SIZE="-1">UTF-8</font> encoded data. </p>
 </dd>
<dt>:win32</dt>
<dd> <p> On Win32 platforms this <i>experimental</i> layer uses native ``handle&#8217;&#8216; <font SIZE="-1">IO</font> rather than a Unix-like numeric file descriptor layer. Known to be buggy in this release (5.14). </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> The default set of layers should give acceptable results on all platforms </p>
<p> For Unix platforms that will be the equivalent of ``unix perlio&#8217;&#8216; or ``stdio&#8217;&#8216;. Configure is set up to prefer the ``stdio&#8217;&#8216; implementation if the system&#8217;s library provides for fast access to the buffer; otherwise, it uses the ``unix perlio&#8217;&#8216; implementation. </p>
<p> On Win32 the default in this release (5.14) is ``unix crlf&#8217;&#8216;. Win32&#8217;s ``stdio&#8217;&#8216; has a number of bugs/mis-features for Perl <font SIZE="-1">IO</font> which are somewhat depending on the version and vendor of the C compiler. Using our own <code>&quot;crlf&quot;</code> layer as the buffer avoids those issues and makes things more uniform. The <code>&quot;crlf&quot;</code> layer provides <font SIZE="-1">CRLF</font> conversion as well as buffering. </p>
<p> This release (5.14) uses <code>&quot;unix&quot;</code> as the bottom layer on Win32, and so still uses the C compiler&#8217;s numeric file descriptor routines. There is an experimental native <code>&quot;win32&quot;</code> layer, which is expected to be enhanced and should eventually become the default under Win32. </p>
<p> The <font SIZE="-1">PERLIO</font> environment variable is completely ignored when Perl is run in taint mode. </p>
 </dd></dl>
<dt><font SIZE="-1">PERLIO_DEBUG</font></dt>
<dd> <p> If set to the name of a file or device when Perl is run with the <code>-Di</code> command-line switch, the logging of certain operations of the PerlIO subsystem will be redirected to the specified file rather than going to stderr, which is the default. The file is opened in append mode. Typical uses are in Unix: </p>
<pre><code>   % env PERLIO_DEBUG=/tmp/perlio.log perl -Di script ...
</code></pre>
<p> and under Win32, the approximately equivalent: </p>
<pre><code>   &gt; set PERLIO_DEBUG=CON
   perl -Di script ...
</code></pre>
<p> This functionality is disabled for setuid scripts, for scripts run with <code>-T</code>, and for scripts run on a Perl built without <code>&quot;-DDEBUGGING&quot;</code> support. </p>
 </dd>
<dt><font SIZE="-1">PERLLIB</font></dt>
<dd> <p> A list of directories in which to look for Perl library files before looking in the standard library. If <font SIZE="-1">PERL5LIB</font> is defined, <font SIZE="-1">PERLLIB</font> is not used. </p>
<p> The <font SIZE="-1">PERLLIB</font> environment variable is completely ignored when Perl is run in taint mode. </p>
 </dd>
<dt><font SIZE="-1">PERL5DB</font></dt>
<dd> <p> The command used to load the debugger code. The default is: </p>
<pre><code>        BEGIN { require &quot;perl5db.pl&quot; }
</code></pre>
<p> The <font SIZE="-1">PERL5DB</font> environment variable is only used when Perl is started with a bare <code>-d</code> switch. </p>
 </dd>
<dt><font SIZE="-1">PERL5DB_THREADED</font></dt>
<dd> <p> If set to a true value, indicates to the debugger that the code being debugged uses threads. </p>
 </dd>
<dt><font SIZE="-1">PERL5SHELL</font> (specific to the Win32 port)</dt>
<dd> <p> On Win32 ports only, may be set to an alternative shell that Perl must use internally for executing ``backtick&#8217;&#8216; commands or <code>system()</code>. Default is <code>&quot;cmd.exe /x/d/c&quot;</code> on WindowsNT and <code>&quot;command.com /c&quot;</code> on Windows95. The value is considered space-separated. Precede any character that needs to be protected, like a space or backslash, with another backslash. </p>
<p> Note that Perl doesn&#8217;t use <font SIZE="-1">COMSPEC</font> for this purpose because <font SIZE="-1">COMSPEC</font> has a high degree of variability among users, leading to portability concerns. Besides, Perl can use a shell that may not be fit for interactive use, and setting <font SIZE="-1">COMSPEC</font> to such a shell may interfere with the proper functioning of other programs (which usually look in <font SIZE="-1">COMSPEC</font> to find a shell fit for interactive use). </p>
<p> Before Perl 5.10.0 and 5.8.8, <font SIZE="-1">PERL5SHELL</font> was not taint checked when running external commands. It is recommended that you explicitly set (or delete) <code>$ENV{PERL5SHELL}</code> when running in taint mode under Windows. </p>
 </dd>
<dt><font SIZE="-1">PERL_ALLOW_NON_IFS_LSP</font> (specific to the Win32 port)</dt>
<dd> <p> Set to 1 to allow the use of non-IFS compatible LSPs (Layered Service Providers). Perl normally searches for an IFS-compatible <font SIZE="-1">LSP</font> because this is required for its emulation of Windows sockets as real filehandles. However, this may cause problems if you have a firewall such as <i>McAfee Guardian</i>, which requires that all applications use its <font SIZE="-1">LSP</font> but which is not IFS-compatible, because clearly Perl will normally avoid using such an <font SIZE="-1">LSP.</font> </p>
<p> Setting this environment variable to 1 means that Perl will simply use the first suitable <font SIZE="-1">LSP</font> enumerated in the catalog, which keeps <i>McAfee Guardian</i> happy---and in that particular case Perl still works too because <i>McAfee Guardian</i>&#8216;s <font SIZE="-1">LSP</font> actually plays other games which allow applications requiring <font SIZE="-1">IFS</font> compatibility to work. </p>
 </dd>
<dt><font SIZE="-1">PERL_DEBUG_MSTATS</font></dt>
<dd> <p> Relevant only if Perl is compiled with the <code>&quot;malloc&quot;</code> included with the Perl distribution; that is, if <code>&quot;perl -V:d_mymalloc&quot;</code> is ``define&#8217;&#8216;. </p>
<p> If set, this dumps out memory statistics after execution. If set to an integer greater than one, also dumps out memory statistics after compilation. </p>
 </dd>
<dt><font SIZE="-1">PERL_DESTRUCT_LEVEL</font></dt>
<dd> <p> Relevant only if your Perl executable was built with <code>-DDEBUGGING</code>, this controls the behaviour of global destruction of objects and other references. See ``<font SIZE="-1">PERL_DESTRUCT_LEVEL&#8217;&#8216;</font> in perlhacktips for more information. </p>
 </dd>
<dt><font SIZE="-1">PERL_DL_NONLAZY</font></dt>
<dd> <p> Set to <code>&quot;1&quot;</code> to have Perl resolve <i>all</i> undefined symbols when it loads a dynamic library. The default behaviour is to resolve symbols when they are used. Setting this variable is useful during testing of extensions, as it ensures that you get an error on misspelled function names even if the test suite doesn&#8217;t call them. </p>
 </dd>
<dt><font SIZE="-1">PERL_ENCODING</font></dt>
<dd> <p> If using the <code>&quot;use encoding&quot;</code> pragma without an explicit encoding name, the <font SIZE="-1">PERL_ENCODING</font> environment variable is consulted for an encoding name. </p>
 </dd>
<dt><font SIZE="-1">PERL_HASH_SEED</font></dt>
<dd> <p> (Since Perl 5.8.1, new semantics in Perl 5.18.0) Used to override the randomization of Perl&#8217;s internal hash function. The value is expressed in hexadecimal, and may include a leading 0x. Truncated patterns are treated as though they are suffixed with sufficient 0&#8217;s as required. </p>
<p> If the option is provided, and <code>&quot;PERL_PERTURB_KEYS&quot;</code> is <font SIZE="-1">NOT</font> set, then a value of &#8216;0&#8217; implies <code>&quot;PERL_PERTURB_KEYS=0&quot;</code> and any other value implies <code>&quot;PERL_PERTURB_KEYS=2&quot;</code>. </p>
<p> <font SIZE="-1"><code>PLEASE NOTE:</code></font><code> The hash seed is sensitive information</code>. Hashes are randomized to protect against local and remote attacks against Perl code. By manually setting a seed, this protection may be partially or completely lost. </p>
<p> See ``Algorithmic Complexity Attacks&#8217;&#8216; in perlsec, ``<font SIZE="-1">PERL_PERTURB_KEYS&#8217;&#8216;</font>, and ``<font SIZE="-1">PERL_HASH_SEED_DEBUG&#8217;&#8216;</font> for more information. </p>
 </dd>
<dt><font SIZE="-1">PERL_PERTURB_KEYS</font></dt>
<dd> <p> (Since Perl 5.18.0) Set to <code>&quot;0&quot;</code> or <code>&quot;NO&quot;</code> then traversing keys will be repeatable from run to run for the same <font SIZE="-1">PERL_HASH_SEED.</font> Insertion into a hash will not change the order, except to provide for more space in the hash. When combined with setting <font SIZE="-1">PERL_HASH_SEED</font> this mode is as close to pre 5.18 behavior as you can get. </p>
<p> When set to <code>&quot;1&quot;</code> or <code>&quot;RANDOM&quot;</code> then traversing keys will be randomized. Every time a hash is inserted into the key order will change in a random fashion. The order may not be repeatable in a following program run even if the <font SIZE="-1">PERL_HASH_SEED</font> has been specified. This is the default mode for perl. </p>
<p> When set to <code>&quot;2&quot;</code> or <code>&quot;DETERMINISTIC&quot;</code> then inserting keys into a hash will cause the key order to change, but in a way that is repeatable from program run to program run. </p>
<p> <font SIZE="-1"><code>NOTE:</code></font> Use of this option is considered insecure, and is intended only for debugging non-deterministic behavior in Perl&#8217;s hash function. Do not use it in production. </p>
<p> See ``Algorithmic Complexity Attacks&#8217;&#8216; in perlsec and ``<font SIZE="-1">PERL_HASH_SEED&#8217;&#8216;</font> and ``<font SIZE="-1">PERL_HASH_SEED_DEBUG&#8217;&#8216;</font> for more information. You can get and set the key traversal mask for a specific hash by using the <code>&quot;hash_traversal_mask()&quot;</code> function from Hash::Util. </p>
 </dd>
<dt><font SIZE="-1">PERL_HASH_SEED_DEBUG</font></dt>
<dd> <p> (Since Perl 5.8.1.) Set to <code>&quot;1&quot;</code> to display (to <font SIZE="-1">STDERR</font>) information about the hash function, seed, and what type of key traversal randomization is in effect at the beginning of execution. This, combined with ``<font SIZE="-1">PERL_HASH_SEED&#8217;&#8216;</font> and ``<font SIZE="-1">PERL_PERTURB_KEYS&#8217;&#8216;</font> is intended to aid in debugging nondeterministic behaviour caused by hash randomization. </p>
<p> <code>Note</code> that any information about the hash function, especially the hash seed is <code>sensitive information</code>: by knowing it, one can craft a denial-of-service attack against Perl code, even remotely; see ``Algorithmic Complexity Attacks&#8217;&#8216; in perlsec for more information. <code>Do not disclose the hash seed</code> to people who don&#8217;t need to know it. See also <code>&quot;hash_seed()&quot;</code> and <code>&quot;key_traversal_mask()&quot;</code> in Hash::Util. </p>
<p> An example output might be: </p>
<pre><code> HASH_FUNCTION = ONE_AT_A_TIME_HARD HASH_SEED = 0x652e9b9349a7a032 PERTURB_KEYS = 1 (RANDOM)
</code></pre>
 </dd>
<dt><font SIZE="-1">PERL_MEM_LOG</font></dt>
<dd> <p> If your Perl was configured with <code>-Accflags=-DPERL_MEM_LOG</code>, setting the environment variable <code>&quot;PERL_MEM_LOG&quot;</code> enables logging debug messages. The value has the form <code>&quot;&lt;</code>number <code>&gt;[m][s][t]&quot;</code>, where <code>&quot;</code>number <code>&quot;</code> is the file descriptor number you want to write to (2 is default), and the combination of letters specifies that you want information about (m)emory and/or (s)v, optionally with (t)imestamps. For example, <code>&quot;PERL_MEM_LOG=1mst&quot;</code> logs all information to stdout. You can write to other opened file descriptors in a variety of ways: </p>
<pre><code>  $ 3&gt;foo3 PERL_MEM_LOG=3m perl ...
</code></pre>
 </dd>
<dt><font SIZE="-1">PERL_ROOT</font> (specific to the <font SIZE="-1">VMS</font> port)</dt>
<dd> <p> A translation-concealed rooted logical name that contains Perl and the logical device for the <code>@INC</code> path on <font SIZE="-1">VMS</font> only. Other logical names that affect Perl on <font SIZE="-1">VMS</font> include <font SIZE="-1">PERLSHR, PERL_ENV_TABLES,</font> and <font SIZE="-1">SYS$TIMEZONE_DIFFERENTIAL,</font> but are optional and discussed further in perlvms and in <i></i><font SIZE="-1"><i>README</i></font><i>.vms</i> in the Perl source distribution. </p>
 </dd>
<dt><font SIZE="-1">PERL_SIGNALS</font></dt>
<dd> <p> Available in Perls 5.8.1 and later. If set to <code>&quot;unsafe&quot;</code>, the pre-Perl-5.8.0 signal behaviour (which is immediate but unsafe) is restored. If set to <code>&quot;safe&quot;</code>, then safe (but deferred) signals are used. See ``Deferred Signals (Safe Signals)&#8216;&#8216; in perlipc. </p>
 </dd>
<dt><font SIZE="-1">PERL_UNICODE</font></dt>
<dd> <p> Equivalent to the <code>-C</code> command-line switch. Note that this is not a boolean variable. Setting this to <code>&quot;1&quot;</code> is not the right way to ``enable Unicode&#8217;&#8216; (whatever that would mean). You can use <code>&quot;0&quot;</code> to ``disable Unicode&#8217;&#8216;, though (or alternatively unset <font SIZE="-1">PERL_UNICODE</font> in your shell before starting Perl). See the description of the <code>-C</code> switch for more information. </p>
 </dd>
<dt><font SIZE="-1">PERL_USE_UNSAFE_INC</font></dt>
<dd> <p> If perl has been configured to not have the current directory in <code>@INC</code> by default, this variable can be set to <code>&quot;1&quot;</code> to reinstate it. It&#8217;s primarily intended for use while building and testing modules that have not been updated to deal with ``.&#8216;&#8216; not being in <code>@INC</code> and should not be set in the environment for day-to-day use. </p>
 </dd>
<dt><font SIZE="-1">SYS$LOGIN</font> (specific to the <font SIZE="-1">VMS</font> port)</dt>
<dd> <p> Used if chdir has no argument and <font SIZE="-1">HOME</font> and <font SIZE="-1">LOGDIR</font> are not set. </p>
 </dd>
<dt><font SIZE="-1">PERL_INTERNAL_RAND_SEED</font></dt>
<dd> <p> Set to a non-negative integer to seed the random number generator used internally by perl for a variety of purposes. </p>
<p> Ignored if perl is run setuid or setgid. Used only for some limited startup randomization (hash keys) if <code>&quot;-T&quot;</code> or <code>&quot;-t&quot;</code> perl is started with tainting enabled. </p>
<p> Perl may be built to ignore this variable. </p>
 </dd></dl>
<p> Perl also has environment variables that control how Perl handles data specific to particular natural languages; see perllocale. </p>
<p> Perl and its various modules and components, including its test frameworks, may sometimes make use of certain other environment variables. Some of these are specific to a particular platform. Please consult the appropriate module documentation and any documentation for your platform (like perlsolaris, perllinux, perlmacosx, perlwin32, etc) for variables peculiar to those specific situations. </p>
<p> Perl makes all environment variables available to the program being executed, and passes these along to any child processes it starts. However, programs running setuid would do well to execute the following lines before doing anything else, just to keep people honest: </p>
<pre><code>    $ENV{PATH} = &quot;/bin:/usr/bin&quot;; # or whatever you need
    $ENV{SHELL} = &quot;/bin/sh&quot; if exists $ENV{SHELL};
    delete @ENV{qw(IFS CDPATH ENV BASH_ENV)};
</code></pre>
