---
title: "a2p(1)"
name: "a2p"
section: "1"
letter: "a"
url: "/docs/linux/man/1-a2p/"
description: "a2p – Awk to Perl translator"
---

<h2 class="name">NAME</h2>
<p> a2p &#8211; Awk to Perl translator </p>
<h2>SYNOPSIS</h2>
<p> <code>a2p</code> [<i>options</i>] [<i>filename</i>]</p>
<h2>DESCRIPTION</h2>
<p> <i>A2p</i> takes an awk script specified on the command line (or from standard input) and produces a comparable <i>perl</i> script on the standard output.</p>
<h3><font SIZE="-1">OPTIONS</font></h3>
<p> Options include:</p>
<dl>
<dt><code>-D&lt;number&gt;</code></p>
<dd> sets debugging flags.</p>
<dt><code>-F&lt;character&gt;</code></p>
<dd> tells a2p that this awk script is always invoked with this <code>-F</code> switch.</p>
<dt><code>-n&lt;fieldlist&gt;</code></p>
<dd> specifies the names of the input fields if input does not have to be split into an array. If you were translating an awk script that processes the password file, you might say: </p>
<pre>
        a2p -7 -nlogin.password.uid.gid.gcos.shell.home
</pre>
<p> Any delimiter can be used to separate the field names.</p>
<dt><code>-&lt;number&gt;</code></p>
<dd> causes a2p to assume that input will always have that many fields.</p>
<dt><code>-o</code></p>
<dd> tells a2p to use old awk behavior. The only current differences are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Old awk always has a line loop, even if there are no line actions, whereas new awk does not.</p>
<dt>&bull;</p>
<dd> In old awk, sprintf is extremely greedy about its arguments. For example, given the statement </p>
<pre>
        print sprintf(some_args), extra_args;
</pre>
<p> old awk considers <i>extra_args</i> to be arguments to <tt>&quot;sprintf&quot;</tt>; new awk considers them arguments to <tt>&quot;print&quot;</tt>.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h3>Considerations</h3>
<p> A2p cannot do as good a job translating as a human would, but it usually does pretty well. There are some areas where you may want to examine the perl script produced and tweak it some. Here are some of them, in no particular order. </p>
<p> There is an awk idiom of putting <i>int()</i> around a string expression to force numeric interpretation, even though the argument is always integer anyway. This is generally unneeded in perl, but a2p can&#8217;t tell if the argument is always going to be integer, so it leaves it in. You may wish to remove it. </p>
<p> Perl differentiates numeric comparison from string comparison. Awk has one operator for both that decides at run time which comparison to do. A2p does not try to do a complete job of awk emulation at this point. Instead it guesses which one you want. It&#8217;s almost always right, but it can be spoofed. All such guesses are marked with the comment &quot;<tt>&quot;#???&quot;</tt>&quot;. You should go through and check them. You might want to run at least once with the <code>-w</code> switch to perl, which will warn you if you use == where you should have used eq. </p>
<p> Perl does not attempt to emulate the behavior of awk in which nonexistent array elements spring into existence simply by being referenced. If somehow you are relying on this mechanism to create null entries for a subsequent for&#8230;in, they won&#8217;t be there in perl. </p>
<p> If a2p makes a split line that assigns to a list of variables that looks like (Fld1, Fld2, Fld3&#8230;) you may want to rerun a2p using the <code>-n</code> option mentioned above. This will let you name the fields throughout the script. If it splits to an array instead, the script is probably referring to the number of fields somewhere. </p>
<p> The exit statement in awk doesn&#8217;t necessarily exit; it goes to the <font SIZE="-1">END</font> block if there is one. Awk scripts that do contortions within the <font SIZE="-1">END</font> block to bypass the block under such circumstances can be simplified by removing the conditional in the <font SIZE="-1">END</font> block and just exiting directly from the perl script. </p>
<p> Perl has two kinds of array, numerically-indexed and associative. Perl associative arrays are called &#8220;hashes&#8221;. Awk arrays are usually translated to hashes, but if you happen to know that the index is always going to be numeric you could change the {&#8230;} to [&#8230;]. Iteration over a hash is done using the <i>keys()</i> function, but iteration over an array is <font SIZE="-1">NOT</font>. You might need to modify any loop that iterates over such an array. </p>
<p> Awk starts by assuming <font SIZE="-1">OFMT</font> has the value %.6g. Perl starts by assuming its equivalent, $#, to have the value %.20g. You&#8217;ll want to set $# explicitly if you use the default value of <font SIZE="-1">OFMT</font>. </p>
<p> Near the top of the line loop will be the split operation that is implicit in the awk script. There are times when you can move this down past some conditionals that test the entire record so that the split is not done as often. </p>
<p> For aesthetic reasons you may wish to change index variables from being 1-based (awk style) to 0-based (Perl style). Be sure to change all operations the variable is involved in to match. </p>
<p> Cute comments that say &#8220;# Here is a workaround because awk is dumb&#8221; are passed through unmodified. </p>
<p> Awk scripts are often embedded in a shell script that pipes stuff into and out of awk. Often the shell script wrapper can be incorporated into the perl script, since perl can start up pipes into and out of itself, and can do other things that awk can&#8217;t do by itself. </p>
<p> Scripts that refer to the special variables <font SIZE="-1">RSTART</font> and <font SIZE="-1">RLENGTH</font> can often be simplified by referring to the variables $`, $&amp; and $&#8217;, as long as they are within the scope of the pattern match that sets them. </p>
<p> The produced perl script may have subroutines defined to deal with awk&#8217;s semantics regarding getline and print. Since a2p usually picks correctness over efficiency. it is almost always possible to rewrite such code to be more efficient by discarding the semantic sugar. </p>
<p> For efficiency, you may wish to remove the keyword from any return statement that is the last statement executed in a subroutine. A2p catches the most common case, but doesn&#8217;t analyze embedded blocks for subtler cases. </p>
<p> ARGV[0] translates to <tt>$ARGV0</tt>, but ARGV[n] translates to <tt>$ARGV</tt>[$n-1]. A loop that tries to iterate over ARGV[0] won&#8217;t find it.</p>
<h2>ENVIRONMENT</h2>
<p> A2p uses no environment variables.</p>
<h2>AUTHOR</h2>
<p> Larry Wall &lt;<i>larry [at] wall.org</i>&gt;</p>
<h2>FILES</h2>
<h2>SEE ALSO</h2>
<pre>
 perl   The perl compiler/interpreter
 
 s2p    sed to perl translator
</pre>
<h2>DIAGNOSTICS</h2>
<h2>BUGS</h2>
<p> It would be possible to emulate awk&#8217;s behavior in selecting string versus numeric operations at run time by inspection of the operands, but it would be gross and inefficient. Besides, a2p almost always guesses right. </p>
<p> Storage for the awk syntax tree is currently static, and can run out. </p>
<h2>Index</h2>
<dt><a href="#lbAG">ENVIRONMENT</a></p>
<dd>
<dt><a href="#lbAH">AUTHOR</a></p>
<dd>
<dt><a href="#lbAI">FILES</a></p>
<dd>
<dt><a href="#lbAJ">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAK">DIAGNOSTICS</a></p>
<dd>
<dt><a href="#lbAL">BUGS</a></p>
<dd></dl>
