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
<dt>&bull;</p>
<dd> <tt>&quot;.&quot;</tt> no longer in <tt>@INC</tt> </p>
<p> For security reasons, the current directory (<tt>&quot;.&quot;</tt>) is no longer included by default at the end of the module search path (<tt>@INC</tt>). This may have widespread implications for the building, testing and installing of modules, and for the execution of scripts. See the section &quot;Removal of the current directory (<tt>&quot;.&quot;</tt>) from <tt>@INC</tt>&quot; for the full details.</p>
<dt>&bull;</p>
<dd> <tt>&quot;do&quot;</tt> may now warn </p>
<p> <tt>&quot;do&quot;</tt> now gives a deprecation warning when it fails to load a file which it would have loaded had <tt>&quot;.&quot;</tt> been in <tt>@INC</tt>.</p>
<dt>&bull;</p>
<dd> In regular expression patterns, a literal left brace <tt>&quot;{&quot;</tt> should be escaped </p>
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
<dt>&bull;</p>
<dd> <i>Configure -Udefault_inc_excludes_dot</i> </p>
<p> There is a new <i>Configure</i> option, <tt>&quot;default_inc_excludes_dot&quot;</tt> (enabled by default) which builds a perl executable without <tt>&quot;.&quot;</tt>; unsetting this option using <tt>&quot;-U&quot;</tt> reverts perl to the old behaviour. This may fix your path issues but will reintroduce all the security concerns, so don&#8217;t build a perl executable like this unless you&#8217;re <i>really</i> confident that such issues are not a concern in your environment.</p>
<dt>&bull;</p>
<dd> <tt>&quot;PERL_USE_UNSAFE_INC&quot;</tt> </p>
<p> There is a new environment variable recognised by the perl interpreter. If this variable has the value 1 when the perl interpreter starts up, then <tt>&quot;.&quot;</tt> will be automatically appended to <tt>@INC</tt> (except under tainting). </p>
<p> This allows you restore the old perl interpreter behaviour on a case-by-case basis. But note that this is intended to be a temporary crutch, and this feature will likely be removed in some future perl version. It is currently set by the <tt>&quot;cpan&quot;</tt> utility and <tt>&quot;Test::Harness&quot;</tt> to ease installation of <font SIZE="-1">CPAN</font> modules which have not been updated to handle the lack of dot. Once again, don&#8217;t use this unless you are sure that this will not reintroduce any security concerns.</p>
<dt>&bull;</p>
<dd> A new deprecation warning issued by <tt>&quot;do&quot;</tt>. </p>
<p> While it is well-known that <tt>&quot;use&quot;</tt> and <tt>&quot;require&quot;</tt> use <tt>@INC</tt> to search for the file to load, many people don&#8217;t realise that <tt>&quot;do &quot;file&quot;&quot;</tt> also searches <tt>@INC</tt> if the file is a relative path. With the removal of <tt>&quot;.&quot;</tt>, a simple <tt>&quot;do &quot;file.pl&quot;&quot;</tt> will fail to read in and execute <tt>&quot;file.pl&quot;</tt> from the current directory. Since this is commonly expected behaviour, a new deprecation warning is now issued whenever <tt>&quot;do&quot;</tt> fails to load a file which it otherwise would have found if a dot had been in <tt>@INC</tt>.</dl>
<p> Here are some things script and module authors may need to do to make their software work in the new regime.</p>
<dl>
<dt>&bull;</p>
<dd> Script authors </p>
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
<dt>&bull;</p>
<dd> Installing and using <font SIZE="-1">CPAN</font> modules </p>
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
<dt>&bull;</p>
<dd> Module Authors </p>
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
<p> A variable name may no longer contain a literal control character under any circumstances. These previously were allowed in single-character names on <font SIZE="-1">ASCII</font> platforms, but have been deprecated there since Perl 5.20. This affects things like <tt>&quot;$</tt>
