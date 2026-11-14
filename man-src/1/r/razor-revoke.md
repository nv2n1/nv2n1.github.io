---
title: "razor-revoke(1)"
name: "razor-revoke"
section: "1"
letter: "r"
url: "/docs/linux/man/1-razor-revoke/"
---

<h2 class="name">NAME</h2>
 

 &quot;razor-revoke&quot; - Razor Revoking Agent 

<h2>SYNOPSIS</h2>

 <pre>
    razor-revoke [options]  file_with_mail_in_rfc822_format
    $ cat mail | razor-revoke
    $ razor-revoke ./mail 
    $ razor-revoke -d ./mail
</pre>

<h2>DESCRIPTION</h2>

 <tt>&quot;razor-revoke&quot;</tt> is the Razor Revoking Agent which is used for reporting messages as <font SIZE="-1">NOT</font> spam to a Razor Nomination Server. For instance, it can be invoked if a check incorrectly marked a message as spam or after a message was incorrectly reported as spam. <tt>&quot;razor-revoke&quot;</tt> should be generally called from a <font SIZE="-1">MUA,</font> although there are no restrictions on invoking it from the command-line. <tt>&quot;razor-revoke&quot;</tt> is a filter, which means that spam messages should be piped through it. By default, <tt>&quot;razor-revoke&quot;</tt> backgrounds and detaches itself from the control terminal at start-up. 

 If <tt>&quot;razor-revoke&quot;</tt> is passed more than one mail, it will revoke each against the database. Please use this with caution, we don't want the database to have inaccurate information. <tt>&quot;razor-revoke&quot;</tt> supports mbox-formatted files with 1 or more mails in them as well as files containing a single <font SIZE="-1">RFC 822 </font>(non-mbox) mail. More than one file may be present on the command line, can be either a non-mbox or mbox in any order. However, more than one non-mbox mail cannot be read from stdin. 

 Both <i><a HREF="/docs/linux/man/1-razor-report/">razor-report</a></i>(1) and <tt>&quot;razor-revoke&quot;</tt> require user authentication to work, see <i><a HREF="/docs/linux/man/1-razor-admin/">razor-admin</a></i>(1). This allows the Razor Nomination Server to keep track of how many messages a user reports and revokes. The more messages a user correctly reports and/or correctly revokes, the more trust the user earns. Likewise, when messages are incorrectly reported or revoked, the trust goes down for that user. Highly trusted users will have the most affect on the Razor database. 

 Note that even after a successful revoke, a mail might still be considered spam in the Razor Catalogue. For instance, this can occur if more trusted users consider the mail spam than not spam.

<h2>USAGE</h2>

 <tt>&quot;razor-revoke&quot;</tt> takes following arguments:
<dl>
<dt>&quot;-h&quot;
<dd> Print a usage message and exit.
<dt>&quot;-v&quot;
<dd> Print the version number and exit.
<dt>&quot;-d | --verbose&quot;
<dd> Print debugging information.
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
<dt>&quot;-M | --mbox&quot;
<dd> Accept a mailbox name on the command line and revoke every mail in the mailbox against the database. If in foreground, <tt>&quot;-f&quot;</tt>, <tt>&quot;razor-revoke&quot;</tt> will print out the mail number of every mail that was accepted by the Catalogue server. 

 <pre>
 C&lt;razor-revoke -f -M ~/Mail/incorrectly-marked-spam&gt;
</pre>
<dt>&quot;-i=filename&quot;
<dd> Used identity from filename instead of reading &lt;razorhome&gt;/identity.
<dt>&quot;-a&quot;
<dd> Authenticate only. If authenticated, exit 0; if not, exit 1.
<dt>&quot;-f&quot;
<dd> Stay in foreground, do not detach and run in background.</dl>

<h2>INTEGRATION WITH MUTT</h2>

 Add the following line to <tt>&quot;mutt.conf&quot;</tt> 

 <pre>
     macro index R &quot;|/usr/bin/razor-revoke&quot;
</pre> 

 Then press R on the spam message in <tt>&quot;mutt&quot;</tt> to report it with <tt>&quot;razor-revoke&quot;</tt>. Since <tt>&quot;razor-revoke&quot;</tt> forks, the control will return immediately.

<h2>AUTHORS</h2>

 Vipul Ved Prakash &lt;mail [at] vipul.net&gt;, and Chad Norwood &lt;chad [at] samo.org&gt;

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-razor-agents/">razor-agents</a></i>(1), <i><a HREF="/docs/linux/man/5-razor-agent-conf/">razor-agent.conf</a></i>(5), <i><a HREF="/docs/linux/man/1-razor-check/">razor-check</a></i>(1), <i><a HREF="/docs/linux/man/1-razor-admin/">razor-admin</a></i>(1), <i><a HREF="/docs/linux/man/1-razor-report/">razor-report</a></i>(1), <i><a HREF="/docs/linux/man/5-razor-whitelist/">razor-whitelist</a></i>(5)

<h2>LICENSE</h2>

 This is free software, distributed under the Artistic License 2.0. 

<h2>Index</h2>


