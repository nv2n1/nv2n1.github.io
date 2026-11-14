---
title: "perldsc(1)"
name: "perldsc"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perldsc/"
description: "perldsc – Perl Data Structures Cookbook"
---

<h2 class="name">NAME</h2>
<p> perldsc &#8211; Perl Data Structures Cookbook </p>
<h2>DESCRIPTION</h2>
<p> Perl lets us have complex data structures. You can write something like this and all of a sudden, you&#8217;d have an array with three dimensions! </p>
<pre><code>
    for
        my $x(1..10)
        {
        for
            my $y(1..10)
            {
            for
                my $z(1..10)
                {
                    $AoA[$x][$y][$z] =
                        $x * *$y + $z;
                }
            }
        }
</code></pre>
<p> Alas, however simple this may appear, underneath it&#8217;s a much more elaborate construct than meets the eye! </p>
<p> How do you print it out? Why can&#8217;t you say just <tt>&quot;print @AoA&quot;</tt>? How do you sort it? How can you pass it to a function or get one of these back from a function? Is it an object? Can you save it to disk to read back later? How do you access whole rows or columns of that matrix? Do all the values have to be numeric? </p>
<p> As you see, it&#8217;s quite easy to become confused. While some small portion of the blame for this can be attributed to the reference-based implementation, it&#8217;s really more due to a lack of existing documentation with examples designed for the beginner. </p>
<p> This document is meant to be a detailed but understandable treatment of the many different sorts of data structures you might want to develop. It should also serve as a cookbook of examples. That way, when you need to create one of these complex data structures, you can just pinch, pilfer, or purloin a drop-in example from here. </p>
<p> Let&#8217;s look at each of these possible constructs in detail. There are separate sections on each of the following:</p>
<dl>
<dt>&bull;</p>
<dd> arrays of arrays</p>
<dt>&bull;</p>
<dd> hashes of arrays</p>
<dt>&bull;</p>
<dd> arrays of hashes</p>
<dt>&bull;</p>
<dd> hashes of hashes</p>
<dt>&bull;</p>
<dd> more elaborate constructs</dl>
<p> But for now, let&#8217;s look at general issues common to all these types of data structures.</p>
<h2>REFERENCES</h2>
<p> The most important thing to understand about all data structures in Perl&#8212;including multidimensional arrays&#8212;is that even though they might appear otherwise, Perl <tt>@ARRAY</tt>s and <tt>%HASH</tt>es are all internally one-dimensional. They can hold only scalar values (meaning a string, number, or a reference). They cannot directly contain other arrays or hashes, but instead contain <i>references</i> to other arrays or hashes. </p>
<p> You can&#8217;t use a reference to an array or hash in quite the same way that you would a real array or hash. For C or C<font SIZE="-2">++</font> programmers unused to distinguishing between arrays and pointers to the same, this can be confusing. If so, just think of it as the difference between a structure and a pointer to a structure. </p>
<p> You can (and should) read more about references in perlref. Briefly, references are rather like pointers that know what they point to. (Objects are also a kind of reference, but we won&#8217;t be needing them right away&#8212;if ever.) This means that when you have something which looks to you like an access to a two-or-more-dimensional array and/or hash, what&#8217;s really going on is that the base type is merely a one-dimensional entity that contains references to the next level. It&#8217;s just that you can <i>use</i> it as though it were a two-dimensional one. This is actually the way almost all C multidimensional arrays work as well. </p>
<p>$array[7][12] #array of arrays<br />
    $array[7]{string} #array of hashes<br />
        $hash{string}[7] #hash of arrays<br />
            $hash{string}<br />
{<br />
    &#8216;another string&#8217;<br />
}<br />
#hash of hashes</p>
<p> Now, because the top level contains only references, if you try to print out your array in with a simple <code>print()</code> function, you&#8217;ll get something that doesn&#8217;t look very nice, like this: </p>
<p>my @AoA = ([ 2, 3 ], [ 4, 5, 7 ], [0]);<br />
print $AoA[1][2];<br />
7 print @AoA;<br />
ARRAY(0x83c38)<br />
ARRAY(0x8b194) ARRAY(0x8b1d0)</p>
<p> That&#8217;s because Perl doesn&#8217;t (ever) implicitly dereference your variables. If you want to get at the thing a reference is referring to, then you have to do this yourself using either prefix typing indicators, like <tt>&quot;${$blah}&quot;</tt>, <tt>&quot;@{$blah}&quot;</tt>, <tt>&quot;@{$blah[$i]}&quot;</tt>, or else postfix pointer arrows, like <tt>&quot;$a-&gt;[3]&quot;</tt>, <tt>&quot;$h-&gt;{fred}&quot;</tt>, or even <tt>&quot;$ob-&gt;method()-&gt;[3]&quot;</tt>.</p>
<h2>COMMON MISTAKES</h2>
<p> The two most common mistakes made in constructing something like an array of arrays is either accidentally counting the number of elements or else taking a reference to the same memory location repeatedly. Here&#8217;s the case where you just get the count instead of a nested array: </p>
<p>    for<br />
        my $i(1..10)<br />
        {<br />
            my @array = somefunc($i);<br />
            $AoA[$i] = @array;<br />
#WRONG !<br />
        }</p>
<p> That&#8217;s just the simple case of assigning an array to a scalar and getting its element count. If that&#8217;s what you really and truly want, then you might do well to consider being a tad more explicit about it, like this: </p>
<p>    for<br />
        my $i(1..10)<br />
        {<br />
            my @array = somefunc($i);<br />
            $counts[$i] = scalar @array;<br />
        }</p>
<p> Here&#8217;s the case of taking a reference to the same memory location again and again: </p>
<p>#Either without strict or having an outer &#8211; scope my @array;<br />
#declaration.<br />
    for<br />
        my $i(1..10)<br />
        {<br />
            @array = somefunc($i);<br />
            $AoA[$i] = \@array;<br />
#WRONG !<br />
        }</p>
<p> So, what&#8217;s the big problem with that? It looks right, doesn&#8217;t it? After all, I just told you that you need an array of references, so by golly, you&#8217;ve made me one! </p>
<p> Unfortunately, while this is true, it&#8217;s still broken. All the references in <tt>@AoA</tt> refer to the <i>very same place</i>, and they will therefore all hold whatever was last in <tt>@array</tt>! It&#8217;s similar to the problem demonstrated in the following C program: </p>
<p>#include &lt;pwd.h&gt;<br />
main()<br />
{<br />
    struct passwd *getpwnam(), *rp, *dp;<br />
    rp = getpwnam(&#8220;root&#8221;);<br />
    dp = getpwnam(&#8220;daemon&#8221;);<br />
    printf(&#8220;daemon name is %s
root name is %s
&#8221;,<br />
           dp-&gt;pw_name, rp-&gt;pw_name);<br />
}</p>
<p> Which will print </p>
<pre>
    daemon name is daemon
    root name is daemon
</pre>
<p> The problem is that both <tt>&quot;rp&quot;</tt> and <tt>&quot;dp&quot;</tt> are pointers to the same location in memory! In C, you&#8217;d have to remember to <code>malloc()</code> yourself some new memory. In Perl, you&#8217;ll want to use the array constructor <tt>&quot;[]&quot;</tt> or the hash constructor <tt>&quot;{}&quot;</tt> instead. Here&#8217;s the right way to do the preceding broken code fragments: </p>
<p>#Either without strict or having an outer &#8211; scope my @array;<br />
#declaration.<br />
    for<br />
        my $i(1..10)<br />
        {<br />
            @array = somefunc($i);<br />
            $AoA[$i] = [@array];<br />
        }</p>
<p> The square brackets make a reference to a new array with a <i>copy</i> of what&#8217;s in <tt>@array</tt> at the time of the assignment. This is what you want. </p>
<p> Note that this will produce something similar, but it&#8217;s much harder to read: </p>
<p>#Either without strict or having an outer &#8211; scope my @array;<br />
#declaration.<br />
    for<br />
        my $i(1..10)<br />
        {<br />
            @array = 0..$i;<br />
            @{$AoA[$i]} = @array;<br />
        }</p>
<p> Is it the same? Well, maybe so&#8212;and maybe not. The subtle difference is that when you assign something in square brackets, you know for sure it&#8217;s always a brand new reference with a new <i>copy</i> of the data. Something else could be going on in this new case with the <tt>&quot;@{$AoA[$i]}&quot;</tt> dereference on the left-hand-side of the assignment. It all depends on whether <tt>$AoA[$i]</tt> had been undefined to start with, or whether it already contained a reference. If you had already populated <tt>@AoA</tt> with references, as in </p>
<pre>
    $AoA[3] = \@another_array;
</pre>
<p> Then the assignment with the indirection on the left-hand-side would use the existing reference that was already there: </p>
<p>@{$AoA[3]} = @array;</p>
<p> Of course, this <i>would</i> have the &#8220;interesting&#8221; effect of clobbering <tt>@another_array</tt>. (Have you ever noticed how when a programmer says something is &#8220;interesting&#8221;, that rather than meaning &#8220;intriguing&#8221;, they&#8217;re disturbingly more apt to mean that it&#8217;s &#8220;annoying&#8221;, &#8220;difficult&#8221;, or both? :-) </p>
<p> So just remember always to use the array or hash constructors with <tt>&quot;[]&quot;</tt> or <tt>&quot;{}&quot;</tt>, and you&#8217;ll be fine, although it&#8217;s not always optimally efficient. </p>
<p> Surprisingly, the following dangerous-looking construct will actually work out fine: </p>
<p>    for<br />
        my $i(1..10)<br />
        {<br />
            my @array = somefunc($i);<br />
            $AoA[$i] = \@array;<br />
        }</p>
<p> That&#8217;s because <code>my()</code> is more of a run-time statement than it is a compile-time declaration <i>per se</i>. This means that the <code>my()</code> variable is remade afresh each time through the loop. So even though it <i>looks</i> as though you stored the same variable reference each time, you actually did not! This is a subtle distinction that can produce more efficient code at the risk of misleading all but the most experienced of programmers. So I usually advise against teaching it to beginners. In fact, except for passing arguments to functions, I seldom like to see the gimme-a-reference operator (backslash) used much at all in code. Instead, I advise beginners that they (and most of the rest of us) should try to use the much more easily understood constructors <tt>&quot;[]&quot;</tt> and <tt>&quot;{}&quot;</tt> instead of relying upon lexical (or dynamic) scoping and hidden reference-counting to do the right thing behind the scenes. </p>
<p> In summary: </p>
<p>$AoA[$i] = [@array];<br />
#usually best<br />
    $AoA[$i] = \@array;<br />
#perilous;<br />
just how my() was that array ? @{$AoA[$i]} = @array;<br />
#way too tricky for most programmers</p>
<h2>CAVEAT ON PRECEDENCE</h2>
<p> Speaking of things like <tt>&quot;@{$AoA[$i]}&quot;</tt>, the following are actually the same thing: </p>
<p>$aref-&gt;[2][2] #clear $$aref[2][2] #confusing</p>
<p> That&#8217;s because Perl&#8217;s precedence rules on its five prefix dereferencers (which look like someone swearing: <tt>&quot;$ @ * % &amp;&quot;</tt>) make them bind more tightly than the postfix subscripting brackets or braces! This will no doubt come as a great shock to the C or C<font SIZE="-2">++</font> programmer, who is quite accustomed to using <tt>*a[i]</tt> to mean what&#8217;s pointed to by the <i>i&#8217;th</i> element of <tt>&quot;a&quot;</tt>. That is, they first take the subscript, and only then dereference the thing at that subscript. That&#8217;s fine in C, but this isn&#8217;t C. </p>
<p> The seemingly equivalent construct in Perl, <tt>$$aref[$i]</tt> first does the deref of <tt>$aref</tt>, making it take <tt>$aref</tt> as a reference to an array, and then dereference that, and finally tell you the <i>i&#8217;th</i> value of the array pointed to by <tt>$AoA</tt>. If you wanted the C notion, you&#8217;d have to write <tt>&quot;${$AoA[$i]}&quot;</tt> to force the <tt>$AoA[$i]</tt> to get evaluated first before the leading <tt>&quot;$&quot;</tt> dereferencer.</p>
<h2>WHY YOU SHOULD ALWAYS use strict</h2>
<p> If this is starting to sound scarier than it&#8217;s worth, relax. Perl has some features to help you avoid its most common pitfalls. The best way to avoid getting confused is to start every program like this: </p>
<pre>
    #!/usr/bin/perl -w
    use strict;
</pre>
<p> This way, you&#8217;ll be forced to declare all your variables with <code>my()</code> and also disallow accidental &#8220;symbolic dereferencing&#8221;. Therefore if you&#8217;d done this: </p>
<p>my $aref = [<br />
    [<br />
        &#8220;fred&#8221;,<br />
        &#8220;barney&#8221;,<br />
        &#8220;pebbles&#8221;,<br />
        &#8220;bambam&#8221;,<br />
        &#8220;dino&#8221;,<br />
    ],<br />
    [<br />
        &#8220;homer&#8221;,<br />
        &#8220;bart&#8221;,<br />
        &#8220;marge&#8221;,<br />
        &#8220;maggie&#8221;,<br />
    ],<br />
    [<br />
        &#8220;george&#8221;,<br />
        &#8220;jane&#8221;,<br />
        &#8220;elroy&#8221;,<br />
        &#8220;judy&#8221;,<br />
    ],<br />
];<br />
print $aref[2][2];</p>
<p> The compiler would immediately flag that as an error <i>at compile time</i>, because you were accidentally accessing <tt>@aref</tt>, an undeclared variable, and it would thereby remind you to write instead: </p>
<p>print $aref-&gt;[2][2]</p>
<h2>DEBUGGING</h2>
<p> You can use the debugger&#8217;s <tt>&quot;x&quot;</tt> command to dump out complex data structures. For example, given the assignment to <tt>$AoA</tt> above, here&#8217;s the debugger output: </p>
<pre>
    DB&lt;1&gt; x $AoA
    $AoA = ARRAY(0x13b5a0)
       0  ARRAY(0x1f0a24)
          0  'fred'
          1  'barney'
          2  'pebbles'
          3  'bambam'
          4  'dino'
       1  ARRAY(0x13b558)
          0  'homer'
          1  'bart'
          2  'marge'
          3  'maggie'
       2  ARRAY(0x13b540)
          0  'george'
          1  'jane'
          2  'elroy'
          3  'judy'
</pre>
<h2>CODE EXAMPLES</h2>
<p> Presented with little comment (these will get their own manpages someday) here are short code examples illustrating access of various types of data structures.</p>
<h2>ARRAYS OF ARRAYS</h2>
<h3>Declaration of an <font SIZE="-1">ARRAY OF ARRAYS</font></h3>
<p>@AoA = ([ &#8220;fred&#8221;, &#8220;barney&#8221; ],<br />
        [ &#8220;george&#8221;, &#8220;jane&#8221;, &#8220;elroy&#8221; ],<br />
        [ &#8220;homer&#8221;, &#8220;marge&#8221;, &#8220;bart&#8221; ], );</p>
<h3>Generation of an <font SIZE="-1">ARRAY OF ARRAYS</font></h3>
<p>#reading from file<br />
while (&lt;&gt;) {<br />
    push @AoA, [split];<br />
}<br />
#calling a function<br />
 for<br />
     $i(1..10)<br />
     {<br />
         $AoA[$i] = [somefunc($i)];<br />
     }<br />
#using temp vars<br />
 for<br />
     $i(1..10)<br />
     {<br />
         @tmp = somefunc($i);<br />
         $AoA[$i] = [@tmp];<br />
     }<br />
#add to an existing row<br />
 push @{$AoA[0]}, &#8220;wilma&#8221;, &#8220;betty&#8221;;</p>
<h3>Access and Printing of an <font SIZE="-1">ARRAY OF ARRAYS</font></h3>
<p>#one element<br />
$AoA[0][0] = &#8220;Fred&#8221;;<br />
#another element<br />
$AoA[1][1] = ~s / (\w) /
