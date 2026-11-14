---
title: "cpan(1)"
name: "cpan"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cpan/"
description: "cpan – easily interact with CPAN from the command line"
---

<h2 class="name">NAME</h2>
<p> cpan &#8211; easily interact with CPAN from the command line </p>
<h2>SYNOPSIS</h2>
<pre><code>
#with arguments and no switches, installs specified modules
cpan module_name[module_name...]
#with switches, installs modules with extra behavior
    cpan[-cfFimtTw] module_name[module_name...]
#use local::lib
    cpan -
    I module_name[module_name...]
#one time mirror override for faster mirrors
    cpan -
    p...
#with just the dot, install from the distribution in the
#current directory
    cpan.
#without arguments, starts CPAN.pm shell
    cpan
#without arguments, but some switches
        cpan[-ahpruvACDLOPX]
</code></pre>
<h2>DESCRIPTION</h2>
<p> This script provides a command interface (not a shell) to <font SIZE="-1">CPAN.</font> At the moment it uses <font SIZE="-1">CPAN</font>.pm to do the work, but it is not a one-shot command runner for <font SIZE="-1">CPAN</font>.pm.</p>
<h3>Options</h3>
<dl>
<dt>-a</p>
<dd> Creates a <font SIZE="-1">CPAN</font>.pm autobundle with CPAN::Shell-&gt;autobundle.</p>
<dt>-A module [ module &#8230; ]</p>
<dd> Shows the primary maintainers for the specified modules.</p>
<dt>-c module</p>
<dd> Runs a `make clean` in the specified module&#8217;s directories.</p>
<dt>-C module [ module &#8230; ]</p>
<dd> Show the <i>Changes</i> files for the specified modules</p>
<dt>-D module [ module &#8230; ]</p>
<dd> Show the module details. This prints one line for each out-of-date module (meaning, modules locally installed but have newer versions on <font SIZE="-1">CPAN</font>). Each line has three columns: module name, local version, and <font SIZE="-1">CPAN</font> version.</p>
<dt>-f</p>
<dd> Force the specified action, when it normally would have failed. Use this to install a module even if its tests fail. When you use this option, -i is not optional for installing a module when you need to force it: </p>
<pre>
        % cpan -f -i Module::Foo
</pre>
<dt>-F</p>
<dd> Turn off <font SIZE="-1">CPAN</font>.pm&#8217;s attempts to lock anything. You should be careful with this since you might end up with multiple scripts trying to muck in the same directory. This isn&#8217;t so much of a concern if you&#8217;re loading a special config with <tt>&quot;-j&quot;</tt>, and that config sets up its own work directories.</p>
<dt>-g module [ module &#8230; ]</p>
<dd> Downloads to the current directory the latest distribution of the module.</p>
<dt>-G module [ module &#8230; ]</p>
<dd> <font SIZE="-1">UNIMPLEMENTED</font> </p>
<p> Download to the current directory the latest distribution of the modules, unpack each distribution, and create a git repository for each distribution. </p>
<p> If you want this feature, check out Yanick Champoux&#8217;s <tt>&quot;Git::CPAN::Patch&quot;</tt> distribution.</p>
<dt>-h</p>
<dd> Print a help message and exit. When you specify <tt>&quot;-h&quot;</tt>, it ignores all of the other options and arguments.</p>
<dt>-i module [ module &#8230; ]</p>
<dd> Install the specified modules. With no other switches, this switch is implied.</p>
<dt>-I</p>
<dd> Load <tt>&quot;local::lib&quot;</tt> (think like <tt>&quot;-I&quot;</tt> for loading lib paths). Too bad <tt>&quot;-l&quot;</tt> was already taken.</p>
<dt>-j Config.pm</p>
<dd> Load the file that has the <font SIZE="-1">CPAN</font> configuration data. This should have the same format as the standard <i>CPAN/Config.pm</i> file, which defines <tt>$CPAN::Config</tt> as an anonymous hash.</p>
<dt>-J</p>
<dd> Dump the configuration in the same format that <font SIZE="-1">CPAN</font>.pm uses. This is useful for checking the configuration as well as using the dump as a starting point for a new, custom configuration.</p>
<dt>-l</p>
<dd> List all installed modules with their versions</p>
<dt>-L author [ author &#8230; ]</p>
<dd> List the modules by the specified authors.</p>
<dt>-m</p>
<dd> Make the specified modules.</p>
<dt>-M mirror1,mirror2,&#8230;</p>
<dd> A comma-separated list of mirrors to use for just this run. The <tt>&quot;-P&quot;</tt> option can find them for you automatically.</p>
<dt>-n</p>
<dd> Do a dry run, but don&#8217;t actually install anything. (unimplemented)</p>
<dt>-O</p>
<dd> Show the out-of-date modules.</p>
<dt>-p</p>
<dd> Ping the configured mirrors and print a report</p>
<dt>-P</p>
<dd> Find the best mirrors you could be using and use them for the current session.</p>
<dt>-r</p>
<dd> Recompiles dynamically loaded modules with CPAN::Shell-&gt;recompile.</p>
<dt>-s</p>
<dd> Drop in the <font SIZE="-1">CPAN</font>.pm shell. This command does this automatically if you don&#8217;t specify any arguments.</p>
<dt>-t module [ module &#8230; ]</p>
<dd> Run a `make test` on the specified modules.</p>
<dt>-T</p>
<dd> Do not test modules. Simply install them.</p>
<dt>-u</p>
<dd> Upgrade all installed modules. Blindly doing this can really break things, so keep a backup.</p>
<dt>-v</p>
<dd> Print the script version and <font SIZE="-1">CPAN</font>.pm version then exit.</p>
<dt>-V</p>
<dd> Print detailed information about the cpan client.</p>
<dt>-w</p>
<dd> <font SIZE="-1">UNIMPLEMENTED</font> </p>
<p> Turn on cpan warnings. This checks various things, like directory permissions, and tells you about problems you might have.</p>
<dt>-x module [ module &#8230; ]</p>
<dd> Find close matches to the named modules that you think you might have mistyped. This requires the optional installation of Text::Levenshtein or Text::Levenshtein::Damerau.</p>
<dt>-X</p>
<dd> Dump all the namespaces to standard output.</dl>
<h3>Examples</h3>
<pre>
        # print a help message
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
        cpan -Ti CGI::Minimal URI
</pre>
<h3>Environment variables</h3>
<p> There are several components in <font SIZE="-1">CPAN</font>.pm that use environment variables. The build tools, ExtUtils::MakeMaker and Module::Build use some, while others matter to the levels above them. Some of these are specified by the Perl Toolchain Gang: </p>
<p> Lancaster Concensus: &lt;<a rel="nofollow" href="https://github.com/Perl-Toolchain-Gang/toolchain-site/blob/master/lancaster-consensus.md">https://github.com/Perl-Toolchain-Gang/toolchain-site/blob/master/lancaster-consensus.md</a>&gt; </p>
<p> Oslo Concensus: &lt;<a rel="nofollow" href="https://github.com/Perl-Toolchain-Gang/toolchain-site/blob/master/oslo-consensus.md">https://github.com/Perl-Toolchain-Gang/toolchain-site/blob/master/oslo-consensus.md</a>&gt;</p>
<dl>
<dt><font SIZE="-1">NONINTERACTIVE_TESTING</font></p>
<dd> Assume no one is paying attention and skips prompts for distributions that do that correctly. <tt><a href="/docs/linux/man/1-cpan/">cpan</a>(1)</tt> sets this to <tt>1</tt> unless it already has a value (even if that value is false).</p>
<dt><font SIZE="-1">PERL_MM_USE_DEFAULT</font></p>
<dd> Use the default answer for a prompted questions. <tt><a href="/docs/linux/man/1-cpan/">cpan</a>(1)</tt> sets this to <tt>1</tt> unless it already has a value (even if that value is false).</p>
<dt><font SIZE="-1">CPAN_OPTS</font></p>
<dd> As with <tt>&quot;PERL5OPT&quot;</tt>, a string of additional <tt><a href="/docs/linux/man/1-cpan/">cpan</a>(1)</tt> options to add to those you specify on the command line.</p>
<dt><font SIZE="-1">CPANSCRIPT_LOGLEVEL</font></p>
<dd> The log level to use, with either the embedded, minimal logger or Log::Log4perl if it is installed. Possible values are the same as the <tt>&quot;Log::Log4perl&quot;</tt> levels: <tt>&quot;TRACE&quot;</tt>, <tt>&quot;DEBUG&quot;</tt>, <tt>&quot;INFO&quot;</tt>, <tt>&quot;WARN&quot;</tt>, <tt>&quot;ERROR&quot;</tt>, and <tt>&quot;FATAL&quot;</tt>. The default is <tt>&quot;INFO&quot;</tt>.</p>
<dt><font SIZE="-1">GIT_COMMAND</font></p>
<dd> The path to the <tt>&quot;git&quot;</tt> binary to use for the Git features. The default is <tt>&quot;/usr/local/bin/git&quot;</tt>.</dl>
<h2>EXIT VALUES</h2>
<p> The script exits with zero if it thinks that everything worked, or a positive number if it thinks that something failed. Note, however, that in some cases it has to divine a failure by the output of things it does not control. For now, the exit codes are vague: </p>
<pre>
        1       An unknown error
        2       The was an external problem
        4       There was an internal problem with the script
        8       A module failed to install
</pre>
<h2>TO DO</h2>
<p> * one shot configuration values from the command line</p>
<h2>BUGS</h2>
<p> * none noted</p>
<h2>SEE ALSO</h2>
<p> Most behaviour, including environment variables and configuration, comes directly from <font SIZE="-1">CPAN</font>.pm.</p>
<h2>SOURCE AVAILABILITY</h2>
<p> This code is in Github in the <font SIZE="-1">CPAN</font>.pm repository: </p>
<pre>
        <a rel="nofollow" href="https://github.com/andk/cpanpm">https://github.com/andk/cpanpm</a>
</pre>
<p> The source used to be tracked separately in another GitHub repo, but the canonical source is now in the above repo.</p>
<h2>CREDITS</h2>
<p> Japheth Cleaver added the bits to allow a forced install (-f). </p>
<p> Jim Brandt suggest and provided the initial implementation for the up-to-date and Changes features. </p>
<p> Adam Kennedy pointed out that <code>exit()</code> causes problems on Windows where this script ends up with a .bat extension</p>
<h2>AUTHOR</h2>
<p> brian d foy, <tt>&quot;&lt;bdfoy [at] cpan.org&gt;&quot;</tt></p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2001-2015, brian d foy, All Rights Reserved. </p>
<p> You may redistribute this under the same terms as Perl itself. </p>
<h2>Index</h2>
