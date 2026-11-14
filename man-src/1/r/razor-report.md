---
title: "razor-report(1)"
name: "razor-report"
section: "1"
letter: "r"
url: "/docs/linux/man/1-razor-report/"
---

<h2 class="name">NAME</h2>
 

 &quot;razor-report&quot; - Razor Reporting Agent 

<h2>SYNOPSIS</h2>

 <pre>
    razor-report [options]  file_with_mail_in_rfc822_format
    $ cat mail | razor-report
    $ razor-report ./mail 
    $ razor-report -d ./mail
</pre>

<h2>DESCRIPTION</h2>

 <tt>&quot;razor-report&quot;</tt> is the Razor Reporting Agent which is used for reporting spam messages to a Razor Nomination Server. <tt>&quot;razor-report&quot;</tt> should be generally called from a <font SIZE="-1">MUA,</font> although there are no restrictions on invoking it from the command-line. <tt>&quot;razor-report&quot;</tt> is a filter, which means that spam messages should be piped through it. By default, <tt>&quot;razor-report&quot;</tt> backgrounds and detaches itself from the control terminal at start-up. 

 If <tt>&quot;razor-report&quot;</tt> is passed more than one mail, it will report each against the database. Please use this with caution, we don't want the database filled up with mails incorrectly identified as spam. <tt>&quot;razor-report&quot;</tt> supports mbox-formatted files with 1 or more mails in them as well as files containing a single <font SIZE="-1">RFC 822 </font>(non-mbox) mail. More than one file may be present on the command line, can be either a non-mbox or mbox in any order. 

 However, more than one non-mbox mail cannot be read from stdin. Both <tt>&quot;razor-report&quot;</tt> and <i><a HREF="/docs/linux/man/1-razor-revoke/">razor-revoke</a></i>(1) require user authentication to work, see <i><a HREF="/docs/linux/man/1-razor-admin/">razor-admin</a></i>(1). This allows the Razor Nomination Server to keep track of how many messages a user reports and revokes. The more messages a user correctly reports and/or correctly revokes, the more trust the user earns. Likewise, when messages are incorrectly reported or revoked, the trust goes down for that user. Highly trusted users will have the most affect on the Razor Catalogue.

<h2>USAGE</h2>

 <tt>&quot;razor-report&quot;</tt> takes following arguments:
<dl>
<dt>&quot;-h&quot;
<dd> Print a usage message and exit.
<dt>&quot;-v&quot;
<dd> Print the version number and exit.
<dt>&quot;-d | --verbose&quot;
<dd> Print debugging information to stdout.
<dt>&quot;-debuglevel=n | -dl=n&quot;
<dd> Set debug level to 'n'. Default is 3 without <tt>&quot;-d&quot;</tt> option, 9 with.
<dt>&quot;-whitelist=file&quot;
<dd> Specify file to use for whitelisting. Overrides 'whitelist' option in <tt>&quot;razor-agent.conf&quot;</tt>.
<dt>&quot;-s&quot;
<dd> Simulate a check. Do everything except talk to the server.
<dt>&quot;-conf=filename&quot;
<dd> Specifies an alternate configuration file. If not specified, it is computed, see <i><a HREF="/docs/linux/man/1-razor-agents/">razor-agents</a></i>(1) manpage for details. See <i><a HREF="/docs/linux/man/5-razor-agent-conf/">razor-agent.conf</a></i>(5) manpage for various configuration options. The default is <tt>&quot;&lt;razorhome&gt;/razor-agent.conf&quot;</tt>.
<dt>&quot;-home=dir&quot;
<dd> Specify razorhome directory. This is where the configuration file, logfiles, identities, and server files live. If not specified, it is computed, see <i><a HREF="/docs/linux/man/1-razor-agents/">razor-agents</a></i>(1) manpage for details.
<dt>&quot;-logfile=file&quot;
<dd> Specify file to log to instead of whats in configuration file. The default is <tt>&quot;&lt;razorhome&gt;/razor-agent.log&quot;</tt>.
<dt>&quot;-ident=filename&quot;
<dd> Specify an identify file to use for authenticating with Razor Servers. If not specified, <tt>&quot;&lt;razorhome&gt;/identity-&lt;user&gt;&quot;</tt> is used.
<dt>&quot;-rs=razor.server.com&quot;
<dd> Use this Razor Nomination Server instead of reading <tt>&quot;servers.nomination.lst&quot;</tt>.
<dt>&quot;-H&quot;
<dd> Compute and print the signature of the mail contents and exit. If <tt>&quot;-e=integer&quot;</tt> is not specified, all supported engines will be used.
<dt>&quot;-S=string&quot;
<dd> Accept a list of pre-computed (with <tt>&quot;-H&quot;</tt>) signatures on the command line, instead of computing one from mail content. Signatures can be submitted in hex or base64, but base64 is preferred. Requires <tt>&quot;-e=integer&quot;</tt>. Usage: 

 razor-report -e 1 -S a8a3d545adb73f9733675571ffeaf10cba87745b
<dt>&quot;-e=integer&quot;
<dd> Specify engine used to create signatures. Must be 1, 2, 3, or 4 in this version. Engine 1, or <tt>&quot;-e=1&quot;</tt>, is used for Razor 1.x signatures. Used only with <tt>&quot;-S=string&quot;</tt> or <tt>&quot;-H&quot;</tt>.
<dt>&quot;-ep4=string&quot;
<dd> String used by engine 4 when computing signatures. Published by the Razor Nomination Servers and updated very frequently. Used only when <tt>&quot;-e=4&quot;</tt>.
<dt>&quot;-i=filename&quot;
<dd> Use identity from filename instead of reading &lt;razorhome&gt;/identity. Razor Servers compute trust for each unique identity. Razor Agents figure out the identity by a 2 step process. First, check if identity is specified via cmd-line (-i=file). If not there, then look in &lt;razorhome&gt; for identity file. If &lt;razorhome&gt; has no identity file, authentication will fail - you cannot report or revoke. See <i><a HREF="/docs/linux/man/5-razor-agents-conf/">razor-agents.conf</a></i>(5) for more on &lt;razorhome&gt;. ---fixme----
<dt>&quot;-a&quot;
<dd> Authenticate only. If authenticated, exit 0; if not, exit 1.
<dt>&quot;-f&quot;
<dd> Stay in foreground, do not detach and run in background.</dl>

<h2>INTEGRATION WITH MUTT</h2>

 Add the following line to <tt>&quot;mutt.conf&quot;</tt> 

 <pre>
     macro index S &quot;|/usr/bin/razor-report&quot;
</pre> 

 Then press S on the spam message in <tt>&quot;mutt&quot;</tt> to report it with <tt>&quot;razor-report&quot;</tt>. Since <tt>&quot;razor-report&quot;</tt> forks, the control will return immediately.

<h2>AUTHORS</h2>

 Vipul Ved Prakash &lt;mail [at] vipul.net&gt;, and Chad Norwood &lt;chad [at] samo.org&gt;

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-razor-agents/">razor-agents</a></i>(1), <i><a HREF="/docs/linux/man/5-razor-agent-conf/">razor-agent.conf</a></i>(5), <i><a HREF="/docs/linux/man/1-razor-check/">razor-check</a></i>(1), <i><a HREF="/docs/linux/man/1-razor-admin/">razor-admin</a></i>(1), <i><a HREF="/docs/linux/man/1-razor-revoke/">razor-revoke</a></i>(1), <i><a HREF="/docs/linux/man/5-razor-whitelist/">razor-whitelist</a></i>(5)

<h2>LICENSE</h2>

 This is free software, distributed under the Artistic License 2.0. 

<h2>Index</h2>


