---
title: "systemd-tmpfiles-setup(8)"
name: "systemd-tmpfiles-setup"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-tmpfiles-setup/"
description: "systemd-tmpfiles, systemd-tmpfiles-setup.service, systemd-tmpfiles-setup-dev.service, systemd-tmpfiles-clean.service, systemd-tmpfiles-clean.timer – Creates, deletes and cleans up volatile and temp..."
---

<p>systemd-tmpfiles, systemd-tmpfiles-setup.service, systemd-tmpfiles-setup-dev.service, systemd-tmpfiles-clean.service, systemd-tmpfiles-clean.timer &#8211; Creates, deletes and cleans up volatile and temporary files and directories</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>systemd-tmpfiles</code> [OPTIONS&#8230;] [<i>CONFIGFILE</i>&#8230;]</dl>
<dd>systemd-tmpfiles-setup.service </p>
<p> systemd-tmpfiles-setup-dev.service </p>
<p> systemd-tmpfiles-clean.service </p>
<p> systemd-tmpfiles-clean.timer</p>
<h2>Description</h2>
<p><code>systemd-tmpfiles</code> creates, deletes, and cleans up volatile and temporary files and directories, based on the configuration file format and location specified in <code><a href="/docs/linux/man/5-tmpfiles-d/">tmpfiles.d</a></code>(5). </p>
<p> If invoked with no arguments, it applies all directives from all configuration files. If one or more filenames are passed on the command line, only the directives in these files are applied. If only the basename of a configuration file is specified, all configuration directories as specified in <code><a href="/docs/linux/man/5-tmpfiles-d/">tmpfiles.d</a></code>(5) are searched for a matching file.</p>
<h2>Options</h2>
<p>The following options are understood: </p>
<p> <code>&#8211;create</code></p>
<dl>
<dd>If this option is passed, all files and directories marked with <i>f</i>, <i>F</i>, <i>w</i>, <i>d</i>, <i>D</i>, <i>p</i>, <i>L</i>, <i>c</i>, <i>b</i>, <i>m</i> in the configuration files are created or written to. Files and directories marked with <i>z</i>, <i>Z</i>, <i>m</i> have their ownership, access mode and security labels set.</dl>
<p> <code>&#8211;clean</code></p>
<dl>
<dd>If this option is passed, all files and directories with an age parameter configured will be cleaned up.</dl>
<p> <code>&#8211;remove</code></p>
<dl>
<dd>If this option is passed, all files and directories marked with <i>r</i>, <i>R</i> in the configuration files are removed.</dl>
<p> <code>&#8211;boot</code></p>
<dl>
<dd>Also execute lines with an exclamation mark.</dl>
<p> <code>&#8211;prefix=</code><i>path</i></p>
<dl>
<dd>Only apply rules that apply to paths with the specified prefix. This option can be specified multiple times.</dl>
<p> <code>&#8211;exclude-prefix=</code><i>path</i></p>
<dl>
<dd>Ignore rules that apply to paths with the specified prefix. This option can be specified multiple times.</dl>
<p> <code>&#8211;root=</code><i>root</i></p>
<dl>
<dd>Takes a directory path as an argument. All paths will be prefixed with the given alternate <i>root</i> path, including config search paths.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>Print a short version string and exit.</dl>
<p> It is possible to combine <code>&#8211;create</code>, <code>&#8211;clean</code>, and <code>&#8211;remove</code> in one invocation. For example, during boot the following command line is executed to ensure that all temporary and volatile directories are removed and created according to the configuration file: </p>
<dl>
<dd>
<pre>systemd-tmpfiles --remove --create</pre>
</dl>
<h2>Exit Status</h2>
<p>On success, 0 is returned, a non-zero failure code otherwise.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-tmpfiles-d/">tmpfiles.d</a></code>(5) </p>
