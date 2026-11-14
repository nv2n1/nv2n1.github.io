---
title: "perlfaq3(1)"
name: "perlfaq3"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perlfaq3/"
description: "perlfaq3 – Programming Tools"
---

<h2 class="name">NAME</h2>
<p> perlfaq3 &#8211; Programming Tools </p>
<h2>VERSION</h2>
<p> version 5.20190126</p>
<h2>DESCRIPTION</h2>
<p> This section of the <font SIZE="-1">FAQ</font> answers questions related to programmer tools and programming support.</p>
<h3>How do I do (anything)?</h3>
<p> Have you looked at <font SIZE="-1">CPAN</font> (see perlfaq2)? The chances are that someone has already written a module that can solve your problem. Have you read the appropriate manpages? Here&#8217;s a brief index:</p>
<dl>
<dt>Basics</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>perldata &#8211; Perl data types</p>
<dd>
<dt>perlvar &#8211; Perl pre-defined variables</p>
<dd>
<dt>perlsyn &#8211; Perl syntax</p>
<dd>
<dt>perlop &#8211; Perl operators and precedence</p>
<dd>
<dt>perlsub &#8211; Perl subroutines</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>Execution</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>perlrun &#8211; how to execute the Perl interpreter</p>
<dd>
<dt>perldebug &#8211; Perl debugging</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>Functions</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>perlfunc &#8211; Perl builtin functions</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>Objects</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>perlref &#8211; Perl references and nested data structures</p>
<dd>
<dt>perlmod &#8211; Perl modules (packages and symbol tables)</p>
<dd>
<dt>perlobj &#8211; Perl objects</p>
<dd>
<dt>perltie &#8211; how to hide an object class in a simple variable</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>Data Structures</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>perlref &#8211; Perl references and nested data structures</p>
<dd>
<dt>perllol &#8211; Manipulating arrays of arrays in Perl</p>
<dd>
<dt>perldsc &#8211; Perl Data Structures Cookbook</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>Modules</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>perlmod &#8211; Perl modules (packages and symbol tables)</p>
<dd>
<dt>perlmodlib &#8211; constructing new Perl modules and finding existing ones</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>Regexes</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>perlre &#8211; Perl regular expressions</p>
<dd>
<dt>perlfunc &#8211; Perl builtin functions&gt;</p>
<dd>
<dt>perlop &#8211; Perl operators and precedence</p>
<dd>
<dt>perllocale &#8211; Perl locale handling (internationalization and localization)</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>Moving to perl5</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>perltrap &#8211; Perl traps for the unwary</p>
<dd>
<dt>perl</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>Linking with C</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>perlxstut &#8211; Tutorial for writing XSUBs</p>
<dd>
<dt>perlxs &#8211; <font SIZE="-1">XS</font> language reference manual</p>
<dd>
<dt>perlcall &#8211; Perl calling conventions from C</p>
<dd>
<dt>perlguts &#8211; Introduction to the Perl <font SIZE="-1">API</font></p>
<dd>
<dt>perlembed &#8211; how to embed perl in your C program</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>Various</p>
<dd> &lt;<a rel="nofollow" href="http://www.cpan.org/misc/olddoc/FMTEYEWTK.tgz">http://www.cpan.org/misc/olddoc/FMTEYEWTK.tgz</a>&gt; (not a man-page but still useful, a collection of various essays on Perl techniques)</dl>
<p> A crude table of contents for the Perl manpage set is found in perltoc.</p>
<h3>How can I use Perl interactively?</h3>
<p> The typical approach uses the Perl debugger, described in the <code><a href="/docs/linux/man/1-perldebug/">perldebug</a></code>(1) manpage, on an &#8220;empty&#8221; program, like this: </p>
<pre>
    perl -de 42
</pre>
<p> Now just type in any legal Perl code, and it will be immediately evaluated. You can also examine the symbol table, get stack backtraces, check variable values, set breakpoints, and other operations typically found in symbolic debuggers. </p>
<p> You can also use Devel::REPL which is an interactive shell for Perl, commonly known as a <font SIZE="-1">REPL</font> &#8211; Read, Evaluate, Print, Loop. It provides various handy features.</p>
<h3>How do I find which modules are installed on my system?</h3>
<p> From the command line, you can use the <tt>&quot;cpan&quot;</tt> command&#8217;s <tt>&quot;-l&quot;</tt> switch: </p>
<pre>
    $ cpan -l
</pre>
<p> You can also use <tt>&quot;cpan&quot;</tt>&#8216;s <tt>&quot;-a&quot;</tt> switch to create an autobundle file that <tt>&quot;CPAN.pm&quot;</tt> understands and can use to re-install every module: </p>
<pre>
    $ cpan -a
</pre>
<p> Inside a Perl program, you can use the ExtUtils::Installed module to show all installed distributions, although it can take awhile to do its magic. The standard library which comes with Perl just shows up as &#8220;Perl&#8221; (although you can get those with Module::CoreList). </p>
<pre><code>
use ExtUtils::Installed;
my $inst = ExtUtils::Installed-&gt;new ();
my @modules = $inst-&gt;modules();
</code></pre>
<p> If you want a list of all of the Perl module filenames, you can use File::Find::Rule: </p>
<p>use File::Find::Rule;<br />
my @files = File::Find::Rule-&gt;extras({follow = &gt; 1})-&gt;file()-&gt;name(&#8216;*.pm&#8217;)-&gt;in(@INC);</p>
<p> If you do not have that module, you can do the same thing with File::Find which is part of the standard library: </p>
<p>use File::Find;<br />
my @files;<br />
find(<br />
    {<br />
        wanted = &gt; sub{<br />
                       push @files, $File::Find::fullname if &#8211; f $File::Find::fullname &amp;&amp; /\.pm$ / },<br />
        follow = &gt; 1,<br />
        follow_skip = &gt; 2,<br />
    },<br />
    @INC);<br />
print join &#8220;
&#8221;, @files;</p>
<p> If you simply need to check quickly to see if a module is available, you can check for its documentation. If you can read the documentation the module is most likely installed. If you cannot read the documentation, the module might not have any (in rare cases): </p>
<pre>
    $ perldoc Module::Name
</pre>
<p> You can also try to include the module in a one-liner to see if perl finds it: </p>
<pre>
    $ perl -MModule::Name -e1
</pre>
<p> (If you don&#8217;t receive a &#8220;Can&#8217;t locate &#8230; in <tt>@INC</tt>&#8221; error message, then Perl found the module name you asked for.)</p>
<h3>How do I debug my Perl programs?</h3>
<p> (contributed by brian d foy) </p>
<p> Before you do anything else, you can help yourself by ensuring that you let Perl tell you about problem areas in your code. By turning on warnings and strictures, you can head off many problems before they get too big. You can find out more about these in strict and warnings. </p>
<pre>
    #!/usr/bin/perl
    use strict;
    use warnings;
</pre>
<p> Beyond that, the simplest debugger is the <tt>&quot;print&quot;</tt> function. Use it to look at values as you run your program: </p>
<pre>
    print STDERR &quot;The value is [$value]
&quot;;
</pre>
<p> The Data::Dumper module can pretty-print Perl data structures: </p>
<p>use Data::Dumper qw(Dumper);<br />
print STDERR &#8220;The hash is &#8220;.Dumper( \% hash).&#8221;
&#8221;;</p>
<p> Perl comes with an interactive debugger, which you can start with the <tt>&quot;-d&quot;</tt> switch. It&#8217;s fully explained in perldebug. </p>
<p> If you&#8217;d like a graphical user interface and you have Tk, you can use <tt>&quot;ptkdb&quot;</tt>. It&#8217;s on <font SIZE="-1">CPAN</font> and available for free. </p>
<p> If you need something much more sophisticated and controllable, Leon Brocard&#8217;s Devel::ebug (which you can call with the <tt>&quot;-D&quot;</tt> switch as <tt>&quot;-Debug&quot;</tt>) gives you the programmatic hooks into everything you need to write your own (without too much pain and suffering). </p>
<p> You can also use a commercial debugger such as Affrus (Mac <font SIZE="-1">OS X</font>), Komodo from Activestate (Windows and Mac <font SIZE="-1">OS X</font>), or <font SIZE="-1">EPIC</font> (most platforms).</p>
<h3>How do I profile my Perl programs?</h3>
<p> (contributed by brian d foy, updated Fri Jul 25 12:22:26 <font SIZE="-1">PDT 2008</font>) </p>
<p> The <tt>&quot;Devel&quot;</tt> namespace has several modules which you can use to profile your Perl programs. </p>
<p> The Devel::NYTProf (New York Times Profiler) does both statement and subroutine profiling. It&#8217;s available from <font SIZE="-1">CPAN</font> and you also invoke it with the <tt>&quot;-d&quot;</tt> switch: </p>
<pre>
    perl -d:NYTProf some_perl.pl
</pre>
<p> It creates a database of the profile information that you can turn into reports. The <tt>&quot;nytprofhtml&quot;</tt> command turns the data into an <font SIZE="-1">HTML</font> report similar to the Devel::Cover report: </p>
<pre>
    nytprofhtml
</pre>
<p> You might also be interested in using the Benchmark to measure and compare code snippets. </p>
<p> You can read more about profiling in <i>Programming Perl</i>, chapter 20, or <i>Mastering Perl</i>, chapter 5. </p>
<p> perldebguts documents creating a custom debugger if you need to create a special sort of profiler. brian d foy describes the process in <i>The Perl Journal</i>, &#8220;Creating a Perl Debugger&#8221;, &lt;<a rel="nofollow" href="http://www.ddj.com/184404522">http://www.ddj.com/184404522</a>&gt; , and &#8220;Profiling in Perl&#8221; &lt;<a rel="nofollow" href="http://www.ddj.com/184404580">http://www.ddj.com/184404580</a>&gt; . </p>
<p> Perl.com has two interesting articles on profiling: &#8220;Profiling Perl&#8221;, by Simon Cozens, &lt;<a rel="nofollow" href="http://www.perl.com/lpt/a/850">http://www.perl.com/lpt/a/850</a>&gt; and &#8220;Debugging and Profiling mod_perl Applications&#8221;, by Frank Wiles, &lt;<a rel="nofollow" href="http://www.perl.com/pub/a/2006/02/09/debug_mod_perl.html">http://www.perl.com/pub/a/2006/02/09/debug_mod_perl.html</a>&gt; . </p>
<p> Randal L. Schwartz writes about profiling in &#8220;Speeding up Your Perl Programs&#8221; for <i>Unix Review</i>, &lt;<a rel="nofollow" href="http://www.stonehenge.com/merlyn/UnixReview/col49.html">http://www.stonehenge.com/merlyn/UnixReview/col49.html</a>&gt; , and &#8220;Profiling in Template Toolkit via Overriding&#8221; for <i>Linux Magazine</i>, &lt;<a rel="nofollow" href="http://www.stonehenge.com/merlyn/LinuxMag/col75.html">http://www.stonehenge.com/merlyn/LinuxMag/col75.html</a>&gt; .</p>
<h3>How do I cross-reference my Perl programs?</h3>
<p> The B::Xref module can be used to generate cross-reference reports for Perl programs. </p>
<pre>
    perl -MO=Xref[,OPTIONS] scriptname.plx
</pre>
<h3>Is there a pretty-printer (formatter) for Perl?</h3>
<p> Perl::Tidy comes with a perl script perltidy which indents and reformats Perl scripts to make them easier to read by trying to follow the rules of the perlstyle. If you write Perl, or spend much time reading Perl, you will probably find it useful. </p>
<p> Of course, if you simply follow the guidelines in perlstyle, you shouldn&#8217;t need to reformat. The habit of formatting your code as you write it will help prevent bugs. Your editor can and should help you with this. The perl-mode or newer cperl-mode for emacs can provide remarkable amounts of help with most (but not all) code, and even less programmable editors can provide significant assistance. Tom Christiansen and many other <font SIZE="-1">VI</font> users swear by the following settings in vi and its clones: </p>
<pre>
    set ai sw=4
    map! ^O {^M}^[O^T
</pre>
<p> Put that in your <i>.exrc</i> file (replacing the caret characters with control characters) and away you go. In insert mode, ^T is for indenting, ^D is for undenting, and ^O is for blockdenting&#8212;as it were. A more complete example, with comments, can be found at &lt;<a rel="nofollow" href="http://www.cpan.org/authors/id/TOMC/scripts/toms.exrc.gz">http://www.cpan.org/authors/id/TOMC/scripts/toms.exrc.gz</a>&gt;</p>
<h3>Is there an <font SIZE="-1">IDE</font> or Windows Perl Editor?</h3>
<p> Perl programs are just plain text, so any editor will do. </p>
<p> If you&#8217;re on Unix, you already have an IDE&#8212;Unix itself. The Unix philosophy is the philosophy of several small tools that each do one thing and do it well. It&#8217;s like a carpenter&#8217;s toolbox. </p>
<p> If you want an <font SIZE="-1">IDE,</font> check the following (in alphabetical order, not order of preference):</p>
<dl>
<dt>Eclipse</p>
<dd> &lt;<a rel="nofollow" href="http://e-p-i-c.sf.net/">http://e-p-i-c.sf.net/</a>&gt; </p>
<p> The Eclipse Perl Integration Project integrates Perl editing/debugging with Eclipse.</p>
<dt>Enginsite</p>
<dd> &lt;<a rel="nofollow" href="http://www.enginsite.com/">http://www.enginsite.com/</a>&gt; </p>
<p> Perl Editor by EngInSite is a complete integrated development environment (<font SIZE="-1">IDE</font>) for creating, testing, and debugging Perl scripts; the tool runs on Windows 9x/NT/2000/XP or later.</p>
<dt>IntelliJ <font SIZE="-1">IDEA</font></p>
<dd> &lt;<a rel="nofollow" href="https://plugins.jetbrains.com/plugin/7796">https://plugins.jetbrains.com/plugin/7796</a>&gt; </p>
<p> Camelcade plugin provides Perl5 support in IntelliJ <font SIZE="-1">IDEA</font> and other JetBrains IDEs.</p>
<dt>Kephra</p>
<dd> &lt;<a rel="nofollow" href="http://kephra.sf.net">http://kephra.sf.net</a>&gt; </p>
<p> <font SIZE="-1">GUI</font> editor written in Perl using wxWidgets and Scintilla with lots of smaller features. Aims for a <font SIZE="-1">UI</font> based on Perl principles like <font SIZE="-1">TIMTOWTDI</font> and &#8220;easy things should be easy, hard things should be possible&#8221;.</p>
<dt>Komodo</p>
<dd> &lt;<a rel="nofollow" href="http://www.ActiveState.com/Products/Komodo/">http://www.ActiveState.com/Products/Komodo/</a>&gt; </p>
<p> ActiveState&#8217;s cross-platform (as of October 2004, that&#8217;s Windows, Linux, and Solaris), multi-language <font SIZE="-1">IDE</font> has Perl support, including a regular expression debugger and remote debugging.</p>
<dt>Notepad++</p>
<dd> &lt;<a rel="nofollow" href="http://notepad-plus.sourceforge.net/">http://notepad-plus.sourceforge.net/</a>&gt;</p>
<dt>Open Perl <font SIZE="-1">IDE</font></p>
<dd> &lt;<a rel="nofollow" href="http://open-perl-ide.sourceforge.net/">http://open-perl-ide.sourceforge.net/</a>&gt; </p>
<p> Open Perl <font SIZE="-1">IDE</font> is an integrated development environment for writing and debugging Perl scripts with ActiveState&#8217;s ActivePerl distribution under Windows 95/98/NT/2000.</p>
<dt>OptiPerl</p>
<dd> &lt;<a rel="nofollow" href="http://www.optiperl.com/">http://www.optiperl.com/</a>&gt; </p>
<p> OptiPerl is a Windows <font SIZE="-1">IDE</font> with simulated <font SIZE="-1">CGI</font> environment, including debugger and syntax-highlighting editor.</p>
<dt>Padre</p>
<dd> &lt;<a rel="nofollow" href="http://padre.perlide.org/">http://padre.perlide.org/</a>&gt; </p>
<p> Padre is cross-platform <font SIZE="-1">IDE</font> for Perl written in Perl using wxWidgets to provide a native look and feel. It&#8217;s open source under the Artistic License. It is one of the newer Perl IDEs.</p>
<dt>PerlBuilder</p>
<dd> &lt;<a rel="nofollow" href="http://www.solutionsoft.com/perl.htm">http://www.solutionsoft.com/perl.htm</a>&gt; </p>
<p> PerlBuilder is an integrated development environment for Windows that supports Perl development.</p>
<dt>visiPerl+</p>
<dd> &lt;<a rel="nofollow" href="http://helpconsulting.net/visiperl/index.html">http://helpconsulting.net/visiperl/index.html</a>&gt; </p>
<p> From Help Consulting, for Windows.</p>
<dt>Visual Perl</p>
<dd> &lt;<a rel="nofollow" href="http://www.activestate.com/Products/Visual_Perl/">http://www.activestate.com/Products/Visual_Perl/</a>&gt; </p>
<p> Visual Perl is a Visual Studio.NET plug-in from ActiveState.</p>
<dt>Zeus</p>
<dd> &lt;<a rel="nofollow" href="http://www.zeusedit.com/lookmain.html">http://www.zeusedit.com/lookmain.html</a>&gt; </p>
<p> Zeus for Windows is another Win32 multi-language editor/IDE that comes with support for Perl.</dl>
<p> For editors: if you&#8217;re on Unix you probably have vi or a vi clone already, and possibly an emacs too, so you may not need to download anything. In any emacs the cperl-mode (M-x cperl-mode) gives you perhaps the best available Perl editing mode in any editor. </p>
<p> If you are using Windows, you can use any editor that lets you work with plain text, such as NotePad or WordPad. Word processors, such as Microsoft Word or WordPerfect, typically do not work since they insert all sorts of behind-the-scenes information, although some allow you to save files as &#8220;Text Only&#8221;. You can also download text editors designed specifically for programming, such as Textpad ( &lt;<a rel="nofollow" href="http://www.textpad.com/">http://www.textpad.com/</a>&gt; ) and UltraEdit ( &lt;<a rel="nofollow" href="http://www.ultraedit.com/">http://www.ultraedit.com/</a>&gt; ), among others. </p>
<p> If you are using MacOS, the same concerns apply. MacPerl (for Classic environments) comes with a simple editor. Popular external editors are BBEdit ( &lt;<a rel="nofollow" href="http://www.barebones.com/products/bbedit/">http://www.barebones.com/products/bbedit/</a>&gt; ) or Alpha ( &lt;<a rel="nofollow" href="http://www.his.com/~jguyer/Alpha/Alpha8.html">http://www.his.com/~jguyer/Alpha/Alpha8.html</a>&gt; ). MacOS X users can use Unix editors as well.</p>
<dl>
<dt><font SIZE="-1">GNU</font> Emacs</p>
<dd> &lt;<a rel="nofollow" href="http://www.gnu.org/software/emacs/windows/ntemacs.html">http://www.gnu.org/software/emacs/windows/ntemacs.html</a>&gt;</p>
<dt>MicroEMACS</p>
<dd> &lt;<a rel="nofollow" href="http://www.microemacs.de/">http://www.microemacs.de/</a>&gt;</p>
<dt>XEmacs</p>
<dd> &lt;<a rel="nofollow" href="http://www.xemacs.org/Download/index.html">http://www.xemacs.org/Download/index.html</a>&gt;</p>
<dt>Jed</p>
<dd> &lt;<a rel="nofollow" href="http://space.mit.edu/~davis/jed/">http://space.mit.edu/~davis/jed/</a>&gt;</dl>
<p> or a vi clone such as</p>
<dl>
<dt>Vim</p>
<dd> &lt;<a rel="nofollow" href="http://www.vim.org/">http://www.vim.org/</a>&gt;</p>
<dt>Vile</p>
<dd> &lt;<a rel="nofollow" href="http://dickey.his.com/vile/vile.html">http://dickey.his.com/vile/vile.html</a>&gt;</dl>
<p> The following are Win32 multilanguage editor/IDEs that support Perl:</p>
<dl>
<dt>MultiEdit</p>
<dd> &lt;<a rel="nofollow" href="http://www.MultiEdit.com/">http://www.MultiEdit.com/</a>&gt;</p>
<dt>SlickEdit</p>
<dd> &lt;<a rel="nofollow" href="http://www.slickedit.com/">http://www.slickedit.com/</a>&gt;</p>
<dt>ConTEXT</p>
<dd> &lt;<a rel="nofollow" href="http://www.contexteditor.org/">http://www.contexteditor.org/</a>&gt;</dl>
<p> There is also a toyedit Text widget based editor written in Perl that is distributed with the Tk module on <font SIZE="-1">CPAN.</font> The ptkdb ( &lt;<a rel="nofollow" href="http://ptkdb.sourceforge.net/">http://ptkdb.sourceforge.net/</a>&gt; ) is a Perl/Tk-based debugger that acts as a development environment of sorts. Perl Composer ( &lt;<a rel="nofollow" href="http://perlcomposer.sourceforge.net/">http://perlcomposer.sourceforge.net/</a>&gt; ) is an <font SIZE="-1">IDE</font> for Perl/Tk <font SIZE="-1">GUI</font> creation. </p>
<p> In addition to an editor/IDE you might be interested in a more powerful shell environment for Win32. Your options include</p>
<dl>
<dt>bash</p>
<dd> from the Cygwin package ( &lt;<a rel="nofollow" href="http://cygwin.com/">http://cygwin.com/</a>&gt; )</p>
<dt>zsh</p>
<dd> &lt;<a rel="nofollow" href="http://www.zsh.org/">http://www.zsh.org/</a>&gt;</dl>
<p> Cygwin is covered by the <font SIZE="-1">GNU</font> General Public License (but that shouldn&#8217;t matter for Perl use). Cygwin contains (in addition to the shell) a comprehensive set of standard Unix toolkit utilities.</p>
<dl>
<dt>BBEdit and TextWrangler</p>
<dd> are text editors for <font SIZE="-1">OS X</font> that have a Perl sensitivity mode ( &lt;<a rel="nofollow" href="http://www.barebones.com/">http://www.barebones.com/</a>&gt; ).</dl>
<h3>Where can I get Perl macros for vi?</h3>
<p> For a complete version of Tom Christiansen&#8217;s vi configuration file, see &lt;<a rel="nofollow" href="http://www.cpan.org/authors/Tom_Christiansen/scripts/toms.exrc.gz">http://www.cpan.org/authors/Tom_Christiansen/scripts/toms.exrc.gz</a>&gt; , the standard benchmark file for vi emulators. The file runs best with nvi, the current version of vi out of Berkeley, which incidentally can be built with an embedded Perl interpreter&#8212;see &lt;<a rel="nofollow" href="http://www.cpan.org/src/misc/">http://www.cpan.org/src/misc/</a>&gt; .</p>
<h3>Where can I get perl-mode or cperl-mode for emacs?</h3>
<p> Since Emacs version 19 patchlevel 22 or so, there have been both a perl-mode.el and support for the Perl debugger built in. These should come with the standard Emacs 19 distribution. </p>
<p> Note that the perl-mode of emacs will have fits with <tt>&quot;main'foo&quot;</tt> (single quote), and mess up the indentation and highlighting. You are probably using <tt>&quot;main::foo&quot;</tt> in new Perl code anyway, so this shouldn&#8217;t be an issue. </p>
<p> For CPerlMode, see &lt;<a rel="nofollow" href="http://www.emacswiki.org/cgi-bin/wiki/CPerlMode">http://www.emacswiki.org/cgi-bin/wiki/CPerlMode</a>&gt;</p>
<h3>How can I use curses with Perl?</h3>
<p> The Curses module from <font SIZE="-1">CPAN</font> provides a dynamically loadable object module interface to a curses library. A small demo can be found at the directory &lt;<a rel="nofollow" href="http://www.cpan.org/authors/Tom_Christiansen/scripts/rep.gz">http://www.cpan.org/authors/Tom_Christiansen/scripts/rep.gz</a>&gt; ; this program repeats a command and updates the screen as needed, rendering <code>rep ps axu</code> similar to <code>top</code>.</p>
<h3>How can I write a <font SIZE="-1">GUI</font> (X, Tk, Gtk, etc.) in Perl?</h3>
<p> (contributed by Ben Morrow) </p>
<p> There are a number of modules which let you write GUIs in Perl. Most <font SIZE="-1">GUI</font> toolkits have a perl interface: an incomplete list follows.</p>
<dl>
<dt>Tk</p>
<dd> This works under Unix and Windows, and the current version doesn&#8217;t look half as bad under Windows as it used to. Some of the gui elements still don&#8217;t &#8216;feel&#8217; quite right, though. The interface is very natural and &#8216;perlish&#8217;, making it easy to use in small scripts that just need a simple gui. It hasn&#8217;t been updated in a while.</p>
<dt>Wx</p>
<dd> This is a Perl binding for the cross-platform wxWidgets toolkit ( &lt;<a rel="nofollow" href="http://www.wxwidgets.org">http://www.wxwidgets.org</a>&gt; ). It works under Unix, Win32 and Mac <font SIZE="-1">OS X,</font> using native widgets (Gtk under Unix). The interface follows the C<font SIZE="-2">++</font> interface closely, but the documentation is a little sparse for someone who doesn&#8217;t know the library, mostly just referring you to the C<font SIZE="-2">++</font> documentation.</p>
<dt>Gtk and Gtk2</p>
<dd> These are Perl bindings for the Gtk toolkit ( &lt;<a rel="nofollow" href="http://www.gtk.org">http://www.gtk.org</a>&gt; ). The interface changed significantly between versions 1 and 2 so they have separate Perl modules. It runs under Unix, Win32 and Mac <font SIZE="-1">OS X</font> (currently it requires an X server on Mac <font SIZE="-1">OS,</font> but a &#8216;native&#8217; port is underway), and the widgets look the same on every platform: i.e., they don&#8217;t match the native widgets. As with Wx, the Perl bindings follow the C <font SIZE="-1">API</font> closely, and the documentation requires you to read the C documentation to understand it.</p>
<dt>Win32::GUI</p>
<dd> This provides access to most of the Win32 <font SIZE="-1">GUI</font> widgets from Perl. Obviously, it only runs under Win32, and uses native widgets. The Perl interface doesn&#8217;t really follow the C interface: it&#8217;s been made more Perlish, and the documentation is pretty good. More advanced stuff may require familiarity with the C Win32 APIs, or reference to <font SIZE="-1">MSDN.</font></p>
<dt>CamelBones</p>
<dd> CamelBones ( &lt;<a rel="nofollow" href="http://camelbones.sourceforge.net">http://camelbones.sourceforge.net</a>&gt; ) is a Perl interface to Mac <font SIZE="-1">OS X</font>&#8216;s Cocoa <font SIZE="-1">GUI</font> toolkit, and as such can be used to produce native GUIs on Mac <font SIZE="-1">OS X.</font> It&#8217;s not on <font SIZE="-1">CPAN,</font> as it requires frameworks that <font SIZE="-1">CPAN</font>.pm doesn&#8217;t know how to install, but installation is via the standard <font SIZE="-1">OSX</font> package installer. The Perl <font SIZE="-1">API</font> is, again, very close to the ObjC <font SIZE="-1">API</font> it&#8217;s wrapping, and the documentation just tells you how to translate from one to the other.</p>
<dt>Qt</p>
<dd> There is a Perl interface to TrollTech&#8217;s Qt toolkit, but it does not appear to be maintained.</p>
<dt>Athena</p>
<dd> Sx is an interface to the Athena widget set which comes with X, but again it appears not to be much used nowadays.</dl>
<h3>How can I make my Perl program run faster?</h3>
<p> The best way to do this is to come up with a better algorithm. This can often make a dramatic difference. Jon Bentley&#8217;s book <i>Programming Pearls</i> (that&#8217;s not a misspelling!) has some good tips on optimization, too. Advice on benchmarking boils down to: benchmark and profile to make sure you&#8217;re optimizing the right part, look for better algorithms instead of microtuning your code, and when all else fails consider just buying faster hardware. You will probably want to read the answer to the earlier question &#8220;How do I profile my Perl programs?&#8221; if you haven&#8217;t done so already. </p>
<p> A different approach is to autoload seldom-used Perl code. See the AutoSplit and AutoLoader modules in the standard distribution for that. Or you could locate the bottleneck and think about writing just that part in C, the way we used to take bottlenecks in C code and write them in assembler. Similar to rewriting in C, modules that have critical sections can be written in C (for instance, the <font SIZE="-1">PDL</font> module from <font SIZE="-1">CPAN</font>). </p>
<p> If you&#8217;re currently linking your perl executable to a shared <i>libc.so</i>, you can often gain a 10-25% performance benefit by rebuilding it to link with a static libc.a instead. This will make a bigger perl executable, but your Perl programs (and programmers) may thank you for it. See the <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file in the source distribution for more information. </p>
<p> The undump program was an ancient attempt to speed up Perl program by storing the already-compiled form to disk. This is no longer a viable option, as it only worked on a few architectures, and wasn&#8217;t a good solution anyway.</p>
<h3>How can I make my Perl program take less memory?</h3>
<p> When it comes to time-space tradeoffs, Perl nearly always prefers to throw memory at a problem. Scalars in Perl use more memory than strings in C, arrays take more than that, and hashes use even more. While there&#8217;s still a lot to be done, recent releases have been addressing these issues. For example, as of 5.004, duplicate hash keys are shared amongst all hashes using them, so require no reallocation. </p>
<p> In some cases, using <code>substr()</code> or <code>vec()</code> to simulate arrays can be highly beneficial. For example, an array of a thousand booleans will take at least 20,000 bytes of space, but it can be turned into one 125-byte bit vector&#8212;a considerable memory savings. The standard Tie::SubstrHash module can also help for certain types of data structure. If you&#8217;re working with specialist data structures (matrices, for instance) modules that implement these in C may use less memory than equivalent Perl modules. </p>
<p> Another thing to try is learning whether your Perl was compiled with the system malloc or with Perl&#8217;s builtin malloc. Whichever one it is, try using the other one and see whether this makes a difference. Information about malloc is in the <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> file in the source distribution. You can find out whether you are using perl&#8217;s malloc by typing <tt>&quot;perl -V:usemymalloc&quot;</tt>. </p>
<p> Of course, the best way to save memory is to not do anything to waste it in the first place. Good programming practices can go a long way toward this:</p>
<dl>
<dt>Don&#8217;t slurp!</p>
<dd> Don&#8217;t read an entire file into memory if you can process it line by line. Or more concretely, use a loop like this: </p>
<pre>
    #
    # Good Idea
    #
    while (my $line = &lt;$file_handle&gt;) {
       # ...
    }
</pre>
<p> instead of this: </p>
<pre>
    #
    # Bad Idea
    #
    my @data = &lt;$file_handle&gt;;
    foreach (@data) {
        # ...
    }
</pre>
<p> When the files you&#8217;re processing are small, it doesn&#8217;t much matter which way you do it, but it makes a huge difference when they start getting larger.</p>
<dt>Use map and grep selectively</p>
<dd> Remember that both map and grep expect a <font SIZE="-1">LIST</font> argument, so doing this: </p>
<pre>
        @wanted = grep {/pattern/} &lt;$file_handle&gt;;
</pre>
<p> will cause the entire file to be slurped. For large files, it&#8217;s better to loop: </p>
<p>while (&lt;$file_handle&gt;) {<br />
    push(@wanted, $_) if / pattern / ;<br />
}</p>
<dt>Avoid unnecessary quotes and stringification</p>
<dd> Don&#8217;t quote large strings unless absolutely necessary: </p>
<pre>
        my $copy = &quot;$large_string&quot;;
</pre>
<p> makes 2 copies of <tt>$large_string</tt> (one for <tt>$copy</tt> and another for the quotes), whereas </p>
<pre>
        my $copy = $large_string;
</pre>
<p> only makes one copy. </p>
<p> Ditto for stringifying large arrays: </p>
<p>{<br />
    local $, = &#8220;
&#8221;;<br />
    print @big_array;<br />
}</p>
<p> is much more memory-efficient than either </p>
<pre>
    print join &quot;
&quot;, @big_array;
</pre>
<p> or </p>
<p>{<br />
    local $ &#8221; = &#8220;
 &#8220;;<br />
        print &#8220;@big_array&#8221;;<br />
}</p>
<dt>Pass by reference</p>
<dd> Pass arrays and hashes by reference, not by value. For one thing, it&#8217;s the only way to pass multiple lists or hashes (or both) in a single call/return. It also avoids creating a copy of all the contents. This requires some judgement, however, because any changes will be propagated back to the original data. If you really want to mangle (er, modify) a copy, you&#8217;ll have to sacrifice the memory needed to make one.</p>
<dt>Tie large variables to disk</p>
<dd> For &#8220;big&#8221; data stores (i.e. ones that exceed available memory) consider using one of the <font SIZE="-1">DB</font> modules to store it on disk instead of in <font SIZE="-1">RAM.</font> This will incur a penalty in access time, but that&#8217;s probably better than causing your hard disk to thrash due to massive swapping.</dl>
<h3>Is it safe to return a reference to local or lexical data?</h3>
<p> Yes. Perl&#8217;s garbage collection system takes care of this so everything works out right. </p>
<p>sub makeone<br />
{<br />
    my @a = (1..10);<br />
    return \@a;<br />
}<br />
for (1..10) {<br />
    push @many, makeone();<br />
}<br />
print $many[4][5], &#8220;
&#8221;;<br />
print &#8220;@many
&#8221;;</p>
<h3>How can I free an array or hash so my program shrinks?</h3>
<p> (contributed by Michael Carman) </p>
<p> You usually can&#8217;t. Memory allocated to lexicals (i.e. <code>my()</code> variables) cannot be reclaimed or reused even if they go out of scope. It is reserved in case the variables come back into scope. Memory allocated to global variables can be reused (within your program) by using <code>undef()</code> and/or <code>delete()</code>. </p>
<p> On most operating systems, memory allocated to a program can never be returned to the system. That&#8217;s why long-running programs sometimes re- exec themselves. Some operating systems (notably, systems that use <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) for allocating large chunks of memory) can reclaim memory that is no longer used, but on such systems, perl must be configured and compiled to use the <font SIZE="-1">OS</font>&#8216;s malloc, not perl&#8217;s. </p>
<p> In general, memory allocation and de-allocation isn&#8217;t something you can or should be worrying about much in Perl. </p>
<p> See also &#8220;How can I make my Perl program take less memory?&#8221;</p>
<h3>How can I make my <font SIZE="-1">CGI</font> script more efficient?</h3>
<p> Beyond the normal measures described to make general Perl programs faster or smaller, a <font SIZE="-1">CGI</font> program has additional issues. It may be run several times per second. Given that each time it runs it will need to be re-compiled and will often allocate a megabyte or more of system memory, this can be a killer. Compiling into C <code>isn&#8217;t going to help you</code> because the process start-up overhead is where the bottleneck is. </p>
<p> There are three popular ways to avoid this overhead. One solution involves running the Apache <font SIZE="-1">HTTP</font> server (available from &lt;<a rel="nofollow" href="http://www.apache.org/">http://www.apache.org/</a>&gt; ) with either of the mod_perl or mod_fastcgi plugin modules. </p>
<p> With mod_perl and the Apache::Registry module (distributed with mod_perl), httpd will run with an embedded Perl interpreter which pre-compiles your script and then executes it within the same address space without forking. The Apache extension also gives Perl access to the internal server <font SIZE="-1">API,</font> so modules written in Perl can do just about anything a module written in C can. For more on mod_perl, see &lt;<a rel="nofollow" href="http://perl.apache.org/">http://perl.apache.org/</a>&gt; </p>
<p> With the <font SIZE="-1">FCGI</font> module (from <font SIZE="-1">CPAN</font>) and the mod_fastcgi module (available from &lt;<a rel="nofollow" href="http://www.fastcgi.com/">http://www.fastcgi.com/</a>&gt; ) each of your Perl programs becomes a permanent <font SIZE="-1">CGI</font> daemon process. </p>
<p> Finally, Plack is a Perl module and toolkit that contains <font SIZE="-1">PSGI</font> middleware, helpers and adapters to web servers, allowing you to easily deploy scripts which can continue running, and provides flexibility with regards to which web server you use. It can allow existing <font SIZE="-1">CGI</font> scripts to enjoy this flexibility and performance with minimal changes, or can be used along with modern Perl web frameworks to make writing and deploying web services with Perl a breeze. </p>
<p> These solutions can have far-reaching effects on your system and on the way you write your <font SIZE="-1">CGI</font> programs, so investigate them with care. </p>
<p> See also &lt;<a rel="nofollow" href="http://www.cpan.org/modules/by-category/15_World_Wide_Web_HTML_HTTP_CGI/">http://www.cpan.org/modules/by-category/15_World_Wide_Web_HTML_HTTP_CGI/</a>&gt; .</p>
<h3>How can I hide the source for my Perl program?</h3>
<p> Delete it. :-) Seriously, there are a number of (mostly unsatisfactory) solutions with varying levels of &#8220;security&#8221;. </p>
<p> First of all, however, you <i>can&#8217;t</i> take away read permission, because the source code has to be readable in order to be compiled and interpreted. (That doesn&#8217;t mean that a <font SIZE="-1">CGI</font> script&#8217;s source is readable by people on the web, though&#8212;only by people with access to the filesystem.) So you have to leave the permissions at the socially friendly 0755 level. </p>
<p> Some people regard this as a security problem. If your program does insecure things and relies on people not knowing how to exploit those insecurities, it is not secure. It is often possible for someone to determine the insecure things and exploit them without viewing the source. Security through obscurity, the name for hiding your bugs instead of fixing them, is little security indeed. </p>
<p> You can try using encryption via source filters (Starting from Perl 5.8 the Filter::Simple and Filter::Util::Call modules are included in the standard distribution), but any decent programmer will be able to decrypt it. You can try using the byte code compiler and interpreter described later in perlfaq3, but the curious might still be able to de-compile it. You can try using the native-code compiler described later, but crackers might be able to disassemble it. These pose varying degrees of difficulty to people wanting to get at your code, but none can definitively conceal it (true of every language, not just Perl). </p>
<p> It is very easy to recover the source of Perl programs. You simply feed the program to the perl interpreter and use the modules in the B:: hierarchy. The B::Deparse module should be able to defeat most attempts to hide source. Again, this is not unique to Perl. </p>
<p> If you&#8217;re concerned about people profiting from your code, then the bottom line is that nothing but a restrictive license will give you legal security. License your software and pepper it with threatening statements like &#8220;This is unpublished proprietary software of <font SIZE="-1">XYZ</font> Corp. Your access to it does not give you permission to use it blah blah blah.&#8221; We are not lawyers, of course, so you should see a lawyer if you want to be sure your license&#8217;s wording will stand up in court.</p>
<h3>How can I compile my Perl program into byte code or C?</h3>
<p> (contributed by brian d foy) </p>
<p> In general, you can&#8217;t do this. There are some things that may work for your situation though. People usually ask this question because they want to distribute their works without giving away the source code, and most solutions trade disk space for convenience. You probably won&#8217;t see much of a speed increase either, since most solutions simply bundle a Perl interpreter in the final product (but see &#8220;How can I make my Perl program run faster?&#8221;). </p>
<p> The Perl Archive Toolkit is Perl&#8217;s analog to Java&#8217;s <font SIZE="-1">JAR.</font> It&#8217;s freely available and on <font SIZE="-1">CPAN</font> ( &lt;<a rel="nofollow" href="https://metacpan.org/pod/PAR">https://metacpan.org/pod/PAR</a>&gt; ). </p>
<p> There are also some commercial products that may work for you, although you have to buy a license for them. </p>
<p> The Perl Dev Kit ( &lt;<a rel="nofollow" href="http://www.activestate.com/Products/Perl_Dev_Kit/">http://www.activestate.com/Products/Perl_Dev_Kit/</a>&gt; ) from ActiveState can &#8220;Turn your Perl programs into ready-to-run executables for HP-UX, Linux, Solaris and Windows.&#8221; </p>
<p> Perl2Exe ( &lt;<a rel="nofollow" href="http://www.indigostar.com/perl2exe.htm">http://www.indigostar.com/perl2exe.htm</a>&gt; ) is a command line program for converting perl scripts to executable files. It targets both Windows and Unix platforms.</p>
<h3>How can I get #!perl to work on [<font SIZE="-1">MS-DOS,NT,&#8230;</font>]?</h3>
<p> For <font SIZE="-1">OS/2</font> just use </p>
<pre>
    extproc perl -S -your_switches
</pre>
<p> as the first line in <tt>&quot;*.cmd&quot;</tt> file (<tt>&quot;-S&quot;</tt> due to a bug in cmd.exe&#8217;s &#8220;extproc&#8221; handling). For <font SIZE="-1">DOS</font> one should first invent a corresponding batch file and codify it in <tt>&quot;ALTERNATE_SHEBANG&quot;</tt> (see the <i>dosish.h</i> file in the source distribution for more information). </p>
<p> The Win95/NT installation, when using the ActiveState port of Perl, will modify the Registry to associate the <tt>&quot;.pl&quot;</tt> extension with the perl interpreter. If you install another port, perhaps even building your own Win95/NT Perl from the standard sources by using a Windows port of gcc (e.g., with cygwin or mingw32), then you&#8217;ll have to modify the Registry yourself. In addition to associating <tt>&quot;.pl&quot;</tt> with the interpreter, <font SIZE="-1">NT</font> people can use: <tt>&quot;SET PATHEXT=%PATHEXT%;.PL&quot;</tt> to let them run the program <tt>&quot;install-linux.pl&quot;</tt> merely by typing <tt>&quot;install-linux&quot;</tt>. </p>
<p> Under &#8220;Classic&#8221; MacOS, a perl program will have the appropriate Creator and Type, so that double-clicking them will invoke the MacPerl application. Under Mac <font SIZE="-1">OS X,</font> clickable apps can be made from any <tt>&quot;#!&quot;</tt> script using Wil Sanchez&#8217; DropScript utility: &lt;<a rel="nofollow" href="http://www.wsanchez.net/software/">http://www.wsanchez.net/software/</a>&gt; . </p>
<p> <i></i><font SIZE="-1"><i>IMPORTANT</i></font><i>!</i>: Whatever you do, <font SIZE="-1">PLEASE</font> don&#8217;t get frustrated, and just throw the perl interpreter into your cgi-bin directory, in order to get your programs working for a web server. This is an <font SIZE="-1">EXTREMELY</font> big security risk. Take the time to figure out how to do it correctly.</p>
<h3>Can I write useful Perl programs on the command line?</h3>
<p> Yes. Read perlrun for more information. Some examples follow. (These assume standard Unix shell quoting rules.) </p>
<p>#sum first and last fields<br />
perl &#8211; lane &#8216;print $F[0] + $F[-1]&#8217; *<br />
#identify text files<br />
                perl &#8211;<br />
            le &#8216;for(@ARGV) {print if -f &amp;&amp; -T _}&#8217; *<br />
#remove(most) comments from C program<br />
                perl &#8211;<br />
            0777 &#8211; pe &#8216;s{/\*.*?\*/}{}gs&#8217; foo.c<br />
#make file a month younger than today, defeating reaper daemons<br />
                       perl &#8211;<br />
            e &#8216;$X=24*60*60; utime(time(),time() + 30 * $X,@ARGV)&#8217; *<br />
#find first unused uid<br />
                perl &#8211;<br />
            le &#8216;$i++ while getpwuid($i); print $i&#8217;<br />
#display reasonable manpath<br />
            echo $PATH |<br />
        perl &#8211; nl &#8211; 072 &#8211; e &#8216; s ![^ / +] * $ !man !&amp;&amp;-d &amp;&amp;<br />
    !$s<br />
{<br />
    $_<br />
}<br />
++&amp;&amp;push @m, $_;<br />
END<br />
{<br />
    print &#8220;@m&#8221;<br />
}<br />
&#8216;</p>
<p> <font SIZE="-1">OK,</font> the last one was actually an Obfuscated Perl Contest entry. :-)</p>
<h3>Why don&#8217;t Perl one-liners work on my DOS/Mac/VMS system?</h3>
<p> The problem is usually that the command interpreters on those systems have rather different ideas about quoting than the Unix shells under which the one-liners were created. On some systems, you may have to change single-quotes to double ones, which you must <i></i><font SIZE="-1"><i>NOT</i></font><i></i> do on Unix or Plan9 systems. You might also have to change a single % to a %%. </p>
<p> For example: </p>
<pre>
    # Unix (including Mac OS X)
    perl -e 'print &quot;Hello world
&quot;'
    # DOS, etc.
    perl -e &quot;print \&quot;Hello world
\&quot;&quot;
    # Mac Classic
    print &quot;Hello world
&quot;
     (then Run &quot;Myscript&quot; or Shift-Command-R)
    # MPW
    perl -e 'print &quot;Hello world
&quot;'
    # VMS
    perl -e &quot;print &quot;&quot;Hello world
&quot;&quot;&quot;
</pre>
<p> The problem is that none of these examples are reliable: they depend on the command interpreter. Under Unix, the first two often work. Under <font SIZE="-1">DOS,</font> it&#8217;s entirely possible that neither works. If 4DOS was the command shell, you&#8217;d probably have better luck like this: </p>
<pre>
  perl -e &quot;print &lt;Ctrl-x&gt;&quot;Hello world
&lt;Ctrl-x&gt;&quot;&quot;
</pre>
<p> Under the Mac, it depends which environment you are using. The MacPerl shell, or <font SIZE="-1">MPW,</font> is much like Unix shells in its support for several quoting variants, except that it makes free use of the Mac&#8217;s non-ASCII characters as control characters. </p>
<p> Using <code>qq()</code>, q(), and <code>qx()</code>, instead of &#8220;double quotes&#8221;, &#8216;single quotes&#8217;, and `backticks`, may make one-liners easier to write. </p>
<p> There is no general solution to all of this. It is a mess. </p>
<p> [Some of this answer was contributed by Kenneth Albanowski.]</p>
<h3>Where can I learn about <font SIZE="-1">CGI</font> or Web programming in Perl?</h3>
<p> For modules, get the <font SIZE="-1">CGI</font> or <font SIZE="-1">LWP</font> modules from <font SIZE="-1">CPAN.</font> For textbooks, see the two especially dedicated to web stuff in the question on books. For problems and questions related to the web, like &#8220;Why do I get 500 Errors&#8221; or &#8220;Why doesn&#8217;t it run from the browser right when it runs fine on the command line&#8221;, see the troubleshooting guides and references in perlfaq9 or in the <font SIZE="-1">CGI</font> MetaFAQ: </p>
<pre>
    L&lt;<a rel="nofollow" href="http://www.perl.org/CGI_MetaFAQ.html">http://www.perl.org/CGI_MetaFAQ.html</a>&gt;
</pre>
<p> Looking in to Plack and modern Perl web frameworks is highly recommended, though; web programming in Perl has evolved a long way from the old days of simple <font SIZE="-1">CGI</font> scripts.</p>
<h3>Where can I learn about object-oriented Perl programming?</h3>
<p> A good place to start is perlootut, and you can use perlobj for reference. </p>
<p> A good book on <font SIZE="-1">OO</font> on Perl is the &#8220;Object-Oriented Perl&#8221; by Damian Conway from Manning Publications, or &#8220;Intermediate Perl&#8221; by Randal Schwartz, brian d foy, and Tom Phoenix from O&#8217;Reilly Media.</p>
<h3>Where can I learn about linking C with Perl?</h3>
<p> If you want to call C from Perl, start with perlxstut, moving on to perlxs, xsubpp, and perlguts. If you want to call Perl from C, then read perlembed, perlcall, and perlguts. Don&#8217;t forget that you can learn a lot from looking at how the authors of existing extension modules wrote their code and solved their problems. </p>
<p> You might not need all the power of <font SIZE="-1">XS.</font> The Inline::C module lets you put C code directly in your Perl source. It handles all the magic to make it work. You still have to learn at least some of the perl <font SIZE="-1">API</font> but you won&#8217;t have to deal with the complexity of the <font SIZE="-1">XS</font> support files.</p>
<h3>I&#8217;ve read perlembed, perlguts, etc., but I can&#8217;t embed perl in my C program; what am I doing wrong?</h3>
<p> Download the ExtUtils::Embed kit from <font SIZE="-1">CPAN</font> and run `make test&#8217;. If the tests pass, read the pods again and again and again. If they fail, see perlbug and send a bug report with the output of <tt>&quot;make test TEST_VERBOSE=1&quot;</tt> along with <tt>&quot;perl -V&quot;</tt>.</p>
<h3>When I tried to run my script, I got this message. What does it mean?</h3>
<p> A complete list of Perl&#8217;s error messages and warnings with explanatory text can be found in perldiag. You can also use the splain program (distributed with Perl) to explain the error messages: </p>
<pre><code>
perl program 2 &gt; diag.out
                     splain[-v][-p] diag.out
</code></pre>
<p> or change your program to explain the messages for you: </p>
<pre>
    use diagnostics;
</pre>
<p> or </p>
<pre>
    use diagnostics -verbose;
</pre>
<h3>What&#8217;s MakeMaker?</h3>
<p> (contributed by brian d foy) </p>
<p> The ExtUtils::MakeMaker module, better known simply as &#8220;MakeMaker&#8221;, turns a Perl script, typically called <tt>&quot;Makefile.PL&quot;</tt>, into a Makefile. The Unix tool <tt>&quot;make&quot;</tt> uses this file to manage dependencies and actions to process and install a Perl distribution.</p>
<h2>AUTHOR AND COPYRIGHT</h2>
<p> Copyright (c) 1997-2010 Tom Christiansen, Nathan Torkington, and other authors as noted. All rights reserved. </p>
<p> This documentation is free; you can redistribute it and/or modify it under the same terms as Perl itself. </p>
<p> Irrespective of its distribution, all code examples here are in the public domain. You are permitted and encouraged to use this code and any derivatives thereof in your own programs for fun or for profit as you see fit. A simple comment in the code giving credit to the <font SIZE="-1">FAQ</font> would be courteous but is not required. </p>
<h2>Index</h2>
<dt><a href="#lbBG">AUTHOR AND COPYRIGHT</a></p>
<dd></dl>
