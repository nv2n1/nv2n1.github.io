---
title: "unopkg(1)"
name: "unopkg"
section: "1"
letter: "u"
url: "/docs/linux/man/1-unopkg/"
description: "unopkg – LibreOffice Extension Manager"
---

<h2>Name</h2>
<p> unopkg &#8211; LibreOffice Extension Manager</p>
<h2>SYNOPSIS</h2>
<p> <code>unopkg</code> [<code>add</code>] &lt;<i>options</i>&gt; <i>extension-path&#8230;</i><br />
 <code>unopkg</code> [<code>remove</code>] &lt;<i>options</i>&gt; <i>extension-identifier&#8230;</i><br />
 <code>unopkg</code> [<code>list</code>] &lt;<i>options</i>&gt; <i>extension-identifier&#8230;</i><br />
 <code>unopkg</code> [<code>reinstall</code>] &lt;<i>options</i>&gt;<br />
 <code>unopkg</code> [<code>gui</code>]<br />
 <code>unopkg</code> [<code>&#8211;help</code>|<code>-h</code>] </p>
<h2>DESCRIPTION</h2>
<p> LibreOffice is a fully featured office suite for the daily use with all features you would normally expect in an office suite. </p>
<p> There exists many LibreOffice extensions all over the world. For example, see <code><a rel="nofollow" href="https://extensions.libreoffice.org/">https://extensions.libreoffice.org/</a></code> </p>
<p> This tool allows managing the extensions from the command line. </p>
<h2>SUB-COMMANDS</h2>
<dl>
<dt><code>add</code></p>
<dd> add the given extensions</p>
<dt><code>remove</code></p>
<dd> remove extensions by the given identifiers</p>
<dt><code>reinstall</code></p>
<dd> reinstall all deployed extensions (only for experts)</p>
<dt><code>list</code></p>
<dd> list information about the deployed extensions</p>
<dt><code>gui</code></p>
<dd> raise Extension Manager Graphical User Interface (GUI) </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code>|<code>-h</code></p>
<dd> display help and exit</p>
<dt><code>&#8211;version</code>|<code>-V</code></p>
<dd> output version information and exit</p>
<dt><code>&#8211;verbose</code>|<code>-v</code></p>
<dd> verbose output</p>
<dt><code>&#8211;force</code>|<code>-f</code></p>
<dd> force overwriting existing extensions</p>
<dt><code>&#8211;log-file</code> &lt;<i>file</i>&gt;</p>
<dd> custom log file; the default one is &lt;cache-dir&gt;/log.txt</p>
<dt><code>&#8211;shared</code>|<code>-f</code></p>
<dd> operate on the system installation deployment context; use only when no concurrent Office process(es) are running! (only for experts)</p>
<dt><code>&#8211;deployment-context</code> &lt;<i>context</i>&gt;</p>
<dd> operate on explicit deployment context (only for experts) </p>
</dl>
<h2>TROUBLESHOOTING PROBLEMS</h2>
<p> See <code><a rel="nofollow" href="http://wiki.documentfoundation.org/BugReport">http://wiki.documentfoundation.org/BugReport</a></code> for more details about how to report bugs in LibreOffice.</p>
<h2>SEE ALSO</h2>
<p> <code><a rel="nofollow" href="http://www.documentfoundation.org/">http://www.documentfoundation.org/</a></code></p>
<h2>AUTHOR</h2>
<p> This manual page was created by Petr Mladek &lt;pmladek [at] suse.cz&gt;. </p>
<h2>Index</h2>
