---
title: "qrstat(1)"
name: "qrstat"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qrstat/"
description: "qrstat – show the status of xxQS_NAMExx Advance Reservations (AR)"
---

<h2 class="name">NAME</h2>
<p> qrstat &#8211; show the status of xxQS_NAMExx Advance Reservations (AR) </p>
<h2>SYNTAX</h2>
<p> <code>qrstat</code> [<code>-ar</code> <i>ar_id</i>,&#8230;] [<code>-help</code>] [<code>-u</code> <i>user</i>,&#8230;] [<code>-explain</code>]</p>
<h2>DESCRIPTION</h2>
<p> <i>qrstat</i> shows the current status of the available xxQS_NAMExx ARs. The selection option <code>-ar</code> allows you to get information about specific AR. </p>
<p> The administrator and the user may define files which can contain any of the options described below. A cluster-wide sge_qrstat file may be placed under $xxQS_NAME_Sxx_ROOT/$xxQS_NAME_Sxx_CELL/common/sge_qrstat The user private file is searched at the location $HOME/.sge_qrstat. The home directory request file has the highest precedence over the cluster global file. Command line can be used to override the flags contained in the files.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-ar</code> <i>ar_id</i>,&#8230;</p>
<dd> Prints various information about the ARs identified by the given <i>ar_id</i> list.</p>
<dt><code>-explain</code></p>
<dd> Displays the reason for the error state of an AR. Possible reasons are the unknown state of a host or queue instance. </p>
<p> The output format for the alarm reasons is one line per reason.</p>
<dt><code>-help</code></p>
<dd> Prints a listing of all options.</p>
<dt><code>-u</code> <i>user</i>,&#8230;</p>
<dd> Display information only for those ARs created by the users from the given user list. </p>
<p> The string <code>&nbsp;$user</code> is a placeholder for the current username. An asterisk &quot;<code>*&quot; can be used as a username wildcard to request that all users&#8217; ARs be displayed. The default value for this switch is &quot;-u $user</code>&quot;.</p>
<dt><code>-xml</code></p>
<dd> This option can be used with all other options and changes the output to XML. The schemas used are referenced in the XML output. The output is printed to stdout.
</dl>
<h2>OUTPUT FORMATS</h2>
<p> Depending on the presence or absence of the <code>-ar</code> option there are two output formats need to be differentiated.</p>
<h3><code>Advance Reservation Summary (without -ar)</code></h3>
<p> Following the header line, a section for each AR is provided. The columns contain information for</p>
<dl>
<dt>&bull;</p>
<dd> the AR id;</p>
<dt>&bull;</p>
<dd> the name of the AR;</p>
<dt>&bull;</p>
<dd> the current state of the AR. One of the following letters with the given meaning: </p>
<pre>
<code>w</code> - waiting without error
<code>W</code> - warning (effective - waiting with error)
<code>r</code> - running
<code>E</code> - error (effective - running with error)
<code>d</code> - deleted
</pre>
<dt>&bull;</p>
<dd> the start time of the AR;</p>
<dt>&bull;</p>
<dd> the end time of the AR;</p>
<dt>&bull;</p>
<dd> the duration of the AR.</dl>
<h3><code>Detailed Format (with -ar)</code></h3>
<p> The output contains two columns. The first one contains all AR attributes. The second one the corresponding value.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>xxQS_NAME_Sxx_ROOT</code></p>
<dd> Specifies the location of the xxQS_NAMExx standard configuration files.</p>
<dt><code>xxQS_NAME_Sxx_CELL</code></p>
<dd> If set, specifies the default xxQS_NAMExx cell. To address a xxQS_NAMExx cell <i>qrstat</i> uses (in the order of precedence): </p>
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
<dd> If set, specifies the tcp port on which is expected to listen for communication requests. Most installations will use a services map entry for the service &quot;sge_qmaster&quot; instead to define that port.</dl>
<h2>FILES</h2>
<pre>
<i>&lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/common/act_qmaster</i>
                          xxQS_NAMExx master host file
<i>&lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/common/xxqs_name_sxx_qrstat</i>
                          cluster qrstat default options
<i>$HOME/.xxqs_name_sxx_qrstat</i>
                          user qrstat default options
</pre>
<h2>SEE ALSO</h2>
<h2>COPYRIGHT</h2>
<p> See for a full statement of rights and permissions. </p>
<h2>Index</h2>
<dt><a href="#lbAI">ENVIRONMENT VARIABLES</a></p>
<dd>
<dt><a href="#lbAJ">FILES</a></p>
<dd>
<dt><a href="#lbAK">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAL">COPYRIGHT</a></p>
<dd></dl>
