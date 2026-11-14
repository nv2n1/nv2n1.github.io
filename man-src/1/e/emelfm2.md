---
title: "emelfm2(1)"
name: "emelfm2"
section: "1"
letter: "e"
url: "/docs/linux/man/1-emelfm2/"
description: "emelFM2 – a GTK+2 file manager"
---

<h2>NAME</h2>
<p> emelFM2 &#8211; a GTK+2 file manager</p>
<h2>SYNOPSIS</h2>
<p> <code>emelfm2</code> [<i>OPTION</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> emelFM2 is a file manager for UNIX-like operating systems. It uses a simple and efficient interface pioneered by Norton Commander in the 1980&#8217;s. The main window is divided into three &quot;panes&quot; or &quot;panels&quot;. Two of them show information about the contents of selected filesystem directories. That information is presented as text. The third pane shows the output of commands executed within the program. </p>
<p> A built-in command-line, toolbar buttons or assigned keys can be used to initiate commands. A flexible filetyping mechanism provides user-determined actions for desired filetypes.</p>
<h2>COMMAND LINE OPTIONS</h2>
<dl>
<dt><code>-1</code>,<code>&#8211;one</code>=<i> DIR</i></p>
<dd> At session-start, show DIR in the first filelist pane.</p>
<dt><code>-2</code>,<code>&#8211;two</code>=<i> DIR</i></p>
<dd> At session-start, show DIR in the second filelist pane.</p>
<dt><code>-c</code>,<code>&#8211;config</code>=<i> DIR</i></p>
<dd> Set the configuration-data directory to DIR (default: ~/.config/emelfm2).</p>
<dt><code>-e</code>,<code>&#8211;encoding</code>=<i> TYPE</i></p>
<dd> Set the filesystem character encoding to TYPE.</p>
<dt><code>-f</code>,<code>&#8211;fallback-encoding=</code><i> TYPE</i></p>
<dd> Set the fallback encoding to TYPE (default: ISO-8859-1).</p>
<dt><code>-i</code>,<code>&#8211;ignore-problems</code></p>
<dd> Ignore the encoding/locale problems (use at your own risk!).</p>
<dt><code>-l</code>,<code>&#8211;log-all</code></p>
<dd> Maximise GTK+2 error logging.</p>
<dt><code>-m</code>,<code>&#8211;daemon</code></p>
<dd> Detach the emelFM2 session from its controlling terminal. Will not work when emelFM2 is compiled with debug support.</p>
<dt><code>-r</code>,<code>&#8211;run-at</code>-start=<i> COMMAND</i></p>
<dd> Run COMMAND immediately after session start.</p>
<dt><code>-s</code>,<code>&#8211;set-option OPTION_NAME=string-value</code></p>
<dd> Set one-line config option. &quot;OPTION_NAME=string-value&quot; is a string in the format used in the config file.</p>
<dt><code>-t</code>,<code>&#8211;trash</code>=<i> DIR</i></p>
<dd> Set the trash directory to DIR (default: ~/.local/share/Trash/files).</dl>
<p> Help options:</p>
<dl>
<dt><code>-h</code>,<code>&#8211;help</code></p>
<dd> Display a brief help message.</p>
<dt><code>-u</code>,<code>&#8211;usage</code></p>
<dd> Display a brief usage message.</p>
<dt><code>-v</code>,<code>&#8211;version</code></p>
<dd> Display the version and build information. </p>
</dl>
<p> These only work when emelFM2 is compiled with debug support:</p>
<dl>
<dt><code>-d</code>,<code>&#8211;debug</code>=<i> N</i></p>
<dd> Set the debug level. N = digit from 1 (lowest) to 5 (highest). Default is 5.</p>
<dt><code>-x</code>,<code>&#8211;verbose</code></p>
<dd> Display time and location information in debug messages. Only works when emelFM2 is compiled with debug support. </p>
</dl>
<h2>FILES AND DIRECTORIES</h2>
<dl>
<dt><i>[PREFIX]/bin</i></p>
<dd> Location for the emelFM2 binary. Default PREFIX is /usr/local, which may be modified at compilation time.</p>
<dt><i>[PREFIX]/lib/emelfm2/plugins</i></p>
<dd> Default location for emelFM2 plugin files, named like e2p*.so.</p>
<dt><i>[PREFIX]/share/doc/emelfm2</i></p>
<dd> Default documentation files&#8217; location.</p>
<dt><i>[PREFIX]/share/pixmaps/emelfm2</i></p>
<dd> Default location of application-specific icon files.</p>
<dt><i>~/.config/emelfm2</i></p>
<dd> Default location for configuration files, named &quot;config&quot; and &quot;cache&quot;.</p>
<dt><i>~/.local/share/Trash/files</i></p>
<dd> Default trash directory. </p>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> These are directly used:</p>
<dl>
<dt><i>G_BROKEN_FILENAMES, G_FILENAME_ENCODING, HOSTNAME, LC_ALL, LC_MESSAGES, LANGUAGE or LANG, PATH</i></p>
<dd></dl>
<h2>SUGGESTIONS AND BUG REPORTS</h2>
<p> Please send bug reports, comments or feature requests to the mailing list &lt;emelfm2 [at] freelists.org&gt;. You do not need to be a subscriber.<br />
 For known bugs refer to <a rel="nofollow" href="http://emelfm2.net/TODO.">http://emelfm2.net/TODO.</a> </p>
<h2>CREDITS</h2>
<p> The original emelFM was essentially a compilation of some of the features that Michael Clark found most useful in other file managers. The current maintainer of emelFM2 is tooar. For a complete list of contributors please refer to [PREFIX]/share/doc/emelfm2/CREDITS. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2003-2009, tooar &lt;tooar [at] emelfm2.net&gt;.<br />
 This program is licensed under the terms of the FSF General Public License and comes with ABSOLUTELY NO WARRANTY. </p>
<h2>SEE ALSO</h2>
<p> emelFM2 <a rel="nofollow" href="http://emelfm2.net">http://emelfm2.net</a><br />
 User Guide <a rel="nofollow" href="http://emelfm2.net/UserGuide">http://emelfm2.net/UserGuide</a><br />
 updated emelFM <a rel="nofollow" href="http://www.havens.de/elm/emelfm.html">http://www.havens.de/elm/emelfm.html</a><br />
 old emelFM <a rel="nofollow" href="http://www.pitt.edu/~macst92/emelFM/">http://www.pitt.edu/~macst92/emelFM/</a> or </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="http://emelFM.sourceforge.net/">http://emelFM.sourceforge.net/</a> </p>
<h2>Index</h2>
