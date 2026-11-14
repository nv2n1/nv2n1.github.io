---
title: "pdlquickstart(1)"
name: "pdlquickstart"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdlquickstart/"
description: "PDL::QuickStart – Quick introduction to PDL features."
---

<p>PDL::QuickStart &#8211; Quick introduction to PDL features. </p>
<h2>Synopsis</h2>
<p>A brief summary of the main <font SIZE="-1">PDL</font> features and how to use them.</p>
<h2>Description</h2>
<h3>Introduction</h3>
<p>Perl is an extremely good and versatile scripting language, well suited to beginners and allows rapid prototyping. However until recently it did not support data structures which allowed it to do fast number crunching. </p>
<p> However with the development of Perl v5, Perl acquired &#8216;Objects&#8217;. To put it simply users can define their own special data types, and write custom routines to manipulate them either in low level languages (C and Fortran) or in Perl itself. </p>
<p> This has been fully exploited by the PerlDL developers. The &#8216;<font SIZE="-1">PDL</font>&#8216; module is a complete Object-Oriented extension to Perl (although you don&#8217;t have to know what an object is to use it) which allows large N-dimensional data sets, such as large images, spectra, time series, etc to be stored <code>efficiently</code> and manipulated <code>en masse</code>. For example with the <font SIZE="-1">PDL</font> module we can write the Perl code <tt>&quot;$a = $b + $c&quot;</tt>, where <tt>$b</tt> and <tt>$c</tt> are large datasets (e.g. 2048&#215;2048 images), and get the result in only a fraction of a second. </p>
<p> <font SIZE="-1">PDL</font> variables (or &#8216;piddles&#8217; as they have come to be known) support a wide range of fundamental data types &#8211; arrays can be bytes, short integers (signed or unsigned), long integers, floats or double precision floats. And because of the Object-Oriented nature of <font SIZE="-1">PDL</font> new customised datatypes can be derived from them. </p>
<p> As well as the <font SIZE="-1">PDL</font> modules, that can be used by normal Perl programs, PerlDL comes with a command line Perl shell, called &#8216;perldl&#8217;, which supports command line editing. In combination with the various <font SIZE="-1">PDL</font> graphics modules this allows data to be easily played with and visualised.</p>
<h3>Help</h3>
<p><font SIZE="-1">PDL</font> contains extensive documentation, available both within the <i>perldl</i> or <i>pdl2</i> shells and from the command line, using the <tt>&quot;pdldoc&quot;</tt> program. For further information try either of: </p>
<pre> pdl&gt; help help
 $ pdldoc</pre>
<p><font SIZE="-1">HTML</font> copies of the documentation should also be available. To find their location, try the following: </p>
<pre> pdl&gt; foreach ( map{&quot;$_/PDL/HtmlDocs&quot;}@INC ) { p &quot;$_
&quot; if -d $_ }</pre>
<h3>Perl Datatypes and how <font SIZE="-1">PDL</font> extends them</h3>
<p>The fundamental Perl data structures are scalar variables, e.g. <tt>$x</tt>, which can hold numbers or strings, lists or arrays of scalars, e.g. <tt>@x</tt>, and associative arrays/hashes of scalars, e.g. <tt>%x</tt>. </p>
<p> Perl v5 introduces to Perl data structures and objects. A simple scalar variable <tt>$x</tt> now be a user-defined data type or full blown object (it actually holds a reference (a smart &#8220;pointer&#8221;) to this but that is not relevant for ordinary use of perlDL) </p>
<p> The fundamental idea behind perlDL is to allow <tt>$x</tt> to hold a whole 1D spectrum, or a 2D image, a 3D data cube, and so on up to large N-dimensional data sets. These can be manipulated all at once, e.g. <tt>&quot;$a = $b + 2&quot;</tt> does a vector operation on each value in the spectrum/image/etc. </p>
<p> You may well ask: &quot;Why not just store a spectrum as a simple Perl <tt>@x</tt> style list with each pixel being a list item?&quot; The two key answers to this are <i>memory</i> and <i>speed</i>. Because we know our spectrum consists of pure numbers we can compactly store them in a single block of memory corresponding to a C style numeric array. This takes up a <font SIZE="-1">LOT</font> less memory than the equivalent Perl list. It is then easy to pass this block of memory to a fast addition routine, or to any other C function which deals with arrays. As a result perlDL is very fast &#8212; for example one can multiply a 2048*2048 image in exactly the same time as it would take in C or <font SIZE="-1">FORTRAN </font>(0.1 sec on my <font SIZE="-1">SPARC</font>). A further advantage of this is that for simple operations (e.g. <tt>&quot;$x += 2&quot;</tt>) one can manipulate the whole array without caring about its dimensionality. </p>
<p> I find when using perlDL it is most useful to think of standard Perl <tt>@x</tt> variables as &#8220;lists&#8221; of generic &#8220;things&#8221; and <font SIZE="-1">PDL</font> variables like <tt>$x</tt> as &#8220;arrays&#8221; which can be contained in lists or hashes. Quite often in my perlDL scripts I have <tt>@x</tt> contain a list of spectra, or a list of images (or even a mix!). Or perhaps one could have a hash (e.g. <tt>%x</tt>) of images&#8230; the only limit is memory! </p>
<p> perlDL variables support a range of data types &#8211; arrays can be bytes, short integers (signed or unsigned), long integers, floats or double precision floats.</p>
<h3>Usage</h3>
<p>PerlDL is loaded into your Perl script using this command: </p>
<pre> use PDL; # in Perl scripts: use the standard perlDL modules</pre>
<p>There are also a lot of extension modules, e.g. PDL::Graphics::TriD. Most of these (but not all as sometimes it is not appropriate) follow a standard convention. If you say: </p>
<pre> use PDL::Graphics::TriD;</pre>
<p>You import everything in a standard list from the module. Sometimes you might want to import nothing (e.g. if you want to use <font SIZE="-1">OO</font> syntax all the time and save the import tax). For these you say: </p>
<pre> use PDL::Graphics::TriD qw();</pre>
<p>And the empty <tt>&quot;qw()&quot;</tt> quotes are recognised as meaning &#8216;nothing&#8217;. You can also specify a list of functions to import in the normal Perl way. </p>
<p> There is also an interactive shell, <tt>&quot;perldl&quot;</tt> or <tt>&quot;pdl2&quot;</tt>, see <i>perldl</i> or pdl2 for details.</p>
<h3>To create a new <font SIZE="-1">PDL</font> variable</h3>
<p>Here are some ways of creating a <font SIZE="-1">PDL</font> variable: </p>
<pre> $a = pdl [1..10]; # 1D array
 $a = pdl (1,2,3,4); # Ditto
 $a = pdl '[1 2 3 4]'; # Ditto
 $b = pdl [[1,2,3],[4,5,6]]; # 2D 3x2 array
 $b = pdl '[1 2 3; 4 5 6]'; # Ditto
 $b = pdl q[1,2,3; 4,5,6]; # Ditto
 $b = pdl &lt;&lt;NEWPDL # Ditto
 [1 2 3]
 [4 5 6]
 NEWPDL
 $c = pdl q[1 -2]; # 2-element piddle containing 1 and -2
 $c = pdl q[1 - 2]; # 2-element piddle containing 1 and -2
 $b = pdl 42 # 0-dimensional scalar
 $c = pdl $a; # Make a new copy
 
 $d = byte [1..10]; # See &quot;Type conversion&quot;
 $e = zeroes(3,2,4); # 3x2x4 zero-filled array
 
 $c = rfits $file; # Read FITS file
 
 @x = ( pdl(42), zeroes(3,2,4), rfits($file) ); # Is a LIST of PDL variables!</pre>
<p>The <i>pdl()</i> function is used to initialise a <font SIZE="-1">PDL</font> variable from a scalar, list, list reference, another <font SIZE="-1">PDL</font> variable, or a properly formatted string. </p>
<p> In addition all <font SIZE="-1">PDL</font> functions automatically convert normal Perl scalars to <font SIZE="-1">PDL</font> variables on-the-fly. </p>
<p> (also see &#8220;Type Conversion&#8221; and &#8220;Input/Output&#8221; sections below)</p>
<h3>Arithmetic (and boolean expressions)</h3>
<pre> $a = $b + 2; $a++; $a = $b / $c; # Etc.
 $c=sqrt($a); $d = log10($b+100); # Etc
 $e = $a&gt;42; # Vector conditional
 $e = 42*($a&gt;42) + $a*($a&lt;=42); # Cap top
 $b = $a-&gt;log10 unless any ($a &lt;= 0); # avoid floating point error
 $a = $a / ( max($a) - min($a) );
 $f = where($a, $a &gt; 10); # where returns a piddle of elements for
 # which the condition is true
 print $a; # $a in string context prints it in a N-dimensional format</pre>
<p>(and other Perl operators/functions) </p>
<p> When using piddles in conditional expressions (i.e. <tt>&quot;if&quot;</tt>, <tt>&quot;unless&quot;</tt> and <tt>&quot;while&quot;</tt> constructs) only piddles with exactly one element are allowed, e.g. </p>
<pre> $a = pdl (1,0,0,1);
 print &quot;is set&quot; if $a-&gt;<a href="//www.systutorials.com/docs/linux/man/2-index/">index</a>(2);</pre>
<p>Note that the boolean operators return in general multi-element piddles. Therefore, the following will raise an error </p>
<pre> print &quot;is ok&quot; if $a &gt; 3;</pre>
<p>since <tt>&quot;$a &gt; 3&quot;</tt> is a piddle with 4 elements. Rather use all or any to test if all or any of the elements fulfill the condition: </p>
<pre> print &quot;some are &gt; 3&quot; if any $a&gt;3;
 print &quot;can't take logarithm&quot; unless all $a&gt;0;</pre>
<p>There are also many predefined functions, which are described on other man pages. Check PDL::Index.</p>
<h3>Matrix functions</h3>
<p><tt>'x'</tt> is hijacked as the matrix multiplication operator. e.g. <tt>&quot;$c = $a x $b&quot;</tt>; </p>
<p> perlDL is row-major not column major so this is actually <tt>&quot;c(i,j) = sum_k a(k,j) b(i,k)&quot;</tt> &#8211; but when matrices are printed the results will look right. Just remember the indices are reversed. e.g.: </p>
<pre> $a = [ $b = [
 [ 1 2 3 0] [1 1]
 [ 1 -1 2 7] [0 2]
 [ 1 0 0 1] [0 2]
 ] [1 1]
 ]
 gives $c = [
 [ 1 11]
 [ 8 10]
 [ 2 2]
 ]</pre>
<p>Note: <i>transpose()</i> does what it says and is a convenient way to turn row vectors into column vectors.</p>
<h3>How to write a simple function</h3>
<pre> sub dotproduct {
 my ($a,$b) = @_;
 return sum($a*$b) ;
 }
 1;</pre>
<p>If put in file dotproduct.pdl would be autoloaded if you are using PDL::AutoLoader (see below). </p>
<p> Of course, this function is already available as the inner function, see PDL::Primitive.</p>
<h3>Type Conversion</h3>
<p>Default for <i>pdl()</i> is double. Conversions are: </p>
<pre> $a = float($b);
 $c = long($d); # &quot;long&quot; is generally a 4 byte int
 $d = byte($a);</pre>
<p>Also <i>double()</i>, <i>short()</i>, <i>ushort()</i>, <i>indx()</i>. </p>
<pre> NOTE: The indx() routine is a special integer type that
 is the correct size for a PDL index value (dimension size,
 index, or offest) which can be either a 32bit (long) or
 64bit (longlong) quantity depending on whether the perl
 is built with 32bit or 64bit support.</pre>
<p>These routines also automatically convert Perl lists to allow the convenient shorthand: </p>
<pre> $a = byte [[1..10],[1..10]]; # Create 2D byte array
 $a = float [1..1000]; # Create 1D float array</pre>
<p>etc.</p>
<h3>Printing</h3>
<p>Automatically expands array in N-dimensional format: </p>
<pre> print $a;
 $b = &quot;Answer is = $a &quot;;</pre>
<h3>Sections</h3>
<p><font SIZE="-1">PDL</font> has very powerful multidimensional slicing and sectioning operators; see the <i><a href="/docs/linux/man/3-pdl--slices/">PDL::Slices</a></i>(3) man page for details; we&#8217;ll describe the most important one here. </p>
<p> <font SIZE="-1">PDL</font> shows its Perl/C heritage in that arrays are zero-offset. Thus a 100&#215;100 image has indices <tt>&quot;0..99,0..99&quot;</tt>. (The convention is that the <i>center</i> of pixel (0,0) is at coordinate (0.0,0.0). All <font SIZE="-1">PDL</font> graphics functions conform to this definition and hide away the unit offsets of, for example, the <font SIZE="-1">PGPLOT FORTRAN</font> library. </p>
<p> Following the usual convention coordinate (0,0) is displayed at the bottom left when displaying an image. It appears at the top left when using &quot;<tt>&quot;print $a&quot;</tt>&quot; etc. </p>
<p> Simple sectioning uses a syntax extension to Perl, PDL::NiceSlice, that allows you to specify subranges via a null-method modifier to a <font SIZE="-1">PDL:</font> </p>
<pre> $b = $a-&gt;($x1:$x2,$y1:$y2,($z1)); # Take subsection</pre>
<p>Here, <tt>$a</tt> is a 3-dimensional variable, and <tt>$b</tt> gets a planar cutout that is defined by the limits <tt>$x1</tt>, <tt>$x2</tt>, <tt>$y1</tt>, <tt>$y2</tt>, at the location <tt>$z1</tt>. The parenthesis around <tt>$z1</tt> cause the trivial index to be omitted &#8212; otherwise <tt>$b</tt> would be three-dimensional with a third dimension of order 1. </p>
<p> You can put <font SIZE="-1">PDL</font> slices on either side of the element-wise assignment operator <tt>&quot;.=&quot;</tt>, like so: </p>
<pre> # Set part of $bigimage to values from $smallimage
 $bigimage-&gt;($xa:$xb,$ya:$yb) .= $smallimage;</pre>
<p>Some other miscellany: </p>
<pre> $c = nelem($a); # Number of pixels
 $val = at($object, $x,$y,$z...) # Pixel value at position, as a Perl scalar
 $val = $object-&gt;at($x,$y,$z...) # equivalent (method syntax OK)
 $b = xvals($a); # Fill array with X-coord values (also yvals(), zvals(),
 # axisvals($x,$axis) and rvals() for radial distance
 # from centre).</pre>
<h3>Input/Output</h3>
<p>The <tt>&quot;PDL::IO&quot;</tt> modules implement several useful <font SIZE="-1">IO</font> format functions. It would be too much to give examples of each, but you can find a nice overview at <font SIZE="-1">PDL::IO</font>. Here is a sample of some of the supported <font SIZE="-1">IO</font> formats in <font SIZE="-1">PDL.</font></p>
<dl>
<dt>PDL::IO::Misc</p>
<dd>Ascii, <font SIZE="-1">FITS</font> and <font SIZE="-1">FIGARO/NDF IO</font> routines.</p>
<dt>PDL::IO::FastRaw</p>
<dd>Using the raw data types of your machine, an unportable but blindingly fast <font SIZE="-1">IO</font> format. Also supports memory mapping to conserve memory as well as get more speed.</p>
<dt>PDL::IO::FlexRaw</p>
<dd>General raw data formats. Like FastRaw, only better.</p>
<dt>PDL::IO::Browser</p>
<dd>A Curses browser for arrays.</p>
<dt>PDL::IO::Pnm</p>
<dd>Portaple bitmap and pixmap support.</p>
<dt>PDL::IO::Pic</p>
<dd>Using the previous module and netpbm, makes it possible to easily write <font SIZE="-1">GIF,</font> jpeg and whatever with simple commands.</dl>
<h3>Graphics</h3>
<p>The philosophy behind perlDL is to make it work with a variety of existing graphics libraries since no single package will satisfy all needs and all people and this allows one to work with packages one already knows and likes. Obviously there will be some overlaps in functionality and some lack of consistency and uniformity. However this allows <font SIZE="-1">PDL</font> to keep up with a rapidly developing field &#8211; the latest <font SIZE="-1">PDL</font> modules provide interfaces to OpenGL and <font SIZE="-1">VRML</font> graphics!</p>
<dl>
<dt>PDL::Graphics::PGPLOT</p>
<dd><font SIZE="-1">PGPLOT</font> provides a simple library for line graphics and image display. </p>
<p> There is an easy interface to this in the internal module PDL::Graphics::PGPLOT, which calls routines in the separately available <font SIZE="-1">PGPLOT</font> top-level module.</p>
<dt>PDL::Graphics::PLplot</p>
<dd>PLplot provides a simple library for creating graphics with multiple output drivers, including a direct-to-piddle driver. </p>
<p> This module provides both high-level and low-level functionality built on PLplot. The low-level commands are pretty much direct bindings to PLplot&#8217;s C interface. Read more at PDL::Graphics::PLplot.</p>
<dt>PDL::Graphics::IIS</p>
<dd>Many astronomers like to use SAOimage and Ximtool (or there derivations/clones). These are useful free widgets for inspection and visualisation of images. (They are not provided with perlDL but can easily be obtained from their official sites off the Net.) </p>
<p> The PDL::Graphics::IIS package provides allows one to display images in these (&#8220;<font SIZE="-1">IIS&#8221;</font> is the name of an ancient item of image display hardware whose protocols these tools conform to.)</p>
<dt>PDL::Graphics::TriD</p>
<dd>See PDL::Graphics::TriD, this is a collection of 3D routines for OpenGL and (soon) <font SIZE="-1">VRML</font> and other 3D formats which allow 3D point, line, and surface plots from <font SIZE="-1">PDL.</font></dl>
<h3>Autoloading</h3>
<p>See PDL::AutoLoader. This allows one to autoload functions on demand, in a way perhaps familiar to users of MatLab. </p>
<p> One can also write <font SIZE="-1">PDL</font> extensions as normal Perl modules.</p>
<h3><font SIZE="-1">PDL</font> shells</h3>
<p>The Perl script <tt>&quot;pdl2&quot;</tt> (or <tt>&quot;perldl&quot;</tt>) provides a simple command line interface to <font SIZE="-1">PDL. </font> If the latest Readlines/ReadKey modules have been installed <tt>&quot;pdl2&quot;</tt> detects this and enables command line recall and editing. See the man page for details. </p>
<p> e.g.: </p>
<pre> % perldl
 perlDL shell v1.354
 PDL comes with ABSOLUTELY NO WARRANTY. For details, see the file
 'COPYING' in the PDL distribution. This is free software and you
 are welcome to redistribute it under certain conditions, see
 the same file for details.
 ReadLines, NiceSlice, MultiLines enabled
 Reading PDL/default.perldlrc...
 Found docs database /home/pdl/dev/lib/perl5/site_perl/PDL/pdldoc.db
 Type 'help' for online help
 Type 'demo' for online demos
 Loaded PDL v2.4.9_003 (supports bad values)
 pdl&gt; $x = rfits 'm51.fits'
 Reading IMAGE data...
 BITPIX = 32 size = 147456 pixels 
 Reading 589824 bytes
 BSCALE = &amp;&amp; BZERO = 
 pdl&gt; use PDL::Graphics::PGPLOT;
 pdl&gt; imag $x
 Displaying 384 x 384 image from 40 to 761, using 84 colors (16-99)...</pre>
<p>You can also run it from the Perl debugger (<tt>&quot;perl -MPDL -d -e 1&quot;</tt>) if you want. </p>
<p> Miscellaneous shell features:</p>
<dl>
<dt>p</p>
<dd>The shell aliases <tt>&quot;p&quot;</tt> to be a convenient short form of <tt>&quot;print&quot;</tt>, e.g. </p>
<pre> pdl&gt; p ones 5,3
 [
 [1 1 1 1 1]
 [1 1 1 1 1]
 [1 1 1 1 1]
 ]</pre>
<dt>Initialization</p>
<dd>The files <tt>&quot;~/.perldlrc&quot;</tt> and <tt>&quot;local.perldlrc&quot;</tt> (in the current directory) are sourced if found. This allows the user to have global and local <font SIZE="-1">PDL</font> code for startup.</p>
<dt>Help</p>
<dd>Type &#8216;help&#8217;! One can search the <font SIZE="-1">PDL</font> documentation, and look up documentation on any function.</p>
<dt>Escape</p>
<dd>Any line starting with the <tt>&quot;#&quot;</tt> character is treated as a shell escape. This character is configurable by setting the Perl variable <tt>$PERLDL_ESCAPE</tt>. This could, for example, be set in <tt>&quot;~/.perldlrc&quot;</tt>.</dl>
<h3>Overload operators</h3>
<p>The following builtin Perl operators and functions have been overloaded to work on <font SIZE="-1">PDL</font> variables: </p>
<pre> + - * / &gt; &lt; &gt;= &lt;= &lt;&lt; &gt;&gt; &amp; | ^ == != &lt;=&gt; ** % ! ~
 sin log abs atan2 sqrt cos exp</pre>
<p>[All the unary functions (sin etc.) may be used with <i>inplace()</i> &#8211; see &#8220;Memory&#8221; below.]</p>
<h3>Object-Orientation and perlDL</h3>
<p><font SIZE="-1">PDL</font> operations are available as functions and methods. Thus one can derive new types of object, to represent custom data classes. </p>
<p> By using overloading one can make mathematical operators do whatever you please, and <font SIZE="-1">PDL</font> has some built-in tricks which allow existing <font SIZE="-1">PDL</font> functions to work unchanged, even if the underlying data representation is vastly changed! See PDL::Objects</p>
<h3>Memory usage and references</h3>
<p>Messing around with really huge data arrays may require some care. perlDL provides many facilities to let you perform operations on big arrays without generating extra copies though this does require a bit more thought and care from the programmer. </p>
<p> <font SIZE="-1">NOTE:</font> On some most systems it is better to configure Perl (during the build options) to use the system <tt>&quot;malloc()&quot;</tt> function rather than Perl&#8217;s built-in one. This is because Perl&#8217;s one is optimised for speed rather than consumption of virtual memory &#8211; this can result in a factor of two improvement in the amount of memory storage you can use. The Perl malloc in 5.004 and later does have a number of compile-time options you can use to tune the behaviour.</p>
<dl>
<dt>Simple arithmetic</p>
<dd>If <tt>$a</tt> is a big image (e.g. occupying 10MB) then the command </p>
<pre> $a = $a + 1;</pre>
<p>eats up another 10MB of memory. This is because the expression <tt>&quot;$a+1&quot;</tt> creates a temporary copy of <tt>$a</tt> to hold the result, then <tt>$a</tt> is assigned a reference to that. After this, the original <tt>$a</tt> is destroyed so there is no <i>permanent</i> memory waste. But on a small machine, the growth in the memory footprint can be considerable. It is obviously done this way so <tt>&quot;$c=$a+1&quot;</tt> works as expected. </p>
<p> Also if one says: </p>
<pre> $b = $a; # $b and $a now point to same data
 $a = $a + 1;</pre>
<p>Then <tt>$b</tt> and <tt>$a</tt> end up being different, as one naively expects, because a new reference is created and <tt>$a</tt> is assigned to it. </p>
<p> However if <tt>$a</tt> was a huge memory hog (e.g. a 3D volume) creating a copy of it may not be a good thing. One can avoid this memory overhead in the above example by saying: </p>
<pre> $a++;</pre>
<p>The operations <tt>&quot;++,+=,--,-=&quot;</tt>, etc. all call a special &#8220;in-place&#8221; version of the arithmetic subroutine. This means no more memory is needed &#8211; the downside of this is that if <tt>&quot;$b=$a&quot;</tt> then <tt>$b</tt> is also incremented. To force a copy explicitly: </p>
<pre> $b = pdl $a; # Real copy</pre>
<p>or, alternatively, perhaps better style: </p>
<pre> $b = $a-&gt;copy;</pre>
<dt>Functions</p>
<dd>Most functions, e.g. <tt>&quot;log()&quot;</tt>, return a result which is a transformation of their argument. This makes for good programming practice. However many operations can be done &#8220;in-place&#8221; and this may be required when large arrays are in use and memory is at a premium. For these circumstances the operator <i>inplace()</i> is provided which prevents the extra copy and allows the argument to be modified. e.g.: </p>
<pre> $x = log($array); # $array unaffected
 log( inplace($bigarray) ); # $bigarray changed in situ</pre>
<p><font SIZE="-1">WARNINGS:</font></p>
<dl>
<dd>
<dl>
<dt>1.</p>
<dd>The usual caveats about duplicate references apply.</p>
<dt>2.</p>
<dd>Obviously when used with some functions which can not be applied in situ (e.g. <tt>&quot;convolve()&quot;</tt>) unexpected effects may occur! We try to indicate <tt>&quot;inplace()&quot;</tt>-safe functions in the documentation.</p>
<dt>3.</p>
<dd>Type conversions, such as<tt>&quot;float()&quot;</tt>, may cause hidden copying.</dl>
</dl>
<dl>
<dd></dl>
</dl>
<h3>Ensuring piddleness</h3>
<p>If you have written a simple function and you don&#8217;t want it to blow up in your face if you pass it a simple number rather than a <font SIZE="-1">PDL</font> variable. Simply call the function <i>topdl()</i> first to make it safe. e.g.: </p>
<pre> sub myfiddle { my $pdl = topdl(shift); $pdl-&gt;fiddle_foo(...); ... }</pre>
<p><tt>&quot;topdl()&quot;</tt> does <font SIZE="-1">NOT</font> perform a copy if a pdl variable is passed &#8211; it just falls through &#8211; which is obviously the desired behaviour. The routine is not of course necessary in normal user defined functions which do not care about internals.</p>
<h2>Author</h2>
<p>Copyright (C) Karl Glazebrook (kgb [at] aaoepp.aao.gov.au), Tuomas J. Lukka, (lukka [at] husc.harvard.edu) and Christian Soeller (c.soeller [at] auckland.ac.nz) 1997. Commercial reproduction of this documentation in a different format is forbidden.</p>
