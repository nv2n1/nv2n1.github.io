---
title: "perl5180delta(1)"
name: "perl5180delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5180delta/"
description: "perl5180delta – what is new for perl v5.18.0"
---

<h2 class="name">NAME</h2>
<p> perl5180delta &#8211; what is new for perl v5.18.0 </p>
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
<dt>&bull;</p>
<dd> <tt>&quot;op-entry&quot;</tt></p>
<dt>&bull;</p>
<dd> <tt>&quot;loading-file&quot;</tt></p>
<dt>&bull;</p>
<dd> <tt>&quot;loaded-file&quot;</tt></dl>
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
<p> Unicode has now withdrawn their previous recommendation for regular expressions to automatically handle cases where a single character can match multiple characters case-insensitively, for example, the letter <font SIZE="-1">LATIN SMALL LETTER SHARP S</font> and the sequence <tt>&quot;ss&quot;</tt>. This is because it turns out to be impracticable to do this correctly in all circumstances. Because Perl has tried to do this as best it can, it will continue to do so. (We are considering an option to turn it off.) However, a new restriction is being added on such matches when they occur in [bracketed] character classes. People were specifying things such as <tt>&quot;/[
