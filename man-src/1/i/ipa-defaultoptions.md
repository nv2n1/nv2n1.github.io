---

title: "ipa-defaultoptions(1)"
name: "ipa-defaultoptions"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-defaultoptions/"
description: "ipa-defaultoptions – Display or modify the IPA Search and User Policies"
---

<p> ipa-defaultoptions &#8211; Display or modify the IPA Search and User Policies</p>
<h2>SYNOPSIS</h2>
<p> ipa-defaultoptions [&#8211;maxusername number] [&#8211;homedir directory] [&#8211;defaultshell shell] [&#8211;defaultgroup group] [&#8211;emaildomain domain] [&#8211;searchtimelimit number] [&#8211;searchrecordslimit number] [&#8211;usersearch fields] [&#8211;groupsearch fields] [-v|&#8211;verbose] ipa-defaultoptions &#8211;show</p>
<h2>DESCRIPTION</h2>
<p> Displays or updates the IPA Search and User Policy. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;maxusername</code>=<i>MAXUSERNAME</i></dt>
<dd> Max. Length of a username</dd>
<dt><code>&#8211;homedir</code>=<i>HOMEDIR</i></dt>
<dd> Default location of home directories</dd>
<dt><code>&#8211;defaultshell</code>=<i>DEFAULTSHELL</i></dt>
<dd> Default shell for new users</dd>
<dt><code>&#8211;defaultgroup</code>=<i>DEFAULTGROUP</i></dt>
<dd> Default group for new users</dd>
<dt><code>&#8211;emaildomain</code>=<i>EMAILDOMAIN</i></dt>
<dd> Default e-mail domain</dd>
<dt><code>&#8211;searchtimelimit</code>=<i>SEARCHTIMELIMIT</i></dt>
<dd> Max. amount of time (sec.) for a search (-1 for unlimited)</dd>
<dt><code>&#8211;searchrecordslimit</code>=<i>SEARCHRECORDSLIMIT</i></dt>
<dd> Max. number of records to search (-1 for unlimited)</dd>
<dt><code>&#8211;usersearch</code>=<i>USERSEARCH</i></dt>
<dd> A comma-separated list of fields to search when searching for users</dd>
<dt><code>&#8211;groupsearch</code>=<i>GROUPSEARCH</i></dt>
<dd> A comma-separated list of fields to search when searching for groups</dd>
<dt><code>&#8211;show</code></dt>
<dd> Display the current password policy.</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Display the XML-RPC request and response for more verbose debugging output</dd></dl>
<h2>EXIT STATUS</h2>
<p> The exit status is 0 on success, nonzero on error. </p>
