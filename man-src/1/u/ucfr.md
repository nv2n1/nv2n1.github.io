---
title: "ucfr(1)"
name: "ucfr"
section: "1"
letter: "u"
url: "/docs/linux/man/1-ucfr/"
description: "ucfr – Update Configuration File Registry: associate packages with configuration files"
---

<h2 class="name">NAME</h2>
<p> ucfr &#8211; Update Configuration File Registry: associate packages with configuration files </p>
<h2>SYNOPSIS</h2>
<p> <code>ucfr</code> [<i>options</i>] <i>&lt;Package&gt;</i> <i>&lt;Path to configuration file&gt;</i></p>
<h2>DESCRIPTION</h2>
<p> Where <i>Package</i> is the package associated with the configuration file (and, in some sense, its owner), and <i>Path to configuration file</i> is the full path to the location (usually under /etc) where the configuration file lives, and is potentially modified by the end user. Please note that usually this means that we register actual files, and not symbolic links to files. <code>ucfr</code> will follow symbolic links and register the real file, and not the symbolic link. </p>
<p> This script maintains an association between configuration files and packages, and is meant to help provide facilities that <i>dpkg</i> provides conffiles for configuration files and not shipped in a <code>Debian</code> package, but handled by the postinst by <i>ucf</i> instead. This script is idempotent, associating a package to a file multiple times is not an error. It is normally an error to try to associate a file which is already associated with another package, but this can be overridden by using the <i>&#8211;force</i> option.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Print a short usage message</p>
<dt><code>-n, &#8211;no-action</code></p>
<dd> Dry run. Print the actions that would be taken if the script is invoked, but take no action.</p>
<dt><code>-d [n], &#8211;debug [n]</code></p>
<dd> Set the debug level to the (optional) level <i>n</i> (n defaults to 1). This turns on copious debugging information.</p>
<dt><code>-p, &#8211;purge</code></p>
<dd> Removes all vestiges of the association between the named package and the configuration file from the registry. The association must already exist; if the configuration file is associated with some other package, an error happens, unless the option <i>&#8211;force</i> is also given. In that case, the any associations for the configuration file are removed from the registry, whether or not the package name matches. This action is idempotent, asking for an association to be purged multiple times does not result in an error, since attempting to remove an non-existent association is silently ignored unless the <i>&#8211;verbose</i> option is used (in which case it just issues a diagnostic).</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Make the script be very verbose about setting internal variables.</p>
<dt><code>-f, &#8211;force</code></p>
<dd> This option forces operations requested even if the configuration file in consideration is owned by another package. This allows a package to <i>hijack</i> a configuration file from another package, or to purge the association between the file and some other package in the registry.</p>
<dt><code>&#8211;state-dir /path/to/dir</code></p>
<dd> Set the state directory to /path/to/dir instead of the default <i>/var/lib/ucf.</i> Used mostly for testing.</dl>
<h2>USAGE</h2>
<p> The most common case usage is pretty simple: a single line invocation in the postinst on configure, and another single line in the postrm to tell <code>ucfr</code> to forget about the association with the configuration file on purge (using the &#8211;purge option) is all that is needed (assuming ucfr is still on the system).</p>
<h2>FILES</h2>
<p> <i>/var/lib/ucf/registry,</i> and <i>/var/lib/ucf/registry.X,</i> where <i>X</i> is a small integer, where previous versions of the registry are stored. </p>
<p> <i>/etc/ucf.conf</i></p>
<h2>EXAMPLES</h2>
<p> If the package <i>foo</i> wants to use ucfr to associate itself with a configuration file <i>foo.conf,</i> a simple invocation of ucfr in the postinst file is all that is needed: </p>
<p> <code>ucfr</code> <i>foo</i> <i>/etc/foo.conf</i> </p>
<p> On purge, one should tell ucf to forget about the file (see detailed examples in /usr/share/doc/ucf/examples): </p>
<p> <code>ucfr</code> <i>&#8211;purge</i> <i>foo</i> <i>/etc/foo.conf</i> </p>
<p> If you want to remove all the conf files for a given package <i>foo,</i> the simplest way is to use <code>ucfq.</code> For example </p>
<p> <code>ucfq</code> <i>-w</i> <i>foo |</i> <code>cut</code> <i>-d : -f 1 |</i> <code>while read</code> <i>cfile ;</i> <code>do</code> <code>ucfr</code> <i>-v $cfile ;</i> <code>done</code></p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ucf/">ucf</a>(1), <a href="/docs/linux/man/5-ucf-conf/">ucf.conf</a>(5).</p>
<h2>AUTHOR</h2>
<p> This manual page was written Manoj Srivastava &lt;srivasta [at] debian.org&gt;, for the Debian GNU/Linux system. </p>
<h2>Index</h2>
