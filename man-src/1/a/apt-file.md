---
title: "apt-file(1)"
name: "apt-file"
section: "1"
letter: "a"
url: "/docs/linux/man/1-apt-file/"
description: "apt-file — APT package searching utility — command-line interface"
---

<h2 class="name">NAME</h2>
<p> apt-file &#8212; APT package searching utility &#8212; command-line interface </p>
<h2>SYNOPSIS</h2>
<p> <code>apt-file</code> [<i>options</i>] search <i>pattern</i> </p>
<p> <code>apt-file</code> [<i>options</i>] show <i>package</i></p>
<h2>DESCRIPTION</h2>
<p> <code>apt-file</code> is a command line tool for searching files in packages for the <font SIZE="-1">APT</font> package management system. </p>
<p> Some actions are required to run the search:</p>
<dl>
<dt>find</p>
<dd> Alias for search.</p>
<dt>list</p>
<dd> List the contents of a package. This action is very close to the <code>dpkg -L</code> command except the package does not need to be installed or fetched. </p>
<p> By default, the <code>list</code> action interprets its pattern as if <code>&#8211;fixed-string</code> was specified.</p>
<dt>list-indices</p>
<dd> List the known Content indices and their status in a human readable format. These indices can be searched via the <code>-I</code> option (when enabled and after fetching the indices). The output is subject to change without notice and is therefore unsuited for script usage / automation. </p>
<p> For a machine-readable formats (e.g. automation), please use <code>apt-config dump</code> (search for options starting with <code>Acquire::IndexTargets</code>) and <code>apt-get indextargets</code> for checking the cache (Look for entries with an <i>Identifier</i> field starting with <i>Contents-</i>). </p>
<p> Note that individual sources.list entries can override the global default. Please consult <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5) for more information on advanced configuration of the <code>sources.list</code> files.</p>
<dt>search</p>
<dd> Search in which package a file is included. A list of all packages containing the pattern pattern is returned. </p>
<p> Since Contents files does not contain directories, the pattern must match (part of a) file name. </p>
<p> By default, the <code>search</code> action interprets its pattern as if <code>&#8211;substring-match</code> was specified.</p>
<dt>show</p>
<dd> Alias for list.</p>
<dt>update</p>
<dd> This action that just calls <code>apt update</code> or <code>apt-get update</code> (depending on whether a tty is available). </p>
<p> The only advantage using this over a regular <code>apt update</code> or <code>apt-get update</code> directly is for the case where you have configured an apt-file specific configuration (via the <code>Dir::Etc::apt-file-main</code> configuration option). In that case, said configuration will be included automatically.</dl>
<h2>OPTIONS</h2>
<p> The following options are available:</p>
<dl>
<dt>-a, &#8211;architecture <i>architecture[,&#8230;]</i></p>
<dd> This option is useful if you search a package for a different architecture from the one installed on your system. </p>
<p> It can be a comma-separated list for searching on multiple architectures.</p>
<dt>-c, &#8211;config-file <i></i><font SIZE="-1"><i>APT</i></font><i> config-file</i></p>
<dd> Configuration File; Specify a configuration file to use. The program will read the default configuration file and then this configuration file. If configuration settings need to be set before the default configuration files are parsed specify a file with the <font SIZE="-1"><code>APT_CONFIG</code></font> environment variable. See <code><a href="/docs/linux/man/5-apt-conf/">apt.conf</a></code>(5) for syntax information. </p>
<p> The configuration file will be read relative to when it appears on the command line and can overwrite options that appear before it. </p>
<p> Note that the config file will also be passed to all <font SIZE="-1">APT</font> tools called by <code>apt-file</code>.</p>
<dt>-D, &#8211;from-deb</p>
<dd> Use contents of the given .deb archives(s) as patterns. Useful for searching for file conflicts with other packages. Implies -F.</p>
<dt>-f, &#8211;from-file</p>
<dd> Read patterns from the given file(s), one per line. Use &#8211; as filename for stdin. If no files are given, then the list will be read from stdin. This is much faster than invoking apt-file many times.</p>
<dt>&#8211;filter-origins <i>origin[,&#8230;]</i></p>
<dd> Only search indices from the listed origins (e.g. &#8220;Debian&#8221;). </p>
<p> This filter matches against the name listed in the <i>Origin</i> field from the Release file. </p>
<p> If set to &#8216;*&#8217;, this filter will be disabled (mostly useful for overriding the setting in a configuration file) </p>
<p> Alias of the <font SIZE="-1">APT</font> config option: <code>apt-file::Search-Filter::Origin</code></p>
<dt>&#8211;filter-suites <i>suite[,&#8230;]</i></p>
<dd> Only search indices from the listed suites or codenames (e.g. &#8220;unstable&#8221;). </p>
<p> This filter matches against the name listed in the <i>Codename</i> and <i>Suite</i> fields from the Release file. This means that either &#8220;unstable&#8221; or &#8220;sid&#8221; will match Debian&#8217;s unstable suite. </p>
<p> If set to &#8216;*&#8217;, this filter will be disabled (mostly useful for overriding the setting in a configuration file) </p>
<p> Alias of the <font SIZE="-1">APT</font> config option: <code>apt-file::Search-Filter::Suite</code></p>
<dt>-F, &#8211;fixed-string</p>
<dd> Do not expand search pattern with generic characters at pattern&#8217;s start and end. </p>
<p> This is default for <code>show</code> and <code>list</code> actions.</p>
<dt>&#8211;index-names <i>type[,&#8230;]</i>, -I <i>type[,&#8230;]</i></p>
<dd> Only search indexes of the given name(s). If set to the special value <i></i><font SIZE="-1"><i>ALL</i></font><i></i> (case-sensitive), then all <code>apt-file</code> indices are searched. </p>
<p> The name(s) must match one or more of the identifiers used in the <font SIZE="-1">APT</font> configuration (minus leading &#8220;Contents-&#8221;). Example if the configuration has the following snippets: </p>
<pre><code>
Acquire::IndexTargets::deb::Contents - deb{...};
Acquire::IndexTargets::deb - src::Contents - dsc{...};
Acquire::IndexTargets::deb::Contents - udeb{...};
Acquire::IndexTargets::deb::Contents - deb - legacy
{
#Explicitly named to "Contents-deb"
    Identifier "Contents-deb";
    ...;
};
</code></pre>
<p> Then, apt-file will recognise &#8220;deb&#8221;, &#8220;dsc&#8221; and &#8220;udeb&#8221; as index names. </p>
<p> This option defaults to the value of the &#8220;apt-file::Index-Names&#8221; apt config option (or &#8220;deb&#8221; if omitted).</p>
<dt>-i, &#8211;ignore-case</p>
<dd> Ignore case when searching for pattern.</p>
<dt>-l, &#8211;package-only</p>
<dd> Only display package name; do not display file names.</p>
<dt>-o, &#8211;option APT::Option=Value</p>
<dd> Set a Configuration Option; This will set an arbitrary configuration option. The syntax is <code>-o APT::Option=Value</code>. <code>-o</code> and <code>&#8211;option</code> can be used multiple times to set different options. </p>
<p> This option <i>can</i> be used to overwrite other command line options (e.g. &#8220;-o apt-file::Search-Filter::Origin=Debian&#8221; is effectively the same as &#8220;&#8211;filter-origins Debian&#8221;). </p>
<p> Note that the config options passed via this option will also be passed to all <font SIZE="-1">APT</font> tools called by <code>apt-file</code>.</p>
<dt>&#8211;substring-match</p>
<dd> Match if the given search <i>pattern</i> is a substring of a path or package. </p>
<p> This is default for <code>search</code> and <code>find</code> actions.</p>
<dt>-v, &#8211;verbose</p>
<dd> Run apt-file in verbose/debug mode.</p>
<dt>-x, &#8211;regexp</p>
<dd> Treat pattern as a (perl) regular expression. See <code><a href="/docs/linux/man/1-perlreref/">perlreref</a></code>(1) for details. Without this option, pattern is treated as a literal string to search for. </p>
<p> Be advised that this option can be rather slow. If performance is an issue, consider giving apt-file non-regex pattern matching too much and pipe the output to <code>perl -ne &#8216;/&lt;pattern-here&gt;/&#8217;</code>. This enables apt-file to use more optimizations and leaves less work to the &#8220;slower&#8221; regex.</p>
<dt>-h, &#8211;help</p>
<dd> Display a short help screen.</dl>
<h2>CONFIGURATION FILES</h2>
<p> The apt-file command relies on the <font SIZE="-1">APT</font> configuration. Notably, the default configuration makes <code>apt</code> fetch Contents files by default during a call to <code>apt update</code>. </p>
<p> For information on how to configure <font SIZE="-1">APT</font> to fetch more or fewer Contents files, please refer to <i>/usr/share/doc/apt-file/README.md.gz</i>. </p>
<p> The following files are notably interesting:</p>
<dl>
<dt><i>/etc/apt/apt-file.conf</i></p>
<dd> Note this path is actually configurable by changing the value of the <font SIZE="-1">APT</font> configuration called &#8220;Dir::Etc::apt-file-main&#8221;. The listed value is merely the default value of that option. </p>
<p> If this file is present, <code>apt-file</code> will read this file <i>after</i> all default <font SIZE="-1">APT</font> configuration files. Any config file <code>-c</code> or option (<code>-o</code>) will be evaluated <i>before</i> this file (and can override options set in it). </p>
<p> The file will also be passed on to all <font SIZE="-1">APT</font> tools called by <code>apt-file</code>.</p>
<dt><i>/etc/apt/apt.conf.d/50apt-file.conf</i></p>
<dd> Chooses which Contents files to download. Note that apt-file recognises only &#8220;Acquire&#8221; targets that starts with &#8220;Contents-&#8221;.</dl>
<h3>Special configurations similar to apt-file 2</h3>
<p> Here are some <code>apt-file</code> 2 related work flows and how to (almost) emulate them with <code>apt-file</code> 3. They are documented as a <i>starting point</i> for people, who are attached to these. </p>
<p> The emulation may not be perfect for you out of the box. Patches are welcome to keep the examples updated as long as the examples remain &#8220;trivial&#8221;.</p>
<dl>
<dt>&bull;</p>
<dd> Only make <code>apt-file update</code> fetch Contents files </p>
<p> If you are accustomed to <code>apt update</code> <i>not</i> fetching Contents files, then you can run <i>/usr/share/doc/apt-file/examples/apt-file-2-update.sh</i>. This script will configure <code>apt</code> and <code>apt-file</code> accordingly after best effort. </p>
<p> Please read the resulting <i>/etc/apt/apt-file.conf</i>.</p>
<dt>&bull;</p>
<dd> Creating/using &#8220;user&#8221; caches </p>
<p> Previous versions of <code>apt-file</code> had a &#8220;&#8211;cache&#8221; option, which could be used to denote a directory to store the Contents files. This can be emulated by doing: </p>
<pre><code>
#Setup
$ mkdir - p ~ /.cache / apt - file ~ /.config $ touch ~ /.cache / apt - file / dpkg - status $ sed '/^Dir::State/ d; /^Dir::Cache/ d;' / usr / share / doc / apt - file / examples / apt - file.conf &gt; ~ /.config / apt - file.conf
                                                                                                                                                                                                                              $ cat
                                                                                                                                                                                                           &lt;&lt; EOF &gt;&gt;
    ~ /.config / apt - file.conf
                           Dir::State "$HOME/.cache/apt-file";
Dir::Cache "$HOME/.cache/apt-file";
Dir::State::status "$HOME/.cache/apt-file/dpkg-status";
EOF
#Update the cache
        $ apt -
    file - c ~ /.config / apt - file.conf update
#Search using the cache
                                    $ apt -
    file - c ~ /.config / apt - file.conf show apt - file
#Removal of the cache + config
                                                         $ rm -
    fr ~ /.cache / apt - file ~ /.config / apt - file.conf
</code></pre>
<p> (You will probably want to add an alias apt-file in your <i>~/.bashrc</i>) </p>
<p> Please read the resulting <i>./apt-file-user-cache.conf</i>.</dl>
<h2>BUGS, QUIRKS</h2>
<p> There are some known issues or &#8220;quirks&#8221; that are good to keep in mind.</p>
<dl>
<dt>&bull;</p>
<dd> The Contents files do <code>not</code> include a leading slash on paths. This means that <i>/bin/ls</i> is listed as <i>bin/ls</i> in the Contents file. If you are looking for something in a top-level directory, it is often better to omit the leading slash. </p>
<p> The search algorithm will attempt to work around the leading slash, but it will not work in all cases. As a workaround, try to pull the leading slash to the beginning of regular expressions. For example, use &#8220;/(?:usr/bin/vim|sbin/lvm)&#8221; instead of &#8220;/usr/bin/vim|/sbin/lvm&#8221;.</p>
<dt>&bull;</p>
<dd> When a new line has been added to the sources.list and apt update has not been run, apt-file does not print a warning message.</p>
<dt>&bull;</p>
<dd> By default, <code>apt-file</code> assumes that Contents files do <i>not</i> include a descriptive header (explaining what the file is and how to interpret it). However, some tools have generated them with such a header (e.g. for old versions of Contents files for the Debian archive or Contents files generated by reprepro prior to version 5.2.0). </p>
<p> If you search such files, you will want to set <code>apt-file::Parser::Check-For-Description-Header</code> to true (e.g. in <i>/etc/apt/apt.conf.d/50apt-file.conf</i>) to have <code>apt-file</code> properly filter out the headers to avoid false matches. </p>
<p> The reason this is not the default is that it costs a factor 2 in overhead while most common Contents files no longer have the header. (see #881405 for more details).</p>
<dt>&bull;</p>
<dd> Not all <font SIZE="-1">APT</font> repositories have Contents files. Notably common install media (CDs etc.) may omit them to conserve space. </p>
<p> The default configuration by <code>apt-file</code> marks Contents files as optional and will just silently fail to search in Contents files in such repositories.</dl>
<h2>EXIT CODES</h2>
<p> <code>apt-file</code> has the following defined exit codes, which can be used for scripting purposes.</p>
<dl>
<dt><code>0</code></p>
<dd> <code>apt-file</code> returned successfully. If the command was a search, there was at least one result.</p>
<dt><code>1</code></p>
<dd> <code>apt-file</code> completed a search successfully, but it had no results.</p>
<dt><code>2</code></p>
<dd> An error occurred (including invalid/conflicting user options).</p>
<dt><code>3</code></p>
<dd> <code>apt-file</code> could not complete the command because the cache was empty. Please ensure there are indices enabled in the <font SIZE="-1">APT</font> config and run <code>apt update</code> to fetch them.</p>
<dt><code>4</code></p>
<dd> <code>apt-file</code> could not complete the command because the cache does not have any files matching the restrictions. Either change the restrictions (e.g. <code>&#8211;index-names</code>) or configure apt to fetch the relevant files and run <code>apt update</code>.</p>
<dt><code>255</code></p>
<dd> There was an internal errors / uncaught exception in <code>apt-file</code>. Please file a bug against <code>apt-file</code>.</dl>
<p> Any other exit code is reserved for future use.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-apt/">apt</a></code>(1), <code><a href="/docs/linux/man/8-apt-cache/">apt-cache</a></code>(8), <code><a href="/docs/linux/man/5-apt-conf/">apt.conf</a></code>(5) </p>
<p> The <font SIZE="-1">APT</font> users guide in /usr/share/doc/apt/ </p>
<p> The example config in /usr/share/doc/apt-file/examples </p>
<p> The <font SIZE="-1">README</font> at <i>/usr/share/doc/apt-file/README.md.gz</i> </p>
<h2>Index</h2>
