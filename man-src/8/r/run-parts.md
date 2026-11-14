---
title: "run-parts(8)"
name: "run-parts"
section: "8"
letter: "r"
url: "/docs/linux/man/8-run-parts/"
description: "run-parts – run scripts or programs in a directory"
---

<p>run-parts &#8211; run scripts or programs in a directory</p>
<h2>Synopsis</h2>
<p><code>run-parts</code> [&#8211;test] [&#8211;verbose] [&#8211;debug] [&#8211;report] [&#8211;lsbsysinit] [&#8211;regex=RE] [&#8211;umask=umask] [&#8211;arg=argument] [&#8211;exit-on-error] [&#8211;help] [&#8211;version] [&#8211;list] [&#8211;reverse] [&#8211;] DIRECTORY </p>
<p> <code>run-parts</code> -V</p>
<h2>Description</h2>
<p><code>run-parts</code> runs all the executable files named within constraints described below, found in directory <i>directory</i>. Other files and directories are silently ignored. If neither the &#8211;lsbsysinit option nor the &#8211;regex option is given then the names must consist entirely of ASCII upper- and lower-case letters, ASCII digits, ASCII underscores, and ASCII minus-hyphens. If the &#8211;lsbsysinit option is given, then the names must not end in .dpkg-old or .dpkg-dist or .dpkg-new or .dpkg-tmp, and must belong to one or more of the following namespaces: the LANANA-assigned namespace (^[a-z0-9]+$); the LSB hierarchical and reserved namespaces (^_?([a-z0-9_.]+-)+[a-z0-9]+$); and the Debian cron script namespace (^[a-zA-Z0-9_-]+$). If the &#8211;regex option is given, the names must match the custom extended regular expression specified as that option&#8217;s argument. Files are run sequentially in the lexical sort order (according to the C/POSIX locale character collation rules) of their names unless the &#8211;reverse option is given, in which case they are run in the opposite order. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;test</code></p>
<dd>print the names of the scripts which would be run, but don&#8217;t actually run them.</p>
<dt><code>&#8211;list</code></p>
<dd>print the names of the all matching files (not limited to executables), but don&#8217;t actually run them. This option cannot be used with &#8211;test.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>print the name of each script to stderr before running.</p>
<dt><code>&#8211;report</code></p>
<dd>similar to <code>&#8211;verbose</code>, but only prints the name of scripts which produce output. The script&#8217;s name is printed to whichever of stdout or stderr the script first produces output on.</p>
<dt><code>-d, &#8211;debug</code></p>
<dd>print to stderr which scripts get selected for running and which don&#8217;t.</p>
<dt><code>&#8211;reverse</code></p>
<dd>reverse the scripts&#8217; execution order.</p>
<dt><code>&#8211;exit-on-error</code></p>
<dd>exit as soon as a script returns with a non-zero exit code.</p>
<dt><code>&#8211;lsbsysinit</code></p>
<dd>use LSB namespaces instead of classical behavior.</p>
<dt><code>&#8211;new-session</code></p>
<dd>run each script in a separate process session. If you use this option, killing run-parts will not kill the currently running script, it will run until completion.</p>
<dt><code>&#8211;regex=</code><i>RE</i></p>
<dd>validate filenames against custom extended regular expression <i>RE</i>. See the EXAMPLES section for an example.</p>
<dt><code>-u, &#8211;umask=</code><i>umask</i></p>
<dd>sets the umask to <i>umask</i> before running the scripts. <i>umask</i> should be specified in octal. By default the umask is set to 022.</p>
<dt><code>-a, &#8211;arg=</code><i>argument</i></p>
<dd>pass <i>argument</i> to the scripts. Use <code>&#8211;arg</code> once for each argument you want passed.</p>
<dt><code>&#8212;</code></p>
<dd>specifies that this is the end of the options. Any filename after <code>&#8212;</code> will be not be interpreted as an option even if it starts with a hyphen.</p>
<dt><code>-h, &#8211;help</code></p>
<dd>display usage information and exit.</p>
<dt><code>-V, &#8211;version</code></p>
<dd>display version and copyright and exit. </p>
</dl>
<h2>Examples</h2>
<p>Print the names of all files in /etc that start with `p&#8217; and end with `d&#8217;: run-parts &#8211;list &#8211;regex &#8216;^p.*d$&#8217; /etc </p>
<h2>Copyright</h2>
<p>Copyright (C) 1994 Ian Jackson. </p>
<p> Copyright (C) 1996 Jeff Noxon. </p>
<p> Copyright (C) 1996, 1997, 1998 Guy Maor </p>
<p> Copyright (C) 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009 Clint Adams </p>
<p> <code>run-parts</code> is free software; see the GNU General Public License version 2 or later for copying conditions. There is <i>no</i> warranty.</p>
