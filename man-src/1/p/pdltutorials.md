---
title: "pdltutorials(1)"
name: "pdltutorials"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdltutorials/"
description: "PDL::Tutorials – A guide to PDL’s tutorial documentation."
---

<p>PDL::Tutorials &#8211; A guide to PDL&#8217;s tutorial documentation. </p>
<h2>Migration</h2>
<p>These are our migration guides for users familiar with other types of numerical analysis software.</p>
<dl>
<dt><font SIZE="-1">PDL::MATLAB</font></p>
<dd>Migration guide for <font SIZE="-1">MATLAB</font> users. This page explains the key differences between <font SIZE="-1">MATLAB</font> and <font SIZE="-1">PDL</font> from the point of view of a <font SIZE="-1">MATLAB</font> user.</p>
<dt>PDL::Scilab</p>
<dd>Migration guide for Scilab users. This page explains the key differences between Scilab and <font SIZE="-1">PDL</font> from the point of view of a Scilab user.</dl>
<h2>Foundation</h2>
<dl>
<dt>PDL::Philosophy</p>
<dd>Why did we write <font SIZE="-1">PDL</font>? This document explains some of the history and motivation behind the Perl Data Language. It is an attempt to answer the question &#8220;Why <font SIZE="-1">PDL</font>?&#8221;.</p>
<dt>PDL::QuickStart</p>
<dd>Quick introduction to <font SIZE="-1">PDL</font> features. A hands-on guide suitable for complete beginners. This page assumes no previous knowledge of Perl or <font SIZE="-1">PDL.</font></p>
<dt>PDL::Indexing</p>
<dd>After you have read the QuickStart guide, you should follow up with this document. This guide goes more deeply into the concepts of &#8220;indexing&#8221; and &#8220;slicing&#8221; and how they form the core of numerical analysis with <font SIZE="-1">PDL.</font></dl>
<h2>Intermediate</h2>
<dl>
<dt>PDL::Threading</p>
<dd><code>Threading</code> is one of <font SIZE="-1">PDL</font>&#8216;s most powerful features. If you know <font SIZE="-1">MATLAB,</font> you&#8217;ve heard of &#8220;vectorizing&#8221;. Well, <code>threading</code> is like &#8220;vectorizing on steroids&#8221;. It lets you make very fast and compact code by avoiding nested loops. All vector-based languages do this, but <font SIZE="-1">PDL</font> generalizes the technique to all sorts of applications. </p>
<p> This tutorial introduces <font SIZE="-1">PDL</font>&#8216;s threading feature, and it shows an example implementing Conway&#8217;s Game of Life in 10 lines and 80 times faster than a classical implementation.</p>
<dt>PDL::BadValues</p>
<dd>Sometimes it is useful to specify that a certain value is &#8220;bad&#8221; or &#8220;missing&#8221;. Scientific instruments some times include portions of invalid data. For example, a <font SIZE="-1">CCD</font> camera might produce an image with over-exposed pixels. <font SIZE="-1">PDL</font>&#8216;s &#8220;bad values&#8221; feature gives you an easy way to deal with this sort of imperfect data.</p>
<dt>PDL::Tips</p>
<dd>Tips and suggestions for using <font SIZE="-1">PDL.</font> This page is an assorted collection of programming tidbits that some <font SIZE="-1">PDL</font> users have found useful. Some of these tips might be of help when you write your programs.</dl>
<h2>Advanced</h2>
<dl>
<dt><font SIZE="-1">PDL::PP</font></p>
<dd><font SIZE="-1">PDL</font>&#8216;s Pre-Processor is one of <font SIZE="-1">PDL</font>&#8216;s most powerful features. You write a function definition in special markup and the preprocessor generates real C code which can be compiled. With <font SIZE="-1">PDL:PP</font> you get the full speed of native C code without having to deal with the full complexity of the C language.</p>
<dt><font SIZE="-1">PDL::API</font></p>
<dd>A simple cookbook explaining how to create piddle manually, either from Perl or from C/XS code. This page covers the <font SIZE="-1">PDL</font> core routines that comprise the <font SIZE="-1">PDL API.</font> If you need to access piddles from C/XS, this is the document for you.</p>
<dt>PDL::Internals</p>
<dd>Description of the inner workings of the <font SIZE="-1">PDL</font> module. Very few people need to see this. This page is mainly for <font SIZE="-1">PDL</font> developers, or people interested in debugging <font SIZE="-1">PDL</font> or changing the internals of <font SIZE="-1">PDL.</font> If you can read this document and understand all of it, and you additionally understand <font SIZE="-1">PDL::PP</font>, you will be awarded the title of &#8220;<font SIZE="-1">PDL</font> Guru&#8221;.</dl>
<h2>Copyright</h2>
<p>Copyright 2010 Daniel Carrera (dcarrera [at] gmail.com). You can distribute and/or modify this document under the same terms as the current Perl license. </p>
<p> See: <a rel="nofollow" href="http://dev.perl.org/licenses/">http://dev.perl.org/licenses/</a></p>
