---
title: "globus-personal-gatekeeper(1)"
name: "globus-personal-gatekeeper"
section: "1"
letter: "g"
url: "/docs/linux/man/1-globus-personal-gatekeeper/"
description: "globus-personal-gatekeeper – Manage a user’s personal gatekeeper daemon"
---

<h2 class="name">NAME</h2>
<p> globus-personal-gatekeeper &#8211; Manage a user&#8217;s personal gatekeeper daemon </p>
<h2>SYNOPSIS</h2>
<p> <code>globus-personal-gatekeeper</code> [-help ] [-usage ] [-version ] [-versions ] [-list ] [-directory <i>CONTACT</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>globus-personal-gatekeeper</code> command is a utility which manages a gatekeeper and job manager service for a single user. Depending on the command-line arguments it will operate in one of several modes. In the first set of arguments indicated in the synopsis, the program provides information about the <code>globus-personal-gatekeeper</code> command or about instances of the <code>globus-personal-gatekeeper</code> that are running currently. The second set of arguments indicated in the synopsis provide control over starting a new <code>globus-personal-gatekeeper</code> instance. The final set of arguments provide control for terminating one or more <code>globus-personal-gatekeeper</code> instances. </p>
<p> The <i>-start</i> mode will create a new subdirectory of $HOME/.globus and write the configuration files needed to start a and write the configuration files needed to start a <code>globus-gatekeeper</code> daemon which will invoke the <code>globus-job-manager</code> service when new authenticated connections are made to its service port. The <code>globus-personal-gatekeeper</code> then exits, printing the contact string for the new gatekeeper prefixed by GRAM contact: to standard output. In addition to the arguments described above, any arguments described in <code><a href="/docs/linux/man/8-globus-job-manager/">globus-job-manager</a>(8)</code> can be appended to the command-line and will be added to the job manager configuration for the service started by the <code>globus-gatekeeper</code>. </p>
<p> The new <code>globus-gatekeeper</code> will continue to run in the background until killed by invoking <code>globus-personal-gatekeeper</code> with the <i>-kill</i> or <i>-killall</i> argument. When killed, it will kill the <code>globus-gatekeeper</code> and <code>globus-job-manager</code> processes, remove state files and configuration data, and then exit. Jobs which are running when the personal gatekeeper is killed will continue to run, but their job directory will be destroyed so they may fail in the LRM. </p>
<p> The full set of command-line options to <code>globus-personal-gatekeeper</code> consists of: </p>
<p> <code>-help, -usage</code></p>
<dl>
<dt>
<dd> Print command-line option summary and exit</dl>
<p> <code>-version</code></p>
<dl>
<dt>
<dd> Print software version</dl>
<p> <code>-versions</code></p>
<dl>
<dt>
<dd> Print software version including DiRT information</dl>
<p> <code>-list</code></p>
<dl>
<dt>
<dd> Print a list of all currently running personal gatekeepers. These entries will be printed one per line.</dl>
<p> <code>-directory </code><i>CONTACT</i></p>
<dl>
<dt>
<dd> Print the configuration directory for the personal gatekeeper with the contact string <i>CONTACT</i>.</dl>
<p> <code>-debug</code></p>
<dl>
<dt>
<dd> Print additional debugging information when starting a personal gatekeeper. This option is ignored in other modes.</dl>
<p> <code>-start</code></p>
<dl>
<dt>
<dd> Start a new personal gatekeeper process.</dl>
<p> <code>-jmtype </code><i>LRM</i></p>
<dl>
<dt>
<dd> Use <i>LRM</i> as the local resource manager interface. If not provided when starting a personal gatekeeper, the job manager will use the default fork LRM.</dl>
<p> <code>-auditdir </code><i>AUDIT_DIRECTORY</i></p>
<dl>
<dt>
<dd> Write audit report files to <i>AUDIT_DIRECTORY</i>. If not provided, the job manager will not write any audit files.</dl>
<p> <code>-port </code><i>PORT</i></p>
<dl>
<dt>
<dd> Listen for gatekeeper TCP/IP connections on the port <i>PORT</i>. If not provided, the gatekeeper will let the operating system choose.</dl>
<p> <code>-log[=</code><i>DIRECTORY</i><code>]</code></p>
<dl>
<dt>
<dd> Write job manager log files to <i>DIRECTORY</i>. If <i>DIRECTORY</i> is omitted, the default of $HOME will be used. If this option is not present, the job manager will not write any log files. will be used. If this option is not present, the job manager will not write any log files.</dl>
<p> <code>-seg</code></p>
<dl>
<dt>
<dd> Try to use the SEG mechanism to receive job state change information, instead of polling for these. These require either the system administrator or the user to run an instance of the <code>globus-job-manager-event-generator</code> program for the LRM specified by the <i>-jmtype</i> option.</dl>
<p> <code>-acctfile </code><i>ACCOUNTING_FILE</i></p>
<dl>
<dt>
<dd> Write gatekeeper accounting entries to <i>ACCOUNTING_FILE</i>. If not provided, no accounting records are written.</dl>
<h2>EXAMPLES</h2>
<p> This example shows the output when starting a new personal gatekeeper which will schedule jobs via the lsf LRM, with debugging enabled. </p>
<dl>
<dt>
<dd>
<pre>
% globus-personal-gatekeeper -start -jmtype lsf
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
verifying setup...
done.
GRAM contact: personal-grid.example.org:57846:/DC=org/DC=example/CN=Joe User
</pre>
</dl>
<p> This example shows the output when listing the current active personal gatekeepers. </p>
<dl>
<dt>
<dd>
<pre>
%  globus-personal-gatekeeper -list
personal-grid.example.org:57846:/DC=org/DC=example/CN=Joe User
</pre>
</dl>
<p> This example shows the output when querying the configuration directory for the above personal gatekeeper. gatekeepers. </p>
<dl>
<dt>
<dd>
<pre>
%  globus-personal-gatekeeper -directory &quot;personal-grid.example.org:57846:/DC=org/DC=example/CN=Joe User&quot;
/home/juser/.globus/.personal-gatekeeper.personal-grid.example.org.1337
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
%  globus-personal-gatekeeper -kill &quot;personal-grid.example.org:57846:/DC=org/DC=example/CN=Joe User&quot;
killing gatekeeper: &quot;personal-grid.example.org:57846:/DC=org/DC=example/CN=Joe User&quot;
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-globusrun/">globusrun</a>(1), <a href="/docs/linux/man/8-globus-job-manager/">globus-job-manager</a>(8), <a href="/docs/linux/man/8-globus-gatekeeper/">globus-gatekeeper</a>(8)</p>
<h2>AUTHOR</h2>
<p> Copyright &#169; 1999-2016 University of Chicago </p>
<h2>Index</h2>
