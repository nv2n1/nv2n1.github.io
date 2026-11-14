---
title: "otter-browser(1)"
name: "otter-browser"
section: "1"
letter: "o"
url: "/docs/linux/man/1-otter-browser/"
description: "otter-browser – the web browser controlled by the user, not vice-versa"
---

<h2>NAME</h2>
<p> otter-browser &#8211; the web browser controlled by the user, not vice-versa</p>
<h2>SYNOPSIS</h2>
<p> <code>otter-browser</code> [<i>OPTIONS</i>] [<i>PATH</i>|<i>URL</i>|<i>TERM</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> See the Otter Browser wiki for help on using the browser:</p>
<dl>
<dt>
<dd> &lt;<a rel="nofollow" href="https://github.com/Emdek/otter/wiki/">https://github.com/Emdek/otter/wiki/</a>&gt;</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;profile</code>=<i>PATH</i></p>
<dd> Specifies the directory that profile (user data) is kept in. Defaults to <i>~/.config/otter</i>.</p>
<dt><code>&#8211;cache</code>=<i>PATH</i></p>
<dd> Specifies the directory that cache data is kept in. Defaults to <i>~/.cache/otter</i>.</p>
<dt><code>&#8211;session</code>=<i>IDENTIFIER</i></p>
<dd> Tries to load session specified by <i>IDENTIFIER</i>.</p>
<dt><code>&#8211;privatesession</code></p>
<dd> Starts private session.</p>
<dt><code>&#8211;sessionchooser</code></p>
<dd> Forces session chooser dialog.</p>
<dt><code>&#8211;portable</code></p>
<dd> Sets profile and cache paths to directories inside the same directory as that of application binary.</p>
<dt><code>&#8211;report</code></p>
<dd> Prints out diagnostic report and exits application.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show list of supported command line options.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Show version information.</dl>
<p> As a Qt application, Otter also obeys Qt command-line flags, see the Qt documentation for complete list:</p>
<dl>
<dt>
<dd> &lt;<a rel="nofollow" href="http://doc.qt.io/qt-5/qguiapplication.html#QGuiApplication">http://doc.qt.io/qt-5/qguiapplication.html#QGuiApplication</a>&gt;</dl>
<h2>FILES</h2>
<dl>
<dt><i>~/.config/otter</i></p>
<dd> Default directory for configuration data.</p>
<dt><i>~/.cache/otter</i></p>
<dd> Default directory for cache data.</dl>
<h2>BUGS</h2>
<p> Bug tracker:</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://github.com/OtterBrowser/otter-browser/issues">https://github.com/OtterBrowser/otter-browser/issues</a></dl>
<p> Be sure to do your search within open and closed issues before submitting reports.</p>
<h2>AUTHOR</h2>
<p> The Otter Browser team &#8211; &lt;<a rel="nofollow" href="http://otter-browser.org">http://otter-browser.org</a>&gt; </p>
<h2>Index</h2>
