---
title: "owncloudcmd(1)"
name: "owncloudcmd"
section: "1"
letter: "o"
url: "/docs/linux/man/1-owncloudcmd/"
description: "owncloudcmd – Command line ownCloud client tool."
---

<h2>NAME</h2>
<p> owncloudcmd &#8211; Command line ownCloud client tool.</p>
<h2>SYNOPSIS</h2>
<p> <i>owncloudcmd</i> [<i>OPTIONS</i>&#8230;] sourcedir owncloudurl</p>
<h2>DESCRIPTION</h2>
<p> owncloudcmd is the command line tool used for the ownCloud file synchronization desktop utility. </p>
<p> Contrary to the <i><a href="/docs/linux/man/1-owncloud/">owncloud</a>(1)</i> GUI client, <i>owncloudcmd</i> only performs a single sync run and then exits. In so doing, <i>owncloudcmd</i> replaces the <i>ocsync</i> binary used for the same purpose in earlier releases. </p>
<p> A <i>sync run</i> synchronizes a single local directory using a WebDAV share on a remote ownCloud server. </p>
<p> To invoke the command line client, provide the local and the remote repository: The first parameter is the local directory. The second parameter is the server URL. </p>
<p> <code>NOTE:</code> Prior to the 1.6 release of owncloudcmd, the tool only accepted <code>owncloud://</code> or <code>ownclouds://</code> in place of <code>http://</code> and <code>https://</code> as a scheme. See <code>Examples</code> for details.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;user</code>, <code>-u</code> <code>[user]</code></p>
<dd> Use <code>user</code> as the login name.</p>
<dt><code>&#8211;password</code>, <code>-p</code> <code>[password]</code></p>
<dd> Use <code>password</code> as the password.</p>
<dt><code>-n</code></p>
<dd> Use <code>netrc (5)</code> for login.</p>
<dt><code>&#8211;non-interactive</code></p>
<dd> Do not prompt for questions.</p>
<dt><code>&#8211;silent</code>, <code>&#8211;s</code></p>
<dd> Inhibits verbose log output.</p>
<dt><code>&#8211;trust</code></p>
<dd> Trust any SSL certificate, including invalid ones.</p>
<dt><code>&#8211;httpproxy <a rel="nofollow" href="http://[user@pass:]">http://[user@pass:]</a>&lt;server&gt;:&lt;port&gt;</code></p>
<dd> Uses <code>server</code> as HTTP proxy.</p>
<dt><code>&#8211;nonshib</code></p>
<dd> Uses Non Shibboleth WebDAV Authentication</p>
<dt><code>&#8211;davpath [path]</code></p>
<dd> Overrides the WebDAV Path with <code>path</code></p>
<dt><code>&#8211;exclude [file]</code></p>
<dd> Exclude list file</p>
<dt><code>&#8211;unsyncedfolders [file]</code></p>
<dd> File containing the list of unsynced folders (selective sync)</p>
<dt><code>&#8211;max-sync-retries [n]</code></p>
<dd> Retries maximum n times (defaults to 3)</p>
<dt><code>-h</code></p>
<dd> Sync hidden files,do not ignore them</dl>
<h2>EXAMPLE</h2>
<p> To synchronize the ownCloud directory <code>Music</code> to the local directory <code>media/music</code> through a proxy listening on port <code>8080</code> on the gateway machine <code>192.168.178.1</code>, the command line would be: </p>
<pre>
$ owncloudcmd --httpproxy <a rel="nofollow" href="http://192.168.178.1:8080">http://192.168.178.1:8080</a> \
              $HOME/media/music \
              <a rel="nofollow" href="https://server/owncloud/remote.php/webdav/Music">https://server/owncloud/remote.php/webdav/Music</a>
</pre>
<p> <code>owncloudcmd</code> will enquire user name and password, unless they have been specified on the command line or <code>-n</code> (see <i><a href="/docs/linux/man/5-netrc/">netrc</a>(5)</i>) has been passed. </p>
<p> Using the legacy scheme, it would be: </p>
<pre>
$ owncloudcmd --httpproxy <a rel="nofollow" href="http://192.168.178.1:8080">http://192.168.178.1:8080</a> \
              $HOME/media/music \
              ownclouds://server/owncloud/remote.php/webdav/Music
</pre>
<h2>BUGS</h2>
<p> Please report bugs at <i><a rel="nofollow" href="https://github.com/owncloud/client/issues">https://github.com/owncloud/client/issues</a></i>.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-owncloud/">owncloud</a>(1)</i></p>
<h2>AUTHOR</h2>
<p> The ownCloud developers</p>
<h2>COPYRIGHT</h2>
<p> 2013-2016, The ownCloud developers </p>
<h2>Index</h2>
