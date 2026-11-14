---
title: "perlhacktut(1)"
name: "perlhacktut"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlhacktut/"
description: "perlhacktut – Walk through the creation of a simple C code patch"
---

<h2 class="name">NAME</h2>
<p> perlhacktut &#8211; Walk through the creation of a simple C code patch </p>
<h2>DESCRIPTION</h2>
<p> This document takes you through a simple patch example. </p>
<p> If you haven&#8217;t read perlhack yet, go do that first! You might also want to read through perlsource too. </p>
<p> Once you&#8217;re done here, check out perlhacktips next.</p>
<h2>EXAMPLE OF A SIMPLE PATCH</h2>
<p> Let&#8217;s take a simple patch from start to finish. </p>
<p> Here&#8217;s something Larry suggested: if a <tt>&quot;U&quot;</tt> is the first active format during a <tt>&quot;pack&quot;</tt>, (for example, <tt>&quot;pack &quot;U3C8&quot;, @stuff&quot;</tt>) then the resulting string should be treated as <font SIZE="-1">UTF-8</font> encoded. </p>
<p> If you are working with a git clone of the Perl repository, you will want to create a branch for your changes. This will make creating a proper patch much simpler. See the perlgit for details on how to do this.</p>
<h3>Writing the patch</h3>
<p> How do we prepare to fix this up? First we locate the code in question &#8211; the <tt>&quot;pack&quot;</tt> happens at runtime, so it&#8217;s going to be in one of the <i>pp</i> files. Sure enough, <tt>&quot;pp_pack&quot;</tt> is in <i>pp.c</i>. Since we&#8217;re going to be altering this file, let&#8217;s copy it to <i>pp.c~</i>. </p>
<p> [Well, it was in <i>pp.c</i> when this tutorial was written. It has now been split off with <tt>&quot;pp_unpack&quot;</tt> to its own file, <i>pp_pack.c</i>] </p>
<p> Now let&#8217;s look over <tt>&quot;pp_pack&quot;</tt>: we take a pattern into <tt>&quot;pat&quot;</tt>, and then loop over the pattern, taking each format character in turn into <tt>&quot;datum_type&quot;</tt>. Then for each possible format character, we swallow up the other arguments in the pattern (a field width, an asterisk, and so on) and convert the next chunk input into the specified format, adding it onto the output <font SIZE="-1">SV</font> <tt>&quot;cat&quot;</tt>. </p>
<p> How do we know if the <tt>&quot;U&quot;</tt> is the first format in the <tt>&quot;pat&quot;</tt>? Well, if we have a pointer to the start of <tt>&quot;pat&quot;</tt> then, if we see a <tt>&quot;U&quot;</tt> we can test whether we&#8217;re still at the start of the string. So, here&#8217;s where <tt>&quot;pat&quot;</tt> is set up: </p>
<pre><code>
STRLEN fromlen;
char *pat = SvPVx(*++MARK, fromlen);
char *patend = pat + fromlen;
I32 len;
I32 datumtype;
SV *fromstr;
</code></pre>
<p> We&#8217;ll have another string pointer in there: </p>
<p>STRLEN fromlen;<br />
char *pat = SvPVx(*++MARK, fromlen);<br />
char *patend = pat + fromlen;<br />
+ char *patcopy;<br />
I32 len;<br />
I32 datumtype;<br />
SV *fromstr;</p>
<p> And just before we start the loop, we&#8217;ll set <tt>&quot;patcopy&quot;</tt> to be the start of <tt>&quot;pat&quot;</tt>: </p>
<p>items = SP &#8211; MARK;<br />
MARK++;<br />
SvPVCLEAR(cat);<br />
+ patcopy = pat;<br />
while (pat &lt; patend) {</p>
<p> Now if we see a <tt>&quot;U&quot;</tt> which was at the start of the string, we turn on the <tt>&quot;UTF8&quot;</tt> flag for the output <font SIZE="-1">SV,</font> <tt>&quot;cat&quot;</tt>: </p>
<p>+ if (datumtype == &#8216;U&#8217; &amp;&amp; pat == patcopy + 1) + SvUTF8_on(cat);<br />
if (datumtype == &#8216;#&#8217;) {<br />
    while (pat &lt; patend &amp;&amp; *pat != &#8216;
&#8217;)<br />
        pat++;</p>
<p> Remember that it has to be <tt>&quot;patcopy+1&quot;</tt> because the first character of the string is the <tt>&quot;U&quot;</tt> which has been swallowed into <tt>&quot;datumtype!&quot;</tt> </p>
<p> Oops, we forgot one thing: what if there are spaces at the start of the pattern? <tt>&quot;pack(&quot; U*&quot;, @stuff)&quot;</tt> will have <tt>&quot;U&quot;</tt> as the first active character, even though it&#8217;s not the first thing in the pattern. In this case, we have to advance <tt>&quot;patcopy&quot;</tt> along with <tt>&quot;pat&quot;</tt> when we see spaces: </p>
<pre>
    if (isSPACE(datumtype))
        continue;
</pre>
<p> needs to become </p>
<p>if (isSPACE(datumtype)) {<br />
    patcopy++;<br />
    continue;<br />
}</p>
<p> <font SIZE="-1">OK.</font> That&#8217;s the C part done. Now we must do two additional things before this patch is ready to go: we&#8217;ve changed the behaviour of Perl, and so we must document that change. We must also provide some more regression tests to make sure our patch works and doesn&#8217;t create a bug somewhere else along the line.</p>
<h3>Testing the patch</h3>
<p> The regression tests for each operator live in <i>t/op/</i>, and so we make a copy of <i>t/op/pack.t</i> to <i>t/op/pack.t~</i>. Now we can add our tests to the end. First, we&#8217;ll test that the <tt>&quot;U&quot;</tt> does indeed create Unicode strings. </p>
<p> t/op/pack.t has a sensible <code>ok()</code> function, but if it didn&#8217;t we could use the one from t/test.pl. </p>
<p>require &#8216;./test.pl&#8217;;<br />
plan(tests = &gt; 159);</p>
<p> so instead of this: </p>
<pre><code>
print 'not ' unless "1.20.300.4000" eq sprintf "%vd",
    pack("U*", 1, 20, 300, 4000);
print "ok $test
";
$test++;
</code></pre>
<p> we can write the more sensible (see Test::More for a full explanation of <code>is()</code> and other testing functions). </p>
<pre>
 is( &quot;1.20.300.4000&quot;, sprintf &quot;%vd&quot;, pack(&quot;U*&quot;,1,20,300,4000),
                                       &quot;U* produces Unicode&quot; );
</pre>
<p> Now we&#8217;ll test that we got that space-at-the-beginning business right: </p>
<pre>
 is( &quot;1.20.300.4000&quot;, sprintf &quot;%vd&quot;, pack(&quot;  U*&quot;,1,20,300,4000),
                                     &quot;  with spaces at the beginning&quot; );
</pre>
<p> And finally we&#8217;ll test that we don&#8217;t make Unicode strings if <tt>&quot;U&quot;</tt> is <code>not</code> the first active format: </p>
<pre>
 isnt( v1.20.300.4000, sprintf &quot;%vd&quot;, pack(&quot;C0U*&quot;,1,20,300,4000),
                                       &quot;U* not first isn't Unicode&quot; );
</pre>
<p> Mustn&#8217;t forget to change the number of tests which appears at the top, or else the automated tester will get confused. This will either look like this: </p>
<pre>
 print &quot;1..156
&quot;;
</pre>
<p> or this: </p>
<pre>
 plan( tests =&gt; 156 );
</pre>
<p> We now compile up Perl, and run it through the test suite. Our new tests pass, hooray!</p>
<h3>Documenting the patch</h3>
<p> Finally, the documentation. The job is never done until the paperwork is over, so let&#8217;s describe the change we&#8217;ve just made. The relevant place is <i>pod/perlfunc.pod</i>; again, we make a copy, and then we&#8217;ll insert this text in the description of <tt>&quot;pack&quot;</tt>: </p>
<pre>
 =item *
 If the pattern begins with a C&lt;U&gt;, the resulting string will be treated
 as UTF-8-encoded Unicode. You can force UTF-8 encoding on in a string
 with an initial C&lt;U0&gt;, and the bytes that follow will be interpreted as
 Unicode characters. If you don't want this to happen, you can begin
 your pattern with C&lt;C0&gt; (or anything else) to force Perl not to UTF-8
 encode your string, and then follow this with a C&lt;U*&gt; somewhere in your
 pattern.
</pre>
<h3>Submit</h3>
<p> See perlhack for details on how to submit this patch.</p>
<h2>AUTHOR</h2>
<p> This document was originally written by Nathan Torkington, and is maintained by the perl5-porters mailing list. </p>
<h2>Index</h2>
