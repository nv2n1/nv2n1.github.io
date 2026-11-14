---
title: "zauth_v2(3)"
name: "zauth_v2"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zauth_v2/"
description: "zauth_v2 – authentication for ZeroMQ servers (deprecated)"
---

<p>zauth_v2 &#8211; authentication for ZeroMQ servers (deprecated)</p>
<h2>Synopsis</h2>
<pre>#ifndef CURVE_ALLOW_ANY
# define CURVE_ALLOW_ANY &quot;*&quot;
#endif
// Constructor
// Install authentication for the specified context. Returns a new zauth
// object that you can use to configure authentication. Note that until you
// add policies, all incoming NULL connections are allowed (classic ZeroMQ
// behaviour), and all PLAIN and CURVE connections are denied. If there was
// an error during initialization, returns NULL.
CZMQ_EXPORT zauth_t *
 zauth_new (zctx_t *ctx);
// Destructor
CZMQ_EXPORT void
 zauth_destroy (zauth_t **self_p);
// Allow (whitelist) a single IP address. For NULL, all clients from this
// address will be accepted. For PLAIN and CURVE, they will be allowed to
// continue with authentication. You can call this method multiple times
// to whitelist multiple IP addresses. If you whitelist a single address,
// any non-whitelisted addresses are treated as blacklisted.
CZMQ_EXPORT void
 zauth_allow (zauth_t *self, const char *address);
// Deny (blacklist) a single IP address. For all security mechanisms, this
// rejects the connection without any further authentication. Use either a
// whitelist, or a blacklist, not not both. If you define both a whitelist
// and a blacklist, only the whitelist takes effect.
CZMQ_EXPORT void
 zauth_deny (zauth_t *self, const char *address);
// Configure PLAIN authentication for a given domain. PLAIN authentication
// uses a plain-text password file. To cover all domains, use &quot;*&quot;. You can
// modify the password file at any time; it is reloaded automatically.
CZMQ_EXPORT void
 zauth_configure_plain (zauth_t *self, const char *domain, const char *filename);
// Configure CURVE authentication for a given domain. CURVE authentication
// uses a directory that holds all public client certificates, i.e. their
// public keys. The certificates must be in zcert_save () format. To cover
// all domains, use &quot;*&quot;. You can add and remove certificates in that
// directory at any time. To allow all client keys without checking, specify
// CURVE_ALLOW_ANY for the location.
CZMQ_EXPORT void
 zauth_configure_curve (zauth_t *self, const char *domain, const char *location);
// Configure GSSAPI authentication for a given domain. GSSAPI authentication
// uses an underlying mechanism (usually Kerberos) to establish a secure
// context and perform mutual authentication. To cover all domains, use &quot;*&quot;.
CZMQ_EXPORT void
 zauth_configure_gssapi (zauth_t *self, char *domain);
// Enable verbose tracing of commands and activity
CZMQ_EXPORT void
 zauth_set_verbose (zauth_t *self, bool verbose);
// Selftest
CZMQ_EXPORT void
 zauth_v2_test (bool verbose);</pre>
<h2>Description</h2>
<p>A zauth object takes over authentication for all incoming connections in its context. </p>
<p> This class is deprecated in CZMQ v3; it works together with zctx, zsocket, and other deprecated V2 classes. New applications should use the V3 zauth interface, based on zactor, together with the zsock class for sockets.</p>
<h2>Example</h2>
<p><code>From zauth_v2_test method</code>. </p>
<pre><code>//  Create temporary directory for test files
#define TESTDIR &quot;.test_zauth&quot;
zsys_dir_create(TESTDIR);

//  Install the authenticator
zctx_t *ctx = zctx_new();
assert(ctx);
zauth_t *auth = zauth_new(ctx);
assert(auth);
zauth_set_verbose(auth, verbose);

//  A default NULL connection should always success, and not
//  go through our authentication infrastructure at all.
void *server = zsocket_new(ctx, ZMQ_PUSH);
assert(server);
void *client = zsocket_new(ctx, ZMQ_PULL);
assert(client);
bool success = s_can_connect(ctx, &amp;server, &amp;client);
assert(success);

//  When we set a domain on the server, we switch on authentication
//  for NULL sockets, but with no policies, the client connection
//  will be allowed.
zsocket_set_zap_domain(server, &quot;global&quot;);
success = s_can_connect(ctx, &amp;server, &amp;client);
assert(success);

//  Blacklist 127.0.0.1, connection should fail
zsocket_set_zap_domain(server, &quot;global&quot;);
zauth_deny(auth, &quot;127.0.0.1&quot;);
success = s_can_connect(ctx, &amp;server, &amp;client);
assert(!success);

//  Whitelist our address, which overrides the blacklist
zsocket_set_zap_domain(server, &quot;global&quot;);
zauth_allow(auth, &quot;127.0.0.1&quot;);
success = s_can_connect(ctx, &amp;server, &amp;client);
assert(success);

//  Try PLAIN authentication
zsocket_set_plain_server(server, 1);
zsocket_set_plain_username(client, &quot;admin&quot;);
zsocket_set_plain_password(client, &quot;Password&quot;);
success = s_can_connect(ctx, &amp;server, &amp;client);
assert(!success);

FILE *password = fopen(TESTDIR &quot;/password-file&quot;, &quot;w&quot;);
assert(password);
fprintf(password, &quot;admin=Password
&quot;);
fclose(password);
zsocket_set_plain_server(server, 1);
zsocket_set_plain_username(client, &quot;admin&quot;);
zsocket_set_plain_password(client, &quot;Password&quot;);
zauth_configure_plain(auth, &quot;*&quot;, TESTDIR &quot;/password-file&quot;);
success = s_can_connect(ctx, &amp;server, &amp;client);
assert(success);

zsocket_set_plain_server(server, 1);
zsocket_set_plain_username(client, &quot;admin&quot;);
zsocket_set_plain_password(client, &quot;Bogus&quot;);
success = s_can_connect(ctx, &amp;server, &amp;client);
assert(!success);

if (zsys_has_curve()) {
    //  Try CURVE authentication
    //  We'll create two new certificates and save the client public
    //  certificate on disk; in a real case we'd transfer this securely
    //  from the client machine to the server machine.
    zcert_t *server_cert = zcert_new();
    assert(server_cert);
    zcert_t *client_cert = zcert_new();
    assert(client_cert);
    char *server_key = zcert_public_txt(server_cert);

    //  Test without setting-up any authentication
    zcert_apply(server_cert, server);
    zcert_apply(client_cert, client);
    zsocket_set_curve_server(server, 1);
    zsocket_set_curve_serverkey(client, server_key);
    success = s_can_connect(ctx, &amp;server, &amp;client);
    assert(!success);

    //  Test CURVE_ALLOW_ANY
    zcert_apply(server_cert, server);
    zcert_apply(client_cert, client);
    zsocket_set_curve_server(server, 1);
    zsocket_set_curve_serverkey(client, server_key);
    zauth_configure_curve(auth, &quot;*&quot;, CURVE_ALLOW_ANY);
    success = s_can_connect(ctx, &amp;server, &amp;client);
    assert(success);

    //  Test full client authentication using certificates
    zcert_apply(server_cert, server);
    zcert_apply(client_cert, client);
    zsocket_set_curve_server(server, 1);
    zsocket_set_curve_serverkey(client, server_key);
    zcert_save_public(client_cert, TESTDIR &quot;/mycert.txt&quot;);
    zauth_configure_curve(auth, &quot;*&quot;, TESTDIR);
    success = s_can_connect(ctx, &amp;server, &amp;client);
    assert(success);

    zcert_destroy(&amp;server_cert);
    zcert_destroy(&amp;client_cert);
}
//  Remove the authenticator and check a normal connection works
zauth_destroy(&amp;auth);
success = s_can_connect(ctx, &amp;server, &amp;client);
assert(success);

zctx_destroy(&amp;ctx);

//  Delete all test files
zdir_t *dir = zdir_new(TESTDIR, NULL);
assert(dir);
zdir_remove(dir, true);
zdir_destroy(&amp;dir);
</code></pre>
<h2>Authors</h2>
<p>The czmq manual was written by the authors in the AUTHORS file.</p>
<h2>Resources</h2>
<p>Main web site: m[blue]m[] </p>
<p> Report bugs to the email &lt;m[blue]<code>zeromq-dev [at] lists.zeromq.org</code>m[]<font SIZE="-2">[1]</font>&gt;</p>
<h2>Copyright</h2>
<p>Copyright (c) 1991-2012 iMatix Corporation &#8212; <a rel="nofollow" href="http://www.imatix.com">http://www.imatix.com</a> Copyright other contributors as noted in the AUTHORS file. This file is part of CZMQ, the high-level C binding for 0MQ: <a href="http://czmq.zeromq.org">http://czmq.zeromq.org</a> This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at <a href="http://mozilla.org/MPL/2.0/.">http://mozilla.org/MPL/2.0/.</a> LICENSE included with the czmq distribution.</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>zeromq-dev [at] lists.zeromq.org</p>
<dl>
<dd>mailto:zeromq-dev [at] lists.zeromq.org</dl>
