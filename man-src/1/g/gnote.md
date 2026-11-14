---
title: "gnote(1)"
name: "gnote"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnote/"
description: "gnote – A simple note-taking application for Gnome"
---

<h2 class="name">NAME</h2>
<p> gnote &#8211; A simple note-taking application for Gnome</p>
<h2>SYNOPSIS</h2>
<p> <code>gnote</code> <i>[OPTION] &#8230;</i> </p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>gnote</code> command. </p>
<p> <code>Gnote</code> is a desktop note-taking application for Linux and Unix. Simple and easy to use, but with potential to help you organize the ideas and information you deal with every day. </p>
<p> Gnote&#8217;s usefulness lies in the ability to relate notes and ideas together, using a WikiWiki-like linking system. </p>
<p> When run without any options, either a Search All Notes window or the Gnote note menu appears in the notification tray area depending on configuration. Selecting a note from a list in Search All Notes or from the menu from notification area displays the note&#8217;s spatial window. </p>
<p> Changes to notes are saved automatically. Links to URLs, files, and other notes are detected as you type. Rich editing such as highlighting, bold, italics, undo/redo, and variable font sizes are supported. </p>
<p> Global keybindings exist to allow fast access to Gnote notes and dialogs. These keybindings are set in GSettings (see below) and may be activated from any application. </p>
<h2>OPTIONS</h2>
<p> The program follows the usual GNU command line syntax, with options starting with two dashes (`&#8211;&#8216;). A summary of options are included below.</p>
<dl>
<dt><code>&#8211;background</code></p>
<dd> Run Gnote in background.</p>
<dt><code>&#8211;note-path PATH</code></p>
<dd> Specify the path of the directory containing the notes.</p>
<dt><code>&#8211;new-note</code></p>
<dd> Create and display a new note.</p>
<dt><code>&#8211;new-note TITLE</code></p>
<dd> Create and display a new note with the title given.</p>
<dt><code>&#8211;open-note TITLE/URL</code></p>
<dd> Display the existing note matching TITLE or URL.</p>
<dt><code>&#8211;search</code></p>
<dd> Open the search all notes window with the search text.</p>
<dt><code>&#8211;start-here</code></p>
<dd> Display the &quot;Start Here&quot; note.</p>
<dt><code>&#8211;highlight-search TEXT</code></p>
<dd> Search and highlight TEXT in the opened note.</p>
<dt><code>&#8211;help<tt>&nbsp;<wbr>&nbsp;<wbr></tt></code></p>
<dd> Show summary of options.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version of program. </p>
</dl>
<h2>GSETTINGS SETTINGS</h2>
<p> Gnote has several preference settings stored in GSettings. Changes to Settings are applied instantly to any running Gnote instance. A summary of the GConf settings and their purpose are described below.</p>
<dl>
<dt><code>org.gnome.gnote.global-keybindings</code></p>
<dd> A GSettings schema for key bindings. Keys are listed below.</p>
<dt><code>open-start-here</code></p>
<dd> Global X keybinding for displaying the &quot;Start Here&quot; note. The default keybinding is &lt;Alt&gt;F11.</p>
<dt><code>show-note-menu</code></p>
<dd> Global X keybinding for displaying the Gnote applet&#8217;s note menu. The default keybinding is &lt;Alt&gt;F12.</p>
<dt><code>create-new-note</code></p>
<dd> Global X keybinding for creating and displaying a new note.</p>
<dt><code>open-recent-changes</code></p>
<dd> Global X keybinding for opening the recent changes dialog.</p>
<dt><code>open-search</code></p>
<dd> Global X keybinding for opening the note search dialog. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <i><a rel="nofollow" href="http://live.gnome.org/Gnote/">http://live.gnome.org/Gnote/</a></i> </p>
<h2>BUGS</h2>
<p> Please enter bug reports in the Gnome Bugzilla bug tracker (<a rel="nofollow" href="http://bugzilla.gnome.org/enter_bug.cgi?product=Gnote">http://bugzilla.gnome.org/enter_bug.cgi?product=Gnote</a>). </p>
<h2>AUTHORS</h2>
<p> Hubert Figuiere &lt;hub [at] figuiere.net&gt;</p>
<dl>
<dt>Debarshi Ray &lt;debarshir [at] src.gnome.org&gt;</p>
<dd>
<dt>Aurimas Cernius &lt;aurisc4 [at] gmail.com&gt;</p>
<dd>
<p> This manual page was originally written by Luca Capello &lt;luca [at] pca.it&gt;. Adapted to Gnote by Hubert Figuiere and Aurimas Cernius </p>
</dl>
<h2>Index</h2>
