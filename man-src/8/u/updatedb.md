---
title: "updatedb(8)"
name: "updatedb"
section: "8"
letter: "u"
url: "/docs/linux/man/8-updatedb/"
description: "updatedb – update a database for mlocate"
---

<p>updatedb &#8211; update a database for mlocate</p>
<h2>Synopsis</h2>
<p><code>updatedb</code> [<i>OPTION</i>]&#8230; </p>
<h2>Description</h2>
<p><code>updatedb</code> creates or updates a database used by <code><a href="/docs/linux/man/1-locate/">locate</a></code>(1). If the database already exists, its data is reused to avoid rereading directories that have not changed. <code>updatedb</code> is usually run daily by <code><a href="/docs/linux/man/8-cron/">cron</a></code>(8) to update the default database. </p>
<h2>Exit Status</h2>
<p><code>updatedb</code> returns with exit status 0 on success, 1 on error.</p>
<h2>Options</h2>
<p>The <code>PRUNE_BIND_MOUNTS</code>, <code>PRUNEFS</code>, <code>PRUNENAMES</code> and <code>PRUNEPATHS</code> variables, which are modified by some of the options, are documented in detail in <code><a href="/docs/linux/man/5-updatedb-conf/">updatedb.conf</a></code>(5). </p>
<dl>
<dt><code>-f</code>, <code>&#8211;add-prunefs </code><i>FS</i></p>
<dd>Add entries in white-space-separated list <i>FS</i> to <code>PRUNEFS</code>. </p>
<dt><code>-n</code>, <code>&#8211;add-prunenames </code><i>NAMES</i></p>
<dd>Add entries in white-space-separated list <i>NAMES</i> to <code>PRUNENAMES</code>. </p>
<dt><code>-e</code>, <code>&#8211;add-prunepaths </code><i>PATHS</i></p>
<dd>Add entries in white-space-separated list <i>PATHS</i> to <code>PRUNEPATHS</code>. </p>
<dt><code>-U</code>, <code>&#8211;database-root</code> <i>PATH</i></p>
<dd>Store only results of scanning the file system subtree rooted at <i>PATH</i> to the generated database. The whole file system is scanned by default. </p>
<p> <code><a href="/docs/linux/man/1-locate/">locate</a></code>(1) outputs entries as absolute path names which don&#8217;t contain symbolic links, regardless of the form of <i>PATH</i>. </p>
<dt><code>&#8211;debug-pruning</code></p>
<dd>Write debugging information about pruning decisions to standard error output. </p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Write a summary of the available options to standard output and exit successfully. </p>
<dt><code>-o</code>, <code>&#8211;output</code> <i>FILE</i></p>
<dd>Write the database to <i>FILE</i> instead of using the default database. </p>
<dt><code>&#8211;prune-bind-mounts</code> <i>FLAG</i></p>
<dd>Set <code>PRUNE_BIND_MOUNTS</code> to <i>FLAG</i>, overriding the configuration file. </p>
<dt><code>&#8211;prunefs</code> <i>FS</i></p>
<dd>Set <code>PRUNEFS</code> to <i>FS</i>, overriding the configuration file. </p>
<dt><code>&#8211;prunenames</code> <i>NAMES</i></p>
<dd>Set <code>PRUNENAMES</code> to <i>NAMES</i>, overriding the configuration file. </p>
<dt><code>&#8211;prunepaths</code> <i>PATHS</i></p>
<dd>Set <code>PRUNEPATHS</code> to <i>PATHS</i>, overriding the configuration file. </p>
<dt><code>-l</code>, <code>&#8211;require-visibility</code> <i>FLAG</i></p>
<dd>Set the &#8220;require file visibility before reporting it&#8221; flag in the generated database to <i>FLAG</i>. </p>
<p> If <i>FLAG</i> is <code>0</code> or <code>no</code>, or if the database file is readable by &quot;others&quot; or it is not owned by <code>mlocate</code>, <code><a href="/docs/linux/man/1-locate/">locate</a></code>(1) outputs the database entries even if the user running <code><a href="/docs/linux/man/1-locate/">locate</a></code>(1) could not have read the directory necessary to find out the file described by the database entry. </p>
<p> If <i>FLAG</i> is <code>1</code> or <code>yes</code> (the default), <code><a href="/docs/linux/man/1-locate/">locate</a></code>(1) checks the permissions of parent directories of each entry before reporting it to the invoking user. To make the file existence truly hidden from other users, the database group is set to <code>mlocate</code> and the database permissions prohibit reading the database by users using other means than <code><a href="/docs/linux/man/1-locate/">locate</a></code>(1), which is set-gid <code>mlocate</code>. </p>
<p> Note that the visibility flag is checked only if the database is owned by <code>mlocate</code> and it is not readable by &quot;others&quot;. </p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Output path names of files to standard output, as soon as they are found. </p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Write information about the version and license of <code>locate</code> on standard output and exit successfully. </p>
</dl>
<h2>Examples</h2>
<p>To create a private mlocate database as an user other than <code>root</code>, run</p>
<dl>
<dd><code>updatedb -l 0 -o</code> <i>db_file</i> <code>-U</code> <i>source_directory</i></dl>
<p> Note that all users that can read <i>db_file</i> can get the complete list of files in the subtree of <i>source_directory</i>. </p>
<h2>Files</h2>
<dl>
<dt><code>/etc/updatedb.conf</code></p>
<dd>A configuration file. See <code><a href="/docs/linux/man/5-updatedb-conf/">updatedb.conf</a></code>(5). </p>
<dt><code>/var/lib/mlocate/mlocate.db</code></p>
<dd>The database updated by default. </p>
</dl>
<h2>Security</h2>
<p>Databases built with <code>&#8211;require-visibility no</code> allow users to find names of files and directories of other users, which they would not otherwise be able to do.</p>
<h2>Notes</h2>
<p>The accompanying <code><a href="/docs/linux/man/1-locate/">locate</a></code>(1) utility was designed to be compatible to <code>slocate</code> and attempts to be compatible to <font SIZE="-1">GNU</font> <code>locate</code> where possible. This is not the case for <code>updatedb</code>. </p>
<h2>Author</h2>
<p>Miloslav Trmac &lt;mitr [at] redhat.com&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-locate/">locate</a></code>(1), <code><a href="/docs/linux/man/5-mlocate-db/">mlocate.db</a></code>(5), <code><a href="/docs/linux/man/5-updatedb-conf/">updatedb.conf</a></code>(5) </p>
