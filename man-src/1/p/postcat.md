---
title: "postcat(1)"
name: "postcat"
section: "1"
letter: "p"
url: "/docs/linux/man/1-postcat/"
description: "postcat – show Postfix queue file contents"
---

<h2 class="name">NAME</h2>
<p> postcat &#8211; show Postfix queue file contents </p>
<h2>SYNOPSIS</h2>
<pre><code>
postcat[-bdehnoqv][-c config_dir][files...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/1-postcat/">postcat</a></code>(1) command prints the contents of the named <i>files</i> in human-readable form. The files are expected to be in Postfix queue file format. If no <i>files</i> are specified on the command line, the program reads from standard input. </p>
<p> By default, <code><a href="/docs/linux/man/1-postcat/">postcat</a></code>(1) shows the envelope and message content, as if the options <code>-beh</code> were specified. To view message content only, specify <code>-bh</code> (Postfix 2.7 and later). </p>
<p> Options:</p>
<dl>
<dt><code>-b</code></p>
<dd> Show body content. The <code>-b</code> option starts producing output at the first non-header line, and stops when the end of the message is reached. </p>
<p> This feature is available in Postfix 2.7 and later.</p>
<dt><code>-c </code><i>config_dir</i></p>
<dd> The <code>main.cf</code> configuration file is in the named directory instead of the default configuration directory.</p>
<dt><code>-d</code></p>
<dd> Print the decimal type of each record.</p>
<dt><code>-e</code></p>
<dd> Show message envelope content. </p>
<p> This feature is available in Postfix 2.7 and later.</p>
<dt><code>-h</code></p>
<dd> Show message header content. The <code>-h</code> option produces output from the beginning of the message up to, but not including, the first non-header line. </p>
<p> This feature is available in Postfix 2.7 and later.</p>
<dt><code>-o</code></p>
<dd> Print the queue file offset of each record.</p>
<dt><code>-q</code></p>
<dd> Search the Postfix queue for the named <i>files</i> instead of taking the names literally. </p>
<p> This feature is available in Postfix 2.0 and later.</p>
<dt><code>-v</code></p>
<dd> Enable verbose logging for debugging purposes. Multiple <code>-v</code> options make the software increasingly verbose.</dl>
<h2>DIAGNOSTICS</h2>
<p> Problems are reported to the standard error stream.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>MAIL_CONFIG</code></p>
<dd> Directory with Postfix configuration files.</dl>
<h2>CONFIGURATION PARAMETERS</h2>
<p> The following <code>main.cf</code> parameters are especially relevant to this program. </p>
<p> The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples.</p>
<dl>
<dt><code>config_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The default location of the Postfix main.cf and master.cf configuration files.</p>
<dt><code>import_environment (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The list of environment parameters that a privileged Postfix process will import from a non-Postfix parent process, or name=value environment overrides.</p>
<dt><code>queue_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The location of the Postfix top-level queue directory.</dl>
<h2>FILES</h2>
<pre>
/var/spool/postfix, Postfix queue directory
</pre>
<h2>SEE ALSO</h2>
<pre>
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), Postfix configuration
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
