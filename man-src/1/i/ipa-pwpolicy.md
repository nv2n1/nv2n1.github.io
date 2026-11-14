---
title: "ipa-pwpolicy(1)"
name: "ipa-pwpolicy"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-pwpolicy/"
description: "ipa-pwpolicy – Display or modify the IPA password policy"
---

<h2>NAME</h2>
<p> ipa-pwpolicy &#8211; Display or modify the IPA password policy </p>
<h2>SYNOPSIS</h2>
<p> ipa-pwpolicy [&#8211;maxlife days] [&#8211;minlife hours] [&#8211;history number] [&#8211;minclasses number] [&#8211;minlength number]</p>
<dl>
<dt>ipa-pwpolicy &#8211;show</p>
<dd></dl>
<h2>DESCRIPTION</h2>
<p> Displays or updates the IPA password policy. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;maxlife</code>=<i>days</i></p>
<dd> Set the maximum Password Lifetime in days</p>
<dt><code>&#8211;minlife</code>=<i>hours</i></p>
<dd> Set the minimum Password Lifetime in hours</p>
<dt><code>&#8211;history</code>=<i>integer</i></p>
<dd> The number of passwords stored in the password history. A value of 0 means do not store a password history.</p>
<dt><code>&#8211;minclasses</code>=<i>integer</i></p>
<dd> Set the minimum number of character classes required in a password. The classes are alpha, numeric, mixed-case and special characters.</p>
<dt><code>&#8211;minlength</code>=<i>integer</i></p>
<dd> Set the minimum password length.</p>
<dt><code>&#8211;show</code></p>
<dd> Display the current password policy.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Display the XML-RPC request and response for more verbose debugging output</dl>
<h2>EXIT STATUS</h2>
<p> The exit status is 0 on success, nonzero on error. </p>
<h2>Index</h2>
