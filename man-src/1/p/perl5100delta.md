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
<dt>Recursive Patterns</dt>
<dd> It is now possible to write recursive patterns without using the <tt>&quot;(??{})&quot;</tt> construct. This new way is more efficient, and in many cases easier to read. </dd>
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
<dt>Named Capture Buffers</dt>
<dd> It is now possible to name capturing parenthesis in a pattern and refer to the captured contents by name. The naming syntax is <tt>&quot;(?&lt;NAME&gt;....)&quot;</tt>. It&#8217;s possible to backreference to a named buffer with the <tt>&quot;\k&lt;NAME&gt;&quot;</tt> syntax. In code, the new magical hashes <tt>&quot;%+&quot;</tt> and <tt>&quot;%-&quot;</tt> can be used to access the contents of the capture buffers. </dd>
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
<dt>Possessive Quantifiers</dt>
<dd> Perl now supports the &#8220;possessive quantifier&#8221; syntax of the &#8220;atomic match&#8221; pattern. Basically a possessive quantifier matches as much as it can and never gives any back. Thus it can be used to control backtracking. The syntax is similar to non-greedy matching, except instead of using a &#8216;?&#8217; as the modifier the &#8216;+&#8217; is used. Thus <tt>&quot;?+&quot;</tt>, <tt>&quot;*+&quot;</tt>, <tt>&quot;++&quot;</tt>, <tt>&quot;{min,max}+&quot;</tt> are now legal quantifiers. (Yves Orton)</dd>
<dt>Backtracking control verbs</dt>
<dd> The regex engine now supports a number of special-purpose backtrack control verbs: (*THEN), (*PRUNE), (*MARK), (*SKIP), (*COMMIT), (*FAIL) and (*ACCEPT). See perlre for their descriptions. (Yves Orton)</dd>
<dt>Relative backreferences</dt>
<dd> A new syntax <tt>&quot;\g{N}&quot;</tt> or <tt>&quot;\gN&quot;</tt> where &#8220;N&#8221; is a decimal integer allows a safer form of back-reference notation as well as allowing relative backreferences. This should make it easier to generate and embed patterns that contain backreferences. See &#8220;Capture buffers&#8221; in perlre. (Yves Orton)</dd>
<dt>&quot;\K&quot; escape</dt>
<dd> The functionality of Jeff Pinyan&#8217;s module Regexp::Keep has been added to the core. In regular expressions you can now use the special escape <tt>&quot;\K&quot;</tt> as a way to do something like floating length positive lookbehind. It is also useful in substitutions like: </dd>
<pre>
  s/(foo)bar/$1/g
</pre>
<p> that can now be converted to </p>
<pre>
  s/foo\Kbar//g
</pre>
<p> which is much more efficient. (Yves Orton)</p>
<dt>Vertical and horizontal whitespace, and linebreak</dt>
<dd> Regular expressions now recognize the <tt>&quot;&quot;</tt> and <tt>&quot;\h&quot;</tt> escapes that match vertical and horizontal whitespace, respectively. <tt>&quot;\V&quot;</tt> and <tt>&quot;\H&quot;</tt> logically match their complements. </dd>
<p> <tt>&quot;\R&quot;</tt> matches a generic linebreak, that is, vertical whitespace, plus the multi-character sequence <tt>&quot;
&quot;</tt>.</p>
<dt>Optional pre-match and post-match captures with the /p flag</dt>
<dd> There is a new flag <tt>&quot;/p&quot;</tt> for regular expressions. Using this makes the engine preserve a copy of the part of the matched string before the matching substring to the new special variable <tt>&quot;${^PREMATCH}&quot;</tt>, the part after the matching substring to <tt>&quot;${^POSTMATCH}&quot;</tt>, and the matched substring itself to <tt>&quot;${^MATCH}&quot;</tt>. </dd>
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
<dt>&quot;${^RE_DEBUG_FLAGS}&quot;</dt>
<dd> This variable controls what debug flags are in effect for the regular expression engine when running under <tt>&quot;use re &quot;debug&quot;&quot;</tt>. See re for details.</dd>
<dt>&quot;${^CHILD_ERROR_NATIVE}&quot;</dt>
<dd> This variable gives the native status returned by the last pipe close, backtick command, successful call to <code>wait()</code> or <code>waitpid()</code>, or from the <code>system()</code> operator. See perlvar for details. (Contributed by Gisle Aas.)</dd>
<dt>&quot;${^RE_TRIE_MAXBUF}&quot;</dt>
<dd> See &#8220;Trie optimisation of literal string alternations&#8221;.</dd>
<dt>&quot;${^WIN32_SLOPPY_STAT}&quot;</dt>
<dd> See &#8220;Sloppy stat on Windows&#8221;.</dd></dl>
<h3>Miscellaneous</h3>
<p> <tt>&quot;unpack()&quot;</tt> now defaults to unpacking the <tt>$_</tt> variable. </p>
<p> <tt>&quot;mkdir()&quot;</tt> without arguments now defaults to <tt>$_</tt>. </p>
<p> The internal dump output has been improved, so that non-printable characters such as newline and backspace are output in <tt>&quot;</tt>\x&quot;</code> notation, rather than octal. </p>
<p> The <code>-C</code> option can no longer be used on the <code>&quot;#!&quot;</code> line. It wasn&#8217;t working there anyway, since the standard streams are already set up at this point in the execution of the perl interpreter. You can use <code>binmode()</code> instead to get the desired behaviour.  </p>
<font SIZE="-1"></font><h3>UCD 5.0.0</h3>
<p> The copy of the Unicode Character Database included in Perl 5 has been updated to version 5.0.0.  </p>
<font SIZE="-1"></font><h3>MAD</h3>
<p> <font SIZE="-1">MAD,</font> which stands for <i>Miscellaneous Attribute Decoration</i>, is a still-in-development work leading to a Perl 5 to Perl 6 converter. To enable it, it&#8217;s necessary to pass the argument <code>&quot;-Dmad&quot;</code> to Configure. The obtained perl isn&#8217;t binary compatible with a regular perl 5.10, and has space and speed penalties; moreover not all regression tests still pass with it. (Larry Wall, Nicholas Clark)  </p>
<code></code><h3>kill() on Windows</h3>
<p> On Windows platforms, <code>&quot;kill(-9, $pid)&quot;</code> now kills a process tree. (On Unix, this delivers the signal to all processes in the same process group.)  </p>
<h2>Incompatible Changes</h2>
<font SIZE="-1"></font><h3>Packing and UTF-8 strings</h3>
<p> The semantics of <code>pack()</code> and <code>unpack()</code> regarding UTF-8-encoded data has been changed. Processing is now by default character per character instead of byte per byte on the underlying encoding. Notably, code that used things like <code>&quot;pack(&quot;a*&quot;, $string)&quot;</code> to see through the encoding of string will now simply get back the original <code>$string</code>. Packed strings can also get upgraded during processing when you store upgraded characters. You can get the old behaviour by using <code>&quot;use bytes&quot;</code>. </p>
<p> To be consistent with <code>pack()</code>, the <code>&quot;C0&quot;</code> in <code>unpack()</code> templates indicates that the data is to be processed in character mode, i.e. character by character; on the contrary, <code>&quot;U0&quot;</code> in <code>unpack()</code> indicates <font SIZE="-1">UTF-8</font> mode, where the packed string is processed in its UTF-8-encoded Unicode form on a byte by byte basis. This is reversed with regard to perl 5.8.X, but now consistent between <code>pack()</code> and <code>unpack()</code>. </p>
<p> Moreover, <code>&quot;C0&quot;</code> and <code>&quot;U0&quot;</code> can also be used in <code>pack()</code> templates to specify respectively character and byte modes. </p>
<p> <code>&quot;C0&quot;</code> and <code>&quot;U0&quot;</code> in the middle of a pack or unpack format now switch to the specified encoding mode, honoring parens grouping. Previously, parens were ignored. </p>
<p> Also, there is a new <code>pack()</code> character format, <code>&quot;W&quot;</code>, which is intended to replace the old <code>&quot;C&quot;</code>. <code>&quot;C&quot;</code> is kept for unsigned chars coded as bytes in the strings internal representation. <code>&quot;W&quot;</code> represents unsigned (logical) character values, which can be greater than 255. It is therefore more robust when dealing with potentially UTF-8-encoded data (as <code>&quot;C&quot;</code> will wrap values outside the range 0..255, and not respect the string encoding). </p>
<p> In practice, that means that pack formats are now encoding-neutral, except <code>&quot;C&quot;</code>. </p>
<p> For consistency, <code>&quot;A&quot;</code> in <code>unpack()</code> format now trims all Unicode whitespace from the end of the string. Before perl 5.9.2, it used to strip only the classical <font SIZE="-1">ASCII</font> space characters.  </p>
<code></code><h3>Byte/character count feature in unpack()</h3>
<p> A new <code>unpack()</code> template character, <code>&quot;.&quot;</code>, returns the number of bytes or characters (depending on the selected encoding mode, see above) read so far.  </p>
<h3>The $* and $# variables have been removed</h3>
<p> <code>$*</code>, which was deprecated in favor of the <code>&quot;/s&quot;</code> and <code>&quot;/m&quot;</code> regexp modifiers, has been removed. </p>
<p> The deprecated <code>$#</code> variable (output format for numbers) has been removed. </p>
<p> Two new severe warnings, <code>&quot;$#/$* is no longer supported&quot;</code>, have been added.  </p>
<code></code><h3>substr() lvalues are no longer fixed-length</h3>
<p> The lvalues returned by the three argument form of <code>substr()</code> used to be a ``fixed length window&#8217;&#8216; on the original string. In some cases this could cause surprising action at distance or other undefined behaviour. Now the length of the window adjusts itself to the length of the string assigned to it.  </p>
<h3>Parsing of -f _</h3>
<p> The identifier <code>&quot;_&quot;</code> is now forced to be a bareword after a filetest operator. This solves a number of misparsing issues when a global <code>&quot;_&quot;</code> subroutine is defined.  </p>
<h3>:unique</h3>
<p> The <code>&quot;:unique&quot;</code> attribute has been made a no-op, since its current implementation was fundamentally flawed and not threadsafe.  </p>
<h3>Effect of pragmas in eval</h3>
<p> The compile-time value of the <code>&quot;%^H&quot;</code> hint variable can now propagate into eval(&quot;&quot;)uated code. This makes it more useful to implement lexical pragmas. </p>
<p> As a side-effect of this, the overloaded-ness of constants now propagates into eval(&quot;&quot;).  </p>
<font SIZE="-1"></font><h3>chdir FOO</h3>
<p> A bareword argument to <code>chdir()</code> is now recognized as a file handle. Earlier releases interpreted the bareword as a directory name. (Gisle Aas)  </p>
<h3>Handling of .pmc files</h3>
<p> An old feature of perl was that before <code>&quot;require&quot;</code> or <code>&quot;use&quot;</code> look for a file with a <i>.pm</i> extension, they will first look for a similar filename with a <i>.pmc</i> extension. If this file is found, it will be loaded in place of any potentially existing file ending in a <i>.pm</i> extension. </p>
<p> Previously, <i>.pmc</i> files were loaded only if more recent than the matching <i>.pm</i> file. Starting with 5.9.4, they&#8217;ll be always loaded if they exist.  </p>
<h3>$^V is now a version object instead of a v-string</h3>
<p> $^V can still be used with the <code>%vd</code> format in printf, but any character-level operations will now access the string representation of the <code>&quot;version&quot;</code> object and not the ordinals of a v-string. Expressions like <code>&quot;substr($^V, 0, 2)&quot;</code> or <code>&quot;split //, $^V&quot;</code> no longer work and must be rewritten.  </p>
<h3>@- and @+ in patterns</h3>
<p> The special arrays <code>&quot;@-&quot;</code> and <code>&quot;@+&quot;</code> are no longer interpolated in regular expressions. (Sadahiro Tomoyuki)  </p>
<h3>$AUTOLOAD can now be tainted</h3>
<p> If you call a subroutine by a tainted name, and if it defers to an <font SIZE="-1">AUTOLOAD</font> function, then <code>$AUTOLOAD</code> will be (correctly) tainted. (Rick Delaney)  </p>
<h3>Tainting and printf</h3>
<p> When perl is run under taint mode, <code>&quot;printf()&quot;</code> and <code>&quot;sprintf()&quot;</code> will now reject any tainted format argument. (Rafael Garcia-Suarez)  </p>
<h3>undef and signal handlers</h3>
<p> Undefining or deleting a signal handler via <code>&quot;undef $SIG{FOO}&quot;</code> is now equivalent to setting it to <code>&#8216;DEFAULT&#8217;</code>. (Rafael Garcia-Suarez)  </p>
<code></code><h3>strictures and dereferencing in defined()</h3>
<p> <code>&quot;use strict &#8216;refs&#8217;&quot;</code> was ignoring taking a hard reference in an argument to <code>defined()</code>, as in : </p>
<pre><code>    use strict 'refs';
    my $x = 'foo';
    if (defined $$x) {...}
</code></pre>
<p> This now correctly produces the run-time error <code>&quot;Can&#8217;t use string as a SCALAR ref while &quot;strict refs&quot; in use&quot;</code>. </p>
<p> <code>&quot;defined @$foo&quot;</code> and <code>&quot;defined %$bar&quot;</code> are now also subject to <code>&quot;strict &#8216;refs&#8217;&quot;</code> (that is, <code>$foo</code> and <code>$bar</code> shall be proper references there.) (<code>&quot;defined(@foo)&quot;</code> and <code>&quot;defined(%bar)&quot;</code> are discouraged constructs anyway.) (Nicholas Clark)  </p>
<h3>(?p{}) has been removed</h3>
<p> The regular expression construct <code>&quot;(?p{})&quot;</code>, which was deprecated in perl 5.8, has been removed. Use <code>&quot;(??{})&quot;</code> instead. (Rafael Garcia-Suarez)  </p>
<h3>Pseudo-hashes have been removed</h3>
<p> Support for pseudo-hashes has been removed from Perl 5.9. (The <code>&quot;fields&quot;</code> pragma remains here, but uses an alternate implementation.)  </p>
<h3>Removal of the bytecode compiler and of perlcc</h3>
<p> <code>&quot;perlcc&quot;</code>, the byteloader and the supporting modules (B::C, B::CC, B::Bytecode, etc.) are no longer distributed with the perl sources. Those experimental tools have never worked reliably, and, due to the lack of volunteers to keep them in line with the perl interpreter developments, it was decided to remove them instead of shipping a broken version of those. The last version of those modules can be found with perl 5.9.4. </p>
<p> However the B compiler framework stays supported in the perl core, as with the more useful modules it has permitted (among others, B::Deparse and B::Concise).  </p>
<font SIZE="-1"></font><h3>Removal of the JPL</h3>
<p> The <font SIZE="-1">JPL</font> (Java-Perl Lingo) has been removed from the perl sources tarball.  </p>
<h3>Recursive inheritance detected earlier</h3>
<p> Perl will now immediately throw an exception if you modify any package&#8217;s <code>@ISA</code> in such a way that it would cause recursive inheritance. </p>
<p> Previously, the exception would not occur until Perl attempted to make use of the recursive inheritance while resolving a method or doing a <code>&quot;$foo-&gt;isa($bar)&quot;</code> lookup.  </p>
<h3>warnings::enabled and warnings::warnif changed to favor users of modules</h3>
<p> The behaviour in 5.10.x favors the person using the module; The behaviour in 5.8.x favors the module writer; </p>
<p> Assume the following code: </p>
<pre><code>  main calls Foo::Bar::baz()
  Foo::Bar inherits from Foo::Base
  Foo::Bar::baz() calls Foo::Base::_bazbaz()
  Foo::Base::_bazbaz() calls: warnings::warnif('substr', 'some warning
message');
</code></pre>
<p> On 5.8.x, the code warns when Foo::Bar contains <code>&quot;use warnings;&quot;</code> It does not matter if Foo::Base or main have warnings enabled to disable the warning one has to modify Foo::Bar. </p>
<p> On 5.10.0 and newer, the code warns when main contains <code>&quot;use warnings;&quot;</code> It does not matter if Foo::Base or Foo::Bar have warnings enabled to disable the warning one has to modify main.  </p>
<h2>Modules and Pragmata</h2>
<h3>Upgrading individual core modules</h3>
<p> Even more core modules are now also available separately through the <font SIZE="-1">CPAN.</font> If you wish to update one of these modules, you don&#8217;t need to wait for a new perl release. From within the cpan shell, running the &#8216;r&#8217; command will report on modules with upgrades available. See <code>&quot;perldoc CPAN&quot;</code> for more information.  </p>
<h3>Pragmata Changes</h3>
<dl>
<dt>&quot;feature&quot;</dt>
<dd> <p> The new pragma <code>&quot;feature&quot;</code> is used to enable new features that might break old code. See &quot;The <code>&quot;feature&quot;</code> pragma&quot; above. </p>
 </dd>
<dt>&quot;mro&quot;</dt>
<dd> <p> This new pragma enables to change the algorithm used to resolve inherited methods. See &quot;New Pragma, <code>&quot;mro&quot;</code>&quot; above. </p>
 </dd>
<dt>Scoping of the &quot;sort&quot; pragma</dt>
<dd> <p> The <code>&quot;sort&quot;</code> pragma is now lexically scoped. Its effect used to be global. </p>
 </dd>
<dt>Scoping of &quot;bignum&quot;, &quot;bigint&quot;, &quot;bigrat&quot;</dt>
<dd> <p> The three numeric pragmas <code>&quot;bignum&quot;</code>, <code>&quot;bigint&quot;</code> and <code>&quot;bigrat&quot;</code> are now lexically scoped. (Tels) </p>
 </dd>
<dt>&quot;base&quot;</dt>
<dd> <p> The <code>&quot;base&quot;</code> pragma now warns if a class tries to inherit from itself. (Curtis ``Ovid&#8217;&#8216; Poe) </p>
 </dd>
<dt>&quot;strict&quot; and &quot;warnings&quot;</dt>
<dd> <p> <code>&quot;strict&quot;</code> and <code>&quot;warnings&quot;</code> will now complain loudly if they are loaded via incorrect casing (as in <code>&quot;use Strict;&quot;</code>). (Johan Vromans) </p>
 </dd>
<dt>&quot;version&quot;</dt>
<dd> <p> The <code>&quot;version&quot;</code> module provides support for version objects. </p>
 </dd>
<dt>&quot;warnings&quot;</dt>
<dd> <p> The <code>&quot;warnings&quot;</code> pragma doesn&#8217;t load <code>&quot;Carp&quot;</code> anymore. That means that code that used <code>&quot;Carp&quot;</code> routines without having loaded it at compile time might need to be adjusted; typically, the following (faulty) code won&#8217;t work anymore, and will require parentheses to be added after the function name: </p>
<pre><code>    use warnings;
    require Carp;
    Carp::confess 'argh';
</code></pre>
 </dd>
<dt>&quot;less&quot;</dt>
<dd> <p> <code>&quot;less&quot;</code> now does something useful (or at least it tries to). In fact, it has been turned into a lexical pragma. So, in your modules, you can now test whether your users have requested to use less <font SIZE="-1">CPU,</font> or less memory, less magic, or maybe even less fat. See less for more. (Joshua ben Jore) </p>
 </dd></dl>
<h3>New modules</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;encoding::warnings&quot;</code>, by Audrey Tang, is a module to emit warnings whenever an <font SIZE="-1">ASCII</font> character string containing high-bit bytes is implicitly converted into <font SIZE="-1">UTF-8.</font> It&#8217;s a lexical pragma since Perl 5.9.4; on older perls, its effect is global. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Module::CoreList&quot;</code>, by Richard Clamp, is a small handy module that tells you what versions of core modules ship with any versions of Perl 5. It comes with a command-line frontend, <code>&quot;corelist&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Math::BigInt::FastCalc&quot;</code> is an XS-enabled, and thus faster, version of <code>&quot;Math::BigInt::Calc&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Compress::Zlib&quot;</code> is an interface to the zlib compression library. It comes with a bundled version of zlib, so having a working zlib is not a prerequisite to install it. It&#8217;s used by <code>&quot;Archive::Tar&quot;</code> (see below). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;IO::Zlib&quot;</code> is an <code>&quot;IO::&quot;</code>-style interface to <code>&quot;Compress::Zlib&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Archive::Tar&quot;</code> is a module to manipulate <code>&quot;tar&quot;</code> archives. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Digest::SHA&quot;</code> is a module used to calculate many types of <font SIZE="-1">SHA</font> digests, has been included for <font SIZE="-1">SHA</font> support in the <font SIZE="-1">CPAN</font> module. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;ExtUtils::CBuilder&quot;</code> and <code>&quot;ExtUtils::ParseXS&quot;</code> have been added. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Hash::Util::FieldHash&quot;</code>, by Anno Siegel, has been added. This module provides support for <i>field hashes</i>: hashes that maintain an association of a reference with a value, in a thread-safe garbage-collected way. Such hashes are useful to implement inside-out objects. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Module::Build&quot;</code>, by Ken Williams, has been added. It&#8217;s an alternative to <code>&quot;ExtUtils::MakeMaker&quot;</code> to build and install perl modules. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Module::Load&quot;</code>, by Jos Boumans, has been added. It provides a single interface to load Perl modules and <i>.pl</i> files. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Module::Loaded&quot;</code>, by Jos Boumans, has been added. It&#8217;s used to mark modules as loaded or unloaded. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Package::Constants&quot;</code>, by Jos Boumans, has been added. It&#8217;s a simple helper to list all constants declared in a given package. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Win32API::File&quot;</code>, by Tye McQueen, has been added (for Windows builds). This module provides low-level access to Win32 system <font SIZE="-1">API</font> calls for files/dirs. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Locale::Maketext::Simple&quot;</code>, needed by <font SIZE="-1">CPANPLUS,</font> is a simple wrapper around <code>&quot;Locale::Maketext::Lexicon&quot;</code>. Note that <code>&quot;Locale::Maketext::Lexicon&quot;</code> isn&#8217;t included in the perl core; the behaviour of <code>&quot;Locale::Maketext::Simple&quot;</code> gracefully degrades when the later isn&#8217;t present. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Params::Check&quot;</code> implements a generic input parsing/checking mechanism. It is used by <font SIZE="-1">CPANPLUS.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Term::UI&quot;</code> simplifies the task to ask questions at a terminal prompt. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Object::Accessor&quot;</code> provides an interface to create per-object accessors. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Module::Pluggable&quot;</code> is a simple framework to create modules that accept pluggable sub-modules. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Module::Load::Conditional&quot;</code> provides simple ways to query and possibly load installed modules. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Time::Piece&quot;</code> provides an object oriented interface to time functions, overriding the built-ins <code>localtime()</code> and <code>gmtime()</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;IPC::Cmd&quot;</code> helps to find and run external commands, possibly interactively. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;File::Fetch&quot;</code> provide a simple generic file fetching mechanism. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Log::Message&quot;</code> and <code>&quot;Log::Message::Simple&quot;</code> are used by the log facility of <code>&quot;CPANPLUS&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Archive::Extract&quot;</code> is a generic archive extraction mechanism for <i>.tar</i> (plain, gzipped or bzipped) or <i>.zip</i> files. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;CPANPLUS&quot;</code> provides an <font SIZE="-1">API</font> and a command-line tool to access the <font SIZE="-1">CPAN</font> mirrors. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Pod::Escapes&quot;</code> provides utilities that are useful in decoding Pod E&lt;...&gt; sequences. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Pod::Simple&quot;</code> is now the backend for several of the Pod-related modules included with Perl. </p>
 </dd></dl>
<h3>Selected Changes to Core Modules</h3>
<dl>
<dt>&quot;Attribute::Handlers&quot;</dt>
<dd> <p> <code>&quot;Attribute::Handlers&quot;</code> can now report the caller&#8217;s file and line number. (David Feldman) </p>
<p> All interpreted attributes are now passed as array references. (Damian Conway) </p>
 </dd>
<dt>&quot;B::Lint&quot;</dt>
<dd> <p> <code>&quot;B::Lint&quot;</code> is now based on <code>&quot;Module::Pluggable&quot;</code>, and so can be extended with plugins. (Joshua ben Jore) </p>
 </dd>
<dt>&quot;B&quot;</dt>
<dd> <p> It&#8217;s now possible to access the lexical pragma hints (<code>&quot;%^H&quot;</code>) by using the method <code>B::COP::hints_hash()</code>. It returns a <code>&quot;B::RHE&quot;</code> object, which in turn can be used to get a hash reference via the method <code>B::RHE::HASH()</code>. (Joshua ben Jore) </p>
 </dd>
<dt>&quot;Thread&quot;</dt>
<dd> <p> As the old 5005thread threading model has been removed, in favor of the ithreads scheme, the <code>&quot;Thread&quot;</code> module is now a compatibility wrapper, to be used in old code only. It has been removed from the default list of dynamic extensions. </p>
 </dd></dl>
<h2>Utility Changes</h2>
<dl>
<dt>perl -d</dt>
<dd> <p> The Perl debugger can now save all debugger commands for sourcing later; notably, it can now emulate stepping backwards, by restarting and rerunning all bar the last command from a saved command history. </p>
<p> It can also display the parent inheritance tree of a given class, with the <code>&quot;i&quot;</code> command. </p>
 </dd>
<dt>ptar</dt>
<dd> <p> <code>&quot;ptar&quot;</code> is a pure perl implementation of <code>&quot;tar&quot;</code> that comes with <code>&quot;Archive::Tar&quot;</code>. </p>
 </dd>
<dt>ptardiff</dt>
<dd> <p> <code>&quot;ptardiff&quot;</code> is a small utility used to generate a diff between the contents of a tar archive and a directory tree. Like <code>&quot;ptar&quot;</code>, it comes with <code>&quot;Archive::Tar&quot;</code>. </p>
 </dd>
<dt>shasum</dt>
<dd> <p> <code>&quot;shasum&quot;</code> is a command-line utility, used to print or to check <font SIZE="-1">SHA</font> digests. It comes with the new <code>&quot;Digest::SHA&quot;</code> module. </p>
 </dd>
<dt>corelist</dt>
<dd> <p> The <code>&quot;corelist&quot;</code> utility is now installed with perl (see ``New modules&#8217;&#8216; above). </p>
 </dd>
<dt>h2ph and h2xs</dt>
<dd> <p> <code>&quot;h2ph&quot;</code> and <code>&quot;h2xs&quot;</code> have been made more robust with regard to ``modern&#8217;&#8216; C code. </p>
<p> <code>&quot;h2xs&quot;</code> implements a new option <code>&quot;--use-xsloader&quot;</code> to force use of <code>&quot;XSLoader&quot;</code> even in backwards compatible modules. </p>
<p> The handling of authors&#8217; names that had apostrophes has been fixed. </p>
<p> Any enums with negative values are now skipped. </p>
 </dd>
<dt>perlivp</dt>
<dd> <p> <code>&quot;perlivp&quot;</code> no longer checks for <i>*.ph</i> files by default. Use the new <code>&quot;-a&quot;</code> option to run <i>all</i> tests. </p>
 </dd>
<dt>find2perl</dt>
<dd> <p> <code>&quot;find2perl&quot;</code> now assumes <code>&quot;-print&quot;</code> as a default action. Previously, it needed to be specified explicitly. </p>
<p> Several bugs have been fixed in <code>&quot;find2perl&quot;</code>, regarding <code>&quot;-exec&quot;</code> and <code>&quot;-eval&quot;</code>. Also the options <code>&quot;-path&quot;</code>, <code>&quot;-ipath&quot;</code> and <code>&quot;-iname&quot;</code> have been added. </p>
 </dd>
<dt>config_data</dt>
<dd> <p> <code>&quot;config_data&quot;</code> is a new utility that comes with <code>&quot;Module::Build&quot;</code>. It provides a command-line interface to the configuration of Perl modules that use Module::Build&#8217;s framework of configurability (that is, <code>*::ConfigData</code> modules that contain local configuration information for their parent modules.) </p>
 </dd>
<dt>cpanp</dt>
<dd> <p> <code>&quot;cpanp&quot;</code>, the <font SIZE="-1">CPANPLUS</font> shell, has been added. (<code>&quot;cpanp-run-perl&quot;</code>, a helper for <font SIZE="-1">CPANPLUS</font> operation, has been added too, but isn&#8217;t intended for direct use). </p>
 </dd>
<dt>cpan2dist</dt>
<dd> <p> <code>&quot;cpan2dist&quot;</code> is a new utility that comes with <font SIZE="-1">CPANPLUS.</font> It&#8217;s a tool to create distributions (or packages) from <font SIZE="-1">CPAN</font> modules. </p>
 </dd>
<dt>pod2html</dt>
<dd> <p> The output of <code>&quot;pod2html&quot;</code> has been enhanced to be more customizable via <font SIZE="-1">CSS.</font> Some formatting problems were also corrected. (Jari Aalto) </p>
 </dd></dl>
<h2>New Documentation</h2>
<p> The perlpragma manpage documents how to write one&#8217;s own lexical pragmas in pure Perl (something that is possible starting with 5.9.4). </p>
<p> The new perlglossary manpage is a glossary of terms used in the Perl documentation, technical and otherwise, kindly provided by O&#8217;Reilly Media, Inc. </p>
<p> The perlreguts manpage, courtesy of Yves Orton, describes internals of the Perl regular expression engine. </p>
<p> The perlreapi manpage describes the interface to the perl interpreter used to write pluggable regular expression engines (by Ævar Arnfjörð Bjarmason). </p>
<p> The perlunitut manpage is a tutorial for programming with Unicode and string encodings in Perl, courtesy of Juerd Waalboer. </p>
<p> A new manual page, perlunifaq (the Perl Unicode <font SIZE="-1">FAQ</font>), has been added (Juerd Waalboer). </p>
<p> The perlcommunity manpage gives a description of the Perl community on the Internet and in real life. (Edgar ``Trizor&#8217;&#8216; Bering) </p>
<p> The <font SIZE="-1">CORE</font> manual page documents the <code>&quot;CORE::&quot;</code> namespace. (Tels) </p>
<p> The long-existing feature of <code>&quot;/(?{...})/&quot;</code> regexps setting <code>$_</code> and <code>pos()</code> is now documented.  </p>
<h2>Performance Enhancements</h2>
<h3>In-place sorting</h3>
<p> Sorting arrays in place (<code>&quot;@a = sort @a&quot;</code>) is now optimized to avoid making a temporary copy of the array. </p>
<p> Likewise, <code>&quot;reverse sort ...&quot;</code> is now optimized to sort in reverse, avoiding the generation of a temporary intermediate list.  </p>
<h3>Lexical array access</h3>
<p> Access to elements of lexical arrays via a numeric constant between 0 and 255 is now faster. (This used to be only the case for global arrays.)  </p>
<font SIZE="-1"></font><h3>XS-assisted SWASHGET</h3>
<p> Some pure-perl code that perl was using to retrieve Unicode properties and transliteration mappings has been reimplemented in <font SIZE="-1">XS.</font>  </p>
<h3>Constant subroutines</h3>
<p> The interpreter internals now support a far more memory efficient form of inlineable constants. Storing a reference to a constant value in a symbol table is equivalent to a full typeglob referencing a constant subroutine, but using about 400 bytes less memory. This proxy constant subroutine is automatically upgraded to a real typeglob with subroutine if necessary. The approach taken is analogous to the existing space optimisation for subroutine stub declarations, which are stored as plain scalars in place of the full typeglob. </p>
<p> Several of the core modules have been converted to use this feature for their system dependent constants &#8211; as a result <code>&quot;use POSIX;&quot;</code> now takes about 200K less memory.  </p>
<h3>PERL_DONT_CREATE_GVSV</h3>
<p> The new compilation flag <code>&quot;PERL_DONT_CREATE_GVSV&quot;</code>, introduced as an option in perl 5.8.8, is turned on by default in perl 5.9.3. It prevents perl from creating an empty scalar with every new typeglob. See perl589delta for details.  </p>
<h3>Weak references are cheaper</h3>
<p> Weak reference creation is now <i><a href="/docs/linux/man/1-O/">O</a>(1)</i> rather than <i><a href="/docs/linux/man/n-O/">O</a>(n)</i>, courtesy of Nicholas Clark. Weak reference deletion remains <i><a href="/docs/linux/man/n-O/">O</a>(n)</i>, but if deletion only happens at program exit, it may be skipped completely.  </p>
<code></code><h3>sort() enhancements</h3>
<p> Salvador Fandiño provided improvements to reduce the memory usage of <code>&quot;sort&quot;</code> and to speed up some cases.  </p>
<h3>Memory optimisations</h3>
<p> Several internal data structures (typeglobs, GVs, CVs, formats) have been restructured to use less memory. (Nicholas Clark)  </p>
<font SIZE="-1"></font><h3>UTF-8 cache optimisation</h3>
<p> The <font SIZE="-1">UTF-8</font> caching code is now more efficient, and used more often. (Nicholas Clark)  </p>
<h3>Sloppy stat on Windows</h3>
<p> On Windows, perl&#8217;s <code>stat()</code> function normally opens the file to determine the link count and update attributes that may have been changed through hard links. Setting ${^WIN32_SLOPPY_STAT} to a true value speeds up <code>stat()</code> by not performing this operation. (Jan Dubois)  </p>
<h3>Regular expressions optimisations</h3>
<dl>
<dt>Engine de-recursivised</dt>
<dd> <p> The regular expression engine is no longer recursive, meaning that patterns that used to overflow the stack will either die with useful explanations, or run to completion, which, since they were able to blow the stack before, will likely take a very long time to happen. If you were experiencing the occasional stack overflow (or segfault) and upgrade to discover that now perl apparently hangs instead, look for a degenerate regex. (Dave Mitchell) </p>
 </dd>
<dt>Single char char-classes treated as literals</dt>
<dd> <p> Classes of a single character are now treated the same as if the character had been used as a literal, meaning that code that uses char-classes as an escaping mechanism will see a speedup. (Yves Orton) </p>
 </dd>
<dt>Trie optimisation of literal string alternations</dt>
<dd> <p> Alternations, where possible, are optimised into more efficient matching structures. String literal alternations are merged into a trie and are matched simultaneously. This means that instead of O(N) time for matching N alternations at a given point, the new code performs in <a href="/docs/linux/man/1-O/">O</a>(1) time. A new special variable, ${^RE_TRIE_MAXBUF}, has been added to fine-tune this optimization. (Yves Orton) </p>
<p> <code>Note:</code> Much code exists that works around perl&#8217;s historic poor performance on alternations. Often the tricks used to do so will disable the new optimisations. Hopefully the utility modules used for this purpose will be educated about these new optimisations. </p>
 </dd>
<dt>Aho-Corasick start-point optimisation</dt>
<dd> <p> When a pattern starts with a trie-able alternation and there aren&#8217;t better optimisations available, the regex engine will use Aho-Corasick matching to find the start point. (Yves Orton) </p>
 </dd></dl>
<h2>Installation and Configuration Improvements</h2>
<h3>Configuration improvements</h3>
<dl>
<dt>&quot;-Dusesitecustomize&quot;</dt>
<dd> <p> Run-time customization of <code>@INC</code> can be enabled by passing the <code>&quot;-Dusesitecustomize&quot;</code> flag to Configure. When enabled, this will make perl run <i></i>$sitelibexp <i>/sitecustomize.pl</i> before anything else. This script can then be set up to add additional entries to <code>@INC</code>. </p>
 </dd>
<dt>Relocatable installations</dt>
<dd> <p> There is now Configure support for creating a relocatable perl tree. If you Configure with <code>&quot;-Duserelocatableinc&quot;</code>, then the paths in <code>@INC</code> (and everything else in <code>%Config</code>) can be optionally located via the path of the perl executable. </p>
<p> That means that, if the string <code>&quot;.../&quot;</code> is found at the start of any path, it&#8217;s substituted with the directory of $^X. So, the relocation can be configured on a per-directory basis, although the default with <code>&quot;-Duserelocatableinc&quot;</code> is that everything is relocated. The initial install is done to the original configured prefix. </p>
 </dd>
<dt><code>strlcat()</code> and <code>strlcpy()</code></dt>
<dd> <p> The configuration process now detects whether <code>strlcat()</code> and <code>strlcpy()</code> are available. When they are not available, perl&#8217;s own version is used (from Russ Allbery&#8217;s public domain implementation). Various places in the perl interpreter now use them. (Steve Peters) </p>
 </dd>
<dt>&quot;d_pseudofork&quot; and &quot;d_printf_format_null&quot;</dt>
<dd> <p> A new configuration variable, available as <code>$Config{d_pseudofork}</code> in the Config module, has been added, to distinguish real <code>fork()</code> support from fake pseudofork used on Windows platforms. </p>
<p> A new configuration variable, <code>&quot;d_printf_format_null&quot;</code>, has been added, to see if printf-like formats are allowed to be <font SIZE="-1">NULL.</font> </p>
 </dd>
<dt>Configure help</dt>
<dd> <p> <code>&quot;Configure -h&quot;</code> has been extended with the most commonly used options. </p>
 </dd></dl>
<h3>Compilation improvements</h3>
<dl>
<dt>Parallel build</dt>
<dd> <p> Parallel makes should work properly now, although there may still be problems if <code>&quot;make test&quot;</code> is instructed to run in parallel. </p>
 </dd>
<dt>Borland&#8217;s compilers support</dt>
<dd> <p> Building with Borland&#8217;s compilers on Win32 should work more smoothly. In particular Steve Hay has worked to side step many warnings emitted by their compilers and at least one C compiler internal error. </p>
 </dd>
<dt>Static build on Windows</dt>
<dd> <p> Perl extensions on Windows now can be statically built into the Perl <font SIZE="-1">DLL.</font> </p>
<p> Also, it&#8217;s now possible to build a <code>&quot;perl-static.exe&quot;</code> that doesn&#8217;t depend on the Perl <font SIZE="-1">DLL</font> on Win32. See the Win32 makefiles for details. (Vadim Konovalov) </p>
 </dd>
<dt>ppport.h files</dt>
<dd> <p> All <i>ppport.h</i> files in the <font SIZE="-1">XS</font> modules bundled with perl are now autogenerated at build time. (Marcus Holland-Moritz) </p>
 </dd>
<dt>C<font SIZE="-2">++</font> compatibility</dt>
<dd> <p> Efforts have been made to make perl and the core <font SIZE="-1">XS</font> modules compilable with various C<font SIZE="-2">++</font> compilers (although the situation is not perfect with some of the compilers on some of the platforms tested.) </p>
 </dd>
<dt>Support for Microsoft 64-bit compiler</dt>
<dd> <p> Support for building perl with Microsoft&#8217;s 64-bit compiler has been improved. (ActiveState) </p>
 </dd>
<dt>Visual C<font SIZE="-2">++</font></dt>
<dd> <p> Perl can now be compiled with Microsoft Visual C<font SIZE="-2">++</font> 2005 (and 2008 Beta 2). </p>
 </dd>
<dt>Win32 builds</dt>
<dd> <p> All win32 builds (MS-Win, WinCE) have been merged and cleaned up. </p>
 </dd></dl>
<h3>Installation improvements</h3>
<dl>
<dt>Module auxiliary files</dt>
<dd> <p> <font SIZE="-1">README</font> files and changelogs for <font SIZE="-1">CPAN</font> modules bundled with perl are no longer installed. </p>
 </dd></dl>
<h3>New Or Improved Platforms</h3>
<p> Perl has been reported to work on Symbian <font SIZE="-1">OS.</font> See perlsymbian for more information. </p>
<p> Many improvements have been made towards making Perl work correctly on z/OS. </p>
<p> Perl has been reported to work on DragonFlyBSD and MidnightBSD. </p>
<p> Perl has also been reported to work on NexentaOS ( <a rel="nofollow" href="http://www.gnusolaris.org/">http://www.gnusolaris.org/</a> ). </p>
<p> The <font SIZE="-1">VMS</font> port has been improved. See perlvms. </p>
<p> Support for Cray <font SIZE="-1">XT4</font> Catamount/Qk has been added. See <i>hints/catamount.sh</i> in the source code distribution for more information. </p>
<p> Vendor patches have been merged for RedHat and Gentoo. </p>
<p> <code>DynaLoader::dl_unload_file()</code> now works on Windows.  </p>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>strictures in regexp-eval blocks</dt>
<dd> <p> <code>&quot;strict&quot;</code> wasn&#8217;t in effect in regexp-eval blocks (<code>&quot;/(?{...})/&quot;</code>). </p>
 </dd>
<dt>Calling <code>CORE::require()</code></dt>
<dd> <p> <code>CORE::require()</code> and <code>CORE::do()</code> were always parsed as <code>require()</code> and <code>do()</code> when they were overridden. This is now fixed. </p>
 </dd>
<dt>Subscripts of slices</dt>
<dd> <p> You can now use a non-arrowed form for chained subscripts after a list slice, like in: </p>
<pre><code>    ({foo =&gt; &quot;bar&quot;})[0]{foo}
</code></pre>
<p> This used to be a syntax error; a <code>&quot;-&gt;&quot;</code> was required. </p>
 </dd>
<dt>&quot;no warnings &#8216;category&#8217;&quot; works correctly with -w</dt>
<dd> <p> Previously when running with warnings enabled globally via <code>&quot;-w&quot;</code>, selective disabling of specific warning categories would actually turn off all warnings. This is now fixed; now <code>&quot;no warnings &#8216;io&#8217;;&quot;</code> will only turn off warnings in the <code>&quot;io&quot;</code> class. Previously it would erroneously turn off all warnings. </p>
 </dd>
<dt>threads improvements</dt>
<dd> <p> Several memory leaks in ithreads were closed. Also, ithreads were made less memory-intensive. </p>
<p> <code>&quot;threads&quot;</code> is now a dual-life module, also available on <font SIZE="-1">CPAN.</font> It has been expanded in many ways. A <code>kill()</code> method is available for thread signalling. One can get thread status, or the list of running or joinable threads. </p>
<p> A new <code>&quot;threads-&gt;exit()&quot;</code> method is used to exit from the application (this is the default for the main thread) or from the current thread only (this is the default for all other threads). On the other hand, the <code>exit()</code> built-in now always causes the whole application to terminate. (Jerry D. Hedden) </p>
 </dd>
<dt><code>chr()</code> and negative values</dt>
<dd> <p> <code>chr()</code> on a negative value now gives <code>&quot;\x{FFFD}&quot;</code>, the Unicode replacement character, unless when the <code>&quot;bytes&quot;</code> pragma is in effect, where the low eight bits of the value are used. </p>
 </dd>
<dt><font SIZE="-1">PERL5SHELL</font> and tainting</dt>
<dd> <p> On Windows, the <font SIZE="-1">PERL5SHELL</font> environment variable is now checked for taintedness. (Rafael Garcia-Suarez) </p>
 </dd>
<dt>Using *FILE{<font SIZE="-1">IO</font>}</dt>
<dd> <p> <code>&quot;stat()&quot;</code> and <code>&quot;-X&quot;</code> filetests now treat *FILE{<font SIZE="-1">IO</font>} filehandles like *FILE filehandles. (Steve Peters) </p>
 </dd>
<dt>Overloading and reblessing</dt>
<dd> <p> Overloading now works when references are reblessed into another class. Internally, this has been implemented by moving the flag for ``overloading&#8217;&#8216; from the reference to the referent, which logically is where it should always have been. (Nicholas Clark) </p>
 </dd>
<dt>Overloading and <font SIZE="-1">UTF-8</font></dt>
<dd> <p> A few bugs related to <font SIZE="-1">UTF-8</font> handling with objects that have stringification overloaded have been fixed. (Nicholas Clark) </p>
 </dd>
<dt>eval memory leaks fixed</dt>
<dd> <p> Traditionally, <code>&quot;eval &#8216;syntax error&#8217;&quot;</code> has leaked badly. Many (but not all) of these leaks have now been eliminated or reduced. (Dave Mitchell) </p>
 </dd>
<dt>Random device on Windows</dt>
<dd> <p> In previous versions, perl would read the file <i>/dev/urandom</i> if it existed when seeding its random number generator. That file is unlikely to exist on Windows, and if it did would probably not contain appropriate data, so perl no longer tries to read it on Windows. (Alex Davies) </p>
 </dd>
<dt><font SIZE="-1">PERLIO_DEBUG</font></dt>
<dd> <p> The <code>&quot;PERLIO_DEBUG&quot;</code> environment variable no longer has any effect for setuid scripts and for scripts run with <code>-T</code>. </p>
<p> Moreover, with a thread-enabled perl, using <code>&quot;PERLIO_DEBUG&quot;</code> could lead to an internal buffer overflow. This has been fixed. </p>
 </dd>
<dt>PerlIO::scalar and read-only scalars</dt>
<dd> <p> PerlIO::scalar will now prevent writing to read-only scalars. Moreover, <code>seek()</code> is now supported with PerlIO::scalar-based filehandles, the underlying string being zero-filled as needed. (Rafael, Jarkko Hietaniemi) </p>
 </dd>
<dt><code>study()</code> and <font SIZE="-1">UTF-8</font></dt>
<dd> <p> <code>study()</code> never worked for <font SIZE="-1">UTF-8</font> strings, but could lead to false results. It&#8217;s now a no-op on <font SIZE="-1">UTF-8</font> data. (Yves Orton) </p>
 </dd>
<dt>Critical signals</dt>
<dd> <p> The signals <font SIZE="-1">SIGILL, SIGBUS</font> and <font SIZE="-1">SIGSEGV</font> are now always delivered in an ``unsafe&#8217;&#8216; manner (contrary to other signals, that are deferred until the perl interpreter reaches a reasonably stable state; see ``Deferred Signals (Safe Signals)&#8216;&#8216; in perlipc). (Rafael) </p>
 </dd>
<dt>@INC-hook fix</dt>
<dd> <p> When a module or a file is loaded through an <code>@INC</code>-hook, and when this hook has set a filename entry in <code>%INC</code>, __FILE__ is now set for this module accordingly to the contents of that <code>%INC</code> entry. (Rafael) </p>
 </dd>
<dt>&quot;-t&quot; switch fix</dt>
<dd> <p> The <code>&quot;-w&quot;</code> and <code>&quot;-t&quot;</code> switches can now be used together without messing up which categories of warnings are activated. (Rafael) </p>
 </dd>
<dt>Duping <font SIZE="-1">UTF-8</font> filehandles</dt>
<dd> <p> Duping a filehandle which has the <code>&quot;:utf8&quot;</code> PerlIO layer set will now properly carry that layer on the duped filehandle. (Rafael) </p>
 </dd>
<dt>Localisation of hash elements</dt>
<dd> <p> Localizing a hash element whose key was given as a variable didn&#8217;t work correctly if the variable was changed while the <code>local()</code> was in effect (as in <code>&quot;local $h{$x}; ++$x&quot;</code>). (Bo Lindbergh) </p>
 </dd></dl>
<h2>New or Changed Diagnostics</h2>
<dl>
<dt>Use of uninitialized value</dt>
<dd> <p> Perl will now try to tell you the name of the variable (if any) that was undefined. </p>
 </dd>
<dt>Deprecated use of <code>my()</code> in false conditional</dt>
<dd> <p> A new deprecation warning, <i>Deprecated use of </i>my()<i> in false conditional</i>, has been added, to warn against the use of the dubious and deprecated construct </p>
<pre><code>    my $x if 0;
</code></pre>
<p> See perldiag. Use <code>&quot;state&quot;</code> variables instead. </p>
 </dd>
<dt>!=~ should be !~</dt>
<dd> <p> A new warning, <code>&quot;!=~ should be !~&quot;</code>, is emitted to prevent this misspelling of the non-matching operator. </p>
 </dd>
<dt>Newline in left-justified string</dt>
<dd> <p> The warning <i>Newline in left-justified string</i> has been removed. </p>
 </dd>
<dt>Too late for &quot;-T&quot; option</dt>
<dd> <p> The error <i>Too late for ``-T&#8217;&#8216; option</i> has been reformulated to be more descriptive. </p>
 </dd>
<dt>&quot;%s&quot; variable %s masks earlier declaration</dt>
<dd> <p> This warning is now emitted in more consistent cases; in short, when one of the declarations involved is a <code>&quot;my&quot;</code> variable: </p>
<pre><code>    my $x; my $x; # warns
    my $x; our $x; # warns
    our $x; my $x; # warns
</code></pre>
<p> On the other hand, the following: </p>
<pre><code>    our $x; our $x;
</code></pre>
<p> now gives a <code>&quot;&quot;our&quot; variable %s redeclared&quot;</code> warning. </p>
 </dd>
<dt><code>readdir()</code>/<code>closedir()</code>/etc. attempted on invalid dirhandle</dt>
<dd> <p> These new warnings are now emitted when a dirhandle is used but is either closed or not really a dirhandle. </p>
 </dd>
<dt>Opening dirhandle/filehandle %s also as a file/directory</dt>
<dd> <p> Two deprecation warnings have been added: (Rafael) </p>
<pre><code>    Opening dirhandle %s also as a file
    Opening filehandle %s also as a directory
</code></pre>
 </dd>
<dt>Use of -P is deprecated</dt>
<dd> <p> Perl&#8217;s command-line switch <code>&quot;-P&quot;</code> is now deprecated. </p>
 </dd>
<dt>v-string in use/require is non-portable</dt>
<dd> <p> Perl will warn you against potential backwards compatibility problems with the <code>&quot;use VERSION&quot;</code> syntax. </p>
 </dd>
<dt>perl -V</dt>
<dd> <p> <code>&quot;perl -V&quot;</code> has several improvements, making it more useable from shell scripts to get the value of configuration variables. See perlrun for details. </p>
 </dd></dl>
<h2>Changed Internals</h2>
<p> In general, the source code of perl has been refactored, tidied up, and optimized in many places. Also, memory management and allocation has been improved in several points. </p>
<p> When compiling the perl core with gcc, as many gcc warning flags are turned on as is possible on the platform. (This quest for cleanliness doesn&#8217;t extend to <font SIZE="-1">XS</font> code because we cannot guarantee the tidiness of code we didn&#8217;t write.) Similar strictness flags have been added or tightened for various other C compilers.  </p>
<h3>Reordering of SVt_* constants</h3>
<p> The relative ordering of constants that define the various types of <code>&quot;SV&quot;</code> have changed; in particular, <code>&quot;SVt_PVGV&quot;</code> has been moved before <code>&quot;SVt_PVLV&quot;</code>, <code>&quot;SVt_PVAV&quot;</code>, <code>&quot;SVt_PVHV&quot;</code> and <code>&quot;SVt_PVCV&quot;</code>. This is unlikely to make any difference unless you have code that explicitly makes assumptions about that ordering. (The inheritance hierarchy of <code>&quot;B::*&quot;</code> objects has been changed to reflect this.)  </p>
<h3>Elimination of SVt_PVBM</h3>
<p> Related to this, the internal type <code>&quot;SVt_PVBM&quot;</code> has been removed. This dedicated type of <code>&quot;SV&quot;</code> was used by the <code>&quot;index&quot;</code> operator and parts of the regexp engine to facilitate fast Boyer-Moore matches. Its use internally has been replaced by <code>&quot;SV&quot;</code>s of type <code>&quot;SVt_PVGV&quot;</code>.  </p>
<h3>New type SVt_BIND</h3>
<p> A new type <code>&quot;SVt_BIND&quot;</code> has been added, in readiness for the project to implement Perl 6 on 5. There deliberately is no implementation yet, and they cannot yet be created or destroyed.  </p>
<font SIZE="-1"></font><h3>Removal of CPP symbols</h3>
<p> The C preprocessor symbols <code>&quot;PERL_PM_APIVERSION&quot;</code> and <code>&quot;PERL_XS_APIVERSION&quot;</code>, which were supposed to give the version number of the oldest perl binary-compatible (resp. source-compatible) with the present one, were not used, and sometimes had misleading values. They have been removed.  </p>
<h3>Less space is used by ops</h3>
<p> The <code>&quot;BASEOP&quot;</code> structure now uses less space. The <code>&quot;op_seq&quot;</code> field has been removed and replaced by a single bit bit-field <code>&quot;op_opt&quot;</code>. <code>&quot;op_type&quot;</code> is now 9 bits long. (Consequently, the <code>&quot;B::OP&quot;</code> class doesn&#8217;t provide an <code>&quot;seq&quot;</code> method anymore.)  </p>
<h3>New parser</h3>
<p> perl&#8217;s parser is now generated by bison (it used to be generated by byacc.) As a result, it seems to be a bit more robust. </p>
<p> Also, Dave Mitchell improved the lexer debugging output under <code>&quot;-DT&quot;</code>.  </p>
<h3>Use of const</h3>
<p> Andy Lester supplied many improvements to determine which function parameters and local variables could actually be declared <code>&quot;const&quot;</code> to the C compiler. Steve Peters provided new <code>*_set</code> macros and reworked the core to use these rather than assigning to macros in <font SIZE="-1">LVALUE</font> context.  </p>
<h3>Mathoms</h3>
<p> A new file, <i>mathoms.c</i>, has been added. It contains functions that are no longer used in the perl core, but that remain available for binary or source compatibility reasons. However, those functions will not be compiled in if you add <code>&quot;-DNO_MATHOMS&quot;</code> in the compiler flags.  </p>
<h3>AvFLAGS has been removed</h3>
<p> The <code>&quot;AvFLAGS&quot;</code> macro has been removed.  </p>
<h3>av_* changes</h3>
<p> The <code>&quot;av_*()&quot;</code> functions, used to manipulate arrays, no longer accept null <code>&quot;AV*&quot;</code> parameters.  </p>
<h3>$^H and %^H</h3>
<p> The implementation of the special variables $^H and %^H has changed, to allow implementing lexical pragmas in pure Perl.  </p>
<h3>B:: modules inheritance changed</h3>
<p> The inheritance hierarchy of <code>&quot;B::&quot;</code> modules has changed; <code>&quot;B::NV&quot;</code> now inherits from <code>&quot;B::SV&quot;</code> (it used to inherit from <code>&quot;B::IV&quot;</code>).  </p>
<h3>Anonymous hash and array constructors</h3>
<p> The anonymous hash and array constructors now take 1 op in the optree instead of 3, now that pp_anonhash and pp_anonlist return a reference to a hash/array when the op is flagged with OPf_SPECIAL. (Nicholas Clark)  </p>
<h2>Known Problems</h2>
<p> There&#8217;s still a remaining problem in the implementation of the lexical <code>$_</code>: it doesn&#8217;t work inside <code>&quot;/(?{...})/&quot;</code> blocks. (See the <font SIZE="-1">TODO</font> test in <i>t/op/mydef.t</i>.) </p>
<p> Stacked filetest operators won&#8217;t work when the <code>&quot;filetest&quot;</code> pragma is in effect, because they rely on the <code>stat()</code> buffer <code>&quot;_&quot;</code> being populated, and filetest bypasses <code>stat()</code>.  </p>
<font SIZE="-1"></font><h3>UTF-8 problems</h3>
<p> The handling of Unicode still is unclean in several places, where it&#8217;s dependent on whether a string is internally flagged as <font SIZE="-1">UTF-8.</font> This will be made more consistent in perl 5.12, but that won&#8217;t be possible without a certain amount of backwards incompatibility.  </p>
<h2>Platform Specific Problems</h2>
<p> When compiled with g++ and thread support on Linux, it&#8217;s reported that the <code>$!</code> stops working correctly. This is related to the fact that the glibc provides two <code><a href="/docs/linux/man/3-strerror_r/">strerror_r</a></code>(3) implementation, and perl selects the wrong one.  </p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://rt.perl.org/rt3/">http://rt.perl.org/rt3/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the <code>perlbug</code> program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <code>&quot;perl -V&quot;</code>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team.  </p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file and the perl590delta to perl595delta man pages for exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
<h2>Index</h2>
