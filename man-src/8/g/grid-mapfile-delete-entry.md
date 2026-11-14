---
title: "grid-mapfile-delete-entry(8)"
name: "grid-mapfile-delete-entry"
section: "8"
letter: "g"
url: "/docs/linux/man/8-grid-mapfile-delete-entry/"
description: "grid-mapfile-delete-entry – Remove entries from a gridmap file"
---

<p>grid-mapfile-delete-entry &#8211; Remove entries from a gridmap file</p>
<h2>Synopsis</h2>
<p><code>grid-mapfile-delete-entry</code> [ -help | -usage | -version | -versions ] </p>
<p> <code>grid-mapfile-delete-entry</code> -dn <i>DISTINGUISHED-NAME</i> -ln LOCAL-NAME&#8230; [ -d | -dryrun ] [ -mapfile MAPFILE | -f MAPFILE ]</p>
<h2>Description</h2>
<p>The <code>grid-mapfile-delete-entry</code> program deletes mappings from a gridmap file. If both the <i>-dn</i> and <i>-ln</i> options are specified, <code>grid-mapfile-delete-entry</code> removes entries which meet both criteria (remove entries mapping <i>DISTINGUISHED-NAME</i> to <i>LOCAL-NAME</i> for each <i>LOCAL-NAME</i> specified). If only <i>-dn</i> or <i>-ln</i> is specified <code>all</code> entries for the specified <i>DISTINGUISHED-NAME</i> or <i>LOCAL-NAME</i> are removed. </p>
<p> By default, <code>grid-mapfile-delete-entry</code> will modify the gridmap file named by the GRIDMAP environment variable if present, or the file /etc/grid-security/grid-mapfile if not. This can be changed by the use of the <i>-mapfile</i> or &#8216;-f command-line options. </p>
<p> Prior to modifying a gridmap file, <code>grid-mapfile-delete-entry</code> saves its current contents to a file with the string .old appended to the original file name. </p>
<p> The full set of command-line options to <code>grid-mapfile-delete-entry</code> are: </p>
<p> <code>-help, -usage</code></p>
<dl>
<dd>Display the command-line options to <code>grid-mapfile-delete-entry</code>.</dl>
<p> <code>-version, -versions</code></p>
<dl>
<dd>Display the version number of the <code>grid-mapfile-delete-entry</code> command. The second form includes more details.</dl>
<p> <code>-dn DISTINGUISHED-NAME</code></p>
<dl>
<dd>The X.509 distinguished name to remove from the gridmap file. If the <i>-ln</i> option is not specified, remove all entries for this name; otherwise, remove entries that match both this name and the local name. The name should be in OpenSSL&#8217;s oneline format.</dl>
<p> <code>-ln LOCAL-NAME&#8230;</code></p>
<dl>
<dd>The POSIX user name to remove from the gridmap file. Include multiple <i>LOCAL-NAME</i> strings after the <i>-ln</i> command-line option to remove multiple names from the gridmap. If the <i>-dn</i> option is not specifeid, remove all entries for these names; otherwise, remove entries that match the <i>DISTINGUISHED-NAME</i> and any of the <i>LOCAL-NAME</i> values.</dl>
<p> <code>-d, -dryrun</code></p>
<dl>
<dd>Display diagnostics about what would be removed from the gridmap file, but don&#8217;t actually modify the file.</dl>
<p> <code>-mapfile MAPFILE, -f MAPFILE</code></p>
<dl>
<dd>Modify the gridmap file named by <i>MAPFILE</i> instead of the default.</dl>
<h2>Examples</h2>
<p>Remove all mappings for a distinguished name: </p>
<dl>
<dd>
<pre>% grid-mapfile-delete-entry &quot;/DC=org/DC=example/DC=grid/CN=Joe User&quot;
Modifying /etc/grid-security/grid-mapfile ...
Deleting entry: &quot;/DC=org/DC=example/DC=grid/CN=Joe User&quot; juser,juser2
(1) entry deleted</pre>
</dl>
<p> Remove the mapping between a distinguished name and a single local username: </p>
<dl>
<dd>
<pre>% grid-mapfile-delete-entry &quot;/DC=org/DC=example/DC=grid/CN=Joe User&quot; -ln juser2
Modifying /etc/grid-security/grid-mapfile ...
Current entry: &quot;/DC=org/DC=example/DC=grid/CN=Joe User&quot; juser
(1) mapping removed: (juser2), (0) not present and ignored
(0) entries deleted</pre>
</dl>
<h2>Environment</h2>
<p>The following environment variables affect the execution of <code>grid-mapfile-delete-entry</code>: </p>
<p> <code>GRIDMAP</code></p>
<dl>
<dd>Path to the gridmap to modify.</dl>
<h2>Files</h2>
<p>The following files affect the execution of <code>grid-mapfile-delete-entry</code>: </p>
<p> <code>/etc/grid-security/grid-mapfile</code></p>
<dl>
<dd>Path to the default gridmap to modify if GRIDMAP environment variable is not set.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-grid-mapfile-add-entry/">grid-mapfile-add-entry</a>(8), <a href="/docs/linux/man/8-grid-mapfile-check-consistency/">grid-mapfile-check-consistency</a>(8)</p>
<h2>Author</h2>
<p>Copyright &#169; 1999-2016 University of Chicago</p>
