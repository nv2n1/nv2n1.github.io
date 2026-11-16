---
title: "perl5141delta(1)"
name: "perl5141delta"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perl5141delta/"
description: "perl5141delta – what is new for perl v5.14.1"
---

<h2 class="name">NAME</h2>
<p> perl5141delta &#8211; what is new for perl v5.14.1 </p>
<h2>DESCRIPTION</h2>
<p> This document describes differences between the 5.14.0 release and the 5.14.1 release. </p>
<p> If you are upgrading from an earlier release such as 5.12.0, first read perl5140delta, which describes differences between 5.12.0 and 5.14.0.</p>
<h2>Core Enhancements</h2>
<p> No changes since 5.14.0.</p>
<h2>Security</h2>
<p> No changes since 5.14.0.</p>
<h2>Incompatible Changes</h2>
<p> There are no changes intentionally incompatible with 5.14.0. If any exist, they are bugs and reports are welcome.</p>
<h2>Deprecations</h2>
<p> There have been no deprecations since 5.14.0.</p>
<h2>Modules and Pragmata</h2>
<h3>New Modules and Pragmata</h3>
<p> None</p>
<h3>Updated Modules and Pragmata</h3>
<dl>
<dt>&bull;</dt>
<dd> B::Deparse has been upgraded from version 1.03 to 1.04, to address two regressions in Perl 5.14.0: </dd>
<p> Deparsing of the <tt>&quot;glob&quot;</tt> operator and its diamond (<tt>&quot;&lt;&gt;&quot;</tt>) form now works again. [perl #90898] </p>
<p> The presence of subroutines named <tt>&quot;::::&quot;</tt> or <tt>&quot;::::::&quot;</tt> no longer causes B::Deparse to hang.</p>
<dt>&bull;</dt>
<dd> Pod::Perldoc has been upgraded from version 3.15_03 to 3.15_04. </dd>
<p> It corrects the search paths on <font SIZE="-1">VMS.</font> [perl #90640]</dl>
<h3>Removed Modules and Pragmata</h3>
<p> None</p>
<h2>Documentation</h2>
<h3>New Documentation</h3>
<p> None</p>
<h3>Changes to Existing Documentation</h3>
<p> <i>perlfunc</i></p>
<dl>
<dt>&bull;</dt>
<dd> <tt>&quot;given&quot;</tt>, <tt>&quot;when&quot;</tt> and <tt>&quot;default&quot;</tt> are now listed in perlfunc.</dd>
<dt>&bull;</dt>
<dd> Documentation for <tt>&quot;use&quot;</tt> now includes a pointer to <i>if.pm</i>.</dd></dl>
<p> <i>perllol</i></p>
<dl>
<dt>&bull;</dt>
<dd> perllol has been expanded with examples using the new <tt>&quot;push $scalar&quot;</tt> syntax introduced in Perl 5.14.0.</dd></dl>
<p> <i>perlop</i></p>
<dl>
<dt>&bull;</dt>
<dd> The explanation of bitwise operators has been expanded to explain how they work on Unicode strings.</dd>
<dt>&bull;</dt>
<dd> The section on the triple-dot or yada-yada operator has been moved up, as it used to separate two closely related sections about the comma operator.</dd>
<dt>&bull;</dt>
<dd> More examples for <tt>&quot;m//g&quot;</tt> have been added.</dd>
<dt>&bull;</dt>
<dd> The <tt>&quot;&lt;&lt;\FOO&quot;</tt> here-doc syntax has been documented.</dd></dl>
<p> <i>perlrun</i></p>
<dl>
<dt>&bull;</dt>
<dd> perlrun has undergone a significant clean-up. Most notably, the <code>-0x&#8230;</code> form of the <code>-0</code> flag has been clarified, and the final section on environment variables has been corrected and expanded.</dd></dl>
<p> <i></i><font SIZE="-1"><i>POSIX</i></font><i></i></p>
<dl>
<dt>&bull;</dt>
<dd> The invocation documentation for <tt>&quot;WIFEXITED&quot;</tt>, <tt>&quot;WEXITSTATUS&quot;</tt>, <tt>&quot;WIFSIGNALED&quot;</tt>, <tt>&quot;WTERMSIG&quot;</tt>, <tt>&quot;WIFSTOPPED&quot;</tt>, and <tt>&quot;WSTOPSIG&quot;</tt> was corrected.</dd></dl>
<h2>Diagnostics</h2>
<p> The following additions or changes have been made to diagnostic output, including warnings and fatal error messages. For the complete list of diagnostic messages, see perldiag.</p>
<h3>New Diagnostics</h3>
<p> None</p>
<h3>Changes to Existing Diagnostics</h3>
<p> None</p>
<h2>Utility Changes</h2>
<p> None</p>
<h2>Configuration and Compilation</h2>
<dl>
<dt>&bull;</dt>
<dd> <i>regexp.h</i> has been modified for compatibility with <font SIZE="-1">GCC</font>&#8216;s <tt>&quot;-Werror&quot;</tt> option, as used by some projects that include perl&#8217;s header files.</dd></dl>
<h2>Testing</h2>
<dl>
<dt>&bull;</dt>
<dd> Some test failures in <i>dist/Locale-Maketext/t/09_compile.t</i> that could occur depending on the environment have been fixed. [perl #89896]</dd>
<dt>&bull;</dt>
<dd> A watchdog timer for <i>t/re/re.t</i> was lengthened to accommodate <font SIZE="-1">SH-4</font> systems which were unable to complete the tests before the previous timer ran out.</dd></dl>
<h2>Platform Support</h2>
<h3>New Platforms</h3>
<p> None</p>
<h3>Discontinued Platforms</h3>
<p> None</p>
<h3>Platform-Specific Notes</h3>
<p> <i>Solaris</i></p>
<dl>
<dt>&bull;</dt>
<dd> Documentation listing the Solaris packages required to build Perl on Solaris 9 and Solaris 10 has been corrected.</dd></dl>
<p> <i>Mac </i><font SIZE="-1"><i>OS X</i></font><i></i></p>
<dl>
<dt>&bull;</dt>
<dd> The <i>lib/locale.t</i> test script has been updated to work on the upcoming Lion release.</dd>
<dt>&bull;</dt>
<dd> Mac <font SIZE="-1">OS X</font> specific compilation instructions have been clarified.</dd></dl>
<p> <i>Ubuntu Linux</i></p>
<dl>
<dt>&bull;</dt>
<dd> The ODBM_File installation process has been updated with the new library paths on Ubuntu natty.</dd></dl>
<h2>Internal Changes</h2>
<dl>
<dt>&bull;</dt>
<dd> The compiled representation of formats is now stored via the mg_ptr of their PERL_MAGIC_fm. Previously it was stored in the string buffer, beyond <code>SvLEN()</code>, the regular end of the string. <code>SvCOMPILED()</code> and SvCOMPILED_{on,off}() now exist solely for compatibility for <font SIZE="-1">XS</font> code. The first is always 0, the other two now no-ops.</dd></dl>
<h2>Bug Fixes</h2>
<dl>
<dt>&bull;</dt>
<dd> A bug has been fixed that would cause a &#8220;Use of freed value in iteration&#8221; error if the next two hash elements that would be iterated over are deleted. [perl #85026]</dd>
<dt>&bull;</dt>
<dd> Passing the same constant subroutine to both <tt>&quot;index&quot;</tt> and <tt>&quot;formline&quot;</tt> no longer causes one or the other to fail. [perl #89218]</dd>
<dt>&bull;</dt>
<dd> 5.14.0 introduced some memory leaks in regular expression character classes such as <tt>&quot;[\w\s]&quot;</tt>, which have now been fixed.</dd>
<dt>&bull;</dt>
<dd> An edge case in regular expression matching could potentially loop. This happened only under <tt>&quot;/i&quot;</tt> in bracketed character classes that have characters with multi-character folds, and the target string to match against includes the first portion of the fold, followed by another character that has a multi-character fold that begins with the remaining portion of the fold, plus some more. </dd>
<pre><code>
"s\N{U+DF}" = ~ / [
</dl>
</code></pre>
