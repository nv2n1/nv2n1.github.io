---
title: "kproplog(8)"
name: "kproplog"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kproplog/"
description: "kproplog – display the contents of the Kerberos principal update log"
---

<p>kproplog &#8211; display the contents of the Kerberos principal update log</p>
<h2>Synopsis</h2>
<p><code>kproplog</code> [<code>-h</code>] [<code>-e</code> <i>num</i>] [-v] <code>kproplog</code> [-R]</p>
<h2>Description</h2>
<p>The kproplog command displays the contents of the KDC database update log to standard output. It can be used to keep track of incremental updates to the principal database. The update log file contains the update log maintained by the <i><a href="/docs/linux/man/8-kadmind/">kadmind</a>(8)</i> process on the master KDC server and the <i><a href="/docs/linux/man/8-kpropd/">kpropd</a>(8)</i> process on the slave KDC servers. When updates occur, they are logged to this file. Subsequently any KDC slave configured for incremental updates will request the current data from the master KDC and update their log file with any updates returned. </p>
<p> The kproplog command requires read access to the update log file. It will display update entries only for the KDC it runs on. </p>
<p> If no options are specified, kproplog displays a summary of the update log. If invoked on the master, kproplog also displays all of the update entries. If invoked on a slave KDC server, kproplog displays only a summary of the updates, which includes the serial number of the last update received and the associated time stamp of the last update.</p>
<h2>Options</h2>
<dl>
<dt><code>-R</code></p>
<dd>Reset the update log. This forces full resynchronization. If used on a slave then that slave will request a full resync. If used on the master then all slaves will request full resyncs.</p>
<dt><code>-h</code></p>
<dd>Display a summary of the update log. This information includes the database version number, state of the database, the number of updates in the log, the time stamp of the first and last update, and the version number of the first and last update entry.</p>
<dt><code>-e</code> <i>num</i></p>
<dd>Display the last <i>num</i> update entries in the log. This is useful when debugging synchronization between KDC servers.</p>
<dt><code>-v</code></p>
<dd>Display individual attributes per update. An example of the output generated for one entry: </p>
<pre>Update Entry
 Update serial # : 4
 Update operation : Add
 Update principal : test [at] EXAMPLE.COM
 Update size : 424
 Update committed : True
 Update time stamp : Fri Feb 20 23:37:42 2004
 Attributes changed : 6
 Principal
 Key data
 Password last changed
 Modifying principal
 Modification time
 TL data</pre>
</dl>
<h2>Environment</h2>
<p>kproplog uses the following environment variables:</p>
<dl>
<dt>&bull;</p>
<dd><code>KRB5_KDC_PROFILE</code></dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-kpropd/">kpropd</a>(8)</i></p>
<h2>Author</h2>
<p>MIT</p>
<h2>Copyright</h2>
<p>1985-2016, MIT</p>
