---
title: "zonec(8)"
name: "zonec"
section: "8"
letter: "z"
url: "/docs/linux/man/8-zonec/"
description: "zonec – NSD zone compiler version 3.2.4."
---

<p><code>zonec</code> &#8211; NSD zone compiler version 3.2.4.</p>
<h2>Synopsis</h2>
<p><code>zonec</code> [<code>-v</code>] [<code>-h</code>] [<code>-C</code>] [<code>-L</code>] [<code>-F</code>] [<code>-c</code> <i>configfile</i>] [<code>-d</code> <i>directory</i>] [<code>-o</code> <i>origin</i>] [<code>-z</code> <i>zonefile</i>] [<code>-f</code> <i>database</i>]</p>
<h2>Description</h2>
<p><code>Zonec</code> is the <a href="/docs/linux/man/8-nsd/">nsd</a>(8) database compiler for creating name space databases from a set of input master zone files specified in <a href="/docs/linux/man/5-nsd-conf/">nsd.conf</a>(5) file. </p>
<p> It is normally invoked via <a href="/docs/linux/man/8-nsdc/">nsdc</a>(8) rebuild command. <code>Zonec</code> will then parse every zone in <a href="/docs/linux/man/5-nsd-conf/">nsd.conf</a>(5) file and add it to the name space database, <i>/var/db/nsd/nsd.db</i> by default, that is used by <a href="/docs/linux/man/8-nsd/">nsd</a>(8) to answer incoming queries.</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code><i> configfile</i></p>
<dd>Read specified configfile instead of the default <i>/etc/nsd/nsd.conf</i>.</p>
<dt><code>-C </code></p>
<dd>No config file is read (use with -f, -o and -z).</p>
<dt><code>-d</code><i> directory</i></p>
<dd>Change the working directory to <i>directory</i> before doing any work. Overrides zonesdir: option in config file.</p>
<dt><code>-f</code><i> database</i></p>
<dd>Create the specified <i>database</i> instead of the file specified as database: in the config file.</p>
<dt><code>-o</code><i> origin</i></p>
<dd>Use this as the first origin. Zone information is read from zonefile specified with -z. When reading zones from config file this option is ignored.</p>
<dt><code>-z</code><i> zonefile</i></p>
<dd>Reads all zone information from <i>zonefile</i>. If <i>zonefile</i> equals `-`, then all zone information is read from stdin, making constructs like:</dl>
<dl>
<dd><code># cat zones* </code> | <code>./zonec -C -f nsd.db -o example.net -z &#8211;</code></dl>
<dl>
<dd>possible. When reading zones from config file this option is ignored.</dl>
<dl>
<dt><code>-v</code></p>
<dd>Increase the verbosity of zonec. This flag can be specified multiple times to increase the level of verbosity. The first level of verbosity will print per zone summary information. The second level of will print progress information for each 10,000 RRs processed.</p>
<dt><code>-F</code></p>
<dd>Set debug facilities. (If compiled with &#8211;enable-checking.)</p>
<dt><code>-L</code></p>
<dd>Set debug level. (If compiled with &#8211;enable-checking.)</dl>
<h2>Files</h2>
<dl>
<dt>/var/db/nsd/nsd.db</p>
<dd>default <code>NSD</code> database</p>
<dt>/etc/nsd/nsd.conf</p>
<dd>default <code>NSD</code> configuration file</dl>
<h2>Diagnostics</h2>
<p><code>Zonec</code> will log all the problems via the standard error output and progress via stdout if the <code>v</code> option is specified.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-nsd/">nsd</a>(8), <a href="/docs/linux/man/8-nsdc/">nsdc</a>(8), <a href="/docs/linux/man/5-nsd-conf/">nsd.conf</a>(5), <a href="/docs/linux/man/8-nsd-checkconf/">nsd-checkconf</a>(8), <a href="/docs/linux/man/8-nsd-notify/">nsd-notify</a>(8), <a href="/docs/linux/man/8-nsd-patch/">nsd-patch</a>(8), <a href="/docs/linux/man/8-nsd-xfer/">nsd-xfer</a>(8)</p>
<h2>Authors</h2>
<p><code>NSD</code> was written by NLnet Labs and RIPE NCC joint team. Please see CREDITS file in the distribution for further details.</p>
<h2>Bugs</h2>
<p><code>Zonec </code> has rather weak error diagnostics that will change in further versions. <code>Zonec</code> expects the input files to be free of syntax errors and very little fool proof checks are done. </p>
