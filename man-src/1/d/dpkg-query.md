---
title: "dpkg-query(1)"
name: "dpkg-query"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dpkg-query/"
description: "dpkg-query – a tool to query the dpkg database"
---

<h2 class="name">NAME</h2>
<p> dpkg-query &#8211; a tool to query the dpkg database </p>
<h2>SYNOPSIS</h2>
<p> <code>dpkg-query</code> [<i>option</i>&#8230;] <i>command</i></p>
<h2>DESCRIPTION</h2>
<p> <code>dpkg-query</code> is a tool to show information about packages listed in the <code>dpkg</code> database.</p>
<h2>COMMANDS</h2>
<dl>
<dt><code>-l</code>, <code>&#8211;list</code> [<i>package-name-pattern</i>&#8230;]</p>
<dd> List all known packages matching one or more patterns, regardless of their status, which includes any real or virtual package referenced in any dependency relationship field (such as <code>Breaks</code>, <code>Enhances</code>, etc.). If no <i>package-name-pattern</i> is given, list all packages in <i>/var/lib/dpkg/status</i>, excluding the ones marked as not-installed (i.e. those which have been previously purged). Normal shell wildcard characters are allowed in <i>package-name-pattern</i>. Please note you will probably have to quote <i>package-name-pattern</i> to prevent the shell from performing filename expansion. For example this will list all package names starting with &#8220;libc6&#8221;:</p>
<dl>
<dt>
<dd>
<pre>
 dpkg-query -l 'libc6*'
</pre>
</dl>
<dl>
<dt>
<dd>
<p> The first three columns of the output show the desired action, the package status, and errors, in that order. </p>
<p> Desired action:</p>
<dl>
<dt>u = Unknown</p>
<dd>
<dt>i = Install</p>
<dd>
<dt>h = Hold</p>
<dd>
<dt>r = Remove</p>
<dd>
<dt>p = Purge</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> Package status:</p>
<dl>
<dt>n = Not-installed</p>
<dd>
<dt>c = Config-files</p>
<dd>
<dt>H = Half-installed</p>
<dd>
<dt>U = Unpacked</p>
<dd>
<dt>F = Half-configured</p>
<dd>
<dt>W = Triggers-awaiting</p>
<dd>
<dt>t = Triggers-pending</p>
<dd>
<dt>i = Installed</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> Error flags:</p>
<dl>
<dt>&lt;empty&gt; = (none)</p>
<dd>
<dt>R = Reinst-required</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> An uppercase status or error letter indicates the package is likely to cause severe problems. Please refer to <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1) for information about the above states and flags. </p>
<p> The output format of this option is not configurable, but varies automatically to fit the terminal width. It is intended for human readers, and is not easily machine-readable. See <code>-W</code> (<code>&#8211;show</code>) and <code>&#8211;showformat</code> for a way to configure the output format.</dl>
<dt><code>-W</code>, <code>&#8211;show</code> [<i>package-name-pattern</i>&#8230;]</p>
<dd> Just like the <code>&#8211;list</code> option this will list all packages matching the given patterns. However the output can be customized using the <code>&#8211;showformat</code> option. The default output format gives one line per matching package, each line having the name (extended with the architecture qualifier for <code>Multi-Arch</code> <code>same</code> packages) and installed version of the package, separated by a tab.</p>
<dt><code>-s</code>, <code>&#8211;status</code> [<i>package-name</i>&#8230;]</p>
<dd> Report status of specified packages. This just displays the entry in the installed package status database. If no <i>package-name</i> is specified it will display all package entries in the status database (since dpkg 1.19.1). When multiple <i>package-name</i> entries are listed, the requested status entries are separated by an empty line, with the same order as specified on the argument list.</p>
<dt><code>-L</code>, <code>&#8211;listfiles</code> <i>package-name</i>&#8230;</p>
<dd> List files installed to your system from <i>package-name</i>. When multiple <i>package-name</i>s are listed, the requested lists of files are separated by an empty line, with the same order as specified on the argument list. </p>
<p> Each file diversion is printed on its own line after its diverted file, prefixed with one of the following localized strings: </p>
<p>&nbsp;<wbr>&nbsp;locally diverted to:&nbsp;<i>diverted-to</i><br />
&nbsp;<wbr>&nbsp;package diverts others to:&nbsp;<i>diverted-to</i><br />
&nbsp;<wbr>&nbsp;diverted by&nbsp;<i>pkg</i>&nbsp;to:&nbsp;<i>diverted-to</i> </p>
<p> Hint: When machine parsing the output, it is customary to set the locale to <code>C.UTF-8</code> to get reproducible results. </p>
<p> This command will not list extra files created by maintainer scripts, nor will it list alternatives.</p>
<dt><code>&#8211;control-list</code> <i>package-name</i></p>
<dd> List control files installed to your system from <i>package-name</i> (since dpkg 1.16.5). These can be used as input arguments to <code>&#8211;control-show</code>.</p>
<dt><code>&#8211;control-show</code> <i>package-name</i> <i>control-file</i></p>
<dd> Print the <i>control-file</i> installed to your system from <i>package-name</i> to the standard output (since dpkg 1.16.5).</p>
<dt><code>-c</code>, <code>&#8211;control-path</code> <i>package-name</i> [<i>control-file</i>]</p>
<dd> List paths for control files installed to your system from <i>package-name</i> (since dpkg 1.15.4). If <i>control-file</i> is specified then only list the path for that control file if it is present. </p>
<p> <code>Warning</code>: this command is deprecated as it gives direct access to the internal dpkg database, please switch to use <code>&#8211;control-list</code> and <code>&#8211;control-show</code> instead for all cases where those commands might give the same end result. Although, as long as there is still at least one case where this command is needed (i.e. when having to remove a damaging postrm maintainer script), and while there is no good solution for that, this command will not get removed.</p>
<dt><code>-S</code>, <code>&#8211;search</code> <i>filename-search-pattern</i>&#8230;</p>
<dd> Search for packages that own files corresponding to the given patterns. Standard shell wildcard characters can be used in the pattern, where asterisk (<code>*</code>) and question mark (<code>?</code>) will match a slash, and backslash (<code>\</code>) will be used as an escape character. </p>
<p> If the first character in the <i>filename-search-pattern</i> is none of &#8216;<code>*[?/</code>&#8216; then it will be considered a substring match and will be implicitly surrounded by &#8216;<code>*</code>&#8216; (as in <code>*</code><i>filename-search-pattern</i><code>*</code>). If the subsequent string contains any of &#8216;<code>*[?\</code>&#8216;, then it will handled like a glob pattern, otherwise any trailing &#8216;<code>/</code>&#8216; or &#8216;<code>/.</code>&#8216; will be removed and a literal path lookup will be performed. </p>
<p> This command will not list extra files created by maintainer scripts, nor will it list alternatives. </p>
<p> The output format consists of one line per matching pattern, with a list of packages owning the pathname separated by a comma (U+002C &#8216;<code>,</code>&#8216;) and a space (U+0020 &#8221;), followed by a colon (U+003A &#8216;<code>:</code>&#8216;) and a space, followed by the pathname. As in: </p>
<pre>
  pkgname1, pkgname2: pathname1
  pkgname3: pathname2
</pre>
<p> File diversions are printed with the following localized strings: </p>
<p>&nbsp;<wbr>&nbsp;diversion by&nbsp;<i>pkgname</i>&nbsp;from:&nbsp;<i>diverted-from</i><br />
&nbsp;<wbr>&nbsp;diversion by&nbsp;<i>pkgname</i>&nbsp;to:&nbsp;<i>diverted-to</i> </p>
<p> or for local diversions: </p>
<p>&nbsp;<wbr>&nbsp;local diversion from:&nbsp;<i>diverted-from</i><br />
&nbsp;<wbr>&nbsp;local diversion to:&nbsp;<i>diverted-to</i> </p>
<p> Hint: When machine parsing the output, it is customary to set the locale to <code>C.UTF-8</code> to get reproducible results.</p>
<dt><code>-p</code>, <code>&#8211;print-avail</code> [<i>package-name</i>&#8230;]</p>
<dd> Display details about packages, as found in <i>/var/lib/dpkg/available</i>. If no <i>package-name</i> is specified, it will display all package entries in the <i>available</i> database (since dpkg 1.19.1). When multiple <i>package-name</i> are listed, the requested <i>available</i> entries are separated by an empty line, with the same order as specified on the argument list. </p>
<p> Users of APT-based frontends should use <code>apt show</code> <i>package-name</i> instead as the <i>available</i> file is only kept up-to-date when using <code>dselect</code>.</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Show the usage message and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Show the version and exit.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;admindir=</code><i>dir</i></p>
<dd> Change the location of the <code>dpkg</code> database. The default location is <i>/var/lib/dpkg</i>.</p>
<dt><code>&#8211;root=</code><i>directory</i></p>
<dd> Set the root directory to <i>directory</i>, which sets the administrative directory to &laquo;<i>directory</i>/var/lib/dpkg&raquo; (since dpkg 1.21.0).</p>
<dt><code>&#8211;load-avail</code></p>
<dd> Also load the available file when using the <code>&#8211;show</code> and <code>&#8211;list</code> commands, which now default to only querying the status file (since dpkg 1.16.2).</p>
<dt><code>&#8211;no-pager</code></p>
<dd> Disables the use of any pager when showing information (since dpkg 1.19.2).</p>
<dt><code>-f</code>, <code>&#8211;showformat=</code><i>format</i></p>
<dd> This option is used to specify the format of the output <code>&#8211;show</code> will produce (short option since dpkg 1.13.1). The format is a string that will be output for each package listed. </p>
<p> In the format string, &#8220;<code>\</code>&#8221; introduces escapes:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>
</code> newline</p>
<dd>
<dt><code></code> carriage return</p>
<dd>
<dt><code>	</code> tab</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> &#8220;<code>\</code>&#8221; before any other character suppresses any special meaning of the following character, which is useful for &#8220;<code>\</code>&#8221; and &#8220;<code>$</code>&#8220;. </p>
<p> Package information can be included by inserting variable references to package fields using the syntax &#8220;<code>${</code><i>field</i>[<code>;</code><i>width</i>]<code>}</code>&#8220;. Fields are printed right-aligned unless the width is negative in which case left alignment will be used. The following <i>field</i>s are recognized but they are not necessarily available in the status file (only internal fields or fields stored in the binary package end up in it):</p>
<dl>
<dt><code>Architecture</code></p>
<dd>
<dt><code>Bugs</code></p>
<dd>
<dt><code>Conffiles</code> (internal)</p>
<dd>
<dt><code>Config-Version</code> (internal)</p>
<dd>
<dt><code>Conflicts</code></p>
<dd>
<dt><code>Breaks</code></p>
<dd>
<dt><code>Depends</code></p>
<dd>
<dt><code>Description</code></p>
<dd>
<dt><code>Enhances</code></p>
<dd>
<dt><code>Protected</code></p>
<dd>
<dt><code>Essential</code></p>
<dd>
<dt><code>Filename</code> (internal, front-end related)</p>
<dd>
<dt><code>Homepage</code></p>
<dd>
<dt><code>Installed-Size</code></p>
<dd>
<dt><code>MD5sum</code> (internal, front-end related)</p>
<dd>
<dt><code>MSDOS-Filename</code> (internal, front-end related)</p>
<dd>
<dt><code>Maintainer</code></p>
<dd>
<dt><code>Origin</code></p>
<dd>
<dt><code>Package</code></p>
<dd>
<dt><code>Pre-Depends</code></p>
<dd>
<dt><code>Priority</code></p>
<dd>
<dt><code>Provides</code></p>
<dd>
<dt><code>Recommends</code></p>
<dd>
<dt><code>Replaces</code></p>
<dd>
<dt><code>Revision</code> (obsolete)</p>
<dd>
<dt><code>Section</code></p>
<dd>
<dt><code>Size</code> (internal, front-end related)</p>
<dd>
<dt><code>Source</code></p>
<dd>
<dt><code>Status</code> (internal)</p>
<dd>
<dt><code>Suggests</code></p>
<dd>
<dt><code>Tag</code> (usually not in .deb but in repository Packages files)</p>
<dd>
<dt><code>Triggers-Awaited</code> (internal)</p>
<dd>
<dt><code>Triggers-Pending</code> (internal)</p>
<dd>
<dt><code>Version</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> The following are virtual fields, generated by <code>dpkg-query</code> from values from other fields (note that these do not use valid names for fields in control files):</p>
<dl>
<dt><code>binary:Package</code></p>
<dd> It contains the binary package name with a possible architecture qualifier like &#8220;libc6:amd64&#8221; (since dpkg 1.16.2). An architecture qualifier will be present to make the package name unambiguous, for example if the package has a <code>Multi-Arch</code> field with a value of <code>same</code> or the package is of a foreign architecture.</p>
<dt><code>binary:Synopsis</code></p>
<dd> It contains the package short description (since dpkg 1.19.1).</p>
<dt><code>binary:Summary</code></p>
<dd> This is an alias for <code>binary:Synopsis</code> (since dpkg 1.16.2).</p>
<dt><code>db:Status-Abbrev</code></p>
<dd> It contains the abbreviated package status (as three characters), such as &#8220;ii &#8221; or &#8220;iHR&#8221; (since dpkg 1.16.2). See the <code>&#8211;list</code> command description for more details.</p>
<dt><code>db:Status-Want</code></p>
<dd> It contains the package wanted status, part of the Status field (since dpkg 1.17.11).</p>
<dt><code>db:Status-Status</code></p>
<dd> It contains the package status word, part of the Status field (since dpkg 1.17.11).</p>
<dt><code>db:Status-Eflag</code></p>
<dd> It contains the package status error flag, part of the Status field (since dpkg 1.17.11).</p>
<dt><code>db-fsys:Files</code></p>
<dd> It contains the list of the package filesystem entries separated by newlines (since dpkg 1.19.3).</p>
<dt><code>db-fsys:Last-Modified</code></p>
<dd> It contains the timestamp in seconds of the last time the package filesystem entries were modified (since dpkg 1.19.3).</p>
<dt><code>source:Package</code></p>
<dd> It contains the source package name for this binary package (since dpkg 1.16.2).</p>
<dt><code>source:Version</code></p>
<dd> It contains the source package version for this binary package (since dpkg 1.16.2)</p>
<dt><code>source:Upstream-Version</code></p>
<dd> It contains the source package upstream version for this binary package (since dpkg 1.18.16)</dl>
</dl>
<dl>
<dt>
<dd>
<p> The default format string is &#8220;<code>${binary:Package}	${Version}
</code>&#8220;. Actually, all other fields found in the status file (i.e. user defined fields) can be requested, too. They will be printed as-is, though, no conversion nor error checking is done on them. To get the name of the <code>dpkg</code> maintainer and the installed version, you could run: </p>
<pre><code>
dpkg - query - f = '${binary:Package} ${Version}	${Maintainer}
' - W dpkg
</code></pre>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></p>
<dd> The requested query was successfully performed.</p>
<dt><code>1</code></p>
<dd> The requested query failed either fully or partially, due to no file or package being found (except for <code>&#8211;control-path</code>, <code>&#8211;control-list</code> and <code>&#8211;control-show</code> were such errors are fatal).</p>
<dt><code>2</code></p>
<dd> Fatal or unrecoverable error due to invalid command-line usage, or interactions with the system, such as accesses to the database, memory allocations, etc.</dl>
<h2>ENVIRONMENT</h2>
<h3>External environment</h3>
<dl>
<dt><font SIZE="-1"><code>SHELL</code></font></p>
<dd> Sets the program to execute when spawning a command via a shell (since dpkg 1.19.2).</p>
<dt><font SIZE="-1"><code>PAGER</code></font></p>
<dd>
<dt><font SIZE="-1"><code>DPKG_PAGER</code></font></p>
<dd> Sets the pager command to use (since dpkg 1.19.1), which will be executed with &laquo;$SHELL<code> -c</code>&raquo;. If <font SIZE="-1"><code>SHELL</code></font> is not set, &laquo;<code>sh</code>&raquo; will be used instead. The <font SIZE="-1"><code>DPKG_PAGER</code></font> overrides the <font SIZE="-1"><code>PAGER</code></font> environment variable (since dpkg 1.19.2).</p>
<dt><font SIZE="-1"><code>DPKG_ROOT</code></font></p>
<dd> If set and the <code>&#8211;root</code> option has not been specified, it will be used as the filesystem root directory (since dpkg 1.21.0).</p>
<dt><font SIZE="-1"><code>DPKG_ADMINDIR</code></font></p>
<dd> If set and the <code>&#8211;admindir</code> option has not been specified, it will be used as the <code>dpkg</code> data directory.</p>
<dt><font SIZE="-1"><code>DPKG_COLORS</code></font></p>
<dd> Sets the color mode (since dpkg 1.18.5). The currently accepted values are: <code>auto</code> (default), <code>always</code> and <code>never</code>.</dl>
<h3>Internal environment</h3>
<dl>
<dt><font SIZE="-1"><code>LESS</code></font></p>
<dd> Defined by <code>dpkg-query</code> to &#8220;<code>-FRSXMQ</code>&#8220;, if not already set, when spawning a pager (since dpkg 1.19.2). To change the default behavior, this variable can be preset to some other value including an empty string, or the <font SIZE="-1"><code>PAGER</code></font> or <font SIZE="-1"><code>DPKG_PAGER</code></font> variables can be set to disable specific options with &laquo;<code>-+</code>&raquo;, for example <code>DPKG_PAGER=&#8220;less -+F&#8221;</code>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1). </p>
<h2>Index</h2>
