---
title: "ptksh(1)"
name: "ptksh"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ptksh/"
description: "ptksh – Perl/Tk script to provide a graphical user interface for testing Perl/Tk commands and scripts."
---

<h2 class="name">NAME</h2>
<p> ptksh &#8211; Perl/Tk script to provide a graphical user interface for testing Perl/Tk commands and scripts. </p>
<h2>SYNOPSIS</h2>
<pre><code>
% ptksh ? scriptfile ? ... version information... ptksh &gt; $b = $mw-&gt;Button(-text = &gt; 'Hi', -command = &gt; sub{print 'Hi'})
                                                                   ptksh &gt; $b-&gt;pack
                                                                               ptksh &gt; o $b... list of options... ptksh &gt; help... help information... ptksh &gt; exit %
</code></pre>
<h2>DESCRIPTION</h2>
<p> ptksh is a perl/Tk shell to enter perl commands interactively. When one starts ptksh a MainWindow is automaticly created, along with a ptksh command window. One can access the main window by typing commands using the variable <tt>$mw</tt> at the &#8216;ptksh&gt; &#8216; prompt of the command window. </p>
<p> ptksh supports command line editing and history. Just type &#8220;&lt;Up&gt;&#8221; at the command prompt to see a history list. The last 50 commands entered are saved, then reloaded into history list the next time you start ptksh. </p>
<p> ptksh supports some convenient commands for inspecting Tk widgets. See below. </p>
<p> To exit ptksh use: <tt>&quot;exit&quot;</tt>. </p>
<p> ptksh is <code>*not*</code> a full symbolic debugger. To debug perl/Tk programs at a low level use the more powerful perl debugger. (Just enter &#8220;O tk&#8221; on debuggers command line to start the Tk eventloop.)</p>
<h2>FEATURES</h2>
<h3>History</h3>
<p> Press &lt;Up&gt; (the Up Arrow) in the perlwish window to obtain a gui-based history list. Press &lt;Enter&gt; on any history line to enter it into the perlwish window. Then hit return. So, for example, repeat last command is &lt;Up&gt;&lt;Enter&gt;&lt;Enter&gt;. You can quit the history window with &lt;Escape&gt;. <font SIZE="-1">NOTE:</font> history is only saved if exit is &#8220;graceful&#8221; (i.e. by the &#8220;exit&#8221; command from the console or by quitting all main windows&#8212;NOT by interrupt).</p>
<h3>Debugging Support</h3>
<p> ptksh provides some convenience function to make browsing in perl/Tk widget easier:</p>
<dl>
<dt><code>?</code>, or <code>h</code></p>
<dd> displays a short help summary.</p>
<dt><code>d</code>, or <code>x</code> ?<i>args</i>, &#8230;?</p>
<dd> Dumps recursively arguments to stdout. (see Data::Dumper). You must have &lt;Data::Dumper&gt; installed to support this feature. </p>
<p> <code>x</code> was introduced for perl debugger compatibility.</p>
<dt><code>p</code> ?<i>arg</i>, &#8230;?</p>
<dd> appends &#8220;|
&#8221; to each of it&#8217;s arguments and prints it. If value is <code>undef</code>, &#8216;(undef)&#8217; is printed to stdout.</p>
<dt><code>o</code> <i>$widget</i> ?<i>-option</i> &#8230;?</p>
<dd> prints the option(s) of <i></i>$widget<i></i> one on each line. If no options are given all options of the widget are listed. See Tk::options for more details on the format and contents of the returned list.</p>
<dt><code>o</code> <i>$widget</i> <code>/</code><i>regexp</i><code>/</code></p>
<dd> Lists options of <i></i>$widget<i></i> matching the regular expression <i>regexp</i>.</p>
<dt><code>u</code> ?<i>class</i>?</p>
<dd> If no argument is given it lists the modules loaded by the commands you executed or since the last time you called <tt>&quot;u&quot;</tt>. </p>
<p> If argument is the empty string lists all modules that are loaded by ptksh. </p>
<p> If argument is a string, &#8220;text&#8221; it tries to do a &#8220;use Tk::Text;&#8221;.</dl>
<h3>Packages</h3>
<p> Ptksh compiles into package Tk::ptksh. Your code is eval&#8217;ed into package main. The coolness of this is that your eval code should not interfere with ptksh itself.</p>
<h3>Multiline Commands</h3>
<p> ptksh will accept multiline commands. Simply put a &#8220;\&#8221; character immediately before the newline, and ptksh will continue your command onto the next line.</p>
<h3>Source File Support</h3>
<p> If you have a perl/Tk script that you want to do debugging on, try running the command </p>
<pre>
  ptksh&gt; do 'myscript';
   -- or  (at shell command prompt) --
  % ptksh myscript
</pre>
<p> Then use the perl/Tk commands to try out different operations on your script.</p>
<h2>ENVIRONMENT</h2>
<p> Looks for your .ptksh_history in the directory specified by the <tt>$HOME</tt> environment variable ($HOMEPATH on Win32 systems).</p>
<h2>FILES</h2>
<dl>
<dt><i>.ptksh_init</i></p>
<dd> If found in current directory it is read in an evaluated after the mainwindow <i></i>$mw<i></i> is created. <i>.ptksh_init</i> can contain any valid perl code.</p>
<dt><i>~/.ptksh_history</i></p>
<dd> Contains the last 50 lines entered in ptksh session(s).</dl>
<h2>PITFALLS</h2>
<p> It is best not to use &#8220;my&#8221; in the commands you type into ptksh. For example &#8220;my <tt>$v</tt>&#8221; will make <tt>$v</tt> local just to the command or commands entered until &lt;Return&gt; is pressed. For a related reason, there are no file-scopy &#8220;my&#8221; variables in the ptksh code itself (else the user might trounce on them by accident).</p>
<h2>BUGS</h2>
<p> <code>Tk::MainLoop</code> function interactively entered or sourced in a init or script file will block ptksh.</p>
<h2>SEE ALSO</h2>
<p> Tk perldebug</p>
<h2>VERSION</h2>
<p> <font SIZE="-1">VERSION 2.03</font></p>
<h2>AUTHORS</h2>
<p> Mike Beller &lt;beller [at] penvision.com&gt;, Achim Bohnet &lt;ach [at] mpe.mpg.de&gt; </p>
<p> Copyright (c) 1996 &#8211; 1998 Achim Bohnet and Mike Beller. All rights reserved. This program is free software; you can redistribute it and/or modify it under the same terms as Perl itself. </p>
<h2>Index</h2>
