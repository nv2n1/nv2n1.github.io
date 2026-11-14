---
title: "kgb-add-project(1)"
name: "kgb-add-project"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kgb-add-project/"
description: "kgb-add-project – helper script for adding new projects to kgb-bot configuration file"
---

<h2 class="name">NAME</h2>
<p> kgb-add-project &#8211; helper script for adding new projects to kgb-bot configuration file </p>
<h2>SYNOPSIS</h2>
<p> <code>kgb-add-project</code> [&#8211;file configfile] [&#8211;dir configdir] [&#8211;net|&#8211;networks ircnetwork] [&#8211;save|&#8211;write] project-id ircchannel password</p>
<h2>DESCRIPTION</h2>
<p> <code>kgb-add-project</code> allows one to add new projects to <code>kgb-bot</code>&#8216;s configuration file from the command line. It writes the new config to stdout unless <i>&#8211;save|&#8211;write</i> is given.</p>
<h2>ARGUMENTS</h2>
<dl>
<dt><code>&#8211;file</code> configfile</p>
<dd> Optional. Defaults to <i>/etc/kgb-bot/kgb.conf</i>.</p>
<dt><code>&#8211;dir</code> configdir</p>
<dd> Optional. Defaults to <i>/etc/kgb-bot/kgb.conf.d/</i>. Used for writing config snippets for projects with <code>&#8211;save|&#8211;write</code>.</p>
<dt><code>&#8211;net|network</code> ircnetwork</p>
<dd> Optional. Defaults to <code>oftc</code>. Needs to be in the <i>networks</i> section of the configuration file.</p>
<dt><code>&#8211;save|&#8211;write</code></p>
<dd> Optional. Write new config back to file instead of stdout.</p>
<dt><code>project-id</code></p>
<dd> <code>project-id</code> to be added.</p>
<dt><code>irchannel</code></p>
<dd> <font SIZE="-1">IRC</font> channel where the new project sends its messages. If the channel doesn&#8217;t start with a character denoting <font SIZE="-1">IRC</font> channel (<tt>&quot;#&amp;+&quot;</tt>), then a hash sign is prepended.</p>
<dt><code>password</code></p>
<dd> Password for the new project.</dl>
<h2>EXAMPLE</h2>
<p> <code>kgb-add-project</code> my-project \#projectchannel RudFiarced0</p>
<h2>CAVEATS</h2>
<dl>
<dt>&bull;</p>
<dd> <code>kgb-add-project</code> sorts the top-level sections of the configuration file in a fixed order and re-orders the subsections alphabetically.</p>
<dt>&bull;</p>
<dd> The output of <code>kgb-add-project</code> does not contain the comments that were present in the source configuration file.</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>App::KGB</p>
<dd>
<dt><i><a href="/docs/linux/man/1-kgb-bot/">kgb-bot</a></i>(1)</p>
<dd></dl>
<h2>COPYRIGHT AND LICENSE</h2>
<p> Copyright (C) 2012 Damyan Ivanov </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, <font SIZE="-1">MA 02110-1301, USA.</font> </p>
<h2>Index</h2>
