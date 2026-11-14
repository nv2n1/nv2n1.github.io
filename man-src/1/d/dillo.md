---
title: "dillo(1)"
name: "dillo"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dillo/"
description: "dillo – web browser"
---

<h2>NAME</h2>
<p> dillo &#8211; web browser</p>
<h2>SYNOPSIS</h2>
<p> <code>dillo</code> [<i>OPTION</i>]&#8230; [<code>&#8212;</code>] [<i>URL</i>|<i>FILE</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Dillo is a lightweight graphical web browser that aims to be secure. It handles HTTP internally, and FILE, FTP, and DATA URIs are handled through a plugin system (dpi). In addition, <i>INSECURE</i> HTTPS support can be enabled. Both FTP and Dillo&#8217;s download manager use the <code><a href="/docs/linux/man/1-wget/">wget</a></code>(1) downloader. </p>
<p> Dillo displays HTML, text, PNG, JPEG, and GIF files. It handles cookies, HTTP authentication (basic and digest), proxying (basic), and some CSS. </p>
<p> Framesets are displayed as links to frames, and there is currently no support for javascript or video. </p>
<p> In order to use the hyphenation feature, pattern files from CTAN need to be installed to <i>/usr/lib/dillo/hyphenation/</i>. This can be done with the script <i>dillo-install-hyphenation</i>. Call it with ISO-639-1 language codes as arguments, or without arguments to get more help.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code>, <code>&#8211;fullwindow</code></p>
<dd> Start in full window mode: hide address bar, navigation buttons, menu, and status bar.</p>
<dt><code>-g</code>, <code>-geometry </code><i>GEO</i></p>
<dd> Set initial window position where <i>GEO</i> is <i>W</i><code>x</code><i>H</i>[{<code>+-</code>}<i>X</i>{<code>+-</code>}<i>Y</i>].</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display this help text and exit.</p>
<dt><code>-l</code>, <code>&#8211;local</code></p>
<dd> Don&#8217;t load images or stylesheets, or follow redirections, for these FILEs or URLs. This is intended for use with HTML email.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Display version info and exit.</p>
<dt><code>-x</code>, <code>&#8211;xid </code><i>XID</i></p>
<dd> Open first Dillo window in an existing window whose window ID is <i>XID</i>.</dl>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></p>
<dd> No error.</p>
<dt><code>1</code></p>
<dd> Internal error.</p>
<dt><code>2</code></p>
<dd> Error in command line arguments.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>HOME </code>(or <code>HOMEDRIVE </code>and <code>HOMEPATH </code>on Cygwin)</p>
<dd> User&#8217;s home directory.</p>
<dt><code>http_proxy</code></p>
<dd> URL of proxy to send HTTP traffic through.</dl>
<h2>FILES</h2>
<dl>
<dt><i>dpid</i></p>
<dd> Dillo plugin daemon</p>
<dt><i>dpidc</i></p>
<dd> Control program for dpid.</p>
<dt><i>~/.dillo/bm.txt</i></p>
<dd> User bookmarks</p>
<dt><i>~/.dillo/certs/</i></p>
<dd> Saved certificates for HTTPS.</p>
<dt><i>~/.dillo/cookies.txt</i></p>
<dd> Stored cookies</p>
<dt><i>~/.dillo/cookiesrc</i></p>
<dd> Cookie settings</p>
<dt><i>~/.dillo/dillorc</i></p>
<dd> Configuration file.</p>
<dt><i>~/.dillo/domainrc</i></p>
<dd> Rules for cross-domain requests.</p>
<dt><i>~/.dillo/dpid_comm_keys</i></p>
<dd> Keys used in dpi daemon communication.</p>
<dt><i>~/.dillo/dpidrc</i></p>
<dd> Contains name of directory containing dpis, and associates dpi files with protocols.</p>
<dt><i>~/.dillo/keysrc</i></p>
<dd> Keybindings.</p>
<dt><i>~/.dillo/style.css</i></p>
<dd> User style sheet.</p>
<dt><i>/usr/lib/dillo/hyphenation/</i></p>
<dd> Hyphenation pattern files.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wget/">wget</a></code>(1) </p>
<p> Dillo website: <code><a rel="nofollow" href="http://www.dillo.org">http://www.dillo.org</a></code> </p>
<h2>Index</h2>
