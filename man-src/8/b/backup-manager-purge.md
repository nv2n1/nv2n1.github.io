---
title: "backup-manager-purge(8)"
name: "backup-manager-purge"
section: "8"
letter: "b"
url: "/docs/linux/man/8-backup-manager-purge/"
description: "backup-manager-purge – backup-manager’s wrapper for outdating files"
---

<p>backup-manager-purge &#8211; backup-manager&#8217;s wrapper for outdating files</p>
<h2>Synopsis</h2>
<p>backup-manager-purge [<font SIZE="-1">TTL</font>] &lt;options&gt;</p>
<h2>Description</h2>
<p><code>backup-manager-purge</code> is the only authorized entity that can say if an archive should be purged or not. Any tasks used by backup-manager may have to know if an archive is deprecated (eg: the purging phase of an upload method). This tool is here to fulfill that need. </p>
<p> Given a <i>time to live (</i><font SIZE="-1"><i>TTL</i></font><i>)</i> and a list of archives, <code>backup-manager-purge</code> will return another list of archives, corresponding to the ones that are outdated by the <font SIZE="-1">TTL. </font></p>
<h2>Required Args</h2>
<dl>
<dt><code>&#8211;ttl=</code><i>time-to-live</i></p>
<dd>Specify the time to live (in days) for the archives. Any archive that is older than <i>ttl</i> days will be outdated.</dl>
<h2>Optional Args</h2>
<dl>
<dt><code>&#8211;files-from=</code>file</p>
<dd>A file containing a list of archives to parse, one archive per line. If this option is not used, <font SIZE="-1">STDIN</font> will be used for catching the files to parse.</dl>
<h2>Return</h2>
<p><code>backup-manager-purge</code> will return the list of outdated files on <font SIZE="-1">STDOUT,</font> one file per line.</p>
<h2>Error Codes</h2>
<p>If an error occurs, it will print the error message on stderr and will exit with an error code greater than 0. </p>
<p> Here are the possible error codes:</p>
<dl>
<dt>bad command line (wrong arguments) : 10</p>
<dd>
<dt>internal error (should be reported as a bug) : 20</p>
<dd></dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-backup-manager/">backup-manager</a></i>(8) <i><a href="/docs/linux/man/8-backup-manager-upload/">backup-manager-upload</a></i>(8)</p>
<h2>Authors</h2>
<p>Concept and design by Alexis Sukrieh and Jan Metzger.</p>
