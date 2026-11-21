---

title: "ipa-finduser(1)"
name: "ipa-finduser"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-finduser/"
description: "ipa-finduser – Find a user"
---

<h2>NAME</h2>
<p> ipa-finduser &#8211; Find a user</p>
<p> ipa-finduser [<i>OPTION</i>]&#8230; <i>string</i> </p>
<p> Searches for a user that contains <i>string</i>. </p>
<p> The search is a substring search in the username, given name, family name, telephone number, organization and title attributes. </p>
<p> All entries that match are displayed.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code>, <code>&#8211;all</dt>
<dd> Display all attributes</dd>
<dt>-n</code>, <code>&#8211;notranslate</code></dt>
<dd> Don&#8217;t translate the LDAP attribute names to labels that match the UI.</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Display the XML-RPC request and response for more verbose debugging output.</dd></dl>
<p> By default, the full name, home directory, login shell, and username fields are displayed.</p>
<h2>EXIT STATUS</h2>
<p> 0 if one or more entries were found </p>
<p> 1 if an error occurred </p>
<p> 2 if no matching entries were found </p>
