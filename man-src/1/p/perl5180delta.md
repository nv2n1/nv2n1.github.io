---
title: "perl5180delta(1)"
name: "perl5180delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5180delta/"
description: "perl5180delta – what is new for perl v5.18.0"
---

<h2>DESCRIPTION</h2>
<p> This document describes differences between the v5.16.0 release and the v5.18.0 release. </p>
<p> If you are upgrading from an earlier release such as v5.14.0, first read perl5160delta, which describes differences between v5.14.0 and v5.16.0.</p>
<h2>Core Enhancements</h2>
<h3>New mechanism for experimental features</h3>
<p> Newly-added experimental features will now require this incantation: </p>
<pre>
    no warnings &quot;experimental::feature_name&quot;;
    use feature &quot;feature_name&quot;;  # would warn without the prev line
</pre>
<p> There is a new warnings category, called &#8220;experimental&#8221;, containing warnings that the feature pragma emits when enabling experimental features. </p>
<p> Newly-added experimental features will also be given special warning IDs, which consist of &#8220;experimental::&#8221; followed by the name of the feature. (The plan is to extend this mechanism eventually to all warnings, to allow them to be enabled or disabled individually, and not just by category.) </p>
<p> By saying </p>
<pre>
    no warnings &quot;experimental::feature_name&quot;;
</pre>
<p> you are taking responsibility for any breakage that future changes to, or removal of, the feature may cause. </p>
<p> Since some features (like <tt>&quot;~~&quot;</tt> or <tt>&quot;my $_&quot;</tt>) now emit experimental warnings, and you may want to disable them in code that is also run on perls that do not recognize these warning categories, consider using the <tt>&quot;if&quot;</tt> pragma like this: </p>
<pre><code>
    no if $] &gt;= 5.018, warnings =&gt; "experimental::feature_name";
</code></pre>
<p> Existing experimental features may begin emitting these warnings, too. Please consult perlexperiment for information on which features are considered experimental.</p>
<h3>Hash overhaul</h3>
<p> Changes to the implementation of hashes in perl v5.18.0 will be one of the most visible changes to the behavior of existing code. </p>
<p> By default, two distinct hash variables with identical keys and values may now provide their contents in a different order where it was previously identical. </p>
<p> When encountering these changes, the key to cleaning up from them is to accept that <code>hashes are unordered collections</code> and to act accordingly. </p>
<p> <i>Hash randomization</i> </p>
<p> The seed used by Perl&#8217;s hash function is now random. This means that the order which keys/values will be returned from functions like <tt>&quot;keys()&quot;</tt>, <tt>&quot;values()&quot;</tt>, and <tt>&quot;each()&quot;</tt> will differ from run to run. </p>
<p> This change was introduced to make Perl&#8217;s hashes more robust to algorithmic complexity attacks, and also because we discovered that it exposes hash ordering dependency bugs and makes them easier to track down. </p>
<p> Toolchain maintainers might want to invest in additional infrastructure to test for things like this. Running tests several times in a row and then comparing results will make it easier to spot hash order dependencies in code. Authors are strongly encouraged not to expose the key order of Perl&#8217;s hashes to insecure audiences. </p>
<p> Further, every hash has its own iteration order, which should make it much more difficult to determine what the current hash seed is. </p>
<p> <i>New hash functions</i> </p>
<p> Perl v5.18 includes support for multiple hash functions, and changed the default (to <font SIZE="-1">ONE_AT_A_TIME_HARD</font>), you can choose a different algorithm by defining a symbol at compile time. For a current list, consult the <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> document. Note that as of Perl v5.18 we can only recommend use of the default or <font SIZE="-1">SIPHASH.</font> All the others are known to have security issues and are for research purposes only. </p>
<p> <i></i><font SIZE="-1"><i>PERL_HASH_SEED</i></font><i> environment variable now takes a hex value</i> </p>
<p> <tt>&quot;PERL_HASH_SEED&quot;</tt> no longer accepts an integer as a parameter; instead the value is expected to be a binary value encoded in a hex string, such as &#8220;0xf5867c55039dc724&#8221;. This is to make the infrastructure support hash seeds of arbitrary lengths, which might exceed that of an integer. (SipHash uses a 16 byte seed.) </p>
<p> <i></i><font SIZE="-1"><i>PERL_PERTURB_KEYS</i></font><i> environment variable added</i> </p>
<p> The <tt>&quot;PERL_PERTURB_KEYS&quot;</tt> environment variable allows one to control the level of randomization applied to <tt>&quot;keys&quot;</tt> and friends. </p>
<p> When <tt>&quot;PERL_PERTURB_KEYS&quot;</tt> is 0, perl will not randomize the key order at all. The chance that <tt>&quot;keys&quot;</tt> changes due to an insert will be the same as in previous perls, basically only when the bucket size is changed. </p>
<p> When <tt>&quot;PERL_PERTURB_KEYS&quot;</tt> is 1, perl will randomize keys in a non-repeatable way. The chance that <tt>&quot;keys&quot;</tt> changes due to an insert will be very high. This is the most secure and default mode. </p>
<p> When <tt>&quot;PERL_PERTURB_KEYS&quot;</tt> is 2, perl will randomize keys in a repeatable way. Repeated runs of the same program should produce the same output every time. </p>
<p> <tt>&quot;PERL_HASH_SEED&quot;</tt> implies a non-default <tt>&quot;PERL_PERTURB_KEYS&quot;</tt> setting. Setting <tt>&quot;PERL_HASH_SEED=0&quot;</tt> (exactly one 0) implies <tt>&quot;PERL_PERTURB_KEYS=0&quot;</tt> (hash key randomization disabled); setting <tt>&quot;PERL_HASH_SEED&quot;</tt> to any other value implies <tt>&quot;PERL_PERTURB_KEYS=2&quot;</tt> (deterministic and repeatable hash key randomization). Specifying <tt>&quot;PERL_PERTURB_KEYS&quot;</tt> explicitly to a different level overrides this behavior. </p>
<p> <i></i>Hash::Util::hash_seed()<i> now returns a string</i> </p>
<p> <code>Hash::Util::hash_seed()</code> now returns a string instead of an integer. This is to make the infrastructure support hash seeds of arbitrary lengths which might exceed that of an integer. (SipHash uses a 16 byte seed.) </p>
<p> <i>Output of </i><font SIZE="-1"><i>PERL_HASH_SEED_DEBUG</i></font><i> has been changed</i> </p>
<p> The environment variable <font SIZE="-1">PERL_HASH_SEED_DEBUG</font> now makes perl show both the hash function perl was built with, <i>and</i> the seed, in hex, in use for that process. Code parsing this output, should it exist, must change to accommodate the new format. Example of the new format: </p>
<pre>
    $ PERL_HASH_SEED_DEBUG=1 ./perl -e1
    HASH_FUNCTION = MURMUR3 HASH_SEED = 0x1476bb9f
</pre>
<h3>Upgrade to Unicode 6.2</h3>
<p> Perl now supports Unicode 6.2. A list of changes from Unicode 6.1 is at &lt;<a rel="nofollow" href="http://www.unicode.org/versions/Unicode6.2.0">http://www.unicode.org/versions/Unicode6.2.0</a>&gt;.</p>
<h3>Character name aliases may now include non-Latin1-range characters</h3>
<p> It is possible to define your own names for characters for use in <tt>&quot;\N{...}&quot;</tt>, <tt>&quot;charnames::vianame()&quot;</tt>, etc. These names can now be comprised of characters from the whole Unicode range. This allows for names to be in your native language, and not just English. Certain restrictions apply to the characters that may be used (you can&#8217;t define a name that has punctuation in it, for example). See &#8220;<font SIZE="-1">CUSTOM ALIASES&#8221;</font> in charnames.</p>
<h3>New DTrace probes</h3>
<p> The following new DTrace probes have been added:</p>
<dl>
<dt>&bull;</dt>
<dd> <tt>&quot;op-entry&quot;</tt></dd>
<dt>&bull;</dt>
<dd> <tt>&quot;loading-file&quot;</tt></dd>
<dt>&bull;</dt>
<dd> <tt>&quot;loaded-file&quot;</tt></dd></dl>
<h3>${^LAST_FH}</h3>
<p> This new variable provides access to the filehandle that was last read. This is the handle used by <tt>$.</tt> and by <tt>&quot;tell&quot;</tt> and <tt>&quot;eof&quot;</tt> without arguments.</p>
<h3>Regular Expression Set Operations</h3>
<p> This is an <code>experimental</code> feature to allow matching against the union, intersection, etc., of sets of code points, similar to Unicode::Regex::Set. It can also be used to extend <tt>&quot;/x&quot;</tt> processing to [bracketed] character classes, and as a replacement of user-defined properties, allowing more complex expressions than they do. See &#8220;Extended Bracketed Character Classes&#8221; in perlrecharclass.</p>
<h3>Lexical subroutines</h3>
<p> This new feature is still considered <code>experimental</code>. To enable it: </p>
<pre>
    use 5.018;
    no warnings &quot;experimental::lexical_subs&quot;;
    use feature &quot;lexical_subs&quot;;
</pre>
<p> You can now declare subroutines with <tt>&quot;state sub foo&quot;</tt>, <tt>&quot;my sub foo&quot;</tt>, and <tt>&quot;our sub foo&quot;</tt>. (<tt>&quot;state sub&quot;</tt> requires that the &#8220;state&#8221; feature be enabled, unless you write it as <tt>&quot;CORE::state sub foo&quot;</tt>.) </p>
<p> <tt>&quot;state sub&quot;</tt> creates a subroutine visible within the lexical scope in which it is declared. The subroutine is shared between calls to the outer sub. </p>
<p> <tt>&quot;my sub&quot;</tt> declares a lexical subroutine that is created each time the enclosing block is entered. <tt>&quot;state sub&quot;</tt> is generally slightly faster than <tt>&quot;my sub&quot;</tt>. </p>
<p> <tt>&quot;our sub&quot;</tt> declares a lexical alias to the package subroutine of the same name. </p>
<p> For more information, see &#8220;Lexical Subroutines&#8221; in perlsub.</p>
<h3>Computed Labels</h3>
<p> The loop controls <tt>&quot;next&quot;</tt>, <tt>&quot;last&quot;</tt> and <tt>&quot;redo&quot;</tt>, and the special <tt>&quot;dump&quot;</tt> operator, now allow arbitrary expressions to be used to compute labels at run time. Previously, any argument that was not a constant was treated as the empty string.</p>
<h3>More <font SIZE="-1">CORE::</font> subs</h3>
<p> Several more built-in functions have been added as subroutines to the <font SIZE="-1">CORE::</font> namespace &#8211; namely, those non-overridable keywords that can be implemented without custom parsers: <tt>&quot;defined&quot;</tt>, <tt>&quot;delete&quot;</tt>, <tt>&quot;exists&quot;</tt>, <tt>&quot;glob&quot;</tt>, <tt>&quot;pos&quot;</tt>, <tt>&quot;prototype&quot;</tt>, <tt>&quot;scalar&quot;</tt>, <tt>&quot;split&quot;</tt>, <tt>&quot;study&quot;</tt>, and <tt>&quot;undef&quot;</tt>. </p>
<p> As some of these have prototypes, <tt>&quot;prototype('CORE::...')&quot;</tt> has been changed to not make a distinction between overridable and non-overridable keywords. This is to make <tt>&quot;prototype('CORE::pos')&quot;</tt> consistent with <tt>&quot;prototype(&amp;CORE::pos)&quot;</tt>.</p>
<h3>kill with negative signal names</h3>
<p> <tt>&quot;kill&quot;</tt> has always allowed a negative signal number, which kills the process group instead of a single process. It has also allowed signal names. But it did not behave consistently, because negative signal names were treated as 0. Now negative signals names like <tt>&quot;-INT&quot;</tt> are supported and treated the same way as -2 [perl #112990].</p>
<h2>Security</h2>
<h3>See also: hash overhaul</h3>
<p> Some of the changes in the hash overhaul were made to enhance security. Please read that section.</p>
<h3>Storable security warning in documentation</h3>
<p> The documentation for <tt>&quot;Storable&quot;</tt> now includes a section which warns readers of the danger of accepting Storable documents from untrusted sources. The short version is that deserializing certain types of data can lead to loading modules and other code execution. This is documented behavior and wanted behavior, but this opens an attack vector for malicious entities.</p>
<h3>Locale::Maketext allowed code injection via a malicious template</h3>
<p> If users could provide a translation string to Locale::Maketext, this could be used to invoke arbitrary Perl subroutines available in the current process. </p>
<p> This has been fixed, but it is still possible to invoke any method provided by <tt>&quot;Locale::Maketext&quot;</tt> itself or a subclass that you are using. One of these methods in turn will invoke the Perl core&#8217;s <tt>&quot;sprintf&quot;</tt> subroutine. </p>
<p> In summary, allowing users to provide translation strings without auditing them is a bad idea. </p>
<p> This vulnerability is documented in <font SIZE="-1">CVE-2012-6329.</font></p>
<h3>Avoid calling memset with a negative count</h3>
<p> Poorly written perl code that allows an attacker to specify the count to perl&#8217;s <tt>&quot;x&quot;</tt> string repeat operator can already cause a memory exhaustion denial-of-service attack. A flaw in versions of perl before v5.15.5 can escalate that into a heap buffer overrun; coupled with versions of glibc before 2.16, it possibly allows the execution of arbitrary code. </p>
<p> The flaw addressed to this commit has been assigned identifier <font SIZE="-1">CVE-2012-5195</font> and was researched by Tim Brown.</p>
<h2>Incompatible Changes</h2>
<h3>See also: hash overhaul</h3>
<p> Some of the changes in the hash overhaul are not fully compatible with previous versions of perl. Please read that section.</p>
<h3>An unknown character name in \N{&#8230;} is now a syntax error</h3>
<p> Previously, it warned, and the Unicode <font SIZE="-1">REPLACEMENT CHARACTER</font> was substituted. Unicode now recommends that this situation be a syntax error. Also, the previous behavior led to some confusing warnings and behaviors, and since the <font SIZE="-1">REPLACEMENT CHARACTER</font> has no use other than as a stand-in for some unknown character, any code that has this problem is buggy.</p>
<h3>Formerly deprecated characters in \N{} character name aliases are now errors.</h3>
<p> Since v5.12.0, it has been deprecated to use certain characters in user-defined <tt>&quot;\N{...}&quot;</tt> character names. These now cause a syntax error. For example, it is now an error to begin a name with a digit, such as in </p>
<pre>
 my $undraftable = &quot;\N{4F}&quot;;    # Syntax error!
</pre>
<p> or to have commas anywhere in the name. See &#8220;<font SIZE="-1">CUSTOM ALIASES&#8221;</font> in charnames.</p>
<h3>\N{BELL} now refers to U+1F514 instead of U+0007</h3>
<p> Unicode 6.0 reused the name &#8220;<font SIZE="-1">BELL&#8221;</font> for a different code point than it traditionally had meant. Since Perl v5.14, use of this name still referred to U+0007, but would raise a deprecation warning. Now, &#8220;<font SIZE="-1">BELL&#8221;</font> refers to U+1F514, and the name for U+0007 is &#8220;<font SIZE="-1">ALERT&#8221;.</font> All the functions in charnames have been correspondingly updated.</p>
<h3>New Restrictions in Multi-Character Case-Insensitive Matching in Regular Expression Bracketed Character Classes</h3>
<p> Unicode has now withdrawn their previous recommendation for regular expressions to automatically handle cases where a single character can match multiple characters case-insensitively, for example, the letter <font SIZE="-1">LATIN SMALL LETTER SHARP S</font> and the sequence <tt>&quot;ss&quot;</tt>. This is because it turns out to be impracticable to do this correctly in all circumstances. Because Perl has tried to do this as best it can, it will continue to do so. (We are considering an option to turn it off.) However, a new restriction is being added on such matches when they occur in [bracketed] character classes. People were specifying things such as <tt>&quot;/[</tt>\0-\xff]/i&quot;</code>, and being surprised that it matches the two character sequence <code>&quot;ss&quot;</code> (since <font SIZE="-1">LATIN SMALL LETTER SHARP S</font> occurs in this range). This behavior is also inconsistent with using a property instead of a range: <code>&quot;\p{Block=Latin1}&quot;</code> also includes <font SIZE="-1">LATIN SMALL LETTER SHARP S,</font> but <code>&quot;/[\p{Block=Latin1}]/i&quot;</code> does not match <code>&quot;ss&quot;</code>. The new rule is that for there to be a multi-character case-insensitive match within a bracketed character class, the character must be explicitly listed, and not as an end point of a range. This more closely obeys the Principle of Least Astonishment. See ``Bracketed Character Classes&#8217;&#8216; in perlrecharclass. Note that a bug [perl #89774], now fixed as part of this change, prevented the previous behavior from working fully.  </p>
<h3>Explicit rules for variable names and identifiers</h3>
<p> Due to an oversight, single character variable names in v5.16 were completely unrestricted. This opened the door to several kinds of insanity. As of v5.18, these now follow the rules of other identifiers, in addition to accepting characters that match the <code>&quot;\p{POSIX_Punct}&quot;</code> property. </p>
<p> There is no longer any difference in the parsing of identifiers specified by using braces versus without braces. For instance, perl used to allow <code>&quot;${foo:bar}&quot;</code> (with a single colon) but not <code>$foo:bar</code>. Now that both are handled by a single code path, they are both treated the same way: both are forbidden. Note that this change is about the range of permissible literal identifiers, not other expressions.  </p>
<h3>Vertical tabs are now whitespace</h3>
<p> No one could recall why <code>&quot;\s&quot;</code> didn&#8217;t match <code>&quot;\cK&quot;</code>, the vertical tab. Now it does. Given the extreme rarity of that character, very little breakage is expected. That said, here&#8217;s what it means: </p>
<p> <code>&quot;\s&quot;</code> in a regex now matches a vertical tab in all circumstances. </p>
<p> Literal vertical tabs in a regex literal are ignored when the <code>&quot;/x&quot;</code> modifier is used. </p>
<p> Leading vertical tabs, alone or mixed with other whitespace, are now ignored when interpreting a string as a number. For example: </p>
<pre><code>  $dec = &quot; \cK \t 123&quot;;
  $hex = &quot; \cK \t 0xF&quot;;
  say 0 + $dec; # was 0 with warning, now 123
  say int $dec; # was 0, now 123
  say oct $hex; # was 0, now 15
</code></pre>
<h3>/(?{})/ and /(??{})/ have been heavily reworked</h3>
<p> The implementation of this feature has been almost completely rewritten. Although its main intent is to fix bugs, some behaviors, especially related to the scope of lexical variables, will have changed. This is described more fully in the ``Selected Bug Fixes&#8217;&#8216; section.  </p>
<h3>Stricter parsing of substitution replacement</h3>
<p> It is no longer possible to abuse the way the parser parses <code>&quot;s///e&quot;</code> like this: </p>
<pre><code>    %_=(_,&quot;Just another &quot;);
    $_=&quot;Perl hacker,\n&quot;;
    s//_}-&gt;{_/e;print
</code></pre>
<h3>given now aliases the global $_</h3>
<p> Instead of assigning to an implicit lexical <code>$_</code>, <code>&quot;given&quot;</code> now makes the global <code>$_</code> an alias for its argument, just like <code>&quot;foreach&quot;</code>. However, it still uses lexical <code>$_</code> if there is lexical <code>$_</code> in scope (again, just like <code>&quot;foreach&quot;</code>) [perl #114020].  </p>
<h3>The smartmatch family of features are now experimental</h3>
<p> Smart match, added in v5.10.0 and significantly revised in v5.10.1, has been a regular point of complaint. Although there are a number of ways in which it is useful, it has also proven problematic and confusing for both users and implementors of Perl. There have been a number of proposals on how to best address the problem. It is clear that smartmatch is almost certainly either going to change or go away in the future. Relying on its current behavior is not recommended. </p>
<p> Warnings will now be issued when the parser sees <code>&quot;~~&quot;</code>, <code>&quot;given&quot;</code>, or <code>&quot;when&quot;</code>. To disable these warnings, you can add this line to the appropriate scope: </p>
<pre><code>  no if $] &gt;= 5.018, warnings =&gt; &quot;experimental::smartmatch&quot;;
</code></pre>
<p> Consider, though, replacing the use of these features, as they may change behavior again before becoming stable.  </p>
<h3>Lexical $_ is now experimental</h3>
<p> Since it was introduced in Perl v5.10, it has caused much confusion with no obvious solution: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Various modules (e.g., List::Util) expect callback routines to use the global <code>$_</code>. <code>&quot;use List::Util &#8216;first&#8217;; my $_; first { $_ == 1 } @list&quot;</code> does not work as one would expect. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A <code>&quot;my $_&quot;</code> declaration earlier in the same file can cause confusing closure warnings. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The ``_&#8216;&#8216; subroutine prototype character allows called subroutines to access your lexical <code>$_</code>, so it is not really private after all. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Nevertheless, subroutines with a ``(@)&#8216;&#8216; prototype and methods cannot access the caller&#8217;s lexical <code>$_</code>, unless they are written in <font SIZE="-1">XS.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> But even <font SIZE="-1">XS</font> routines cannot access a lexical <code>$_</code> declared, not in the calling subroutine, but in an outer scope, iff that subroutine happened not to mention <code>$_</code> or use any operators that default to <code>$_</code>. </p>
 </dd></dl>
<p> It is our hope that lexical <code>$_</code> can be rehabilitated, but this may cause changes in its behavior. Please use it with caution until it becomes stable.  </p>
<code></code><h3>readline() with $/ = \N now reads N characters, not N bytes</h3>
<p> Previously, when reading from a stream with I/O layers such as <code>&quot;encoding&quot;</code>, the <code>readline()</code> function, otherwise known as the <code>&quot;&lt;&gt;&quot;</code> operator, would read <i>N</i> bytes from the top-most layer. [perl #79960] </p>
<p> Now, <i>N</i> characters are read instead. </p>
<p> There is no change in behaviour when reading from streams with no extra layers, since bytes map exactly to characters.  </p>
<h3>Overridden glob is now passed one argument</h3>
<p> <code>&quot;glob&quot;</code> overrides used to be passed a magical undocumented second argument that identified the caller. Nothing on <font SIZE="-1">CPAN</font> was using this, and it got in the way of a bug fix, so it was removed. If you really need to identify the caller, see Devel::Callsite on <font SIZE="-1">CPAN.</font>  </p>
<h3>Here doc parsing</h3>
<p> The body of a here document inside a quote-like operator now always begins on the line after the ``&lt;&lt;foo&#8217;&#8216; marker. Previously, it was documented to begin on the line following the containing quote-like operator, but that was only sometimes the case [perl #114040].  </p>
<h3>Alphanumeric operators must now be separated from the closing delimiter of regular expressions</h3>
<p> You may no longer write something like: </p>
<pre><code> m/a/and 1
</code></pre>
<p> Instead you must write </p>
<pre><code> m/a/ and 1
</code></pre>
<p> with whitespace separating the operator from the closing delimiter of the regular expression. Not having whitespace has resulted in a deprecation warning since Perl v5.14.0.  </p>
<h3>qw(...) can no longer be used as parentheses</h3>
<p> <code>&quot;qw&quot;</code> lists used to fool the parser into thinking they were always surrounded by parentheses. This permitted some surprising constructions such as <code>&quot;foreach $x qw(a b c) {...}&quot;</code>, which should really be written <code>&quot;foreach $x (qw(a b c)) {...}&quot;</code>. These would sometimes get the lexer into the wrong state, so they didn&#8217;t fully work, and the similar <code>&quot;foreach qw(a b c) {...}&quot;</code> that one might expect to be permitted never worked at all. </p>
<p> This side effect of <code>&quot;qw&quot;</code> has now been abolished. It has been deprecated since Perl v5.13.11. It is now necessary to use real parentheses everywhere that the grammar calls for them.  </p>
<h3>Interaction of lexical and default warnings</h3>
<p> Turning on any lexical warnings used first to disable all default warnings if lexical warnings were not already enabled: </p>
<pre><code>    $*; # deprecation warning
    use warnings &quot;void&quot;;
    $#; # void warning; no deprecation warning
</code></pre>
<p> Now, the <code>&quot;debugging&quot;</code>, <code>&quot;deprecated&quot;</code>, <code>&quot;glob&quot;</code>, <code>&quot;inplace&quot;</code> and <code>&quot;malloc&quot;</code> warnings categories are left on when turning on lexical warnings (unless they are turned off by <code>&quot;no warnings&quot;</code>, of course). </p>
<p> This may cause deprecation warnings to occur in code that used to be free of warnings. </p>
<p> Those are the only categories consisting only of default warnings. Default warnings in other categories are still disabled by <code>&quot;use warnings &quot;category&quot;&quot;</code>, as we do not yet have the infrastructure for controlling individual warnings.  </p>
<h3>state sub and our sub</h3>
<p> Due to an accident of history, <code>&quot;state sub&quot;</code> and <code>&quot;our sub&quot;</code> were equivalent to a plain <code>&quot;sub&quot;</code>, so one could even create an anonymous sub with <code>&quot;our sub { ... }&quot;</code>. These are now disallowed outside of the ``lexical_subs&#8217;&#8216; feature. Under the ``lexical_subs&#8217;&#8216; feature they have new meanings described in ``Lexical Subroutines&#8217;&#8216; in perlsub.  </p>
<h3>Defined values stored in environment are forced to byte strings</h3>
<p> A value stored in an environment variable has always been stringified when inherited by child processes. </p>
<p> In this release, when assigning to <code>%ENV</code>, values are immediately stringified, and converted to be only a byte string. </p>
<p> First, it is forced to be only a string. Then if the string is utf8 and the equivalent of <code>&quot;utf8::downgrade()&quot;</code> works, that result is used; otherwise, the equivalent of <code>&quot;utf8::encode()&quot;</code> is used, and a warning is issued about wide characters (``Diagnostics&#8217;&#8216;).  </p>
<h3>require dies for unreadable files</h3>
<p> When <code>&quot;require&quot;</code> encounters an unreadable file, it now dies. It used to ignore the file and continue searching the directories in <code>@INC</code> [perl #113422].  </p>
<font SIZE="-1"></font><h3>gv_fetchmeth_* and SUPER</h3>
<p> The various <code>&quot;gv_fetchmeth_*&quot;</code> <font SIZE="-1">XS</font> functions used to treat a package whose named ended with <code>&quot;::SUPER&quot;</code> specially. A method lookup on the <code>&quot;Foo::SUPER&quot;</code> package would be treated as a <code>&quot;SUPER&quot;</code> method lookup on the <code>&quot;Foo&quot;</code> package. This is no longer the case. To do a <code>&quot;SUPER&quot;</code> lookup, pass the <code>&quot;Foo&quot;</code> stash and the <code>&quot;GV_SUPER&quot;</code> flag.  </p>
<h3>split's first argument is more consistently interpreted</h3>
<p> After some changes earlier in v5.17, <code>&quot;split&quot;</code>&#8216;s behavior has been simplified: if the <font SIZE="-1">PATTERN</font> argument evaluates to a string containing one space, it is treated the way that a <i>literal</i> string containing one space once was.  </p>
<h2>Deprecations</h2>
<h3>Module removals</h3>
<p> The following modules will be removed from the core distribution in a future release, and will at that time need to be installed from <font SIZE="-1">CPAN.</font> Distributions on <font SIZE="-1">CPAN</font> which require these modules will need to list them as prerequisites. </p>
<p> The core versions of these modules will now issue <code>&quot;deprecated&quot;</code>-category warnings to alert you to this fact. To silence these deprecation warnings, install the modules in question from <font SIZE="-1">CPAN.</font> </p>
<p> Note that these are (with rare exceptions) fine modules that you are encouraged to continue to use. Their disinclusion from core primarily hinges on their necessity to bootstrapping a fully functional, CPAN-capable Perl installation, not usually on concerns over their design. </p>
<dl>
<dt>encoding</dt>
<dd> <p> The use of this pragma is now strongly discouraged. It conflates the encoding of source text with the encoding of I/O data, reinterprets escape sequences in source text (a questionable choice), and introduces the <font SIZE="-1">UTF-8</font> bug to all runtime handling of character strings. It is broken as designed and beyond repair. </p>
<p> For using non-ASCII literal characters in source text, please refer to utf8. For dealing with textual I/O data, please refer to Encode and open. </p>
 </dd>
<dt>Archive::Extract</dt>
<dd>  </dd>
<dt>B::Lint</dt>
<dd>  </dd>
<dt>B::Lint::Debug</dt>
<dd>  </dd>
<dt><font SIZE="-1">CPANPLUS</font> and all included &quot;CPANPLUS::*&quot; modules</dt>
<dd>  </dd>
<dt>Devel::InnerPackage</dt>
<dd>  </dd>
<dt>Log::Message</dt>
<dd>  </dd>
<dt>Log::Message::Config</dt>
<dd>  </dd>
<dt>Log::Message::Handlers</dt>
<dd>  </dd>
<dt>Log::Message::Item</dt>
<dd>  </dd>
<dt>Log::Message::Simple</dt>
<dd>  </dd>
<dt>Module::Pluggable</dt>
<dd>  </dd>
<dt>Module::Pluggable::Object</dt>
<dd>  </dd>
<dt>Object::Accessor</dt>
<dd>  </dd>
<dt>Pod::LaTeX</dt>
<dd>  </dd>
<dt>Term::UI</dt>
<dd>  </dd>
<dt>Term::UI::History</dt>
<dd>  </dd></dl>
<h3>Deprecated Utilities</h3>
<p> The following utilities will be removed from the core distribution in a future release as their associated modules have been deprecated. They will remain available with the applicable <font SIZE="-1">CPAN</font> distribution. </p>
<dl>
<dt>cpanp</dt>
<dd>  </dd>
<dt>&quot;cpanp-run-perl&quot;</dt>
<dd>  </dd>
<dt>cpan2dist</dt>
<dd> <p> These items are part of the <code>&quot;CPANPLUS&quot;</code> distribution. </p>
 </dd>
<dt>pod2latex</dt>
<dd> <p> This item is part of the <code>&quot;Pod::LaTeX&quot;</code> distribution. </p>
 </dd></dl>
<h3>PL_sv_objcount</h3>
<p> This interpreter-global variable used to track the total number of Perl objects in the interpreter. It is no longer maintained and will be removed altogether in Perl v5.20.  </p>
<h3>Five additional characters should be escaped in patterns with /x</h3>
<p> When a regular expression pattern is compiled with <code>&quot;/x&quot;</code>, Perl treats 6 characters as white space to ignore, such as <font SIZE="-1">SPACE</font> and <font SIZE="-1">TAB.</font> However, Unicode recommends 11 characters be treated thusly. We will conform with this in a future Perl version. In the meantime, use of any of the missing characters will raise a deprecation warning, unless turned off. The five characters are: </p>
<pre><code>    U+0085 NEXT LINE
    U+200E LEFT-TO-RIGHT MARK
    U+200F RIGHT-TO-LEFT MARK
    U+2028 LINE SEPARATOR
    U+2029 PARAGRAPH SEPARATOR
</code></pre>
<h3>User-defined charnames with surprising whitespace</h3>
<p> A user-defined character name with trailing or multiple spaces in a row is likely a typo. This now generates a warning when defined, on the assumption that uses of it will be unlikely to include the excess whitespace.  </p>
<h3>Various XS-callable functions are now deprecated</h3>
<p> All the functions used to classify characters will be removed from a future version of Perl, and should not be used. With participating C compilers (e.g., gcc), compiling any file that uses any of these will generate a warning. These were not intended for public use; there are equivalent, faster, macros for most of them. </p>
<p> See ``Character classes&#8217;&#8216; in perlapi. The complete list is: </p>
<p> <code>&quot;is_uni_alnum&quot;</code>, <code>&quot;is_uni_alnumc&quot;</code>, <code>&quot;is_uni_alnumc_lc&quot;</code>, <code>&quot;is_uni_alnum_lc&quot;</code>, <code>&quot;is_uni_alpha&quot;</code>, <code>&quot;is_uni_alpha_lc&quot;</code>, <code>&quot;is_uni_ascii&quot;</code>, <code>&quot;is_uni_ascii_lc&quot;</code>, <code>&quot;is_uni_blank&quot;</code>, <code>&quot;is_uni_blank_lc&quot;</code>, <code>&quot;is_uni_cntrl&quot;</code>, <code>&quot;is_uni_cntrl_lc&quot;</code>, <code>&quot;is_uni_digit&quot;</code>, <code>&quot;is_uni_digit_lc&quot;</code>, <code>&quot;is_uni_graph&quot;</code>, <code>&quot;is_uni_graph_lc&quot;</code>, <code>&quot;is_uni_idfirst&quot;</code>, <code>&quot;is_uni_idfirst_lc&quot;</code>, <code>&quot;is_uni_lower&quot;</code>, <code>&quot;is_uni_lower_lc&quot;</code>, <code>&quot;is_uni_print&quot;</code>, <code>&quot;is_uni_print_lc&quot;</code>, <code>&quot;is_uni_punct&quot;</code>, <code>&quot;is_uni_punct_lc&quot;</code>, <code>&quot;is_uni_space&quot;</code>, <code>&quot;is_uni_space_lc&quot;</code>, <code>&quot;is_uni_upper&quot;</code>, <code>&quot;is_uni_upper_lc&quot;</code>, <code>&quot;is_uni_xdigit&quot;</code>, <code>&quot;is_uni_xdigit_lc&quot;</code>, <code>&quot;is_utf8_alnum&quot;</code>, <code>&quot;is_utf8_alnumc&quot;</code>, <code>&quot;is_utf8_alpha&quot;</code>, <code>&quot;is_utf8_ascii&quot;</code>, <code>&quot;is_utf8_blank&quot;</code>, <code>&quot;is_utf8_char&quot;</code>, <code>&quot;is_utf8_cntrl&quot;</code>, <code>&quot;is_utf8_digit&quot;</code>, <code>&quot;is_utf8_graph&quot;</code>, <code>&quot;is_utf8_idcont&quot;</code>, <code>&quot;is_utf8_idfirst&quot;</code>, <code>&quot;is_utf8_lower&quot;</code>, <code>&quot;is_utf8_mark&quot;</code>, <code>&quot;is_utf8_perl_space&quot;</code>, <code>&quot;is_utf8_perl_word&quot;</code>, <code>&quot;is_utf8_posix_digit&quot;</code>, <code>&quot;is_utf8_print&quot;</code>, <code>&quot;is_utf8_punct&quot;</code>, <code>&quot;is_utf8_space&quot;</code>, <code>&quot;is_utf8_upper&quot;</code>, <code>&quot;is_utf8_xdigit&quot;</code>, <code>&quot;is_utf8_xidcont&quot;</code>, <code>&quot;is_utf8_xidfirst&quot;</code>. </p>
<p> In addition these three functions that have never worked properly are deprecated: <code>&quot;to_uni_lower_lc&quot;</code>, <code>&quot;to_uni_title_lc&quot;</code>, and <code>&quot;to_uni_upper_lc&quot;</code>.  </p>
<h3>Certain rare uses of backslashes within regexes are now deprecated</h3>
<p> There are three pairs of characters that Perl recognizes as metacharacters in regular expression patterns: <code>&quot;{}&quot;</code>, <code>&quot;[]&quot;</code>, and <code>&quot;()&quot;</code>. These can be used as well to delimit patterns, as in: </p>
<pre><code>  m{foo}
  s(foo)(bar)
</code></pre>
<p> Since they are metacharacters, they have special meaning to regular expression patterns, and it turns out that you can&#8217;t turn off that special meaning by the normal means of preceding them with a backslash, if you use them, paired, within a pattern delimited by them. For example, in </p>
<pre><code>  m{foo\{1,3\}}
</code></pre>
<p> the backslashes do not change the behavior, and this matches <code>&quot;f o&quot;</code> followed by one to three more occurrences of <code>&quot;o&quot;</code>. </p>
<p> Usages like this, where they are interpreted as metacharacters, are exceedingly rare; we think there are none, for example, in all of <font SIZE="-1">CPAN.</font> Hence, this deprecation should affect very little code. It does give notice, however, that any such code needs to change, which will in turn allow us to change the behavior in future Perl versions so that the backslashes do have an effect, and without fear that we are silently breaking any existing code.  </p>
<h3>Splitting the tokens (? and (* in regular expressions</h3>
<p> A deprecation warning is now raised if the <code>&quot;(&quot;</code> and <code>&quot;?&quot;</code> are separated by white space or comments in <code>&quot;(?...)&quot;</code> regular expression constructs. Similarly, if the <code>&quot;(&quot;</code> and <code>&quot;*&quot;</code> are separated in <code>&quot;(*VERB...)&quot;</code> constructs.  </p>
<font SIZE="-1"></font><h3>Pre-PerlIO IO implementations</h3>
<p> In theory, you can currently build perl without PerlIO. Instead, you&#8217;d use a wrapper around stdio or sfio. In practice, this isn&#8217;t very useful. It&#8217;s not well tested, and without any support for <font SIZE="-1">IO</font> layers or (thus) Unicode, it&#8217;s not much of a perl. Building without PerlIO will most likely be removed in the next version of perl. </p>
<p> PerlIO supports a <code>&quot;stdio&quot;</code> layer if stdio use is desired. Similarly a sfio layer could be produced in the future, if needed.  </p>
<h2>Future Deprecations</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> Platforms without support infrastructure </p>
<p> Both Windows <font SIZE="-1">CE</font> and z/OS have been historically under-maintained, and are currently neither successfully building nor regularly being smoke tested. Efforts are underway to change this situation, but it should not be taken for granted that the platforms are safe and supported. If they do not become buildable and regularly smoked, support for them may be actively removed in future releases. If you have an interest in these platforms and you can lend your time, expertise, or hardware to help support these platforms, please let the perl development effort know by emailing <code>&quot;perl5-porters [at] perl.org&quot;</code>. </p>
<p> Some platforms that appear otherwise entirely dead are also on the short list for removal between now and v5.20.0: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><font SIZE="-1">DG/UX</font></dt>
<dd>  </dd>
<dt>NeXT</dt>
<dd>  </dd></dl>
</dl>
<dl>
<dd> <p> We also think it likely that current versions of Perl will no longer build AmigaOS, <font SIZE="-1">DJGPP,</font> NetWare (natively), <font SIZE="-1">OS/2</font> and Plan 9. If you are using Perl on such a platform and have an interest in ensuring Perl&#8217;s future on them, please contact us. </p>
<p> We believe that Perl has long been unable to build on mixed endian architectures (such as PDP-11s), and intend to remove any remaining support code. Similarly, code supporting the long umaintained <font SIZE="-1">GNU</font> dld will be removed soon if no-one makes themselves known as an active user. </p>
 </dd></dl>
<dt>&bull;</dt>
<dd> <p> Swapping of $&lt; and $&gt; </p>
<p> Perl has supported the idiom of swapping $&lt; and $&gt; (and likewise $( and $)) to temporarily drop permissions since 5.0, like this: </p>
<pre><code>    ($&lt;, $&gt;) = ($&gt;, $&lt;);
</code></pre>
<p> However, this idiom modifies the real user/group id, which can have undesirable side-effects, is no longer useful on any platform perl supports and complicates the implementation of these variables and list assignment in general. </p>
<p> As an alternative, assignment only to <code>$&gt;</code> is recommended: </p>
<pre><code>    local $&gt; = $&lt;;
</code></pre>
<p> See also: Setuid Demystified &lt;<a rel="nofollow" href="http://www.cs.berkeley.edu/~daw/papers/setuid-usenix02.pdf">http://www.cs.berkeley.edu/~daw/papers/setuid-usenix02.pdf</a>&gt;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;microperl&quot;</code>, long broken and of unclear present purpose, will be removed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Revamping <code>&quot;\Q&quot;</code> semantics in double-quotish strings when combined with other escapes. </p>
<p> There are several bugs and inconsistencies involving combinations of <code>&quot;\Q&quot;</code> and escapes like <code>&quot;\x&quot;</code>, <code>&quot;\L&quot;</code>, etc., within a <code>&quot;\Q...\E&quot;</code> pair. These need to be fixed, and doing so will necessarily change current behavior. The changes have not yet been settled. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Use of <code>$x</code>, where <code>&quot;x&quot;</code> stands for any actual (non-printing) C0 control character will be disallowed in a future Perl version. Use <code>&quot;${x}&quot;</code> instead (where again <code>&quot;x&quot;</code> stands for a control character), or better, <code>$^A</code> , where <code>&quot;^&quot;</code> is a caret (<font SIZE="-1">CIRCUMFLEX ACCENT</font>), and <code>&quot;A&quot;</code> stands for any of the characters listed at the end of ``<font SIZE="-1">OPERATOR DIFFERENCES&#8217;&#8216;</font> in perlebcdic. </p>
 </dd></dl>
<h2>Performance Enhancements</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> Lists of lexical variable declarations (<code>&quot;my($x, $y)&quot;</code>) are now optimised down to a single op and are hence faster than before. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new C preprocessor define <code>&quot;NO_TAINT_SUPPORT&quot;</code> was added that, if set, disables Perl&#8217;s taint support altogether. Using the -T or -t command line flags will cause a fatal error. Beware that both core tests as well as many a <font SIZE="-1">CPAN</font> distribution&#8217;s tests will fail with this change. On the upside, it provides a small performance benefit due to reduced branching. </p>
<p> <code>Do not enable this unless you know exactly what you are getting yourself into.</code> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;pack&quot;</code> with constant arguments is now constant folded in most cases [perl #113470]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Speed up in regular expression matching against Unicode properties. The largest gain is for <code>&quot;\X&quot;</code>, the Unicode ``extended grapheme cluster.&#8216;&#8216; The gain for it is about 35% &#8211; 40%. Bracketed character classes, e.g., <code>&quot;[0-9\x{100}]&quot;</code> containing code points above 255 are also now faster. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On platforms supporting it, several former macros are now implemented as static inline functions. This should speed things up slightly on non-GCC platforms. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The optimisation of hashes in boolean context has been extended to affect <code>&quot;scalar(%hash)&quot;</code>, <code>&quot;%hash ? ... : ...&quot;</code>, and <code>&quot;sub { %hash || ... }&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Filetest operators manage the stack in a fractionally more efficient manner. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Globs used in a numeric context are now numified directly in most cases, rather than being numified via stringification. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;x&quot;</code> repetition operator is now folded to a single constant at compile time if called in scalar context with constant operands and no parentheses around the left operand. </p>
 </dd></dl>
<h2>Modules and Pragmata</h2>
<h3>New Modules and Pragmata</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Config::Perl::V version 0.16 has been added as a dual-lifed module. It provides structured data retrieval of <code>&quot;perl -V&quot;</code> output including information only known to the <code>&quot;perl&quot;</code> binary and not available via Config. </p>
 </dd></dl>
<h3>Updated Modules and Pragmata</h3>
<p> For a complete list of updates, run: </p>
<pre><code>  $ corelist --diff 5.16.0 5.18.0
</code></pre>
<p> You can substitute your favorite version in place of <code>5.16.0</code>, too. </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Archive::Extract has been upgraded to 0.68. </p>
<p> Work around an edge case on Linux with Busybox&#8217;s unzip. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Archive::Tar has been upgraded to 1.90. </p>
<p> ptar now supports the -T option as well as dashless options [rt.cpan.org #75473], [rt.cpan.org #75475]. </p>
<p> Auto-encode filenames marked as <font SIZE="-1">UTF-8</font> [rt.cpan.org #75474]. </p>
<p> Don&#8217;t use <code>&quot;tell&quot;</code> on IO::Zlib handles [rt.cpan.org #64339]. </p>
<p> Don&#8217;t try to <code>&quot;chown&quot;</code> on symlinks. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> autodie has been upgraded to 2.13. </p>
<p> <code>&quot;autodie&quot;</code> now plays nicely with the &#8216;open&#8217; pragma. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> B has been upgraded to 1.42. </p>
<p> The <code>&quot;stashoff&quot;</code> method of COPs has been added. This provides access to an internal field added in perl 5.16 under threaded builds [perl #113034]. </p>
<p> <code>&quot;B::COP::stashpv&quot;</code> now supports <font SIZE="-1">UTF-8</font> package names and embedded NULs. </p>
<p> All <code>&quot;CVf_*&quot;</code> and <code>&quot;GVf_*&quot;</code> and more SV-related flag values are now provided as constants in the <code>&quot;B::&quot;</code> namespace and available for export. The default export list has not changed. </p>
<p> This makes the module work with the new pad <font SIZE="-1">API.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> B::Concise has been upgraded to 0.95. </p>
<p> The <code>&quot;-nobanner&quot;</code> option has been fixed, and <code>&quot;format&quot;</code>s can now be dumped. When passed a sub name to dump, it will check also to see whether it is the name of a format. If a sub and a format share the same name, it will dump both. </p>
<p> This adds support for the new <code>&quot;OpMAYBE_TRUEBOOL&quot;</code> and <code>&quot;OPpTRUEBOOL&quot;</code> flags. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> B::Debug has been upgraded to 1.18. </p>
<p> This adds support (experimentally) for <code>&quot;B::PADLIST&quot;</code>, which was added in Perl 5.17.4. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> B::Deparse has been upgraded to 1.20. </p>
<p> Avoid warning when run under <code>&quot;perl -w&quot;</code>. </p>
<p> It now deparses loop controls with the correct precedence, and multiple statements in a <code>&quot;format&quot;</code> line are also now deparsed correctly. </p>
<p> This release suppresses trailing semicolons in formats. </p>
<p> This release adds stub deparsing for lexical subroutines. </p>
<p> It no longer dies when deparsing <code>&quot;sort&quot;</code> without arguments. It now correctly omits the comma for <code>&quot;system $prog @args&quot;</code> and <code>&quot;exec $prog @args&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> bignum, bigint and bigrat have been upgraded to 0.33. </p>
<p> The overrides for <code>&quot;hex&quot;</code> and <code>&quot;oct&quot;</code> have been rewritten, eliminating several problems, and making one incompatible change: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Formerly, whichever of <code>&quot;use bigint&quot;</code> or <code>&quot;use bigrat&quot;</code> was compiled later would take precedence over the other, causing <code>&quot;hex&quot;</code> and <code>&quot;oct&quot;</code> not to respect the other pragma when in scope. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Using any of these three pragmata would cause <code>&quot;hex&quot;</code> and <code>&quot;oct&quot;</code> anywhere else in the program to evaluate their arguments in list context and prevent them from inferring <code>$_</code> when called without arguments. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Using any of these three pragmata would make <code>&quot;oct(&quot;1234&quot;)&quot;</code> return 1234 (for any number not beginning with 0) anywhere in the program. Now ``1234&#8217;&#8216; is translated from octal to decimal, whether within the pragma&#8217;s scope or not. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The global overrides that facilitate lexical use of <code>&quot;hex&quot;</code> and <code>&quot;oct&quot;</code> now respect any existing overrides that were in place before the new overrides were installed, falling back to them outside of the scope of <code>&quot;use bignum&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;use bignum &quot;hex&quot;&quot;</code>, <code>&quot;use bignum &quot;oct&quot;&quot;</code> and similar invocations for bigint and bigrat now export a <code>&quot;hex&quot;</code> or <code>&quot;oct&quot;</code> function, instead of providing a global override. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>&bull;</dt>
<dd> <p> Carp has been upgraded to 1.29. </p>
<p> Carp is no longer confused when <code>&quot;caller&quot;</code> returns undef for a package that has been deleted. </p>
<p> The <code>&quot;longmess()&quot;</code> and <code>&quot;shortmess()&quot;</code> functions are now documented. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">CGI</font> has been upgraded to 3.63. </p>
<p> Unrecognized <font SIZE="-1">HTML</font> escape sequences are now handled better, problematic trailing newlines are no longer inserted after &lt;form&gt; tags by <code>&quot;startform()&quot;</code> or <code>&quot;start_form()&quot;</code>, and bogus ``Insecure Dependency&#8217;&#8216; warnings appearing with some versions of perl are now worked around. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Class::Struct has been upgraded to 0.64. </p>
<p> The constructor now respects overridden accessor methods [perl #29230]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Compress::Raw::Bzip2 has been upgraded to 2.060. </p>
<p> The misuse of Perl&#8217;s ``magic&#8217;&#8216; <font SIZE="-1">API</font> has been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Compress::Raw::Zlib has been upgraded to 2.060. </p>
<p> Upgrade bundled zlib to version 1.2.7. </p>
<p> Fix build failures on Irix, Solaris, and Win32, and also when building as C<font SIZE="-2">++</font> [rt.cpan.org #69985], [rt.cpan.org #77030], [rt.cpan.org #75222]. </p>
<p> The misuse of Perl&#8217;s ``magic&#8217;&#8216; <font SIZE="-1">API</font> has been fixed. </p>
<p> <code>&quot;compress()&quot;</code>, <code>&quot;uncompress()&quot;</code>, <code>&quot;memGzip()&quot;</code> and <code>&quot;memGunzip()&quot;</code> have been speeded up by making parameter validation more efficient. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> CPAN::Meta::Requirements has been upgraded to 2.122. </p>
<p> Treat undef requirements to <code>&quot;from_string_hash&quot;</code> as 0 (with a warning). </p>
<p> Added <code>&quot;requirements_for_module&quot;</code> method. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">CPANPLUS</font> has been upgraded to 0.9135. </p>
<p> Allow adding <i>blib/script</i> to <font SIZE="-1">PATH.</font> </p>
<p> Save the history between invocations of the shell. </p>
<p> Handle multiple <code>&quot;makemakerargs&quot;</code> and <code>&quot;makeflags&quot;</code> arguments better. </p>
<p> This resolves issues with the SQLite source engine. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Data::Dumper has been upgraded to 2.145. </p>
<p> It has been optimized to only build a seen-scalar hash as necessary, thereby speeding up serialization drastically. </p>
<p> Additional tests were added in order to improve statement, branch, condition and subroutine coverage. On the basis of the coverage analysis, some of the internals of Dumper.pm were refactored. Almost all methods are now documented. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> DB_File has been upgraded to 1.827. </p>
<p> The main Perl module no longer uses the <code>&quot;@_&quot;</code> construct. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Devel::Peek has been upgraded to 1.11. </p>
<p> This fixes compilation with C<font SIZE="-2">++</font> compilers and makes the module work with the new pad <font SIZE="-1">API.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Digest::MD5 has been upgraded to 2.52. </p>
<p> Fix <code>&quot;Digest::Perl::MD5&quot;</code> <font SIZE="-1">OO</font> fallback [rt.cpan.org #66634]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Digest::SHA has been upgraded to 5.84. </p>
<p> This fixes a double-free bug, which might have caused vulnerabilities in some cases. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> DynaLoader has been upgraded to 1.18. </p>
<p> This is due to a minor code change in the <font SIZE="-1">XS</font> for the <font SIZE="-1">VMS</font> implementation. </p>
<p> This fixes warnings about using <code>&quot;CODE&quot;</code> sections without an <code>&quot;OUTPUT&quot;</code> section. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Encode has been upgraded to 2.49. </p>
<p> The Mac alias x-mac-ce has been added, and various bugs have been fixed in Encode::Unicode, Encode::UTF7 and Encode::GSM0338. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Env has been upgraded to 1.04. </p>
<p> Its <font SIZE="-1">SPLICE</font> implementation no longer misbehaves in list context. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::CBuilder has been upgraded to 0.280210. </p>
<p> Manifest files are now correctly embedded for those versions of <font SIZE="-1">VC++</font> which make use of them. [perl #111782, #111798]. </p>
<p> A list of symbols to export can now be passed to <code>&quot;link()&quot;</code> when on Windows, as on other OSes [perl #115100]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ExtUtils::ParseXS has been upgraded to 3.18. </p>
<p> The generated C code now avoids unnecessarily incrementing <code>&quot;PL_amagic_generation&quot;</code> on Perl versions where it&#8217;s done automatically (or on current Perl where the variable no longer exists). </p>
<p> This avoids a bogus warning for initialised <font SIZE="-1">XSUB</font> non-parameters [perl #112776]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Copy has been upgraded to 2.26. </p>
<p> <code>&quot;copy()&quot;</code> no longer zeros files when copying into the same directory, and also now fails (as it has long been documented to do) when attempting to copy a file over itself. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::DosGlob has been upgraded to 1.10. </p>
<p> The internal cache of file names that it keeps for each caller is now freed when that caller is freed. This means <code>&quot;use File::DosGlob &#8216;glob&#8217;; eval &#8216;scalar &lt;*&gt;&#8216;&quot;</code> no longer leaks memory. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Fetch has been upgraded to 0.38. </p>
<p> Added the &#8216;file_default&#8217; option for URLs that do not have a file component. </p>
<p> Use <code>&quot;File::HomeDir&quot;</code> when available, and provide <code>&quot;PERL5_CPANPLUS_HOME&quot;</code> to override the autodetection. </p>
<p> Always re-fetch <i></i><font SIZE="-1"><i>CHECKSUMS</i></font><i></i> if <code>&quot;fetchdir&quot;</code> is set. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Find has been upgraded to 1.23. </p>
<p> This fixes inconsistent unixy path handling on <font SIZE="-1">VMS.</font> </p>
<p> Individual files may now appear in list of directories to be searched [perl #59750]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Glob has been upgraded to 1.20. </p>
<p> File::Glob has had exactly the same fix as File::DosGlob. Since it is what Perl&#8217;s own <code>&quot;glob&quot;</code> operator itself uses (except on <font SIZE="-1">VMS</font>), this means <code>&quot;eval &#8216;scalar &lt;*&gt;&#8216;&quot;</code> no longer leaks. </p>
<p> A space-separated list of patterns return long lists of results no longer results in memory corruption or crashes. This bug was introduced in Perl 5.16.0. [perl #114984] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Spec::Unix has been upgraded to 3.40. </p>
<p> <code>&quot;abs2rel&quot;</code> could produce incorrect results when given two relative paths or the root directory twice [perl #111510]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::stat has been upgraded to 1.07. </p>
<p> <code>&quot;File::stat&quot;</code> ignores the filetest pragma, and warns when used in combination therewith. But it was not warning for <code>&quot;-r&quot;</code>. This has been fixed [perl #111640]. </p>
<p> <code>&quot;-p&quot;</code> now works, and does not return false for pipes [perl #111638]. </p>
<p> Previously <code>&quot;File::stat&quot;</code>&#8216;s overloaded <code>&quot;-x&quot;</code> and <code>&quot;-X&quot;</code> operators did not give the correct results for directories or executable files when running as root. They had been treating executable permissions for root just like for any other user, performing group membership tests <i>etc</i> for files not owned by root. They now follow the correct Unix behaviour &#8211; for a directory they are always true, and for a file if any of the three execute permission bits are set then they report that root can execute the file. Perl&#8217;s builtin <code>&quot;-x&quot;</code> and <code>&quot;-X&quot;</code> operators have always been correct. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> File::Temp has been upgraded to 0.23 </p>
<p> Fixes various bugs involving directory removal. Defers unlinking tempfiles if the initial unlink fails, which fixes problems on <font SIZE="-1">NFS.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> GDBM_File has been upgraded to 1.15. </p>
<p> The undocumented optional fifth parameter to <code>&quot;TIEHASH&quot;</code> has been removed. This was intended to provide control of the callback used by <code>&quot;gdbm*&quot;</code> functions in case of fatal errors (such as filesystem problems), but did not work (and could never have worked). No code on <font SIZE="-1">CPAN</font> even attempted to use it. The callback is now always the previous default, <code>&quot;croak&quot;</code>. Problems on some platforms with how the <code>&quot;C&quot;</code> <code>&quot;croak&quot;</code> function is called have also been resolved. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Hash::Util has been upgraded to 0.15. </p>
<p> <code>&quot;hash_unlocked&quot;</code> and <code>&quot;hashref_unlocked&quot;</code> now returns true if the hash is unlocked, instead of always returning false [perl #112126]. </p>
<p> <code>&quot;hash_unlocked&quot;</code>, <code>&quot;hashref_unlocked&quot;</code>, <code>&quot;lock_hash_recurse&quot;</code> and <code>&quot;unlock_hash_recurse&quot;</code> are now exportable [perl #112126]. </p>
<p> Two new functions, <code>&quot;hash_locked&quot;</code> and <code>&quot;hashref_locked&quot;</code>, have been added. Oddly enough, these two functions were already exported, even though they did not exist [perl #112126]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> HTTP::Tiny has been upgraded to 0.025. </p>
<p> Add <font SIZE="-1">SSL</font> verification features [github #6], [github #9]. </p>
<p> Include the final <font SIZE="-1">URL</font> in the response hashref. </p>
<p> Add <code>&quot;local_address&quot;</code> option. </p>
<p> This improves <font SIZE="-1">SSL</font> support. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">IO</font> has been upgraded to 1.28. </p>
<p> <code>&quot;sync()&quot;</code> can now be called on read-only file handles [perl #64772]. </p>
<p> IO::Socket tries harder to cache or otherwise fetch socket information. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> IPC::Cmd has been upgraded to 0.80. </p>
<p> Use <code>&quot;POSIX::_exit&quot;</code> instead of <code>&quot;exit&quot;</code> in <code>&quot;run_forked&quot;</code> [rt.cpan.org #76901]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> IPC::Open3 has been upgraded to 1.13. </p>
<p> The <code>&quot;open3()&quot;</code> function no longer uses <code>&quot;POSIX::close()&quot;</code> to close file descriptors since that breaks the ref-counting of file descriptors done by PerlIO in cases where the file descriptors are shared by PerlIO streams, leading to attempts to close the file descriptors a second time when any such PerlIO streams are closed later on. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Locale::Codes has been upgraded to 3.25. </p>
<p> It includes some new codes. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Memoize has been upgraded to 1.03. </p>
<p> Fix the <code>&quot;MERGE&quot;</code> cache option. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Module::Build has been upgraded to 0.4003. </p>
<p> Fixed bug where modules without <code>$VERSION</code> might have a version of &#8216;0&#8217; listed in &#8216;provides&#8217; metadata, which will be rejected by <font SIZE="-1">PAUSE.</font> </p>
<p> Fixed bug in PodParser to allow numerals in module names. </p>
<p> Fixed bug where giving arguments twice led to them becoming arrays, resulting in install paths like <i></i><font SIZE="-1"><i></i>ARRAY</font><i>(0xdeadbeef)/lib/Foo.pm</i>. </p>
<p> A minor bug fix allows markup to be used around the leading ``Name&#8217;&#8216; in a <font SIZE="-1">POD</font> ``abstract&#8217;&#8216; line, and some documentation improvements have been made. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Module::CoreList has been upgraded to 2.90 </p>
<p> Version information is now stored as a delta, which greatly reduces the size of the <i>CoreList.pm</i> file. </p>
<p> This restores compatibility with older versions of perl and cleans up the corelist data for various modules. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Module::Load::Conditional has been upgraded to 0.54. </p>
<p> Fix use of <code>&quot;requires&quot;</code> on perls installed to a path with spaces. </p>
<p> Various enhancements include the new use of Module::Metadata. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Module::Metadata has been upgraded to 1.000011. </p>
<p> The creation of a Module::Metadata object for a typical module file has been sped up by about 40%, and some spurious warnings about <code>$VERSION</code>s have been suppressed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Module::Pluggable has been upgraded to 4.7. </p>
<p> Amongst other changes, triggers are now allowed on events, which gives a powerful way to modify behaviour. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Net::Ping has been upgraded to 2.41. </p>
<p> This fixes some test failures on Windows. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Opcode has been upgraded to 1.25. </p>
<p> Reflect the removal of the boolkeys opcode and the addition of the clonecv, introcv and padcv opcodes. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> overload has been upgraded to 1.22. </p>
<p> <code>&quot;no overload&quot;</code> now warns for invalid arguments, just like <code>&quot;use overload&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> PerlIO::encoding has been upgraded to 0.16. </p>
<p> This is the module implementing the ``:encoding(...)&#8216;&#8216; I/O layer. It no longer corrupts memory or crashes when the encoding back-end reallocates the buffer or gives it a typeglob or shared hash key scalar. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> PerlIO::scalar has been upgraded to 0.16. </p>
<p> The buffer scalar supplied may now only contain code points 0xFF or lower. [perl #109828] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl::OSType has been upgraded to 1.003. </p>
<p> This fixes a bug detecting the <font SIZE="-1">VOS</font> operating system. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pod::Html has been upgraded to 1.18. </p>
<p> The option <code>&quot;--libpods&quot;</code> has been reinstated. It is deprecated, and its use does nothing other than issue a warning that it is no longer supported. </p>
<p> Since the <font SIZE="-1">HTML</font> files generated by pod2html claim to have a <font SIZE="-1">UTF-8</font> charset, actually write the files out using <font SIZE="-1">UTF-8</font> [perl #111446]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pod::Simple has been upgraded to 3.28. </p>
<p> Numerous improvements have been made, mostly to Pod::Simple::XHTML, which also has a compatibility change: the <code>&quot;codes_in_verbatim&quot;</code> option is now disabled by default. See <i>cpan/Pod-Simple/ChangeLog</i> for the full details. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> re has been upgraded to 0.23 </p>
<p> Single character [class]es like <code>&quot;/[s]/&quot;</code> or <code>&quot;/[s]/i&quot;</code> are now optimized as if they did not have the brackets, i.e. <code>&quot;/s/&quot;</code> or <code>&quot;/s/i&quot;</code>. </p>
<p> See note about <code>&quot;op_comp&quot;</code> in the ``Internal Changes&#8217;&#8216; section below. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Safe has been upgraded to 2.35. </p>
<p> Fix interactions with <code>&quot;Devel::Cover&quot;</code>. </p>
<p> Don&#8217;t eval code under <code>&quot;no strict&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Scalar::Util has been upgraded to version 1.27. </p>
<p> Fix an overloading issue with <code>&quot;sum&quot;</code>. </p>
<p> <code>&quot;first&quot;</code> and <code>&quot;reduce&quot;</code> now check the callback first (so <code>&amp;<a href="/docs/linux/man/1-first/">first</a>(1)</code> is disallowed). </p>
<p> Fix <code>&quot;tainted&quot;</code> on magical values [rt.cpan.org #55763]. </p>
<p> Fix <code>&quot;sum&quot;</code> on previously magical values [rt.cpan.org #61118]. </p>
<p> Fix reading past the end of a fixed buffer [rt.cpan.org #72700]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Search::Dict has been upgraded to 1.07. </p>
<p> No longer require <code>&quot;stat&quot;</code> on filehandles. </p>
<p> Use <code>&quot;fc&quot;</code> for casefolding. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Socket has been upgraded to 2.009. </p>
<p> Constants and functions required for <font SIZE="-1">IP</font> multicast source group membership have been added. </p>
<p> <code>&quot;unpack_sockaddr_in()&quot;</code> and <code>&quot;unpack_sockaddr_in6()&quot;</code> now return just the <font SIZE="-1">IP</font> address in scalar context, and <code>&quot;inet_ntop()&quot;</code> now guards against incorrect length scalars being passed in. </p>
<p> This fixes an uninitialized memory read. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Storable has been upgraded to 2.41. </p>
<p> Modifying <code>$_[0]</code> within <code>&quot;STORABLE_freeze&quot;</code> no longer results in crashes [perl #112358]. </p>
<p> An object whose class implements <code>&quot;STORABLE_attach&quot;</code> is now thawed only once when there are multiple references to it in the structure being thawed [perl #111918]. </p>
<p> Restricted hashes were not always thawed correctly [perl #73972]. </p>
<p> Storable would croak when freezing a blessed <font SIZE="-1">REF</font> object with a <code>&quot;STORABLE_freeze()&quot;</code> method [perl #113880]. </p>
<p> It can now freeze and thaw vstrings correctly. This causes a slight incompatible change in the storage format, so the format version has increased to 2.9. </p>
<p> This contains various bugfixes, including compatibility fixes for older versions of Perl and vstring handling. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Sys::Syslog has been upgraded to 0.32. </p>
<p> This contains several bug fixes relating to <code>&quot;getservbyname()&quot;</code>, <code>&quot;setlogsock()&quot;</code>and log levels in <code>&quot;syslog()&quot;</code>, together with fixes for Windows, Haiku-OS and GNU/kFreeBSD. See <i>cpan/Sys-Syslog/Changes</i> for the full details. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Term::ANSIColor has been upgraded to 4.02. </p>
<p> Add support for italics. </p>
<p> Improve error handling. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Term::ReadLine has been upgraded to 1.10. This fixes the use of the <code>cpan</code> and <code>cpanp</code> shells on Windows in the event that the current drive happens to contain a <i>\dev\tty</i> file. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Test::Harness has been upgraded to 3.26. </p>
<p> Fix glob semantics on Win32 [rt.cpan.org #49732]. </p>
<p> Don&#8217;t use <code>&quot;Win32::GetShortPathName&quot;</code> when calling perl [rt.cpan.org #47890]. </p>
<p> Ignore -T when reading shebang [rt.cpan.org #64404]. </p>
<p> Handle the case where we don&#8217;t know the wait status of the test more gracefully. </p>
<p> Make the test summary &#8216;ok&#8217; line overridable so that it can be changed to a plugin to make the output of prove idempotent. </p>
<p> Don&#8217;t run world-writable files. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Text::Tabs and Text::Wrap have been upgraded to 2012.0818. Support for Unicode combining characters has been added to them both. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> threads::shared has been upgraded to 1.31. </p>
<p> This adds the option to warn about or ignore attempts to clone structures that can&#8217;t be cloned, as opposed to just unconditionally dying in that case. </p>
<p> This adds support for dual-valued values as created by Scalar::Util::dualvar. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Tie::StdHandle has been upgraded to 4.3. </p>
<p> <code>&quot;READ&quot;</code> now respects the offset argument to <code>&quot;read&quot;</code> [perl #112826]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Time::Local has been upgraded to 1.2300. </p>
<p> Seconds values greater than 59 but less than 60 no longer cause <code>&quot;timegm()&quot;</code> and <code>&quot;timelocal()&quot;</code> to croak. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unicode::UCD has been upgraded to 0.53. </p>
<p> This adds a function <code>all_casefolds()</code> that returns all the casefolds. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Win32 has been upgraded to 0.47. </p>
<p> New APIs have been added for getting and setting the current code page. </p>
 </dd></dl>
<h3>Removed Modules and Pragmata</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> Version::Requirements has been removed from the core distribution. It is available under a different name: CPAN::Meta::Requirements. </p>
 </dd></dl>
<h2>Documentation</h2>
<h3>Changes to Existing Documentation</h3>
<p> <i>perlcheat</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> perlcheat has been reorganized, and a few new sections were added. </p>
 </dd></dl>
<p> <i>perldata</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Now explicitly documents the behaviour of hash initializer lists that contain duplicate keys. </p>
 </dd></dl>
<p> <i>perldiag</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The explanation of symbolic references being prevented by ``strict refs&#8217;&#8216; now doesn&#8217;t assume that the reader knows what symbolic references are. </p>
 </dd></dl>
<p> <i>perlfaq</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> perlfaq has been synchronized with version 5.0150040 from <font SIZE="-1">CPAN.</font> </p>
 </dd></dl>
<p> <i>perlfunc</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The return value of <code>&quot;pipe&quot;</code> is now documented. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Clarified documentation of <code>&quot;our&quot;</code>. </p>
 </dd></dl>
<p> <i>perlop</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Loop control verbs (<code>&quot;dump&quot;</code>, <code>&quot;goto&quot;</code>, <code>&quot;next&quot;</code>, <code>&quot;last&quot;</code> and <code>&quot;redo&quot;</code>) have always had the same precedence as assignment operators, but this was not documented until now. </p>
 </dd></dl>
<p> <i>Diagnostics</i> </p>
<p> The following additions or changes have been made to diagnostic output, including warnings and fatal error messages. For the complete list of diagnostic messages, see perldiag.  </p>
<h3>New Diagnostics</h3>
<p> <i>New Errors</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Unterminated delimiter for here document </p>
<p> This message now occurs when a here document label has an initial quotation mark but the final quotation mark is missing. </p>
<p> This replaces a bogus and misleading error message about not finding the label itself [perl #114104]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> panic: child pseudo-process was never scheduled </p>
<p> This error is thrown when a child pseudo-process in the ithreads implementation on Windows was not scheduled within the time period allowed and therefore was not able to initialize properly [perl #88840]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Group name must start with a non-digit word character in regex; marked by &lt;-- <font SIZE="-1">HERE</font> in m/%s/ </p>
<p> This error has been added for <code>&quot;(?&amp;0)&quot;</code>, which is invalid. It used to produce an incomprehensible error message [perl #101666]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Can&#8217;t use an undefined value as a subroutine reference </p>
<p> Calling an undefined value as a subroutine now produces this error message. It used to, but was accidentally disabled, first in Perl 5.004 for non-magical variables, and then in Perl v5.14 for magical (e.g., tied) variables. It has now been restored. In the mean time, undef was treated as an empty string [perl #113576]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Experimental ``%s&#8217;&#8216; subs not enabled </p>
<p> To use lexical subs, you must first enable them: </p>
<pre><code>    no warnings 'experimental::lexical_subs';
    use feature 'lexical_subs';
    my sub foo { ... }
</code></pre>
 </dd></dl>
<p> <i>New Warnings</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> &#8216;Strings with code points over 0xFF may not be mapped into in-memory file handles&#8217; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> &#8216;%s&#8217; resolved to &#8216;\o{%s}%d&#8217; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> &#8216;Trailing white-space in a charnames alias definition is deprecated&#8217; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> &#8216;A sequence of multiple spaces in a charnames alias definition is deprecated&#8217; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> &#8216;Passing malformed <font SIZE="-1">UTF-8</font> to ``%s&#8217;&#8216; is deprecated&#8217; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Subroutine ``&amp;%s&#8217;&#8216; is not available </p>
<p> (W closure) During compilation, an inner named subroutine or eval is attempting to capture an outer lexical subroutine that is not currently available. This can happen for one of two reasons. First, the lexical subroutine may be declared in an outer anonymous subroutine that has not yet been created. (Remember that named subs are created at compile time, while anonymous subs are created at run-time.) For example, </p>
<pre><code>    sub { my sub a {...} sub f { \&amp;a } }
</code></pre>
<p> At the time that f is created, it can&#8217;t capture the current the ``a&#8217;&#8216; sub, since the anonymous subroutine hasn&#8217;t been created yet. Conversely, the following won&#8217;t give a warning since the anonymous subroutine has by now been created and is live: </p>
<pre><code>    sub { my sub a {...} eval 'sub f { \&amp;a }' }-&gt;();
</code></pre>
<p> The second situation is caused by an eval accessing a variable that has gone out of scope, for example, </p>
<pre><code>    sub f {
        my sub a {...}
        sub { eval '\&amp;a' }
    }
    f()-&gt;();
</code></pre>
<p> Here, when the &#8216;\&amp;a&#8217; in the eval is being compiled, f() is not currently being executed, so its &amp;a is not available for capture. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ``%s&#8217;&#8216; subroutine &amp;%s masks earlier declaration in same <code>%s</code> </p>
<p> (W misc) A ``my&#8217;&#8216; or ``state&#8217;&#8216; subroutine has been redeclared in the current scope or statement, effectively eliminating all access to the previous instance. This is almost always a typographical error. Note that the earlier subroutine will still exist until the end of the scope or until all closure references to it are destroyed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>%s</code> feature is experimental </p>
<p> (S experimental) This warning is emitted if you enable an experimental feature via <code>&quot;use feature&quot;</code>. Simply suppress the warning if you want to use the feature, but know that in doing so you are taking the risk of using an experimental feature which may change or be removed in a future Perl version: </p>
<pre><code>    no warnings &quot;experimental::lexical_subs&quot;;
    use feature &quot;lexical_subs&quot;;
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> sleep(%u) too large </p>
<p> (W overflow) You called <code>&quot;sleep&quot;</code> with a number that was larger than it can reliably handle and <code>&quot;sleep&quot;</code> probably slept for less time than requested. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Wide character in setenv </p>
<p> Attempts to put wide characters into environment variables via <code>%ENV</code> now provoke this warning. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> &quot;Invalid negative number (%s) in chr&quot; </p>
<p> <code>&quot;chr()&quot;</code> now warns when passed a negative value [perl #83048]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> &quot;Integer overflow in srand&quot; </p>
<p> <code>&quot;srand()&quot;</code> now warns when passed a value that doesn&#8217;t fit in a <code>&quot;UV&quot;</code> (since the value will be truncated rather than overflowing) [perl #40605]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> &quot;-i used with no filenames on the command line, reading from <font SIZE="-1">STDIN</font>&quot; </p>
<p> Running perl with the <code>&quot;-i&quot;</code> flag now warns if no input files are provided on the command line [perl #113410]. </p>
 </dd></dl>
<h3>Changes to Existing Diagnostics</h3>
<dl>
<dt>&bull;</dt>
<dd> <p> $* is no longer supported </p>
<p> The warning that use of <code>$*</code> and <code>$#</code> is no longer supported is now generated for every location that references them. Previously it would fail to be generated if another variable using the same typeglob was seen first (e.g. <code>&quot;@*&quot;</code> before <code>$*</code>), and would not be generated for the second and subsequent uses. (It&#8217;s hard to fix the failure to generate warnings at all without also generating them every time, and warning every time is consistent with the warnings that <code>$[</code> used to generate.) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The warnings for <code>&quot;\b{&quot;</code> and <code>&quot;\B{&quot;</code> were added. They are a deprecation warning which should be turned off by that category. One should not have to turn off regular regexp warnings as well to get rid of these. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Constant(%s): Call to &amp;{$^H{%s}} did not return a defined value </p>
<p> Constant overloading that returns <code>&quot;undef&quot;</code> results in this error message. For numeric constants, it used to say ``Constant(undef)&#8216;&#8216;. ``undef&#8217;&#8216; has been replaced with the number itself. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The error produced when a module cannot be loaded now includes a hint that the module may need to be installed: ``Can&#8217;t locate hopping.pm in <code>@INC</code> (you may need to install the hopping module) (@INC contains: ...)&#8216;&#8216; </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> vector argument not supported with alpha versions </p>
<p> This warning was not suppressible, even with <code>&quot;no warnings&quot;</code>. Now it is suppressible, and has been moved from the ``internal&#8217;&#8216; category to the ``printf&#8217;&#8216; category. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;Can&#8217;t do {n,m} with n &gt; m in regex; marked by &lt;-- HERE in m/%s/&quot;</code> </p>
<p> This fatal error has been turned into a warning that reads: </p>
<p> Quantifier {n,m} with n &gt; m can&#8217;t match in regex </p>
<p> (W regexp) Minima should be less than or equal to maxima. If you really want your regexp to match something 0 times, just put {0}. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The ``Runaway prototype&#8217;&#8216; warning that occurs in bizarre cases has been removed as being unhelpful and inconsistent. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The ``Not a format reference&#8217;&#8216; error has been removed, as the only case in which it could be triggered was a bug. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The ``Unable to create sub named <code>%s</code>&#8216;&#8216; error has been removed for the same reason. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The &#8216;Can&#8217;t use ``my <code>%s</code>&#8216;&#8216; in sort comparison&#8217; error has been downgraded to a warning, &#8216;``my <code>%s</code>&#8216;&#8216; used in sort comparison&#8217; (with &#8216;state&#8217; instead of &#8216;my&#8217; for state variables). In addition, the heuristics for guessing whether lexical <code>$a</code> or <code>$b</code> has been misused have been improved to generate fewer false positives. Lexical <code>$a</code> and <code>$b</code> are no longer disallowed if they are outside the sort block. Also, a named unary or list operator inside the sort block no longer causes the <code>$a</code> or <code>$b</code> to be ignored [perl #86136]. </p>
 </dd></dl>
<h2>Utility Changes</h2>
<p> <i>h2xs</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> <i>h2xs</i> no longer produces invalid code for empty defines. [perl #20636] </p>
 </dd></dl>
<h2>Configuration and Compilation</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> Added <code>&quot;useversionedarchname&quot;</code> option to Configure </p>
<p> When set, it includes &#8216;api_versionstring&#8217; in &#8216;archname&#8217;. E.g. x86_64-linux-5.13.6-thread-multi. It is unset by default. </p>
<p> This feature was requested by Tim Bunce, who observed that <code>&quot;INSTALL_BASE&quot;</code> creates a library structure that does not differentiate by perl version. Instead, it places architecture specific files in ``$install_base/lib/perl5/$archname&#8217;&#8216;. This makes it difficult to use a common <code>&quot;INSTALL_BASE&quot;</code> library path with multiple versions of perl. </p>
<p> By setting <code>&quot;-Duseversionedarchname&quot;</code>, the <code>$archname</code> will be distinct for architecture <i>and</i> <font SIZE="-1">API</font> version, allowing mixed use of <code>&quot;INSTALL_BASE&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Add a <code>&quot;PERL_NO_INLINE_FUNCTIONS&quot;</code> option </p>
<p> If <code>&quot;PERL_NO_INLINE_FUNCTIONS&quot;</code> is defined, don&#8217;t include ``inline.h&#8217;&#8216; </p>
<p> This permits test code to include the perl headers for definitions without creating a link dependency on the perl library (which may not exist yet). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Configure will honour the external <code>&quot;MAILDOMAIN&quot;</code> environment variable, if set. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;installman&quot;</code> no longer ignores the silent option </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Both <code>&quot;META.yml&quot;</code> and <code>&quot;META.json&quot;</code> files are now included in the distribution. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <i>Configure</i> will now correctly detect <code>&quot;isblank()&quot;</code> when compiling with a C<font SIZE="-2">++</font> compiler. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The pager detection in <i>Configure</i> has been improved to allow responses which specify options after the program name, e.g. <code>/usr/bin/less -R</code>, if the user accepts the default value. This helps <code>perldoc</code> when handling <font SIZE="-1">ANSI</font> escapes [perl #72156]. </p>
 </dd></dl>
<h2>Testing</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> The test suite now has a section for tests that require very large amounts of memory. These tests won&#8217;t run by default; they can be enabled by setting the <code>&quot;PERL_TEST_MEMORY&quot;</code> environment variable to the number of gibibytes of memory that may be safely used. </p>
 </dd></dl>
<h2>Platform Support</h2>
<h3>Discontinued Platforms</h3>
<dl>
<dt>BeOS</dt>
<dd> <p> BeOS was an operating system for personal computers developed by Be Inc, initially for their BeBox hardware. The <font SIZE="-1">OS</font> Haiku was written as an open source replacement for/continuation of BeOS, and its perl port is current and actively maintained. </p>
 </dd>
<dt><font SIZE="-1">UTS</font> Global</dt>
<dd> <p> Support code relating to <font SIZE="-1">UTS</font> global has been removed. <font SIZE="-1">UTS</font> was a mainframe version of System V created by Amdahl, subsequently sold to <font SIZE="-1">UTS</font> Global. The port has not been touched since before Perl v5.8.0, and <font SIZE="-1">UTS</font> Global is now defunct. </p>
 </dd>
<dt><font SIZE="-1">VM/ESA</font></dt>
<dd> <p> Support for <font SIZE="-1">VM/ESA</font> has been removed. The port was tested on 2.3.0, which <font SIZE="-1">IBM</font> ended service on in March 2002. 2.4.0 ended service in June 2003, and was superseded by Z/VM. The current version of Z/VM is V6.2.0, and scheduled for end of service on 2015/04/30. </p>
 </dd>
<dt><font SIZE="-1">MPE/IX</font></dt>
<dd> <p> Support for <font SIZE="-1">MPE/IX</font> has been removed. </p>
 </dd>
<dt><font SIZE="-1">EPOC</font></dt>
<dd> <p> Support code relating to <font SIZE="-1">EPOC</font> has been removed. <font SIZE="-1">EPOC</font> was a family of operating systems developed by Psion for mobile devices. It was the predecessor of Symbian. The port was last updated in April 2002. </p>
 </dd>
<dt>Rhapsody</dt>
<dd> <p> Support for Rhapsody has been removed. </p>
 </dd></dl>
<h3>Platform-Specific Notes</h3>
<p> <i></i><font SIZE="-1"><i>AIX</i></font><i></i> </p>
<p> Configure now always adds <code>&quot;-qlanglvl=extc99&quot;</code> to the <font SIZE="-1">CC</font> flags on <font SIZE="-1">AIX</font> when using xlC. This will make it easier to compile a number of XS-based modules that assume C99 [perl #113778]. </p>
<p> <i>clang++</i> </p>
<p> There is now a workaround for a compiler bug that prevented compiling with clang++ since Perl v5.15.7 [perl #112786]. </p>
<p> <i>C<font SIZE="-2">++</font></i> </p>
<p> When compiling the Perl core as C<font SIZE="-2">++</font> (which is only semi-supported), the mathom functions are now compiled as <code>&quot;extern &quot;C&quot;&quot;</code>, to ensure proper binary compatibility. (However, binary compatibility isn&#8217;t generally guaranteed anyway in the situations where this would matter.) </p>
<p> <i>Darwin</i> </p>
<p> Stop hardcoding an alignment on 8 byte boundaries to fix builds using -Dusemorebits. </p>
<p> <i>Haiku</i> </p>
<p> Perl should now work out of the box on Haiku R1 Alpha 4. </p>
<p> <i>MidnightBSD</i> </p>
<p> <code>&quot;libc_r&quot;</code> was removed from recent versions of MidnightBSD and older versions work better with <code>&quot;pthread&quot;</code>. Threading is now enabled using <code>&quot;pthread&quot;</code> which corrects build errors with threading enabled on 0.4-CURRENT. </p>
<p> <i>Solaris</i> </p>
<p> In Configure, avoid running sed commands with flags not supported on Solaris. </p>
<p> <i></i><font SIZE="-1"><i>VMS</i></font><i></i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Where possible, the case of filenames and command-line arguments is now preserved by enabling the <font SIZE="-1">CRTL</font> features <code>&quot;DECC$EFS_CASE_PRESERVE&quot;</code> and <code>&quot;DECC$ARGV_PARSE_STYLE&quot;</code> at start-up time. The latter only takes effect when extended parse is enabled in the process from which Perl is run. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The character set for Extended Filename Syntax (<font SIZE="-1">EFS</font>) is now enabled by default on <font SIZE="-1">VMS.</font> Among other things, this provides better handling of dots in directory names, multiple dots in filenames, and spaces in filenames. To obtain the old behavior, set the logical name <code>&quot;DECC$EFS_CHARSET&quot;</code> to <code>&quot;DISABLE&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed linking on builds configured with <code>&quot;-Dusemymalloc=y&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Experimental support for building Perl with the <font SIZE="-1">HP C<font SIZE="-2">++</font></font> compiler is available by configuring with <code>&quot;-Dusecxx&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> All C header files from the top-level directory of the distribution are now installed on <font SIZE="-1">VMS,</font> providing consistency with a long-standing practice on other platforms. Previously only a subset were installed, which broke non-core extension builds for extensions that depended on the missing include files. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Quotes are now removed from the command verb (but not the parameters) for commands spawned via <code>&quot;system&quot;</code>, backticks, or a piped <code>&quot;open&quot;</code>. Previously, quotes on the verb were passed through to <font SIZE="-1">DCL,</font> which would fail to recognize the command. Also, if the verb is actually a path to an image or command procedure on an <font SIZE="-1">ODS-5</font> volume, quoting it now allows the path to contain spaces. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>a2p</code> build has been fixed for the <font SIZE="-1">HP C<font SIZE="-2">++</font></font> compiler on OpenVMS. </p>
 </dd></dl>
<p> <i>Win32</i> </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Perl can now be built using Microsoft&#8217;s Visual C<font SIZE="-2">++</font> 2012 compiler by specifying CCTYPE=MSVC110 (or <font SIZE="-1">MSVC110FREE</font> if you are using the free Express edition for Windows Desktop) in <i>win32/Makefile</i>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The option to build without <code>&quot;USE_SOCKETS_AS_HANDLES&quot;</code> has been removed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Fixed a problem where perl could crash while cleaning up threads (including the main thread) in threaded debugging builds on Win32 and possibly other platforms [perl #114496]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A rare race condition that would lead to sleep taking more time than requested, and possibly even hanging, has been fixed [perl #33096]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;link&quot;</code> on Win32 now attempts to set <code>$!</code> to more appropriate values based on the Win32 <font SIZE="-1">API</font> error code. [perl #112272] </p>
<p> Perl no longer mangles the environment block, e.g. when launching a new sub-process, when the environment contains non-ASCII characters. Known problems still remain, however, when the environment contains characters outside of the current <font SIZE="-1">ANSI</font> codepage (e.g. see the item about Unicode in <code>%ENV</code> in &lt;<a rel="nofollow" href="http://perl5.git.perl.org/perl.git/blob/HEAD:/Porting/todo.pod">http://perl5.git.perl.org/perl.git/blob/HEAD:/Porting/todo.pod</a>&gt;). [perl #113536] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Building perl with some Windows compilers used to fail due to a problem with miniperl&#8217;s <code>&quot;glob&quot;</code> operator (which uses the <code>&quot;perlglob&quot;</code> program) deleting the <font SIZE="-1">PATH</font> environment variable [perl #113798]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new makefile option, <code>&quot;USE_64_BIT_INT&quot;</code>, has been added to the Windows makefiles. Set this to ``define&#8217;&#8216; when building a 32-bit perl if you want it to use 64-bit integers. </p>
<p> Machine code size reductions, already made to the DLLs of <font SIZE="-1">XS</font> modules in Perl v5.17.2, have now been extended to the perl <font SIZE="-1">DLL</font> itself. </p>
<p> Building with <font SIZE="-1">VC++ 6.0</font> was inadvertently broken in Perl v5.17.2 but has now been fixed again. </p>
 </dd></dl>
<p> <i>WinCE</i> </p>
<p> Building on WinCE is now possible once again, although more work is required to fully restore a clean build.  </p>
<h2>Internal Changes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> Synonyms for the misleadingly named <code>&quot;av_len()&quot;</code> have been created: <code>&quot;av_top_index()&quot;</code> and <code>&quot;av_tindex&quot;</code>. All three of these return the number of the highest index in the array, not the number of elements it contains. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>SvUPGRADE()</code> is no longer an expression. Originally this macro (and its underlying function, <code>sv_upgrade()</code>) were documented as boolean, although in reality they always croaked on error and never returned false. In 2005 the documentation was updated to specify a void return value, but <code>SvUPGRADE()</code> was left always returning 1 for backwards compatibility. This has now been removed, and <code>SvUPGRADE()</code> is now a statement with no return value. </p>
<p> So this is now a syntax error: </p>
<pre><code>    if (!SvUPGRADE(sv)) { croak(...); }
</code></pre>
<p> If you have code like that, simply replace it with </p>
<pre><code>    SvUPGRADE(sv);
</code></pre>
<p> or to avoid compiler warnings with older perls, possibly </p>
<pre><code>    (void)SvUPGRADE(sv);
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl has a new copy-on-write mechanism that allows any SvPOK scalar to be upgraded to a copy-on-write scalar. A reference count on the string buffer is stored in the string buffer itself. This feature is <code>not enabled by default</code>. </p>
<p> It can be enabled in a perl build by running <i>Configure</i> with <code>-Accflags=-DPERL_NEW_COPY_ON_WRITE</code>, and we would encourage <font SIZE="-1">XS</font> authors to try their code with such an enabled perl, and provide feedback. Unfortunately, there is not yet a good guide to updating <font SIZE="-1">XS</font> code to cope with <font SIZE="-1">COW.</font> Until such a document is available, consult the perl5-porters mailing list. </p>
<p> It breaks a few <font SIZE="-1">XS</font> modules by allowing copy-on-write scalars to go through code paths that never encountered them before. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Copy-on-write no longer uses the SvFAKE and SvREADONLY flags. Hence, SvREADONLY indicates a true read-only <font SIZE="-1">SV.</font> </p>
<p> Use the SvIsCOW macro (as before) to identify a copy-on-write scalar. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;PL_glob_index&quot;</code> is gone. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The private Perl_croak_no_modify has had its context parameter removed. It is now has a void prototype. Users of the public <font SIZE="-1">API</font> croak_no_modify remain unaffected. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Copy-on-write (shared hash key) scalars are no longer marked read-only. <code>&quot;SvREADONLY&quot;</code> returns false on such an <font SIZE="-1">SV,</font> but <code>&quot;SvIsCOW&quot;</code> still returns true. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new op type, <code>&quot;OP_PADRANGE&quot;</code> has been introduced. The perl peephole optimiser will, where possible, substitute a single padrange op for a pushmark followed by one or more pad ops, and possibly also skipping list and nextstate ops. In addition, the op can carry out the tasks associated with the <font SIZE="-1">RHS</font> of a <code>&quot;my(...) = @_&quot;</code> assignment, so those ops may be optimised away too. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Case-insensitive matching inside a [bracketed] character class with a multi-character fold no longer excludes one of the possibilities in the circumstances that it used to. [perl #89774]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;PL_formfeed&quot;</code> has been removed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The regular expression engine no longer reads one byte past the end of the target string. While for all internally well-formed scalars this should never have been a problem, this change facilitates clever tricks with string buffers in <font SIZE="-1">CPAN</font> modules. [perl #73542] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Inside a <font SIZE="-1">BEGIN</font> block, <code>&quot;PL_compcv&quot;</code> now points to the currently-compiling subroutine, rather than the <font SIZE="-1">BEGIN</font> block itself. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;mg_length&quot;</code> has been deprecated. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;sv_len&quot;</code> now always returns a byte count and <code>&quot;sv_len_utf8&quot;</code> a character count. Previously, <code>&quot;sv_len&quot;</code> and <code>&quot;sv_len_utf8&quot;</code> were both buggy and would sometimes returns bytes and sometimes characters. <code>&quot;sv_len_utf8&quot;</code> no longer assumes that its argument is in <font SIZE="-1">UTF-8.</font> Neither of these creates <font SIZE="-1">UTF-8</font> caches for tied or overloaded values or for non-PVs any more. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;sv_mortalcopy&quot;</code> now copies string buffers of shared hash key scalars when called from <font SIZE="-1">XS</font> modules [perl #79824]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The new <code>&quot;RXf_MODIFIES_VARS&quot;</code> flag can be set by custom regular expression engines to indicate that the execution of the regular expression may cause variables to be modified. This lets <code>&quot;s///&quot;</code> know to skip certain optimisations. Perl&#8217;s own regular expression engine sets this flag for the special backtracking verbs that set <code>$REGMARK</code> and <code>$REGERROR</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The APIs for accessing lexical pads have changed considerably. </p>
<p> <code>&quot;PADLIST&quot;</code>s are now longer <code>&quot;AV&quot;</code>s, but their own type instead. <code>&quot;PADLIST&quot;</code>s now contain a <code>&quot;PAD&quot;</code> and a <code>&quot;PADNAMELIST&quot;</code> of <code>&quot;PADNAME&quot;</code>s, rather than <code>&quot;AV&quot;</code>s for the pad and the list of pad names. <code>&quot;PAD&quot;</code>s, <code>&quot;PADNAMELIST&quot;</code>s, and <code>&quot;PADNAME&quot;</code>s are to be accessed as such through the newly added pad <font SIZE="-1">API</font> instead of the plain <code>&quot;AV&quot;</code> and <code>&quot;SV&quot;</code> APIs. See perlapi for details. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In the regex <font SIZE="-1">API,</font> the numbered capture callbacks are passed an index indicating what match variable is being accessed. There are special index values for the <code>&quot;$`, $&amp;, $&amp;&quot;</code> variables. Previously the same three values were used to retrieve <code>&quot;${^PREMATCH}, ${^MATCH}, ${^POSTMATCH}&quot;</code> too, but these have now been assigned three separate values. See ``Numbered capture callbacks&#8217;&#8216; in perlreapi. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;PL_sawampersand&quot;</code> was previously a boolean indicating that any of <code>&quot;$`, $&amp;, $&amp;&quot;</code> had been seen; it now contains three one-bit flags indicating the presence of each of the variables individually. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;CV *&quot;</code> typemap entry now supports <code>&quot;&amp;{}&quot;</code> overloading and typeglobs, just like <code>&quot;&amp;{...}&quot;</code> [perl #96872]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;SVf_AMAGIC&quot;</code> flag to indicate overloading is now on the stash, not the object. It is now set automatically whenever a method or <code>@ISA</code> changes, so its meaning has changed, too. It now means ``potentially overloaded&#8217;&#8216;. When the overload table is calculated, the flag is automatically turned off if there is no overloading, so there should be no noticeable slowdown. </p>
<p> The staleness of the overload tables is now checked when overload methods are invoked, rather than during <code>&quot;bless&quot;</code>. </p>
<p> ``A&#8217;&#8216; magic is gone. The changes to the handling of the <code>&quot;SVf_AMAGIC&quot;</code> flag eliminate the need for it. </p>
<p> <code>&quot;PL_amagic_generation&quot;</code> has been removed as no longer necessary. For <font SIZE="-1">XS</font> modules, it is now a macro alias to <code>&quot;PL_na&quot;</code>. </p>
<p> The fallback overload setting is now stored in a stash entry separate from overloadedness itself. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The character-processing code has been cleaned up in places. The changes should be operationally invisible. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;study&quot;</code> function was made a no-op in v5.16. It was simply disabled via a <code>&quot;return&quot;</code> statement; the code was left in place. Now the code supporting what <code>&quot;study&quot;</code> used to do has been removed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Under threaded perls, there is no longer a separate <font SIZE="-1">PV</font> allocated for every <font SIZE="-1">COP</font> to store its package name (<code>&quot;cop-&gt;stashpv&quot;</code>). Instead, there is an offset (<code>&quot;cop-&gt;stashoff&quot;</code>) into the new <code>&quot;PL_stashpad&quot;</code> array, which holds stash pointers. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In the pluggable regex <font SIZE="-1">API,</font> the <code>&quot;regexp_engine&quot;</code> struct has acquired a new field <code>&quot;op_comp&quot;</code>, which is currently just for perl&#8217;s internal use, and should be initialized to <font SIZE="-1">NULL</font> by other regex plugin modules. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A new function <code>&quot;alloccopstash&quot;</code> has been added to the <font SIZE="-1">API,</font> but is considered experimental. See perlapi. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl used to implement get magic in a way that would sometimes hide bugs in code that could call <code>mg_get()</code> too many times on magical values. This hiding of errors no longer occurs, so long-standing bugs may become visible now. If you see magic-related errors in <font SIZE="-1">XS</font> code, check to make sure it, together with the Perl <font SIZE="-1">API</font> functions it uses, calls <code>mg_get()</code> only once on <code>SvGMAGICAL()</code> values. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <font SIZE="-1">OP</font> allocation for CVs now uses a slab allocator. This simplifies memory management for OPs allocated to a <font SIZE="-1">CV,</font> so cleaning up after a compilation error is simpler and safer [perl #111462][perl #112312]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;PERL_DEBUG_READONLY_OPS&quot;</code> has been rewritten to work with the new slab allocator, allowing it to catch more violations than before. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The old slab allocator for ops, which was only enabled for <code>&quot;PERL_IMPLICIT_SYS&quot;</code> and <code>&quot;PERL_DEBUG_READONLY_OPS&quot;</code>, has been retired. </p>
 </dd></dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> Here document terminators no longer require a terminating newline character when they occur at the end of a file. This was already the case at the end of a string eval [perl #65838]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;-DPERL_GLOBAL_STRUCT&quot;</code> builds now free the global struct <code>after</code> they&#8217;ve finished using it. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A trailing &#8216;/&#8216; on a path in <code>@INC</code> will no longer have an additional &#8216;/&#8216; appended. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;:crlf&quot;</code> layer now works when unread data doesn&#8217;t fit into its own buffer. [perl #112244]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;ungetc()&quot;</code> now handles <font SIZE="-1">UTF-8</font> encoded data. [perl #116322]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A bug in the core typemap caused any C types that map to the T_BOOL core typemap entry to not be set, updated, or modified when the T_BOOL variable was used in an <font SIZE="-1">OUTPUT:</font> section with an exception for <font SIZE="-1">RETVAL. T_BOOL</font> in an <font SIZE="-1">INPUT:</font> section was not affected. Using a T_BOOL return type for an <font SIZE="-1">XSUB</font> (<font SIZE="-1">RETVAL</font>) was not affected. A side effect of fixing this bug is, if a T_BOOL is specified in the <font SIZE="-1">OUTPUT:</font> section (which previous did nothing to the <font SIZE="-1">SV</font>), and a read only <font SIZE="-1">SV</font> (literal) is passed to the <font SIZE="-1">XSUB,</font> croaks like ``Modification of a read-only value attempted&#8217;&#8216; will happen. [perl #115796] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On many platforms, providing a directory name as the script name caused perl to do nothing and report success. It should now universally report an error and exit nonzero. [perl #61362] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;sort {undef} ...&quot;</code> under fatal warnings no longer crashes. It had begun crashing in Perl v5.16. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Stashes blessed into each other (<code>&quot;bless \%Foo::, &#8216;Bar&#8217;; bless \%Bar::, &#8216;Foo&#8217;&quot;</code>) no longer result in double frees. This bug started happening in Perl v5.16. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Numerous memory leaks have been fixed, mostly involving fatal warnings and syntax errors. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Some failed regular expression matches such as <code>&quot;&#8216;f&#8217; =~ /../g&quot;</code> were not resetting <code>&quot;pos&quot;</code>. Also, ``match-once&#8217;&#8216; patterns (<code>&quot;m?...?g&quot;</code>) failed to reset it, too, when invoked a second time [perl #23180]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Several bugs involving <code>&quot;local *ISA&quot;</code> and <code>&quot;local *Foo::&quot;</code> causing stale <font SIZE="-1">MRO</font> caches have been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Defining a subroutine when its typeglob has been aliased no longer results in stale method caches. This bug was introduced in Perl v5.10. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Localising a typeglob containing a subroutine when the typeglob&#8217;s package has been deleted from its parent stash no longer produces an error. This bug was introduced in Perl v5.14. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Under some circumstances, <code>&quot;local *method=...&quot;</code> would fail to reset method caches upon scope exit. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;/[.foo.]/&quot;</code> is no longer an error, but produces a warning (as before) and is treated as <code>&quot;/[.fo]/&quot;</code> [perl #115818]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;goto $tied_var&quot;</code> now calls <font SIZE="-1">FETCH</font> before deciding what type of goto (subroutine or label) this is. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Renaming packages through glob assignment (<code>&quot;*Foo:: = *Bar::; *Bar:: = *Baz::&quot;</code>) in combination with <code>&quot;m?...?&quot;</code> and <code>&quot;reset&quot;</code> no longer makes threaded builds crash. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A number of bugs related to assigning a list to hash have been fixed. Many of these involve lists with repeated keys like <code>&quot;(1, 1, 1, 1)&quot;</code>. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> The expression <code>&quot;scalar(%h = (1, 1, 1, 1))&quot;</code> now returns <code>4</code>, not <code>2</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The return value of <code>&quot;%h = (1, 1, 1)&quot;</code> in list context was wrong. Previously this would return <code>&quot;(1, undef, 1)&quot;</code>, now it returns <code>&quot;(1, undef)&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl now issues the same warning on <code>&quot;($s, %h) = (1, {})&quot;</code> as it does for <code>&quot;(%h) = ({})&quot;</code>, ``Reference found where even-sized list expected&#8217;&#8216;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A number of additional edge cases in list assignment to hashes were corrected. For more details see commit 23b7025ebc. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>&bull;</dt>
<dd> <p> Attributes applied to lexical variables no longer leak memory. [perl #114764] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;dump&quot;</code>, <code>&quot;goto&quot;</code>, <code>&quot;last&quot;</code>, <code>&quot;next&quot;</code>, <code>&quot;redo&quot;</code> or <code>&quot;require&quot;</code> followed by a bareword (or version) and then an infix operator is no longer a syntax error. It used to be for those infix operators (like <code>&quot;+&quot;</code>) that have a different meaning where a term is expected. [perl #105924] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;require a::b . 1&quot;</code> and <code>&quot;require a::b + 1&quot;</code> no longer produce erroneous ambiguity warnings. [perl #107002] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Class method calls are now allowed on any string, and not just strings beginning with an alphanumeric character. [perl #105922] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> An empty pattern created with <code>&quot;qr//&quot;</code> used in <code>&quot;m///&quot;</code> no longer triggers the ``empty pattern reuses last pattern&#8217;&#8216; behaviour. [perl #96230] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Tying a hash during iteration no longer results in a memory leak. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Freeing a tied hash during iteration no longer results in a memory leak. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> List assignment to a tied array or hash that dies on <font SIZE="-1">STORE</font> no longer results in a memory leak. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> If the hint hash (<code>&quot;%^H&quot;</code>) is tied, compile-time scope entry (which copies the hint hash) no longer leaks memory if <font SIZE="-1">FETCH</font> dies. [perl #107000] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Constant folding no longer inappropriately triggers the special <code>&quot;split &quot; &quot;&quot;</code> behaviour. [perl #94490] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;defined scalar(@array)&quot;</code>, <code>&quot;defined do { &amp;foo }&quot;</code>, and similar constructs now treat the argument to <code>&quot;defined&quot;</code> as a simple scalar. [perl #97466] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Running a custom debugging that defines no <code>*DB::DB</code> glob or provides a subroutine stub for <code>&amp;DB::DB</code> no longer results in a crash, but an error instead. [perl #114990] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;reset &quot;&quot;&quot;</code> now matches its documentation. <code>&quot;reset&quot;</code> only resets <code>&quot;m?...?&quot;</code> patterns when called with no argument. An empty string for an argument now does nothing. (It used to be treated as no argument.) [perl #97958] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;printf&quot;</code> with an argument returning an empty list no longer reads past the end of the stack, resulting in erratic behaviour. [perl #77094] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;--subname&quot;</code> no longer produces erroneous ambiguity warnings. [perl #77240] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;v10&quot;</code> is now allowed as a label or package name. This was inadvertently broken when v-strings were added in Perl v5.6. [perl #56880] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;length&quot;</code>, <code>&quot;pos&quot;</code>, <code>&quot;substr&quot;</code> and <code>&quot;sprintf&quot;</code> could be confused by ties, overloading, references and typeglobs if the stringification of such changed the internal representation to or from <font SIZE="-1">UTF-8.</font> [perl #114410] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> utf8::encode now calls <font SIZE="-1">FETCH</font> and <font SIZE="-1">STORE</font> on tied variables. utf8::decode now calls <font SIZE="-1">STORE</font> (it was already calling <font SIZE="-1">FETCH</font>). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;$tied =~ s/$non_utf8/$utf8/&quot;</code> no longer loops infinitely if the tied variable returns a Latin-1 string, shared hash key scalar, or reference or typeglob that stringifies as <font SIZE="-1">ASCII</font> or Latin-1. This was a regression from v5.12. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;s///&quot;</code> without /e is now better at detecting when it needs to forego certain optimisations, fixing some buggy cases: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Match variables in certain constructs (<code>&quot;&amp;&amp;&quot;</code>, <code>&quot;||&quot;</code>, <code>&quot;..&quot;</code> and others) in the replacement part; e.g., <code>&quot;s/(.)/$l{$a||$1}/g&quot;</code>. [perl #26986] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Aliases to match variables in the replacement. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>$REGERROR</code> or <code>$REGMARK</code> in the replacement. [perl #49190] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> An empty pattern (<code>&quot;s//$foo/&quot;</code>) that causes the last-successful pattern to be used, when that pattern contains code blocks that modify the variables in the replacement. </p>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>&bull;</dt>
<dd> <p> The taintedness of the replacement string no longer affects the taintedness of the return value of <code>&quot;s///e&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>$|</code> autoflush variable is created on-the-fly when needed. If this happened (e.g., if it was mentioned in a module or eval) when the currently-selected filehandle was a typeglob with an empty <font SIZE="-1">IO</font> slot, it used to crash. [perl #115206] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Line numbers at the end of a string eval are no longer off by one. [perl #114658] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>@INC</code> filters (subroutines returned by subroutines in <code>@INC</code>) that set <code>$_</code> to a copy-on-write scalar no longer cause the parser to modify that string buffer in place. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;length($object)&quot;</code> no longer returns the undefined value if the object has string overloading that returns undef. [perl #115260] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The use of <code>&quot;PL_stashcache&quot;</code>, the stash name lookup cache for method calls, has been restored, </p>
<p> Commit da6b625f78f5f133 in August 2011 inadvertently broke the code that looks up values in <code>&quot;PL_stashcache&quot;</code>. As it&#8217;s only a cache, quite correctly everything carried on working without it. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The error ``Can&#8217;t localize through a reference&#8217;&#8216; had disappeared in v5.16.0 when <code>&quot;local %$ref&quot;</code> appeared on the last line of an lvalue subroutine. This error disappeared for <code>&quot;\local %$ref&quot;</code> in perl v5.8.1. It has now been restored. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The parsing of here-docs has been improved significantly, fixing several parsing bugs and crashes and one memory leak, and correcting wrong subsequent line numbers under certain conditions. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Inside an eval, the error message for an unterminated here-doc no longer has a newline in the middle of it [perl #70836]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A substitution inside a substitution pattern (<code>&quot;s/${s|||}//&quot;</code>) no longer confuses the parser. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> It may be an odd place to allow comments, but <code>&quot;s//&quot;&quot; # hello/e&quot;</code> has always worked, <i>unless</i> there happens to be a null character before the first #. Now it works even in the presence of nulls. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> An invalid range in <code>&quot;tr///&quot;</code> or <code>&quot;y///&quot;</code> no longer results in a memory leak. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> String eval no longer treats a semicolon-delimited quote-like operator at the very end (<code>&quot;eval &#8216;q;;&#8216;&quot;</code>) as a syntax error. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;warn {$_ =&gt; 1} + 1&quot;</code> is no longer a syntax error. The parser used to get confused with certain list operators followed by an anonymous hash and then an infix operator that shares its form with a unary operator. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;(caller $n)[6]&quot;</code> (which gives the text of the eval) used to return the actual parser buffer. Modifying it could result in crashes. Now it always returns a copy. The string returned no longer has ``\n;&#8216;&#8216; tacked on to the end. The returned text also includes here-doc bodies, which used to be omitted. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <font SIZE="-1">UTF-8</font> position cache is now reset when accessing magical variables, to avoid the string buffer and the <font SIZE="-1">UTF-8</font> position cache getting out of sync [perl #114410]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Various cases of get magic being called twice for magical <font SIZE="-1">UTF-8</font> strings have been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> This code (when not in the presence of <code>$&amp;</code> etc) </p>
<pre><code>    $_ = 'x' x 1_000_000;
    1 while /(.)/;
</code></pre>
<p> used to skip the buffer copy for performance reasons, but suffered from <code>$1</code> etc changing if the original string changed. That&#8217;s now been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl doesn&#8217;t use PerlIO anymore to report out of memory messages, as PerlIO might attempt to allocate more memory. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In a regular expression, if something is quantified with <code>&quot;{n,m}&quot;</code> where <code>&quot;n &gt; m&quot;</code>, it can&#8217;t possibly match. Previously this was a fatal error, but now is merely a warning (and that something won&#8217;t match). [perl #82954]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> It used to be possible for formats defined in subroutines that have subsequently been undefined and redefined to close over variables in the wrong pad (the newly-defined enclosing sub), resulting in crashes or ``Bizarre copy&#8217;&#8216; errors. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Redefinition of XSUBs at run time could produce warnings with the wrong line number. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>%vd</code> sprintf format does not support version objects for alpha versions. It used to output the format itself (%vd) when passed an alpha version, and also emit an ``Invalid conversion in printf&#8217;&#8216; warning. It no longer does, but produces the empty string in the output. It also no longer leaks memory in this case. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;$obj-&gt;SUPER::method&quot;</code> calls in the main package could fail if the <font SIZE="-1">SUPER</font> package had already been accessed by other means. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Stash aliasing (<code>&quot;*foo:: = *bar::&quot;</code>) no longer causes <font SIZE="-1">SUPER</font> calls to ignore changes to methods or <code>@ISA</code> or use the wrong package. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Method calls on packages whose names end in ::SUPER are no longer treated as <font SIZE="-1">SUPER</font> method calls, resulting in failure to find the method. Furthermore, defining subroutines in such packages no longer causes them to be found by <font SIZE="-1">SUPER</font> method calls on the containing package [perl #114924]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;\w&quot;</code> now matches the code points U+200C (<font SIZE="-1">ZERO WIDTH</font> NON-JOINER) and U+200D (<font SIZE="-1">ZERO WIDTH JOINER</font>). <code>&quot;\W&quot;</code> no longer matches these. This change is because Unicode corrected their definition of what <code>&quot;\w&quot;</code> should match. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;dump LABEL&quot;</code> no longer leaks its label. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Constant folding no longer changes the behaviour of functions like <code>&quot;stat()&quot;</code> and <code>&quot;truncate()&quot;</code> that can take either filenames or handles. <code>&quot;stat 1 ? foo : bar&quot;</code> nows treats its argument as a file name (since it is an arbitrary expression), rather than the handle ``foo&#8217;&#8216;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;truncate FOO, $len&quot;</code> no longer falls back to treating ``<font SIZE="-1">FOO&#8217;&#8216;</font> as a file name if the filehandle has been deleted. This was broken in Perl v5.16.0. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Subroutine redefinitions after sub-to-glob and glob-to-glob assignments no longer cause double frees or panic messages. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;s///&quot;</code> now turns vstrings into plain strings when performing a substitution, even if the resulting string is the same (<code>&quot;s/a/a/&quot;</code>). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Prototype mismatch warnings no longer erroneously treat constant subs as having no prototype when they actually have &quot;&quot;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Constant subroutines and forward declarations no longer prevent prototype mismatch warnings from omitting the sub name. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;undef&quot;</code> on a subroutine now clears call checkers. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;ref&quot;</code> operator started leaking memory on blessed objects in Perl v5.16.0. This has been fixed [perl #114340]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;use&quot;</code> no longer tries to parse its arguments as a statement, making <code>&quot;use constant { () };&quot;</code> a syntax error [perl #114222]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On debugging builds, ``uninitialized&#8217;&#8216; warnings inside formats no longer cause assertion failures. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> On debugging builds, subroutines nested inside formats no longer cause assertion failures [perl #78550]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Formats and <code>&quot;use&quot;</code> statements are now permitted inside formats. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;print $x&quot;</code> and <code>&quot;sub { print $x }-&gt;()&quot;</code> now always produce the same output. It was possible for the latter to refuse to close over <code>$x</code> if the variable was not active; e.g., if it was defined outside a currently-running named subroutine. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Similarly, <code>&quot;print $x&quot;</code> and <code>&quot;print eval &#8216;$x&#8217;&quot;</code> now produce the same output. This also allows ``my <code>$x</code> if 0&#8217;&#8216; variables to be seen in the debugger [perl #114018]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Formats called recursively no longer stomp on their own lexical variables, but each recursive call has its own set of lexicals. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Attempting to free an active format or the handle associated with it no longer results in a crash. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Format parsing no longer gets confused by braces, semicolons and low-precedence operators. It used to be possible to use braces as format delimiters (instead of <code>&quot;=&quot;</code> and <code>&quot;.&quot;</code>), but only sometimes. Semicolons and low-precedence operators in format argument lines no longer confuse the parser into ignoring the line&#8217;s return value. In format argument lines, braces can now be used for anonymous hashes, instead of being treated always as <code>&quot;do&quot;</code> blocks. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Formats can now be nested inside code blocks in regular expressions and other quoted constructs (<code>&quot;/(?{...})/&quot;</code> and <code>&quot;qq/${...}/&quot;</code>) [perl #114040]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Formats are no longer created after compilation errors. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Under debugging builds, the <code>-DA</code> command line option started crashing in Perl v5.16.0. It has been fixed [perl #114368]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A potential deadlock scenario involving the premature termination of a pseudo- forked child in a Windows build with ithreads enabled has been fixed. This resolves the common problem of the <i>t/op/fork.t</i> test hanging on Windows [perl #88840]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The code which generates errors from <code>&quot;require()&quot;</code> could potentially read one or two bytes before the start of the filename for filenames less than three bytes long and ending <code>&quot;/\.p?\z/&quot;</code>. This has now been fixed. Note that it could never have happened with module names given to <code>&quot;use()&quot;</code> or <code>&quot;require()&quot;</code> anyway. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The handling of pathnames of modules given to <code>&quot;require()&quot;</code> has been made thread-safe on <font SIZE="-1">VMS.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Non-blocking sockets have been fixed on <font SIZE="-1">VMS.</font> </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Pod can now be nested in code inside a quoted construct outside of a string eval. This used to work only within string evals [perl #114040]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;goto &#8216;&#8216;&quot;</code> now looks for an empty label, producing the ``goto must have label&#8217;&#8216; error message, instead of exiting the program [perl #111794]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;goto &quot;\0&quot;&quot;</code> now dies with ``Can&#8217;t find label&#8217;&#8216; instead of ``goto must have label&#8217;&#8216;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The C function <code>&quot;hv_store&quot;</code> used to result in crashes when used on <code>&quot;%^H&quot;</code> [perl #111000]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A call checker attached to a closure prototype via <code>&quot;cv_set_call_checker&quot;</code> is now copied to closures cloned from it. So <code>&quot;cv_set_call_checker&quot;</code> now works inside an attribute handler for a closure. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Writing to <code>$^N</code> used to have no effect. Now it croaks with ``Modification of a read-only value&#8217;&#8216; by default, but that can be overridden by a custom regular expression engine, as with <code>$1</code> [perl #112184]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;undef&quot;</code> on a control character glob (<code>&quot;undef *^H&quot;</code>) no longer emits an erroneous warning about ambiguity [perl #112456]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> For efficiency&#8217;s sake, many operators and built-in functions return the same scalar each time. Lvalue subroutines and subroutines in the <font SIZE="-1">CORE::</font> namespace were allowing this implementation detail to leak through. <code>&quot;print &amp;CORE::uc(&quot;a&quot;), &amp;CORE::uc(&quot;b&quot;)&quot;</code> used to print ``<font SIZE="-1">BB&#8217;&#8216;.</font> The same thing would happen with an lvalue subroutine returning the return value of <code>&quot;uc&quot;</code>. Now the value is copied in such cases. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;method {}&quot;</code> syntax with an empty block or a block returning an empty list used to crash or use some random value left on the stack as its invocant. Now it produces an error. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;vec&quot;</code> now works with extremely large offsets (&gt;2 <font SIZE="-1">GB</font>) [perl #111730]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Changes to overload settings now take effect immediately, as do changes to inheritance that affect overloading. They used to take effect only after <code>&quot;bless&quot;</code>. </p>
<p> Objects that were created before a class had any overloading used to remain non-overloaded even if the class gained overloading through <code>&quot;use overload&quot;</code> or <code>@ISA</code> changes, and even after <code>&quot;bless&quot;</code>. This has been fixed [perl #112708]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Classes with overloading can now inherit fallback values. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Overloading was not respecting a fallback value of 0 if there were overloaded objects on both sides of an assignment operator like <code>&quot;+=&quot;</code> [perl #111856]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;pos&quot;</code> now croaks with hash and array arguments, instead of producing erroneous warnings. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;while(each %h)&quot;</code> now implies <code>&quot;while(defined($_ = each %h))&quot;</code>, like <code>&quot;readline&quot;</code> and <code>&quot;readdir&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Subs in the <font SIZE="-1">CORE::</font> namespace no longer crash after <code>&quot;undef *_&quot;</code> when called with no argument list (<code>&amp;CORE::time</code> with no parentheses). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;unpack&quot;</code> no longer produces the ``&#8216;/&#8216; must follow a numeric type in unpack&#8217;&#8216; error when it is the data that are at fault [perl #60204]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;join&quot;</code> and <code>&quot;@array&quot;</code> now call <font SIZE="-1">FETCH</font> only once on a tied <code>$&quot;</code> [perl #8931]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Some subroutine calls generated by compiling core ops affected by a <code>&quot;CORE::GLOBAL&quot;</code> override had op checking performed twice. The checking is always idempotent for pure Perl code, but the double checking can matter when custom call checkers are involved. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A race condition used to exist around fork that could cause a signal sent to the parent to be handled by both parent and child. Signals are now blocked briefly around fork to prevent this from happening [perl #82580]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The implementation of code blocks in regular expressions, such as <code>&quot;(?{})&quot;</code> and <code>&quot;(??{})&quot;</code>, has been heavily reworked to eliminate a whole slew of bugs. The main user-visible changes are: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> Code blocks within patterns are now parsed in the same pass as the surrounding code; in particular it is no longer necessary to have balanced braces: this now works: </p>
<pre><code>    /(?{ $x='{' })/
</code></pre>
<p> This means that this error message is no longer generated: </p>
<pre><code>    Sequence (?{...}) not terminated or not {}-balanced in regex
</code></pre>
<p> but a new error may be seen: </p>
<pre><code>    Sequence (?{...}) not terminated with ')'
</code></pre>
<p> In addition, literal code blocks within run-time patterns are only compiled once, at perl compile-time: </p>
<pre><code>    for my $p (...) {
        # this 'FOO' block of code is compiled once,
        # at the same time as the surrounding 'for' loop
        /$p{(?{FOO;})/;
    }
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Lexical variables are now sane as regards scope, recursion and closure behavior. In particular, <code>&quot;/A(?{B})C/&quot;</code> behaves (from a closure viewpoint) exactly like <code>&quot;/A/ &amp;&amp; do { B } &amp;&amp; /C/&quot;</code>, while <code>&quot;qr/A(?{B})C/&quot;</code> is like <code>&quot;sub {/A/ &amp;&amp; do { B } &amp;&amp; /C/}&quot;</code>. So this code now works how you might expect, creating three regexes that match 0, 1, and 2: </p>
<pre><code>    for my $i (0..2) {
        push @r, qr/^(??{$i})$/;
    }
    &quot;1&quot; =~ $r[1]; # matches
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;use re &#8216;eval&#8217;&quot;</code> pragma is now only required for code blocks defined at runtime; in particular in the following, the text of the <code>$r</code> pattern is still interpolated into the new pattern and recompiled, but the individual compiled code-blocks within <code>$r</code> are reused rather than being recompiled, and <code>&quot;use re &#8216;eval&#8217;&quot;</code> isn&#8217;t needed any more: </p>
<pre><code>    my $r = qr/abc(?{....})def/;
    /xyz$r/;
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Flow control operators no longer crash. Each code block runs in a new dynamic scope, so <code>&quot;next&quot;</code> etc. will not see any enclosing loops. <code>&quot;return&quot;</code> returns a value from the code block, not from any enclosing subroutine. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Perl normally caches the compilation of run-time patterns, and doesn&#8217;t recompile if the pattern hasn&#8217;t changed, but this is now disabled if required for the correct behavior of closures. For example: </p>
<pre><code>    my $code = '(??{$x})';
    for my $x (1..3) {
        # recompile to see fresh value of $x each time
        $x =~ /$code/;
    }
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> The <code>&quot;/msix&quot;</code> and <code>&quot;(?msix)&quot;</code> etc. flags are now propagated into the return value from <code>&quot;(??{})&quot;</code>; this now works: </p>
<pre><code>    &quot;AB&quot; =~ /a(??{'b'})/i;
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Warnings and errors will appear to come from the surrounding code (or for run-time code blocks, from an eval) rather than from an <code>&quot;re_eval&quot;</code>: </p>
<pre><code>    use re 'eval'; $c = '(?{ warn &quot;foo&quot; })'; /$c/;
    /(?{ warn &quot;foo&quot; })/;
</code></pre>
<p> formerly gave: </p>
<pre><code>    foo at (re_eval 1) line 1.
    foo at (re_eval 2) line 1.
</code></pre>
<p> and now gives: </p>
<pre><code>    foo at (eval 1) line 1.
    foo at /some/prog line 2.
</code></pre>
 </dd></dl>
</dl>
<dl>
<dd>  </dd></dl>
<dt>&bull;</dt>
<dd> <p> Perl now can be recompiled to use any Unicode version. In v5.16, it worked on Unicodes 6.0 and 6.1, but there were various bugs if earlier releases were used; the older the release the more problems. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;vec&quot;</code> no longer produces ``uninitialized&#8217;&#8216; warnings in lvalue context [perl #9423]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> An optimization involving fixed strings in regular expressions could cause a severe performance penalty in edge cases. This has been fixed [perl #76546]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In certain cases, including empty subpatterns within a regular expression (such as <code>&quot;(?:)&quot;</code> or <code>&quot;(?:|)&quot;</code>) could disable some optimizations. This has been fixed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The ``Can&#8217;t find an opnumber&#8217;&#8216; message that <code>&quot;prototype&quot;</code> produces when passed a string like ``CORE::nonexistent_keyword&#8217;&#8216; now passes <font SIZE="-1">UTF-8</font> and embedded NULs through unchanged [perl #97478]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;prototype&quot;</code> now treats magical variables like <code>$1</code> the same way as non-magical variables when checking for the <font SIZE="-1">CORE::</font> prefix, instead of treating them as subroutine names. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Under threaded perls, a runtime code block in a regular expression could corrupt the package name stored in the op tree, resulting in bad reads in <code>&quot;caller&quot;</code>, and possibly crashes [perl #113060]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Referencing a closure prototype (<code>&quot;\&amp;{$_[1]}&quot;</code> in an attribute handler for a closure) no longer results in a copy of the subroutine (or assertion failures on debugging builds). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;eval &#8216;__PACKAGE__&#8216;&quot;</code> now returns the right answer on threaded builds if the current package has been assigned over (as in <code>&quot;*ThisPackage:: = *ThatPackage::&quot;</code>) [perl #78742]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> If a package is deleted by code that it calls, it is possible for <code>&quot;caller&quot;</code> to see a stack frame belonging to that deleted package. <code>&quot;caller&quot;</code> could crash if the stash&#8217;s memory address was reused for a scalar and a substitution was performed on the same scalar [perl #113486]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;UNIVERSAL::can&quot;</code> no longer treats its first argument differently depending on whether it is a string or number internally. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;open&quot;</code> with <code>&quot;&lt;&amp;&quot;</code> for the mode checks to see whether the third argument is a number, in determining whether to treat it as a file descriptor or a handle name. Magical variables like <code>$1</code> were always failing the numeric check and being treated as handle names. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;warn&quot;</code>&#8216;s handling of magical variables (<code>$1</code>, ties) has undergone several fixes. <code>&quot;FETCH&quot;</code> is only called once now on a tied argument or a tied <code>$@</code> [perl #97480]. Tied variables returning objects that stringify as &quot;&quot; are no longer ignored. A tied <code>$@</code> that happened to return a reference the <i>previous</i> time it was used is no longer ignored. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;warn &quot;&quot;&quot;</code> now treats <code>$@</code> with a number in it the same way, regardless of whether it happened via <code>&quot;$@=3&quot;</code> or <code>&quot;$@=&quot;3&quot;&quot;</code>. It used to ignore the former. Now it appends ``\t...caught&#8217;&#8216;, as it has always done with <code>&quot;$@=&quot;3&quot;&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Numeric operators on magical variables (e.g., <code>&quot;$1 + 1&quot;</code>) used to use floating point operations even where integer operations were more appropriate, resulting in loss of accuracy on 64-bit platforms [perl #109542]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unary negation no longer treats a string as a number if the string happened to be used as a number at some point. So, if <code>$x</code> contains the string ``dogs&#8217;&#8216;, <code>&quot;-$x&quot;</code> returns ``-dogs&#8217;&#8216; even if <code>&quot;$y=0+$x&quot;</code> has happened at some point. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> In Perl v5.14, <code>&quot;-&#8216;-10&#8217;&quot;</code> was fixed to return ``10&#8217;&#8216;, not ``+10&#8217;&#8216;. But magical variables (<code>$1</code>, ties) were not fixed till now [perl #57706]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unary negation now treats strings consistently, regardless of the internal <code>&quot;UTF8&quot;</code> flag. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A regression introduced in Perl v5.16.0 involving <code>&quot;tr/</code>SEARCHLIST <code>/</code>REPLACEMENTLIST <code>/&quot;</code> has been fixed. Only the first instance is supposed to be meaningful if a character appears more than once in <code>&quot;</code>SEARCHLIST <code>&quot;</code>. Under some circumstances, the final instance was overriding all earlier ones. [perl #113584] </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Regular expressions like <code>&quot;qr/\87/&quot;</code> previously silently inserted a <font SIZE="-1">NUL</font> character, thus matching as if it had been written <code>&quot;qr/\00087/&quot;</code>. Now it matches as if it had been written as <code>&quot;qr/87/&quot;</code>, with a message that the sequence <code>&quot;\8&quot;</code> is unrecognized. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;__SUB__&quot;</code> now works in special blocks (<code>&quot;BEGIN&quot;</code>, <code>&quot;END&quot;</code>, etc.). </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Thread creation on Windows could theoretically result in a crash if done inside a <code>&quot;BEGIN&quot;</code> block. It still does not work properly, but it no longer crashes [perl #111610]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;\&amp;{&#8216;&#8216;}&quot;</code> (with the empty string) now autovivifies a stub like any other sub name, and no longer produces the ``Unable to create sub&#8217;&#8216; error [perl #94476]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A regression introduced in v5.14.0 has been fixed, in which some calls to the <code>&quot;re&quot;</code> module would clobber <code>$_</code> [perl #113750]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;do FILE&quot;</code> now always either sets or clears <code>$@</code>, even when the file can&#8217;t be read. This ensures that testing <code>$@</code> first (as recommended by the documentation) always returns the correct result. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The array iterator used for the <code>&quot;each @array&quot;</code> construct is now correctly reset when <code>@array</code> is cleared [perl #75596]. This happens, for example, when the array is globally assigned to, as in <code>&quot;@array = (...)&quot;</code>, but not when its <code>values</code> are assigned to. In terms of the <font SIZE="-1">XS API,</font> it means that <code>&quot;av_clear()&quot;</code> will now reset the iterator. </p>
<p> This mirrors the behaviour of the hash iterator when the hash is cleared. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;$class-&gt;can&quot;</code>, <code>&quot;$class-&gt;isa&quot;</code>, and <code>&quot;$class-&gt;DOES&quot;</code> now return correct results, regardless of whether that package referred to by <code>$class</code> exists [perl #47113]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Arriving signals no longer clear <code>$@</code> [perl #45173]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Allow <code>&quot;my ()&quot;</code> declarations with an empty variable list [perl #113554]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> During parsing, subs declared after errors no longer leave stubs [perl #113712]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Closures containing no string evals no longer hang on to their containing subroutines, allowing variables closed over by outer subroutines to be freed when the outer sub is freed, even if the inner sub still exists [perl #89544]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Duplication of in-memory filehandles by opening with a ``&lt;&amp;=&#8216;&#8216; or ``&gt;&amp;=&#8216;&#8216; mode stopped working properly in v5.16.0. It was causing the new handle to reference a different scalar variable. This has been fixed [perl #113764]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;qr//&quot;</code> expressions no longer crash with custom regular expression engines that do not set <code>&quot;offs&quot;</code> at regular expression compilation time [perl #112962]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;delete local&quot;</code> no longer crashes with certain magical arrays and hashes [perl #112966]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;local&quot;</code> on elements of certain magical arrays and hashes used not to arrange to have the element deleted on scope exit, even if the element did not exist before <code>&quot;local&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;scalar(write)&quot;</code> no longer returns multiple items [perl #73690]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> String to floating point conversions no longer misparse certain strings under <code>&quot;use locale&quot;</code> [perl #109318]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>@INC</code> filters that die no longer leak memory [perl #92252]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The implementations of overloaded operations are now called in the correct context. This allows, among other things, being able to properly override <code>&quot;&lt;&gt;&quot;</code> [perl #47119]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Specifying only the <code>&quot;fallback&quot;</code> key when calling <code>&quot;use overload&quot;</code> now behaves properly [perl #113010]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;sub foo { my $a = 0; while ($a) { ... } }&quot;</code> and <code>&quot;sub foo { while (0) { ... } }&quot;</code> now return the same thing [perl #73618]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> String negation now behaves the same under <code>&quot;use integer;&quot;</code> as it does without [perl #113012]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;chr&quot;</code> now returns the Unicode replacement character (U+FFFD) for -1, regardless of the internal representation. -1 used to wrap if the argument was tied or a string internally. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Using a <code>&quot;format&quot;</code> after its enclosing sub was freed could crash as of perl v5.12.0, if the format referenced lexical variables from the outer sub. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Using a <code>&quot;format&quot;</code> after its enclosing sub was undefined could crash as of perl v5.10.0, if the format referenced lexical variables from the outer sub. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Using a <code>&quot;format&quot;</code> defined inside a closure, which format references lexical variables from outside, never really worked unless the <code>&quot;write&quot;</code> call was directly inside the closure. In v5.10.0 it even started crashing. Now the copy of that closure nearest the top of the call stack is used to find those variables. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Formats that close over variables in special blocks no longer crash if a stub exists with the same name as the special block before the special block is compiled. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The parser no longer gets confused, treating <code>&quot;eval foo ()&quot;</code> as a syntax error if preceded by <code>&quot;print;&quot;</code> [perl #16249]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The return value of <code>&quot;syscall&quot;</code> is no longer truncated on 64-bit platforms [perl #113980]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Constant folding no longer causes <code>&quot;print 1 ? FOO : BAR&quot;</code> to print to the <font SIZE="-1">FOO</font> handle [perl #78064]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;do subname&quot;</code> now calls the named subroutine and uses the file name it returns, instead of opening a file named ``subname&#8217;&#8216;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Subroutines looked up by rv2cv check hooks (registered by <font SIZE="-1">XS</font> modules) are now taken into consideration when determining whether <code>&quot;foo bar&quot;</code> should be the sub call <code>&quot;foo(bar)&quot;</code> or the method call <code>&quot;&quot;bar&quot;-&gt;foo&quot;</code>. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;CORE::foo::bar&quot;</code> is no longer treated specially, allowing global overrides to be called directly via <code>&quot;CORE::GLOBAL::uc(...)&quot;</code> [perl #113016]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Calling an undefined sub whose typeglob has been undefined now produces the customary ``Undefined subroutine called&#8217;&#8216; error, instead of ``Not a <font SIZE="-1">CODE</font> reference&#8217;&#8216;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Two bugs involving <code>@ISA</code> have been fixed. <code>&quot;*ISA = *glob_without_array&quot;</code> and <code>&quot;undef *ISA; @{*ISA}&quot;</code> would prevent future modifications to <code>@ISA</code> from updating the internal caches used to look up methods. The *glob_without_array case was a regression from Perl v5.12. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Regular expression optimisations sometimes caused <code>&quot;$&quot;</code> with <code>&quot;/m&quot;</code> to produce failed or incorrect matches [perl #114068]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;__SUB__&quot;</code> now works in a <code>&quot;sort&quot;</code> block when the enclosing subroutine is predeclared with <code>&quot;sub foo;&quot;</code> syntax [perl #113710]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Unicode properties only apply to Unicode code points, which leads to some subtleties when regular expressions are matched against above-Unicode code points. There is a warning generated to draw your attention to this. However, this warning was being generated inappropriately in some cases, such as when a program was being parsed. Non-Unicode matches such as <code>&quot;\w&quot;</code> and <code>&quot;[:word:]&quot;</code> should not generate the warning, as their definitions don&#8217;t limit them to apply to only Unicode code points. Now the message is only generated when matching against <code>&quot;\p{}&quot;</code> and <code>&quot;\P{}&quot;</code>. There remains a bug, [perl #114148], for the very few properties in Unicode that match just a single code point. The warning is not generated if they are matched against an above-Unicode code point. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Uninitialized warnings mentioning hash elements would only mention the element name if it was not in the first bucket of the hash, due to an off-by-one error. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A regular expression optimizer bug could cause multiline ``^&#8216;&#8216; to behave incorrectly in the presence of line breaks, such that <code>&quot;&quot;/\n\n&quot; =~ m#\A(?:^/$)#im&quot;</code> would not match [perl #115242]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Failed <code>&quot;fork&quot;</code> in list context no longer corrupts the stack. <code>&quot;@a = (1, 2, fork, 3)&quot;</code> used to gobble up the 2 and assign <code>&quot;(1, undef, 3)&quot;</code> if the <code>&quot;fork&quot;</code> call failed. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Numerous memory leaks have been fixed, mostly involving tied variables that die, regular expression character classes and code blocks, and syntax errors. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Assigning a regular expression (<code>&quot;${qr//}&quot;</code>) to a variable that happens to hold a floating point number no longer causes assertion failures on debugging builds. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Assigning a regular expression to a scalar containing a number no longer causes subsequent numification to produce random numbers. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Assigning a regular expression to a magic variable no longer wipes away the magic. This was a regression from v5.10. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Assigning a regular expression to a blessed scalar no longer results in crashes. This was also a regression from v5.10. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Regular expression can now be assigned to tied hash and array elements with flattening into strings. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Numifying a regular expression no longer results in an uninitialized warning. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Negative array indices no longer cause <font SIZE="-1">EXISTS</font> methods of tied variables to be ignored. This was a regression from v5.12. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Negative array indices no longer result in crashes on arrays tied to non-objects. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;$byte_overload .= $utf8&quot;</code> no longer results in doubly-encoded <font SIZE="-1">UTF-8</font> if the left-hand scalar happened to have produced a <font SIZE="-1">UTF-8</font> string the last time overloading was invoked. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>&quot;goto &amp;sub&quot;</code> now uses the current value of <code>@_</code>, instead of using the array the subroutine was originally called with. This means <code>&quot;local @_ = (...); goto &amp;sub&quot;</code> now works [perl #43077]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> If a debugger is invoked recursively, it no longer stomps on its own lexical variables. Formerly under recursion all calls would share the same set of lexical variables [perl #115742]. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> <code>*_{ARRAY}</code> returned from a subroutine no longer spontaneously becomes empty. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> When using <code>&quot;say&quot;</code> to print to a tied filehandle, the value of <code>&quot;$\&quot;</code> is correctly localized, even if it was previously undef. [perl #119927] </p>
 </dd></dl>
<h2>Known Problems</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> UTF8-flagged strings in <code>%ENV</code> on HP-UX 11.00 are buggy </p>
<p> The interaction of UTF8-flagged strings and <code>%ENV</code> on HP-UX 11.00 is currently dodgy in some not-yet-fully-diagnosed way. Expect test failures in <i>t/op/magic.t</i>, followed by unknown behavior when storing wide characters in the environment. </p>
 </dd></dl>
<h2>Obituary</h2>
<p> Hojung Yoon (<font SIZE="-1">AMORETTE</font>), 24, of Seoul, South Korea, went to his long rest on May 8, 2013 with llama figurine and autographed <font SIZE="-1">TIMTOADY</font> card. He was a brilliant young Perl 5 &amp; 6 hacker and a devoted member of Seoul.pm. He programmed Perl, talked Perl, ate Perl, and loved Perl. We believe that he is still programming in Perl with his broken <font SIZE="-1">IBM</font> laptop somewhere. He will be missed.  </p>
<h2>Acknowledgements</h2>
<p> Perl v5.18.0 represents approximately 12 months of development since Perl v5.16.0 and contains approximately 400,000 lines of changes across 2,100 files from 113 authors. </p>
<p> Perl continues to flourish into its third decade thanks to a vibrant community of users and developers. The following people are known to have contributed the improvements that became Perl v5.18.0: </p>
<p> Aaron Crane, Aaron Trevena, Abhijit Menon-Sen, Adrian M. Enache, Alan Haggai Alavi, Alexandr Ciornii, Andrew Tam, Andy Dougherty, Anton Nikishaev, Aristotle Pagaltzis, Augustina Blair, Bob Ernst, Brad Gilbert, Breno G. de Oliveira, Brian Carlson, Brian Fraser, Charlie Gonzalez, Chip Salzenberg, Chris &#8216;BinGOs&#8217; Williams, Christian Hansen, Colin Kuskie, Craig A. Berry, Dagfinn Ilmari Mannsåker, Daniel Dragan, Daniel Perrett, Darin McBride, Dave Rolsky, David Golden, David Leadbeater, David Mitchell, David Nicol, Dominic Hargreaves, E. Choroba, Eric Brine, Evan Miller, Father Chrysostomos, Florian Ragwitz, François Perrad, George Greer, Goro Fuji, H.Merijn Brand, Herbert Breunung, Hugo van der Sanden, Igor Zaytsev, James E Keenan, Jan Dubois, Jasmine Ahuja, Jerry D. Hedden, Jess Robinson, Jesse Luehrs, Joaquin Ferrero, Joel Berger, John Goodyear, John Peacock, Karen Etheridge, Karl Williamson, Karthik Rajagopalan, Kent Fredric, Leon Timmermans, Lucas Holt, Lukas Mai, Marcus Holland-Moritz, Markus Jansen, Martin Hasch, Matthew Horsfall, Max Maischein, Michael G Schwern, Michael Schroeder, Moritz Lenz, Nicholas Clark, Niko Tyni, Oleg Nesterov, Patrik Hägglund, Paul Green, Paul Johnson, Paul Marquess, Peter Martini, Rafael Garcia-Suarez, Reini Urban, Renee Baecker, Rhesa Rozendaal, Ricardo Signes, Robin Barker, Ronald J. Kimball, Ruslan Zakirov, Salvador Fandiño, Sawyer X, Scott Lanning, Sergey Alekseev, Shawn M Moore, Shirakata Kentaro, Shlomi Fish, Sisyphus, Smylers, Steffen Müller, Steve Hay, Steve Peters, Steven Schubiger, Sullivan Beck, Sven Strickroth, Sébastien Aperghis-Tramoni, Thomas Sibley, Tobias Leich, Tom Wyant, Tony Cook, Vadim Konovalov, Vincent Pit, Volker Schatz, Walt Mankowski, Yves Orton, Zefram. </p>
<p> The list above is almost certainly incomplete as it is automatically generated from version control history. In particular, it does not include the names of the (very much appreciated) contributors who reported issues to the Perl bug tracker. </p>
<p> Many of the changes included in this version originated in the <font SIZE="-1">CPAN</font> modules included in Perl&#8217;s core. We&#8217;re grateful to the entire <font SIZE="-1">CPAN</font> community for helping Perl to flourish. </p>
<p> For a more complete list of all of Perl&#8217;s historical contributors, please see the <i></i><font SIZE="-1"><i>AUTHORS</i></font><i></i> file in the Perl source distribution.  </p>
<h2>Reporting Bugs</h2>
<p> If you find what you think is a bug, you might check the articles recently posted to the comp.lang.perl.misc newsgroup and the perl bug database at <a rel="nofollow" href="http://rt.perl.org/perlbug/">http://rt.perl.org/perlbug/</a> . There may also be information at <a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a> , the Perl Home Page. </p>
<p> If you believe you have an unreported bug, please run the perlbug program included with your release. Be sure to trim your bug down to a tiny but sufficient test case. Your bug report, along with the output of <code>&quot;perl -V&quot;</code>, will be sent off to perlbug [at] perl.org to be analysed by the Perl porting team. </p>
<p> If the bug you are reporting has security implications, which make it inappropriate to send to a publicly archived mailing list, then please send it to perl5-security-report [at] perl.org. This points to a closed subscription unarchived mailing list, which includes all the core committers, who will be able to help assess the impact of issues, figure out a resolution, and help co-ordinate the release of patches to mitigate or fix the problem across all platforms on which Perl is supported. Please only use this address for security issues in the Perl core, not for modules independently distributed on <font SIZE="-1">CPAN.</font>  </p>
<h2>SEE ALSO</h2>
<p> The <i>Changes</i> file for an explanation of how to view exhaustive details on what changed. </p>
<p> The <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file for how to build Perl. </p>
<p> The <i></i><font SIZE="-1"><i>README</i></font><i></i> file for general stuff. </p>
<p> The <i>Artistic</i> and <i>Copying</i> files for copyright information. </p>
