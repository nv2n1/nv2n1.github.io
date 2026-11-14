---
title: "ark(1)"
name: "ark"
section: "1"
letter: "a"
url: "/docs/linux/man/1-ark/"
description: "ark – KDE archiving tool"
---

<h2 class="name">NAME</h2>
<p> ark &#8211; KDE archiving tool </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ark</code> [<code>-b</code>] [<code>-a</code>] [<code>-e</code>] [<code>-c</code>] [<code>-f</code><i></p>
<dd>suffix</i>] [<code>-p</code>] [<code>-t</code><i> file</i>] [<code>-d</code>] [<code>-o</code><i> directory</i>] [KDE Generic Options] [Qt(TM)&nbsp;<wbr>Generic Options]</dl>
<h2>DESCRIPTION</h2>
<p> Ark is a program for managing various compressed file formats within KDE. Archives can be viewed, extracted, created and modified with Ark. The program can handle various formats such as tar, gzip, bzip2, zip, rar (when the appropriate libraries or command-line programs are installed).</p>
<h2>OPERATION MODES</h2>
<p> Ark can be used either as a stand-alone GUI program as well as a command-line program in order to perform some specific tasks. </p>
<p> If invoked without the -b (&#8211;batch) or -c (&#8211;add) options, Ark is started as a normal GUI program. </p>
<p> When the -b (&#8211;batch) option is used, Ark can be used to extract the contents of one or more files directly from the command-line, without launching its GUI. </p>
<p> When the -c (&#8211;add) option is used, Ark prompts for files that should be added to a new archive or to an existing archive. </p>
<h2>OPTIONS</h2>
<p> <code>-d, &#8211;dialog</code></p>
<dl>
<dt>
<dd> Show a dialog for specifying the options for a batch or add operation.</dl>
<p> <code>-o, &#8211;destination </code><i>directory</i></p>
<dl>
<dt>
<dd> Default the extraction directory to <i>directory</i>. If not passed, the current path is used.</dl>
<h3>Options for adding files</h3>
<p> <code>-c, &#8211;add</code></p>
<dl>
<dt>
<dd> Query the user for an archive filename and add specified files to it. Quit when finished.</dl>
<p> <code>-t, &#8211;add-to </code><i>filename</i></p>
<dl>
<dt>
<dd> Add the specified files to <i>filename</i>. Create archive if it does not exist. Quit when finished.</dl>
<p> <code>-p, &#8211;changetofirstpath</code></p>
<dl>
<dt>
<dd> Change the current directory to the first entry and add all other entries relative to this one.</dl>
<p> <code>-f, &#8211;autofilename </code><i>suffix</i></p>
<dl>
<dt>
<dd> Automatically choose a filename, with the selected <i>suffix</i> (for example rar, tar.gz, zip or any other supported types).</dl>
<h3>Options for batch extraction</h3>
<p> <code>b, &#8211;batch</code></p>
<dl>
<dt>
<dd> Use the batch interface instead of the usual dialog. This option is implied if more than one url is specified.</dl>
<p> <code>-e, &#8211;autodestination</code></p>
<dl>
<dt>
<dd> The destination argument will be set to the path of the first file supplied.</dl>
<p> <code>-a, &#8211;autosubfolder</code></p>
<dl>
<dt>
<dd> Archive contents will be read, and if detected to not be a single folder archive, a subfolder by the name of the archive will be created.</dl>
<h2>EXAMPLES</h2>
<p> <code>ark</code><code>&#8211;batch</code><i>archive.tar.bz2</i></p>
<dl>
<dt>
<dd> Will extract <i>archive.tar.bz2</i> into the current directory without showing any GUI.</dl>
<p> <code>ark</code><code>-b</code><code>-d</code><i>archive.tar.bz2</i><i>archive2.zip</i></p>
<dl>
<dt>
<dd> Will first show an extraction options dialog and then extract both <i>archive.tar.bz2</i> and <i>archive2.zip</i> into the directory chosen in the dialog.</dl>
<p> <code>ark</code><code>&#8211;add-to</code><i>my-archive.zip</i><i>photo1.jpg</i><i>text.txt</i></p>
<dl>
<dt>
<dd> Will create <i>my-archive.zip</i> if does not exist and then add <i>photo1.jpg</i> and <i>text.txt</i> to it.</dl>
<h2>AUTHORS</h2>
<p> Ark is currently maintained by Harald Hvaal&lt;haraldhv [at] stud.ntnu.no&gt; and Raphael Kubo da Costa&lt;kubito [at] gmail.com&gt;. </p>
<p> This man page was first written by Lauri Watts&lt;lauri [at] kde.org&gt; in 2005 for KDE 3.4, and was later updated in 2009 by Raphael Kubo da Costa&lt;kubito [at] gmail.com&gt;.</p>
<h2>AUTHORS</h2>
<p> <code>Lauri Watts</code> &lt;lauri [at] kde.org&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<p> <code>Raphael Kubo da Costa</code> &lt;kubito [at] gmail.com&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>Index</h2>
