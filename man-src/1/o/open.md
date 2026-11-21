---
title: "open(1)"
name: "open"
section: "1"
letter: "o"
url: "/docs/linux/man/1-open/"
description: "xdg-open – opens a file or URL in the user’s preferred application"
---

<h2 class="name">NAME</h2>
<p> xdg-open &#8211; opens a file or URL in the user&#8217;s preferred application </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>xdg-open</code> {<i>file</i> | <i>URL</i>}</dt>
<dt> <code>xdg-open</code> {<code>&#8211;help</code> | <code>&#8211;manual</code> | <code>&#8211;version</code>}</dt></dl>
<h2>DESCRIPTION</h2>
<dd>xdg-open opens a file or URL in the user&#8217;s preferred application. If a URL is provided the URL will be opened in the user&#8217;s preferred web browser. If a file is provided the file will be opened in the preferred application for files of that type. xdg-open supports file, ftp, http and https URLs. </dd>
<p> xdg-open is for use inside a desktop session only. It is not recommended to use xdg-open as root.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Show command synopsis.</dd></dl>
<p> <code>&#8211;manual</code></p>
<dl>
<dt>
</dt><dd> Show this manual page.</dd></dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
</dt><dd> Show the xdg-utils version information.</dd></dl>
<h2>EXIT CODES</h2>
<p> An exit code of 0 indicates success while a non-zero exit code indicates failure. The following failure codes can be returned: </p>
<p> <code>1</code></p>
<dl>
<dt>
</dt><dd> Error in command line syntax.</dd></dl>
<p> <code>2</code></p>
<dl>
<dt>
</dt><dd> One of the files passed on the command line did not exist.</dd></dl>
<p> <code>3</code></p>
<dl>
<dt>
</dt><dd> A required tool could not be found.</dd></dl>
<p> <code>4</code></p>
<dl>
<dt>
</dt><dd> The action failed.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xdg-mime/">xdg-mime</a></code>(1), <code><a href="/docs/linux/man/1-xdg-settings/">xdg-settings</a></code>(1), m[blue]<code>MIME applications associations specification</code>m[]<font SIZE="-2">[1]</font></p>
<h2>EXAMPLES</h2>
<dl>
<dt>
</dt><dd>
<pre>
xdg-open '<a rel="nofollow" href="http://www.freedesktop.org/'">http://www.freedesktop.org/'</a>
</pre>
</dd></dl>
<p> Opens the freedesktop.org website in the user&#8217;s default browser. </p>
<dl>
<dt>
</dt><dd>
<pre>
xdg-open /tmp/foobar.png
</pre>
</dd></dl>
<p> Opens the PNG image file /tmp/foobar.png in the user&#8217;s default image viewing application.</p>
<h2>AUTHORS</h2>
<p> <code>Kevin Krammer</code></p>
<dl>
<dt>
</dt><dd> Author.</dd></dl>
<p> <code>Jeremy White</code></p>
<dl>
<dt>
</dt><dd> Author.</dd></dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2006 </p>
<h2>NOTES</h2>
<dl>
<dt> 1.</dt>
<dd> MIME applications associations specification</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.freedesktop.org/wiki/Specifications/mime-apps-spec/">http://www.freedesktop.org/wiki/Specifications/mime-apps-spec/</a></dd></dl>
</dl>
