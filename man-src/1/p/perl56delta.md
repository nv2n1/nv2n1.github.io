---
title: "perl56delta(1)"
name: "perl56delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl56delta/"
description: "perl56delta – what’s new for perl v5.6.0"
---

<h2 class="name">NAME</h2>
<p> perl56delta &#8211; what&#8217;s new for perl v5.6.0 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.005 release and the 5.6.0 release.</p>
<h2>Core Enhancements</h2>
<h3>Interpreter cloning, threads, and concurrency</h3>
<p> Perl 5.6.0 introduces the beginnings of support for running multiple interpreters concurrently in different threads. In conjunction with the <code>perl_clone()</code> <font SIZE="-1">API</font> call, which can be used to selectively duplicate the state of any given interpreter, it is possible to compile a piece of code once in an interpreter, clone that interpreter one or more times, and run all the resulting interpreters in distinct threads. </p>
<p> On the Windows platform, this feature is used to emulate <code>fork()</code> at the interpreter level. See perlfork for details about that. </p>
<p> This feature is still in evolution. It is eventually meant to be used to selectively clone a subroutine and data reachable from that subroutine in a separate interpreter and run the cloned subroutine in a separate thread. Since there is no shared data between the interpreters, little or no locking will be needed (unless parts of the symbol table are explicitly shared). This is obviously intended to be an easy-to-use replacement for the existing threads support. </p>
<p> Support for cloning interpreters and interpreter concurrency can be enabled using the -Dusethreads Configure option (see win32/Makefile for how to enable it on Windows.) The resulting perl executable will be functionally identical to one that was built with -Dmultiplicity, but the <code>perl_clone()</code> <font SIZE="-1">API</font> call will only be available in the former. </p>
<p> -Dusethreads enables the cpp macro <font SIZE="-1">USE_ITHREADS</font> by default, which in turn enables Perl source code changes that provide a clear separation between the op tree and the data it operates with. The former is immutable, and can therefore be shared between an interpreter and all of its clones, while the latter is considered local to each interpreter, and is therefore copied for each clone. </p>
<p> Note that building Perl with the -Dusemultiplicity Configure option is adequate if you wish to run multiple <code>independent</code> interpreters concurrently in different threads. -Dusethreads only provides the additional functionality of the <code>perl_clone()</code> <font SIZE="-1">API</font> call and other support for running <code>cloned</code> interpreters concurrently. </p>
<pre>
    NOTE: This is an experimental feature.  Implementation details are
    subject to change.
</pre>
<h3>Lexically scoped warning categories</h3>
<p> You can now control the granularity of warnings emitted by perl at a finer level using the <tt>&quot;use warnings&quot;</tt> pragma. warnings and perllexwarn have copious documentation on this feature.</p>
<h3>Unicode and <font SIZE="-1">UTF-8</font> support</h3>
<p> Perl now uses <font SIZE="-1">UTF-8</font> as its internal representation for character strings. The <tt>&quot;utf8&quot;</tt> and <tt>&quot;bytes&quot;</tt> pragmas are used to control this support in the current lexical scope. See perlunicode, utf8 and bytes for more information. </p>
<p> This feature is expected to evolve quickly to support some form of I/O disciplines that can be used to specify the kind of input and output data (bytes or characters). Until that happens, additional modules from <font SIZE="-1">CPAN</font> will be needed to complete the toolkit for dealing with Unicode. </p>
<pre>
    NOTE: This should be considered an experimental feature.  Implementation
    details are subject to change.
</pre>
<h3>Support for interpolating named characters</h3>
<p> The new <tt>&quot;\N&quot;</tt> escape interpolates named characters within strings. For example, <tt>&quot;Hi! \N{WHITE SMILING FACE}&quot;</tt> evaluates to a string with a unicode smiley face at the end.</p>
<h3>our declarations</h3>
<p> An &#8220;our&#8221; declaration introduces a value that can be best understood as a lexically scoped symbolic alias to a global variable in the package that was current where the variable was declared. This is mostly useful as an alternative to the <tt>&quot;vars&quot;</tt> pragma, but also provides the opportunity to introduce typing and other attributes for such variables. See &#8220;our&#8221; in perlfunc.</p>
<h3>Support for strings represented as a vector of ordinals</h3>
<p> Literals of the form <tt>&quot;v1.2.3.4&quot;</tt> are now parsed as a string composed of characters with the specified ordinals. This is an alternative, more readable way to construct (possibly unicode) strings instead of interpolating characters, as in <tt>&quot;
