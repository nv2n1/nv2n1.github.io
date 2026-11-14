---
title: "nsd-checkconf(8)"
name: "nsd-checkconf"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nsd-checkconf/"
description: "nsd-checkconf – NSD configuration file checker."
---

<p><code>nsd-checkconf</code> &#8211; NSD configuration file checker.</p>
<h2>Synopsis</h2>
<p><code>nsd-checkconf</code> [<code>-v</code>] [<code>-f</code>] [<code>-h</code>] [<code>-o</code> <i>option</i>] [<code>-z</code> <i>zonename</i>] [<code>-p</code> <i>pattern</i>] [<code>-s</code> <i>keyname</i>] <i>configfile</i></p>
<h2>Description</h2>
<p><code>nsd-checkconf</code> reads a configuration file. It prints parse errors to standard error, and performs additional checks on the contents. The configfile format is described in <a href="/docs/linux/man/5-nsd-conf/">nsd.conf</a>(5). The utility of this program is to check a config file for errors before using it in <a href="/docs/linux/man/8-nsd/">nsd</a>(8). This program can also be used for shell scripts to access the nsd config file, using the -o and -z options. </p>
<h2>Options</h2>
<dl>
<dt><code>-v</code></p>
<dd>After reading print the options to standard output in configfile format. Without this option, only success or parse errors are reported.</p>
<dt><code>-f</code></p>
<dd>Print full pathname when used with files, like with -o pidfile. This includes the chroot in the way it is applied to the pidfile.</p>
<dt><code>-h</code></p>
<dd>Print usage help information and exit.</p>
<dt><code>-o</code><i> option</i></p>
<dd>Return only this option from the config file. This option can be used in conjunction with the <code>-z</code> and the <code>-p</code> option, or without them to query the server: section. The special value <i>zones</i> prints out a list of configured zones. The special value <i>patterns</i> prints out a list of configured patterns.</dl>
<dl>
<dd>This option can be used to parse the config file from the shell. If the <code>-z</code> option is given, but the <code>-o </code> option is not given, nothing is printed.</dl>
<dl>
<dt><code>-s</code><i> keyname</i></p>
<dd>Prints the key secret (base64 blob) configured for this key in the config file. Used to help shell scripts parse the config file.</p>
<dt><code>-p</code><i> pattern</i></p>
<dd>Return the option specified with <code>-o</code> for the given pattern name.</p>
<dt><code>-z</code><i> zonename</i></p>
<dd>Return the option specified with <code>-o</code> for zone &#8216;zonename&#8217;.</dl>
<dl>
<dd>If this option is not given, the server section of the config file is used.</dl>
<dl>
<dd>The -o, -s and -z option print configfile options to standard output.</dl>
<h2>Files</h2>
<dl>
<dt>/etc/nsd/nsd.conf</p>
<dd>default <code>NSD</code> configuration file</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-nsd/">nsd</a></i>(8), <i><a href="/docs/linux/man/5-nsd-conf/">nsd.conf</a></i>(5), <i><a href="/docs/linux/man/8-nsd-control/">nsd-control</a></i>(8)</p>
<h2>Authors</h2>
<p><code>NSD</code> was written by NLnet Labs and RIPE NCC joint team. Please see CREDITS file in the distribution for further details.</p>
