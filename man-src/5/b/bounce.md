---
title: "bounce(5)"
name: "bounce"
section: "5"
letter: "b"
url: "/docs/linux/man/5-bounce/"
description: "bounce – Postfix bounce message template format"
---

<p>bounce &#8211; Postfix bounce message template format</p>
<h2>Synopsis</h2>
<pre><code>bounce_template_file = /etc/postfix/bounce.cf</code>
<code>postconf -b</code> [<i>template_file</i>]</pre>
<h2>Description</h2>
<p>The Postfix <code><a href="/docs/linux/man/8-bounce/">bounce</a></code>(8) server produces delivery status notification (DSN) messages for undeliverable mail, delayed mail, successful delivery or address verification requests. </p>
<p> By default, these notifications are generated from built-in templates with message headers and message text. Sites can override the built-in information by specifying a bounce template file with the <code>bounce_template_file</code> configuration parameter. </p>
<p> This document describes the general procedure to create a bounce template file, followed by the specific details of bounce template formats.</p>
<h2>General Procedure</h2>
<p>To create a customized bounce template file, create a temporary copy of the file <code>/etc/postfix/bounce.cf.default</code> and edit the temporary file. </p>
<p> To preview the results of $<i>name</i> expansions in the template text, use the command </p>
<pre> <code>postconf -b</code> <i>temporary_file</i></pre>
<p>Errors in the template will be reported to the standard error stream and to the syslog daemon. </p>
<p> While previewing the text, be sure to pay particular attention to the expansion of time value parameters that appear in the delayed mail notification text. </p>
<p> Once the result is satisfactory, copy the template to the Postfix configuration directory and specify in main.cf something like: </p>
<pre>/etc/postfix/main.cf:
 bounce_template_file = /etc/postfix/bounce.cf</pre>
<h2>Template File Format</h2>
<p>The template file can specify templates for failed mail, delayed mail, successful delivery or for address verification. These templates are named <code>failure_template</code>, <code>delay_template</code>, <code>success_template</code> and <code>verify_template</code>, respectively. You can but do not have to specify all four templates in a bounce template file. </p>
<p> Each template starts with &quot;<i>template_name</i><code> = &lt;&lt;EOF</code>&quot; and ends with a line that contains the word &quot;<code>EOF</code>&quot; only. You can change the word EOF, but you can&#8217;t enclose it in quotes as with the shell or with Perl (<i>template_name</i><code> = &lt;&lt;&#8216;EOF&#8217;</code>). Here is an example: </p>
<pre> # The failure template is used for undeliverable mail.
 failure_template = &lt;&lt;EOF
 Charset: us-ascii
 From: MAILER-DAEMON (Mail Delivery System)
 Subject: Undelivered Mail Returned to Sender
 Postmaster-Subject: Postmaster Copy: Undelivered Mail
 This is the mail system at host $myhostname.
 I'm sorry to have to inform you that your message could not
 be delivered to one or more recipients. It's attached below.
 For further assistance, please send mail to postmaster.
 If you do so, please include this problem report. You can
 delete your own text from the attached returned message.
 The mail system
 EOF</pre>
<p>The usage and specification of bounce templates is subject to the following restrictions:</p>
<dl>
<dt>&bull;</p>
<dd>No special meaning is given to the backslash character or to leading whitespace; these are always taken literally.</p>
<dt>&bull;</p>
<dd>Inside the &lt;&lt; context, the &quot;$&quot; character is special. To produce a &quot;$&quot; character as output, specify &quot;$$&quot;.</p>
<dt>&bull;</p>
<dd>Outside the &lt;&lt; context, lines beginning with &quot;#&quot; are ignored, as are empty lines, and lines consisting of whitespace only.</dl>
<p> Examples of all templates can be found in the file <code>bounce.cf.default</code> in the Postfix configuration directory.</p>
<h2>Template Header Format</h2>
<p>The first portion of a bounce template consists of optional template headers. Some become message headers in the delivery status notification; some control the formatting of that notification. Headers not specified in a template will be left at their default value. </p>
<p> The following headers are supported:</p>
<dl>
<dt><code>Charset:</code></p>
<dd>The MIME character set of the template message text. See the &quot;TEMPLATE MESSAGE TEXT FORMAT&quot; description below.</p>
<dt><code>From:</code></p>
<dd>The sender address in the message header of the delivery status notification.</p>
<dt><code>Subject:</code></p>
<dd>The subject in the message header of the delivery status notification that is returned to the sender.</p>
<dt><code>Postmaster-Subject:</code></p>
<dd>The subject that will be used in Postmaster copies of undeliverable or delayed mail notifications. These copies are sent under control of the notify_classes configuration parameter.</dl>
<p> The usage and specification of template message headers is subject to the following restrictions:</p>
<dl>
<dt>&bull;</p>
<dd>Template message header names can be specified in upper case, lower case or mixed case. Postfix always produces bounce message header labels of the form &quot;<code>From:</code>&quot; and &quot;<code>Subject:</code>&quot;.</p>
<dt>&bull;</p>
<dd>Template message headers must not span multiple lines.</p>
<dt>&bull;</p>
<dd>Template message headers do not support $parameter expansions.</p>
<dt>&bull;</p>
<dd>Template message headers must contain ASCII characters only, and must not contain ASCII null characters.</dl>
<h2>Template Message Text Format</h2>
<p>The second portion of a bounce template consists of message text. As the above example shows, template message text may contain main.cf $parameters. Besides the parameters that are defined in main.cf, the following parameters are treated specially depending on the suffix that is appended to their name.</p>
<dl>
<dt><code>delay_warning_time_</code><i>suffix</i></p>
<dd>Expands into the value of the <code>delay_warning_time</code> parameter, expressed in the time unit specified by <i>suffix</i>, which is one of <code>seconds</code>, <code>minutes</code>, <code>hours, days</code>, or <code>weeks</code>.</p>
<dt><code>maximal_queue_lifetime_</code><i>suffix</i></p>
<dd>Expands into the value of the <code>maximal_queue_lifetime</code> parameter, expressed in the time unit specified by <i>suffix</i>. See above under <code>delay_warning_time</code> for possible <i>suffix</i> values.</p>
<dt><code>mydomain</code></p>
<dd>Expands into the value of the <code>mydomain</code> parameter. With &quot;smtputf8_enable = yes&quot;, this replaces ACE labels (xn--mumble) with their UTF-8 equivalent. </p>
<p> This feature is available in Postfix 3.0.</p>
<dt><code>myhostname</code></p>
<dd>Expands into the value of the <code>myhostname</code> parameter. With &quot;smtputf8_enable = yes&quot;, this replaces ACE labels (xn--mumble) with their UTF-8 equivalent. </p>
<p> This feature is available in Postfix 3.0.</dl>
<p> The usage and specification of template message text is subject to the following restrictions:</p>
<dl>
<dt>&bull;</p>
<dd>The template message text is not sent in Postmaster copies of delivery status notifications.</p>
<dt>&bull;</p>
<dd>If the template message text contains non-ASCII characters, Postfix requires that the <code>Charset:</code> template header is updated. Specify an appropriate superset of US-ASCII. A superset is needed because Postfix appends ASCII text after the message template when it sends a delivery status notification.</dl>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/8-bounce/">bounce</a>(8), Postfix delivery status notifications
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters</pre>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>History</h2>
<p>The Postfix bounce template format was originally developed by Nicolas Riendeau.</p>
<h2>Author(S)</h2>
<pre>Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA
Wietse Venema
Google, Inc.
111 8th Avenue
New York, NY 10011, USA</pre>
