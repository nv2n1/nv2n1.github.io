---
title: "warnquota-conf(5)"
name: "warnquota-conf"
section: "5"
letter: "w"
url: "/docs/linux/man/5-warnquota-conf/"
description: "warnquota.conf – configuration for warnquota"
---

<p>warnquota.conf &#8211; configuration for warnquota</p>
<h2>Synopsis</h2>
<p><code>/etc/warnquota.conf</code></p>
<h2>Description</h2>
<p>The <code>warnquota.conf</code> file stores a configuration for <code><a href="/docs/linux/man/8-warnquota/">warnquota</a></code>(8) tool which is used to notify an user or a group who exceeds its disk quota limits. </p>
<p> The syntax is an option name followed by a equal sign and the option value. White space characters surrounding the option names and values are allowed. </p>
<p> Empty lines or lines starting with a hash sign or a semicolon are ignored. </p>
<p> An option value can but does not have to be quoted. The value can span across multiple lines provided each previous line ends with a backslash. </p>
<p> Some option values can contain formatting sequences which will be expanded to their respective values. Following sequences are recognizes: </p>
<dl>
<dt><code>%d</code></p>
<dd>domain name</p>
<dt><code>%h</code></p>
<dd>host name</p>
<dt><code>%i</code>, <code>%s</code></p>
<dd>user or group name</p>
<dt><code>%%</code></p>
<dd>literal % character</p>
<dt><code>|</code></p>
<dd>new-line character</dl>
<h2>Options</h2>
<dl>
<dt><code>CC_BEFORE</code></p>
<dd>Send to copy-carbon address only when an user has less than specified grace time left. Value is a number followed by a time unit. Known units are <i>seconds</i>, <i>minutes</i>, <i>hours</i>, and <i>days</i>. Example: <i>5 days</i></p>
<dt><code>CC_TO</code></p>
<dd>An e-mail address to put into copy-carbon (CC:) recipient header. Default value is <i>root</i>.</p>
<dt><code>CHARSET</code></p>
<dd>Defines character set for sent e-mails. Default value will be current locale character set used when executing warnquota command, if locale is not either <i>C</i> or <i>POSIX</i>. Otherwise none character set will be specified in the e-mails.</p>
<dt><code>FROM</code></p>
<dd>Defines From: e-email address. Default value is <i>support [at] localhost</i>.</p>
<dt><code>GROUP_MESSAGE</code></p>
<dd>A text sent as an e-mail body if a group exceeds its limits. This option recognizes formatting sequences.</p>
<dt><code>GROUP_SIGNATURE</code></p>
<dd>A signature text appended to notification for a group. Default value is a general explanation utilizing <code>SUPPORT</code> and <code>PHONE</code> values. This option recognizes formatting sequences.</p>
<dt><code>LDAP_BASEDN</code></p>
<dd>Base distinguished name for LDAP queries.</p>
<dt><code>LDAP_BINDDN</code></p>
<dd>Bind distinguished name for LDAP queries.</p>
<dt><code>LDAP_BINDPW</code></p>
<dd>Bind password for LDAP queries.</p>
<dt><code>LDAP_DEFAULT_MAIL_DOMAIN</code></p>
<dd>Default e-mail address domain of searched user if given LDAP attribute does not specify any.</p>
<dt><code>LDAP_HOST</code></p>
<dd>LDAP server name to connect to if <code>LDAP_URI</code> is not defined.</p>
<dt><code>LDAP_MAIL</code></p>
<dd>A boolean controlling if LDAP has to be used to look up an user&#8217;s e-mail address. Possible values are <i>true</i> and <i>false</i>. Default value is <i>false</i>.</p>
<dt><code>LDAP_MAIL_ATTRIBUTE</code></p>
<dd>The LDAP attribute which holds user&#8217;s e-mail address.</p>
<dt><code>LDAP_PORT</code></p>
<dd>LDAP server port number to connect to if <code>LDAP_URI</code> is not defined.</p>
<dt><code>LDAP_SEARCH_ATTRIBUTE</code></p>
<dd>The LDAP attribute which holds user&#8217;s ID to look up.</p>
<dt><code>LDAP_URI</code></p>
<dd>The URL of LDAP server to use to search user&#8217;s e-mail addresses. This option takes preference over <code>LDAP_HOST</code> and <code>LDAP_PORT</code>. Example: <i><a href="ldaps://example.com:389/">ldaps://example.com:389/</a></i></p>
<dt><code>MESSAGE</code></p>
<dd>A beginning of text sent as an e-mail body if a user exceeds his limits. This option recognizes formatting sequences.</p>
<dt><code>MAIL_CMD</code></p>
<dd>The command to execute to send an e-mail. The e-mail text including all headers is passed to the standard input of the command. Default value is <i>/usr/lib/sendmail -t</i>.</p>
<dt><code>MAILDEV</code></p>
<dd>The device with disk quotas to exclude from sending notifications if there are exceeded limits. This option should identify the device where mail boxes are stored to prevent from bouncing the warnquota notification by local MDA due to no space for storing new e-mails. Special value <i>any</i> denotes all devices.</p>
<dt><code>PHONE</code></p>
<dd>The telephone contact to the user support. Default value is <i>(xxx) xxx-xxxx or (yyy) yyy-yyyy</i>.</p>
<dt><code>SIGNATURE</code></p>
<dd>The end of e-mail body if a user exceeds its limits. Default value is a general explanation utilizing <code>SUPPORT</code> and <code>PHONE</code> values. This option recognizes formatting sequences.</p>
<dt><code>SUBJECT</code></p>
<dd>The text to put into Subject: header. Default value is <i>Disk Quota usage on system</i>.</p>
<dt><code>SUPPORT</code></p>
<dd>The contact to the user support. Default value is <i>support [at] localhost</i>.</dl>
<h2>Example</h2>
<p># comment</p>
<dl>
<dd>FROM = root [at] example.com</p>
<dl>
<dd>SUPPORT = support [at] example.com</p>
<dl>
<dd>PHONE = 1234</dl>
</dl>
</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/warnquota.conf</code></p>
<dd>configuration for <code><a href="/docs/linux/man/8-warnquota/">warnquota</a></code>(8)</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-warnquota/">warnquota</a></code>(8). </p>
