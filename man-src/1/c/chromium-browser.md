---
title: "chromium-browser(1)"
name: "chromium-browser"
section: "1"
letter: "c"
url: "/docs/linux/man/1-chromium-browser/"
description: "chromium-browser – the web browser from Google"
---

<h2 class="name">NAME</h2>
<p> chromium-browser &#8211; the web browser from Google</p>
<h2>SYNOPSIS</h2>
<p> <code>chromium-browser</code> [<i>OPTION</i>] [<i>PATH</i>|<i>URL</i>] </p>
<h2>DESCRIPTION</h2>
<p> See the Google Chrome help center for help on using the browser.</p>
<dl>
<dt>
<dd> &lt;<a rel="nofollow" href="https://support.google.com/chrome/">https://support.google.com/chrome/</a>&gt;</dl>
<p> This manpage only describes invocation, environment, and arguments. </p>
<h2>OPTIONS</h2>
<p> Chromium has hundreds of undocumented command-line flags that are added and removed at the whim of the developers. Here, we document relatively stable flags.</p>
<dl>
<dt><code>&#8211;user-data-dir</code>=<i>DIR</i></p>
<dd> Specifies the directory that user data (your &quot;profile&quot;) is kept in. Defaults to <i>~/.config/chromium .</i> Separate instances of Chromium must use separate user data directories; repeated invocations of chromium-browser will reuse an existing process for a given user data directory. </p>
<dt><code>&#8211;app</code>=<i>URL</i></p>
<dd> Runs <i>URL</i> in &quot;app mode&quot;: with no browser toolbars. </p>
<dt><code>&#8211;incognito</code></p>
<dd> Open in incognito mode. </p>
<dt><code>&#8211;proxy-server</code>=<i>host:port</i></p>
<dd> Specify the HTTP/SOCKS4/SOCKS5 proxy server to use for requests. This overrides any environment variables or settings picked via the options dialog. An individual proxy server is specified using the format: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>[&lt;proxy-scheme&gt;://]&lt;proxy-host&gt;[:&lt;proxy-port&gt;] </p>
<p> Where &lt;proxy-scheme&gt; is the protocol of the proxy server, and is one of: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&quot;http&quot;,&nbsp;<wbr>&quot;socks&quot;,&nbsp;<wbr>&quot;socks4&quot;,&nbsp;<wbr>&quot;socks5&quot;. </p>
<p> If the &lt;proxy-scheme&gt; is omitted, it defaults to &quot;http&quot;. Also note that &quot;socks&quot; is equivalent to &quot;socks5&quot;. </p>
<p> Examples: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;proxy-server=&quot;foopy:99&quot;<br />
Use the HTTP proxy&nbsp;<wbr>&quot;foopy:99&quot;&nbsp;<wbr>to load all URLs. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;proxy-server=&quot;<a href="socks://foobar:1080">socks://foobar:1080</a>&quot;<br />
Use the SOCKS v5 proxy&nbsp;<wbr>&quot;foobar:1080&quot;&nbsp;<wbr>to load all URLs. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;proxy-server=&quot;socks4://foobar:1080&quot;<br />
Use the SOCKS v4 proxy&nbsp;<wbr>&quot;foobar:1080&quot;&nbsp;<wbr>to load all URLs. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;proxy-server=&quot;socks5://foobar:66&quot;<br />
Use the SOCKS v5 proxy&nbsp;<wbr>&quot;foobar:66&quot;&nbsp;<wbr>to load all URLs. </p>
<p> It is also possible to specify a separate proxy server for different URL types, by prefixing the proxy server specifier with a URL specifier: </p>
<p> Example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;proxy-server=&quot;https=proxy1:80;http=socks4://baz:1080&quot;<br />
Load&nbsp;<wbr><a rel="nofollow" href="https://*">https://*</a>&nbsp;<wbr>URLs using the HTTP proxy&nbsp;<wbr>&quot;proxy1:80&quot;. And load&nbsp;<wbr><a href="http://*">http://*</a><br />
URLs using the SOCKS v4 proxy&nbsp;<wbr>&quot;baz:1080&quot;. </p>
<dt><code>&#8211;no-proxy-server</code></p>
<dd> Disables the proxy server. Overrides any environment variables or settings picked via the options dialog. </p>
<dt><code>&#8211;proxy-auto-detect</code></p>
<dd> Autodetect proxy configuration. Overrides any environment variables or settings picked via the options dialog. </p>
<dt><code>&#8211;proxy-pac-url</code>=<i>URL</i></p>
<dd> Specify proxy autoconfiguration URL. Overrides any environment variables or settings picked via the options dialog. </p>
<dt><code>&#8211;password-store</code>=&lt;<i>basic</i>|<i>gnome</i>|<i>kwallet</i>&gt;</p>
<dd> Set the password store to use. The default is to automatically detect based on the desktop environment. <i>basic</i> selects the built in, unencrypted password store. <i>gnome</i> selects Gnome keyring. <i>kwallet</i> selects (KDE) KWallet. (Note that KWallet may not work reliably outside KDE.) </p>
<dt><code>&#8211;version</code></p>
<dd> Show version information. </p>
</dl>
<p> As a GTK+ app, Chromium also obeys GTK+ command-line flags, such as <code>&#8211;display</code>. See the GTK documentation for more:</p>
<dl>
<dt>
<dd> &lt;<a rel="nofollow" href="http://library.gnome.org/devel/gtk/stable/gtk-running.html">http://library.gnome.org/devel/gtk/stable/gtk-running.html</a>&gt; &lt;<a rel="nofollow" href="http://library.gnome.org/devel/gtk/stable/gtk-x11.html">http://library.gnome.org/devel/gtk/stable/gtk-x11.html</a>&gt; </p>
</dl>
<h2>ENVIRONMENT</h2>
<p> Chromium obeys the following environment variables: </p>
<dl>
<dt><code>all_proxy</code></p>
<dd> Shorthand for specifying all of <code>http_proxy, https_proxy, ftp_proxy</code> </p>
<dt><code>http_proxy, https_proxy, ftp_proxy</code></p>
<dd> The proxy servers used for HTTP, HTTPS, and FTP. <i>Note:</i> because Gnome/KDE proxy settings may propagate into these variables in some terminals, this variable is ignored (in preference for actual system proxy settings) when running under Gnome or KDE. Use the command-line flags to set these when you want to force their values. </p>
<dt><code>auto_proxy</code></p>
<dd> Specify proxy autoconfiguration. Defined and empty autodetects; otherwise, it should be an autoconfig URL. But see above note about Gnome/KDE. </p>
<dt><code>SOCKS_SERVER</code></p>
<dd> SOCKS proxy server (defaults to SOCKS v4, also set <code>SOCKS_VERSION=5</code> to use SOCKS v5). </p>
<dt><code>no_proxy</code></p>
<dd> Comma separated list of hosts or patterns to bypass proxying. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><i>~/.config/chromium</i></p>
<dd> Default directory for configuration data. </p>
<dt><i>~/.cache/chromium</i></p>
<dd> Default directory for cache data. (Why? See &lt;<a rel="nofollow" href="http://standards.freedesktop.org/basedir-spec/latest/">http://standards.freedesktop.org/basedir-spec/latest/</a>&gt; .) </p>
</dl>
<h2>BUGS</h2>
<p> Bug tracker:</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://code.google.com/p/chromium/issues/list">http://code.google.com/p/chromium/issues/list</a></dl>
<p> Be sure to do your search within &quot;All Issues&quot; before reporting bugs, and be sure to pick the &quot;Defect on Linux&quot; template when filing a new one. </p>
<h2>AUTHOR</h2>
<p> The Chromium team &#8211; &lt;<a rel="nofollow" href="http://www.chromium.org">http://www.chromium.org</a>&gt; </p>
<h2>Index</h2>
