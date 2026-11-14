---
title: "nicotine-import-winconfig(1)"
name: "nicotine-import-winconfig"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nicotine-import-winconfig/"
description: "nicotine-import-winconfig is a script to convert SoulSeek Windows client configuration file to the Nicotine format."
---

<h2 class="name">NAME</h2>
<p> <code>nicotine-import-winconfig</code> is a script to convert SoulSeek Windows client configuration file to the Nicotine format. </p>
<h2>SYNOPSIS</h2>
<p> <code>nicotine-import-winconfig</code> [options] &lt;path_to_the_windows_soulseek_files&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>nicotine-import-winconfig</code> will read the SoulSeek Windows client configuration file and will extract information like download queue, userlist, login information, list of autojoined chatrooms, list of banned users, user info/picture, and write them to $HOME/.nicotine/config, which is the default nicotine configuration file.</p>
<h2>OPTIONS</h2>
<p> If you don&#8217;t want to import the whole configuration, you may consider using the command line flags below.</p>
<dl>
<dt><i>-q, &#8211;queue</i></p>
<dd> Import the download queue.</p>
<dt><i>-u, &#8211;userlist</i></p>
<dd> Import the userlist.</p>
<dt><i>-l, &#8211;login</i></p>
<dd> Import the login information.</p>
<dt><i>-C, &#8211;chatrooms</i></p>
<dd> Import the list of autojoined chatrooms.</p>
<dt><i>-b, &#8211;banned</i></p>
<dd> Import the list of banned users.</p>
<dt><i>-i, &#8211;userinfo</i></p>
<dd> Import the userinfo and picture.</p>
<dt><i>-h, &#8211;help</i></p>
<dd> Show help and exit.</p>
<dt><i>-c &lt;file&gt;, &#8211;config=&lt;file&gt;</i></p>
<dd> Use &lt;file&gt; as Nicotine configuration file. If &lt;file&gt; do not exists a new empty configuration file will be created.</dl>
<h2>EXAMPLES</h2>
<p> Import the SoulSeek Windows client configuration from /mnt/windows into the default nicotine configuration file : </p>
<p> Nicotine should be shut down before doing this. </p>
<p> <code>nicotine-import-winconfig</code> &quot;/mnt/windows/Program Files/SoulSeek&quot;</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Adam Cecile &lt;gandalf [at] le-vert.net&gt; for the Nicotine+ project.<br />
 Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-nicotine/">nicotine</a>(1)</code> </p>
<h2>Index</h2>
