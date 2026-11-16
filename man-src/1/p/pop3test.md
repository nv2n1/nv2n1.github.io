---
title: "pop3test(1)"
name: "pop3test"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pop3test/"
description: "pop3test – interactive POP3 test program"
---

<p>&nbsp;<wbr>*</p>
<h2 class="name">NAME</h2>
<p> pop3test &#8211; interactive POP3 test program </p>
<h2>SYNOPSIS</h2>
<p> <code>pop3test</code> [ <code>-t</code> <i>keyfile</i> ] [ <code>-p</code> <i>port</i> ] [ <code>-m</code> <i>mechanism</i> ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[ <code>-a</code> <i>userid</i> ] [ <code>-u</code> <i>userid</i> ] [ <code>-k</code> <i>num</i> ] [ <code>-l</code> <i>num</i> ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[ <code>-r</code> <i>realm</i> ] [ <code>-f</code> <i>file</i> ] [ <code>-n</code> <i>num</i> ] [ <code>-s</code> ] [ <code>-c</code> ] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[ <code>-i</code> ] [ <code>-o</code> <i>option</i><code>=</code><i>value</i> ] [ <code>-v</code> ] <i>hostname</i></p>
<h2>DESCRIPTION</h2>
<p> <i>pop3test</i> is a utility that allows you to authenticate to a POP3 server and interactively issue commands to it. Once authenticated you may issue any POP3 command by simply typing it in. It is capable of multiple SASL authentication mechanisms and handles encryption layers transparently. This utility is often used for testing the operation of a pop3 server. Also those developing POP3 clients find it useful. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-t</code><i> keyfile</i></dt>
<dd> Enable TLS. <i>keyfile</i> contains the TLS public and private keys. Specify <code>&quot;&quot;</code> to negotiate a TLS encryption layer but not use TLS authentication.</dd>
<dt><code>-p</code><i> port</i></dt>
<dd> Port to connect to. If left off this defaults to <code>pop3</code> as defined in /etc/services.</dd>
<dt><code>-m</code><i> mechanism</i></dt>
<dd> Force pop3test to use <i>mechanism</i> for authentication. If not specified the strongest authentication mechanism supported by the server is chosen. Specify <code>user</code> to use the USER/PASS commands or <code>apop</code> to use the APOP command instead of AUTH.</dd>
<dt><code>-a</code><i> userid</i></dt>
<dd> Userid to use for authentication; defaults to the current user. This is the userid whose password or credentials will be presented to the server for verification.</dd>
<dt><code>-u</code><i> userid</i></dt>
<dd> Userid to use for authorization; defaults to the current user. This is the userid whose identity will be assumed after authentication. <code>NOTE:</code> This is only used with SASL mechanisms that allow proxying (e.g. PLAIN, DIGEST-MD5).</dd>
<dt><code>-k</code><i> num</i></dt>
<dd> Minimum protection layer required.</dd>
<dt><code>-l</code><i> num</i></dt>
<dd> Maximum protection layer to use (<code>0</code>=none; <code>1=</code>integrity; etc). For example if you are using the KERBEROS_V4 authentication mechanism specifying <code>0</code> will force pop3test to not use any layer and specifying <code>1</code> will force it to use the integrity layer. By default the maximum supported protection layer will be used.</dd>
<dt><code>-r</code><i> realm</i></dt>
<dd> Specify the <i>realm</i> to use. Certain authentication mechanisms (e.g. DIGEST-MD5) may require one to specify the realm.</dd>
<dt><code>-f</code><i> file</i></dt>
<dd> Pipe <i>file</i> into connection after authentication.</dd>
<dt><code>-n</code><i> num</i></dt>
<dd> Number of authentication attempts; default = 1. The client will attempt to do SSL/TLS session reuse and/or fast reauth (e.g. DIGEST-MD5), if possible.</dd>
<dt><code>-s</code></dt>
<dd> Enable POP3 over SSL (pop3s).</dd>
<dt><code>-c</code></dt>
<dd> Enable challenge prompt callbacks. This will cause the OTP mechanism to ask for the the one-time password instead of the secret pass-phrase (library generates the correct response).</dd>
<dt><code>-i</code></dt>
<dd> Don&#8217;t send an initial client response for SASL mechanisms, even if the protocol supports it.</dd>
<dt><code>-o </code><i>option</i><code>=</code><i>value</i></dt>
<dd> Set the SASL <i>option</i> to <i>value</i>.</dd>
<dt><code>-v</code></dt>
<dd> Verbose. Print out more information than usual.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code>pop3d(8)</code> </p>
<h2>Index</h2>
