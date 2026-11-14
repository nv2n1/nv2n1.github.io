---
title: "kwallet-query(1)"
name: "kwallet-query"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kwallet-query/"
description: "kwallet-query – KDE Wallet command-line manipulation tool"
---

<h2 class="name">NAME</h2>
<p> kwallet-query &#8211; KDE Wallet command-line manipulation tool </p>
<h2>SYNOPSIS</h2>
<p> <code>kwallet-query</code> <i>OPTIONS</i> <i>wallet</i></p>
<h2>DESCRIPTION</h2>
<p> kwallet-query comes in handy when shell scripts need to read or update the KDE Wallet. It works by manipulating the entries displayed in the <code>KDE Wallet Manager</code> utility. It&#8217;s only parameter is the <i>wallet</i>name the tool should read or update. The operation mode is specified by the options.</p>
<h2>OPTIONS</h2>
<p> <code>-h,&#8211;help</code></p>
<dl>
<dt>
<dd> Display a short help message</dl>
<p> <code>-l,&#8211;list-entries</code></p>
<dl>
<dt>
<dd> List password entries. These are the folder names displayed in the <code>KDE Wallet Manager</code> utility. If the <code>-f</code> option is given, this will only display the subfolders of the specified folder.</dl>
<p> <code>-r,&#8211;read-password</code> <i>Entry</i></p>
<dl>
<dt>
<dd> Read the contents of the given <i>Entry</i> from the <code>Folder</code>section of the <i>wallet</i> and output it on the standard output. Maps are exported as JSON object.</dl>
<p> <code>-w,&#8211;write-password</code> <i>Entry</i></p>
<dl>
<dt>
<dd> Write secrets to the given <i>Entry</i> under the <code>Folder</code> section of the given <i>wallet</i>. The secrets are read from the standard input. Maps take in input a well-formed JSON object. <code>IMPORTANT</code> previous wallet entry value will be overwritten by this option, so be careful when using it!</dl>
<p> <code>-f,&#8211;folder</code> <i>Folder</i></p>
<dl>
<dt>
<dd> Set the <i>wallet</i> folder to <i>Folder</i> value. By default <code>Passwords</code> is used.</dl>
<p> <code>-v,&#8211;verbose</code></p>
<dl>
<dt>
<dd> Output more information when performing the operation, to help debugging.</dl>
<h2>EXIT STATUS</h2>
<p> <code>0</code></p>
<dl>
<dt>
<dd> Success</dl>
<p> <code>1</code></p>
<dl>
<dt>
<dd> The wallet <i>wallet</i> was not found</dl>
<p> <code>2</code></p>
<dl>
<dt>
<dd> The wallet <i>wallet</i> could not be opened. For example, that would be an indication of a bad password entry or some other problem with the KDE Wallet system</dl>
<p> <code>3</code></p>
<dl>
<dt>
<dd> The <code>Folder</code> section was not found inside the wallet <i>wallet</i>. Perhaps the wallet file is corrupt?</dl>
<p> <code>4</code></p>
<dl>
<dt>
<dd> The read or write operation has failed for some reason.</dl>
<h2>BUGS</h2>
<p> Please report all bugs on the KDE bug reporting website: bugs.kde.org. Be sure to select kwallet-query when submitting your bug-report.</p>
<h2>AUTHOR</h2>
<p> kwallet-query was originally written by Valentin Rusu and is part of KDE.</p>
<h2>COPYING</h2>
<p> Copyright (C) 2015 Valentin Rusu. Free use of this software is granted under the terms of the GNU General Public License (GPL).</p>
<h2>AUTHOR</h2>
<p> <code>Valentin Rusu</code> &lt;kde [at] rusu.info&gt;</p>
<dl>
<dt>
<dd> Original author</dl>
<h2>Index</h2>
