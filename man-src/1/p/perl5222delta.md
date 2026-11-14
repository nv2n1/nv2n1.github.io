---
title: "perl5222delta(1)"
name: "perl5222delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5222delta/"
description: "perl5222delta – what is new for perl v5.22.2"
---

<h2 class="name">NAME</h2>
<p> perl5222delta &#8211; what is new for perl v5.22.2 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.22.1 release and the 5.22.2 release. </p>
<p> If you are upgrading from an earlier release such as 5.22.0, first read perl5221delta, which describes differences between 5.22.0 and 5.22.1.</p>
<h2>Security</h2>
<h3>Fix out of boundary access in Win32 path handling</h3>
<p> This is <font SIZE="-1">CVE-2015-8608.</font> For more information see [perl #126755] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126755">https://rt.perl.org/Ticket/Display.html?id=126755</a>&gt;.</p>
<h3>Fix loss of taint in canonpath()</h3>
<p> This is <font SIZE="-1">CVE-2015-8607.</font> For more information see [perl #126862] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126862">https://rt.perl.org/Ticket/Display.html?id=126862</a>&gt;.</p>
<h3>Set proper umask before calling <a href="/docs/linux/man/3-mkstemp/">mkstemp</a>(3)</h3>
<p> In 5.22.0 perl started setting umask to <tt>0600</tt> before calling <tt><a href="/docs/linux/man/3-mkstemp/">mkstemp</a>(3)</tt> and restoring it afterwards. This wrongfully tells <tt><a href="/docs/linux/man/2-open/">open</a>(2)</tt> to strip the owner read and write bits from the given mode before applying it, rather than the intended negation of leaving only those bits in place. </p>
<p> Systems that use mode <tt>0666</tt> in <tt><a href="/docs/linux/man/3-mkstemp/">mkstemp</a>(3)</tt> (like old versions of glibc) create a file with permissions <tt>0066</tt>, leaving world read and write permissions regardless of current umask. </p>
<p> This has been fixed by using umask <tt>0177</tt> instead. </p>
<p> [perl #127322] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=127322">https://rt.perl.org/Ticket/Display.html?id=127322</a>&gt;</p>
<h3>Avoid accessing uninitialized memory in Win32 crypt()</h3>
<p> Validation that will detect both a short salt and invalid characters in the salt has been added. </p>
<p> [perl #126922] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126922">https://rt.perl.org/Ticket/Display.html?id=126922</a>&gt;</p>
<h3>Remove duplicate environment variables from environ</h3>
<p> Previously, if an environment variable appeared more than once in <tt>&quot;environ[]&quot;</tt>, <tt>%ENV</tt> would contain the last entry for that name, while a typical <tt>&quot;getenv()&quot;</tt> would return the first entry. We now make sure <tt>%ENV</tt> contains the same as what <tt>&quot;getenv()&quot;</tt> returns. </p>
<p> Secondly, we now remove duplicates from <tt>&quot;environ[]&quot;</tt>, so if a setting with that name is set in <tt>%ENV</tt> we won&#8217;t pass an unsafe value to a child process. </p>
<p> This is <font SIZE="-1">CVE-2016-2381.</font></p>
<h2>Incompatible Changes</h2>
<p> There are no changes intentionally incompatible with Perl 5.22.1. If any exist, they are bugs, and we request that you submit a report. See &#8220;Reporting Bugs&#8221; below.</p>
<h2>Modules and Pragmata</h2>
<h3>Updated Modules and Pragmata</h3>
<dl>
<dt>&bull;</p>
<dd> File::Spec has been upgraded from version 3.56 to 3.56_01. </p>
<p> <tt>&quot;canonpath()&quot;</tt> now preserves taint. See &quot;Fix loss of taint in <tt>&quot;canonpath()&quot;</tt>&quot;.</p>
<dt>&bull;</p>
<dd> Module::CoreList has been upgraded from version 5.20151213 to 5.20160429. </p>
<p> The version number of Digest::SHA listed for Perl 5.18.4 was wrong and has been corrected. Likewise for the version number of Config in 5.18.3 and 5.18.4. [perl #127624] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=127624">https://rt.perl.org/Ticket/Display.html?id=127624</a>&gt;</dl>
<h2>Documentation</h2>
<h3>Changes to Existing Documentation</h3>
<p> <i>perldiag</i></p>
<dl>
<dt>&bull;</p>
<dd> The explanation of the warning &#8220;unable to close filehandle <tt>%s</tt> properly: <tt>%s</tt>&#8221; which can occur when doing an implicit close of a filehandle has been expanded and improved.</dl>
<p> <i>perlfunc</i></p>
<dl>
<dt>&bull;</p>
<dd> The documentation of <tt>&quot;hex()&quot;</tt> has been revised to clarify valid inputs.</dl>
<h2>Configuration and Compilation</h2>
<dl>
<dt>&bull;</p>
<dd> Dtrace builds now build successfully on systems with a newer dtrace that require an input object file that uses the probes in the <i>.d</i> file. </p>
<p> Previously the probe would fail and cause a build failure. </p>
<p> [perl #122287] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=122287">https://rt.perl.org/Ticket/Display.html?id=122287</a>&gt;</p>
<dt>&bull;</p>
<dd> <i>Configure</i> no longer probes for <i>libnm</i> by default. Originally this was the &#8220;New Math&#8221; library, but the name has been re-used by the <font SIZE="-1">GNOME</font> NetworkManager. </p>
<p> [perl #127131] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=127131">https://rt.perl.org/Ticket/Display.html?id=127131</a>&gt;</p>
<dt>&bull;</p>
<dd> <i>Configure</i> now knows about gcc 5.</p>
<dt>&bull;</p>
<dd> Compiling perl with <code>-DPERL_MEM_LOG</code> now works again.</dl>
<h2>Platform Support</h2>
<h3>Platform-Specific Notes</h3>
<dl>
<dt>Darwin</p>
<dd> Compiling perl with <code>-Dusecbacktrace</code> on Darwin now works again. </p>
<p> [perl #127764] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=127764">https://rt.perl.org/Ticket/Display.html?id=127764</a>&gt;</p>
<dt><font SIZE="-1">OS</font> X/Darwin</p>
<dd> Builds with both <code>-DDEBUGGING</code> and threading enabled would fail with a &#8220;panic: free from wrong pool&#8221; error when built or tested from Terminal on <font SIZE="-1">OS X.</font> This was caused by perl&#8217;s internal management of the environment conflicting with an atfork handler using the libc <tt>&quot;setenv()&quot;</tt> function to update the environment. </p>
<p> Perl now uses <tt>&quot;setenv()&quot;</tt>/<tt>&quot;unsetenv()&quot;</tt> to update the environment on <font SIZE="-1">OS X.</font> </p>
<p> [perl #126240] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126240">https://rt.perl.org/Ticket/Display.html?id=126240</a>&gt;</p>
<dt>ppc64el</p>
<dd> The floating point format of ppc64el (Debian naming for little-endian PowerPC) is now detected correctly.</p>
<dt>Tru64</p>
<dd> A test failure in <i>t/porting/extrefs.t</i> has been fixed.</dl>
<h2>Internal Changes</h2>
<dl>
<dt>&bull;</p>
<dd> An unwarranted assertion in <tt>&quot;Perl_newATTRSUB_x()&quot;</tt> has been removed. If a stub subroutine definition with a prototype has been seen, then any subsequent stub (or definition) of the same subroutine with an attribute was causing an assertion failure because of a null pointer. </p>
<p> [perl #126845] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126845">https://rt.perl.org/Ticket/Display.html?id=126845</a>&gt;</dl>
<h2>Selected Bug Fixes</h2>
<dl>
<dt>&bull;</p>
<dd> Calls to the placeholder <tt>&amp;PL_sv_yes</tt> used internally when an <tt>&quot;import()&quot;</tt> or <tt>&quot;unimport()&quot;</tt> method isn&#8217;t found now correctly handle scalar context. [perl #126042] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126042">https://rt.perl.org/Ticket/Display.html?id=126042</a>&gt;</p>
<dt>&bull;</p>
<dd> The <tt>&quot;pipe()&quot;</tt> operator would assert for <tt>&quot;DEBUGGING&quot;</tt> builds instead of producing the correct error message. The condition asserted on is detected and reported on correctly without the assertions, so the assertions were removed. [perl #126480] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126480">https://rt.perl.org/Ticket/Display.html?id=126480</a>&gt;</p>
<dt>&bull;</p>
<dd> In some cases, failing to parse a here-doc would attempt to use freed memory. This was caused by a pointer not being restored correctly. [perl #126443] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=126443">https://rt.perl.org/Ticket/Display.html?id=126443</a>&gt;</p>
<dt>&bull;</p>
<dd> Perl now reports more context when it sees an array where it expects to see an operator, and avoids an assertion failure. [perl #123737] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=123737">https://rt.perl.org/Ticket/Display.html?id=123737</a>&gt;</p>
<dt>&bull;</p>
<dd> If a here-doc was found while parsing another operator, the parser had already read end of file, and the here-doc was not terminated, perl could produce an assertion or a segmentation fault. This now reliably complains about the unterminated here-doc. [perl #125540] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=125540">https://rt.perl.org/Ticket/Display.html?id=125540</a>&gt;</p>
<dt>&bull;</p>
<dd> Parsing beyond the end of the buffer when processing a <tt>&quot;#line&quot;</tt> directive with no filename is now avoided. [perl #127334] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=127334">https://rt.perl.org/Ticket/Display.html?id=127334</a>&gt;</p>
<dt>&bull;</p>
<dd> Perl 5.22.0 added support for the C99 hexadecimal floating point notation, but sometimes misparsed hex floats. This has been fixed. [perl #127183] &lt;<a rel="nofollow" href="https://rt.perl.org/Ticket/Display.html?id=127183">https://rt.perl.org/Ticket/Display.html?id=127183</a>&gt;</p>
<dt>&bull;</p>
<dd> Certain regex patterns involving a complemented posix class in an inverted bracketed character class, and matching something else optionally would improperly fail to match. An example of one that could fail is <tt>&quot;qr/_?[^\Wbar]
