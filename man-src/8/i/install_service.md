---
title: "install_service(8)"
name: "install_service"
section: "8"
letter: "i"
url: "/docs/linux/man/8-install_service/"
description: "install_service – install initng‘s .ii files"
---

<p>install_service &#8211; install <i>initng</i>&#8216;s .ii files</p>
<h2>Synopsis</h2>
<p><code>install_service</code> <i>&#8211;in</i>|<i>-i</i> [<i>&#8211;out</i>|<i>-o</i>] [<i>&#8211;dist</i>|<i>-d</i>]</p>
<h2>Description</h2>
<p><code>install_service</code> parses files (normally .ii files) and sets distribution dependent values.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;in, -i</code></p>
<dd>Set the file which should be parsed.</p>
<dt><code>&#8211;out, -o</code></p>
<dd>Set the file the ouptput should be saved to. If this option is not set output goes to stdout.</p>
<dt><code>&#8211;dist, -d</code></p>
<dd>Set the distribution you want to install the file for (e.g. debian, gentoo, fedora). If this option is not set <i>install_service</i> will try to guess the distribution.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-initng/">initng</a>(8)</code> <code><a href="/docs/linux/man/8-ngc/">ngc</a>(8),</code> <code><a href="/docs/linux/man/8-ngdc/">ngdc</a>(8),</code> <code><a href="/docs/linux/man/8-ng-update/">ng-update</a>(8),</code> <code><a href="/docs/linux/man/8-gen_system_runlevel/">gen_system_runlevel</a>(8),</code> <code><a href="/docs/linux/man/8-system_off/">system_off</a>(8).</code></p>
<h2>Author</h2>
<p>initng was written by Jimmy Wennlund &lt;jimmy.wennlund [at] gmail.com&gt; and can be found at <a rel="nofollow" href="http://www.initng.org/.">http://www.initng.org/.</a> </p>
<p> This manual page was written by Armin Berres &lt;a.berres [at] onlinehome.de&gt;.</p>
