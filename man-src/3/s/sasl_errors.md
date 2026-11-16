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
</dt><dd>Success
</dd><dt>SASL_CONTINUE
</dt><dd>Another step is needed in authentication
</dd><dt>SASL_FAIL
</dt><dd>Generic Failure
</dd><dt>SASL_NOMEM
</dt><dd>Memory shortage failure
</dd><dt>SASL_BUFOVER
</dt><dd>Overflowed buffer
</dd><dt>SASL_NOMECH
</dt><dd>Mechanism not supported / No mechanisms matched requirements
</dd><dt>SASL_BADPROT
</dt><dd>Bad / Invalid Protocol or Protocol cancel
</dd><dt>SASL_NOTDONE
</dt><dd>Can't request information / Not applicable until later in exchange
</dd><dt>SASL_BADPARAM
</dt><dd>Invalid Parameter Supplied
</dd><dt>SASL_TRYAGAIN
</dt><dd>Transient Failure (e.g. weak key)
</dd><dt>SASL_BADMAC
</dt><dd>Integrity Check Failed
</dd><dt>SASL_NOTINIT
</dt><dd>SASL library not initialized 
</dd></dl>

<h2>Client-only Result Codes</h2>

<dl><dt>SASL_INTERACT
</dt><dd>Needs user interaction
</dd><dt>SASL_BADSERV
</dt><dd>Server failed mutual authentication step
</dd><dt>SASL_WRONGMECH
</dt><dd>Mechanism does not support requested feature 
</dd></dl>

<h2>Server-only Result Codes</h2>

<dl><dt>SASL_BADAUTH
</dt><dd>Authentication Failure
</dd><dt>SASL_NOAUTHZ
</dt><dd>Authorization Failure
</dd><dt>SASL_TOOWEAK
</dt><dd>Mechanism too weak for this user
</dd><dt>SASL_ENCRYPT
</dt><dd>Encryption needed to use mechanism
</dd><dt>SASL_TRANS
</dt><dd>One time use of a plaintext password will enable requested mechanism for user
</dd><dt>SASL_EXPIRED
</dt><dd>Passphrase expired, must be reset
</dd><dt>SASL_DISABLED
</dt><dd>Account Disabled
</dd><dt>SASL_NOUSER
</dt><dd>User Not Found
</dd><dt>SASL_BADVERS
</dt><dd>Version mismatch with plug-in
</dd><dt>SASL_NOVERIFY
</dt><dd>USer exists, but no verifier for user 
</dd></dl>

<h2>Password Setting Result Codes</h2>

<dl><dt>SASL_PWLOCK
</dt><dd>Passphrase locked
</dd><dt>SASL_NOCHANGE
</dt><dd>Requested change was not needed
</dd><dt>SASL_WEAKPASS
</dt><dd>Passphrase is too week for security policy.
</dd><dt>SASL_NOUSERPASS
</dt><dd>User supplied passwords are not permitted 
</dd></dl>

<h2>Conforming To</h2>

RFC 4422 

<h2>See Also</h2>

<a HREF="/docs/linux/man/3-sasl/">sasl</a>(3) 
