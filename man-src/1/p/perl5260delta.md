---
title: "perl5260delta(1)"
name: "perl5260delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5260delta/"
description: "perl5260delta – what is new for perl v5.26.0"
---

<h2 class="name">NAME</h2>
<p> perl5260delta &#8211; what is new for perl v5.26.0 </p>
<h2>DESCRIPTION</h2>
<p> This document describes the differences between the 5.24.0 release and the 5.26.0 release.</p>
<h2>Notice</h2>
<p> This release includes three updates with widespread effects:</p>
<dl>
<dt>&bull;</dt>
<dd> <tt>&quot;.&quot;</tt> no longer in <tt>@INC</tt> </dd>
<p> For security reasons, the current directory (<tt>&quot;.&quot;</tt>) is no longer included by default at the end of the module search path (<tt>@INC</tt>). This may have widespread implications for the building, testing and installing of modules, and for the execution of scripts. See the section &quot;Removal of the current directory (<tt>&quot;.&quot;</tt>) from <tt>@INC</tt>&quot; for the full details.</p>
<dt>&bull;</dt>
<dd> <tt>&quot;do&quot;</tt> may now warn </dd>
<p> <tt>&quot;do&quot;</tt> now gives a deprecation warning when it fails to load a file which it would have loaded had <tt>&quot;.&quot;</tt> been in <tt>@INC</tt>.</p>
<dt>&bull;</dt>
<dd> In regular expression patterns, a literal left brace <tt>&quot;{&quot;</tt> should be escaped </dd>
<p> See &quot;Unescaped literal <tt>&quot;{&quot;</tt> characters in regular expression patterns are no longer permissible&quot;.</dl>
<h2>Core Enhancements</h2>
<h3>Lexical subroutines are no longer experimental</h3>
<p> Using the <tt>&quot;lexical_subs&quot;</tt> feature introduced in v5.18 no longer emits a warning. Existing code that disables the <tt>&quot;experimental::lexical_subs&quot;</tt> warning category that the feature previously used will continue to work. The <tt>&quot;lexical_subs&quot;</tt> feature has no effect; all Perl code can use lexical subroutines, regardless of what feature declarations are in scope.</p>
<h3>Indented Here-documents</h3>
<p> This adds a new modifier <tt>&quot;~&quot;</tt> to here-docs that tells the parser that it should look for <tt>&quot;/^\s*$DELIM
/&quot;</tt> as the closing delimiter. </p>
<p> These syntaxes are all supported: </p>
<pre><code>
    &lt;&lt;~EOF;
    &lt;&lt;~\EOF;
    &lt;&lt;~'EOF';
    &lt;&lt;~"EOF";
    &lt;&lt;~`EOF`;
    &lt;&lt;~ 'EOF';
    &lt;&lt;~ "EOF";
    &lt;&lt;~ `EOF`;
</code></pre>
<p> The <tt>&quot;~&quot;</tt> modifier will strip, from each line in the here-doc, the same whitespace that appears before the delimiter. </p>
<p> Newlines will be copied as-is, and lines that don&#8217;t include the proper beginning whitespace will cause perl to croak. </p>
<p> For example: </p>
<p>if (1) {<br />
    print &lt;&lt; ~EOF;<br />
    Hello there<br />
        EOF<br />
}</p>
<p> prints &#8220;Hello there
&#8221; with no leading whitespace.</p>
<h3>New regular expression modifier /xx</h3>
<p> Specifying two <tt>&quot;x&quot;</tt> characters to modify a regular expression pattern does everything that a single one does, but additionally <font SIZE="-1">TAB</font> and <font SIZE="-1">SPACE</font> characters within a bracketed character class are generally ignored and can be added to improve readability, like <tt>&quot;/[ ^ A-Z d-f p-x ]/xx&quot;</tt>. Details are at &#8220;/x and /xx&#8221; in perlre.</p>
<h3>@{^CAPTURE}, %{^CAPTURE}, and %{^CAPTURE_ALL}</h3>
<p> <tt>&quot;@{^CAPTURE}&quot;</tt> exposes the capture buffers of the last match as an array. So <tt>$1</tt> is <tt>&quot;${^CAPTURE}[0]&quot;</tt>. This is a more efficient equivalent to code like <tt>&quot;substr($matched_string,$-[0],$+[0]-$-[0])&quot;</tt>, and you don&#8217;t have to keep track of the <tt>$matched_string</tt> either. This variable has no single character equivalent. Note that, like the other regex magic variables, the contents of this variable is dynamic; if you wish to store it beyond the lifetime of the match you must copy it to another array. </p>
<p> <tt>&quot;%{^CAPTURE}&quot;</tt> is equivalent to <tt>&quot;%+&quot;</tt> (<i>i.e.</i>, named captures). Other than being more self-documenting there is no difference between the two forms. </p>
<p> <tt>&quot;%{^CAPTURE_ALL}&quot;</tt> is equivalent to <tt>&quot;%-&quot;</tt> (<i>i.e.</i>, all named captures). Other than being more self-documenting there is no difference between the two forms.</p>
<h3>Declaring a reference to a variable</h3>
<p> As an experimental feature, Perl now allows the referencing operator to come after <tt>&quot;my()&quot;</tt>, <tt>&quot;state()&quot;</tt>, <tt>&quot;our()&quot;</tt>, or <tt>&quot;local()&quot;</tt>. This syntax must be enabled with <tt>&quot;use feature 'declared_refs'&quot;</tt>. It is experimental, and will warn by default unless <tt>&quot;no warnings 'experimental::refaliasing'&quot;</tt> is in effect. It is intended mainly for use in assignments to references. For example: </p>
<pre>
    use experimental 'refaliasing', 'declared_refs';
    my \$a = \$b;
</pre>
<p> See &#8220;Assigning to References&#8221; in perlref for more details.</p>
<h3>Unicode 9.0 is now supported</h3>
<p> A list of changes is at &lt;<a rel="nofollow" href="http://www.unicode.org/versions/Unicode9.0.0/">http://www.unicode.org/versions/Unicode9.0.0/</a>&gt;. Modules that are shipped with core Perl but not maintained by p5p do not necessarily support Unicode 9.0. Unicode::Normalize does work on 9.0.</p>
<h3>Use of \p{script} uses the improved Script_Extensions property</h3>
<p> Unicode 6.0 introduced an improved form of the Script (<tt>&quot;sc&quot;</tt>) property, and called it Script_Extensions (<tt>&quot;scx&quot;</tt>). Perl now uses this improved version when a property is specified as just <tt>&quot;\p{</tt>script<tt>}&quot;</tt>. This should make programs more accurate when determining if a character is used in a given script, but there is a slight chance of breakage for programs that very specifically needed the old behavior. The meaning of compound forms, like <tt>&quot;\p{sc=</tt>script<tt>}&quot;</tt> are unchanged. See &#8220;Scripts&#8221; in perlunicode.</p>
<h3>Perl can now do default collation in <font SIZE="-1">UTF-8</font> locales on platforms that support it</h3>
<p> Some platforms natively do a reasonable job of collating and sorting in <font SIZE="-1">UTF-8</font> locales. Perl now works with those. For portability and full control, Unicode::Collate is still recommended, but now you may not need to do anything special to get good-enough results, depending on your application. See &quot;Category <tt>&quot;LC_COLLATE&quot;</tt>: Collation: Text Comparisons and Sorting&quot; in perllocale.</p>
<h3>Better locale collation of strings containing embedded NUL characters</h3>
<p> In locales that have multi-level character weights, <tt>&quot;NUL&quot;</tt>s are now ignored at the higher priority ones. There are still some gotchas in some strings, though. See &quot;Collation of strings containing embedded <tt>&quot;NUL&quot;</tt> characters&quot; in perllocale.</p>
<h3>CORE subroutines for hash and array functions callable via reference</h3>
<p> The hash and array functions in the <tt>&quot;CORE&quot;</tt> namespace (<tt>&quot;keys&quot;</tt>, <tt>&quot;each&quot;</tt>, <tt>&quot;values&quot;</tt>, <tt>&quot;push&quot;</tt>, <tt>&quot;pop&quot;</tt>, <tt>&quot;shift&quot;</tt>, <tt>&quot;unshift&quot;</tt> and <tt>&quot;splice&quot;</tt>) can now be called with ampersand syntax (<tt>&quot;&amp;CORE::keys(\%hash&quot;</tt>) and via reference (<tt>&quot;my $k = \&amp;CORE::keys; $k-&gt;(\%hash)&quot;</tt>). Previously they could only be used when inlined.</p>
<h3>New Hash Function For 64-bit Builds</h3>
<p> We have switched to a hybrid hash function to better balance performance for short and long keys. </p>
<p> For short keys, 16 bytes and under, we use an optimised variant of One At A Time Hard, and for longer keys we use Siphash 1-3. For very long keys this is a big improvement in performance. For shorter keys there is a modest improvement.</p>
<h2>Security</h2>
<h3>Removal of the current directory (.) from @INC</h3>
<p> The perl binary includes a default set of paths in <tt>@INC</tt>. Historically it has also included the current directory (<tt>&quot;.&quot;</tt>) as the final entry, unless run with taint mode enabled (<tt>&quot;perl -T&quot;</tt>). While convenient, this has security implications: for example, where a script attempts to load an optional module when its current directory is untrusted (such as <i>/tmp</i>), it could load and execute code from under that directory. </p>
<p> Starting with v5.26, <tt>&quot;.&quot;</tt> is always removed by default, not just under tainting. This has major implications for installing modules and executing scripts. </p>
<p> The following new features have been added to help ameliorate these issues.</p>
<dl>
<dt>&bull;</dt>
<dd> <i>Configure -Udefault_inc_excludes_dot</i> </dd>
<p> There is a new <i>Configure</i> option, <tt>&quot;default_inc_excludes_dot&quot;</tt> (enabled by default) which builds a perl executable without <tt>&quot;.&quot;</tt>; unsetting this option using <tt>&quot;-U&quot;</tt> reverts perl to the old behaviour. This may fix your path issues but will reintroduce all the security concerns, so don&#8217;t build a perl executable like this unless you&#8217;re <i>really</i> confident that such issues are not a concern in your environment.</p>
<dt>&bull;</dt>
<dd> <tt>&quot;PERL_USE_UNSAFE_INC&quot;</tt> </dd>
<p> There is a new environment variable recognised by the perl interpreter. If this variable has the value 1 when the perl interpreter starts up, then <tt>&quot;.&quot;</tt> will be automatically appended to <tt>@INC</tt> (except under tainting). </p>
<p> This allows you restore the old perl interpreter behaviour on a case-by-case basis. But note that this is intended to be a temporary crutch, and this feature will likely be removed in some future perl version. It is currently set by the <tt>&quot;cpan&quot;</tt> utility and <tt>&quot;Test::Harness&quot;</tt> to ease installation of <font SIZE="-1">CPAN</font> modules which have not been updated to handle the lack of dot. Once again, don&#8217;t use this unless you are sure that this will not reintroduce any security concerns.</p>
<dt>&bull;</dt>
<dd> A new deprecation warning issued by <tt>&quot;do&quot;</tt>. </dd>
<p> While it is well-known that <tt>&quot;use&quot;</tt> and <tt>&quot;require&quot;</tt> use <tt>@INC</tt> to search for the file to load, many people don&#8217;t realise that <tt>&quot;do &quot;file&quot;&quot;</tt> also searches <tt>@INC</tt> if the file is a relative path. With the removal of <tt>&quot;.&quot;</tt>, a simple <tt>&quot;do &quot;file.pl&quot;&quot;</tt> will fail to read in and execute <tt>&quot;file.pl&quot;</tt> from the current directory. Since this is commonly expected behaviour, a new deprecation warning is now issued whenever <tt>&quot;do&quot;</tt> fails to load a file which it otherwise would have found if a dot had been in <tt>@INC</tt>.</dl>
<p> Here are some things script and module authors may need to do to make their software work in the new regime.</p>
<dl>
<dt>&bull;</dt>
<dd> Script authors </dd>
<p> If the issue is within your own code (rather than within included modules), then you have two main options. Firstly, if you are confident that your script will only be run within a trusted directory (under which you expect to find trusted files and modules), then add <tt>&quot;.&quot;</tt> back into the path; <i>e.g.</i>: </p>
<p>BEGIN<br />
{<br />
    my $dir = &#8220;/some/trusted/directory&#8221;;<br />
    chdir $dir or die &#8220;Can&#8217;t chdir to $dir: $!
&#8221;;<br />
#safe now<br />
    push @INC, &#8216;.&#8217;;<br />
}<br />
use &#8220;Foo::Bar&#8221;;<br />
#may load / some / trusted / directory / Foo / Bar.pm do &#8220;config.pl&#8221;;<br />
#may load / some / trusted / directory / config.pl</p>
<p> On the other hand, if your script is intended to be run from within untrusted directories (such as <i>/tmp</i>), then your script suddenly failing to load files may be indicative of a security issue. You most likely want to replace any relative paths with full paths; for example, </p>
<pre>
    do &quot;foo_config.pl&quot;
</pre>
<p> might become </p>
<pre>
    do &quot;$ENV{HOME}/foo_config.pl&quot;
</pre>
<p> If you are absolutely certain that you want your script to load and execute a file from the current directory, then use a <tt>&quot;./&quot;</tt> prefix; for example: </p>
<pre>
    do &quot;./foo_config.pl&quot;
</pre>
<dt>&bull;</dt>
<dd> Installing and using <font SIZE="-1">CPAN</font> modules </dd>
<p> If you install a <font SIZE="-1">CPAN</font> module using an automatic tool like <tt>&quot;cpan&quot;</tt>, then this tool will itself set the <tt>&quot;PERL_USE_UNSAFE_INC&quot;</tt> environment variable while building and testing the module, which may be sufficient to install a distribution which hasn&#8217;t been updated to be dot-aware. If you want to install such a module manually, then you&#8217;ll need to replace the traditional invocation: </p>
<pre>
    perl Makefile.PL &amp;&amp; make &amp;&amp; make test &amp;&amp; make install
</pre>
<p> with something like </p>
<p>(export PERL_USE_UNSAFE_INC = 1;<br />
 perl Makefile.PL &amp;&amp; make &amp;&amp; make test &amp;&amp; make install)</p>
<p> Note that this only helps build and install an unfixed module. It&#8217;s possible for the tests to pass (since they were run under <tt>&quot;PERL_USE_UNSAFE_INC=1&quot;</tt>), but for the module itself to fail to perform correctly in production. In this case, you may have to temporarily modify your script until a fixed version of the module is released. For example: </p>
<p>use Foo::Bar;<br />
{<br />
    local @INC = (@INC, &#8216;.&#8217;);<br />
#assuming read_config() needs &#8216;.&#8217; in @INC<br />
    $config = Foo::Bar-&gt;read_config();<br />
}</p>
<p> This is only rarely expected to be necessary. Again, if doing this, assess the resultant risks first.</p>
<dt>&bull;</dt>
<dd> Module Authors </dd>
<p> If you maintain a <font SIZE="-1">CPAN</font> distribution, it may need updating to run in a dotless environment. Although <tt>&quot;cpan&quot;</tt> and other such tools will currently set the <tt>&quot;PERL_USE_UNSAFE_INC&quot;</tt> during module build, this is a temporary workaround for the set of modules which rely on <tt>&quot;.&quot;</tt> being in <tt>@INC</tt> for installation and testing, and this may mask deeper issues. It could result in a module which passes tests and installs, but which fails at run time. </p>
<p> During build, test, and install, it will normally be the case that any perl processes will be executing directly within the root directory of the untarred distribution, or a known subdirectory of that, such as <i>t/</i>. It may well be that <i>Makefile.PL</i> or <i>t/foo.t</i> will attempt to include local modules and configuration files using their direct relative filenames, which will now fail. </p>
<p> However, as described above, automatic tools like <i>cpan</i> will (for now) set the <tt>&quot;PERL_USE_UNSAFE_INC&quot;</tt> environment variable, which introduces dot during a build. </p>
<p> This makes it likely that your existing build and test code will work, but this may mask issues with your code which only manifest when used after install. It is prudent to try and run your build process with that variable explicitly disabled: </p>
<p>(export PERL_USE_UNSAFE_INC = 0;<br />
 perl Makefile.PL &amp;&amp; make &amp;&amp; make test &amp;&amp; make install)</p>
<p> This is more likely to show up any potential problems with your module&#8217;s build process, or even with the module itself. Fixing such issues will ensure both that your module can again be installed manually, and that it will still build once the <tt>&quot;PERL_USE_UNSAFE_INC&quot;</tt> crutch goes away. </p>
<p> When fixing issues in tests due to the removal of dot from <tt>@INC</tt>, reinsertion of dot into <tt>@INC</tt> should be performed with caution, for this too may suppress real errors in your runtime code. You are encouraged wherever possible to apply the aforementioned approaches with explicit absolute/relative paths, or to relocate your needed files into a subdirectory and insert that subdirectory into <tt>@INC</tt> instead. </p>
<p> If your runtime code has problems under the dotless <tt>@INC</tt>, then the comments above on how to fix for script authors will mostly apply here too. Bear in mind though that it is considered bad form for a module to globally add a dot to <tt>@INC</tt>, since it introduces both a security risk and hides issues of accidentally requiring dot in <tt>@INC</tt>, as explained above.</dl>
<h3>Escaped colons and relative paths in <font SIZE="-1">PATH</font></h3>
<p> On Unix systems, Perl treats any relative paths in the <tt>&quot;PATH&quot;</tt> environment variable as tainted when starting a new process. Previously, it was allowing a backslash to escape a colon (unlike the <font SIZE="-1">OS</font>), consequently allowing relative paths to be considered safe if the <font SIZE="-1">PATH</font> was set to something like <tt>&quot;/\:.&quot;</tt>. The check has been fixed to treat <tt>&quot;.&quot;</tt> as tainted in that example.</p>
<h3>New -Di switch is now required for PerlIO debugging output</h3>
<p> This is used for debugging of code within PerlIO to avoid recursive calls. Previously this output would be sent to the file specified by the <tt>&quot;PERLIO_DEBUG&quot;</tt> environment variable if perl wasn&#8217;t running setuid and the <tt>&quot;-T&quot;</tt> or <tt>&quot;-t&quot;</tt> switches hadn&#8217;t been parsed yet. </p>
<p> If perl performed output at a point where it hadn&#8217;t yet parsed its switches this could result in perl creating or overwriting the file named by <tt>&quot;PERLIO_DEBUG&quot;</tt> even when the <tt>&quot;-T&quot;</tt> switch had been supplied. </p>
<p> Perl now requires the <tt>&quot;-Di&quot;</tt> switch to be present before it will produce PerlIO debugging output. By default this is written to <tt>&quot;stderr&quot;</tt>, but can optionally be redirected to a file by setting the <tt>&quot;PERLIO_DEBUG&quot;</tt> environment variable. </p>
<p> If perl is running setuid or the <tt>&quot;-T&quot;</tt> switch was supplied, <tt>&quot;PERLIO_DEBUG&quot;</tt> is ignored and the debugging output is sent to <tt>&quot;stderr&quot;</tt> as for any other <tt>&quot;-D&quot;</tt> switch.</p>
<h2>Incompatible Changes</h2>
<h3>Unescaped literal { characters in regular expression patterns are no longer permissible</h3>
<p> You have to now say something like <tt>&quot;\{&quot;</tt> or <tt>&quot;[{]&quot;</tt> to specify to match a <font SIZE="-1">LEFT CURLY BRACKET</font>; otherwise, it is a fatal pattern compilation error. This change will allow future extensions to the language. </p>
<p> These have been deprecated since v5.16, with a deprecation message raised for some uses starting in v5.22. Unfortunately, the code added to raise the message was buggy and failed to warn in some cases where it should have. Therefore, enforcement of this ban for these cases is deferred until Perl 5.30, but the code has been fixed to raise a default-on deprecation message for them in the meantime. </p>
<p> Some uses of literal <tt>&quot;{&quot;</tt> occur in contexts where we do not foresee the meaning ever being anything but the literal, such as the very first character in the pattern, or after a <tt>&quot;|&quot;</tt> meaning alternation. Thus </p>
<pre>
 qr/{fee|{fie/
</pre>
<p> matches either of the strings <tt>&quot;{fee&quot;</tt> or <tt>&quot;{fie&quot;</tt>. To avoid forcing unnecessary code changes, these uses do not need to be escaped, and no warning is raised about them, and there are no current plans to change this. </p>
<p> But it is always correct to escape <tt>&quot;{&quot;</tt>, and the simple rule to remember is to always do so. </p>
<p> See Unescaped left brace in regex is illegal here.</p>
<h3>scalar(%hash) return signature changed</h3>
<p> The value returned for <tt>&quot;scalar(%hash)&quot;</tt> will no longer show information about the buckets allocated in the hash. It will simply return the count of used keys. It is thus equivalent to <tt>&quot;0+keys(%hash)&quot;</tt>. </p>
<p> A form of backward compatibility is provided via <tt>&quot;Hash::Util::bucket_ratio()&quot;</tt> which provides the same behavior as <tt>&quot;scalar(%hash)&quot;</tt> provided in Perl 5.24 and earlier.</p>
<h3>keys returned from an lvalue subroutine</h3>
<p> <tt>&quot;keys&quot;</tt> returned from an lvalue subroutine can no longer be assigned to in list context. </p>
<p>sub foo : lvalue{keys(% INC)}(foo) = 3;<br />
#death sub bar : lvalue<br />
{<br />
    keys(@_)<br />
}<br />
(bar) = 3;<br />
#also an error</p>
<p> This makes the lvalue sub case consistent with <tt>&quot;(keys %hash) = ...&quot;</tt> and <tt>&quot;(keys @_) = ...&quot;</tt>, which are also errors. [perl #128187] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128187">https://rt.perl.org/Public/Bug/Display.html?id=128187</a>&gt;</p>
<h3>The ${^ENCODING} facility has been removed</h3>
<p> The special behaviour associated with assigning a value to this variable has been removed. As a consequence, the encoding pragma&#8217;s default mode is no longer supported. If you still need to write your source code in encodings other than <font SIZE="-1">UTF-8,</font> use a source filter such as Filter::Encoding on <font SIZE="-1">CPAN</font> or encoding&#8217;s <tt>&quot;Filter&quot;</tt> option.</p>
<h3>POSIX::tmpnam() has been removed</h3>
<p> The fundamentally unsafe <tt>&quot;tmpnam()&quot;</tt> interface was deprecated in Perl 5.22 and has now been removed. In its place, you can use, for example, the File::Temp interfaces.</p>
<h3>require ::Foo::Bar is now illegal.</h3>
<p> Formerly, <tt>&quot;require ::Foo::Bar&quot;</tt> would try to read <i>/Foo/Bar.pm</i>. Now any bareword require which starts with a double colon dies instead.</p>
<h3>Literal control character variable names are no longer permissible</h3>
<p> A variable name may no longer contain a literal control character under any circumstances. These previously were allowed in single-character names on <font SIZE="-1">ASCII</font> platforms, but have been deprecated there since Perl 5.20. This affects things like <tt>&quot;$</tt></code>\cT <code>&quot;</code>, where <i>\cT</i> is a literal control (such as a <code>&quot;NAK&quot;</code> or <code>&quot;NEGATIVE ACKNOWLEDGE&quot;</code> character) in the source code.  </p>
<h3>NBSP is no longer permissible in \N{...}</h3>
<p> The name of a character may no longer contain non-breaking spaces. It has been deprecated to do so since Perl 5.22.  </p>
<h2>Deprecations</h2>
<h3>String delimiters that aren't stand-alone graphemes are now deprecated</h3>
<p> For Perl to eventually allow string delimiters to be Unicode grapheme clusters (which look like a single character, but may be a sequence of several ones), we have to stop allowing a single character delimiter that isn&#8217;t a grapheme by itself. These are unlikely to exist in actual code, as they would typically display as attached to the character in front of them.  </p>
<h3>\cX that maps to a printable is no longer deprecated</h3>
<p> This means we have no plans to remove this feature. It still raises a warning, but only if syntax warnings are enabled. The feature was originally intended to be a way to express non-printable characters that don&#8217;t have a mnemonic (<code>&quot;\t&quot;</code> and <code>&quot;\n&quot;</code> are mnemonics for two non-printable characters, but most non-printables don&#8217;t have a mnemonic.) But the feature can be used to specify a few printable characters, though those are more clearly expressed as the printable itself. See &lt;<a rel="nofollow" href="http://www.nntp.perl.org/group/perl.perl5.porters/2017/02/msg242944.html">http://www.nntp.perl.org/group/perl.perl5.porters/2017/02/msg242944.html</a>&gt;.  </p>
<h2>Performance Enhancements</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> A hash in boolean context is now sometimes faster, <i>e.g.</i> </p>
<pre><code>    if (!%h) { ... }
</code></pre>
<p> This was already special-cased, but some cases were missed (such as <code>&quot;grep %$_, @AoH&quot;</code>), and even the ones which weren&#8217;t have been improved. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> New Faster Hash Function on 64 bit builds </p>
<p> We use a different hash function for short and long keys. This should improve performance and security, especially for long keys. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> readline is faster </p>
<p> Reading from a file line-by-line with <code>&quot;readline()&quot;</code> or <code>&quot;&lt;&gt;&quot;</code> should now typically be faster due to a better implementation of the code that searches for the next newline character. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Assigning one reference to another, <i>e.g.</i> <code>&quot;$ref1 = $ref2&quot;</code> has been optimized in some cases. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Remove some exceptions to creating Copy-on-Write strings. The string buffer growth algorithm has been slightly altered so that you&#8217;re less likely to encounter a string which can&#8217;t be COWed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Better optimise array and hash assignment: where an array or hash appears in the <font SIZE="-1">LHS</font> of a list assignment, such as <code>&quot;(..., @a) = (...);&quot;</code>, it&#8217;s likely to be considerably faster, especially if it involves emptying the array/hash. For example, this code runs about a third faster compared to Perl 5.24.0: </p>
<pre><code>    my @a;
    for my $i (1..10_000_000) {
        @a = (1,2,3);
        @a = ();
    }
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Converting a single-digit string to a number is now substantially faster. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;split&quot;</code> builtin is now slightly faster in many cases: in particular for the two specially-handled forms </p>
<pre><code>    my @a = split ...;
    local @a = split ...;
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> The rather slow implementation for the experimental subroutine signatures feature has been made much faster; it is now comparable in speed with the traditional <code>&quot;my ($a, $b, @c) = @_&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Bareword constant strings are now permitted to take part in constant folding. They were originally exempted from constant folding in August 1999, during the development of Perl 5.6, to ensure that <code>&quot;use strict &quot;subs&quot;&quot;</code> would still apply to bareword constants. That has now been accomplished a different way, so barewords, like other constants, now gain the performance benefits of constant folding. </p>
<p> This also means that void-context warnings on constant expressions of barewords now report the folded constant operand, rather than the operation; this matches the behaviour for non-bareword constants. </p>
 </dd></dl>
<h2>Modules and Pragmata</h2>
<h3>Updated Modules and Pragmata</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> IO::Compress has been upgraded from version 2.069 to 2.074. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Archive::Tar has been upgraded from version 2.04 to 2.24. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> arybase has been upgraded from version 0.11 to 0.12. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> attributes has been upgraded from version 0.27 to 0.29. </p>
<p> The deprecation message for the <code>&quot;:unique&quot;</code> and <code>&quot;:locked&quot;</code> attributes now mention that they will disappear in Perl 5.28. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> B has been upgraded from version 1.62 to 1.68. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> B::Concise has been upgraded from version 0.996 to 0.999. </p>
<p> Its output is now more descriptive for <code>&quot;op_private&quot;</code> flags. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> B::Debug has been upgraded from version 1.23 to 1.24. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> B::Deparse has been upgraded from version 1.37 to 1.40. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> B::Xref has been upgraded from version 1.05 to 1.06. </p>
<p> It now uses 3-arg <code>&quot;open()&quot;</code> instead of 2-arg <code>&quot;open()&quot;</code>. [perl #130122] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=130122">https://rt.perl.org/Public/Bug/Display.html?id=130122</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> base has been upgraded from version 2.23 to 2.25. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> bignum has been upgraded from version 0.42 to 0.47. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Carp has been upgraded from version 1.40 to 1.42. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> charnames has been upgraded from version 1.43 to 1.44. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Compress::Raw::Bzip2 has been upgraded from version 2.069 to 2.074. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Compress::Raw::Zlib has been upgraded from version 2.069 to 2.074. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Config::Perl::V has been upgraded from version 0.25 to 0.28. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">CPAN</font> has been upgraded from version 2.11 to 2.18. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> CPAN::Meta has been upgraded from version 2.150005 to 2.150010. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Data::Dumper has been upgraded from version 2.160 to 2.167. </p>
<p> The <font SIZE="-1">XS</font> implementation now supports Deparse. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> DB_File has been upgraded from version 1.835 to 1.840. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Devel::Peek has been upgraded from version 1.23 to 1.26. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Devel::PPPort has been upgraded from version 3.32 to 3.35. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Devel::SelfStubber has been upgraded from version 1.05 to 1.06. </p>
<p> It now uses 3-arg <code>&quot;open()&quot;</code> instead of 2-arg <code>&quot;open()&quot;</code>. [perl #130122] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=130122">https://rt.perl.org/Public/Bug/Display.html?id=130122</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> diagnostics has been upgraded from version 1.34 to 1.36. </p>
<p> It now uses 3-arg <code>&quot;open()&quot;</code> instead of 2-arg <code>&quot;open()&quot;</code>. [perl #130122] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=130122">https://rt.perl.org/Public/Bug/Display.html?id=130122</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Digest has been upgraded from version 1.17 to 1.17_01. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Digest::MD5 has been upgraded from version 2.54 to 2.55. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Digest::SHA has been upgraded from version 5.95 to 5.96. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> DynaLoader has been upgraded from version 1.38 to 1.42. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Encode has been upgraded from version 2.80 to 2.88. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> encoding has been upgraded from version 2.17 to 2.19. </p>
<p> This module&#8217;s default mode is no longer supported. It now dies when imported, unless the <code>&quot;Filter&quot;</code> option is being used. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> encoding::warnings has been upgraded from version 0.12 to 0.13. </p>
<p> This module is no longer supported. It emits a warning to that effect and then does nothing. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Errno has been upgraded from version 1.25 to 1.28. </p>
<p> It now documents that using <code>&quot;%!&quot;</code> automatically loads Errno for you. </p>
<p> It now uses 3-arg <code>&quot;open()&quot;</code> instead of 2-arg <code>&quot;open()&quot;</code>. [perl #130122] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=130122">https://rt.perl.org/Public/Bug/Display.html?id=130122</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::Embed has been upgraded from version 1.33 to 1.34. </p>
<p> It now uses 3-arg <code>&quot;open()&quot;</code> instead of 2-arg <code>&quot;open()&quot;</code>. [perl #130122] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=130122">https://rt.perl.org/Public/Bug/Display.html?id=130122</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::MakeMaker has been upgraded from version 7.10_01 to 7.24. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::Miniperl has been upgraded from version 1.05 to 1.06. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::ParseXS has been upgraded from version 3.31 to 3.34. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::Typemaps has been upgraded from version 3.31 to 3.34. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> feature has been upgraded from version 1.42 to 1.47. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Copy has been upgraded from version 2.31 to 2.32. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Fetch has been upgraded from version 0.48 to 0.52. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Glob has been upgraded from version 1.26 to 1.28. </p>
<p> It now Issues a deprecation message for <code>&quot;File::Glob::glob()&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Spec has been upgraded from version 3.63 to 3.67. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> FileHandle has been upgraded from version 2.02 to 2.03. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Filter::Simple has been upgraded from version 0.92 to 0.93. </p>
<p> It no longer treats <code>&quot;no MyFilter&quot;</code> immediately following <code>&quot;use MyFilter&quot;</code> as end-of-file. [perl #107726] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=107726">https://rt.perl.org/Public/Bug/Display.html?id=107726</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Getopt::Long has been upgraded from version 2.48 to 2.49. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Getopt::Std has been upgraded from version 1.11 to 1.12. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Hash::Util has been upgraded from version 0.19 to 0.22. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> HTTP::Tiny has been upgraded from version 0.056 to 0.070. </p>
<p> Internal 599-series errors now include the redirect history. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> I18N::LangTags has been upgraded from version 0.40 to 0.42. </p>
<p> It now uses 3-arg <code>&quot;open()&quot;</code> instead of 2-arg <code>&quot;open()&quot;</code>. [perl #130122] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=130122">https://rt.perl.org/Public/Bug/Display.html?id=130122</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">IO</font> has been upgraded from version 1.36 to 1.38. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> IO::Socket::IP has been upgraded from version 0.37 to 0.38. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> IPC::Cmd has been upgraded from version 0.92 to 0.96. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> IPC::SysV has been upgraded from version 2.06_01 to 2.07. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">JSON::PP</font> has been upgraded from version 2.27300 to 2.27400_02. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> lib has been upgraded from version 0.63 to 0.64. </p>
<p> It now uses 3-arg <code>&quot;open()&quot;</code> instead of 2-arg <code>&quot;open()&quot;</code>. [perl #130122] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=130122">https://rt.perl.org/Public/Bug/Display.html?id=130122</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> List::Util has been upgraded from version 1.42_02 to 1.46_02. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Locale::Codes has been upgraded from version 3.37 to 3.42. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Locale::Maketext has been upgraded from version 1.26 to 1.28. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Locale::Maketext::Simple has been upgraded from version 0.21 to 0.21_01. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Math::BigInt has been upgraded from version 1.999715 to 1.999806. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Math::BigInt::FastCalc has been upgraded from version 0.40 to 0.5005. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Math::BigRat has been upgraded from version 0.260802 to 0.2611. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Math::Complex has been upgraded from version 1.59 to 1.5901. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Memoize has been upgraded from version 1.03 to 1.03_01. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Module::CoreList has been upgraded from version 5.20170420 to 5.20170530. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Module::Load::Conditional has been upgraded from version 0.64 to 0.68. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Module::Metadata has been upgraded from version 1.000031 to 1.000033. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> mro has been upgraded from version 1.18 to 1.20. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Net::Ping has been upgraded from version 2.43 to 2.55. </p>
<p> IPv6 addresses and <code>&quot;AF_INET6&quot;</code> sockets are now supported, along with several other enhancements. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">NEXT</font> has been upgraded from version 0.65 to 0.67. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Opcode has been upgraded from version 1.34 to 1.39. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> open has been upgraded from version 1.10 to 1.11. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> OS2::Process has been upgraded from version 1.11 to 1.12. </p>
<p> It now uses 3-arg <code>&quot;open()&quot;</code> instead of 2-arg <code>&quot;open()&quot;</code>. [perl #130122] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=130122">https://rt.perl.org/Public/Bug/Display.html?id=130122</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> overload has been upgraded from version 1.26 to 1.28. </p>
<p> Its compilation speed has been improved slightly. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> parent has been upgraded from version 0.234 to 0.236. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perl5db.pl has been upgraded from version 1.50 to 1.51. </p>
<p> It now ignores <i>/dev/tty</i> on non-Unix systems. [perl #113960] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=113960">https://rt.perl.org/Public/Bug/Display.html?id=113960</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl::OSType has been upgraded from version 1.009 to 1.010. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> perlfaq has been upgraded from version 5.021010 to 5.021011. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> PerlIO has been upgraded from version 1.09 to 1.10. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> PerlIO::encoding has been upgraded from version 0.24 to 0.25. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> PerlIO::scalar has been upgraded from version 0.24 to 0.26. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pod::Checker has been upgraded from version 1.60 to 1.73. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pod::Functions has been upgraded from version 1.10 to 1.11. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pod::Html has been upgraded from version 1.22 to 1.2202. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pod::Perldoc has been upgraded from version 3.25_02 to 3.28. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pod::Simple has been upgraded from version 3.32 to 3.35. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pod::Usage has been upgraded from version 1.68 to 1.69. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">POSIX</font> has been upgraded from version 1.65 to 1.76. </p>
<p> This remedies several defects in making its symbols exportable. [perl #127821] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=127821">https://rt.perl.org/Public/Bug/Display.html?id=127821</a>&gt; </p>
<p> The <code>&quot;POSIX::tmpnam()&quot;</code> interface has been removed, see ``<code>POSIX::tmpnam()</code> has been removed&#8217;&#8216;. </p>
<p> The following deprecated functions have been removed: </p>
<pre><code>    POSIX::isalnum
    POSIX::isalpha
    POSIX::iscntrl
    POSIX::isdigit
    POSIX::isgraph
    POSIX::islower
    POSIX::isprint
    POSIX::ispunct
    POSIX::isspace
    POSIX::isupper
    POSIX::isxdigit
    POSIX::tolower
    POSIX::toupper
</code></pre>
<p> Trying to import <font SIZE="-1">POSIX</font> subs that have no real implementations (like <code>&quot;POSIX::atend()&quot;</code>) now fails at import time, instead of waiting until runtime. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> re has been upgraded from version 0.32 to 0.34 </p>
<p> This adds support for the new <code>&quot;/xx&quot;</code> regular expression pattern modifier, and a change to the <code>&quot;use re &#8216;strict&#8217;&quot;</code> experimental feature. When <code>&quot;re &#8216;strict&#8217;&quot;</code> is enabled, a warning now will be generated for all unescaped uses of the two characters <code>&quot;}&quot;</code> and <code>&quot;]&quot;</code> in regular expression patterns (outside bracketed character classes) that are taken literally. This brings them more in line with the <code>&quot;)&quot;</code> character which is always a metacharacter unless escaped. Being a metacharacter only sometimes, depending on an action at a distance, can lead to silently having the pattern mean something quite different than was intended, which the <code>&quot;re &#8216;strict&#8217;&quot;</code> mode is intended to minimize. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Safe has been upgraded from version 2.39 to 2.40. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Scalar::Util has been upgraded from version 1.42_02 to 1.46_02. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Storable has been upgraded from version 2.56 to 2.62. </p>
<p> Fixes [perl #130098] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=130098">https://rt.perl.org/Public/Bug/Display.html?id=130098</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Symbol has been upgraded from version 1.07 to 1.08. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Sys::Syslog has been upgraded from version 0.33 to 0.35. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Term::ANSIColor has been upgraded from version 4.04 to 4.06. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Term::ReadLine has been upgraded from version 1.15 to 1.16. </p>
<p> It now uses 3-arg <code>&quot;open()&quot;</code> instead of 2-arg <code>&quot;open()&quot;</code>. [perl #130122] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=130122">https://rt.perl.org/Public/Bug/Display.html?id=130122</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Test has been upgraded from version 1.28 to 1.30. </p>
<p> It now uses 3-arg <code>&quot;open()&quot;</code> instead of 2-arg <code>&quot;open()&quot;</code>. [perl #130122] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=130122">https://rt.perl.org/Public/Bug/Display.html?id=130122</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Test::Harness has been upgraded from version 3.36 to 3.38. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Test::Simple has been upgraded from version 1.001014 to 1.302073. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Thread::Queue has been upgraded from version 3.09 to 3.12. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Thread::Semaphore has been upgraded from 2.12 to 2.13. </p>
<p> Added the <code>&quot;down_timed&quot;</code> method. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> threads has been upgraded from version 2.07 to 2.15. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> threads::shared has been upgraded from version 1.51 to 1.56. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Tie::Hash::NamedCapture has been upgraded from version 0.09 to 0.10. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Time::HiRes has been upgraded from version 1.9733 to 1.9741. </p>
<p> It now builds on systems with C<font SIZE="-2">++</font>11 compilers (such as G++ 6 and Clang++ 3.9). </p>
<p> Now uses <code>&quot;clockid_t&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Time::Local has been upgraded from version 1.2300 to 1.25. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unicode::Collate has been upgraded from version 1.14 to 1.19. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unicode::UCD has been upgraded from version 0.64 to 0.68. </p>
<p> It now uses 3-arg <code>&quot;open()&quot;</code> instead of 2-arg <code>&quot;open()&quot;</code>. [perl #130122] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=130122">https://rt.perl.org/Public/Bug/Display.html?id=130122</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> version has been upgraded from version 0.9916 to 0.9917. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> VMS::DCLsym has been upgraded from version 1.06 to 1.08. </p>
<p> It now uses 3-arg <code>&quot;open()&quot;</code> instead of 2-arg <code>&quot;open()&quot;</code>. [perl #130122] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=130122">https://rt.perl.org/Public/Bug/Display.html?id=130122</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> warnings has been upgraded from version 1.36 to 1.37. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> XS::Typemap has been upgraded from version 0.14 to 0.15. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> XSLoader has been upgraded from version 0.21 to 0.27. </p>
<p> Fixed a security hole in which binary files could be loaded from a path outside of <code>@INC</code>. </p>
<p> It now uses 3-arg <code>&quot;open()&quot;</code> instead of 2-arg <code>&quot;open()&quot;</code>. [perl #130122] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=130122">https://rt.perl.org/Public/Bug/Display.html?id=130122</a>&gt; </p>
 </dd></dl>
<h2>Documentation</h2>
<h3>New Documentation</h3>
<p> <i>perldeprecation</i> </p>
<p> This file documents all upcoming deprecations, and some of the deprecations which already have been removed. The purpose of this documentation is two-fold: document what will disappear, and by which version, and serve as a guide for people dealing with code which has features that no longer work after an upgrade of their perl.  </p>
<h3>Changes to Existing Documentation</h3>
<p> We have attempted to update the documentation to reflect the changes listed in this document. If you find any we have missed, send email to perlbug [at] perl.org &lt;mailto:perlbug [at] perl.org&gt;. </p>
<p> Additionally, all references to Usenet have been removed, and the following selected changes have been made: </p>
<p> <i>perlfunc</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Removed obsolete text about <code>&quot;defined()&quot;</code> on aggregates that should have been deleted earlier, when the feature was removed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Corrected documentation of <code>&quot;eval()&quot;</code>, and <code>&quot;evalbytes()&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Clarified documentation of <code>&quot;seek()&quot;</code>, <code>&quot;tell()&quot;</code> and <code>&quot;sysseek()&quot;</code> emphasizing that positions are in bytes and not characters. [perl #128607] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128607">https://rt.perl.org/Public/Bug/Display.html?id=128607</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Clarified documentation of <code>&quot;sort()&quot;</code> concerning the variables <code>$a</code> and <code>$b</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In <code>&quot;split()&quot;</code> noted that certain pattern modifiers are legal, and added a caution about its use in Perls before v5.11. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Removed obsolete documentation of <code>&quot;study()&quot;</code>, noting that it is now a no-op. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Noted that <code>&quot;vec()&quot;</code> doesn&#8217;t work well when the string contains characters whose code points are above 255. </p>
 </dd></dl>
<p> <i>perlguts</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Added advice on formatted printing of operands of <code>&quot;Size_t&quot;</code> and <code>&quot;SSize_t&quot;</code> </p>
 </dd></dl>
<p> <i>perlhack</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Clarify what editor tab stop rules to use, and note that we are migrating away from using tabs, replacing them with sequences of <font SIZE="-1">SPACE</font> characters. </p>
 </dd></dl>
<p> <i>perlhacktips</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Give another reason to use <code>&quot;cBOOL&quot;</code> to cast an expression to boolean. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Note that the macros <code>&quot;TRUE&quot;</code> and <code>&quot;FALSE&quot;</code> are available to express boolean values. </p>
 </dd></dl>
<p> <i>perlinterp</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> perlinterp has been expanded to give a more detailed example of how to hunt around in the parser for how a given operator is handled. </p>
 </dd></dl>
<p> <i>perllocale</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Some locales aren&#8217;t compatible with Perl. Note that these can cause core dumps. </p>
 </dd></dl>
<p> <i>perlmod</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Various clarifications have been added. </p>
 </dd></dl>
<p> <i>perlmodlib</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Updated the site mirror list. </p>
 </dd></dl>
<p> <i>perlobj</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Added a section on calling methods using their fully qualified names. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Do not discourage manual <code>@ISA</code>. </p>
 </dd></dl>
<p> <i>perlootut</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Mention <code>&quot;Moo&quot;</code> more. </p>
 </dd></dl>
<p> <i>perlop</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Note that white space must be used for quoting operators if the delimiter is a word character (<i>i.e.</i>, matches <code>&quot;\w&quot;</code>). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Clarify that in regular expression patterns delimited by single quotes, no variable interpolation is done. </p>
 </dd></dl>
<p> <i>perlre</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The first part was extensively rewritten to incorporate various basic points, that in earlier versions were mentioned in sort of an appendix on Version 8 regular expressions. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Note that it is common to have the <code>&quot;/x&quot;</code> modifier and forget that this means that <code>&quot;#&quot;</code> has to be escaped. </p>
 </dd></dl>
<p> <i>perlretut</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Add introductory material. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Note that a metacharacter occurring in a context where it can&#8217;t mean that, silently loses its meta-ness and matches literally. <code>&quot;use re &#8216;strict&#8217;&quot;</code> can catch some of these. </p>
 </dd></dl>
<p> <i>perlunicode</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Corrected the text about Unicode <font SIZE="-1">BYTE ORDER MARK</font> handling. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Updated the text to correspond with changes in Unicode UTS#18, concerning regular expressions, and Perl compatibility with what it says. </p>
 </dd></dl>
<p> <i>perlvar</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Document <code>@ISA</code>. It was documented in other places, but not in perlvar. </p>
 </dd></dl>
<h2>Diagnostics</h2>
<h3>New Diagnostics</h3>
<p> <i>New Errors</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> A signature parameter must start with <code>&#8216;$&#8216;</code>, <code>&#8216;@&#8216;</code> or <code>&#8216;%&#8216;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Bareword in require contains ``%s&#8217;&#8216; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Bareword in require maps to empty filename </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Bareword in require maps to disallowed filename ``%s&#8217;&#8216; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Bareword in require must not start with a double-colon: ``%s&#8217;&#8216; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>%s:</code> command not found </p>
<p> (A) You&#8217;ve accidentally run your script through <code>bash</code> or another shell instead of Perl. Check the <code>&quot;#!&quot;</code> line, or manually feed your script into Perl yourself. The <code>&quot;#!&quot;</code> line at the top of your file could look like: </p>
<pre><code>  #!/usr/bin/perl
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>%s:</code> command not found: <code>%s</code> </p>
<p> (A) You&#8217;ve accidentally run your script through <code>zsh</code> or another shell instead of Perl. Check the <code>&quot;#!&quot;</code> line, or manually feed your script into Perl yourself. The <code>&quot;#!&quot;</code> line at the top of your file could look like: </p>
<pre><code>  #!/usr/bin/perl
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> The experimental declared_refs feature is not enabled </p>
<p> (F) To declare references to variables, as in <code>&quot;my \%x&quot;</code>, you must first enable the feature: </p>
<pre><code>    no warnings &quot;experimental::declared_refs&quot;;
    use feature &quot;declared_refs&quot;;
</code></pre>
<p> See ``Declaring a reference to a variable&#8217;&#8216;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Illegal character following sigil in a subroutine signature </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Indentation on line <code>%d</code> of here-doc doesn&#8217;t match delimiter </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Infinite recursion via empty pattern. </p>
<p> Using the empty pattern (which re-executes the last successfully-matched pattern) inside a code block in another regex, as in <code>&quot;/(?{ s!!new! })/&quot;</code>, has always previously yielded a segfault. It now produces this error. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Malformed <font SIZE="-1">UTF-8</font> string in ``%s&#8217;&#8216; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Multiple slurpy parameters not allowed </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&#8216;#&#8216;</code> not allowed immediately following a sigil in a subroutine signature </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> panic: unknown OA_*: <code>%x</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unescaped left brace in regex is illegal here </p>
<p> Unescaped left braces are now illegal in some contexts in regular expression patterns. In other contexts, they are still just deprecated; they will be illegal in Perl 5.30. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Version control conflict marker </p>
<p> (F) The parser found a line starting with <code>&quot;&lt;&lt;&lt;&lt;&lt;&lt;&lt;&quot;</code>, <code>&quot;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&quot;</code>, or <code>&quot;=======&quot;</code>. These may be left by a version control system to mark conflicts after a failed merge operation. </p>
 </dd></dl>
<p> <i>New Warnings</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Can&#8217;t determine class of operator <code>%s</code>, assuming <code>&quot;BASEOP&quot;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Declaring references is experimental </p>
<p> (S experimental::declared_refs) This warning is emitted if you use a reference constructor on the right-hand side of <code>&quot;my()&quot;</code>, <code>&quot;state()&quot;</code>, <code>&quot;our()&quot;</code>, or <code>&quot;local()&quot;</code>. Simply suppress the warning if you want to use the feature, but know that in doing so you are taking the risk of using an experimental feature which may change or be removed in a future Perl version: </p>
<pre><code>    no warnings &quot;experimental::declared_refs&quot;;
    use feature &quot;declared_refs&quot;;
    $fooref = my \$foo;
</code></pre>
<p> See ``Declaring a reference to a variable&#8217;&#8216;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> do ``%s&#8217;&#8216; failed, &#8216;.&#8216; is no longer in <code>@INC</code> </p>
<p> Since <code>&quot;.&quot;</code> is now removed from <code>@INC</code> by default, <code>&quot;do&quot;</code> will now trigger a warning recommending to fix the <code>&quot;do&quot;</code> statement. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;File::Glob::glob()&quot;</code> will disappear in perl 5.30. Use <code>&quot;File::Glob::bsd_glob()&quot;</code> instead. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unescaped literal &#8216;%c&#8217; in regex; marked by &lt;-- <font SIZE="-1">HERE</font> in m/%s/ </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Use of unassigned code point or non-standalone grapheme for a delimiter will be a fatal error starting in Perl 5.30 </p>
<p> See ``Deprecations&#8217;&#8216; </p>
 </dd></dl>
<h3>Changes to Existing Diagnostics</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> When a <code>&quot;require&quot;</code> fails, we now do not provide <code>@INC</code> when the <code>&quot;require&quot;</code> is for a file instead of a module. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> When <code>@INC</code> is not scanned for a <code>&quot;require&quot;</code> call, we no longer display <code>@INC</code> to avoid confusion. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Attribute ``locked&#8217;&#8216; is deprecated, and will disappear in Perl 5.28 </p>
<p> This existing warning has had the <i>and will disappear</i> text added in this release. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Attribute ``unique&#8217;&#8216; is deprecated, and will disappear in Perl 5.28 </p>
<p> This existing warning has had the <i>and will disappear</i> text added in this release. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Calling POSIX::%s() is deprecated </p>
<p> This warning has been removed, as the deprecated functions have been removed from <font SIZE="-1">POSIX.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Constants from lexical variables potentially modified elsewhere are deprecated. This will not be allowed in Perl 5.32 </p>
<p> This existing warning has had the <i>this will not be allowed</i> text added in this release. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Deprecated use of <code>&quot;my()&quot;</code> in false conditional. This will be a fatal error in Perl 5.30 </p>
<p> This existing warning has had the <i>this will be a fatal error</i> text added in this release. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;dump()&quot;</code> better written as <code>&quot;CORE::dump()&quot;</code>. <code>&quot;dump()&quot;</code> will no longer be available in Perl 5.30 </p>
<p> This existing warning has had the <i>no longer be available</i> text added in this release. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Experimental <code>%s</code> on scalar is now forbidden </p>
<p> This message is now followed by more helpful text. [perl #127976] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=127976">https://rt.perl.org/Public/Bug/Display.html?id=127976</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Experimental ``%s&#8217;&#8216; subs not enabled </p>
<p> This warning was been removed, as lexical subs are no longer experimental. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Having more than one /%c regexp modifier is deprecated </p>
<p> This deprecation warning has been removed, since <code>&quot;/xx&quot;</code> now has a new meaning. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> %s() is deprecated on <code>&quot;:utf8&quot;</code> handles. This will be a fatal error in Perl 5.30 . </p>
<p> where ``%s&#8217;&#8216; is one of <code>&quot;sysread&quot;</code>, <code>&quot;recv&quot;</code>, <code>&quot;syswrite&quot;</code>, or <code>&quot;send&quot;</code>. </p>
<p> This existing warning has had the <i>this will be a fatal error</i> text added in this release. </p>
<p> This warning is now enabled by default, as all <code>&quot;deprecated&quot;</code> category warnings should be. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>$*</code> is no longer supported. Its use will be fatal in Perl 5.30 </p>
<p> This existing warning has had the <i>its use will be fatal</i> text added in this release. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>$#</code> is no longer supported. Its use will be fatal in Perl 5.30 </p>
<p> This existing warning has had the <i>its use will be fatal</i> text added in this release. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Malformed <font SIZE="-1">UTF-8</font> character%s </p>
<p> Details as to the exact problem have been added at the end of this message </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Missing or undefined argument to <code>%s</code> </p>
<p> This warning used to warn about <code>&quot;require&quot;</code>, even if it was actually <code>&quot;do&quot;</code> which being executed. It now gets the operation name right. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> NO-BREAK <font SIZE="-1">SPACE</font> in a charnames alias definition is deprecated </p>
<p> This warning has been removed as the behavior is now an error. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Odd name/value argument for subroutine &#8216;%s&#8217; </p>
<p> This warning now includes the name of the offending subroutine. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Opening dirhandle <code>%s</code> also as a file. This will be a fatal error in Perl 5.28 </p>
<p> This existing warning has had the <i>this will be a fatal error</i> text added in this release. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Opening filehandle <code>%s</code> also as a directory. This will be a fatal error in Perl 5.28 </p>
<p> This existing warning has had the <i>this will be a fatal error</i> text added in this release. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> panic: ck_split, type=%u </p>
<p> panic: pp_split, pm=%p, s=%p </p>
<p> These panic errors have been removed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Passing malformed <font SIZE="-1">UTF-8</font> to ``%s&#8217;&#8216; is deprecated </p>
<p> This warning has been changed to the fatal Malformed <font SIZE="-1">UTF-8</font> string in ``%s&#8217;&#8216; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Setting <code>$/</code> to a reference to <code>%s</code> as a form of slurp is deprecated, treating as undef. This will be fatal in Perl 5.28 </p>
<p> This existing warning has had the <i>this will be fatal</i> text added in this release. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;${^ENCODING}&quot;</code> is no longer supported. Its use will be fatal in Perl 5.28 </p>
<p> This warning used to be: &quot;Setting <code>&quot;${^ENCODING}&quot;</code> is deprecated&quot;. </p>
<p> The special action of the variable <code>&quot;${^ENCODING}&quot;</code> was formerly used to implement the <code>&quot;encoding&quot;</code> pragma. As of Perl 5.26, rather than being deprecated, assigning to this variable now has no effect except to issue the warning. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Too few arguments for subroutine &#8216;%s&#8217; </p>
<p> This warning now includes the name of the offending subroutine. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Too many arguments for subroutine &#8216;%s&#8217; </p>
<p> This warning now includes the name of the offending subroutine. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unescaped left brace in regex is deprecated here (and will be fatal in Perl 5.30), passed through in regex; marked by &lt;-- <font SIZE="-1">HERE</font> in m/%s/ </p>
<p> This existing warning has had the <i>here (and will be fatal...)</i> text added in this release. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unknown charname &#8216;&#8216; is deprecated. Its use will be fatal in Perl 5.28 </p>
<p> This existing warning has had the <i>its use will be fatal</i> text added in this release. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Use of bare &lt;&lt; to mean &lt;&lt;&quot;&quot; is deprecated. Its use will be fatal in Perl 5.28 </p>
<p> This existing warning has had the <i>its use will be fatal</i> text added in this release. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Use of code point 0x%s is deprecated; the permissible max is 0x%s. This will be fatal in Perl 5.28 </p>
<p> This existing warning has had the <i>this will be fatal</i> text added in this release. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Use of comma-less variable list is deprecated. Its use will be fatal in Perl 5.28 </p>
<p> This existing warning has had the <i>its use will be fatal</i> text added in this release. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Use of inherited <code>&quot;AUTOLOAD&quot;</code> for non-method %s() is deprecated. This will be fatal in Perl 5.28 </p>
<p> This existing warning has had the <i>this will be fatal</i> text added in this release. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Use of strings with code points over 0xFF as arguments to <code>%s</code> operator is deprecated. This will be a fatal error in Perl 5.28 </p>
<p> This existing warning has had the <i>this will be a fatal error</i> text added in this release. </p>
 </dd></dl>
<h2>Utility Changes</h2>
<i></i><i></i><h3>c2ph and pstruct</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> These old utilities have long since superceded by h2xs, and are now gone from the distribution. </p>
 </dd></dl>
<i></i><h3>Porting/pod_lib.pl</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Removed spurious executable bit. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Account for the possibility of <font SIZE="-1">DOS</font> file endings. </p>
 </dd></dl>
<i></i><h3>Porting/sync-with-cpan</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Many improvements. </p>
 </dd></dl>
<i></i><h3>perf/benchmarks</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Tidy file, rename some symbols. </p>
 </dd></dl>
<i></i><h3>Porting/checkAUTHORS.pl</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Replace obscure character range with <code>&quot;\w&quot;</code>. </p>
 </dd></dl>
<i></i><h3>t/porting/regen.t</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Try to be more helpful when tests fail. </p>
 </dd></dl>
<i></i><h3>utils/h2xs.PL</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Avoid infinite loop for enums. </p>
 </dd></dl>
<h3>perlbug</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Long lines in the message body are now wrapped at 900 characters, to stay well within the 1000-character limit imposed by <font SIZE="-1">SMTP</font> mail transfer agents. This is particularly likely to be important for the list of arguments to <i>Configure</i>, which can readily exceed the limit if, for example, it names several non-default installation paths. This change also adds the first unit tests for perlbug. [perl #128020] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128020">https://rt.perl.org/Public/Bug/Display.html?id=128020</a>&gt; </p>
 </dd></dl>
<h2>Configuration and Compilation</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> <code>&quot;-Ddefault_inc_excludes_dot&quot;</code> has added, and enabled by default. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;dtrace&quot;</code> build process has further changes [perl #130108] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=130108">https://rt.perl.org/Public/Bug/Display.html?id=130108</a>&gt;: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> If the <code>&quot;-xnolibs&quot;</code> is available, use that so a <i>dtrace</i> perl can be built within a FreeBSD jail. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On systems that build a <i>dtrace</i> object file (FreeBSD, Solaris, and SystemTap&#8217;s dtrace emulation), copy the input objects to a separate directory and process them there, and use those objects in the link, since <code>&quot;dtrace -G&quot;</code> also modifies these objects. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Add <i>libelf</i> to the build on FreeBSD 10.x, since <i>dtrace</i> adds references to <i>libelf</i> symbols. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Generate a dummy <i>dtrace_main.o</i> if <code>&quot;dtrace -G&quot;</code> fails to build it. A default build on Solaris generates probes from the unused inline functions, while they don&#8217;t on FreeBSD, which causes <code>&quot;dtrace -G&quot;</code> to fail. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>&bull;</dt>
<dd> <p> You can now disable perl&#8217;s use of the <code>&quot;PERL_HASH_SEED&quot;</code> and <code>&quot;PERL_PERTURB_KEYS&quot;</code> environment variables by configuring perl with <code>&quot;-Accflags=NO_PERL_HASH_ENV&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> You can now disable perl&#8217;s use of the <code>&quot;PERL_HASH_SEED_DEBUG&quot;</code> environment variable by configuring perl with <code>&quot;-Accflags=-DNO_PERL_HASH_SEED_DEBUG&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>Configure</i> now zeroes out the alignment bytes when calculating the bytes for 80-bit <code>&quot;NaN&quot;</code> and <code>&quot;Inf&quot;</code> to make builds more reproducible. [perl #130133] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=130133">https://rt.perl.org/Public/Bug/Display.html?id=130133</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Since v5.18, for testing purposes we have included support for building perl with a variety of non-standard, and non-recommended hash functions. Since we do not recommend the use of these functions, we have removed them and their corresponding build options. Specifically this includes the following build options: </p>
<pre><code>    PERL_HASH_FUNC_SDBM
    PERL_HASH_FUNC_DJB2
    PERL_HASH_FUNC_SUPERFAST
    PERL_HASH_FUNC_MURMUR3
    PERL_HASH_FUNC_ONE_AT_A_TIME
    PERL_HASH_FUNC_ONE_AT_A_TIME_OLD
    PERL_HASH_FUNC_MURMUR_HASH_64A
    PERL_HASH_FUNC_MURMUR_HASH_64B
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Remove ``Warning: perl appears in your path&#8217;&#8216; </p>
<p> This install warning is more or less obsolete, since most platforms already <code>will</code> have a <i>/usr/bin/perl</i> or similar provided by the <font SIZE="-1">OS.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Reduce verbosity of <code>&quot;make install.man&quot;</code> </p>
<p> Previously, two progress messages were emitted for each manpage: one by installman itself, and one by the function in <i>install_lib.pl</i> that it calls to actually install the file. Disabling the second of those in each case saves over 750 lines of unhelpful output. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Cleanup for <code>&quot;clang -Weverything&quot;</code> support. [perl #129961] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=129961">https://rt.perl.org/Public/Bug/Display.html?id=129961</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>Configure</i>: signbit scan was assuming too much, stop assuming negative 0. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Various compiler warnings have been silenced. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Several smaller changes have been made to remove impediments to compiling under C<font SIZE="-2">++</font>11. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Builds using <code>&quot;USE_PAD_RESET&quot;</code> now work again; this configuration had bit-rotted. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A probe for <code>&quot;gai_strerror&quot;</code> was added to <i>Configure</i> that checks if the <code>&quot;gai_strerror()&quot;</code> routine is available and can be used to translate error codes returned by <code>&quot;getaddrinfo()&quot;</code> into human readable strings. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>Configure</i> now aborts if both <code>&quot;-Duselongdouble&quot;</code> and <code>&quot;-Dusequadmath&quot;</code> are requested. [perl #126203] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=126203">https://rt.perl.org/Public/Bug/Display.html?id=126203</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed a bug in which <i>Configure</i> could append <code>&quot;-quadmath&quot;</code> to the archname even if it was already present. [perl #128538] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128538">https://rt.perl.org/Public/Bug/Display.html?id=128538</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Clang builds with <code>&quot;-DPERL_GLOBAL_STRUCT&quot;</code> or <code>&quot;-DPERL_GLOBAL_STRUCT_PRIVATE&quot;</code> have been fixed (by disabling Thread Safety Analysis for these configurations). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>make_ext.pl</i> no longer updates a module&#8217;s <i>pm_to_blib</i> file when no files require updates. This could cause dependencies, <i>perlmain.c</i> in particular, to be rebuilt unnecessarily. [perl #126710] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=126710">https://rt.perl.org/Public/Bug/Display.html?id=126710</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The output of <code>&quot;perl -V&quot;</code> has been reformatted so that each configuration and compile-time option is now listed one per line, to improve readability. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>Configure</i> now builds <code>&quot;miniperl&quot;</code> and <code>&quot;generate_uudmap&quot;</code> if you invoke it with <code>&quot;-Dusecrosscompiler&quot;</code> but not <code>&quot;-Dtargethost=somehost&quot;</code>. This means you can supply your target platform <code>&quot;config.sh&quot;</code>, generate the headers and proceed to build your cross-target perl. [perl #127234] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=127234">https://rt.perl.org/Public/Bug/Display.html?id=127234</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl built with <code>&quot;-Accflags=-DPERL_TRACE_OPS&quot;</code> now only dumps the operator counts when the environment variable <code>&quot;PERL_TRACE_OPS&quot;</code> is set to a non-zero integer. This allows <code>&quot;make test&quot;</code> to pass on such a build. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> When building with <font SIZE="-1">GCC 6</font> and link-time optimization (the <code>&quot;-flto&quot;</code> option to <code>&quot;gcc&quot;</code>), <i>Configure</i> was treating all probed symbols as present on the system, regardless of whether they actually exist. This has been fixed. [perl #128131] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128131">https://rt.perl.org/Public/Bug/Display.html?id=128131</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <i>t/test.pl</i> library is used for internal testing of Perl itself, and also copied by several <font SIZE="-1">CPAN</font> modules. Some of those modules must work on older versions of Perl, so <i>t/test.pl</i> must in turn avoid newer Perl features. Compatibility with Perl 5.8 was inadvertently removed some time ago; it has now been restored. [perl #128052] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128052">https://rt.perl.org/Public/Bug/Display.html?id=128052</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The build process no longer emits an extra blank line before building each ``simple&#8217;&#8216; extension (those with only <i>*.pm</i> and <i>*.pod</i> files). </p>
 </dd></dl>
<h2>Testing</h2>
<p> Tests were added and changed to reflect the other additions and changes in this release. Furthermore, these substantive changes were made: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> A new test script, <i>comp/parser_run.t</i>, has been added that is like <i>comp/parser.t</i> but with <i>test.pl</i> included so that <code>&quot;runperl()&quot;</code> and the like are available for use. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Tests for locales were erroneously using locales incompatible with Perl. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Some parts of the test suite that try to exhaustively test edge cases in the regex implementation have been restricted to running for a maximum of five minutes. On slow systems they could otherwise take several hours, without significantly improving our understanding of the correctness of the code under test. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new internal facility allows analysing the time taken by the individual tests in Perl&#8217;s own test suite; see <i>Porting/harness-timer-report.pl</i>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/re/regexp_nonull.t</i> has been added to test that the regular expression engine can handle scalars that do not have a null byte just past the end of the string. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new test script, <i>t/op/decl-refs.t</i>, has been added to test the new feature ``Declaring a reference to a variable&#8217;&#8216;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new test script, <i>t/re/keep_tabs.t</i> has been added to contain tests where <code>&quot;\t&quot;</code> characters should not be expanded into spaces. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new test script, <i>t/re/anyof.t</i>, has been added to test that the <font SIZE="-1">ANYOF</font> nodes generated by bracketed character classes are as expected. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> There is now more extensive testing of the Unicode-related <font SIZE="-1">API</font> macros and functions. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Several of the longer running <font SIZE="-1">API</font> test files have been split into multiple test files so that they can be run in parallel. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>t/harness</i> now tries really hard not to run tests which are located outside of the Perl source tree. [perl #124050] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=124050">https://rt.perl.org/Public/Bug/Display.html?id=124050</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Prevent debugger tests (<i>lib/perl5db.t</i>) from failing due to the contents of <code>$ENV{PERLDB_OPTS}</code>. [perl #130445] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=130445">https://rt.perl.org/Public/Bug/Display.html?id=130445</a>&gt; </p>
 </dd></dl>
<h2>Platform Support</h2>
<h3>New Platforms</h3>
<dl>
<dt>NetBSD/VAX</dt>
<dd> <p> Perl now compiles under NetBSD on <font SIZE="-1">VAX</font> machines. However, it&#8217;s not possible for that platform to implement floating-point infinities and NaNs compatible with most modern systems, which implement the <font SIZE="-1">IEEE-754</font> floating point standard. The hexadecimal floating point (<code>&quot;0x...p[+-]n&quot;</code> literals, <code>&quot;printf %a&quot;</code>) is not implemented, either. The <code>&quot;make test&quot;</code> passes 98% of tests. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Test fixes and minor updates. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Account for lack of <code>&quot;inf&quot;</code>, <code>&quot;nan&quot;</code>, and <code>&quot;-0.0&quot;</code> support. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
</dl>
<h3>Platform-Specific Notes</h3>
<dl>
<dt>Darwin</dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Don&#8217;t treat <code>&quot;-Dprefix=/usr&quot;</code> as special: instead require an extra option <code>&quot;-Ddarwin_distribution&quot;</code> to produce the same results. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">OS X</font> El Capitan doesn&#8217;t implement the <code>&quot;clock_gettime()&quot;</code> or <code>&quot;clock_getres()&quot;</code> APIs; emulate them as necessary. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Deprecated <code><a href="/docs/linux/man/2-syscall/">syscall</a>(2)</code> on macOS 10.12. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt><font SIZE="-1">EBCDIC</font></dt>
<dd> <p> Several tests have been updated to work (or be skipped) on <font SIZE="-1">EBCDIC</font> platforms. </p>
 </dd>
<dt>HP-UX</dt>
<dd> <p> The Net::Ping <font SIZE="-1">UDP</font> test is now skipped on HP-UX. </p>
 </dd>
<dt>Hurd</dt>
<dd> <p> The hints for Hurd have been improved, enabling malloc wrap and reporting the <font SIZE="-1">GNU</font> libc used (previously it was an empty string when reported). </p>
 </dd>
<dt><font SIZE="-1">VAX</font></dt>
<dd> <p> <font SIZE="-1">VAX</font> floating point formats are now supported on NetBSD. </p>
 </dd>
<dt><font SIZE="-1">VMS</font></dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> The path separator for the <code>&quot;PERL5LIB&quot;</code> and <code>&quot;PERLLIB&quot;</code> environment entries is now a colon (<code>&quot;:&quot;</code>) when running under a Unix shell. There is no change when running under <font SIZE="-1">DCL</font> (it&#8217;s still <code>&quot;|&quot;</code>). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>configure.com</i> now recognizes the VSI-branded C compiler and no longer recognizes the ``<font SIZE="-1">DEC</font>&#8216;&#8216;-branded C compiler (as there hasn&#8217;t been such a thing for 15 or more years). </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>Windows</dt>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Support for compiling perl on Windows using Microsoft Visual Studio 2015 (containing Visual C<font SIZE="-2">++</font> 14.0) has been added. </p>
<p> This version of <font SIZE="-1">VC++</font> includes a completely rewritten C run-time library, some of the changes in which mean that work done to resolve a socket <code>&quot;close()&quot;</code> bug in perl #120091 and perl #118059 is not workable in its current state with this version of <font SIZE="-1">VC++.</font> Therefore, we have effectively reverted that bug fix for <font SIZE="-1">VS2015</font> onwards on the basis that being able to build with <font SIZE="-1">VS2015</font> onwards is more important than keeping the bug fix. We may revisit this in the future to attempt to fix the bug again in a way that is compatible with <font SIZE="-1">VS2015.</font> </p>
<p> These changes do not affect compilation with <font SIZE="-1">GCC</font> or with Visual Studio versions up to and including <font SIZE="-1">VS2013,</font> <i>i.e.</i>, the bug fix is retained (unchanged) for those compilers. </p>
<p> Note that you may experience compatibility problems if you mix a perl built with <font SIZE="-1">GCC</font> or <font SIZE="-1">VS</font> &lt;= <font SIZE="-1">VS2013</font> with <font SIZE="-1">XS</font> modules built with <font SIZE="-1">VS2015,</font> or if you mix a perl built with <font SIZE="-1">VS2015</font> with <font SIZE="-1">XS</font> modules built with <font SIZE="-1">GCC</font> or <font SIZE="-1">VS</font> &lt;= <font SIZE="-1">VS2013.</font> Some incompatibility may arise because of the bug fix that has been reverted for <font SIZE="-1">VS2015</font> builds of perl, but there may well be incompatibility anyway because of the rewritten <font SIZE="-1">CRT</font> in <font SIZE="-1">VS2015</font> (<i>e.g.</i>, see discussion at &lt;<a rel="nofollow" href="http://stackoverflow.com/questions/30412951">http://stackoverflow.com/questions/30412951</a>&gt;). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> It now automatically detects <font SIZE="-1">GCC</font> versus Visual C and sets the <font SIZE="-1">VC</font> version number on Win32. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>Linux</dt>
<dd> <p> Drop support for Linux <i>a.out</i> executable format. Linux has used <font SIZE="-1">ELF</font> for over twenty years. </p>
 </dd>
<dt>OpenBSD 6</dt>
<dd> <p> OpenBSD 6 still does not support returning <code>&quot;pid&quot;</code>, <code>&quot;gid&quot;</code>, or <code>&quot;uid&quot;</code> with <code>&quot;SA_SIGINFO&quot;</code>. Make sure to account for it. </p>
 </dd>
<dt>FreeBSD</dt>
<dd> <p> <i>t/uni/overload.t</i>: Skip hanging test on FreeBSD. </p>
 </dd>
<dt>DragonFly <font SIZE="-1">BSD</font></dt>
<dd> <p> DragonFly <font SIZE="-1">BSD</font> now has support for <code>&quot;setproctitle()&quot;</code>. [perl #130068] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=130068">https://rt.perl.org/Public/Bug/Display.html?id=130068</a>&gt;. </p>
 </dd></dl>
<h2>Internal Changes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> A new <font SIZE="-1">API</font> function <code>&quot;sv_setpv_bufsize()&quot;</code> allows simultaneously setting the length and the allocated size of the buffer in an <code>&quot;SV&quot;</code>, growing the buffer if necessary. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new <font SIZE="-1">API</font> macro <code>&quot;SvPVCLEAR()&quot;</code> sets its <code>&quot;SV&quot;</code> argument to an empty string, like Perl-space <code>&quot;$x = &#8216;&#8216;&quot;</code>, but with several optimisations. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Several new macros and functions for dealing with Unicode and UTF-8-encoded strings have been added to the <font SIZE="-1">API,</font> as well as some changes in the functionality of existing functions (see ``Unicode Support&#8217;&#8216; in perlapi for more details): </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> New versions of the <font SIZE="-1">API</font> macros like <code>&quot;isALPHA_utf8&quot;</code> and <code>&quot;toLOWER_utf8&quot;</code> have been added, each with the suffix <code>&quot;_safe&quot;</code>, like <code>&quot;isSPACE_utf8_safe&quot;</code>. These take an extra parameter, giving an upper limit of how far into the string it is safe to read. Using the old versions could cause attempts to read beyond the end of the input buffer if the <font SIZE="-1">UTF-8</font> is not well-formed, and their use now raises a deprecation warning. Details are at ``Character classification&#8217;&#8216; in perlapi. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Macros like <code>&quot;isALPHA_utf8&quot;</code> and <code>&quot;toLOWER_utf8&quot;</code> now die if they detect that their input <font SIZE="-1">UTF-8</font> is malformed. A deprecation warning had been issued since Perl 5.18. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Several new macros for analysing the validity of utf8 sequences. These are: </p>
<p> <code>&quot;UTF8_GOT_ABOVE_31_BIT&quot;</code> <code>&quot;UTF8_GOT_CONTINUATION&quot;</code> <code>&quot;UTF8_GOT_EMPTY&quot;</code> <code>&quot;UTF8_GOT_LONG&quot;</code> <code>&quot;UTF8_GOT_NONCHAR&quot;</code> <code>&quot;UTF8_GOT_NON_CONTINUATION&quot;</code> <code>&quot;UTF8_GOT_OVERFLOW&quot;</code> <code>&quot;UTF8_GOT_SHORT&quot;</code> <code>&quot;UTF8_GOT_SUPER&quot;</code> <code>&quot;UTF8_GOT_SURROGATE&quot;</code> <code>&quot;UTF8_IS_INVARIANT&quot;</code> <code>&quot;UTF8_IS_NONCHAR&quot;</code> <code>&quot;UTF8_IS_SUPER&quot;</code> <code>&quot;UTF8_IS_SURROGATE&quot;</code> <code>&quot;UVCHR_IS_INVARIANT&quot;</code> <code>&quot;isUTF8_CHAR_flags&quot;</code> <code>&quot;isSTRICT_UTF8_CHAR&quot;</code> <code>&quot;isC9_STRICT_UTF8_CHAR&quot;</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Functions that are all extensions of the <code>&quot;is_utf8_string_</code>*<code>()&quot;</code> functions, that apply various restrictions to the <font SIZE="-1">UTF-8</font> recognized as valid: </p>
<p> <code>&quot;is_strict_utf8_string&quot;</code>, <code>&quot;is_strict_utf8_string_loc&quot;</code>, <code>&quot;is_strict_utf8_string_loclen&quot;</code>, </p>
<p> <code>&quot;is_c9strict_utf8_string&quot;</code>, <code>&quot;is_c9strict_utf8_string_loc&quot;</code>, <code>&quot;is_c9strict_utf8_string_loclen&quot;</code>, </p>
<p> <code>&quot;is_utf8_string_flags&quot;</code>, <code>&quot;is_utf8_string_loc_flags&quot;</code>, <code>&quot;is_utf8_string_loclen_flags&quot;</code>, </p>
<p> <code>&quot;is_utf8_fixed_width_buf_flags&quot;</code>, <code>&quot;is_utf8_fixed_width_buf_loc_flags&quot;</code>, <code>&quot;is_utf8_fixed_width_buf_loclen_flags&quot;</code>. </p>
<p> <code>&quot;is_utf8_invariant_string&quot;</code>. <code>&quot;is_utf8_valid_partial_char&quot;</code>. <code>&quot;is_utf8_valid_partial_char_flags&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The functions <code>&quot;utf8n_to_uvchr&quot;</code> and its derivatives have had several changes of behaviour. </p>
<p> Calling them, while passing a string length of 0 is now asserted against in <font SIZE="-1">DEBUGGING</font> builds, and otherwise, returns the Unicode <font SIZE="-1">REPLACEMENT CHARACTER.</font> If you have nothing to decode, you shouldn&#8217;t call the decode function. </p>
<p> They now return the Unicode <font SIZE="-1">REPLACEMENT CHARACTER</font> if called with <font SIZE="-1">UTF-8</font> that has the overlong malformation and that malformation is allowed by the input parameters. This malformation is where the <font SIZE="-1">UTF-8</font> looks valid syntactically, but there is a shorter sequence that yields the same code point. This has been forbidden since Unicode version 3.1. </p>
<p> They now accept an input flag to allow the overflow malformation. This malformation is when the <font SIZE="-1">UTF-8</font> may be syntactically valid, but the code point it represents is not capable of being represented in the word length on the platform. What ``allowed&#8217;&#8216; means, in this case, is that the function doesn&#8217;t return an error, and it advances the parse pointer to beyond the <font SIZE="-1">UTF-8</font> in question, but it returns the Unicode <font SIZE="-1">REPLACEMENT CHARACTER</font> as the value of the code point (since the real value is not representable). </p>
<p> They no longer abandon searching for other malformations when the first one is encountered. A call to one of these functions thus can generate multiple diagnostics, instead of just one. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;valid_utf8_to_uvchr()&quot;</code> has been added to the <font SIZE="-1">API</font> (although it was present in core earlier). Like <code>&quot;utf8_to_uvchr_buf()&quot;</code>, but assumes that the next character is well-formed. Use with caution. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new function, <code>&quot;utf8n_to_uvchr_error&quot;</code>, has been added for use by modules that need to know the details of <font SIZE="-1">UTF-8</font> malformations beyond pass/fail. Previously, the only ways to know why a sequence was ill-formed was to capture and parse the generated diagnostics or to do your own analysis. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> There is now a safer version of <code>utf8_hop()</code>, called <code>&quot;utf8_hop_safe()&quot;</code>. Unlike <code>utf8_hop()</code>, <code>utf8_hop_safe()</code> won&#8217;t navigate before the beginning or after the end of the supplied buffer. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Two new functions, <code>&quot;utf8_hop_forward()&quot;</code> and <code>&quot;utf8_hop_back()&quot;</code> are similar to <code>&quot;utf8_hop_safe()&quot;</code> but are for when you know which direction you wish to travel. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Two new macros which return useful utf8 byte sequences: </p>
<p> <code>&quot;BOM_UTF8&quot;</code> </p>
<p> <code>&quot;REPLACEMENT_CHARACTER_UTF8&quot;</code> </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>&bull;</dt>
<dd> <p> Perl is now built with the <code>&quot;PERL_OP_PARENT&quot;</code> compiler define enabled by default. To disable it, use the <code>&quot;PERL_NO_OP_PARENT&quot;</code> compiler define. This flag alters how the <code>&quot;op_sibling&quot;</code> field is used in <code>&quot;OP&quot;</code> structures, and has been available optionally since perl 5.22. </p>
<p> See ``Internal Changes&#8217;&#8216; in perl5220delta for more details of what this build option does. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Three new ops, <code>&quot;OP_ARGELEM&quot;</code>, <code>&quot;OP_ARGDEFELEM&quot;</code>, and <code>&quot;OP_ARGCHECK&quot;</code> have been added. These are intended principally to implement the individual elements of a subroutine signature, plus any overall checking required. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;OP_PUSHRE&quot;</code> op has been eliminated and the <code>&quot;OP_SPLIT&quot;</code> op has been changed from class <code>&quot;LISTOP&quot;</code> to <code>&quot;PMOP&quot;</code>. </p>
<p> Formerly the first child of a split would be a <code>&quot;pushre&quot;</code>, which would have the <code>&quot;split&quot;</code>&#8216;s regex attached to it. Now the regex is attached directly to the <code>&quot;split&quot;</code> op, and the <code>&quot;pushre&quot;</code> has been eliminated. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;op_class()&quot;</code> <font SIZE="-1">API</font> function has been added. This is like the existing <code>&quot;OP_CLASS()&quot;</code> macro, but can more accurately determine what struct an op has been allocated as. For example <code>&quot;OP_CLASS()&quot;</code> might return <code>&quot;OA_BASEOP_OR_UNOP&quot;</code> indicating that ops of this type are usually allocated as an <code>&quot;OP&quot;</code> or <code>&quot;UNOP&quot;</code>; while <code>&quot;op_class()&quot;</code> will return <code>&quot;OPclass_BASEOP&quot;</code> or <code>&quot;OPclass_UNOP&quot;</code> as appropriate. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> All parts of the internals now agree that the <code>&quot;sassign&quot;</code> op is a <code>&quot;BINOP&quot;</code>; previously it was listed as a <code>&quot;BASEOP&quot;</code> in <i>regen/opcodes</i>, which meant that several parts of the internals had to be special-cased to accommodate it. This oddity&#8217;s original motivation was to handle code like <code>&quot;$x ||= 1&quot;</code>; that is now handled in a simpler way. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The output format of the <code>&quot;op_dump()&quot;</code> function (as used by <code>&quot;perl -Dx&quot;</code>) has changed: it now displays an ``ASCII-art&#8217;&#8216; tree structure, and shows more low-level details about each op, such as its address and class. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;PADOFFSET&quot;</code> type has changed from being unsigned to signed, and several pad-related variables such as <code>&quot;PL_padix&quot;</code> have changed from being of type <code>&quot;I32&quot;</code> to type <code>&quot;PADOFFSET&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;DEBUGGING&quot;</code>-mode output for regex compilation and execution has been enhanced. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Several obscure <font SIZE="-1">SV</font> flags have been eliminated, sometimes along with the macros which manipulate them: <code>&quot;SVpbm_VALID&quot;</code>, <code>&quot;SVpbm_TAIL&quot;</code>, <code>&quot;SvTAIL_on&quot;</code>, <code>&quot;SvTAIL_off&quot;</code>, <code>&quot;SVrepl_EVAL&quot;</code>, <code>&quot;SvEVALED&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> An <font SIZE="-1">OP</font> <code>&quot;op_private&quot;</code> flag has been eliminated: <code>&quot;OPpRUNTIME&quot;</code>. This used to often get set on <code>&quot;PMOP&quot;</code> ops, but had become meaningless over time. </p>
 </dd></dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> Perl no longer panics when switching into some locales on machines with buggy <code>&quot;strxfrm()&quot;</code> implementations in their <i>libc</i>. [perl #121734] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=121734">https://rt.perl.org/Public/Bug/Display.html?id=121734</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot; $-{$name} &quot;</code> would leak an <code>&quot;AV&quot;</code> on each access if the regular expression had no named captures. The same applies to access to any hash tied with Tie::Hash::NamedCapture and <code>&quot;all =&gt; 1&quot;</code>. [perl #130822] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=130822">https://rt.perl.org/Public/Bug/Display.html?id=130822</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Attempting to use the deprecated variable <code>$#</code> as the object in an indirect object method call could cause a heap use after free or buffer overflow. [perl #129274] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=129274">https://rt.perl.org/Public/Bug/Display.html?id=129274</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> When checking for an indirect object method call, in some rare cases the parser could reallocate the line buffer but then continue to use pointers to the old buffer. [perl #129190] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=129190">https://rt.perl.org/Public/Bug/Display.html?id=129190</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Supplying a glob as the format argument to <code>&quot;formline&quot;</code> would cause an assertion failure. [perl #130722] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=130722">https://rt.perl.org/Public/Bug/Display.html?id=130722</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Code like <code>&quot; $value1 =~ qr/.../ ~~ $value2 &quot;</code> would have the match converted into a <code>&quot;qr//&quot;</code> operator, leaving extra elements on the stack to confuse any surrounding expression. [perl #130705] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=130705">https://rt.perl.org/Public/Bug/Display.html?id=130705</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Since v5.24 in some obscure cases, a regex which included code blocks from multiple sources (<i>e.g.</i>, via embedded via <code>&quot;qr//&quot;</code> objects) could end up with the wrong current pad and crash or give weird results. [perl #129881] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=129881">https://rt.perl.org/Public/Bug/Display.html?id=129881</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Occasionally <code>&quot;local()&quot;</code>s in a code block within a patterns weren&#8217;t being undone when the pattern matching backtracked over the code block. [perl #126697] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=126697">https://rt.perl.org/Public/Bug/Display.html?id=126697</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Using <code>&quot;substr()&quot;</code> to modify a magic variable could access freed memory in some cases. [perl #129340] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=129340">https://rt.perl.org/Public/Bug/Display.html?id=129340</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Under <code>&quot;use utf8&quot;</code>, the entire source code is now checked for being <font SIZE="-1">UTF-8</font> well formed, not just quoted strings as before. [perl #126310] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=126310">https://rt.perl.org/Public/Bug/Display.html?id=126310</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The range operator <code>&quot;..&quot;</code> on strings now handles its arguments correctly when in the scope of the <code>&quot;unicode_strings&quot;</code> feature. The previous behaviour was sufficiently unexpected that we believe no correct program could have made use of it. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;split&quot;</code> operator did not ensure enough space was allocated for its return value in scalar context. It could then write a single pointer immediately beyond the end of the memory block allocated for the stack. [perl #130262] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=130262">https://rt.perl.org/Public/Bug/Display.html?id=130262</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Using a large code point with the <code>&quot;W&quot;</code> pack template character with the current output position aligned at just the right point could cause a write of a single zero byte immediately beyond the end of an allocated buffer. [perl #129149] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=129149">https://rt.perl.org/Public/Bug/Display.html?id=129149</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Supplying a format&#8217;s picture argument as part of the format argument list where the picture specifies modifying the argument could cause an access to the new freed compiled form.at. [perl #129125] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=129125">https://rt.perl.org/Public/Bug/Display.html?id=129125</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>sort()</code> operator&#8217;s built-in numeric comparison function didn&#8217;t handle large integers that weren&#8217;t exactly representable by a double. This now uses the same code used to implement the <code>&quot;&lt;=&gt;&quot;</code> operator. [perl #130335] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=130335">https://rt.perl.org/Public/Bug/Display.html?id=130335</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fix issues with <code>&quot;/(?{ ... &lt;&lt;EOF })/&quot;</code> that broke Method::Signatures. [perl #130398] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=130398">https://rt.perl.org/Public/Bug/Display.html?id=130398</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed an assertion failure with <code>&quot;chop&quot;</code> and <code>&quot;chomp&quot;</code>, which could be triggered by <code>&quot;chop(@x =~ tr/1/1/)&quot;</code>. [perl #130198] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=130198">https://rt.perl.org/Public/Bug/Display.html?id=130198</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed a comment skipping error in patterns under <code>&quot;/x&quot;</code>; it could stop skipping a byte early, which could be in the middle of a <font SIZE="-1">UTF-8</font> character. [perl #130495] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=130495">https://rt.perl.org/Public/Bug/Display.html?id=130495</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>perldb</i> now ignores <i>/dev/tty</i> on non-Unix systems. [perl #113960] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=113960">https://rt.perl.org/Public/Bug/Display.html?id=113960</a>&gt;; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fix assertion failure for <code>&quot;{}-&gt;$x&quot;</code> when <code>$x</code> isn&#8217;t defined. [perl #130496] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=130496">https://rt.perl.org/Public/Bug/Display.html?id=130496</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fix an assertion error which could be triggered when a lookahead string in patterns exceeded a minimum length. [perl #130522] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=130522">https://rt.perl.org/Public/Bug/Display.html?id=130522</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Only warn once per literal number about a misplaced <code>&quot;_&quot;</code>. [perl #70878] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=70878">https://rt.perl.org/Public/Bug/Display.html?id=70878</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;tr///&quot;</code> parse code could be looking at uninitialized data after a perse error. [perl #129342] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=129342">https://rt.perl.org/Public/Bug/Display.html?id=129342</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In a pattern match, a back-reference (<code>&quot;\1&quot;</code>) to an unmatched capture could read back beyond the start of the string being matched. [perl #129377] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=129377">https://rt.perl.org/Public/Bug/Display.html?id=129377</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;use re &#8216;strict&#8217;&quot;</code> is supposed to warn if you use a range (such as <code>&quot;/(?[ [ X-Y ] ])/&quot;</code>) whose start and end digit aren&#8217;t from the same group of 10. It didn&#8217;t do that for five groups of mathematical digits starting at <code>&quot;U+1D7E&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A sub containing a ``forward&#8217;&#8216; declaration with the same name (<i>e.g.</i>, <code>&quot;sub c { sub c; }&quot;</code>) could sometimes crash or loop infinitely. [perl #129090] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=129090">https://rt.perl.org/Public/Bug/Display.html?id=129090</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A crash in executing a regex with a non-anchored <font SIZE="-1">UTF-8</font> substring against a target string that also used <font SIZE="-1">UTF-8</font> has been fixed. [perl #129350] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=129350">https://rt.perl.org/Public/Bug/Display.html?id=129350</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Previously, a shebang line like <code>&quot;#!perl -i u&quot;</code> could be erroneously interpreted as requesting the <code>&quot;-u&quot;</code> option. This has been fixed. [perl #129336] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=129336">https://rt.perl.org/Public/Bug/Display.html?id=129336</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The regex engine was previously producing incorrect results in some rare situations when backtracking past an alternation that matches only one thing; this showed up as capture buffers (<code>$1</code>, <code>$2</code>, <i>etc.</i>) erroneously containing data from regex execution paths that weren&#8217;t actually executed for the final match. [perl #129897] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=129897">https://rt.perl.org/Public/Bug/Display.html?id=129897</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Certain regexes making use of the experimental <code>&quot;regex_sets&quot;</code> feature could trigger an assertion failure. This has been fixed. [perl #129322] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=129322">https://rt.perl.org/Public/Bug/Display.html?id=129322</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Invalid assignments to a reference constructor (<i>e.g.</i>, <code>&quot;\eval=time&quot;</code>) could sometimes crash in addition to giving a syntax error. [perl #125679] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=125679">https://rt.perl.org/Public/Bug/Display.html?id=125679</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The parser could sometimes crash if a bareword came after <code>&quot;evalbytes&quot;</code>. [perl #129196] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=129196">https://rt.perl.org/Public/Bug/Display.html?id=129196</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Autoloading via a method call would warn erroneously (``Use of inherited <font SIZE="-1">AUTOLOAD</font> for non-method&#8217;&#8216;) if there was a stub present in the package into which the invocant had been blessed. The warning is no longer emitted in such circumstances. [perl #47047] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=47047">https://rt.perl.org/Public/Bug/Display.html?id=47047</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The use of <code>&quot;splice&quot;</code> on arrays with non-existent elements could cause other operators to crash. [perl #129164] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=129164">https://rt.perl.org/Public/Bug/Display.html?id=129164</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A possible buffer overrun when a pattern contains a fixed utf8 substring. [perl #129012] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=129012">https://rt.perl.org/Public/Bug/Display.html?id=129012</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed two possible use-after-free bugs in perl&#8217;s lexer. [perl #129069] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=129069">https://rt.perl.org/Public/Bug/Display.html?id=129069</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed a crash with <code>&quot;s///l&quot;</code> where it thought it was dealing with <font SIZE="-1">UTF-8</font> when it wasn&#8217;t. [perl #129038] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=129038">https://rt.perl.org/Public/Bug/Display.html?id=129038</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed a place where the regex parser was not setting the syntax error correctly on a syntactically incorrect pattern. [perl #129122] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=129122">https://rt.perl.org/Public/Bug/Display.html?id=129122</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;&amp;.&quot;</code> operator (and the <code>&quot;&amp;&quot;</code> operator, when it treats its arguments as strings) were failing to append a trailing null byte if at least one string was marked as utf8 internally. Many code paths (system calls, regexp compilation) still expect there to be a null byte in the string buffer just past the end of the logical string. An assertion failure was the result. [perl #129287] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=129287">https://rt.perl.org/Public/Bug/Display.html?id=129287</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Avoid a heap-after-use error in the parser when creating an error messge for a syntactically invalid heredoc. [perl #128988] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128988">https://rt.perl.org/Public/Bug/Display.html?id=128988</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fix a segfault when run with <code>&quot;-DC&quot;</code> options on <font SIZE="-1">DEBUGGING</font> builds. [perl #129106] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=129106">https://rt.perl.org/Public/Bug/Display.html?id=129106</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed the parser error handling in subroutine attributes for an &#8216;<code>&quot;:attr(foo&quot;</code>&#8216; that does not have an ending &#8216;<code>&quot;)&quot;</code>&#8216;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fix the perl lexer to correctly handle a backslash as the last char in quoted-string context. This actually fixed two bugs, [perl #129064] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=129064">https://rt.perl.org/Public/Bug/Display.html?id=129064</a>&gt; and [perl #129176] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=129176">https://rt.perl.org/Public/Bug/Display.html?id=129176</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In the <font SIZE="-1">API</font> function <code>&quot;gv_fetchmethod_pvn_flags&quot;</code>, rework separator parsing to prevent possible string overrun with an invalid <code>&quot;len&quot;</code> argument. [perl #129267] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=129267">https://rt.perl.org/Public/Bug/Display.html?id=129267</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Problems with in-place array sorts: code like <code>&quot;@a = sort { ... } @a&quot;</code>, where the source and destination of the sort are the same plain array, are optimised to do less copying around. Two side-effects of this optimisation were that the contents of <code>@a</code> as seen by sort routines were partially sorted; and under some circumstances accessing <code>@a</code> during the sort could crash the interpreter. Both these issues have been fixed, and Sort functions see the original value of <code>@a</code>. [perl #128340] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128340">https://rt.perl.org/Public/Bug/Display.html?id=128340</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Non-ASCII string delimiters are now reported correctly in error messages for unterminated strings. [perl #128701] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128701">https://rt.perl.org/Public/Bug/Display.html?id=128701</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;pack(&quot;p&quot;, ...)&quot;</code> used to emit its warning (``Attempt to pack pointer to temporary value&#8217;&#8216;) erroneously in some cases, but has been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>@DB::args</code> is now exempt from ``used once&#8217;&#8216; warnings. The warnings only occurred under <code>-w</code>, because <i>warnings.pm</i> itself uses <code>@DB::args</code> multiple times. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The use of built-in arrays or hash slices in a double-quoted string no longer issues a warning (``Possible unintended interpolation...&#8216;&#8216;) if the variable has not been mentioned before. This affected code like <code>&quot;qq|@DB::args|&quot;</code> and <code>&quot;qq|@SIG{&#8216;CHLD&#8217;, &#8216;HUP&#8217;}|&quot;</code>. (The special variables <code>&quot;@-&quot;</code> and <code>&quot;@+&quot;</code> were already exempt from the warning.) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;gethostent&quot;</code> and similar functions now perform a null check internally, to avoid crashing with the torsocks library. This was a regression from v5.22. [perl #128740] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128740">https://rt.perl.org/Public/Bug/Display.html?id=128740</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;defined *{&#8216;!&#8216;}&quot;</code>, <code>&quot;defined *{&#8216;[&#8216;}&quot;</code>, and <code>&quot;defined *{&#8216;-&#8216;}&quot;</code> no longer leak memory if the typeglob in question has never been accessed before. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Mentioning the same constant twice in a row (which is a syntax error) no longer fails an assertion under debugging builds. This was a regression from v5.20. [perl #126482] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=126482">https://rt.perl.org/Public/Bug/Display.html?id=126482</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Many issues relating to <code>&quot;printf &quot;%a&quot;&quot;</code> of hexadecimal floating point were fixed. In addition, the ``subnormals&#8217;&#8216; (formerly known as ``denormals&#8217;&#8216;) floating point numbers are now supported both with the plain <font SIZE="-1">IEEE 754</font> floating point numbers (64-bit or 128-bit) and the x86 80-bit ``extended precision&#8217;&#8216;. Note that subnormal hexadecimal floating point literals will give a warning about ``exponent underflow&#8217;&#8216;. [perl #128843] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128843">https://rt.perl.org/Public/Bug/Display.html?id=128843</a>&gt; [perl #128889] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128889">https://rt.perl.org/Public/Bug/Display.html?id=128889</a>&gt; [perl #128890] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128890">https://rt.perl.org/Public/Bug/Display.html?id=128890</a>&gt; [perl #128893] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128893">https://rt.perl.org/Public/Bug/Display.html?id=128893</a>&gt; [perl #128909] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128909">https://rt.perl.org/Public/Bug/Display.html?id=128909</a>&gt; [perl #128919] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128919">https://rt.perl.org/Public/Bug/Display.html?id=128919</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A regression in v5.24 with <code>&quot;tr/\N{U+...}/foo/&quot;</code> when the code point was between 128 and 255 has been fixed. [perl #128734] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128734">https://rt.perl.org/Public/Bug/Display.html?id=128734</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Use of a string delimiter whose code point is above 2**31 now works correctly on platforms that allow this. Previously, certain characters, due to truncation, would be confused with other delimiter characters with special meaning (such as <code>&quot;?&quot;</code> in <code>&quot;m?...?&quot;</code>), resulting in inconsistent behaviour. Note that this is non-portable, and is based on Perl&#8217;s extension to <font SIZE="-1">UTF-8,</font> and is probably not displayable nor enterable by any editor. [perl #128738] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128738">https://rt.perl.org/Public/Bug/Display.html?id=128738</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;@{x&quot;</code> followed by a newline where <code>&quot;x&quot;</code> represents a control or non-ASCII character no longer produces a garbled syntax error message or a crash. [perl #128951] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128951">https://rt.perl.org/Public/Bug/Display.html?id=128951</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> An assertion failure with <code>&quot;%: = 0&quot;</code> has been fixed. [perl #128238] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128238">https://rt.perl.org/Public/Bug/Display.html?id=128238</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In Perl 5.18, the parsing of <code>&quot;$foo::$bar&quot;</code> was accidentally changed, such that it would be treated as <code>&quot;$foo.&quot;::&quot;.$bar&quot;</code>. The previous behavior, which was to parse it as <code>&quot;$foo:: . $bar&quot;</code>, has been restored. [perl #128478] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128478">https://rt.perl.org/Public/Bug/Display.html?id=128478</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Since Perl 5.20, line numbers have been off by one when perl is invoked with the <code>-x</code> switch. This has been fixed. [perl #128508] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128508">https://rt.perl.org/Public/Bug/Display.html?id=128508</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Vivifying a subroutine stub in a deleted stash (<i>e.g.</i>, <code>&quot;delete $My::{&quot;Foo::&quot;}; \&amp;My::Foo::foo&quot;</code>) no longer crashes. It had begun crashing in Perl 5.18. [perl #128532] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128532">https://rt.perl.org/Public/Bug/Display.html?id=128532</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Some obscure cases of subroutines and file handles being freed at the same time could result in crashes, but have been fixed. The crash was introduced in Perl 5.22. [perl #128597] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128597">https://rt.perl.org/Public/Bug/Display.html?id=128597</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Code that looks for a variable name associated with an uninitialized value could cause an assertion failure in cases where magic is involved, such as <code>$ISA[0][0]</code>. This has now been fixed. [perl #128253] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128253">https://rt.perl.org/Public/Bug/Display.html?id=128253</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A crash caused by code generating the warning ``Subroutine <font SIZE="-1">STASH::NAME</font> redefined&#8217;&#8216; in cases such as <code>&quot;sub P::f{} undef *P::; *P::f =sub{};&quot;</code> has been fixed. In these cases, where the <font SIZE="-1">STASH</font> is missing, the warning will now appear as ``Subroutine <font SIZE="-1">NAME</font> redefined&#8217;&#8216;. [perl #128257] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128257">https://rt.perl.org/Public/Bug/Display.html?id=128257</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed an assertion triggered by some code that handles deprecated behavior in formats, <i>e.g.</i>, in cases like this: </p>
<pre><code>    format STDOUT =
    @
    0&quot;$x&quot;
</code></pre>
<p> [perl #128255] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128255">https://rt.perl.org/Public/Bug/Display.html?id=128255</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A possible divide by zero in string transformation code on Windows has been avoided, fixing a crash when collating an empty string. [perl #128618] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128618">https://rt.perl.org/Public/Bug/Display.html?id=128618</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Some regular expression parsing glitches could lead to assertion failures with regular expressions such as <code>&quot;/(?&lt;=/&quot;</code> and <code>&quot;/(?&lt;!/&quot;</code>. This has now been fixed. [perl #128170] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128170">https://rt.perl.org/Public/Bug/Display.html?id=128170</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot; until ($x = 1) { ... } &quot;</code> and <code>&quot; ... until $x = 1 &quot;</code> now properly warn when syntax warnings are enabled. [perl #127333] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=127333">https://rt.perl.org/Public/Bug/Display.html?id=127333</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>socket()</code> now leaves the error code returned by the system in <code>$!</code> on failure. [perl #128316] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128316">https://rt.perl.org/Public/Bug/Display.html?id=128316</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Assignment variants of any bitwise ops under the <code>&quot;bitwise&quot;</code> feature would crash if the left-hand side was an array or hash. [perl #128204] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128204">https://rt.perl.org/Public/Bug/Display.html?id=128204</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;require&quot;</code> followed by a single colon (as in <code>&quot;foo() ? require : ...&quot;</code> is now parsed correctly as <code>&quot;require&quot;</code> with implicit <code>$_</code>, rather than <code>&quot;require &quot;&quot;&quot;</code>. [perl #128307] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128307">https://rt.perl.org/Public/Bug/Display.html?id=128307</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Scalar <code>&quot;keys %hash&quot;</code> can now be assigned to consistently in all scalar lvalue contexts. Previously it worked for some contexts but not others. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> List assignment to <code>&quot;vec&quot;</code> or <code>&quot;substr&quot;</code> with an array or hash for its first argument used to result in crashes or ``Can&#8217;t coerce&#8217;&#8216; error messages at run time, unlike scalar assignment, which would give an error at compile time. List assignment now gives a compile-time error, too. [perl #128260] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128260">https://rt.perl.org/Public/Bug/Display.html?id=128260</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Expressions containing an <code>&quot;&amp;&amp;&quot;</code> or <code>&quot;||&quot;</code> operator (or their synonyms <code>&quot;and&quot;</code> and <code>&quot;or&quot;</code>) were being compiled incorrectly in some cases. If the left-hand side consisted of either a negated bareword constant or a negated <code>&quot;do {}&quot;</code> block containing a constant expression, and the right-hand side consisted of a negated non-foldable expression, one of the negations was effectively ignored. The same was true of <code>&quot;if&quot;</code> and <code>&quot;unless&quot;</code> statement modifiers, though with the left-hand and right-hand sides swapped. This long-standing bug has now been fixed. [perl #127952] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=127952">https://rt.perl.org/Public/Bug/Display.html?id=127952</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;reset&quot;</code> with an argument no longer crashes when encountering stash entries other than globs. [perl #128106] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128106">https://rt.perl.org/Public/Bug/Display.html?id=128106</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Assignment of hashes to, and deletion of, typeglobs named <code>*::::::</code> no longer causes crashes. [perl #128086] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128086">https://rt.perl.org/Public/Bug/Display.html?id=128086</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl wasn&#8217;t correctly handling true/false values in the <font SIZE="-1">LHS</font> of a list assign; specifically the truth values returned by boolean operators. This could trigger an assertion failure in something like the following: </p>
<pre><code>    for ($x &gt; $y) {
        ($_, ...) = (...); # here $_ is aliased to a truth value
    }
</code></pre>
<p> This was a regression from v5.24. [perl #129991] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=129991">https://rt.perl.org/Public/Bug/Display.html?id=129991</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Assertion failure with user-defined Unicode-like properties. [perl #130010] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=130010">https://rt.perl.org/Public/Bug/Display.html?id=130010</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fix error message for unclosed <code>&quot;\N{&quot;</code> in a regex. An unclosed <code>&quot;\N{&quot;</code> could give the wrong error message: <code>&quot;\N{NAME} must be resolved by the lexer&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> List assignment in list context where the <font SIZE="-1">LHS</font> contained aggregates and where there were not enough <font SIZE="-1">RHS</font> elements, used to skip scalar lvalues. Previously, <code>&quot;(($a,$b,@c,$d) = (1))&quot;</code> in list context returned <code>&quot;($a)&quot;</code>; now it returns <code>&quot;($a,$b,$d)&quot;</code>. <code>&quot;(($a,$b,$c) = (1))&quot;</code> is unchanged: it still returns <code>&quot;($a,$b,$c)&quot;</code>. This can be seen in the following: </p>
<pre><code>    sub inc { $_++ for @_ }
    inc(($a,$b,@c,$d) = (10))
</code></pre>
<p> Formerly, the values of <code>&quot;($a,$b,$d)&quot;</code> would be left as <code>&quot;(11,undef,undef)&quot;</code>; now they are <code>&quot;(11,1,1)&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Code like this: <code>&quot;/(?{ s!!! })/&quot;</code> could trigger infinite recursion on the C stack (not the normal perl stack) when the last successful pattern in scope is itself. We avoid the segfault by simply forbidding the use of the empty pattern when it would resolve to the currently executing pattern. [perl #129903] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=129903">https://rt.perl.org/Public/Bug/Display.html?id=129903</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Avoid reading beyond the end of the line buffer in perl&#8217;s lexer when there&#8217;s a short <font SIZE="-1">UTF-8</font> character at the end. [perl #128997] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128997">https://rt.perl.org/Public/Bug/Display.html?id=128997</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Alternations in regular expressions were sometimes failing to match a utf8 string against a utf8 alternate. [perl #129950] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=129950">https://rt.perl.org/Public/Bug/Display.html?id=129950</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Make <code>&quot;do &quot;a\0b&quot;&quot;</code> fail silently (and return <code>&quot;undef&quot;</code> and set <code>$!</code>) instead of throwing an error. [perl #129928] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=129928">https://rt.perl.org/Public/Bug/Display.html?id=129928</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;chdir&quot;</code> with no argument didn&#8217;t ensure that there was stack space available for returning its result. [perl #129130] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=129130">https://rt.perl.org/Public/Bug/Display.html?id=129130</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> All error messages related to <code>&quot;do&quot;</code> now refer to <code>&quot;do&quot;</code>; some formerly claimed to be from <code>&quot;require&quot;</code> instead. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Executing <code>&quot;undef $x&quot;</code> where <code>$x</code> is tied or magical no longer incorrectly blames the variable for an uninitialized-value warning encountered by the tied/magical code. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Code like <code>&quot;$x = $x . &quot;a&quot;&quot;</code> was incorrectly failing to yield a use of uninitialized value warning when <code>$x</code> was a lexical variable with an undefined value. That has now been fixed. [perl #127877] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=127877">https://rt.perl.org/Public/Bug/Display.html?id=127877</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;undef *_; shift&quot;</code> or <code>&quot;undef *_; pop&quot;</code> inside a subroutine, with no argument to <code>&quot;shift&quot;</code> or <code>&quot;pop&quot;</code>, began crashing in Perl 5.14, but has now been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;string$scalar-&gt;$*&quot;</code> now correctly prefers concatenation overloading to string overloading if <code>&quot;$scalar-&gt;$*&quot;</code> returns an overloaded object, bringing it into consistency with <code>$$scalar</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;/@0{0*-&gt;@*/*0&quot;</code> and similar contortions used to crash, but no longer do, but merely produce a syntax error. [perl #128171] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128171">https://rt.perl.org/Public/Bug/Display.html?id=128171</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;do&quot;</code> or <code>&quot;require&quot;</code> with an argument which is a reference or typeglob which, when stringified, contains a null character, started crashing in Perl 5.20, but has now been fixed. [perl #128182] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128182">https://rt.perl.org/Public/Bug/Display.html?id=128182</a>&gt; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Improve the error message for a missing <code>&quot;tie()&quot;</code> package/method. This brings the error messages in line with the ones used for normal method calls. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Parsing bad <font SIZE="-1">POSIX</font> charclasses no longer leaks memory. [perl #128313] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=128313">https://rt.perl.org/Public/Bug/Display.html?id=128313</a>&gt; </p>
 </dd></dl>
<h2>Known Problems</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> G++ 6 handles subnormal (denormal) floating point values differently than gcc 6 or g++ 5 resulting in ``flush-to-zero&#8217;&#8216;. The end result is that if you specify very small values using the hexadecimal floating point format, like <code>&quot;0x1.fffffffffffffp-1022&quot;</code>, they become zeros. [perl #131388] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=131388">https://rt.perl.org/Ticket/Display.html?id=131388</a>&gt; </p>
 </dd></dl>
<h2>Errata From Previous Releases</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> Fixed issues with recursive regexes. The behavior was fixed in Perl 5.24. [perl #126182] &lt;<a rel="nofollow" href="https://rt.perl.org/Public/Bug/Display.html?id=126182">https://rt.perl.org/Public/Bug/Display.html?id=126182</a>&gt; </p>
 </dd></dl>
<h2>Obituary</h2>
<p> Jon Portnoy (<font SIZE="-1">AVENJ</font>), a prolific Perl author and admired Gentoo community member, has passed away on August 10, 2016. He will be remembered and missed by all those who he came in contact with, and enriched with his intellect, wit, and spirit. </p>
<p> It is with great sadness that we also note Kip Hampton&#8217;s passing. Probably best known as the author of the Perl &amp; <font SIZE="-1">XML</font> column on <font SIZE="-1">XML</font>.com, he was a core contributor to AxKit, an <font SIZE="-1">XML</font> server platform that became an Apache Foundation project. He was a frequent speaker in the early days at <font SIZE="-1">OSCON,</font> and most recently at <font SIZE="-1">YAPC::NA</font> in Madison. He was frequently on irc.perl.org as ubu, generally in the #axkit-dahut community, the group responsible for <font SIZE="-1">YAPC::NA</font> Asheville in 2011. </p>
<p> Kip and his constant contributions to the community will be greatly missed.  </p>
<h2>Acknowledgements</h2>
<p> Perl 5.26.0 represents approximately 13 months of development since Perl 5.24.0 and contains approximately 360,000 lines of changes across 2,600 files from 86 authors. </p>
<p> Excluding auto-generated files, documentation and release tools, there were approximately 230,000 lines of changes to 1,800 .pm, .t, .c and .h files. </p>
<p> Perl continues to flourish into its third decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl 5.26.0: </p>
<p> Aaron Crane, Abigail, Ævar Arnfjörð Bjarmason, Alex Vandiver, Andreas König, Andreas Voegele, Andrew Fresh, Andy Lester, Aristotle Pagaltzis, Chad Granum, Chase Whitener, Chris &#8216;BinGOs&#8217; Williams, Chris Lamb, Christian Hansen, Christian Millour, Colin Newell, Craig A. Berry, Dagfinn Ilmari Mannsåker, Dan Collins, Daniel Dragan, Dave Cross, Dave Rolsky, David Golden, David H. Gutteridge, David Mitchell, Dominic Hargreaves, Doug Bell, E. Choroba, Ed Avis, Father Chrysostomos, François Perrad, Hauke D, H.Merijn Brand, Hugo van der Sanden, Ivan Pozdeev, James E Keenan, James Raspass, Jarkko Hietaniemi, Jerry D. Hedden, Jim Cromie, J. Nick Koston, John Lightsey, Karen Etheridge, Karl Williamson, Leon Timmermans, Lukas Mai, Matthew Horsfall, Maxwell Carey, Misty De Meo, Neil Bowers, Nicholas Clark, Nicolas R., Niko Tyni, Pali, Paul Marquess, Peter Avalos, Petr Písař, Pino Toscano, Rafael Garcia-Suarez, Reini Urban, Renee Baecker, Ricardo Signes, Richard Levitte, Rick Delaney, Salvador Fandiño, Samuel Thibault, Sawyer X, Sébastien Aperghis-Tramoni, Sergey Aleynikov, Shlomi Fish, Smylers, Stefan Seifert, Steffen Müller, Stevan Little, Steve Hay, Steven Humphrey, Sullivan Beck, Theo Buehler, Thomas Sibley, Todd Rinaldo, Tomasz Konojacki, Tony Cook, Unicode Consortium, Yaroslav Kuzmin, Yves Orton, Zefram. </p>
<p> The list above is almost certainly incomplete as it is automatically generated from version control history. In particular, it does not include the names of the (very much appreciated) contributors who reported issues to the Perl bug tracker. </p>
<p> Many of the changes included in this version originated in the <font SIZE="-1">CPAN</font> modules included in Perl&#8217;s core. We&#8217;re grateful to the entire <font SIZE="-1">CPAN</font> community for helping Perl to flourish. </p>
<p> For a more complete list of all of Perl&#8217;s historical contributors, please see the <i></i><font SIZE="-1"><i>AUTHORS</i></font><i></i> file in the Perl source distribution.  </p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the perl bug database at &lt;<a rel="nofollow" href="https://rt.perl.org/">https://rt.perl.org/</a>&gt;. There may also be information at &lt;<a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a>&gt;, the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the perlbug program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <code>&quot;perl -V&quot;</code>, will be sent off to <code>&quot;perlbug [at] perl.org&quot;</code> to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications which make it inappropriate to send to a publicly archived mailing list, then see ``<font SIZE="-1">SECURITY VULNERABILITY CONTACT INFORMATION&#8217;&#8216;</font> in perlsec for details of how to report the issue.  </p>
<h2>Give Thanks</h2>
<p> If you wish to thank the Perl 5 Porters for the work we had done in Perl 5, you can do so by running the <code>&quot;perlthanks&quot;</code> program: </p>
<pre><code>    perlthanks
</code></pre>
<p> This will send an email to the Perl 5 Porters list with your show of thanks.  </p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
<h2>Index</h2>
