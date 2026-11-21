---
title: "perldebguts(1)"
name: "perldebguts"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perldebguts/"
description: "perldebguts – Guts of Perl debugging"
---
<h2 class="name">NAME</h2>
<p> perldebguts - Guts of Perl debugging </p>
<h2>DESCRIPTION</h2>
<p> This is not perldebug, which tells you how to use the debugger. This manpage describes low-level details concerning the debugger&#8217;s internals, which range from difficult to impossible to understand for anyone who isn&#8217;t incredibly intimate with Perl&#8217;s guts. Caveat lector.  </p>
<h2>Debugger Internals</h2>
<p> Perl has special debugging hooks at compile-time and run-time used to create debugging environments. These hooks are not to be confused with the <i>perl -Dxxx</i> command described in perlrun, which is usable only if a special Perl is built per the instructions in the <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> podpage in the Perl source tree. </p>
<p> For example, whenever you call Perl&#8217;s built-in <code>&quot;caller&quot;</code> function from the package <code>&quot;DB&quot;</code>, the arguments that the corresponding stack frame was called with are copied to the <code>@DB::args</code> array. These mechanisms are enabled by calling Perl with the <code>-d</code> switch. Specifically, the following additional features are enabled (cf. ``$^P&#8217;&#8216; in perlvar): </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Perl inserts the contents of <code>$ENV{PERL5DB}</code> (or <code>&quot;BEGIN {require &#8216;perl5db.pl&#8217;}&quot;</code> if not present) before the first line of your program. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Each array <code>&quot;@{&quot;_&lt;$filename&quot;}&quot;</code> holds the lines of <code>$filename</code> for a file compiled by Perl. The same is also true for <code>&quot;eval&quot;</code>ed strings that contain subroutines, or which are currently being executed. The <code>$filename</code> for <code>&quot;eval&quot;</code>ed strings looks like <code>&quot;(eval 34)&quot;</code>. </p>
<p> Values in this array are magical in numeric context: they compare equal to zero only if the line is not breakable. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Each hash <code>&quot;%{&quot;_&lt;$filename&quot;}&quot;</code> contains breakpoints and actions keyed by line number. Individual entries (as opposed to the whole hash) are settable. Perl only cares about Boolean true here, although the values used by <i>perl5db.pl</i> have the form <code>&quot;$break_condition\0$action&quot;</code>. </p>
<p> The same holds for evaluated strings that contain subroutines, or which are currently being executed. The <code>$filename</code> for <code>&quot;eval&quot;</code>ed strings looks like <code>&quot;(eval 34)&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Each scalar <code>&quot;${&quot;_&lt;$filename&quot;}&quot;</code> contains <code>&quot;_&lt;$filename&quot;</code>. This is also the case for evaluated strings that contain subroutines, or which are currently being executed. The <code>$filename</code> for <code>&quot;eval&quot;</code>ed strings looks like <code>&quot;(eval 34)&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> After each <code>&quot;require&quot;</code>d file is compiled, but before it is executed, <code>&quot;DB::postponed(*{&quot;_&lt;$filename&quot;})&quot;</code> is called if the subroutine <code>&quot;DB::postponed&quot;</code> exists. Here, the <code>$filename</code> is the expanded name of the <code>&quot;require&quot;</code>d file, as found in the values of <code>%INC</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> After each subroutine <code>&quot;subname&quot;</code> is compiled, the existence of <code>$DB::postponed{subname}</code> is checked. If this key exists, <code>&quot;DB::postponed(subname)&quot;</code> is called if the <code>&quot;DB::postponed&quot;</code> subroutine also exists. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A hash <code>%DB::sub</code> is maintained, whose keys are subroutine names and whose values have the form <code>&quot;filename:startline-endline&quot;</code>. <code>&quot;filename&quot;</code> has the form <code>&quot;(eval 34)&quot;</code> for subroutines defined inside <code>&quot;eval&quot;</code>s. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> When the execution of your program reaches a point that can hold a breakpoint, the <code>&quot;DB::DB()&quot;</code> subroutine is called if any of the variables <code>$DB::trace</code>, <code>$DB::single</code>, or <code>$DB::signal</code> is true. These variables are not <code>&quot;local&quot;</code>izable. This feature is disabled when executing inside <code>&quot;DB::DB()&quot;</code>, including functions called from it unless <code>&quot;$^D &amp; (1&lt;&lt;30)&quot;</code> is true. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> When execution of the program reaches a subroutine call, a call to <code>&amp;DB::sub</code>(<i>args</i>) is made instead, with <code>$DB::sub</code> set to identify the called subroutine. (This doesn&#8217;t happen if the calling subroutine was compiled in the <code>&quot;DB&quot;</code> package.) <code>$DB::sub</code> normally holds the name of the called subroutine, if it has a name by which it can be looked up. Failing that, <code>$DB::sub</code> will hold a reference to the called subroutine. Either way, the <code>&amp;DB::sub</code> subroutine can use <code>$DB::sub</code> as a reference by which to call the called subroutine, which it will normally want to do. </p>
<p> If the call is to an lvalue subroutine, and <code>&amp;DB::lsub</code> is defined <code>&amp;DB::lsub</code>(<i>args</i>) is called instead, otherwise falling back to <code>&amp;DB::sub</code>(<i>args</i>). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> When execution of the program uses <code>&quot;goto&quot;</code> to enter a non-XS subroutine and the 0x80 bit is set in <code>$^P</code>, a call to <code>&amp;DB::goto</code> is made, with <code>$DB::sub</code> set to identify the subroutine being entered. The call to <code>&amp;DB::goto</code> does not replace the <code>&quot;goto&quot;</code>; the requested subroutine will still be entered once <code>&amp;DB::goto</code> has returned. <code>$DB::sub</code> normally holds the name of the subroutine being entered, if it has one. Failing that, <code>$DB::sub</code> will hold a reference to the subroutine being entered. Unlike when <code>&amp;DB::sub</code> is called, it is not guaranteed that <code>$DB::sub</code> can be used as a reference to operate on the subroutine being entered. </p>
 </dd></dl>
<p> Note that if <code>&amp;DB::sub</code> needs external data for it to work, no subroutine call is possible without it. As an example, the standard debugger&#8217;s <code>&amp;DB::sub</code> depends on the <code>$DB::deep</code> variable (it defines how many levels of recursion deep into the debugger you can go before a mandatory break). If <code>$DB::deep</code> is not defined, subroutine calls are not possible, even though <code>&amp;DB::sub</code> exists.  </p>
<h3>Writing Your Own Debugger</h3>
<p> <i>Environment Variables</i> </p>
<p> The <code>&quot;PERL5DB&quot;</code> environment variable can be used to define a debugger. For example, the minimal ``working&#8217;&#8216; debugger (it actually doesn&#8217;t do anything) consists of one line: </p>
<pre><code>  sub DB::DB {}
</code></pre>
<p> It can easily be defined like this: </p>
<pre><code>  $ PERL5DB=&quot;sub DB::DB {}&quot; perl -d your-script
</code></pre>
<p> Another brief debugger, slightly more useful, can be created with only the line: </p>
<pre><code>  sub DB::DB {print ++$i; scalar &lt;STDIN&gt;}
</code></pre>
<p> This debugger prints a number which increments for each statement encountered and waits for you to hit a newline before continuing to the next statement. </p>
<p> The following debugger is actually useful: </p>
<pre><code>  {
    package DB;
    sub DB {}
    sub sub {print ++$i, &quot; $sub\n&quot;; &amp;$sub}
  }
</code></pre>
<p> It prints the sequence number of each subroutine call and the name of the called subroutine. Note that <code>&amp;DB::sub</code> is being compiled into the package <code>&quot;DB&quot;</code> through the use of the <code>&quot;package&quot;</code> directive. </p>
<p> When it starts, the debugger reads your rc file (<i>./.perldb</i> or <i>~/.perldb</i> under Unix), which can set important options. (A subroutine (<code>&amp;afterinit</code>) can be defined here as well; it is executed after the debugger completes its own initialization.) </p>
<p> After the rc file is read, the debugger reads the <font SIZE="-1">PERLDB_OPTS</font> environment variable and uses it to set debugger options. The contents of this variable are treated as if they were the argument of an <code>&quot;o ...&quot;</code> debugger command (q.v. in ``Configurable Options&#8217;&#8216; in perldebug). </p>
<p> <i>Debugger Internal Variables</i> </p>
<p> In addition to the file and subroutine-related variables mentioned above, the debugger also maintains various magical internal variables. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>@DB::dbline</code> is an alias for <code>&quot;@{&quot;::_&lt;current_file&quot;}&quot;</code>, which holds the lines of the currently-selected file (compiled by Perl), either explicitly chosen with the debugger&#8217;s <code>&quot;f&quot;</code> command, or implicitly by flow of execution. </p>
<p> Values in this array are magical in numeric context: they compare equal to zero only if the line is not breakable. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>%DB::dbline</code> is an alias for <code>&quot;%{&quot;::_&lt;current_file&quot;}&quot;</code>, which contains breakpoints and actions keyed by line number in the currently-selected file, either explicitly chosen with the debugger&#8217;s <code>&quot;f&quot;</code> command, or implicitly by flow of execution. </p>
<p> As previously noted, individual entries (as opposed to the whole hash) are settable. Perl only cares about Boolean true here, although the values used by <i>perl5db.pl</i> have the form <code>&quot;$break_condition\0$action&quot;</code>. </p>
 </dd></dl>
<p> <i>Debugger Customization Functions</i> </p>
<p> Some functions are provided to simplify customization. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> See ``Configurable Options&#8217;&#8216; in perldebug for a description of options parsed by <code>&quot;DB::parse_options(string)&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;DB::dump_trace(skip[,count])&quot;</code> skips the specified number of frames and returns a list containing information about the calling frames (all of them, if <code>&quot;count&quot;</code> is missing). Each entry is reference to a hash with keys <code>&quot;context&quot;</code> (either <code>&quot;.&quot;</code>, <code>&quot;$&quot;</code>, or <code>&quot;@&quot;</code>), <code>&quot;sub&quot;</code> (subroutine name, or info about <code>&quot;eval&quot;</code>), <code>&quot;args&quot;</code> (<code>&quot;undef&quot;</code> or a reference to an array), <code>&quot;file&quot;</code>, and <code>&quot;line&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;DB::print_trace(FH, skip[, count[, short]])&quot;</code> prints formatted info about caller frames. The last two functions may be convenient as arguments to <code>&quot;&lt;&quot;</code>, <code>&quot;&lt;&lt;&quot;</code> commands. </p>
 </dd></dl>
<p> Note that any variables and functions that are not documented in this manpages (or in perldebug) are considered for internal use only, and as such are subject to change without notice.  </p>
<h2>Frame Listing Output Examples</h2>
<p> The <code>&quot;frame&quot;</code> option can be used to control the output of frame information. For example, contrast this expression trace: </p>
<pre><code> $ perl -de 42
 Stack dump during die enabled outside of evals.
 Loading DB routines from perl5db.pl patch level 0.94
 Emacs support available.
 Enter h or 'h h' for help.
 main::(-e:1): 0
   DB&lt;1&gt; sub foo { 14 }
   DB&lt;2&gt; sub bar { 3 }
   DB&lt;3&gt; t print foo() * bar()
 main::((eval 172):3): print foo() + bar();
 main::foo((eval 168):2):
 main::bar((eval 170):2):
 42
</code></pre>
<p> with this one, once the <code>&quot;o&quot;</code>ption <code>&quot;frame=2&quot;</code> has been set: </p>
<pre><code>   DB&lt;4&gt; o f=2
                frame = '2'
   DB&lt;5&gt; t print foo() * bar()
 3: foo() * bar()
 entering main::foo
  2: sub foo { 14 };
 exited main::foo
 entering main::bar
  2: sub bar { 3 };
 exited main::bar
 42
</code></pre>
<p> By way of demonstration, we present below a laborious listing resulting from setting your <code>&quot;PERLDB_OPTS&quot;</code> environment variable to the value <code>&quot;f=n N&quot;</code>, and running <i>perl -d -V</i> from the command line. Examples using various values of <code>&quot;n&quot;</code> are shown to give you a feel for the difference between settings. Long though it may be, this is not a complete listing, but only excerpts. </p>
<dl>
<dt>1.</dt>
<dd> <pre><code> entering main::BEGIN
  entering Config::BEGIN
   Package lib/Exporter.pm.
   Package lib/Carp.pm.
  Package lib/Config.pm.
  entering Config::TIEHASH
  entering Exporter::import
   entering Exporter::export
 entering Config::myconfig
  entering Config::FETCH
  entering Config::FETCH
  entering Config::FETCH
  entering Config::FETCH
</code></pre>
 </dd>
<dt>2.</dt>
<dd> <pre><code> entering main::BEGIN
  entering Config::BEGIN
   Package lib/Exporter.pm.
   Package lib/Carp.pm.
  exited Config::BEGIN
  Package lib/Config.pm.
  entering Config::TIEHASH
  exited Config::TIEHASH
  entering Exporter::import
   entering Exporter::export
   exited Exporter::export
  exited Exporter::import
 exited main::BEGIN
 entering Config::myconfig
  entering Config::FETCH
  exited Config::FETCH
  entering Config::FETCH
  exited Config::FETCH
  entering Config::FETCH
</code></pre>
 </dd>
<dt>3.</dt>
<dd> <pre><code> in $=main::BEGIN() from /dev/null:0
  in $=Config::BEGIN() from lib/Config.pm:2
   Package lib/Exporter.pm.
   Package lib/Carp.pm.
  Package lib/Config.pm.
  in $=Config::TIEHASH('Config') from lib/Config.pm:644
  in $=Exporter::import('Config', 'myconfig', 'config_vars') from /dev/null:0
   in $=Exporter::export('Config', 'main', 'myconfig', 'config_vars') from li
 in @=Config::myconfig() from /dev/null:0
  in $=Config::FETCH(ref(Config), 'package') from lib/Config.pm:574
  in $=Config::FETCH(ref(Config), 'baserev') from lib/Config.pm:574
  in $=Config::FETCH(ref(Config), 'PERL_VERSION') from lib/Config.pm:574
  in $=Config::FETCH(ref(Config), 'PERL_SUBVERSION') from lib/Config.pm:574
  in $=Config::FETCH(ref(Config), 'osname') from lib/Config.pm:574
  in $=Config::FETCH(ref(Config), 'osvers') from lib/Config.pm:574
</code></pre>
 </dd>
<dt>4.</dt>
<dd> <pre><code> in $=main::BEGIN() from /dev/null:0
  in $=Config::BEGIN() from lib/Config.pm:2
   Package lib/Exporter.pm.
   Package lib/Carp.pm.
  out $=Config::BEGIN() from lib/Config.pm:0
  Package lib/Config.pm.
  in $=Config::TIEHASH('Config') from lib/Config.pm:644
  out $=Config::TIEHASH('Config') from lib/Config.pm:644
  in $=Exporter::import('Config', 'myconfig', 'config_vars') from /dev/null:0
   in $=Exporter::export('Config', 'main', 'myconfig', 'config_vars') from lib/
   out $=Exporter::export('Config', 'main', 'myconfig', 'config_vars') from lib/
  out $=Exporter::import('Config', 'myconfig', 'config_vars') from /dev/null:0
 out $=main::BEGIN() from /dev/null:0
 in @=Config::myconfig() from /dev/null:0
  in $=Config::FETCH(ref(Config), 'package') from lib/Config.pm:574
  out $=Config::FETCH(ref(Config), 'package') from lib/Config.pm:574
  in $=Config::FETCH(ref(Config), 'baserev') from lib/Config.pm:574
  out $=Config::FETCH(ref(Config), 'baserev') from lib/Config.pm:574
  in $=Config::FETCH(ref(Config), 'PERL_VERSION') from lib/Config.pm:574
  out $=Config::FETCH(ref(Config), 'PERL_VERSION') from lib/Config.pm:574
  in $=Config::FETCH(ref(Config), 'PERL_SUBVERSION') from lib/Config.pm:574
</code></pre>
 </dd>
<dt>5.</dt>
<dd> <pre><code> in $=main::BEGIN() from /dev/null:0
  in $=Config::BEGIN() from lib/Config.pm:2
   Package lib/Exporter.pm.
   Package lib/Carp.pm.
  out $=Config::BEGIN() from lib/Config.pm:0
  Package lib/Config.pm.
  in $=Config::TIEHASH('Config') from lib/Config.pm:644
  out $=Config::TIEHASH('Config') from lib/Config.pm:644
  in $=Exporter::import('Config', 'myconfig', 'config_vars') from /dev/null:0
   in $=Exporter::export('Config', 'main', 'myconfig', 'config_vars') from lib/E
   out $=Exporter::export('Config', 'main', 'myconfig', 'config_vars') from lib/E
  out $=Exporter::import('Config', 'myconfig', 'config_vars') from /dev/null:0
 out $=main::BEGIN() from /dev/null:0
 in @=Config::myconfig() from /dev/null:0
  in $=Config::FETCH('Config=HASH(0x1aa444)', 'package') from lib/Config.pm:574
  out $=Config::FETCH('Config=HASH(0x1aa444)', 'package') from lib/Config.pm:574
  in $=Config::FETCH('Config=HASH(0x1aa444)', 'baserev') from lib/Config.pm:574
  out $=Config::FETCH('Config=HASH(0x1aa444)', 'baserev') from lib/Config.pm:574
</code></pre>
 </dd>
<dt>6.</dt>
<dd> <pre><code> in $=CODE(0x15eca4)() from /dev/null:0
  in $=CODE(0x182528)() from lib/Config.pm:2
   Package lib/Exporter.pm.
  out $=CODE(0x182528)() from lib/Config.pm:0
  scalar context return from CODE(0x182528): undef
  Package lib/Config.pm.
  in $=Config::TIEHASH('Config') from lib/Config.pm:628
  out $=Config::TIEHASH('Config') from lib/Config.pm:628
  scalar context return from Config::TIEHASH: empty hash
  in $=Exporter::import('Config', 'myconfig', 'config_vars') from /dev/null:0
   in $=Exporter::export('Config', 'main', 'myconfig', 'config_vars') from lib/Exporter.pm:171
   out $=Exporter::export('Config', 'main', 'myconfig', 'config_vars') from lib/Exporter.pm:171
   scalar context return from Exporter::export: ''
  out $=Exporter::import('Config', 'myconfig', 'config_vars') from /dev/null:0
  scalar context return from Exporter::import: ''
</code></pre>
 </dd></dl>
<p> In all cases shown above, the line indentation shows the call tree. If bit 2 of <code>&quot;frame&quot;</code> is set, a line is printed on exit from a subroutine as well. If bit 4 is set, the arguments are printed along with the caller info. If bit 8 is set, the arguments are printed even if they are tied or references. If bit 16 is set, the return value is printed, too. </p>
<p> When a package is compiled, a line like this </p>
<pre><code>    Package lib/Carp.pm.
</code></pre>
<p> is printed with proper indentation.  </p>
<h2>Debugging Regular Expressions</h2>
<p> There are two ways to enable debugging output for regular expressions. </p>
<p> If your perl is compiled with <code>&quot;-DDEBUGGING&quot;</code>, you may use the <code>-Dr</code> flag on the command line, and <code>&quot;-Drv&quot;</code> for more verbose information. </p>
<p> Otherwise, one can <code>&quot;use re &#8216;debug&#8217;&quot;</code>, which has effects at both compile time and run time. Since Perl 5.9.5, this pragma is lexically scoped.  </p>
<h3>Compile-time Output</h3>
<p> The debugging output at compile time looks like this: </p>
<pre><code>  Compiling REx '[bc]d(ef*g)+h[ij]k$'
  size 45 Got 364 bytes for offset annotations.
  first at 1
  rarest char g at 0
  rarest char d at 0
     1: ANYOF[bc](12)
    12: EXACT &lt;d&gt;(14)
    14: CURLYX[0] {1,32767}(28)
    16: OPEN1(18)
    18: EXACT &lt;e&gt;(20)
    20: STAR(23)
    21: EXACT &lt;f&gt;(0)
    23: EXACT &lt;g&gt;(25)
    25: CLOSE1(27)
    27: WHILEM[1/1](0)
    28: NOTHING(29)
    29: EXACT &lt;h&gt;(31)
    31: ANYOF[ij](42)
    42: EXACT &lt;k&gt;(44)
    44: EOL(45)
    45: END(0)
  anchored 'de' at 1 floating 'gh' at 3..2147483647 (checking floating)
        stclass 'ANYOF[bc]' minlen 7
  Offsets: [45]
        1[4] 0[0] 0[0] 0[0] 0[0] 0[0] 0[0] 0[0] 0[0] 0[0] 0[0] 5[1]
        0[0] 12[1] 0[0] 6[1] 0[0] 7[1] 0[0] 9[1] 8[1] 0[0] 10[1] 0[0]
        11[1] 0[0] 12[0] 12[0] 13[1] 0[0] 14[4] 0[0] 0[0] 0[0] 0[0]
        0[0] 0[0] 0[0] 0[0] 0[0] 0[0] 18[1] 0[0] 19[1] 20[0]
  Omitting $` $&amp; $' support.
</code></pre>
<p> The first line shows the pre-compiled form of the regex. The second shows the size of the compiled form (in arbitrary units, usually 4-byte words) and the total number of bytes allocated for the offset/length table, usually 4+<code>&quot;size&quot;</code>*8. The next line shows the label <i>id</i> of the first node that does a match. </p>
<p> The </p>
<pre><code>  anchored 'de' at 1 floating 'gh' at 3..2147483647 (checking floating)
        stclass 'ANYOF[bc]' minlen 7
</code></pre>
<p> line (split into two lines above) contains optimizer information. In the example shown, the optimizer found that the match should contain a substring <code>&quot;de&quot;</code> at offset 1, plus substring <code>&quot;gh&quot;</code> at some offset between 3 and infinity. Moreover, when checking for these substrings (to abandon impossible matches quickly), Perl will check for the substring <code>&quot;gh&quot;</code> before checking for the substring <code>&quot;de&quot;</code>. The optimizer may also use the knowledge that the match starts (at the <code>&quot;first&quot;</code> <i>id</i>) with a character class, and no string shorter than 7 characters can possibly match. </p>
<p> The fields of interest which may appear in this line are </p>
<dl>
<dt>&quot;anchored&quot; <i></i><font SIZE="-1"><i>STRING</i></font><i></i> &quot;at&quot; <i></i><font SIZE="-1"><i>POS</i></font><i></i></dt>
<dd>  </dd>
<dt>&quot;floating&quot; <i></i><font SIZE="-1"><i>STRING</i></font><i></i> &quot;at&quot; <i></i><font SIZE="-1"><i>POS1..POS2</i></font><i></i></dt>
<dd> <p> See above. </p>
 </dd>
<dt>&quot;matching floating/anchored&quot;</dt>
<dd> <p> Which substring to check first. </p>
 </dd>
<dt>&quot;minlen&quot;</dt>
<dd> <p> The minimal length of the match. </p>
 </dd>
<dt>&quot;stclass&quot; <i></i><font SIZE="-1"><i>TYPE</i></font><i></i></dt>
<dd> <p> Type of first matching node. </p>
 </dd>
<dt>&quot;noscan&quot;</dt>
<dd> <p> Don&#8217;t scan for the found substrings. </p>
 </dd>
<dt>&quot;isall&quot;</dt>
<dd> <p> Means that the optimizer information is all that the regular expression contains, and thus one does not need to enter the regex engine at all. </p>
 </dd>
<dt>&quot;GPOS&quot;</dt>
<dd> <p> Set if the pattern contains <code>&quot;\G&quot;</code>. </p>
 </dd>
<dt>&quot;plus&quot;</dt>
<dd> <p> Set if the pattern starts with a repeated char (as in <code>&quot;x+y&quot;</code>). </p>
 </dd>
<dt>&quot;implicit&quot;</dt>
<dd> <p> Set if the pattern starts with <code>&quot;.*&quot;</code>. </p>
 </dd>
<dt>&quot;with eval&quot;</dt>
<dd> <p> Set if the pattern contain eval-groups, such as <code>&quot;(?{ code })&quot;</code> and <code>&quot;(??{ code })&quot;</code>. </p>
 </dd>
<dt>&quot;anchored(TYPE)&quot;</dt>
<dd> <p> If the pattern may match only at a handful of places, with <code>&quot;TYPE&quot;</code> being <code>&quot;SBOL&quot;</code>, <code>&quot;MBOL&quot;</code>, or <code>&quot;GPOS&quot;</code>. See the table below. </p>
 </dd></dl>
<p> If a substring is known to match at end-of-line only, it may be followed by <code>&quot;$&quot;</code>, as in <code>&quot;floating &#8216;k&#8217;$&quot;</code>. </p>
<p> The optimizer-specific information is used to avoid entering (a slow) regex engine on strings that will not definitely match. If the <code>&quot;isall&quot;</code> flag is set, a call to the regex engine may be avoided even when the optimizer found an appropriate place for the match. </p>
<p> Above the optimizer section is the list of <i>nodes</i> of the compiled form of the regex. Each line has format </p>
<p> <code>&quot; &quot;</code><i>id</i>: <i></i><font SIZE="-1"><i>TYPE</i></font><i></i> <i>OPTIONAL-INFO</i> (<i>next-id</i>)  </p>
<h3>Types of Nodes</h3>
<p> Here are the current possible types, with short descriptions: </p>
<pre><code> # TYPE arg-description [num-args] [longjump-len] DESCRIPTION
 # Exit points
 END no End of program.
 SUCCEED no Return from a subroutine, basically.
 # Line Start Anchors:
 SBOL no Match &quot;&quot; at beginning of line: /^/, /\A/
 MBOL no Same, assuming multiline: /^/m
 # Line End Anchors:
 SEOL no Match &quot;&quot; at end of line: /$/
 MEOL no Same, assuming multiline: /$/m
 EOS no Match &quot;&quot; at end of string: /\z/
 # Match Start Anchors:
 GPOS no Matches where last m//g left off.
 # Word Boundary Opcodes:
 BOUND no Like BOUNDA for non-utf8, otherwise match
                             &quot;&quot; between any Unicode \w\W or \W\w
 BOUNDL no Like BOUND/BOUNDU, but \w and \W are
                             defined by current locale
 BOUNDU no Match &quot;&quot; at any boundary of a given type
                             using /u rules.
 BOUNDA no Match &quot;&quot; at any boundary between \w\W or
                             \W\w, where \w is [_a-zA-Z0-9]
 NBOUND no Like NBOUNDA for non-utf8, otherwise match
                             &quot;&quot; between any Unicode \w\w or \W\W
 NBOUNDL no Like NBOUND/NBOUNDU, but \w and \W are
                             defined by current locale
 NBOUNDU no Match &quot;&quot; at any non-boundary of a given
                             type using using /u rules.
 NBOUNDA no Match &quot;&quot; betweeen any \w\w or \W\W, where
                             \w is [_a-zA-Z0-9]
 # [Special] alternatives:
 REG_ANY no Match any one character (except newline).
 SANY no Match any one character.
 ANYOF sv Match character in (or not in) this class,
                  charclass single char match only
 ANYOFD sv Like ANYOF, but /d is in effect
                  charclass
 ANYOFL sv Like ANYOF, but /l is in effect
                  charclass
 ANYOFPOSIXL sv Like ANYOFL, but matches [[:posix:]]
                  charclass_ classes
                  posixl
 ANYOFH sv 1 Like ANYOF, but only has &quot;High&quot; matches,
                             none in the bitmap; non-zero flags &quot;f&quot;
                             means &quot;f&quot; is the first UTF-8 byte shared in
                             common by all code points matched
 ANYOFM byte 1 Like ANYOF, but matches an invariant byte
                             as determined by the mask and arg
 NANYOFM byte 1 complement of ANYOFM
 # POSIX Character Classes:
 POSIXD none Some [[:class:]] under /d; the FLAGS field
                             gives which one
 POSIXL none Some [[:class:]] under /l; the FLAGS field
                             gives which one
 POSIXU none Some [[:class:]] under /u; the FLAGS field
                             gives which one
 POSIXA none Some [[:class:]] under /a; the FLAGS field
                             gives which one
 NPOSIXD none complement of POSIXD, [[:^class:]]
 NPOSIXL none complement of POSIXL, [[:^class:]]
 NPOSIXU none complement of POSIXU, [[:^class:]]
 NPOSIXA none complement of POSIXA, [[:^class:]]
 CLUMP no Match any extended grapheme cluster
                             sequence
 # Alternation
 # BRANCH The set of branches constituting a single choice are
 # hooked together with their &quot;next&quot; pointers, since
 # precedence prevents anything being concatenated to
 # any individual branch. The &quot;next&quot; pointer of the last
 # BRANCH in a choice points to the thing following the
 # whole choice. This is also where the final &quot;next&quot;
 # pointer of each individual branch points; each branch
 # starts with the operand node of a BRANCH node.
 #
 BRANCH node Match this alternative, or the next...
 # Literals
 EXACT str Match this string (preceded by length).
 EXACTL str Like EXACT, but /l is in effect (used so
                             locale-related warnings can be checked
                             for).
 EXACTF str Match this string using /id rules (w/len);
                             (string not UTF-8, not guaranteed to be
                             folded).
 EXACTFL str Match this string using /il rules (w/len);
                             (string not guaranteed to be folded).
 EXACTFU str Match this string using /iu rules (w/len);
                             (string folded iff in UTF-8; non-UTF8
                             folded length &lt;= unfolded).
 EXACTFAA str Match this string using /iaa rules (w/len)
                             (string folded iff in UTF-8; non-UTF8
                             folded length &lt;= unfolded).
 EXACTFUP str Match this string using /iu rules (w/len);
                             (string not UTF-8, not guaranteed to be
                             folded; and its Problematic).
 EXACTFLU8 str Like EXACTFU, but use /il, UTF-8, folded,
                             and everything in it is above 255.
 EXACTFAA_NO_TRIE str Match this string using /iaa rules (w/len)
                             (string not UTF-8, not guaranteed to be
                             folded, not currently trie-able).
 EXACT_ONLY8 str Like EXACT, but only UTF-8 encoded targets
                             can match
 EXACTFU_ONLY8 str Like EXACTFU, but only UTF-8 encoded
                             targets can match
 EXACTFU_S_EDGE str /di rules, but nothing in it precludes /ui,
                             except begins and/or ends with [Ss];
                             (string not UTF-8; compile-time only).
 # Do nothing types
 NOTHING no Match empty string.
 # A variant of above which delimits a group, thus stops optimizations
 TAIL no Match empty string. Can jump here from
                             outside.
 # Loops
 # STAR,PLUS '?', and complex '*' and '+', are implemented as
 # circular BRANCH structures. Simple cases
 # (one character per match) are implemented with STAR
 # and PLUS for speed and to minimize recursive plunges.
 #
 STAR node Match this (simple) thing 0 or more times.
 PLUS node Match this (simple) thing 1 or more times.
 CURLY sv 2 Match this simple thing {n,m} times.
 CURLYN no 2 Capture next-after-this simple thing
 CURLYM no 2 Capture this medium-complex thing {n,m}
                             times.
 CURLYX sv 2 Match this complex thing {n,m} times.
 # This terminator creates a loop structure for CURLYX
 WHILEM no Do curly processing and see if rest
                             matches.
 # Buffer related
 # OPEN,CLOSE,GROUPP ...are numbered at compile time.
 OPEN num 1 Mark this point in input as start of #n.
 CLOSE num 1 Close corresponding OPEN of #n.
 SROPEN none Same as OPEN, but for script run
 SRCLOSE none Close preceding SROPEN
 REF num 1 Match some already matched string
 REFF num 1 Match already matched string, using /di
                             rules.
 REFFL num 1 Match already matched string, using /li
                             rules.
 REFFU num 1 Match already matched string, usng /ui.
 REFFA num 1 Match already matched string, using /aai
                             rules.
 # Named references. Code in regcomp.c assumes that these all are after
 # the numbered references
 NREF no-sv 1 Match some already matched string
 NREFF no-sv 1 Match already matched string, using /di
                             rules.
 NREFFL no-sv 1 Match already matched string, using /li
                             rules.
 NREFFU num 1 Match already matched string, using /ui
                             rules.
 NREFFA num 1 Match already matched string, using /aai
                             rules.
 # Support for long RE
 LONGJMP off 1 1 Jump far away.
 BRANCHJ off 1 1 BRANCH with long offset.
 # Special Case Regops
 IFMATCH off 1 1 Succeeds if the following matches; non-zero
                             flags &quot;f&quot;, next_off &quot;o&quot; means lookbehind
                             assertion starting &quot;f..(f-o)&quot; characters
                             before current
 UNLESSM off 1 1 Fails if the following matches; non-zero
                             flags &quot;f&quot;, next_off &quot;o&quot; means lookbehind
                             assertion starting &quot;f..(f-o)&quot; characters
                             before current
 SUSPEND off 1 1 &quot;Independent&quot; sub-RE.
 IFTHEN off 1 1 Switch, should be preceded by switcher.
 GROUPP num 1 Whether the group matched.
 # The heavy worker
 EVAL evl/flags Execute some Perl code.
                  2L
 # Modifiers
 MINMOD no Next operator is not greedy.
 LOGICAL no Next opcode should set the flag only.
 # This is not used yet
 RENUM off 1 1 Group with independently numbered parens.
 # Trie Related
 # Behave the same as A|LIST|OF|WORDS would. The '..C' variants
 # have inline charclass data (ascii only), the 'C' store it in the
 # structure.
 TRIE trie 1 Match many EXACT(F[ALU]?)? at once.
                             flags==type
 TRIEC trie Same as TRIE, but with embedded charclass
                  charclass data
 AHOCORASICK trie 1 Aho Corasick stclass. flags==type
 AHOCORASICKC trie Same as AHOCORASICK, but with embedded
                  charclass charclass data
 # Regex Subroutines
 GOSUB num/ofs 2L recurse to paren arg1 at (signed) ofs arg2
 # Special conditionals
 NGROUPP no-sv 1 Whether the group matched.
 INSUBP num 1 Whether we are in a specific recurse.
 DEFINEP none 1 Never execute directly.
 # Backtracking Verbs
 ENDLIKE none Used only for the type field of verbs
 OPFAIL no-sv 1 Same as (?!), but with verb arg
 ACCEPT no-sv/num Accepts the current matched string, with
                  2L verbar
 # Verbs With Arguments
 VERB no-sv 1 Used only for the type field of verbs
 PRUNE no-sv 1 Pattern fails at this startpoint if no-
                             backtracking through this
 MARKPOINT no-sv 1 Push the current location for rollback by
                             cut.
 SKIP no-sv 1 On failure skip forward (to the mark)
                             before retrying
 COMMIT no-sv 1 Pattern fails outright if backtracking
                             through this
 CUTGROUP no-sv 1 On failure go to the next alternation in
                             the group
 # Control what to keep in $&amp;.
 KEEPS no $&amp; begins here.
 # New charclass like patterns
 LNBREAK none generic newline pattern
 # SPECIAL REGOPS
 # This is not really a node, but an optimized away piece of a &quot;long&quot;
 # node. To simplify debugging output, we mark it as if it were a node
 OPTIMIZED off Placeholder for dump.
 # Special opcode with the property that no opcode in a compiled program
 # will ever be of this type. Thus it can be used as a flag value that
 # no other opcode has been seen. END is used similarly, in that an END
 # node cant be optimized. So END implies &quot;unoptimizable&quot; and PSEUDO
 # mean &quot;not seen anything to optimize yet&quot;.
 PSEUDO off Pseudo opcode for internal use.
</code></pre>
<p> Following the optimizer information is a dump of the offset/length table, here split across several lines: </p>
<pre><code>  Offsets: [45]
        1[4] 0[0] 0[0] 0[0] 0[0] 0[0] 0[0] 0[0] 0[0] 0[0] 0[0] 5[1]
        0[0] 12[1] 0[0] 6[1] 0[0] 7[1] 0[0] 9[1] 8[1] 0[0] 10[1] 0[0]
        11[1] 0[0] 12[0] 12[0] 13[1] 0[0] 14[4] 0[0] 0[0] 0[0] 0[0]
        0[0] 0[0] 0[0] 0[0] 0[0] 0[0] 18[1] 0[0] 19[1] 20[0]
</code></pre>
<p> The first line here indicates that the offset/length table contains 45 entries. Each entry is a pair of integers, denoted by <code>&quot;offset[length]&quot;</code>. Entries are numbered starting with 1, so entry #1 here is <code>&quot;1[4]&quot;</code> and entry #12 is <code>&quot;5[1]&quot;</code>. <code>&quot;1[4]&quot;</code> indicates that the node labeled <code>&quot;1:&quot;</code> (the <code>&quot;1: ANYOF[bc]&quot;</code>) begins at character position 1 in the pre-compiled form of the regex, and has a length of 4 characters. <code>&quot;5[1]&quot;</code> in position 12 indicates that the node labeled <code>&quot;12:&quot;</code> (the <code>&quot;12: EXACT &lt;d&gt;&quot;</code>) begins at character position 5 in the pre-compiled form of the regex, and has a length of 1 character. <code>&quot;12[1]&quot;</code> in position 14 indicates that the node labeled <code>&quot;14:&quot;</code> (the <code>&quot;14: CURLYX[0] {1,32767}&quot;</code>) begins at character position 12 in the pre-compiled form of the regex, and has a length of 1 character---that is, it corresponds to the <code>&quot;+&quot;</code> symbol in the precompiled regex. </p>
<p> <code>&quot;0[0]&quot;</code> items indicate that there is no corresponding node.  </p>
<h3>Run-time Output</h3>
<p> First of all, when doing a match, one may get no run-time output even if debugging is enabled. This means that the regex engine was never entered and that all of the job was therefore done by the optimizer. </p>
<p> If the regex engine was entered, the output may look like this: </p>
<pre><code>  Matching '[bc]d(ef*g)+h[ij]k$' against 'abcdefg__gh__'
    Setting an EVAL scope, savestack=3
     2 &lt;ab&gt; &lt;cdefg__gh_&gt; | 1: ANYOF
     3 &lt;abc&gt; &lt;defg__gh_&gt; | 11: EXACT &lt;d&gt;
     4 &lt;abcd&gt; &lt;efg__gh_&gt; | 13: CURLYX {1,32767}
     4 &lt;abcd&gt; &lt;efg__gh_&gt; | 26: WHILEM
                                0 out of 1..32767 cc=effff31c
     4 &lt;abcd&gt; &lt;efg__gh_&gt; | 15: OPEN1
     4 &lt;abcd&gt; &lt;efg__gh_&gt; | 17: EXACT &lt;e&gt;
     5 &lt;abcde&gt; &lt;fg__gh_&gt; | 19: STAR
                             EXACT &lt;f&gt; can match 1 times out of 32767...
    Setting an EVAL scope, savestack=3
     6 &lt;bcdef&gt; &lt;g__gh__&gt; | 22: EXACT &lt;g&gt;
     7 &lt;bcdefg&gt; &lt;__gh__&gt; | 24: CLOSE1
     7 &lt;bcdefg&gt; &lt;__gh__&gt; | 26: WHILEM
                                    1 out of 1..32767 cc=effff31c
    Setting an EVAL scope, savestack=12
     7 &lt;bcdefg&gt; &lt;__gh__&gt; | 15: OPEN1
     7 &lt;bcdefg&gt; &lt;__gh__&gt; | 17: EXACT &lt;e&gt;
       restoring \1 to4(4)..7
                                    failed, try continuation...
     7 &lt;bcdefg&gt; &lt;__gh__&gt; | 27: NOTHING
     7 &lt;bcdefg&gt; &lt;__gh__&gt; | 28: EXACT &lt;h&gt;
                                    failed...
                                failed...
</code></pre>
<p> The most significant information in the output is about the particular <i>node</i> of the compiled regex that is currently being tested against the target string. The format of these lines is </p>
<p> <code>&quot; &quot;</code><i>STRING-OFFSET</i> &lt;<i>PRE-STRING</i>&gt; &lt;<i>POST-STRING</i>&gt; |<i></i><font SIZE="-1"><i>ID</i></font><i></i>: <i></i><font SIZE="-1"><i>TYPE</i></font><i></i> </p>
<p> The <i></i><font SIZE="-1"><i>TYPE</i></font><i></i> info is indented with respect to the backtracking level. Other incidental information appears interspersed within.  </p>
<h2>Debugging Perl Memory Usage</h2>
<p> Perl is a profligate wastrel when it comes to memory use. There is a saying that to estimate memory usage of Perl, assume a reasonable algorithm for memory allocation, multiply that estimate by 10, and while you still may miss the mark, at least you won&#8217;t be quite so astonished. This is not absolutely true, but may provide a good grasp of what happens. </p>
<p> Assume that an integer cannot take less than 20 bytes of memory, a float cannot take less than 24 bytes, a string cannot take less than 32 bytes (all these examples assume 32-bit architectures, the result are quite a bit worse on 64-bit architectures). If a variable is accessed in two of three different ways (which require an integer, a float, or a string), the memory footprint may increase yet another 20 bytes. A sloppy <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) implementation can inflate these numbers dramatically. </p>
<p> On the opposite end of the scale, a declaration like </p>
<pre><code>  sub foo;
</code></pre>
<p> may take up to 500 bytes of memory, depending on which release of Perl you&#8217;re running. </p>
<p> Anecdotal estimates of source-to-compiled code bloat suggest an eightfold increase. This means that the compiled form of reasonable (normally commented, properly indented etc.) code will take about eight times more space in memory than the code took on disk. </p>
<p> The <code>-DL</code> command-line switch is obsolete since circa Perl 5.6.0 (it was available only if Perl was built with <code>&quot;-DDEBUGGING&quot;</code>). The switch was used to track Perl&#8217;s memory allocations and possible memory leaks. These days the use of malloc debugging tools like <i>Purify</i> or <i>valgrind</i> is suggested instead. See also ``<font SIZE="-1">PERL_MEM_LOG&#8217;&#8216;</font> in perlhacktips. </p>
<p> One way to find out how much memory is being used by Perl data structures is to install the Devel::Size module from <font SIZE="-1">CPAN:</font> it gives you the minimum number of bytes required to store a particular data structure. Please be mindful of the difference between the <code>size()</code> and <code>total_size()</code>. </p>
<p> If Perl has been compiled using Perl&#8217;s malloc you can analyze Perl memory usage by setting <code>$ENV</code>{<font SIZE="-1">PERL_DEBUG_MSTATS</font>}.  </p>
<h3>Using $ENV{PERL_DEBUG_MSTATS}</h3>
<p> If your perl is using Perl&#8217;s <code>malloc()</code> and was compiled with the necessary switches (this is the default), then it will print memory usage statistics after compiling your code when <code>&quot;$ENV{PERL_DEBUG_MSTATS} &gt; 1&quot;</code>, and before termination of the program when <code>&quot;$ENV{PERL_DEBUG_MSTATS} &gt;= 1&quot;</code>. The report format is similar to the following example: </p>
<pre><code> $ PERL_DEBUG_MSTATS=2 perl -e &quot;require Carp&quot;
 Memory allocation statistics after compilation: (buckets4(4)..8188(8192)
    14216 free: 130 117 28 7 9 0 2 2 1 0 0
                437 61 36 0 5
    60924 used: 125 137 161 55 7 8 6 16 2 0 1
                 74 109 304 84 20
 Total sbrk(): 77824/21:119. Odd ends: pad+heads+chain+tail: 0+636+0+2048.
 Memory allocation statistics after execution: (buckets4(4)..8188(8192)
    30888 free: 245 78 85 13 6 2 1 3 2 0 1
                315 162 39 42 11
   175816 used: 265 176 1112 111 26 22 11 27 2 1 1
                196 178 1066 798 39
 Total sbrk(): 215040/47:145. Odd ends: pad+heads+chain+tail: 0+2192+0+6144.
</code></pre>
<p> It is possible to ask for such a statistic at arbitrary points in your execution using the <code>mstat()</code> function out of the standard Devel::Peek module. </p>
<p> Here is some explanation of that format: </p>
<dl>
<dt>&quot;buckets SMALLEST(APPROX)..GREATEST(APPROX)&quot;</dt>
<dd> <p> Perl&#8217;s <code>malloc()</code> uses bucketed allocations. Every request is rounded up to the closest bucket size available, and a bucket is taken from the pool of buckets of that size. </p>
<p> The line above describes the limits of buckets currently in use. Each bucket has two sizes: memory footprint and the maximal size of user data that can fit into this bucket. Suppose in the above example that the smallest bucket were size 4. The biggest bucket would have usable size 8188, and the memory footprint would be 8192. </p>
<p> In a Perl built for debugging, some buckets may have negative usable size. This means that these buckets cannot (and will not) be used. For larger buckets, the memory footprint may be one page greater than a power of 2. If so, the corresponding power of two is printed in the <code>&quot;APPROX&quot;</code> field above. </p>
 </dd>
<dt>Free/Used</dt>
<dd> <p> The 1 or 2 rows of numbers following that correspond to the number of buckets of each size between <code>&quot;SMALLEST&quot;</code> and <code>&quot;GREATEST&quot;</code>. In the first row, the sizes (memory footprints) of buckets are powers of two---or possibly one page greater. In the second row, if present, the memory footprints of the buckets are between the memory footprints of two buckets ``above&#8217;&#8216;. </p>
<p> For example, suppose under the previous example, the memory footprints were </p>
<pre><code>   free: 8 16 32 64 128 256 512 1024 2048 4096 8192
           4 12 24 48 80
</code></pre>
<p> With a non-<code>&quot;DEBUGGING&quot;</code> perl, the buckets starting from <code>128</code> have a 4-byte overhead, and thus an 8192-long bucket may take up to 8188-byte allocations. </p>
 </dd>
<dt>&quot;Total sbrk(): SBRKed/SBRKs:CONTINUOUS&quot;</dt>
<dd> <p> The first two fields give the total amount of memory perl <code><a href="/docs/linux/man/2-sbrk/">sbrk</a></code>(2)ed (ess-broken? :-) and number of <code><a href="/docs/linux/man/2-sbrk/">sbrk</a></code>(2)s used. The third number is what perl thinks about continuity of returned chunks. So long as this number is positive, <code>malloc()</code> will assume that it is probable that <code><a href="/docs/linux/man/2-sbrk/">sbrk</a></code>(2) will provide continuous memory. </p>
<p> Memory allocated by external libraries is not counted. </p>
 </dd>
<dt>&quot;pad: 0&quot;</dt>
<dd> <p> The amount of <code><a href="/docs/linux/man/2-sbrk/">sbrk</a></code>(2)ed memory needed to keep buckets aligned. </p>
 </dd>
<dt>&quot;heads: 2192&quot;</dt>
<dd> <p> Although memory overhead of bigger buckets is kept inside the bucket, for smaller buckets, it is kept in separate areas. This field gives the total size of these areas. </p>
 </dd>
<dt>&quot;chain: 0&quot;</dt>
<dd> <p> <code>malloc()</code> may want to subdivide a bigger bucket into smaller buckets. If only a part of the deceased bucket is left unsubdivided, the rest is kept as an element of a linked list. This field gives the total size of these chunks. </p>
 </dd>
<dt>&quot;tail: 6144&quot;</dt>
<dd> <p> To minimize the number of <code><a href="/docs/linux/man/2-sbrk/">sbrk</a></code>(2)s, <code>malloc()</code> asks for more memory. This field gives the size of the yet unused part, which is <code><a href="/docs/linux/man/2-sbrk/">sbrk</a></code>(2)ed, but never touched. </p>
 </dd></dl>
<h2>SEE ALSO</h2>
<p> perldebug, perlguts, perlrun re, and Devel::DProf. </p>
