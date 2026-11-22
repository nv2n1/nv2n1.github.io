---
title: "kcookiejar4(8)"
name: "kcookiejar4"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kcookiejar4/"
description: "kcookiejar4 – KDE HTTP cookie daemon"
---

<p>kcookiejar4 &#8211; KDE HTTP cookie daemon</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>kcookiejar4</code> [&#8211;help] [Generic-options] [Qt-options] [KDE-options] [&#8211;shutdown] [&#8211;remove<i>&nbsp;<wbr>domain</i>] [&#8211;remove-all] [&#8211;reload-config]</dt></dl>
<h2>Description</h2>
<p><code>kcookiejar4</code></p>
<dd>handles the HTTP cookies providing a D-BUS service to store/retrieve/clean cookies.</dd>
<h2>Generic Options</h2>
<p><code>&#8211;author</code></p>
<dl>
<dd>Show author information.</dd></dl>
<p> <code>&#8211;help</code></p>
<dl>
<dd>Show help about options.</dd></dl>
<p> <code>&#8211;help-all</code></p>
<dl>
<dd>Show all options.</dd></dl>
<p> <code>&#8211;help-kde</code></p>
<dl>
<dd>Show KDE specific options.</dd></dl>
<p> <code>&#8211;help-qt</code></p>
<dl>
<dd>Show Qt specific options.</dd></dl>
<p> <code>&#8211;license</code></p>
<dl>
<dd>Show license information.</dd></dl>
<p> <code>-v</code><code>&#8211;version</code></p>
<dl>
<dd>Show version information</dd></dl>
<h2>Application Options</h2>
<p><code>&#8211;shutdown</code></p>
<dl>
<dd>Shut down cookie jar and the D-BUS service.</dd></dl>
<p> <code>&#8211;remove</code> <i>domain</i></p>
<dl>
<dd>Removes cookies for <i>domain</i> from the cookie jar.</dd></dl>
<p> <code>&#8211;remove-all</code></p>
<dl>
<dd>Removes all the cookies from the cookie jar.</dd></dl>
<p> <code>&#8211;reaload-config</code></p>
<dl>
<dd>Reloads the configuration file.</dd></dl>
<h2>Usage</h2>
<p>KDE web browser <code>konqueror</code> uses <code>kcookiejar4</code> for storing and managing cookies using the D-Bus service <code>kcookiejar4</code> provides. </p>
<p> When <code>kcookiejar4</code> is started without parameters, it provides a D-BUS service to handle HTTP cookies. </p>
<p> When <code>kcookiejar4</code> is started with some parameters, it does additional tasks to the cookies jar it provides, like removing the cookies from one <i>domain</i>.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/7-kdeoptions/">kdeoptions</a></i>(7), <i><a href="/docs/linux/man/7-qtoptions/">qtoptions</a></i>(7)</p>
<h2>Bugs</h2>
<p>There are probably tons of bugs. Use m[blue]<code>bugs.kde.org</code>m[][1] to report them.</p>
<h2>Authors</h2>
<p><code>Waldo Bastian</code> &lt;bastian [at] kde.org&gt;</p>
<dl>
<dd>Author.</dd></dl>
<p> <code>Dawit Alemayehu</code> &lt;adawit [at] kde.org&gt;</p>
<dl>
<dd>Author.</dd></dl>
<h2>Notes</h2>
<dl>
<dt> 1.</dt>
<dd>bugs.kde.org</dd>
<dl>
<dd><a rel="nofollow" href="http://bugs.kde.org">http://bugs.kde.org</a></dd></dl>
</dl>