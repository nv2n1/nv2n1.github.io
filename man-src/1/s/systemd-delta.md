---
title: "systemd-delta(1)"
name: "systemd-delta"
section: "1"
letter: "s"
url: "/docs/linux/man/1-systemd-delta/"
description: "systemd-delta – Find overridden configuration files"
---

<h2 class="name">NAME</h2>
<p> systemd-delta &#8211; Find overridden configuration files </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>systemd-delta</code> [OPTIONS&#8230;] [<i>PREFIX</i>[/<i>SUFFIX</i>]|<i>SUFFIX</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>systemd-delta</code></p>
<dd>may be used to identify and compare configuration files that override other configuration files. Files in /etc/ have highest priority, files in /run/ have the second highest priority, &#8230;, files in /usr/lib/ have lowest priority. Files in a directory with higher priority override files with the same name in directories of lower priority. In addition, certain configuration files can have &quot;.d&quot; directories which contain &quot;drop-in&quot; files with configuration snippets which augment the main configuration file. &quot;Drop-in&quot; files can be overridden in the same way by placing files with the same name in a directory of higher priority (except that, in case of &quot;drop-in&quot; files, both the &quot;drop-in&quot; file name and the name of the containing directory, which corresponds to the name of the main configuration file, must match). For a fuller explanation, see <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5). </p>
<p> The command line argument will be split into a prefix and a suffix. Either is optional. The prefix must be one of the directories containing configuration files (/etc/, /run/, /lib/, &#8230;). If it is given, only overriding files contained in this directory will be shown. Otherwise, all overriding files will be shown. The suffix must be a name of a subdirectory containing configuration files like tmpfiles.d, sysctl.d or systemd/system. If it is given, only configuration files in this subdirectory (across all configuration paths) will be analyzed. Otherwise, all configuration files will be analyzed. If the command line argument is not given at all, all configuration files will be analyzed. See below for some examples.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>-t</code>, <code>&#8211;type=</code></p>
<dl>
<dt>
<dd> When listing the differences, only list those that are asked for. The list itself is a comma-separated list of desired difference types. </p>
<p> Recognized types are: </p>
<p> <i>masked</i></p>
<dl>
<dt>
<dd> Show masked files</dl>
<p> <i>equivalent</i></p>
<dl>
<dt>
<dd> Show overridden files that while overridden, do not differ in content.</dl>
<p> <i>redirected</i></p>
<dl>
<dt>
<dd> Show files that are redirected to another.</dl>
<p> <i>overridden</i></p>
<dl>
<dt>
<dd> Show overridden, and changed files.</dl>
<p> <i>extended</i></p>
<dl>
<dt>
<dd> Show *.conf files in drop-in directories for units.</dl>
<p> <i>unchanged</i></p>
<dl>
<dt>
<dd> Show unmodified files too.</dl>
</dl>
<p> <code>&#8211;diff=</code></p>
<dl>
<dt>
<dd> When showing modified files, when a file is overridden show a diff as well. This option takes a boolean argument. If omitted, it defaults to <code>true</code>.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print a short version string and exit.</dl>
<p> <code>&#8211;no-pager</code></p>
<dl>
<dt>
<dd> Do not pipe output into a pager.</dl>
<h2>EXAMPLES</h2>
<p> To see all local configuration: </p>
<dl>
<dt>
<dd>
<pre>
systemd-delta
</pre>
</dl>
<p> To see all runtime configuration: </p>
<dl>
<dt>
<dd>
<pre>
systemd-delta /run
</pre>
</dl>
<p> To see all system unit configuration changes: </p>
<dl>
<dt>
<dd>
<pre>
systemd-delta systemd/system
</pre>
</dl>
<p> To see all runtime &quot;drop-in&quot; changes for system units: </p>
<dl>
<dt>
<dd>
<pre>
systemd-delta --type=extended /run/systemd/system
</pre>
</dl>
<h2>EXIT STATUS</h2>
<p> On success, 0 is returned, a non-zero failure code otherwise.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) </p>
<h2>Index</h2>
