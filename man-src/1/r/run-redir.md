---
title: "run-redir(1)"
name: "run-redir"
section: "1"
letter: "r"
url: "/docs/linux/man/1-run-redir/"
description: "run-redir – run program but redirect some resulting files"
---

<h2>NAME</h2>
<p> run-redir &#8211; run program but redirect some resulting files</p>
<h2>SYNOPSIS</h2>
<p> <code>run-redir</code> <i>COMMAND-TO-RUN</i> </p>
<p> <code>run-redir -p | &#8211;print</code></p>
<h2>DESCRIPTION</h2>
<p> This program is intended to make it possible to run install scripts that do not support the DESTDIR convention, and yet have their resulting files redirected elsewhere. Where possible, use make-redir instead, as that provides a simpler higher-level interface for common cases. </p>
<p> In the first form, run the COMMAND-TO-RUN, but wrap certain programs so that any files they write will be redirected to a different subdirectory if they were to have been stored in a privileged directory (like &quot;/usr/bin&quot;). The different subdirectory is specified by REDIR_DESTDIR or DESTDIR, with the former taking precedence. </p>
<p> With the &quot;-p&quot; or &quot;&#8211;print&quot; option, just print the directory containing the redirecting (wrapping) scripts and exit. The run-redir program is installed with a default value of the directory containing the wrapping scripts; you can override this default by setting the environment variable RUN_REDIR_SCRIPTDIR to point to a different directory of wrapping scripts. </p>
<p> See <a href="/docs/linux/man/1-make-redir/">make-redir</a>(1) for much more information on this program. More background information is here: <a rel="nofollow" href="http://www.dwheeler.com/essays/automating-destdir.html">http://www.dwheeler.com/essays/automating-destdir.html</a></p>
<h2>AUTHOR</h2>
<p> David A. Wheeler</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;dwheeler, at, dwheeler dot com&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2009 Institute for Defense Analyses. Released under the &quot;MIT&quot; license.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-make-redir/">make-redir</a>(1) </p>
<h2>Index</h2>
