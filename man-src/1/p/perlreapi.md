---
title: "perlreapi(1)"
name: "perlreapi"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlreapi/"
description: "perlreapi – Perl regular expression plugin interface"
---

<h2 class="name">NAME</h2>
<p> perlreapi &#8211; Perl regular expression plugin interface </p>
<h2>DESCRIPTION</h2>
<p> As of Perl 5.9.5 there is a new interface for plugging and using regular expression engines other than the default one. </p>
<p> Each engine is supposed to provide access to a constant structure of the following format: </p>
<pre><code>
typedef struct regexp_engine {
    REGEXP *(*comp)(pTHX_ const SV *const pattern, const U32 flags);
    I32 (*exec)
    (pTHX_
         REGEXP *const rx,
     char *stringarg,
     char *strend, char *strbeg,
     SSize_t minend, SV *sv,
     void *data, U32 flags);
    char *(*intuit)(pTHX_
                        REGEXP *const rx,
                    SV *sv,
                    const char *const strbeg,
                    char *strpos, char *strend, U32 flags,
                    struct re_scream_pos_data_s *data);
    SV *(*checkstr)(pTHX_ REGEXP *const rx);
    void (*free)(pTHX_ REGEXP *const rx);
    void (*numbered_buff_FETCH)(pTHX_
                                    REGEXP *const rx,
                                const I32 paren,
                                SV *const sv);
    void (*numbered_buff_STORE)(pTHX_
                                    REGEXP *const rx,
                                const I32 paren,
                                SV const *const value);
    I32 (*numbered_buff_LENGTH)
    (pTHX_
         REGEXP *const rx,
     const SV *const sv,
     const I32 paren);
    SV *(*named_buff)(pTHX_
                          REGEXP *const rx,
                      SV *const key,
                      SV *const value,
                      U32 flags);
    SV *(*named_buff_iter)(pTHX_
                               REGEXP *const rx,
                           const SV *const lastkey,
                           const U32 flags);
    SV *(*qr_package)(pTHX_ REGEXP *const rx);
#ifdef USE_ITHREADS
    void *(*dupe)(pTHX_ REGEXP *const rx, CLONE_PARAMS *param);
#endif
    REGEXP *(*op_comp)(...);
</code></pre>
<p> When a regexp is compiled, its <tt>&quot;engine&quot;</tt> field is then set to point at the appropriate structure, so that when it needs to be used Perl can find the right routines to do so. </p>
<p> In order to install a new regexp handler, <tt>$^H{regcomp}</tt> is set to an integer which (when casted appropriately) resolves to one of these structures. When compiling, the <tt>&quot;comp&quot;</tt> method is executed, and the resulting <tt>&quot;regexp&quot;</tt> structure&#8217;s engine field is expected to point back at the same structure. </p>
<p> The pTHX_ symbol in the definition is a macro used by Perl under threading to provide an extra argument to the routine holding a pointer back to the interpreter that is executing the regexp. So under threading all routines get an extra argument.</p>
<h2>Callbacks</h2>
<h3>comp</h3>
<p>REGEXP *comp(pTHX_ const SV *const pattern, const U32 flags);</p>
<p> Compile the pattern stored in <tt>&quot;pattern&quot;</tt> using the given <tt>&quot;flags&quot;</tt> and return a pointer to a prepared <tt>&quot;REGEXP&quot;</tt> structure that can perform the match. See &#8220;The <font SIZE="-1">REGEXP</font> structure&#8221; below for an explanation of the individual fields in the <font SIZE="-1">REGEXP</font> struct. </p>
<p> The <tt>&quot;pattern&quot;</tt> parameter is the scalar that was used as the pattern. Previous versions of Perl would pass two <tt>&quot;char*&quot;</tt> indicating the start and end of the stringified pattern; the following snippet can be used to get the old parameters: </p>
<p>STRLEN plen;<br />
char *exp = SvPV(pattern, plen);<br />
char *xend = exp + plen;</p>
<p> Since any scalar can be passed as a pattern, it&#8217;s possible to implement an engine that does something with an array (<tt>&quot;&quot;ook&quot; =~ [ qw/ eek hlagh / ]&quot;</tt>) or with the non-stringified form of a compiled regular expression (<tt>&quot;&quot;ook&quot; =~ qr/eek/&quot;</tt>). Perl&#8217;s own engine will always stringify everything using the snippet above, but that doesn&#8217;t mean other engines have to. </p>
<p> The <tt>&quot;flags&quot;</tt> parameter is a bitfield which indicates which of the <tt>&quot;msixpn&quot;</tt> flags the regex was compiled with. It also contains additional info, such as if <tt>&quot;use locale&quot;</tt> is in effect. </p>
<p> The <tt>&quot;eogc&quot;</tt> flags are stripped out before being passed to the comp routine. The regex engine does not need to know if any of these are set, as those flags should only affect what Perl does with the pattern and its match variables, not how it gets compiled and executed. </p>
<p> By the time the comp callback is called, some of these flags have already had effect (noted below where applicable). However most of their effect occurs after the comp callback has run, in routines that read the <tt>&quot;rx-&gt;extflags&quot;</tt> field which it populates. </p>
<p> In general the flags should be preserved in <tt>&quot;rx-&gt;extflags&quot;</tt> after compilation, although the regex engine might want to add or delete some of them to invoke or disable some special behavior in Perl. The flags along with any special behavior they cause are documented below: </p>
<p> The pattern modifiers:</p>
<dl>
<dt>&quot;/m&quot; &#8211; RXf_PMf_MULTILINE</p>
<dd> If this is in <tt>&quot;rx-&gt;extflags&quot;</tt> it will be passed to <tt>&quot;Perl_fbm_instr&quot;</tt> by <tt>&quot;pp_split&quot;</tt> which will treat the subject string as a multi-line string.</p>
<dt>&quot;/s&quot; &#8211; RXf_PMf_SINGLELINE</p>
<dd>
<dt>&quot;/i&quot; &#8211; RXf_PMf_FOLD</p>
<dd>
<dt>&quot;/x&quot; &#8211; RXf_PMf_EXTENDED</p>
<dd> If present on a regex, <tt>&quot;#&quot;</tt> comments will be handled differently by the tokenizer in some cases. </p>
<p> <font SIZE="-1">TODO:</font> Document those cases.</p>
<dt>&quot;/p&quot; &#8211; RXf_PMf_KEEPCOPY</p>
<dd> <font SIZE="-1">TODO:</font> Document this</p>
<dt>Character set</p>
<dd> The character set rules are determined by an enum that is contained in this field. This is still experimental and subject to change, but the current interface returns the rules by use of the in-line function <tt>&quot;get_regex_charset(const U32 flags)&quot;</tt>. The only currently documented value returned from it is <font SIZE="-1">REGEX_LOCALE_CHARSET,</font> which is set if <tt>&quot;use locale&quot;</tt> is in effect. If present in <tt>&quot;rx-&gt;extflags&quot;</tt>, <tt>&quot;split&quot;</tt> will use the locale dependent definition of whitespace when RXf_SKIPWHITE or RXf_WHITE is in effect. <font SIZE="-1">ASCII</font> whitespace is defined as per isSPACE, and by the internal macros <tt>&quot;is_utf8_space&quot;</tt> under <font SIZE="-1">UTF-8,</font> and <tt>&quot;isSPACE_LC&quot;</tt> under <tt>&quot;use locale&quot;</tt>.</dl>
<p> Additional flags:</p>
<dl>
<dt>RXf_SPLIT</p>
<dd> This flag was removed in perl 5.18.0. <tt>&quot;split ' '&quot;</tt> is now special-cased solely in the parser. RXf_SPLIT is still #defined, so you can test for it. This is how it used to work: </p>
<p> If <tt>&quot;split&quot;</tt> is invoked as <tt>&quot;split ' '&quot;</tt> or with no arguments (which really means <tt>&quot;split(' ', $_)&quot;</tt>, see split), Perl will set this flag. The regex engine can then check for it and set the <font SIZE="-1">SKIPWHITE</font> and <font SIZE="-1">WHITE</font> extflags. To do this, the Perl engine does: </p>
<p>if (flags &amp; RXf_SPLIT &amp;&amp; r-&gt;prelen == 1 &amp;&amp; r-&gt;precomp[0] == &#8216; &#8216;)<br />
    r-&gt;extflags |= (RXf_SKIPWHITE | RXf_WHITE);
</dl>
<p> These flags can be set during compilation to enable optimizations in the <tt>&quot;split&quot;</tt> operator.</p>
<dl>
<dt>RXf_SKIPWHITE</p>
<dd> This flag was removed in perl 5.18.0. It is still #defined, so you can set it, but doing so will have no effect. This is how it used to work: </p>
<p> If the flag is present in <tt>&quot;rx-&gt;extflags&quot;</tt> <tt>&quot;split&quot;</tt> will delete whitespace from the start of the subject string before it&#8217;s operated on. What is considered whitespace depends on if the subject is a <font SIZE="-1">UTF-8</font> string and if the <tt>&quot;RXf_PMf_LOCALE&quot;</tt> flag is set. </p>
<p> If RXf_WHITE is set in addition to this flag, <tt>&quot;split&quot;</tt> will behave like <tt>&quot;split &quot; &quot;&quot;</tt> under the Perl engine.</p>
<dt>RXf_START_ONLY</p>
<dd> Tells the split operator to split the target string on newlines (<tt>&quot;
&quot;</tt>) without invoking the regex engine. </p>
<p> Perl&#8217;s engine sets this if the pattern is <tt>&quot;/^/&quot;</tt> (<tt>&quot;plen == 1 &amp;&amp; *exp == '^'&quot;</tt>), even under <tt>&quot;/^/s&quot;</tt>; see split. Of course a different regex engine might want to use the same optimizations with a different syntax.</p>
<dt>RXf_WHITE</p>
<dd> Tells the split operator to split the target string on whitespace without invoking the regex engine. The definition of whitespace varies depending on if the target string is a <font SIZE="-1">UTF-8</font> string and on if RXf_PMf_LOCALE is set. </p>
<p> Perl&#8217;s engine sets this flag if the pattern is <tt>&quot;\s+&quot;</tt>.</p>
<dt>RXf_NULL</p>
<dd> Tells the split operator to split the target string on characters. The definition of character varies depending on if the target string is a <font SIZE="-1">UTF-8</font> string. </p>
<p> Perl&#8217;s engine sets this flag on empty patterns, this optimization makes <tt>&quot;split //&quot;</tt> much faster than it would otherwise be. It&#8217;s even faster than <tt>&quot;unpack&quot;</tt>.</p>
<dt>RXf_NO_INPLACE_SUBST</p>
<dd> Added in perl 5.18.0, this flag indicates that a regular expression might perform an operation that would interfere with inplace substitution. For instance it might contain lookbehind, or assign to non-magical variables (such as <tt>$REGMARK</tt> and <tt>$REGERROR</tt>) during matching. <tt>&quot;s///&quot;</tt> will skip certain optimisations when this is set.</dl>
<h3>exec</h3>
<p>I32 exec(pTHX_ REGEXP *const rx,<br />
         char *stringarg, char *strend, char *strbeg,<br />
         SSize_t minend, SV *sv,<br />
         void *data, U32 flags);</p>
<p> Execute a regexp. The arguments are</p>
<dl>
<dt>rx</p>
<dd> The regular expression to execute.</p>
<dt>sv</p>
<dd> This is the <font SIZE="-1">SV</font> to be matched against. Note that the actual char array to be matched against is supplied by the arguments described below; the <font SIZE="-1">SV</font> is just used to determine UTF8ness, <tt>&quot;pos()&quot;</tt> etc.</p>
<dt>strbeg</p>
<dd> Pointer to the physical start of the string.</p>
<dt>strend</p>
<dd> Pointer to the character following the physical end of the string (i.e. the <tt>&quot;
