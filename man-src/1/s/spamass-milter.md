---
title: "spamass-milter(1)"
name: "spamass-milter"
section: "1"
letter: "s"
url: "/docs/linux/man/1-spamass-milter/"
description: "spamass-milter – sendmail milter for passing emails through SpamAssassin"
---

<h2 class="name">NAME</h2>
<p> <code>spamass-milter</code> &#8211; sendmail milter for passing emails through SpamAssassin </p>
<h2>SYNOPSIS</h2>
<p> &#8211;<code>p </code><i>socket</i> [-<code>b | -B </code><i>spamaddress</i> ] [-<code>C rejectcode</code> ] [-<code>d </code><i>debugflags</i> ] [-<code>D </code><i>host</i> ] [-<code>e </code><i>defaultdomain</i> ] [-<code>f</code> ] [-<code>g </code><i>group</i> ] [-<code>i </code><i>networks</i> ] [-<code>I</code> ] [-<code>m</code> ] [-<code>M</code> ] [-<code>P </code><i>pidfile</i> ] [-<code>r </code><i>nn</i> ] [-<code>r rejectmsg</code> ] [-<code>u </code><i>defaultuser</i> ] [-<code>x</code> ] [-<code>S /path/to/sendmail</code> ] [-<code>&#8211; </code><i>spamc flags &#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The utility is a sendmail milter that checks and modifies incoming email messages with SpamAssassin. </p>
<p> The following options are available:</p>
<dl>
<dt><code>-p </code><i>socket</i></p>
<dd> Specifies the pathname of a socket to create for communication with <code>sendmail</code> If it is removed, <code>sendmail</code> will not be able to access the milter. This may cause messages to bounce, queue, or be passed through unmiltered, depending on the parameters in <code>sendmail &#8216;s .cf file.</code></p>
<dt><code>-b </code><i>spamaddress</i></p>
<dd> Redirects tagged spam to the specified email address. All envelope recipients are removed, and inserted into the message as `X-Spam-Orig-To:&#8217; headers.</p>
<dt><code>-B </code><i>spamaddress</i></p>
<dd> Same as &#8211;<code>b</code> except the original recipients are retained. Only one of &#8211;<code>b</code> and &#8211;<code>B</code> may be used.</p>
<dt><code>-C </code><i>rejectcode</i></p>
<dd> Mail that is rejected is rejected by default with a 5.7.1 code. This option allows that to be overridden. See also, -R &#8211;<code>S</code> option.</p>
<dt><code>-d </code><i>debugflags</i></p>
<dd> Enables logging. <i>debugflags </i> is a comma-separated list of tokens:</p>
<dl>
<dt><code>func</code></p>
<dd> Entry and exit of internal functions.</p>
<dt><code>misc</code></p>
<dd> Other non-verbose logging.</p>
<dt><code>net</code></p>
<dd> Lookups of the ignored netblocks list.</p>
<dt><code>poll</code></p>
<dd> Low-level I/O to the child spamc process.</p>
<dt><code>rcpt</code></p>
<dd> Recipient processing.</p>
<dt><code>spamc</code></p>
<dd> High-level I/O to the child spamc process.</p>
<dt><code>str</code></p>
<dd> Calls to field lookup and string comparison functions.</p>
<dt><code>uori</code></p>
<dd> Calls to the update_or_insert function.</p>
<dt><code>1</code></p>
<dd> (historical) Same as <i>func,misc</i></p>
<dt><code>2</code></p>
<dd> (historical) Same as <i>func,misc,poll</i></p>
<dt><code>3</code></p>
<dd> (historical) Same as <i>func,misc,poll,str,uori</i></dl>
<dt><code>-D </code><i>host</i></p>
<dd> Connects to a remote spamd server on <i>host , </i> instead of using one on localhost. This option is deprecated; use &#8211;<code>&#8211; -d </code><i>host </i> instead.</p>
<dt><code>-e </code><i>defaultdomain</i></p>
<dd> Pass the full user [at] domain address to spamc. The default is to pass only the username part on the assumption that all users are local. This flag is useful if you are using an SQL (or other username) backend with spamassassin and have listed the full address there. If the recipient name has no domain part (if the recipient is on the local machine for example), <i>defaultdomain </i> is added. Requires the &#8211;<code>u</code> flag.</p>
<dt><code>-f</code></p>
<dd> Causes to fork into the background.</p>
<dt><code>-g </code><i>group</i></p>
<dd> Makes the socket for communication with the MTA group-writable (mode 0750) and sets the socket&#8217;s group to <i>group</i> This option is intended for use with MTA&#8217;s like Postfix that do not run as root, and is incompatible with Sendmail usage.</p>
<dt><code>-i </code><i>networks</i></p>
<dd> Ignores messages if the originating IP is in the network(s) listed. The message will be passed through without calling SpamAssassin at all. <i>networks</i> is a comma-separated list, where each element can be either an IP address (nnn.nnn.nnn.nnn), a CIDR network (nnn.nnn.nnn.nnn/nn), or a network/netmask pair (nnn.nnn.nnn.nnn/nnn.nnn.nnn.nnn). Multiple &#8211;<code>i</code> flags will append to the list. For example, if you list all your internal networks, no outgoing emails will be filtered.</p>
<dt><code>-I</code></p>
<dd> Ignores messages if the sender has authenticated via SMTP AUTH.</p>
<dt><code>-m</code></p>
<dd> Disables modification of the `Subject:&#8217; </p>
<p> and `Content-Type:&#8217; </p>
<p> headers and message body. This is useful when SpamAssassin is configured with `defang_mime&#8217; 0 and `report_header&#8217; 1 , or when SA is simply used to add headers for postprocessing later. Updating the body through the milter interface can be slow for large messages.</p>
<dt><code>-M</code></p>
<dd> Like &#8211;<code>m</code> but also disables creation of any SpamAssassin `X-Spam-*&#8217; </p>
<p> headers as well. Both tagged and untagged mail gets passed through unchanged. To be useful, this option should be used with the &#8211;<code>r</code> &#8211;<code>b , </code> or &#8211;<code>B</code> flags. If &#8211;<code>b</code> is used, the `X-Spam-Orig-To:&#8217; headers will still be added.</p>
<dt><code>-P </code><i>pidfile</i></p>
<dd> Create the file <i>pidfile</i> containing the processid of the milter.</p>
<dt><code>-r </code><i>nn</i></p>
<dd> Reject scanned email if it greater than or equal to <i>nn</i> If <i>-1</i> reject scanned email if SpamAssassin tags it as spam (useful if you are also using the &#8211;<code>u</code> flag, and users have changed their required_hits value). </p>
<p> For example, if you usually use procmail to redirect tagged email into a separate folder just in case of false positives, you can use &#8211;<code>r </code><i>15</i> and reject flagrant spam outright while still receiving low-scoring messages.</p>
<dt><code>-R </code><i>rejecttext</i></p>
<dd> Mail that is rejected is rejected with the message &quot;Blocked by SpamAssassin&quot;. This option allows the user to call with a different message, instead. See also, the &#8211;<code>C</code> option</p>
<dt><code>-S </code><i>/path/to/sendmail</i></p>
<dd> This option is used in conjunction with the -x option to specify a path to sendmail if the default compiled in choice is not satisfactory.</p>
<dt><code>-u </code><i>defaultuser</i></p>
<dd> Pass the username part of the first recipient to spamc with the &#8211;<code>u </code> flag. This allows user preferences files to be used. If the message is addressed to multiple recipients, the username <i>defaultuser</i> is passed instead. </p>
<p> Note that does not know whether an email is incoming or outgoing, so a message from Aq user1 [at] localdomain.com to Aq user2 [at] yahoo.com will make pass &#8211;<code>u </code><i>user2</i> to spamc.</p>
<dt><code>-x</code></p>
<dd> Pass the recipient address through <code>sendmail -bv</code> which will perform virtusertable and alias expansion. The resulting username is then passed to spamc. Requires the &#8211;<code>u</code> flag. The spamass-milter configuration process does its best to find sendmail, but it is possible to override this compiled-in setting via the</p>
<dt><code>&#8212; </code><i>spamc flags &#8230;</i></p>
<dd> Pass all remaining options to spamc. This allows you to connect to a remote spamd with &#8211;<code>d</code> or &#8211;<code>p</code></dl>
<h2>FILES</h2>
<dl>
<dt><code>/usr/bin/spamc </code></p>
<dd> client interface to SpamAssassin</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-spamassassin/">spamassassin</a>(1), <a href="/docs/linux/man/1-spamd/">spamd</a>(1)</p>
<h2>AUTHORS</h2>
<p> An Georg C. F. Greve Aq greve [at] gnu.org An Dan Nelson Aq dnelson [at] allantgroup.com An Todd Kover Aq kovert [at] omniscient.com </p>
<h2>Index</h2>
