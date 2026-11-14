---
title: "reporter-mailx(1)"
name: "reporter-mailx"
section: "1"
letter: "r"
url: "/docs/linux/man/1-reporter-mailx/"
---

<h2 class="name">NAME</h2>
 

 reporter-mailx - Sends contents of a problem directory via email. 

<h2>SYNOPSIS</h2>

 

 <i>reporter-mailx</i> [-v] -d DIR [-c CONFFILE] [-F FMTFILE]

<h2>DESCRIPTION</h2>

 

 The tool reads a problem directory, composes an email message from the directory contents, and uses mailx to send the message to specified recipient. 

 Properties of email messages can be specified in a configuration file, and via environment variables.

<h3>Configuration file</h3>

 

 Configuration file contains entries in a format &quot;Option = Value&quot;. 

 The options are: 

 <i>Subject</i>
<dl>
<dt>
<dd> The subject of the email message.</dl>
 

 <i>EmailFrom</i>
<dl>
<dt>
<dd> The sender of the email message.</dl>
 

 <i>EmailTo</i>
<dl>
<dt>
<dd> The recipient of the email message.</dl>
 

 <i>SendBinaryData</i>
<dl>
<dt>
<dd> Use yes/true/on/1 to attach all binary files from the problem directory to the email. This can cause the emails to be very large.</dl>

<h3>Formatting configuration files</h3>

 

 Lines starting with # are ignored. 

 Lines can be continued on the next line using trailing backslash. 

 Format: 

 &quot;%summary
<dl>
<dt>
<dd> subject format&quot;</dl>
 

 &quot;section
<dl>
<dt>
<dd> element1[,element2]...&quot; The literal text line to be added to email. Can be empty. (Empty lines are NOT ignored!) 

<dl>
<dt>
<dd> <pre><code>
Subject format is a line of text, where % element % is replaced by text element's content, and [[...%element%...]] block is used only if % element % exists.[[...]] blocks can nest.
</code></pre></dl>
 

<dl>
<dt>
<dd> <pre>
Sections can be:
- %summary: email subject format string.
- %attach: a list of elements to attach.
- text, double colon (::) and the list of comma-separated elements.
</pre></dl>
 

<dl>
<dt>
<dd> <pre>
Elements can be:
- problem directory element names, which get formatted as
  &lt;element_name&gt;: &lt;contents&gt;
  or
  &lt;element_name&gt;:
  :&lt;contents&gt;
  :&lt;contents&gt;
  :&lt;contents&gt;
- problem directory element names prefixed by &quot;%bare_&quot;,
  which is formatted as-is, without &quot;&lt;element_name&gt;:&quot; and colons
- %oneline, %multiline, %text wildcards, which select all corresponding
  elements for output or attachment
- %binary wildcard, valid only for %attach section, instructs to attach
  binary elements
- problem directory element names prefixed by &quot;-&quot;,
  which excludes given element from all wildcards
</pre></dl>
 

<dl>
<dt>
<dd> <pre>
Nonexistent elements are silently ignored.
If none of elements exists, the section will not be created.
</pre></dl>
</dl>

<h3>Integration with ABRT events</h3>

 

 <i>reporter-mailx</i> can be used as a reporter, to allow users report problems via email when they decide to do it. This usage is pre-configured in /etc/libreport/events.d/mailx_event.conf: 

<dl>
<dt>
<dd> <pre>
EVENT=report_Mailx      reporter-mailx
</pre></dl>
 

 It can also be used to notify administrator automatically when a problem happens. When this is desired, modify the event configuration file to run the tool on the <i>post-create</i> event: 

<dl>
<dt>
<dd> <pre>
EVENT=post-create       reporter-mailx
</pre></dl>

<h2>OPTIONS</h2>

 

 -d DIR
<dl>
<dt>
<dd> Path to problem directory.</dl>
 

 -c CONFFILE
<dl>
<dt>
<dd> Path to configuration file. When used in ABRT event system, the file contains site-wide configuration. Users can change the values via environment variables.</dl>
 

 -F CONF_FORMAT_FILE Formatting file for an email.

<h2>ENVIRONMENT VARIABLES</h2>

 

 Environment variables take precedence over values provided in the configuration file. 

 <i>Mailx_Subject</i>
<dl>
<dt>
<dd> Subject of the email message.</dl>
 

 <i>Mailx_EmailFrom</i>
<dl>
<dt>
<dd> Sender of the email message.</dl>
 

 <i>Mailx_EmailTo</i>
<dl>
<dt>
<dd> Recipient of the email message. If nor the environment variable nor the corresponding option is defined, the message is send to &quot;root [at] localhost&quot;.</dl>
 

 <i>Mailx_SendBinaryData</i>
<dl>
<dt>
<dd> Use yes/true/on/1 to attach all binary files from the problem directory to the email.</dl>

<h2>FILES</h2>

 

 /usr/share/libreport/conf.d/plugins/mailx.conf
<dl>
<dt>
<dd> Readonly default configuration files.</dl>
 

 /etc/libreport/plugins/mailx.conf
<dl>
<dt>
<dd> Configuration files.</dl>

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/5-mailx_event-conf/">mailx_event.conf</a>(5), <a HREF="/docs/linux/man/5-mailx-conf/">mailx.conf</a>(5), <a HREF="/docs/linux/man/5-report_mailx-conf/">report_mailx.conf</a>(5)

<h2>AUTHORS</h2>

 

<dl>
<dt>
<dd> &bull; ABRT team</dl>
 

<h2>Index</h2>


