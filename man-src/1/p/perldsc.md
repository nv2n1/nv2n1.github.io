---
title: "perldsc(1)"
name: "perldsc"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perldsc/"
description: "perldsc – Perl Data Structures Cookbook"
---
<h2 class="name">NAME</h2>
<p> perldsc - Perl Data Structures Cookbook </p>
<h2>DESCRIPTION</h2>
<p> Perl lets us have complex data structures. You can write something like this and all of a sudden, you&#8217;d have an array with three dimensions! </p>
<pre><code>    for my $x (1 .. 10) {
        for my $y (1 .. 10) {
            for my $z (1 .. 10) {
                $AoA[$x][$y][$z] =
                    $x ** $y + $z;
            }
        }
    }
</code></pre>
<p> Alas, however simple this may appear, underneath it&#8217;s a much more elaborate construct than meets the eye! </p>
<p> How do you print it out? Why can&#8217;t you say just <code>&quot;print @AoA&quot;</code>? How do you sort it? How can you pass it to a function or get one of these back from a function? Is it an object? Can you save it to disk to read back later? How do you access whole rows or columns of that matrix? Do all the values have to be numeric? </p>
<p> As you see, it&#8217;s quite easy to become confused. While some small portion of the blame for this can be attributed to the reference-based implementation, it&#8217;s really more due to a lack of existing documentation with examples designed for the beginner. </p>
<p> This document is meant to be a detailed but understandable treatment of the many different sorts of data structures you might want to develop. It should also serve as a cookbook of examples. That way, when you need to create one of these complex data structures, you can just pinch, pilfer, or purloin a drop-in example from here. </p>
<p> Let&#8217;s look at each of these possible constructs in detail. There are separate sections on each of the following: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> arrays of arrays </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> hashes of arrays </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> arrays of hashes </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> hashes of hashes </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> more elaborate constructs </p>
 </dd></dl>
<p> But for now, let&#8217;s look at general issues common to all these types of data structures.  </p>
<h2>REFERENCES</h2>
<p> The most important thing to understand about all data structures in Perl---including multidimensional arrays---is that even though they might appear otherwise, Perl <code>@ARRAY</code>s and <code>%HASH</code>es are all internally one-dimensional. They can hold only scalar values (meaning a string, number, or a reference). They cannot directly contain other arrays or hashes, but instead contain <i>references</i> to other arrays or hashes. </p>
<p> You can&#8217;t use a reference to an array or hash in quite the same way that you would a real array or hash. For C or C<font SIZE="-2">++</font> programmers unused to distinguishing between arrays and pointers to the same, this can be confusing. If so, just think of it as the difference between a structure and a pointer to a structure. </p>
<p> You can (and should) read more about references in perlref. Briefly, references are rather like pointers that know what they point to. (Objects are also a kind of reference, but we won&#8217;t be needing them right away---if ever.) This means that when you have something which looks to you like an access to a two-or-more-dimensional array and/or hash, what&#8217;s really going on is that the base type is merely a one-dimensional entity that contains references to the next level. It&#8217;s just that you can <i>use</i> it as though it were a two-dimensional one. This is actually the way almost all C multidimensional arrays work as well. </p>
<pre><code>    $array[7][12] # array of arrays
    $array[7]{string} # array of hashes
    $hash{string}[7] # hash of arrays
    $hash{string}{'another string'} # hash of hashes
</code></pre>
<p> Now, because the top level contains only references, if you try to print out your array in with a simple <code>print()</code> function, you&#8217;ll get something that doesn&#8217;t look very nice, like this: </p>
<pre><code>    my @AoA = ( [2, 3], [4, 5, 7], [0] );
    print $AoA[1][2];
  7
    print @AoA;
  ARRAY(0x83c38)ARRAY(0x8b194)ARRAY(0x8b1d0)
</code></pre>
<p> That&#8217;s because Perl doesn&#8217;t (ever) implicitly dereference your variables. If you want to get at the thing a reference is referring to, then you have to do this yourself using either prefix typing indicators, like <code>&quot;${$blah}&quot;</code>, <code>&quot;@{$blah}&quot;</code>, <code>&quot;@{$blah[$i]}&quot;</code>, or else postfix pointer arrows, like <code>&quot;$a-&gt;[3]&quot;</code>, <code>&quot;$h-&gt;{fred}&quot;</code>, or even <code>&quot;$ob-&gt;method()-&gt;[3]&quot;</code>.  </p>
<h2>COMMON MISTAKES</h2>
<p> The two most common mistakes made in constructing something like an array of arrays is either accidentally counting the number of elements or else taking a reference to the same memory location repeatedly. Here&#8217;s the case where you just get the count instead of a nested array: </p>
<pre><code>    for my $i (1..10) {
        my @array = somefunc($i);
        $AoA[$i] = @array; # WRONG!
    }
</code></pre>
<p> That&#8217;s just the simple case of assigning an array to a scalar and getting its element count. If that&#8217;s what you really and truly want, then you might do well to consider being a tad more explicit about it, like this: </p>
<pre><code>    for my $i (1..10) {
        my @array = somefunc($i);
        $counts[$i] = scalar @array;
    }
</code></pre>
<p> Here&#8217;s the case of taking a reference to the same memory location again and again: </p>
<pre><code>    # Either without strict or having an outer-scope my @array;
    # declaration.
    for my $i (1..10) {
        @array = somefunc($i);
        $AoA[$i] = \@array; # WRONG!
    }
</code></pre>
<p> So, what&#8217;s the big problem with that? It looks right, doesn&#8217;t it? After all, I just told you that you need an array of references, so by golly, you&#8217;ve made me one! </p>
<p> Unfortunately, while this is true, it&#8217;s still broken. All the references in <code>@AoA</code> refer to the <i>very same place</i>, and they will therefore all hold whatever was last in <code>@array</code>! It&#8217;s similar to the problem demonstrated in the following C program: </p>
<pre><code>    #include &lt;pwd.h&gt;
    main() {
        struct passwd *getpwnam(), *rp, *dp;
        rp = getpwnam(&quot;root&quot;);
        dp = getpwnam(&quot;daemon&quot;);
        printf(&quot;daemon name is %s\nroot name is %s\n&quot;,
                dp-&gt;pw_name, rp-&gt;pw_name);
    }
</code></pre>
<p> Which will print </p>
<pre><code>    daemon name is daemon
    root name is daemon
</code></pre>
<p> The problem is that both <code>&quot;rp&quot;</code> and <code>&quot;dp&quot;</code> are pointers to the same location in memory! In C, you&#8217;d have to remember to <code>malloc()</code> yourself some new memory. In Perl, you&#8217;ll want to use the array constructor <code>&quot;[]&quot;</code> or the hash constructor <code>&quot;{}&quot;</code> instead. Here&#8217;s the right way to do the preceding broken code fragments: </p>
<pre><code>    # Either without strict or having an outer-scope my @array;
    # declaration.
    for my $i (1..10) {
        @array = somefunc($i);
        $AoA[$i] = [ @array ];
    }
</code></pre>
<p> The square brackets make a reference to a new array with a <i>copy</i> of what&#8217;s in <code>@array</code> at the time of the assignment. This is what you want. </p>
<p> Note that this will produce something similar, but it&#8217;s much harder to read: </p>
<pre><code>    # Either without strict or having an outer-scope my @array;
    # declaration.
    for my $i (1..10) {
        @array = 0 .. $i;
        @{$AoA[$i]} = @array;
    }
</code></pre>
<p> Is it the same? Well, maybe so---and maybe not. The subtle difference is that when you assign something in square brackets, you know for sure it&#8217;s always a brand new reference with a new <i>copy</i> of the data. Something else could be going on in this new case with the <code>&quot;@{$AoA[$i]}&quot;</code> dereference on the left-hand-side of the assignment. It all depends on whether <code>$AoA[$i]</code> had been undefined to start with, or whether it already contained a reference. If you had already populated <code>@AoA</code> with references, as in </p>
<pre><code>    $AoA[3] = \@another_array;
</code></pre>
<p> Then the assignment with the indirection on the left-hand-side would use the existing reference that was already there: </p>
<pre><code>    @{$AoA[3]} = @array;
</code></pre>
<p> Of course, this <i>would</i> have the ``interesting&#8217;&#8216; effect of clobbering <code>@another_array</code>. (Have you ever noticed how when a programmer says something is ``interesting&#8217;&#8216;, that rather than meaning ``intriguing&#8217;&#8216;, they&#8217;re disturbingly more apt to mean that it&#8217;s ``annoying&#8217;&#8216;, ``difficult&#8217;&#8216;, or both? :-) </p>
<p> So just remember always to use the array or hash constructors with <code>&quot;[]&quot;</code> or <code>&quot;{}&quot;</code>, and you&#8217;ll be fine, although it&#8217;s not always optimally efficient. </p>
<p> Surprisingly, the following dangerous-looking construct will actually work out fine: </p>
<pre><code>    for my $i (1..10) {
        my @array = somefunc($i);
        $AoA[$i] = \@array;
    }
</code></pre>
<p> That&#8217;s because <code>my()</code> is more of a run-time statement than it is a compile-time declaration <i>per se</i>. This means that the <code>my()</code> variable is remade afresh each time through the loop. So even though it <i>looks</i> as though you stored the same variable reference each time, you actually did not! This is a subtle distinction that can produce more efficient code at the risk of misleading all but the most experienced of programmers. So I usually advise against teaching it to beginners. In fact, except for passing arguments to functions, I seldom like to see the gimme-a-reference operator (backslash) used much at all in code. Instead, I advise beginners that they (and most of the rest of us) should try to use the much more easily understood constructors <code>&quot;[]&quot;</code> and <code>&quot;{}&quot;</code> instead of relying upon lexical (or dynamic) scoping and hidden reference-counting to do the right thing behind the scenes. </p>
<p> In summary: </p>
<pre><code>    $AoA[$i] = [ @array ]; # usually best
    $AoA[$i] = \@array; # perilous; just how my() was that array?
    @{ $AoA[$i] } = @array; # way too tricky for most programmers
</code></pre>
<h2>CAVEAT ON PRECEDENCE</h2>
<p> Speaking of things like <code>&quot;@{$AoA[$i]}&quot;</code>, the following are actually the same thing: </p>
<pre><code>    $aref-&gt;[2][2] # clear
    $$aref[2][2] # confusing
</code></pre>
<p> That&#8217;s because Perl&#8217;s precedence rules on its five prefix dereferencers (which look like someone swearing: <code>&quot;$ @ * % &amp;&quot;</code>) make them bind more tightly than the postfix subscripting brackets or braces! This will no doubt come as a great shock to the C or C<font SIZE="-2">++</font> programmer, who is quite accustomed to using <code>*a[i]</code> to mean what&#8217;s pointed to by the <i>i&#8217;th</i> element of <code>&quot;a&quot;</code>. That is, they first take the subscript, and only then dereference the thing at that subscript. That&#8217;s fine in C, but this isn&#8217;t C. </p>
<p> The seemingly equivalent construct in Perl, <code>$$aref[$i]</code> first does the deref of <code>$aref</code>, making it take <code>$aref</code> as a reference to an array, and then dereference that, and finally tell you the <i>i&#8217;th</i> value of the array pointed to by <code>$AoA</code>. If you wanted the C notion, you&#8217;d have to write <code>&quot;${$AoA[$i]}&quot;</code> to force the <code>$AoA[$i]</code> to get evaluated first before the leading <code>&quot;$&quot;</code> dereferencer.  </p>
<h2>WHY YOU SHOULD ALWAYS use strict</h2>
<p> If this is starting to sound scarier than it&#8217;s worth, relax. Perl has some features to help you avoid its most common pitfalls. The best way to avoid getting confused is to start every program like this: </p>
<pre><code>    #!/usr/bin/perl -w
    use strict;
</code></pre>
<p> This way, you&#8217;ll be forced to declare all your variables with <code>my()</code> and also disallow accidental ``symbolic dereferencing&#8217;&#8216;. Therefore if you&#8217;d done this: </p>
<pre><code>    my $aref = [
        [ &quot;fred&quot;, &quot;barney&quot;, &quot;pebbles&quot;, &quot;bambam&quot;, &quot;dino&quot;, ],
        [ &quot;homer&quot;, &quot;bart&quot;, &quot;marge&quot;, &quot;maggie&quot;, ],
        [ &quot;george&quot;, &quot;jane&quot;, &quot;elroy&quot;, &quot;judy&quot;, ],
    ];
    print $aref[2][2];
</code></pre>
<p> The compiler would immediately flag that as an error <i>at compile time</i>, because you were accidentally accessing <code>@aref</code>, an undeclared variable, and it would thereby remind you to write instead: </p>
<pre><code>    print $aref-&gt;[2][2]
</code></pre>
<h2>DEBUGGING</h2>
<p> You can use the debugger&#8217;s <code>&quot;x&quot;</code> command to dump out complex data structures. For example, given the assignment to <code>$AoA</code> above, here&#8217;s the debugger output: </p>
<pre><code>    DB&lt;1&gt; x $AoA
    $AoA = ARRAY(0x13b5a0)
       0 ARRAY(0x1f0a24)
          0 'fred'
          1 'barney'
          2 'pebbles'
          3 'bambam'
          4 'dino'
       1 ARRAY(0x13b558)
          0 'homer'
          1 'bart'
          2 'marge'
          3 'maggie'
       2 ARRAY(0x13b540)
          0 'george'
          1 'jane'
          2 'elroy'
          3 'judy'
</code></pre>
<h2>CODE EXAMPLES</h2>
<p> Presented with little comment (these will get their own manpages someday) here are short code examples illustrating access of various types of data structures.  </p>
<h2>ARRAYS OF ARRAYS</h2>
<font SIZE="-1"></font><h3>Declaration of an ARRAY OF ARRAYS</h3>
<pre><code> @AoA = (
        [ &quot;fred&quot;, &quot;barney&quot; ],
        [ &quot;george&quot;, &quot;jane&quot;, &quot;elroy&quot; ],
        [ &quot;homer&quot;, &quot;marge&quot;, &quot;bart&quot; ],
      );
</code></pre>
<font SIZE="-1"></font><h3>Generation of an ARRAY OF ARRAYS</h3>
<pre><code> # reading from file
 while ( &lt;&gt; ) {
     push @AoA, [ split ];
 }
 # calling a function
 for $i ( 1 .. 10 ) {
     $AoA[$i] = [ somefunc($i) ];
 }
 # using temp vars
 for $i ( 1 .. 10 ) {
     @tmp = somefunc($i);
     $AoA[$i] = [ @tmp ];
 }
 # add to an existing row
 push @{ $AoA[0] }, &quot;wilma&quot;, &quot;betty&quot;;
</code></pre>
<font SIZE="-1"></font><h3>Access and Printing of an ARRAY OF ARRAYS</h3>
<pre><code> # one element
 $AoA[0][0] = &quot;Fred&quot;;
 # another element
 $AoA[1][1] =~ s/(\w)/\u$1/;
 # print the whole thing with refs
 for $aref ( @AoA ) {
     print &quot;\t [ @$aref ],\n&quot;;
 }
 # print the whole thing with indices
 for $i ( 0 .. $#AoA ) {
     print &quot;\t [ @{$AoA[$i]} ],\n&quot;;
 }
 # print the whole thing one at a time
 for $i ( 0 .. $#AoA ) {
     for $j ( 0 .. $#{ $AoA[$i] } ) {
         print &quot;elt $i $j is $AoA[$i][$j]\n&quot;;
     }
 }
</code></pre>
<h2>HASHES OF ARRAYS</h2>
<font SIZE="-1"></font><h3>Declaration of a HASH OF ARRAYS</h3>
<pre><code> %HoA = (
        flintstones =&gt; [ &quot;fred&quot;, &quot;barney&quot; ],
        jetsons =&gt; [ &quot;george&quot;, &quot;jane&quot;, &quot;elroy&quot; ],
        simpsons =&gt; [ &quot;homer&quot;, &quot;marge&quot;, &quot;bart&quot; ],
      );
</code></pre>
<font SIZE="-1"></font><h3>Generation of a HASH OF ARRAYS</h3>
<pre><code> # reading from file
 # flintstones: fred barney wilma dino
 while ( &lt;&gt; ) {
     next unless s/^(.*?):\s*//;
     $HoA{$1} = [ split ];
 }
 # reading from file; more temps
 # flintstones: fred barney wilma dino
 while ( $line = &lt;&gt; ) {
     ($who, $rest) = split /:\s*/, $line, 2;
     @fields = split ' ', $rest;
     $HoA{$who} = [ @fields ];
 }
 # calling a function that returns a list
 for $group ( &quot;simpsons&quot;, &quot;jetsons&quot;, &quot;flintstones&quot; ) {
     $HoA{$group} = [ get_family($group) ];
 }
 # likewise, but using temps
 for $group ( &quot;simpsons&quot;, &quot;jetsons&quot;, &quot;flintstones&quot; ) {
     @members = get_family($group);
     $HoA{$group} = [ @members ];
 }
 # append new members to an existing family
 push @{ $HoA{&quot;flintstones&quot;} }, &quot;wilma&quot;, &quot;betty&quot;;
</code></pre>
<font SIZE="-1"></font><h3>Access and Printing of a HASH OF ARRAYS</h3>
<pre><code> # one element
 $HoA{flintstones}[0] = &quot;Fred&quot;;
 # another element
 $HoA{simpsons}[1] =~ s/(\w)/\u$1/;
 # print the whole thing
 foreach $family ( keys %HoA ) {
     print &quot;$family: @{ $HoA{$family} }\n&quot;
 }
 # print the whole thing with indices
 foreach $family ( keys %HoA ) {
     print &quot;family: &quot;;
     foreach $i ( 0 .. $#{ $HoA{$family} } ) {
         print &quot; $i = $HoA{$family}[$i]&quot;;
     }
     print &quot;\n&quot;;
 }
 # print the whole thing sorted by number of members
 foreach $family ( sort { @{$HoA{$b}} &lt;=&gt; @{$HoA{$a}} } keys %HoA ) {
     print &quot;$family: @{ $HoA{$family} }\n&quot;
 }
 # print the whole thing sorted by number of members and name
 foreach $family ( sort {
                            @{$HoA{$b}} &lt;=&gt; @{$HoA{$a}}
                                        ||
                                    $a cmp $b
            } keys %HoA )
 {
     print &quot;$family: &quot;, join(&quot;, &quot;, sort @{ $HoA{$family} }), &quot;\n&quot;;
 }
</code></pre>
<h2>ARRAYS OF HASHES</h2>
<font SIZE="-1"></font><h3>Declaration of an ARRAY OF HASHES</h3>
<pre><code> @AoH = (
        {
            Lead =&gt; &quot;fred&quot;,
            Friend =&gt; &quot;barney&quot;,
        },
        {
            Lead =&gt; &quot;george&quot;,
            Wife =&gt; &quot;jane&quot;,
            Son =&gt; &quot;elroy&quot;,
        },
        {
            Lead =&gt; &quot;homer&quot;,
            Wife =&gt; &quot;marge&quot;,
            Son =&gt; &quot;bart&quot;,
        }
  );
</code></pre>
<font SIZE="-1"></font><h3>Generation of an ARRAY OF HASHES</h3>
<pre><code> # reading from file
 # format: LEAD=fred FRIEND=barney
 while ( &lt;&gt; ) {
     $rec = {};
     for $field ( split ) {
         ($key, $value) = split /=/, $field;
         $rec-&gt;{$key} = $value;
     }
     push @AoH, $rec;
 }
 # reading from file
 # format: LEAD=fred FRIEND=barney
 # no temp
 while ( &lt;&gt; ) {
     push @AoH, { split /[\s+=]/ };
 }
 # calling a function that returns a key/value pair list, like
 # &quot;lead&quot;,&quot;fred&quot;,&quot;daughter&quot;,&quot;pebbles&quot;
 while ( %fields = getnextpairset() ) {
     push @AoH, { %fields };
 }
 # likewise, but using no temp vars
 while (&lt;&gt;) {
     push @AoH, { parsepairs($_) };
 }
 # add key/value to an element
 $AoH[0]{pet} = &quot;dino&quot;;
 $AoH[2]{pet} = &quot;santa's little helper&quot;;
</code></pre>
<font SIZE="-1"></font><h3>Access and Printing of an ARRAY OF HASHES</h3>
<pre><code> # one element
 $AoH[0]{lead} = &quot;fred&quot;;
 # another element
 $AoH[1]{lead} =~ s/(\w)/\u$1/;
 # print the whole thing with refs
 for $href ( @AoH ) {
     print &quot;{ &quot;;
     for $role ( keys %$href ) {
         print &quot;$role=$href-&gt;{$role} &quot;;
     }
     print &quot;}\n&quot;;
 }
 # print the whole thing with indices
 for $i ( 0 .. $#AoH ) {
     print &quot;$i is { &quot;;
     for $role ( keys %{ $AoH[$i] } ) {
         print &quot;$role=$AoH[$i]{$role} &quot;;
     }
     print &quot;}\n&quot;;
 }
 # print the whole thing one at a time
 for $i ( 0 .. $#AoH ) {
     for $role ( keys %{ $AoH[$i] } ) {
         print &quot;elt $i $role is $AoH[$i]{$role}\n&quot;;
     }
 }
</code></pre>
<h2>HASHES OF HASHES</h2>
<font SIZE="-1"></font><h3>Declaration of a HASH OF HASHES</h3>
<pre><code> %HoH = (
        flintstones =&gt; {
                lead =&gt; &quot;fred&quot;,
                pal =&gt; &quot;barney&quot;,
        },
        jetsons =&gt; {
                lead =&gt; &quot;george&quot;,
                wife =&gt; &quot;jane&quot;,
                &quot;his boy&quot; =&gt; &quot;elroy&quot;,
        },
        simpsons =&gt; {
                lead =&gt; &quot;homer&quot;,
                wife =&gt; &quot;marge&quot;,
                kid =&gt; &quot;bart&quot;,
        },
 );
</code></pre>
<font SIZE="-1"></font><h3>Generation of a HASH OF HASHES</h3>
<pre><code> # reading from file
 # flintstones: lead=fred pal=barney wife=wilma pet=dino
 while ( &lt;&gt; ) {
     next unless s/^(.*?):\s*//;
     $who = $1;
     for $field ( split ) {
         ($key, $value) = split /=/, $field;
         $HoH{$who}{$key} = $value;
     }
 # reading from file; more temps
 while ( &lt;&gt; ) {
     next unless s/^(.*?):\s*//;
     $who = $1;
     $rec = {};
     $HoH{$who} = $rec;
     for $field ( split ) {
         ($key, $value) = split /=/, $field;
         $rec-&gt;{$key} = $value;
     }
 }
 # calling a function that returns a key,value hash
 for $group ( &quot;simpsons&quot;, &quot;jetsons&quot;, &quot;flintstones&quot; ) {
     $HoH{$group} = { get_family($group) };
 }
 # likewise, but using temps
 for $group ( &quot;simpsons&quot;, &quot;jetsons&quot;, &quot;flintstones&quot; ) {
     %members = get_family($group);
     $HoH{$group} = { %members };
 }
 # append new members to an existing family
 %new_folks = (
     wife =&gt; &quot;wilma&quot;,
     pet =&gt; &quot;dino&quot;,
 );
 for $what (keys %new_folks) {
     $HoH{flintstones}{$what} = $new_folks{$what};
 }
</code></pre>
<font SIZE="-1"></font><h3>Access and Printing of a HASH OF HASHES</h3>
<pre><code> # one element
 $HoH{flintstones}{wife} = &quot;wilma&quot;;
 # another element
 $HoH{simpsons}{lead} =~ s/(\w)/\u$1/;
 # print the whole thing
 foreach $family ( keys %HoH ) {
     print &quot;$family: { &quot;;
     for $role ( keys %{ $HoH{$family} } ) {
         print &quot;$role=$HoH{$family}{$role} &quot;;
     }
     print &quot;}\n&quot;;
 }
 # print the whole thing somewhat sorted
 foreach $family ( sort keys %HoH ) {
     print &quot;$family: { &quot;;
     for $role ( sort keys %{ $HoH{$family} } ) {
         print &quot;$role=$HoH{$family}{$role} &quot;;
     }
     print &quot;}\n&quot;;
 }
 # print the whole thing sorted by number of members
 foreach $family ( sort { keys %{$HoH{$b}} &lt;=&gt; keys %{$HoH{$a}} }
                                                             keys %HoH )
 {
     print &quot;$family: { &quot;;
     for $role ( sort keys %{ $HoH{$family} } ) {
         print &quot;$role=$HoH{$family}{$role} &quot;;
     }
     print &quot;}\n&quot;;
 }
 # establish a sort order (rank) for each role
 $i = 0;
 for ( qw(lead wife son daughter pal pet) ) { $rank{$_} = ++$i }
 # now print the whole thing sorted by number of members
 foreach $family ( sort { keys %{ $HoH{$b} } &lt;=&gt; keys %{ $HoH{$a} } }
                                                             keys %HoH )
 {
     print &quot;$family: { &quot;;
     # and print these according to rank order
     for $role ( sort { $rank{$a} &lt;=&gt; $rank{$b} }
                                               keys %{ $HoH{$family} } )
     {
         print &quot;$role=$HoH{$family}{$role} &quot;;
     }
     print &quot;}\n&quot;;
 }
</code></pre>
<h2>MORE ELABORATE RECORDS</h2>
<font SIZE="-1"></font><h3>Declaration of MORE ELABORATE RECORDS</h3>
<p> Here&#8217;s a sample showing how to create and use a record whose fields are of many different sorts: </p>
<pre><code>     $rec = {
         TEXT =&gt; $string,
         SEQUENCE =&gt; [ @old_values ],
         LOOKUP =&gt; { %some_table },
         THATCODE =&gt; \&amp;some_function,
         THISCODE =&gt; sub { $_[0] ** $_[1] },
         HANDLE =&gt; \*STDOUT,
     };
     print $rec-&gt;{TEXT};
     print $rec-&gt;{SEQUENCE}[0];
     $last = pop @ { $rec-&gt;{SEQUENCE} };
     print $rec-&gt;{LOOKUP}{&quot;key&quot;};
     ($first_k, $first_v) = each %{ $rec-&gt;{LOOKUP} };
     $answer = $rec-&gt;{THATCODE}-&gt;($arg);
     $answer = $rec-&gt;{THISCODE}-&gt;($arg1, $arg2);
     # careful of extra block braces on fh ref
     print { $rec-&gt;{HANDLE} } &quot;a string\n&quot;;
     use FileHandle;
     $rec-&gt;{HANDLE}-&gt;autoflush(1);
     $rec-&gt;{HANDLE}-&gt;print(&quot; a string\n&quot;);
</code></pre>
<font SIZE="-1"></font><h3>Declaration of a HASH OF COMPLEX RECORDS</h3>
<pre><code>     %TV = (
        flintstones =&gt; {
            series =&gt; &quot;flintstones&quot;,
            nights =&gt; [ qw(monday thursday friday) ],
            members =&gt; [
                { name =&gt; &quot;fred&quot;, role =&gt; &quot;lead&quot;, age =&gt; 36, },
                { name =&gt; &quot;wilma&quot;, role =&gt; &quot;wife&quot;, age =&gt; 31, },
                { name =&gt; &quot;pebbles&quot;, role =&gt; &quot;kid&quot;, age =&gt; 4, },
            ],
        },
        jetsons =&gt; {
            series =&gt; &quot;jetsons&quot;,
            nights =&gt; [ qw(wednesday saturday) ],
            members =&gt; [
                { name =&gt; &quot;george&quot;, role =&gt; &quot;lead&quot;, age =&gt; 41, },
                { name =&gt; &quot;jane&quot;, role =&gt; &quot;wife&quot;, age =&gt; 39, },
                { name =&gt; &quot;elroy&quot;, role =&gt; &quot;kid&quot;, age =&gt; 9, },
            ],
         },
        simpsons =&gt; {
            series =&gt; &quot;simpsons&quot;,
            nights =&gt; [ qw(monday) ],
            members =&gt; [
                { name =&gt; &quot;homer&quot;, role =&gt; &quot;lead&quot;, age =&gt; 34, },
                { name =&gt; &quot;marge&quot;, role =&gt; &quot;wife&quot;, age =&gt; 37, },
                { name =&gt; &quot;bart&quot;, role =&gt; &quot;kid&quot;, age =&gt; 11, },
            ],
         },
      );
</code></pre>
<font SIZE="-1"></font><h3>Generation of a HASH OF COMPLEX RECORDS</h3>
<pre><code>     # reading from file
     # this is most easily done by having the file itself be
     # in the raw data format as shown above. perl is happy
     # to parse complex data structures if declared as data, so
     # sometimes it's easiest to do that
     # here's a piece by piece build up
     $rec = {};
     $rec-&gt;{series} = &quot;flintstones&quot;;
     $rec-&gt;{nights} = [ find_days() ];
     @members = ();
     # assume this file in field=value syntax
     while (&lt;&gt;) {
         %fields = split /[\s=]+/;
         push @members, { %fields };
     }
     $rec-&gt;{members} = [ @members ];
     # now remember the whole thing
     $TV{ $rec-&gt;{series} } = $rec;
     ###########################################################
     # now, you might want to make interesting extra fields that
     # include pointers back into the same data structure so if
     # change one piece, it changes everywhere, like for example
     # if you wanted a {kids} field that was a reference
     # to an array of the kids' records without having duplicate
     # records and thus update problems.
     ###########################################################
     foreach $family (keys %TV) {
         $rec = $TV{$family}; # temp pointer
         @kids = ();
         for $person ( @{ $rec-&gt;{members} } ) {
             if ($person-&gt;{role} =~ /kid|son|daughter/) {
                 push @kids, $person;
             }
         }
         # REMEMBER: $rec and $TV{$family} point to same data!!
         $rec-&gt;{kids} = [ @kids ];
     }
     # you copied the array, but the array itself contains pointers
     # to uncopied objects. this means that if you make bart get
     # older via
     $TV{simpsons}{kids}[0]{age}++;
     # then this would also change in
     print $TV{simpsons}{members}[2]{age};
     # because $TV{simpsons}{kids}[0] and $TV{simpsons}{members}[2]
     # both point to the same underlying anonymous hash table
     # print the whole thing
     foreach $family ( keys %TV ) {
         print &quot;the $family&quot;;
         print &quot; is on during @{ $TV{$family}{nights} }\n&quot;;
         print &quot;its members are:\n&quot;;
         for $who ( @{ $TV{$family}{members} } ) {
             print &quot; $who-&gt;{name} ($who-&gt;{role}), age $who-&gt;{age}\n&quot;;
         }
         print &quot;it turns out that $TV{$family}{lead} has &quot;;
         print scalar ( @{ $TV{$family}{kids} } ), &quot; kids named &quot;;
         print join (&quot;, &quot;, map { $_-&gt;{name} } @{ $TV{$family}{kids} } );
         print &quot;\n&quot;;
     }
</code></pre>
<h2>Database Ties</h2>
<p> You cannot easily tie a multilevel data structure (such as a hash of hashes) to a dbm file. The first problem is that all but <font SIZE="-1">GDBM</font> and Berkeley <font SIZE="-1">DB</font> have size limitations, but beyond that, you also have problems with how references are to be represented on disk. One experimental module that does partially attempt to address this need is the <font SIZE="-1">MLDBM</font> module. Check your nearest <font SIZE="-1">CPAN</font> site as described in perlmodlib for source code to <font SIZE="-1">MLDBM.</font>  </p>
<h2>SEE ALSO</h2>
<p> perlref, perllol, perldata, perlobj  </p>
<h2>AUTHOR</h2>
<p> Tom Christiansen &lt;<i>tchrist [at] perl.com</i>&gt; </p>
