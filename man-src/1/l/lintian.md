---
title: "lintian(1)"
name: "lintian"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lintian/"
description: "lintian – Static analysis tool for Debian packages"
---

<h2 class="name">NAME</h2>
<p> lintian &#8211; Static analysis tool for Debian packages </p>
<h2>SYNOPSIS</h2>
<p> <code>lintian</code> [<i>action</i>] [<i>options</i>] [<i>packages</i>] &#8230;</p>
<h2>DESCRIPTION</h2>
<p> Lintian dissects Debian packages and reports bugs and policy violations. It contains automated checks for many aspects of Debian policy as well as some checks for common errors. </p>
<p> There are two ways to specify binary, udeb or source packages for Lintian to process: by file name (the .deb file for a binary package or the .dsc file for a source package), or by naming a <i>.changes</i> file. </p>
<p> If you specify a <i>.changes</i> file, Lintian will process all packages listed in that file. This is convenient when checking a new package before uploading it. </p>
<p> If you specify packages to be checked or use the option <code>&#8211;packages-from-file</code>, the packages requested will be processed. Otherwise, if <i>debian/changelog</i> exists, it is parsed to determine the name of the .changes file to look for in the parent directory (when using the actions <code>&#8211;check</code> or <code>&#8211;unpack</code>). See &#8220;<font SIZE="-1">CHECKING LAST BUILD&#8221;</font> for more information.</p>
<h2>OPTIONS</h2>
<p> Actions of the lintian command: (Only one action can be specified per invocation)</p>
<dl>
<dt><code>-c</code>, <code>&#8211;check</code></p>
<dd> Run all checks over the specified packages. This is the default action.</p>
<dt><code>-C</code> chk1,chk2,&#8230;, <code>&#8211;check-part</code> chk1,chk2,&#8230;</p>
<dd> Run only the specified checks. You can either specify the name of the check script or the abbreviation. For details, see the &#8220;<font SIZE="-1">CHECKS&#8221;</font> section below.</p>
<dt><code>-F</code>, <code>&#8211;ftp-master-rejects</code></p>
<dd> Run only the checks that issue tags that result in automatic rejects from the Debian upload queue. The list of such tags is refreshed with each Lintian release, so may be slightly out of date if it has changed recently. </p>
<p> This is implemented via a profile and thus this option cannot be used together with <code>&#8211;profile</code>.</p>
<dt><code>-T</code> tag1,tag2,&#8230;, <code>&#8211;tags</code> tag1,tag2,&#8230;</p>
<dd> Run only the checks that issue the requested tags. The tests for other tags within the check scripts will be run but the tags will not be issued. </p>
<p> With this options all tags listed will be displayed regardless of the display settings.</p>
<dt><code>&#8211;tags-from-file</code> filename</p>
<dd> Same functionality as <code>&#8211;tags</code>, but read the list of tags from a file. Blank lines and lines beginning with # are ignored. All other lines are taken to be tag names or comma-separated lists of tag names to (potentially) issue. </p>
<p> With this options all tags listed will be displayed regardless of the display settings.</p>
<dt><code>-u</code>, <code>&#8211;unpack</code></p>
<dd> Unpacks the package will all collections. See the &#8220;<font SIZE="-1">COLLECTION&#8221;</font> section below. </p>
<p> Note in this option will also run all collections. See the &#8220;<font SIZE="-1">COLLECTION&#8221;</font> section below.</p>
<dt><code>-X</code> chk1,chk2,&#8230;, <code>&#8211;dont-check-part</code> chk1,chk2,&#8230;</p>
<dd> Run all but the specified checks. You can either specify the name of the check script or the abbreviation. For details, see the &#8220;<font SIZE="-1">CHECKS&#8221;</font> section below.</dl>
<p> General options:</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display usage information and exit.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Suppress all informational messages including override comments (normally shown with <code>&#8211;show-overrides</code>). </p>
<p> This option is silently ignored if <code>&#8211;debug</code> is given. Otherwise, if both <code>&#8211;verbose</code> and <code>&#8211;quiet</code> is used, the last of these two options take effect. </p>
<p> This option overrides the <code>verbose</code> and the <code>quiet</code> variable in the configuration file. In the configuration file, this option is enabled by using <code>quiet</code> variable. The <code>verbose</code> and <code>quiet</code> variables may not both appear in the config file.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Display verbose messages. </p>
<p> If <code>&#8211;debug</code> is used this option is always enabled. Otherwise, if both <code>&#8211;verbose</code> and <code>&#8211;quiet</code> is used (and <code>&#8211;debug</code> is not used), the last of these two options take effect. </p>
<p> This option overrides the <code>quiet</code> variable in the configuration file. In the configuration file, this option is enabled by using <code>verbose</code> variable. The <code>verbose</code> and <code>quiet</code> variables may not both appear in the config file.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Display lintian version number and exit.</p>
<dt><code>&#8211;print-version</code></p>
<dd> Print unadorned version number and exit.</dl>
<p> Behavior options for <code>lintian</code>.</p>
<dl>
<dt><code>&#8211;color</code> (never|always|auto|html)</p>
<dd> Whether to colorize tags in lintian output based on their visibility. The default is &#8220;never&#8221;, which never uses color. &#8220;always&#8221; will always use color, &#8220;auto&#8221; will use color only if the output is going to a terminal, and &#8220;html&#8221; will use <font SIZE="-1">HTML</font> &lt;span&gt; tags with a color style attribute (instead of <font SIZE="-1">ANSI</font> color escape sequences). </p>
<p> This option overrides the <code>color</code> variable in the configuration file.</p>
<dt><code>&#8211;hyperlinks</code> (on|off)</p>
<dd> Shows text-based hyperlinks to tag descriptions on lintian.debian.org on terminals that support it. The default is on for terminals that support it, unless the user selected &#8216;&#8211;color never&#8217;. This currently only works in <font SIZE="-1">GNOME</font> Terminal. </p>
<p> This option overrides the <code>color</code> variable in the configuration file.</p>
<dt><code>&#8211;default-display-level</code></p>
<dd> Reset the current display level to the default. Basically, this option behaves exactly like passing the following options to lintian:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>-L</code> &#8220;&gt;=warning&#8221;</dl>
</dl>
<dl>
<dt>
<dd>
<p> The primary use for this is to ensure that lintian&#8217;s display level has been reset to the built-in default values. Notably, this can be used to override display settings earlier on the command-line or in the lintian configuration file. </p>
<p> Further changes to the display level can be done <i>after</i> this option. Example: <code>&#8211;default-display-level &#8211;display-info</code> gives you the default display level plus informational (&#8220;I:&#8221;) tags.</dl>
<dt><code>&#8211;display-source</code> X</p>
<dd> Only display tags from the source X (e.g. the Policy Manual or the Developer Reference). This option can be used multiple times to add additional sources. Example sources are &#8220;policy&#8221; or &#8220;devref&#8221; being the Policy Manual and the Developer Reference (respectively). </p>
<p> The entire list of sources can be found in <i></i>$LINTIAN_ROOT<i>/data/output/manual-references</i></p>
<dt><code>-E</code>, <code>&#8211;display-experimental</code>, <code>&#8211;no-display-experimental</code></p>
<dd> Control whether to display experimental (&#8220;X:&#8221;) tags. They are normally suppressed. </p>
<p> If a tag is marked experimental, this means that the code that generates this message is not as well tested as the rest of Lintian, and might still give surprising results. Feel free to ignore Experimental messages that do not seem to make sense, though of course bug reports are always welcome (particularly if they include fixes). </p>
<p> These options overrides the <code>display-experimental</code> variable in the configuration file.</p>
<dt><code>-i</code>, <code>&#8211;info</code></p>
<dd> Print explanatory information about each problem discovered in addition to the lintian error tags. To print a long tag description without running lintian, see <code><a href="/docs/linux/man/1-lintian-info/">lintian-info</a></code>(1). </p>
<p> This option overrides <code>info</code> variable in the configuration file.</p>
<dt><code>-I</code>, <code>&#8211;display-info</code></p>
<dd> Display informational (&#8220;I:&#8221;) tags as well. They are normally suppressed. (This is equivalent to <code>-L</code> &#8220;&gt;=info&#8221;). </p>
<p> This option overrides the <code>display-info</code> variable in the configuration file. </p>
<p> Note: <code>display-level</code> and <code>display-info</code> may not both appear in the configuration file.</p>
<dt><code>-L</code> [+|-|=][&gt;=|&gt;|=|&lt;|&lt;=][S|C|S/C], <code>&#8211;display-level</code> [+|-|=][&gt;=|&gt;|=|&lt;|&lt;=][S|C|S/C]</p>
<dd> Fine-grained selection of tags to be displayed. It is possible to add, remove or set the levels to display, specifying a visibility (error, warning, info, pedantic, or classification. The default settings are equivalent to <code>-L</code> &#8220;&gt;=warning&#8221;. </p>
<p> The value consists of 3 parts, where two of them are optional. The parts are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>modifier operator</p>
<dd> How to affect the current display level. Can be one of add to (&#8220;+&#8221;), remove from (&#8220;-&#8221;) or set to (&#8220;=&#8221;) the display level(s) denoted by the following selection. </p>
<p> The default value is &#8220;=&#8221; (i.e. set the display level).</p>
<dt>set operator</p>
<dd> The visibility to be selected. The operator can be one of &#8220;&gt;=&#8221;, &#8220;&gt;&#8221;, &#8220;=&#8221;, &#8220;&lt;&#8221; or &#8220;&lt;=&#8221;. As an example, this can be used to select all info (and more serious) tags via &#8220;&gt;=info&#8221;. </p>
<p> The default value is &#8220;=&#8221;, which means &#8220;exactly&#8221; the given visibility.</dl>
</dl>
<dl>
<dt>
<dd>
<p> This option overrides the <code>display-level</code> variable in the configuration file. The value of the <code>display-level</code> in configuration file should be space separated entries in the same format as passed via command-line. </p>
<p> Note: <code>display-level</code> may not be used with <code>display-info</code> or <code>pedantic</code> in the configuration file.</dl>
<dt><code>-o</code>, <code>&#8211;no-override</code></p>
<dd> Ignore all overrides provided by the package. This option will overrule <code>&#8211;show-overrides</code>. </p>
<p> This option overrides the <code>override</code> variable in the configuration file.</p>
<dt><code>&#8211;pedantic</code></p>
<dd> Display pedantic (&#8220;P:&#8221;) tags as well. They are normally suppressed. (This is equivalent to <code>-L</code> &#8220;+=pedantic&#8221;). </p>
<p> Pedantic tags are Lintian at its most pickiest and include checks for particular Debian packaging styles and checks that many people disagree with. Expect false positives and Lintian tags that you don&#8217;t consider useful if you use this option. Adding overrides for pedantic tags is probably not worth the effort. </p>
<p> This option overrides the <code>pedantic</code> variable in the configuration file. </p>
<p> Note: <code>pedantic</code> and <code>display-level</code> may not both appear in the configuration file.</p>
<dt><code>&#8211;profile</code> vendor[/prof]</p>
<dd> Use the profile from vendor (or the profile with that name). If the profile name does not contain a slash, the default profile for than vendor is chosen. </p>
<p> As an example, if you are on Ubuntu and want to use Lintian&#8217;s Debian checks, you can use: </p>
<pre>
  --profile debian
</pre>
<p> Likewise, on a Debian machine you can use this to request the Ubuntu checks. </p>
<p> If the token <i>{</i><font SIZE="-1"><i>VENDOR</i></font><i>}</i> appears in the profile name, <code>lintian</code> will substitute the token with a vendor name to find the profile. <code>lintian</code> uses Dpkg::Vendor to determine the best vendor to use (the closer to the current vendor, the better). This is mostly useful for people implementing their own checks on top of Lintian. </p>
<p> If not specified, the default value is <i>{</i><font SIZE="-1"><i>VENDOR</i></font><i>}/main</i>. </p>
<p> Please Refer to the Lintian User Manual for the full documentation of profiles.</p>
<dt><code>&#8211;show-overrides</code>, <code>&#8211;hide-overrides</code></p>
<dd> Controls whether tags that have been overridden should be shown. </p>
<p> The <code>&#8211;show-overrides</code> differs from <code>&#8211;no-overrides</code> in that shown overridden tags will still be marked as overridden (using an &#8220;O&#8221; code). </p>
<p> If the overridden tags are shown, the related override comments will also be displayed (unless &#8211;quiet is used). Please refer to the Lintian User Manual for the documentation on how lintian relates comments to a given override. </p>
<p> These options override the <code>show-overrides</code> variable in the configuration file.</p>
<dt><code>&#8211;suppress-tags</code> tag1,tag2,&#8230;</p>
<dd> Suppress the listed tags. They will not be reported if they occur and will not affect the exit status of Lintian. This option can be given multiple times and can be mixed with <code>&#8211;suppress-tags-from-file</code>. </p>
<p> This option can be used together with <code>&#8211;dont-check-part</code> (&#8220;Not those checks nor these tags&#8221;) and <code>&#8211;check-part</code> (&#8220;Only those checks, but not these tags (from those checks)&#8221;) to further reduce the selection of tags. </p>
<p> When used with <code>&#8211;tags</code>, this option is mostly ignored.</p>
<dt><code>&#8211;suppress-tags-from-file</code> file</p>
<dd> Suppress all tags listed in the given file. Blank lines and lines beginning with # are ignored. All other lines are taken to be tag names or comma-separated lists of tag names to suppress. The suppressed tags will not be reported if they occur and will not affect the exit status of Lintian. </p>
<p> Tags parsed from the file will be handled as if they had been given to the <code>&#8211;suppress-tags</code> option (e.g. ignored if <code>&#8211;tags</code> is used).</p>
<dt><code>&#8211;tag-display-limit</code>[=X]</p>
<dd> By default, lintian limits itself to emitting at most 4 instances of each tag per processable when <font SIZE="-1">STDOUT</font> is a <font SIZE="-1">TTY.</font> This option specified that limit. See also <code>&#8211;no-tag-display-limit</code>.</p>
<dt><code>&#8211;no-tag-display-limit</code></p>
<dd> By default, lintian limits itself to emitting at most 4 instances of each tag per processable when <font SIZE="-1">STDOUT</font> is a <font SIZE="-1">TTY.</font> This option disables that limit. </p>
<p> When <font SIZE="-1">STDOUT</font> is not a <font SIZE="-1">TTY,</font> lintian has no limit. See also <code>&#8211;tag-display-limit</code>.</dl>
<p> Configuration options:</p>
<dl>
<dt><code>&#8211;cfg</code> configfile</p>
<dd> Read the configuration from configfile rather than the default locations. This option overrides the <font SIZE="-1"><code>LINTIAN_CFG</code></font> environment variable.</p>
<dt><code>&#8211;no-cfg</code></p>
<dd> Do not read any configuration file. This option overrides the <code>&#8211;cfg</code> above.</p>
<dt><code>&#8211;ignore-lintian-env</code></p>
<dd> Ignore all environment variables starting with <i></i><font SIZE="-1"><i>LINTIAN_</i></font><i></i>. </p>
<p> This option is mostly useful for applications running <code>lintian</code> for checking packages and do not want the invoking user to affect the result (by setting <font SIZE="-1">LINTIAN_PROFILE</font> etc.). </p>
<p> Note it does <i>not</i> cause <code>lintian</code> to ignore the entire environment like <i></i><font SIZE="-1"><i>TMPDIR</i></font><i></i> or <i></i><font SIZE="-1"><i>DEB_VENDOR</i></font><i></i>. The latter can affect the default profile (or &#8220;{<font SIZE="-1">VENDOR</font>}&#8221; token for <code>&#8211;profile</code>). </p>
<p> Should usually be combined with <code>&#8211;no-user-dirs</code> (or unsetting <tt>$HOME</tt> and all <i></i><font SIZE="-1"><i>XDG_</i></font><i></i> variables).</p>
<dt><code>&#8211;include-dir</code> dir</p>
<dd> Use dir as an additional &#8220;<font SIZE="-1">LINTIAN_ROOT&#8221;.</font> The directory is expected have a similar layout to the <font SIZE="-1">LINTIAN_ROOT</font> (if it exists), but does not need to be a full self-contained root. </p>
<p> <code>lintian</code> will check this directory for (additional) profiles, data files, support libraries and checks. The latter two imply that Lintian may attempt to <i>load and execute code</i> from this directory. </p>
<p> This option may appear more than once; each time adding an additional directory. Directories are searched in the order they appear on the command line. </p>
<p> The additional directories will be checked <i>after</i> the user directories (though see <code>&#8211;no-user-dirs</code>) and <i>before</i> the core <font SIZE="-1">LINTIAN_ROOT.</font> </p>
<p> <code>Note</code>: This option should be the very first if given.</p>
<dt><code>-j</code> X, <code>&#8211;jobs</code>=X</p>
<dd> Set the limit for how many unpacking jobs Lintian will run in parallel. This option overrides the <code>jobs</code> variable in the configuration file. </p>
<p> By default Lintian will use <i>nproc</i> to determine a reasonable default (or 2, if the nproc fails).</p>
<dt><code>&#8211;user-dirs</code>, <code>&#8211;no-user-dirs</code></p>
<dd> By default, <code>lintian</code> will check <i></i>$HOME<i></i> and <i>/etc</i> for files supplied by the user or the local sysadmin (e.g. config files and profiles). This default can be disabled (and re-enabled) by using <code>&#8211;no-user-dirs</code> (and <code>&#8211;user-dirs</code>, respectively). </p>
<p> These options will <i>not</i> affect the inclusion of <font SIZE="-1">LINTIAN_ROOT,</font> which is always included. </p>
<p> These option can appear multiple times, in which case the last of them to appear determines the result. </p>
<p> Note that if the intention is only to disable the user&#8217;s <i></i>$HOME<i></i>, then unsetting <i></i>$HOME<i></i> and <i>XDG_*_HOME</i> may suffice. Alternatively, <i>/etc</i> can be &#8220;re-added&#8221; by using <i>&#8211;include-dir</i> (caveat: <i>/etc/lintianrc</i> will be ignored by this). </p>
<p> If the intention is to avoid (unintentional) side-effects from the calling user, then this option could be combined with <code>&#8211;ignore-lintian-env</code>. </p>
<p> If for some reason <code>&#8211;no-user-dirs</code> cannot be used, then consider unsetting <i></i>$HOME<i></i> and all the <i></i>$XDG_<i>*</i> variables (not just the <i></i>$XDG_<i>*_HOME</i> ones). </p>
<p> <code>Note</code>: This option should be the very first if given.</dl>
<p> Developer/Special usage options:</p>
<dl>
<dt><code>&#8211;allow-root</code></p>
<dd> Override lintian&#8217;s warning when it is run with superuser privileges.</p>
<dt><code>&#8211;keep-lab</code></p>
<dd> By default, temporary labs will be removed after lintian is finished. Specifying this options will leave the lab behind, which might be useful for debugging purposes. You can find out where the temporary lab is located by running lintian with the <code>&#8211;verbose</code> option.</p>
<dt><code>&#8211;packages-from-file</code> X</p>
<dd> The line is read as the path to a file to process (all whitespace is included!). </p>
<p> If X is &#8220;-&#8221;, Lintian will read the packages from <font SIZE="-1">STDIN.</font></p>
<dt><code>&#8211;perf-debug</code></p>
<dd> Enable performance related debug logging. </p>
<p> The data logged and the format used is subject to change with every release. </p>
<p> Note that some of the information may also be available (possibly in a different format) with the <code>&#8211;debug</code> option.</p>
<dt><code>&#8211;perf-output</code> <font SIZE="-1">OUTPUT</font></p>
<dd> Write performance related debug information to the specified file or file descriptor. If <font SIZE="-1">OUTPUT</font> starts with a &#8216;&amp;&#8217; or &#8216;+&#8217;, Lintian will handle <font SIZE="-1">OUTPUT</font> specially. Otherwise, Lintian will open the file denoted by <font SIZE="-1">OUTPUT</font> for writing (truncating if it exists, creating it if it does not exist). </p>
<p> If the first character of <font SIZE="-1">OUTPUT</font> is a &amp; and the rest of argument is a number N, then lintian attempts to write it to the file descriptor with the number N. Said file descriptor must be open for writing. E.g <i>&amp;2</i> makes Lintian write the performance logging to <font SIZE="-1">STDERR.</font> </p>
<p> If the first character of <font SIZE="-1">OUTPUT</font> is a +, Lintian will append to the file rather than truncating it. In this case, the file name is <font SIZE="-1">OUTPUT</font> with initial &#8220;+&#8221; character removed. E.g. <i>+my-file</i> makes Lintian append to <i>my-file</i> </p>
<p> If Lintian should write the output to a file starting with a literal &#8216;&amp;&#8217; or &#8216;+&#8217;, then simply prefix it with &#8220;./&#8221; (e.g. &#8220;+my-file&#8221; becomes &#8220;./+my-file&#8221;). </p>
<p> If this option omitted, Lintian will default to using <font SIZE="-1">STDOUT.</font></p>
<dt><code>-U</code> info1,info2,&#8230;, <code>&#8211;unpack-info</code> info1,info2,&#8230;</p>
<dd> Collect information info1, info2, etc. even if these are not required by the checks. Collections requested by this option are also not auto-removed (in this run). </p>
<p> This option is mostly useful for debugging or special purpose setups. </p>
<p> It is allowed to give this option more than once. The following two lines of arguments are semantically equivalent: </p>
<pre>
 -U info1 -U info2
 -U info1,info2
</pre>
</dl>
<h2>CHECKS</h2>
<h2>COLLECTION</h2>
<p> <tt>@COLLECTION</tt>@</p>
<h2>FILES</h2>
<p> Lintian looks for its configuration file in the following locations:</p>
<dl>
<dt>&bull;</p>
<dd> The argument given to <code>&#8211;cfg</code></p>
<dt>&bull;</p>
<dd> <i></i>$LINTIAN_CFG<i></i></p>
<dt>&bull;</p>
<dd> <i></i>$XDG_CONFIG_HOME<i>/lintian/lintianrc</i></p>
<dt>&bull;</p>
<dd> <i></i>$HOME<i>/.lintianrc</i> </p>
<p> Deprecated in Lintian/2.5.12 and newer (use the <font SIZE="-1">XDG</font> based variant above)</p>
<dt>&bull;</p>
<dd> <i>XGD_DIR/lintian/lintianrc</i> </p>
<p> Where <font SIZE="-1">XGD_DIR</font> is a directories listed in <i></i>$XDG_CONFIG_DIRS<i></i> (or <i>/etc/xdg</i> if <i></i>$XDG_CONFIG_DIRS<i></i> is unset).</p>
<dt>&bull;</p>
<dd> <i>/etc/lintianrc</i> </p>
<p> Deprecated in Lintian/2.5.12 and newer (use the <font SIZE="-1">XDG</font> based variant above)</dl>
<p> Lintian uses the following directories:</p>
<dl>
<dt><i>/tmp</i></p>
<dd> Lintian defaults to creating a temporary lab directory in <i>/tmp</i>. To change the directory used, set the <font SIZE="-1">TMPDIR</font> environment variable to a suitable directory. <font SIZE="-1">TMPDIR</font> can be set in the configuration file.</p>
<dt><i>/usr/share/lintian/checks</i></p>
<dd> Scripts that check aspects of a package.</p>
<dt><i>/usr/share/lintian/collection</i></p>
<dd> Scripts that collect information about a package and store it for use by the check scripts.</p>
<dt><i>/usr/share/lintian/data</i></p>
<dd> Supporting data used by Lintian checks and for output formatting.</p>
<dt><i>/usr/share/lintian/lib</i></p>
<dd> Utility scripts used by the other lintian scripts.</dl>
<p> For binary packages, Lintian looks for overrides in a file named <i>usr/share/lintian/overrides/&lt;package&gt;</i> inside the binary package, where <i>&lt;package&gt;</i> is the name of the binary package. For source packages, Lintian looks for overrides in <i>debian/source/lintian-overrides</i> and then in <i>debian/source.lintian-overrides</i> if the first file is not found. The first path is preferred. See the Lintian User&#8217;s Manual for the syntax of overrides.</p>
<h2>CONFIGURATION FILE</h2>
<p> The configuration file can be used to specify default values for some options. The general format is: </p>
<pre>
 option = value
</pre>
<p> All whitespace adjacent to the &#8220;=&#8221; sign as well as leading and trailing whitespace is ignored. However whitespace within the value is respected, as demonstrated by this example: </p>
<pre>
 # Parsed as &quot;opt1&quot; with value &quot;val1&quot;
    opt1    =   val1
 # Parsed as &quot;opt2&quot; with value &quot;val2.1  val2.2     val2.3&quot;
 opt2 = val2.1  val2.2     val2.3
</pre>
<p> Unless otherwise specified, no option may appear more than once. Lintian will ignore empty lines or lines starting with the <code>#</code>-character. </p>
<p> Generally options will be the long form of the command-line option without the leading dashes. There some exceptions (such as &#8211;profile), where Lintian uses the same name as the environment variable. </p>
<p> Lintian only allows a subset of the options specified in the configuration file; please refer to the individual options in &#8220;<font SIZE="-1">OPTIONS&#8221;</font>. </p>
<p> In the configuration file, all options listed must have a value, even if they do not accept a value on command line (e.g. &#8211;pedantic). The values &#8220;yes&#8221;, &#8220;y&#8221;, &#8220;1&#8221;, or &#8220;true&#8221; will enable such an option and &#8220;no&#8221;, &#8220;n&#8221;, &#8220;0&#8221; or &#8220;false&#8221; will disable it. Prior to the 2.5.2 release, these values were case sensitive. </p>
<p> For other options, they generally take the same values as they do on the command line. Though some options allow a slightly different format (e.g. &#8211;display-level). These exceptions are explained for the relevant options in &#8220;<font SIZE="-1">OPTIONS&#8221;</font>. </p>
<p> Beyond command line options, it is also allowed to specify the environment variable &#8220;<font SIZE="-1">TMPDIR&#8221;</font> in the configuration file. </p>
<p> A sample configuration file could look like: </p>
<pre><code>
#Sample configuration file for lintian
#
#Set the default profile(--profile)
LINTIAN_PROFILE = debian
#Set the default TMPDIR for lintian to / var / tmp / lintian
#- useful if / tmp is tmpfs with "limited" size.
    TMPDIR = / var / tmp / lintian /
#Show info(I:) tags by default(--display - info)
#NB : this cannot be used with display - level
                 display -
             info = yes
#Ignore all overrides(--no - override)
#NB : called "override" in the config file
#and has inverted value !
                 override = no
#Automatically determine if color should be used
                     color = auto
</code></pre>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></p>
<dd> No policy violations or major errors detected. (There may have been warnings, though.)</p>
<dt><code>1</code></p>
<dd> Policy violations or major errors detected.</p>
<dt><code>2</code></p>
<dd> Lintian run-time error. An error message is sent to stderr.</dl>
<h2>CHECKING LAST BUILD</h2>
<p> When run in an unpacked package dir (with no package selection arguments), Lintian will use <i>debian/changelog</i> to determine the source and version of the package. Lintian will then attempt to find a matching <i>.changes</i> file for this source and version combination. </p>
<p> Lintian will (in order) search the following directories:</p>
<dl>
<dt>..</p>
<dd> Used by <code><a href="/docs/linux/man/1-dpkg-buildpackage/">dpkg-buildpackage</a></code>(1).</p>
<dt>../build-area</p>
<dd> Used by <code><a href="/docs/linux/man/1-svn-buildpackage/">svn-buildpackage</a></code>(1).</p>
<dt>/var/cache/pbuilder/result</p>
<dd> Used by <code><a href="/docs/linux/man/1-pbuilder/">pbuilder</a></code>(1) and <code><a href="/docs/linux/man/1-cowbuilder/">cowbuilder</a></code>(1).</dl>
<p> In each directory, Lintian will attempt to find a <i>.changes</i> file using the following values as architecture (in order):</p>
<dl>
<dt><i></i>$DEB_BUILD_ARCH<i></i> (or <i>dpkg &#8211;print-architecture</i>)</p>
<dd> The environment variable <font SIZE="-1">DEB_BUILD_ARCH</font> (if not set, &#8220;dpkg &#8211;print-architecture&#8221; will be used instead)</p>
<dt><i></i>$DEB_HOST_ARCH<i></i></p>
<dd> The environment variable <font SIZE="-1">DEB_HOST_ARCH.</font></p>
<dt><i>dpkg &#8211;print-foreign-architectures</i></p>
<dd> If <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1) appears to support multi-arch, then any architecture listed by &#8220;dpkg &#8211;print-foreign-architectures&#8221; will be used (in the order returned by dpkg).</p>
<dt><i>multi</i></p>
<dd> Pseudo architecture used by <code><a href="/docs/linux/man/1-mergechanges/">mergechanges</a></code>(1).</p>
<dt><i>all</i></p>
<dd> Used when building architecture indep packages only (e.g. dpkg-buildpackage -A).</p>
<dt><i>source</i></p>
<dd> Used for &#8220;source only&#8221; builds (e.g. dpkg-buildpackage -S).</dl>
<p> If a <i>.changes</i> file matches any combination above exists, Lintian will process the first match as if you had passed it per command line. If no <i>.changes</i> file can be found, Lintian will print a list of attempted locations on <font SIZE="-1">STDERR</font> and exit 0.</p>
<h2>EXAMPLES</h2>
<dl>
<dt><code>$ lintian foo.changes</code></p>
<dd> Check the changes file itself and any (binary, udeb or source) package listed in it.</p>
<dt><code>$ lintian foo.deb</code></p>
<dd> Check binary package foo given by foo.deb.</p>
<dt><code>$ lintian foo.dsc</code></p>
<dd> Check source package foo given by foo.dsc.</p>
<dt><code>$ lintian foo.dsc -L +info</code></p>
<dd> Check source package foo given by foo.dsc, including info tags.</p>
<dt><code>$ lintian -i foo.changes</code></p>
<dd> Check the changes file and, if listed, the source and binary package of the upload. The output will contain detailed information about the reported tags.</p>
<dt><code>$ lintian</code></p>
<dd> Assuming <i>debian/changelog</i> exists, look for a changes file for the source in the parent dir. Otherwise, print usage information and exit.</dl>
<h2>BUGS</h2>
<p> Lintian does not have any locking mechanisms yet. (Running several Lintian processes on the same laboratory simultaneously is likely to fail or corrupt the laboratory.) </p>
<p> If you discover any other bugs in lintian, please contact the authors.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-lintian-info/">lintian-info</a></code>(1), Lintian User Manual (/usr/share/doc/lintian/lintian.html) </p>
<p> Packaging tools: <code><a href="/docs/linux/man/7-debhelper/">debhelper</a></code>(7), <code><a href="/docs/linux/man/8-dh_make/">dh_make</a></code>(8), <code><a href="/docs/linux/man/1-dpkg-buildpackage/">dpkg-buildpackage</a></code>(1).</p>
<h2>AUTHORS</h2>
<p> Niels Thykier &lt;niels [at] thykier.net&gt; </p>
<p> Richard Braakman &lt;dark [at] xs4all.nl&gt; </p>
<p> Christian Schwarz &lt;schwarz [at] monet.m.isar.de&gt; </p>
<p> Please use the email address &lt;lintian-maint [at] debian.org&gt; for Lintian related comments. </p>
<h2>Index</h2>
