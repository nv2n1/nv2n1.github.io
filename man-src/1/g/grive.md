---
title: "grive(1)"
name: "grive"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grive/"
description: "grive – Google Drive client for GNU/Linux"
---

<h2>NAME</h2>
<p> grive &#8211; Google Drive client for GNU/Linux </p>
<h2>SYNOPSIS</h2>
<p> <code>grive [OPTIONS]</code></p>
<h2>DESCRIPTION</h2>
<p> <i>Grive</i> is a Google Drive (online storage service) client for GNU/Linux systems. </p>
<p> It allows the synchronization of all your files on the cloud with a directory of your choice and the upload of new files to Google Drive. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-a</code>, <code>&#8211;auth</code></p>
<dd> Requests authorization token from Google</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> Enable debug level messages. Implies -V</p>
<dt><code>&#8211;dry-run</code></p>
<dd> Only detect which files need to be uploaded/downloaded, without actually performing changes</p>
<dt><code>-f, &#8211;force</code></p>
<dd> Forces <i>grive</i> to always download a file from Google Drive instead uploading it</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Produces help message</p>
<dt><code>&#8211;ignore</code> &lt;perl_regexp&gt;</p>
<dd> Ignore files with relative paths matching this Perl Regular Expression. Value is remembered for next runs.</p>
<dt><code>-l</code> &lt;filename&gt;, <code>&#8211;log</code> &lt;filename&gt;</p>
<dd> Write log output to <i>&lt;filename&gt;</i></p>
<dt><code>&#8211;log-http</code> &lt;filename_prefix&gt;</p>
<dd> Log all HTTP responses in files named <i>&lt;filename_prefix&gt;YYYY-MM-DD.HHMMSS.txt</i> for debugging</p>
<dt><code>&#8211;new-rev</code></p>
<dd> Create new revisions in server for updated files</p>
<dt><code>-p</code> &lt;root_path&gt;, <code>&#8211;path</code> &lt;root_path&gt;</p>
<dd> Set root sync directory to <i>&lt;root_path&gt;</i></p>
<dt><code>-s</code> &lt;subdir&gt;, <code>&#8211;dir</code> &lt;subdir&gt;</p>
<dd> Sync a single <i>&lt;subdir&gt;</i> subdirectory. Internally converted to an ignore regexp, remembered for next runs.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Displays program version</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd> Verbose mode. Enables more messages than usual. </p>
</dl>
<h2>AUTHORS</h2>
<p> Current maintainer is Vitaliy Filippov. </p>
<p> Original author was Nestal Wan. This manpage was written by José Luis Segura Lucas (josel.segura [at] gmx.es) </p>
<p> The full list of contributors may be found here <i><a rel="nofollow" href="http://yourcmc.ru/wiki/Grive2#Full_list_of_contributors">http://yourcmc.ru/wiki/Grive2#Full_list_of_contributors</a></i> </p>
<h2>REPORT BUGS</h2>
<p> <i><a rel="nofollow" href="https://github.com/vitalif/grive2/issues">https://github.com/vitalif/grive2/issues</a></i> <i><a rel="nofollow" href="https://groups.google.com/forum/?fromgroups#!forum/grive-devel">https://groups.google.com/forum/?fromgroups#!forum/grive-devel</a></i> </p>
<h2>Index</h2>
