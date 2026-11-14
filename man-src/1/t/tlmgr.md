---
title: "tlmgr(1)"
name: "tlmgr"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tlmgr/"
description: "tlmgr – the native TeX Live Manager"
---

<h2 class="name">NAME</h2>
<p> tlmgr &#8211; the native TeX Live Manager </p>
<h2>SYNOPSIS</h2>
<p> tlmgr [<i>option</i>&#8230;] <i>action</i> [<i>option</i>&#8230;] [<i>operand</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>tlmgr</code> manages an existing TeX Live installation, both packages and configuration options. For information on initially downloading and installing TeX Live, see &lt;<a rel="nofollow" href="https://tug.org/texlive/acquire.html">https://tug.org/texlive/acquire.html</a>&gt;. </p>
<p> The most up-to-date version of this documentation (updated nightly from the development sources) is available at &lt;<a rel="nofollow" href="https://tug.org/texlive/tlmgr.html">https://tug.org/texlive/tlmgr.html</a>&gt;, along with procedures for updating <tt>&quot;tlmgr&quot;</tt> itself and information about test versions. </p>
<p> WARNING: tlmgr in Debian runs always in user mode </p>
<p> TeX Live is organized into a few top-level <i>schemes</i>, each of which is specified as a different set of <i>collections</i> and <i>packages</i>, where a collection is a set of packages, and a package is what contains actual files. Schemes typically contain a mix of collections and packages, but each package is included in exactly one collection, no more and no less. A TeX Live installation can be customized and managed at any level. </p>
<p> See &lt;<a rel="nofollow" href="https://tug.org/texlive/doc">https://tug.org/texlive/doc</a>&gt; for all the TeX Live documentation available.</p>
<h2>EXAMPLES</h2>
<p> After successfully installing TeX Live, here are a few common operations with <tt>&quot;tlmgr&quot;</tt>:</p>
<dl>
<dt>&quot;tlmgr option repository ctan&quot;</p>
<dd>
<dt>&quot;tlmgr option repository <a rel="nofollow" href="https://mirror.ctan.org/systems/texlive/tlnet">https://mirror.ctan.org/systems/texlive/tlnet</a>&quot;</p>
<dd> Tell <tt>&quot;tlmgr&quot;</tt> to use a nearby <font SIZE="-1">CTAN</font> mirror for future updates; useful if you installed TeX Live from the <font SIZE="-1">DVD</font> image and want to have continuing updates. The two commands are equivalent; <tt>&quot;ctan&quot;</tt> is just an alias for the given url. </p>
<p> Caveat: <tt>&quot;mirror.ctan.org&quot;</tt> resolves to many different hosts, and they are not perfectly synchronized; we recommend updating only daily (at most), and not more often. You can choose a particular mirror if problems; the list of all <font SIZE="-1">CTAN</font> mirrors with the status of each is at &lt;<a rel="nofollow" href="https://ctan.org/mirrors/mirmon">https://ctan.org/mirrors/mirmon</a>&gt;.</p>
<dt>&quot;tlmgr update &#8211;list&quot;</p>
<dd> Report what would be updated without actually updating anything.</p>
<dt>&quot;tlmgr update &#8211;all&quot;</p>
<dd> Make your local TeX installation correspond to what is in the package repository (typically useful when updating from <font SIZE="-1">CTAN</font>).</p>
<dt>&quot;tlmgr info&quot; <i>what</i></p>
<dd> Display detailed information about a package <i>what</i>, such as the installation status and description, of searches for <i>what</i> in all packages.</dl>
<p> For all the capabilities and details of <tt>&quot;tlmgr&quot;</tt>, please read the following voluminous information.</p>
<h2>OPTIONS</h2>
<p> The following options to <tt>&quot;tlmgr&quot;</tt> are global options, not specific to any action. All options, whether global or action-specific, can be given anywhere on the command line, and in any order. The first non-option argument will be the main action. In all cases, <tt>&quot;--&quot;</tt><i>option</i> and <tt>&quot;-&quot;</tt><i>option</i> are equivalent, and an <tt>&quot;=&quot;</tt> is optional between an option name and its value.</p>
<dl>
<dt><code>&#8211;repository</code> <i>url|path</i></p>
<dd> Specify the package repository from which packages should be installed or updated, either a local directory or network location, as below. This overridesthe default package repository found in the installation&#8217;s TeX Live Package Database (a.k.a. the <font SIZE="-1">TLPDB,</font> which is given entirely in the file <tt>&quot;tlpkg/texlive.tlpdb&quot;</tt>). </p>
<p> This <tt>&quot;--repository&quot;</tt> option changes the location only for the current run; to make a permanent change, use <tt>&quot;option repository&quot;</tt> (see the &#8220;option&#8221; action). </p>
<p> As an example, you can choose a particular <font SIZE="-1">CTAN</font> mirror with something like this: </p>
<pre>
  -repository <a rel="nofollow" href="http://ctan.example.org/its/ctan/dir/systems/texlive/tlnet">http://ctan.example.org/its/ctan/dir/systems/texlive/tlnet</a>
</pre>
<p> Of course a real hostname and its particular top-level <font SIZE="-1">CTAN</font> directory have to be specified. The list of <font SIZE="-1">CTAN</font> mirrors is available at &lt;<a rel="nofollow" href="https://ctan.org/mirrors/mirmon">https://ctan.org/mirrors/mirmon</a>&gt;. </p>
<p> Here&#8217;s an example of using a local directory: </p>
<pre>
  -repository /local/TL/repository
</pre>
<p> For backward compatibility and convenience, <tt>&quot;--location&quot;</tt> and <tt>&quot;--repo&quot;</tt> are accepted as aliases for this option. </p>
<p> Locations can be specified as any of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&quot;/some/local/dir&quot;</p>
<dd>
<dt>&quot;file:/some/local/dir&quot;</p>
<dd> Equivalent ways of specifying a local directory.</p>
<dt>&quot;ctan&quot;</p>
<dd>
<dt>&quot;<a rel="nofollow" href="https://mirror.ctan.org/systems/texlive/tlnet">https://mirror.ctan.org/systems/texlive/tlnet</a>&quot;</p>
<dd> Pick a <font SIZE="-1">CTAN</font> mirror automatically, trying for one that is both nearby and up-to-date. The chosen mirror is used for the entire download. The bare <tt>&quot;ctan&quot;</tt> is merely an alias for the full url. (See &lt;<a rel="nofollow" href="https://ctan.org">https://ctan.org</a>&gt; for more about <font SIZE="-1">CTAN</font> and its mirrors.)</p>
<dt>&quot;<a rel="nofollow" href="http://server/path/to/tlnet">http://server/path/to/tlnet</a>&quot;</p>
<dd> Standard <font SIZE="-1">HTTP.</font> If the (default) <font SIZE="-1">LWP</font> method is used, persistent connections are supported. <font SIZE="-1">TL</font> can also use <tt>&quot;curl&quot;</tt> or <tt>&quot;wget&quot;</tt> to do the downloads, or an arbitrary user-specified program, as described in the <tt>&quot;tlmgr&quot;</tt> documentation (&lt;<a rel="nofollow" href="https://tug.org/texlive/doc/tlmgr.html#ENVIRONMENT-VARIABLES">https://tug.org/texlive/doc/tlmgr.html#ENVIRONMENT-VARIABLES</a>&gt;).</p>
<dt>&quot;<a rel="nofollow" href="https://server/path/to/tlnet">https://server/path/to/tlnet</a>&quot;</p>
<dd> Again, if the (default) <font SIZE="-1">LWP</font> method is used, this supports persistent connections. Unfortunately, some versions of <tt>&quot;wget&quot;</tt> and <tt>&quot;curl&quot;</tt> do not support https, and even when <tt>&quot;wget&quot;</tt> supports https, certificates may be rejected even when the certificate is fine, due to a lack of local certificate roots. The simplest workaround for this problem is to use http or ftp.</p>
<dt>&quot;<a href="ftp://server/path/to/tlnet">ftp://server/path/to/tlnet</a>&quot;</p>
<dd> If the (default) <font SIZE="-1">LWP</font> method is used, persistent connections are supported.</p>
<dt>&quot;user [at] machine:/path/to/tlnet&quot;</p>
<dd>
<dt>&quot;<a href="scp://user@machine/path/to/tlnet">scp://user@machine/path/to/tlnet</a>&quot;</p>
<dd>
<dt>&quot;<a href="ssh://user@machine/path/to/tlnet">ssh://user@machine/path/to/tlnet</a>&quot;</p>
<dd> These forms are equivalent; they all use <tt>&quot;scp&quot;</tt> to transfer files. Using <tt>&quot;ssh-agent&quot;</tt> is recommended. (Info: &lt;<a rel="nofollow" href="https://en.wikipedia.org/wiki/OpenSSH">https://en.wikipedia.org/wiki/OpenSSH</a>&gt;, &lt;<a rel="nofollow" href="https://en.wikipedia.org/wiki/Ssh-agent">https://en.wikipedia.org/wiki/Ssh-agent</a>&gt;.)</dl>
</dl>
<dl>
<dt>
<dd>
<p> If the repository is on the network, trailing <tt>&quot;/&quot;</tt> characters and/or trailing <tt>&quot;/tlpkg&quot;</tt> and/or <tt>&quot;/archive&quot;</tt> components are ignored.</dl>
<dt><code>&#8211;gui</code> [<i>action</i>]</p>
<dd> Two notable <font SIZE="-1">GUI</font> front-ends for <tt>&quot;tlmgr&quot;</tt>, <tt>&quot;tlshell&quot;</tt> and <tt>&quot;tlcockpit&quot;</tt>, are started up as separate programs; see their own documentation. </p>
<p> <tt>&quot;tlmgr&quot;</tt> itself has a graphical interface as well as the command line interface. You can give the option to invoke it, <tt>&quot;--gui&quot;</tt>, together with an action to be brought directly into the respective screen of the <font SIZE="-1">GUI.</font> For example, running </p>
<pre>
  tlmgr --gui update
</pre>
<p> starts you directly at the update screen. If no action is given, the <font SIZE="-1">GUI</font> will be started at the main screen. See &#8220;<font SIZE="-1">GUI FOR TLMGR&#8221;</font>. </p>
<p> However, the native <font SIZE="-1">GUI</font> requires Perl/TK, which is no longer included in TeX Live&#8217;s Perl distribution for Windows. You may find <tt>&quot;tlshell&quot;</tt> or <tt>&quot;tlcockpit&quot;</tt> easier to work with.</p>
<dt><code>&#8211;gui-lang</code> <i>llcode</i></p>
<dd> By default, the <font SIZE="-1">GUI</font> tries to deduce your language from the environment (on Windows via the registry, on Unix via <tt>&quot;LC_MESSAGES&quot;</tt>). If that fails you can select a different language by giving this option with a language code (based on <font SIZE="-1">ISO 639-1</font>). Currently supported (but not necessarily completely translated) are: English&nbsp;(en, default), Czech&nbsp;(cs), German&nbsp;(de), French&nbsp;(fr), Italian&nbsp;(it), Japanese&nbsp;(ja), Dutch&nbsp;(nl), Polish&nbsp;(pl), Brazilian Portuguese&nbsp;(pt_BR), Russian&nbsp;(ru), Slovak&nbsp;(sk), Slovenian&nbsp;(sl), Serbian&nbsp;(sr), Ukrainian&nbsp;(uk), Vietnamese&nbsp;(vi), simplified Chinese&nbsp;(zh_CN), and traditional Chinese&nbsp;(zh_TW). </p>
<p> tlshell shares its message catalog with tlmgr.</p>
<dt><code>&#8211;command-logfile</code> <i>file</i></p>
<dd> <tt>&quot;tlmgr&quot;</tt> logs the output of all programs invoked (mktexlr, mtxrun, fmtutil, updmap) to a separate log file, by default <tt>&quot;TEXMFSYSVAR/web2c/tlmgr-commands.log&quot;</tt>. This option allows you to specify a different file for the log.</p>
<dt><code>&#8211;debug-translation</code></p>
<dd> In <font SIZE="-1">GUI</font> mode, this switch tells <tt>&quot;tlmgr&quot;</tt> to report any untranslated (or missing) messages to standard error. This can help translators to see what remains to be done.</p>
<dt><code>&#8211;machine-readable</code></p>
<dd> Instead of the normal output intended for human consumption, write (to standard output) a fixed format more suitable for machine parsing. See the &#8220;MACHINE-READABLE <font SIZE="-1">OUTPUT&#8221;</font> section below.</p>
<dt><code>&#8211;no-execute-actions</code></p>
<dd> Suppress the execution of the execute actions as defined in the tlpsrc files. Documented only for completeness, as this is only useful in debugging.</p>
<dt><code>&#8211;package-logfile</code> <i>file</i></p>
<dd> <tt>&quot;tlmgr&quot;</tt> logs all package actions (install, remove, update, failed updates, failed restores) to a separate log file, by default <tt>&quot;TEXMFSYSVAR/web2c/tlmgr.log&quot;</tt>. This option allows you to specify a different file for the log.</p>
<dt><code>&#8211;pause</code></p>
<dd> This option makes <tt>&quot;tlmgr&quot;</tt> wait for user input before exiting. Useful on Windows to avoid disappearing command windows.</p>
<dt><code>&#8211;persistent-downloads</code></p>
<dd>
<dt><code>&#8211;no-persistent-downloads</code></p>
<dd> For network-based installations, this option (on by default) makes <tt>&quot;tlmgr&quot;</tt> try to set up a persistent connection (using the <tt>&quot;LWP&quot;</tt> Perl module). The idea is to open and reuse only one connection per session between your computer and the server, instead of initiating a new download for each package. </p>
<p> If this is not possible, <tt>&quot;tlmgr&quot;</tt> will fall back to using <tt>&quot;wget&quot;</tt>. To disable these persistent connections, use <tt>&quot;--no-persistent-downloads&quot;</tt>.</p>
<dt><code>&#8211;pin-file</code></p>
<dd> Change the pinning file location from <tt>&quot;TEXMFLOCAL/tlpkg/pinning.txt&quot;</tt> (see &#8220;Pinning&#8221; below). Documented only for completeness, as this is only useful in debugging.</p>
<dt><code>&#8211;usermode</code></p>
<dd> Activates user mode for this run of <tt>&quot;tlmgr&quot;</tt>; see &#8220;<font SIZE="-1">USER MODE&#8221;</font> below.</p>
<dt><code>&#8211;usertree</code> <i>dir</i></p>
<dd> Uses <i>dir</i> for the tree in user mode; see &#8220;<font SIZE="-1">USER MODE&#8221;</font> below.</p>
<dt><code>&#8211;verify-repo=[none|main|all]</code></p>
<dd> Defines the level of verification done: If <tt>&quot;none&quot;</tt> is specified, no verification whatsoever is done. If <tt>&quot;main&quot;</tt> is given and a working GnuPG (<tt>&quot;gpg&quot;</tt>) binary is available, all repositories are checked, but only the main repository is required to be signed. If <tt>&quot;all&quot;</tt> is given, then all repositories need to be signed. See &#8220;<font SIZE="-1">CRYPTOGRAPHIC VERIFICATION&#8221;</font> below for details.</dl>
<p> The standard options for TeX Live programs are also accepted: <tt>&quot;--help/-h/-?&quot;</tt>, <tt>&quot;--version&quot;</tt>, <tt>&quot;-q&quot;</tt> (no informational messages), <tt>&quot;-v&quot;</tt> (debugging messages, can be repeated). For the details about these, see the <tt>&quot;TeXLive::TLUtils&quot;</tt> documentation. </p>
<p> The <tt>&quot;--version&quot;</tt> option shows version information about the TeX Live release and about the <tt>&quot;tlmgr&quot;</tt> script itself. If <tt>&quot;-v&quot;</tt> is also given, revision number for the loaded TeX Live Perl modules are shown, too.</p>
<h2>ACTIONS</h2>
<h3>help</h3>
<p> Display this help information and exit (same as <tt>&quot;--help&quot;</tt>, and on the web at &lt;<a rel="nofollow" href="https://tug.org/texlive/doc/tlmgr.html">https://tug.org/texlive/doc/tlmgr.html</a>&gt;). Sometimes the <tt>&quot;perldoc&quot;</tt> and/or <tt>&quot;PAGER&quot;</tt> programs on the system have problems, resulting in control characters being literally output. This can&#8217;t always be detected, but you can set the <tt>&quot;NOPERLDOC&quot;</tt> environment variable and <tt>&quot;perldoc&quot;</tt> will not be used.</p>
<h3>version</h3>
<p> Gives version information (same as <tt>&quot;--version&quot;</tt>). </p>
<p> If <tt>&quot;-v&quot;</tt> has been given the revisions of the used modules are reported, too.</p>
<h3>backup</h3>
<dl>
<dt><code>backup [</code>option<code>&#8230;] &#8211;all</code></p>
<dd>
<dt><code>backup [</code>option<code>&#8230;] </code>pkg<code>&#8230;</code></p>
<dd> If the <tt>&quot;--clean&quot;</tt> option is not specified, this action makes a backup of the given packages, or all packages given <tt>&quot;--all&quot;</tt>. These backups are saved to the value of the <tt>&quot;--backupdir&quot;</tt> option, if that is an existing and writable directory. If <tt>&quot;--backupdir&quot;</tt> is not given, the <tt>&quot;backupdir&quot;</tt> option setting in the <font SIZE="-1">TLPDB</font> is used, if present. If both are missing, no backups are made. (The installer sets <tt>&quot;backupdir&quot;</tt> to <tt>&quot;.../tlpkg/backups&quot;</tt>, under the <font SIZE="-1">TL</font> root installation directory, so it is usually defined; see the &#8220;option&#8221; description for more information.) </p>
<p> If the <tt>&quot;--clean&quot;</tt> option is specified, backups are pruned (removed) instead of saved. The optional integer value <i>N</i> may be specified to set the number of backups that will be retained when cleaning. If <tt>&quot;N&quot;</tt> is not given, the value of the <tt>&quot;autobackup&quot;</tt> option is used. If both are missing, an error is issued. For more details of backup pruning, see the <tt>&quot;option&quot;</tt> action. </p>
<p> Options:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;backupdir</code> <i>directory</i></p>
<dd> Overrides the <tt>&quot;backupdir&quot;</tt> option setting in the <font SIZE="-1">TLPDB.</font> The <i>directory</i> argument is required and must specify an existing, writable directory where backups are to be placed.</p>
<dt><code>&#8211;all</code></p>
<dd> If <tt>&quot;--clean&quot;</tt> is not specified, make a backup of all packages in the TeX Live installation; this will take quite a lot of space and time. If <tt>&quot;--clean&quot;</tt> is specified, all packages are pruned.</p>
<dt><code>&#8211;clean</code>[=<i>N</i>]</p>
<dd> Instead of making backups, prune the backup directory of old backups, as explained above. The optional integer argument <i>N</i> overrides the <tt>&quot;autobackup&quot;</tt> option set in the <font SIZE="-1">TLPDB.</font> You must use <tt>&quot;--all&quot;</tt> or a list of packages together with this option, as desired.</p>
<dt><code>&#8211;dry-run</code></p>
<dd> Nothing is actually backed up or removed; instead, the actions to be performed are written to the terminal.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h3>candidates <i>pkg</i></h3>
<p> Shows the available candidate repositories for package <i>pkg</i>. See &#8220;<font SIZE="-1">MULTIPLE REPOSITORIES&#8221;</font> below.</p>
<h3>check [<i>option</i>&#8230;] [depends|executes|files|runfiles|texmfdbs|all]</h3>
<p> Execute one (or all) check(s) of the consistency of the installation. If no problems are found, there will be no output. (To get a view of what is being done, run <tt>&quot;tlmgr -v check&quot;</tt>.)</p>
<dl>
<dt><code>depends</code></p>
<dd> Lists those packages which occur as dependencies in an installed collection, but are themselves not installed, and those packages which are not contained in any collection. </p>
<p> If you call <tt>&quot;tlmgr check collections&quot;</tt> this test will be carried out instead since former versions for <tt>&quot;tlmgr&quot;</tt> called it that way.</p>
<dt><code>executes</code></p>
<dd> Check that the files referred to by <tt>&quot;execute&quot;</tt> directives in the TeX Live Database are present.</p>
<dt><code>files</code></p>
<dd> Checks that all files listed in the local <font SIZE="-1">TLPDB</font> (<tt>&quot;texlive.tlpdb&quot;</tt>) are actually present, and lists those missing.</p>
<dt><code>runfiles</code></p>
<dd> List those filenames that are occurring more than one time in the runfiles sections, except for known duplicates.</p>
<dt><code>texmfdbs</code></p>
<dd> Checks related to the <tt>&quot;ls-R&quot;</tt> files. If you have defined new trees, or changed the <tt>&quot;TEXMF&quot;</tt> or <tt>&quot;TEXMFDBS&quot;</tt> variables, it can&#8217;t hurt to run this. It checks that:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211; all items in &quot;TEXMFDBS&quot; have the &quot;!!&quot; prefix.</p>
<dd>
<dt>&#8211; all items in &quot;TEXMFBDS&quot; have an &quot;ls-R&quot; file (if they exist at all).</p>
<dd>
<dt>&#8211; all items in &quot;TEXMF&quot; with &quot;!!&quot; are listed in &quot;TEXMFDBS&quot;.</p>
<dd>
<dt>&#8211; all items in &quot;TEXMF&quot; with an &quot;ls-R&quot; file are listed in &quot;TEXMFDBS&quot;.</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<p> Options:</p>
<dl>
<dt><code>&#8211;use-svn</code></p>
<dd> Use the output of <tt>&quot;svn status&quot;</tt> instead of listing the files; for checking the <font SIZE="-1">TL</font> development repository. (This is run nightly.)</dl>
<h3>conf</h3>
<dl>
<dt><code>conf [texmf|tlmgr|updmap [&#8211;conffile </code>file<code>] [&#8211;delete] [</code>key<code> [</code>value<code>]]]</code></p>
<dd>
<dt><code>conf auxtrees [&#8211;conffile </code>file<code>] [show|add|remove] [</code>value<code>]</code></p>
<dd> With only <tt>&quot;conf&quot;</tt>, show general configuration information for TeX Live, including active configuration files, path settings, and more. This is like running <tt>&quot;texconfig conf&quot;</tt>, but works on all supported platforms. </p>
<p> With one of <tt>&quot;conf texmf&quot;</tt>, <tt>&quot;conf tlmgr&quot;</tt>, or <tt>&quot;conf updmap&quot;</tt>, shows all key/value pairs (i.e., all settings) as saved in <tt>&quot;ROOT/texmf.cnf&quot;</tt>, the user-specific <tt>&quot;tlmgr&quot;</tt> configuration file (see below), or the first found (via <tt>&quot;kpsewhich&quot;</tt>) <tt>&quot;updmap.cfg&quot;</tt> file, respectively. </p>
<p> If <i>key</i> is given in addition, shows the value of only that <i>key</i> in the respective file. If option <i>&#8211;delete</i> is also given, the value in the given configuration file is entirely removed (not just commented out). </p>
<p> If <i>value</i> is given in addition, <i>key</i> is set to <i>value</i> in the respective file. <i>No error checking is done!</i> </p>
<p> The <tt>&quot;PATH&quot;</tt> value shown by <tt>&quot;conf&quot;</tt> is as used by <tt>&quot;tlmgr&quot;</tt>. The directory in which the <tt>&quot;tlmgr&quot;</tt> executable is found is automatically prepended to the <font SIZE="-1">PATH</font> value inherited from the environment. </p>
<p> Here is a practical example of changing configuration values. If the execution of (some or all) system commands via <tt>&quot;\write18&quot;</tt> was left enabled during installation, you can disable it afterwards: </p>
<pre>
  tlmgr conf texmf shell_escape 0
</pre>
<p> The subcommand <tt>&quot;auxtrees&quot;</tt> allows adding and removing arbitrary additional texmf trees, completely under user control. <tt>&quot;auxtrees show&quot;</tt> shows the list of additional trees, <tt>&quot;auxtrees add&quot;</tt> <i>tree</i> adds a tree to the list, and <tt>&quot;auxtrees remove&quot;</tt> <i>tree</i> removes a tree from the list (if present). The trees should not contain an <tt>&quot;ls-R&quot;</tt> file (or files will not be found if the <tt>&quot;ls-R&quot;</tt> becomes stale). This works by manipulating the Kpathsea variable <tt>&quot;TEXMFAUXTREES&quot;</tt>, in (by default) <tt>&quot;ROOT/texmf.cnf&quot;</tt>. Example: </p>
<pre>
  tlmgr conf auxtrees add /quick/test/tree
  tlmgr conf auxtrees remove /quick/test/tree
</pre>
<p> In all cases the configuration file can be explicitly specified via the option <tt>&quot;--conffile&quot;</tt> <i>file</i>, e.g., if you don&#8217;t want to change the system-wide configuration. </p>
<p> Warning: The general facility for changing configuration values is here, but tinkering with settings in this way is strongly discouraged. Again, no error checking on either keys or values is done, so any sort of breakage is possible.</dl>
<h3>dump-tlpdb [<i>option</i>&#8230;] [&#8211;json]</h3>
<p> Dump complete local or remote <font SIZE="-1">TLPDB</font> to standard output, as-is. The output is analogous to the <tt>&quot;--machine-readable&quot;</tt> output; see &#8220;MACHINE-READABLE <font SIZE="-1">OUTPUT&#8221;</font> section. </p>
<p> Options:</p>
<dl>
<dt><code>&#8211;local</code></p>
<dd> Dump the local <font SIZE="-1">TLPDB.</font></p>
<dt><code>&#8211;remote</code></p>
<dd> Dump the remote <font SIZE="-1">TLPDB.</font></p>
<dt><code>&#8211;json</code></p>
<dd> Instead of dumping the actual content, the database is dumped as <font SIZE="-1">JSON.</font> For the format of <font SIZE="-1">JSON</font> output see <tt>&quot;tlpkg/doc/JSON-formats.txt&quot;</tt>, format definition <tt>&quot;TLPDB&quot;</tt>.</dl>
<p> Exactly one of <tt>&quot;--local&quot;</tt> and <tt>&quot;--remote&quot;</tt> must be given. </p>
<p> In either case, the first line of the output specifies the repository location, in this format: </p>
<pre>
  &quot;location-url&quot; &quot;	&quot; location
</pre>
<p> where <tt>&quot;location-url&quot;</tt> is the literal field name, followed by a tab, and <i>location</i> is the file or url to the repository. </p>
<p> Line endings may be either <font SIZE="-1">LF</font> or <font SIZE="-1">CRLF</font> depending on the current platform.</p>
<h3>generate</h3>
<dl>
<dt><code>generate [</code>option<code>&#8230;] language</code></p>
<dd>
<dt><code>generate [</code>option<code>&#8230;] language.dat</code></p>
<dd>
<dt><code>generate [</code>option<code>&#8230;] language.def</code></p>
<dd>
<dt><code>generate [</code>option<code>&#8230;] language.dat.lua</code></p>
<dd></dl>
<p> The <tt>&quot;generate&quot;</tt> action overwrites any manual changes made in the respective files: it recreates them from scratch based on the information of the installed packages, plus local adaptions. The TeX Live installer and <tt>&quot;tlmgr&quot;</tt> routinely call <tt>&quot;generate&quot;</tt> for all of these files. </p>
<p> For managing your own fonts, please read the <tt>&quot;updmap --help&quot;</tt> information and/or &lt;<a rel="nofollow" href="https://tug.org/fonts/fontinstall.html">https://tug.org/fonts/fontinstall.html</a>&gt;. </p>
<p> For managing your own formats, please read the <tt>&quot;fmtutil --help&quot;</tt> information. </p>
<p> In more detail: <tt>&quot;generate&quot;</tt> remakes any of the configuration files <tt>&quot;language.dat&quot;</tt>, <tt>&quot;language.def&quot;</tt>, and <tt>&quot;language.dat.lua&quot;</tt> from the information present in the local <font SIZE="-1">TLPDB,</font> plus locally-maintained files. </p>
<p> The locally-maintained files are <tt>&quot;language-local.dat&quot;</tt>, <tt>&quot;language-local.def&quot;</tt>, or <tt>&quot;language-local.dat.lua&quot;</tt>, searched for in <tt>&quot;TEXMFLOCAL&quot;</tt> in the respective directories. If local additions are present, the final file is made by starting with the main file, omitting any entries that the local file specifies to be disabled, and finally appending the local file. </p>
<p> (Historical note: The formerly supported <tt>&quot;updmap-local.cfg&quot;</tt> and <tt>&quot;fmtutil-local.cnf&quot;</tt> are no longer read, since <tt>&quot;updmap&quot;</tt> and <tt>&quot;fmtutil&quot;</tt> now reads and supports multiple configuration files. Thus, local additions can and should be put into an <tt>&quot;updmap.cfg&quot;</tt> of <tt>&quot;fmtutil.cnf&quot;</tt> file in <tt>&quot;TEXMFLOCAL&quot;</tt>. The <tt>&quot;generate updmap&quot;</tt> and <tt>&quot;generate fmtutil&quot;</tt> actions no longer exist.) </p>
<p> Local files specify entries to be disabled with a comment line, namely one of these: </p>
<pre>
  %!NAME
  --!NAME
</pre>
<p> where <tt>&quot;language.dat&quot;</tt> and <tt>&quot;language.def&quot;</tt> use <tt>&quot;%&quot;</tt>, and <tt>&quot;language.dat.lua&quot;</tt> use <tt>&quot;--&quot;</tt>. In all cases, the <i>name</i> is the respective format name or hyphenation pattern identifier. Examples: </p>
<pre>
  %!german
  --!usenglishmax
</pre>
<p> (Of course, you&#8217;re not likely to actually want to disable those particular items. They&#8217;re just examples.) </p>
<p> After such a disabling line, the local file can include another entry for the same item, if a different definition is desired. In general, except for the special disabling lines, the local files follow the same syntax as the master files. </p>
<p> The form <tt>&quot;generate language&quot;</tt> recreates all three files <tt>&quot;language.dat&quot;</tt>, <tt>&quot;language.def&quot;</tt>, and <tt>&quot;language.dat.lua&quot;</tt>, while the forms with an extension recreates only that given language file. </p>
<p> Options:</p>
<dl>
<dt><code>&#8211;dest</code> <i>output_file</i></p>
<dd> specifies the output file (defaults to the respective location in <tt>&quot;TEXMFSYSVAR&quot;</tt>). If <tt>&quot;--dest&quot;</tt> is given to <tt>&quot;generate language&quot;</tt>, it serves as a basename onto which <tt>&quot;.dat&quot;</tt> will be appended for the name of the <tt>&quot;language.dat&quot;</tt> output file, <tt>&quot;.def&quot;</tt> will be appended to the value for the name of the <tt>&quot;language.def&quot;</tt> output file, and <tt>&quot;.dat.lua&quot;</tt> to the name of the <tt>&quot;language.dat.lua&quot;</tt> file. (This is just to avoid overwriting; if you want a specific name for each output file, we recommend invoking <tt>&quot;tlmgr&quot;</tt> twice.)</p>
<dt><code>&#8211;localcfg</code> <i>local_conf_file</i></p>
<dd> specifies the (optional) local additions (defaults to the respective location in <tt>&quot;TEXMFLOCAL&quot;</tt>).</p>
<dt><code>&#8211;rebuild-sys</code></p>
<dd> tells <tt>&quot;tlmgr&quot;</tt> to run necessary programs after config files have been regenerated. These are: <tt>&quot;fmtutil-sys --all&quot;</tt> after <tt>&quot;generate fmtutil&quot;</tt>, <tt>&quot;fmtutil-sys --byhyphen .../language.dat&quot;</tt> after <tt>&quot;generate language.dat&quot;</tt>, and <tt>&quot;fmtutil-sys --byhyphen .../language.def&quot;</tt> after <tt>&quot;generate language.def&quot;</tt>. </p>
<p> These subsequent calls cause the newly-generated files to actually take effect. This is not done by default since those calls are lengthy processes and one might want to made several related changes in succession before invoking these programs.</dl>
<p> The respective locations are as follows: </p>
<pre>
  tex/generic/config/language.dat (and language-local.dat)
  tex/generic/config/language.def (and language-local.def)
  tex/generic/config/language.dat.lua (and language-local.dat.lua)
</pre>
<h3>gui</h3>
<p> Start the graphical user interface. See <font SIZE="-1"><code>GUI</code></font> below.</p>
<h3>info</h3>
<dl>
<dt><code>info [</code>option<code>&#8230;] </code>pkg<code>&#8230;</code></p>
<dd>
<dt><code>info [</code>option<code>&#8230;] collections</code></p>
<dd>
<dt><code>info [</code>option<code>&#8230;] schemes</code></p>
<dd> With no argument, lists all packages available at the package repository, prefixing those already installed with <tt>&quot;i&quot;</tt>. </p>
<p> With the single word <tt>&quot;collections&quot;</tt> or <tt>&quot;schemes&quot;</tt> as the argument, lists the request type instead of all packages. </p>
<p> With any other arguments, display information about <i>pkg</i>: the name, category, short and long description, sizes, installation status, and TeX Live revision number. If <i>pkg</i> is not locally installed, searches in the remote installation source. </p>
<p> For normal packages (not collections or schemes), the sizes of the four groups of files (run/src/doc/bin files) are shown separately. For collections, the cumulative size is shown, including all directly-dependent packages (but not dependent collections). For schemes, the cumulative size is also shown, including all directly-dependent collections and packages. </p>
<p> If <i>pkg</i> is not found locally or remotely, the search action is used and lists matching packages and files. </p>
<p> It also displays information taken from the TeX Catalogue, namely the package version, date, and license. Consider these, especially the package version, as approximations only, due to timing skew of the updates of the different pieces. By contrast, the <tt>&quot;revision&quot;</tt> value comes directly from <font SIZE="-1">TL</font> and is reliable. </p>
<p> The former actions <tt>&quot;show&quot;</tt> and <tt>&quot;list&quot;</tt> are merged into this action, but are still supported for backward compatibility. </p>
<p> Options:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;list</code></p>
<dd> If the option <tt>&quot;--list&quot;</tt> is given with a package, the list of contained files is also shown, including those for platform-specific dependencies. When given with schemes and collections, <tt>&quot;--list&quot;</tt> outputs their dependencies in a similar way.</p>
<dt><code>&#8211;only-installed</code></p>
<dd> If this option is given, the installation source will not be used; only locally installed packages, collections, or schemes are listed.</p>
<dt><code>&#8211;only-remote</code></p>
<dd> Only list packages from the remote repository. Useful when checking what is available in a remote repository using <tt>&quot;tlmgr --repo ... --only-remote info&quot;</tt>. Note that <tt>&quot;--only-installed&quot;</tt> and <tt>&quot;--only-remote&quot;</tt> cannot both be specified.</p>
<dt><code>&#8211;data </code>&quot;item1,item2,&#8230;&quot;</p>
<dd> If the option <tt>&quot;--data&quot;</tt> is given, its argument must be a comma or colon separated list of field names from: <tt>&quot;name&quot;</tt>, <tt>&quot;category&quot;</tt>, <tt>&quot;localrev&quot;</tt>, <tt>&quot;remoterev&quot;</tt>, <tt>&quot;shortdesc&quot;</tt>, <tt>&quot;longdesc&quot;</tt>, <tt>&quot;installed&quot;</tt>, <tt>&quot;size&quot;</tt>, <tt>&quot;relocatable&quot;</tt>, <tt>&quot;depends&quot;</tt>, <tt>&quot;cat-version&quot;</tt>, <tt>&quot;cat-date&quot;</tt>, <tt>&quot;cat-license&quot;</tt>, plus various <tt>&quot;cat-contact-*&quot;</tt> fields (see below). </p>
<p> The <tt>&quot;cat-*&quot;</tt> fields all come from the TeX Catalogue (&lt;<a rel="nofollow" href="https://ctan.org/pkg/catalogue">https://ctan.org/pkg/catalogue</a>&gt;). For each, there are two more variants with prefix <tt>&quot;l&quot;</tt> and <tt>&quot;r&quot;</tt>, e.g., <tt>&quot;lcat-version&quot;</tt> and <tt>&quot;rcat-version&quot;</tt>, which indicate the local and remote information, respectively. The variants without <tt>&quot;l&quot;</tt> and <tt>&quot;r&quot;</tt> show the most current one, which is normally the remote value. </p>
<p> The requested packages&#8217; information is listed in <font SIZE="-1">CSV</font> format, one package per line, and the column information is given by the <tt>&quot;itemN&quot;</tt>. The <tt>&quot;depends&quot;</tt> column contains the names of all the dependencies separated by <tt>&quot;:&quot;</tt> characters. </p>
<p> At this writing, the <tt>&quot;cat-contact-*&quot;</tt> fields include: <tt>&quot;home&quot;</tt>, <tt>&quot;repository&quot;</tt>, <tt>&quot;support&quot;</tt>, <tt>&quot;bugs&quot;</tt>, <tt>&quot;announce&quot;</tt>, <tt>&quot;development&quot;</tt>. Each may be empty or a url value. A brief description is on the <font SIZE="-1">CTAN</font> upload page for new packages: &lt;<a rel="nofollow" href="https://ctan.org/upload">https://ctan.org/upload</a>&gt;.</p>
<dt><code>&#8211;json</code></p>
<dd> In case <tt>&quot;--json&quot;</tt> is specified, the output is a <font SIZE="-1">JSON</font> encoded array where each array element is the <font SIZE="-1">JSON</font> representation of a single <tt>&quot;TLPOBJ&quot;</tt> but with additional information. For details see <tt>&quot;tlpkg/doc/JSON-formats.txt&quot;</tt>, format definition: <tt>&quot;TLPOBJINFO&quot;</tt>. If both <tt>&quot;--json&quot;</tt> and <tt>&quot;--data&quot;</tt> are given, <tt>&quot;--json&quot;</tt> takes precedence.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h3>init-usertree</h3>
<p> Sets up a texmf tree for so-called user mode management, either the default user tree (<tt>&quot;TEXMFHOME&quot;</tt>), or one specified on the command line with <tt>&quot;--usertree&quot;</tt>. See &#8220;<font SIZE="-1">USER MODE&#8221;</font> below.</p>
<h3>install [<i>option</i>&#8230;] <i>pkg</i>&#8230;</h3>
<p> Install each <i>pkg</i> given on the command line, if it is not already installed. It does not touch existing packages; see the <tt>&quot;update&quot;</tt> action for how to get the latest version of a package. </p>
<p> By default this also installs all packages on which the given <i>pkg</i>s are dependent. Options:</p>
<dl>
<dt><code>&#8211;dry-run</code></p>
<dd> Nothing is actually installed; instead, the actions to be performed are written to the terminal.</p>
<dt><code>&#8211;file</code></p>
<dd> Instead of fetching a package from the installation repository, use the package files given on the command line. These files must be standard TeX Live package files (with contained tlpobj file).</p>
<dt><code>&#8211;force</code></p>
<dd> If updates to <tt>&quot;tlmgr&quot;</tt> itself (or other parts of the basic infrastructure) are present, <tt>&quot;tlmgr&quot;</tt> will bail out and not perform the installation unless this option is given. Not recommended.</p>
<dt><code>&#8211;no-depends</code></p>
<dd> Do not install dependencies. (By default, installing a package ensures that all dependencies of this package are fulfilled.)</p>
<dt><code>&#8211;no-depends-at-all</code></p>
<dd> Normally, when you install a package which ships binary files the respective binary package will also be installed. That is, for a package <tt>&quot;foo&quot;</tt>, the package <tt>&quot;foo.i386-linux&quot;</tt> will also be installed on an <tt>&quot;i386-linux&quot;</tt> system. This option suppresses this behavior, and also implies <tt>&quot;--no-depends&quot;</tt>. Don&#8217;t use it unless you are sure of what you are doing.</p>
<dt><code>&#8211;reinstall</code></p>
<dd> Reinstall a package (including dependencies for collections) even if it already seems to be installed (i.e, is present in the <font SIZE="-1">TLPDB</font>). This is useful to recover from accidental removal of files in the hierarchy. </p>
<p> When re-installing, only dependencies on normal packages are followed (i.e., not those of category Scheme or Collection).</p>
<dt><code>&#8211;with-doc</code></p>
<dd>
<dt><code>&#8211;with-src</code></p>
<dd> While not recommended, the <tt>&quot;install-tl&quot;</tt> program provides an option to omit installation of all documentation and/or source files. (By default, everything is installed.) After such an installation, you may find that you want the documentation or source files for a given package after all. You can get them by using these options in conjunction with <tt>&quot;--reinstall&quot;</tt>, as in (using the <tt>&quot;fontspec&quot;</tt> package as the example): </p>
<pre>
  tlmgr install --reinstall --with-doc --with-src fontspec
</pre>
</dl>
<p> This action does not automatically add new symlinks in system directories; you need to run <tt>&quot;tlmgr path add&quot;</tt> (&#8220;path&#8221;) yourself if you are using this feature and want new symlinks added.</p>
<h3>key</h3>
<dl>
<dt><code>key list</code></p>
<dd>
<dt><code>key add </code>file</p>
<dd>
<dt><code>key remove </code>keyid</p>
<dd> The action <tt>&quot;key&quot;</tt> allows listing, adding and removing additional <font SIZE="-1">GPG</font> keys to the set of trusted keys, that is, those that are used to verify the TeX Live databases. </p>
<p> With the <tt>&quot;list&quot;</tt> argument, <tt>&quot;key&quot;</tt> lists all keys. </p>
<p> The <tt>&quot;add&quot;</tt> argument requires another argument, either a filename or <tt>&quot;-&quot;</tt> for stdin, from which the key is added. The key is added to the local keyring <tt>&quot;GNUPGHOME/repository-keys.gpg&quot;</tt>, which is normally <tt>&quot;tlpkg/gpg/repository-keys.gpg&quot;</tt>. </p>
<p> The <tt>&quot;remove&quot;</tt> argument requires a key id and removes the requested id from the local keyring.</dl>
<h3>list</h3>
<p> Synonym for &#8220;info&#8221;.</p>
<h3>option</h3>
<dl>
<dt><code>option [&#8211;json] [show]</code></p>
<dd>
<dt><code>option [&#8211;json] showall|help</code></p>
<dd>
<dt><code>option </code>key<code> [</code>value<code>]</code></p>
<dd></dl>
<p> The first form, <tt>&quot;show&quot;</tt>, shows the global TeX Live settings currently saved in the <font SIZE="-1">TLPDB</font> with a short description and the <tt>&quot;key&quot;</tt> used for changing it in parentheses. </p>
<p> The second form, <tt>&quot;showall&quot;</tt>, is similar, but also shows options which can be defined but are not currently set to any value (<tt>&quot;help&quot;</tt> is a synonym). </p>
<p> Both <tt>&quot;show...&quot;</tt> forms take an option <tt>&quot;--json&quot;</tt>, which dumps the option information in <font SIZE="-1">JSON</font> format. In this case, both forms dump the same data. For the format of the <font SIZE="-1">JSON</font> output see <tt>&quot;tlpkg/doc/JSON-formats.txt&quot;</tt>, format definition <tt>&quot;TLOPTION&quot;</tt>. </p>
<p> In the third form, with <i>key</i>, if <i>value</i> is not given, the setting for <i>key</i> is displayed. If <i>value</i> is present, <i>key</i> is set to <i>value</i>. </p>
<p> Possible values for <i>key</i> are (run <tt>&quot;tlmgr option showall&quot;</tt> for the definitive list): </p>
<pre>
 repository (default package repository),
 formats    (generate formats at installation or update time),
 postcode   (run postinst code blobs)
 docfiles   (install documentation files),
 srcfiles   (install source files),
 backupdir  (default directory for backups),
 autobackup (number of backups to keep).
 sys_bin    (directory to which executables are linked by the path action)
 sys_man    (directory to which man pages are linked by the path action)
 sys_info   (directory to which Info files are linked by the path action)
 desktop_integration (Windows-only: create Start menu shortcuts)
 fileassocs (Windows-only: change file associations)
 multiuser  (Windows-only: install for all users)
</pre>
<p> One common use of <tt>&quot;option&quot;</tt> is to permanently change the installation to get further updates from the Internet, after originally installing from <font SIZE="-1">DVD.</font> To do this, you can run </p>
<pre>
 tlmgr option repository <a rel="nofollow" href="https://mirror.ctan.org/systems/texlive/tlnet">https://mirror.ctan.org/systems/texlive/tlnet</a>
</pre>
<p> The <tt>&quot;install-tl&quot;</tt> documentation has more information about the possible values for <tt>&quot;repository&quot;</tt>. (For backward compatibility, <tt>&quot;location&quot;</tt> can be used as a synonym for <tt>&quot;repository&quot;</tt>.) </p>
<p> If <tt>&quot;formats&quot;</tt> is set (this is the default), then formats are regenerated when either the engine or the format files have changed. Disable this only when you know how and want to regenerate formats yourself whenever needed (which is often, in practice). </p>
<p> The <tt>&quot;postcode&quot;</tt> option controls execution of per-package postinstallation action code. It is set by default, and again disabling is not likely to be of interest except to developers doing debugging. </p>
<p> The <tt>&quot;docfiles&quot;</tt> and <tt>&quot;srcfiles&quot;</tt> options control the installation of their respective file groups (documentation, sources; grouping is approximate) per package. By default both are enabled (1). Either or both can be disabled (set to 0) if disk space is limited or for minimal testing installations, etc. When disabled, the respective files are not downloaded at all. </p>
<p> The options <tt>&quot;autobackup&quot;</tt> and <tt>&quot;backupdir&quot;</tt> determine the defaults for the actions <tt>&quot;update&quot;</tt>, <tt>&quot;backup&quot;</tt> and <tt>&quot;restore&quot;</tt>. These three actions need a directory in which to read or write the backups. If <tt>&quot;--backupdir&quot;</tt> is not specified on the command line, the <tt>&quot;backupdir&quot;</tt> option value is used (if set). The <font SIZE="-1">TL</font> installer sets <tt>&quot;backupdir&quot;</tt> to <tt>&quot;.../tlpkg/backups&quot;</tt>, under the <font SIZE="-1">TL</font> root installation directory. </p>
<p> The <tt>&quot;autobackup&quot;</tt> option (de)activates automatic generation of backups. Its value is an integer. If the <tt>&quot;autobackup&quot;</tt> value is <tt>&quot;-1&quot;</tt>, no backups are removed. If <tt>&quot;autobackup&quot;</tt> is 0 or more, it specifies the number of backups to keep. Thus, backups are disabled if the value is 0. In the <tt>&quot;--clean&quot;</tt> mode of the <tt>&quot;backup&quot;</tt> action this option also specifies the number to be kept. The default value is 1, so that backups are made, but only one backup is kept. </p>
<p> To setup <tt>&quot;autobackup&quot;</tt> to <tt>&quot;-1&quot;</tt> on the command line, use: </p>
<pre>
  tlmgr option -- autobackup -1
</pre>
<p> The <tt>&quot;--&quot;</tt> avoids having the <tt>&quot;-1&quot;</tt> treated as an option. (The <tt>&quot;--&quot;</tt> stops parsing for options at the point where it appears; this is a general feature across most Unix programs.) </p>
<p> The <tt>&quot;sys_bin&quot;</tt>, <tt>&quot;sys_man&quot;</tt>, and <tt>&quot;sys_info&quot;</tt> options are used on Unix systems to control the generation of links for executables, Info files and man pages. See the <tt>&quot;path&quot;</tt> action for details. </p>
<p> The last three options affect behavior on Windows installations. If <tt>&quot;desktop_integration&quot;</tt> is set, then some packages will install items in a sub-folder of the Start menu for <tt>&quot;tlmgr gui&quot;</tt>, documentation, etc. If <tt>&quot;fileassocs&quot;</tt> is set, Windows file associations are made (see also the <tt>&quot;postaction&quot;</tt> action). Finally, if <tt>&quot;multiuser&quot;</tt> is set, then adaptions to the registry and the menus are done for all users on the system instead of only the current user. All three options are on by default.</p>
<h3>paper</h3>
<dl>
<dt><code>paper [a4|letter]</code></p>
<dd>
<dt><code>&lt;[xdvi|pdftex|dvips|dvipdfmx|context|psutils] paper [</code>papersize<code>|&#8211;list]</code>&gt;</p>
<dd>
<dt><code>paper &#8211;json</code></p>
<dd></dl>
<p> With no arguments (<tt>&quot;tlmgr paper&quot;</tt>), shows the default paper size setting for all known programs. </p>
<p> With one argument (e.g., <tt>&quot;tlmgr paper a4&quot;</tt>), sets the default for all known programs to that paper size. </p>
<p> With a program given as the first argument and no paper size specified (e.g., <tt>&quot;tlmgr dvips paper&quot;</tt>), shows the default paper size for that program. </p>
<p> With a program given as the first argument and a paper size as the last argument (e.g., <tt>&quot;tlmgr dvips paper a4&quot;</tt>), set the default for that program to that paper size. </p>
<p> With a program given as the first argument and <tt>&quot;--list&quot;</tt> given as the last argument (e.g., <tt>&quot;tlmgr dvips paper --list&quot;</tt>), shows all valid paper sizes for that program. The first size shown is the default. </p>
<p> If <tt>&quot;--json&quot;</tt> is specified without other options, the paper setup is dumped in <font SIZE="-1">JSON</font> format. For the format of <font SIZE="-1">JSON</font> output see <tt>&quot;tlpkg/doc/JSON-formats.txt&quot;</tt>, format definition <tt>&quot;TLPAPER&quot;</tt>. </p>
<p> Incidentally, this syntax of having a specific program name before the <tt>&quot;paper&quot;</tt> keyword is unusual. It is inherited from the longstanding <tt>&quot;texconfig&quot;</tt> script, which supports other configuration settings for some programs, notably <tt>&quot;dvips&quot;</tt>. <tt>&quot;tlmgr&quot;</tt> does not support those extra settings.</p>
<h3>path</h3>
<dl>
<dt><code>path [&#8211;w32mode=user|admin] add</code></p>
<dd>
<dt><code>path [&#8211;w32mode=user|admin] remove</code></p>
<dd> On Unix, adds or removes symlinks for executables, man pages, and info pages in the system directories specified by the respective options (see the &#8220;option&#8221; description above). Does not change any initialization files, either system or personal. Furthermore, any executables added or removed by future updates are not taken care of automatically; this command must be rerun as needed. </p>
<p> On Windows, the registry part where the binary directory is added or removed is determined in the following way: </p>
<p> If the user has admin rights, and the option <tt>&quot;--w32mode&quot;</tt> is not given, the setting <i>w32_multi_user</i> determines the location (i.e., if it is on then the system path, otherwise the user path is changed). </p>
<p> If the user has admin rights, and the option <tt>&quot;--w32mode&quot;</tt> is given, this option determines the path to be adjusted. </p>
<p> If the user does not have admin rights, and the option <tt>&quot;--w32mode&quot;</tt> is not given, and the setting <i>w32_multi_user</i> is off, the user path is changed, while if the setting <i>w32_multi_user</i> is on, a warning is issued that the caller does not have enough privileges. </p>
<p> If the user does not have admin rights, and the option <tt>&quot;--w32mode&quot;</tt> is given, it must be <tt>&quot;user&quot;</tt> and the user path will be adjusted. If a user without admin rights uses the option <tt>&quot;--w32mode admin&quot;</tt> a warning is issued that the caller does not have enough privileges.</dl>
<h3>pinning</h3>
<p> The <tt>&quot;pinning&quot;</tt> action manages the pinning file, see &#8220;Pinning&#8221; below.</p>
<dl>
<dt>&quot;pinning show&quot;</p>
<dd> Shows the current pinning data.</p>
<dt>&quot;pinning add&quot; <i>repo</i> <i>pkgglob</i>&#8230;</p>
<dd> Pins the packages matching the <i>pkgglob</i>(s) to the repository <i>repo</i>.</p>
<dt>&quot;pinning remove&quot; <i>repo</i> <i>pkgglob</i>&#8230;</p>
<dd> Any packages recorded in the pinning file matching the &lt;pkgglob&gt;s for the given repository <i>repo</i> are removed.</p>
<dt>&quot;pinning remove <i>repo</i> &#8211;all&quot;</p>
<dd> Remove all pinning data for repository <i>repo</i>.</dl>
<h3>platform</h3>
<dl>
<dt><code>platform list|add|remove </code>platform<code>&#8230;</code></p>
<dd>
<dt><code>platform set </code>platform</p>
<dd>
<dt><code>platform set auto</code></p>
<dd> <tt>&quot;platform list&quot;</tt> lists the TeX Live names of all the platforms (a.k.a. architectures), (<tt>&quot;i386-linux&quot;</tt>, &#8230;) available at the package repository. </p>
<p> <tt>&quot;platform add&quot;</tt> <i>platform</i>&#8230; adds the executables for each given platform <i>platform</i> to the installation from the repository. </p>
<p> <tt>&quot;platform remove&quot;</tt> <i>platform</i>&#8230; removes the executables for each given platform <i>platform</i> from the installation, but keeps the currently running platform in any case. </p>
<p> <tt>&quot;platform set&quot;</tt> <i>platform</i> switches TeX Live to always use the given platform instead of auto detection. </p>
<p> <tt>&quot;platform set auto&quot;</tt> switches TeX Live to auto detection mode for platform. </p>
<p> Platform detection is needed to select the proper <tt>&quot;xz&quot;</tt> and <tt>&quot;wget&quot;</tt> binaries that are shipped with TeX Live. </p>
<p> <tt>&quot;arch&quot;</tt> is a synonym for <tt>&quot;platform&quot;</tt>. </p>
<p> Options:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;dry-run</code></p>
<dd> Nothing is actually installed; instead, the actions to be performed are written to the terminal.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h3>postaction</h3>
<dl>
<dt><code>postaction [</code>option<code>&#8230;] install [shortcut|fileassoc|script] [</code>pkg<code>&#8230;]</code></p>
<dd>
<dt><code>postaction [</code>option<code>&#8230;] remove [shortcut|fileassoc|script] [</code>pkg<code>&#8230;]</code></p>
<dd> Carry out the postaction <tt>&quot;shortcut&quot;</tt>, <tt>&quot;fileassoc&quot;</tt>, or <tt>&quot;script&quot;</tt> given as the second required argument in install or remove mode (which is the first required argument), for either the packages given on the command line, or for all if <tt>&quot;--all&quot;</tt> is given. </p>
<p> Options:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;w32mode=[user|admin]</code></p>
<dd> If the option <tt>&quot;--w32mode&quot;</tt> is given the value <tt>&quot;user&quot;</tt>, all actions will only be carried out in the user-accessible parts of the registry/filesystem, while the value <tt>&quot;admin&quot;</tt> selects the system-wide parts of the registry for the file associations. If you do not have enough permissions, using <tt>&quot;--w32mode=admin&quot;</tt> will not succeed.</p>
<dt><code>&#8211;fileassocmode=[1|2]</code></p>
<dd> <tt>&quot;--fileassocmode&quot;</tt> specifies the action for file associations. If it is set to 1 (the default), only new associations are added; if it is set to 2, all associations are set to the TeX Live programs. (See also <tt>&quot;option fileassocs&quot;</tt>.)</p>
<dt><code>&#8211;all</code></p>
<dd> Carry out the postactions for all packages</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h3>print-platform</h3>
<p> Print the TeX Live identifier for the detected platform (hardware/operating system) combination to standard output, and exit. <tt>&quot;--print-arch&quot;</tt> is a synonym.</p>
<h3>print-platform-info</h3>
<p> Print the TeX Live platform identifier, <font SIZE="-1">TL</font> platform long name, and original output from guess.</p>
<h3>remove [<i>option</i>&#8230;] <i>pkg</i>&#8230;</h3>
<p> Remove each <i>pkg</i> specified. Removing a collection removes all package dependencies (unless <tt>&quot;--no-depends&quot;</tt> is specified), but not any collection dependencies of that collection. However, when removing a package, dependencies are never removed. Options:</p>
<dl>
<dt><code>&#8211;all</code></p>
<dd> Uninstalls all of TeX Live, asking for confirmation unless <tt>&quot;--force&quot;</tt> is also specified.</p>
<dt><code>&#8211;backup</code></p>
<dd>
<dt><code>&#8211;backupdir</code> <i>directory</i></p>
<dd> These options behave just as with the update action (q.v.), except they apply to making backups of packages before they are removed. The default is to make such a backup, that is, to save a copy of packages before removal. </p>
<p> The &#8220;restore&#8221; action explains how to restore from a backup.</p>
<dt><code>&#8211;no-depends</code></p>
<dd> Do not remove dependent packages.</p>
<dt><code>&#8211;no-depends-at-all</code></p>
<dd> See above under install (and beware).</p>
<dt><code>&#8211;force</code></p>
<dd> By default, removal of a package or collection that is a dependency of another collection or scheme is not allowed. With this option, the package will be removed unconditionally. Use with care. </p>
<p> A package that has been removed using the <tt>&quot;--force&quot;</tt> option because it is still listed in an installed collection or scheme will not be updated, and will be mentioned as <tt>&quot;forcibly removed&quot;</tt> in the output of <tt>&quot;tlmgr update --list&quot;</tt>.</p>
<dt><code>&#8211;dry-run</code></p>
<dd> Nothing is actually removed; instead, the actions to be performed are written to the terminal.</dl>
<p> Except with <tt>&quot;--all&quot;</tt>, this <tt>&quot;remove&quot;</tt> action does not automatically remove symlinks to executables from system directories; you need to run <tt>&quot;tlmgr path remove&quot;</tt> (&#8220;path&#8221;) yourself if you remove an individual package with a symlink in a system directory.</p>
<h3>repository</h3>
<dl>
<dt><code>repository list</code></p>
<dd>
<dt><code>repository list </code>path|url|tag</p>
<dd>
<dt><code>repository add </code>path<code> [</code>tag<code>]</code></p>
<dd>
<dt><code>repository remove </code>path|tag</p>
<dd>
<dt><code>repository set </code>path<code>[#</code>tag<code>] [</code>path<code>[#</code>tag<code>] &#8230;]</code></p>
<dd>
<dt><code>repository status</code></p>
<dd> This action manages the list of repositories. See <font SIZE="-1">MULTIPLE REPOSITORIES</font> below for detailed explanations. </p>
<p> The first form, <tt>&quot;repository list&quot;</tt>, lists all configured repositories and the respective tags if set. If a path, url, or tag is given after the <tt>&quot;list&quot;</tt> keyword, it is interpreted as the source from which to initialize a <font SIZE="-1">TL</font> database and lists the contained packages. This can also be an otherwise-unused repository, either local or remote. If the option <tt>&quot;--with-platforms&quot;</tt> is specified in addition, for each package the available platforms (if any) are also listed. </p>
<p> The form <tt>&quot;repository add&quot;</tt> adds a repository (optionally attaching a tag) to the list of repositories, while <tt>&quot;repository remove&quot;</tt> removes a repository, either by full path/url, or by tag. </p>
<p> The form <tt>&quot;repository set&quot;</tt> sets the list of available repositories to the items given on the command line, overwriting previous settings. </p>
<p> The form <tt>&quot;repository status&quot;</tt> reports the verification status of the loaded repositories with the format of one repository per line with fields separated by a single space:</p>
<dl>
<dt>
<dd>
<dl>
<dt>The tag (which can be the same as the url);</p>
<dd> = the url; </p>
<p> = iff machine-readable output is specified, the verification code (a number); </p>
<p> = a textual description of the verification status, as the last field extending to the end of line.</dl>
</dl>
<dl>
<dt>
<dd>
<p> That is, in normal (not machine-readable) output, the third field (numeric verification status) is not present. </p>
<p> In all cases, one of the repositories must be tagged as <tt>&quot;main&quot;</tt>; otherwise, all operations will fail!</dl>
</dl>
<h3>restore</h3>
<dl>
<dt><code>restore [</code>option<code>&#8230;] </code>pkg<code> [</code>rev<code>]</code></p>
<dd>
<dt><code>restore [</code>option<code>&#8230;] &#8211;all</code></p>
<dd> Restore a package from a previously-made backup. </p>
<p> If <tt>&quot;--all&quot;</tt> is given, try to restore the latest revision of all package backups found in the backup directory. </p>
<p> Otherwise, if neither <i>pkg</i> nor <i>rev</i> are given, list the available backup revisions for all packages. With <i>pkg</i> given but no <i>rev</i>, list all available backup revisions of <i>pkg</i>. </p>
<p> When listing available packages, <tt>&quot;tlmgr&quot;</tt> shows the revision, and in parenthesis the creation time if available (in format yyyy-mm-dd hh:mm). </p>
<p> If (and only if) both <i>pkg</i> and a valid revision number <i>rev</i> are specified, try to restore the package from the specified backup. </p>
<p> Options:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;all</code></p>
<dd> Try to restore the latest revision of all package backups found in the backup directory. Additional non-option arguments (like <i>pkg</i>) are not allowed.</p>
<dt><code>&#8211;backupdir</code> <i>directory</i></p>
<dd> Specify the directory where the backups are to be found. If not given it will be taken from the configuration setting in the <font SIZE="-1">TLPDB.</font></p>
<dt><code>&#8211;dry-run</code></p>
<dd> Nothing is actually restored; instead, the actions to be performed are written to the terminal.</p>
<dt><code>&#8211;force</code></p>
<dd> Don&#8217;t ask questions.</p>
<dt><code>&#8211;json</code></p>
<dd> When listing backups, the option <tt>&quot;--json&quot;</tt> turn on <font SIZE="-1">JSON</font> output. The format is an array of <font SIZE="-1">JSON</font> objects (<tt>&quot;name&quot;</tt>, <tt>&quot;rev&quot;</tt>, <tt>&quot;date&quot;</tt>). For details see <tt>&quot;tlpkg/doc/JSON-formats.txt&quot;</tt>, format definition: <tt>&quot;TLBACKUPS&quot;</tt>. If both <tt>&quot;--json&quot;</tt> and <tt>&quot;--data&quot;</tt> are given, <tt>&quot;--json&quot;</tt> takes precedence.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h3>search</h3>
<dl>
<dt><code>search [</code>option<code>&#8230;] </code>what</p>
<dd>
<dt><code>search [</code>option<code>&#8230;] &#8211;file </code>what</p>
<dd>
<dt><code>search [</code>option<code>&#8230;] &#8211;all </code>what</p>
<dd> By default, search the names, short descriptions, and long descriptions of all locally installed packages for the argument <i>what</i>, interpreted as a (Perl) regular expression. </p>
<p> Options:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;file</code></p>
<dd> List all filenames containing <i>what</i>.</p>
<dt><code>&#8211;all</code></p>
<dd> Search everything: package names, descriptions and filenames.</p>
<dt><code>&#8211;global</code></p>
<dd> Search the TeX Live Database of the installation medium, instead of the local installation.</p>
<dt><code>&#8211;word</code></p>
<dd> Restrict the search of package names and descriptions (but not filenames) to match only full words. For example, searching for <tt>&quot;table&quot;</tt> with this option will not output packages containing the word <tt>&quot;tables&quot;</tt> (unless they also contain the word <tt>&quot;table&quot;</tt> on its own).</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h3>shell</h3>
<p> Starts an interactive mode, where tlmgr prompts for commands. This can be used directly, or for scripting. The first line of output is <tt>&quot;protocol&quot;</tt> <i>n</i>, where <i>n</i> is an unsigned number identifying the protocol version (currently 1). </p>
<p> In general, tlmgr actions that can be given on the command line translate to commands in this shell mode. For example, you can say <tt>&quot;update --list&quot;</tt> to see what would be updated. The <font SIZE="-1">TLPDB</font> is loaded the first time it is needed (not at the beginning), and used for the rest of the session. </p>
<p> Besides these actions, a few commands are specific to shell mode:</p>
<dl>
<dt>protocol</p>
<dd> Print <tt>&quot;protocol </tt>n<tt>&quot;</tt>, the current protocol version.</p>
<dt>help</p>
<dd> Print pointers to this documentation.</p>
<dt>version</p>
<dd> Print tlmgr version information.</p>
<dt>quit, end, bye, byebye, <font SIZE="-1">EOF</font></p>
<dd> Exit.</p>
<dt>restart</p>
<dd> Restart <tt>&quot;tlmgr shell&quot;</tt> with the original command line; most useful when developing <tt>&quot;tlmgr&quot;</tt>.</p>
<dt>load [local|remote]</p>
<dd> Explicitly load the local or remote, respectively, <font SIZE="-1">TLPDB.</font></p>
<dt>save</p>
<dd> Save the local <font SIZE="-1">TLPDB,</font> presumably after other operations have changed it.</p>
<dt>get [<i>var</i>] =item set [<i>var</i> [<i>val</i>]]</p>
<dd> Get the value of <i>var</i>, or set it to <i>val</i>. Possible <i>var</i> names: <tt>&quot;debug-translation&quot;</tt>, <tt>&quot;machine-readable&quot;</tt>, <tt>&quot;no-execute-actions&quot;</tt>, <tt>&quot;require-verification&quot;</tt>, <tt>&quot;verify-downloads&quot;</tt>, <tt>&quot;repository&quot;</tt>, and <tt>&quot;prompt&quot;</tt>. All except <tt>&quot;repository&quot;</tt> and <tt>&quot;prompt&quot;</tt> are booleans, taking values 0 and 1, and behave like the corresponding command line option. The <tt>&quot;repository&quot;</tt> variable takes a string, and sets the remote repository location. The <tt>&quot;prompt&quot;</tt> variable takes a string, and sets the current default prompt. </p>
<p> If <i>var</i> or then <i>val</i> is not specified, it is prompted for.</dl>
<h3>show</h3>
<p> Synonym for &#8220;info&#8221;.</p>
<h3>uninstall</h3>
<p> Synonym for remove.</p>
<h3>update [<i>option</i>&#8230;] [<i>pkg</i>&#8230;]</h3>
<p> Updates the packages given as arguments to the latest version available at the installation source. Either <tt>&quot;--all&quot;</tt> or at least one <i>pkg</i> name must be specified. Options:</p>
<dl>
<dt><code>&#8211;all</code></p>
<dd> Update all installed packages except for <tt>&quot;tlmgr&quot;</tt> itself. If updates to <tt>&quot;tlmgr&quot;</tt> itself are present, this gives an error, unless also the option <tt>&quot;--force&quot;</tt> or <tt>&quot;--self&quot;</tt> is given. (See below.) </p>
<p> In addition to updating the installed packages, during the update of a collection the local installation is (by default) synchronized to the status of the collection on the server, for both additions and removals. </p>
<p> This means that if a package has been removed on the server (and thus has also been removed from the respective collection), <tt>&quot;tlmgr&quot;</tt> will remove the package in the local installation. This is called &#8220;auto-remove&#8221; and is announced as such when using the option <tt>&quot;--list&quot;</tt>. This auto-removal can be suppressed using the option <tt>&quot;--no-auto-remove&quot;</tt> (not recommended, see option description). </p>
<p> Analogously, if a package has been added to a collection on the server that is also installed locally, it will be added to the local installation. This is called &#8220;auto-install&#8221; and is announced as such when using the option <tt>&quot;--list&quot;</tt>. This auto-installation can be suppressed using the option <tt>&quot;--no-auto-install&quot;</tt> (also not recommended). </p>
<p> An exception to the collection dependency checks (including the auto-installation of packages just mentioned) are those that have been &#8220;forcibly removed&#8221; by you, that is, you called <tt>&quot;tlmgr remove --force&quot;</tt> on them. (See the <tt>&quot;remove&quot;</tt> action documentation.) To reinstall any such forcibly removed packages use <tt>&quot;--reinstall-forcibly-removed&quot;</tt>. </p>
<p> To reiterate: automatic removals and additions are entirely determined by comparison of collections. Thus, if you manually install an individual package <tt>&quot;foo&quot;</tt> which is later removed from the server, <tt>&quot;tlmgr&quot;</tt> will not notice and will not remove it locally. (It has to be this way, without major rearchitecture work, because the tlpdb does not record the repository from which packages come from.) </p>
<p> If you want to exclude some packages from the current update run (e.g., due to a slow link), see the <tt>&quot;--exclude&quot;</tt> option below.</p>
<dt><code>&#8211;self</code></p>
<dd> Update <tt>&quot;tlmgr&quot;</tt> itself (that is, the infrastructure packages) if updates to it are present. On Windows this includes updates to the private Perl interpreter shipped inside TeX Live. </p>
<p> If this option is given together with either <tt>&quot;--all&quot;</tt> or a list of packages, then <tt>&quot;tlmgr&quot;</tt> will be updated first and, if this update succeeds, the new version will be restarted to complete the rest of the updates. </p>
<p> In short: </p>
<pre><code>
tlmgr update-- self #update infrastructure only
        tlmgr update-- self-- all #update infrastructure and all packages
            tlmgr update-- force-- all #update all packages but *
    not *infrastructure
#... this last at your own risk, not recommended !
</code></pre>
<dt><code>&#8211;dry-run</code></p>
<dd> Nothing is actually installed; instead, the actions to be performed are written to the terminal. This is a more detailed report than <tt>&quot;--list&quot;</tt>.</p>
<dt><code>&#8211;list</code> [<i>pkg</i>]</p>
<dd> Concisely list the packages which would be updated, newly installed, or removed, without actually changing anything. If <tt>&quot;--all&quot;</tt> is also given, all available updates are listed. If <tt>&quot;--self&quot;</tt> is given, but not <tt>&quot;--all&quot;</tt>, only updates to the critical packages (tlmgr, texlive infrastructure, perl on Windows, etc.) are listed. If neither <tt>&quot;--all&quot;</tt> nor <tt>&quot;--self&quot;</tt> is given, and in addition no <i>pkg</i> is given, then <tt>&quot;--all&quot;</tt> is assumed (thus, <tt>&quot;tlmgr update --list&quot;</tt> is the same as <tt>&quot;tlmgr update --list --all&quot;</tt>). If neither <tt>&quot;--all&quot;</tt> nor <tt>&quot;--self&quot;</tt> is given, but specific package names are given, those packages are checked for updates.</p>
<dt><code>&#8211;exclude</code> <i>pkg</i></p>
<dd> Exclude <i>pkg</i> from the update process. If this option is given more than once, its arguments accumulate. </p>
<p> An argument <i>pkg</i> excludes both the package <i>pkg</i> itself and all its related platform-specific packages <i>pkg.ARCH</i>. For example, </p>
<pre>
  tlmgr update --all --exclude a2ping
</pre>
<p> will not update <tt>&quot;a2ping&quot;</tt>, <tt>&quot;a2ping.i386-linux&quot;</tt>, or any other <tt>&quot;a2ping.&quot;</tt><i></i><font SIZE="-1"><i>ARCH</i></font><i></i> package. </p>
<p> If this option specifies a package that would otherwise be a candidate for auto-installation, auto-removal, or reinstallation of a forcibly removed package, <tt>&quot;tlmgr&quot;</tt> quits with an error message. Excludes are not supported in these circumstances. </p>
<p> This option can also be set permanently in the tlmgr config file with the key <tt>&quot;update-exclude&quot;</tt>.</p>
<dt><code>&#8211;no-auto-remove</code> [<i>pkg</i>&#8230;]</p>
<dd> By default, <tt>&quot;tlmgr&quot;</tt> tries to remove packages in an existing collection which have disappeared on the server, as described above under <tt>&quot;--all&quot;</tt>. This option prevents such removals, either for all packages (with <tt>&quot;--all&quot;</tt>), or for just the given <i>pkg</i> names. This can lead to an inconsistent TeX installation, since packages are not infrequently renamed or replaced by their authors. Therefore this is not recommended.</p>
<dt><code>&#8211;no-auto-install</code> [<i>pkg</i>&#8230;]</p>
<dd> Under normal circumstances <tt>&quot;tlmgr&quot;</tt> will install packages which are new on the server, as described above under <tt>&quot;--all&quot;</tt>. This option prevents any such automatic installation, either for all packages (with <tt>&quot;--all&quot;</tt>), or the given <i>pkg</i> names. </p>
<p> Furthermore, after the <tt>&quot;tlmgr&quot;</tt> run using this has finished, the packages that would have been auto-installed <i>will be considered as forcibly removed</i>. So, if <tt>&quot;foobar&quot;</tt> is the only new package on the server, then </p>
<pre>
  tlmgr update --all --no-auto-install
</pre>
<p> is equivalent to </p>
<pre>
  tlmgr update --all
  tlmgr remove --force foobar
</pre>
<p> Again, since packages are sometimes renamed or replaced, using this option is not recommended.</p>
<dt><code>&#8211;reinstall-forcibly-removed</code></p>
<dd> Under normal circumstances <tt>&quot;tlmgr&quot;</tt> will not install packages that have been forcibly removed by the user; that is, removed with <tt>&quot;remove --force&quot;</tt>, or whose installation was prohibited by <tt>&quot;--no-auto-install&quot;</tt> during an earlier update. </p>
<p> This option makes <tt>&quot;tlmgr&quot;</tt> ignore the forcible removals and re-install all such packages. This can be used to completely synchronize an installation with the server&#8217;s idea of what is available: </p>
<pre>
  tlmgr update --reinstall-forcibly-removed --all
</pre>
<dt><code>&#8211;backup</code></p>
<dd>
<dt><code>&#8211;backupdir</code> <i>directory</i></p>
<dd> These two options control the creation of backups of packages <i>before</i> updating; that is, backing up packages as currently installed. If neither option is given, no backup will made. If <tt>&quot;--backupdir&quot;</tt> is given and specifies a writable directory then a backup will be made in that location. If only <tt>&quot;--backup&quot;</tt> is given, then a backup will be made to the directory previously set via the &#8220;option&#8221; action (see below). If both are given then a backup will be made to the specified <i>directory</i>. </p>
<p> You can also set options via the &#8220;option&#8221; action to automatically make backups for all packages, and/or keep only a certain number of backups. </p>
<p> <tt>&quot;tlmgr&quot;</tt> always makes a temporary backup when updating packages, in case of download or other failure during an update. In contrast, the purpose of this <tt>&quot;--backup&quot;</tt> option is to save a persistent backup in case the actual <i>content</i> of the update causes problems, e.g., introduces an TeX incompatibility. </p>
<p> The &#8220;restore&#8221; action explains how to restore from a backup.</p>
<dt><code>&#8211;no-depends</code></p>
<dd> If you call for updating a package normally all depending packages will also be checked for updates and updated if necessary. This switch suppresses this behavior.</p>
<dt><code>&#8211;no-depends-at-all</code></p>
<dd> See above under install (and beware).</p>
<dt><code>&#8211;force</code></p>
<dd> Force update of normal packages, without updating <tt>&quot;tlmgr&quot;</tt> itself (unless the <tt>&quot;--self&quot;</tt> option is also given). Not recommended. </p>
<p> Also, <tt>&quot;update --list&quot;</tt> is still performed regardless of this option.</dl>
<p> If the package on the server is older than the package already installed (e.g., if the selected mirror is out of date), <tt>&quot;tlmgr&quot;</tt> does not downgrade. Also, packages for uninstalled platforms are not installed. </p>
<p> <tt>&quot;tlmgr&quot;</tt> saves one copy of the main <tt>&quot;texlive.tlpdb&quot;</tt> file used for an update with a suffix representing the repository url, as in <tt>&quot;tlpkg/texlive.tlpdb.main.&quot;</tt><i>long-hash-string</i>. Thus, even when many mirrors are used, only one main <tt>&quot;tlpdb&quot;</tt> backup is kept. For non-main repositories, which do not generally have (m)any mirrors, no pruning of backups is done. </p>
<p> This action does not automatically add or remove new symlinks in system directories; you need to run <tt>&quot;tlmgr&quot;</tt> &#8220;path&#8221; yourself if you are using this feature and want new symlinks added.</p>
<h2>CONFIGURATION FILE FOR TLMGR</h2>
<p> <tt>&quot;tlmgr&quot;</tt> reads two configuration files: one is system-wide, in <tt>&quot;TEXMFSYSCONFIG/tlmgr/config&quot;</tt>, and the other is user-specific, in <tt>&quot;TEXMFCONFIG/tlmgr/config&quot;</tt>. The user-specific one is the default for the <tt>&quot;conf tlmgr&quot;</tt> action. (Run <tt>&quot;kpsewhich -var-value=TEXMFSYSCONFIG&quot;</tt> or <tt>&quot;... TEXMFCONFIG ...&quot;</tt> to see the actual directory names.) </p>
<p> A few defaults corresponding to command-line options can be set in these configuration files. In addition, the system-wide file can contain a directive to restrict the allowed actions. </p>
<p> In these config files, empty lines and lines starting with # are ignored. All other lines must look like: </p>
<pre>
  key = value
</pre>
<p> where the spaces are optional but the <tt>&quot;=&quot;</tt> is required. </p>
<p> The allowed keys are:</p>
<dl>
<dt>&quot;auto-remove&quot;, value 0 or 1 (default 1), same as command-line option.</p>
<dd>
<dt>&quot;gui-expertmode&quot;, value 0 or 1 (default 1). This switches between the full <font SIZE="-1">GUI</font> and a simplified <font SIZE="-1">GUI</font> with only the most common settings.</p>
<dd>
<dt>&quot;gui-lang&quot; <i>llcode</i>, with a language code value as with the command-line option.</p>
<dd>
<dt>&quot;no-checksums&quot;, value 0 or 1 (default 0, see below).</p>
<dd>
<dt>&quot;persistent-downloads&quot;, value 0 or 1 (default 1), same as command-line option.</p>
<dd>
<dt>&quot;require-verification&quot;, value 0 or 1 (default 0), same as command-line option.</p>
<dd>
<dt>&quot;tkfontscale&quot;, value any float. Controls the scaling of fonts in the Tk based frontends.</p>
<dd>
<dt>&quot;update-exclude&quot;, value: comma-separated list of packages (no space allowed). Same as the command line option &quot;&#8211;exclude&quot; for the action &quot;update&quot;.</p>
<dd>
<dt>&quot;verify-downloads&quot;, value 0 or 1 (default 1), same as command-line option.</p>
<dd></dl>
<p> The system-wide config file can contain one additional key:</p>
<dl>
<dt>&quot;allowed-actions&quot; <i>action1</i> [,<i>action</i>,&#8230;] The value is a comma-separated list of &quot;tlmgr&quot; actions which are allowed to be executed when &quot;tlmgr&quot; is invoked in system mode (that is, without &quot;&#8211;usermode&quot;).</p>
<dd> This allows distributors to include the <tt>&quot;tlmgr&quot;</tt> in their packaging, but allow only a restricted set of actions that do not interfere with their distro package manager. For native TeX Live installations, it doesn&#8217;t make sense to set this.</dl>
<p> The <tt>&quot;no-checksums&quot;</tt> key needs more explanation. By default, package checksums computed and stored on the server (in the <font SIZE="-1">TLPDB</font>) are compared to checksums computed locally after downloading. <tt>&quot;no-checksums&quot;</tt> disables this process. </p>
<p> The checksum algorithm is <font SIZE="-1">SHA-512.</font> Your system must have one of (looked for in this order) the Perl <tt>&quot;Digest::SHA&quot;</tt> module, the <tt>&quot;openssl&quot;</tt> program (&lt;<a rel="nofollow" href="https://openssl.org">https://openssl.org</a>&gt;), the <tt>&quot;sha512sum&quot;</tt> program (from <font SIZE="-1">GNU</font> Coreutils, &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils">https://www.gnu.org/software/coreutils</a>&gt;), or finally the <tt>&quot;shasum&quot;</tt> program (just to support old Macs). If none of these are available, a warning is issued and <tt>&quot;tlmgr&quot;</tt> proceeds without checking checksums. (Incidentally, other <font SIZE="-1">SHA</font> implementations, such as the pure Perl and pure Lua modules, are much too slow to be usable in our context.) <tt>&quot;no-checksums&quot;</tt> avoids the warning.</p>
<h2>CRYPTOGRAPHIC VERIFICATION</h2>
<p> <tt>&quot;tlmgr&quot;</tt> and <tt>&quot;install-tl&quot;</tt> perform cryptographic verification if possible. If verification is performed and successful, the programs report <tt>&quot;(verified)&quot;</tt> after loading the <font SIZE="-1">TLPDB</font>; otherwise, they report <tt>&quot;(not verified)&quot;</tt>. But either way, by default the installation and/or updates proceed normally. </p>
<p> If a program named <tt>&quot;gpg&quot;</tt> is available (that is, found in <tt>&quot;PATH&quot;</tt>), by default cryptographic signatures will be checked: we require the main repository be signed, but not any additional repositories. If <tt>&quot;gpg&quot;</tt> is not available, by default signatures are not checked and no verification is carried out, but <tt>&quot;tlmgr&quot;</tt> still proceeds normally. </p>
<p> The behavior of the verification can be controlled by the command line and config file option <tt>&quot;verify-repo&quot;</tt> which takes one of the following values: <tt>&quot;none&quot;</tt>, <tt>&quot;main&quot;</tt>, or <tt>&quot;all&quot;</tt>. With <tt>&quot;none&quot;</tt>, no verification whatsoever is attempted. With <tt>&quot;main&quot;</tt> (the default) verification is required only for the main repository, and only if <tt>&quot;gpg&quot;</tt> is available; though attempted for all, missing signatures of subsidiary repositories will not result in an error. Finally, in the case of <tt>&quot;all&quot;</tt>, <tt>&quot;gpg&quot;</tt> must be available and all repositories need to be signed. </p>
<p> In all cases, if a signature is checked and fails to verify, an error is raised. </p>
<p> Cryptographic verification requires checksum checking (described just above) to succeed, and a working GnuPG (<tt>&quot;gpg&quot;</tt>) program (see below for search method). Then, unless cryptographic verification has been disabled, a signature file (<tt>&quot;texlive.tlpdb.*.asc&quot;</tt>) of the checksum file is downloaded and the signature verified. The signature is created by the TeX Live Distribution <font SIZE="-1">GPG</font> key 0x0D5E5D9106BAB6BC, which in turn is signed by Karl Berry&#8217;s key 0x0716748A30D155AD and Norbert Preining&#8217;s key 0x6CACA448860CDC13. All of these keys are obtainable from the standard key servers. </p>
<p> Additional trusted keys can be added using the <tt>&quot;key&quot;</tt> action.</p>
<h3>Configuration of GnuPG invocation</h3>
<p> The executable used for GnuPG is searched as follows: If the environment variable <tt>&quot;TL_GNUPG&quot;</tt> is set, it is tested and used; otherwise <tt>&quot;gpg&quot;</tt> is checked; finally <tt>&quot;gpg2&quot;</tt> is checked. </p>
<p> Further adaptation of the <tt>&quot;gpg&quot;</tt> invocation can be made using the two environment variables <tt>&quot;TL_GNUPGHOME&quot;</tt>, which is passed to <tt>&quot;gpg&quot;</tt> as the value for <tt>&quot;--homedir&quot;</tt>, and <tt>&quot;TL_GNUPGARGS&quot;</tt>, which replaces the default options <tt>&quot;--no-secmem-warning --no-permission-warning&quot;</tt>.</p>
<h2>USER MODE</h2>
<p> <tt>&quot;tlmgr&quot;</tt> provides a restricted way, called &#8220;user mode&#8221;, to manage arbitrary texmf trees in the same way as the main installation. For example, this allows people without write permissions on the installation location to update/install packages into a tree of their own. </p>
<p> <tt>&quot;tlmgr&quot;</tt> is switched into user mode with the command line option <tt>&quot;--usermode&quot;</tt>. It does not switch automatically, nor is there any configuration file setting for it. Thus, this option has to be explicitly given every time user mode is to be activated. </p>
<p> This mode of <tt>&quot;tlmgr&quot;</tt> works on a user tree, by default the value of the <tt>&quot;TEXMFHOME&quot;</tt> variable. This can be overridden with the command line option <tt>&quot;--usertree&quot;</tt>. In the following when we speak of the user tree we mean either <tt>&quot;TEXMFHOME&quot;</tt> or the one given on the command line. </p>
<p> Not all actions are allowed in user mode; <tt>&quot;tlmgr&quot;</tt> will warn you and not carry out any problematic actions. Currently not supported (and probably will never be) is the <tt>&quot;platform&quot;</tt> action. The <tt>&quot;gui&quot;</tt> action is currently not supported, but may be in a future release. </p>
<p> Some <tt>&quot;tlmgr&quot;</tt> actions don&#8217;t need any write permissions and thus work the same in user mode and normal mode. Currently these are: <tt>&quot;check&quot;</tt>, <tt>&quot;help&quot;</tt>, <tt>&quot;list&quot;</tt>, <tt>&quot;print-platform&quot;</tt>, <tt>&quot;print-platform-info&quot;</tt>, <tt>&quot;search&quot;</tt>, <tt>&quot;show&quot;</tt>, <tt>&quot;version&quot;</tt>. </p>
<p> On the other hand, most of the actions dealing with package management do need write permissions, and thus behave differently in user mode, as described below: <tt>&quot;install&quot;</tt>, <tt>&quot;update&quot;</tt>, <tt>&quot;remove&quot;</tt>, <tt>&quot;option&quot;</tt>, <tt>&quot;paper&quot;</tt>, <tt>&quot;generate&quot;</tt>, <tt>&quot;backup&quot;</tt>, <tt>&quot;restore&quot;</tt>, <tt>&quot;uninstall&quot;</tt>, <tt>&quot;symlinks&quot;</tt>. </p>
<p> Before using <tt>&quot;tlmgr&quot;</tt> in user mode, you have to set up the user tree with the <tt>&quot;init-usertree&quot;</tt> action. This creates <i>usertree</i><tt>&quot;/web2c&quot;</tt> and <i>usertree</i><tt>&quot;/tlpkg/tlpobj&quot;</tt>, and a minimal <i>usertree</i><tt>&quot;/tlpkg/texlive.tlpdb&quot;</tt>. At that point, you can tell <tt>&quot;tlmgr&quot;</tt> to do the (supported) actions by adding the <tt>&quot;--usermode&quot;</tt> command line option. </p>
<p> In user mode the file <i>usertree</i><tt>&quot;/tlpkg/texlive.tlpdb&quot;</tt> contains only the packages that have been installed into the user tree using <tt>&quot;tlmgr&quot;</tt>, plus additional options from the &#8220;virtual&#8221; package <tt>&quot;00texlive.installation&quot;</tt> (similar to the main installation&#8217;s <tt>&quot;texlive.tlpdb&quot;</tt>). </p>
<p> All actions on packages in user mode can only be carried out on packages that are known as <tt>&quot;relocatable&quot;</tt>. This excludes all packages containing executables and a few other core packages. Of the 2500 or so packages currently in TeX Live the vast majority are relocatable and can be installed into a user tree. </p>
<p> Description of changes of actions in user mode:</p>
<h3>User mode install</h3>
<p> In user mode, the <tt>&quot;install&quot;</tt> action checks that the package and all dependencies are all either relocated or already installed in the system installation. If this is the case, it unpacks all containers to be installed into the user tree (to repeat, that&#8217;s either <tt>&quot;TEXMFHOME&quot;</tt> or the value of <tt>&quot;--usertree&quot;</tt>) and add the respective packages to the user tree&#8217;s <tt>&quot;texlive.tlpdb&quot;</tt> (creating it if need be). </p>
<p> Currently installing a collection in user mode installs all dependent packages, but in contrast to normal mode, does <i>not</i> install dependent collections. For example, in normal mode <tt>&quot;tlmgr install collection-context&quot;</tt> would install <tt>&quot;collection-basic&quot;</tt> and other collections, while in user mode, <i>only</i> the packages mentioned in <tt>&quot;collection-context&quot;</tt> are installed. </p>
<p> If a package shipping map files is installed in user mode, a backup of the user&#8217;s <tt>&quot;updmap.cfg&quot;</tt> in <tt>&quot;USERTREE/web2c/&quot;</tt> is made, and then this file regenerated from the list of installed packages.</p>
<h3>User mode backup, restore, remove, update</h3>
<p> In user mode, these actions check that all packages to be acted on are installed in the user tree before proceeding; otherwise, they behave just as in normal mode.</p>
<h3>User mode generate, option, paper</h3>
<p> In user mode, these actions operate only on the user tree&#8217;s configuration files and/or <tt>&quot;texlive.tlpdb&quot;</tt>. creates configuration files in user tree</p>
<h2>MULTIPLE REPOSITORIES</h2>
<p> The main TeX Live repository contains a vast array of packages. Nevertheless, additional local repositories can be useful to provide locally-installed resources, such as proprietary fonts and house styles. Also, alternative package repositories distribute packages that cannot or should not be included in TeX Live, for whatever reason. </p>
<p> The simplest and most reliable method is to temporarily set the installation source to any repository (with the <tt>&quot;-repository&quot;</tt> or <tt>&quot;option repository&quot;</tt> command line options), and perform your operations. </p>
<p> When you are using multiple repositories over a sustained length of time, however, explicitly switching between them becomes inconvenient. Thus, it&#8217;s possible to tell <tt>&quot;tlmgr&quot;</tt> about additional repositories you want to use. The basic command is <tt>&quot;tlmgr repository add&quot;</tt>. The rest of this section explains further. </p>
<p> When using multiple repositories, one of them has to be set as the main repository, which distributes most of the installed packages. When you switch from a single repository installation to a multiple repository installation, the previous sole repository will be set as the main repository. </p>
<p> By default, even if multiple repositories are configured, packages are <i>still</i> <i>only</i> installed from the main repository. Thus, simply adding a second repository does not actually enable installation of anything from there. You also have to specify which packages should be taken from the new repository, by specifying so-called &#8220;pinning&#8221; rules, described next.</p>
<h3>Pinning</h3>
<p> When a package <tt>&quot;foo&quot;</tt> is pinned to a repository, a package <tt>&quot;foo&quot;</tt> in any other repository, even if it has a higher revision number, will not be considered an installable candidate. </p>
<p> As mentioned above, by default everything is pinned to the main repository. Let&#8217;s now go through an example of setting up a second repository and enabling updates of a package from it. </p>
<p> First, check that we have support for multiple repositories, and have only one enabled (as is the case by default): </p>
<pre>
 $ tlmgr repository list
 List of repositories (with tags if set):
   /var/www/norbert/tlnet
</pre>
<p> Ok. Let&#8217;s add the <tt>&quot;tlcontrib&quot;</tt> repository (this is a real repository hosted at &lt;<a rel="nofollow" href="http://contrib.texlive.info">http://contrib.texlive.info</a>&gt;) with the tag <tt>&quot;tlcontrib&quot;</tt>: </p>
<pre>
 $ tlmgr repository add <a rel="nofollow" href="http://contrib.texlive.info/current">http://contrib.texlive.info/current</a> tlcontrib
</pre>
<p> Check the repository list again: </p>
<pre>
 $ tlmgr repository list
 List of repositories (with tags if set):
    <a rel="nofollow" href="http://contrib.texlive.info/current">http://contrib.texlive.info/current</a> (tlcontrib)
    /var/www/norbert/tlnet (main)
</pre>
<p> Now we specify a pinning entry to get the package <tt>&quot;classico&quot;</tt> from <tt>&quot;tlcontrib&quot;</tt>: </p>
<pre>
 $ tlmgr pinning add tlcontrib classico
</pre>
<p> Check that we can find <tt>&quot;classico&quot;</tt>: </p>
<pre>
 $ tlmgr show classico
 package:     classico
 ...
 shortdesc:   URW Classico fonts
 ...
</pre>
<p> &#8211; install <tt>&quot;classico&quot;</tt>: </p>
<pre><code>
 $ tlmgr install classico
 tlmgr: package repositories:
 ...
 [1/1,  ??:??/??:??] install: classico @tlcontrib [737k]
</code></pre>
<p> In the output here you can see that the <tt>&quot;classico&quot;</tt> package has been installed from the <tt>&quot;tlcontrib&quot;</tt> repository (<tt>@tlcontrib</tt>). </p>
<p> Finally, <tt>&quot;tlmgr pinning&quot;</tt> also supports removing certain or all packages from a given repository: </p>
<pre>
  $ tlmgr pinning remove tlcontrib classico # remove just classico
  $ tlmgr pinning remove tlcontrib --all    # take nothing from tlcontrib
</pre>
<p> A summary of <tt>&quot;tlmgr pinning&quot;</tt> actions is given above.</p>
<h2>GUI FOR TLMGR</h2>
<p> The graphical user interface for <tt>&quot;tlmgr&quot;</tt> requires Perl/Tk &lt;<a rel="nofollow" href="https://search.cpan.org/search?query=perl%2Ftk">https://search.cpan.org/search?query=perl%2Ftk</a>&gt;. For Unix-based systems Perl/Tk (as well as Perl of course) has to be installed outside of <font SIZE="-1">TL.</font> &lt;<a rel="nofollow" href="https://tug.org/texlive/distro.html#perltk">https://tug.org/texlive/distro.html#perltk</a>&gt; has a list of invocations for some distros. For Windows the necessary modules are no longer shipped within TeX Live, so you&#8217;ll have to have an external Perl available that includes them. </p>
<p> We are talking here about the <font SIZE="-1">GUI</font> built into tlmgr itself, not about the other tlmgr GUIs, which are: tlshell (Tcl/Tk-based), tlcockpit (Java-based) and, only on Macs, TeX Live Utility. These are invoked as separate programs. </p>
<p> The <font SIZE="-1">GUI</font> mode of tlmgr is started with the invocation <tt>&quot;tlmgr gui&quot;</tt>; assuming Tk is loadable, the graphical user interface will be shown. The main window contains a menu bar, the main display, and a status area where messages normally shown on the console are displayed. </p>
<p> Within the main display there are three main parts: the <tt>&quot;Display configuration&quot;</tt> area, the list of packages, and the action buttons. </p>
<p> Also, at the top right the currently loaded repository is shown; this also acts as a button and when clicked will try to load the default repository. To load a different repository, see the <tt>&quot;tlmgr&quot;</tt> menu item. </p>
<p> Finally, the status area at the bottom of the window gives additional information about what is going on.</p>
<h3>Main display</h3>
<p> <i>Display configuration area</i> </p>
<p> The first part of the main display allows you to specify (filter) which packages are shown. By default, all are shown. Changes here are reflected right away.</p>
<dl>
<dt>Status</p>
<dd> Select whether to show all packages (the default), only those installed, only those <i>not</i> installed, or only those with update available.</p>
<dt>Category</p>
<dd> Select which categories are shown: packages, collections, and/or schemes. These are briefly explained in the &#8220;<font SIZE="-1">DESCRIPTION&#8221;</font> section above.</p>
<dt>Match</p>
<dd> Select packages matching for a specific pattern. By default, this searches both descriptions and filenames. You can also select a subset for searching.</p>
<dt>Selection</p>
<dd> Select packages to those selected, those not selected, or all. Here, &#8220;selected&#8221; means that the checkbox in the beginning of the line of a package is ticked.</p>
<dt>Display configuration buttons</p>
<dd> To the right there are three buttons: select all packages, select none (a.k.a. deselect all), and reset all these filters to the defaults, i.e., show all available.</dl>
<p> <i>Package list area</i> </p>
<p> The second are of the main display lists all installed packages. If a repository is loaded, those that are available but not installed are also listed. </p>
<p> Double clicking on a package line pops up an informational window with further details: the long description, included files, etc. </p>
<p> Each line of the package list consists of the following items:</p>
<dl>
<dt>a checkbox</p>
<dd> Used to select particular packages; some of the action buttons (see below) work only on the selected packages.</p>
<dt>package name</p>
<dd> The name (identifier) of the package as given in the database.</p>
<dt>local revision (and version)</p>
<dd> If the package is installed the TeX Live revision number for the installed package will be shown. If there is a catalogue version given in the database for this package, it will be shown in parentheses. However, the catalogue version, unlike the <font SIZE="-1">TL</font> revision, is not guaranteed to reflect what is actually installed.</p>
<dt>remote revision (and version)</p>
<dd> If a repository has been loaded the revision of the package in the repository (if present) is shown. As with the local column, if a catalogue version is provided it will be displayed. And also as with the local column, the catalogue version may be stale.</p>
<dt>short description</p>
<dd> The short description of the package.</dl>
<p> <i>Main display action buttons</i> </p>
<p> Below the list of packages are several buttons:</p>
<dl>
<dt>Update all installed</p>
<dd> This calls <tt>&quot;tlmgr update --all&quot;</tt>, i.e., tries to update all available packages. Below this button is a toggle to allow reinstallation of previously removed packages as part of this action. </p>
<p> The other four buttons only work on the selected packages, i.e., those where the checkbox at the beginning of the package line is ticked.</p>
<dt>Update</p>
<dd> Update only the selected packages.</p>
<dt>Install</p>
<dd> Install the selected packages; acts like <tt>&quot;tlmgr install&quot;</tt>, i.e., also installs dependencies. Thus, installing a collection installs all its constituent packages.</p>
<dt>Remove</p>
<dd> Removes the selected packages; acts like <tt>&quot;tlmgr remove&quot;</tt>, i.e., it will also remove dependencies of collections (but not dependencies of normal packages).</p>
<dt>Backup</p>
<dd> Makes a backup of the selected packages; acts like <tt>&quot;tlmgr backup&quot;</tt>. This action needs the option <tt>&quot;backupdir&quot;</tt> set (see <tt>&quot;Options -&quot;</tt> General&gt;).</dl>
<h3>Menu bar</h3>
<p> The following entries can be found in the menu bar:</p>
<dl>
<dt>&quot;tlmgr&quot; menu</p>
<dd> The items here load various repositories: the default as specified in the TeX Live database, the default network repository, the repository specified on the command line (if any), and an arbitrarily manually-entered one. Also has the so-necessary <tt>&quot;quit&quot;</tt> operation.</p>
<dt>&quot;Options menu&quot;</p>
<dd> Provides access to several groups of options: <tt>&quot;Paper&quot;</tt> (configuration of default paper sizes), <tt>&quot;Platforms&quot;</tt> (only on Unix, configuration of the supported/installed platforms), <tt>&quot;GUI Language&quot;</tt> (select language used in the <font SIZE="-1">GUI</font> interface), and <tt>&quot;General&quot;</tt> (everything else). </p>
<p> Several toggles are also here. The first is <tt>&quot;Expert options&quot;</tt>, which is set by default. If you turn this off, the next time you start the <font SIZE="-1">GUI</font> a simplified screen will be shown that display only the most important functionality. This setting is saved in the configuration file of <tt>&quot;tlmgr&quot;</tt>; see &#8220;<font SIZE="-1">CONFIGURATION FILE FOR TLMGR&#8221;</font> for details. </p>
<p> The other toggles are all off by default: for debugging output, to disable the automatic installation of new packages, and to disable the automatic removal of packages deleted from the server. Playing with the choices of what is or isn&#8217;t installed may lead to an inconsistent TeX Live installation; e.g., when a package is renamed.</p>
<dt>&quot;Actions menu&quot;</p>
<dd> Provides access to several actions: update the filename database (aka <tt>&quot;ls-R&quot;</tt>, <tt>&quot;mktexlsr&quot;</tt>, <tt>&quot;texhash&quot;</tt>), rebuild all formats (<tt>&quot;fmtutil-sys --all&quot;</tt>), update the font map database (<tt>&quot;updmap-sys&quot;</tt>), restore from a backup of a package, and use of symbolic links in system directories (not on Windows). </p>
<p> The final action is to remove the entire TeX Live installation (also not on Windows).</p>
<dt>&quot;Help menu&quot;</p>
<dd> Provides access to the TeX Live manual (also on the web at &lt;<a rel="nofollow" href="https://tug.org/texlive/doc.html">https://tug.org/texlive/doc.html</a>&gt;) and the usual &#8220;About&#8221; box.</dl>
<h3><font SIZE="-1">GUI</font> options</h3>
<p> Some generic Perl/Tk options can be specified with <tt>&quot;tlmgr gui&quot;</tt> to control the display:</p>
<dl>
<dt>&quot;-background&quot; <i>color</i></p>
<dd> Set background color.</p>
<dt>&quot;-font &quot;&quot; <i>fontname</i> <i>fontsize</i> &quot;&quot;&quot;</p>
<dd> Set font, e.g., <tt>&quot;tlmgr gui -font &quot;helvetica 18&quot;&quot;</tt>. The argument to <tt>&quot;-font&quot;</tt> must be quoted, i.e., passed as a single string.</p>
<dt>&quot;-foreground&quot; <i>color</i></p>
<dd> Set foreground color.</p>
<dt>&quot;-geometry&quot; <i>geomspec</i></p>
<dd> Set the X geometry, e.g., <tt>&quot;tlmgr gui -geometry 1024x512-0+0&quot;</tt> creates the window of (approximately) the given size in the upper-right corner of the display.</p>
<dt>&quot;-xrm&quot; <i>xresource</i></p>
<dd> Pass the arbitrary X resource string <i>xresource</i>.</dl>
<p> A few other obscure options are recognized but not mentioned here. See the Perl/Tk documentation (&lt;<a rel="nofollow" href="https://search.cpan.org/perldoc?Tk">https://search.cpan.org/perldoc?Tk</a>&gt;) for the complete list, and any X documentation for general information.</p>
<h2>MACHINE-READABLE OUTPUT</h2>
<p> With the <tt>&quot;--machine-readable&quot;</tt> option, <tt>&quot;tlmgr&quot;</tt> writes to stdout in the fixed line-oriented format described here, and the usual informational messages for human consumption are written to stderr (normally they are written to stdout). The idea is that a program can get all the information it needs by reading stdout. </p>
<p> Currently this option only applies to the update, install, and &#8220;option&#8221; actions.</p>
<h3>Machine-readable update and install output</h3>
<p> The output format is as follows: </p>
<pre>
  fieldname &quot;	&quot; value
  ...
  &quot;end-of-header&quot;
  pkgname status localrev serverrev size runtime esttot
  ...
  &quot;end-of-updates&quot;
  other output from post actions, not in machine readable form
</pre>
<p> The header section currently has two fields: <tt>&quot;location-url&quot;</tt> (the repository source from which updates are being drawn), and <tt>&quot;total-bytes&quot;</tt> (the total number of bytes to be downloaded). </p>
<p> The <i>localrev</i> and <i>serverrev</i> fields for each package are the revision numbers in the local installation and server repository, respectively. The <i>size</i> field is the number of bytes to be downloaded, i.e., the size of the compressed tar file for a network installation, not the unpacked size. The runtime and esttot fields are only present for updated and auto-install packages, and contain the currently passed time since start of installation/updates and the estimated total time. </p>
<p> Line endings may be either <font SIZE="-1">LF</font> or <font SIZE="-1">CRLF</font> depending on the current platform.</p>
<dl>
<dt>&quot;location-url&quot; <i>location</i></p>
<dd> The <i>location</i> may be a url (including <tt>&quot;file:///foo/bar/...&quot;</tt>), or a directory name (<tt>&quot;/foo/bar&quot;</tt>). It is the package repository from which the new package information was drawn.</p>
<dt>&quot;total-bytes&quot; <i>count</i></p>
<dd> The <i>count</i> is simply a decimal number, the sum of the sizes of all the packages that need updating or installing (which are listed subsequently).</dl>
<p> Then comes a line with only the literal string <tt>&quot;end-of-header&quot;</tt>. </p>
<p> Each following line until a line with literal string <tt>&quot;end-of-updates&quot;</tt> reports on one package. The fields on each line are separated by a tab. Here are the fields.</p>
<dl>
<dt><i>pkgname</i></p>
<dd> The TeX Live package identifier, with a possible platform suffix for executables. For instance, <tt>&quot;pdftex&quot;</tt> and <tt>&quot;pdftex.i386-linux&quot;</tt> are given as two separate packages, one on each line.</p>
<dt><i>status</i></p>
<dd> The status of the package update. One character, as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&quot;d&quot;</p>
<dd> The package was removed on the server.</p>
<dt>&quot;f&quot;</p>
<dd> The package was removed in the local installation, even though a collection depended on it. (E.g., the user ran <tt>&quot;tlmgr remove --force&quot;</tt>.)</p>
<dt>&quot;u&quot;</p>
<dd> Normal update is needed.</p>
<dt>&quot;r&quot;</p>
<dd> Reversed non-update: the locally-installed version is newer than the version on the server.</p>
<dt>&quot;a&quot;</p>
<dd> Automatically-determined need for installation, the package is new on the server and is (most probably) part of an installed collection.</p>
<dt>&quot;i&quot;</p>
<dd> Package will be installed and isn&#8217;t present in the local installation (action install).</p>
<dt>&quot;I&quot;</p>
<dd> Package is already present but will be reinstalled (action install).</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><i>localrev</i></p>
<dd> The revision number of the installed package, or <tt>&quot;-&quot;</tt> if it is not present locally.</p>
<dt><i>serverrev</i></p>
<dd> The revision number of the package on the server, or <tt>&quot;-&quot;</tt> if it is not present on the server.</p>
<dt><i>size</i></p>
<dd> The size in bytes of the package on the server. The sum of all the package sizes is given in the <tt>&quot;total-bytes&quot;</tt> header field mentioned above.</p>
<dt><i>runtime</i></p>
<dd> The run time since start of installations or updates.</p>
<dt><i>esttot</i></p>
<dd> The estimated total time.</dl>
<h3>Machine-readable option output</h3>
<p> The output format is as follows: </p>
<pre>
  key &quot;	&quot; value
</pre>
<p> If a value is not saved in the database the string <tt>&quot;(not set)&quot;</tt> is shown. </p>
<p> If you are developing a program that uses this output, and find that changes would be helpful, do not hesitate to write the mailing list.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> <tt>&quot;tlmgr&quot;</tt> uses many of the standard TeX environment variables, as reported by, e.g., <tt>&quot;tlmgr conf&quot;</tt> (&#8220;conf&#8221;). </p>
<p> In addition, for ease in scripting and debugging, <tt>&quot;tlmgr&quot;</tt> looks for the following environment variables. These are not of interest for normal user installations.</p>
<dl>
<dt>&quot;TEXLIVE_COMPRESSOR&quot;</p>
<dd> This variable allows selecting a different compressor program for backups and intermediate rollback containers. The order of selection is:</p>
<dl>
<dt>
<dd>
<dl>
<dt>1.</p>
<dd> If the environment variable <tt>&quot;TEXLIVE_COMPRESSOR&quot;</tt> is defined, use it; abort if it doesn&#8217;t work. Possible values: <tt>&quot;lz4&quot;</tt>, <tt>&quot;gzip&quot;</tt>, <tt>&quot;xz&quot;</tt>. The necessary options are added internally.</p>
<dt>2.</p>
<dd> If lz4 is available (either from the system or <font SIZE="-1">TL</font>) and working, use that.</p>
<dt>3.</p>
<dd> If gzip is available (from the system) and working, use that.</p>
<dt>4.</p>
<dd> If xz is available (either from the system or <font SIZE="-1">TL</font>) and working, use that.</dl>
</dl>
<dl>
<dt>
<dd>
<p> lz4 and gzip are faster in creating tlmgr&#8217;s local backups, hence they are preferred. The unconditional use of xz for the tlnet containers is unaffected, to minimize download sizes.</dl>
<dt>&quot;TEXLIVE_DOWNLOADER&quot;</p>
<dd>
<dt>&quot;TL_DOWNLOAD_PROGRAM&quot;</p>
<dd>
<dt>&quot;TL_DOWNLOAD_ARGS&quot;</p>
<dd> These options allow selecting different download programs then the ones automatically selected by the installer. The order of selection is:</p>
<dl>
<dt>
<dd>
<dl>
<dt>1.</p>
<dd> If the environment variable <tt>&quot;TEXLIVE_DOWNLOADER&quot;</tt> is defined, use it; abort if the specified program doesn&#8217;t work. Possible values: <tt>&quot;lwp&quot;</tt>, <tt>&quot;curl&quot;</tt>, <tt>&quot;wget&quot;</tt>. The necessary options are added internally.</p>
<dt>2.</p>
<dd> If the environment variable <tt>&quot;TL_DOWNLOAD_PROGRAM&quot;</tt> is defined (can be any value), use it together with <tt>&quot;TL_DOWNLOAD_ARGS&quot;</tt>; abort if it doesn&#8217;t work.</p>
<dt>3.</p>
<dd> If <font SIZE="-1">LWP</font> is available and working, use that (by far the most efficient method, as it supports persistent downloads).</p>
<dt>4.</p>
<dd> If curl is available (from the system) and working, use that.</p>
<dt>5.</p>
<dd> If wget is available (either from the system or <font SIZE="-1">TL</font>) and working, use that.</dl>
</dl>
<dl>
<dt>
<dd>
<p> <font SIZE="-1">TL</font> provides <tt>&quot;wget&quot;</tt> binaries for platforms where necessary, so some download method should always be available.</dl>
<dt>&quot;TEXLIVE_PREFER_OWN&quot;</p>
<dd> By default, compression and download programs provided by the system, i.e., found along <tt>&quot;PATH&quot;</tt> are preferred over those shipped with TeX Live. </p>
<p> This can create problems with systems that are too old, and so can be overridden by setting the environment variable <tt>&quot;TEXLIVE_PREFER_OWN&quot;</tt> to 1. In this case, executables shipped with <font SIZE="-1">TL</font> will be preferred. </p>
<p> Extra compression/download programs not provided by <font SIZE="-1">TL,</font> such as gzip, lwp, and curl, are still checked for on the system and used if available, per the above. <tt>&quot;TEXLIVE_PREFER_OWN&quot;</tt> only applies when the program being checked for is shipped with <font SIZE="-1">TL,</font> namely the lz4 and xz compressors and wget downloader. </p>
<p> Exception: on Windows, the <tt>&quot;tar.exe&quot;</tt> shipped with <font SIZE="-1">TL</font> is always used, regardless of any setting.</dl>
<h2>AUTHORS AND COPYRIGHT</h2>
<p> This script and its documentation were written for the TeX Live distribution (&lt;<a rel="nofollow" href="https://tug.org/texlive">https://tug.org/texlive</a>&gt;) and both are licensed under the <font SIZE="-1">GNU</font> General Public License Version 2 or later. </p>
<p> <tt>$Id:</tt> tlmgr.pl 60557 2021-09-20 10:46:43Z preining $ </p>
<h2>Index</h2>
<dt><a href="#lbBL">CONFIGURATION FILE FOR TLMGR</a></p>
<dd>
<dt><a href="#lbBM">CRYPTOGRAPHIC VERIFICATION</a></p>
<dd>
<dt><a href="#lbBO">USER MODE</a></p>
<dd>
<dt><a href="#lbBS">MULTIPLE REPOSITORIES</a></p>
<dd>
<dt><a href="#lbBU">GUI FOR TLMGR</a></p>
<dd>
<dt><a href="#lbBY">MACHINE-READABLE OUTPUT</a></p>
<dd>
<dt><a href="#lbCB">ENVIRONMENT VARIABLES</a></p>
<dd>
<dt><a href="#lbCC">AUTHORS AND COPYRIGHT</a></p>
<dd></dl>
