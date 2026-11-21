---

title: "otter-browser(1)"
name: "otter-browser"
section: "1"
letter: "o"
url: "/docs/linux/man/1-otter-browser/"
description: "otter-browser – the web browser controlled by the user, not vice-versa"
---

<p> otter-browser &#8211; the web browser controlled by the user, not vice-versa</p>
<h2>SYNOPSIS</h2>
<p> <code>otter-browser</code> [<i>OPTIONS</i>] [<i>PATH</i>|<i>URL</i>|<i>TERM</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> See the Otter Browser wiki for help on using the browser:</p>
<dl>
<dt>
</dt><dd> &lt;<a rel="nofollow" href="https://github.com/Emdek/otter/wiki/">https://github.com/Emdek/otter/wiki/</a>&gt;</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;profile</code>=<i>PATH</i></dt>
<dd> Specifies the directory that profile (user data) is kept in. Defaults to <i>~/.config/otter</i>.</dd>
<dt><code>&#8211;cache</code>=<i>PATH</i></dt>
<dd> Specifies the directory that cache data is kept in. Defaults to <i>~/.cache/otter</i>.</dd>
<dt><code>&#8211;session</code>=<i>IDENTIFIER</i></dt>
<dd> Tries to load session specified by <i>IDENTIFIER</i>.</dd>
<dt><code>&#8211;privatesession</code></dt>
<dd> Starts private session.</dd>
<dt><code>&#8211;sessionchooser</code></dt>
<dd> Forces session chooser dialog.</dd>
<dt><code>&#8211;portable</code></dt>
<dd> Sets profile and cache paths to directories inside the same directory as that of application binary.</dd>
<dt><code>&#8211;report</code></dt>
<dd> Prints out diagnostic report and exits application.</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Show list of supported command line options.</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> Show version information.</dd></dl>
<p> As a Qt application, Otter also obeys Qt command-line flags, see the Qt documentation for complete list:</p>
<dl>
<dt>
</dt><dd> &lt;<a rel="nofollow" href="http://doc.qt.io/qt-5/qguiapplication.html#QGuiApplication">http://doc.qt.io/qt-5/qguiapplication.html#QGuiApplication</a>&gt;</dd></dl>
<h2>FILES</h2>
<dl>
<dt><i>~/.config/otter</i></dt>
<dd> Default directory for configuration data.</dd>
<dt><i>~/.cache/otter</i></dt>
<dd> Default directory for cache data.</dd></dl>
<h2>BUGS</h2>
<p> Bug tracker:</p>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="https://github.com/OtterBrowser/otter-browser/issues">https://github.com/OtterBrowser/otter-browser/issues</a></dd></dl>
<p> Be sure to do your search within open and closed issues before submitting reports.</p>
<h2>AUTHOR</h2>
<p> The Otter Browser team &#8211; &lt;<a rel="nofollow" href="http://otter-browser.org">http://otter-browser.org</a>&gt; </p>
