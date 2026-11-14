---
title: "grid-change-pass-phrase(1)"
name: "grid-change-pass-phrase"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grid-change-pass-phrase/"
description: "grid-change-pass-phrase – Change the pass phrase of a private key"
---

<h2 class="name">NAME</h2>
<p> grid-change-pass-phrase &#8211; Change the pass phrase of a private key </p>
<h2>SYNOPSIS</h2>
<p> <code>grid-change-pass-phrase</code> -help | -usage | -version | -versions </p>
<p> <code>grid-change-pass-phrase</code> [-file <i>PRIVATE-KEY</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>grid-change-pass-phrase</code> program changes the pass phrase protecting a private key or PKCS12 bundle containing a private key and certificate. By default, <code>grid-change-pass-phrase</code> uses the <i>X509_USER_KEY</i> environment variable to locate the private key. If that is not set, then it looks for $HOME/.globus/userkey.pem and $HOME/.globus/usercred.p12 in succession. The path to a key can be specified by using the <i>-file</i> command-line option.</p>
<h2>OPTIONS</h2>
<p> The full set of command-line options to <code>grid-change-pass-phrase</code> are: </p>
<p> <code>-help, -usage</code></p>
<dl>
<dt>
<dd> Display the command-line options to <code>grid-change-pass-phrase</code> and exit.</dl>
<p> <code>-version, -versions</code></p>
<dl>
<dt>
<dd> Display the version number of the <code>grid-change-pass-phrase</code> command. The second form includes more details.</dl>
<p> <code>-file </code><i>PRIVATE-KEY</i></p>
<dl>
<dt>
<dd> Change the pass phrase of the private key named by <i>PRIVATE-KEY</i> instead of the default.</dl>
<h2>EXAMPLES</h2>
<p> Change the pass phrase of the default private key: </p>
<dl>
<dt>
<dd>
<pre>
% grid-change-pass-phrase
Enter pass phrase for /home/juser/.globus/userkey.pem:
writing RSA key
Enter PEM pass phrase: XXXXXXXX
Verifying - Enter PEM pass phrase: XXXXXXXX
</pre>
</dl>
<h2>ENVIRONMENT</h2>
<p> The following environment variables affect the execution of <code>grid-change-pass-phrase</code>: </p>
<p> <code>X509_USER_KEY</code></p>
<dl>
<dt>
<dd> Path to the default private key file.</dl>
<h2>AUTHOR</h2>
<p> Copyright &#169; 1999-2014 University of Chicago </p>
<h2>Index</h2>
