---
title: "enemies-of-carlotta(1)"
name: "enemies-of-carlotta"
section: "1"
letter: "e"
url: "/docs/linux/man/1-enemies-of-carlotta/"
description: "enemies-of-carlotta – a simple mailing list manager"
---

<h2>NAME</h2>
<p> enemies-of-carlotta &#8211; a simple mailing list manager</p>
<h2>SYNOPSIS</h2>
<p> <code>enemies-of-carlotta </code> <i></i>[<i>options</i>] [<i>addresses</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>enemies-of-carlotta</code> is a simple mailing list manager. If you don&#8217;t know what a mailing list manager is, you should learn what they are before trying to use one. A manual page is unfortunately too short to explain it. </p>
<p> Enemies of Carlotta keeps all data about the lists in the <i>~/.enemies-of-carlotta</i> directory. It will be created automatically when you create your first list. You need to arrange manually for the mails to be processed by the list manager. The details differ from mail system to another. For QMail and Postfix, see below. </p>
<p> Each list has one or more owners, who also moderate subscriptions or moderate some or all postings. On completely unmoderated lists the list owners are responsible for answering questions about the list. On completely moderated lists, they have to approve each message before it is sent to the list. On lists with <i>posting=auto</i>, messages from subscribers are sent automatically to the list, and the moderators have to approve the rest.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;name=</code>foo [at] example.com</p>
<dd> Specify the list the command is to operate on. Most of the remaining options require you to set the list name with this option. With the &#8211;edit, &#8211;subscribe, &#8211;unsubscribe, and &#8211;list options, the name can be abbreviated to by leaving out the @ sign and domain.</p>
<dt><code>&#8211;create</code></p>
<dd> Create a new list. You must specify at least one owner with <code>&#8211;owner</code>.</p>
<dt><code>&#8211;owner=</code><i>address</i></p>
<dd> Specify a list owner when creating or editing a list.</p>
<dt><code>&#8211;moderator=</code><i>address</i></p>
<dd> Specificy a list moderator when creating or editing a list.</p>
<dt><code>&#8211;language=</code><i>language-code</i></p>
<dd> Set the language code used for looking up template files. The code should be empty (the default, meaning English), or a two-letter code such as <code>fi</code> or <code>es</code>.</p>
<dt><code>&#8211;cleaning-woman</code></p>
<dd> Deal with bouncing addresses and do other cleanup. You must run <code>enemies-of-carlotta &#8211;cleaning-woman</code> periodically, such as once per hour. It will clean up all your lists.</p>
<dt><code>&#8211;destroy</code></p>
<dd> Destroy the list.</p>
<dt><code>&#8211;edit</code></p>
<dd> Modify the list configuration.</p>
<dt><code>&#8211;subscription=</code><i>type</i></p>
<dd> When creating a list, set its subscription mode to <i>free</i> or <i>moderated</i>. Use with <code>&#8211;edit</code>, or <code>&#8211;create</code>.</p>
<dt><code>&#8211;posting=</code><i>type</i></p>
<dd> When creating a list, set its posting mode to <i>free</i> (anyone can post), <i>auto</i> (only subscribers can post, mails from others need to be moderated), or <i>moderated</i> (all mails are moderated). Use with <code>&#8211;edit</code>, or <code>&#8211;create</code>.</p>
<dt><code>&#8211;archived=</code><i>yes-or-no</i></p>
<dd> Should list messages be archived to the <code>archive-box</code> directory in the list directory under the <code>~/.enemies-of-carlotta</code> directory. Use <i>yes</i> or <i>no</i>.</p>
<dt><code>&#8211;mail-on-subscription-changes=</code><i>yes-or-no</i></p>
<dd> Should the list owners be notified when someone subscribes to or unsubscribes from the list? Use <i>yes</i> or <i>no</i>. Default is no.</p>
<dt><code>&#8211;mail-on-forced-unsubscription=</code><i>yes-or-no</i></p>
<dd> Should list owners be notified when someone is forcibly dropped from the list due to too much bouncing? Use <i>yes</i> or <i>no</i>. Default is no.</p>
<dt><code>&#8211;ignore-bounce=</code><i>yes-or-no</i></p>
<dd> Should bounces be ignored? Use <i>yes</i> or <i>no</i>. Default is no.</p>
<dt><code>&#8211;list</code></p>
<dd> List the subscribers of a list.</p>
<dt><code>&#8211;subscribe</code></p>
<dd> Add subscribers to a list. The non-option arguments are the addresses to be subscribed. Note that addresses added this way won&#8217;t be sent confirmation requests.</p>
<dt><code>&#8211;unsubscribe</code></p>
<dd> Remove subscribers from a list. The non-option arguments are the addresses to be unsubscribed. Note that addresses removed this way won&#8217;t be sent confirmation requests.</p>
<dt><code>&#8211;incoming</code></p>
<dd> Deal with an incoming message in the standard input. The SMTP envelope sender address must be given in the <i>SENDER</i> environment variable, and the SMTP envelope recipient address in the <i>RECIPIENT</i> environment variable. (QMail and Postfix do this automatically.)</p>
<dt><code>&#8211;skip-prefix=</code><i>string</i></p>
<dd> Before analyzing the recipient address to see which list it refers, remove <i>string</i> from its beginning. This helps deal with QMail and Postfix virtual domains, see above.</p>
<dt><code>&#8211;domain=</code><i>domain.name</i></p>
<dd> Before analyzing the recipient address to see which list it refers, replace the domain name part with <i>domain.name</i>. This helps deal with Postfix virtual domains.</p>
<dt><code>&#8211;is-list</code></p>
<dd> Does the address specified with <code>&#8211;name</code> refer to a valid list? This sets the exit code to zero (success) if it does, or one (failure) if it does not.</p>
<dt><code>&#8211;sendmail=</code><i>pathname</i></p>
<dd> Use <i>pathname</i> instead of <code>/usr/sbin/sendmail</code> for sending mail via a command line interface. Note that the command must obey the sendmail command line interface.</p>
<dt><code>&#8211;smtp-server=</code><i>hostname</i></p>
<dd> Send mail using the SMTP server at <i>hostname</i> (port 25). The server must be configured to allow the list host to relay mail through it. Note that a command line interface is used by default; SMTP sending is used only if you use this option.</p>
<dt><code>&#8211;qmqp-server=</code><i>hostname</i></p>
<dd> Send mail using the QMQP server at <i>hostname</i> (port 628). The server must be configured to allow the list host to relay mail through it. Note that a command line interface is used by default; QMQP sending is used only if you use this option.</p>
<dt><code>&#8211;moderate</code></p>
<dd> Force an incoming message to be moderated, even if it is going to a list where posting is free. This can be used for spam filtering: you pipe incoming messages through whatever spam filter you choose to use and if the mssage looks like spam, you ask it to be moderated by a human.</p>
<dt><code>&#8211;post</code></p>
<dd> Force an incoming message to be posted, even if it is going to a list where posting is moderated. This can be used when there is an external check for whether a mail is acceptable to the list, e.g., by checking digital signatures.</p>
<dt><code>&#8211;quiet</code></p>
<dd> By default, debugging log messages are sent to the standard error output stream. With this option, they aren&#8217;t.</p>
<dt><code>&#8211;sender=</code><i>foo [at] example.com</i></p>
<dd>
<dt><code>&#8211;recipient=</code><i>foo [at] example.com</i></p>
<dd> These two options are used with <code>&#8211;incoming </code> and <code>&#8211;is-list</code> to override the environment variables <code>SENDER</code> and <code>RECIPIENT</code>, respectively.</p>
<dt><code>&#8211;get</code></p>
<dd> Get the values of one or more configuration variables. The name of the variables are given on the command line after the options. Each value is printed on a separate line.</p>
<dt><code>&#8211;set</code></p>
<dd> Set the values of one or more configuration variables. The names and values are given on the command line after the options and separated by an equals sign (&quot;=&quot;). For example, the following would set the language of a list to Finnish: <code>enemies-of-carlotta &#8211;name=foo@bar &#8211;set language=fi</code></p>
<dt><code>&#8211;version</code></p>
<dd> Print out the version of the program.</p>
<dt><code>&#8211;show-lists</code></p>
<dd> List the lists enemies-of-carlotta knows about.</dl>
<h2>CONFIGURATION</h2>
<p> Each list is represented by a directory, named after the list, in <i>~/.enemies-of-carlotta</i>. That directory contains several files and directories, described below. In general, it is not necessary to touch these at all. However, some esoteric configuration can only be done by hand editing of the list configuration file.</p>
<dl>
<dt><code>config</code></p>
<dd> The list configuration file. Contents are described below.</p>
<dt><code>subscribers</code></p>
<dd> Subscriber database. Each line contains a subscriber group, with the first five space delimited fields being group identifier, status, timestamp for when the group was created, timestamp for the bounce that made it switch from status &#8216;ok&#8217; to &#8216;bounced&#8217;, and the bounce identifier.</p>
<dt><code>archive-box</code></p>
<dd> Archived messages.</p>
<dt><code>bounce-box</code></p>
<dd> Bounce messages groups not in state &#8216;ok&#8217;.</p>
<dt><code>headers-to-add</code></p>
<dd> These headers are added to the mails sent to the list. They are copied to the beginning of the existing headers exactly as they are in the file, after list headers (&quot;List-ID&quot; and such) have been added and those mentioned in <code>headers-to-remove</code> have been removed.</p>
<dt><code>headers-to-remove</code></p>
<dd> These headers are removed from mails sent to the list.</p>
<dt><code>moderation-box</code></p>
<dd> Messages waiting for moderator approval.</p>
<dt><code>subscription-box</code></p>
<dd> Subscription and unsubscription requests waiting to be confirmed by the user.</p>
<dt><code>templates</code></p>
<dd> Directory containing list specific templates (optional). If this directory exists, templates are searched from it before going for system wide templates. An empty file here means the corresponding message is not sent at all. This can, for example, to be used to turn off the &quot;please wait for moderator&quot; mails on a per-list basis.</p>
<dt><code>plugins</code></p>
<dd> Directory containing plugins, Python source files that are loaded automatically by EoC upon startup. The plugins may change how EoC operates.</dl>
<p> The <code>config</code> file has a <i>keyword</i>=<i>value</i> format: </p>
<dl>
<dt>
<dd>
<pre><code>
[list] owners = liw[at] liw.iki.fi
                    archived = no
    posting = free
        subscription = free
                           mail -
                       on - subscription - changes = yes
                                                         mail -
                                                     on - forced - unsubscribe = yes
                                                         language = fi
</code></pre>
</dl>
<p> The keywords <code>archived</code>, <code>posting</code>, and <code>subscription </code> correspond to the options with the same names. Other keywords are:</p>
<dl>
<dt><code>owners</code></p>
<dd> List of addresses for the owners. Set with the <i>&#8211;owner</i> option.</p>
<dt><code>moderators</code></p>
<dd> List of addresses for the moderators. Set with the <i>&#8211;moderator</i> option.</p>
<dt><code>mail-on-subscription-changes</code></p>
<dd> Should the owners be mailed when users subscribe or unsubscribe?</p>
<dt><code>mail-on-forced-unsubscribe</code></p>
<dd> Should the owners be mailed when people are removed from the list due to excessive bouncing?</p>
<dt><code>ignore_bounce</code></p>
<dd> Bounce messages are ignored on this list. Useful for example if list should have static subscriber list.</p>
<dt><code>language</code></p>
<dd> Suffix for templates, to allow support for multiple languages. (If <i>language</i> is set to &quot;fi&quot;, then the template named &quot;foo&quot; is first searched as &quot;foo.fi&quot;.)</p>
<dt><code>pristine-headers</code></p>
<dd> Do not MIME encode the headers. Set to &quot;yes&quot; to not encode, anything else (including empty or unset) means encoding will happen.</dl>
<h2>EXAMPLES</h2>
<p> To create a list called <i>moviefans [at] example.com</i>, owned by <i>ding [at] example.com</i>, use the following command (all on one line): </p>
<p>enemies &#8211; of &#8211; carlotta&#8211; name = moviefans[at] example.com&#8211; owner = ding[at] example.com&#8211; create</p>
<p> Note that you need to arrange mail to arrive at the list (and its command addresses) by configuring your mail system. For Qmail and Postfix, see below. </p>
<p> To see the subscribers on that list: </p>
<pre><code>
enemies - of - carlotta-- name = moviefans[at] example.com-- list
</code></pre>
<p> People wanting to subscribe to the list should mail </p>
<pre>
<dl><dt><dd>moviefans-subscribe [at] example.com
</dl>
</pre>
<h2>QMAIL</h2>
<p> With QMail, to arrange for incoming mail to be processed by Enemies of Carlotta, you need to create a couple of <i>.qmail-extension</i> files per list. For example, if your username is joe and you wish to run the joe-fans mailing list, you need to create two files, <i>.qmail-fans</i> and <i>.qmail-fans-default</i>, containing </p>
<dl>
<dt>
<dd> |enemies-of-carlotta &#8211;incoming</dl>
<p> If you&#8217;re running a virtual domain, example.com, and the mails are being delivered to via <i>/var/qmail/control/virtualdomains</i> to <i>joe-exampledotcom</i>, the files would be called <i>.qmail-exampledotcom-fans</i> and <i>.qmail-exampledotcom-fans-default</i> and would contain </p>
<dl>
<dt>
<dd> |enemies-of-carlotta &#8211;incoming &#8211;skip-prefix=joe-exampledotcom-</dl>
<p> (all on one line, of course, in case the manual page formatter breaks it on several lines).</p>
<h2>COURIER-MTA</h2>
<p> For Courier-MTA, the instructions are similar to the Qmail ones above. If your user name is joe and you wish to run the joe-fans email list, you need to create the two files .courier-fans and .courier-fans-default in your home directory with the content </p>
<dl>
<dt>
<dd> |enemies-of-carlotta &#8211;is-list &#8211;name $RECIPIENT || exit 67<br />
 |enemies-of-carlotta &#8211;incoming</dl>
<p> (The former file needs only the second line, but the first line does no harm and it is easier to keep track of things when the files have the same content. Note that $RECIPIENT should be included verbatim, it is not a metavariable for you to expand.) </p>
<p> If you are running a virtual domain configured so that all mail to the domain @example.com is delivered to joe-exampledotcom, you need to create the files .courier-exampledotcom-fans and </p>
<dl>
<dt>
<dd> |enemies-of-carlotta &#8211;is-list &#8211;name $RECIPIENT &#8211;skip-prefix=joe-exampledotcom || exit 67<br />
 |enemies-of-carlotta &#8211;incoming &#8211;skip-prefix=joe-exampledotcom</dl>
<p> If the virtual domain is for list use only, then it is sufficient to create only the file .courier-exampledotcom-default containing the latter two lines.</p>
<h2>POSTFIX</h2>
<p> With Postfix, you need to set up a <i>.forward</i> file containing </p>
<dl>
<dt>
<dd> &quot;|procmail -p&quot;</dl>
<p> and then a <i>.procmailrc</i> file containing </p>
<dl>
<dt>
<dd> :0<br />
 * ? enemies-of-carlotta &#8211;name=$RECIPIENT &#8211;is-list<br />
 | enemies-of-carlotta &#8211;incoming</dl>
<p> To use Enemies of Carlotta with a Postfix virtual domain, you need to set up a <i>virtual regular expression map</i>, typically called <i>/etc/postfix/virtual_regexp</i> (add <i>virtual_maps = regexp:/etc/postfix/virtual_regexp</i> to your <i>/etc/postfix/main.cf</i> file to enable it). The regexp file needs to do ugly things to preserve the recipient address. Add the following to the regexp file: </p>
<dl>
<dt>
<dd> /^your.virtual.domain$/ dummy<br />
 /^(yourlist|yourlist-.*)@(your.virtual.domain)$/ joe+virtual-$1</dl>
<p> That&#8217;s two lines. Use <code>joe-virtual</code> instead, if <i>recipient_delimiter</i> for your Postfix is configured to a minus instead of a plus.. Then, in your <i>.procmailrc</i> file, add the <i>&#8211;skip-prefix=joe-virtual-</i> and <i>&#8211;domain=your.virtual.domain</i> options to both calls to <code>enemies-of-carlotta</code>. </p>
<p> (Yes, I think these things are much too complicated, too.)</p>
<h2>MAIL COMMANDS</h2>
<p> Users and list owners use Enemies of Carlotta via e-mail using command addresses such as <code>foo-subscribe [at] example.com</code>. Here is a list of all command addresses list users and owners can give. In all these examples, the name of the mailing list is <code>foo [at] example.com</code>.</p>
<h3>Mail commands anyone can use</h3>
<p> These commands are meant for everyone&#8217;s use. They don&#8217;t require any special priviledges.</p>
<dl>
<dt><code>foo [at] example.com</code></p>
<dd> Send mail to all list subscribers. The message may have to be manually approved by the list moderators first, and they have the power to reject a message.</p>
<dt><code>foo-owner [at] example.com</code></p>
<dd> Send mail to the list owner or owners instead.</p>
<dt><code>foo-help [at] example.com</code></p>
<dd> Sending mail to this address makes the list manager reply with the help message for the list.</p>
<dt><code>foo-subscribe [at] example.com</code></p>
<dd> Send mail to this address to subscribe to a list. The list manager will respond with a confirmation request. You won&#8217;t be subscribed unless you reply to the confirmation request. This way, malicious people can&#8217;t put your address on a mailing list, or many mailing lists.</p>
<dt><code>foo-subscribe-joe=example.com [at] example.com</code></p>
<dd> This is a second form of the subscription address. If you want to subscribe to the list with another address than the one you&#8217;re sending mail from, use this one. In this case, the address to be subscribed is joe [at] example.com. Note that the confirmation request is sent to Joe, since it is his address that is to be added to the list.</p>
<dt><code>foo-unsubscribe [at] example.com</code></p>
<dd> To unsubscribe from a list, send mail to this address from the address that is subscribed to the list. Again, you will receive a confirmation request, to prevent malicious people from unsubscribing you against your will.</p>
<dt><code>foo-unsubscribe-joe=example.com [at] example.com</code></p>
<dd> To unsubscribe Joe, use this address. Again, it is Joe who gets to confirm.</dl>
<h3>Mail commands for the list owners</h3>
<p> These are commands that list owners can use to administer their list.</p>
<dl>
<dt><code>foo-subscribe-joe=example.com [at] example.com</code></p>
<dd> If a list owner sends mail like this, it is they who get the confirmation request, not Joe. It is generally better for people to subscribe themselves, but sometimes list owners want to do it, when they have permission from the person and feel helpful.</p>
<dt><code>foo-unsubscribe-joe=example.com [at] example.com</code></p>
<dd> List owners can also unsubscribe other people.</p>
<dt><code>foo-list [at] example.com</code></p>
<dd> To see who are on the list, this is the address to use. It only works if the sender address is one of the list owners. The sender address is the one used on the SMTP level, not the one in the From: header.</p>
<dt><code>foo-setlist [at] example.com</code></p>
<dd> This lets a list owner set the whole subscriber list at once. This is similar to using lots and lots and lots of -subscribe and -unsubscribe commands, only less painful. Everyone who is added to the list gets a welcome message, and everyone who is removed from the list gets a goodbye message.</p>
<dt><code>foo-setlistsilently [at] example.com</code></p>
<dd> This is similar to -setlist, but no welcome and goodbye messages are sent.</dl>
<h2>PLUGINS</h2>
<p> Enemies of Carlotta supports plugins. If you don&#8217;t know what Python programming is, you may want to skip this section. </p>
<p> A plugin is a Python module (file named with a <code>.py</code> suffix), placed in the <code>~/.enemies-of-carlotta/plugins</code> directory. The plugins are loaded automatically upon startup, if their declared interface version matches the one implemented by Enemies of Carlotta. The interface version is declared by the module global variable <code>PLUGIN_INTERFACE_VERSION</code>. </p>
<p> Plugins can define hook functions that are called by appropriate places in the EoC code. At the moment, the only hook function is <code>send_mail_to_subscribers_hook</code>, which can manipulate a mail message before it is sent to the subscribers. The function must look like this: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> def send_mail_to_subscribers_hook(list, text): </p>
<p> The <i>list</i> argument is a reference to the <i>MailingList</i> object that corresponds to the list in question, and <i>text</i> is the complete text of the mail message as it exists. The function must return the new contents of the mail message.</p>
<h2>FILES</h2>
<dl>
<dt><i>~/.enemies-of-carlotta</i></p>
<dd> All files related to your mailing lists.</p>
<dt><i>~/.enemies-of-carlotta/secret</i></p>
<dd> Secret password used to generate signed addresses for bounce checking and subscription verification.</p>
<dt><i>~/.enemies-of-carlotta/foo [at] example.com</i></p>
<dd> Directory containing data pertaining to the foo [at] example.com list. Except for the <i>config</i> file in this directory, you shouldn&#8217;t edit anything by hand.</p>
<dt><i>~/.enemies-of-carlotta/foo [at] example.com/config</i></p>
<dd> Configuration file for the mailing list. You may need to edit this file by hand if you wish to change moderation status or list owners.</dl>
<h2>SEE ALSO</h2>
<p> You may want to visit the <i>Enemies of Carlotta</i> home page at <i><a rel="nofollow" href="http://www.iki.fi/liw/eoc/">http://www.iki.fi/liw/eoc/</a></i>. </p>
<h2>Index</h2>
