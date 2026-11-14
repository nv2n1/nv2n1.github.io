---
title: "perldebguts(1)"
name: "perldebguts"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perldebguts/"
description: "perldebguts – Guts of Perl debugging"
---

<h2 class="name">NAME</h2>
<p> perldebguts &#8211; Guts of Perl debugging </p>
<h2>DESCRIPTION</h2>
<p> This is not perldebug, which tells you how to use the debugger. This manpage describes low-level details concerning the debugger&#8217;s internals, which range from difficult to impossible to understand for anyone who isn&#8217;t incredibly intimate with Perl&#8217;s guts. Caveat lector.</p>
<h2>Debugger Internals</h2>
<p> Perl has special debugging hooks at compile-time and run-time used to create debugging environments. These hooks are not to be confused with the <i>perl -Dxxx</i> command described in perlrun, which is usable only if a special Perl is built per the instructions in the <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> podpage in the Perl source tree. </p>
<p> For example, whenever you call Perl&#8217;s built-in <tt>&quot;caller&quot;</tt> function from the package <tt>&quot;DB&quot;</tt>, the arguments that the corresponding stack frame was called with are copied to the <tt>@DB::args</tt> array. These mechanisms are enabled by calling Perl with the <code>-d</code> switch. Specifically, the following additional features are enabled (cf. &#8220;$^P&#8221; in perlvar):</p>
<dl>
<dt>&bull;</p>
<dd> Perl inserts the contents of <tt>$ENV{PERL5DB}</tt> (or <tt>&quot;BEGIN {require 'perl5db.pl'}&quot;</tt> if not present) before the first line of your program.</p>
<dt>&bull;</p>
<dd> Each array <tt>&quot;@{&quot;_&lt;$filename&quot;}&quot;</tt> holds the lines of <tt>$filename</tt> for a file compiled by Perl. The same is also true for <tt>&quot;eval&quot;</tt>ed strings that contain subroutines, or which are currently being executed. The <tt>$filename</tt> for <tt>&quot;eval&quot;</tt>ed strings looks like <tt>&quot;(eval 34)&quot;</tt>. </p>
<p> Values in this array are magical in numeric context: they compare equal to zero only if the line is not breakable.</p>
<dt>&bull;</p>
<dd> Each hash <tt>&quot;%{&quot;_&lt;$filename&quot;}&quot;</tt> contains breakpoints and actions keyed by line number. Individual entries (as opposed to the whole hash) are settable. Perl only cares about Boolean true here, although the values used by <i>perl5db.pl</i> have the form <tt>&quot;$break_condition
