---
title: "sagator(8)"
name: "sagator"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sagator/"
description: "sagator – an email/web antivirus/antispam gateway"
---

<p>sagator &#8211; an email/web antivirus/antispam gateway</p>
<h2>Synopsis</h2>
<p><code>sagator</code> [&#8211;help] [&#8211;config filename] [&#8211;nodaemon] [&#8211;logfile logfilename] [&#8211;debug level]</p>
<h2>Description</h2>
<p>This program is an email/web antivirus/antispam gateway. It is an interface to the postfix, sendmail (or any other smtpd), which runs antivirus and/or spamchecker. It also can be used as http proxy with filtering abilities. Its modular architecture can use any combination of antivirus/spamchecker according to configuration.</p>
<h2>Options</h2>
<dl>
<dt>-h, &#8211;help</p>
<dd>Display a short help text.</p>
<dt>-c, &#8211;config=filename</p>
<dd>Load &quot;filename&quot; as alternate config. This filename must be without &quot;.py&quot; extension.</p>
<dt>-n, &#8211;nodaemon</p>
<dd>Don&#8217;t fork into background after startup. It also implicitly set logfile to stdout. You can change this as next parameter after &#8211;nodaemon.</p>
<dt>-l, &#8211;logfile=logfilename</p>
<dd>Filename to store logs. If it is set to &quot;-&quot;, standard output will be used.</p>
<dt>&#8211;debug=level</p>
<dd>Set debug level to &quot;level&quot;. You can specifi level from 0 to 9. Levels over 9 are dangerous. Please do not use them, if you do not know what are you doing.</p>
<dt>&#8211;test</p>
<dd>Test configuration and exit.</p>
<dt>&#8211;kill</p>
<dd>Kill all processes and wait for pid file removation.</p>
<dt>&#8211;wait</p>
<dd>Wait for pid file removation.</dl>
<h2>Author</h2>
<p>Jan ONDREJ (SAL) &lt;ondrejj (at) salstar.sk&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-sgscan/">sgscan</a>(1), <a href="/docs/linux/man/1-sgfilter/">sgfilter</a>(1), <a href="/docs/linux/man/8-sqback/">sqback</a>(8) </p>
