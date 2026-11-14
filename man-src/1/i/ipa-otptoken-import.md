---
title: "ipa-otptoken-import(1)"
name: "ipa-otptoken-import"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipa-otptoken-import/"
description: "ipa-otptoken-import – Imports OTP tokens from RFC 6030 XML file"
---

<h2>NAME</h2>
<p> ipa-otptoken-import &#8211; Imports OTP tokens from RFC 6030 XML file</p>
<h2>SYNOPSIS</h2>
<p> ipa-otptoken-import [options] &lt;infile&gt; &lt;outfile&gt;</p>
<h2>DESCRIPTION</h2>
<p> Running the command will attempt to import all tokens specified in <code>infile</code>. If the command is unable to import a token, the reason for the failure will be printed to standard error and all failed tokens will be written to the <code>outfile</code> for further inspection. </p>
<p> If the <code>infile</code> contains encrypted token data, then the <i>keyfile</i> (<code>-k</code>) option MUST be specified. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-k</code> <i>keyfile</i></p>
<dd> File containing the key used to decrypt the token data.</dl>
<h2>EXIT STATUS</h2>
<p> 0 if the command was successful </p>
<p> 1 if an error occurred </p>
<h2>Index</h2>
