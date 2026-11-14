---
title: "ipa-defaultoptions(1)"
name: "ipa-defaultoptions"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-defaultoptions/"
description: "ipa-defaultoptions – Display or modify the IPA Search and User Policies"
---

<h2>NAME</h2>
<p> ipa-defaultoptions &#8211; Display or modify the IPA Search and User Policies</p>
<h2>SYNOPSIS</h2>
<p> ipa-defaultoptions [&#8211;maxusername number] [&#8211;homedir directory] [&#8211;defaultshell shell] [&#8211;defaultgroup group] [&#8211;emaildomain domain] [&#8211;searchtimelimit number] [&#8211;searchrecordslimit number] [&#8211;usersearch fields] [&#8211;groupsearch fields] [-v|&#8211;verbose] ipa-defaultoptions &#8211;show</p>
<h2>DESCRIPTION</h2>
<p> Displays or updates the IPA Search and User Policy. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;maxusername</code>=<i>MAXUSERNAME</i></p>
<dd> Max. Length of a username</p>
<dt><code>&#8211;homedir</code>=<i>HOMEDIR</i></p>
<dd> Default location of home directories</p>
<dt><code>&#8211;defaultshell</code>=<i>DEFAULTSHELL</i></p>
<dd> Default shell for new users</p>
<dt><code>&#8211;defaultgroup</code>=<i>DEFAULTGROUP</i></p>
<dd> Default group for new users</p>
<dt><code>&#8211;emaildomain</code>=<i>EMAILDOMAIN</i></p>
<dd> Default e-mail domain</p>
<dt><code>&#8211;searchtimelimit</code>=<i>SEARCHTIMELIMIT</i></p>
<dd> Max. amount of time (sec.) for a search (-1 for unlimited)</p>
<dt><code>&#8211;searchrecordslimit</code>=<i>SEARCHRECORDSLIMIT</i></p>
<dd> Max. number of records to search (-1 for unlimited)</p>
<dt><code>&#8211;usersearch</code>=<i>USERSEARCH</i></p>
<dd> A comma-separated list of fields to search when searching for users</p>
<dt><code>&#8211;groupsearch</code>=<i>GROUPSEARCH</i></p>
<dd> A comma-separated list of fields to search when searching for groups</p>
<dt><code>&#8211;show</code></p>
<dd> Display the current password policy.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Display the XML-RPC request and response for more verbose debugging output</dl>
<h2>EXIT STATUS</h2>
<p> The exit status is 0 on success, nonzero on error. </p>
<h2>Index</h2>
