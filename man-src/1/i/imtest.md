---
title: "imtest(1)"
name: "imtest"
section: "1"
letter: "i"
url: "/docs/linux/man/1-imtest/"
description: "imtest – interactive IMAP test program"
---

<p>&nbsp;<wbr>*</p>
<h2 class="name">NAME</h2>
<p> imtest &#8211; interactive IMAP test program </p>
<h2>SYNOPSIS</h2>
<p> <code>imtest</code> [ <code>-t</code> <i>keyfile</i> ] [ <code>-p</code> <i>port</i> ] [ <code>-m</code> <i>mechanism</i> ] </p>
<p>&nbsp;<wbr>[ <code>-a</code> <i>userid</i> ] [ <code>-u</code> <i>userid</i> ] [ <code>-k</code> <i>num</i> ] [ <code>-l</code> <i>num</i> ] </p>
<p>&nbsp;<wbr>[ <code>-r</code> <i>realm</i> ] [ <code>-f</code> <i>file</i> ] [ <code>-n</code> <i>num</i> ] [ <code>-s</code> ] [ <code>-q</code> ] </p>
<p>&nbsp;<wbr>[ <code>-c</code> ] [ <code>-i</code> ] [ <code>-z</code> ] [ <code>-v</code> ] [ <code>-I</code> <i>file</i> ] [ <code>-x</code> <i>file</i> ] </p>
<p>&nbsp;<wbr>[ <code>-X</code> <i>file</i> ] [ <code>-o</code> <i>option</i><code>=</code><i>value</i> ] <i>hostname</i></p>
<h2>DESCRIPTION</h2>
<p> <i>imtest</i> is a utility that allows you to authenticate to a IMAP or IMSP server and interactively issue commands to it. Once authenticated you may issue any IMAP or IMSP command by simply typing it in. It is capable of multiple SASL authentication mechanisms and handles encryption layers transparently. This utility is often used for testing the operation of a imsp or imap server. Also those developing IMAP clients find it useful. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-t</code><i> keyfile</i></p>
<dd> Enable TLS. <i>keyfile</i> contains the TLS public and private keys. Specify <code>&quot;&quot;</code> to negotiate a TLS encryption layer but not use TLS authentication.</p>
<dt><code>-p</code><i> port</i></p>
<dd> Port to connect to. If left off this defaults to <code>imap</code> as defined in /etc/services.</p>
<dt><code>-m</code><i> mechanism</i></p>
<dd> Force imtest to use <i>mechanism</i> for authentication. If not specified the strongest authentication mechanism supported by the server is chosen. Specify <code>login</code> to use the LOGIN command instead of AUTHENTICATE.</p>
<dt><code>-a</code><i> userid</i></p>
<dd> Userid to use for authentication; defaults to the current user. This is the userid whose password or credentials will be presented to the server for verification.</p>
<dt><code>-u</code><i> userid</i></p>
<dd> Userid to use for authorization; defaults to the current user. This is the userid whose identity will be assumed after authentication. <code>NOTE:</code> This is only used with SASL mechanisms that allow proxying (e.g. PLAIN, DIGEST-MD5).</p>
<dt><code>-k</code><i> num</i></p>
<dd> Minimum protection layer required.</p>
<dt><code>-l</code><i> num</i></p>
<dd> Maximum protection layer to use (<code>0</code>=none; <code>1=</code>integrity; etc). For example if you are using the KERBEROS_V4 authentication mechanism specifying <code>0</code> will force imtest to not use any layer and specifying <code>1</code> will force it to use the integrity layer. By default the maximum supported protection layer will be used.</p>
<dt><code>-r</code><i> realm</i></p>
<dd> Specify the <i>realm</i> to use. Certain authentication mechanisms (e.g. DIGEST-MD5) may require one to specify the realm.</p>
<dt><code>-f</code><i> file</i></p>
<dd> Pipe <i>file</i> into connection after authentication.</p>
<dt><code>-n</code><i> num</i></p>
<dd> Number of authentication attempts; default = 1. The client will attempt to do SSL/TLS session reuse and/or fast reauth (e.g. DIGEST-MD5), if possible.</p>
<dt><code>-s</code></p>
<dd> Enable IMAP over SSL (imaps).</p>
<dt><code>-q</code></p>
<dd> Enable IMAP COMPRESSion (before the last authentication attempt).</p>
<dt><code>-c</code></p>
<dd> Enable challenge prompt callbacks. This will cause the OTP mechanism to ask for the the one-time password instead of the secret pass-phrase (library generates the correct response).</p>
<dt><code>-i</code></p>
<dd> Don&#8217;t send an initial client response for SASL mechanisms, even if the protocol supports it.</p>
<dt><code>-I</code><i> file</i></p>
<dd> Echo the PID of the running process into <i>file</i> (This can be useful with -X).</p>
<dt><code>-x</code><i> file</i></p>
<dd> Open the named socket for the interactive portion</p>
<dt><code>-X</code><i> file</i></p>
<dd> Like -x, only close all file descriptors &amp; daemonize the process.</p>
<dt><code>-o </code><i>option</i><code>=</code><i>value</i></p>
<dd> Set the SASL <i>option</i> to <i>value</i>.</p>
<dt><code>-v</code></p>
<dd> Verbose. Print out more information than usual.</p>
<dt><code>-z</code></p>
<dd> Timing test.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-imapd/">imapd</a>(8)</code> </p>
<h2>Index</h2>
