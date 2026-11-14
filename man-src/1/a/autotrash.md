---
title: "autotrash(1)"
name: "autotrash"
section: "1"
letter: "a"
url: "/docs/linux/man/1-autotrash/"
description: "autotrash — program to automatically purge old files from the FreeDesktop.org trash"
---

<h2>NAME</h2>
<p> autotrash &#8212; program to automatically purge old files from the FreeDesktop.org trash</p>
<h2>SYNOPSIS</h2>
<p> <code>autotrash</code> [<code>-d </code><i>purge_n_days_old</i>] </p>
<p> <code>autotrash</code> [<code>&#8211;delete </code><i>number_of_megabytes_to_purge</i>] </p>
<p> <code>autotrash</code> [<code>&#8211;keep-free </code><i>number_of_megabytes_to_free</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>autotrash</code> is a program that looks in a FreeDesktop.org Trash folder for information on it&#8217;s contents and then purges a part of the trash depending on the options. </p>
<p> The most common option is <code>-d</code>, which will purge files that have been in the trash for more then a given number of days. </p>
<p> The option <code>&#8211;delete</code> will remove at least the given number of megabytes from the trash, removing the oldest trash first. </p>
<p> Using <code>&#8211;keep-free</code> will make sure at least the given number of megabytes of free space is available, by automatically setting <code>&#8211;delete</code> to the right value. For example, to keep at least a 1GB of free space, removing files from the trash if needed, use <code>autotrash</code> <code>&#8211;keep-free</code> 1024 .</p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;).</p>
<dl>
<dt><code>-h</code> <code>&#8211;help</code></p>
<dd> Show a summary of options.</p>
<dt><code>-d </code><i>DAYS</i> <code>&#8211;days </code><i>DAYS</i></p>
<dd> Purge files older than DAYS number of days.</p>
<dt><code>-T </code><i>PATH</i> <code>&#8211;trash-path </code><i>PATH</i></p>
<dd> Use the given path as the location of the Trash directory, instead of the default: ~/.local/share/Trash .</p>
<dt><code>&#8211;max-free </code><i>M</i></p>
<dd> Only purge files if there is less than <i>M</i> megabytes of free space left at the trash location. As an example, if you set this to 1024, then autotrash will only start to work if there is less than 1GB of free space in the trash. Till that time, autotrash will just exit normally without scanning the Trash directory. If unsure, try running autotrash with <code>&#8211;dry-run</code> and <code>&#8211;verbose</code> to see the effect.</p>
<dt><code>&#8211;delete </code><i>M</i></p>
<dd> Purge at least <i>M</i> megabytes, deleting oldest trash addition first. It uses trash entries, NOT individual files. This means that if your oldest trashed item is a 1GB directory, and you request at least 10MB to be removed (M=10), autotrash will remove 1GB. If unsure, try running autotrash with both <code>&#8211;dry-run</code> and <code>&#8211;stat</code> to see the effect.</p>
<dt><code>&#8211;min-free </code><i>M</i> <code>&#8211;keep-free </code><i>M</i></p>
<dd> Make sure there is a minimum of <i>M</i> megabytes of free space. If there is less free space, set <code>&#8211;delete</code> to the difference between <i>M</i> and the amount of free space. If unsure, try running autotrash with <code>&#8211;dry-run</code> and <code>&#8211;verbose</code> to see the effect.</p>
<dt><code>-D </code><i>REGEX</i> <code>&#8211;delete-first </code><i>REGEX</i></p>
<dd> Purge any file which matches REGEX first, regardless of it&#8217;s time-stamp. REGEX must be a valid regular expression. If this option is used multiple times, the files matching the first regular expression are deleted first, then the second etc. Example, delete any *.avi files first, then by age: &#8211;delete-first &#8216;.*\.avi&#8217;</p>
<dt><code>-v</code> <code>&#8211;verbose</code></p>
<dd> Output information on what is happening and why.</p>
<dt><code>-q</code> <code>&#8211;quiet</code></p>
<dd> Only output warnings.</p>
<dt><code>&#8211;check</code></p>
<dd> Report .trashinfo files that point to a non-existing file. This will only happen with a broken Trashcan. It is left up to the user to actually do something with this information. These files will be removed as soon as the mentioned file would be removed by autotrash.</p>
<dt><code>&#8211;dry-run</code></p>
<dd> Only list what would be done, but actually do nothing.</p>
<dt><code>&#8211;stat</code></p>
<dd> Show the number, and total size of files involved.</p>
<dt><code>-V</code> <code>&#8211;version</code></p>
<dd> Show the version of program.</dl>
<h2>EXAMPLES</h2>
<p> Examples of program use.</p>
<dl>
<dt>autotrash -d 30</p>
<dd> Purge any file that has been in the trash for more then 30 days.</p>
<dt>autotrash &#8211;max-free 1024 -d 30</p>
<dd> Only purge files from the trash if there is less than 1GB of space left on the trash filesystem. If so, only trash files that are older than 30 days.</p>
<dt>autotrash &#8211;min-free 2048</p>
<dd> Purge files from trash, oldest first, till there is at least 2GB of space on the trash filesystem. There is no restriction on how old trashed files are.</p>
<dt>autotrash &#8211;min-free 2048 -D &#8216;.*\.bak&#8217; -D &#8216;.*\.avi&#8217;</p>
<dd> Purge files from trash till there is at least 2GB of space on the trash filesystem. If we need to remove files, make sure we remove *.bak files first, then all *.avi files and after that the oldest to the newest. There is no restriction on how old trashed files can get. Please note that &#8216;.*\.bak&#8217; and &#8216;.*\.avi&#8217; are regular expressions and not glob patterns. Given that they are regular expressions, using -D &#8216;.*\.(png|gif|jpg|jpeg)&#8217; will match images with any of the given extensions.</p>
<dt>autotrash &#8211;max-free 4000 &#8211;min-free 2048 -d 30</p>
<dd> Start reading the trash if there is less than 4000MB of free space, then start keeping an eye on. At that point, remove files older than 30 days and if there is less than 2GB of free space after that remove even newer files.</p>
<dt>@hourly /usr/bin/autotrash &#8211;max-free 4000 &#8211;min-free 2048 -d 30</p>
<dd> Experienced users should consider adding autotrash as a crontab entry, using <code>crontab -e</code> and adding the line above.</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by A. Bram Neijt bram [at] neijt.nl for the <code>Debian</code> system (and may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 3 or any later version published by the Free Software Foundation.<br />
&nbsp;<wbr> </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.<br />
&nbsp;<wbr> </p>
<h2>Index</h2>
