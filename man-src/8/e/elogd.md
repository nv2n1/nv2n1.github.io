---
title: "elogd(8)"
name: "elogd"
section: "8"
letter: "e"
url: "/docs/linux/man/8-elogd/"
description: "elogd – web server program for Electronic Logbook ELOG"
---

<p>elogd &#8211; web server program for Electronic Logbook ELOG</p>
<h2>Synopsis</h2>
<p><code>elog</code> [ <code>-C </code><i>url</i> ] [ <code>-c </code><i>file</i> ] [ <code>-D</code> ] [ <code>-d </code><i>directory</i> ] [ <code>-f </code><i>file</i> ] [ <code>-k</code> ] [ <code>-l </code><i>logbook</i> ] [ <code>-M</code> ] [ <code>-m</code> ] [ <code>-n </code><i>hostname</i> ] [ <code>-p </code><i>port</i> ] [ <code>-S</code> ] [ <code>-s </code><i>directory</i> ] [ <code>-v</code> ] [ <code>-x</code> ] </p>
<h2>Description</h2>
<p>The Electronic Logbook <code>ELOG</code> can be used to store and retrieve messages through a Web interface. Depending on the configuration, the <code>ELOG</code> system can host one or more logbooks which are stored in separate sections on the server. <code>elogd</code> is the daemon program serving as a simple web server for the <code>ELOG</code> system.</p>
<h2>Options</h2>
<p><code>elogd</code> accepts the following options:</p>
<dl>
<dt><code>-C</code><i> url</i></dt>
<dd>clone remote elogd configuration</dd>
<dt><code>-c</code><i> file</i></dt>
<dd>specify configuration file</dd>
<dt><code>-D</code></dt>
<dd>become a daemon</dd>
<dt><code>-d</code><i> directory</i></dt>
<dd>specify logbook root directory</dd>
<dt><code>-f</code><i> file</i></dt>
<dd>specify PID file</dd>
<dt><code>-M</code></dt>
<dd>synchronize with removing deleted entries</dd>
<dt><code>-m</code></dt>
<dd>synchronize logbook(s) with remote server</dd>
<dt><code>-n</code><i> host</i></dt>
<dd>host where <code>elogd</code> will run</dd>
<dt><code>-k</code></dt>
<dd>do not use keep-alive</dd>
<dt><code>-l</code><i> logbook</i></dt>
<dd>specify logbook for `-r&#8217; and `-w&#8217; commands</dd>
<dt><code>-p</code><i> port</i></dt>
<dd>port where <code>elogd</code> will run</dd>
<dt><code>-S</code></dt>
<dd>be silent</dd>
<dt><code>-s</code><i> directory</i></dt>
<dd>specify resource directory (eg. themes, icons)</dd>
<dt><code>-v</code></dt>
<dd>debugging output</dd>
<dt><code>-x</code></dt>
<dd>enable execution of shell commands (unless compiled with this feature)</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-elog/">elog</a></code>(1). </p>
<p> The full documentation for <code>ELOG</code> is maintained as an html manual. You can reach it from the package document directory.</p>
<h2>Warnings</h2>
<p><code>elogd</code> is run under a separate user/group <i>elog</i> , by default. You might change it via <i>Usr</i> and <i>Grp</i> options in configuration file. The configuration and stylesheet files should be readable by that user. </p>
<p> Passwords are transferred over the network in plain text and therefore, are not secure. So if passwords are used <code>elogd</code> should be started with the SSL option in the configuration file for secure connections.</p>
<h2>Author</h2>
<p>Written by Stefan Ritt &lt;stefan.ritt [at] psi.ch&gt;. </p>
<p> This manual page was written by Recai Oktas &lt;roktas [at] omu.edu.tr&gt;, for the Debian GNU/Linux system (but may be used by others).</p>
