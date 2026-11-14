---
title: "a2enconf(8)"
name: "a2enconf"
section: "8"
letter: "a"
url: "/docs/linux/man/8-a2enconf/"
description: "a2enconf, a2disconf – enable or disable an apache2 configuration file"
---

<p>a2enconf, a2disconf &#8211; enable or disable an apache2 configuration file</p>
<h2>Synopsis</h2>
<p><code>a2enconf</code> [-q|&#8211;quiet] [-m|&#8211;maintmode] [ <i>configuration</i> ] </p>
<p> <code>a2disconf</code> [-q|&#8211;quiet] [-m|&#8211;maintmode] [-p|&#8211;purge] [ <i>configuration</i> ]</p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>a2enconf</code> and <code>a2disconf</code> commands. </p>
<p> <code>a2enconf</code> is a script that enables the specified configuration file within the <code>apache2</code> configuration. It does this by creating symlinks within <code>/etc/apache2/conf-enabled</code>. Likewise, <code>a2disconf</code> disables a specific configuration part by removing those symlinks. It is not an error to enable a configuration which is already enabled, or to disable one which is already disabled. </p>
<p> Note that many configuration file may have a dependency to specific modules. Unlike module dependencies, these are not resolved automatically. Configuration fragments stored in the conf-available directory are considered non-essential or being installed and manged by reverse dependencies (e.g. web scripts).</p>
<h2>Options</h2>
<dl>
<dt><code>-q, &#8211;quiet</code></p>
<dd>Don&#8217;t show informative messages.</p>
<dt><code>-m, &#8211;maintmode</code></p>
<dd>Enables the maintainer mode, that is the program invocation is effectuated automatically by a maintainer script. This switch should not be used by end users.</p>
<dt><code>-p, &#8211;purge</code></p>
<dd>When disabling a module, purge all traces of the module in the internal state data base.</dl>
<h2>Exit Status</h2>
<p><code>a2enconf</code> and <code>a2disconf</code> exit with status 0 if all <i>configuration</i>s are processed successfully, 1 if errors occur, 2 if an invalid option was used.</p>
<h2>Examples</h2>
<dl>
<dd><code>a2enconf security</code><br />
 <code>a2disconf charset</code></dl>
<p> Enables Apache security directives stored in the <code>security</code> configuration files, and disables the <code>charset</code> configuration.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/apache2/conf-available</code></p>
<dd>Directory with files giving information on available configuration files.</p>
<dt><code>/etc/apache2/conf-enabled</code></p>
<dd>Directory with links to the files in <code>conf-available</code> for enabled configuration files.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-apache2ctl/">apache2ctl</a></code>(8), <code><a href="/docs/linux/man/8-a2enmod/">a2enmod</a></code>(8), <code><a href="/docs/linux/man/8-a2dismod/">a2dismod</a></code>(8), <code><a href="/docs/linux/man/8-a2ensite/">a2ensite</a></code>(8), <code><a href="/docs/linux/man/8-a2dissite/">a2dissite</a></code>(8).</p>
<h2>Author</h2>
<p>This manual page was written by Arno Toell &lt;debian [at] toell.net&gt; for the Debian GNU/Linux distribution, as it is a Debian-specific script with the package.</p>
