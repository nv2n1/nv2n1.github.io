---
title: "ucf-conf(5)"
name: "ucf-conf"
section: "5"
letter: "u"
url: "/docs/linux/man/5-ucf-conf/"
description: "ucf.conf – site-wide configuration file for ucf"
---

<p>ucf.conf &#8211; site-wide configuration file for <code>ucf</code></p>
<h2>Synopsis</h2>
<p><i>/etc/ucf.conf</i></p>
<h2>Description</h2>
<p>The file <i>/etc/ucf.conf</i> is actually a <code>Bourne Shell</code> snippet included during the package build process, and hence you may put any shell directive in that file (just make very sure you know what you are doing). </p>
<p> All the variables have reasonable default values, and some may be overridden on a per run or a per individual basis by using environment variables, and all configurable variables can be overridden by options to the scripts themselves. </p>
<p> The value of a variable can be set so:</p>
<dl>
<dt>a)</p>
<dd>Defaults exist in the rules file. These are the values used if no customization is done.</p>
<dt>b)</p>
<dd>Some variables can be set in the config file <i>/etc/ucf.conf. </i> These values override the defaults.</p>
<dt>c)</p>
<dd>Some variables can also be set by setting a corresponding environment variable. These values override the config file and the defaults.</p>
<dt>d)</p>
<dd>Using script command line options. All configurable variables may be set by this method, and will override the other methods above.</dl>
<h2>Configuration File options</h2>
<p>At the moment, the user modifiable variables supported are:</p>
<dl>
<dt><code>DEBUG</code></p>
<dd>Debugging information: The default value is 0 (no debugging information is printed). To enable debugging output, set the value to 1.</p>
<dt><code>VERBOSE</code></p>
<dd>Verbosity: The default value is 0 (quiet). To change the default behavior, set the value to 1.</p>
<dt><code>conf_force_conffold</code></p>
<dd>Force the installed file to be retained. The default is to have this variable unset, which makes the script ask in case of doubt. This can be overridden by the environment variable <code>UCF_FORCE_CONFFOLD</code></p>
<dt><code>conf_force_conffnew</code></p>
<dd>Force the installed file to be overridden. The default is to have this variable unset, which makes the script ask in case of doubt. This can be overridden by the environment variable <code>UCF_FORCE_CONFFNEW</code></p>
<dt><code>conf_source_dir</code></p>
<dd>This is the directory where the historical md5sums for a file are looked for. Specifically, the historical md5sums are looked for in either the file <i>${filename}.md5sum,</i> or the subdirectory <i>${filename}.md5sum.d/ </i></p>
<dt><code>conf_old_mdsum_file</code></p>
<dd>Force the historical md5sums to be read from this file, rather than defaulting to living in the source directory. Setting this option overrides settings in the environment variable <code>UCF_OLD_MDSUM_FILE</code></dl>
<h2>Files</h2>
<p>System-wide defaults are placed in <i>/etc/ucf.conf,</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ucf/">ucf</a></code>(1),</p>
<h2>Bugs</h2>
<p>There are no bugs. Any resemblance thereof is delirium. Really.</p>
<h2>Author</h2>
<p>This manual page was written by Manoj Srivastava &lt;srivasta [at] debian.org&gt;, for the Debian GNU/Linux system.</p>
