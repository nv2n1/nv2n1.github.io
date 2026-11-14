---
title: "perl5100delta(1)"
name: "perl5100delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5100delta/"
description: "perl5100delta – what is new for perl 5.10.0"
---

<h2 class="name">NAME</h2>
<p> perl5100delta &#8211; what is new for perl 5.10.0 </p>
<h2>DESCRIPTION</h2>
<p> This document describes the differences between the 5.8.8 release and the 5.10.0 release. </p>
<p> Many of the bug fixes in 5.10.0 were already seen in the 5.8.X maintenance releases; they are not duplicated here and are documented in the set of man pages named perl58[1-8]?delta.</p>
<h2>Core Enhancements</h2>
<h3>The feature pragma</h3>
<p> The <tt>&quot;feature&quot;</tt> pragma is used to enable new syntax that would break Perl&#8217;s backwards-compatibility with older releases of the language. It&#8217;s a lexical pragma, like <tt>&quot;strict&quot;</tt> or <tt>&quot;warnings&quot;</tt>. </p>
<p> Currently the following new features are available: <tt>&quot;switch&quot;</tt> (adds a switch statement), <tt>&quot;say&quot;</tt> (adds a <tt>&quot;say&quot;</tt> built-in function), and <tt>&quot;state&quot;</tt> (adds a <tt>&quot;state&quot;</tt> keyword for declaring &#8220;static&#8221; variables). Those features are described in their own sections of this document. </p>
<p> The <tt>&quot;feature&quot;</tt> pragma is also implicitly loaded when you require a minimal perl version (with the <tt>&quot;use VERSION&quot;</tt> construct) greater than, or equal to, 5.9.5. See feature for details.</p>
<h3>New <code>-E</code> command-line switch</h3>
<p> <code>-E</code> is equivalent to <code>-e</code>, but it implicitly enables all optional features (like <tt>&quot;use feature &quot;:5.10&quot;&quot;</tt>).</p>
<h3>Defined-or operator</h3>
<p> A new operator <tt>&quot;//&quot;</tt> (defined-or) has been implemented. The following expression: </p>
<pre>
    $a // $b
</pre>
<p> is merely equivalent to </p>
<pre>
   defined $a ? $a : $b
</pre>
<p> and the statement </p>
<pre>
   $c //= $d;
</pre>
<p> can now be used instead of </p>
<pre>
   $c = $d unless defined $c;
</pre>
<p> The <tt>&quot;//&quot;</tt> operator has the same precedence and associativity as <tt>&quot;||&quot;</tt>. Special care has been taken to ensure that this operator Do What You Mean while not breaking old code, but some edge cases involving the empty regular expression may now parse differently. See perlop for details.</p>
<h3>Switch and Smart Match operator</h3>
<p> Perl 5 now has a switch statement. It&#8217;s available when <tt>&quot;use feature 'switch'&quot;</tt> is in effect. This feature introduces three new keywords, <tt>&quot;given&quot;</tt>, <tt>&quot;when&quot;</tt>, and <tt>&quot;default&quot;</tt>: </p>
<pre><code>
given($foo)
{
    when(/ ^abc /)
    {
        $abc = 1;
    }
    when(/ ^def /)
    {
        $def = 1;
    }
    when(/ ^xyz /)
    {
        $xyz = 1;
    }
    default
    {
        $nothing = 1;
    }
}
</code></pre>
<p> A more complete description of how Perl matches the switch variable against the <tt>&quot;when&quot;</tt> conditions is given in &#8220;Switch statements&#8221; in perlsyn. </p>
<p> This kind of match is called <i>smart match</i>, and it&#8217;s also possible to use it outside of switch statements, via the new <tt>&quot;~~&quot;</tt> operator. See &#8220;Smart matching in detail&#8221; in perlsyn. </p>
<p> This feature was contributed by Robin Houston.</p>
<h3>Regular expressions</h3>
<dl>
<dt>Recursive Patterns</p>
<dd> It is now possible to write recursive patterns without using the <tt>&quot;(??{})&quot;</tt> construct. This new way is more efficient, and in many cases easier to read. </p>
<p> Each capturing parenthesis can now be treated as an independent pattern that can be entered by using the <tt>&quot;(?PARNO)&quot;</tt> syntax (<tt>&quot;PARNO&quot;</tt> standing for &#8220;parenthesis number&#8221;). For example, the following pattern will match nested balanced angle brackets: </p>
<pre>
    /
     ^                      # start of line
     (                      # start capture buffer 1
        &lt;                   #   match an opening angle bracket
        (?:                 #   match one of:
            (?&gt;             #     don't backtrack over the inside of this group
                [^&lt;&gt;]+      #       one or more non angle brackets
            )               #     end non backtracking group
        |                   #     ... or ...
            (?1)            #     recurse to bracket 1 and try it again
        )*                  #   0 or more times.
        &gt;                   #   match a closing angle bracket
     )                      # end capture buffer one
     $                      # end of line
    /x
</pre>
<p> <font SIZE="-1">PCRE</font> users should note that Perl&#8217;s recursive regex feature allows backtracking into a recursed pattern, whereas in <font SIZE="-1">PCRE</font> the recursion is atomic or &#8220;possessive&#8221; in nature. As in the example above, you can add (?&gt;) to control this selectively. (Yves Orton)</p>
<dt>Named Capture Buffers</p>
<dd> It is now possible to name capturing parenthesis in a pattern and refer to the captured contents by name. The naming syntax is <tt>&quot;(?&lt;NAME&gt;....)&quot;</tt>. It&#8217;s possible to backreference to a named buffer with the <tt>&quot;\k&lt;NAME&gt;&quot;</tt> syntax. In code, the new magical hashes <tt>&quot;%+&quot;</tt> and <tt>&quot;%-&quot;</tt> can be used to access the contents of the capture buffers. </p>
<p> Thus, to replace all doubled chars with a single copy, one could write </p>
<pre>
    s/(?&lt;letter&gt;.)\k&lt;letter&gt;/$+{letter}/g
</pre>
<p> Only buffers with defined contents will be &#8220;visible&#8221; in the <tt>&quot;%+&quot;</tt> hash, so it&#8217;s possible to do something like </p>
<p>foreach<br />
    my $name(keys % +)<br />
    {<br />
        print &#8220;content of buffer &#8216;$name&#8217; is $+{$name}
&#8221;;<br />
    }</p>
<p> The <tt>&quot;%-&quot;</tt> hash is a bit more complete, since it will contain array refs holding values from all capture buffers similarly named, if there should be many of them. </p>
<p> <tt>&quot;%+&quot;</tt> and <tt>&quot;%-&quot;</tt> are implemented as tied hashes through the new module <tt>&quot;Tie::Hash::NamedCapture&quot;</tt>. </p>
<p> Users exposed to the .NET regex engine will find that the perl implementation differs in that the numerical ordering of the buffers is sequential, and not &#8220;unnamed first, then named&#8221;. Thus in the pattern </p>
<pre>
   /(A)(?&lt;B&gt;B)(C)(?&lt;D&gt;D)/
</pre>
<p> <tt>$1</tt> will be &#8216;A&#8217;, <tt>$2</tt> will be &#8216;B&#8217;, <tt>$3</tt> will be &#8216;C&#8217; and <tt>$4</tt> will be &#8216;D&#8217; and not <tt>$1</tt> is &#8216;A&#8217;, <tt>$2</tt> is &#8216;C&#8217; and <tt>$3</tt> is &#8216;B&#8217; and <tt>$4</tt> is &#8216;D&#8217; that a .NET programmer would expect. This is considered a feature. :-) (Yves Orton)</p>
<dt>Possessive Quantifiers</p>
<dd> Perl now supports the &#8220;possessive quantifier&#8221; syntax of the &#8220;atomic match&#8221; pattern. Basically a possessive quantifier matches as much as it can and never gives any back. Thus it can be used to control backtracking. The syntax is similar to non-greedy matching, except instead of using a &#8216;?&#8217; as the modifier the &#8216;+&#8217; is used. Thus <tt>&quot;?+&quot;</tt>, <tt>&quot;*+&quot;</tt>, <tt>&quot;++&quot;</tt>, <tt>&quot;{min,max}+&quot;</tt> are now legal quantifiers. (Yves Orton)</p>
<dt>Backtracking control verbs</p>
<dd> The regex engine now supports a number of special-purpose backtrack control verbs: (*THEN), (*PRUNE), (*MARK), (*SKIP), (*COMMIT), (*FAIL) and (*ACCEPT). See perlre for their descriptions. (Yves Orton)</p>
<dt>Relative backreferences</p>
<dd> A new syntax <tt>&quot;\g{N}&quot;</tt> or <tt>&quot;\gN&quot;</tt> where &#8220;N&#8221; is a decimal integer allows a safer form of back-reference notation as well as allowing relative backreferences. This should make it easier to generate and embed patterns that contain backreferences. See &#8220;Capture buffers&#8221; in perlre. (Yves Orton)</p>
<dt>&quot;\K&quot; escape</p>
<dd> The functionality of Jeff Pinyan&#8217;s module Regexp::Keep has been added to the core. In regular expressions you can now use the special escape <tt>&quot;\K&quot;</tt> as a way to do something like floating length positive lookbehind. It is also useful in substitutions like: </p>
<pre>
  s/(foo)bar/$1/g
</pre>
<p> that can now be converted to </p>
<pre>
  s/foo\Kbar//g
</pre>
<p> which is much more efficient. (Yves Orton)</p>
<dt>Vertical and horizontal whitespace, and linebreak</p>
<dd> Regular expressions now recognize the <tt>&quot;&quot;</tt> and <tt>&quot;\h&quot;</tt> escapes that match vertical and horizontal whitespace, respectively. <tt>&quot;\V&quot;</tt> and <tt>&quot;\H&quot;</tt> logically match their complements. </p>
<p> <tt>&quot;\R&quot;</tt> matches a generic linebreak, that is, vertical whitespace, plus the multi-character sequence <tt>&quot;
&quot;</tt>.</p>
<dt>Optional pre-match and post-match captures with the /p flag</p>
<dd> There is a new flag <tt>&quot;/p&quot;</tt> for regular expressions. Using this makes the engine preserve a copy of the part of the matched string before the matching substring to the new special variable <tt>&quot;${^PREMATCH}&quot;</tt>, the part after the matching substring to <tt>&quot;${^POSTMATCH}&quot;</tt>, and the matched substring itself to <tt>&quot;${^MATCH}&quot;</tt>. </p>
<p> Perl is still able to store these substrings to the special variables <tt>&quot;$`&quot;</tt>, <tt>&quot;$'&quot;</tt>, <tt>$&amp;</tt>, but using these variables anywhere in the program adds a penalty to all regular expression matches, whereas if you use the <tt>&quot;/p&quot;</tt> flag and the new special variables instead, you pay only for the regular expressions where the flag is used. </p>
<p> For more detail on the new variables, see perlvar; for the use of the regular expression flag, see perlop and perlre.</dl>
<h3>say()</h3>
<p> <code>say()</code> is a new built-in, only available when <tt>&quot;use feature 'say'&quot;</tt> is in effect, that is similar to <code>print()</code>, but that implicitly appends a newline to the printed string. See &#8220;say&#8221; in perlfunc. (Robin Houston)</p>
<h3>Lexical $_</h3>
<p> The default variable <tt>$_</tt> can now be lexicalized, by declaring it like any other lexical variable, with a simple </p>
<pre>
    my $_;
</pre>
<p> The operations that default on <tt>$_</tt> will use the lexically-scoped version of <tt>$_</tt> when it exists, instead of the global <tt>$_</tt>. </p>
<p> In a <tt>&quot;map&quot;</tt> or a <tt>&quot;grep&quot;</tt> block, if <tt>$_</tt> was previously my&#8217;ed, then the <tt>$_</tt> inside the block is lexical as well (and scoped to the block). </p>
<p> In a scope where <tt>$_</tt> has been lexicalized, you can still have access to the global version of <tt>$_</tt> by using <tt>$::_</tt>, or, more simply, by overriding the lexical declaration with <tt>&quot;our $_&quot;</tt>. (Rafael Garcia-Suarez)</p>
<h3>The _ prototype</h3>
<p> A new prototype character has been added. <tt>&quot;_&quot;</tt> is equivalent to <tt>&quot;$&quot;</tt> but defaults to <tt>$_</tt> if the corresponding argument isn&#8217;t supplied (both <tt>&quot;$&quot;</tt> and <tt>&quot;_&quot;</tt> denote a scalar). Due to the optional nature of the argument, you can only use it at the end of a prototype, or before a semicolon. </p>
<p> This has a small incompatible consequence: the <code>prototype()</code> function has been adjusted to return <tt>&quot;_&quot;</tt> for some built-ins in appropriate cases (for example, <tt>&quot;prototype('CORE::rmdir')&quot;</tt>). (Rafael Garcia-Suarez)</p>
<h3><font SIZE="-1">UNITCHECK</font> blocks</h3>
<p> <tt>&quot;UNITCHECK&quot;</tt>, a new special code block has been introduced, in addition to <tt>&quot;BEGIN&quot;</tt>, <tt>&quot;CHECK&quot;</tt>, <tt>&quot;INIT&quot;</tt> and <tt>&quot;END&quot;</tt>. </p>
<p> <tt>&quot;CHECK&quot;</tt> and <tt>&quot;INIT&quot;</tt> blocks, while useful for some specialized purposes, are always executed at the transition between the compilation and the execution of the main program, and thus are useless whenever code is loaded at runtime. On the other hand, <tt>&quot;UNITCHECK&quot;</tt> blocks are executed just after the unit which defined them has been compiled. See perlmod for more information. (Alex Gough)</p>
<h3>New Pragma, mro</h3>
<p> A new pragma, <tt>&quot;mro&quot;</tt> (for Method Resolution Order) has been added. It permits to switch, on a per-class basis, the algorithm that perl uses to find inherited methods in case of a multiple inheritance hierarchy. The default <font SIZE="-1">MRO</font> hasn&#8217;t changed (<font SIZE="-1">DFS,</font> for Depth First Search). Another <font SIZE="-1">MRO</font> is available: the C3 algorithm. See mro for more information. (Brandon Black) </p>
<p> Note that, due to changes in the implementation of class hierarchy search, code that used to undef the <tt>*ISA</tt> glob will most probably break. Anyway, undef&#8217;ing <tt>*ISA</tt> had the side-effect of removing the magic on the <tt>@ISA</tt> array and should not have been done in the first place. Also, the cache <tt>*::ISA::CACHE::</tt> no longer exists; to force reset the <tt>@ISA</tt> cache, you now need to use the <tt>&quot;mro&quot;</tt> <font SIZE="-1">API,</font> or more simply to assign to <tt>@ISA</tt> (e.g. with <tt>&quot;@ISA = @ISA&quot;</tt>).</p>
<h3><code>readdir()</code> may return a short filename on Windows</h3>
<p> The <code>readdir()</code> function may return a &#8220;short filename&#8221; when the long filename contains characters outside the <font SIZE="-1">ANSI</font> codepage. Similarly <code>Cwd::cwd()</code> may return a short directory name, and <code>glob()</code> may return short names as well. On the <font SIZE="-1">NTFS</font> file system these short names can always be represented in the <font SIZE="-1">ANSI</font> codepage. This will not be true for all other file system drivers; e.g. the <font SIZE="-1">FAT</font> filesystem stores short filenames in the <font SIZE="-1">OEM</font> codepage, so some files on <font SIZE="-1">FAT</font> volumes remain unaccessible through the <font SIZE="-1">ANSI</font> APIs. </p>
<p> Similarly, $^X, <tt>@INC</tt>, and <tt>$ENV</tt>{<font SIZE="-1">PATH</font>} are preprocessed at startup to make sure all paths are valid in the <font SIZE="-1">ANSI</font> codepage (if possible). </p>
<p> The <code>Win32::GetLongPathName()</code> function now returns the <font SIZE="-1">UTF-8</font> encoded correct long file name instead of using replacement characters to force the name into the <font SIZE="-1">ANSI</font> codepage. The new <code>Win32::GetANSIPathName()</code> function can be used to turn a long pathname into a short one only if the long one cannot be represented in the <font SIZE="-1">ANSI</font> codepage. </p>
<p> Many other functions in the <tt>&quot;Win32&quot;</tt> module have been improved to accept <font SIZE="-1">UTF-8</font> encoded arguments. Please see Win32 for details.</p>
<h3><code>readpipe()</code> is now overridable</h3>
<p> The built-in function <code>readpipe()</code> is now overridable. Overriding it permits also to override its operator counterpart, <tt>&quot;qx//&quot;</tt> (a.k.a. <tt>&quot;``&quot;</tt>). Moreover, it now defaults to <tt>$_</tt> if no argument is provided. (Rafael Garcia-Suarez)</p>
<h3>Default argument for <code>readline()</code></h3>
<p> <code>readline()</code> now defaults to <tt>*ARGV</tt> if no argument is provided. (Rafael Garcia-Suarez)</p>
<h3><code>state()</code> variables</h3>
<p> A new class of variables has been introduced. State variables are similar to <tt>&quot;my&quot;</tt> variables, but are declared with the <tt>&quot;state&quot;</tt> keyword in place of <tt>&quot;my&quot;</tt>. They&#8217;re visible only in their lexical scope, but their value is persistent: unlike <tt>&quot;my&quot;</tt> variables, they&#8217;re not undefined at scope entry, but retain their previous value. (Rafael Garcia-Suarez, Nicholas Clark) </p>
<p> To use state variables, one needs to enable them by using </p>
<pre>
    use feature 'state';
</pre>
<p> or by using the <tt>&quot;-E&quot;</tt> command-line switch in one-liners. See &#8220;Persistent Private Variables&#8221; in perlsub.</p>
<h3>Stacked filetest operators</h3>
<p> As a new form of syntactic sugar, it&#8217;s now possible to stack up filetest operators. You can now write <tt>&quot;-f -w -x $file&quot;</tt> in a row to mean <tt>&quot;-x $file &amp;&amp; -w _ &amp;&amp; -f _&quot;</tt>. See &#8220;-X&#8221; in perlfunc.</p>
<h3><font SIZE="-1"><code>UNIVERSAL::DOES</code></font><code>()</code></h3>
<p> The <tt>&quot;UNIVERSAL&quot;</tt> class has a new method, <tt>&quot;DOES()&quot;</tt>. It has been added to solve semantic problems with the <tt>&quot;isa()&quot;</tt> method. <tt>&quot;isa()&quot;</tt> checks for inheritance, while <tt>&quot;DOES()&quot;</tt> has been designed to be overridden when module authors use other types of relations between classes (in addition to inheritance). (chromatic) </p>
<p> See &#8220;$obj-&gt;<font SIZE="-1">DOES</font>( <font SIZE="-1">ROLE</font> )&#8221; in <font SIZE="-1">UNIVERSAL</font>.</p>
<h3>Formats</h3>
<p> Formats were improved in several ways. A new field, <tt>&quot;^*&quot;</tt>, can be used for variable-width, one-line-at-a-time text. Null characters are now handled correctly in picture lines. Using <tt>&quot;@#&quot;</tt> and <tt>&quot;~~&quot;</tt> together will now produce a compile-time error, as those format fields are incompatible. perlform has been improved, and miscellaneous bugs fixed.</p>
<h3>Byte-order modifiers for <code>pack()</code> and <code>unpack()</code></h3>
<p> There are two new byte-order modifiers, <tt>&quot;&gt;&quot;</tt> (big-endian) and <tt>&quot;&lt;&quot;</tt> (little-endian), that can be appended to most <code>pack()</code> and <code>unpack()</code> template characters and groups to force a certain byte-order for that type or group. See &#8220;pack&#8221; in perlfunc and perlpacktut for details.</p>
<h3>no VERSION</h3>
<p> You can now use <tt>&quot;no&quot;</tt> followed by a version number to specify that you want to use a version of perl older than the specified one.</p>
<h3>chdir, chmod and chown on filehandles</h3>
<p> <tt>&quot;chdir&quot;</tt>, <tt>&quot;chmod&quot;</tt> and <tt>&quot;chown&quot;</tt> can now work on filehandles as well as filenames, if the system supports respectively <tt>&quot;fchdir&quot;</tt>, <tt>&quot;fchmod&quot;</tt> and <tt>&quot;fchown&quot;</tt>, thanks to a patch provided by Gisle Aas.</p>
<h3><font SIZE="-1">OS</font> groups</h3>
<p> <tt>$(</tt> and <tt>$)</tt> now return groups in the order where the <font SIZE="-1">OS</font> returns them, thanks to Gisle Aas. This wasn&#8217;t previously the case.</p>
<h3>Recursive sort subs</h3>
<p> You can now use recursive subroutines with <code>sort()</code>, thanks to Robin Houston.</p>
<h3>Exceptions in constant folding</h3>
<p> The constant folding routine is now wrapped in an exception handler, and if folding throws an exception (such as attempting to evaluate 0/0), perl now retains the current optree, rather than aborting the whole program. Without this change, programs would not compile if they had expressions that happened to generate exceptions, even though those expressions were in code that could never be reached at runtime. (Nicholas Clark, Dave Mitchell)</p>
<h3>Source filters in @INC</h3>
<p> It&#8217;s possible to enhance the mechanism of subroutine hooks in <tt>@INC</tt> by adding a source filter on top of the filehandle opened and returned by the hook. This feature was planned a long time ago, but wasn&#8217;t quite working until now. See &#8220;require&#8221; in perlfunc for details. (Nicholas Clark)</p>
<h3>New internal variables</h3>
<dl>
<dt>&quot;${^RE_DEBUG_FLAGS}&quot;</p>
<dd> This variable controls what debug flags are in effect for the regular expression engine when running under <tt>&quot;use re &quot;debug&quot;&quot;</tt>. See re for details.</p>
<dt>&quot;${^CHILD_ERROR_NATIVE}&quot;</p>
<dd> This variable gives the native status returned by the last pipe close, backtick command, successful call to <code>wait()</code> or <code>waitpid()</code>, or from the <code>system()</code> operator. See perlvar for details. (Contributed by Gisle Aas.)</p>
<dt>&quot;${^RE_TRIE_MAXBUF}&quot;</p>
<dd> See &#8220;Trie optimisation of literal string alternations&#8221;.</p>
<dt>&quot;${^WIN32_SLOPPY_STAT}&quot;</p>
<dd> See &#8220;Sloppy stat on Windows&#8221;.</dl>
<h3>Miscellaneous</h3>
<p> <tt>&quot;unpack()&quot;</tt> now defaults to unpacking the <tt>$_</tt> variable. </p>
<p> <tt>&quot;mkdir()&quot;</tt> without arguments now defaults to <tt>$_</tt>. </p>
<p> The internal dump output has been improved, so that non-printable characters such as newline and backspace are output in <tt>&quot;
