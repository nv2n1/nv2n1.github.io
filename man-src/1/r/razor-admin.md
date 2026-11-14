---
title: "razor-admin(1)"
name: "razor-admin"
section: "1"
letter: "r"
url: "/docs/linux/man/1-razor-admin/"
---

<h2 class="name">NAME</h2>
 

 &quot;razor-admin&quot; - Razor Registering Agent 

<h2>SYNOPSIS</h2>

 <pre><code>
razor - admin[options][-register | -create | -discover]
</code></pre>

<h2>DESCRIPTION</h2>

 <tt>&quot;razor-admin&quot;</tt> is the Razor Agent that performs administrative functions, most notably registering (-register)

<h2>USAGE</h2>

 <tt>&quot;razor-admin&quot;</tt> must have one of the following arguments:
<dl>
<dt>&quot;-register&quot;
<dd> Registers a new identity, used for authenticating with Razor Nomination Servers. Identities are a user + password pair stored in <tt>&quot;&lt;razorhome&gt;/identity-&lt;user&gt;&quot;</tt>. The first time <tt>&quot;razor-admin -register&quot;</tt> exits successfully, a symlink <tt>&quot;identity&quot;</tt> is created to point to the active <tt>&quot;identity-&lt;user&gt;&quot;</tt> file. After that, new identities can be created, but in order to use them the symlink <tt>&quot;identity&quot;</tt> must be changed to point to them. In general, it should be called once from the command line. Exits 0 for success, exits 1 on failure with a human-readable output message. 

 Both <i><a HREF="/docs/linux/man/1-razor-report/">razor-report</a></i>(1) and <i><a HREF="/docs/linux/man/1-razor-revoke/">razor-revoke</a></i>(1) require user authentication to work, <i><a HREF="/docs/linux/man/1-razor-check/">razor-check</a></i>(1) does not. This allows the Razor Nomination Server to keep track of how many messages a user reports and revokes. The more messages a user correctly reports and/or correctly revokes, the more trust the user earns. Likewise, when messages are incorrectly reported or revoked, the trust goes down for that user. Highly trusted users will have the most affect on the Razor database.
<dt>&quot;-discover&quot;
<dd> Force discovery. This will create <tt>&quot;server.*.lst&quot;</tt> files in &lt;razorhome&gt;.
<dt>&quot;-create&quot;
<dd> Explicitly creates <tt>&quot;razor-agent.conf&quot;</tt> file in &lt;razorhome&gt;, as well as &lt;razorhome&gt; if it does not exist. Normally loads <tt>&quot;/etc/razor/razor-agent.conf&quot;</tt> if it exists, using defaults for anything not found. Does not attempt to register with server, but will do discovery, see <tt>&quot;-discover&quot;</tt>.</dl>

<h2>OPTIONS</h2>

 <tt>&quot;razor-admin&quot;</tt> takes following optional arguments:
<dl>
<dt>&quot;-h&quot;
<dd> Print a usage message and exit.
<dt>&quot;-v&quot;
<dd> Print the version number and exit.
<dt>&quot;-d | --verbose&quot;
<dd> Print debugging information.
<dt>&quot;-debuglevel=n | -dl=n&quot;
<dd> Set debug level to 'n'. Default is 3 without <tt>&quot;-d&quot;</tt> option, 9 with.
<dt>&quot;-s&quot;
<dd> Simulate a check. Do everything except talk to the server.
<dt>&quot;-conf=filename&quot;
<dd> Specifies an alternate configuration file. If not specified, it is computed, see <i><a HREF="/docs/linux/man/1-razor-agents/">razor-agents</a></i>(1) manpage for details. See <i><a HREF="/docs/linux/man/5-razor-agent-conf/">razor-agent.conf</a></i>(5) manpage for various configuration options. The default is <tt>&quot;&lt;razorhome&gt;/razor-agent.conf&quot;</tt>.
<dt>&quot;-home=directory&quot;
<dd> Specify razorhome directory. This is where the configuration file, logfiles, identities, and server files live. If not specified, it is computed, see <i><a HREF="/docs/linux/man/1-razor-agents/">razor-agents</a></i>(1) manpage for details.
<dt>&quot;-logfile=file&quot;
<dd> Specify file to log to instead of what is in the configuration file. The default is <tt>&quot;&lt;razorhome&gt;/razor-agent.log&quot;</tt>.
<dt>&quot;-ident=filename&quot;
<dd> Specify an identify file to use for storing a newly registered identity. If not specified, <tt>&quot;&lt;razorhome&gt;/identity-&lt;user&gt;&quot;</tt> is used.
<dt>&quot;-rs=razor.server.com&quot;
<dd> Use this Razor Nomination Server instead of reading <tt>&quot;servers.nomination.lst&quot;</tt>.
<dt>&quot;-user=user [at] domain.com&quot;
<dd> Request to be known as this username. Must be less than 64 chars and may contain A-Z, a-z, 0-9, as well printable chars [ex: - _ @ . + / ]. If not specified, a username will be assigned. Razor users are encouraged to use their email addresses as their username.
<dt>&quot;-pass=password&quot;
<dd> Request this password. Valid chars are the same as for -user. If not specified, it will be assigned.
<dt>&quot;-l&quot;
<dd> The identity created during this <tt>&quot;razor-admin&quot;</tt> becomes the default. Normally, the first identity file created by <tt>&quot;razor-admin&quot;</tt> is the default one used.</dl>

<h2>EXAMPLES</h2>

<dl>
<dt>razor-admin -d -create
<dd> With no global razorhome defined (default) in /etc/razor/razor-agents.conf, creates .razor directory in user's home directory. 

 With global razorhome defined in /etc/razor/razor-agents.conf, will try to use that one, will fail if it does not have correct permissions.
<dt>razor-admin -register
<dd> Registers a new identity, storing it in &lt;lt&gt;razorhome&lt;gt&gt;. User and pass will be server generated. An identity is required for <i><a HREF="/docs/linux/man/1-razor-report/">razor-report</a></i>(1) and <i><a HREF="/docs/linux/man/1-razor-revoke/">razor-revoke</a></i>(1).
<dt>razor-admin -register -user me [at] a.com
<dd> Attempts to register a new identity using the user name 'me\@a.com'. Will fail if user is already taken.
<dt>razor-admin -d -create -home=/home/me/.razor
<dd> Creates .razor directory in user's home directory, which will then be the default home unless specified from cmd-line. Sends debugging information to stdout, and does not talk to any Razor Servers.
<dt>razor-admin -d -create -home=/etc/razor
<dd> Creates global razorhome, /etc/razor. This is the magic directory that will be consulted if no razorhome is specified on the cmd-line or found in user's home directory.</dl>

<h2>AUTHORS</h2>

 Vipul Ved Prakash &lt;mail [at] vipul.net&gt;, and Chad Norwood &lt;chad [at] samo.org&gt;

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-razor-agents/">razor-agents</a></i>(1), <i><a HREF="/docs/linux/man/5-razor-agent-conf/">razor-agent.conf</a></i>(5), <i><a HREF="/docs/linux/man/1-razor-check/">razor-check</a></i>(1), <i><a HREF="/docs/linux/man/1-razor-report/">razor-report</a></i>(1), <i><a HREF="/docs/linux/man/1-razor-revoke/">razor-revoke</a></i>(1), <i><a HREF="/docs/linux/man/5-razor-whitelist/">razor-whitelist</a></i>(5)

<h2>LICENSE</h2>

 This is free software, distributed under the Artistic License 2.0. 

<h2>Index</h2>


