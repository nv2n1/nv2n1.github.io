---
title: "tarsnap-conf(5)"
name: "tarsnap-conf"
section: "5"
letter: "t"
url: "/docs/linux/man/5-tarsnap-conf/"
description: "tarsnap.conf – configuration file for tarsnap(1)"
---

<p><code>tarsnap.conf</code> &#8211; configuration file for <a href="/docs/linux/man/1-tarsnap/">tarsnap</a>(1)</p>
<h2>Description</h2>
<p>The file is read by the <a href="/docs/linux/man/1-tarsnap/">tarsnap</a>(1) utility and specifies default options which will be ignored if the options in question are specified at the command line. Options may be specified in /etc/tarsnap.conf and/or ~/.tarsnaprc if the two files conflict, the user&#8217;s local configuration takes precedence. The file(s) contain lines consisting of a case-sensitive option name and zero or one parameters depending upon the option. Empty lines and lines starting with a `#&#8217; character are ignored. If a parameter begins with a `~&#8217; character, it will be replaced by the value of the HOME variable (the current user&#8217;s home directory). The following options may be specified: </p>
<dt><code>aggressive-networking</code></p>
<dd>
<dt><code>cachedir </code><i>cache-dir</i></p>
<dd>
<dt><code>checkpoint-bytes </code><i>bytespercheckpoint</i></p>
<dd>
<dt><code>disk-pause </code><i>X</i></p>
<dd>
<dt><code>exclude </code><i>pattern</i></p>
<dd>
<dt><code>humanize-numbers</code></p>
<dd>
<dt><code>include </code><i>pattern</i></p>
<dd>
<dt><code>insane-filesystems</code></p>
<dd>
<dt><code>keyfile key-file </code></p>
<dd>
<dt><code>lowmem</code></p>
<dd>
<dt><code>maxbw</code></p>
<dd>
<dt><code>maxbw-rate</code></p>
<dd>
<dt><code>maxbw-rate-down</code></p>
<dd>
<dt><code>maxbw-rate-up</code></p>
<dd>
<dt><code>nodump</code></p>
<dd>
<dt><code>normalmem</code></p>
<dd>
<dt><code>no-aggressive-networking</code></p>
<dd>
<dt><code>no-config-exclude</code></p>
<dd>
<dt><code>no-config-include</code></p>
<dd>
<dt><code>no-disk-pause</code></p>
<dd>
<dt><code>no-humanize-numbers</code></p>
<dd>
<dt><code>no-insane-filesystems</code></p>
<dd>
<dt><code>no-maxbw</code></p>
<dd>
<dt><code>no-maxbw-rate-down</code></p>
<dd>
<dt><code>no-maxbw-rate-up</code></p>
<dd>
<dt><code>no-nodump</code></p>
<dd>
<dt><code>no-print-stats</code></p>
<dd>
<dt><code>no-quiet</code></p>
<dd>
<dt><code>no-snaptime</code></p>
<dd>
<dt><code>no-store-atime</code></p>
<dd>
<dt><code>no-totals</code></p>
<dd>
<dt><code>print-stats</code></p>
<dd>
<dt><code>quiet</code></p>
<dd>
<dt><code>snaptime file </code></p>
<dd>
<dt><code>store-atime</code></p>
<dd>
<dt><code>totals</code></p>
<dd>
<dt><code>verylowmem</code></p>
<dd></dl>
<p> Each option is handled the same way as the corresponding &#8211;<code>-option</code> see <a href="/docs/linux/man/1-tarsnap/">tarsnap</a>(1) for more details. Note that the <code>normalmem</code> and <code>no-*</code> options are only useful in the user-specific ~/.tarsnaprc configuration file, at which point they act to override options set in the global /etc/tarsnap.conf configuration file.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/tarsnap.conf </code></p>
<dd>The system global configuration file. Parameters specified here only take effect if they are not specified via the current user&#8217;s local configuration file or via the command line.</p>
<dt><code>~/.tarsnaprc </code></p>
<dd>The configuration file for the current user. Parameters specified here take effect unless they are specified via the command line.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-tarsnap/">tarsnap</a>(1) </p>
