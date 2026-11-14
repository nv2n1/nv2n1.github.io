---
title: "zarafa-dagent(1)"
name: "zarafa-dagent"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zarafa-dagent/"
description: "zarafa-dagent – Deliver mails to Zarafa."
---

<h2 class="name">NAME</h2>
<p> zarafa-dagent &#8211; Deliver mails to Zarafa. </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>zarafa-dagent</code> [<i>OPTION</i>&#8230;] <i>RECIPIENT</i></dl>
<h2>DESCRIPTION</h2>
<dd>With <code>zarafa-dagent</code>, mail messages can be imported from Internet Mail format to Zarafa. The message is read from standard in and delivered to the Zarafa server in the mailbox of <i>RECIPIENT</i>. You can alter source and destination of this mail with various options. </p>
<p> The <i>RECIPIENT</i> value is resolved by zarafa-dagent prior to delivery, and therefore accepts any unique identifier for the recipient. In practice it is most useful to pass the emailaddress of the user as the <i>RECIPIENT</i> parameter since it is always unique (Note that login names are sometimes not unique since group names may overlap). </p>
<p> The delivery agent will accept and deliver the message piped through it or specified by <code>-f</code> and exit immediately. </p>
<p> The delivery agent can also run as LMTP daemon.</p>
<h2>OPTIONS</h2>
<p> Various options are possible. None of these options are required. </p>
<p> <code>&#8211;config</code>, <code>-c</code> <i>file</i></p>
<dl>
<dt>
<dd> Use a configuration file. See the <code>CONFIG</code>() section for more information. </p>
<p> Default: <i>/etc/zarafa/dagent.cfg</i></dl>
<p> <code>&#8211;deamonize</code>, <code>-d</code></p>
<dl>
<dt>
<dd> Daemonize after starting. This implies &#8211;listen and is only used when LMTP is active.</dl>
<p> <code>&#8211;junk</code>, <code>-j</code></p>
<dl>
<dt>
<dd> Deliver in the Junk mail folder of the specified user.</dl>
<p> <code>&#8211;file</code>, <code>-f</code> <i>file</i></p>
<dl>
<dt>
<dd> Read e-mail input from file. When not given, input is read from standard in.</dl>
<p> <code>&#8211;host</code>, <code>-h</code> <i>path</i></p>
<dl>
<dt>
<dd> Connect to the Zarafa server through <i>path</i>, e.g. file:///path/to/socket. Default: file:///var/run/zarafa.</dl>
<p> <code>&#8211;listen</code>, <code>-l</code></p>
<dl>
<dt>
<dd> Listen for incoming LMTP connections</dl>
<p> <code>-q</code></p>
<dl>
<dt>
<dd> Use qmail style exit codes. Please see the <code>EXITCODES</code>() section for more information.</dl>
<p> <code>-s</code></p>
<dl>
<dt>
<dd> Silent mode. No output will be printed by the DAgent, except when wrong parameters are used to call zarafa-dagent.</dl>
<p> <code>-v</code></p>
<dl>
<dt>
<dd> Verbose mode. More output can be printed when processing the e-mail for rules. </p>
<p> When given a second time, more debugging output will be printed.</dl>
<p> <code>-e</code></p>
<dl>
<dt>
<dd> Strip the domain from the given username. For example, when the DAgent is called with &#8216;-e&#8217; and the username is &#8216;name [at] domain.com&#8217;, the delivery will be started for user &#8216;name&#8217; instead of &#8216;name [at] domain.com&#8217;.</dl>
<p> <code>-R</code></p>
<dl>
<dt>
<dd> The passed recipient name will always be resolved first. This means that the recipient can be a username, e-mail address or any other resolvable, unique identifier for the user. However, if the resolve fails (eg. when running as a non-trusted user), the passed name will be assumed to be a loginname of a user. Passing the -R option will disable this and will cause zarafa-dagent to exit with an error when the resolve fails. </p>
<p> In practice, the resolve will only fail if zarafa-dagent is not running in a trusted account and is therefore only really here for backward-compatibility of earlier zarafa-dagent versions.</dl>
<p> <code>-n</code></p>
<dl>
<dt>
<dd> Use &#8216;now&#8217; as the delivery time. Normally, the dagent will use the date from the first Received header, which is most likely to be the header from your own mailserver.</dl>
<p> <code>&#8211;do-not-notify</code>, <code>-N</code></p>
<dl>
<dt>
<dd> Do not send a new mail notification to othere connected clients. This option can be usefull when you have connected Outlook 2000 clients, which will also process rules when the mail is delivered. This is a bug workaround, and this option may disappear in the future.</dl>
<p> <code>&#8211;folder</code>, <code>-F</code> <i>path	oolder</i></p>
<dl>
<dt>
<dd> Deliver the incoming email to a specified subfolder of the store. Eg. &#8211;folder &#8216;Inbox\important&#8217;. Note that the &#8216;Inbox&#8217; folder is language specific. If the folder does not exist, delivery is reverted to the normal Inbox of the user, or use the &#8211;create flag.</dl>
<p> <code>&#8211;public</code>, <code>-P</code> <i>path	oolder</i></p>
<dl>
<dt>
<dd> Deliver the incoming email to a specified subfolder of the public store. Eg. &#8211;public &#8216;sales\incoming&#8217;. If the folder does not exist, delivery is reverted to the normal Inbox of the user, or use the &#8211;create flag. </p>
<p> Note that before 6.20 you&#8217;d need to add &#8216;Public Folders&#8217; to the folder name. This is not needed anymore.</dl>
<p> <code>-p</code> <i>&lt;path separator&gt;</i></p>
<dl>
<dt>
<dd> Use a different path separator. The default is &#8216;\&#8217;. If your delivery path contains a \ character, you can use this to alter the separator. Eg. -p _ &#8211;folder &#8216;Inbox_resellers\dealers&#8217;. The mail will now be delivered in a folder called &#8216;resellers\dealers&#8217; as a subfolder of the Inbox.</dl>
<p> <code>&#8211;create</code>, <code>-C</code></p>
<dl>
<dt>
<dd> Create the folder that was requested to deliver in. If there are no sufficient rights to create the folder, delivery is reverted to the normal Inbox of the user.</dl>
<p> <code>&#8211;read</code>, <code>-r</code></p>
<dl>
<dt>
<dd> Deliver the mail as read. Normally, the message will be marked as unread. This option can be usefull when importing old mail.</dl>
<p> <code>-a</code> <i>autoresponder</i></p>
<dl>
<dt>
<dd> Path to autoresponder, e.g. /usr/local/bin/zarafa-autorespond. This script will be called when the user enabled a vacation message in the Webaccess settings. When a header <i>X-Zarafa-Vacation</i> or <i>Precedence</i> was found in the received e-mail, this program will not be called to avoid loops. The Precedence header is often used in mailing lists. Other loop protections can be archieved in this separate program. This program or script will be called with the following arguments, in order: </p>
<p> <i>from</i></p>
<dl>
<dt>
<dd> The e-mail address of the Zarafa user sending the vacation message</dl>
<p> <i>to</i></p>
<dl>
<dt>
<dd> The e-mail address of the user to send the response to</dl>
<p> <i>subject</i></p>
<dl>
<dt>
<dd> The auto response subject set by the Zarafa user</dl>
<p> <i>zarafa-username</i></p>
<dl>
<dt>
<dd> The username of the Zarafa user which set the auto response</dl>
<p> <i>messagefile</i></p>
<dl>
<dt>
<dd> A file where the auto respond message will be temporary written to during the autorespond</dl>
<p> The following environment variables are present: </p>
<p> <i>MESSAGE_TO_ME</i></p>
<dl>
<dt>
<dd> Set to 1 if the original mail had the user in the To header.</dl>
<p> <i>MESSAGE_CC_ME</i></p>
<dl>
<dt>
<dd> Set to 1 if the original mail had the user in the Cc header.</dl>
<p> <i>MAILHEADERS</i></p>
<dl>
<dt>
<dd> Optional, if this value is present it points to a file that contains the original headers of the received email.</dl>
<p> Default: <i>/usr/bin/zarafa-autorespond</i>.</dl>
<h2>USAGE</h2>
<p> To deliver an e-mail to a Zarafa user&#8217;s mailbox: </p>
<p> <code>cat</code><i>mail</i><code>|</code><code>zarafa-dagent</code><i>username</i> </p>
<p> This pipes the input to the dagent via the standard input interface.</p>
<h2>CONFIG</h2>
<p> Normally, no configuration file is used or required. The following options can be set in the configuation file: </p>
<p> <code>server_socket</code></p>
<dl>
<dt>
<dd> Unix socket to find the connection to the Zarafa server. </p>
<p> Default: <i>file:///var/run/zarafa</i></dl>
<p> <code>sslkey_file</code></p>
<dl>
<dt>
<dd> Use this file as key to logon to the server. This is only used when server_socket is set to an HTTPS transport. See the <code><a href="/docs/linux/man/1-zarafa-server/">zarafa-server</a></code>(1) manual page on how to setup SSL keys. </p>
<p> Default: value not set.</dl>
<p> <code>sslkey_pass</code></p>
<dl>
<dt>
<dd> The password of the SSL key file that is set in sslkey_file. </p>
<p> Default: value not set.</dl>
<h2>EXITCODES</h2>
<p> The following exitcodes can be returned: </p>
<p> 0</p>
<dl>
<dt>
<dd> Delivery was successful</dl>
<p> 64</p>
<dl>
<dt>
<dd> Wrong or not enough parameters were passed to the DAgent. Delivery cannot be started.</dl>
<p> 70, 100</p>
<dl>
<dt>
<dd> Delivery was failed, and cannot be delivered. The SMTP server should not try again. When the <code>-q</code> option is used, this value is changed to 100, otherwise 70 is returned.</dl>
<p> 75, 111</p>
<dl>
<dt>
<dd> Delivery was temporarily failed. This happens when the Zarafa server is unavailable. The SMTP server may try again in a short while. When the <code>-q</code> option is used, this value is changed to 111, otherwise 75 is returned.</dl>
<h2>AUTHOR</h2>
<p> Written by Zarafa.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-zarafa-server/">zarafa-server</a></code>(1)<code><a href="/docs/linux/man/5-zarafa-dagent-cfg/">zarafa-dagent.cfg</a></code>(5) </p>
<h2>Index</h2>
