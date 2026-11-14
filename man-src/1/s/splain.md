---
title: "splain(1)"
name: "splain"
section: "1"
letter: "s"
url: "/docs/linux/man/1-splain/"
description: "diagnostics, splain – produce verbose warning diagnostics"
---

<h2 class="name">NAME</h2>
<p> diagnostics, splain &#8211; produce verbose warning diagnostics </p>
<h2>SYNOPSIS</h2>
<p> Using the <tt>&quot;diagnostics&quot;</tt> pragma: </p>
<pre><code>
use diagnostics;
use diagnostics - verbose;
enable diagnostics;
disable diagnostics;
</code></pre>
<p> Using the <tt>&quot;splain&quot;</tt> standalone filter program: </p>
<p>perl program 2 &gt; diag.out<br />
                     splain[-v][-p] diag.out</p>
<p> Using diagnostics to get stack traces from a misbehaving script: </p>
<pre>
    perl -Mdiagnostics=-traceonly my_script.pl
</pre>
<h2>DESCRIPTION</h2>
<h3>The diagnostics Pragma</h3>
<p> This module extends the terse diagnostics normally emitted by both the perl compiler and the perl interpreter (from running perl with a -w switch or <tt>&quot;use warnings&quot;</tt>), augmenting them with the more explicative and endearing descriptions found in perldiag. Like the other pragmata, it affects the compilation phase of your program rather than merely the execution phase. </p>
<p> To use in your program as a pragma, merely invoke </p>
<pre>
    use diagnostics;
</pre>
<p> at the start (or near the start) of your program. (Note that this <i>does</i> enable perl&#8217;s <code>-w</code> flag.) Your whole compilation will then be subject(ed :-) to the enhanced diagnostics. These still go out <font SIZE="-1"><code>STDERR</code></font>. </p>
<p> Due to the interaction between runtime and compiletime issues, and because it&#8217;s probably not a very good idea anyway, you may not use <tt>&quot;no diagnostics&quot;</tt> to turn them off at compiletime. However, you may control their behaviour at runtime using the <code>disable()</code> and <code>enable()</code> methods to turn them off and on respectively. </p>
<p> The <code>-verbose</code> flag first prints out the perldiag introduction before any other diagnostics. The <tt>$diagnostics::PRETTY</tt> variable can generate nicer escape sequences for pagers. </p>
<p> Warnings dispatched from perl itself (or more accurately, those that match descriptions found in perldiag) are only displayed once (no duplicate descriptions). User code generated warnings a la <code>warn()</code> are unaffected, allowing duplicate user messages to be displayed. </p>
<p> This module also adds a stack trace to the error message when perl dies. This is useful for pinpointing what caused the death. The <code>-traceonly</code> (or just <code>-t</code>) flag turns off the explanations of warning messages leaving just the stack traces. So if your script is dieing, run it again with </p>
<pre>
  perl -Mdiagnostics=-traceonly my_bad_script
</pre>
<p> to see the call stack at the time of death. By supplying the <code>-warntrace</code> (or just <code>-w</code>) flag, any warnings emitted will also come with a stack trace.</p>
<h3>The <i>splain</i> Program</h3>
<p> While apparently a whole nuther program, <i>splain</i> is actually nothing more than a link to the (executable) <i>diagnostics.pm</i> module, as well as a link to the <i>diagnostics.pod</i> documentation. The <code>-v</code> flag is like the <tt>&quot;use diagnostics -verbose&quot;</tt> directive. The <code>-p</code> flag is like the <tt>$diagnostics::PRETTY</tt> variable. Since you&#8217;re post-processing with <i>splain</i>, there&#8217;s no sense in being able to <code>enable()</code> or <code>disable()</code> processing. </p>
<p> Output from <i>splain</i> is directed to <font SIZE="-1"><code>STDOUT</code></font>, unlike the pragma.</p>
<h2>EXAMPLES</h2>
<p> The following file is certain to trigger a few errors at both runtime and compiletime: </p>
<p>use diagnostics;<br />
print NOWHERE &#8220;nothing
&#8221;;<br />
print STDERR &#8220;
	This message should be unadorned.
&#8221;;<br />
warn &#8220;	This is a user warning&#8221;;<br />
print &#8220;
DIAGNOSTIC TESTER: Please enter a &lt;CR&gt; here: &#8220;;<br />
my $a, $b = scalar&lt;STDIN&gt;;<br />
print &#8220;
&#8221;;<br />
print $x / $y;</p>
<p> If you prefer to run your program first and look at its problem afterwards, do this: </p>
<pre>
    perl -w test.pl 2&gt;test.out
    ./splain &lt; test.out
</pre>
<p> Note that this is not in general possible in shells of more dubious heritage, as the theoretical </p>
<pre>
    (perl -w test.pl &gt;/dev/tty) &gt;&amp; test.out
    ./splain &lt; test.out
</pre>
<p> Because you just moved the existing <code>stdout</code> to somewhere else. </p>
<p> If you don&#8217;t want to modify your source code, but still have on-the-fly warnings, do this: </p>
<pre>
    exec 3&gt;&amp;1; perl -w test.pl 2&gt;&amp;1 1&gt;&amp;3 3&gt;&amp;- | splain 1&gt;&amp;2 3&gt;&amp;-
</pre>
<p> Nifty, eh? </p>
<p> If you want to control warnings on the fly, do something like this. Make sure you do the <tt>&quot;use&quot;</tt> first, or you won&#8217;t be able to get at the <code>enable()</code> or <code>disable()</code> methods. </p>
<pre><code>
use diagnostics;
#checks entire compilation phase
    print "
time for 1st bogus diags: SQUAWKINGS
";
print BOGUS1 'nada';
print "done with 1st bogus
";
disable diagnostics;
#only turns off runtime warnings
    print "
time for 2nd bogus: (squelched)
";
print BOGUS2 'nada';
print "done with 2nd bogus
";
enable diagnostics;
#turns back on runtime warnings
    print "
time for 3rd bogus: SQUAWKINGS
";
print BOGUS3 'nada';
print "done with 3rd bogus
";
disable diagnostics;
print "
time for 4th bogus: (squelched)
";
print BOGUS4 'nada';
print "done with 4th bogus
";
</code></pre>
<h2>INTERNALS</h2>
<p> Diagnostic messages derive from the <i>perldiag.pod</i> file when available at runtime. Otherwise, they may be embedded in the file itself when the splain package is built. See the <i>Makefile</i> for details. </p>
<p> If an extant <tt>$SIG</tt>{__WARN__} handler is discovered, it will continue to be honored, but only after the <code>diagnostics::splainthis()</code> function (the module&#8217;s <tt>$SIG</tt>{__WARN__} interceptor) has had its way with your warnings. </p>
<p> There is a <tt>$diagnostics::DEBUG</tt> variable you may set if you&#8217;re desperately curious what sorts of things are being intercepted. </p>
<pre>
    BEGIN { $diagnostics::DEBUG = 1 }
</pre>
<h2>BUGS</h2>
<p> Not being able to say &#8220;no diagnostics&#8221; is annoying, but may not be insurmountable. </p>
<p> The <tt>&quot;-pretty&quot;</tt> directive is called too late to affect matters. You have to do this instead, and <i>before</i> you load the module. </p>
<pre>
    BEGIN { $diagnostics::PRETTY = 1 }
</pre>
<p> I could start up faster by delaying compilation until it should be needed, but this gets a &#8220;panic: top_level&#8221; when using the pragma form in Perl 5.001e. </p>
<p> While it&#8217;s true that this documentation is somewhat subserious, if you use a program named <i>splain</i>, you should expect a bit of whimsy.</p>
<h2>AUTHOR</h2>
<p> Tom Christiansen &lt;<i>tchrist [at] mox.perl.com</i>&gt;, 25 June 1995. </p>
<h2>Index</h2>
<dt><a href="#lbAG">EXAMPLES</a></p>
<dd>
<dt><a href="#lbAH">INTERNALS</a></p>
<dd>
<dt><a href="#lbAI">BUGS</a></p>
<dd>
<dt><a href="#lbAJ">AUTHOR</a></p>
<dd></dl>
