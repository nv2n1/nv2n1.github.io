---
title: "tomboy(1)"
name: "tomboy"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tomboy/"
description: "tomboy – A simple note-taking application for Gnome"
---

<h2 class="name">NAME</h2>
<p> tomboy &#8211; A simple note-taking application for Gnome</p>
<h2>SYNOPSIS</h2>
<p> <code>tomboy</code> <i>[OPTION] &#8230;</i> </p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>tomboy</code> command. </p>
<p> <code>Tomboy</code> is a desktop note-taking application for Linux and Unix. Simple and easy to use, but with potential to help you organize the ideas and information you deal with every day. </p>
<p> Tomboy&#8217;s usefulness lies in the ability to relate notes and ideas together, using a WikiWiki-like linking system. </p>
<p> When run without any options, the Tomboy note menu appears in the Gnome Panel&#8217;s notification tray area. Selecting a note from the menu displays the note&#8217;s spatial window. </p>
<p> Changes to notes are saved automatically. Links to URLs, files, and other notes are detected as you type. Rich editing such as highlighting, bold, italics, undo/redo, and variable font sizes are supported. </p>
<p> Global keybindings exist to allow fast access to Tomboy notes and dialogs. These keybindings are set in GConf (see below) and may be activated from any application. </p>
<h2>OPTIONS</h2>
<p> The program follows the usual GNU command line syntax, with options starting with two dashes (`&#8211;&#8216;). A summary of options are included below.</p>
<dl>
<dt><code>&#8211;new-note</code></p>
<dd> Create and display a new note.</p>
<dt><code>&#8211;new-note TITLE</code></p>
<dd> Create and display a new note with the title given.</p>
<dt><code>&#8211;open-note TITLE/URL</code></p>
<dd> Display the existing note matching TITLE or URL.</p>
<dt><code>&#8211;note-path [PATH]</code></p>
<dd> Load/store note data in this directory.</p>
<dt><code>&#8211;start-here</code></p>
<dd> Display the &quot;Start Here&quot; note.</p>
<dt><code>&#8211;panel-applet</code></p>
<dd> Launches Tomboy as a panel applet. This feature is not meant for users, but must be utilized only by gnome-panel.</p>
<dt><code>&#8211;search TEXT</code></p>
<dd> Searches notes for the specified TEXT and opens the Search All Notes window with the search text</p>
<dt><code>&#8211;highlight-search TEXT</code></p>
<dd> Search and highlight TEXT in the opened note.</p>
<dt><code>&#8211;help<tt>&nbsp;<wbr>&nbsp;<wbr></tt></code></p>
<dd> Show summary of options.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version of program.</p>
<dt><code>&#8211;debug</code></p>
<dd> Turn on debugging output. </p>
</dl>
<h2>GCONF SETTINGS</h2>
<p> Tomboy has several preference settings stored in GConf. Changes to Settings are applied instantly to any running Tomboy instance. A summary of the GConf settings and their purpose are described below.</p>
<dl>
<dt><code>/apps/tomboy/global_keybindings/open_start_here</code></p>
<dd> Global X keybinding for displaying the &quot;Start Here&quot; note. The default keybinding is &lt;Alt&gt;F11.</p>
<dt><code>/apps/tomboy/global_keybindings/show_note_menu</code></p>
<dd> Global X keybinding for displaying the Tomboy applet&#8217;s note menu. The default keybinding is &lt;Alt&gt;F12.</p>
<dt><code>/apps/tomboy/global_keybindings/create_new_note</code></p>
<dd> Global X keybinding for creating and displaying a new note.</p>
<dt><code>/apps/tomboy/global_keybindings/open_recent_changes</code></p>
<dd> Global X keybinding for opening the recent changes dialog.</p>
<dt><code>/apps/tomboy/global_keybindings/open_search</code></p>
<dd> Global X keybinding for opening the note search dialog. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <i><a rel="nofollow" href="http://www.beatniksoftware.com/tomboy/">http://www.beatniksoftware.com/tomboy/</a></i> </p>
<h2>BUGS</h2>
<p> Please send bug reports to the Tomboy mailing list (tomboy-list [at] beatniksoftware.com) or enter them in the Gnome Bugzilla bug tracker (<a rel="nofollow" href="http://bugzilla.gnome.org/enter_bug.cgi?product=Tomboy">http://bugzilla.gnome.org/enter_bug.cgi?product=Tomboy</a>). </p>
<h2>AUTHOR</h2>
<p> Alex Graveley &lt;alex [at] beatniksoftware.com&gt; </p>
<p> This manual page was originally written by Luca Capello &lt;luca [at] pca.it&gt;. </p>
<h2>Index</h2>
