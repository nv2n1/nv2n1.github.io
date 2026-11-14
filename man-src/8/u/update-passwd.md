---
title: "update-passwd(8)"
name: "update-passwd"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-passwd/"
description: "update-passwd – safely update /etc/passwd, /etc/shadow and /etc/group"
---

<p>update-passwd &#8211; safely update /etc/passwd, /etc/shadow and /etc/group</p>
<h2>Synopsis</h2>
<p><code>update-passwd</code> [<i>options</i>]</p>
<h2>Description</h2>
<p><code>update-passwd</code> handles updates of /etc/passwd, /etc/shadow and /etc/group on running Debian systems. It compares the current files to master copies, distributed in the base-passwd package, and updates all entries in the global system range (that is, 0-99). It leaves backup copies of the previous versions of modified files with the extension &#8216;.org&#8217; (for &#8220;original&#8221;).</p>
<h2>Options</h2>
<p><code>update-passwd</code> follows the usual GNU command line syntax, with long options starting with two dashes (&#8216;-&#8216;).</p>
<dl>
<dt><code>-p</code>,&nbsp;<code>&#8211;passwd-master=FILE</code></p>
<dd>Use FILE as the master copy of the passwd database. The default value is <i>/usr/share/base-passwd/passwd.master</i>.</p>
<dt><code>-g</code>,&nbsp;<code>&#8211;group-master=FILE</code></p>
<dd>Use FILE as the master copy of the group database. The default value is <i>/usr/share/base-passwd/group.master</i>.</p>
<dt><code>-P</code>,&nbsp;<code>&#8211;passwd=FILE</code></p>
<dd>Use FILE as the system passwd database. The default value is <i>/etc/passwd</i>.</p>
<dt><code>-S</code>,&nbsp;<code>&#8211;shadow=FILE</code></p>
<dd>Use FILE as the system shadow database. The default value is <i>/etc/shadow</i>.</p>
<dt><code>-G</code>,&nbsp;<code>&#8211;group=FILE</code></p>
<dd>Use FILE as the system group database. The default value is <i>/etc/group</i>.</p>
<dt><code>-s</code>,&nbsp;<code>&#8211;sanity-check</code></p>
<dd>Only perform sanity-checks but don&#8217;t do anything.</p>
<dt><code>-v</code>,&nbsp;<code>&#8211;verbose</code></p>
<dd>Give detailed information about what we are doing. A second -v gives additional detail.</p>
<dt><code>-n</code>,&nbsp;<code>&#8211;dry-run</code></p>
<dd>Don&#8217;t do anything but only show what we would do.</p>
<dt><code>-L</code>,&nbsp;<code>&#8211;no-locking</code></p>
<dd>Don&#8217;t attempt to lock the account database. This should only be used for debugging purposes. <code>I repeat: do not do this unless you are really sure you need this!</code></p>
<dt><code>-h</code>,&nbsp;<code>&#8211;help</code></p>
<dd>Show a summary of how to use <code>update-passwd</code>.</p>
<dt><code>-V</code>,&nbsp;<code>&#8211;version</code></p>
<dd>Show the version number</dl>
<h2>Environment</h2>
<dl>
<dt>DEBIAN_HAS_FRONTEND</p>
<dd>If this environment variable is set and the <code>&#8211;dry-run</code> flag was not given, <code>update-passwd</code> uses debconf to prompt for whether to make changes. Each proposed change will produce a separate prompt. User or group removals, UID or GID changes, and home directory changes will be asked with high priority. User or group additions and shell changes will be asked with medium priority. Questions about whether to move entries above the NIS compat inclusion entry or whether to change the GECOS of a user are asked at low priority.</dl>
<h2>Bugs</h2>
<p>At this moment <code>update-passwd</code> does not verify the shadow-file. It should check if the entries in the passwd are also in shadow and vice versa, and that passwords are not present in both files.</p>
<h2>Author</h2>
<p>Wichert Akkerman &lt;wakkerma [at] debian.org&gt; </p>
<p> This program was written for the Debian project, and is copyright 1999-2002 Wichert Akkerman and copyright 2002, 2003 Colin Watson. It is distributed under version 2 of the GNU General Public License.</p>
