---
title: "pdlcourse(1)"
name: "pdlcourse"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdlcourse/"
---

PDL::Course - A journey through PDL's documentation, from beginner to advanced. 

<h2>Author, Date</h2>This is written by David Mertens with edits by Daniel Carrera.
<h2>Preface</h2><font SIZE="-1">PDL</font>'s documentation is extensive. Some sections cover deep core magic while others cover more usual topics like <font SIZE="-1">IO</font> and numerical computation. How are these related? Where should you begin? 

 This document is an attempt to pull all the key <font SIZE="-1">PDL</font> documentation together in a coherent study course, starting from the beginner level, up to the expert. 

 I've broken down everything by level of expertise, and within expertise I've covered documentation, library, and workflow modules. The documentation modules are useful for what they tell you; the library modules are useful for the functions that they define for you; the workflow modules are useful for the way that they allow you to get your work done in new and different ways.
<h2>Introductory</h2>If you are new to <font SIZE="-1">PDL,</font> these documentation modules will get you started down the right path for using <font SIZE="-1">PDL.</font>
<h3>Documentation</h3>Modules that tell you how to start using <font SIZE="-1">PDL. </font> Many of these are library modules technically, but they are included when you <tt>&quot;use PDL&quot;</tt>, so I've included them for their documentation. 

 After the first three, most of the docs listed below are rather dry. Perhaps they would be better summarized by tables or better synopses. You should at least scan through them to familiarize yourself with the basic capabilities of <font SIZE="-1">PDL.</font>
<dl><dt>&bull;
<dd>PDL::Philosophy, PDL::QuickStart 

 A couple of brief introductions to <font SIZE="-1">PDL.</font> The second one is a bit more hands-on. If you are new to <font SIZE="-1">PDL,</font> you should start with these.
<dt>&bull;
<dd>PDL::Basic 

 Covers basic piddle-creation routines like <tt>&quot;sequence&quot;</tt>, <tt>&quot;rvals&quot;</tt>, and <tt>&quot;logxvals&quot;</tt> to name a random few. Also covers <tt>&quot;hist&quot;</tt> and <tt>&quot;transpose&quot;</tt>.
<dt>&bull;
<dd>PDL::Ufunc 

 Explains a large collection of built-in functions which, given an N-dimension piddle, will create a piddle with N-1 dimensions.
<dt>&bull;
<dd>PDL::NiceSlice 

 <font SIZE="-1">PDL</font> came of age right around the turn of the millennium and NiceSlice came on the scene slightly after that. Some of the docs still haven't caught up. NiceSlice is the 'modern' way to slice and dice your piddles. Read the Synopsis, then scroll down to The New Slicing Syntax. After you've read to the bottom, return to and read the stuff at the top.
<dt>&bull;
<dd>PDL::Primitive 

 Defines a whole slew of useful built-in functions. These are the sorts of things that beginners are likely to write to the list and say, ``How do I do xxx?'' You would be well on your way to learning the ropes after you've gotten through this document.
<dt>&bull;
<dd>Selections from PDL::Core 

 Like PDL::Primitive, defines a large set of useful functions. Unfortunately, some of the functions are quite esoteric, but are mixed in with the rest of the simple and easy ones. Skim the whole document, skipping over the complicated functions for now. I would point out in particular the function <tt>&quot;approx&quot;</tt>.</dl><h3>Workflow</h3><dl><dt>&bull;
<dd>The perldl or pdl2 Shell 

 The Perldl Shell is a <font SIZE="-1">REPL </font>(Read-Evaluate-Print-Loop, in other words, a prompt or shell) that allows you to work with <font SIZE="-1">PDL </font>(or any Perl, for that matter) in 'real time', loading data from files, plotting, manipulating... Anything you can do in a script, you can do in the <font SIZE="-1">PDL</font> Shell, with instant feedback!</dl><h3>Libraries</h3><dl><dt>&bull;
<dd><font SIZE="-1">PDL</font> 

 The main workhorse module. You'll include this in nearly every <font SIZE="-1">PDL</font> program you write.</dl><h2>Normal Usage</h2>The sorts of modules that you'll likely use on a normal basis in scripts or from within the perldl shell. Some of these modules you may never use, but you should still be aware that they exist, just in case you need their functionality.
<h3>Documentation</h3><dl><dt>&bull;
<dd>PDL::Slices 

 In addition to explaining the original slicing and dicing functions - for which you can usually use PDL::NiceSlice - this also covers many dimension-handling functions such as <tt>&quot;mv&quot;</tt>, <tt>&quot;xchg&quot;</tt>, and <tt>&quot;reorder&quot;</tt>. This also thoroughly documents the <tt>&quot;range&quot;</tt> function, which can be very powerful, and covers a number of internal functions, which can probably be skipped.
<dt>&bull;
<dd>PDL::Indexing 

 This covers a lot of the deeper conceptual ground that you'll need to grasp to really use <font SIZE="-1">PDL</font> to its full potential. It gets more complex as you go along, so don't be troubled if you find yourself loosing interest half way through. However, reading this document all the way through will bring you much closer to <font SIZE="-1">PDL</font> enlightenment.
<dt>&bull;
<dd><font SIZE="-1">PDL::IO</font> 

 <font SIZE="-1">PDL</font> has quite a few <font SIZE="-1">IO</font> modules, most of which are discussed in this summary module.
<dt>&bull;
<dd>PDL::Tips 

 A collection of some of Tuomas's ideas for making good use of <font SIZE="-1">PDL.</font>
<dt>&bull;
<dd>PDL::BadValues 

 Explains what bad values are and how and why they are implemented.
<dt>&bull;
<dd>Selections from Inline::Pdlpp 

 Although writing <font SIZE="-1">PDL::PP</font> code is considered an Advanced topic, and is covered in the next section, you should be aware that it is possible (and surprisingly simple) to write PDL-aware code. You needn't read the whole thing at this point, but to get some feel for how it works, you should read everything up through the first example. A copy of this documentation is contained in PDL::PP-Inline.
<dt>&bull;
<dd>PDL::Objects 

 Explains how to subclass a piddle object.
<dt>&bull;
<dd>PDL::Index 

 This was discussed in the Preface. It is an automatically generated file that lists all of the <font SIZE="-1">PDL</font> modules on your computer. There are many modules that may be on your machine but which are not documented here, such as bindings to the <font SIZE="-1">FFTW</font> library, or <font SIZE="-1">GSL.</font> Give it a read!</dl><h3>Libraries</h3><dl><dt>&bull;
<dd>PDL::Complex 

 Complex number support. No, <font SIZE="-1">PDL</font> does not have complex number support built into the core, but this should help you out.
<dt>&bull;
<dd><font SIZE="-1">PDL::FFT</font> 

 <font SIZE="-1">PDL</font>'s own Fast Fourier Transform. If you have <font SIZE="-1">FFTW,</font> then you should probably make use of it; this is <font SIZE="-1">PDL</font>'s internal implementation and should always be available.
<dt>&bull;
<dd><font SIZE="-1">GSL</font> 

 <font SIZE="-1">PDL</font> does not have bindings for every sub-library in the <font SIZE="-1">GNU</font> Scientific Library, but it has quite a few. If you have <font SIZE="-1">GSL</font> installed on your machine then chances are decent that your <font SIZE="-1">PDL</font> has the <font SIZE="-1">GSL</font> bindings. For a full list of the <font SIZE="-1">GSL</font> bindings, check PDL::Index.
<dt>&bull;
<dd>PDL::Func 

 A somewhat uniform interface to the different interpolation modules in <font SIZE="-1">PDL.</font>
<dt>&bull;
<dd>PDL::Bad 

 Includes some basic bad-value functionality, including functions to query if a piddle has bad values (<tt>&quot;isbad&quot;</tt>) and functions to set certain elements as bad (<tt>&quot;setbadat&quot;</tt> and <tt>&quot;setbadif&quot;</tt>). Among other places, bad values are used in PDL::Graphics::PLplot's xyplot to make a gap in a line plot.
<dt>&bull;
<dd>PDL::DiskCache 

 A cool module that allows you to tie a Perl array to a collection of files on your disk, which will be loaded into and out of memory as piddles. If you find yourself writing scripts to process many data files, especially if that data processing is not necessarily in sequential order, you should consider using PDL::DiskCache.
<dt>&bull;
<dd>PDL::Char 

 A <font SIZE="-1">PDL</font> subclass that allows you to store and manipulate collections of fixed-length character strings using <font SIZE="-1">PDL.</font>
<dt>&bull;
<dd>PDL::Image2D 

 A whole collection of methods for manipulating images whose image data are stored in a piddle. These include methods for convolutions (smoothing), polygon fills, scaling, rotation, and warping, among others.
<dt>&bull;
<dd>PDL::ImageND 

 Contains a few functions that are conceptually related to image processing, but which can be defined for higher-dimensional data. For examples this module defines high-dimensional convolution and interpolation, among others.
<dt>&bull;
<dd>PDL::ImageRGB 

 Defines some useful functions for working with <font SIZE="-1">RBG</font> image data. It's not very feature-full, but it may have something you need, and if not, you can always add more!
<dt>&bull;
<dd>PDL::Transform 

 Creates the transform class, which allows you to create various coordinate transforms. For example, if you data is a collection of Cartesian coordinates, you could create a transform object to convert them to Spherical-Polar coordinates (although many such standard coordinate transformations are predefined for you, in this case it's called <tt>&quot;t_spherical&quot;</tt>).
<dt>&bull;
<dd>PDL::Opt::Simplex 

 This package states that it ``implements the commonly used simplex optimization algorithm.'' I'm going to assume that if you need this algorithm then you already know what it is.
<dt>&bull;
<dd>PDL::Math 

 A collection of fairly standard math functions, like the inverse trigonometric functions, hyperbolic functions and their inverses, and others. This module is included in the standard call to <tt>&quot;use PDL&quot;</tt>, but not in the Lite versions.
<dt>&bull;
<dd>PDL::Matrix 

 Provides a few functions that use the standard mathematical Matrix notation of row-column indexing rather than the PDL-standard column-row. It appears that this module has not been heavily tested with other modules, so although it should work with other modules, don't be surprised if something breaks when you use it (and feel free to offer any fixes that you may develop).
<dt>&bull;
<dd>PDL::MatrixOps 

 Provides many standard matrix operations for piddles, such as computing eigenvalues, inverting square matrices, LU-decomposition, and solving a system of linear equations. Though it is not built on PDL::Matrix, it should generally work with that module. Also, the methods provided by this module do not depend on external libraries such as Slatec or <font SIZE="-1">GSL.</font>
<dt>&bull;
<dd>PDL::Reduce 

 Implements an interface to all the functions that return piddles with one less dimension (for example, <tt>&quot;sumover&quot;</tt>), such that they can be called by suppling their name, as a string.</dl><h3>Workflow</h3><dl><dt>&bull;
<dd>PDL::AutoLoader 

 Enables Matlab-style autoloading. When you call an unknown function, instead of complaining and croaking, <font SIZE="-1">PDL</font> will go hunt around in the directories you specify in search of a like-named file. Particularly useful when used with the Perldl Shell.
<dt>&bull;
<dd>PDL::Dbg 

 Declares the <tt>&quot;px&quot;</tt> function, which can be handy for debugging your <font SIZE="-1">PDL</font> scripts and/or perldl shell commands.
<dt>&bull;
<dd>PDL::Options 

 Suppose you define a powerful, versatile function. Chances are good that you'll accept the arguments in the form of a hash or hashref. Now you face the problem of processing that hashref. PDL::Options assists you in writing code to process those options. (You'd think Perl would have tons of these sorts of modules lying around, but I couldn't find any.) Note this module does not depend on <font SIZE="-1">PDL</font> for its usage or installation.
<dt>&bull;
<dd>PDL::pdldoc 

 Ever fired-up the perldl shell just to look up the help for a particular function? You can use <tt>&quot;pdldoc&quot;</tt> instead. This shell script extracts information from the help index without needing to start the perldl shell.</dl><h2>Advanced Usage</h2>The sorts of modules and documentation that you'll use if you write modules that use <font SIZE="-1">PDL,</font> or if you work on <font SIZE="-1">PDL</font> maintenance. These modules can be difficult to use, but enable you to tackle some of your harder problems.
<dl><dt>&bull;
<dd>PDL::Lite, PDL::LiteF 

 Lite-weight replacements for <tt>&quot;use PDL&quot;</tt>, from the standpoint of namespace pollution and load time.
<dt>&bull;
<dd>Inline::Pdlpp 

 This was mentioned earlier. Before you begin reading about <font SIZE="-1">PDL::PP</font> (next), you should remind yourself about how to use this. Inline::Pdlpp will help you experiment with <font SIZE="-1">PDL::PP</font> without having to go through the trouble of building a module and constructing makefiles (but see PDL::pptemplate for help on that).
<dt>&bull;
<dd><font SIZE="-1">PDL::PP</font> 

 The <font SIZE="-1">PDL</font> Pre-Processor, which vastly simplifies making you C or Fortran code play with Perl and piddles. Most of <font SIZE="-1">PDL</font>'s basic functionality is written using <font SIZE="-1">PDL::PP,</font> so if you're thinking about how you might integrate some numerical library written in C, look no further.
<dt>&bull;
<dd>PDL::pptemplate 

 A script that automates the creation of modules that use <font SIZE="-1">PDL::PP</font>, which should make your life as a module author a bit simpler.
<dt>&bull;
<dd>PDL::CallExt 

 Allows you to call functions using external shared libraries. This is an alternative to using <font SIZE="-1">PDL::PP</font>. The major difference between <font SIZE="-1">PDL::PP</font> and PDL::CallExt is that the former will handle threading over implicit thread dimensions for you, whereas PDL::CallExt simply calls an external function. <font SIZE="-1">PDL::PP</font> is generally the recommended way to interface your code with <font SIZE="-1">PDL,</font> but it wouldn't be Perl if there wasn't another way to do it.
<dt>&bull;
<dd>PDL::Config 

 Defines the <tt>%PDL::Config</tt> hash, which has lots of useful information pertinent to your <font SIZE="-1">PDL</font> build.
<dt>&bull;
<dd>PDL::Doc 

 Explanation of the <font SIZE="-1">PDL</font> documentation conventions, and an interface to the <font SIZE="-1">PDL</font> Documentation parser. Following these guidelines when writing documentation for <font SIZE="-1">PDL</font> functions will ensure that your wonderful documentation is accessible from the perldl shell and from calls to <tt>&quot;barf&quot;</tt>. (Did you notice that <tt>&quot;barf&quot;</tt> used your documentation? Time to reread PDL::Core...)
<dt>&bull;
<dd>PDL::Exporter 

 A simple replacement for the standard Exporter module. The only major difference is that the default imported modules are those marked ':Func'.
<dt>&bull;
<dd>PDL::Types 

 Defines some useful functions for getting a piddle's type, as well as getting information about that type.
<dt>&bull;
<dd>PDL::Version 

 Simply defines the scalar <tt>$PDL::Version::Version</tt> with the current version of <font SIZE="-1">PDL,</font> as defined in <font SIZE="-1">PDL</font>.pm. This is most useful if you distribute your own module on <font SIZE="-1">CPAN,</font> use PDL::Lite or PDL::LiteF and want to make sure that your users have a recent-enough version of <font SIZE="-1">PDL. </font> Since the variable is defined in <font SIZE="-1">PDL</font>.pm, you don't need this module if you <tt>&quot;use PDL&quot;</tt>.</dl><h2>Expert Usage</h2><dl><dt>&bull;
<dd>PDL::Core::Dev 

 Provides some decently useful functions that are pretty much only needed by the <font SIZE="-1">PDL</font> Porters.
<dt>&bull;
<dd><font SIZE="-1">PDL::API</font> 

 Explains how to make a piddle <i>by hand</i>, from Perl or your C source code, using the <font SIZE="-1">PDL API.</font>
<dt>&bull;
<dd>PDL::Internals 

 Explains the nitty-gritty of the <font SIZE="-1">PDL</font> data structures. After reading this (a few times :), you should be able to create a piddle completely from scratch (i.e. without using the <font SIZE="-1">PDL API</font>). Put a little differently, if you want to understand how <font SIZE="-1">PDL::PP</font> works, you'll need to read this.</dl><h2>Copyright</h2>Copyright 2010 David Mertens (dcmertens.perl [at] gmail.com). You can distribute and/or modify this document under the same terms as the current Perl license. 

 See: <a rel="nofollow" HREF="http://dev.perl.org/licenses/">http://dev.perl.org/licenses/</a>
