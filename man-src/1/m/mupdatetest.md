---
title: "mupdatetest(1)"
name: "mupdatetest"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mupdatetest/"
description: "mupdatetest – interactive MUPDATE test program"
---

<p>&nbsp;<wbr>*</p>
<h2 class="name">NAME</h2>
<p> mupdatetest &#8211; interactive MUPDATE test program </p>
<h2>SYNOPSIS</h2>
<p> <code>mupdatetest</code> [ <code>-p</code> <i>port</i> ] [ <code>-m</code> <i>mechanism</i> ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[ <code>-a</code> <i>userid</i> ] [ <code>-u</code> <i>userid</i> ] [ <code>-k</code> <i>num</i> ] [ <code>-l</code> <i>num</i> ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[ <code>-r</code> <i>realm</i> ] [ <code>-f</code> <i>file</i> ] [ <code>-n</code> <i>num</i> ] [ <code>-q</code> ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[ <code>-c</code> ] [ <code>-i</code> ] [ <code>-o</code> <i>option</i><code>=</code><i>value</i> ] [ <code>-v</code> ] <i>hostname</i></p>
<h2>DESCRIPTION</h2>
<p> <i>mupdatetest</i> is a utility that allows you to authenticate to a MUPDATE server and interactively issue commands to it. Once authenticated you may issue any MUPDATE command by simply typing it in. It is capable of multiple SASL authentication mechanisms and handles encryption layers transparently. This utility is often used for testing the operation of a mupdate server. Note that you must be an admin in order to authenticate to an mupdate server. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p</code><i> port</i></p>
<dd> Port to connect to. If left off this defaults to <code>mupdate</code> as defined in /etc/services.</p>
<dt><code>-m</code><i> mechanism</i></p>
<dd> Force mupdatetest to use <i>mechanism</i> for authentication. If not specified the strongest authentication mechanism supported by the server is chosen.</p>
<dt><code>-a</code><i> userid</i></p>
<dd> Userid to use for authentication; defaults to the current user. This is the userid whose password or credentials will be presented to the server for verification.</p>
<dt><code>-u</code><i> userid</i></p>
<dd> Userid to use for authorization; defaults to the current user. This is the userid whose identity will be assumed after authentication. <code>NOTE:</code> This is only used with SASL mechanisms that allow proxying (e.g. PLAIN, DIGEST-MD5).</p>
<dt><code>-k</code><i> num</i></p>
<dd> Minimum protection layer required.</p>
<dt><code>-l</code><i> num</i></p>
<dd> Maximum protection layer to use (<code>0</code>=none; <code>1=</code>integrity; etc). For example if you are using the KERBEROS_V4 authentication mechanism specifying <code>0</code> will force mupdatetest to not use any layer and specifying <code>1</code> will force it to use the integrity layer. By default the maximum supported protection layer will be used.</p>
<dt><code>-r</code><i> realm</i></p>
<dd> Specify the <i>realm</i> to use. Certain authentication mechanisms (e.g. DIGEST-MD5) may require one to specify the realm.</p>
<dt><code>-f</code><i> file</i></p>
<dd> Pipe <i>file</i> into connection after authentication.</p>
<dt><code>-n</code><i> num</i></p>
<dd> Number of authentication attempts; default = 1. The client will attempt to fast reauth (e.g. DIGEST-MD5), if possible.</p>
<dt><code>-q</code></p>
<dd> Enable MUPDATE COMPRESSion (before the last authentication attempt).</p>
<dt><code>-c</code></p>
<dd> Enable challenge prompt callbacks. This will cause the OTP mechanism to ask for the the one-time password instead of the secret pass-phrase (library generates the correct response).</p>
<dt><code>-i</code></p>
<dd> Don&#8217;t send an initial client response for SASL mechanisms, even if the protocol supports it.</p>
<dt><code>-o </code><i>option</i><code>=</code><i>value</i></p>
<dd> Set the SASL <i>option</i> to <i>value</i>.</p>
<dt><code>-v</code></p>
<dd> Verbose. Print out more information than usual.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-mupdate/">mupdate</a>(8)</code> </p>
<h2>Index</h2>
