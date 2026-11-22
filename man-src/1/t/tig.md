---

title: "tig(1)"
name: "tig"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tig/"
description: "tig – text-mode interface for Git"
---

<p> tig &#8211; text-mode interface for Git </p>
<h2>SYNOPSIS</h2>
<pre><code>
tig[options][revisions][--][paths] tig log[options][revisions][--][paths] tig show[options][revisions][--][paths] tig reflog[options][revisions] tig blame[options][rev][--] path
        tig grep[options][pattern] tig refs[options] tig stash
            tig status
                tig &lt; [Git command output]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Tig is an ncurses-based text-mode interface for <a href="/docs/linux/man/1-git/">git</a>(1). It functions mainly as a Git repository browser, but can also assist in staging changes for commit at chunk level and act as a pager for output from various Git commands.</p>
<h2>OPTIONS</h2>
<p> Command line options recognized by Tig include all valid <a href="/docs/linux/man/1-git-log/">git-log</a>(1) and <a href="/docs/linux/man/1-git-diff/">git-diff</a>(1) options, as well as the following subcommands and Tig-specific options. The first command line parameter not starting with &quot;-&quot; is interpreted as being either a revision specification or a path and will end the option parsing. All additional options will be passed to the underlying Git command. </p>
<p> show</p>
<dl>
<dt>
</dt><dd> Open diff view using the given <a href="/docs/linux/man/1-git-show/">git-show</a>(1) options.</dd></dl>
<p> blame</p>
<dl>
<dt>
</dt><dd> Show given file annotated by commits. Takes zero or more <a href="/docs/linux/man/1-git-blame/">git-blame</a>(1) options. Optionally limited from given revision.</dd></dl>
<p> status</p>
<dl>
<dt>
</dt><dd> Start up in status view.</dd></dl>
<p> log</p>
<dl>
<dt>
</dt><dd> Start up in log view, displaying <a href="/docs/linux/man/1-git-log/">git-log</a>(1) output.</dd></dl>
<p> reflog</p>
<dl>
<dt>
</dt><dd> Start up in reflog view.</dd></dl>
<p> refs</p>
<dl>
<dt>
</dt><dd> Start up in refs view.</dd></dl>
<p> stash</p>
<dl>
<dt>
</dt><dd> Start up in stash view.</dd></dl>
<p> grep</p>
<dl>
<dt>
</dt><dd> Open the grep view. Supports the same options as <a href="/docs/linux/man/1-git-grep/">git-grep</a>(1).</dd></dl>
<p> +&lt;number&gt;</p>
<dl>
<dt>
</dt><dd> Show the first view with line &lt;number&gt; visible and selected.</dd></dl>
<p> -v, &#8211;version</p>
<dl>
<dt>
</dt><dd> Show version and exit.</dd></dl>
<p> -h, &#8211;help</p>
<dl>
<dt>
</dt><dd> Show help message and exit.</dd></dl>
<p> -C&lt;path&gt;</p>
<dl>
<dt>
</dt><dd> Run as if Tig was started in &lt;path&gt; instead of the current working directory.</dd></dl>
<h2>PAGER MODE</h2>
<p> Tig enters pager mode when input is provided via stdin and supports the following subcommands and options: </p>
<dl>
<dt>
</dt><dd> &bull; When the <i>show</i> subcommand is specified and the <i>&#8211;stdin</i> option is given, stdin is assumed to be a list of commit IDs and will be forwarded to the diff view&#8217;s underlying <a href="/docs/linux/man/1-git-show/">git-show</a>(1) command. For example:</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
$ git rev-list --author=vivien HEAD | tig show --stdin
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd> &bull; When <i>&#8211;stdin</i> is given, stdin is assumed to be a list of commit IDs and will be forwarded to the main view&#8217;s underlying <a href="/docs/linux/man/1-git-log/">git-log</a>(1) command. For example:</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
$ tig --no-walk --stdin &lt; cherry-picks.txt
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd> &bull; When <i>&#8211;pretty=raw</i> is given, stdin is assumed to be a &quot;pretty=raw&quot; formatted output similar to that of <a href="/docs/linux/man/1-git-log/">git-log</a>(1). For example:</dd></dl>
<dl>
<dt>
</dt><dd>
<pre>
$ git reflog --pretty=raw | tig --pretty=raw
</pre>
</dd></dl>
<p> When no subcommands nor options are given, the pager view will be used for displaying the Git command input given on stdin. The pager view assumes the input is either from <a href="/docs/linux/man/1-git-log/">git-log</a>(1) or <a href="/docs/linux/man/1-git-diff/">git-diff</a>(1) and will highlight it similar to the log and diff views. For example: </p>
<dl>
<dt>
</dt><dd>
<pre>
$ git log -Schange -p --raw | tig
</pre>
</dd></dl>
<h2>EXAMPLES</h2>
<p> Display the list of commits for the current branch: </p>
<dl>
<dt>
</dt><dd>
<pre>
$ tig
</pre>
</dd></dl>
<p> Display commits from one or more branches: </p>
<dl>
<dt>
</dt><dd>
<pre>
$ tig test master
</pre>
</dd></dl>
<p> Pretend as if all the refs in refs/ are listed on the command line: </p>
<dl>
<dt>
</dt><dd>
<pre>
$ tig --all
</pre>
</dd></dl>
<p> Display differences between two branches: </p>
<dl>
<dt>
</dt><dd>
<pre>
$ tig test..master
</pre>
</dd></dl>
<p> Display changes for sub-module versions: </p>
<dl>
<dt>
</dt><dd>
<pre>
$ tig --submodule
</pre>
</dd></dl>
<p> Display changes for a single file: </p>
<dl>
<dt>
</dt><dd>
<pre>
$ tig -- README
</pre>
</dd></dl>
<p> Display contents of the README file in a specific revision: </p>
<dl>
<dt>
</dt><dd>
<pre>
$ tig show tig-0.8:README
</pre>
</dd></dl>
<p> Display revisions between two dates for a specific file: </p>
<dl>
<dt>
</dt><dd>
<pre>
$ tig --after=&quot;2004-01-01&quot; --before=&quot;2006-05-16&quot; -- README
</pre>
</dd></dl>
<p> Blame file with copy detection enabled: </p>
<dl>
<dt>
</dt><dd>
<pre>
$ tig blame -C README
</pre>
</dd></dl>
<p> Display the list of stashes: </p>
<dl>
<dt>
</dt><dd>
<pre>
$ tig stash
</pre>
</dd></dl>
<p> Grep all files for lines containing DEFINE_ENUM: </p>
<dl>
<dt>
</dt><dd>
<pre>
$ tig grep -p DEFINE_ENUM
</pre>
</dd></dl>
<p> Show references (branches, remotes and tags): </p>
<dl>
<dt>
</dt><dd>
<pre>
$ tig refs
</pre>
</dd></dl>
<p> Use word diff in the diff view: </p>
<dl>
<dt>
</dt><dd>
<pre>
$ tig --word-diff=plain
</pre>
</dd></dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> In addition to environment variables used by Git (e.g. GIT_DIR), Tig defines the ones below. The command related environment variables have access to the internal state of Tig via replacement variables, such as %(commit) and %(blob). See <code><a href="/docs/linux/man/5-tigrc/">tigrc</a></code>(5) for a full list. </p>
<p> TIGRC_USER</p>
<dl>
<dt>
</dt><dd> Path of the user configuration file (defaults to ~/.tigrc or $XDG_CONFIG_HOME/tig/config).</dd></dl>
<p> TIGRC_SYSTEM</p>
<dl>
<dt>
</dt><dd> Path of the system wide configuration file (defaults to {sysconfdir}/tigrc). Define to empty string to use built-in configuration.</dd></dl>
<p> TIG_LS_REMOTE</p>
<dl>
<dt>
</dt><dd> Command for retrieving all repository references. The command should output data in the same format as <a href="/docs/linux/man/1-git-ls-remote/">git-ls-remote</a>(1).</dd></dl>
<p> TIG_DIFF_OPTS</p>
<dl>
<dt>
</dt><dd> The diff options to use in the diff view. The diff view uses <a href="/docs/linux/man/1-git-show/">git-show</a>(1) for formatting and always passes &#8211;patch-with-stat. You may also set the diff-options setting in the configuration file.</dd></dl>
<p> TIG_TRACE</p>
<dl>
<dt>
</dt><dd> Path for trace file where information about Git commands are logged.</dd></dl>
<p> TIG_SCRIPT</p>
<dl>
<dt>
</dt><dd> Path to script that should be executed automatically on startup. If this environment variable is defined to the empty string, the script is read from stdin. The script is interpreted line-by-line and can contain prompt commands and key mappings.</dd></dl>
<p> TIG_NO_DISPLAY</p>
<dl>
<dt>
</dt><dd> Open Tig without rendering anything to the terminal. This force Ncurses to write to /dev/null. The main use is for automated testing of Tig.</dd></dl>
<h2>FILES</h2>
<p> <i>$XDG_CONFIG_HOME/tig/config</i>, <i>~/.config/tig/config</i>, <i>~/.tigrc</i></p>
<dl>
<dt>
</dt><dd> The Tig user configuration file is loaded in the following way. If $XDG_CONFIG_HOME is set, read user configuration from $XDG_CONFIG_HOME/tig/config. If $XDG_CONFIG_HOME is empty or undefined, read user configuration from ~/.config/tig/config if it exists and fall back to ~/.tigrc if it does not exist. See <code><a href="/docs/linux/man/5-tigrc/">tigrc</a></code>(5) for examples.</dd></dl>
<p> <i>/etc/tigrc</i></p>
<dl>
<dt>
</dt><dd> System wide configuration file.</dd></dl>
<p> <i>$GIT_DIR/config</i>, <i>~/.gitconfig</i>, <i>/etc/gitconfig</i></p>
<dl>
<dt>
</dt><dd> Git configuration files. Read on start-up with the help of <a href="/docs/linux/man/1-git-config/">git-config</a>(1).</dd></dl>
<p> <i>$XDG_DATA_HOME/tig/history</i>, <i>~/.local/share/tig/history</i>, <i>~/.tig_history</i></p>
<dl>
<dt>
</dt><dd> When compiled with readline support, Tig writes a persistent command and search history. The location of the history file is determined in the following way. If $XDG_DATA_HOME is set and $XDG_DATA_HOME/tig/ exists, store history to $XDG_DATA_HOME/tig/history. If $XDG_DATA_HOME is empty or undefined, store history to ~/.local/share/tig/history if the directory ~/.local/share/tig/ exists, and fall back to ~/.tig_history if it does not exist.</dd></dl>
<h2>BUGS</h2>
<p> Please visit Tig&#8217;s m[blue]<code>home page</code>m[][1] or m[blue]<code>main Git repository</code>m[][2] for information about new releases and how to report bugs or feature request.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2006-2014 Jonas Fonseca &lt;m[blue]<code>jonas.fonseca [at] gmail.com</code>m[][3]&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-tigrc/">tigrc</a></code>(5), <code><a href="/docs/linux/man/7-tigmanual/">tigmanual</a></code>(7), git(7)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</dt>
<dd> home page</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="https://jonas.github.io/tig">https://jonas.github.io/tig</a></dd></dl>
<dt> 2.</dt>
<dd> main Git repository</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="https://github.com/jonas/tig">https://github.com/jonas/tig</a></dd></dl>
<dt> 3.</dt>
<dd> jonas.fonseca [at] gmail.com</dd>
<dl>
<dt>
</dt><dd> mailto:jonas.fonseca [at] gmail.com</dd></dl>
</dl>
