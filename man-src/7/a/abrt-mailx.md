---
title: "abrt-mailx(7)"
name: "abrt-mailx"
section: "7"
letter: "a"
url: "/docs/linux/man/7-abrt-mailx/"
---

Mailx plugin for <a HREF="/docs/linux/man/8-abrt/">abrt</a>(8)

<h2>Description</h2>

<i>abrt</i> is a daemon that watches for application crashes. When a crash occurs, it collects the crash data and takes action according to its configuration. This manual page describes the <i>Mailx</i> plugin for <i>abrt</i>. This plugin is used to mail the data about the crash to a specified mail address.

<h2>Invocation</h2>

The plugin is invoked in the <i>abrt.conf</i> configuration file. It can take one parameter, a subject of the mail (if it differs from the one specified in the <i>Mailx.conf</i> configuration file).

<h2>Configuration</h2>

The <i>Mailx.conf</i> configuration file contains several entries in a format &quot;Option = Value&quot;. The options are:

<h3>Subject</h3>

The subject of the mail.

<h3>Parameters</h3>

The <i>Mailx</i> plugin executes the external &quot;mailx&quot; command to send the mail. This option defines some additional command line parameters, which should be added to the program invocation, if any.

<h3>EmailFrom</h3>

The address from which the email is sent.

<h3>EmailTo</h3>

The address to which the email is sent.

<h3>SendBinaryData</h3>

Can be &quot;yes&quot; or &quot;no&quot;. If set to &quot;yes&quot;, the email will also contain the binary files associated with the crash. Warning: this can cause the emails to be large! (several MB)

<h2>Examples</h2>

These are snippets from the <i>abrt.conf</i> configuration file. 1) Each time a crash happens, a mail is sent 

 [common] 
 ActionsAndReporters = Mailx(&quot;[abrt] a crash occurs&quot;) 2) When a program in a specific package (in this case &quot;httpd&quot;) crashes, send a mail about it. 

 [AnalyzerActionsAndReporters] 
 CCpp:httpd = Mailx(&quot;[abrt] Apache crash&quot;)

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/8-abrt/">abrt</a></i>(8), <i><a HREF="/docs/linux/man/5-abrt-conf/">abrt.conf</a></i>(5), <i><a HREF="/docs/linux/man/7-abrt-plugins/">abrt-plugins</a></i>(7)

<h2>Author</h2>

Written by Zdenek Prikryl &lt;zprikryl [at] redhat.com&gt;. Manual page by Daniel Novotny &lt;dnovotny [at] redhat.com&gt;.
