---
title: "pdlthreading(1)"
name: "pdlthreading"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdlthreading/"
description: "PDL::Threading – Tutorial for PDL’s Threading feature"
---

<p>PDL::Threading &#8211; Tutorial for PDL&#8217;s Threading feature </p>
<h2>Introduction</h2>
<p>One of the most powerful features of <font SIZE="-1">PDL</font> is <code>threading</code>, which can produce very compact and very fast <font SIZE="-1">PDL</font> code by avoiding multiple nested for loops that C and <font SIZE="-1">BASIC</font> users may be familiar with. The trouble is that it can take some getting used to, and new users may not appreciate the benefits of threading. </p>
<p> Other vector based languages, such as <font SIZE="-1">MATLAB,</font> use a subset of threading techniques, but <font SIZE="-1">PDL</font> shines by completely generalizing them for all sorts of vector-based applications.</p>
<h2>Terminology: Piddle</h2>
<p><font SIZE="-1">MATLAB</font> typically refers to vectors, matrices, and arrays. Perl already has arrays, and the terms &#8220;vector&#8221; and &#8220;matrix&#8221; typically refer to one- and two-dimensional collections of data. Having no good term to describe their object, <font SIZE="-1">PDL</font> developers coined the term &quot;<i>piddle</i>&quot; to give a name to their data type. </p>
<p> A <i>piddle</i> consists of a series of numbers organized as an N-dimensional data set. Piddles provide efficient storage and fast computation of large N-dimensional matrices. They are highly optimized for numerical work.</p>
<h2>Thinking In Terms Of Threading</h2>
<p>If you have used <font SIZE="-1">PDL</font> for a little while already, you may have been using threading without realising it. Start the <font SIZE="-1">PDL</font> shell (type <tt>&quot;perldl&quot;</tt> or <tt>&quot;pdl2&quot;</tt> on a terminal). Most examples in this tutorial use the <font SIZE="-1">PDL</font> shell. Make sure that PDL::NiceSlice and PDL::AutoLoader are enabled. For example: </p>
<pre> % pdl2
 perlDL shell v1.352
 ...
 ReadLines, NiceSlice, MultiLines enabled
 ...
 Note: AutoLoader not enabled ('use PDL::AutoLoader' recommended)
 pdl&gt;</pre>
<p>In this example, NiceSlice was automatically enabled, but AutoLoader was not. To enable it, type <tt>&quot;use PDL::AutoLoader&quot;</tt>. </p>
<p> Let&#8217;s start with a two-dimensional <i>piddle</i>: </p>
<pre> pdl&gt; $a = sequence(11,9)
 pdl&gt; p $a
 [
 [ 0 1 2 3 4 5 6 7 8 9 10]
 [11 12 13 14 15 16 17 18 19 20 21]
 [22 23 24 25 26 27 28 29 30 31 32]
 [33 34 35 36 37 38 39 40 41 42 43]
 [44 45 46 47 48 49 50 51 52 53 54]
 [55 56 57 58 59 60 61 62 63 64 65]
 [66 67 68 69 70 71 72 73 74 75 76]
 [77 78 79 80 81 82 83 84 85 86 87]
 [88 89 90 91 92 93 94 95 96 97 98]
 ]</pre>
<p>The <tt>&quot;info&quot;</tt> method gives you basic information about a <i>piddle</i>: </p>
<pre> pdl&gt; p $a-&gt;info
 PDL: Double D [11,9]</pre>
<p>This tells us that <tt>$a</tt> is an 11 x 9 <i>piddle</i> composed of double precision numbers. If we wanted to add 3 to all elements in an <tt>&quot;n x m&quot;</tt> piddle, a traditional language would use two nested for-loops: </p>
<pre> # Pseudo-code. Traditional way to add 3 to an array.
 for (x=0; x &lt; n; x++) {
 for (y=0; y &lt; m; y++) {
 a(x,y) = a(x,y) + 3
 }
 }</pre>
<p><code>Note</code>: Notice that indices start at 0, as in Perl, C and Java (and unlike <font SIZE="-1">MATLAB</font> and <font SIZE="-1">IDL</font>). </p>
<p> But with <font SIZE="-1">PDL,</font> we can just write: </p>
<pre> pdl&gt; $b = $a + 3
 pdl&gt; p $b
 [
 [ 3 4 5 6 7 8 9 10 11 12 13]
 [ 14 15 16 17 18 19 20 21 22 23 24]
 [ 25 26 27 28 29 30 31 32 33 34 35]
 [ 36 37 38 39 40 41 42 43 44 45 46]
 [ 47 48 49 50 51 52 53 54 55 56 57]
 [ 58 59 60 61 62 63 64 65 66 67 68]
 [ 69 70 71 72 73 74 75 76 77 78 79]
 [ 80 81 82 83 84 85 86 87 88 89 90]
 [ 91 92 93 94 95 96 97 98 99 100 101]
 ]</pre>
<p>This is the simplest example of threading, and it is something that all numerical software tools do. The <tt>&quot;+ 3&quot;</tt> operation was automatically applied along two dimensions. Now suppose you want to to subtract a line from every row in <tt>$a</tt>: </p>
<pre> pdl&gt; $line = sequence(11)
 pdl&gt; p $line
 [0 1 2 3 4 5 6 7 8 9 10]
 pdl&gt; $c = $a - $line
 pdl&gt; p $c
 [
 [ 0 0 0 0 0 0 0 0 0 0 0]
 [11 11 11 11 11 11 11 11 11 11 11]
 [22 22 22 22 22 22 22 22 22 22 22]
 [33 33 33 33 33 33 33 33 33 33 33]
 [44 44 44 44 44 44 44 44 44 44 44]
 [55 55 55 55 55 55 55 55 55 55 55]
 [66 66 66 66 66 66 66 66 66 66 66]
 [77 77 77 77 77 77 77 77 77 77 77]
 [88 88 88 88 88 88 88 88 88 88 88]
 ]</pre>
<p>Two things to note here: First, the value of <tt>$a</tt> is still the same. Try <tt>&quot;p $a&quot;</tt> to check. Second, <font SIZE="-1">PDL</font> automatically subtracted <tt>$line</tt> from each row in <tt>$a</tt>. Why did it do that? Let&#8217;s look at the dimensions of <tt>$a</tt>, <tt>$line</tt> and <tt>$c</tt>: </p>
<pre> pdl&gt; p $line-&gt;info =&gt; PDL: Double D [11]
 pdl&gt; p $a-&gt;info =&gt; PDL: Double D [11,9]
 pdl&gt; p $c-&gt;info =&gt; PDL: Double D [11,9]</pre>
<p>So, both <tt>$a</tt> and <tt>$line</tt> have the same number of elements in the 0th dimension! What <font SIZE="-1">PDL</font> then did was thread over the higher dimensions in <tt>$a</tt> and repeated the same operation 9 times to all the rows on <tt>$a</tt>. This is <font SIZE="-1">PDL</font> threading in action. </p>
<p> What if you want to subtract <tt>$line</tt> from the first line in <tt>$a</tt> only? You can do that by specifying the line explicitly: </p>
<pre> pdl&gt; $a(:,0) -= $line
 pdl&gt; p $a
 [
 [ 0 0 0 0 0 0 0 0 0 0 0]
 [11 12 13 14 15 16 17 18 19 20 21]
 [22 23 24 25 26 27 28 29 30 31 32]
 [33 34 35 36 37 38 39 40 41 42 43]
 [44 45 46 47 48 49 50 51 52 53 54]
 [55 56 57 58 59 60 61 62 63 64 65]
 [66 67 68 69 70 71 72 73 74 75 76]
 [77 78 79 80 81 82 83 84 85 86 87]
 [88 89 90 91 92 93 94 95 96 97 98]
 ]</pre>
<p>See PDL::Indexing and PDL::NiceSlice to learn more about specifying subsets from piddles. </p>
<p> The true power of threading comes when you realise that the piddle can have any number of dimensions! Let&#8217;s make a 4 dimensional piddle: </p>
<pre> pdl&gt; $piddle_4D = sequence(11,3,7,2)
 pdl&gt; $c = $piddle_4D - $line</pre>
<p>Now <tt>$c</tt> is a piddle of the same dimension as <tt>$piddle_4D</tt>. </p>
<pre> pdl&gt; p $piddle_4D-&gt;info =&gt; PDL: Double D [11,3,7,2]
 pdl&gt; p $c-&gt;info =&gt; PDL: Double D [11,3,7,2]</pre>
<p>This time <font SIZE="-1">PDL</font> has threaded over three higher dimensions automatically, subtracting <tt>$line</tt> all the way. </p>
<p> But, maybe you don&#8217;t want to subtract from the rows (dimension 0), but from the columns (dimension 1). How do I subtract a column of numbers from each column in <tt>$a</tt>? </p>
<pre> pdl&gt; $cols = <a href="//www.systutorials.com/docs/linux/man/9-sequence/">sequence</a>(9)
 pdl&gt; p $a-&gt;info =&gt; PDL: Double D [11,9]
 pdl&gt; p $cols-&gt;info =&gt; PDL: Double D [9]</pre>
<p>Naturally, we can&#8217;t just type <tt>&quot;$a - $cols&quot;</tt>. The dimensions don&#8217;t match: </p>
<pre> pdl&gt; p $a - $cols
 PDL: PDL::Ops::minus(a,b,c): Parameter 'b'
 PDL: Mismatched implicit thread dimension 0: should be 11, is 9</pre>
<p>How do we tell <font SIZE="-1">PDL</font> that we want to subtract from dimension 1 instead?</p>
<h2>Manipulating Dimensions</h2>
<p>There are many <font SIZE="-1">PDL</font> functions that let you rearrange the dimensions of <font SIZE="-1">PDL</font> arrays. They are mostly covered in PDL::Slices. The three most common ones are: </p>
<pre> xchg
 mv
 reorder</pre>
<h3>Method: xchg</h3>
<p>The <tt>&quot;xchg&quot;</tt> method &quot;<code>exchanges</code>&quot; two dimensions in a piddle: </p>
<pre> pdl&gt; $a = sequence(6,7,8,9)
 pdl&gt; $a_xchg = $a-&gt;xchg(0,3)
 
 pdl&gt; p $a-&gt;info =&gt; PDL: Double D [6,7,8,9]
 pdl&gt; p $a_xchg-&gt;info =&gt; PDL: Double D [9,7,8,6]
 | |
 V V
 (dim 0) (dim 3)</pre>
<p>Notice that dimensions 0 and 3 were exchanged without affecting the other dimensions. Notice also that <tt>&quot;xchg&quot;</tt> does not alter <tt>$a</tt>. The original variable <tt>$a</tt> remains untouched.</p>
<h3>Method: mv</h3>
<p>The <tt>&quot;mv&quot;</tt> method &quot;<code>moves</code>&quot; one dimension, in a piddle, shifting other dimensions as necessary. </p>
<pre> pdl&gt; $a = sequence(6,7,8,9) (dim 0)
 pdl&gt; $a_mv = $a-&gt;mv(0,3) |
 pdl&gt; V _____
 pdl&gt; p $a-&gt;info =&gt; PDL: Double D [6,7,8,9]
 pdl&gt; p $a_mv-&gt;info =&gt; PDL: Double D [7,8,9,6]
 ----- |
 V
 (dim 3)</pre>
<p>Notice that when dimension 0 was moved to position 3, all the other dimensions had to be shifted as well. Notice also that <tt>&quot;mv&quot;</tt> does not alter <tt>$a</tt>. The original variable <tt>$a</tt> remains untouched.</p>
<h3>Method: reorder</h3>
<p>The <tt>&quot;reorder&quot;</tt> method is a generalization of the <tt>&quot;xchg&quot;</tt> and <tt>&quot;mv&quot;</tt> methods. It &quot;<code>reorders</code>&quot; the dimensions in any way you specify: </p>
<pre> pdl&gt; $a = sequence(6,7,8,9)
 pdl&gt; $a_reorder = $a-&gt;reorder(3,0,2,1)
 pdl&gt;
 pdl&gt; p $a-&gt;info =&gt; PDL: Double D [6,7,8,9]
 pdl&gt; p $a_reorder-&gt;info =&gt; PDL: Double D [9,6,8,7]
 | | | |
 V V v V
 dimensions: 0 1 2 3</pre>
<p>Notice what happened. When we wrote <tt>&quot;reorder(3,0,2,1)&quot;</tt> we instructed <font SIZE="-1">PDL</font> to: </p>
<pre> * Put dimension 3 first.
 * Put dimension 0 next.
 * Put dimension 2 next.
 * Put dimension 1 next.</pre>
<p>When you use the <tt>&quot;reorder&quot;</tt> method, all the dimensions are shuffled. Notice that <tt>&quot;reorder&quot;</tt> does not alter <tt>$a</tt>. The original variable <tt>$a</tt> remains untouched.</p>
<h2>Gotcha: Linking Vs Assignment</h2>
<h3>Linking</h3>
<p>By default, piddles are <code>linked together</code> so that changes on one will go back and affect the original <code>as well</code>. </p>
<pre> pdl&gt; $a = sequence(4,5)
 pdl&gt; $a_xchg = $a-&gt;xchg(1,0)</pre>
<p>Here, <tt>$a_xchg</tt> <code>is not a separate object</code>. It is merely a different way of looking at <tt>$a</tt>. Any change in <tt>$a_xchg</tt> will appear in <tt>$a</tt> as well. </p>
<pre> pdl&gt; p $a
 [
 [ 0 1 2 3]
 [ 4 5 6 7]
 [ 8 9 10 11]
 [12 13 14 15]
 [16 17 18 19]
 ]
 pdl&gt; $a_xchg += 3
 pdl&gt; p $a
 [
 [ 3 4 5 6]
 [ 7 8 9 10]
 [11 12 13 14]
 [15 16 17 18]
 [19 20 21 22]
 ]</pre>
<h3>Assignment</h3>
<p>Some times, linking is not the behaviour you want. If you want to make the piddles independent, use the <tt>&quot;copy&quot;</tt> method: </p>
<pre> pdl&gt; $a = sequence(4,5)
 pdl&gt; $a_xchg = $a-&gt;copy-&gt;xchg(1,0)</pre>
<p>Now <tt>$a</tt> and <tt>$a_xchg</tt> are completely separate objects: </p>
<pre> pdl&gt; p $a
 [
 [ 0 1 2 3]
 [ 4 5 6 7]
 [ 8 9 10 11]
 [12 13 14 15]
 [16 17 18 19]
 ]
 pdl&gt; $a_xchg += 3
 pdl&gt; p $a
 [
 [ 0 1 2 3]
 [ 4 5 6 7]
 [ 8 9 10 11]
 [12 13 14 15]
 [16 17 18 19]
 ]
 pdl&gt; $a_xchg
 [
 [ 3 7 11 15 19]
 [ 4 8 12 16 20]
 [ 5 9 13 17 21]
 [ 6 10 14 18 22]
 ]</pre>
<h2>Putting It All Together</h2>
<p>Now we are ready to solve the problem that motivated this whole discussion: </p>
<pre> pdl&gt; $a = sequence(11,9)
 pdl&gt; $cols = <a href="//www.systutorials.com/docs/linux/man/9-sequence/">sequence</a>(9)
 pdl&gt;
 pdl&gt; p $a-&gt;info =&gt; PDL: Double D [11,9]
 pdl&gt; p $cols-&gt;info =&gt; PDL: Double D [9]</pre>
<p>How do we tell <font SIZE="-1">PDL</font> to subtract <tt>$cols</tt> along dimension 1 instead of dimension 0? The simplest way is to use the <tt>&quot;xchg&quot;</tt> method and rely on <font SIZE="-1">PDL</font> linking: </p>
<pre> pdl&gt; p $a
 [
 [ 0 1 2 3 4 5 6 7 8 9 10]
 [11 12 13 14 15 16 17 18 19 20 21]
 [22 23 24 25 26 27 28 29 30 31 32]
 [33 34 35 36 37 38 39 40 41 42 43]
 [44 45 46 47 48 49 50 51 52 53 54]
 [55 56 57 58 59 60 61 62 63 64 65]
 [66 67 68 69 70 71 72 73 74 75 76]
 [77 78 79 80 81 82 83 84 85 86 87]
 [88 89 90 91 92 93 94 95 96 97 98]
 ]
 pdl&gt; $a-&gt;xchg(1,0) -= $cols
 pdl&gt; p $a
 [
 [ 0 1 2 3 4 5 6 7 8 9 10]
 [10 11 12 13 14 15 16 17 18 19 20]
 [20 21 22 23 24 25 26 27 28 29 30]
 [30 31 32 33 34 35 36 37 38 39 40]
 [40 41 42 43 44 45 46 47 48 49 50]
 [50 51 52 53 54 55 56 57 58 59 60]
 [60 61 62 63 64 65 66 67 68 69 70]
 [70 71 72 73 74 75 76 77 78 79 80]
 [80 81 82 83 84 85 86 87 88 89 90]
 ]</pre>
<dl>
<dt>General Strategy:</p>
<dd>Move the dimensions you want to operate on to the start of your piddle&#8217;s dimension list. Then let <font SIZE="-1">PDL</font> thread over the higher dimensions.</dl>
<h2>Example: Conway&#8217;S Game Of Life</h2>
<p>Okay, enough theory. Let&#8217;s do something a bit more interesting: We&#8217;ll write <code>Conway&#8217;s Game of Life</code> in <font SIZE="-1">PDL</font> and see how powerful <font SIZE="-1">PDL</font> can be! </p>
<p> The <code>Game of Life</code> is a simulation run on a big two dimensional grid. Each cell in the grid can either be alive or dead (represented by 1 or 0). The next generation of cells in the grid is calculated with simple rules according to the number of living cells in it&#8217;s immediate neighbourhood: </p>
<p> 1) If an empty cell has exactly three neighbours, a living cell is generated. </p>
<p> 2) If a living cell has less than two neighbours, it dies of overfeeding. </p>
<p> 3) If a living cell has 4 or more neighbours, it dies from starvation. </p>
<p> Only the first generation of cells is determined by the programmer. After that, the simulation runs completely according to these rules. To calculate the next generation, you need to look at each cell in the 2D field (requiring two loops), calculate the number of live cells adjacent to this cell (requiring another two loops) and then fill the next generation grid.</p>
<h3>Classical implementation</h3>
<p>Here&#8217;s a classic way of writing this program in Perl. We only use <font SIZE="-1">PDL</font> for addressing individual cells. </p>
<pre> #!/usr/bin/perl -w
 use PDL;
 use PDL::NiceSlice;
 
 # Make a board for the game of life.
 my $nx = 20;
 my $ny = 20;
 
 # Current generation.
 my $a = zeroes($nx, $ny);
 
 # Next generation.
 my $n = zeroes($nx, $ny);
 
 # Put in a simple glider.
 $a(1:3,1:3) .= pdl ( [1,1,1],
 [0,0,1],
 [0,1,0] );
 
 for (my $i = 0; $i &lt; 100; $i++) {
 $n = zeroes($nx, $ny);
 $new_a = $a-&gt;copy;
 for ($x = 0; $x &lt; $nx; $x++) {
 for ($y = 0; $y &lt; $ny; $y++) {
 
 # For each cell, look at the surrounding neighbours.
 for ($dx = -1; $dx &lt;= 1; $dx++) {
 for ($dy = -1; $dy &lt;= 1; $dy++) {
 $px = $x + $dx;
 $py = $y + $dy;
 
 # Wrap around at the edges.
 if ($px &lt; 0) {$px = $nx-1};
 if ($py &lt; 0) {$py = $ny-1};
 if ($px &gt;= $nx) {$px = 0};
 if ($py &gt;= $ny) {$py = 0};
 
 $n($x,$y) .= $n($x,$y) + $a($px,$py);
 }
 }
 # Do not count the central cell itself.
 $n($x,$y) -= $a($x,$y);
 
 # Work out if cell lives or dies:
 # Dead cell lives if n = 3
 # Live cell dies if n is not 2 or 3
 if ($a($x,$y) == 1) { 
 if ($n($x,$y) &lt; 2) {$new_a($x,$y) .= 0};
 if ($n($x,$y) &gt; 3) {$new_a($x,$y) .= 0};
 } else { 
 if ($n($x,$y) == 3) {$new_a($x,$y) .= 1} 
 }
 }
 }
 
 print $a;
 
 $a = $new_a;
 }</pre>
<p>If you run this, you will see a small glider crawl diagonally across the grid of zeroes. On my machine, it prints out a couple of generations per second.</p>
<h3>Threaded <font SIZE="-1">PDL</font> implementation</h3>
<p>And here&#8217;s the threaded version in <font SIZE="-1">PDL.</font> Just four lines of <font SIZE="-1">PDL</font> code, and one of those is printing out the latest generation! </p>
<pre> #!/usr/bin/perl -w
 use PDL;
 use PDL::NiceSlice;
 
 my $a = zeroes(20,20);
 
 # Put in a simple glider.
 $a(1:3,1:3) .= pdl ( [1,1,1],
 [0,0,1],
 [0,1,0] );
 
 my $n;
 for (my $i = 0; $i &lt; 100; $i++) {
 # Calculate the number of neighbours per cell.
 $n = $a-&gt;range(ndcoords($a)-1,3,&quot;periodic&quot;)-&gt;reorder(2,3,0,1);
 $n = $n-&gt;sumover-&gt;sumover - $a;
 
 # Calculate the next generation.
 $a = ((($n == 2) + ($n == 3))* $a) + (($n==3) * !$a);
 
 print $a;
 }</pre>
<p>The threaded <font SIZE="-1">PDL</font> version is much faster: </p>
<pre> Classical =&gt; 32.79 seconds.
 Threaded =&gt; 0.41 seconds.</pre>
<h3>Explanation</h3>
<p>How does the threaded version work? </p>
<p> There are many <font SIZE="-1">PDL</font> functions designed to help you carry out <font SIZE="-1">PDL</font> threading. In this example, the key functions are: </p>
<p> <i>Method: </i>&quot;range&quot;<i></i> </p>
<p> At the simplest level, the <tt>&quot;range&quot;</tt> method is a different way to select a portion of a piddle. Instead of using the <tt>&quot;$a(2,3)&quot;</tt> notation, we use another piddle. </p>
<pre> pdl&gt; $a = sequence(6,7)
 pdl&gt; p $a
 [
 [ 0 1 2 3 4 5]
 [ 6 7 8 9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]
 [24 25 26 27 28 29]
 [30 31 32 33 34 35]
 [36 37 38 39 40 41]
 ]
 pdl&gt; p $a-&gt;range( pdl [1,2] )
 13
 pdl&gt; p $a(1,2)
 [
 [13]
 ]</pre>
<p>At this point, the <tt>&quot;range&quot;</tt> method looks very similar to a regular <font SIZE="-1">PDL</font> slice. But the <tt>&quot;range&quot;</tt> method is more general. For example, you can select several components at once: </p>
<pre> pdl&gt; $index = pdl [ [1,2],[2,3],[3,4],[4,5] ]
 pdl&gt; p $a-&gt;range( $index )
 [13 20 27 34]</pre>
<p>Additionally, <tt>&quot;range&quot;</tt> takes a second parameter which determines the size of the chunk to return: </p>
<pre> pdl&gt; $size = 3
 pdl&gt; p $a-&gt;range( pdl([1,2]) , $size )
 [
 [13 14 15]
 [19 20 21]
 [25 26 27]
 ]</pre>
<p>We can use this to select one or more 3&#215;3 boxes. </p>
<p> Finally, <tt>&quot;range&quot;</tt> can take a third parameter called the &#8220;boundary&#8221; condition. It tells <font SIZE="-1">PDL</font> what to do if the size box you request goes beyond the edge of the piddle. We won&#8217;t go over all the options. We&#8217;ll just say that the option <tt>&quot;periodic&quot;</tt> means that the piddle &#8220;wraps around&#8221;. For example: </p>
<pre> pdl&gt; p $a
 [
 [ 0 1 2 3 4 5]
 [ 6 7 8 9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]
 [24 25 26 27 28 29]
 [30 31 32 33 34 35]
 [36 37 38 39 40 41]
 ]
 pdl&gt; $size = 3
 pdl&gt; p $a-&gt;range( pdl([4,2]) , $size , &quot;periodic&quot; )
 [
 [16 17 12]
 [22 23 18]
 [28 29 24]
 ]
 pdl&gt; p $a-&gt;range( pdl([5,2]) , $size , &quot;periodic&quot; )
 [
 [17 12 13]
 [23 18 19]
 [29 24 25]
 ]</pre>
<p>Notice how the box wraps around the boundary of the piddle. </p>
<p> <i>Method: </i>&quot;ndcoords&quot;<i></i> </p>
<p> The <tt>&quot;ndcoords&quot;</tt> method is a convenience method that returns an enumerated list of coordinates suitable for use with the <tt>&quot;range&quot;</tt> method. </p>
<pre> pdl&gt; p $piddle = sequence(3,3)
 [
 [0 1 2]
 [3 4 5]
 [6 7 8]
 ]
 pdl&gt; p ndcoords($piddle)
 [
 [
 [0 0]
 [1 0]
 [2 0]
 ]
 [
 [0 1]
 [1 1]
 [2 1]
 ]
 [
 [0 2]
 [1 2]
 [2 2]
 ]
 ]</pre>
<p>This can be a little hard to read. Basically it&#8217;s saying that the coordinates for every element in <tt>$piddle</tt> is given by: </p>
<pre> (0,0) (1,0) (2,0)
 (1,0) (1,1) (2,1)
 (2,0) (2,1) (2,2)</pre>
<p><i>Combining </i>&quot;range&quot;<i> and </i>&quot;ndcoords&quot;<i></i> </p>
<p> What really matters is that <tt>&quot;ndcoords&quot;</tt> is designed to work together with <tt>&quot;range&quot;</tt>, with no <tt>$size</tt> parameter, you get the same piddle back. </p>
<pre> pdl&gt; p $piddle
 [
 [0 1 2]
 [3 4 5]
 [6 7 8]
 ]
 pdl&gt; p $piddle-&gt;range( ndcoords($piddle) )
 [
 [0 1 2]
 [3 4 5]
 [6 7 8]
 ]</pre>
<p>Why would this be useful? Because now we can ask for a series of &#8220;boxes&#8221; for the entire piddle. For example, 2&#215;2 boxes: </p>
<pre> pdl&gt; p $piddle-&gt;range( ndcoords($piddle) , 2 , &quot;periodic&quot; )</pre>
<p>The output of this function is difficult to read because the &#8220;boxes&#8221; along the last two dimension. We can make the result more readable by rearranging the dimensions: </p>
<pre> pdl&gt; p $piddle-&gt;range( ndcoords($piddle) , 2 , &quot;periodic&quot; )-&gt;reorder(2,3,0,1)
 [
 [
 [
 [0 1]
 [3 4]
 ]
 [
 [1 2]
 [4 5]
 ]
 ...
 ]</pre>
<p>Here you can see more clearly that </p>
<pre> [0 1]
 [3 4]</pre>
<p>Is the 2&#215;2 box starting with the (0,0) element of <tt>$piddle</tt>. </p>
<p> We are not done yet. For the game of life, we want 3&#215;3 boxes from <tt>$a</tt>: </p>
<pre> pdl&gt; p $a
 [
 [ 0 1 2 3 4 5]
 [ 6 7 8 9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]
 [24 25 26 27 28 29]
 [30 31 32 33 34 35]
 [36 37 38 39 40 41]
 ]
 pdl&gt; p $a-&gt;range( ndcoords($a) , 3 , &quot;periodic&quot; )-&gt;reorder(2,3,0,1)
 [
 [
 [
 [ 0 1 2]
 [ 6 7 8]
 [12 13 14]
 ]
 ...
 ]</pre>
<p>We can confirm that this is the 3&#215;3 box starting with the (0,0) element of <tt>$a</tt>. But there is one problem. We actually want the 3&#215;3 box to be <code>centered</code> on (0,0). That&#8217;s not a problem. Just subtract 1 from all the coordinates in <tt>&quot;ndcoords($a)&quot;</tt>. Remember that the &#8220;periodic&#8221; option takes care of making everything wrap around. </p>
<pre> pdl&gt; p $a-&gt;range( ndcoords($a) - 1 , 3 , &quot;periodic&quot; )-&gt;reorder(2,3,0,1)
 [
 [
 [
 [41 36 37]
 [ 5 0 1]
 [11 6 7]
 ]
 [
 [36 37 38]
 [ 0 1 2]
 [ 6 7 8]
 ]
 ...</pre>
<p>Now we see a 3&#215;3 box with the (0,0) element in the centre of the box. </p>
<p> <i>Method: </i>&quot;sumover&quot;<i></i> </p>
<p> The <tt>&quot;sumover&quot;</tt> method adds along only the first dimension. If we apply it twice, we will be adding all the elements of each 3&#215;3 box. </p>
<pre> pdl&gt; $n = $a-&gt;range(ndcoords($a)-1,3,&quot;periodic&quot;)-&gt;reorder(2,3,0,1)
 pdl&gt; p $n
 [
 [
 [
 [41 36 37]
 [ 5 0 1]
 [11 6 7]
 ]
 [
 [36 37 38]
 [ 0 1 2]
 [ 6 7 8]
 ]
 ...
 pdl&gt; p $n-&gt;sumover-&gt;sumover
 [
 [144 135 144 153 162 153]
 [ 72 63 72 81 90 81]
 [126 117 126 135 144 135]
 [180 171 180 189 198 189]
 [234 225 234 243 252 243]
 [288 279 288 297 306 297]
 [216 207 216 225 234 225]
 ]</pre>
<p>Use a calculator to confirm that 144 is the sum of all the elements in the first 3&#215;3 box and 135 is the sum of all the elements in the second 3&#215;3 box. </p>
<p> <i>Counting neighbours</i> </p>
<p> We are almost there! </p>
<p> Adding up all the elements in a 3&#215;3 box is not <code>quite</code> what we want. We don&#8217;t want to count the center box. Fortunately, this is an easy fix: </p>
<pre> pdl&gt; p $n-&gt;sumover-&gt;sumover - $a
 [
 [144 134 142 150 158 148]
 [ 66 56 64 72 80 70]
 [114 104 112 120 128 118]
 [162 152 160 168 176 166]
 [210 200 208 216 224 214]
 [258 248 256 264 272 262]
 [180 170 178 186 194 184]
 ]</pre>
<p>When applied to Conway&#8217;s Game of Life, this will tell us how many living neighbours each cell has: </p>
<pre> pdl&gt; $a = zeroes(10,10)
 pdl&gt; $a(1:3,1:3) .= pdl ( [1,1,1],
 ..( &gt; [0,0,1],
 ..( &gt; [0,1,0] )
 pdl&gt; p $a
 [
 [0 0 0 0 0 0 0 0 0 0]
 [0 1 1 1 0 0 0 0 0 0]
 [0 0 0 1 0 0 0 0 0 0]
 [0 0 1 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 ]
 pdl&gt; $n = $a-&gt;range(ndcoords($a)-1,3,&quot;periodic&quot;)-&gt;reorder(2,3,0,1)
 pdl&gt; $n = $n-&gt;sumover-&gt;sumover - $a
 pdl&gt; p $n
 [
 [1 2 3 2 1 0 0 0 0 0]
 [1 1 3 2 2 0 0 0 0 0]
 [1 3 5 3 2 0 0 0 0 0]
 [0 1 1 2 1 0 0 0 0 0]
 [0 1 1 1 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 ]</pre>
<p>For example, this tells us that cell (0,0) has 1 living neighbour, while cell (2,2) has 5 living neighbours. </p>
<p> <i>Calculating the next generation</i> </p>
<p> At this point, the variable <tt>$n</tt> has the number of living neighbours for every cell. Now we apply the rules of the game of life to calculate the next generation.</p>
<dl>
<dt>If an empty cell has exactly three neighbours, a living cell is generated.</p>
<dd>Get a list of cells that have exactly three neighbours: </p>
<pre> pdl&gt; p ($n == 3)
 [
 [0 0 1 0 0 0 0 0 0 0]
 [0 0 1 0 0 0 0 0 0 0]
 [0 1 0 1 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 ]</pre>
<p>Get a list of <code>empty</code> cells that have exactly three neighbours: </p>
<pre> pdl&gt; p ($n == 3) * !$a</pre>
<dt>If a living cell has less than 2 or more than 3 neighbours, it dies.</p>
<dd>Get a list of cells that have exactly 2 or 3 neighbours: </p>
<pre> pdl&gt; p (($n == 2) + ($n == 3))
 [
 [0 1 1 1 0 0 0 0 0 0]
 [0 0 1 1 1 0 0 0 0 0]
 [0 1 0 1 1 0 0 0 0 0]
 [0 0 0 1 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 ]</pre>
<p>Get a list of <code>living</code> cells that have exactly 2 or 3 neighbours: </p>
<pre> pdl&gt; p (($n == 2) + ($n == 3)) * $a</pre>
</dl>
<p> Putting it all together, the next generation is: </p>
<pre> pdl&gt; $a = ((($n == 2) + ($n == 3)) * $a) + (($n == 3) * !$a)
 pdl&gt; p $a
 [
 [0 0 1 0 0 0 0 0 0 0]
 [0 0 1 1 0 0 0 0 0 0]
 [0 1 0 1 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 ]</pre>
<h3>Bonus feature: Graphics!</h3>
<p>If you have PDL::Graphics::TriD installed, you can make a graphical version of the program by just changing three lines: </p>
<pre> #!/usr/bin/perl
 use PDL;
 use PDL::NiceSlice;
 use PDL::Graphics::TriD;
 
 my $a = zeroes(20,20);
 
 # Put in a simple glider.
 $a(1:3,1:3) .= pdl ( [1,1,1],
 [0,0,1],
 [0,1,0] );
 
 my $n;
 for (my $i = 0; $i &lt; 100; $i++) {
 # Calculate the number of neighbours per cell.
 $n = $a-&gt;range(ndcoords($a)-1,3,&quot;periodic&quot;)-&gt;reorder(2,3,0,1);
 $n = $n-&gt;sumover-&gt;sumover - $a;
 
 # Calculate the next generation.
 $a = ((($n == 2) + ($n == 3))* $a) + (($n==3) * !$a);
 
 # Display.
 nokeeptwiddling3d();
 imagrgb [$a];
 }</pre>
<p>But if we really want to see something interesting, we should make a few more changes: </p>
<p> 1) Start with a random collection of 1&#8217;s and 0&#8217;s. </p>
<p> 2) Make the grid larger. </p>
<p> 3) Add a small timeout so we can see the game evolve better. </p>
<p> 4) Use a while loop so that the program can run as long as it needs to. </p>
<pre> #!/usr/bin/perl
 use PDL;
 use PDL::NiceSlice;
 use PDL::Graphics::TriD;
 use Time::HiRes qw(usleep);
 
 my $a = random(100,100);
 $a = ($a &lt; 0.5);
 
 my $n;
 while (1) {
 # Calculate the number of neighbours per cell.
 $n = $a-&gt;range(ndcoords($a)-1,3,&quot;periodic&quot;)-&gt;reorder(2,3,0,1);
 $n = $n-&gt;sumover-&gt;sumover - $a;
 
 # Calculate the next generation.
 $a = ((($n == 2) + ($n == 3))* $a) + (($n==3) * !$a);
 
 # Display.
 nokeeptwiddling3d();
 imagrgb [$a];
 
 # Sleep for 0.1 seconds.
 usleep(100000);
 }</pre>
<h2>Conclusion: General Strategy</h2>
<p>The general strategy is: <i>Move the dimensions you want to operate on to the start of your piddle&#8217;s dimension list. Then let </i><font SIZE="-1"><i>PDL</i></font><i> thread over the higher dimensions.</i> </p>
<p> Threading is a powerful tool that helps eliminate for-loops and can make your code more concise. Hopefully this tutorial has shown why it is worth getting to grips with threading in <font SIZE="-1">PDL.</font></p>
<h2>Copyright</h2>
<p>Copyright 2010 Matthew Kenworthy (kenworthy [at] strw.leidenuniv.nl) and Daniel Carrera (dcarrera [at] gmail.com). You can distribute and/or modify this document under the same terms as the current Perl license. </p>
<p> See: <a rel="nofollow" href="http://dev.perl.org/licenses/">http://dev.perl.org/licenses/</a></p>
