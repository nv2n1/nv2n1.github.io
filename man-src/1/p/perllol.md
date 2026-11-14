---
title: "perllol(1)"
name: "perllol"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perllol/"
---

<h2 class="name">NAME</h2>
 

 perllol - Manipulating Arrays of Arrays in Perl 

<h2>DESCRIPTION</h2>

<h3>Declaration and Access of Arrays of Arrays</h3>

 The simplest two-level data structure to build in Perl is an array of arrays, sometimes casually called a list of lists. It's reasonably easy to understand, and almost everything that applies here will also be applicable later on with the fancier data structures. 

 An array of an array is just a regular old array <tt>@AoA</tt> that you can get at with two subscripts, like <tt>$AoA[3][2]</tt>. Here's a declaration of the array: 

 <pre><code>
use 5.010;
#so we can use say()
#assign to our array, an array of array references
    @AoA = ([
        "fred",
        "barney",
        "pebbles",
        "bambam",
        "dino",
    ],
            [
                "george",
                "jane",
                "elroy",
                "judy",
            ],
            [
                "homer",
                "bart",
                "marge",
                "maggie",
            ], );
say $AoA[2][1];
bart
</code></pre> 

 Now you should be very careful that the outer bracket type is a round one, that is, a parenthesis. That's because you're assigning to an <tt>@array</tt>, so you need parentheses. If you wanted there <i>not</i> to be an <tt>@AoA</tt>, but rather just a reference to it, you could do something more like this: 

 
#assign a reference to array of array references
$ref_to_AoA = [
    [
        "fred",
        "barney",
        "pebbles",
        "bambam",
        "dino",
    ],
    [
        "george",
        "jane",
        "elroy",
        "judy",
    ],
    [
        "homer",
        "bart",
        "marge",
        "maggie",
    ],
];
say $ref_to_AoA-&gt;[2][1];
bart
 

 Notice that the outer bracket type has changed, and so our access syntax has also changed. That's because unlike C, in perl you can't freely interchange arrays and references thereto. <tt>$ref_to_AoA</tt> is a reference to an array, whereas <tt>@AoA</tt> is an array proper. Likewise, <tt>$AoA[2]</tt> is not an array, but an array ref. So how come you can write these: 

 
$AoA[2][2] $ref_to_AoA-&gt;[2][2]
 

 instead of having to write these: 

 
$AoA[2]-&gt;[2] $ref_to_AoA -&gt; [2] -&gt; [2]
 

 Well, that's because the rule is that on adjacent brackets only (whether square or curly), you are free to omit the pointer dereferencing arrow. But you cannot do so for the very first one if it's a scalar containing a reference, which means that <tt>$ref_to_AoA</tt> always needs it.

<h3>Growing Your Own</h3>

 That's all well and good for declaration of a fixed data structure, but what if you wanted to add new elements on the fly, or build it up entirely from scratch? 

 First, let's look at reading it in from a file. This is something like adding a row at a time. We'll assume that there's a flat file in which each line is a row and each word an element. If you're trying to develop an <tt>@AoA</tt> array containing all these, here's the right way to do that: 

 
while (&lt;&gt;) {
    @tmp = split;
    push @AoA, [@tmp];
}
 

 You might also have loaded that from a function: 

 
    for
        $i(1..10)
        {
            $AoA[$i] = [somefunc($i)];
        }
 

 Or you might have had a temporary variable sitting around with the array in it. 

 
    for
        $i(1..10)
        {
            @tmp = somefunc($i);
            $AoA[$i] = [@tmp];
        }
 

 It's important you make sure to use the <tt>&quot;[ ]&quot;</tt> array reference constructor. That's because this wouldn't work: 

 <pre>
    $AoA[$i] = @tmp;   # WRONG!
</pre> 

 The reason that doesn't do what you want is because assigning a named array like that to a scalar is taking an array in scalar context, which means just counts the number of elements in <tt>@tmp</tt>. 

 If you are running under <tt>&quot;use strict&quot;</tt> (and if you aren't, why in the world aren't you?), you'll have to add some declarations to make it happy: 

 
use strict;
my(@AoA, @tmp);
while (&lt;&gt;) {
    @tmp = split;
    push @AoA, [@tmp];
}
 

 Of course, you don't need the temporary array to have a name at all: 

 
while (&lt;&gt;) {
    push @AoA, [split];
}
 

 You also don't have to use <b>push()</b>. You could just make a direct assignment if you knew where you wanted to put it: 

 
my(@AoA, $i, $line);
    for
        $i(0..10)
        {
            $line = &lt;&gt;;
            $AoA[$i] = [ split " ", $line ];
        }
 

 or even just 

 
my(@AoA, $i);
    for
        $i(0..10)
        {
            $AoA[$i] = [ split " ", &lt;&gt; ];
        }
 

 You should in general be leery of using functions that could potentially return lists in scalar context without explicitly stating such. This would be clearer to the casual reader: 

 
my(@AoA, $i);
    for
        $i(0..10)
        {
            $AoA[$i] = [ split " ", scalar(&lt;&gt;) ];
        }
 

 If you wanted to have a <tt>$ref_to_AoA</tt> variable as a reference to an array, you'd have to do something like this: 

 
while (&lt;&gt;) {
    push @$ref_to_AoA, [split];
}
 

 Now you can add new rows. What about adding new columns? If you're dealing with just matrices, it's often easiest to use simple assignment: 

 
    for
        $x(1..10)
        {
        for
            $y(1..10)
            {
                $AoA[$x][$y] = func($x, $y);
            }
        }
    for
        $x(3, 7, 9)
        {
            $AoA[$x][20] += func2($x);
        }
 

 It doesn't matter whether those elements are already there or not: it'll gladly create them for you, setting intervening elements to <tt>&quot;undef&quot;</tt> as need be. 

 If you wanted just to append to a row, you'd have to do something a bit funnier looking: 

 
#add new columns to an existing row
push @{$AoA[0]}, "wilma", "betty";
#explicit deref


<h3>Access and Printing</h3>

 Now it's time to print your data structure out. How are you going to do that? Well, if you want only one of the elements, it's trivial: 

 
print $AoA[0][0];
 

 If you want to print the whole thing, though, you can't say 

 <pre>
    print @AoA;         # WRONG
</pre> 

 because you'll get just references listed, and perl will never automatically dereference things for you. Instead, you have to roll yourself a loop or two. This prints the whole structure, using the shell-style <b>for()</b> construct to loop across the outer set of subscripts. 

 
    for
        $aref(@AoA)
        {
            say "\t [ @$aref ],";
        }
 

 If you wanted to keep track of subscripts, you might do this: 

 
    for
        $i(0..$ #AoA)
        {
            say "\t elt $i is [ @{$AoA[$i]} ],";
        }
 

 or maybe even this. Notice the inner loop. 

 
    for
        $i(0..$ #AoA)
        {
        for
            $j(0..$ #{$AoA[$i]})
            {
                say "elt $i $j is $AoA[$i][$j]";
            }
        }
 

 As you can see, it's getting a bit complicated. That's why sometimes is easier to take a temporary on your way through: 

 
    for
        $i(0..$ #AoA)
        {
            $aref = $AoA[$i];
        for
            $j(0..$ #{$aref})
            {
                say "elt $i $j is $AoA[$i][$j]";
            }
        }
 

 Hmm... that's still a bit ugly. How about this: 

 
    for
        $i(0..$ #AoA)
        {
            $aref = $AoA[$i];
            $n = @$aref - 1;
        for
            $j(0..$n)
            {
                say "elt $i $j is $AoA[$i][$j]";
            }
        }
 

 When you get tired of writing a custom print for your data structures, you might look at the standard Dumpvalue or Data::Dumper modules. The former is what the Perl debugger uses, while the latter generates parsable Perl code. For example: 

 
use v5 .14;
#using the + prototype, new to v5 .14 sub show(+)
{
    require Dumpvalue;
        state $prettily = new Dumpvalue::
                            tick        =&gt; q("),
                            compactDump =&gt; 1,  # comment these two lines
#out
                            veryCompact =&gt; 1,  # if you want a bigger
#dump
                        ;
        dumpValue $prettily @_;
}
#Assign a list of array references to an array.
my @AoA = ([ "fred", "barney" ],
           [ "george", "jane", "elroy" ],
           [ "homer", "marge", "bart" ], );
push @{$AoA[0]}, "wilma", "betty";
show @AoA;
 

 will print out: 

 <pre>
    0  0..3  &quot;fred&quot; &quot;barney&quot; &quot;wilma&quot; &quot;betty&quot;
    1  0..2  &quot;george&quot; &quot;jane&quot; &quot;elroy&quot;
    2  0..2  &quot;homer&quot; &quot;marge&quot; &quot;bart&quot;
</pre> 

 Whereas if you comment out the two lines I said you might wish to, then it shows it to you this way instead: 

 <pre>
    0  ARRAY(0x8031d0)
       0  &quot;fred&quot;
       1  &quot;barney&quot;
       2  &quot;wilma&quot;
       3  &quot;betty&quot;
    1  ARRAY(0x803d40)
       0  &quot;george&quot;
       1  &quot;jane&quot;
       2  &quot;elroy&quot;
    2  ARRAY(0x803e10)
       0  &quot;homer&quot;
       1  &quot;marge&quot;
       2  &quot;bart&quot;
</pre>

<h3>Slices</h3>

 If you want to get at a slice (part of a row) in a multidimensional array, you're going to have to do some fancy subscripting. That's because while we have a nice synonym for single elements via the pointer arrow for dereferencing, no such convenience exists for slices. 

 Here's how to do one operation using a loop. We'll assume an <tt>@AoA</tt> variable as before. 

 
@part = ();
$x = 4;
for ($y = 7; $y &lt; 13; $y++) {
    push @part, $AoA[$x][$y];
}
 

 That same loop could be replaced with a slice operation: 

 
@part = @{$AoA[4]}[7..12];
 

 or spaced out a bit: 

 
@part = @{$AoA[4]}[7..12];
 

 But as you might well imagine, this can get pretty rough on the reader. 

 Ah, but what if you wanted a <i>two-dimensional slice</i>, such as having <tt>$x</tt> run from 4..8 and <tt>$y</tt> run from 7 to 12? Hmm... here's the simple way: 

 
@newAoA = ();
for ($startx = $x = 4; $x &lt;= 8; $x++) {
    for ($starty = $y = 7; $y &lt;= 12; $y++) {
        $newAoA[$x - $startx][$y - $starty] = $AoA[$x][$y];
    }
}
 

 We can reduce some of the looping through slices 

 
for ($x = 4; $x &lt;= 8; $x++) {
    push @newAoA, [@{$AoA[$x]}[7..12]];
}
 

 If you were into Schwartzian Transforms, you would probably have selected map for that 

 
@newAoA = map
{
    [@{$AoA[$_]}[7..12]]
}
4..8;
 

 Although if your manager accused you of seeking job security (or rapid insecurity) through inscrutable code, it would be hard to argue. :-) If I were you, I'd put that in a function: 

 <pre><code>
@newAoA = splice_2D( \@AoA, 4 = &gt; 8, 7 = &gt; 12);
sub splice_2D
{
    my $lrr = shift;
#ref to array of array refs !my($x_lo, $x_hi,
                                    $y_lo, $y_hi) = @_;
    return map
    {
        [@{$lrr-&gt;[$_]}[$y_lo..$y_hi]]
    }
    $x_lo..$x_hi;
}
</code></pre>

<h2>SEE ALSO</h2>

 perldata, perlref, perldsc

<h2>AUTHOR</h2>

 Tom Christiansen &lt;<i>tchrist [at] perl.com</i>&gt; 

 Last update: Tue Apr 26 18:30:55 <font SIZE="-1">MDT 2011</font> 

<h2>Index</h2>


