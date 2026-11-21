---

title: "elog(1)"
name: "elog"
section: "1"
letter: "e"
url: "/docs/linux/man/1-elog/"
description: "elog – utility program for Electronic Logbook ELOG"
---

<p> elog &#8211; utility program for Electronic Logbook ELOG </p>
<h2>SYNOPSIS</h2>
<p> <code>elog</code> <code>-a </code><i>attribute=value</i> [ <code>-e </code><i>id</i> ] [ <code>-f </code><i>file&#8230;</i> ] <code>-h </code><i>host</i> [ <code>-l </code><i>logbook</i> ] [ <code>-m </code><i>textfile</i> ] [ <code>-p </code><i>port</i> ] [ <code>-r </code><i>id</i> ] [ <code>-s </code><i>subdir</i> ] [ <code>-u </code><i>username</i><i>password</i> ] [ <code>-v</code> ] [ <code>-w </code><i>password</i> ] <i>message</i> [ <code>-x</code> ]</p>
<h2>DESCRIPTION</h2>
<p> The Electronic Logbook <code>ELOG</code> can be used to store and retrieve messages through a Web interface. Depending on the configuration, the <code>ELOG</code> system can host one or more logbooks which are stored in separate sections on the server. <code>elog</code> is the standalone client program which can be used from the command line to interact with the <code>ELOG</code> daemon (elogd). The <code>elog</code> message can either be submitted on the command line or piped through `stdin&#8217; or in a file with the `-m&#8217; flag. For the former case, message with blanks must be enclosed in quotes. Multiple attributes can be specified as well as several attachments. The password must match the write password defined on the server. If user level access is defined on the server (via the `Password file&#8217; option), a valid user name / password pair must be specified with the `-u&#8217; option. </p>
<p> The <code>elog</code> program makes it possible to submit logbook entries automatically by the system or from scripts. In some shift logbooks this feature is used to enter alarm messages automatically into the logbook.</p>
<h2>OPTIONS</h2>
<p> <code>elog</code> accepts the following options:</p>
<dl>
<dt><code>-a</code><i> attribute=value</i></dt>
<dd> set attribute to value</dd>
<dt><code>-e</code><i> id</i></dt>
<dd> edit existing message of id</dd>
<dt><code>-f</code><i> file&#8230;</i></dt>
<dd> attach files while submitting</dd>
<dt><code>-h</code><i> host</i></dt>
<dd> host where <code>elogd</code> is running</dd>
<dt><code>-l</code><i> logbook</i></dt>
<dd> name of logbook or experiment</dd>
<dt><code>-m</code><i> textfile</i></dt>
<dd> submit message from textfile</dd>
<dt><code>-p</code><i> port</i></dt>
<dd> port where <code>elogd</code> is running</dd>
<dt><code>-r</code><i> id</i></dt>
<dd> reply to existing message of id</dd>
<dt><code>-s</code><i> dir</i></dt>
<dd> directory where logbooks reside</dd>
<dt><code>-u</code><i> username password</i></dt>
<dd> username and password</dd>
<dt><code>-v</code></dt>
<dd> verbose output</dd>
<dt><code>-w</code><i> password</i></dt>
<dd> write password defined on server</dd>
<dt><code>-x</code></dt>
<dd> suppress email notification</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-elogd/">elogd</a></code>(8). </p>
<p> The full documentation for <code>ELOG</code> is maintained as an html manual. You can reach it from the package document directory.</p>
<h2>AUTHOR</h2>
<p> Written by Stefan Ritt &lt;stefan.ritt [at] psi.ch&gt;. </p>
<p> This manual page was written by Recai Oktas &lt;roktas [at] omu.edu.tr&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
