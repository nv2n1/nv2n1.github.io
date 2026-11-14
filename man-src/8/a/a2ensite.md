---
title: "a2ensite(8)"
name: "a2ensite"
section: "8"
letter: "a"
url: "/docs/linux/man/8-a2ensite/"
description: "a2ensite, a2dissite – enable or disable an apache2 site / virtual host"
---

<p>a2ensite, a2dissite &#8211; enable or disable an apache2 site / virtual host</p>
<h2>Synopsis</h2>
<p><code>a2ensite</code> [-q|&#8211;quiet] [-m|&#8211;maintmode] [ <i>site</i> ] </p>
<p> <code>a2dissite</code> [-q|&#8211;quiet] [-m|&#8211;maintmode] [-p|&#8211;purge] [ <i>site</i> ]</p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>a2ensite</code> and <code>a2dissite</code> commands. </p>
<p> <code>a2ensite</code> is a script that enables the specified site (which contains a &lt;VirtualHost&gt; block) within the <code>apache2</code> configuration. It does this by creating symlinks within <code>/etc/apache2/sites-enabled</code>. Likewise, <code>a2dissite</code> disables a site by removing those symlinks. It is not an error to enable a site which is already enabled, or to disable one which is already disabled. </p>
<p> Apache treats the very first virtual host enabled specially as every request not matching any actual directive is being redirected there. Thus it should be called <code>000-default</code> in order to sort before the remaining hosts to be loaded first.</p>
<h2>Options</h2>
<dl>
<dt><code>-q, &#8211;quiet</code></p>
<dd>Don&#8217;t show informative messages.</p>
<dt><code>-m, &#8211;maintmode</code></p>
<dd>Enables the maintainer mode, that is the program invocation is effectuated automatically by a maintainer script. This switch should not be used by end users.</p>
<dt><code>-p, &#8211;purge</code></p>
<dd>When disabling a module, purge all traces of the module in the internal state data base.</dl>
<h2>Exit Status</h2>
<p><code>a2ensite</code> and <code>a2dissite</code> exit with status 0 if all <i>site</i>s are processed successfully, 1 if errors occur, 2 if an invalid option was used.</p>
<h2>Examples</h2>
<dl>
<dd><code>a2dissite 000-default</code></dl>
<p> Disables the <code>default</code> site.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/apache2/sites-available</code></p>
<dd>Directory with files giving information on available sites.</p>
<dt><code>/etc/apache2/sites-enabled</code></p>
<dd>Directory with links to the files in <code>sites-available</code> for enabled sites.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-apache2ctl/">apache2ctl</a></code>(8), <code><a href="/docs/linux/man/8-a2enmod/">a2enmod</a></code>(8), <code><a href="/docs/linux/man/8-a2dismod/">a2dismod</a></code>(8), <code><a href="/docs/linux/man/8-a2enconf/">a2enconf</a></code>(8), <code><a href="/docs/linux/man/8-a2disconf/">a2disconf</a></code>(8).</p>
<h2>Author</h2>
<p>This manual page was written by Stefan Fritsch &lt;sf [at] debian.org&gt; (based on the a2enmod manual page by Daniel Stone &lt;daniel [at] sfarc.net&gt;) for the Debian GNU/Linux distribution.</p>
