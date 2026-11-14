---
title: "grid-mapfile-check-consistency(8)"
name: "grid-mapfile-check-consistency"
section: "8"
letter: "g"
url: "/docs/linux/man/8-grid-mapfile-check-consistency/"
description: "grid-mapfile-check-consistency – Add an entry to a grid map file"
---

<p>grid-mapfile-check-consistency &#8211; Add an entry to a grid map file</p>
<h2>Synopsis</h2>
<p><code>grid-mapfile-check-consistency</code> [ -h | -help | -usage | -version | -versions ] </p>
<p> <code>grid-mapfile-check-consistency</code> [ -mapfile <i>MAPFILE</i> | -f <i>MAPFILE</i> ]</p>
<h2>Description</h2>
<p>The <code>grid-mapfile-check-consistency</code> program performs basic checks for validity of a gridmap file. These checks include checks for existence, duplication of entries, and valid local user names. If the gridmap file is valid, <code>grid-mapfile-check-consistency</code> exits with a zero exit code, otherwise it exits with a non-zero exit code. In either case, it displays information about its progress as it parses and validates the gridmap file. </p>
<p> By default, <code>grid-mapfile-check-consistency</code> will check the gridmap file named by the GRIDMAP environment variable if present. If that variable is not set, it will check the file $HOME/.gridmap for non-root users if present. If that doesn&#8217;t exist or <code>grid-mapfile-check-consistency</code> is run as root, it will then check /etc/grid-security/grid-mapfile. This can be changed by the use of the <i>-mapfile</i> or <i>-f</i> command-line options. </p>
<p> The full set of command-line options to <code>grid-mapfile-check-consistency</code> are: </p>
<p> <code>-h, -help, -usage</code></p>
<dl>
<dd>Display the command-line options to <code>grid-mapfile-check-consistency</code>.</dl>
<p> <code>-version, -versions</code></p>
<dl>
<dd>Display the version number of the <code>grid-mapfile-check-consistency</code> command.</dl>
<p> <code>-mapfile </code><i>MAPFILE</i><code>, -f </code><i>MAPFILE</i></p>
<dl>
<dd>Check the gridmap file named by <i>MAPFILE</i> instead of the default.</dl>
<h2>Examples</h2>
<p>Check that the gridmap file in /etc/grid-security is valid: </p>
<dl>
<dd>
<pre>% grid-mapfile-check-consistency* -f /etc/grid-security/grid-mapfile
Checking /etc/grid-security/grid-mapfile
Verifying grid mapfile existence...OK
Checking for duplicate entries...OK
Checking for valid user names...OK</pre>
</dl>
<p> Check a gridmap file that has an invalid local user name: </p>
<dl>
<dd>
<pre>grid-mapfile-check-consistency -f /etc/grid-security/grid-mapfile
Checking /etc/grid-security/grid-mapfile
Verifying grid mapfile existence...OK
Checking for duplicate entries...OK
ERROR: baduser is not a valid local username
ERROR: Found 1 invalid username(s)</pre>
</dl>
<h2>Environment</h2>
<p>The following environment variables affect the execution of <code>grid-mapfile-check-consistency</code>: </p>
<p> <code>GRIDMAP</code></p>
<dl>
<dd>Path to the gridmap to check.</dl>
<h2>Files</h2>
<p>The following files affect the execution of <code>grid-mapfile-check-consistency</code>: </p>
<p> <code>$HOME/.gridmap</code></p>
<dl>
<dd>Path to the default gridmap to check if the GRIDMAP environment variable is not set for non-root users.</dl>
<p> <code>/etc/grid-security/grid-mapfile</code></p>
<dl>
<dd>Path to the default gridmap to check if GRIDMAP environment variable is not set and the above file does not exist.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-grid-mapfile-add-entry/">grid-mapfile-add-entry</a>(8), <a href="/docs/linux/man/8-grid-mapfile-delete-entry/">grid-mapfile-delete-entry</a>(8)</p>
<h2>Author</h2>
<p>Copyright &#169; 1999-2016 University of Chicago</p>
