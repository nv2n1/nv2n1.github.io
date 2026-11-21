---

title: "dpkg-query(1)"
name: "dpkg-query"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dpkg-query/"
description: "dpkg-query – a tool to query the dpkg database"
---

<p> <code>dpkg-query</code> [<i>option</i>&#8230;] <i>command</i></p>
<p> <code>dpkg-query</code> is a tool to show information about packages listed in the <code>dpkg</code> database.</p>
<h2>COMMANDS</h2>
<dl>
<dt><code>-l</code>, <code>&#8211;list</code> [<i>package-name-pattern</i>&#8230;]</dt>
<dd> List all known packages matching one or more patterns, regardless of their status, which includes any real or virtual package referenced in any dependency relationship field (such as <code>Breaks</code>, <code>Enhances</code>, etc.). If no <i>package-name-pattern</i> is given, list all packages in <i>/var/lib/dpkg/status</i>, excluding the ones marked as not-installed (i.e. those which have been previously purged). Normal shell wildcard characters are allowed in <i>package-name-pattern</i>. Please note you will probably have to quote <i>package-name-pattern</i> to prevent the shell from performing filename expansion. For example this will list all package names starting with &#8220;libc6&#8221;:</dd>
<dl>
<dt>
</dt><dd>
<pre>
 dpkg-query -l 'libc6*'
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<p> The first three columns of the output show the desired action, the package status, and errors, in that order. </p>
<p> Desired action:</p>
</dd><dl>
<dt>u = Unknown</dt>
<dd>
</dd><dt>i = Install</dt>
<dd>
</dd><dt>h = Hold</dt>
<dd>
</dd><dt>r = Remove</dt>
<dd>
</dd><dt>p = Purge</dt>
<dd></dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> Package status:</p>
</dd><dl>
<dt>n = Not-installed</dt>
<dd>
</dd><dt>c = Config-files</dt>
<dd>
</dd><dt>H = Half-installed</dt>
<dd>
</dd><dt>U = Unpacked</dt>
<dd>
</dd><dt>F = Half-configured</dt>
<dd>
</dd><dt>W = Triggers-awaiting</dt>
<dd>
</dd><dt>t = Triggers-pending</dt>
<dd>
</dd><dt>i = Installed</dt>
<dd></dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> Error flags:</p>
</dd><dl>
<dt>&lt;empty&gt; = (none)</dt>
<dd>
</dd><dt>R = Reinst-required</dt>
<dd></dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> An uppercase status or error letter indicates the package is likely to cause severe problems. Please refer to <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1) for information about the above states and flags. </p>
<p> The output format of this option is not configurable, but varies automatically to fit the terminal width. It is intended for human readers, and is not easily machine-readable. See <code>-W</code> (<code>&#8211;show</code>) and <code>&#8211;showformat</code> for a way to configure the output format.</dd></dl>
<dt><code>-W</code>, <code>&#8211;show</code> [<i>package-name-pattern</i>&#8230;]</dt>
<dd> Just like the <code>&#8211;list</code> option this will list all packages matching the given patterns. However the output can be customized using the <code>&#8211;showformat</code> option. The default output format gives one line per matching package, each line having the name (extended with the architecture qualifier for <code>Multi-Arch</code> <code>same</code> packages) and installed version of the package, separated by a tab.</dd>
<dt><code>-s</code>, <code>&#8211;status</code> [<i>package-name</i>&#8230;]</dt>
<dd> Report status of specified packages. This just displays the entry in the installed package status database. If no <i>package-name</i> is specified it will display all package entries in the status database (since dpkg 1.19.1). When multiple <i>package-name</i> entries are listed, the requested status entries are separated by an empty line, with the same order as specified on the argument list.</dd>
<dt><code>-L</code>, <code>&#8211;listfiles</code> <i>package-name</i>&#8230;</dt>
<dd> List files installed to your system from <i>package-name</i>. When multiple <i>package-name</i>s are listed, the requested lists of files are separated by an empty line, with the same order as specified on the argument list. </dd>
<p> Each file diversion is printed on its own line after its diverted file, prefixed with one of the following localized strings: </p>
<p>&nbsp;<wbr>&nbsp;locally diverted to:&nbsp;<i>diverted-to</i><br />
&nbsp;<wbr>&nbsp;package diverts others to:&nbsp;<i>diverted-to</i><br />
&nbsp;<wbr>&nbsp;diverted by&nbsp;<i>pkg</i>&nbsp;to:&nbsp;<i>diverted-to</i> </p>
<p> Hint: When machine parsing the output, it is customary to set the locale to <code>C.UTF-8</code> to get reproducible results. </p>
<p> This command will not list extra files created by maintainer scripts, nor will it list alternatives.</p>
<dt><code>&#8211;control-list</code> <i>package-name</i></dt>
<dd> List control files installed to your system from <i>package-name</i> (since dpkg 1.16.5). These can be used as input arguments to <code>&#8211;control-show</code>.</dd>
<dt><code>&#8211;control-show</code> <i>package-name</i> <i>control-file</i></dt>
<dd> Print the <i>control-file</i> installed to your system from <i>package-name</i> to the standard output (since dpkg 1.16.5).</dd>
<dt><code>-c</code>, <code>&#8211;control-path</code> <i>package-name</i> [<i>control-file</i>]</dt>
<dd> List paths for control files installed to your system from <i>package-name</i> (since dpkg 1.15.4). If <i>control-file</i> is specified then only list the path for that control file if it is present. </dd>
<p> <code>Warning</code>: this command is deprecated as it gives direct access to the internal dpkg database, please switch to use <code>&#8211;control-list</code> and <code>&#8211;control-show</code> instead for all cases where those commands might give the same end result. Although, as long as there is still at least one case where this command is needed (i.e. when having to remove a damaging postrm maintainer script), and while there is no good solution for that, this command will not get removed.</p>
<dt><code>-S</code>, <code>&#8211;search</code> <i>filename-search-pattern</i>&#8230;</dt>
<dd> Search for packages that own files corresponding to the given patterns. Standard shell wildcard characters can be used in the pattern, where asterisk (<code>*</code>) and question mark (<code>?</code>) will match a slash, and backslash (<code>\</code>) will be used as an escape character. </dd>
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
<dt><code>-p</code>, <code>&#8211;print-avail</code> [<i>package-name</i>&#8230;]</dt>
<dd> Display details about packages, as found in <i>/var/lib/dpkg/available</i>. If no <i>package-name</i> is specified, it will display all package entries in the <i>available</i> database (since dpkg 1.19.1). When multiple <i>package-name</i> are listed, the requested <i>available</i> entries are separated by an empty line, with the same order as specified on the argument list. </dd>
<p> Users of APT-based frontends should use <code>apt show</code> <i>package-name</i> instead as the <i>available</i> file is only kept up-to-date when using <code>dselect</code>.</p>
<dt><code>-?</code>, <code>&#8211;help</code></dt>
<dd> Show the usage message and exit.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Show the version and exit.</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;admindir=</code><i>dir</i></dt>
<dd> Change the location of the <code>dpkg</code> database. The default location is <i>/var/lib/dpkg</i>.</dd>
<dt><code>&#8211;root=</code><i>directory</i></dt>
<dd> Set the root directory to <i>directory</i>, which sets the administrative directory to &laquo;<i>directory</i>/var/lib/dpkg&raquo; (since dpkg 1.21.0).</dd>
<dt><code>&#8211;load-avail</code></dt>
<dd> Also load the available file when using the <code>&#8211;show</code> and <code>&#8211;list</code> commands, which now default to only querying the status file (since dpkg 1.16.2).</dd>
<dt><code>&#8211;no-pager</code></dt>
<dd> Disables the use of any pager when showing information (since dpkg 1.19.2).</dd>
<dt><code>-f</code>, <code>&#8211;showformat=</code><i>format</i></dt>
<dd> This option is used to specify the format of the output <code>&#8211;show</code> will produce (short option since dpkg 1.13.1). The format is a string that will be output for each package listed. </dd>
<p> In the format string, &#8220;<code>\</code>&#8221; introduces escapes:</p>
<dl>
<dl>
<dt><code>
</code> newline</dt>
<dd>
</dd><dt><code>
</code> carriage return</dt>
<dd>
</dd><dt><code>	</code> tab</dt>
<dd></dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> &#8220;<code>\</code>&#8221; before any other character suppresses any special meaning of the following character, which is useful for &#8220;<code>\</code>&#8221; and &#8220;<code>$</code>&#8220;. </p>
<p> Package information can be included by inserting variable references to package fields using the syntax &#8220;<code>${</code><i>field</i>[<code>;</code><i>width</i>]<code>}</code>&#8220;. Fields are printed right-aligned unless the width is negative in which case left alignment will be used. The following <i>field</i>s are recognized but they are not necessarily available in the status file (only internal fields or fields stored in the binary package end up in it):</p>
</dd><dl>
<dt><code>Architecture</code></dt>
<dd>
</dd><dt><code>Bugs</code></dt>
<dd>
</dd><dt><code>Conffiles</code> (internal)</dt>
<dd>
</dd><dt><code>Config-Version</code> (internal)</dt>
<dd>
</dd><dt><code>Conflicts</code></dt>
<dd>
</dd><dt><code>Breaks</code></dt>
<dd>
</dd><dt><code>Depends</code></dt>
<dd>
</dd><dt><code>Description</code></dt>
<dd>
</dd><dt><code>Enhances</code></dt>
<dd>
</dd><dt><code>Protected</code></dt>
<dd>
</dd><dt><code>Essential</code></dt>
<dd>
</dd><dt><code>Filename</code> (internal, front-end related)</dt>
<dd>
</dd><dt><code>Homepage</code></dt>
<dd>
</dd><dt><code>Installed-Size</code></dt>
<dd>
</dd><dt><code>MD5sum</code> (internal, front-end related)</dt>
<dd>
</dd><dt><code>MSDOS-Filename</code> (internal, front-end related)</dt>
<dd>
</dd><dt><code>Maintainer</code></dt>
<dd>
</dd><dt><code>Origin</code></dt>
<dd>
</dd><dt><code>Package</code></dt>
<dd>
</dd><dt><code>Pre-Depends</code></dt>
<dd>
</dd><dt><code>Priority</code></dt>
<dd>
</dd><dt><code>Provides</code></dt>
<dd>
</dd><dt><code>Recommends</code></dt>
<dd>
</dd><dt><code>Replaces</code></dt>
<dd>
</dd><dt><code>Revision</code> (obsolete)</dt>
<dd>
</dd><dt><code>Section</code></dt>
<dd>
</dd><dt><code>Size</code> (internal, front-end related)</dt>
<dd>
</dd><dt><code>Source</code></dt>
<dd>
</dd><dt><code>Status</code> (internal)</dt>
<dd>
</dd><dt><code>Suggests</code></dt>
<dd>
</dd><dt><code>Tag</code> (usually not in .deb but in repository Packages files)</dt>
<dd>
</dd><dt><code>Triggers-Awaited</code> (internal)</dt>
<dd>
</dd><dt><code>Triggers-Pending</code> (internal)</dt>
<dd>
</dd><dt><code>Version</code></dt>
<dd></dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> The following are virtual fields, generated by <code>dpkg-query</code> from values from other fields (note that these do not use valid names for fields in control files):</p>
</dd><dl>
<dt><code>binary:Package</code></dt>
<dd> It contains the binary package name with a possible architecture qualifier like &#8220;libc6:amd64&#8221; (since dpkg 1.16.2). An architecture qualifier will be present to make the package name unambiguous, for example if the package has a <code>Multi-Arch</code> field with a value of <code>same</code> or the package is of a foreign architecture.</dd>
<dt><code>binary:Synopsis</code></dt>
<dd> It contains the package short description (since dpkg 1.19.1).</dd>
<dt><code>binary:Summary</code></dt>
<dd> This is an alias for <code>binary:Synopsis</code> (since dpkg 1.16.2).</dd>
<dt><code>db:Status-Abbrev</code></dt>
<dd> It contains the abbreviated package status (as three characters), such as &#8220;ii &#8221; or &#8220;iHR&#8221; (since dpkg 1.16.2). See the <code>&#8211;list</code> command description for more details.</dd>
<dt><code>db:Status-Want</code></dt>
<dd> It contains the package wanted status, part of the Status field (since dpkg 1.17.11).</dd>
<dt><code>db:Status-Status</code></dt>
<dd> It contains the package status word, part of the Status field (since dpkg 1.17.11).</dd>
<dt><code>db:Status-Eflag</code></dt>
<dd> It contains the package status error flag, part of the Status field (since dpkg 1.17.11).</dd>
<dt><code>db-fsys:Files</code></dt>
<dd> It contains the list of the package filesystem entries separated by newlines (since dpkg 1.19.3).</dd>
<dt><code>db-fsys:Last-Modified</code></dt>
<dd> It contains the timestamp in seconds of the last time the package filesystem entries were modified (since dpkg 1.19.3).</dd>
<dt><code>source:Package</code></dt>
<dd> It contains the source package name for this binary package (since dpkg 1.16.2).</dd>
<dt><code>source:Version</code></dt>
<dd> It contains the source package version for this binary package (since dpkg 1.16.2)</dd>
<dt><code>source:Upstream-Version</code></dt>
<dd> It contains the source package upstream version for this binary package (since dpkg 1.18.16)</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> The default format string is &#8220;<code>${binary:Package}	${Version}
</code>&#8220;. Actually, all other fields found in the status file (i.e. user defined fields) can be requested, too. They will be printed as-is, though, no conversion nor error checking is done on them. To get the name of the <code>dpkg</code> maintainer and the installed version, you could run: </p>
<pre><code>
dpkg - query - f = '${binary:Package} ${Version}	${Maintainer}
' - W dpkg
</code></pre>
</dd></dl>
<dl>
</dl>
</dl>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></dt>
<dd> The requested query was successfully performed.</dd>
<dt><code>1</code></dt>
<dd> The requested query failed either fully or partially, due to no file or package being found (except for <code>&#8211;control-path</code>, <code>&#8211;control-list</code> and <code>&#8211;control-show</code> were such errors are fatal).</dd>
<dt><code>2</code></dt>
<dd> Fatal or unrecoverable error due to invalid command-line usage, or interactions with the system, such as accesses to the database, memory allocations, etc.</dd></dl>
<h2>ENVIRONMENT</h2>
<h3>External environment</h3>
<dl>
<dt><font SIZE="-1"><code>SHELL</code></font></dt>
<dd> Sets the program to execute when spawning a command via a shell (since dpkg 1.19.2).</dd>
<dt><font SIZE="-1"><code>PAGER</code></font></dt>
<dd>
</dd><dt><font SIZE="-1"><code>DPKG_PAGER</code></font></dt>
<dd> Sets the pager command to use (since dpkg 1.19.1), which will be executed with &laquo;$SHELL<code> -c</code>&raquo;. If <font SIZE="-1"><code>SHELL</code></font> is not set, &laquo;<code>sh</code>&raquo; will be used instead. The <font SIZE="-1"><code>DPKG_PAGER</code></font> overrides the <font SIZE="-1"><code>PAGER</code></font> environment variable (since dpkg 1.19.2).</dd>
<dt><font SIZE="-1"><code>DPKG_ROOT</code></font></dt>
<dd> If set and the <code>&#8211;root</code> option has not been specified, it will be used as the filesystem root directory (since dpkg 1.21.0).</dd>
<dt><font SIZE="-1"><code>DPKG_ADMINDIR</code></font></dt>
<dd> If set and the <code>&#8211;admindir</code> option has not been specified, it will be used as the <code>dpkg</code> data directory.</dd>
<dt><font SIZE="-1"><code>DPKG_COLORS</code></font></dt>
<dd> Sets the color mode (since dpkg 1.18.5). The currently accepted values are: <code>auto</code> (default), <code>always</code> and <code>never</code>.</dd></dl>
<h3>Internal environment</h3>
<dl>
<dt><font SIZE="-1"><code>LESS</code></font></dt>
<dd> Defined by <code>dpkg-query</code> to &#8220;<code>-FRSXMQ</code>&#8220;, if not already set, when spawning a pager (since dpkg 1.19.2). To change the default behavior, this variable can be preset to some other value including an empty string, or the <font SIZE="-1"><code>PAGER</code></font> or <font SIZE="-1"><code>DPKG_PAGER</code></font> variables can be set to disable specific options with &laquo;<code>-+</code>&raquo;, for example <code>DPKG_PAGER=&#8220;less -+F&#8221;</code>.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1). </p>
