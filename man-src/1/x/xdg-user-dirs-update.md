---
title: "xdg-user-dirs-update(1)"
name: "xdg-user-dirs-update"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xdg-user-dirs-update/"
description: "xdg-user-dirs-update – Update XDG user dir configuration"
---

<h2 class="name">NAME</h2>
<p> xdg-user-dirs-update &#8211; Update XDG user dir configuration </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>xdg-user-dirs-update</code> [OPTION&#8230;] [&#8211;set&nbsp;<i>NAME</i>&nbsp;<i>PATH</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>xdg-user-dirs-update</code></p>
<dd>updates the current state of the users user-dirs.dir. If none existed before then one is created based on the system default values, or falling back to the old non-translated filenames if such directories exists. The list of old directories used are: ~/Desktop, ~/Templates and ~/Public. </p>
<p> If an old configuration exists it is updated with any new default directories. Additionally, any configured directories that point to non-existing locations are reset by pointing then to the users home directory. This typically happens when the users removed the directory, so they likely don&#8217;t want to use it anymore. </p>
<p> On the first run a user-dirs.locale file is created containing the locale that was used for the translation. This is used later by GUI tools like <code>xdg-user-dirs-gtk-update</code> to detect if the locale was changed, letting you to migrate from the old names. </p>
<p> <code>xdg-user-dirs-update</code> is normally run automatically at the start of a user session to update the XDG user dirs according to the users locale.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print help output and exit.</dl>
<p> <code>&#8211;force</code></p>
<dl>
<dt>
<dd> Update existing user-dirs.dir, but force a full reset. This means: Don&#8217;t reset nonexisting directories to HOME, rather recreate the directory. Never use backwards compatible non-translated names. Always recreate user-dirs.locale.</dl>
<p> <code>&#8211;dummy-output </code><i>PATH</i></p>
<dl>
<dt>
<dd> Write the configuration to <i>PATH</i> instead of the default configuration file. Also, no directories are created.</dl>
<p> <code>&#8211;set </code><i>NAME</i><i>PATH</i></p>
<dl>
<dt>
<dd> Sets the XDG user dir with the given name. </p>
<p> <i>NAME</i> should be one of the following:</p>
<dl>
<dt>
<dd> DESKTOP</dl>
<dl>
<dt>
<dd> DOWNLOAD</dl>
<dl>
<dt>
<dd> TEMPLATES</dl>
<dl>
<dt>
<dd> PUBLICSHARE</dl>
<dl>
<dt>
<dd> DOCUMENTS</dl>
<dl>
<dt>
<dd> MUSIC</dl>
<dl>
<dt>
<dd> PICTURES</dl>
<dl>
<dt>
<dd> VIDEOS</dl>
<p> <i>PATH</i> must be an absolute path, e.g. $HOME/Some/Directory.</dl>
<h2>FILES</h2>
<p> The XDG user dirs configuration is stored in the user-dirs.dir file in the location pointed to by the <code>XDG_CONFIG_HOME</code> environment variable.</p>
<h2>ENVIRONMENT</h2>
<p> The <code>XDG_CONFIG_HOME</code> environment variable determines where the user-dirs.dirs file is located.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xdg-user-dir/">xdg-user-dir</a></code>(1), <code><a href="/docs/linux/man/5-user-dirs-dirs/">user-dirs.dirs</a></code>(5), <code><a href="/docs/linux/man/5-user-dirs-defaults/">user-dirs.defaults</a></code>(5), <code><a href="/docs/linux/man/5-user-dirs-conf/">user-dirs.conf</a></code>(5). </p>
<h2>Index</h2>
