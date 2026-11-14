---
title: "qpdfview(1)"
name: "qpdfview"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qpdfview/"
description: "qpdfview – tabbed document viewer"
---

<h2 class="name">NAME</h2>
<p> qpdfview &#8211; tabbed document viewer </p>
<h2>SYNOPSIS</h2>
<p> <code>qpdfview</code> <i>[options] [&#8211;] [file[#page]] [file[#src:name:line:column]] &#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> <code>qpdfview</code> is a simple viewer for document files in the portable document format (PDF). It uses the Poppler library for rendering and the Qt toolkit for its interface.</p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;help</p>
<dd> Displays usage information.</p>
<dt>&#8211;quiet</p>
<dd> Suppresses warning messages which are displayed if the program fails to open a file.</p>
<dt>&#8211;search text</p>
<dd> Initiates a search for <i>text</i> in the current tab.</p>
<dt>&#8211;unique</p>
<dd> If an instance of qpdfview is started with this option, any files that are opened using this option afterwards, are opened as tabs in the original window. If a file is already opened in a tab of the original window, it is merely reloaded.</p>
<dt>&#8211;instance name</p>
<dd> Uses <i>name</i> as the name of the instance contacted or created using the &quot;&#8211;unique&quot; option. This allows one to run multiple instances and remotely open and refresh tabs in any of them by passing the instance name. The argument must only contain the characters &quot;[A-Z][a-z][0-9]_&quot; and must not begin with a digit.</p>
<dt>&#8211;choose-instance</p>
<dd> Can be combined with the &quot;&#8211;unique&quot; option to display a dialog at start-up where the instance name can be chosen with all instances that have tabs stored as suggestions.</p>
<dt>[file[#page]]</p>
<dd> <i>file</i> specifies the file to open. The optional parameter <i>page</i> opens the file at the given page. Multiple files will be opened in separate tabs.</p>
<dt>[file[#src:name:line:column]]</p>
<dd> Forward search using SyncTeX is performed using the optional parameters <i>name</i> which is the name of the source file, <i>line</i> which is the line number in the source file and <i>column</i> which is the column number in the source file where the number 0 matches all lines respectively columns.</dl>
<h2>INTER-PROCESS COMMUNICATION</h2>
<p> If the program is invoked using the &quot;&#8211;unique&quot; option, it registers an introspectable D-Bus interface at &quot;local.qpdfview/MainWindow&quot; which can be used to communicate with the application. If the &quot;&#8211;instance&quot; option is used, the D-Bus interface is registered at &quot;local.qpdfview.name/MainWindow&quot;.</p>
<h2>CONFIGURATION FILES</h2>
<p> qpdfview uses configuration files usually located at</p>
<dl>
<dt>
<dd> &quot;~/.config/qpdfview&quot;</dl>
<p> with the majority of settings contained in &quot;qpdfview.conf&quot;. </p>
<p> Persitent state like per-file settings, bookmarks and tabs is stored in an SQLite database usually located at</p>
<dl>
<dt>
<dd> &quot;~/.local/share/data/qpdfview/qpdfview&quot;.</dl>
<p> The icon theme used by Qt can be changed by setting the key &quot;iconTheme&quot; in the section &quot;mainWindow&quot;. The application-wide Qt style sheet can be changed by setting the key &quot;styleSheet&quot; in the section &quot;mainWindow&quot;. </p>
<p> The tile size in pixels used for tiled rendering can be adjusted by setting the key &quot;tileSize&quot; in the section &quot;pageItem&quot;. The default value is 1024 pixels. </p>
<p> The minimum resp. maximum scale factor can be modified by changing the keys &quot;minimumScaleFactor&quot; resp. &quot;maximumScaleFactor&quot; in the section &quot;documentView&quot;. The default values are 0.1 resp. 10.0. </p>
<p> The timeout for auto-refresh resp. prefetch can be changed by setting the keys &quot;autoRefreshTimeout&quot; resp. &quot;prefetchTimeout&quot; in the section &quot;documentView&quot;. The defaults are 750 resp. 250 milliseconds. </p>
<p> The maximum number of per-file settings can be modified by changing the key &quot;perFileSettingsLimit&quot; in the section &quot;mainWindow&quot;. The default value is 1000.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> The command</dl>
<p> <code>qpdfview foo.pdf#3 bar.pdf</code></p>
<dl>
<dt>
<dd> opens &quot;foo.pdf&quot; in the first tab displaying the third page of the document and &quot;bar.pdf&quot; in the second tab displaying the beginning of the document. </p>
<p> The command</dl>
<p> <code>qpdfview &#8211;quiet foobar/*</code></p>
<dl>
<dt>
<dd> opens all files that can be opened in the directory &quot;foobar&quot;, suppressing warning messages for files that cannot be opened. </p>
<p> The command</dl>
<p> <code>qpdfview &#8211;search foo bar.pdf</code></p>
<dl>
<dt>
<dd> opens &quot;bar.pdf&quot; in the first tab and starts a search for &quot;foo&quot;. </p>
<p> Subsequent execution of the commands</dl>
<p> <code>qpdfview &#8211;unique foo.pdf bar.pdf</code></p>
<dl>
<dt>
<dd> and</dl>
<p> <code>qpdfview &#8211;unique foo.pdf#5</code></p>
<dl>
<dt>
<dd> opens &quot;foo.pdf&quot; and &quot;bar.pdf&quot;, then reloads &quot;foo.pdf&quot; and displays its fifth page. </p>
<p> Subsequent execution of the commands</dl>
<p> <code>qpdfview &#8211;unique foo.pdf</code></p>
<dl>
<dt>
<dd> and</dl>
<p> <code>qpdfview bar.pdf</code></p>
<dl>
<dt>
<dd> and</dl>
<p> <code>qpdfview &#8211;unique foo1.pdf bar1.pdf</code></p>
<dl>
<dt>
<dd> opens &quot;foo.pdf&quot; in the first window, &quot;bar.pdf&quot; in a second window and then &quot;foo1.pdf&quot; and &quot;bar1.pdf&quot; in additional tabs in the first window. </p>
<p> Subsequent execution of the commands</dl>
<p> <code>qpdfview &#8211;unique &#8211;instance a foo1.pdf bar1.pdf</code></p>
<dl>
<dt>
<dd> and</dl>
<p> <code>qpdfview &#8211;unique &#8211;instance b foo2.pdf bar2.pdf</code></p>
<dl>
<dt>
<dd> and</dl>
<p> <code>qpdfview &#8211;unique foo3.pdf bar3.pdf</code></p>
<dl>
<dt>
<dd> and</dl>
<p> <code>qpdfview &#8211;unique &#8211;instance a foo1.pdf#4 bar4.pdf</code></p>
<dl>
<dt>
<dd> opens &quot;foo1.pdf&quot; and &quot;bar1.pdf&quot; in the first window, &quot;foo2.pdf&quot; and &quot;bar2.pdf&quot; in the second window, &quot;foo3.pdf&quot; and &quot;bar3.pdf&quot; in the third window and then reloads &quot;foo1.pdf&quot; and displays its fourth page and opens &quot;bar4.pdf&quot; in an additional tab in the first window. </p>
<p> Subsequent execution of the commands</dl>
<p> <code>qpdfview &#8211;unique &#8211;instance a foo.pdf bar.pdf</code></p>
<dl>
<dt>
<dd> and</dl>
<p> <code>qpdfview &#8211;unique &#8211;instance a &#8211;search foobar</code></p>
<dl>
<dt>
<dd> opens &quot;foo.pdf&quot; and &quot;bar.pdf&quot; in a window and then starts a search for the term &quot;foobar&quot; in the document in the active tab (which is the last opened &quot;bar.pdf&quot;). </p>
<p> The command</dl>
<p> <code>qpdfview &#8211;unique foobar.pdf#src:foobar.tex:42:0</code></p>
<dl>
<dt>
<dd> opens or refreshes &quot;foobar.pdf&quot; jumping to and highlighting the position that corresponds to line 42 of the source file &quot;foobar.tex&quot;. </p>
<p> The lines</dl>
<p> <code>[documentView]</code></p>
<dl>
<dt>
<dd></dl>
<p> <code>autoRefreshTimeout=1250</code></p>
<dl>
<dt>
<dd></dl>
<p> <code>[mainWindow]</code></p>
<dl>
<dt>
<dd></dl>
<p> <code>styleSheet=QTabBar::tab { max-width: 150px; }</code></p>
<dl>
<dt>
<dd> will configure the auto-refresh timeout to 1250 milliseconds and the change the maximum tab width to 150 pixel. </p>
</dl>
<h2>BUGS</h2>
<p> If you find a bug, please report it at</p>
<dl>
<dt>
<dd> &quot;<a rel="nofollow" href="https://launchpad.net/qpdfview">https://launchpad.net/qpdfview</a>&quot;.</dl>
<h2>Index</h2>
