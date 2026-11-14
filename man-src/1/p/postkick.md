---
title: "postkick(1)"
name: "postkick"
section: "1"
letter: "p"
url: "/docs/linux/man/1-postkick/"
description: "postkick – kick a Postfix service"
---

<h2 class="name">NAME</h2>
<p> postkick &#8211; kick a Postfix service </p>
<h2>SYNOPSIS</h2>
<p> <code>postkick</code> [<code>-c </code><i>config_dir</i>] [<code>-v</code>] <i>class service request</i></p>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/1-postkick/">postkick</a></code>(1) command sends <i>request</i> to the specified <i>service</i> over a local transport channel. This command makes Postfix private IPC accessible for use in, for example, shell scripts. </p>
<p> Options:</p>
<dl>
<dt><code>-c</code> <i>config_dir</i></p>
<dd> Read the <code>main.cf</code> configuration file in the named directory instead of the default configuration directory.</p>
<dt><code>-v</code></p>
<dd> Enable verbose logging for debugging purposes. Multiple <code>-v</code> options make the software increasingly verbose.</dl>
<p> Arguments:</p>
<dl>
<dt><i>class</i></p>
<dd> Name of a class of local transport channel endpoints, either <code>public</code> (accessible by any local user) or <code>private</code> (administrative access only).</p>
<dt><i>service</i></p>
<dd> The name of a local transport endpoint within the named class.</p>
<dt><i>request</i></p>
<dd> A string. The list of valid requests is service-specific.</dl>
<h2>DIAGNOSTICS</h2>
<p> Problems and transactions are logged to the standard error stream.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>MAIL_CONFIG</code></p>
<dd> Directory with Postfix configuration files.</p>
<dt><code>MAIL_VERBOSE</code></p>
<dd> Enable verbose logging for debugging purposes.</dl>
<h2>CONFIGURATION PARAMETERS</h2>
<p> The following <code>main.cf</code> parameters are especially relevant to this program. The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples.</p>
<dl>
<dt><code>config_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The default location of the Postfix main.cf and master.cf configuration files.</p>
<dt><code>application_event_drain_time (100s)</code></p>
<dd> How long the <code><a href="/docs/linux/man/1-postkick/">postkick</a></code>(1) command waits for a request to enter the Postfix daemon process input buffer before giving up.</p>
<dt><code>import_environment (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The list of environment parameters that a privileged Postfix process will import from a non-Postfix parent process, or name=value environment overrides.</p>
<dt><code>queue_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The location of the Postfix top-level queue directory.</dl>
<h2>FILES</h2>
<pre>
/var/spool/postfix/private, private class endpoints
/var/spool/postfix/public, public class endpoints
</pre>
<h2>SEE ALSO</h2>
<pre>
<a href="//www.systutorials.com/docs/linux/man/8-qmgr/">qmgr</a>(8), queue manager trigger protocol
<a href="//www.systutorials.com/docs/linux/man/8-pickup/">pickup</a>(8), local pickup daemon
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters
</pre>
<h2>LICENSE</h2>
<p> The Secure Mailer license must be distributed with this software.</p>
<h2>AUTHOR(S)</h2>
<pre>
Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA
Wietse Venema
Google, Inc.
111 8th Avenue
New York, NY 10011, USA
</pre>
<h2>Index</h2>
