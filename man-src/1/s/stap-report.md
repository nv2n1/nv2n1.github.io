---
title: "stap-report(1)"
name: "stap-report"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stap-report/"
description: "stap-report – collect system information that is useful for debugging systemtap bugs"
---

<h2>NAME</h2>
<p> stap-report &#8211; collect system information that is useful for debugging systemtap bugs </p>
<h2>SYNOPSIS</h2>
<p> <code>stap-report</code> </p>
<h2>DESCRIPTION</h2>
<p> The stap-report executable collects system information that is useful for debugging systemtap bugs. It is a good idea to include such a report in bug reports especially if you send them directly to the upstream. stap-report can be run either as a normal user or as root. The report will be more complete if stap-report is run as root. </p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre><code>
$ stap - report &gt; report.txt
                      $ head report.txt ==
    id ==
    uid = 1000(user)gid = 1000(user)groups = 122(stapdev),
    123(stapusr), 129(stapsys) == stap - V == Systemtap translator / driver(version 2.2.1 / 0.153, Debian version 2.2.1 - 1) Copyright(C) 2005 - 2013 Red Hat, Inc.and others This is free software; see the source for copying conditions.
enabled features: AVAHI LIBSQLITE3 NSS TR1_UNORDERED_MAP NLS
== which stap ==
/usr/bin/stap
== locate --regex '/stap(run)?$' | xargs ls -ald ==
</code></pre>
</dl>
<h2>SEE ALSO</h2>
<pre>
<i><a href="//www.systutorials.com/docs/linux/man/1-stap/">stap</a></i>(1)
</pre>
<h2>BUGS</h2>
<p> Use the Bugzilla link of the project web page or our mailing list. <code><a rel="nofollow" href="http://sourceware.org/systemtap/">http://sourceware.org/systemtap/</a></code>,<code>&lt;systemtap [at] sourceware.org&gt;</code>. </p>
<h2>Index</h2>
