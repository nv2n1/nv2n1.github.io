---
title: "qtcsh(1)"
name: "qtcsh"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qtcsh/"
description: "qtcsh – tcsh with transparent remote execution by use of qrsh"
---

<h2 class="name">NAME</h2>
<p> qtcsh &#8211; tcsh with transparent remote execution by use of qrsh </p>
<h2>SYNTAX</h2>
<p> <code>qtcsh</code> [ <code>tcsh options</code> | <code>-ABLR</code> ]</p>
<h2>DESCRIPTION</h2>
<p> <i>Qtcsh</i> is an extension to the popular derivative <i>tcsh</i>. It allows the transparent remote execution of commands entered in <i>qtcsh</i> controlled via xxQS_NAMExx. <i>Qtcsh</i> can be used as interactive command interpreter as well as for the processing of <i>tcsh</i> shell scripts. </p>
<p> When invoked, <i>qtcsh</i> identifies which commands are to be run remotely and which are not. For this purpose the files &lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/common/qtask and ~/.qtask are processed. Each line in these files defines a command that is intended to be run remotely (see for a definition of the file format). The .qtask file in the user&#8217;s home directory contains the user&#8217;s remote task specification, while the file in the common directory is maintained by the administrator and defines a cluster-wide default behavior. The contents of the administrator supplied file are completely overridden in case there is an appropriate entry in the users file. This is prevented in case an exclamation mark is prefixed to the command name in the administrators qtask file. </p>
<p> <i>Qtcsh</i> always attempts to start the designated tasks remotely via Exceptions are</p>
<dl>
<dt>&bull;</p>
<dd> if the user enters such commands via a relative or absolute pathname instead of the stand-alone command name (see for more information);</p>
<dt>&bull;</p>
<dd> if the environment variable JOB_ID is set and thus <i>qtcsh</i> assumes that execution already happens remotely within a xxQS_NAMExx job and thus executes tasks locally. This avoids unwanted recursions but can be overridden by the command-line option <code>-R</code> and the built-in command <i>qrshmode -R</i> (see corresponding descriptions below);</p>
<dt>&bull;</p>
<dd> if <i>qtcsh</i> cannot establish a connection of xxQS_NAMExx during start-up. This allows using <i>qtcsh</i> as a login shell without the danger of being blocked when no xxQS_NAMExx service is available.</dl>
<p> <i>Qtcsh</i> can operate in three different modes determining whether</p>
<dl>
<dt>&bull;</p>
<dd> tasks are executed remotely;</p>
<dt>&bull;</p>
<dd> immediate or batch execution is requested;</p>
<dt>&bull;</p>
<dd> status output is verbose or only in case of any errors.</dl>
<p> These modes either can be controlled by the command-line switches described below during <i>qtcsh</i> invocation or within an executing <i>qtcsh</i> via the built-in command <i>qrshmode</i>, as described in section <code>BUILT-IN COMMANDS</code>.</p>
<h2>OPTIONS</h2>
<p> The options listed below are specific to <i>qtcsh</i>. The user is referred to the documentation for the explanation of further options. </p>
<dl>
<dt><code>-A</code></p>
<dd> Switches <i>qtcsh</i> into verbose mode, causing diagnostic output in case of remote execution.</p>
<dt><code>-B</code></p>
<dd> Switches remote task execution into batch mode. Tasks submitted to xxQS_NAMExx will be queued if they cannot start immediately. As a consequence, <i>qtcsh</i> may block until the queued task can be started by xxQS_NAMExx. While this behavior probably is undesirable during an interactive session, it may be very useful for execution of shell scripts through <i>qtcsh</i>, as it avoids failure of the scripts due to temporarily unavailable resources for particular tasks.</p>
<dt><code>-L</code></p>
<dd> Switches off the default behavior of remote execution of commands. Causes all commands to be executed locally even if they are contained in one of the files.</p>
<dt><code>-R</code></p>
<dd> Enforces remote execution of commands even if JOB_ID is set as environment variable.</dl>
<h2>BUILT-IN COMMANDS</h2>
<p> This section only describes additional shell builtin commands which are not available in standard </p>
<dl>
<dt><code>qrshmode</code> [<code>-ANBILR</code>]</p>
<dd> Without options, the current operational mode of <i>qtcsh</i> is displayed. The options have the following effect: </p>
<pre><code>
- A switch to verbose output mode - N switch to non - verbose output mode - B switch to batch execution mode - I switch to immediate execution mode - L always execute commands locally - R execute configured commands remotely
</code></pre>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>xxQS_NAME_Sxx_ROOT</code></p>
<dd> Specifies the location of the xxQS_NAMExx standard configuration files.</p>
<dt><code>xxQS_NAME_Sxx_CELL</code></p>
<dd> If set, specifies the default xxQS_NAMExx cell. To address a xxQS_NAMExx cell <i>qtcsh</i> uses (in the order of precedence): </p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> The name of the cell specified in the environment variable xxQS_NAME_Sxx_CELL, if it is set. </p>
<p> The name of the default cell, i.e. <code>default</code>. </p>
</dl>
</dl>
<dt><code>xxQS_NAME_Sxx_DEBUG_LEVEL</code></p>
<dd> If set, specifies that debug information should be written to stderr. In addition the level of detail in which debug information is generated is defined.</p>
<dt><code>xxQS_NAME_Sxx_QMASTER_PORT</code></p>
<dd> If set, specifies the tcp port on which is expected to listen for communication requests. Most installations will use a services map entry for the service &quot;sge_qmaster&quot; instead to define that port.</p>
<dt><code>JOB_ID</code></p>
<dd> If set when starting <i>qtcsh</i> the local operation mode is activated implicitly as if the <code>-L</code> option was specified.</dl>
<h2>FILES</h2>
<pre>
<i>~/.qtask</i>       user qtask file.
<i>&lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/common/qtask</i>
               cluster qtask file.
</pre>
<h2>SEE ALSO</h2>
<p> as well as</p>
<h2>COPYRIGHT</h2>
<p> <i>Qtcsh</i> is an adaptation of <i>tcsh</i> which is copyrighted by The Regents of the University of California. </p>
<p> See and the information provided in &lt;xxqs_name_sxx_root&gt;/doc/LICENCES for a statement of further rights and permissions. </p>
<h2>Index</h2>
