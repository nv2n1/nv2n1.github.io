---
title: "pdlpp(1)"
name: "pdlpp"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdlpp/"
description: "PDL::PP – Generate PDL routines from concise descriptions"
---

<p>PDL::PP &#8211; Generate PDL routines from concise descriptions </p>
<h2>Synopsis</h2>
<p>e.g. </p>
<pre> pp_def(
 'sumover',
 Pars =&gt; '<a href="//www.systutorials.com/docs/linux/man/n-a/">a</a>(n); [o]b();',
 Code =&gt; q{
 double tmp=0;
 <a href="//www.systutorials.com/docs/linux/man/n-loop/">loop</a>(n) %{
 tmp += $a();
 %}
 $b() = tmp;
 },
 );
 pp_done();</pre>
<h2>Functions</h2>
<p>Here is a quick reference list of the functions provided by <font SIZE="-1">PDL::PP.</font></p>
<h3>pp_add_boot</h3>
<p>Add code to the <font SIZE="-1">BOOT</font> section of generated <font SIZE="-1">XS</font> file</p>
<h3>pp_add_exported</h3>
<p>Add functions to the list of exported functions</p>
<h3>pp_add_isa</h3>
<p>Add entries to the <tt>@ISA</tt> list</p>
<h3>pp_addbegin</h3>
<p>Sets code to be added at the top of the generate .pm file</p>
<h3>pp_addhdr</h3>
<p>Add code and includes to C section of the generated <font SIZE="-1">XS</font> file</p>
<h3>pp_addpm</h3>
<p>Add code to the generated .pm file</p>
<h3>pp_addxs</h3>
<p>Add extra <font SIZE="-1">XS</font> code to the generated <font SIZE="-1">XS</font> file</p>
<h3>pp_beginwrap</h3>
<p>Add BEGIN-block wrapping to code for the generated .pm file</p>
<h3>pp_bless</h3>
<p>Sets the package to which the <font SIZE="-1">XS</font> code is added (default is <font SIZE="-1">PDL</font>)</p>
<h3>pp_boundscheck</h3>
<p>Control state of <font SIZE="-1">PDL</font> bounds checking activity</p>
<h3>pp_core_importList</h3>
<p>Specify what is imported from PDL::Core</p>
<h3>pp_def</h3>
<p>Define a new <font SIZE="-1">PDL</font> function</p>
<h3>pp_deprecate_module</h3>
<p>Add runtime and <font SIZE="-1">POD</font> warnings about a module being deprecated</p>
<h3>pp_done</h3>
<p>Mark the end of <font SIZE="-1">PDL::PP</font> definitions in the file</p>
<h3>pp_export_nothing</h3>
<p>Clear out the export list for your generated module</p>
<h3>pp_line_numbers</h3>
<p>Add line number information to simplify debugging of <font SIZE="-1">PDL::PP</font> code</p>
<h3>pp_setversion</h3>
<p>Set the version for .pm and .xs files</p>
<h2>Overview</h2>
<p>Why do we need <font SIZE="-1">PP</font>? Several reasons: firstly, we want to be able to generate subroutine code for each of the <font SIZE="-1">PDL</font> datatypes (PDL_Byte, PDL_Short,. etc). <font SIZE="-1">AUTOMATICALLY. </font> Secondly, when referring to slices of <font SIZE="-1">PDL</font> arrays in Perl (e.g. <tt>&quot;$a-&gt;slice('0:10:2,:')&quot;</tt> or other things such as transposes) it is nice to be able to do this transparently and to be able to do this &#8216;in-place&#8217; &#8211; i.e, not to have to make a memory copy of the section. <font SIZE="-1">PP</font> handles all the necessary element and offset arithmetic for you. There are also the notions of threading (repeated calling of the same routine for multiple slices, see PDL::Indexing) and dataflow (see PDL::Dataflow) which use of <font SIZE="-1">PP</font> allows. </p>
<p> In much of what follows we will assume familiarity of the reader with the concepts of implicit and explicit threading and index manipulations within <font SIZE="-1">PDL.</font> If you have not yet heard of these concepts or are not very comfortable with them it is time to check PDL::Indexing. </p>
<p> As you may appreciate from its name <font SIZE="-1">PDL::PP</font> is a Pre-Processor, i.e. it expands code via substitutions to make real C-code. Technically, the output is <font SIZE="-1">XS</font> code (see <i>perlxs</i>) but that is very close to C. </p>
<p> So how do you use <font SIZE="-1">PP</font>? Well for the most part you just write ordinary C code except for special <font SIZE="-1">PP</font> constructs which take the form: </p>
<pre> $something(something else)</pre>
<p>or: </p>
<pre> PPfunction %{
 &lt;stuff&gt;
 %}</pre>
<p>The most important <font SIZE="-1">PP</font> construct is the form <tt>&quot;$array()&quot;</tt>. Consider the very simple <font SIZE="-1">PP</font> function to sum the elements of a 1D vector (in fact this is very similar to the actual code used by &#8216;sumover&#8217;): </p>
<pre> pp_def('sumit',
 Pars =&gt; '<a href="//www.systutorials.com/docs/linux/man/n-a/">a</a>(n); [o]b();',
 Code =&gt; q{
 double tmp;
 tmp = 0;
 <a href="//www.systutorials.com/docs/linux/man/n-loop/">loop</a>(n) %{
 tmp += $a();
 %}
 $b() = tmp;
 }
 );</pre>
<p>What&#8217;s going on? The <tt>&quot;Pars =&gt;&quot;</tt> line is very important for <font SIZE="-1">PP &#8211;</font> it specifies all the arguments and their dimensionality. We call this the <i>signature</i> of the <font SIZE="-1">PP</font> function (compare also the explanations in PDL::Indexing). In this case the routine takes a 1-D function as input and returns a 0-D scalar as output. The <tt>&quot;$a()&quot;</tt> <font SIZE="-1">PP</font> construct is used to access elements of the array <a href="/docs/linux/man/n-a/">a</a>(n) for you &#8211; <font SIZE="-1">PP</font> fills in all the required C code. </p>
<p> You will notice that we are using the <tt>&quot;q{}&quot;</tt> single-quote operator. This is not an accident. You generally want to use single quotes to denote your <font SIZE="-1">PP</font> Code sections. <font SIZE="-1">PDL::PP</font> uses <tt>&quot;$var()&quot;</tt> for its parsing and if you don&#8217;t use single quotes, Perl will try to interpolate <tt>&quot;$var()&quot;</tt>. Also, using the single quote <tt>&quot;q&quot;</tt> operator with curly braces makes it look like you are creating a code block, which is What You Mean. (Perl is smart enough to look for nested curly braces and not close the quote until it finds the matching curly brace, so it&#8217;s safe to have nested blocks.) Under other circumstances, such as when you&#8217;re stitching together a Code block using string concatenations, it&#8217;s often easiest to use real single quotes as </p>
<pre> Code =&gt; 'something'.$interpolatable.'somethingelse;'</pre>
<p>In the simple case here where all elements are accessed the <font SIZE="-1">PP</font> construct <tt>&quot;<a href="/docs/linux/man/n-loop/">loop</a>(n) %{ ... %}&quot;</tt> is used to loop over all elements in dimension <tt>&quot;n&quot;</tt>. Note this feature of <font SIZE="-1">PP: ALL DIMENSIONS ARE SPECIFIED BY NAME.</font> </p>
<p> This is made clearer if we avoid the <font SIZE="-1">PP</font> <i>loop()</i> construct and write the loop explicitly using conventional C: </p>
<pre> pp_def('sumit',
 Pars =&gt; '<a href="//www.systutorials.com/docs/linux/man/n-a/">a</a>(n); [o]b();',
 Code =&gt; q{
 int i,n_size;
 double tmp;
 n_size = $<a href="//www.systutorials.com/docs/linux/man/n-SIZE/">SIZE</a>(n);
 tmp = 0;
 for(i=0; i&lt;n_size; i++) {
 tmp += $a(n=&gt;i);
 }
 $b() = tmp;
 },
 );</pre>
<p>which does the same as before, but is more long-winded. You can see to get element <tt>&quot;i&quot;</tt> of a() we say <tt>&quot;$a(n=&gt;i)&quot;</tt> &#8211; we are specifying the dimension by name <tt>&quot;n&quot;</tt>. In 2D we might say: </p>
<pre> Pars=&gt;'a(m,n);',
 ...
 tmp += $a(m=&gt;i,n=&gt;j);
 ...</pre>
<p>The syntax <tt>&quot;m=&gt;i&quot;</tt> borrows from Perl hashes, which are in fact used in the implementation of <font SIZE="-1">PP.</font> One could also say <tt>&quot;$a(n=&gt;j,m=&gt;i)&quot;</tt> as order is not important. </p>
<p> You can also see in the above example the use of another <font SIZE="-1">PP</font> construct &#8211; <tt>$<a href="/docs/linux/man/n-size/">SIZE</a>(n)</tt> to get the length of the dimension <tt>&quot;n&quot;</tt>. </p>
<p> It should, however, be noted that you shouldn&#8217;t write an explicit C-loop when you could have used the <font SIZE="-1">PP </font><tt>&quot;loop&quot;</tt> construct since <font SIZE="-1">PDL::PP</font> checks automatically the loop limits for you, usage of <tt>&quot;loop&quot;</tt> makes the code more concise, etc. But there are certainly situations where you need explicit control of the loop and now you know how to do it ;). </p>
<p> To revisit &#8216;Why <font SIZE="-1">PP</font>?&#8217; &#8211; the above code for <i>sumit()</i> will be generated for each data-type. It will operate on slices of arrays &#8216;in-place&#8217;. It will thread automatically &#8211; e.g. if a 2D array is given it will be called repeatedly for each 1D row (again check PDL::Indexing for the details of threading). And then b() will be a 1D array of sums of each row. We could call it with <tt>$a</tt>-&gt;xchg(0,1) to sum the columns instead. And Dataflow tracing etc. will be available. </p>
<p> You can see <font SIZE="-1">PP</font> saves the programmer from writing a lot of needlessly repetitive C-code &#8212; in our opinion this is one of the best features of <font SIZE="-1">PDL</font> making writing new C subroutines for <font SIZE="-1">PDL</font> an amazingly concise exercise. A second reason is the ability to make <font SIZE="-1">PP</font> expand your concise code definitions into different C code based on the needs of the computer architecture in question. Imagine for example you are lucky to have a supercomputer at your hands; in that case you want <font SIZE="-1">PDL::PP</font> certainly to generate code that takes advantage of the vectorising/parallel computing features of your machine (this a project for the future). In any case, the bottom line is that your unchanged code should still expand to working <font SIZE="-1">XS</font> code even if the internals of <font SIZE="-1">PDL</font> changed. </p>
<p> Also, because you are generating the code in an actual Perl script, there are many fun things that you can do. Let&#8217;s say that you need to write both sumit (as above) and multit. With a little bit of creativity, we can do </p>
<pre> for({Name =&gt; 'sumit', Init =&gt; '0', Op =&gt; '+='},
 {Name =&gt; 'multit', Init =&gt; '1', Op =&gt; '*='}) {
 pp_def($_-&gt;{Name},
 Pars =&gt; '<a href="//www.systutorials.com/docs/linux/man/n-a/">a</a>(n); [o]b();',
 Code =&gt; '
 double tmp;
 tmp = '.$_-&gt;{Init}.';
 <a href="//www.systutorials.com/docs/linux/man/n-loop/">loop</a>(n) %{
 tmp '.$_-&gt;{Op}.' $a();
 %}
 $b() = tmp;
 ');
 }</pre>
<p>which defines both the functions easily. Now, if you later need to change the signature or dimensionality or whatever, you only need to change one place in your code. Yeah, sure, your editor does have &#8216;cut and paste&#8217; and &#8216;search and replace&#8217; but it&#8217;s still less bothersome and definitely more difficult to forget just one place and have strange bugs creep in. Also, adding &#8216;orit&#8217; (bitwise or) later is a one-liner. </p>
<p> And remember, you really have Perl&#8217;s full abilities with you &#8211; you can very easily read any input file and make routines from the information in that file. For simple cases like the above, the author (Tjl) currently favors the hash syntax like the above &#8211; it&#8217;s not too much more characters than the corresponding array syntax but much easier to understand and change. </p>
<p> We should mention here also the ability to get the pointer to the beginning of the data in memory &#8211; a prerequisite for interfacing <font SIZE="-1">PDL</font> to some libraries. This is handled with the <tt>&quot;$P(var)&quot;</tt> directive, see below. </p>
<p> When starting work on a new pp_def&#8217;ined function, if you make a mistake, you will usually find a pile of compiler errors indicating line numbers in the generated <font SIZE="-1">XS</font> file. If you know how to read <font SIZE="-1">XS</font> files (or if you want to learn the hard way), you could open the generated <font SIZE="-1">XS</font> file and search for the line number with the error. However, a recent addition to <font SIZE="-1">PDL::PP</font> helps report the correct line number of your errors: <tt>&quot;pp_line_numbers&quot;</tt>. Working with the original summit example, if you had a mis-spelling of tmp in your code, you could change the (erroneos) code to something like this and the compiler would give you much more useful information: </p>
<pre> pp_def('sumit',
 Pars =&gt; '<a href="//www.systutorials.com/docs/linux/man/n-a/">a</a>(n); [o]b();',
 Code =&gt; pp_line_numbers(__LINE__, q{
 double tmp;
 tmp = 0;
 <a href="//www.systutorials.com/docs/linux/man/n-loop/">loop</a>(n) %{
 tmp += $a();
 %}
 $b() = rmp;
 })
 );</pre>
<p>For the above situation, my compiler tells me: </p>
<pre> ...
 test.pd:15: error: XrmpX undeclared (first use in this function)
 ...</pre>
<p>In my example script (called test.pd), line 15 is exactly the line at which I made my typo: <tt>&quot;rmp&quot;</tt> instead of <tt>&quot;tmp&quot;</tt>. </p>
<p> So, after this quick overview of the general flavour of programming <font SIZE="-1">PDL</font> routines using <font SIZE="-1">PDL::PP</font> let&#8217;s summarise in which circumstances you should actually use this preprocessor/precompiler. You should use <font SIZE="-1">PDL::PP</font> if you want to</p>
<dl>
<dt>&bull;</p>
<dd>interface <font SIZE="-1">PDL</font> to some external library</p>
<dt>&bull;</p>
<dd>write some algorithm that would be slow if coded in Perl (this is not as often as you think; take a look at threading and dataflow first).</p>
<dt>&bull;</p>
<dd>be a <font SIZE="-1">PDL</font> developer (and even then it&#8217;s not obligatory)</dl>
<h2>Warning</h2>
<p>Because of its architecture, <font SIZE="-1">PDL::PP</font> can be both flexible and easy to use on the one hand, yet exuberantly complicated at the same time. Currently, part of the problem is that error messages are not very informative and if something goes wrong, you&#8217;d better know what you are doing and be able to hack your way through the internals (or be able to figure out by trial and error what is wrong with your args to <tt>&quot;pp_def&quot;</tt>). Although work is being done to produce better warnings, do not be afraid to send your questions to the mailing list if you run into trouble.</p>
<h2>Description</h2>
<p>Now that you have some idea how to use <tt>&quot;pp_def&quot;</tt> to define new <font SIZE="-1">PDL</font> functions it is time to explain the general syntax of <tt>&quot;pp_def&quot;</tt>. <tt>&quot;pp_def&quot;</tt> takes as arguments first the name of the function you are defining and then a hash list that can contain various keys. </p>
<p> Based on these keys <font SIZE="-1">PP</font> generates <font SIZE="-1">XS</font> code and a .pm file. The function <tt>&quot;pp_done&quot;</tt> (see example in the <font SIZE="-1">SYNOPSIS</font>) is used to tell <font SIZE="-1">PDL::PP</font> that there are no more definitions in this file and it is time to generate the .xs and<br />
&nbsp;<wbr>.pm file. </p>
<p> As a consequence, there may be several <i>pp_def()</i> calls inside a file (by convention files with <font SIZE="-1">PP</font> code have the extension .pd or .pp) but generally only one <i>pp_done()</i>. </p>
<p> There are two main different types of usage of <i>pp_def()</i>, the &#8216;data operation&#8217; and &#8216;slice operation&#8217; prototypes. </p>
<p> The &#8216;data operation&#8217; is used to take some data, mangle it and output some other data; this includes for example the &#8216;+&#8217; operation, matrix inverse, sumover etc and all the examples we have talked about in this document so far. Implicit and explicit threading and the creation of the result are taken care of automatically in those operations. You can even do dataflow with <tt>&quot;sumit&quot;</tt>, <tt>&quot;sumover&quot;</tt>, etc (don&#8217;t be dismayed if you don&#8217;t understand the concept of dataflow in <font SIZE="-1">PDL</font> very well yet; it is still very much experimental). </p>
<p> The &#8216;slice operation&#8217; is a different kind of operation: in a slice operation, you are not changing any data, you are defining correspondences between different elements of two piddles (examples include the index manipulation/slicing function definitions in the file <i>slices.pd</i> that is part of the <font SIZE="-1">PDL</font> distribution; but beware, this is not introductory level stuff). </p>
<p> If <font SIZE="-1">PDL</font> was compiled with support for bad values (i.e. <tt>&quot;WITH_BADVAL =&gt; 1&quot;</tt>), then additional keys are required for <tt>&quot;pp_def&quot;</tt>, as explained below. </p>
<p> If you are just interested in communicating with some external library (for example some linear algebra/matrix library), you&#8217;ll usually want the &#8216;data operation&#8217; so we are going to discuss that first.</p>
<h2>Data operation</h2>
<h3>A simple example</h3>
<p>In the data operation, you must know what dimensions of data you need. First, an example with scalars: </p>
<pre> pp_def('add',
 Pars =&gt; 'a(); b(); [o]c();',
 Code =&gt; '$c() = $a() + $b();'
 );</pre>
<p>That looks a little strange but let&#8217;s dissect it. The first line is easy: we&#8217;re defining a routine with the name &#8216;add&#8217;. The second line simply declares our parameters and the parentheses mean that they are scalars. We call the string that defines our parameters and their dimensionality the <i>signature</i> of that function. For its relevance with regard to threading and index manipulations check the PDL::Indexing man page. </p>
<p> The third line is the actual operation. You need to use the dollar signs and parentheses to refer to your parameters (this will probably change at some point in the future, once a good syntax is found). </p>
<p> These lines are all that is necessary to actually define the function for <font SIZE="-1">PDL </font>(well, actually it isn&#8217;t; you additionally need to write a Makefile.PL (see below) and build the module (something like &#8216;perl Makefile.PL; make&#8217;); but let&#8217;s ignore that for the moment). So now you can do </p>
<pre> use MyModule;
 $a = pdl 2,3,4;
 $b = pdl 5;
 $c = add($a,$b);
 # or
 add($a,$b,($c=null)); # Alternative form, useful if $c has been
 # preset to something big, not useful here.</pre>
<p>and have threading work correctly (the result is <tt>$c</tt> == [7 8 9]).</p>
<h3>The Pars section: the signature of a <font SIZE="-1">PP</font> function</h3>
<p>Seeing the above example code you will most probably ask: what is this strange <tt>&quot;$c=null&quot;</tt> syntax in the second call to our new <tt>&quot;add&quot;</tt> function? If you take another look at the definition of <tt>&quot;add&quot;</tt> you will notice that the third argument <tt>&quot;c&quot;</tt> is flagged with the qualifier <tt>&quot;[o]&quot;</tt> which tells <font SIZE="-1">PDL::PP</font> that this is an output argument. So the above call to add means &#8216;create a new <tt>$c</tt> from scratch with correct dimensions&#8217; &#8211; <tt>&quot;null&quot;</tt> is a special token for &#8217;empty piddle&#8217; (you might ask why we haven&#8217;t used the value <tt>&quot;undef&quot;</tt> to flag this instead of the <font SIZE="-1">PDL</font> specific <tt>&quot;null&quot;</tt>; we are currently thinking about it ;). </p>
<p> [This should be explained in some other section of the manual as well!!] The reason for having this syntax as an alternative is that if you have really huge piddles, you can do </p>
<pre> $c = PDL-&gt;null;
 for(some long loop) {
 # munge a,b
 add($a,$b,$c);
 # munge c, put something back to a,b
 }</pre>
<p>and avoid allocating and deallocating <tt>$c</tt> each time. It is allocated once at the first <i>add()</i> and thereafter the memory stays until <tt>$c</tt> is destroyed. </p>
<p> If you just say </p>
<pre> $c = add($a,$b);</pre>
<p>the code generated by <font SIZE="-1">PP</font> will automatically fill in <tt>&quot;$c=null&quot;</tt> and return the result. If you want to learn more about the reasons why <font SIZE="-1">PDL::PP</font> supports this style where output arguments are given as last arguments check the PDL::Indexing man page. </p>
<p> <tt>&quot;[o]&quot;</tt> is not the only qualifier a pdl argument can have in the signature. Another important qualifier is the <tt>&quot;[t]&quot;</tt> option which flags a pdl as temporary. What does that mean? You tell <font SIZE="-1">PDL::PP</font> that this pdl is only used for temporary results in the course of the calculation and you are not interested in its value after the computation has been completed. But why should <font SIZE="-1">PDL::PP</font> want to know about this in the first place? The reason is closely related to the concepts of pdl auto creation (you heard about that above) and implicit threading. If you use implicit threading the dimensionality of automatically created pdls is actually larger than that specified in the signature. With <tt>&quot;[o]&quot;</tt> flagged pdls will be created so that they have the additional dimensions as required by the number of implicit thread dimensions. When creating a temporary pdl, however, it will always only be made big enough so that it can hold the result for one iteration in a thread loop, i.e. as large as required by the signature. So less memory is wasted when you flag a pdl as temporary. Secondly, you can use output auto creation with temporary pdls even when you are using explicit threading which is forbidden for normal output pdls flagged with <tt>&quot;[o]&quot;</tt> (see PDL::Indexing). </p>
<p> Here is an example where we use the [t] qualifier. We define the function <tt>&quot;callf&quot;</tt> that calls a C routine <tt>&quot;f&quot;</tt> which needs a temporary array of the same size and type as the array <tt>&quot;a&quot;</tt> (sorry about the forward reference for <tt>$P</tt>; it&#8217;s a pointer access, see below) : </p>
<pre> pp_def('callf',
 Pars =&gt; '<a href="//www.systutorials.com/docs/linux/man/n-a/">a</a>(n); [t] <a href="//www.systutorials.com/docs/linux/man/n-tmp/">tmp</a>(n); [o] b()',
 Code =&gt; 'int ns = $<a href="//www.systutorials.com/docs/linux/man/n-SIZE/">SIZE</a>(n);
 f($P(a),$P(b),$P(tmp),ns);
 '
 );</pre>
<h3>Argument dimensions and the signature</h3>
<p>Now we have just talked about dimensions of pdls and the signature. How are they related? Let&#8217;s say that we want to add a scalar + the index number to a vector: </p>
<pre> pp_def('add2',
 Pars =&gt; '<a href="//www.systutorials.com/docs/linux/man/n-a/">a</a>(n); b(); [o]<a href="//www.systutorials.com/docs/linux/man/n-c/">c</a>(n);',
 Code =&gt; '<a href="//www.systutorials.com/docs/linux/man/n-loop/">loop</a>(n) %{
 $c() = $a() + $b() + n;
 %}'
 );</pre>
<p>There are several points to notice here: first, the <tt>&quot;Pars&quot;</tt> argument now contains the <i>n</i> arguments to show that we have a single dimensions in <i>a</i> and <i>c</i>. It is important to note that dimensions are actual entities that are accessed by name so this declares <i>a</i> and <i>c</i> to have the <code>same</code> first dimensions. In most <font SIZE="-1">PP</font> definitions the size of named dimensions will be set from the respective dimensions of non-output pdls (those with no <tt>&quot;[o]&quot;</tt> flag) but sometimes you might want to set the size of a named dimension explicitly through an integer parameter. See below in the description of the <tt>&quot;OtherPars&quot;</tt> section how that works.</p>
<h3>Constant argument dimensions in the signature</h3>
<p>Suppose you want an output piddle to be created automatically and you know that on every call its dimension will have the same size (say 9) regardless of the dimensions of the input piddles. In this case you use the following syntax in the Pars section to specify the size of the dimension: </p>
<pre> ' [o] y(n=9); '</pre>
<p>As expected, extra dimensions required by threading will be created if necessary. If you need to assign a named dimension according to a more complicated formula (than a constant) you must use the <tt>&quot;RedoDimsCode&quot;</tt> key described below.</p>
<h3>Type conversions and the signature</h3>
<p>The signature also determines the type conversions that will be performed when a <font SIZE="-1">PP</font> function is invoked. So what happens when we invoke one of our previously defined functions with pdls of different type, e.g. </p>
<pre> add2($a,$b,($ret=null));</pre>
<p>where <tt>$a</tt> is of type <tt>&quot;PDL_Float&quot;</tt> and <tt>$b</tt> of type <tt>&quot;PDL_Short&quot;</tt>? With the signature as shown in the definition of <tt>&quot;add2&quot;</tt> above the datatype of the operation (as determined at runtime) is that of the pdl with the &#8216;highest&#8217; type (sequence is byte &lt; short &lt; ushort &lt; long &lt; float &lt; double). In the add2 example the datatype of the operation is float ($a has that datatype). All pdl arguments are then type converted to that datatype (they are not converted inplace but a copy with the right type is created if a pdl argument doesn&#8217;t have the type of the operation). Null pdls don&#8217;t contribute a type in the determination of the type of the operation. However, they will be created with the datatype of the operation; here, for example, <tt>$ret</tt> will be of type float. You should be aware of these rules when calling <font SIZE="-1">PP</font> functions with pdls of different types to take the additional storage and runtime requirements into account. </p>
<p> These type conversions are correct for most functions you normally define with <tt>&quot;pp_def&quot;</tt>. However, there are certain cases where slightly modified type conversion behaviour is desired. For these cases additional qualifiers in the signature can be used to specify the desired properties with regard to type conversion. These qualifiers can be combined with those we have encountered already (the <i>creation qualifiers</i> <tt>&quot;[o]&quot;</tt> and <tt>&quot;[t]&quot;</tt>). Let&#8217;s go through the list of qualifiers that change type conversion behaviour. </p>
<p> The most important is the <tt>&quot;int&quot;</tt> qualifier which comes in handy when a pdl argument represents indices into another pdl. Let&#8217;s take a look at an example from <tt>&quot;PDL::Ufunc&quot;</tt>: </p>
<pre> pp_def('maximum_ind',
 Pars =&gt; '<a href="//www.systutorials.com/docs/linux/man/n-a/">a</a>(n); int [o] b()',
 Code =&gt; '$GENERIC() cur;
 int curind;
 <a href="//www.systutorials.com/docs/linux/man/n-loop/">loop</a>(n) %{
 if (!n || $a() &gt; cur) {cur = $a(); curind = n;}
 %}
 $b() = curind;',
 );</pre>
<p>The function <tt>&quot;maximum_ind&quot;</tt> finds the index of the largest element of a vector. If you look at the signature you notice that the output argument <tt>&quot;b&quot;</tt> has been declared with the additional <tt>&quot;int&quot;</tt> qualifier. This has the following consequences for type conversions: regardless of the type of the input pdl <tt>&quot;a&quot;</tt> the output pdl <tt>&quot;b&quot;</tt> will be of type <tt>&quot;PDL_Long&quot;</tt> which makes sense since <tt>&quot;b&quot;</tt> will represent an index into <tt>&quot;a&quot;</tt>. Furthermore, if you call the function with an existing output pdl <tt>&quot;b&quot;</tt> its type will not influence the datatype of the operation (see above). Hence, even if <tt>&quot;a&quot;</tt> is of a smaller type than <tt>&quot;b&quot;</tt> it will not be converted to match the type of <tt>&quot;b&quot;</tt> but stays untouched, which saves memory and <font SIZE="-1">CPU</font> cycles and is the right thing to do when <tt>&quot;b&quot;</tt> represents indices. Also note that you can use the &#8216;int&#8217; qualifier together with other qualifiers (the <tt>&quot;[o]&quot;</tt> and <tt>&quot;[t]&quot;</tt> qualifiers). Order is significant &#8212; type qualifiers precede creation qualifiers (<tt>&quot;[o]&quot;</tt> and <tt>&quot;[t]&quot;</tt>). </p>
<p> The above example also demonstrates typical usage of the <tt>&quot;$GENERIC()&quot;</tt> macro. It expands to the current type in a so called generic loop. What is a generic loop? As you already heard a <font SIZE="-1">PP</font> function has a runtime datatype as determined by the type of the pdl arguments it has been invoked with. The <font SIZE="-1">PP</font> generated <font SIZE="-1">XS</font> code for this function therefore contains a switch like <tt>&quot;switch (type) {case PDL_Byte: ... case PDL_Double: ...}&quot;</tt> that selects a case based on the runtime datatype of the function (it&#8217;s called a type &#8220;loop&#8221; because there is a loop in <font SIZE="-1">PP</font> code that generates the cases). In any case your code is inserted once for each <font SIZE="-1">PDL</font> type into this switch statement. The <tt>&quot;$GENERIC()&quot;</tt> macro just expands to the respective type in each copy of your parsed code in this <tt>&quot;switch&quot;</tt> statement, e.g., in the <tt>&quot;case PDL_Byte&quot;</tt> section <tt>&quot;cur&quot;</tt> will expand to <tt>&quot;PDL_Byte&quot;</tt> and so on for the other case statements. I guess you realise that this is a useful macro to hold values of pdls in some code. </p>
<p> There are a couple of other qualifiers with similar effects as <tt>&quot;int&quot;</tt>. For your convenience there are the <tt>&quot;float&quot;</tt> and <tt>&quot;double&quot;</tt> qualifiers with analogous consequences on type conversions as <tt>&quot;int&quot;</tt>. Let&#8217;s assume you have a <i>very</i> large array for which you want to compute row and column sums with an equivalent of the <tt>&quot;sumover&quot;</tt> function. However, with the normal definition of <tt>&quot;sumover&quot;</tt> you might run into problems when your data is, e.g. of type short. A call like </p>
<pre> sumover($large_pdl,($sums = null));</pre>
<p>will result in <tt>$sums</tt> be of type short and is therefore prone to overflow errors if <tt>$large_pdl</tt> is a very large array. On the other hand calling </p>
<pre> @dims = $large_pdl-&gt;dims; shift @dims;
 sumover($large_pdl,($sums = zeroes(double,@dims)));</pre>
<p>is not a good alternative either. Now we don&#8217;t have overflow problems with <tt>$sums</tt> but at the expense of a type conversion of <tt>$large_pdl</tt> to double, something bad if this is really a large pdl. That&#8217;s where <tt>&quot;double&quot;</tt> comes in handy: </p>
<pre> pp_def('sumoverd',
 Pars =&gt; '<a href="//www.systutorials.com/docs/linux/man/n-a/">a</a>(n); double [o] b()',
 Code =&gt; 'double tmp=0;
 <a href="//www.systutorials.com/docs/linux/man/n-loop/">loop</a>(n) %{ tmp += a(); %}
 $b() = tmp;',
 );</pre>
<p>This gets us around the type conversion and overflow problems. Again, analogous to the <tt>&quot;int&quot;</tt> qualifier <tt>&quot;double&quot;</tt> results in <tt>&quot;b&quot;</tt> always being of type double regardless of the type of <tt>&quot;a&quot;</tt> without leading to a type conversion of <tt>&quot;a&quot;</tt> as a side effect. </p>
<p> Finally, there are the <tt>&quot;type+&quot;</tt> qualifiers where type is one of <tt>&quot;int&quot;</tt> or <tt>&quot;float&quot;</tt>. What shall that mean. Let&#8217;s illustrate the <tt>&quot;int+&quot;</tt> qualifier with the actual definition of sumover: </p>
<pre> pp_def('sumover',
 Pars =&gt; '<a href="//www.systutorials.com/docs/linux/man/n-a/">a</a>(n); int+ [o] b()',
 Code =&gt; '$GENERIC(b) tmp=0;
 <a href="//www.systutorials.com/docs/linux/man/n-loop/">loop</a>(n) %{ tmp += a(); %}
 $b() = tmp;',
 );</pre>
<p>As we had already seen for the <tt>&quot;int&quot;</tt>, <tt>&quot;float&quot;</tt> and <tt>&quot;double&quot;</tt> qualifiers, a pdl marked with a <tt>&quot;type+&quot;</tt> qualifier does not influence the datatype of the pdl operation. Its meaning is &quot;make this pdl at least of type <tt>&quot;type&quot;</tt> or higher, as required by the type of the operation&quot;. In the sumover example this means that when you call the function with an <tt>&quot;a&quot;</tt> of type PDL_Short the output pdl will be of type PDL_Long (just as would have been the case with the <tt>&quot;int&quot;</tt> qualifier). This again tries to avoid overflow problems when using small datatypes (e.g. byte images). However, when the datatype of the operation is higher than the type specified in the <tt>&quot;type+&quot;</tt> qualifier <tt>&quot;b&quot;</tt> will be created with the datatype of the operation, e.g. when <tt>&quot;a&quot;</tt> is of type double then <tt>&quot;b&quot;</tt> will be double as well. We hope you agree that this is sensible behaviour for <tt>&quot;sumover&quot;</tt>. It should be obvious how the <tt>&quot;float+&quot;</tt> qualifier works by analogy. It may become necessary to be able to specify a set of alternative types for the parameters. However, this will probably not be implemented until someone comes up with a reasonable use for it. </p>
<p> Note that we now had to specify the <tt>$GENERIC</tt> macro with the name of the pdl to derive the type from that argument. Why is that? If you carefully followed our explanations you will have realised that in some cases <tt>&quot;b&quot;</tt> will have a different type than the type of the operation. Calling the &#8216;$GENERIC&#8217; macro with <tt>&quot;b&quot;</tt> as argument makes sure that the type will always the same as that of <tt>&quot;b&quot;</tt> in that part of the generic loop. </p>
<p> This is about all there is to say about the <tt>&quot;Pars&quot;</tt> section in a <tt>&quot;pp_def&quot;</tt> call. You should remember that this section defines the <i>signature</i> of a <font SIZE="-1">PP</font> defined function, you can use several options to qualify certain arguments as output and temporary args and all dimensions that you can later refer to in the <tt>&quot;Code&quot;</tt> section are defined by name. </p>
<p> It is important that you understand the meaning of the signature since in the latest <font SIZE="-1">PDL</font> versions you can use it to define threaded functions from within Perl, i.e. what we call <i>Perl level threading</i>. Please check PDL::Indexing for details.</p>
<h3>The Code section</h3>
<p>The <tt>&quot;Code&quot;</tt> section contains the actual <font SIZE="-1">XS</font> code that will be in the innermost part of a thread loop (if you don&#8217;t know what a thread loop is then you still haven&#8217;t read PDL::Indexing; do it now ;) after any <font SIZE="-1">PP</font> macros (like <tt>$GENERIC</tt>) and <font SIZE="-1">PP</font> functions have been expanded (like the <tt>&quot;loop&quot;</tt> function we are going to explain next). </p>
<p> Let&#8217;s quickly reiterate the <tt>&quot;sumover&quot;</tt> example: </p>
<pre> pp_def('sumover',
 Pars =&gt; '<a href="//www.systutorials.com/docs/linux/man/n-a/">a</a>(n); int+ [o] b()',
 Code =&gt; '$GENERIC(b) tmp=0;
 <a href="//www.systutorials.com/docs/linux/man/n-loop/">loop</a>(n) %{ tmp += a(); %}
 $b() = tmp;',
 );</pre>
<p>The <tt>&quot;loop&quot;</tt> construct in the <tt>&quot;Code&quot;</tt> section also refers to the dimension name so you don&#8217;t need to specify any limits: the loop is correctly sized and everything is done for you, again. </p>
<p> Next, there is the surprising fact that <tt>&quot;$a()&quot;</tt> and <tt>&quot;$b()&quot;</tt> do <code>not</code> contain the index. This is not necessary because we&#8217;re looping over <i>n</i> and both variables know which dimensions they have so they automatically know they&#8217;re being looped over. </p>
<p> This feature comes in very handy in many places and makes for much shorter code. Of course, there are times when you want to circumvent this; here is a function which make a matrix symmetric and serves as an example of how to code explicit looping: </p>
<pre> pp_def('symm',
 Pars =&gt; 'a(n,n); [o]c(n,n);',
 Code =&gt; '<a href="//www.systutorials.com/docs/linux/man/n-loop/">loop</a>(n) %{
 int n2;
 for(n2=n; n2&lt;$<a href="//www.systutorials.com/docs/linux/man/n-SIZE/">SIZE</a>(n); n2++) {
 $c(n0 =&gt; n, n1 =&gt; n2) =
 $c(n0 =&gt; n2, n1 =&gt; n) =
 $a(n0 =&gt; n, n1 =&gt; n2);
 }
 %}
 '
 );</pre>
<p>Let&#8217;s dissect what is happening. Firstly, what is this function supposed to do? From its signature you see that it takes a 2D matrix with equal numbers of columns and rows and outputs a matrix of the same size. From a given input matrix <tt>$a</tt> it computes a symmetric output matrix <tt>$c</tt> (symmetric in the matrix sense that A^T = A where ^T means matrix transpose, or in <font SIZE="-1">PDL</font> parlance <tt>$c</tt> == <tt>$c</tt>-&gt;xchg(0,1)). It does this by using only the values on and below the diagonal of <tt>$a</tt>. In the output matrix <tt>$c</tt> all values on and below the diagonal are the same as those in <tt>$a</tt> while those above the diagonal are a mirror image of those below the diagonal (above and below are here interpreted in the way that <font SIZE="-1">PDL</font> prints 2D pdls). If this explanation still sounds a bit strange just go ahead, make a little file into which you write this definition, build the new <font SIZE="-1">PDL</font> extension (see section on Makefiles for <font SIZE="-1">PP</font> code) and try it out with a couple of examples. </p>
<p> Having explained what the function is supposed to do there are a couple of points worth noting from the syntactical point of view. First, we get the size of the dimension named <tt>&quot;n&quot;</tt> again by using the <tt>$SIZE</tt> macro. Second, there are suddenly these funny <tt>&quot;n0&quot;</tt> and <tt>&quot;n1&quot;</tt> index names in the code though the signature defines only the dimension <tt>&quot;n&quot;</tt>. Why this? The reason becomes clear when you note that both the first and second dimension of <tt>$a</tt> and <tt>$b</tt> are named <tt>&quot;n&quot;</tt> in the signature of <tt>&quot;symm&quot;</tt>. This tells <font SIZE="-1">PDL::PP</font> that the first and second dimension of these arguments should have the same size. Otherwise the generated function will raise a runtime error. However, now in an access to <tt>$a</tt> and <tt>$c</tt> <font SIZE="-1">PDL::PP</font> cannot figure out which index <tt>&quot;n&quot;</tt> refers to any more just from the name of the index. Therefore, the indices with equal dimension names get numbered from left to right starting at 0, e.g. in the above example <tt>&quot;n0&quot;</tt> refers to the first dimension of <tt>$a</tt> and <tt>$c</tt>, <tt>&quot;n1&quot;</tt> to the second and so on. </p>
<p> In all examples so far, we have only used the <tt>&quot;Pars&quot;</tt> and <tt>&quot;Code&quot;</tt> members of the hash that was passed to <tt>&quot;pp_def&quot;</tt>. There are certainly other keys that are recognised by <font SIZE="-1">PDL::PP</font> and we will hear about some of them in the course of this document. Find a (non-exhaustive) list of keys in Appendix A. A list of macros and PPfunctions (we have only encountered some of those in the examples above yet) that are expanded in values of the hash argument to <tt>&quot;pp_def&quot;</tt> is summarised in Appendix B. </p>
<p> At this point, it might be appropriate to mention that <font SIZE="-1">PDL::PP</font> is not a completely static, well designed set of routines (as Tuomas puts it: &#8220;stop thinking of <font SIZE="-1">PP</font> as a set of routines carved in stone&#8221;) but rather a collection of things that the <font SIZE="-1">PDL::PP</font> author (Tuomas J. Lukka) considered he would have to write often into his <font SIZE="-1">PDL</font> extension routines. <font SIZE="-1">PP</font> tries to be expandable so that in the future, as new needs arise, new common code can be abstracted back into it. If you want to learn more on why you might want to change <font SIZE="-1">PDL::PP</font> and how to do it check the section on <font SIZE="-1">PDL::PP</font> internals.</p>
<h3>Handling bad values</h3>
<p>If you do not have bad-value support compiled into <font SIZE="-1">PDL</font> you can ignore this section and the related keys: <tt>&quot;BadCode&quot;</tt>, <tt>&quot;HandleBad&quot;</tt>, &#8230; (try printing out the value of <tt>$PDL::Bad::Status</tt> &#8211; if it equals 0 then move straight on). </p>
<p> There are several keys and macros used when writing code to handle bad values. The first one is the <tt>&quot;HandleBad&quot;</tt> key:</p>
<dl>
<dt>HandleBad =&gt; 0</p>
<dd>This flags a pp-routine as <i></i><font SIZE="-1"><i>NOT</i></font><i></i> handling bad values. If this routine is sent piddles with their <tt>&quot;badflag&quot;</tt> set, then a warning message is printed to <font SIZE="-1">STDOUT</font> and the piddles are processed as if the value used to represent bad values is a valid number. The <tt>&quot;badflag&quot;</tt> value is not propogated to the output piddles. </p>
<p> An example of when this is used is for <font SIZE="-1">FFT</font> routines, which generally do not have a way of ignoring part of the data.</p>
<dt>HandleBad =&gt; 1</p>
<dd>This causes <font SIZE="-1">PDL::PP</font> to write extra code that ensures the BadCode section is used, and that the <tt>&quot;$ISBAD()&quot;</tt> macro (and its brethren) work.</p>
<dt>HandleBad is not given</p>
<dd>If any of the input piddles have their <tt>&quot;badflag&quot;</tt> set, then the output piddles will have their <tt>&quot;badflag&quot;</tt> set, but any supplied BadCode is ignored.</dl>
<p> The value of <tt>&quot;HandleBad&quot;</tt> is used to define the contents of the <tt>&quot;BadDoc&quot;</tt> key, if it is not given. </p>
<p> To handle bad values, code must be written somewhat differently; for instance, </p>
<pre> $c() = $a() + $b();</pre>
<p>becomes something like </p>
<pre> if ( $a() != BADVAL &amp;&amp; $b() != BADVAL ) {
 $c() = $a() + $b();
 } else {
 $c() = BADVAL;
 }</pre>
<p>However, we only want the second version if bad values are present in the input piddles (and that bad-value support is wanted!) &#8211; otherwise we actually want the original code. This is where the <tt>&quot;BadCode&quot;</tt> key comes in; you use it to specify the code to execute if bad values may be present, and <font SIZE="-1">PP</font> uses both it and the <tt>&quot;Code&quot;</tt> section to create something like: </p>
<pre> if ( bad_values_are_present ) {
 fancy_threadloop_stuff {
 BadCode
 }
 } else {
 fancy_threadloop_stuff {
 Code
 }
 }</pre>
<p>This approach means that there is virtually no overhead when bad values are not present (i.e. the badflag routine returns 0). </p>
<p> The BadCode section can use the same macros and looping constructs as the Code section. However, it wouldn&#8217;t be much use without the following additional macros:</p>
<dl>
<dt>$ISBAD(var)</p>
<dd>To check whether a piddle&#8217;s value is bad, use the <tt>$ISBAD</tt> macro: </p>
<pre> if ( $ISBAD(a()) ) { printf(&quot;a() is bad
&quot;); }</pre>
<p>You can also access given elements of a piddle: </p>
<pre> if ( $ISBAD(a(n=&gt;l)) ) { printf(&quot;element %d of a() is bad
&quot;, l); }</pre>
<dt>$ISGOOD(var)</p>
<dd>This is the opposite of the <tt>$ISBAD</tt> macro.</p>
<dt>$SETBAD(var)</p>
<dd>For when you want to set an element of a piddle bad.</p>
<dt>$ISBADVAR(c_var,pdl)</p>
<dd>If you have cached the value of a piddle <tt>&quot;$a()&quot;</tt> into a c-variable (<tt>&quot;foo&quot;</tt> say), then to check whether it is bad, use <tt>&quot;$ISBADVAR(foo,a)&quot;</tt>.</p>
<dt>$ISGOODVAR(c_var,pdl)</p>
<dd>As above, but this time checking that the cached value isn&#8217;t bad.</p>
<dt>$SETBADVAR(c_var,pdl)</p>
<dd>To copy the bad value for a piddle into a c variable, use <tt>&quot;$SETBADVAR(foo,a)&quot;</tt>.</dl>
<p> <i></i><font SIZE="-1"><i>TODO:</i></font><i></i> mention <tt>&quot;$PPISBAD()&quot;</tt> etc macros. </p>
<p> Using these macros, the above code could be specified as: </p>
<pre> Code =&gt; '$c() = $a() + $b();',
 BadCode =&gt; '
 if ( $ISBAD(a()) || $ISBAD(b()) ) {
 $SETBAD(c());
 } else {
 $c() = $a() + $b();
 }',</pre>
<p>Since this is Perl, <font SIZE="-1">TMTOWTDI,</font> so you could also write: </p>
<pre> BadCode =&gt; '
 if ( $ISGOOD(a()) &amp;&amp; $ISGOOD(b()) ) {
 $c() = $a() + $b();
 } else {
 $SETBAD(c());
 }',</pre>
<p>If you want access to the value of the badflag for a given piddle, you can use the <tt>&quot;$PDLSTATExxxx()&quot;</tt> macros:</p>
<dl>
<dt>$PDLSTATEISBAD(pdl)</p>
<dd>
<dt>$PDLSTATEISGOOD(pdl)</p>
<dd>
<dt>$PDLSTATESETBAD(pdl)</p>
<dd>
<dt>$PDLSTATESETGOOD(pdl)</p>
<dd></dl>
<p> <i></i><font SIZE="-1"><i>TODO:</i></font><i></i> mention the <tt>&quot;FindBadStatusCode&quot;</tt> and <tt>&quot;CopyBadStatusCode&quot;</tt> options to <tt>&quot;pp_def&quot;</tt>, as well as the <tt>&quot;BadDoc&quot;</tt> key.</p>
<h3>Interfacing your own/library functions using <font SIZE="-1">PP</font></h3>
<p>Now, consider the following: you have your own C function (that may in fact be part of some library you want to interface to <font SIZE="-1">PDL</font>) which takes as arguments two pointers to vectors of double: </p>
<pre> void myfunc(int n,double *v1,double *v2);</pre>
<p>The correct way of defining the <font SIZE="-1">PDL</font> function is </p>
<pre> pp_def('myfunc',
 Pars =&gt; '<a href="//www.systutorials.com/docs/linux/man/n-a/">a</a>(n); [o]<a href="//www.systutorials.com/docs/linux/man/n-b/">b</a>(n);',
 GenericTypes =&gt; ['D'],
 Code =&gt; 'myfunc($<a href="//www.systutorials.com/docs/linux/man/n-SIZE/">SIZE</a>(n),$P(a),$P(b));'
 );</pre>
<p>The <tt>&quot;$P(&quot;</tt><i>par</i><tt>&quot;)&quot;</tt> syntax returns a pointer to the first element and the other elements are guaranteed to lie after that. </p>
<p> Notice that here it is possible to make many mistakes. First, <tt>$<a href="/docs/linux/man/n-size/">SIZE</a>(n)</tt> must be used instead of <tt>&quot;n&quot;</tt>. Second, you shouldn&#8217;t put any loops in this code. Third, here we encounter a new hash key recognised by <font SIZE="-1">PDL::PP :</font> the <tt>&quot;GenericTypes&quot;</tt> declaration tells <font SIZE="-1">PDL::PP</font> to <font SIZE="-1">ONLY GENERATE THE TYPELOOP FOP THE LIST OF TYPES SPECIFIED.</font> In this case <tt>&quot;double&quot;</tt>. This has two advantages. Firstly the size of the compiled code is reduced vastly, secondly if non-double arguments are passed to <tt>&quot;myfunc()&quot;</tt> <font SIZE="-1">PDL</font> will automatically convert them to double before passing to the external C routine and convert them back afterwards. </p>
<p> One can also use <tt>&quot;Pars&quot;</tt> to qualify the types of individual arguments. Thus one could also write this as: </p>
<pre> pp_def('myfunc',
 Pars =&gt; 'double <a href="//www.systutorials.com/docs/linux/man/n-a/">a</a>(n); double [o]<a href="//www.systutorials.com/docs/linux/man/n-b/">b</a>(n);',
 Code =&gt; 'myfunc($<a href="//www.systutorials.com/docs/linux/man/n-SIZE/">SIZE</a>(n),$P(a),$P(b));'
 );</pre>
<p>The type specification in <tt>&quot;Pars&quot;</tt> exempts the argument from variation in the typeloop &#8211; rather it is automatically converted too and from the type specified. This is obviously useful in a more general example, e.g.: </p>
<pre> void myfunc(int n,float *v1,long *v2);
 pp_def('myfunc',
 Pars =&gt; 'float <a href="//www.systutorials.com/docs/linux/man/n-a/">a</a>(n); long [o]<a href="//www.systutorials.com/docs/linux/man/n-b/">b</a>(n);',
 GenericTypes =&gt; ['F'],
 Code =&gt; 'myfunc($<a href="//www.systutorials.com/docs/linux/man/n-SIZE/">SIZE</a>(n),$P(a),$P(b));'
 );</pre>
<p>Note we still use <tt>&quot;GenericTypes&quot;</tt> to reduce the size of the type loop, obviously <font SIZE="-1">PP</font> could in principle spot this and do it automatically though the code has yet to attain that level of sophistication! </p>
<p> Finally note when types are converted automatically one <font SIZE="-1">MUST</font> use the <tt>&quot;[o]&quot;</tt> qualifier for output variables or you hard one changes will get optimised away by <font SIZE="-1">PP</font>! </p>
<p> If you interface a large library you can automate the interfacing even further. Perl can help you again(!) in doing this. In many libraries you have certain calling conventions. This can be exploited. In short, you can write a little parser (which is really not difficult in Perl) that then generates the calls to <tt>&quot;pp_def&quot;</tt> from parsed descriptions of the functions in that library. For an example, please check the <i>Slatec</i> interface in the <tt>&quot;Lib&quot;</tt> tree of the <font SIZE="-1">PDL</font> distribution. If you want to check (during debugging) which calls to <font SIZE="-1">PP</font> functions your Perl code generated a little helper package comes in handy which replaces the <font SIZE="-1">PP</font> functions by identically named ones that dump their arguments to stdout. </p>
<p> Just say </p>
<pre> perl -MPDL::PP::Dump myfile.pd</pre>
<p>to see the calls to <tt>&quot;pp_def&quot;</tt> and friends. Try it with <i>ops.pd</i> and <i>slatec.pd</i>. If you&#8217;re interested (or want to enhance it), the source is in Basic/Gen/PP/Dump.pm</p>
<h3>Other macros and functions in the Code section</h3>
<p>Macros: So far we have encountered the <tt>$SIZE</tt>, <tt>$GENERIC</tt> and <tt>$P</tt> macros. Now we are going to quickly explain the other macros that are expanded in the <tt>&quot;Code&quot;</tt> section of <font SIZE="-1">PDL::PP</font> along with examples of their usage.</p>
<dl>
<dt>$T</p>
<dd>The <tt>$T</tt> macro is used for type switches. This is very useful when you have to use different external (e.g. library) functions depending on the input type of arguments. The general syntax is </p>
<pre> $Ttypeletters(type_alternatives)</pre>
<p>where <tt>&quot;typeletters&quot;</tt> is a permutation of a subset of the letters <tt>&quot;BSULFD&quot;</tt> which stand for Byte, Short, Ushort, etc. and <tt>&quot;type_alternatives&quot;</tt> are the expansions when the type of the <font SIZE="-1">PP</font> operation is equal to that indicated by the respective letter. Let&#8217;s illustrate this incomprehensible description by an example. Assuming you have two C functions with prototypes </p>
<pre> void float_func(float *in, float *out);
 void double_func(double *in, double *out);</pre>
<p>which do basically the same thing but one accepts float and the other double pointers. You could interface them to <font SIZE="-1">PDL</font> by defining a generic function <tt>&quot;foofunc&quot;</tt> (which will call the correct function depending on the type of the transformation): </p>
<pre> pp_def('foofunc',
 Pars =&gt; ' <a href="//www.systutorials.com/docs/linux/man/n-a/">a</a>(n); [o] b();',
 Code =&gt; ' $TFD(float_func,double_func) ($P(a),$P(b));'
 GenericTypes =&gt; [qw(F D)],
 );</pre>
<p>Please note that you can&#8217;t say </p>
<pre> Code =&gt; ' $TFD(float,double)_func ($P(a),$P(b));'</pre>
<p>since the <tt>$T</tt> macro expands with trailing spaces, analogously to C preprocessor macros. The slightly longer form illustrated above is correct. If you really want brevity, you can of course do </p>
<pre> '$TBSULFD('.(join ',',map {&quot;long_identifier_name_$_&quot;}
 qw/byt short unseigned lounge flotte dubble/).');'</pre>
<dt>$PP</p>
<dd>The <tt>$PP</tt> macro is used for a so called <i>physical pointer access</i>. The <i>physical</i> refers to some internal optimisations of <font SIZE="-1">PDL </font>(for those who are familiar with the <font SIZE="-1">PDL</font> core we are talking about the vaffine optimisations). This macro is mainly for internal use and you shouldn&#8217;t need to use it in any of your normal code.</p>
<dt>$COMP (and the &quot;OtherPars&quot; section)</p>
<dd>The <tt>$COMP</tt> macro is used to access non-pdl values in the code section. Its name is derived from the implementation of transformations in <font SIZE="-1">PDL.</font> The variables you can refer to using <tt>$COMP</tt> are members of the &#8220;compiled&#8221; structure that represents the <font SIZE="-1">PDL</font> transformation in question but does not yet contain any information about dimensions (for further details check PDL::Internals). However, you can treat <tt>$COMP</tt> just as a black box without knowing anything about the implementation of transformations in <font SIZE="-1">PDL.</font> So when would you use this macro? Its main usage is to access values of arguments that are declared in the <tt>&quot;OtherPars&quot;</tt> section of a <tt>&quot;pp_def&quot;</tt> definition. But then you haven&#8217;t heard about the <tt>&quot;OtherPars&quot;</tt> key yet?! Let&#8217;s have another example that illustrates typical usage of both new features: </p>
<pre> pp_def('pnmout',
 Pars =&gt; 'a(m)',
 OtherPars =&gt; &quot;char* fd&quot;,
 GenericTypes =&gt; [qw(B U S L)],
 Code =&gt; 'PerlIO *fp;
 IO *io;
 io = GvIO(gv_fetchpv($COMP(fd),FALSE,SVt_PVIO));
 if (!io || !(fp = IoIFP(io)))
 croak(&quot;Can\'t figure out FP&quot;);
 if (PerlIO_write(fp,$P(a),len) != len)
 croak(&quot;Error writing pnm file&quot;);
 ');</pre>
<p>This function is used to write data from a pdl to a file. The file descriptor is passed as a string into this function. This parameter does not go into the <tt>&quot;Pars&quot;</tt> section since it cannot be usefully treated like a pdl but rather into the aptly named <tt>&quot;OtherPars&quot;</tt> section. Parameters in the <tt>&quot;OtherPars&quot;</tt> section follow those in the <tt>&quot;Pars&quot;</tt> section when invoking the function, i.e. </p>
<pre> open FILE,&quot;&gt;out.dat&quot; or die &quot;couldn't open out.dat&quot;;
 pnmout($pdl,'FILE');</pre>
<p>When you want to access this parameter inside the code section you have to tell <font SIZE="-1">PP</font> by using the <tt>$COMP</tt> macro, i.e. you write <tt>&quot;$COMP(fd)&quot;</tt> as in the example. Otherwise <font SIZE="-1">PP</font> wouldn&#8217;t know that the <tt>&quot;fd&quot;</tt> you are referring to is the same as that specified in the <tt>&quot;OtherPars&quot;</tt> section. </p>
<p> Another use for the <tt>&quot;OtherPars&quot;</tt> section is to set a named dimension in the signature. Let&#8217;s have an example how that is done: </p>
<pre> pp_def('setdim',
 Pars =&gt; '[o] <a href="//www.systutorials.com/docs/linux/man/n-a/">a</a>(n)',
 OtherPars =&gt; 'int ns =&gt; n',
 Code =&gt; '<a href="//www.systutorials.com/docs/linux/man/n-loop/">loop</a>(n) %{ $a() = n; %}',
 );</pre>
<p>This says that the named dimension <tt>&quot;n&quot;</tt> will be initialised from the value of the <i>other parameter</i> <tt>&quot;ns&quot;</tt> which is of integer type (I guess you have realised that we use the <tt>&quot;CType From =&gt; named_dim&quot;</tt> syntax). Now you can call this function in the usual way: </p>
<pre> setdim(($a=null),5);
 print $a;
 [ 0 1 2 3 4 ]</pre>
<p>Admittedly this function is not very useful but it demonstrates how it works. If you call the function with an existing pdl and you don&#8217;t need to explicitly specify the size of <tt>&quot;n&quot;</tt> since <font SIZE="-1">PDL::PP</font> can figure it out from the dimensions of the non-null pdl. In that case you just give the dimension parameter as <tt>&quot;-1&quot;</tt>: </p>
<pre> $a = hist($b);
 setdim($a,-1);</pre>
<p>That should do it.</dl>
<p> The only <font SIZE="-1">PP</font> function that we have used in the examples so far is <tt>&quot;loop&quot;</tt>. Additionally, there are currently two other functions which are recognised in the <tt>&quot;Code&quot;</tt> section:</p>
<dl>
<dt>threadloop</p>
<dd>As we heard above the signature of a <font SIZE="-1">PP</font> defined function defines the dimensions of all the pdl arguments involved in a <i>primitive</i> operation. However, you often call the functions that you defined with <font SIZE="-1">PP</font> with pdls that have more dimensions than those specified in the signature. In this case the primitive operation is performed on all subslices of appropriate dimensionality in what is called a <i>thread loop</i> (see also overview above and PDL::Indexing). Assuming you have some notion of this concept you will probably appreciate that the operation specified in the code section should be optimised since this is the tightest loop inside a thread loop. However, if you revisit the example where we define the <tt>&quot;pnmout&quot;</tt> function, you will quickly realise that looking up the <tt>&quot;IO&quot;</tt> file descriptor in the inner thread loop is not very efficient when writing a pdl with many rows. A better approach would be to look up the <tt>&quot;IO&quot;</tt> descriptor once outside the thread loop and use its value then inside the tightest thread loop. This is exactly where the <tt>&quot;threadloop&quot;</tt> function comes in handy. Here is an improved definition of <tt>&quot;pnmout&quot;</tt> which uses this function: </p>
<pre> pp_def('pnmout',
 Pars =&gt; 'a(m)',
 OtherPars =&gt; &quot;char* fd&quot;,
 GenericTypes =&gt; [qw(B U S L)],
 Code =&gt; 'PerlIO *fp;
 IO *io;
 int len;
 io = GvIO(gv_fetchpv($COMP(fd),FALSE,SVt_PVIO));
 if (!io || !(fp = IoIFP(io)))
 croak(&quot;Can\'t figure out FP&quot;);
 len = $SIZE(m) * sizeof($GENERIC());
 threadloop %{
 if (PerlIO_write(fp,$P(a),len) != len)
 croak(&quot;Error writing pnm file&quot;);
 %}
 ');</pre>
<p>This works as follows. Normally the C code you write inside the <tt>&quot;Code&quot;</tt> section is placed inside a thread loop (i.e. <font SIZE="-1">PP</font> generates the appropriate wrapping <font SIZE="-1">XS</font> code around it). However, when you explicitly use the <tt>&quot;threadloop&quot;</tt> function, <font SIZE="-1">PDL::PP</font> recognises this and doesn&#8217;t wrap your code with an additional thread loop. This has the effect that code you write outside the thread loop is only executed once per transformation and just the code with in the surrounding <tt>&quot;%{ ... %}&quot;</tt> pair is placed within the tightest thread loop. This also comes in handy when you want to perform a decision (or any other code, especially <font SIZE="-1">CPU</font> intensive code) only once per thread, i.e. </p>
<pre> pp_addhdr('
 #define RAW 0
 #define ASCII 1
 ');
 pp_def('do_raworascii',
 Pars =&gt; 'a(); b(); [o]c()',
 OtherPars =&gt; 'int mode',
 Code =&gt; ' switch ($COMP(mode)) {
 case RAW:
 threadloop %{
 /* do raw stuff */
 %}
 break;
 case ASCII:
 threadloop %{
 /* do ASCII stuff */
 %}
 break;
 default:
 croak(&quot;unknown mode&quot;);
 }'
 );</pre>
<dt>types</p>
<dd>The types function works similar to the <tt>$T</tt> macro. However, with the <tt>&quot;types&quot;</tt> function the code in the following block (delimited by <tt>&quot;%{&quot;</tt> and <tt>&quot;%}&quot;</tt> as usual) is executed for all those cases in which the datatype of the operation is <i>any of</i> the types represented by the letters in the argument to <tt>&quot;type&quot;</tt>, e.g. </p>
<pre> Code =&gt; '...
 types(BSUL) %{
 /* do integer type operation */
 %}
 types(FD) %{
 /* do floating point operation */
 %}
 ...'</pre>
</dl>
<h3>The RedoDimsCode Section</h3>
<p>The <tt>&quot;RedoDimsCode&quot;</tt> key is an optional key that is used to compute dimensions of piddles at runtime in case the standard rules for computing dimensions from the signature are not sufficient. The contents of the <tt>&quot;RedoDimsCode&quot;</tt> entry is interpreted in the same way that the Code section is interpreted&#8212; <i>i.e.</i>, <font SIZE="-1">PP</font> macros are expanded and the result is interpreted as C code. The purpose of the code is to set the size of some dimensions that appear in the signature. Storage allocation and threadloops and so forth will be set up as if the computed dimension had appeared in the signature. In your code, you first compute the desired size of a named dimension in the signature according to your needs and then assign that value to it via the $<i>SIZE()</i> macro. </p>
<p> As an example, consider the following situation. You are interfacing an external library routine that requires an temporary array for workspace to be passed as an argument. Two input data arrays that are passed are <tt>p(m)</tt> and <tt><a href="/docs/linux/man/n-x/">x</a>(n)</tt>. The output data array is <tt><a href="/docs/linux/man/n-y/">y</a>(n)</tt>. The routine requires a workspace array with a length of n+m*m, and you&#8217;d like the storage created automatically just like it would be for any piddle flagged with [t] or [o]. What you&#8217;d like is to say something like </p>
<pre> pp_def( &quot;myexternalfunc&quot;,
 Pars =&gt; &quot; p(m); <a href="//www.systutorials.com/docs/linux/man/n-x/">x</a>(n); [o] y; [t] work(n+m*m); &quot;, ...</pre>
<p>but that won&#8217;t work, because <font SIZE="-1">PP</font> can&#8217;t interpret expressions with arithmetic in the signature. Instead you write </p>
<pre> pp_def( &quot;myexternalfunc&quot;,
 Pars =&gt; &quot; p(m); <a href="//www.systutorials.com/docs/linux/man/n-x/">x</a>(n); [o] y; [t] work(wn); &quot;,
 RedoDimsCode =&gt; &quot;
 int im = $PDL(p)-&gt;dims[0];
 int in = $PDL(x)-&gt;dims[0];
 int min = in + im * im;
 int inw = $PDL(work)-&gt;dims[0];
 $SIZE(wn) = inw &gt;= min ? inw : min; &quot;,
 Code =&gt; &quot;
 externalfunc($P(p),$P(x),$SIZE(m),$<a href="//www.systutorials.com/docs/linux/man/n-SIZE/">SIZE</a>(n),$P(work));
 &quot;;)</pre>
<p>This code works as follows: The macro <tt>$PD</tt>L(p) expands to a pointer to the pdl struct for the piddle p. You don&#8217;t want a pointer to the data ( ie <tt>$P</tt> ) in this case, because you want to access the methods for the piddle on the C level. You get the first dimension of each of the piddles and store them in integers. Then you compute the minimum length the work array can be. If the user sent a piddle <tt>&quot;work&quot;</tt> with sufficient storage, then leave it alone. If the user sent, say a null pdl, or no pdl at all, then the size of wn will be zero and you reset it to the minimum value. Before the code in the Code section is executed <font SIZE="-1">PP</font> will create the proper storage for <tt>&quot;work&quot;</tt> if it does not exist. Note that you only took the first dimension of <tt>&quot;p&quot;</tt> and <tt>&quot;x&quot;</tt> because the user may have sent piddles with extra threading dimensions. Of course, the temporary piddle <tt>&quot;work&quot;</tt> (note the [t] flag) should not be given any thread dimensions anyway. </p>
<p> You can also use <tt>&quot;RedoDimsCode&quot;</tt> to set the dimension of a piddle flagged with [o]. In this case you set the dimensions for the named dimension in the signature using $<i>SIZE()</i> as in the preceeding example. However, because the piddle is flagged with [o] instead of [t], threading dimensions will be added if required just as if the size of the dimension were computed from the signature according to the usual rules. Here is an example from PDL::Math </p>
<pre> pp_def(&quot;polyroots&quot;,
 Pars =&gt; '<a href="//www.systutorials.com/docs/linux/man/n-cr/">cr</a>(n); <a href="//www.systutorials.com/docs/linux/man/n-ci/">ci</a>(n); [o]rr(m); [o]ri(m);',
 RedoDimsCode =&gt; 'int sn = $PDL(cr)-&gt;dims[0]; $SIZE(m) = sn-1;',</pre>
<p>The input piddles are the real and imaginary parts of complex coefficients of a polynomial. The output piddles are real and imaginary parts of the roots. There are <tt>&quot;n&quot;</tt> roots to an <tt>&quot;n&quot;</tt>th order polynomial and such a polynomial has <tt>&quot;n+1&quot;</tt> coefficients (the zeoreth through the <tt>&quot;n&quot;</tt>th). In this example, threading will work correctly. That is, the first dimension of the output piddle with have its dimension adjusted, but other threading dimensions will be assigned just as if there were no <tt>&quot;RedoDimsCode&quot;</tt>.</p>
<h3>Typemap handling in the OtherPars section</h3>
<p>The <tt>&quot;OtherPars&quot;</tt> section discussed above is very often absolutely crucial when you interface external libraries with <font SIZE="-1">PDL.</font> However in many cases the external libraries either use derived types or pointers of various types. </p>
<p> The standard way to handle this in Perl is to use a <tt>&quot;typemap&quot;</tt> file. This is discussed in some detail in perlxs in the standard Perl documentation. In <font SIZE="-1">PP</font> the functionality is very similar, so you can create a <tt>&quot;typemap&quot;</tt> file in the directory where your <font SIZE="-1">PP</font> file resides and when it is built it is automatically read in to figure out the appropriate translation between the C type and Perl&#8217;s built-in type. </p>
<p> That said, there are a couple of important differences from the general handling of types in <font SIZE="-1">XS.</font> The first, and probably most important, is that at the moment pointers to types are not allowed in the <tt>&quot;OtherPars&quot;</tt> section. To get around this limitation you must use the <tt>&quot;IV&quot;</tt> type (thanks to Judd Taylor for pointing out that this is necessary for portability). </p>
<p> It is probably best to illustrate this with a couple of code-snippets: </p>
<p> For instance the <tt>&quot;gsl_spline_init&quot;</tt> function has the following C declaration: </p>
<pre> int gsl_spline_init(gsl_spline * spline,
 const double xa[], const double ya[], size_t size);</pre>
<p>Clearly the <tt>&quot;xa&quot;</tt> and <tt>&quot;ya&quot;</tt> arrays are candidates for being passed in as piddles and the <tt>&quot;size&quot;</tt> argument is just the length of these piddles so that can be handled by the <tt>&quot;$SIZE()&quot;</tt> macro in <font SIZE="-1">PP.</font> The problem is the pointer to the <tt>&quot;gsl_spline&quot;</tt> type. The natural solution would be to write an <tt>&quot;OtherPars&quot;</tt> declaration of the form </p>
<pre> OtherPars =&gt; 'gsl_spline *spl'</pre>
<p>and write a short <tt>&quot;typemap&quot;</tt> file which handled this type. This does not work at present however! So what you have to do is to go around the problem slightly (and in some ways this is easier too!): </p>
<p> The solution is to declare <tt>&quot;spline&quot;</tt> in the <tt>&quot;OtherPars&quot;</tt> section using an &#8220;Integer Value&#8221;, <tt>&quot;IV&quot;</tt>. This hides the nature of the variable from <font SIZE="-1">PP</font> and you then need to (well to avoid compiler warnings at least!) perform a type cast when you use the variable in your code. Thus <tt>&quot;OtherPars&quot;</tt> should take the form: </p>
<pre> OtherPars =&gt; 'IV spl'</pre>
<p>and when you use it in the code you will write </p>
<pre> INT2PTR(gsl_spline *, $COMP(spl))</pre>
<p>where the Perl <font SIZE="-1">API</font> macro <tt>&quot;INT2PTR&quot;</tt> has been used to handle the pointer cast to avoid compiler warnings and problems for machines with mixed 32bit and 64bit Perl configurations. Putting this together as Andres Jordan has done (with the modification using <tt>&quot;IV&quot;</tt> by Judd Taylor) in the <tt>&quot;gsl_interp.pd&quot;</tt> in the distribution source you get: </p>
<pre> pp_def('init_meat',
 Pars =&gt; 'double <a href="//www.systutorials.com/docs/linux/man/n-x/">x</a>(n); double <a href="//www.systutorials.com/docs/linux/man/n-y/">y</a>(n);',
 OtherPars =&gt; 'IV spl',
 Code =&gt;'
 gsl_spline_init,( INT2PTR(gsl_spline *, $COMP(spl)), $P(x),$P(y),$<a href="//www.systutorials.com/docs/linux/man/n-SIZE/">SIZE</a>(n)));'
 );</pre>
<p>where I have removed a macro wrapper call, but that would obscure the discussion. </p>
<p> The other minor difference as compared to the standard typemap handling in Perl, is that the user cannot specify non-standard typemap locations or typemap filenames using the <tt>&quot;TYPEMAPS&quot;</tt> option in MakeMaker&#8230; Thus you can only use a file called <tt>&quot;typemap&quot;</tt> and/or the <tt>&quot;IV&quot;</tt> trick above.</p>
<h3>Other useful <font SIZE="-1">PP</font> keys in data operation definitions</h3>
<p>You have already heard about the <tt>&quot;OtherPars&quot;</tt> key. Currently, there are not many other keys for a data operation that will be useful in normal (whatever that is) <font SIZE="-1">PP</font> programming. In fact, it would be interesting to hear about a case where you think you need more than what is provided at the moment. Please speak up on one of the <font SIZE="-1">PDL</font> mailing lists. Most other keys recognised by <tt>&quot;pp_def&quot;</tt> are only really useful for what we call <i>slice operations</i> (see also above). </p>
<p> One thing that is strongly being planned is variable number of arguments, which will be a little tricky. </p>
<p> An incomplete list of the available keys:</p>
<dl>
<dt>Inplace</p>
<dd>Setting this key marks the routine as working inplace &#8211; ie the input and output piddles are the same. An example is <tt>&quot;$a-&gt;inplace-&gt;sqrt()&quot;</tt> (or <tt>&quot;sqrt(inplace($a))&quot;</tt>).</p>
<dl>
<dd>
<dl>
<dt>Inplace =&gt; 1</p>
<dd>Use when the routine is a unary function, such as <tt>&quot;sqrt&quot;</tt>.</p>
<dt>Inplace =&gt; [&#8216;a&#8217;]</p>
<dd>If there are more than one input piddles, specify the name of the one that can be changed inplace using an array reference.</p>
<dt>Inplace =&gt; [&#8216;a&#8217;,&#8217;b&#8217;]</p>
<dd>If there are more than one output piddle, specify the name of the input piddle and output piddle in a 2-element array reference. This probably isn&#8217;t needed, but left in for completeness.</dl>
</dl>
<dl>
<dd>If bad values are being used, care must be taken to ensure the propagation of the badflag when inplace is being used; consider this excerpt from <i>Basic/Bad/bad.pd</i>: </p>
<pre> pp_def('replacebad',HandleBad =&gt; 1,
 Pars =&gt; 'a(); [o]b();',
 OtherPars =&gt; 'double newval',
 Inplace =&gt; 1,
 CopyBadStatusCode =&gt; 
 '/* propogate badflag if inplace AND it has changed */
 if ( a == b &amp;&amp; $ISPDLSTATEBAD(a) )
 PDL-&gt;propogate_badflag( b, 0 );
 /* always make sure the output is &quot;good&quot; */
 $SETPDLSTATEGOOD(b);
 ',
 ...</pre>
<p>Since this routine removes all bad values, then the output piddle had its bad flag cleared. If run inplace (so <tt>&quot;a == b&quot;</tt>), then we have to tell all the children of <tt>&quot;a&quot;</tt> that the bad flag has been cleared (to save time we make sure that we call <tt>&quot;PDL-&gt;propogate_badgflag&quot;</tt> only if the input piddle had its bad flag set). </p>
<p> <font SIZE="-1">NOTE:</font> one idea is that the documentation for the routine could be automatically flagged to indicate that it can be executed inplace, ie something similar to how <tt>&quot;HandleBad&quot;</tt> sets <tt>&quot;BadDoc&quot;</tt> if it&#8217;s not supplied (it&#8217;s not an ideal solution).</dl>
</dl>
<h3>Other <font SIZE="-1">PDL::PP</font> functions to support concise package definition</h3>
<p>So far, we have described the <tt>&quot;pp_def&quot;</tt> and <tt>&quot;pp_done&quot;</tt> functions. <font SIZE="-1">PDL::PP</font> exports a few other functions to aid you in writing concise <font SIZE="-1">PDL</font> extension package definitions. </p>
<p> <i>pp_addhdr</i> </p>
<p> Often when you interface library functions as in the above example you have to include additional C include files. Since the <font SIZE="-1">XS</font> file is generated by <font SIZE="-1">PP</font> we need some means to make <font SIZE="-1">PP</font> insert the appropriate include directives in the right place into the generated <font SIZE="-1">XS</font> file. To this end there is the <tt>&quot;pp_addhdr&quot;</tt> function. This is also the function to use when you want to define some C functions for internal use by some of the <font SIZE="-1">XS</font> functions (which are mostly functions defined by <tt>&quot;pp_def&quot;</tt>). By including these functions here you make sure that <font SIZE="-1">PDL::PP</font> inserts your code before the point where the actual <font SIZE="-1">XS</font> module section begins and will therefore be left untouched by xsubpp (cf. <i>perlxs</i> and <i>perlxstut</i> man pages). </p>
<p> A typical call would be </p>
<pre> pp_addhdr('
 #include &lt;unistd.h&gt; /* we need defs of XXXX */
 #include &quot;libprotos.h&quot; /* prototypes of library functions */
 #include &quot;mylocaldecs.h&quot; /* Local decs */
 static void do_the real_work(PDL_Byte * in, PDL_Byte * out, int n)
 {
 /* do some calculations with the data */
 }
 ');</pre>
<p>This ensures that all the constants and prototypes you need will be properly included and that you can use the internal functions defined here in the <tt>&quot;pp_def&quot;</tt>s, e.g.: </p>
<pre> pp_def('barfoo',
 Pars =&gt; ' <a href="//www.systutorials.com/docs/linux/man/n-a/">a</a>(n); [o] <a href="//www.systutorials.com/docs/linux/man/n-b/">b</a>(n)',
 GenericTypes =&gt; ['B'],
 Code =&gt; ' int ns = $<a href="//www.systutorials.com/docs/linux/man/n-SIZE/">SIZE</a>(n);
 do_the_real_work($P(a),$P(b),ns);
 ',
 );</pre>
<p><i>pp_addpm</i> </p>
<p> In many cases the actual <font SIZE="-1">PP</font> code (meaning the arguments to <tt>&quot;pp_def&quot;</tt> calls) is only part of the package you are currently implementing. Often there is additional Perl code and <font SIZE="-1">XS</font> code you would normally have written into the pm and <font SIZE="-1">XS</font> files which are now automatically generated by <font SIZE="-1">PP.</font> So how to get this stuff into those dynamically generated files? Fortunately, there are a couple of functions, generally called <tt>&quot;pp_addXXX&quot;</tt> that assist you in doing this. </p>
<p> Let&#8217;s assume you have additional Perl code that should go into the generated <code>pm</code>-file. This is easily achieved with the <tt>&quot;pp_addpm&quot;</tt> command: </p>
<pre> pp_addpm(&lt;&lt;'EOD');
 =head1 NAME
 PDL::Lib::Mylib -- a PDL interface to the Mylib library
 =head1 DESCRIPTION
 This package implements an interface to the Mylib package with full
 threading and indexing support (see L&lt;PDL::Indexing&gt;).
 =cut
 use PGPLOT;
 =head2 use_myfunc
 this function applies the myfunc operation to all the
 elements of the input pdl regardless of dimensions
 and returns the sum of the result
 =cut
 sub use_myfunc {
 my $pdl = shift;
 myfunc($pdl-&gt;clump(-1),($res=null));
 return $res-&gt;sum;
 }
 EOD</pre>
<p><i>pp_add_exported</i> </p>
<p> You have probably got the idea. In some cases you also want to export your additional functions. To avoid getting into trouble with <font SIZE="-1">PP</font> which also messes around with the <tt>@EXPORT</tt> array you just tell <font SIZE="-1">PP</font> to add your functions to the list of exported functions: </p>
<pre> pp_add_exported('use_myfunc gethynx');</pre>
<p><i>pp_add_isa</i> </p>
<p> The <tt>&quot;pp_add_isa&quot;</tt> command works like the the <tt>&quot;pp_add_exported&quot;</tt> function. The arguments to <tt>&quot;pp_add_isa&quot;</tt> are added the <tt>@ISA</tt> list, e.g. </p>
<pre> pp_add_isa(' Some::Other::Class ');</pre>
<p><i>pp_bless</i> </p>
<p> If your pp_def routines are to be used as object methods use <tt>&quot;pp_bless&quot;</tt> to specify the package (i.e. class) to which your <i>pp_def</i>ed methods will be added. For example, <tt>&quot;pp_bless('PDL::MyClass')&quot;</tt>. The default is <tt>&quot;PDL&quot;</tt> if this is omitted. </p>
<p> <i>pp_addxs</i> </p>
<p> Sometimes you want to add extra <font SIZE="-1">XS</font> code of your own (that is generally not involved with any threading/indexing issues but supplies some other functionality you want to access from the Perl side) to the generated <font SIZE="-1">XS</font> file, for example </p>
<pre> pp_addxs('','
 # Determine endianness of machine
 int
 isbigendian()
 CODE:
 unsigned short i;
 PDL_Byte *b;
 i = 42; b = (PDL_Byte*) (void*) &amp;i;
 if (*b == 42)
 RETVAL = 0;
 else if (*(b+1) == 42)
 RETVAL = 1;
 else
 croak(&quot;Impossible - machine is neither big nor little endian!!
&quot;);
 OUTPUT:
 RETVAL
 ');</pre>
<p>Especially <tt>&quot;pp_add_exported&quot;</tt> and <tt>&quot;pp_addxs&quot;</tt> should be used with care. <font SIZE="-1">PP</font> uses PDL::Exporter, hence letting <font SIZE="-1">PP</font> export your function means that they get added to the standard list of function exported by default (the list defined by the export tag &#8220;:Func&#8221;). If you use <tt>&quot;pp_addxs&quot;</tt> you shouldn&#8217;t try to do anything that involves threading or indexing directly. <font SIZE="-1">PP</font> is much better at generating the appropriate code from your definitions. </p>
<p> <i>pp_add_boot</i> </p>
<p> Finally, you may want to add some code to the <font SIZE="-1">BOOT</font> section of the <font SIZE="-1">XS</font> file (if you don&#8217;t know what that is check <i>perlxs</i>). This is easily done with the <tt>&quot;pp_add_boot&quot;</tt> command: </p>
<pre> pp_add_boot(&lt;&lt;EOB);
 descrip = mylib_initialize(KEEP_OPEN);
 if (descrip == NULL)
 croak(&quot;Can't initialize library&quot;);
 GlobalStruc-&gt;descrip = descrip;
 GlobalStruc-&gt;maxfiles = 200;
 EOB</pre>
<p><i>pp_export_nothing</i> </p>
<p> By default, <font SIZE="-1">PP</font>.pm puts all subs defined using the pp_def function into the output .pm file&#8217;s <font SIZE="-1">EXPORT</font> list. This can create problems if you are creating a subclassed object where you don&#8217;t want any methods exported. (i.e. the methods will only be called using the <tt>$object</tt>-&gt;method syntax). </p>
<p> For these cases you can call <i>pp_export_nothing()</i> to clear out the export list. Example (At the end of the .pd file): </p>
<pre> pp_export_nothing();
 pp_done();</pre>
<p><i>pp_core_importList</i> </p>
<p> By default, <font SIZE="-1">PP</font>.pm puts the &#8216;use Core;&#8217; line into the output .pm file. This imports Core&#8217;s exported names into the current namespace, which can create problems if you are over-riding one of Core&#8217;s methods in the current file. You end up getting messages like &#8220;Warning: sub sumover redefined in file subclass.pm&#8221; when running the program. </p>
<p> For these cases the pp_core_importList can be used to change what is imported from Core.pm. For example: </p>
<pre> pp_core_importList('()')</pre>
<p>This would result in </p>
<pre> use Core();</pre>
<p>being generated in the output .pm file. This would result in no names being imported from Core.pm. Similarly, calling </p>
<pre> pp_core_importList(' qw/ barf /')</pre>
<p>would result in </p>
<pre> use Core qw/ barf/;</pre>
<p>being generated in the output .pm file. This would result in just &#8216;barf&#8217; being imported from Core.pm. </p>
<p> <i>pp_setversion</i> </p>
<p> I am pretty sure that this allows you to simultaneously set the .pm and .xs files&#8217; versions, thus avoiding unnecessary version-skew between the two. To use this, simply have the following line at some point in your .pd file: </p>
<pre> pp_setversion('0.0.3');</pre>
<p>However, don&#8217;t use this if you use Module::Build::PDL. See that module&#8217;s documentation for details. </p>
<p> <i>pp_deprecate_module</i> </p>
<p> If a particular module is deemed obsolete, this function can be used to mark it as deprecated. This has the effect of emitting a warning when a user tries to <tt>&quot;use&quot;</tt> the module. The generated <font SIZE="-1">POD</font> for this module also carries a deprecation notice. The replacement module can be passed as an argument like this: </p>
<pre> pp_deprecate_module( infavor =&gt; &quot;PDL::NewNonDeprecatedModule&quot; );</pre>
<p>Note that function affects <i>only</i> the runtime warning and the <font SIZE="-1">POD.</font></p>
<h2>Making your PP function private</h2>
<p>Let&#8217;s say that you have a function in your module called PDL::foo that uses the <font SIZE="-1">PP</font> function <tt>&quot;bar_pp&quot;</tt> to do the heavy lifting. But you don&#8217;t want to advertise that <tt>&quot;bar_pp&quot;</tt> exists. To do this, you must move your <font SIZE="-1">PP</font> function to the top of your module file, then call </p>
<pre> pp_export_nothing()</pre>
<p>to clear the <tt>&quot;EXPORT&quot;</tt> list. To ensure that no documentation (even the default <font SIZE="-1">PP</font> docs) is generated, set </p>
<pre> Doc =&gt; undef</pre>
<p>and to prevent the function from being added to the symbol table, set </p>
<pre> PMFunc =&gt; ''</pre>
<p>in your pp_def declaration (see Image2D.pd for an example). This will effectively make your <font SIZE="-1">PP</font> function &#8220;private.&#8221; However, it is <i>always</i> accessible via PDL::bar_pp due to Perl&#8217;s module design. But making it private will cause the user to go very far out of his or her way to use it, so he or she shoulders the consequences!</p>
<h2>Slice operation</h2>
<p>The slice operation section of this manual is provided using dataflow and lazy evaluation: when you need it, ask Tjl to write it. a delivery in a week from when I receive the email is 95% probable and two week delivery is 99% probable. </p>
<p> And anyway, the slice operations require a much more intimate knowledge of <font SIZE="-1">PDL</font> internals than the data operations. Furthermore, the complexity of the issues involved is considerably higher than that in the average data operation. If you would like to convince yourself of this fact take a look at the <i>Basic/Slices/slices.pd</i> file in the <font SIZE="-1">PDL</font> distribution :-). Nevertheless, functions generated using the slice operations are at the heart of the index manipulation and dataflow capabilities of <font SIZE="-1">PDL.</font> </p>
<p> Also, there are a lot of dirty issues with virtual piddles and vaffines which we shall entirely skip here.</p>
<h3>Slices and bad values</h3>
<p>Slice operations need to be able to handle bad values (if support is compiled into <font SIZE="-1">PDL</font>). The easiest thing to do is look at <i>Basic/Slices/slices.pd</i> to see how this works. </p>
<p> Along with <tt>&quot;BadCode&quot;</tt>, there are also the <tt>&quot;BadBackCode&quot;</tt> and <tt>&quot;BadRedoDimsCode&quot;</tt> keys for <tt>&quot;pp_def&quot;</tt>. However, any <tt>&quot;EquivCPOffsCode&quot;</tt> should <i>not</i> need changing, since any changes are absorbed into the definition of the <tt>&quot;$EQUIVCPOFFS()&quot;</tt> macro (i.e. it is handled automatically by <font SIZE="-1">PDL::PP</font>&gt;.</p>
<h3>A few notes on writing a slicing routine&#8230;</h3>
<p>The following few paragraphs describe writing of a new slicing routine (&#8216;range&#8217;); any errors are <font SIZE="-1">CED</font>&#8216;s. (&#8211;CED 26-Aug-2002)</p>
<h2>Handling of warn and barf in PP Code</h2>
<p>For printing warning messages or aborting/dieing, you can call <tt>&quot;warn&quot;</tt> or <tt>&quot;barf&quot;</tt> from <font SIZE="-1">PP</font> code. However, you should be aware that these calls have been redefined using C preprocessor macros to <tt>&quot;PDL-&gt;barf&quot;</tt> and <tt>&quot;PDL-&gt;warn&quot;</tt>. These redefinitions are in place to keep you from inadvertently calling perl&#8217;s <tt>&quot;warn&quot;</tt> or <tt>&quot;barf&quot;</tt> directly, which can cause segfaults during pthreading (i.e. processor multi-threading). </p>
<p> <font SIZE="-1">PDL</font>&#8216;s own versions of <tt>&quot;barf&quot;</tt> and <tt>&quot;warn&quot;</tt> will queue-up warning or barf messages until after pthreading is completed, and then call the perl versions of these routines. </p>
<p> See PDL::ParallelCPU for more information on pthreading.</p>
<h2>Useful Routines</h2>
<p>The <font SIZE="-1">PDL </font><tt>&quot;Core&quot;</tt> structure, defined in <i>Basic/Core/pdlcore.h.PL</i>, contains pointers to a number of routines that may be useful to you. The majority of these routines deal with manipulating piddles, but some are more general:</p>
<dl>
<dt><font SIZE="-1">PDL-</font>&gt;qsort_B( PDL_Byte *xx, int a, int b )</p>
<dd>Sort the array <tt>&quot;xx&quot;</tt> between the indices <tt>&quot;a&quot;</tt> and <tt>&quot;b&quot;</tt>. There are also versions for the other <font SIZE="-1">PDL</font> datatypes, with postfix <tt>&quot;_S&quot;</tt>, <tt>&quot;_U&quot;</tt>, <tt>&quot;_L&quot;</tt>, <tt>&quot;_F&quot;</tt>, and <tt>&quot;_D&quot;</tt>. Any module using this must ensure that <tt>&quot;PDL::Ufunc&quot;</tt> is loaded.</p>
<dt><font SIZE="-1">PDL-</font>&gt;qsort_ind_B( PDL_Byte *xx, int *ix, int a, int b )</p>
<dd>As for <tt>&quot;PDL-&gt;qsort_B&quot;</tt>, but this time sorting the indices rather than the data.</dl>
<p> The routine <tt>&quot;med2d&quot;</tt> in <i>Lib/Image2D/image2d.pd</i> shows how such routines are used.</p>
<h2>Makefiles For Pp Files</h2>
<p>If you are going to generate a package from your <font SIZE="-1">PP</font> file (typical file extensions are <tt>&quot;.pd&quot;</tt> or <tt>&quot;.pp&quot;</tt> for the files containing <font SIZE="-1">PP</font> code) it is easiest and safest to leave generation of the appropriate commands to the Makefile. In the following we will outline the typical format of a Perl Makefile to automatically build and install your package from a description in a <font SIZE="-1">PP</font> file. Most of the rules to build the xs, pm and other required files from the <font SIZE="-1">PP</font> file are already predefined in the PDL::Core::Dev package. We just have to tell MakeMaker to use it. </p>
<p> In most cases you can define your Makefile like </p>
<pre> # Makefile.PL for a package defined by PP code.
 use PDL::Core::Dev; # Pick up development utilities
 use ExtUtils::MakeMaker;
 $package = [&quot;mylib.pd&quot;,Mylib,PDL::Lib::Mylib];
 %hash = pdlpp_stdargs($package);
 $hash{OBJECT} .= ' additional_Ccode$(OBJ_EXT) ';
 $hash{clean}-&gt;{FILES} .= ' todelete_Ccode$(OBJ_EXT) ';
 $hash{'VERSION_FROM'} = 'mylib.pd';
 WriteMakefile(%hash);
 sub MY::postamble { pdlpp_postamble($package); }</pre>
<p>Here, the list in <tt>$package</tt> is: first: <font SIZE="-1">PP</font> source file name, then the prefix for the produced files and finally the whole package name. You can modify the hash in whatever way you like but it would be reasonable to stay within some limits so that your package will continue to work with later versions of <font SIZE="-1">PDL.</font> </p>
<p> If you don&#8217;t want to use prepackaged arguments, here is a generic <i>Makefile.PL</i> that you can adapt for your own needs: </p>
<pre> # Makefile.PL for a package defined by PP code.
 use PDL::Core::Dev; # Pick up development utilities
 use ExtUtils::MakeMaker;
 WriteMakefile(
 'NAME' =&gt; 'PDL::Lib::Mylib',
 'VERSION_FROM' =&gt; 'mylib.pd',
 'TYPEMAPS' =&gt; [&amp;PDL_TYPEMAP()],
 'OBJECT' =&gt; 'mylib$(OBJ_EXT) additional_Ccode$(OBJ_EXT)',
 'PM' =&gt; { 'Mylib.pm' =&gt; '$(INST_LIBDIR)/Mylib.pm'},
 'INC' =&gt; &amp;PDL_INCLUDE(), # add include dirs as required by your lib
 'LIBS' =&gt; [''], # add link directives as necessary
 'clean' =&gt; {'FILES' =&gt;
 'Mylib.pm Mylib.xs Mylib$(OBJ_EXT)
 additional_Ccode$(OBJ_EXT)'},
 );
 # Add genpp rule; this will invoke PDL::PP on our PP file
 # the argument is an array reference where the array has three string elements:
 # arg1: name of the source file that contains the PP code
 # arg2: basename of the xs and pm files to be generated
 # arg3: name of the package that is to be generated
 sub MY::postamble { pdlpp_postamble([&quot;mylib.pd&quot;,Mylib,PDL::Lib::Mylib]); }</pre>
<p>To make life even easier PDL::Core::Dev defines the function <tt>&quot;pdlpp_stdargs&quot;</tt> that returns a hash with default values that can be passed (either directly or after appropriate modification) to a call to WriteMakefile. Currently, <tt>&quot;pdlpp_stdargs&quot;</tt> returns a hash where the keys are filled in as follows: </p>
<pre> (
 'NAME' =&gt; $mod,
 'TYPEMAPS' =&gt; [&amp;PDL_TYPEMAP()],
 'OBJECT' =&gt; &quot;$pref\$(OBJ_EXT)&quot;,
 PM =&gt; {&quot;$pref.pm&quot; =&gt; &quot;\$(INST_LIBDIR)/$pref.pm&quot;},
 MAN3PODS =&gt; {&quot;$src&quot; =&gt; &quot;\$(INST_MAN3DIR)/$mod.\$(MAN3EXT)&quot;},
 'INC' =&gt; &amp;PDL_INCLUDE(),
 'LIBS' =&gt; [''],
 'clean' =&gt; {'FILES' =&gt; &quot;$pref.xs $pref.pm $pref\$(OBJ_EXT)&quot;},
 )</pre>
<p>Here, <tt>$src</tt> is the name of the source file with <font SIZE="-1">PP</font> code, <tt>$pref</tt> the prefix for the generated .pm and .xs files and <tt>$mod</tt> the name of the extension module to generate.</p>
<h2>Internals</h2>
<p>The internals of the current version consist of a large table which gives the rules according to which things are translated and the subs which implement these rules. </p>
<p> Later on, it would be good to make the table modifiable by the user so that different things may be tried. </p>
<p> [Meta comment: here will hopefully be more in the future; currently, your best bet will be to read the source code :-( or ask on the list (try the latter first) ]</p>
<h2>Appendix A: Some keys recognised by PDL::PP</h2>
<p>Unless otherwise specified, the arguments are strings. Keys marked with (bad) are only used if bad-value support is compiled into <font SIZE="-1">PDL.</font></p>
<dl>
<dt>Pars</p>
<dd>define the signature of your function</p>
<dt>OtherPars</p>
<dd>arguments which are not pdls. Default: nothing. This is a semi-colon separated list of arguments, e.g., <tt>&quot;OtherPars=&gt;'int k; double value; char* fd'&quot;</tt>. See <tt>$COMP(x)</tt> and also the same entry in Appendix B.</p>
<dt>Code</p>
<dd>the actual code that implements the functionality; several <font SIZE="-1">PP</font> macros and <font SIZE="-1">PP</font> functions are recognised in the string value</p>
<dt>HandleBad (bad)</p>
<dd>If set to 1, the routine is assumed to support bad values and the code in the BadCode key is used if bad values are present; it also sets things up so that the <tt>&quot;$ISBAD()&quot;</tt> etc macros can be used. If set to 0, cause the routine to print a warning if any of the input piddles have their bad flag set.</p>
<dt>BadCode (bad)</p>
<dd>Give the code to be used if bad values may be present in the input piddles. Only used if <tt>&quot;HandleBad =&gt; 1&quot;</tt>.</p>
<dt>GenericTypes</p>
<dd>An array reference. The array may contain any subset of the one-character strings `B&#8217;, `S&#8217;, `U&#8217;, `L&#8217;, `Q&#8217;, `F&#8217; and `D&#8217;, which specify which types your operation will accept. The meaning of each type is: </p>
<pre> B - signed byte (i.e. signed char)
 S - signed short (two-byte integer)
 U - unsigned short
 L - signed long (four-byte integer, int on 32 bit systems)
 Q - signed long long (eight byte integer)
 F - float
 D - double</pre>
<p>This is very useful (and important!) when interfacing an external library. Default: [qw/B S U L Q F D/]</p>
<dt>Inplace</p>
<dd>Mark a function as being able to work inplace. </p>
<pre> Inplace =&gt; 1 if Pars =&gt; 'a(); [o]b();'
 Inplace =&gt; ['a'] if Pars =&gt; 'a(); b(); [o]c();'
 Inplace =&gt; ['a','b'] if Pars =&gt; 'a(); b(); [o]c(); [o]d();'</pre>
<p>If bad values are being used, care must be taken to ensure the propagation of the badflag when inplace is being used; for instance see the code for <tt>&quot;replacebad&quot;</tt> in <i>Basic/Bad/bad.pd</i>.</p>
<dt>Doc</p>
<dd>Used to specify a documentation string in Pod format. See PDL::Doc for information on <font SIZE="-1">PDL</font> documentation conventions. Note: in the special case where the <font SIZE="-1">PP </font>&#8216;Doc&#8217; string is one line this is implicitly used for the quick reference <font SIZE="-1">AND</font> the documentation! </p>
<p> If the Doc field is omitted <font SIZE="-1">PP</font> will generate default documentation (after all it knows about the Signature). </p>
<p> If you really want the function <font SIZE="-1">NOT</font> to be documented in any way at this point (e.g. for an internal routine, or because you are doing it elsewhere in the code) explicitly specify <tt>&quot;Doc=&gt;undef&quot;</tt>.</p>
<dt>BadDoc (bad)</p>
<dd>Contains the text returned by the <tt>&quot;badinfo&quot;</tt> command (in <tt>&quot;perldl&quot;</tt>) or the <tt>&quot;-b&quot;</tt> switch to the <tt>&quot;pdldoc&quot;</tt> shell script. In many cases, you will not need to specify this, since the information can be automatically created by <font SIZE="-1">PDL::PP.</font> However, as befits computer-generated text, it&#8217;s rather stilted; it may be much better to do it yourself!</p>
<dt>NoPthread</p>
<dd>Optional flag to indicate the <font SIZE="-1">PDL</font> function should <code>not</code> use processor threads (i.e. pthreads or <font SIZE="-1">POSIX</font> threads) to split up work across mutliple <font SIZE="-1">CPU</font> cores. This option is typically set to 1 if the underlying <font SIZE="-1">PDL</font> function is not threadsafe. If this option isn&#8217;t present, then the function is assumed to be threadsafe. This option only applies if <font SIZE="-1">PDL</font> has been compiled with <font SIZE="-1">POSIX</font> threads enabled.</p>
<dt>PMCode</p>
<dd><font SIZE="-1">PDL</font> functions allow you to pass in a piddle into which you want the output saved. This is handy because you can allocate an output piddle once and reuse it many times; the alternative would be for <font SIZE="-1">PDL</font> to create a new piddle each time, which may waste compute cycles or, more likely, <font SIZE="-1">RAM.</font> This added flexibility comes at the cost of more complexity: <font SIZE="-1">PDL::PP</font> has to write functions that are smart enough to count the arguments passed to it and create new piddles on the fly, but only if you want them. </p>
<p> <font SIZE="-1">PDL::PP</font> is smart enough to do that, but there are restrictions on argument order and the like. If you want a more flexible function, you can write your own Perl-side wrapper and specify it in the PMCode key. The string that you supply must (should) define a Perl function with a name that matches what you gave to pp_def in the first place. When you wish to eventually invoke the PP-generated function, you will need to supply all piddles in the exact order specified in the signature: output piddles are not optional, and the PP-generated function will not return anything. The obfuscated name that you will call is _&lt;funcname&gt;_int. </p>
<p> I believe this documentation needs further clarification, but this will have to do. :-(</p>
<dt>PMFunc</p>
<dd>When pp_def generates functions, it typically defines them in the <font SIZE="-1">PDL</font> package. Then, in the .pm file that it generates for your module, it typically adds a line that essentially copies that function into your current package&#8217;s symbol table with code that looks like this: </p>
<pre> *func_name = \&amp;PDL::func_name;</pre>
<p>It&#8217;s a little bit smarter than that (it knows when to wrap that sort of thing in a <font SIZE="-1">BEGIN</font> block, for example, and if you specified something different for pp_bless), but that&#8217;s the gist of it. If you don&#8217;t care to import the function into your current package&#8217;s symbol table, you can specify </p>
<pre> PMFunc =&gt; '',</pre>
<p>PMFunc has no other side-effects, so you could use it to insert arbitrary Perl code into your module if you like. However, you should use pp_addpm if you want to add Perl code to your module.</dl>
<h2>Appendix B: PP macros and functions</h2>
<h3>Macros</h3>
<p>Macros labeled by (bad) are only used if bad-value support is compiled into <font SIZE="-1">PDL.</font></p>
<dl>
<dt>$<i>variablename_from_sig</i>()</p>
<dd>access a pdl (by its name) that was specified in the signature</p>
<dt>$COMP(x)</p>
<dd>access a value in the private data structure of this transformation (mainly used to use an argument that is specified in the <tt>&quot;OtherPars&quot;</tt> section)</p>
<dt>$<a href="/docs/linux/man/n-size/">SIZE</a>(n)</p>
<dd>replaced at runtime by the actual size of a <i>named</i> dimension (as specified in the <i>signature</i>)</p>
<dt>$<i>GENERIC()</i></p>
<dd>replaced by the C type that is equal to the runtime type of the operation</p>
<dt>$P(a)</p>
<dd>a pointer access to the <font SIZE="-1">PDL</font> named <tt>&quot;a&quot;</tt> in the signature. Useful for interfacing to C functions</p>
<dt>$PP(a)</p>
<dd>a physical pointer access to pdl <tt>&quot;a&quot;</tt>; mainly for internal use</p>
<dt>$TXXX(Alternative,Alternative)</p>
<dd>expansion alternatives according to runtime type of operation, where <font SIZE="-1">XXX</font> is some string that is matched by <tt>&quot;/[BSULFD+]/&quot;</tt>.</p>
<dt>$PDL(a)</p>
<dd>return a pointer to the pdl data structure (pdl *) of piddle <tt>&quot;a&quot;</tt></p>
<dt>$ISBAD(a()) (bad)</p>
<dd>returns true if the value stored in <tt>&quot;a()&quot;</tt> equals the bad value for this piddle. Requires <tt>&quot;HandleBad&quot;</tt> being set to 1.</p>
<dt>$ISGOOD(a()) (bad)</p>
<dd>returns true if the value stored in <tt>&quot;a()&quot;</tt> does not equal the bad value for this piddle. Requires <tt>&quot;HandleBad&quot;</tt> being set to 1.</p>
<dt>$SETBAD(a()) (bad)</p>
<dd>Sets <tt>&quot;a()&quot;</tt> to equal the bad value for this piddle. Requires <tt>&quot;HandleBad&quot;</tt> being set to 1.</dl>
<h3>functions</h3>
<dl>
<dt>&quot;loop(DIMS) %{ &#8230; %}&quot;</p>
<dd>loop over named dimensions; limits are generated automatically by <font SIZE="-1">PP</font></p>
<dt>&quot;threadloop %{ &#8230; %}&quot;</p>
<dd>enclose following code in a thread loop</p>
<dt>&quot;types(TYPES) %{ &#8230; %}&quot;</p>
<dd>execute following code if type of operation is any of <tt>&quot;TYPES&quot;</tt></dl>
<h2>Appendix C: Functions imported by PDL::PP</h2>
<p>A number of functions are imported when you <tt>&quot;use PDL::PP&quot;</tt>. These include functions that control the generated C or <font SIZE="-1">XS</font> code, functions that control the generated Perl code, and functions that manipulate the packages and symbol tables into which the code is created.</p>
<h3>Generating C and <font SIZE="-1">XS</font> Code</h3>
<p><font SIZE="-1">PDL::PP</font>&#8216;s main purpose is to make it easy for you to wrap the threading engine around your own C code, but you can do some other things, too.</p>
<dl>
<dt>pp_def</p>
<dd>Used to wrap the threading engine around your C code. Virtually all of this document discusses the use of pp_def.</p>
<dt>pp_done</p>
<dd>Indicates you are done with <font SIZE="-1">PDL::PP</font> and that it should generate its .xs and .pm files based upon the other pp_* functions that you have called. This function takes no arguments.</p>
<dt>pp_addxs</p>
<dd>This lets you add <font SIZE="-1">XS</font> code to your .xs file. This is useful if you want to create Perl-accessible functions that invoke C code but cannot or should not invoke the threading engine. <font SIZE="-1">XS</font> is the standard means by which you wrap Perl-accessible C code. You can learn more at perlxs.</p>
<dt>pp_add_boot</p>
<dd>This function adds whatever string you pass to the <font SIZE="-1">XS BOOT</font> section. The <font SIZE="-1">BOOT</font> section is C code that gets called by Perl when your module is loaded and is useful for automatic initialization. You can learn more about <font SIZE="-1">XS</font> and the <font SIZE="-1">BOOT</font> section at perlxs.</p>
<dt>pp_addhdr</p>
<dd>Adds pure-C code to your <font SIZE="-1">XS</font> file. <font SIZE="-1">XS</font> files are structured such that pure C code must come before <font SIZE="-1">XS</font> specifications. This allows you to specify such C code.</p>
<dt>pp_boundscheck</p>
<dd><font SIZE="-1">PDL</font> normally checks the bounds of your accesses before making them. You can turn that on or off at runtime by setting MyPackage::set_boundscheck. This function allows you to remove that runtime flexibility and <code>never</code> do bounds checking. It also returns the current boundschecking status if called without any argumens. </p>
<p> <font SIZE="-1">NOTE: I</font> have not found anything about bounds checking in other documentation. That needs to be addressed.</dl>
<h3>Generating Perl Code</h3>
<p>Many functions imported when you use <font SIZE="-1">PDL::PP</font> allow you to modify the contents of the generated .pm file. In addition to pp_def and pp_done, the role of these functions is primarily to add code to various parts of your generated .pm file.</p>
<dl>
<dt>pp_addpm</p>
<dd>Adds Perl code to the generated .pm file. <font SIZE="-1">PDL::PP</font> actually keeps track of three different sections of generated code: the Top, the Middle, and the Bottom. You can add Perl code to the Middle section using the one-argument form, where the argument is the Perl code you want to supply. In the two-argument form, the first argument is an anonymous hash with only one key that specifies where to put the second argument, which is the string that you want to add to the .pm file. The hash is one of these three: </p>
<pre> {At =&gt; 'Top'}
 {At =&gt; 'Middle'}
 {At =&gt; 'Bot'}</pre>
<p>For example: </p>
<pre> pp_addpm({At =&gt; 'Bot'}, &lt;&lt;POD);
 
 =head1 Some documentation
 
 I know I'm typing this in the middle of my file, but it'll go at
 the bottom.
 
 =cut
 
 POD</pre>
<p>Warning: If, in the middle of your .pd file, you put documentation meant for the bottom of your pod, you will thoroughly confuse <font SIZE="-1">CPAN.</font> On the other hand, if in the middle of your .pd fil, you add some Perl code destined for the bottom or top of your .pm file, you only have yourself to confuse. :-)</p>
<dt>pp_beginwrap</p>
<dd>Adds BEGIN-block wrapping. Certain declarations can be wrapped in <font SIZE="-1">BEGIN</font> blocks, though the default behavior is to have no such wrapping.</p>
<dt>pp_addbegin</p>
<dd>Sets code to be added to the top of your .pm file, even above code that you specify with <tt>&quot;pp_addpm({At =&gt; 'Top'}, ...)&quot;</tt>. Unlike pp_addpm, calling this overwrites whatever was there before. Generally, you probably shouldn&#8217;t use it.</dl>
<h3>Tracking Line Numbers</h3>
<p>When you get compile errors, either from your C-like code or your Perl code, it can help to make those errors back to the line numbers in the source file at which the error occurred.</p>
<dl>
<dt>pp_line_numbers</p>
<dd>Takes a line number and a (usually long) string of code. The line number should indicate the line at which the quote begins. This is usually Perl&#8217;s <tt>&quot;__LINE__&quot;</tt> literal, unless you are using heredocs, in which case it is <tt>&quot;__LINE__ + 1&quot;</tt>. The returned string has #line directives interspersed to help the compiler report errors on the proper line.</dl>
<h3>Modifying the Symbol Table and Export Behavior</h3>
<p><font SIZE="-1">PDL::PP</font> usually exports all functions generated using pp_def, and usually installs them into the <font SIZE="-1">PDL</font> symbol table. However, you can modify this behavior with these functions.</p>
<dl>
<dt>pp_bless</p>
<dd>Sets the package (symbol table) to which the <font SIZE="-1">XS</font> code is added. The default is <font SIZE="-1">PDL,</font> which is generally what you want. If you use the default blessing and you create a function myfunc, then you can do the following: </p>
<pre> $piddle-&gt;myfunc(&lt;args&gt;);
 PDL::myfunc($piddle, &lt;args&gt;);</pre>
<p>On the other hand, if you bless your functions into another package, you cannot invoke them as <font SIZE="-1">PDL</font> methods, and must invoke them as: </p>
<pre> MyPackage::myfunc($piddle, &lt;args&gt;);</pre>
<p>Of course, you could always use the PMFunc key to add your function to the <font SIZE="-1">PDL</font> symbol table, but why do that?</p>
<dt>pp_add_isa</p>
<dd>Adds to the list of modules from which your <code>module</code> inherits. The default list is </p>
<pre> qw(PDL::Exporter DynaLoader)</pre>
<dt>pp_core_importlist</p>
<dd>At the top of your generated .pm file is a line that looks like this: </p>
<pre> use PDL::Core;</pre>
<p>You can modify that by specifying a string to pp_core_importlist. For example, </p>
<pre> pp_core_importlist('::Blarg');</pre>
<p>will result in </p>
<pre> use PDL::Core::Blarg;</pre>
<p>You can use this, for example, to add a list of symbols to import from PDL::Core. For example: </p>
<pre> pp_core_importlist(&quot; ':Internal'&quot;);</pre>
<p>will lead to the following use statement: </p>
<pre> use PDL::Core ':Internal';</pre>
<dt>pp_setversion</p>
<dd>Sets your module&#8217;s version. The version must be consistent between the .xs and the .pm file, and is used to ensure that your Perl&#8217;s libraries do not suffer from version skew.</p>
<dt>pp_add_exported</p>
<dd>Adds to the export list whatever names you give it. Functions created using pp_def are automatically added to the list. This function is useful if you define any Perl functions using pp_addpm or pp_addxs that you want exported as well.</p>
<dt>pp_export_nothing</p>
<dd>This resets the list of exported symbols to nothing. This is probably better called <tt>&quot;pp_export_clear&quot;</tt>, since you can add exported symbols after calling <tt>&quot;pp_export_nothing&quot;</tt>. When called just before calling pp_done, this ensures that your module does not export anything, for example, if you only want programmers to use your functions as methods.</dl>
<h2>See Also</h2>
<p><i></i><font SIZE="-1"><i>PDL</i></font><i></i> </p>
<p> For the concepts of threading and slicing check PDL::Indexing. </p>
<p> PDL::Internals </p>
<p> PDL::BadValues for information on bad values </p>
<p> <i>perlxs</i>, <i>perlxstut</i></p>
<h2>Currently Undocumented</h2>
<p>$<i>RESIZE()</i></p>
<h2>Bugs</h2>
<p>Although <font SIZE="-1">PDL::PP</font> is quite flexible and thoroughly used, there are surely bugs. First amonth them: this documentation needs a thorough revision.</p>
<h2>Author</h2>
<p>Copyright(C) 1997 Tuomas J. Lukka (lukka [at] fas.harvard.edu), Karl Glaazebrook (kgb [at] aaocbn1.aao.GOV.AU) and Christian Soeller (c.soeller [at] auckland.ac.nz). All rights reserved. Documentation updates Copyright(C) 2011 David Mertens (dcmertens.perl [at] gmail.com). This documentation is licensed under the same terms as Perl itself.</p>
<h2>Pod Errors</h2>
<p>Hey! <code>The above document had some coding errors, which are explained below:</code></p>
<dl>
<dt>Around line 350:</p>
<dd>Non-ASCII character seen before =encoding in &#8216;XrmpX&#8217;. Assuming <font SIZE="-1">UTF-8</font> </p>
</dl>
