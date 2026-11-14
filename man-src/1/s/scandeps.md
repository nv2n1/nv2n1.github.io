---
title: "scandeps(1)"
name: "scandeps"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scandeps/"
description: "scandeps.pl – Scan file prerequisites"
---

<h2 class="name">NAME</h2>
<p> scandeps.pl &#8211; Scan file prerequisites </p>
<h2>SYNOPSIS</h2>
<pre>
    % scandeps.pl *.pm          # Print PREREQ_PM section for *.pm
    % scandeps.pl -e 'STRING'   # Scan an one-liner
    % scandeps.pl -B *.pm       # Include core modules
    % scandeps.pl -V *.pm       # Show autoload/shared/data files
    % scandeps.pl -R *.pm       # Don't recurse
    % scandeps.pl -C CACHEFILE  # use CACHEFILE to cache dependencies
</pre>
<h2>DESCRIPTION</h2>
<p> <i>scandeps.pl</i> is a simple-minded utility that prints out the <tt>&quot;PREREQ_PM&quot;</tt> section needed by modules. </p>
<p> If you have <font SIZE="-1"><code>CPANPLUS</code></font> installed, modules that are part of an earlier module&#8217;s distribution with be denoted with <tt>&quot;S&quot;</tt>; modules without a distribution name on <font SIZE="-1">CPAN</font> are marked with <tt>&quot;?&quot;</tt>. </p>
<p> Also, if the <tt>&quot;-B&quot;</tt> option is specified, module belongs to a perl distribution on <font SIZE="-1">CPAN</font> (and thus uninstallable by <tt>&quot;CPAN.pm&quot;</tt> or <tt>&quot;CPANPLUS.pm&quot;</tt>) are marked with <tt>&quot;C&quot;</tt>. </p>
<p> Finally, modules that has loadable shared object files (usually needing a compiler to install) are marked with <tt>&quot;X&quot;</tt>; with the <tt>&quot;-V&quot;</tt> flag, those files (and all other files found) will be listed before the main output. Additionally, all module files that the scanned code depends on but were not found (and thus not scanned recursively) are listed. These may include genuinely missing modules or false positives. That means, modules your code does not depend on (on this particular platform) but that were picked up by the heuristic anyway.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-e <font SIZE="-1">STRING</font></p>
<dd> Scan <i></i><font SIZE="-1"><i>STRING</i></font><i></i> as a string containing perl code.</p>
<dt>-c</p>
<dd> Compiles the code and inspects its <tt>%INC</tt>, in addition to static scanning.</p>
<dt>-x</p>
<dd> Executes the code and inspects its <tt>%INC</tt>, in addition to static scanning.</p>
<dt>-B</p>
<dd> Include core modules in the output and the recursive search list.</p>
<dt>-R</p>
<dd> Only show dependencies found in the files listed and do not recurse.</p>
<dt>-V</p>
<dd> Verbose mode: Output all files found during the process; show dependencies between modules and availability. </p>
<p> Additionally, warns of any missing dependencies. If you find missing dependencies that aren&#8217;t really dependencies, you have probably found false positives.</p>
<dt>-C <font SIZE="-1">CACHEFILE</font></p>
<dd> Use <font SIZE="-1">CACHEFILE</font> to speed up the scanning process by caching dependencies. Creates <font SIZE="-1">CACHEFILE</font> if it does not exist yet.</dl>
<h2>SEE ALSO</h2>
<p> Module::ScanDeps, CPANPLUS::Backend, <font SIZE="-1">PAR</font></p>
<h2>ACKNOWLEDGMENTS</h2>
<p> Simon Cozens, for suggesting this script to be written.</p>
<h2>AUTHORS</h2>
<p> Audrey Tang &lt;autrijus [at] autrijus.org&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright 2003, 2004, 2005, 2006 by Audrey Tang &lt;autrijus [at] autrijus.org&gt;. </p>
<p> This program is free software; you can redistribute it and/or modify it under the same terms as Perl itself. </p>
<p> See &lt;<a rel="nofollow" href="http://www.perl.com/perl/misc/Artistic.html">http://www.perl.com/perl/misc/Artistic.html</a>&gt; </p>
<h2>Index</h2>
