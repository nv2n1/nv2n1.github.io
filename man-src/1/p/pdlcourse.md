---
title: "pdlcourse(1)"
name: "pdlcourse"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdlcourse/"
---

PDL::Course - A journey through PDL's documentation, from beginner to advanced. 

<h2>Author, Date</h2>This is written by David Mertens with edits by Daniel Carrera.
<h2>Preface</h2>PDL's documentation is extensive. Some sections cover deep core magic while others cover more usual topics like IO and numerical computation. How are these related? Where should you begin? 

 This document is an attempt to pull all the key PDL documentation together in a coherent study course, starting from the beginner level, up to the expert. 

 I've broken down everything by level of expertise, and within expertise I've covered documentation, library, and workflow modules. The documentation modules are useful for what they tell you; the library modules are useful for the functions that they define for you; the workflow modules are useful for the way that they allow you to get your work done in new and different ways.
<h2>Introductory</h2>If you are new to PDL, these documentation modules will get you started down the right path for using PDL.
<h3>Documentation</h3>Modules that tell you how to start using PDL.  Many of these are library modules technically, but they are included when you <tt>&quot;use PDL&quot;</tt>, so I've included them for their documentation. 

 After the first three, most of the docs listed below are rather dry. Perhaps they would be better summarized by tables or better synopses. You should at least scan through them to familiarize yourself with the basic capabilities of PDL.
<dl><dt>&bull;
</dt><dd>PDL::Philosophy, PDL::QuickStart 
 A couple of brief introductions to PDL. The second one is a bit more hands-on. If you are new to PDL, you should start with these.
</dd><dt>&bull;
</dt><dd>PDL::Basic 
 Covers basic piddle-creation routines like <tt>&quot;sequence&quot;</tt>, <tt>&quot;rvals&quot;</tt>, and <tt>&quot;logxvals&quot;</tt> to name a random few. Also covers <tt>&quot;hist&quot;</tt> and <tt>&quot;transpose&quot;</tt>.
</dd><dt>&bull;
</dt><dd>PDL::Ufunc 
 Explains a large collection of built-in functions which, given an N-dimension piddle, will create a piddle with N-1 dimensions.
</dd><dt>&bull;
</dt><dd>PDL::NiceSlice 
 PDL came of age right around the turn of the millennium and NiceSlice came on the scene slightly after that. Some of the docs still haven't caught up. NiceSlice is the 'modern' way to slice and dice your piddles. Read the Synopsis, then scroll down to The New Slicing Syntax. After you've read to the bottom, return to and read the stuff at the top.
</dd><dt>&bull;
</dt><dd>PDL::Primitive 
 Defines a whole slew of useful built-in functions. These are the sorts of things that beginners are likely to write to the list and say, ``How do I do xxx?'' You would be well on your way to learning the ropes after you've gotten through this document.
</dd><dt>&bull;
</dt><dd>Selections from PDL::Core 
 Like PDL::Primitive, defines a large set of useful functions. Unfortunately, some of the functions are quite esoteric, but are mixed in with the rest of the simple and easy ones. Skim the whole document, skipping over the complicated functions for now. I would point out in particular the function <tt>&quot;approx&quot;</tt>.</dd></dl><h3>Workflow</h3><dl><dt>&bull;
</dt><dd>The perldl or pdl2 Shell 
 The Perldl Shell is a REPL (Read-Evaluate-Print-Loop, in other words, a prompt or shell) that allows you to work with PDL (or any Perl, for that matter) in 'real time', loading data from files, plotting, manipulating... Anything you can do in a script, you can do in the PDL Shell, with instant feedback!</dd></dl><h3>Libraries</h3><dl><dt>&bull;
</dt><dd>PDL 
 The main workhorse module. You'll include this in nearly every PDL program you write.</dd></dl><h2>Normal Usage</h2>The sorts of modules that you'll likely use on a normal basis in scripts or from within the perldl shell. Some of these modules you may never use, but you should still be aware that they exist, just in case you need their functionality.
<h3>Documentation</h3><dl><dt>&bull;
</dt><dd>PDL::Slices 
 In addition to explaining the original slicing and dicing functions - for which you can usually use PDL::NiceSlice - this also covers many dimension-handling functions such as <tt>&quot;mv&quot;</tt>, <tt>&quot;xchg&quot;</tt>, and <tt>&quot;reorder&quot;</tt>. This also thoroughly documents the <tt>&quot;range&quot;</tt> function, which can be very powerful, and covers a number of internal functions, which can probably be skipped.
</dd><dt>&bull;
</dt><dd>PDL::Indexing 
 This covers a lot of the deeper conceptual ground that you'll need to grasp to really use PDL to its full potential. It gets more complex as you go along, so don't be troubled if you find yourself loosing interest half way through. However, reading this document all the way through will bring you much closer to PDL enlightenment.
</dd><dt>&bull;
</dt><dd>PDL::IO 
 PDL has quite a few IO modules, most of which are discussed in this summary module.
</dd><dt>&bull;
</dt><dd>PDL::Tips 
 A collection of some of Tuomas's ideas for making good use of PDL.
</dd><dt>&bull;
</dt><dd>PDL::BadValues 
 Explains what bad values are and how and why they are implemented.
</dd><dt>&bull;
</dt><dd>Selections from Inline::Pdlpp 
 Although writing PDL::PP code is considered an Advanced topic, and is covered in the next section, you should be aware that it is possible (and surprisingly simple) to write PDL-aware code. You needn't read the whole thing at this point, but to get some feel for how it works, you should read everything up through the first example. A copy of this documentation is contained in PDL::PP-Inline.
</dd><dt>&bull;
</dt><dd>PDL::Objects 
 Explains how to subclass a piddle object.
</dd><dt>&bull;
</dt><dd>PDL::Index 
 This was discussed in the Preface. It is an automatically generated file that lists all of the PDL modules on your computer. There are many modules that may be on your machine but which are not documented here, such as bindings to the FFTW library, or GSL. Give it a read!</dd></dl><h3>Libraries</h3><dl><dt>&bull;
</dt><dd>PDL::Complex 
 Complex number support. No, PDL does not have complex number support built into the core, but this should help you out.
</dd><dt>&bull;
</dt><dd>PDL::FFT 
 PDL's own Fast Fourier Transform. If you have FFTW, then you should probably make use of it; this is PDL's internal implementation and should always be available.
</dd><dt>&bull;
</dt><dd>GSL 
 PDL does not have bindings for every sub-library in the GNU Scientific Library, but it has quite a few. If you have GSL installed on your machine then chances are decent that your PDL has the GSL bindings. For a full list of the GSL bindings, check PDL::Index.
</dd><dt>&bull;
</dt><dd>PDL::Func 
 A somewhat uniform interface to the different interpolation modules in PDL.
</dd><dt>&bull;
</dt><dd>PDL::Bad 
 Includes some basic bad-value functionality, including functions to query if a piddle has bad values (<tt>&quot;isbad&quot;</tt>) and functions to set certain elements as bad (<tt>&quot;setbadat&quot;</tt> and <tt>&quot;setbadif&quot;</tt>). Among other places, bad values are used in PDL::Graphics::PLplot's xyplot to make a gap in a line plot.
</dd><dt>&bull;
</dt><dd>PDL::DiskCache 
 A cool module that allows you to tie a Perl array to a collection of files on your disk, which will be loaded into and out of memory as piddles. If you find yourself writing scripts to process many data files, especially if that data processing is not necessarily in sequential order, you should consider using PDL::DiskCache.
</dd><dt>&bull;
</dt><dd>PDL::Char 
 A PDL subclass that allows you to store and manipulate collections of fixed-length character strings using PDL.
</dd><dt>&bull;
</dt><dd>PDL::Image2D 
 A whole collection of methods for manipulating images whose image data are stored in a piddle. These include methods for convolutions (smoothing), polygon fills, scaling, rotation, and warping, among others.
</dd><dt>&bull;
</dt><dd>PDL::ImageND 
 Contains a few functions that are conceptually related to image processing, but which can be defined for higher-dimensional data. For examples this module defines high-dimensional convolution and interpolation, among others.
</dd><dt>&bull;
</dt><dd>PDL::ImageRGB 
 Defines some useful functions for working with RBG image data. It's not very feature-full, but it may have something you need, and if not, you can always add more!
</dd><dt>&bull;
</dt><dd>PDL::Transform 
 Creates the transform class, which allows you to create various coordinate transforms. For example, if you data is a collection of Cartesian coordinates, you could create a transform object to convert them to Spherical-Polar coordinates (although many such standard coordinate transformations are predefined for you, in this case it's called <tt>&quot;t_spherical&quot;</tt>).
</dd><dt>&bull;
</dt><dd>PDL::Opt::Simplex 
 This package states that it ``implements the commonly used simplex optimization algorithm.'' I'm going to assume that if you need this algorithm then you already know what it is.
</dd><dt>&bull;
</dt><dd>PDL::Math 
 A collection of fairly standard math functions, like the inverse trigonometric functions, hyperbolic functions and their inverses, and others. This module is included in the standard call to <tt>&quot;use PDL&quot;</tt>, but not in the Lite versions.
</dd><dt>&bull;
</dt><dd>PDL::Matrix 
 Provides a few functions that use the standard mathematical Matrix notation of row-column indexing rather than the PDL-standard column-row. It appears that this module has not been heavily tested with other modules, so although it should work with other modules, don't be surprised if something breaks when you use it (and feel free to offer any fixes that you may develop).
</dd><dt>&bull;
</dt><dd>PDL::MatrixOps 
 Provides many standard matrix operations for piddles, such as computing eigenvalues, inverting square matrices, LU-decomposition, and solving a system of linear equations. Though it is not built on PDL::Matrix, it should generally work with that module. Also, the methods provided by this module do not depend on external libraries such as Slatec or GSL.
</dd><dt>&bull;
</dt><dd>PDL::Reduce 
 Implements an interface to all the functions that return piddles with one less dimension (for example, <tt>&quot;sumover&quot;</tt>), such that they can be called by suppling their name, as a string.</dd></dl><h3>Workflow</h3><dl><dt>&bull;
</dt><dd>PDL::AutoLoader 
 Enables Matlab-style autoloading. When you call an unknown function, instead of complaining and croaking, PDL will go hunt around in the directories you specify in search of a like-named file. Particularly useful when used with the Perldl Shell.
</dd><dt>&bull;
</dt><dd>PDL::Dbg 
 Declares the <tt>&quot;px&quot;</tt> function, which can be handy for debugging your PDL scripts and/or perldl shell commands.
</dd><dt>&bull;
</dt><dd>PDL::Options 
 Suppose you define a powerful, versatile function. Chances are good that you'll accept the arguments in the form of a hash or hashref. Now you face the problem of processing that hashref. PDL::Options assists you in writing code to process those options. (You'd think Perl would have tons of these sorts of modules lying around, but I couldn't find any.) Note this module does not depend on PDL for its usage or installation.
</dd><dt>&bull;
</dt><dd>PDL::pdldoc 
 Ever fired-up the perldl shell just to look up the help for a particular function? You can use <tt>&quot;pdldoc&quot;</tt> instead. This shell script extracts information from the help index without needing to start the perldl shell.</dd></dl><h2>Advanced Usage</h2>The sorts of modules and documentation that you'll use if you write modules that use PDL, or if you work on PDL maintenance. These modules can be difficult to use, but enable you to tackle some of your harder problems.
<dl><dt>&bull;
</dt><dd>PDL::Lite, PDL::LiteF 
 Lite-weight replacements for <tt>&quot;use PDL&quot;</tt>, from the standpoint of namespace pollution and load time.
</dd><dt>&bull;
</dt><dd>Inline::Pdlpp 
 This was mentioned earlier. Before you begin reading about PDL::PP (next), you should remind yourself about how to use this. Inline::Pdlpp will help you experiment with PDL::PP without having to go through the trouble of building a module and constructing makefiles (but see PDL::pptemplate for help on that).
</dd><dt>&bull;
</dt><dd>PDL::PP 
 The PDL Pre-Processor, which vastly simplifies making you C or Fortran code play with Perl and piddles. Most of PDL's basic functionality is written using PDL::PP, so if you're thinking about how you might integrate some numerical library written in C, look no further.
</dd><dt>&bull;
</dt><dd>PDL::pptemplate 
 A script that automates the creation of modules that use PDL::PP, which should make your life as a module author a bit simpler.
</dd><dt>&bull;
</dt><dd>PDL::CallExt 
 Allows you to call functions using external shared libraries. This is an alternative to using PDL::PP. The major difference between PDL::PP and PDL::CallExt is that the former will handle threading over implicit thread dimensions for you, whereas PDL::CallExt simply calls an external function. PDL::PP is generally the recommended way to interface your code with PDL, but it wouldn't be Perl if there wasn't another way to do it.
</dd><dt>&bull;
</dt><dd>PDL::Config 
 Defines the <tt>%PDL::Config</tt> hash, which has lots of useful information pertinent to your PDL build.
</dd><dt>&bull;
</dt><dd>PDL::Doc 
 Explanation of the PDL documentation conventions, and an interface to the PDL Documentation parser. Following these guidelines when writing documentation for PDL functions will ensure that your wonderful documentation is accessible from the perldl shell and from calls to <tt>&quot;barf&quot;</tt>. (Did you notice that <tt>&quot;barf&quot;</tt> used your documentation? Time to reread PDL::Core...)
</dd><dt>&bull;
</dt><dd>PDL::Exporter 
 A simple replacement for the standard Exporter module. The only major difference is that the default imported modules are those marked ':Func'.
</dd><dt>&bull;
</dt><dd>PDL::Types 
 Defines some useful functions for getting a piddle's type, as well as getting information about that type.
</dd><dt>&bull;
</dt><dd>PDL::Version 
 Simply defines the scalar <tt>$PDL::Version::Version</tt> with the current version of PDL, as defined in PDL.pm. This is most useful if you distribute your own module on CPAN, use PDL::Lite or PDL::LiteF and want to make sure that your users have a recent-enough version of PDL.  Since the variable is defined in PDL.pm, you don't need this module if you <tt>&quot;use PDL&quot;</tt>.</dd></dl><h2>Expert Usage</h2><dl><dt>&bull;
</dt><dd>PDL::Core::Dev 
 Provides some decently useful functions that are pretty much only needed by the PDL Porters.
</dd><dt>&bull;
</dt><dd>PDL::API 
 Explains how to make a piddle <i>by hand</i>, from Perl or your C source code, using the PDL API.
</dd><dt>&bull;
</dt><dd>PDL::Internals 
 Explains the nitty-gritty of the PDL data structures. After reading this (a few times :), you should be able to create a piddle completely from scratch (i.e. without using the PDL API). Put a little differently, if you want to understand how PDL::PP works, you'll need to read this.</dd></dl><h2>Copyright</h2>Copyright 2010 David Mertens (dcmertens.perl [at] gmail.com). You can distribute and/or modify this document under the same terms as the current Perl license. 

 See: <a rel="nofollow" HREF="http://dev.perl.org/licenses/">http://dev.perl.org/licenses/</a>
