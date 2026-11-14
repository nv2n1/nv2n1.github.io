---
title: "git-instaweb(1)"
name: "git-instaweb"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-instaweb/"
description: "git-instaweb – Instantly browse your working repository in gitweb"
---

<h2 class="name">NAME</h2>
<p> git-instaweb &#8211; Instantly browse your working repository in gitweb </p>
<h2>SYNOPSIS</h2>
<pre><code>
git instaweb[--local][--httpd = &lt;httpd&gt;][--port = &lt;port&gt;]
            [--browser = &lt;browser&gt;] git instaweb[--start][--stop][--restart]
</code></pre>
<h2>DESCRIPTION</h2>
<p> A simple script to set up <code>gitweb</code> and a web server for browsing the local repository.</p>
<h2>OPTIONS</h2>
<p> -l, &#8211;local</p>
<dl>
<dt>
<dd> Only bind the web server to the local IP (127.0.0.1).</dl>
<p> -d, &#8211;httpd</p>
<dl>
<dt>
<dd> The HTTP daemon command-line that will be executed. Command-line options may be specified here, and the configuration file will be added at the end of the command-line. Currently apache2, lighttpd, mongoose, plackup, python and webrick are supported. (Default: lighttpd)</dl>
<p> -m, &#8211;module-path</p>
<dl>
<dt>
<dd> The module path (only needed if httpd is Apache). (Default: /usr/lib/apache2/modules)</dl>
<p> -p, &#8211;port</p>
<dl>
<dt>
<dd> The port number to bind the httpd to. (Default: 1234)</dl>
<p> -b, &#8211;browser</p>
<dl>
<dt>
<dd> The web browser that should be used to view the gitweb page. This will be passed to the <i>git web&#8211;browse</i> helper script along with the URL of the gitweb instance. See <code><a href="/docs/linux/man/1-git-web--browse/">git-web&#8211;browse</a></code>(1) for more information about this. If the script fails, the URL will be printed to stdout.</dl>
<p> start, &#8211;start</p>
<dl>
<dt>
<dd> Start the httpd instance and exit. Regenerate configuration files as necessary for spawning a new instance.</dl>
<p> stop, &#8211;stop</p>
<dl>
<dt>
<dd> Stop the httpd instance and exit. This does not generate any of the configuration files for spawning a new instance, nor does it close the browser.</dl>
<p> restart, &#8211;restart</p>
<dl>
<dt>
<dd> Restart the httpd instance and exit. Regenerate configuration files as necessary for spawning a new instance.</dl>
<h2>CONFIGURATION</h2>
<p> You may specify configuration in your .git/config </p>
<dl>
<dt>
<dd>
<pre>
[instaweb]
        local = true
        httpd = apache2 -f
        port = 4321
        browser = konqueror
        modulePath = /usr/lib/apache2/modules
</pre>
</dl>
<p> If the configuration variable <code>instaweb.browser</code> is not set, <code>web.browser</code> will be used instead if it is defined. See <code><a href="/docs/linux/man/1-git-web--browse/">git-web&#8211;browse</a></code>(1) for more information about this.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gitweb/">gitweb</a></code>(1)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
