---

title: "ipa-adduser(1)"
name: "ipa-adduser"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-adduser/"
description: "ipa-adduser – Add a user"
---

<h2>NAME</h2>
<p> ipa-adduser &#8211; Add a user </p>
<p> ipa-adduser [<i>OPTION</i>]&#8230; <i>user</i> </p>
<p> Adds a user with username <i>user</i>. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;gecos</code>=<i>gecos</i></dt>
<dd> Set the SM]GECOS field to <i>gecos</i>. The SM]GECOS field is traditionally used to store user&#8217;s real name and other information.</dd>
<dt><code>-d</code>, <code>&#8211;directory</code>=<i>directory</i></dt>
<dd> Set user&#8217;s home directory to <i>directory</i>. If this option is not present, a default specified by the <code>freeIPA configuration is used.</code></dd>
<dt><code>-f</code>, <code>&#8211;firstname</code>=<i>givenName</i></dt>
<dd> Set user&#8217;s first name to <i>givenName</i>.</dd>
<dt><code>-l</code>, <code>&#8211;lastname</code>=<i>familyName</i></dt>
<dd> Set user&#8217;s last name to <i>familyName</i>.</dd>
<dt><code>-p</code>, <code>&#8211;password</code>=<i>password</i></dt>
<dd> Set user&#8217;s password to <i>password</i>.</dd>
<dt><code>-P</code></dt>
<dd> Prompt for the user&#8217;s password.</dd>
<dt><code>-s</code>, <code>&#8211;shell</code>=<i>shell</i></dt>
<dd> Set the user&#8217;s login shell to <i>shell</i>. If this option is not present, a default specified by the <code>freeIPA configuration is used.</code></dd>
<dt><code>-G</code>, <code>&#8211;groups</code>=<i>groups</i></dt>
<dd> Add this user to one or more groups in <i>groups</i>. <i>groups</i> is a comma-separated list of groups. Each <i>group</i> must already exist.</dd>
<dt><code>-k</code>, <code>&#8211;krb-principal</code>=<i>principal</i></dt>
<dd> Set this user&#8217;s principal to <i>principal</i>. By default the principal is set to <code>user</code>.</dd>
<dt><code>-M</code>, <code>&#8211;mailAddress</code>=<i>mail</i></dt>
<dd> Set this user&#8217;s e-mail address to <i>mail</i>.</dd>
<dt><code>&#8211;addattr</code> <i>attr=value</i></dt>
<dd> Adds <i>value</i> to attribute <i>attr</i>. Attributes set this way are done after other options. If an attribute is listed more than once or already exists in the entry, it is considered a multi-valued attribute and a list of the values is created.</dd>
<dt><code>&#8211;setattr</code> <i>attr=value</i></dt>
<dd> Set attribute <i>attr</i> to <i>value</i>. Any existing value will be replaced with <i>value</i>.</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Display the XML-RPC request and response for more verbose debugging output.</dd></dl>
<p> The mandatory fields are: user, first name and last name. If any of these are not included on the command line you will be asked interactively. </p>
<p> The password is asked interactively if not passed on the command-line but it isn&#8217;t mandatory. Leaving both values blank will leave the password unset on the account. </p>
<p> If no options are passed then all questions are asked.</p>
<h2>EXIT STATUS</h2>
<p> The exit status is 0 on success, nonzero on error. </p>
