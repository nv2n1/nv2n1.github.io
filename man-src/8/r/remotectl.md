---
title: "remotectl(8)"
name: "remotectl"
section: "8"
letter: "r"
url: "/docs/linux/man/8-remotectl/"
description: "remotectl – Remote Access Configuration"
---

<p>remotectl &#8211; Remote Access Configuration</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>remotectl</code> {COMMAND} [OPTIONS&#8230;]</dl>
<h2>Description</h2>
<dd>The <code>remotectl</code> program will configure remote access to the system. Currently it manages cockpit&#8217;s SSL certificate.</p>
<h2>Commands</h2>
<p><code>certificate</code></p>
<dl>
<dd>Manage Cockpit&#8217;s SSL certificate. If used without options will check if cockpit has a valid certificate without making any changes. </p>
<p> <code>&#8211;ensure</code> Ensure that a certificate exists and can be loaded. Certificate will be created if it does not already exist. </p>
<p> <code>&#8211;user username</code> The unix user that should own the certificate. Only takes effect if used with <code>&#8211;ensure</code>. </p>
<p> <code>&#8211;group groupname</code> The unix group that should read the certificate. Only takes effect if used with <code>&#8211;ensure</code>. </p>
<p> If any additional arguments are given, they are treated as files that should be combined to create a certificate file. If the combined files validate, they will be saved in the appropriate location using the name of the first file given with the extension changed to .cert. For example: </p>
<p> <code>remotectl certificate server.pem chain.pem key.pem</code> </p>
<p> will result in server.cert. If server.cert already exists it will be overwritten.</dl>
<h2>Options</h2>
<p><code>&#8211;help</code></p>
<dl>
<dd>Show help options.</dl>
<p> <code>&#8211;verbose</code></p>
<dl>
<dd>Print verbose messages about the task</dl>
<h2>Bugs</h2>
<p>Please send bug reports to either the distribution bug tracker or the m[blue]<code>upstream bug tracker</code>m[]<font SIZE="-2">[1]</font>.</p>
<h2>Author</h2>
<p>Cockpit has been written by many m[blue]<code>contributors</code>m[]<font SIZE="-2">[2]</font>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-cockpit-ws/">cockpit-ws</a></code>(8)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>upstream bug tracker</p>
<dl>
<dd><a rel="nofollow" href="https://github.com/cockpit-project/cockpit/issues/new">https://github.com/cockpit-project/cockpit/issues/new</a></dl>
<dt> 2.</p>
<dd>contributors</p>
<dl>
<dd><a rel="nofollow" href="https://github.com/cockpit-project/cockpit/">https://github.com/cockpit-project/cockpit/</a></dl>
