---
title: "a2enmod(8)"
name: "a2enmod"
section: "8"
letter: "a"
url: "/docs/linux/man/8-a2enmod/"
description: "a2enmod, a2dismod – enable or disable an apache2 module"
---

<p>a2enmod, a2dismod &#8211; enable or disable an apache2 module</p>
<h2>Synopsis</h2>
<p><code>a2enmod</code> [-q|&#8211;quiet] [-m|&#8211;maintmode] [ <i>module</i> ] </p>
<p> <code>a2dismod</code> [-q|&#8211;quiet] [-f|&#8211;force] [-m|&#8211;maintmode] [-p|&#8211;purge] [ <i>module</i> ]</p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>a2enmod</code> and <code>a2dismod</code> commands. </p>
<p> <code>a2enmod</code> is a script that enables the specified module within the <code>apache2</code> configuration. It does this by creating symlinks within <code>/etc/apache2/mods-enabled</code>. Likewise, <code>a2dismod</code> disables a module by removing those symlinks. It is not an error to enable a module which is already enabled, or to disable one which is already disabled. </p>
<p> Note that many modules have, in addition to a .load file, an associated .conf file. Enabling the module puts the configuration directives in the .conf file as directives into the main server context of <code>apache2.</code></p>
<h2>Options</h2>
<dl>
<dt><code>-q, &#8211;quiet</code></p>
<dd>Don&#8217;t show informative messages.</p>
<dt><code>-f, &#8211;force</code></p>
<dd>When disabling a module, also cascade disables all modules that depends on it.</p>
<dt><code>-m, &#8211;maintmode</code></p>
<dd>Enables the maintainer mode, that is the program invocation is effectuated automatically by a maintainer script. This switch should not be used by end users.</p>
<dt><code>-p, &#8211;purge</code></p>
<dd>When disabling a module, purge all traces of the module in the internal state data base.</dl>
<h2>Exit Status</h2>
<p><code>a2enmod</code> and <code>a2dismod</code> exit with status 0 if all <i>module</i>s are processed successfully, 1 if errors occur, 2 if an invalid option was used.</p>
<h2>Examples</h2>
<dl>
<dd><code>a2enmod imagemap</code><br />
 <code>a2dismod mime_magic</code></dl>
<p> Enables the <code>mod_imagemap</code> module, and disables the <code>mod_mime_magic</code> module.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/apache2/mods-available</code></p>
<dd>Directory with files giving information on available modules.</p>
<dt><code>/etc/apache2/mods-enabled</code></p>
<dd>Directory with links to the files in <code>mods-available</code> for enabled modules.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-apache2ctl/">apache2ctl</a></code>(8), <code><a href="/docs/linux/man/8-a2enconf/">a2enconf</a></code>(8), <code><a href="/docs/linux/man/8-a2disconf/">a2disconf</a></code>(8), <code><a href="/docs/linux/man/8-a2ensite/">a2ensite</a></code>(8), <code><a href="/docs/linux/man/8-a2dissite/">a2dissite</a></code>(8).</p>
<h2>Author</h2>
<p>This manual page was written by Daniel Stone &lt;daniel [at] sfarc.net&gt; for the Debian GNU/Linux distribution, as it is a Debian-specific script with the package.</p>
