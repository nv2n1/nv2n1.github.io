---
title: "gpodder-backup(1)"
name: "gpodder-backup"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpodder-backup/"
description: "gpodder-backup – Backup and restore utility for gPodder user data"
---

<h2>NAME</h2>
<p> gpodder-backup &#8211; Backup and restore utility for gPodder user data</p>
<h2>SYNOPSIS</h2>
<p> <code>gpodder-backup</code> [<i>&#8211;create|&#8211;extract</i>] <i>&lt;archive.gpo.tar.gz&gt; </i>[<i>options</i>] <code>gpodder-backup</code> <i>&#8211;purge</i></p>
<h2>DESCRIPTION</h2>
<p> This utility can be used to create a dump of the current gPodder data (configuration files + downloads), optionally skipping the real contents of the download folder (for submitting your data to a bug report without having to transfer lots of data).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> show program&#8217;s version number and exit</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help message and exit</p>
<dt><code>-c</code> &lt;FILE&gt;, <code>&#8211;create=</code>&lt;FILE&gt;</p>
<dd> Create a new archive</p>
<dt><code>-x</code> &lt;FILE&gt;, <code>&#8211;extract=</code>&lt;FILE&gt;</p>
<dd> Extract an existing archive</p>
<dt><code>-f</code>, <code>&#8211;fake-downloads</code></p>
<dd> Do not store contents of downloaded files</p>
<dt><code>-n</code>, <code>&#8211;no-covers</code></p>
<dd> Do not include cover files in archive</p>
<dt><code>-D</code> &lt;DIR&gt;, <code>&#8211;destination=</code>&lt;DIR&gt;</p>
<dd> Extract downloads in different folder</p>
<dt><code>-P</code>, <code>&#8211;purge</code></p>
<dd> Remove current data (can be combined with &#8211;extract)</dl>
<h2>USAGE FOR BUG REPORTING</h2>
<dl>
<dt>This command is useful if you want to report a bug in gPodder:</p>
<dd>
<dt><code>gpodder-backup &#8211;create bug123.gpo.tar.gz &#8211;fake-downloads</code></p>
<dd> Backup your current data to file <i>bug123.gpo.tar.gz</i>, but don&#8217;t store download data (create zero-size dummy files instead). You can then attach <i>bug123.gpo.tar.gz</i> to the bug report.</p>
<dt>If you are instructed to try gPodder from a &quot;clean state&quot;, you can use the following command (be sure to backup your data before!):</p>
<dd>
<dt><code>gpodder-backup &#8211;purge</code></p>
<dd> Remove all gPodder data, so you can start from a clean state</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>gpodder-backup &#8211;create today.gpo.tar.gz</code></p>
<dd> Backup your current data to file <i>today.gpo.tar.gz</i></p>
<dt><code>gpodder-backup &#8211;extract mybackup.gpo.tar.gz</code></p>
<dd> Restore (without purging) the contents of <i>mybackup.gpo.tar.gz</i></p>
<dt><code>gpodder-backup &#8211;extract default.gpo.tar.gz &#8211;purge</code></p>
<dd> Remove current data, then restore the contents of <i>default.gpo.tar.gz</i></p>
<dt><code>gpodder-backup &#8211;purge</code></p>
<dd> Remove all gPodder data, so you can start from a clean state</dl>
<h2>AUTHOR</h2>
<p> gpodder-backup was written by Thomas Perl (thp [at] gpodder.org) </p>
<h2>Index</h2>
