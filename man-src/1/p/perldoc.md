---
title: "perldoc(1)"
name: "perldoc"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perldoc/"
description: "perldoc – Look up Perl documentation in Pod format."
---

<h2 class="name">NAME</h2>
<p> perldoc &#8211; Look up Perl documentation in Pod format. </p>
<h2>SYNOPSIS</h2>
<pre><code>
perldoc[-h][-D][-t][-u][-m][-l][-U][-F]
       [-i][-V][-T][-r]
       [-d destination_file]
       [-o formatname]
       [-M FormatterClassName]
    [-w formatteroption:value]
       [-n nroff - replacement]
       [-X]
       [-L language_code] PageName |
    ModuleName | ProgramName | URL
</code></pre>
<p> Examples: </p>
<pre>
    perldoc -f BuiltinFunction
    perldoc -L it -f BuiltinFunction
    perldoc -q FAQ Keyword
    perldoc -L fr -q FAQ Keyword
    perldoc -v PerlVariable
    perldoc -a PerlAPI
</pre>
<p> See below for more description of the switches.</p>
<h2>DESCRIPTION</h2>
<p> <code>perldoc</code> looks up documentation in .pod format that is embedded in the perl installation tree or in a perl script, and displays it using a variety of formatters. This is primarily used for the documentation for the perl library modules. </p>
<p> Your system may also have man pages installed for those modules, in which case you can probably just use the <code><a href="/docs/linux/man/1-man/">man</a></code>(1) command. </p>
<p> If you are looking for a table of contents to the Perl library modules documentation, see the perltoc page.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Prints out a brief <code>h</code>elp message.</p>
<dt><code>-D</code></p>
<dd> <code>D</code>escribes search for the item in <code>d</code>etail.</p>
<dt><code>-t</code></p>
<dd> Display docs using plain <code>t</code>ext converter, instead of nroff. This may be faster, but it probably won&#8217;t look as nice.</p>
<dt><code>-u</code></p>
<dd> Skip the real Pod formatting, and just show the raw Pod source (<code>U</code>nformatted)</p>
<dt><code>-m</code> <i>module</i></p>
<dd> Display the entire module: both code and unformatted pod documentation. This may be useful if the docs don&#8217;t explain a function in the detail you need, and you&#8217;d like to inspect the code directly; perldoc will find the file for you and simply hand it off for display.</p>
<dt><code>-l</code></p>
<dd> Display on<code>l</code>y the file name of the module found.</p>
<dt><code>-U</code></p>
<dd> When running as the superuser, don&#8217;t attempt drop privileges for security. This option is implied with <code>-F</code>. </p>
<p> <font SIZE="-1"><code>NOTE</code></font>: Please see the heading <font SIZE="-1">SECURITY</font> below for more information.</p>
<dt><code>-F</code></p>
<dd> Consider arguments as file names; no search in directories will be performed. Implies <code>-U</code> if run as the superuser.</p>
<dt><code>-f</code> <i>perlfunc</i></p>
<dd> The <code>-f</code> option followed by the name of a perl built-in function will extract the documentation of this function from perlfunc. </p>
<p> Example: </p>
<pre>
      perldoc -f sprintf
</pre>
<dt><code>-q</code> <i>perlfaq-search-regexp</i></p>
<dd> The <code>-q</code> option takes a regular expression as an argument. It will search the <code>q</code>uestion headings in perlfaq[1-9] and print the entries matching the regular expression. </p>
<p> Example: </p>
<pre>
     perldoc -q shuffle
</pre>
<dt><code>-a</code> <i>perlapifunc</i></p>
<dd> The <code>-a</code> option followed by the name of a perl api function will extract the documentation of this function from perlapi. </p>
<p> Example: </p>
<pre>
     perldoc -a newHV
</pre>
<dt><code>-v</code> <i>perlvar</i></p>
<dd> The <code>-v</code> option followed by the name of a Perl predefined variable will extract the documentation of this variable from perlvar. </p>
<p> Examples: </p>
<pre>
     perldoc -v '$&quot;'
     perldoc -v @+
     perldoc -v DATA
</pre>
<dt><code>-T</code></p>
<dd> This specifies that the output is not to be sent to a pager, but is to be sent directly to <font SIZE="-1">STDOUT.</font></p>
<dt><code>-d</code> <i>destination-filename</i></p>
<dd> This specifies that the output is to be sent neither to a pager nor to <font SIZE="-1">STDOUT,</font> but is to be saved to the specified filename. Example: <tt>&quot;perldoc -oLaTeX -dtextwrapdocs.tex Text::Wrap&quot;</tt></p>
<dt><code>-o</code> <i>output-formatname</i></p>
<dd> This specifies that you want Perldoc to try using a Pod-formatting class for the output format that you specify. For example: <tt>&quot;-oman&quot;</tt>. This is actually just a wrapper around the <tt>&quot;-M&quot;</tt> switch; using <tt>&quot;-o</tt>formatname<tt>&quot;</tt> just looks for a loadable class by adding that format name (with different capitalizations) to the end of different classname prefixes. </p>
<p> For example, <tt>&quot;-oLaTeX&quot;</tt> currently tries all of the following classes: Pod::Perldoc::ToLaTeX Pod::Perldoc::Tolatex Pod::Perldoc::ToLatex Pod::Perldoc::ToLATEX Pod::Simple::LaTeX Pod::Simple::latex Pod::Simple::Latex Pod::Simple::LATEX Pod::LaTeX Pod::latex Pod::Latex Pod::LATEX.</p>
<dt><code>-M</code> <i>module-name</i></p>
<dd> This specifies the module that you want to try using for formatting the pod. The class must at least provide a <tt>&quot;parse_from_file&quot;</tt> method. For example: <tt>&quot;perldoc -MPod::Perldoc::ToChecker&quot;</tt>. </p>
<p> You can specify several classes to try by joining them with commas or semicolons, as in <tt>&quot;-MTk::SuperPod;Tk::Pod&quot;</tt>.</p>
<dt><code>-w</code> <i>option:value</i> or <code>-w</code> <i>option</i></p>
<dd> This specifies an option to call the formatter <code>w</code>ith. For example, <tt>&quot;-w textsize:15&quot;</tt> will call <tt>&quot;$formatter-&gt;textsize(15)&quot;</tt> on the formatter object before it is used to format the object. For this to be valid, the formatter class must provide such a method, and the value you pass should be valid. (So if <tt>&quot;textsize&quot;</tt> expects an integer, and you do <tt>&quot;-w textsize:big&quot;</tt>, expect trouble.) </p>
<p> You can use <tt>&quot;-w optionname&quot;</tt> (without a value) as shorthand for <tt>&quot;-w optionname:</tt>TRUE<tt>&quot;</tt>. This is presumably useful in cases of on/off features like: <tt>&quot;-w page_numbering&quot;</tt>. </p>
<p> You can use an &#8220;=&#8221; instead of the &#8220;:&#8221;, as in: <tt>&quot;-w textsize=15&quot;</tt>. This might be more (or less) convenient, depending on what shell you use.</p>
<dt><code>-X</code></p>
<dd> Use an index if it is present. The <code>-X</code> option looks for an entry whose basename matches the name given on the command line in the file <tt>&quot;$Config{archlib}/pod.idx&quot;</tt>. The <i>pod.idx</i> file should contain fully qualified filenames, one per line.</p>
<dt><code>-L</code> <i>language_code</i></p>
<dd> This allows one to specify the <i>language code</i> for the desired language translation. If the <tt>&quot;POD2::&lt;language_code&gt;&quot;</tt> package isn&#8217;t installed in your system, the switch is ignored. All available translation packages are to be found under the <tt>&quot;POD2::&quot;</tt> namespace. See <font SIZE="-1">POD2::IT</font> (or <font SIZE="-1">POD2::FR</font>) to see how to create new localized <tt>&quot;POD2::*&quot;</tt> documentation packages and integrate them into Pod::Perldoc.</p>
<dt><code>PageName|ModuleName|ProgramName|URL</code></p>
<dd> The item you want to look up. Nested modules (such as <tt>&quot;File::Basename&quot;</tt>) are specified either as <tt>&quot;File::Basename&quot;</tt> or <tt>&quot;File/Basename&quot;</tt>. You may also give a descriptive name of a page, such as <tt>&quot;perlfunc&quot;</tt>. For URLs, <font SIZE="-1">HTTP</font> and <font SIZE="-1">HTTPS</font> are the only kind currently supported. </p>
<p> For simple names like &#8216;foo&#8217;, when the normal search fails to find a matching page, a search with the &#8220;perl&#8221; prefix is tried as well. So &#8220;perldoc intro&#8221; is enough to find/render &#8220;perlintro.pod&#8221;.</p>
<dt><code>-n</code> <i>some-formatter</i></p>
<dd> Specify replacement for groff</p>
<dt><code>-r</code></p>
<dd> Recursive search.</p>
<dt><code>-i</code></p>
<dd> Ignore case.</p>
<dt><code>-V</code></p>
<dd> Displays the version of perldoc you&#8217;re running.</dl>
<h2>SECURITY</h2>
<p> Because <code>perldoc</code> does not run properly tainted, and is known to have security issues, when run as the superuser it will attempt to drop privileges by setting the effective and real IDs to nobody&#8217;s or nouser&#8217;s account, or -2 if unavailable. If it cannot relinquish its privileges, it will not run. </p>
<p> See the <tt>&quot;-U&quot;</tt> option if you do not want this behavior but <code>beware</code> that there are significant security risks if you choose to use <tt>&quot;-U&quot;</tt>. </p>
<p> Since 3.26, using <tt>&quot;-F&quot;</tt> as the superuser also implies <tt>&quot;-U&quot;</tt> as opening most files and traversing directories requires privileges that are above the nobody/nogroup level.</p>
<h2>ENVIRONMENT</h2>
<p> Any switches in the <tt>&quot;PERLDOC&quot;</tt> environment variable will be used before the command line arguments. </p>
<p> Useful values for <tt>&quot;PERLDOC&quot;</tt> include <tt>&quot;-oterm&quot;</tt>, <tt>&quot;-otext&quot;</tt>, <tt>&quot;-ortf&quot;</tt>, <tt>&quot;-oxml&quot;</tt>, and so on, depending on what modules you have on hand; or the formatter class may be specified exactly with <tt>&quot;-MPod::Perldoc::ToTerm&quot;</tt> or the like. </p>
<p> <tt>&quot;perldoc&quot;</tt> also searches directories specified by the <tt>&quot;PERL5LIB&quot;</tt> (or <tt>&quot;PERLLIB&quot;</tt> if <tt>&quot;PERL5LIB&quot;</tt> is not defined) and <tt>&quot;PATH&quot;</tt> environment variables. (The latter is so that embedded pods for executables, such as <tt>&quot;perldoc&quot;</tt> itself, are available.) </p>
<p> In directories where either <tt>&quot;Makefile.PL&quot;</tt> or <tt>&quot;Build.PL&quot;</tt> exist, <tt>&quot;perldoc&quot;</tt> will add <tt>&quot;.&quot;</tt> and <tt>&quot;lib&quot;</tt> first to its search path, and as long as you&#8217;re not the superuser will add <tt>&quot;blib&quot;</tt> too. This is really helpful if you&#8217;re working inside of a build directory and want to read through the docs even if you have a version of a module previously installed. </p>
<p> <tt>&quot;perldoc&quot;</tt> will use, in order of preference, the pager defined in <tt>&quot;PERLDOC_PAGER&quot;</tt>, <tt>&quot;MANPAGER&quot;</tt>, or <tt>&quot;PAGER&quot;</tt> before trying to find a pager on its own. (<tt>&quot;MANPAGER&quot;</tt> is not used if <tt>&quot;perldoc&quot;</tt> was told to display plain text or unformatted pod.) </p>
<p> When using perldoc in it&#8217;s <tt>&quot;-m&quot;</tt> mode (display module source code), <tt>&quot;perldoc&quot;</tt> will attempt to use the pager set in <tt>&quot;PERLDOC_SRC_PAGER&quot;</tt>. A useful setting for this command is your favorite editor as in <tt>&quot;/usr/bin/nano&quot;</tt>. (Don&#8217;t judge me.) </p>
<p> One useful value for <tt>&quot;PERLDOC_PAGER&quot;</tt> is <tt>&quot;less -+C -E&quot;</tt>. </p>
<p> Having <font SIZE="-1">PERLDOCDEBUG</font> set to a positive integer will make perldoc emit even more descriptive output than the <tt>&quot;-D&quot;</tt> switch does; the higher the number, the more it emits.</p>
<h2>CHANGES</h2>
<p> Up to 3.14_05, the switch <code>-v</code> was used to produce verbose messages of <code>perldoc</code> operation, which is now enabled by <code>-D</code>.</p>
<h2>SEE ALSO</h2>
<p> perlpod, Pod::Perldoc</p>
<h2>AUTHOR</h2>
<p> Current maintainer: Mark Allen <tt>&quot;&lt;mallen [at] cpan.org&gt;&quot;</tt> </p>
<p> Past contributors are: brian d foy <tt>&quot;&lt;bdfoy [at] cpan.org&gt;&quot;</tt> Adriano R. Ferreira <tt>&quot;&lt;ferreira [at] cpan.org&gt;&quot;</tt>, Sean M. Burke <tt>&quot;&lt;sburke [at] cpan.org&gt;&quot;</tt>, Kenneth Albanowski <tt>&quot;&lt;kjahds [at] kjahds.com&gt;&quot;</tt>, Andy Dougherty <tt>&quot;&lt;doughera [at] lafcol.lafayette.edu&gt;&quot;</tt>, and many others. </p>
<h2>Index</h2>
