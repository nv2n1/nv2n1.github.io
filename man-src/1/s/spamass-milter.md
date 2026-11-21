---

title: "spamass-milter(1)"
name: "spamass-milter"
section: "1"
letter: "s"
url: "/docs/linux/man/1-spamass-milter/"
description: "spamass-milter – sendmail milter for passing emails through SpamAssassin"
---

<p> <code>spamass-milter</code> &#8211; sendmail milter for passing emails through SpamAssassin </p>
<p> &#8211;<code>p </code><i>socket</i> [-<code>b | -B </code><i>spamaddress</i> ] [-<code>C rejectcode</code> ] [-<code>d </code><i>debugflags</i> ] [-<code>D </code><i>host</i> ] [-<code>e </code><i>defaultdomain</i> ] [-<code>f</code> ] [-<code>g </code><i>group</i> ] [-<code>i </code><i>networks</i> ] [-<code>I</code> ] [-<code>m</code> ] [-<code>M</code> ] [-<code>P </code><i>pidfile</i> ] [-<code>r </code><i>nn</i> ] [-<code>r rejectmsg</code> ] [-<code>u </code><i>defaultuser</i> ] [-<code>x</code> ] [-<code>S /path/to/sendmail</code> ] [-<code>&#8211; </code><i>spamc flags &#8230;</i> ]</p>
<p> The utility is a sendmail milter that checks and modifies incoming email messages with SpamAssassin. </p>
<p> The following options are available:</p>
<dl>
<dt><code>-p </code><i>socket</i></dt>
<dd> Specifies the pathname of a socket to create for communication with <code>sendmail</code> If it is removed, <code>sendmail</code> will not be able to access the milter. This may cause messages to bounce, queue, or be passed through unmiltered, depending on the parameters in <code>sendmail &#8216;s .cf file.</code></dd>
<dt><code>-b </code><i>spamaddress</i></dt>
<dd> Redirects tagged spam to the specified email address. All envelope recipients are removed, and inserted into the message as `X-Spam-Orig-To:&#8217; headers.</dd>
<dt><code>-B </code><i>spamaddress</i></dt>
<dd> Same as &#8211;<code>b</code> except the original recipients are retained. Only one of &#8211;<code>b</code> and &#8211;<code>B</code> may be used.</dd>
<dt><code>-C </code><i>rejectcode</i></dt>
<dd> Mail that is rejected is rejected by default with a 5.7.1 code. This option allows that to be overridden. See also, -R &#8211;<code>S</code> option.</dd>
<dt><code>-d </code><i>debugflags</i></dt>
<dd> Enables logging. <i>debugflags </i> is a comma-separated list of tokens:</dd>
<dl>
<dt><code>func</code></dt>
<dd> Entry and exit of internal functions.</dd>
<dt><code>misc</code></dt>
<dd> Other non-verbose logging.</dd>
<dt><code>net</code></dt>
<dd> Lookups of the ignored netblocks list.</dd>
<dt><code>poll</code></dt>
<dd> Low-level I/O to the child spamc process.</dd>
<dt><code>rcpt</code></dt>
<dd> Recipient processing.</dd>
<dt><code>spamc</code></dt>
<dd> High-level I/O to the child spamc process.</dd>
<dt><code>str</code></dt>
<dd> Calls to field lookup and string comparison functions.</dd>
<dt><code>uori</code></dt>
<dd> Calls to the update_or_insert function.</dd>
<dt><code>1</code></dt>
<dd> (historical) Same as <i>func,misc</i></dd>
<dt><code>2</code></dt>
<dd> (historical) Same as <i>func,misc,poll</i></dd>
<dt><code>3</code></dt>
<dd> (historical) Same as <i>func,misc,poll,str,uori</i></dd></dl>
<dt><code>-D </code><i>host</i></dt>
<dd> Connects to a remote spamd server on <i>host , </i> instead of using one on localhost. This option is deprecated; use &#8211;<code>&#8211; -d </code><i>host </i> instead.</dd>
<dt><code>-e </code><i>defaultdomain</i></dt>
<dd> Pass the full user [at] domain address to spamc. The default is to pass only the username part on the assumption that all users are local. This flag is useful if you are using an SQL (or other username) backend with spamassassin and have listed the full address there. If the recipient name has no domain part (if the recipient is on the local machine for example), <i>defaultdomain </i> is added. Requires the &#8211;<code>u</code> flag.</dd>
<dt><code>-f</code></dt>
<dd> Causes to fork into the background.</dd>
<dt><code>-g </code><i>group</i></dt>
<dd> Makes the socket for communication with the MTA group-writable (mode 0750) and sets the socket&#8217;s group to <i>group</i> This option is intended for use with MTA&#8217;s like Postfix that do not run as root, and is incompatible with Sendmail usage.</dd>
<dt><code>-i </code><i>networks</i></dt>
<dd> Ignores messages if the originating IP is in the network(s) listed. The message will be passed through without calling SpamAssassin at all. <i>networks</i> is a comma-separated list, where each element can be either an IP address (nnn.nnn.nnn.nnn), a CIDR network (nnn.nnn.nnn.nnn/nn), or a network/netmask pair (nnn.nnn.nnn.nnn/nnn.nnn.nnn.nnn). Multiple &#8211;<code>i</code> flags will append to the list. For example, if you list all your internal networks, no outgoing emails will be filtered.</dd>
<dt><code>-I</code></dt>
<dd> Ignores messages if the sender has authenticated via SMTP AUTH.</dd>
<dt><code>-m</code></dt>
<dd> Disables modification of the `Subject:&#8217; </dd>
<p> and `Content-Type:&#8217; </p>
<p> headers and message body. This is useful when SpamAssassin is configured with `defang_mime&#8217; 0 and `report_header&#8217; 1 , or when SA is simply used to add headers for postprocessing later. Updating the body through the milter interface can be slow for large messages.</p>
<dt><code>-M</code></dt>
<dd> Like &#8211;<code>m</code> but also disables creation of any SpamAssassin `X-Spam-*&#8217; </dd>
<p> headers as well. Both tagged and untagged mail gets passed through unchanged. To be useful, this option should be used with the &#8211;<code>r</code> &#8211;<code>b , </code> or &#8211;<code>B</code> flags. If &#8211;<code>b</code> is used, the `X-Spam-Orig-To:&#8217; headers will still be added.</p>
<dt><code>-P </code><i>pidfile</i></dt>
<dd> Create the file <i>pidfile</i> containing the processid of the milter.</dd>
<dt><code>-r </code><i>nn</i></dt>
<dd> Reject scanned email if it greater than or equal to <i>nn</i> If <i>-1</i> reject scanned email if SpamAssassin tags it as spam (useful if you are also using the &#8211;<code>u</code> flag, and users have changed their required_hits value). </dd>
<p> For example, if you usually use procmail to redirect tagged email into a separate folder just in case of false positives, you can use &#8211;<code>r </code><i>15</i> and reject flagrant spam outright while still receiving low-scoring messages.</p>
<dt><code>-R </code><i>rejecttext</i></dt>
<dd> Mail that is rejected is rejected with the message &quot;Blocked by SpamAssassin&quot;. This option allows the user to call with a different message, instead. See also, the &#8211;<code>C</code> option</dd>
<dt><code>-S </code><i>/path/to/sendmail</i></dt>
<dd> This option is used in conjunction with the -x option to specify a path to sendmail if the default compiled in choice is not satisfactory.</dd>
<dt><code>-u </code><i>defaultuser</i></dt>
<dd> Pass the username part of the first recipient to spamc with the &#8211;<code>u </code> flag. This allows user preferences files to be used. If the message is addressed to multiple recipients, the username <i>defaultuser</i> is passed instead. </dd>
<p> Note that does not know whether an email is incoming or outgoing, so a message from Aq user1 [at] localdomain.com to Aq user2 [at] yahoo.com will make pass &#8211;<code>u </code><i>user2</i> to spamc.</p>
<dt><code>-x</code></dt>
<dd> Pass the recipient address through <code>sendmail -bv</code> which will perform virtusertable and alias expansion. The resulting username is then passed to spamc. Requires the &#8211;<code>u</code> flag. The spamass-milter configuration process does its best to find sendmail, but it is possible to override this compiled-in setting via the</dd>
<dt><code>&#8212; </code><i>spamc flags &#8230;</i></dt>
<dd> Pass all remaining options to spamc. This allows you to connect to a remote spamd with &#8211;<code>d</code> or &#8211;<code>p</code></dd></dl>
<h2>FILES</h2>
<dl>
<dt><code>/usr/bin/spamc </code></dt>
<dd> client interface to SpamAssassin</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-spamassassin/">spamassassin</a>(1), <a href="/docs/linux/man/1-spamd/">spamd</a>(1)</p>
<h2>AUTHORS</h2>
<p> An Georg C. F. Greve Aq greve [at] gnu.org An Dan Nelson Aq dnelson [at] allantgroup.com An Todd Kover Aq kovert [at] omniscient.com </p>
