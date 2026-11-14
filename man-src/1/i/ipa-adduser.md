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
<h2>SYNOPSIS</h2>
<p> ipa-adduser [<i>OPTION</i>]&#8230; <i>user</i> </p>
<h2>DESCRIPTION</h2>
<p> Adds a user with username <i>user</i>. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;gecos</code>=<i>gecos</i></p>
<dd> Set the SM]GECOS field to <i>gecos</i>. The SM]GECOS field is traditionally used to store user&#8217;s real name and other information.</p>
<dt><code>-d</code>, <code>&#8211;directory</code>=<i>directory</i></p>
<dd> Set user&#8217;s home directory to <i>directory</i>. If this option is not present, a default specified by the <code>freeIPA configuration is used.</code></p>
<dt><code>-f</code>, <code>&#8211;firstname</code>=<i>givenName</i></p>
<dd> Set user&#8217;s first name to <i>givenName</i>.</p>
<dt><code>-l</code>, <code>&#8211;lastname</code>=<i>familyName</i></p>
<dd> Set user&#8217;s last name to <i>familyName</i>.</p>
<dt><code>-p</code>, <code>&#8211;password</code>=<i>password</i></p>
<dd> Set user&#8217;s password to <i>password</i>.</p>
<dt><code>-P</code></p>
<dd> Prompt for the user&#8217;s password.</p>
<dt><code>-s</code>, <code>&#8211;shell</code>=<i>shell</i></p>
<dd> Set the user&#8217;s login shell to <i>shell</i>. If this option is not present, a default specified by the <code>freeIPA configuration is used.</code></p>
<dt><code>-G</code>, <code>&#8211;groups</code>=<i>groups</i></p>
<dd> Add this user to one or more groups in <i>groups</i>. <i>groups</i> is a comma-separated list of groups. Each <i>group</i> must already exist.</p>
<dt><code>-k</code>, <code>&#8211;krb-principal</code>=<i>principal</i></p>
<dd> Set this user&#8217;s principal to <i>principal</i>. By default the principal is set to <code>user</code>.</p>
<dt><code>-M</code>, <code>&#8211;mailAddress</code>=<i>mail</i></p>
<dd> Set this user&#8217;s e-mail address to <i>mail</i>.</p>
<dt><code>&#8211;addattr</code> <i>attr=value</i></p>
<dd> Adds <i>value</i> to attribute <i>attr</i>. Attributes set this way are done after other options. If an attribute is listed more than once or already exists in the entry, it is considered a multi-valued attribute and a list of the values is created.</p>
<dt><code>&#8211;setattr</code> <i>attr=value</i></p>
<dd> Set attribute <i>attr</i> to <i>value</i>. Any existing value will be replaced with <i>value</i>.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Display the XML-RPC request and response for more verbose debugging output.</dl>
<p> The mandatory fields are: user, first name and last name. If any of these are not included on the command line you will be asked interactively. </p>
<p> The password is asked interactively if not passed on the command-line but it isn&#8217;t mandatory. Leaving both values blank will leave the password unset on the account. </p>
<p> If no options are passed then all questions are asked.</p>
<h2>EXIT STATUS</h2>
<p> The exit status is 0 on success, nonzero on error. </p>
<h2>Index</h2>
