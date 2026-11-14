---
title: "perlexperiment(1)"
name: "perlexperiment"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlexperiment/"
description: "perlexperiment – A listing of experimental features in Perl"
---

<h2 class="name">NAME</h2>
<p> perlexperiment &#8211; A listing of experimental features in Perl </p>
<h2>DESCRIPTION</h2>
<p> This document lists the current and past experimental features in the perl core. Although all of these are documented with their appropriate topics, this succinct listing gives you an overview and basic facts about their status. </p>
<p> So far we&#8217;ve merely tried to find and list the experimental features and infer their inception, versions, etc. There&#8217;s a lot of speculation here.</p>
<h3>Current experiments</h3>
<dl>
<dt>Smart match (&quot;~~&quot;)</p>
<dd> Introduced in Perl 5.10.0 </p>
<p> Modified in Perl 5.10.1, 5.12.0 </p>
<p> Using this feature triggers warnings in the category <tt>&quot;experimental::smartmatch&quot;</tt>. </p>
<p> The ticket for this feature is [perl #119317] &lt;<a rel="nofollow" href="https://rt.perl.org/rt3/Ticket/Display.html?id=119317">https://rt.perl.org/rt3/Ticket/Display.html?id=119317</a>&gt;.</p>
<dt>Pluggable keywords</p>
<dd> The ticket for this feature is [perl #119455] &lt;<a rel="nofollow" href="https://rt.perl.org/rt3/Ticket/Display.html?id=119455">https://rt.perl.org/rt3/Ticket/Display.html?id=119455</a>&gt;. </p>
<p> See &#8220;PL_keyword_plugin&#8221; in perlapi for the mechanism. </p>
<p> Introduced in Perl 5.11.2</p>
<dt>Regular Expression Set Operations</p>
<dd> Introduced in Perl 5.18 </p>
<p> The ticket for this feature is [perl #119451] &lt;<a rel="nofollow" href="https://rt.perl.org/rt3/Ticket/Display.html?id=119451">https://rt.perl.org/rt3/Ticket/Display.html?id=119451</a>&gt;. </p>
<p> See also: &#8220;Extended Bracketed Character Classes&#8221; in perlrecharclass </p>
<p> Using this feature triggers warnings in the category <tt>&quot;experimental::regex_sets&quot;</tt>.</p>
<dt>Subroutine signatures</p>
<dd> Introduced in Perl 5.20.0 </p>
<p> Using this feature triggers warnings in the category <tt>&quot;experimental::signatures&quot;</tt>. </p>
<p> The ticket for this feature is [perl #121481] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=121481">https://rt.perl.org/Ticket/Display.html?id=121481</a>&gt;.</p>
<dt>Aliasing via reference</p>
<dd> Introduced in Perl 5.22.0 </p>
<p> Using this feature triggers warnings in the category <tt>&quot;experimental::refaliasing&quot;</tt>. </p>
<p> The ticket for this feature is [perl #122947] &lt;<a rel="nofollow" href="https://rt.perl.org/rt3/Ticket/Display.html?id=122947">https://rt.perl.org/rt3/Ticket/Display.html?id=122947</a>&gt;. </p>
<p> See also: &#8220;Assigning to References&#8221; in perlref</p>
<dt>The &quot;const&quot; attribute</p>
<dd> Introduced in Perl 5.22.0 </p>
<p> Using this feature triggers warnings in the category <tt>&quot;experimental::const_attr&quot;</tt>. </p>
<p> The ticket for this feature is [perl #123630] &lt;<a rel="nofollow" href="https://rt.perl.org/rt3/Ticket/Display.html?id=123630">https://rt.perl.org/rt3/Ticket/Display.html?id=123630</a>&gt;. </p>
<p> See also: &#8220;Constant Functions&#8221; in perlsub</p>
<dt>use re &#8216;strict&#8217;;</p>
<dd> Introduced in Perl 5.22.0 </p>
<p> Using this feature triggers warnings in the category <tt>&quot;experimental::re_strict&quot;</tt>. </p>
<p> See &#8220;&#8217;strict&#8217; mode&#8221; in re</p>
<dt>The &lt;:win32&gt; <font SIZE="-1">IO</font> pseudolayer</p>
<dd> The ticket for this feature is [perl #119453] &lt;<a rel="nofollow" href="https://rt.perl.org/rt3/Ticket/Display.html?id=119453">https://rt.perl.org/rt3/Ticket/Display.html?id=119453</a>&gt;. </p>
<p> See also perlrun</p>
<dt>Declaring a reference to a variable</p>
<dd> Introduced in Perl 5.26.0 </p>
<p> Using this feature triggers warnings in the category <tt>&quot;experimental::declared_refs&quot;</tt>. </p>
<p> The ticket for this feature is [perl #128654] &lt;<a rel="nofollow" href="https://rt.perl.org/rt3/Ticket/Display.html?id=128654">https://rt.perl.org/rt3/Ticket/Display.html?id=128654</a>&gt;. </p>
<p> See also: &#8220;Declaring a Reference to a Variable&#8221; in perlref</p>
<dt>There is an &quot;installhtml&quot; target in the Makefile.</p>
<dd> The ticket for this feature is [perl #116487] &lt;<a rel="nofollow" href="https://rt.perl.org/rt3/Ticket/Display.html?id=116487">https://rt.perl.org/rt3/Ticket/Display.html?id=116487</a>&gt;.</p>
<dt>Unicode in Perl on <font SIZE="-1">EBCDIC</font></p>
<dd>
<dt>Script runs</p>
<dd> Introduced in Perl 5.28.0 </p>
<p> Using this feature triggers warnings in the category <tt>&quot;experimental::script_run&quot;</tt>. </p>
<p> See also: &#8220;Script Runs&#8221; in perlre</p>
<dt>Alphabetic assertions</p>
<dd> Introduced in Perl 5.28.0 </p>
<p> Using this feature triggers warnings in the category <tt>&quot;experimental::alpha_assertions&quot;</tt>. </p>
<p> See also: &#8220;Extended Patterns&#8221; in perlre.</dl>
<h3>Accepted features</h3>
<p> These features were so wildly successful and played so well with others that we decided to remove their experimental status and admit them as full, stable features in the world of Perl, lavishing all the benefits and luxuries thereof. They are also awarded +5 Stability and +3 Charisma.</p>
<dl>
<dt>64-bit support</p>
<dd> Introduced in Perl 5.005</p>
<dt>die accepts a reference</p>
<dd> Introduced in Perl 5.005</p>
<dt><font SIZE="-1">DB</font> module</p>
<dd> Introduced in Perl 5.6.0 </p>
<p> See also perldebug, perldebtut</p>
<dt>Weak references</p>
<dd> Introduced in Perl 5.6.0</p>
<dt>Internal file glob</p>
<dd> Introduced in Perl 5.6.0</p>
<dt><code>fork()</code> emulation</p>
<dd> Introduced in Perl 5.6.1 </p>
<p> See also perlfork</p>
<dt>-Dusemultiplicity -Duseithreads</p>
<dd> Introduced in Perl 5.6.0 </p>
<p> Accepted in Perl 5.8.0</p>
<dt>Support for long doubles</p>
<dd> Introduced in Perl 5.6.0 </p>
<p> Accepted in Perl 5.8.1</p>
<dt>The &quot;\N&quot; regex character class</p>
<dd> The <tt>&quot;\N&quot;</tt> character class, not to be confused with the named character sequence <tt>&quot;\N{NAME}&quot;</tt>, denotes any non-newline character in a regular expression. </p>
<p> Introduced in Perl 5.12 </p>
<p> Exact version of acceptance unclear, but no later than Perl 5.18.</p>
<dt>&quot;(?{code})&quot; and &quot;(??{ code })&quot;</p>
<dd> Introduced in Perl 5.6.0 </p>
<p> Accepted in Perl 5.20.0 </p>
<p> See also perlre</p>
<dt>Linux abstract Unix domain sockets</p>
<dd> Introduced in Perl 5.9.2 </p>
<p> Accepted before Perl 5.20.0. The Socket library is now primarily maintained on <font SIZE="-1">CPAN,</font> rather than in the perl core. </p>
<p> See also Socket</p>
<dt>Lvalue subroutines</p>
<dd> Introduced in Perl 5.6.0 </p>
<p> Accepted in Perl 5.20.0 </p>
<p> See also perlsub</p>
<dt>Backtracking control verbs</p>
<dd> <tt>&quot;(*ACCEPT)&quot;</tt> </p>
<p> Introduced in Perl 5.10 </p>
<p> Accepted in Perl 5.20.0</p>
<dt>The &lt;:pop&gt; <font SIZE="-1">IO</font> pseudolayer</p>
<dd> See also perlrun </p>
<p> Accepted in Perl 5.20.0</p>
<dt>&quot;\s&quot; in regexp matches vertical tab</p>
<dd> Accepted in Perl 5.22.0</p>
<dt>Postfix dereference syntax</p>
<dd> Introduced in Perl 5.20.0 </p>
<p> Accepted in Perl 5.24.0</p>
<dt>Lexical subroutines</p>
<dd> Introduced in Perl 5.18.0 </p>
<p> Accepted in Perl 5.26.0</p>
<dt>String- and number-specific bitwise operators</p>
<dd> Introduced in Perl 5.22.0 </p>
<p> Accepted in Perl 5.28.0</dl>
<h3>Removed features</h3>
<p> These features are no longer considered experimental and their functionality has disappeared. It&#8217;s your own fault if you wrote production programs using these features after we explicitly told you not to (see perlpolicy).</p>
<dl>
<dt>5.005-style threading</p>
<dd> Introduced in Perl 5.005 </p>
<p> Removed in Perl 5.10</p>
<dt>perlcc</p>
<dd> Introduced in Perl 5.005 </p>
<p> Moved from Perl 5.9.0 to <font SIZE="-1">CPAN</font></p>
<dt>The pseudo-hash data type</p>
<dd> Introduced in Perl 5.6.0 </p>
<p> Removed in Perl 5.9.0</p>
<dt>GetOpt::Long Options can now take multiple values at once (experimental)</p>
<dd> <tt>&quot;Getopt::Long&quot;</tt> upgraded to version 2.35 </p>
<p> Removed in Perl 5.8.8</p>
<dt>Assertions</p>
<dd> The <tt>&quot;-A&quot;</tt> command line switch </p>
<p> Introduced in Perl 5.9.0 </p>
<p> Removed in Perl 5.9.5</p>
<dt>Test::Harness::Straps</p>
<dd> Moved from Perl 5.10.1 to <font SIZE="-1">CPAN</font></p>
<dt>&quot;legacy&quot;</p>
<dd> The experimental <tt>&quot;legacy&quot;</tt> pragma was swallowed by the <tt>&quot;feature&quot;</tt> pragma. </p>
<p> Introduced in Perl 5.11.2 </p>
<p> Removed in Perl 5.11.3</p>
<dt>Lexical $_</p>
<dd> Using this feature triggered warnings in the category <tt>&quot;experimental::lexical_topic&quot;</tt>. </p>
<p> Introduced in Perl 5.10.0 </p>
<p> Removed in Perl 5.24.0</p>
<dt>Array and hash container functions accept references</p>
<dd> Using this feature triggered warnings in the category <tt>&quot;experimental::autoderef&quot;</tt>. </p>
<p> Superseded by &#8220;Postfix dereference syntax&#8221;. </p>
<p> Introduced in Perl 5.14.0 </p>
<p> Removed in Perl 5.24.0</p>
<dt>&quot;our&quot; can have an experimental optional attribute &quot;unique&quot;</p>
<dd> Introduced in Perl 5.8.0 </p>
<p> Deprecated in Perl 5.10.0 </p>
<p> Removed in Perl 5.28.0</dl>
<h2>SEE ALSO</h2>
<p> For a complete list of features check feature.</p>
<h2>AUTHORS</h2>
<p> brian d foy <tt>&quot;&lt;brian.d.foy [at] gmail.com&gt;&quot;</tt> </p>
<p> Sébastien Aperghis-Tramoni <tt>&quot;&lt;saper [at] cpan.org&gt;&quot;</tt></p>
<h2>COPYRIGHT</h2>
<p> Copyright 2010, brian d foy <tt>&quot;&lt;brian.d.foy [at] gmail.com&gt;&quot;</tt></p>
<h2>LICENSE</h2>
<p> You can use and redistribute this document under the same terms as Perl itself. </p>
<h2>Index</h2>
