---
title: "perlreapi(1)"
name: "perlreapi"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlreapi/"
description: "perlreapi – Perl regular expression plugin interface"
---
<h2 class="name">NAME</h2>
<p> perlreapi - Perl regular expression plugin interface </p>
<h2>DESCRIPTION</h2>
<p> As of Perl 5.9.5 there is a new interface for plugging and using regular expression engines other than the default one. </p>
<p> Each engine is supposed to provide access to a constant structure of the following format: </p>
<pre><code>    typedef struct regexp_engine {
        REGEXP* (*comp) (pTHX_
                         const SV * const pattern, const U32 flags);
        I32 (*exec) (pTHX_
                         REGEXP * const rx,
                         char* stringarg,
                         char* strend, char* strbeg,
                         SSize_t minend, SV* sv,
                         void* data, U32 flags);
        char* (*intuit) (pTHX_
                           REGEXP * const rx, SV *sv,
                           const char * const strbeg,
                           char *strpos, char *strend, U32 flags,
                           struct re_scream_pos_data_s *data);
        SV* (*checkstr) (pTHX_ REGEXP * const rx);
        void (*free) (pTHX_ REGEXP * const rx);
        void (*numbered_buff_FETCH) (pTHX_
                                        REGEXP * const rx,
                                        const I32 paren,
                                        SV * const sv);
        void (*numbered_buff_STORE) (pTHX_
                                        REGEXP * const rx,
                                        const I32 paren,
                                        SV const * const value);
        I32 (*numbered_buff_LENGTH) (pTHX_
                                         REGEXP * const rx,
                                         const SV * const sv,
                                         const I32 paren);
        SV* (*named_buff) (pTHX_
                               REGEXP * const rx,
                               SV * const key,
                               SV * const value,
                               U32 flags);
        SV* (*named_buff_iter) (pTHX_
                                    REGEXP * const rx,
                                    const SV * const lastkey,
                                    const U32 flags);
        SV* (*qr_package)(pTHX_ REGEXP * const rx);
    #ifdef USE_ITHREADS
        void* (*dupe) (pTHX_ REGEXP * const rx, CLONE_PARAMS *param);
    #endif
        REGEXP* (*op_comp) (...);
</code></pre>
<p> When a regexp is compiled, its <code>&quot;engine&quot;</code> field is then set to point at the appropriate structure, so that when it needs to be used Perl can find the right routines to do so. </p>
<p> In order to install a new regexp handler, <code>$^H{regcomp}</code> is set to an integer which (when casted appropriately) resolves to one of these structures. When compiling, the <code>&quot;comp&quot;</code> method is executed, and the resulting <code>&quot;regexp&quot;</code> structure&#8217;s engine field is expected to point back at the same structure. </p>
<p> The pTHX_ symbol in the definition is a macro used by Perl under threading to provide an extra argument to the routine holding a pointer back to the interpreter that is executing the regexp. So under threading all routines get an extra argument.  </p>
<h2>Callbacks</h2>
<h3>comp</h3>
<pre><code>    REGEXP* comp(pTHX_ const SV * const pattern, const U32 flags);
</code></pre>
<p> Compile the pattern stored in <code>&quot;pattern&quot;</code> using the given <code>&quot;flags&quot;</code> and return a pointer to a prepared <code>&quot;REGEXP&quot;</code> structure that can perform the match. See ``The <font SIZE="-1">REGEXP</font> structure&#8217;&#8216; below for an explanation of the individual fields in the <font SIZE="-1">REGEXP</font> struct. </p>
<p> The <code>&quot;pattern&quot;</code> parameter is the scalar that was used as the pattern. Previous versions of Perl would pass two <code>&quot;char*&quot;</code> indicating the start and end of the stringified pattern; the following snippet can be used to get the old parameters: </p>
<pre><code>    STRLEN plen;
    char* exp = SvPV(pattern, plen);
    char* xend = exp + plen;
</code></pre>
<p> Since any scalar can be passed as a pattern, it&#8217;s possible to implement an engine that does something with an array (<code>&quot;&quot;ook&quot; =~ [ qw/ eek hlagh / ]&quot;</code>) or with the non-stringified form of a compiled regular expression (<code>&quot;&quot;ook&quot; =~ qr/eek/&quot;</code>). Perl&#8217;s own engine will always stringify everything using the snippet above, but that doesn&#8217;t mean other engines have to. </p>
<p> The <code>&quot;flags&quot;</code> parameter is a bitfield which indicates which of the <code>&quot;msixpn&quot;</code> flags the regex was compiled with. It also contains additional info, such as if <code>&quot;use locale&quot;</code> is in effect. </p>
<p> The <code>&quot;eogc&quot;</code> flags are stripped out before being passed to the comp routine. The regex engine does not need to know if any of these are set, as those flags should only affect what Perl does with the pattern and its match variables, not how it gets compiled and executed. </p>
<p> By the time the comp callback is called, some of these flags have already had effect (noted below where applicable). However most of their effect occurs after the comp callback has run, in routines that read the <code>&quot;rx-&gt;extflags&quot;</code> field which it populates. </p>
<p> In general the flags should be preserved in <code>&quot;rx-&gt;extflags&quot;</code> after compilation, although the regex engine might want to add or delete some of them to invoke or disable some special behavior in Perl. The flags along with any special behavior they cause are documented below: </p>
<p> The pattern modifiers: </p>
<dl>
<dt>&quot;/m&quot; - RXf_PMf_MULTILINE</dt>
<dd> <p> If this is in <code>&quot;rx-&gt;extflags&quot;</code> it will be passed to <code>&quot;Perl_fbm_instr&quot;</code> by <code>&quot;pp_split&quot;</code> which will treat the subject string as a multi-line string. </p>
 </dd>
<dt>&quot;/s&quot; - RXf_PMf_SINGLELINE</dt>
<dd>  </dd>
<dt>&quot;/i&quot; - RXf_PMf_FOLD</dt>
<dd>  </dd>
<dt>&quot;/x&quot; - RXf_PMf_EXTENDED</dt>
<dd> <p> If present on a regex, <code>&quot;#&quot;</code> comments will be handled differently by the tokenizer in some cases. </p>
<p> <font SIZE="-1">TODO:</font> Document those cases. </p>
 </dd>
<dt>&quot;/p&quot; - RXf_PMf_KEEPCOPY</dt>
<dd> <p> <font SIZE="-1">TODO:</font> Document this </p>
 </dd>
<dt>Character set</dt>
<dd> <p> The character set rules are determined by an enum that is contained in this field. This is still experimental and subject to change, but the current interface returns the rules by use of the in-line function <code>&quot;get_regex_charset(const U32 flags)&quot;</code>. The only currently documented value returned from it is <font SIZE="-1">REGEX_LOCALE_CHARSET,</font> which is set if <code>&quot;use locale&quot;</code> is in effect. If present in <code>&quot;rx-&gt;extflags&quot;</code>, <code>&quot;split&quot;</code> will use the locale dependent definition of whitespace when RXf_SKIPWHITE or RXf_WHITE is in effect. <font SIZE="-1">ASCII</font> whitespace is defined as per isSPACE, and by the internal macros <code>&quot;is_utf8_space&quot;</code> under <font SIZE="-1">UTF-8,</font> and <code>&quot;isSPACE_LC&quot;</code> under <code>&quot;use locale&quot;</code>. </p>
 </dd></dl>
<p> Additional flags: </p>
<dl>
<dt>RXf_SPLIT</dt>
<dd> <p> This flag was removed in perl 5.18.0. <code>&quot;split &#8216; &#8216;&quot;</code> is now special-cased solely in the parser. RXf_SPLIT is still #defined, so you can test for it. This is how it used to work: </p>
<p> If <code>&quot;split&quot;</code> is invoked as <code>&quot;split &#8216; &#8216;&quot;</code> or with no arguments (which really means <code>&quot;split(&#8216; &#8216;, $_)&quot;</code>, see split), Perl will set this flag. The regex engine can then check for it and set the <font SIZE="-1">SKIPWHITE</font> and <font SIZE="-1">WHITE</font> extflags. To do this, the Perl engine does: </p>
<pre><code>    if (flags &amp; RXf_SPLIT &amp;&amp; r-&gt;prelen == 1 &amp;&amp; r-&gt;precomp[0] == ' ')
        r-&gt;extflags |= (RXf_SKIPWHITE|RXf_WHITE);
</code></pre>
 </dd></dl>
<p> These flags can be set during compilation to enable optimizations in the <code>&quot;split&quot;</code> operator. </p>
<dl>
<dt>RXf_SKIPWHITE</dt>
<dd> <p> This flag was removed in perl 5.18.0. It is still #defined, so you can set it, but doing so will have no effect. This is how it used to work: </p>
<p> If the flag is present in <code>&quot;rx-&gt;extflags&quot;</code> <code>&quot;split&quot;</code> will delete whitespace from the start of the subject string before it&#8217;s operated on. What is considered whitespace depends on if the subject is a <font SIZE="-1">UTF-8</font> string and if the <code>&quot;RXf_PMf_LOCALE&quot;</code> flag is set. </p>
<p> If RXf_WHITE is set in addition to this flag, <code>&quot;split&quot;</code> will behave like <code>&quot;split &quot; &quot;&quot;</code> under the Perl engine. </p>
 </dd>
<dt>RXf_START_ONLY</dt>
<dd> <p> Tells the split operator to split the target string on newlines (<code>&quot;\n&quot;</code>) without invoking the regex engine. </p>
<p> Perl&#8217;s engine sets this if the pattern is <code>&quot;/^/&quot;</code> (<code>&quot;plen == 1 &amp;&amp; *exp == &#8216;^&#8216;&quot;</code>), even under <code>&quot;/^/s&quot;</code>; see split. Of course a different regex engine might want to use the same optimizations with a different syntax. </p>
 </dd>
<dt>RXf_WHITE</dt>
<dd> <p> Tells the split operator to split the target string on whitespace without invoking the regex engine. The definition of whitespace varies depending on if the target string is a <font SIZE="-1">UTF-8</font> string and on if RXf_PMf_LOCALE is set. </p>
<p> Perl&#8217;s engine sets this flag if the pattern is <code>&quot;\s+&quot;</code>. </p>
 </dd>
<dt>RXf_NULL</dt>
<dd> <p> Tells the split operator to split the target string on characters. The definition of character varies depending on if the target string is a <font SIZE="-1">UTF-8</font> string. </p>
<p> Perl&#8217;s engine sets this flag on empty patterns, this optimization makes <code>&quot;split //&quot;</code> much faster than it would otherwise be. It&#8217;s even faster than <code>&quot;unpack&quot;</code>. </p>
 </dd>
<dt>RXf_NO_INPLACE_SUBST</dt>
<dd> <p> Added in perl 5.18.0, this flag indicates that a regular expression might perform an operation that would interfere with inplace substitution. For instance it might contain lookbehind, or assign to non-magical variables (such as <code>$REGMARK</code> and <code>$REGERROR</code>) during matching. <code>&quot;s///&quot;</code> will skip certain optimisations when this is set. </p>
 </dd></dl>
<h3>exec</h3>
<pre><code>    I32 exec(pTHX_ REGEXP * const rx,
             char *stringarg, char* strend, char* strbeg,
             SSize_t minend, SV* sv,
             void* data, U32 flags);
</code></pre>
<p> Execute a regexp. The arguments are </p>
<dl>
<dt>rx</dt>
<dd> <p> The regular expression to execute. </p>
 </dd>
<dt>sv</dt>
<dd> <p> This is the <font SIZE="-1">SV</font> to be matched against. Note that the actual char array to be matched against is supplied by the arguments described below; the <font SIZE="-1">SV</font> is just used to determine UTF8ness, <code>&quot;pos()&quot;</code> etc. </p>
 </dd>
<dt>strbeg</dt>
<dd> <p> Pointer to the physical start of the string. </p>
 </dd>
<dt>strend</dt>
<dd> <p> Pointer to the character following the physical end of the string (i.e. the <code>&quot;\0&quot;</code>, if any). </p>
 </dd>
<dt>stringarg</dt>
<dd> <p> Pointer to the position in the string where matching should start; it might not be equal to <code>&quot;strbeg&quot;</code> (for example in a later iteration of <code>&quot;/.../g&quot;</code>). </p>
 </dd>
<dt>minend</dt>
<dd> <p> Minimum length of string (measured in bytes from <code>&quot;stringarg&quot;</code>) that must match; if the engine reaches the end of the match but hasn&#8217;t reached this position in the string, it should fail. </p>
 </dd>
<dt>data</dt>
<dd> <p> Optimisation data; subject to change. </p>
 </dd>
<dt>flags</dt>
<dd> <p> Optimisation flags; subject to change. </p>
 </dd></dl>
<h3>intuit</h3>
<pre><code>    char* intuit(pTHX_
                REGEXP * const rx,
                SV *sv,
                const char * const strbeg,
                char *strpos,
                char *strend,
                const U32 flags,
                struct re_scream_pos_data_s *data);
</code></pre>
<p> Find the start position where a regex match should be attempted, or possibly if the regex engine should not be run because the pattern can&#8217;t match. This is called, as appropriate, by the core, depending on the values of the <code>&quot;extflags&quot;</code> member of the <code>&quot;regexp&quot;</code> structure. </p>
<p> Arguments: </p>
<pre><code>    rx: the regex to match against
    sv: the SV being matched: only used for utf8 flag; the string
            itself is accessed via the pointers below. Note that on
            something like an overloaded SV, SvPOK(sv) may be false
            and the string pointers may point to something unrelated to
            the SV itself.
    strbeg: real beginning of string
    strpos: the point in the string at which to begin matching
    strend: pointer to the byte following the last char of the string
    flags currently unused; set to 0
    data: currently unused; set to NULL
</code></pre>
<h3>checkstr</h3>
<pre><code>    SV* checkstr(pTHX_ REGEXP * const rx);
</code></pre>
<p> Return a <font SIZE="-1">SV</font> containing a string that must appear in the pattern. Used by <code>&quot;split&quot;</code> for optimising matches.  </p>
<h3>free</h3>
<pre><code>    void free(pTHX_ REGEXP * const rx);
</code></pre>
<p> Called by Perl when it is freeing a regexp pattern so that the engine can release any resources pointed to by the <code>&quot;pprivate&quot;</code> member of the <code>&quot;regexp&quot;</code> structure. This is only responsible for freeing private data; Perl will handle releasing anything else contained in the <code>&quot;regexp&quot;</code> structure.  </p>
<h3>Numbered capture callbacks</h3>
<p> Called to get/set the value of <code>&quot;$`&quot;</code>, <code>&quot;$&#8216;&quot;</code>, <code>$&amp;</code> and their named equivalents, ${^PREMATCH}, ${^POSTMATCH} and ${^MATCH}, as well as the numbered capture groups (<code>$1</code>, <code>$2</code>, ...). </p>
<p> The <code>&quot;paren&quot;</code> parameter will be <code>1</code> for <code>$1</code>, <code>2</code> for <code>$2</code> and so forth, and have these symbolic values for the special variables: </p>
<pre><code>    ${^PREMATCH} RX_BUFF_IDX_CARET_PREMATCH
    ${^POSTMATCH} RX_BUFF_IDX_CARET_POSTMATCH
    ${^MATCH} RX_BUFF_IDX_CARET_FULLMATCH
    $` RX_BUFF_IDX_PREMATCH
    $' RX_BUFF_IDX_POSTMATCH
    $&amp; RX_BUFF_IDX_FULLMATCH
</code></pre>
<p> Note that in Perl 5.17.3 and earlier, the last three constants were also used for the caret variants of the variables. </p>
<p> The names have been chosen by analogy with Tie::Scalar methods names with an additional <font SIZE="-1"><code>LENGTH</code></font> callback for efficiency. However named capture variables are currently not tied internally but implemented via magic. </p>
<p> <i>numbered_buff_FETCH</i> </p>
<pre><code>    void numbered_buff_FETCH(pTHX_ REGEXP * const rx, const I32 paren,
                             SV * const sv);
</code></pre>
<p> Fetch a specified numbered capture. <code>&quot;sv&quot;</code> should be set to the scalar to return, the scalar is passed as an argument rather than being returned from the function because when it&#8217;s called Perl already has a scalar to store the value, creating another one would be redundant. The scalar can be set with <code>&quot;sv_setsv&quot;</code>, <code>&quot;sv_setpvn&quot;</code> and friends, see perlapi. </p>
<p> This callback is where Perl untaints its own capture variables under taint mode (see perlsec). See the <code>&quot;Perl_reg_numbered_buff_fetch&quot;</code> function in <i>regcomp.c</i> for how to untaint capture variables if that&#8217;s something you&#8217;d like your engine to do as well. </p>
<p> <i>numbered_buff_STORE</i> </p>
<pre><code>    void (*numbered_buff_STORE) (pTHX_
                                    REGEXP * const rx,
                                    const I32 paren,
                                    SV const * const value);
</code></pre>
<p> Set the value of a numbered capture variable. <code>&quot;value&quot;</code> is the scalar that is to be used as the new value. It&#8217;s up to the engine to make sure this is used as the new value (or reject it). </p>
<p> Example: </p>
<pre><code>    if (&quot;ook&quot; =~ /(o*)/) {
        # 'paren' will be '1' and 'value' will be 'ee'
        $1 =~ tr/o/e/;
    }
</code></pre>
<p> Perl&#8217;s own engine will croak on any attempt to modify the capture variables, to do this in another engine use the following callback (copied from <code>&quot;Perl_reg_numbered_buff_store&quot;</code>): </p>
<pre><code>    void
    Example_reg_numbered_buff_store(pTHX_
                                    REGEXP * const rx,
                                    const I32 paren,
                                    SV const * const value)
    {
        PERL_UNUSED_ARG(rx);
        PERL_UNUSED_ARG(paren);
        PERL_UNUSED_ARG(value);
        if (!PL_localizing)
            Perl_croak(aTHX_ PL_no_modify);
    }
</code></pre>
<p> Actually Perl will not <i>always</i> croak in a statement that looks like it would modify a numbered capture variable. This is because the <font SIZE="-1">STORE</font> callback will not be called if Perl can determine that it doesn&#8217;t have to modify the value. This is exactly how tied variables behave in the same situation: </p>
<pre><code>    package CaptureVar;
    use parent 'Tie::Scalar';
    sub TIESCALAR { bless [] }
    sub FETCH { undef }
    sub STORE { die &quot;This doesn't get called&quot; }
    package main;
    tie my $sv =&gt; &quot;CaptureVar&quot;;
    $sv =~ y/a/b/;
</code></pre>
<p> Because <code>$sv</code> is <code>&quot;undef&quot;</code> when the <code>&quot;y///&quot;</code> operator is applied to it, the transliteration won&#8217;t actually execute and the program won&#8217;t <code>&quot;die&quot;</code>. This is different to how 5.8 and earlier versions behaved since the capture variables were <font SIZE="-1">READONLY</font> variables then; now they&#8217;ll just die when assigned to in the default engine. </p>
<p> <i>numbered_buff_LENGTH</i> </p>
<pre><code>    I32 numbered_buff_LENGTH (pTHX_
                              REGEXP * const rx,
                              const SV * const sv,
                              const I32 paren);
</code></pre>
<p> Get the <code>&quot;length&quot;</code> of a capture variable. There&#8217;s a special callback for this so that Perl doesn&#8217;t have to do a <font SIZE="-1">FETCH</font> and run <code>&quot;length&quot;</code> on the result, since the length is (in Perl&#8217;s case) known from an offset stored in <code>&quot;rx-&gt;offs&quot;</code>, this is much more efficient: </p>
<pre><code>    I32 s1 = rx-&gt;offs[paren].start;
    I32 s2 = rx-&gt;offs[paren].end;
    I32 len = t1 - s1;
</code></pre>
<p> This is a little bit more complex in the case of <font SIZE="-1">UTF-8,</font> see what <code>&quot;Perl_reg_numbered_buff_length&quot;</code> does with is_utf8_string_loclen.  </p>
<h3>Named capture callbacks</h3>
<p> Called to get/set the value of <code>&quot;%+&quot;</code> and <code>&quot;%-&quot;</code>, as well as by some utility functions in re. </p>
<p> There are two callbacks, <code>&quot;named_buff&quot;</code> is called in all the cases the <font SIZE="-1">FETCH, STORE, DELETE, CLEAR, EXISTS</font> and <font SIZE="-1">SCALAR</font> Tie::Hash callbacks would be on changes to <code>&quot;%+&quot;</code> and <code>&quot;%-&quot;</code> and <code>&quot;named_buff_iter&quot;</code> in the same cases as <font SIZE="-1">FIRSTKEY</font> and <font SIZE="-1">NEXTKEY.</font> </p>
<p> The <code>&quot;flags&quot;</code> parameter can be used to determine which of these operations the callbacks should respond to. The following flags are currently defined: </p>
<p> Which Tie::Hash operation is being performed from the Perl level on <code>&quot;%+&quot;</code> or <code>&quot;%+&quot;</code>, if any: </p>
<pre><code>    RXapif_FETCH
    RXapif_STORE
    RXapif_DELETE
    RXapif_CLEAR
    RXapif_EXISTS
    RXapif_SCALAR
    RXapif_FIRSTKEY
    RXapif_NEXTKEY
</code></pre>
<p> If <code>&quot;%+&quot;</code> or <code>&quot;%-&quot;</code> is being operated on, if any. </p>
<pre><code>    RXapif_ONE /* %+ */
    RXapif_ALL /* %- */
</code></pre>
<p> If this is being called as <code>&quot;re::regname&quot;</code>, <code>&quot;re::regnames&quot;</code> or <code>&quot;re::regnames_count&quot;</code>, if any. The first two will be combined with <code>&quot;RXapif_ONE&quot;</code> or <code>&quot;RXapif_ALL&quot;</code>. </p>
<pre><code>    RXapif_REGNAME
    RXapif_REGNAMES
    RXapif_REGNAMES_COUNT
</code></pre>
<p> Internally <code>&quot;%+&quot;</code> and <code>&quot;%-&quot;</code> are implemented with a real tied interface via Tie::Hash::NamedCapture. The methods in that package will call back into these functions. However the usage of Tie::Hash::NamedCapture for this purpose might change in future releases. For instance this might be implemented by magic instead (would need an extension to mgvtbl). </p>
<p> <i>named_buff</i> </p>
<pre><code>    SV* (*named_buff) (pTHX_ REGEXP * const rx, SV * const key,
                           SV * const value, U32 flags);
</code></pre>
<p> <i>named_buff_iter</i> </p>
<pre><code>    SV* (*named_buff_iter) (pTHX_
                                REGEXP * const rx,
                                const SV * const lastkey,
                                const U32 flags);
</code></pre>
<h3>qr_package</h3>
<pre><code>    SV* qr_package(pTHX_ REGEXP * const rx);
</code></pre>
<p> The package the qr// magic object is blessed into (as seen by <code>&quot;ref qr//&quot;</code>). It is recommended that engines change this to their package name for identification regardless of if they implement methods on the object. </p>
<p> The package this method returns should also have the internal <code>&quot;Regexp&quot;</code> package in its <code>@ISA</code>. <code>&quot;qr//-&gt;isa(&quot;Regexp&quot;)&quot;</code> should always be true regardless of what engine is being used. </p>
<p> Example implementation might be: </p>
<pre><code>    SV*
    Example_qr_package(pTHX_ REGEXP * const rx)
    {
        PERL_UNUSED_ARG(rx);
        return newSVpvs(&quot;re::engine::Example&quot;);
    }
</code></pre>
<p> Any method calls on an object created with <code>&quot;qr//&quot;</code> will be dispatched to the package as a normal object. </p>
<pre><code>    use re::engine::Example;
    my $re = qr//;
    $re-&gt;meth; # dispatched to re::engine::Example::meth()
</code></pre>
<p> To retrieve the <code>&quot;REGEXP&quot;</code> object from the scalar in an <font SIZE="-1">XS</font> function use the <code>&quot;SvRX&quot;</code> macro, see ``<font SIZE="-1">REGEXP</font> Functions&#8217;&#8216; in perlapi. </p>
<pre><code>    void meth(SV * rv)
    PPCODE:
        REGEXP * re = SvRX(sv);
</code></pre>
<h3>dupe</h3>
<pre><code>    void* dupe(pTHX_ REGEXP * const rx, CLONE_PARAMS *param);
</code></pre>
<p> On threaded builds a regexp may need to be duplicated so that the pattern can be used by multiple threads. This routine is expected to handle the duplication of any private data pointed to by the <code>&quot;pprivate&quot;</code> member of the <code>&quot;regexp&quot;</code> structure. It will be called with the preconstructed new <code>&quot;regexp&quot;</code> structure as an argument, the <code>&quot;pprivate&quot;</code> member will point at the <code>old</code> private structure, and it is this routine&#8217;s responsibility to construct a copy and return a pointer to it (which Perl will then use to overwrite the field as passed to this routine.) </p>
<p> This allows the engine to dupe its private data but also if necessary modify the final structure if it really must. </p>
<p> On unthreaded builds this field doesn&#8217;t exist.  </p>
<h3>op_comp</h3>
<p> This is private to the Perl core and subject to change. Should be left null.  </p>
<h2>The REGEXP structure</h2>
<p> The <font SIZE="-1">REGEXP</font> struct is defined in <i>regexp.h</i>. All regex engines must be able to correctly build such a structure in their ``comp&#8217;&#8216; routine. </p>
<p> The <font SIZE="-1">REGEXP</font> structure contains all the data that Perl needs to be aware of to properly work with the regular expression. It includes data about optimisations that Perl can use to determine if the regex engine should really be used, and various other control info that is needed to properly execute patterns in various contexts, such as if the pattern anchored in some way, or what flags were used during the compile, or if the program contains special constructs that Perl needs to be aware of. </p>
<p> In addition it contains two fields that are intended for the private use of the regex engine that compiled the pattern. These are the <code>&quot;intflags&quot;</code> and <code>&quot;pprivate&quot;</code> members. <code>&quot;pprivate&quot;</code> is a void pointer to an arbitrary structure, whose use and management is the responsibility of the compiling engine. Perl will never modify either of these values. </p>
<pre><code>    typedef struct regexp {
        /* what engine created this regexp? */
        const struct regexp_engine* engine;
        /* what re is this a lightweight copy of? */
        struct regexp* mother_re;
        /* Information about the match that the Perl core uses to manage
         * things */
        U32 extflags; /* Flags used both externally and internally */
        I32 minlen; /* mininum possible number of chars in */
                           string to match */
        I32 minlenret; /* mininum possible number of chars in $&amp; */
        U32 gofs; /* chars left of pos that we search from */
        /* substring data about strings that must appear
           in the final match, used for optimisations */
        struct reg_substr_data *substrs;
        U32 nparens; /* number of capture groups */
        /* private engine specific data */
        U32 intflags; /* Engine Specific Internal flags */
        void *pprivate; /* Data private to the regex engine which
                           created this object. */
        /* Data about the last/current match. These are modified during
         * matching*/
        U32 lastparen; /* highest close paren matched ($+) */
        U32 lastcloseparen; /* last close paren matched ($^N) */
        regexp_paren_pair *offs; /* Array of offsets for (@-) and
                                     (@+) */
        char *subbeg; /* saved or original string so \digit works
                          forever. */
        SV_SAVED_COPY /* If non-NULL, SV which is COW from original */
        I32 sublen; /* Length of string pointed by subbeg */
        I32 suboffset; /* byte offset of subbeg from logical start of
                           str */
        I32 subcoffset; /* suboffset equiv, but in chars (for @-/@+) */
        /* Information about the match that isn't often used */
        I32 prelen; /* length of precomp */
        const char *precomp; /* pre-compilation regular expression */
        char *wrapped; /* wrapped version of the pattern */
        I32 wraplen; /* length of wrapped */
        I32 seen_evals; /* number of eval groups in the pattern - for
                             security checks */
        HV *paren_names; /* Optional hash of paren names */
        /* Refcount of this regexp */
        I32 refcnt; /* Refcount of this regexp */
    } regexp;
</code></pre>
<p> The fields are discussed in more detail below:  </p>
<h3>engine</h3>
<p> This field points at a <code>&quot;regexp_engine&quot;</code> structure which contains pointers to the subroutines that are to be used for performing a match. It is the compiling routine&#8217;s responsibility to populate this field before returning the regexp object. </p>
<p> Internally this is set to <code>&quot;NULL&quot;</code> unless a custom engine is specified in <code>$^H{regcomp}</code>, Perl&#8217;s own set of callbacks can be accessed in the struct pointed to by <code>&quot;RE_ENGINE_PTR&quot;</code>.  </p>
<h3>mother_re</h3>
<p> <font SIZE="-1">TODO,</font> see &lt;<a rel="nofollow" href="http://www.mail-archive.com/perl5-changes@perl.org/msg17328.html">http://www.mail-archive.com/perl5-changes@perl.org/msg17328.html</a>&gt;  </p>
<h3>extflags</h3>
<p> This will be used by Perl to see what flags the regexp was compiled with, this will normally be set to the value of the flags parameter by the comp callback. See the comp documentation for valid flags.  </p>
<h3>minlen minlenret</h3>
<p> The minimum string length (in characters) required for the pattern to match. This is used to prune the search space by not bothering to match any closer to the end of a string than would allow a match. For instance there is no point in even starting the regex engine if the minlen is 10 but the string is only 5 characters long. There is no way that the pattern can match. </p>
<p> <code>&quot;minlenret&quot;</code> is the minimum length (in characters) of the string that would be found in $&amp; after a match. </p>
<p> The difference between <code>&quot;minlen&quot;</code> and <code>&quot;minlenret&quot;</code> can be seen in the following pattern: </p>
<pre><code>    /ns(?=\d)/
</code></pre>
<p> where the <code>&quot;minlen&quot;</code> would be 3 but <code>&quot;minlenret&quot;</code> would only be 2 as the \d is required to match but is not actually included in the matched content. This distinction is particularly important as the substitution logic uses the <code>&quot;minlenret&quot;</code> to tell if it can do in-place substitutions (these can result in considerable speed-up).  </p>
<h3>gofs</h3>
<p> Left offset from <code>pos()</code> to start match at.  </p>
<h3>substrs</h3>
<p> Substring data about strings that must appear in the final match. This is currently only used internally by Perl&#8217;s engine, but might be used in the future for all engines for optimisations.  </p>
<h3>nparens, lastparen, and lastcloseparen</h3>
<p> These fields are used to keep track of: how many paren capture groups there are in the pattern; which was the highest paren to be closed (see ``$+&#8216;&#8216; in perlvar); and which was the most recent paren to be closed (see ``$^N&#8217;&#8216; in perlvar).  </p>
<h3>intflags</h3>
<p> The engine&#8217;s private copy of the flags the pattern was compiled with. Usually this is the same as <code>&quot;extflags&quot;</code> unless the engine chose to modify one of them.  </p>
<h3>pprivate</h3>
<p> A void* pointing to an engine-defined data structure. The Perl engine uses the <code>&quot;regexp_internal&quot;</code> structure (see ``Base Structures&#8217;&#8216; in perlreguts) but a custom engine should use something else.  </p>
<h3>offs</h3>
<p> A <code>&quot;regexp_paren_pair&quot;</code> structure which defines offsets into the string being matched which correspond to the <code>$&amp;</code> and <code>$1</code>, <code>$2</code> etc. captures, the <code>&quot;regexp_paren_pair&quot;</code> struct is defined as follows: </p>
<pre><code>    typedef struct regexp_paren_pair {
        I32 start;
        I32 end;
    } regexp_paren_pair;
</code></pre>
<p> If <code>&quot;-&gt;offs[num].start&quot;</code> or <code>&quot;-&gt;offs[num].end&quot;</code> is <code>&quot;-1&quot;</code> then that capture group did not match. <code>&quot;-&gt;offs[0].start/end&quot;</code> represents <code>$&amp;</code> (or <code>&quot;${^MATCH}&quot;</code> under <code>&quot;/p&quot;</code>) and <code>&quot;-&gt;offs[paren].end&quot;</code> matches <code>$$paren</code> where <code>$paren </code>= 1&gt;.  </p>
<h3>precomp prelen</h3>
<p> Used for optimisations. <code>&quot;precomp&quot;</code> holds a copy of the pattern that was compiled and <code>&quot;prelen&quot;</code> its length. When a new pattern is to be compiled (such as inside a loop) the internal <code>&quot;regcomp&quot;</code> operator checks if the last compiled <code>&quot;REGEXP&quot;</code>&#8216;s <code>&quot;precomp&quot;</code> and <code>&quot;prelen&quot;</code> are equivalent to the new one, and if so uses the old pattern instead of compiling a new one. </p>
<p> The relevant snippet from <code>&quot;Perl_pp_regcomp&quot;</code>: </p>
<pre><code>        if (!re || !re-&gt;precomp || re-&gt;prelen != (I32)len ||
            memNE(re-&gt;precomp, t, len))
        /* Compile a new pattern */
</code></pre>
<h3>paren_names</h3>
<p> This is a hash used internally to track named capture groups and their offsets. The keys are the names of the buffers the values are dualvars, with the <font SIZE="-1">IV</font> slot holding the number of buffers with the given name and the pv being an embedded array of I32. The values may also be contained independently in the data array in cases where named backreferences are used.  </p>
<h3>substrs</h3>
<p> Holds information on the longest string that must occur at a fixed offset from the start of the pattern, and the longest string that must occur at a floating offset from the start of the pattern. Used to do Fast-Boyer-Moore searches on the string to find out if its worth using the regex engine at all, and if so where in the string to search.  </p>
<h3>subbeg sublen saved_copy suboffset subcoffset</h3>
<p> Used during the execution phase for managing search and replace patterns, and for providing the text for <code>$&amp;</code>, <code>$1</code> etc. <code>&quot;subbeg&quot;</code> points to a buffer (either the original string, or a copy in the case of <code>&quot;RX_MATCH_COPIED(rx)&quot;</code>), and <code>&quot;sublen&quot;</code> is the length of the buffer. The <code>&quot;RX_OFFS&quot;</code> start and end indices index into this buffer. </p>
<p> In the presence of the <code>&quot;REXEC_COPY_STR&quot;</code> flag, but with the addition of the <code>&quot;REXEC_COPY_SKIP_PRE&quot;</code> or <code>&quot;REXEC_COPY_SKIP_POST&quot;</code> flags, an engine can choose not to copy the full buffer (although it must still do so in the presence of <code>&quot;RXf_PMf_KEEPCOPY&quot;</code> or the relevant bits being set in <code>&quot;PL_sawampersand&quot;</code>). In this case, it may set <code>&quot;suboffset&quot;</code> to indicate the number of bytes from the logical start of the buffer to the physical start (i.e. <code>&quot;subbeg&quot;</code>). It should also set <code>&quot;subcoffset&quot;</code>, the number of characters in the offset. The latter is needed to support <code>&quot;@-&quot;</code> and <code>&quot;@+&quot;</code> which work in characters, not bytes.  </p>
<h3>wrapped wraplen</h3>
<p> Stores the string <code>&quot;qr//&quot;</code> stringifies to. The Perl engine for example stores <code>&quot;(?^:eek)&quot;</code> in the case of <code>&quot;qr/eek/&quot;</code>. </p>
<p> When using a custom engine that doesn&#8217;t support the <code>&quot;(?:)&quot;</code> construct for inline modifiers, it&#8217;s probably best to have <code>&quot;qr//&quot;</code> stringify to the supplied pattern, note that this will create undesired patterns in cases such as: </p>
<pre><code>    my $x = qr/a|b/; # &quot;a|b&quot;
    my $y = qr/c/i; # &quot;c&quot;
    my $z = qr/$x$y/; # &quot;a|bc&quot;
</code></pre>
<p> There&#8217;s no solution for this problem other than making the custom engine understand a construct like <code>&quot;(?:)&quot;</code>.  </p>
<h3>seen_evals</h3>
<p> This stores the number of eval groups in the pattern. This is used for security purposes when embedding compiled regexes into larger patterns with <code>&quot;qr//&quot;</code>.  </p>
<h3>refcnt</h3>
<p> The number of times the structure is referenced. When this falls to 0, the regexp is automatically freed by a call to pregfree. This should be set to 1 in each engine&#8217;s ``comp&#8217;&#8216; routine.  </p>
<h2>HISTORY</h2>
<p> Originally part of perlreguts.  </p>
<h2>AUTHORS</h2>
<p> Originally written by Yves Orton, expanded by Ævar Arnfjörð Bjarmason.  </p>
<h2>LICENSE</h2>
<p> Copyright 2006 Yves Orton and 2007 Ævar Arnfjörð Bjarmason. </p>
<p> This program is free software; you can redistribute it and/or modify it under the same terms as Perl itself. </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">Callbacks</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAE">comp</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">exec</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">intuit</a></dt>
<dd>  </dd>
<dt><a href="#lbAH">checkstr</a></dt>
<dd>  </dd>
<dt><a href="#lbAI">free</a></dt>
<dd>  </dd>
<dt><a href="#lbAJ">Numbered capture callbacks</a></dt>
<dd>  </dd>
<dt><a href="#lbAK">Named capture callbacks</a></dt>
<dd>  </dd>
<dt><a href="#lbAL">qr_package</a></dt>
<dd>  </dd>
<dt><a href="#lbAM">dupe</a></dt>
<dd>  </dd>
<dt><a href="#lbAN">op_comp</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAO">The REGEXP structure</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAP">engine</a></dt>
<dd>  </dd>
<dt><a href="#lbAQ">mother_re</a></dt>
<dd>  </dd>
<dt><a href="#lbAR">extflags</a></dt>
<dd>  </dd>
<dt><a href="#lbAS">minlen minlenret</a></dt>
<dd>  </dd>
<dt><a href="#lbAT">gofs</a></dt>
<dd>  </dd>
<dt><a href="#lbAU">substrs</a></dt>
<dd>  </dd>
<dt><a href="#lbAV">nparens, lastparen, and lastcloseparen</a></dt>
<dd>  </dd>
<dt><a href="#lbAW">intflags</a></dt>
<dd>  </dd>
<dt><a href="#lbAX">pprivate</a></dt>
<dd>  </dd>
<dt><a href="#lbAY">offs</a></dt>
<dd>  </dd>
<dt><a href="#lbAZ">precomp prelen</a></dt>
<dd>  </dd>
<dt><a href="#lbBA">paren_names</a></dt>
<dd>  </dd>
<dt><a href="#lbBB">substrs</a></dt>
<dd>  </dd>
<dt><a href="#lbBC">subbeg sublen saved_copy suboffset subcoffset</a></dt>
<dd>  </dd>
<dt><a href="#lbBD">wrapped wraplen</a></dt>
<dd>  </dd>
<dt><a href="#lbBE">seen_evals</a></dt>
<dd>  </dd>
<dt><a href="#lbBF">refcnt</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbBG">HISTORY</a></dt>
<dd>  </dd>
<dt><a href="#lbBH">AUTHORS</a></dt>
<dd>  </dd>
<dt><a href="#lbBI">LICENSE</a></dt>
<dd>  </dd></dl>
