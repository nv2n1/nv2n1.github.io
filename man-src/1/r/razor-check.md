---
title: "razor-check(1)"
name: "razor-check"
section: "1"
letter: "r"
url: "/docs/linux/man/1-razor-check/"
---

<h2 class="name">NAME</h2>
 

 &quot;razor-check&quot; - Razor Filtering Agent 

<h2>SYNOPSIS</h2>

 <pre><code>
razor - check[options][mail1[mail2..]] $ cat mbox | razor - check $ razor - check./ mbox $ razor - check - d mbox mail .1 mail .2 mail .3
</code></pre>

<h2>DESCRIPTION</h2>

 <tt>&quot;razor-check&quot;</tt> checks a mail against the distributed Razor Catalogue by communicating with a Razor Catalogue Server. It should be invoked before the mail is delivered or processed by a human. <tt>&quot;razor-check&quot;</tt> terminates with exit value <tt>0</tt> if the signature for the mail is catalogued on the server (spam) or <tt>1</tt> if the mail is not catalogued by the server (not a spam). <tt>&quot;razor-check&quot;</tt> should be invoked against every incoming mail by mail processors (like procmail) or MTAs (like sendmail). An alternate method would be to call <tt>&quot;razor-check&quot;</tt> from cron, at regular intervals, to identify and mark spam in queued mailboxes. 

 If <tt>&quot;razor-check&quot;</tt> is passed more than one mail, it will check each against the database, printing out the serial number of every mail considered to be spam. <tt>&quot;razor-check&quot;</tt> supports mbox-formatted files with 1 or more mails in them as well as files containing a single <font SIZE="-1">RFC 822 </font>(non-mbox) mail. More than one file may be present on the command line, can be either a non-mbox or mbox in any order. However, more than one non-mbox mail cannot be read from stdin.

<h2>USAGE</h2>

 <tt>&quot;razor-check&quot;</tt> is usually run by piping the contents of the mail to it, or by providing the name of the file that contains the mail message to be checked as the last argument. <tt>&quot;razor-check&quot;</tt> takes the following arguments:
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
<dd> Specify file to log to instead of what is in the configuration file. The default is <tt>&quot;&lt;razorhome&gt;/razor-agent.log&quot;</tt>.
<dt>&quot;-rs=razor.server.com&quot;
<dd> Use this Razor Catalogue Server instead of reading <tt>&quot;servers.catalogue.lst&quot;</tt>.
<dt>&quot;-H&quot;
<dd> Compute and print the signature of the mail contents and exit. If <tt>&quot;-e=integer&quot;</tt> is not specified, all supported engines will be used.
<dt>&quot;-S=string&quot;
<dd> Accept a list of pre-computed (with <tt>&quot;-H&quot;</tt>) signatures on the command line, instead of computing one from mail content. Signatures can be submitted in hex or base64, but base64 is preferred. Requires <tt>&quot;-e=integer&quot;</tt>. Usage: 

 <tt>&quot;razor-report -e 1 -S a8a3d545adb73f9733675571ffeaf10cba87745b&quot;</tt>
<dt>&quot;-e=integer&quot;
<dd> Specify engine used to create signatures. Must be 1, 2, 3, or 4 in this version. Engine 1, or <tt>&quot;-e=1&quot;</tt>, is used for Razor 1.x signatures. Used only with <tt>&quot;-S=string&quot;</tt> or <tt>&quot;-H&quot;</tt>.
<dt>&quot;-ep4=string&quot;
<dd> String used by engine 4 when computing signatures. Published by the Razor Catalogue Servers and updated very frequently. Used only when <tt>&quot;-e=4&quot;</tt>.</dl>

<h2>RECIPES</h2>

 <tt>&quot;razor-check&quot;</tt> is usually invoked from <i><a HREF="/docs/linux/man/1-procmail/">procmail</a></i>(1). Here are some common ways of using it with procmail:
<dl>
<dt>To change the &quot;Subject&quot; header if mail is spam:
<dd> <pre>
    :0 Wc
    | razor-check
    :0 Waf
    | formail -i &quot;Subject: Razor Warning: SPAM/UBE/UCE&quot;
</pre>
<dt>To add a &quot;X-Razor2-Warning&quot; header to spam:
<dd> <pre>
    :0 Wc
    | razor-check
    :0 Waf
    | formail -A &quot;X-Razor2-Warning: SPAM.&quot;
</pre>
<dt>To file spam in a mailbox
<dd> <pre>
    :0 Wc
    | razor-check
    :0 Wa
    /home/foo/Mail/razor-caught
</pre></dl>

<h2>AUTHORS</h2>

 Vipul Ved Prakash &lt;mail [at] vipul.net&gt;, and Chad Norwood &lt;chad [at] samo.org&gt;

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-razor-agents/">razor-agents</a></i>(1), <i><a HREF="/docs/linux/man/5-razor-agent-conf/">razor-agent.conf</a></i>(5), <i><a HREF="/docs/linux/man/1-razor-admin/">razor-admin</a></i>(1), <i><a HREF="/docs/linux/man/1-razor-report/">razor-report</a></i>(1), <i><a HREF="/docs/linux/man/1-razor-revoke/">razor-revoke</a></i>(1), <i><a HREF="/docs/linux/man/5-razor-whitelist/">razor-whitelist</a></i>(5)

<h2>LICENSE</h2>

 This is free software, distributed under the Artistic License 2.0. 

<h2>Index</h2>


