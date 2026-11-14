---
title: "perlamiga(1)"
name: "perlamiga"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlamiga/"
description: "perlamiga – Perl under AmigaOS 4.1"
---

<h2 class="name">NAME</h2>
<p> perlamiga &#8211; Perl under AmigaOS 4.1 </p>
<h2>NOTE</h2>
<p> This is a port of Perl 5.22.1, it is a fresh port and not in any way compatible with my previous ports of Perl 5.8 and 5.16.3. This means you will need to reinstall / rebuild any third party modules you have installed. </p>
<p> newlib.library version 53.28 or greater is required.</p>
<h2>SYNOPSIS</h2>
<p> Once perl is installed you can read this document in the following way </p>
<pre>
        sh -c &quot;perldoc perlamiga&quot;
</pre>
<p> or you may read <i>as is</i>: either as <i></i><font SIZE="-1"><i>README</i></font><i>.amiga</i>, or <i>pod/perlamiga.pod</i>.</p>
<h2>DESCRIPTION</h2>
<h3>Prerequisites for running Perl 5.22.1 under AmigaOS 4.1</h3>
<dl>
<dt><code>AmigaOS 4.1 update 6 with all updates applied as of 9th October 2013</code></p>
<dd> The most important of which is:</p>
<dt><code>newlib.library version 53.28 or greater</code></p>
<dd>
<dt><code>AmigaOS </code><font SIZE="-1"><code>SDK</code></font></p>
<dd> Perl installs into the <font SIZE="-1">SDK</font> directory structure and expects many of the build tools present in the <font SIZE="-1">SDK</font> to be available. So for the best results install the <font SIZE="-1">SDK</font> first.</p>
<dt><code>abc-shell</code></p>
<dd> If you do not have the <font SIZE="-1">SDK</font> installed you must at least have abc-shell installed or some other suitable sh port. This is required to run external commands and should be available as &#8216;sh&#8217; in your path.</dl>
<h3>Starting Perl programs under AmigaOS 4.1</h3>
<p> Perl may be run from the AmigaOS shell but for best results should be run under abc-shell. (abc-shell handles file globbing, pattern expansion, and sets up environment variables in the UN*Xy way that Perl expects.) </p>
<p> For example: </p>
<pre>
        New Shell process 10
        10.AmigaOS4:&gt; sh
        /AmigaOS4&gt;perl path:to/myprog arg1 arrg2 arg3
</pre>
<p> Abc-shell can also launch programs via the #! syntax at the start of the program file, it&#8217;s best use the form #!SDK:Local/C/perl so that the AmigaOS shell may also find perl in the same way. AmigaOS requires the script bit to be set for this to work </p>
<pre>
        10.AmigaOS4:&gt; sh
        /AmigaOS4&gt;myprog arg1 arrg2 arg3
</pre>
<h3>Limitations of Perl under AmigaOS 4.1</h3>
<dl>
<dt><code>Nested Piped programs can crash when run from older abc-shells</code></p>
<dd> abc-shell version 53.2 has a bug that can cause crashes in the subprocesses used to run piped programs, if a later version is available you should install it instead.</p>
<dt><code>Incorrect or unexpected command line unescaping</code></p>
<dd> newlib.library 53.30 and earlier incorrectly unescape slashed escape sequences e.g. \&quot; 
 	 etc requiring unusual extra escaping.</p>
<dt><code>Starting subprocesses via open has limitations</code></p>
<dd>
<pre>
        open FH, &quot;command |&quot;
</pre>
<p> Subprocesses started with open use a minimal <code>popen()</code> routine and therefore they do not return pids usable with waitpid etc.</p>
<dt>If you find any other limitations or bugs then let me know.</p>
<dd> Please report bugs in this version of perl to andy [at] broad.ology.org.uk in the first instance.</dl>
<h2>INSTALLATION</h2>
<p> This guide assumes you have obtained a prebuilt archive from os4depot.net. </p>
<p> Unpack the main archive to a temporary location (<font SIZE="-1">RAM:</font> is fine). </p>
<p> Execute the provided install script from shell or via its icon. </p>
<p> You <code>must not</code> attempt to install by hand. </p>
<p> Once installed you may delete the temporary archive. </p>
<p> This approach will preserve links in the installation without creating duplicate binaries. </p>
<p> If you have the earlier ports perl 5.16 or 5.8 installed you may like to rename your perl executable to perl516 or perl58 or something similar before the installation of 5.22.1, this will allow you to use both versions at the same time.</p>
<h2>Amiga Specific Modules</h2>
<h3>Amiga::ARexx</h3>
<p> The Amiga::ARexx module allows you to easily create a perl based ARexx host or to send ARexx commands to other programs. </p>
<p> Try <tt>&quot;perldoc Amiga::ARexx&quot;</tt> for more info.</p>
<h3>Amiga::Exec</h3>
<p> The Amiga::Exec module introduces support for <code>Wait()</code>. </p>
<p> Try <tt>&quot;perldoc Amiga::Exec&quot;</tt> for more info.</p>
<h2>BUILDING</h2>
<p> To build perl under AmigaOS from the patched sources you will need to have a recent version of the <font SIZE="-1">SDK.</font> Version 53.29 is recommended, earlier versions will probably work too. </p>
<p> With the help of Jarkko Hietaniemi the Configure system has been tweaked to run under abc-shell so the recommend build process is as follows. </p>
<pre>
        stack 2000000
        sh Configure -de
        gmake
</pre>
<p> This will build the default setup that installs under SDK:local/newlib/lib/</p>
<h2>CHANGES</h2>
<dl>
<dt><code>August 2015</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>Port to Perl 5.22</p>
<dd>
<dt>Add handling of <font SIZE="-1">NIL:</font> to <code>afstat()</code></p>
<dd>
<dt>Fix inheritance of environment variables by subprocesses.</p>
<dd>
<dt>Fix exec, and exit in &quot;forked&quot; subprocesses.</p>
<dd>
<dt>Fix issue with newlib&#8217;s unlink, which could cause infinite loops.</p>
<dd>
<dt>Add <code>flock()</code> emulation using <font SIZE="-1">IDOS-</font>&gt;LockRecord thanks to Tony Cook for the suggestion.</p>
<dd>
<dt>Fix issue where kill was using the wrong kind of process <font SIZE="-1">ID</font></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>27th November 2013</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>Create new installation system based on installperl links and Amiga protection bits now set correctly.</p>
<dd>
<dt>Pod now defaults to text.</p>
<dd>
<dt>File::Spec should now recognise an Amiga style absolute path as well as an Unix style one. Relative paths must always be Unix style.</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>20th November 2013</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>Configured to use SDK:Local/C/perl to start standard scripts</p>
<dd>
<dt>Added Amiga::Exec module with support for <code>Wait()</code> and AmigaOS signal numbers.</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>10th October 13</code></p>
<dd> First release of port to 5.16.3.</dl>
<h2>SEE ALSO</h2>
<p> You like this port? See &lt;<a rel="nofollow" href="http://www.broad.ology.org.uk/amiga/">http://www.broad.ology.org.uk/amiga/</a>&gt; for how you can help. </p>
<h2>Index</h2>
