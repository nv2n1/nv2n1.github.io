---
title: "mailstats(8)"
name: "mailstats"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mailstats/"
description: "mailstats – display mail statistics"
---

<p>mailstats &#8211; display mail statistics</p>
<h2>Synopsis</h2>
<p><code>mailstats</code> [<code>-c</code>] [<code>-o</code>] [<code>-p</code>] [<code>-P</code>] [<code>-C</code> <i>cffile</i>] [<code>-f</code> <i>stfile</i>]</p>
<h2>Description</h2>
<p>The <code>mailstats</code> utility displays the current mail statistics. </p>
<p> First, the time at which statistics started being kept is displayed, in the format specified by <a href="/docs/linux/man/3-ctime/">ctime</a>(3). Then, the statistics for each mailer are displayed on a single line, each with the following white space separated fields: </p>
<dl>
<dd>
</dd><dl>
<dt><code>M</code></dt>
<dd>The mailer number.</dd>
<dt><code>msgsfr</code></dt>
<dd>Number of messages from the mailer.</dd>
<dt><code>bytes_from</code></dt>
<dd>Kbytes from the mailer.</dd>
<dt><code>msgsto</code></dt>
<dd>Number of messages to the mailer.</dd>
<dt><code>bytes_to</code></dt>
<dd>Kbytes to the mailer.</dd>
<dt><code>msgsrej</code></dt>
<dd>Number of messages rejected.</dd>
<dt><code>msgsdis</code></dt>
<dd>Number of messages discarded.</dd>
<dt><code>msgsqur</code></dt>
<dd>Number of messages quarantined.</dd>
<dt><code>Mailer</code></dt>
<dd>The name of the mailer.</dd></dl>
</dl>
<p> After this display, a line totaling the values for all of the mailers is displayed (preceded with a &#8220;T&#8221;), separated from the previous information by a line containing only equals (&#8220;=&#8221;) characters. Another line preceded with a &#8220;C&#8221; lists the number of TCP connections. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-C</code></dt>
<dd>Read the specified file instead of the default <code>sendmail</code> configuration file.</dd>
<dt><code>-c</code></dt>
<dd>Try to use submit.cf instead of the default <code>sendmail</code> configuration file.</dd>
<dt><code>-f</code></dt>
<dd>Read the specified statistics file instead of the statistics file specified in the <code>sendmail </code> configuration file.</dd>
<dt><code>-P</code></dt>
<dd>Output information in program-readable mode without clearing statistics.</dd>
<dt><code>-p</code></dt>
<dd>Output information in program-readable mode and clear statistics.</dd>
<dt><code>-o</code></dt>
<dd>Don&#8217;t display the name of the mailer in the output.</dd></dl>
<p> The <code>mailstats</code> utility exits 0 on success, and &gt;0 if an error occurs.</p>
<h2>Files</h2>
<dl>
<dt>/etc/mail/sendmail.cf</dt>
<dd>The default <code>sendmail</code> configuration file.</dd>
<dt>/var/log/mail/statistics</dt>
<dd>The default <code>sendmail</code> statistics file.</dd></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-mailq/">mailq</a>(1), sendmail(8) </p>
