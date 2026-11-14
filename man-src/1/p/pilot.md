---
title: "pilot(1)"
name: "pilot"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pilot/"
description: "pilot – simple file system browser in the style of the Alpine Composer"
---

<h2>Name</h2>
<p> pilot &#8211; simple file system browser in the style of the Alpine Composer</p>
<h2>Syntax</h2>
<p> <code>pilot</code> [ <i>options</i> ] [ <i>directory</i> ]</p>
<h2>Description</h2>
<p> <i>Pilot</i> is a simple, display-oriented file system browser based on the Alpine message system composer. As with Alpine, commands are displayed at the bottom of the screen, and context-sensitive help is provided. </p>
<p> <i>Pilot</i> displays the current working directory at the top of the screen. The directory&#8217;s contents are displayed in columns of file name, file size pairs. Names that are directories are indicated by the name &quot;(dir)&quot; in place of the file size. The parent of the current working directory is indicated by the file name &quot;..&quot; and size of &quot;(parent dir)&quot;. File names that are symbolic links to other files are displayed with a file size of &quot;&#8211;&quot;. </p>
<p> Several basic file manipulation commands are provided: Delete, Rename, Copy, View, Launch, and Edit. The &quot;View&quot; and &quot;Edit&quot; commands operate on text files only. By default, the &quot;View&quot; command displays files using &quot;alpine -F&quot;, but will respect the environment variable PAGER if set. The &quot;Edit&quot; command simply invokes &quot;pico&quot;. The &quot;Launch&quot; command provides a convenient way to either execute the selected file or to run an application on it. </p>
<p> More specific help is available in <i>pilot</i>&#8216;s online help.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></p>
<dd> Display all files including those beginning with a period (.).</p>
<dt><code>-f</code></p>
<dd> Use function keys for commands. This option supported only in conjunction with UW Enhanced NCSA telnet.</p>
<dt><code>-g</code></p>
<dd> Enable &quot;Show Cursor&quot; mode. Cause cursor to be positioned before the current selection rather than placed at the lower left of the display.</p>
<dt><code>-j</code></p>
<dd> Enable &quot;Goto&quot; command. This enables the command to permit explicitly telling <i>pilot</i> which directory to visit.</p>
<dt><code>-m</code></p>
<dd> Enable mouse functionality. This only works when <i>pilot</i> is run from within an X Window System &quot;xterm&quot; window.</p>
<dt><code>-n</code><i>n</i></p>
<dd> The -n<i>n</i> option enables new mail notification. The <i>n</i> argument is optional, and specifies how often, in seconds, your mailbox is checked for new mail. For example, -n60 causes <i>pilot</i> to check for new mail once every minute. The default interval is 180 seconds, while the minimum allowed is 30. (Note: no space between &quot;n&quot; and the number)</p>
<dt><code>-o&nbsp;<wbr></code><i>dir</i></p>
<dd> Sets operating directory. Only files within the specified directory are accessible and browsing is limited to the specified directory subtree.</p>
<dt><code>-v</code></p>
<dd> Enable single vertical column display.</p>
<dt><code>-x</code></p>
<dd> Disable keymenu at the bottom of the screen.</p>
<dt><code>-z</code></p>
<dd> Enable ^Z suspension of <i>pilot</i>.</p>
<dt><code>-q</code></p>
<dd> Termcap or terminfo definition for input escape sequences are used in preference to sequences defined by default. This option is only available if <i>pilot</i> was compiled with the TERMCAP_WINS define turned on.</p>
<dt><code>-setlocale_ctype</code></p>
<dd> Do setlocale(LC_CTYPE) if available. Default is to not do this setlocale.</p>
<dt><code>-no_setlocale_collate</code></p>
<dd> Do not do setlocale(LC_COLLATE). Default is to do this setlocale.</dl>
<h2>Authors</h2>
<p> Michael Seibel &lt;mikes [at] cac.washington.edu&gt;<br />
 Copyright 1994-2007 by the University of Washington.</p>
<h2>See Also</h2>
<p> <a href="/docs/linux/man/1-alpine/">alpine</a>(1)<br />
 Source distribution (part of the Alpine Message System): </p>
<p> $Date: 2005/01/14 20:40:14 $ </p>
<h2>Index</h2>
