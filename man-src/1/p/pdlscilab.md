---
title: "pdlscilab(1)"
name: "pdlscilab"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdlscilab/"
description: "PDL::Scilab – A guide for Scilab users."
---

<p>PDL::Scilab &#8211; A guide for Scilab users. </p>
<h2>Introduction</h2>
<p>If you are a Scilab user, this page is for you. It explains the key differences between Scilab and <font SIZE="-1">PDL</font> to help you get going as quickly as possible. </p>
<p> <code>This document is not a tutorial</code>. For that, go to PDL::QuickStart. This document <code>complements</code> the Quick Start guide, as it highlights the key differences between Scilab and <font SIZE="-1">PDL.</font></p>
<h2>Perl</h2>
<p>The key difference between Scilab and <font SIZE="-1">PDL</font> is <code>Perl</code>. </p>
<p> Perl is a general purpose programming language with thousands of modules freely available on the web. <font SIZE="-1">PDL</font> is an extension of Perl. This gives <font SIZE="-1">PDL</font> programs access to more features than most numerical tools can dream of. At the same time, most syntax differences between Scilab and <font SIZE="-1">PDL</font> are a result of its Perl foundation. </p>
<p> <code>You do not have to learn much Perl to be effective with </code><font SIZE="-1"><code>PDL</code></font>. But if you wish to learn Perl, there is excellent documentation available on-line (&lt;<a rel="nofollow" href="http://perldoc.perl.org">http://perldoc.perl.org</a>&gt;) or through the command <tt>&quot;perldoc perl&quot;</tt>. There is also a beginner&#8217;s portal (&lt;<a rel="nofollow" href="http://perl-begin.org">http://perl-begin.org</a>&gt;). </p>
<p> Perl&#8217;s module repository is called <font SIZE="-1">CPAN </font>(&lt;<a rel="nofollow" href="http://www.cpan.org">http://www.cpan.org</a>&gt;) and it has a vast array of modules. Run <tt>&quot;perldoc cpan&quot;</tt> for more information.</p>
<h2>Terminology: Piddle</h2>
<p>Scilab typically refers to vectors, matrices, and arrays. Perl already has arrays, and the terms &#8220;vector&#8221; and &#8220;matrix&#8221; typically refer to one- and two-dimensional collections of data. Having no good term to describe their object, <font SIZE="-1">PDL</font> developers coined the term &quot;<i>piddle</i>&quot; to give a name to their data type. </p>
<p> A <i>piddle</i> consists of a series of numbers organized as an N-dimensional data set. Piddles provide efficient storage and fast computation of large N-dimensional matrices. They are highly optimized for numerical work. </p>
<p> For more information, see &quot;<code>Piddles vs Perl Arrays</code>&quot; later in this document.</p>
<h2>Command Window And Ide</h2>
<p><font SIZE="-1">PDL</font> does not come with a dedicated <font SIZE="-1">IDE.</font> It does however come with an interactive shell and you can use a Perl <font SIZE="-1">IDE</font> to develop <font SIZE="-1">PDL</font> programs.</p>
<h3><font SIZE="-1">PDL</font> interactive shell</h3>
<p>To start the interactive shell, open a terminal and run <tt>&quot;perldl&quot;</tt> or <tt>&quot;pdl2&quot;</tt>. As in Scilab, the interactive shell is the best way to learn the language. To exit the shell, type <tt>&quot;exit&quot;</tt>, just like Scilab.</p>
<h3>Writing <font SIZE="-1">PDL</font> programs</h3>
<p>One popular <font SIZE="-1">IDE</font> for Perl is called Padre (&lt;<a rel="nofollow" href="http://padre.perlide.org">http://padre.perlide.org</a>&gt;). It is cross platform and easy to use. </p>
<p> Whenever you write a stand-alone <font SIZE="-1">PDL</font> program (i.e. outside the <tt>&quot;perldl&quot;</tt> or <tt>&quot;pdl2&quot;</tt> shells) you must start the program with <tt>&quot;use PDL;&quot;</tt>. This command imports the <font SIZE="-1">PDL</font> module into Perl. Here is a sample <font SIZE="-1">PDL</font> program: </p>
<pre> use PDL; # Import main PDL module.
 use PDL::NiceSlice; # Import additional PDL module.
 
 $b = pdl [2,3,4]; # Statements end in semicolon.
 $A = pdl [ [1,2,3],[4,5,6] ]; # 2-dimensional piddle.
 
 print $A x $b-&gt;transpose;</pre>
<p>Save this file as <tt>&quot;myprogram.pl&quot;</tt> and run it with: </p>
<pre> perl myprogram.pl</pre>
<h3>New: Flexible syntax</h3>
<p>In very recent versions of <font SIZE="-1">PDL </font>(version 2.4.7 or later) there is a flexible matrix syntax that can look extremely similar to Scilab: </p>
<p> 1) Use a &#8216;;&#8217; to delimit rows: </p>
<pre> $b = pdl q[ 2,3,4 ];
 $A = pdl q[ 1,2,3 ; 4,5,6 ];</pre>
<p>2) Use spaces to separate elements: </p>
<pre> $b = pdl q[ 2 3 4 ];
 $A = pdl q[ 1 2 3 ; 4 5 6 ];</pre>
<p>Basically, as long as you put a <tt>&quot;q&quot;</tt> in front of the opening bracket, <font SIZE="-1">PDL</font> should &#8220;do what you mean&#8221;. So you can write in a syntax that is more comfortable for you.</p>
<h2>A Module For Scilab Users</h2>
<p>Here is a module that Scilab users will want to use:</p>
<dl>
<dt>PDL::NiceSlice</p>
<dd>Gives <font SIZE="-1">PDL</font> a syntax for slices (sub-matrices) that is shorter and more familiar to Scilab users. </p>
<pre> // Scilab
 b(1:5) --&gt; Selects the first 5 elements from b.
 
 # PDL without NiceSlice
 $b-&gt;slice(&quot;0:4&quot;) --&gt; Selects the first 5 elements from $b.
 
 # PDL with NiceSlice
 $b(0:4) --&gt; Selects the first 5 elements from $b.</pre>
</dl>
<h2>Basic Features</h2>
<p>This section explains how <font SIZE="-1">PDL</font>&#8216;s syntax differs from Scilab. Most Scilab users will want to start here.</p>
<h3>General gotchas</h3>
<dl>
<dt>Indices</p>
<dd>In <font SIZE="-1">PDL,</font> indices start at &#8216;0&#8217; (like C and Java), not 1 (like Scilab). For example, if <tt>$b</tt> is an array with 5 elements, the elements would be numbered from 0 to 4.</p>
<dt>Displaying an object</p>
<dd>Scilab normally displays object contents automatically. In <font SIZE="-1">PDL</font> you display objects explicitly with the <tt>&quot;print&quot;</tt> command or the shortcut <tt>&quot;p&quot;</tt>: </p>
<p> Scilab: </p>
<pre> --&gt; a = 12
 a = 12.
 --&gt; b = 23; // Suppress output.
 --&gt;</pre>
<p>PerlDL: </p>
<pre> pdl&gt; $a = 12 # No output.
 pdl&gt; print $a # Print object.
 12
 pdl&gt; p $a # &quot;p&quot; is a shorthand for &quot;print&quot; in the shell.
 12</pre>
</dl>
<h3>Creating Piddles</h3>
<dl>
<dt>Variables in <font SIZE="-1">PDL</font></p>
<dd>Variables always start with the &#8216;$&#8217; sign. </p>
<pre> Scilab: value = 42
 PerlDL: $value = 42</pre>
<dt>Basic syntax</p>
<dd>Use the &#8220;pdl&#8221; constructor to create a new <i>piddle</i>. </p>
<pre> Scilab: v = [1,2,3,4]
 PerlDL: $v = pdl [1,2,3,4]
 Scilab: A = [ 1,2,3 ; 3,4,5 ]
 PerlDL: $A = pdl [ [1,2,3] , [3,4,5] ]</pre>
<dt>Simple matrices</p>
<dd>
<pre> Scilab PDL
 ------ ------
 Matrix of ones ones(5,5) ones 5,5
 Matrix of zeros zeros(5,5) zeros 5,5
 Random matrix rand(5,5) random 5,5
 Linear vector 1:5 sequence 5</pre>
<p>Notice that in <font SIZE="-1">PDL</font> the parenthesis in a function call are often optional. It is important to keep an eye out for possible ambiguities. For example: </p>
<pre> pdl&gt; p zeros 2, 2 + 2</pre>
<p>Should this be interpreted as <tt>&quot;zeros(2,2) + 2&quot;</tt> or as <tt>&quot;zeros 2, (2+2)&quot;</tt>? Both are valid statements: </p>
<pre> pdl&gt; p zeros(2,2) + 2
 [
 [2 2]
 [2 2]
 ]
 pdl&gt; p zeros 2, (2+2)
 [
 [0 0]
 [0 0]
 [0 0]
 [0 0]
 ]</pre>
<p>Rather than trying to memorize Perl&#8217;s order of precedence, it is best to use parentheses to make your code unambiguous.</p>
<dt>Linearly spaced sequences</p>
<dd>
<pre> Scilab: --&gt; linspace(2,10,5)
 ans = 2. 4. 6. 8. 10.
 
 PerlDL: pdl&gt; p <a href="//www.systutorials.com/docs/linux/man/5-zeroes/">zeroes</a>(5)-&gt;xlinvals(2,10)
 [2 4 6 8 10]</pre>
<p><code>Explanation</code>: Start with a 1-dimensional piddle of 5 elements and give it equally spaced values from 2 to 10. </p>
<p> Scilab has a single function call for this. On the other hand, <font SIZE="-1">PDL</font>&#8216;s method is more flexible: </p>
<pre> pdl&gt; p zeros(5,5)-&gt;xlinvals(2,10)
 [
 [ 2 4 6 8 10]
 [ 2 4 6 8 10]
 [ 2 4 6 8 10]
 [ 2 4 6 8 10]
 [ 2 4 6 8 10]
 ]
 pdl&gt; p zeros(5,5)-&gt;ylinvals(2,10)
 [
 [ 2 2 2 2 2]
 [ 4 4 4 4 4]
 [ 6 6 6 6 6]
 [ 8 8 8 8 8]
 [10 10 10 10 10]
 ]
 pdl&gt; p zeros(3,3,3)-&gt;zlinvals(2,6)
 [
 [
 [2 2 2]
 [2 2 2]
 [2 2 2]
 ]
 [
 [4 4 4]
 [4 4 4]
 [4 4 4]
 ]
 [
 [6 6 6]
 [6 6 6]
 [6 6 6]
 ]
 ]</pre>
<dt>Slicing and indices</p>
<dd>Extracting a subset from a collection of data is known as <i>slicing</i>. The <font SIZE="-1">PDL</font> shell and Scilab have a similar syntax for slicing, but there are two important differences: </p>
<p> 1) <font SIZE="-1">PDL</font> indices start at 0, as in C and Java. Scilab starts indices at 1. </p>
<p> 2) In Scilab you think &#8220;rows and columns&#8221;. In <font SIZE="-1">PDL,</font> think &#8220;x and y&#8221;. </p>
<pre> Scilab PerlDL
 ------ ------
 --&gt; A pdl&gt; p $A
 A = [
 1. 2. 3. [1 2 3]
 4. 5. 6. [4 5 6]
 7. 8. 9. [7 8 9]
 ]
 -------------------------------------------------------
 (row = 2, col = 1) (x = 0, y = 1)
 --&gt; A(2,1) pdl&gt; p $A(0,1)
 ans = [
 4. [4]
 ]
 -------------------------------------------------------
 (row = 2 to 3, col = 1 to 2) (x = 0 to 1, y = 1 to 2)
 --&gt; A(2:3,1:2) pdl&gt; p $A(0:1,1:2)
 ans = [
 4. 5. [4 5]
 7. 8. [7 8]
 ]</pre>
<dl>
<dd>
<dl>
<dt><code>Warning</code></p>
<dd>When you write a stand-alone <font SIZE="-1">PDL</font> program you have to include the PDL::NiceSlice module. See the previous section &quot;<font SIZE="-1"><code>MODULES FOR SCILAB USERS</code></font>&quot; for more information. </p>
<pre> use PDL; # Import main PDL module.
 use PDL::NiceSlice; # Nice syntax for slicing.
 
 $A = random 4,4;
 print $A(0,1);</pre>
</dl>
</dl>
<dl>
<dd></dl>
</dl>
<h3>Matrix Operations</h3>
<dl>
<dt>Matrix multiplication</p>
<dd>
<pre> Scilab: A * B
 PerlDL: $A x $B</pre>
<dt>Element-wise multiplication</p>
<dd>
<pre> Scilab: A .* B
 PerlDL: $A * $B</pre>
<dt>Transpose</p>
<dd>
<pre> Scilab: A'
 PerlDL: $A-&gt;transpose</pre>
</dl>
<h3>Functions that aggregate data</h3>
<p>Some functions (like <tt>&quot;sum&quot;</tt>, <tt>&quot;max&quot;</tt> and <tt>&quot;min&quot;</tt>) aggregate data for an N-dimensional data set. Scilab and <font SIZE="-1">PDL</font> both give you the option to apply these functions to the entire data set or to just one dimension.</p>
<dl>
<dt>Scilab</p>
<dd>In Scilab, these functions work along the entire data set by default, and an optional parameter &#8220;r&#8221; or &#8220;c&#8221; makes them act over rows or columns. </p>
<pre> --&gt; A = [ 1,5,4 ; 4,2,1 ]
 A = 1. 5. 4.
 4. 2. 1.
 --&gt; max(A)
 ans = 5
 --&gt; max(A, &quot;r&quot;)
 ans = 4. 5. 4.
 --&gt; max(A, &quot;c&quot;)
 ans = 5.
 4.</pre>
<dt><font SIZE="-1">PDL</font></p>
<dd><font SIZE="-1">PDL</font> offers two functions for each feature. </p>
<pre> sum vs sumover
 avg vs average
 max vs maximum
 min vs minimum</pre>
<p>The <code>long name</code> works over a dimension, while the <code>short name</code> works over the entire piddle. </p>
<pre> pdl&gt; p $A = pdl [ [1,5,4] , [4,2,1] ]
 [
 [1 5 4]
 [4 2 1]
 ]
 pdl&gt; p $A-&gt;maximum
 [5 4]
 pdl&gt; p $A-&gt;transpose-&gt;maximum
 [4 5 4]
 pdl&gt; p $A-&gt;max
 5</pre>
</dl>
<h3>Higher dimensional data sets</h3>
<p>A related issue is how Scilab and <font SIZE="-1">PDL</font> understand data sets of higher dimension. Scilab was designed for 1D vectors and 2D matrices with higher dimensional objects added on top. In contrast, <font SIZE="-1">PDL</font> was designed for N-dimensional piddles from the start. This leads to a few surprises in Scilab that don&#8217;t occur in <font SIZE="-1">PDL:</font></p>
<dl>
<dt>Scilab sees a vector as a 2D matrix.</p>
<dd>
<pre> Scilab PerlDL
 ------ ------
 --&gt; vector = [1,2,3,4]; pdl&gt; $vector = pdl [1,2,3,4]
 --&gt; size(vector) pdl&gt; p $vector-&gt;dims
 ans = 1 4 4</pre>
<p>Scilab sees <tt>&quot;[1,2,3,4]&quot;</tt> as a 2D matrix (1&#215;4 matrix). <font SIZE="-1">PDL</font> sees it as a 1D vector: A single dimension of size 4.</p>
<dt>But Scilab ignores the last dimension of a 4x1x1 matrix.</p>
<dd>
<pre> Scilab PerlDL
 ------ ------
 --&gt; A = ones(4,1,1); pdl&gt; $A = ones 4,1,1
 --&gt; size(A) pdl&gt; p $A-&gt;dims
 ans = 4 1 4 1 1</pre>
<dt>And Scilab treats a 4x1x1 matrix differently from a 1x1x4 matrix.</p>
<dd>
<pre> Scilab PerlDL
 ------ ------
 --&gt; A = ones(1,1,4); pdl&gt; $A = ones 1,1,4
 --&gt; size(A) pdl&gt; p $A-&gt;dims
 ans = 1 1 4 1 1 4</pre>
<dt>Scilab has no direct syntax for N-D arrays.</p>
<dd>
<pre> pdl&gt; $A = pdl [ [[1,2,3],[4,5,6]], [[2,3,4],[5,6,7]] ]
 pdl&gt; p $A-&gt;dims
 3 2 2</pre>
<dt>Feature support.</p>
<dd>In Scilab, several features are not available for N-D arrays. In <font SIZE="-1">PDL,</font> just about any feature supported by 1D and 2D piddles, is equally supported by N-dimensional piddles. There is usually no distinction: </p>
<pre> Scilab PerlDL
 ------ ------
 --&gt; A = ones(3,3,3); pdl&gt; $A = ones(3,3,3);
 --&gt; A' pdl&gt; transpose $A
 =&gt; ERROR =&gt; OK</pre>
</dl>
<h3>Loop Structures</h3>
<p>Perl has many loop structures, but we will only show the one that is most familiar to Scilab users: </p>
<pre> Scilab PerlDL
 ------ ------
 for i = 1:10 for $i (1..10) {
 disp(i) print $i
 end }</pre>
<dl>
<dt><code>Note</code></p>
<dd>Never use for-loops for numerical work. Perl&#8217;s for-loops are faster than Scilab&#8217;s, but they both pale against a &#8220;vectorized&#8221; operation. <font SIZE="-1">PDL</font> has many tools that facilitate writing vectorized programs. These are beyond the scope of this guide. To learn more, see: PDL::Indexing, PDL::Threading, and <font SIZE="-1">PDL::PP</font>. </p>
<p> Likewise, never use <tt>1..10</tt> for numerical work, even outside a for-loop. <tt>1..10</tt> is a Perl array. Perl arrays are designed for flexibility, not speed. Use <i>piddles</i> instead. To learn more, see the next section.</dl>
<h3>Piddles vs Perl Arrays</h3>
<p>It is important to note the difference between a <i>Piddle</i> and a Perl array. Perl has a general-purpose array object that can hold any type of element: </p>
<pre> @perl_array = 1..10;
 @perl_array = ( 12, &quot;Hello&quot; );
 @perl_array = ( 1, 2, 3, \@another_perl_array, <a href="//www.systutorials.com/docs/linux/man/5-sequence/">sequence</a>(5) );</pre>
<p>Perl arrays allow you to create powerful data structures (see <code>Data structures</code> below), <code>but they are not designed for numerical work</code>. For that, use <i>piddles</i>: </p>
<pre> $pdl = pdl [ 1, 2, 3, 4 ];
 $pdl = sequence 10_000_000; 
 $pdl = ones 600, 600;</pre>
<p>For example: </p>
<pre> $points = pdl 1..10_000_000 # 4.7 seconds
 $points = sequence 10_000_000 # milliseconds</pre>
<p><font SIZE="-1"><code>TIP</code></font>: You can use underscores in numbers (<tt>&quot;10_000_000&quot;</tt> reads better than <tt>10000000</tt>).</p>
<h3>Conditionals</h3>
<p>Perl has many conditionals, but we will only show the one that is most familiar to Scilab users: </p>
<pre> Scilab PerlDL
 ------ ------
 if value &gt; MAX if ($value &gt; $MAX) {
 disp(&quot;Too large&quot;) print &quot;Too large
&quot;;
 elseif value &lt; MIN } elsif ($value &lt; $MIN) {
 disp(&quot;Too small&quot;) print &quot;Too small
&quot;;
 else } else {
 disp(&quot;Perfect!&quot;) print &quot;Perfect!
&quot;;
 end }</pre>
<dl>
<dt><code>Note</code></p>
<dd>Here is a &#8220;gotcha&#8221;: </p>
<pre> Scilab: elseif
 PerlDL: elsif</pre>
<p>If your conditional gives a syntax error, check that you wrote your <tt>&quot;elsif&quot;</tt>&#8216;s correctly.</dl>
<h3><font SIZE="-1">TIMTOWDI </font>(There Is More Than One Way To Do It)</h3>
<p>One of the most interesting differences between <font SIZE="-1">PDL</font> and other tools is the expressiveness of the Perl language. <font SIZE="-1">TIMTOWDI,</font> or &#8220;There Is More Than One Way To Do It&#8221;, is Perl&#8217;s motto. </p>
<p> Perl was written by a linguist, and one of its defining properties is that statements can be formulated in different ways to give the language a more natural feel. For example, you are unlikely to say to a friend: </p>
<pre> &quot;While I am not finished, I will keep working.&quot;</pre>
<p>Human language is more flexible than that. Instead, you are more likely to say: </p>
<pre> &quot;I will keep working until I am finished.&quot;</pre>
<p>Owing to its linguistic roots, Perl is the only programming language with this sort of flexibility. For example, Perl has traditional while-loops and if-statements: </p>
<pre> while ( ! finished() ) {
 keep_working();
 }
 
 if ( ! wife_angry() ) {
 kiss_wife();
 }</pre>
<p>But it also offers the alternative <code>until</code> and <code>unless</code> statements: </p>
<pre> until ( finished() ) {
 keep_working();
 }
 
 unless ( wife_angry() ) {
 kiss_wife();
 }</pre>
<p>And Perl allows you to write loops and conditionals in &#8220;postfix&#8221; form: </p>
<pre> keep_working() until finished();
 
 kiss_wife() unless wife_angry();</pre>
<p>In this way, Perl often allows you to write more natural, easy to understand code than is possible in more restrictive programming languages.</p>
<h3>Functions</h3>
<p><font SIZE="-1">PDL</font>&#8216;s syntax for declaring functions differs significantly from Scilab&#8217;s. </p>
<pre> Scilab PerlDL
 ------ ------
 function retval = foo(x,y) sub foo {
 retval = x.**2 + x.*y my ($x, $y) = @_;
 endfunction return $x**2 + $x*$y;
 }</pre>
<p>Don&#8217;t be intimidated by all the new syntax. Here is a quick run through a function declaration in <font SIZE="-1">PDL:</font> </p>
<p> 1) &quot;<code>sub</code>&#8220; stands for &#8221;subroutine&quot;. </p>
<p> 2) &quot;<code>my</code>&quot; declares variables to be local to the function. </p>
<p> 3) &quot;@_&quot; is a special Perl array that holds all the function parameters. This might seem like a strange way to do functions, but it allows you to make functions that take a variable number of parameters. For example, the following function takes any number of parameters and adds them together: </p>
<pre> sub mysum {
 my ($i, $total) = (0, 0);
 for $i (@_) {
 $total += $i;
 }
 return $total;
 }</pre>
<p>4) You can assign values to several variables at once using the syntax: </p>
<pre> ($a, $b, $c) = (1, 2, 3);</pre>
<p>So, in the previous examples: </p>
<pre> # This declares two local variables and initializes them to 0.
 my ($i, $total) = (0, 0);
 
 # This takes the first two elements of @_ and puts them in $x and $y.
 my ($x, $y) = @_;</pre>
<p>5) The &quot;<code>return</code>&quot; statement gives the return value of the function, if any.</p>
<h2>Additional Features</h2>
<h3>Data structures</h3>
<p>To create complex data structures, Scilab uses &quot;<i>lists</i>&#8220; and &#8221;<i>structs</i>&quot;. Perl&#8217;s arrays and hashes offer similar functionality. This section is only a quick overview of what Perl has to offer. To learn more about this, please go to &lt;<a rel="nofollow" href="http://perldoc.perl.org/perldata.html">http://perldoc.perl.org/perldata.html</a>&gt; or run the command <tt>&quot;perldoc perldata&quot;</tt>.</p>
<dl>
<dt>Arrays</p>
<dd>Perl arrays are similar to Scilab&#8217;s lists. They are both a sequential data structure that can contain any data type. </p>
<pre> Scilab
 ------
 list( 1, 12, &quot;hello&quot;, zeros(3,3) , list( 1, 2) );
 
 PerlDL
 ------
 @array = ( 1, 12, &quot;hello&quot; , zeros(3,3), [ 1, 2 ] )</pre>
<p>Notice that Perl array&#8217;s start with the &#8220;@&#8221; prefix instead of the &#8220;$&#8221; used by piddles. </p>
<p> <i>To learn about Perl arrays, please go to &lt;<a rel="nofollow" href="http://perldoc.perl.org/perldata.html">http://perldoc.perl.org/perldata.html</a>&gt; or run the command </i>&quot;perldoc perldata&quot;<i>.</i></p>
<dt>Hashes</p>
<dd>Perl hashes are similar to Scilab&#8217;s structure arrays: </p>
<pre> Scilab
 ------
 --&gt; drink = struct('type', 'coke', 'size', 'large', 'myarray', ones(3,3,3))
 --&gt; drink.type = 'sprite'
 --&gt; drink.price = 12 // Add new field to structure array.
 
 PerlDL
 ------
 pdl&gt; %drink = ( type =&gt; 'coke' , size =&gt; 'large', mypiddle =&gt; ones(3,3,3) )
 pdl&gt; $drink{type} = 'sprite'
 pdl&gt; $drink{price} = 12 # Add new field to hash.</pre>
<p>Notice that Perl hashes start with the &#8220;%&#8221; prefix instead of the &#8220;@&#8221; for arrays and &#8220;$&#8221; used by piddles. </p>
<p> <i>To learn about Perl hashes, please go to &lt;<a rel="nofollow" href="http://perldoc.perl.org/perldata.html">http://perldoc.perl.org/perldata.html</a>&gt; or run the command </i>&quot;perldoc perldata&quot;<i>.</i></dl>
<h3>Performance</h3>
<p><font SIZE="-1">PDL</font> has powerful performance features, some of which are not normally available in numerical computation tools. The following pages will guide you through these features:</p>
<dl>
<dt>PDL::Indexing</p>
<dd><code>Level</code>: Beginner </p>
<p> This beginner tutorial covers the standard &#8220;vectorization&#8221; feature that you already know from Scilab. Use this page to learn how to avoid for-loops to make your program more efficient.</p>
<dt>PDL::Threading</p>
<dd><code>Level</code>: Intermediate </p>
<p> <font SIZE="-1">PDL</font>&#8216;s &#8220;vectorization&#8221; feature goes beyond what most numerical software can do. In this tutorial you&#8217;ll learn how to &#8220;thread&#8221; over higher dimensions, allowing you to vectorize your program further than is possible in Scilab.</p>
<dt>Benchmarks</p>
<dd><code>Level</code>: Intermediate </p>
<p> Perl comes with an easy to use benchmarks module to help you find how long it takes to execute different parts of your code. It is a great tool to help you focus your optimization efforts. You can read about it online (&lt;<a rel="nofollow" href="http://perldoc.perl.org/Benchmark.html">http://perldoc.perl.org/Benchmark.html</a>&gt;) or through the command <tt>&quot;perldoc Benchmark&quot;</tt>.</p>
<dt><font SIZE="-1">PDL::PP</font></p>
<dd><code>Level</code>: Advanced </p>
<p> <font SIZE="-1">PDL</font>&#8216;s Pre-Processor is one of <font SIZE="-1">PDL</font>&#8216;s most powerful features. You write a function definition in special markup and the pre-processor generates real C code which can be compiled. With <font SIZE="-1">PDL:PP</font> you get the full speed of native C code without having to deal with the full complexity of the C language.</dl>
<h3>Plotting</h3>
<p><font SIZE="-1">PDL</font> has full-featured plotting abilities. Unlike Scilab, <font SIZE="-1">PDL</font> relies more on third-party libraries (pgplot and PLplot) for its 2D plotting features. Its 3D plotting and graphics uses OpenGL for performance and portability. <font SIZE="-1">PDL</font> has three main plotting modules:</p>
<dl>
<dt>PDL::Graphics::PGPLOT</p>
<dd><code>Best for</code>: Plotting 2D functions and data sets. </p>
<p> This is an interface to the venerable <font SIZE="-1">PGPLOT</font> library. <font SIZE="-1">PGPLOT</font> has been widely used in the academic and scientific communities for many years. In part because of its age, <font SIZE="-1">PGPLOT</font> has some limitations compared to newer packages such as PLplot (e.g. no <font SIZE="-1">RGB</font> graphics). But it has many features that still make it popular in the scientific community.</p>
<dt>PDL::Graphics::PLplot</p>
<dd><code>Best for</code>: Plotting 2D functions as well as 2D and 3D data sets. </p>
<p> This is an interface to the PLplot plotting library. PLplot is a modern, open source library for making scientific plots. It supports plots of both 2D and 3D data sets. PLplot is best supported for unix/linux/macosx platforms. It has an active developers community and support for win32 platforms is improving.</p>
<dt>PDL::Graphics::TriD</p>
<dd><code>Best for</code>: Plotting 3D functions. </p>
<p> The native <font SIZE="-1">PDL 3D</font> graphics library using OpenGL as a backend for 3D plots and data visualization. With OpenGL, it is easy to manipulate the resulting 3D objects with the mouse in real time.</dl>
<h3>Writing GUIs</h3>
<p>Through Perl, <font SIZE="-1">PDL</font> has access to all the major toolkits for creating a cross platform graphical user interface. One popular option is wxPerl (&lt;<a rel="nofollow" href="http://wxperl.sourceforge.net">http://wxperl.sourceforge.net</a>&gt;). These are the Perl bindings for wxWidgets, a powerful <font SIZE="-1">GUI</font> toolkit for writing cross-platform applications. </p>
<p> wxWidgets is designed to make your application look and feel like a native application in every platform. For example, the Perl <font SIZE="-1">IDE </font><code>Padre</code> is written with wxPerl.</p>
<h3>Xcos / Scicos</h3>
<p>Xcos (formerly Scicos) is a graphical dynamical system modeler and simulator. It is part of the standard Scilab distribution. <font SIZE="-1">PDL</font> and Perl do not have a direct equivalent to Scilab&#8217;s Xcos. If this feature is important to you, you should probably keep a copy of Scilab around for that.</p>
<h2>Copyright</h2>
<p>Copyright 2010 Daniel Carrera (dcarrera [at] gmail.com). You can distribute and/or modify this document under the same terms as the current Perl license. </p>
<p> See: <a rel="nofollow" href="http://dev.perl.org/licenses/">http://dev.perl.org/licenses/</a></p>
