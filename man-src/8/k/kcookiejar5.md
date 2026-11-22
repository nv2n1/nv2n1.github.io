---
title: "kcookiejar5(8)"
name: "kcookiejar5"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kcookiejar5/"
description: "kcookiejar5 – Command line interface to the KDE HTTP cookie daemon"
---

<p>kcookiejar5 &#8211; Command line interface to the KDE HTTP cookie daemon</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>kcookiejar5</code> [-h, &#8211;help] [-v, &#8211;version] [&#8211;shutdown] [&#8211;remove<i>&nbsp;<wbr>domain</i>] [&#8211;remove-all] [&#8211;reload-config]</dt></dl>
<h2>Description</h2>
<p><code>kcookiejar5</code></p>
<dd>is a command line interface to the HTTP cookie store used by KDE, a D-BUS service to store/retrieve/clean cookies.</dd>
<h2>Options</h2>
<p><code>-h</code><code>&#8211;help</code></p>
<dl>
<dd>Show help about options.</dd></dl>
<p> <code>-v</code><code>&#8211;version</code></p>
<dl>
<dd>Show version information</dd></dl>
<p> <code>&#8211;shutdown</code></p>
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
<p><code>kcookiejar5</code> is a command line tool to access the kded module which manages cookies in <code>Konqueror</code> and other KDE applications. </p>
<p> When started without parameters it loads the kded module to provide the dbus interface to store cookies. </p>
<p> When <code>kcookiejar5</code> is started with some parameters, it does additional tasks to the cookies jar it provides, like removing the cookies from one <i>domain</i>.</p>
<h2>See Also</h2>
<p><i>kf5options</i>(7), <i>qt5options</i>(7)</p>
<h2>Bugs</h2>
<p>Please use m[blue]<code>KDE&#8217;s bugtracker</code>m[][1] to report bugs.</p>
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
<dd>KDE&#8217;s bugtracker</dd>
<dl>
<dd><a rel="nofollow" href="http://bugs.kde.org">http://bugs.kde.org</a></dd></dl>
</dl>