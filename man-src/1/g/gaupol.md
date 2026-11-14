---
title: "gaupol(1)"
name: "gaupol"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gaupol/"
description: "gaupol – editor for text-based subtitle files"
---

<h2>NAME</h2>
<p> gaupol &#8211; editor for text-based subtitle files</p>
<h2>SYNOPSIS</h2>
<p> <code>gaupol</code> [<i>OPTION&#8230;</i>] [<i>FILE&#8230;</i>] [+[<i>NUM</i>]]</p>
<h2>DESCRIPTION</h2>
<p> <code>gaupol</code> is an editor for text-based subtitle files. It supports multiple subtitle file formats and provides means of correcting texts and timing subtitles to match video.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show command line options.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version number.</p>
<dt><code>-c</code>, <code>&#8211;config-file</code>=<i>FILE</i></p>
<dd> Set the configuration file to use instead of the default.</p>
<dt><code>-e</code>, <code>&#8211;encoding</code>=<i>ENCODING</i></p>
<dd> Set the character encoding to use for opening files.</p>
<dt><code>&#8211;list-encodings</code></p>
<dd> List possible character encodings to use with <code>&#8211;encoding</code>.</p>
<dt><code>+[NUM]</code></p>
<dd> Go to subtitle number NUM in the opened file. If NUM is missing go to the last subtitle.</p>
<dt><code>-t</code>, <code>&#8211;translation-file</code>=<i>FILE</i></p>
<dd> Open translation file.</p>
<dt><code>-a</code>, <code>&#8211;align-method</code>=<i>METHOD</i></p>
<dd> Method used to align translation file&#8217;s subtitle texts with main document&#8217;s subtitles. Possible values are &#8216;number&#8217; and &#8216;position&#8217;. The default is &#8216;position&#8217;, which compares the positions in the main document and the translation file and inserts the translation texts so that those positions match. Existing subtitles are skipped and new ones inserted as needed. &#8216;number&#8217; discards position information and inserts the N translation texts into the first N subtitles.</p>
<dt><code>-v</code>, <code>&#8211;video-file</code>=<i>FILE</i></p>
<dd> Select video file.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The behaviour of gaupol is affected by the following environment variables.</p>
<dl>
<dt><code>GAUPOL_DEBUG</code></p>
<dd> If set to a non-empty string, gaupol will perform additional checks during run-time that may help in finding and locating bugs.</dl>
<h2>AUTHOR</h2>
<p> Written by Osmo Salomaa &lt;otsaloma [at] iki.fi&gt;. </p>
<h2>Index</h2>
