---
title: "cpan5-26-x86_64-linux-gnu(1)"
name: "cpan5-26-x86_64-linux-gnu"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cpan5-26-x86_64-linux-gnu/"
---

cpan - easily interact with CPAN from the command line 

<h2>Synopsis</h2><pre> # with arguments and no switches, installs specified modules
 cpan module_name [ module_name ... ]
 # with switches, installs modules with extra behavior
 cpan [-cfFimtTw] module_name [ module_name ... ]
 # use local::lib
 cpan -I module_name [ module_name ... ]
 # one time mirror override for faster mirrors
 cpan -p ...
 # with just the dot, install from the distribution in the
 # current directory
 cpan .
 # without arguments, starts CPAN.pm shell
 cpan
 # without arguments, but some switches
 cpan [-ahpruvACDLOPX]</pre><h2>Description</h2>This script provides a command interface (not a shell) to <font SIZE="-1">CPAN.</font> At the moment it uses <font SIZE="-1">CPAN</font>.pm to do the work, but it is not a one-shot command runner for <font SIZE="-1">CPAN</font>.pm.
<h3>Options</h3><dl><dt>-a
<dd>Creates a <font SIZE="-1">CPAN</font>.pm autobundle with CPAN::Shell-&gt;autobundle.
<dt>-A module [ module ... ]
<dd>Shows the primary maintainers for the specified modules.
<dt>-c module
<dd>Runs a `make clean` in the specified module's directories.
<dt>-C module [ module ... ]
<dd>Show the <i>Changes</i> files for the specified modules
<dt>-D module [ module ... ]
<dd>Show the module details. This prints one line for each out-of-date module (meaning, modules locally installed but have newer versions on <font SIZE="-1">CPAN</font>). Each line has three columns: module name, local version, and <font SIZE="-1">CPAN</font> version.
<dt>-f
<dd>Force the specified action, when it normally would have failed. Use this to install a module even if its tests fail. When you use this option, -i is not optional for installing a module when you need to force it: 

 <pre> % cpan -f -i Module::Foo</pre><dt>-F
<dd>Turn off <font SIZE="-1">CPAN</font>.pm's attempts to lock anything. You should be careful with this since you might end up with multiple scripts trying to muck in the same directory. This isn't so much of a concern if you're loading a special config with <tt>&quot;-j&quot;</tt>, and that config sets up its own work directories.
<dt>-g module [ module ... ]
<dd>Downloads to the current directory the latest distribution of the module.
<dt>-G module [ module ... ]
<dd><font SIZE="-1">UNIMPLEMENTED</font> 

 Download to the current directory the latest distribution of the modules, unpack each distribution, and create a git repository for each distribution. 

 If you want this feature, check out Yanick Champoux's <tt>&quot;Git::CPAN::Patch&quot;</tt> distribution.
<dt>-h
<dd>Print a help message and exit. When you specify <tt>&quot;-h&quot;</tt>, it ignores all of the other options and arguments.
<dt>-i module [ module ... ]
<dd>Install the specified modules. With no other switches, this switch is implied.
<dt>-I
<dd>Load <tt>&quot;local::lib&quot;</tt> (think like <tt>&quot;-I&quot;</tt> for loading lib paths). Too bad <tt>&quot;-l&quot;</tt> was already taken.
<dt>-j Config.pm
<dd>Load the file that has the <font SIZE="-1">CPAN</font> configuration data. This should have the same format as the standard <i>CPAN/Config.pm</i> file, which defines <tt>$CPAN::Config</tt> as an anonymous hash.
<dt>-J
<dd>Dump the configuration in the same format that <font SIZE="-1">CPAN</font>.pm uses. This is useful for checking the configuration as well as using the dump as a starting point for a new, custom configuration.
<dt>-l
<dd>List all installed modules with their versions
<dt>-L author [ author ... ]
<dd>List the modules by the specified authors.
<dt>-m
<dd>Make the specified modules.
<dt>-M mirror1,mirror2,...
<dd>A comma-separated list of mirrors to use for just this run. The <tt>&quot;-P&quot;</tt> option can find them for you automatically.
<dt>-n
<dd>Do a dry run, but don't actually install anything. (unimplemented)
<dt>-O
<dd>Show the out-of-date modules.
<dt>-p
<dd>Ping the configured mirrors and print a report
<dt>-P
<dd>Find the best mirrors you could be using and use them for the current session.
<dt>-r
<dd>Recompiles dynamically loaded modules with CPAN::Shell-&gt;recompile.
<dt>-s
<dd>Drop in the <font SIZE="-1">CPAN</font>.pm shell. This command does this automatically if you don't specify any arguments.
<dt>-t module [ module ... ]
<dd>Run a `make test` on the specified modules.
<dt>-T
<dd>Do not test modules. Simply install them.
<dt>-u
<dd>Upgrade all installed modules. Blindly doing this can really break things, so keep a backup.
<dt>-v
<dd>Print the script version and <font SIZE="-1">CPAN</font>.pm version then exit.
<dt>-V
<dd>Print detailed information about the cpan client.
<dt>-w
<dd><font SIZE="-1">UNIMPLEMENTED</font> 

 Turn on cpan warnings. This checks various things, like directory permissions, and tells you about problems you might have.
<dt>-x module [ module ... ]
<dd>Find close matches to the named modules that you think you might have mistyped. This requires the optional installation of Text::Levenshtein or Text::Levenshtein::Damerau.
<dt>-X
<dd>Dump all the namespaces to standard output.</dl><h3>Examples</h3><pre> # print a help message
 cpan -h
 # print the version numbers
 cpan -v
 # create an autobundle
 cpan -a
 # recompile modules
 cpan -r
 # upgrade all installed modules
 cpan -u
 # install modules ( sole -i is optional )
 cpan -i Netscape::Booksmarks Business::ISBN
 # force install modules ( must use -i )
 cpan -fi CGI::Minimal URI
 # install modules but without testing them
 cpan -Ti CGI::Minimal URI</pre><h3>Environment variables</h3>There are several components in <font SIZE="-1">CPAN</font>.pm that use environment variables. The build tools, ExtUtils::MakeMaker and Module::Build use some, while others matter to the levels above them. Some of these are specified by the Perl Toolchain Gang: 

 Lancaster Concensus: &lt;<a rel="nofollow" HREF="https://github.com/Perl-Toolchain-Gang/toolchain-site/blob/master/lancaster-consensus.md">https://github.com/Perl-Toolchain-Gang/toolchain-site/blob/master/lancaster-consensus.md</a>&gt; 

 Oslo Concensus: &lt;<a rel="nofollow" HREF="https://github.com/Perl-Toolchain-Gang/toolchain-site/blob/master/oslo-consensus.md">https://github.com/Perl-Toolchain-Gang/toolchain-site/blob/master/oslo-consensus.md</a>&gt;
<dl><dt><font SIZE="-1">NONINTERACTIVE_TESTING</font>
<dd>Assume no one is paying attention and skips prompts for distributions that do that correctly. <tt><a HREF="/docs/linux/man/1-cpan/">cpan</a>(1)</tt> sets this to <tt>1</tt> unless it already has a value (even if that value is false).
<dt><font SIZE="-1">PERL_MM_USE_DEFAULT</font>
<dd>Use the default answer for a prompted questions. <tt><a HREF="/docs/linux/man/1-cpan/">cpan</a>(1)</tt> sets this to <tt>1</tt> unless it already has a value (even if that value is false).
<dt><font SIZE="-1">CPAN_OPTS</font>
<dd>As with <tt>&quot;PERL5OPTS&quot;</tt>, a string of additional <tt><a HREF="/docs/linux/man/1-cpan/">cpan</a>(1)</tt> options to add to those you specify on the command line.
<dt><font SIZE="-1">CPANSCRIPT_LOGLEVEL</font>
<dd>The log level to use, with either the embedded, minimal logger or Log::Log4perl if it is installed. Possible values are the same as the <tt>&quot;Log::Log4perl&quot;</tt> levels: <tt>&quot;TRACE&quot;</tt>, <tt>&quot;DEBUG&quot;</tt>, <tt>&quot;INFO&quot;</tt>, <tt>&quot;WARN&quot;</tt>, <tt>&quot;ERROR&quot;</tt>, and <tt>&quot;FATAL&quot;</tt>. The default is <tt>&quot;INFO&quot;</tt>.
<dt><font SIZE="-1">GIT_COMMAND</font>
<dd>The path to the <tt>&quot;git&quot;</tt> binary to use for the Git features. The default is <tt>&quot;/usr/local/bin/git&quot;</tt>.</dl><h2>Exit Values</h2>The script exits with zero if it thinks that everything worked, or a positive number if it thinks that something failed. Note, however, that in some cases it has to divine a failure by the output of things it does not control. For now, the exit codes are vague: 

 <pre> 1 An unknown error
 2 The was an external problem
 4 There was an internal problem with the script
 8 A module failed to install</pre><h2>To Do</h2>* one shot configuration values from the command line
<h2>Bugs</h2>* none noted
<h2>See Also</h2>Most behaviour, including environment variables and configuration, comes directly from <font SIZE="-1">CPAN</font>.pm.
<h2>Source Availability</h2>This code is in Github in the <font SIZE="-1">CPAN</font>.pm repository: 

 <pre> <a rel="nofollow" HREF="https://github.com/andk/cpanpm">https://github.com/andk/cpanpm</a></pre>The source used to be tracked separately in another GitHub repo, but the canonical source is now in the above repo.
<h2>Credits</h2>Japheth Cleaver added the bits to allow a forced install (-f). 

 Jim Brandt suggest and provided the initial implementation for the up-to-date and Changes features. 

 Adam Kennedy pointed out that <i>exit()</i> causes problems on Windows where this script ends up with a .bat extension
<h2>Author</h2>brian d foy, <tt>&quot;&lt;bdfoy [at] cpan.org&gt;&quot;</tt>
<h2>Copyright</h2>Copyright (c) 2001-2015, brian d foy, All Rights Reserved. 

 You may redistribute this under the same terms as Perl itself.
