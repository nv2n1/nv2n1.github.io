---
title: "sasl_errors(3)"
name: "sasl_errors"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_errors/"
---

sasl_errors - SASL error codes 

<h2>Synopsis</h2>

<pre><code>#include &lt;sasl/sasl.h&gt;</code></pre>

<h2>Description</h2>

The following are the general error codes that may be returned by calls into the SASL library, and their meanings (that may vary slightly based on context): 

<h2>Common Result Codes</h2>

<dl><dt>SASL_OK
<dd>Success
<dt>SASL_CONTINUE
<dd>Another step is needed in authentication
<dt>SASL_FAIL
<dd>Generic Failure
<dt>SASL_NOMEM
<dd>Memory shortage failure
<dt>SASL_BUFOVER
<dd>Overflowed buffer
<dt>SASL_NOMECH
<dd>Mechanism not supported / No mechanisms matched requirements
<dt>SASL_BADPROT
<dd>Bad / Invalid Protocol or Protocol cancel
<dt>SASL_NOTDONE
<dd>Can't request information / Not applicable until later in exchange
<dt>SASL_BADPARAM
<dd>Invalid Parameter Supplied
<dt>SASL_TRYAGAIN
<dd>Transient Failure (e.g. weak key)
<dt>SASL_BADMAC
<dd>Integrity Check Failed
<dt>SASL_NOTINIT
<dd>SASL library not initialized 

</dl>

<h2>Client-only Result Codes</h2>

<dl><dt>SASL_INTERACT
<dd>Needs user interaction
<dt>SASL_BADSERV
<dd>Server failed mutual authentication step
<dt>SASL_WRONGMECH
<dd>Mechanism does not support requested feature 

</dl>

<h2>Server-only Result Codes</h2>

<dl><dt>SASL_BADAUTH
<dd>Authentication Failure
<dt>SASL_NOAUTHZ
<dd>Authorization Failure
<dt>SASL_TOOWEAK
<dd>Mechanism too weak for this user
<dt>SASL_ENCRYPT
<dd>Encryption needed to use mechanism
<dt>SASL_TRANS
<dd>One time use of a plaintext password will enable requested mechanism for user
<dt>SASL_EXPIRED
<dd>Passphrase expired, must be reset
<dt>SASL_DISABLED
<dd>Account Disabled
<dt>SASL_NOUSER
<dd>User Not Found
<dt>SASL_BADVERS
<dd>Version mismatch with plug-in
<dt>SASL_NOVERIFY
<dd>USer exists, but no verifier for user 

</dl>

<h2>Password Setting Result Codes</h2>

<dl><dt>SASL_PWLOCK
<dd>Passphrase locked
<dt>SASL_NOCHANGE
<dd>Requested change was not needed
<dt>SASL_WEAKPASS
<dd>Passphrase is too week for security policy.
<dt>SASL_NOUSERPASS
<dd>User supplied passwords are not permitted 

</dl>

<h2>Conforming To</h2>

RFC 4422 

<h2>See Also</h2>

<a HREF="/docs/linux/man/3-sasl/">sasl</a>(3) 
