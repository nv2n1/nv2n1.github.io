---
title: "wimlib-imagex-verify(1)"
name: "wimlib-imagex-verify"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wimlib-imagex-verify/"
description: "wimlib-imagex-verify – Verify a WIM file"
---

<h2>NAME</h2>
<p> wimlib-imagex-verify &#8211; Verify a WIM file</p>
<h2>SYNOPSIS</h2>
<p> <code>wimlib-imagex verify</code> <i>WIMFILE</i> [<i>OPTION</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>wimlib-imagex verify</code> checks the validity of the specified WIM archive. This command is also available as simply <code>wimverify</code> if the appropriate hard link or batch file has been installed. </p>
<p> Specifically, this command performs the following verifications on the WIM archive:</p>
<dl>
<dt>&bull;</p>
<dd> Verify that the WIM file can be successfully opened, which involves parsing the header, blob table, and XML data.</p>
<dt>&bull;</p>
<dd> If the WIM archive contains an integrity table, verify the integrity of the entire WIM archive. Otherwise, print a warning.</p>
<dt>&bull;</p>
<dd> Verify that the metadata for each image in the WIM archive can be successfully parsed.</p>
<dt>&bull;</p>
<dd> Verify that all files needed by each image are actually contained in the WIM archive or in one of the WIM archives referenced by the <code>&#8211;ref</code> option.</p>
<dt>&bull;</p>
<dd> Verify that all files contained in the WIM archive can be successfully decompressed, with matching cryptographic checksums.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;ref</code>=&quot;<i>GLOB</i>&quot;</p>
<dd> File glob of additional WIMs or split WIM parts to reference resources from. This option can be specified multiple times. Note: <i>GLOB</i> is listed in quotes because it is interpreted by <code>wimlib-imagex</code> and may need to be quoted to protect against shell expansion.</p>
<dt><code>&#8211;nocheck</code></p>
<dd> Do not check the WIM file&#8217;s contents against its integrity table (if it has one).</dl>
<h2>NOTES</h2>
<p> This is a read-only command. It will never modify the WIM file. </p>
<p> In the future, this command might do more thorough verifications than it does now.</p>
<h2>EXAMPLES</h2>
<p> Verify the WIM file &#8216;boot.wim&#8217;:</p>
<dl>
<dt>
<dd>
<p> wimverify boot.wim</dl>
<p> Verify the split WIM file consisting of &#8216;boot.swm&#8217;, &#8216;boot2.swm&#8217;, &#8216;boot3.swm&#8217;, &#8230;:</p>
<dl>
<dt>
<dd>
<p> wimverify boot.swm &#8211;ref=&quot;boot*.swm&quot;</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wimlib-imagex/">wimlib-imagex</a></code>(1) <code><a href="/docs/linux/man/1-wimlib-imagex-optimize/">wimlib-imagex-optimize</a></code>(1) </p>
<h2>Index</h2>
