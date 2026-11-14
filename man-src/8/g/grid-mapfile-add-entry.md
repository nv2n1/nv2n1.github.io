---
title: "grid-mapfile-add-entry(8)"
name: "grid-mapfile-add-entry"
section: "8"
letter: "g"
url: "/docs/linux/man/8-grid-mapfile-add-entry/"
description: "grid-mapfile-add-entry – Add an entry to a gridmap file"
---

<p>grid-mapfile-add-entry &#8211; Add an entry to a gridmap file</p>
<h2>Synopsis</h2>
<p><code>grid-mapfile-add-entry</code> [ -h | -help | -usage | -version | -versions ] </p>
<p> <code>grid-mapfile-add-entry</code> -dn <i>DISTINGUISHED-NAME</i> -ln <i>LOCAL-NAME</i>&#8230; [-d | -dryrun] [ -f <i>MAPFILE</i> | -mapfile <i>MAPFILE</i> ] [ -n ] [ -c ]</p>
<h2>Description</h2>
<p>The <code>grid-mapfile-add-entry</code> program adds a new mapping from an X.509 distinguished name to a local POSIX user name to a gridmap file. Gridmap files are used as a simple authorization method for services such as GRAM5 or GridFTP. </p>
<p> The <code>grid-mapfile-add-entry</code> program verifies that the <i>LOCAL-NAME</i> is a valid user name on the system on which it was run, and that the mapping between <i>DISTINGUISHED-NAME</i> and <i>LOCAL-NAME</i> does not already exist in the gridmap file. </p>
<p> By default, <code>grid-mapfile-add-entry</code> will modify the gridmap file named by the GRIDMAP environment variable if present, or the file /etc/grid-security/grid-mapfile if not. This can be changed by the use of the <i>-mapfile</i> or <i>-f</i> command-line options. </p>
<p> If the gridmap file does not exist, <code>grid-mapfile-add-entry</code> will create it. If it already exists, <code>grid-mapfile-add-entry</code> will save the current contents of the file to a new file with the string .old appended to the file name. </p>
<p> The full set of command-line options to <code>grid-mapfile-add-entry</code> are: </p>
<p> <code>-help, -usage</code></p>
<dl>
<dd>Display the command-line options to <code>grid-mapfile-add-entry</code>.</dl>
<p> <code>-version, -versions</code></p>
<dl>
<dd>Display the version number of the <code>grid-mapfile-add-entry</code> command. The second form includes more details.</dl>
<p> <code>-dn </code><i>DISTINGUISHED-NAME</i></p>
<dl>
<dd>The X.509 distinguished name to add a mapping for. The name should be in OpenSSL&#8217;s oneline format.</dl>
<p> <code>-ln </code><i>LOCAL-NAME</i><code>&#8230;</code></p>
<dl>
<dd>The POSIX user name to map the distinguished name to. This name must be a valid username. Add multiple <i>LOCAL-NAME</i> strings after the <i>-ln</i> command-line option. If any of the local names are invalid, no changes will be made to the gridmap file.</dl>
<p> <code>-d, -dryrun</code></p>
<dl>
<dd>Verify local names and display diagnostics about what would be added to the gridmap file, but don&#8217;t actually modify the file.</dl>
<p> <code>-mapfile </code><i>MAPFILE</i><code>, -f </code><i>MAPFILE</i></p>
<dl>
<dd>Modify the gridmap file named by <i>MAPFILE</i> instead of the default.</dl>
<p> <code>-n</code></p>
<dl>
<dd>Don&#8217;t copy the original file to <i>MAPFILE</i>.old.</dl>
<p> <code>-c</code></p>
<dl>
<dd>Don&#8217;t check for changes to the gridmap during program execution.</dl>
<h2>Examples</h2>
<p>Add a mapping between the current user&#8217;s certificate to the current user id to a gridmap file in $HOME/.gridmap: </p>
<dl>
<dd>
<pre>% grid-mapfile-add-entry -f $HOME/.gridmap -dn &quot;`grid-cert-info -subject`&quot; -ln &quot;`id -un`&quot;
Modifying /home/juser/.gridmap ...
/home/juser/.gridmap does not exist... Attempting to create /home/juser/.gridmap
New entry:
&quot;/DC=org/DC=example/DC=grid/CN=Joe User&quot; juser
(1) entry added</pre>
</dl>
<p> Add a mapping between the a distinguished name and multiple local names: </p>
<dl>
<dd>
<pre>% grid-mapfile-add-entry -dn &quot;/DC=org/DC=example/DC=grid/CN=Joe User&quot; juser&quot; local1 local2
Modifying /home/juser/.gridmap ...
/home/juser/.gridmap does not exist... Attempting to create /home/juser/.gridmap
New entry:
&quot;/DC=org/DC=example/DC=grid/CN=Joe User&quot; local1,local2
(1) entry added</pre>
</dl>
<h2>Environment</h2>
<p>The following environment variables affect the execution of <code>grid-mapfile-add-entry</code>: </p>
<p> GRIDMAP</p>
<dl>
<dd>Path to the default gridmap to modify</dl>
<h2>Files</h2>
<p>The following files affect the execution of <code>grid-mapfile-add-entry</code>: </p>
<p> /etc/grid-security/grid-mapfile</p>
<dl>
<dd>Path to the default gridmap to modify if GRIDMAP environment variable is not set.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-grid-mapfile-check-consistency/">grid-mapfile-check-consistency</a>(8), <a href="/docs/linux/man/8-grid-mapfile-delete-entry/">grid-mapfile-delete-entry</a>(8)</p>
<h2>Author</h2>
<p>Copyright &#169; 1999-2016 University of Chicago</p>
