---
title: "rpmlint(1)"
name: "rpmlint"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rpmlint/"
description: "rpmlint – check common problems in rpm packages"
---

<h2>NAME</h2>
<p> rpmlint &#8211; check common problems in rpm packages</p>
<h2>SYNOPSIS</h2>
<p> <code>rpmlint</code> [<i>OPTION</i>]&#8230; [<i>FILE</i>|<i>PACKAGE</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>rpmlint</code> is a tool for checking common errors in rpm packages. It can be used to test individual packages and spec files before uploading or to check an entire distribution. By default all applicable checks are processed but specific checks can be performed by using command line parameters. </p>
<p> <i>FILE</i> can be a rpm package file, a spec file, or a directory. In case of a directory, it is recursively searched for rpm and spec files to check. The special value <code>&#8211;</code> results in standard input being read and treated as (single) spec file content. <i>PACKAGE</i> is the name of an installed package or a <code><a href="/docs/linux/man/7-glob/">glob</a></code>(7) pattern to match installed packages, unless a file by that name exists.</p>
<dl>
<dt><code>-i</code>, <code>&#8211;info</code></p>
<dd> Display explanations for reported messages.</p>
<dt><code>-I</code>, <code>&#8211;explain</code>=<i>messageid</i></p>
<dd> Display explanations for the specified message identifiers and exit. This option may be given multiple times.</p>
<dt><code>-c</code>, <code>&#8211;check</code>=<i>check</i></p>
<dd> Run only the specified check. This option may be given multiple times to specify multiple checks to run. <i>check</i> is the name of the Python module (as it would be given to Python&#8217;s import statement) containing the check.</p>
<dt><code>-a</code>, <code>&#8211;all</code></p>
<dd> Check all installed packages.</p>
<dt><code>-C</code>, <code>&#8211;checkdir</code>=<i>dir</i></p>
<dd> Insert <i>dir</i> to the front of the list of paths to load checks from, unless it is already in the list. The default list of check dirs typically contains only /usr/share/rpmlint. Directories in the check dirs list are also inserted to the front of the list of paths to load Python modules from when the check process begins.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display summary of command line options and exit.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Operate in verbose mode.</p>
<dt><code>-E</code>, <code>&#8211;extractdir</code>=<i>dir</i></p>
<dd> Base directory for extracted temporary files, default is what Python&#8217;s tempfile.gettempdir() returns.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Display version information and exit.</p>
<dt><code>-n</code>, <code>&#8211;noexception</code></p>
<dd> Ignore output filters.</p>
<dt><code>&#8211;rawout</code>=<i>file</i></p>
<dd> Write unfiltered output to <i>file</i>.</p>
<dt><code>-f</code>, <code>&#8211;file</code>=<i>conffile</i></p>
<dd> Load user configuration from the specified file, default is $XDG_CONFIG_HOME/rpmlint (~/.config/rpmlint if $XDG_CONFIG_HOME is empty or not set).</p>
<dt><code>-o</code>, <code>&#8211;option</code>=<i>value</i></p>
<dd> Override a configuration option. <i>value</i> is a whitespace separated string, first word of which is the option name to set, and the Python eval() return value for the rest is set as the value for the option. Passing only an option name is treated as if None was passed as its value. See the file &quot;config&quot; shipped with rpmlint for the list of configuration options and their types. For example:<br />
&nbsp;<wbr>-o&nbsp;<wbr>&quot;NetworkEnabled True&quot;<br />
&nbsp;<wbr>-o&nbsp;<wbr>&quot;Distribution&nbsp;<wbr>&#8216;My favorite distro&#8217;&quot;<br />
&nbsp;<wbr>-o&nbsp;<wbr>&quot;MaxLineLength 80&quot;<br />
&nbsp;<wbr>-o&nbsp;<wbr>&quot;ValidShells&nbsp;<wbr>(&#8216;/bin/sh&#8217;,&nbsp;<wbr>&#8216;/bin/bash&#8217;)&quot;</dl>
<h2>CAVEATS</h2>
<p> All checks do not apply to all argument types. For best check coverage, run rpmlint on all source and binary packages your build produces. The set of checks rpmlint runs on source packages is a superset of the one for plain specfiles, the set of checks run for installed binary packages is a superset of the one for uninstalled binary package files, and the source and binary package check sets are quite different.</p>
<h2>FILES</h2>
<dl>
<dt><code>/usr/share/rpmlint/config</code>, <code>/usr/share/rpmlint/config.*</code></p>
<dd> Built-in configuration. When invoked as <i>someprefix</i>-rpmlint, /usr/share/rpmlint/config.<i>someprefix</i> is used if it exists, otherwise /usr/share/rpmlint/config.</p>
<dt><code>/etc/rpmlint/*config</code></p>
<dd> System wide configuration.</p>
<dt><code>$XDG_CONFIG_HOME/rpmlint</code> or <code>~/.config/rpmlint</code></p>
<dd> User configuration.</dl>
<h2>EXIT CODES</h2>
<dl>
<dt>0</p>
<dd> No errors.</p>
<dt>1</p>
<dd> Unspecified error.</p>
<dt>2</p>
<dd> Interrupted.</p>
<dt>64</p>
<dd> One or more error message printed.</p>
<dt>66</p>
<dd> Badness threshold exceeded.</dl>
<h2>AUTHOR</h2>
<p> Originally written by Frédéric Lepied, see the file AUTHORS for (probably incomplete) list of additional contributors.</p>
<h2>COPYRIGHT</h2>
<p> This program is licensed under the GNU General Public License, see the file COPYING included in the distribution archive. </p>
<h2>Index</h2>
