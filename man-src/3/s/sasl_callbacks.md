---
title: "sasl_callbacks(3)"
name: "sasl_callbacks"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_callbacks/"
description: "sasl_callbacks – How to work with SASL callbacks"
---

<p>sasl_callbacks &#8211; How to work with SASL callbacks </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;</code></pre>
<h2>Description</h2>
<p><code>sasl_callbacks</code> are used when the application needs some information from the application. Common reasons are getting for getting usernames and passwords. A client MUST specify what callbacks they support in the sasl_client/server_init() or sasl_client/server_new() calls. If an authentication mechanism needs a callback that the application does not state it supports it cannot be used. If a callback has an <code>id</code> parameter that should be checked to make sure you are giving the appropriate value. If an application is using the client side of the library functions to handle the callbacks are not necessary. Instead the application may deal with callbacks via SASL_INTERACT&#8217;s. See sasl_client_start/step() for more information. The list of callbacks follows: </p>
<h2>Common Callbacks</h2>
<dl>
<dt>sasl_getopt_t</dt>
<dd>Get an option value</dd>
<dt>sasl_log_t</dt>
<dd>Log message handler</dd>
<dt>sasl_getpath_t</dt>
<dd>Get path to search for plugins (e.g. SASL mechanisms)</dd>
<dt>sasl_verifyfile_t</dt>
<dd>Verify files for use by SASL</dd>
<dt>sasl_canon_user_t</dt>
<dd>Username canonicalization function. </dd>
</dl>
<h2>Client-only Callbacks</h2>
<dl>
<dt>sasl_getsimple_t</dt>
<dd>Get user/language list</dd>
<dt>sasl_getsecret_t</dt>
<dd>Get authentication secret</dd>
<dt>sasl_chalprompt_t</dt>
<dd>Display challenge and prompt for response</dd>
<dt>sasl_getrealm_t</dt>
<dd>Get the realm for authentication </dd>
</dl>
<h2>Server-only Callbacks</h2>
<dl>
<dt>sasl_authorize_t</dt>
<dd>Authorize policy callback</dd>
<dt>sasl_server_userdb_checkpass_t</dt>
<dd>verify plaintext password</dd>
<dt>sasl_server_userdb_setpass_t</dt>
<dd>set plaintext password</dd>
<dt>sasl_getconfpath_t</dt>
<dd>Get path to search for SASL configuration file (server side only). New in SASL 2.1.22. </dd>
</dl>
<h2>Return Value</h2>
<p>SASL callback functions should return SASL return codes. See sasl.h for a complete list. SASL_OK typically indicates success. </p>
<h2>Conforming To</h2>
<p>RFC 4422 </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_errors/">sasl_errors</a>(3), <a href="/docs/linux/man/3-sasl_authorize_t/">sasl_authorize_t</a>(3), <a href="/docs/linux/man/3-sasl_log_t/">sasl_log_t</a>(3), <a href="/docs/linux/man/3-sasl_getpath_t/">sasl_getpath_t</a>(3), <a href="/docs/linux/man/3-sasl_getconfpath_t/">sasl_getconfpath_t</a>(3), <a href="/docs/linux/man/3-sasl_verifyfile_t/">sasl_verifyfile_t</a>(3), <a href="/docs/linux/man/3-sasl_canon_user_t/">sasl_canon_user_t</a>(3), sasl_getsimple(3), <a href="/docs/linux/man/3-sasl_getsecret_t/">sasl_getsecret_t</a>(3), <a href="/docs/linux/man/3-sasl_chalprompt_t/">sasl_chalprompt_t</a>(3), <a href="/docs/linux/man/3-sasl_getrealm_t/">sasl_getrealm_t</a>(3), <a href="/docs/linux/man/3-sasl_authorize_t/">sasl_authorize_t</a>(3), <a href="/docs/linux/man/3-sasl_server_userdb_checkpass_t/">sasl_server_userdb_checkpass_t</a>(3), <a href="/docs/linux/man/3-sasl_server_userdb_setpass_t/">sasl_server_userdb_setpass_t</a>(3) </p>
