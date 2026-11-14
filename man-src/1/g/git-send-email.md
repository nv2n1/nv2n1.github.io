---
title: "git-send-email(1)"
name: "git-send-email"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-send-email/"
description: "git-send-email – Send a collection of patches as emails"
---

<h2 class="name">NAME</h2>
<p> git-send-email &#8211; Send a collection of patches as emails </p>
<h2>SYNOPSIS</h2>
<pre>
<i>git send-email</i> [options] &lt;file|directory|rev-list options&gt;...
</pre>
<h2>DESCRIPTION</h2>
<p> Takes the patches given on the command line and emails them out. Patches can be specified as files, directories (which will send all files in the directory), or directly as a revision list. In the last case, any format accepted by <code><a href="/docs/linux/man/1-git-format-patch/">git-format-patch</a></code>(1) can be passed to git send-email. </p>
<p> The header of the email is configurable by command line options. If not specified on the command line, the user will be prompted with a ReadLine enabled interface to provide the necessary information. </p>
<p> There are two formats accepted for patch files: </p>
<dl>
<dt>
<dd> 1. mbox format files </p>
<p> This is what <code><a href="/docs/linux/man/1-git-format-patch/">git-format-patch</a></code>(1) generates. Most headers and MIME formatting are ignored.</dl>
<dl>
<dt>
<dd> 2. The original format used by Greg Kroah-Hartman&#8217;s <i>send_lots_of_email.pl</i> script </p>
<p> This format expects the first line of the file to contain the &quot;Cc:&quot; value and the &quot;Subject:&quot; of the message as the second line.</dl>
<h2>OPTIONS</h2>
<h3>Composing</h3>
<p> &#8211;annotate</p>
<dl>
<dt>
<dd> Review and edit each patch you&#8217;re about to send. Default is the value of <i>sendemail.annotate</i>. See the CONFIGURATION section for <i>sendemail.multiedit</i>.</dl>
<p> &#8211;bcc=&lt;address&gt;</p>
<dl>
<dt>
<dd> Specify a &quot;Bcc:&quot; value for each email. Default is the value of <i>sendemail.bcc</i>. </p>
<p> The &#8211;bcc option must be repeated for each user you want on the bcc list.</dl>
<p> &#8211;cc=&lt;address&gt;</p>
<dl>
<dt>
<dd> Specify a starting &quot;Cc:&quot; value for each email. Default is the value of <i>sendemail.cc</i>. </p>
<p> The &#8211;cc option must be repeated for each user you want on the cc list.</dl>
<p> &#8211;compose</p>
<dl>
<dt>
<dd> Invoke a text editor (see GIT_EDITOR in <code><a href="/docs/linux/man/1-git-var/">git-var</a></code>(1)) to edit an introductory message for the patch series. </p>
<p> When <i>&#8211;compose</i> is used, git send-email will use the From, Subject, and In-Reply-To headers specified in the message. If the body of the message (what you type after the headers and a blank line) only contains blank (or Git: prefixed) lines the summary won&#8217;t be sent, but From, Subject, and In-Reply-To headers will be used unless they are removed. </p>
<p> Missing From or In-Reply-To headers will be prompted for. </p>
<p> See the CONFIGURATION section for <i>sendemail.multiedit</i>.</dl>
<p> &#8211;from=&lt;address&gt;</p>
<dl>
<dt>
<dd> Specify the sender of the emails. If not specified on the command line, the value of the <i>sendemail.from</i> configuration option is used. If neither the command line option nor <i>sendemail.from</i> are set, then the user will be prompted for the value. The default for the prompt will be the value of GIT_AUTHOR_IDENT, or GIT_COMMITTER_IDENT if that is not set, as returned by &quot;git var -l&quot;.</dl>
<p> &#8211;in-reply-to=&lt;identifier&gt;</p>
<dl>
<dt>
<dd> Make the first mail (or all the mails with &#8211;no-thread) appear as a reply to the given Message-Id, which avoids breaking threads to provide a new patch series. The second and subsequent emails will be sent as replies according to the &#8211;[no]-chain-reply-to setting. </p>
<p> So for example when &#8211;thread and &#8211;no-chain-reply-to are specified, the second and subsequent patches will be replies to the first one like in the illustration below where [PATCH v2 0/3] is in reply to [PATCH 0/2]: </p>
<dl>
<dt>
<dd>
<pre><code>
[PATCH 0 / 2] Here is what I did...
    [PATCH 1 / 2] Clean up and tests
        [PATCH 2 / 2] Implementation
            [PATCH v2 0 / 3] Here is a reroll
                [PATCH v2 1 / 3] Clean up
                    [PATCH v2 2 / 3] New tests
                        [PATCH v2 3 / 3] Implementation
</code></pre>
</dl>
<p> Only necessary if &#8211;compose is also set. If &#8211;compose is not set, this will be prompted for.</dl>
<p> &#8211;subject=&lt;string&gt;</p>
<dl>
<dt>
<dd> Specify the initial subject of the email thread. Only necessary if &#8211;compose is also set. If &#8211;compose is not set, this will be prompted for.</dl>
<p> &#8211;to=&lt;address&gt;</p>
<dl>
<dt>
<dd> Specify the primary recipient of the emails generated. Generally, this will be the upstream maintainer of the project involved. Default is the value of the <i>sendemail.to</i> configuration value; if that is unspecified, and &#8211;to-cmd is not specified, this will be prompted for. </p>
<p> The &#8211;to option must be repeated for each user you want on the to list.</dl>
<p> &#8211;8bit-encoding=&lt;encoding&gt;</p>
<dl>
<dt>
<dd> When encountering a non-ASCII message or subject that does not declare its encoding, add headers/quoting to indicate it is encoded in &lt;encoding&gt;. Default is the value of the <i>sendemail.assume8bitEncoding</i>; if that is unspecified, this will be prompted for if any non-ASCII files are encountered. </p>
<p> Note that no attempts whatsoever are made to validate the encoding.</dl>
<p> &#8211;compose-encoding=&lt;encoding&gt;</p>
<dl>
<dt>
<dd> Specify encoding of compose message. Default is the value of the <i>sendemail.composeencoding</i>; if that is unspecified, UTF-8 is assumed.</dl>
<h3>Sending</h3>
<p> &#8211;envelope-sender=&lt;address&gt;</p>
<dl>
<dt>
<dd> Specify the envelope sender used to send the emails. This is useful if your default address is not the address that is subscribed to a list. In order to use the <i>From</i> address, set the value to &quot;auto&quot;. If you use the sendmail binary, you must have suitable privileges for the -f parameter. Default is the value of the <i>sendemail.envelopesender</i> configuration variable; if that is unspecified, choosing the envelope sender is left to your MTA.</dl>
<p> &#8211;smtp-encryption=&lt;encryption&gt;</p>
<dl>
<dt>
<dd> Specify the encryption to use, either <i>ssl</i> or <i>tls</i>. Any other value reverts to plain SMTP. Default is the value of <i>sendemail.smtpencryption</i>.</dl>
<p> &#8211;smtp-domain=&lt;FQDN&gt;</p>
<dl>
<dt>
<dd> Specifies the Fully Qualified Domain Name (FQDN) used in the HELO/EHLO command to the SMTP server. Some servers require the FQDN to match your IP address. If not set, git send-email attempts to determine your FQDN automatically. Default is the value of <i>sendemail.smtpdomain</i>.</dl>
<p> &#8211;smtp-pass[=&lt;password&gt;]</p>
<dl>
<dt>
<dd> Password for SMTP-AUTH. The argument is optional: If no argument is specified, then the empty string is used as the password. Default is the value of <i>sendemail.smtppass</i>, however <i>&#8211;smtp-pass</i> always overrides this value. </p>
<p> Furthermore, passwords need not be specified in configuration files or on the command line. If a username has been specified (with <i>&#8211;smtp-user</i> or a <i>sendemail.smtpuser</i>), but no password has been specified (with <i>&#8211;smtp-pass</i> or <i>sendemail.smtppass</i>), then a password is obtained using <i>git-credential</i>.</dl>
<p> &#8211;smtp-server=&lt;host&gt;</p>
<dl>
<dt>
<dd> If set, specifies the outgoing SMTP server to use (e.g. smtp.example.com or a raw IP address). Alternatively it can specify a full pathname of a sendmail-like program instead; the program must support the -i option. Default value can be specified by the <i>sendemail.smtpserver</i> configuration option; the built-in default is /usr/sbin/sendmail or /usr/lib/sendmail if such program is available, or localhost otherwise.</dl>
<p> &#8211;smtp-server-port=&lt;port&gt;</p>
<dl>
<dt>
<dd> Specifies a port different from the default port (SMTP servers typically listen to smtp port 25, but may also listen to submission port 587, or the common SSL smtp port 465); symbolic port names (e.g. &quot;submission&quot; instead of 587) are also accepted. The port can also be set with the <i>sendemail.smtpserverport</i> configuration variable.</dl>
<p> &#8211;smtp-server-option=&lt;option&gt;</p>
<dl>
<dt>
<dd> If set, specifies the outgoing SMTP server option to use. Default value can be specified by the <i>sendemail.smtpserveroption</i> configuration option. </p>
<p> The &#8211;smtp-server-option option must be repeated for each option you want to pass to the server. Likewise, different lines in the configuration files must be used for each option.</dl>
<p> &#8211;smtp-ssl</p>
<dl>
<dt>
<dd> Legacy alias for <i>&#8211;smtp-encryption ssl</i>.</dl>
<p> &#8211;smtp-user=&lt;user&gt;</p>
<dl>
<dt>
<dd> Username for SMTP-AUTH. Default is the value of <i>sendemail.smtpuser</i>; if a username is not specified (with <i>&#8211;smtp-user</i> or <i>sendemail.smtpuser</i>), then authentication is not attempted.</dl>
<p> &#8211;smtp-debug=0|1</p>
<dl>
<dt>
<dd> Enable (1) or disable (0) debug output. If enabled, SMTP commands and replies will be printed. Useful to debug TLS connection and authentication problems.</dl>
<h3>Automating</h3>
<p> &#8211;to-cmd=&lt;command&gt;</p>
<dl>
<dt>
<dd> Specify a command to execute once per patch file which should generate patch file specific &quot;To:&quot; entries. Output of this command must be single email address per line. Default is the value of <i>sendemail.tocmd</i> configuration value.</dl>
<p> &#8211;cc-cmd=&lt;command&gt;</p>
<dl>
<dt>
<dd> Specify a command to execute once per patch file which should generate patch file specific &quot;Cc:&quot; entries. Output of this command must be single email address per line. Default is the value of <i>sendemail.cccmd</i> configuration value.</dl>
<p> &#8211;[no-]chain-reply-to</p>
<dl>
<dt>
<dd> If this is set, each email will be sent as a reply to the previous email sent. If disabled with &quot;&#8211;no-chain-reply-to&quot;, all emails after the first will be sent as replies to the first email sent. When using this, it is recommended that the first file given be an overview of the entire patch series. Disabled by default, but the <i>sendemail.chainreplyto</i> configuration variable can be used to enable it.</dl>
<p> &#8211;identity=&lt;identity&gt;</p>
<dl>
<dt>
<dd> A configuration identity. When given, causes values in the <i>sendemail.&lt;identity&gt;</i> subsection to take precedence over values in the <i>sendemail</i> section. The default identity is the value of <i>sendemail.identity</i>.</dl>
<p> &#8211;[no-]signed-off-by-cc</p>
<dl>
<dt>
<dd> If this is set, add emails found in Signed-off-by: or Cc: lines to the cc list. Default is the value of <i>sendemail.signedoffbycc</i> configuration value; if that is unspecified, default to &#8211;signed-off-by-cc.</dl>
<p> &#8211;suppress-cc=&lt;category&gt;</p>
<dl>
<dt>
<dd> Specify an additional category of recipients to suppress the auto-cc of: </p>
<dl>
<dt>
<dd> &bull; <i>author</i> will avoid including the patch author</dl>
<dl>
<dt>
<dd> &bull; <i>self</i> will avoid including the sender</dl>
<dl>
<dt>
<dd> &bull; <i>cc</i> will avoid including anyone mentioned in Cc lines in the patch header except for self (use <i>self</i> for that).</dl>
<dl>
<dt>
<dd> &bull; <i>bodycc</i> will avoid including anyone mentioned in Cc lines in the patch body (commit message) except for self (use <i>self</i> for that).</dl>
<dl>
<dt>
<dd> &bull; <i>sob</i> will avoid including anyone mentioned in Signed-off-by lines except for self (use <i>self</i> for that).</dl>
<dl>
<dt>
<dd> &bull; <i>cccmd</i> will avoid running the &#8211;cc-cmd.</dl>
<dl>
<dt>
<dd> &bull; <i>body</i> is equivalent to <i>sob</i> + <i>bodycc</i></dl>
<dl>
<dt>
<dd> &bull; <i>all</i> will suppress all auto cc values.</dl>
<p> Default is the value of <i>sendemail.suppresscc</i> configuration value; if that is unspecified, default to <i>self</i> if &#8211;suppress-from is specified, as well as <i>body</i> if &#8211;no-signed-off-cc is specified.</dl>
<p> &#8211;[no-]suppress-from</p>
<dl>
<dt>
<dd> If this is set, do not add the From: address to the cc: list. Default is the value of <i>sendemail.suppressfrom</i> configuration value; if that is unspecified, default to &#8211;no-suppress-from.</dl>
<p> &#8211;[no-]thread</p>
<dl>
<dt>
<dd> If this is set, the In-Reply-To and References headers will be added to each email sent. Whether each mail refers to the previous email (deep threading per <i>git format-patch</i> wording) or to the first email (shallow threading) is governed by &quot;&#8211;[no-]chain-reply-to&quot;. </p>
<p> If disabled with &quot;&#8211;no-thread&quot;, those headers will not be added (unless specified with &#8211;in-reply-to). Default is the value of the <i>sendemail.thread</i> configuration value; if that is unspecified, default to &#8211;thread. </p>
<p> It is up to the user to ensure that no In-Reply-To header already exists when <i>git send-email</i> is asked to add it (especially note that <i>git format-patch</i> can be configured to do the threading itself). Failure to do so may not produce the expected result in the recipient&#8217;s MUA.</dl>
<h3>Administering</h3>
<p> &#8211;confirm=&lt;mode&gt;</p>
<dl>
<dt>
<dd> Confirm just before sending: </p>
<dl>
<dt>
<dd> &bull; <i>always</i> will always confirm before sending</dl>
<dl>
<dt>
<dd> &bull; <i>never</i> will never confirm before sending</dl>
<dl>
<dt>
<dd> &bull; <i>cc</i> will confirm before sending when send-email has automatically added addresses from the patch to the Cc list</dl>
<dl>
<dt>
<dd> &bull; <i>compose</i> will confirm before sending the first message when using &#8211;compose.</dl>
<dl>
<dt>
<dd> &bull; <i>auto</i> is equivalent to <i>cc</i> + <i>compose</i></dl>
<p> Default is the value of <i>sendemail.confirm</i> configuration value; if that is unspecified, default to <i>auto</i> unless any of the suppress options have been specified, in which case default to <i>compose</i>.</dl>
<p> &#8211;dry-run</p>
<dl>
<dt>
<dd> Do everything except actually send the emails.</dl>
<p> &#8211;[no-]format-patch</p>
<dl>
<dt>
<dd> When an argument may be understood either as a reference or as a file name, choose to understand it as a format-patch argument (<i>&#8211;format-patch</i>) or as a file name (<i>&#8211;no-format-patch</i>). By default, when such a conflict occurs, git send-email will fail.</dl>
<p> &#8211;quiet</p>
<dl>
<dt>
<dd> Make git-send-email less verbose. One line per email should be all that is output.</dl>
<p> &#8211;[no-]validate</p>
<dl>
<dt>
<dd> Perform sanity checks on patches. Currently, validation means the following: </p>
<dl>
<dt>
<dd> &bull; Warn of patches that contain lines longer than 998 characters; this is due to SMTP limits as described by m[blue]<code><a rel="nofollow" href="http://www.ietf.org/rfc/rfc2821.txt">http://www.ietf.org/rfc/rfc2821.txt</a></code>m[].</dl>
<p> Default is the value of <i>sendemail.validate</i>; if this is not set, default to <i>&#8211;validate</i>.</dl>
<p> &#8211;force</p>
<dl>
<dt>
<dd> Send emails even if safety checks would prevent it.</dl>
<h2>CONFIGURATION</h2>
<p> sendemail.aliasesfile</p>
<dl>
<dt>
<dd> To avoid typing long email addresses, point this to one or more email aliases files. You must also supply <i>sendemail.aliasfiletype</i>.</dl>
<p> sendemail.aliasfiletype</p>
<dl>
<dt>
<dd> Format of the file(s) specified in sendemail.aliasesfile. Must be one of <i>mutt</i>, <i>mailrc</i>, <i>pine</i>, <i>elm</i>, or <i>gnus</i>.</dl>
<p> sendemail.multiedit</p>
<dl>
<dt>
<dd> If true (default), a single editor instance will be spawned to edit files you have to edit (patches when <i>&#8211;annotate</i> is used, and the summary when <i>&#8211;compose</i> is used). If false, files will be edited one after the other, spawning a new editor each time.</dl>
<p> sendemail.confirm</p>
<dl>
<dt>
<dd> Sets the default for whether to confirm before sending. Must be one of <i>always</i>, <i>never</i>, <i>cc</i>, <i>compose</i>, or <i>auto</i>. See <i>&#8211;confirm</i> in the previous section for the meaning of these values.</dl>
<h2>EXAMPLE</h2>
<h3>Use gmail as the smtp server</h3>
<p> To use <i>git send-email</i> to send your patches through the GMail SMTP server, edit ~/.gitconfig to specify your account settings: </p>
<dl>
<dt>
<dd>
<pre><code>
[sendemail] smtpencryption = tls
    smtpserver = smtp.gmail.com
                     smtpuser = yourname[at] gmail.com
                                    smtpserverport = 587
</code></pre>
</dl>
<p> Once your commits are ready to be sent to the mailing list, run the following commands: </p>
<dl>
<dt>
<dd>
<pre>
$ git format-patch --cover-letter -M origin/master -o outgoing/
$ edit outgoing/0000-*
$ git send-email outgoing/*
</pre>
</dl>
<p> Note: the following perl modules are required Net::SMTP::SSL, MIME::Base64 and Authen::SASL</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-format-patch/">git-format-patch</a></code>(1), <code><a href="/docs/linux/man/1-git-imap-send/">git-imap-send</a></code>(1), <a href="/docs/linux/man/5-mbox/">mbox</a>(5)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
