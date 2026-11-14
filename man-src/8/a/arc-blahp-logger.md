---
title: "arc-blahp-logger(8)"
name: "arc-blahp-logger"
section: "8"
letter: "a"
url: "/docs/linux/man/8-arc-blahp-logger/"
description: "arc-blahp-logger – ARC authplugin to store BLAH accouting logs about FINISHED jobs"
---

<p>arc-blahp-logger &#8211; ARC authplugin to store BLAH accouting logs about FINISHED jobs </p>
<h2>Description</h2>
<p><code>ARC BLAH logger </code> is an authplugin to store FINISHED jobs information in log files used by BLAH parser. Generated logs can be used by APEL/DGAS client tools to send accounting information. </p>
<h2>Synopsis</h2>
<p>arc-blahp-logger -I &lt;jobID&gt; -U &lt;user&gt; -P &lt;proxy file&gt; -L &lt;job status file&gt; [-c &lt;ceid prefix&gt;] [-p &lt;log prefix&gt; ] [-d &lt;log level&gt;] </p>
<h2>Options</h2>
<dl>
<dt><code>-I</code> <i>jobID</i></p>
<dd>A-REX job identifier</p>
<dt><code>-U</code> <i>user</i></p>
<dd>local account that own the job files and processes</p>
<dt><code>-P</code> <i>user proxy</i></p>
<dd>path to user proxy certificate file to get VOMS membership info</p>
<dt><code>-L</code> <i>job status file</i></p>
<dd>A-REX jobstatus .local file containint more info about job (like LRMS id)</p>
<dt><code>-c</code> <i>ceid prefix</i></p>
<dd>prefix to generate CE ID in accordance to GLUE1.3 publishing</p>
<dt><code>-p</code> <i>log prefix</i></p>
<dd>logs location and filename prefix. Default is <code>/var/log/arc/accounting/blahp.log</code></p>
<dt><code>-d</code> <i>loglevel</i></p>
<dd>logging level from 0(ERROR) to 5(DEBUG) </p>
</dl>
<h2>Enabling Plugin In A-Rex Configuration</h2>
<p>You need to add BLAH logger plugin as a handler for FINISHED state, e.g.: </p>
<p> <code>authplugin=FINISHED timeout=10,onfailure=pass /usr/libexec/arc/arc-blahp-logger -I %I -U %u -L %C/job.%I.local -P %C/job.%I.proxy</code></p>
<h2>Configuration</h2>
<p>There are no particular plugin configuration except passing correct options. </p>
<p> By default BLAH log is written to <code>/var/log/arc/accounting/blahp.log-YYYYMMDD. </code> The log prefix (without <code>-YYYYMMDD</code>) can be redefined with optional <code>-p</code> option. </p>
<p> CE ID is generated automatically and has a format <code>host.fqdn:2811/nordugrid-torque-queue</code> in accordance to GLUE1.3 publishing. Queue is added in runtime anyway, but prefix can be redefined with <code>-c</code> option. This option should be added in case of LRMS. </p>
<p> To debug logger execution you can add <code>-d 5</code> option and see all ARC logger output from all subsystems used.</p>
<h2>Author</h2>
<p>Andrii Salnikov &lt;manf at grid dot org dot ua&gt;</p>
