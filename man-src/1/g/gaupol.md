---

title: "gaupol(1)"
name: "gaupol"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gaupol/"
description: "gaupol – editor for text-based subtitle files"
---

<p> gaupol &#8211; editor for text-based subtitle files</p>
<h2>SYNOPSIS</h2>
<p> <code>gaupol</code> [<i>OPTION&#8230;</i>] [<i>FILE&#8230;</i>] [+[<i>NUM</i>]]</p>
<h2>DESCRIPTION</h2>
<p> <code>gaupol</code> is an editor for text-based subtitle files. It supports multiple subtitle file formats and provides means of correcting texts and timing subtitles to match video.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Show command line options.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Show version number.</dd>
<dt><code>-c</code>, <code>&#8211;config-file</code>=<i>FILE</i></dt>
<dd> Set the configuration file to use instead of the default.</dd>
<dt><code>-e</code>, <code>&#8211;encoding</code>=<i>ENCODING</i></dt>
<dd> Set the character encoding to use for opening files.</dd>
<dt><code>&#8211;list-encodings</code></dt>
<dd> List possible character encodings to use with <code>&#8211;encoding</code>.</dd>
<dt><code>+[NUM]</code></dt>
<dd> Go to subtitle number NUM in the opened file. If NUM is missing go to the last subtitle.</dd>
<dt><code>-t</code>, <code>&#8211;translation-file</code>=<i>FILE</i></dt>
<dd> Open translation file.</dd>
<dt><code>-a</code>, <code>&#8211;align-method</code>=<i>METHOD</i></dt>
<dd> Method used to align translation file&#8217;s subtitle texts with main document&#8217;s subtitles. Possible values are &#8216;number&#8217; and &#8216;position&#8217;. The default is &#8216;position&#8217;, which compares the positions in the main document and the translation file and inserts the translation texts so that those positions match. Existing subtitles are skipped and new ones inserted as needed. &#8216;number&#8217; discards position information and inserts the N translation texts into the first N subtitles.</dd>
<dt><code>-v</code>, <code>&#8211;video-file</code>=<i>FILE</i></dt>
<dd> Select video file.</dd></dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The behaviour of gaupol is affected by the following environment variables.</p>
<dl>
<dt><code>GAUPOL_DEBUG</code></dt>
<dd> If set to a non-empty string, gaupol will perform additional checks during run-time that may help in finding and locating bugs.</dd></dl>
<h2>AUTHOR</h2>
<p> Written by Osmo Salomaa &lt;otsaloma [at] iki.fi&gt;. </p>
