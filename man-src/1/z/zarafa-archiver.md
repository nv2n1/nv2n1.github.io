---
title: "zarafa-archiver(1)"
name: "zarafa-archiver"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zarafa-archiver/"
description: "zarafa-archiver – Manages zarafa archives and performs the archive operation."
---

<h2 class="name">NAME</h2>
<p> zarafa-archiver &#8211; Manages zarafa archives and performs the archive operation. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>zarafa-archiver</code> [<i>OPTION</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>This tool is used to attach or detach archives to a users store. An archive is defined as a special non-active store or a folder inside such a store. </p>
<p> On top of managing archives, this tool is used to perform the actual archive operation. Using the <i>-u</i> option, the archiver can be instructed to archive a single store or all stores.</p>
<h2>ACTIONS</h2>
<p> zarafa-archiver needs an action command with the appropriate options. Valid actions are: </p>
<p> <code>-l</code>, <code>&#8211;list</code></p>
<dl>
<dt>
<dd> List archives for the specified user. The <i>-u</i> option is required.</dl>
<p> <code>-L</code>, <code>&#8211;list-archiveusers</code></p>
<dl>
<dt>
<dd> List users that have an archive attached.</dl>
<p> <code>-A</code>, <code>&#8211;archive</code></p>
<dl>
<dt>
<dd> Perform an archive run. If a <i>-u</i> option is provided, only the store of one user will be archived. Otherwise all stores are archived. Optionally the <i>&#8211;local-only</i> option can be set to only archive stores that exist on the server to which zarafa-archiver is connected (usualy the local server).</dl>
<p> <code>-C</code>, <code>&#8211;cleanup</code></p>
<dl>
<dt>
<dd> Perform an archive cleanup run. If a <i>-u</i> option is provided, only the archives of one user will be cleaned. Otherwise all stores are cleaned. Optionally the <i>&#8211;local-only</i> option can be set to only cleanup archives of users that have their primary store on the server to which zarafa-archiver is connected (usualy the local server).</dl>
<p> <code>-a</code> <i>archive</i>, <code>&#8211;attach-to</code> <i>archive</i></p>
<dl>
<dt>
<dd> Attach an archive to the store of the user specified with the <i>-u</i> option. If no additional options are specified, a folder will be created in the archive store, which will act as the root of the archive for the user. The foldername will be set to the username of the user. This behavior can be changed by providing the <i>&#8211;archive-folder </i> or <i>&#8211;no-folder</i> option.</dl>
<p> <code>-d</code> <i>archive</i>, <code>&#8211;detach-from</code> <i>archive</i></p>
<dl>
<dt>
<dd> Detach an archive from the store of the user specified with the <i>-u</i> option. zarafa-archiver will automatically determine which folder to detach. However if a user has two archives in one archive store, zarafa-archiver won&#8217;t be able to tell which one needs to be detached. In this case the folder needs to be specified with the <i>&#8211;archive-folder</i> option.</dl>
<p> <code>-D</code> <i>archiveno</i>, <code>&#8211;detach</code> <i>archiveno</i></p>
<dl>
<dt>
<dd> Detach an archive from the store of the user specified with the <i>-u</i> option. The archive to detach is indicated by archiveno and can be obtained by running <code>zarafa-archiver</code><code>-u</code><i>username</i><code>-l</code></dl>
<p> <code>&#8211;auto-attach</code></p>
<dl>
<dt>
<dd> When no user is specified with -u, all users will have their archives attached or detached based on the LDAP/ADS settings. If a user is specified only that user&#8217;s store will be processed. This option can be combined with <i>-A</i> to force an auto-attach run regardless of the <i>enable_auto_attach</i> configuration option.</dl>
<h2>OPTIONS</h2>
<p> The options used by actions are as follows: </p>
<p> <code>-u</code> <i>username</i></p>
<dl>
<dt>
<dd> Use this parameter to specify a user on which store to perform the provided action.</dl>
<p> <code>&#8211;local-only</code></p>
<dl>
<dt>
<dd> If this option is passed when an archive run is started, only stores that exist on the server to which zarafa-archiver is connected will be archived.</dl>
<p> <code>&#8211;archive-folder</code> <i>foldername</i></p>
<dl>
<dt>
<dd> Use this option to force zarafa-archiver to create the archive folder with a different name than the username of the user for whom to attach an archive.</dl>
<p> <code>&#8211;archive-server</code> <i>serverpath</i></p>
<dl>
<dt>
<dd> Use this option to specify the path to the archive server. This is usefull when using the archiver in a non-multiserver setup.</dl>
<p> <code>&#8211;no-folder</code></p>
<dl>
<dt>
<dd> Use this option to force zarafa-archiver to create the root of the archive in the root of the archive store (IPM subtree). This way only one user store can be attached to an archive.</dl>
<p> <code>-w</code></p>
<dl>
<dt>
<dd> By default zarafa-archiver makes an archive read-only for the user. By passing this option, the user will get read/write permissions in the attached archive. </p>
<p> This will override the <i>auto_attach_writable </i> configuration options when auto attaching archives.</dl>
<p> <code>&#8211;writable</code> <i>yes|no</i></p>
<dl>
<dt>
<dd> Explicitly enable or disable write permissions when (auto) attaching archives. </p>
<p> This will override the <i>auto_attach_writable </i> configuration options when auto attaching archives.</dl>
<p> <code>-c</code> <i>file</i></p>
<dl>
<dt>
<dd> Select an alternate config file to be used by zarafa-archiver. </p>
<p> Default: <i>/etc/zarafa/archiver.cfg</i></dl>
<h2>EXAMPLES</h2>
<p> For attaching an archive: </p>
<p> <code>zarafa-archiver</code><code>-u</code><i>username</i><code>&#8211;attach-to</code><i>archive</i> </p>
<p> For attaching an archive with a custom archive name: </p>
<p> <code>zarafa-archiver</code><code>-u</code><i>username</i><code>&#8211;attach-to</code><i>archive</i><code>&#8211;archive-name</code><i>archivename</i> </p>
<p> For attaching an archive without an archive folder: </p>
<p> <code>zarafa-archiver</code><code>-u</code><i>username</i><code>&#8211;attach-to</code><i>archive</i><code>&#8211;no-folder</code> </p>
<p> For detaching an archive: </p>
<p> <code>zarafa-archiver</code><code>-u</code><i>username</i><code>&#8211;detach-from</code><i>archive</i> </p>
<p> For starting an archive run: </p>
<p> <code>zarafa-archiver</code><code>-A</code> </p>
<p> For starting an archive run for one user: </p>
<p> <code>zarafa-archiver</code><code>-u</code><i>username</i><code>-A</code> </p>
<p> For starting a cleanup run: </p>
<p> <code>zarafa-archiver</code><code>-C</code> </p>
<p> For starting an cleanup run for one user: </p>
<p> <code>zarafa-archiver</code><code>-u</code><i>username</i><code>-C</code></p>
<h2>AUTHOR</h2>
<p> Written by Zarafa.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-zarafa-server/">zarafa-server</a></code>(1)<code><a href="/docs/linux/man/5-zarafa-archiver-cfg/">zarafa-archiver.cfg</a></code>(5) </p>
<h2>Index</h2>
