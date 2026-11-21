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
<dt><code>-t</code><i> keyfile</i></dt>
<dd> Enable TLS. <i>keyfile</i> contains the TLS public and private keys. Specify <code>&quot;&quot;</code> to negotiate a TLS encryption layer but not use TLS authentication.</dd>
<dt><code>-p</code><i> port</i></dt>
<dd> Port to connect to. If left off this defaults to <code>imap</code> as defined in /etc/services.</dd>
<dt><code>-m</code><i> mechanism</i></dt>
<dd> Force imtest to use <i>mechanism</i> for authentication. If not specified the strongest authentication mechanism supported by the server is chosen. Specify <code>login</code> to use the LOGIN command instead of AUTHENTICATE.</dd>
<dt><code>-a</code><i> userid</i></dt>
<dd> Userid to use for authentication; defaults to the current user. This is the userid whose password or credentials will be presented to the server for verification.</dd>
<dt><code>-u</code><i> userid</i></dt>
<dd> Userid to use for authorization; defaults to the current user. This is the userid whose identity will be assumed after authentication. <code>NOTE:</code> This is only used with SASL mechanisms that allow proxying (e.g. PLAIN, DIGEST-MD5).</dd>
<dt><code>-k</code><i> num</i></dt>
<dd> Minimum protection layer required.</dd>
<dt><code>-l</code><i> num</i></dt>
<dd> Maximum protection layer to use (<code>0</code>=none; <code>1=</code>integrity; etc). For example if you are using the KERBEROS_V4 authentication mechanism specifying <code>0</code> will force imtest to not use any layer and specifying <code>1</code> will force it to use the integrity layer. By default the maximum supported protection layer will be used.</dd>
<dt><code>-r</code><i> realm</i></dt>
<dd> Specify the <i>realm</i> to use. Certain authentication mechanisms (e.g. DIGEST-MD5) may require one to specify the realm.</dd>
<dt><code>-f</code><i> file</i></dt>
<dd> Pipe <i>file</i> into connection after authentication.</dd>
<dt><code>-n</code><i> num</i></dt>
<dd> Number of authentication attempts; default = 1. The client will attempt to do SSL/TLS session reuse and/or fast reauth (e.g. DIGEST-MD5), if possible.</dd>
<dt><code>-s</code></dt>
<dd> Enable IMAP over SSL (imaps).</dd>
<dt><code>-q</code></dt>
<dd> Enable IMAP COMPRESSion (before the last authentication attempt).</dd>
<dt><code>-c</code></dt>
<dd> Enable challenge prompt callbacks. This will cause the OTP mechanism to ask for the the one-time password instead of the secret pass-phrase (library generates the correct response).</dd>
<dt><code>-i</code></dt>
<dd> Don&#8217;t send an initial client response for SASL mechanisms, even if the protocol supports it.</dd>
<dt><code>-I</code><i> file</i></dt>
<dd> Echo the PID of the running process into <i>file</i> (This can be useful with -X).</dd>
<dt><code>-x</code><i> file</i></dt>
<dd> Open the named socket for the interactive portion</dd>
<dt><code>-X</code><i> file</i></dt>
<dd> Like -x, only close all file descriptors &amp; daemonize the process.</dd>
<dt><code>-o </code><i>option</i><code>=</code><i>value</i></dt>
<dd> Set the SASL <i>option</i> to <i>value</i>.</dd>
<dt><code>-v</code></dt>
<dd> Verbose. Print out more information than usual.</dd>
<dt><code>-z</code></dt>
<dd> Timing test.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code>imapd(8)</code> </p>
