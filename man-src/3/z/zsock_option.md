---
title: "zsock_option(3)"
name: "zsock_option"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zsock_option/"
description: "zsock_option – get/set 0MQ socket options"
---

<p>zsock_option &#8211; get/set 0MQ socket options</p>
<h2>Synopsis</h2>
<pre><code>#if (ZMQ_VERSION_MAJOR == 4)
//  Get socket options
CZMQ_EXPORT int zsock_tos(void *self);
CZMQ_EXPORT char *zsock_zap_domain(void *self);
CZMQ_EXPORT int zsock_mechanism(void *self);
CZMQ_EXPORT int zsock_plain_server(void *self);
CZMQ_EXPORT char *zsock_plain_username(void *self);
CZMQ_EXPORT char *zsock_plain_password(void *self);
CZMQ_EXPORT int zsock_curve_server(void *self);
CZMQ_EXPORT char *zsock_curve_publickey(void *self);
CZMQ_EXPORT char *zsock_curve_secretkey(void *self);
CZMQ_EXPORT char *zsock_curve_serverkey(void *self);
CZMQ_EXPORT int zsock_gssapi_server(void *self);
CZMQ_EXPORT int zsock_gssapi_plaintext(void *self);
CZMQ_EXPORT char *zsock_gssapi_principal(void *self);
CZMQ_EXPORT char *zsock_gssapi_service_principal(void *self);
CZMQ_EXPORT int zsock_ipv6(void *self);
CZMQ_EXPORT int zsock_immediate(void *self);
CZMQ_EXPORT int zsock_ipv4only(void *self);
CZMQ_EXPORT int zsock_type(void *self);
CZMQ_EXPORT int zsock_sndhwm(void *self);
CZMQ_EXPORT int zsock_rcvhwm(void *self);
CZMQ_EXPORT int zsock_affinity(void *self);
CZMQ_EXPORT char *zsock_identity(void *self);
CZMQ_EXPORT int zsock_rate(void *self);
CZMQ_EXPORT int zsock_recovery_ivl(void *self);
CZMQ_EXPORT int zsock_sndbuf(void *self);
CZMQ_EXPORT int zsock_rcvbuf(void *self);
CZMQ_EXPORT int zsock_linger(void *self);
CZMQ_EXPORT int zsock_reconnect_ivl(void *self);
CZMQ_EXPORT int zsock_reconnect_ivl_max(void *self);
CZMQ_EXPORT int zsock_backlog(void *self);
CZMQ_EXPORT int zsock_maxmsgsize(void *self);
CZMQ_EXPORT int zsock_multicast_hops(void *self);
CZMQ_EXPORT int zsock_rcvtimeo(void *self);
CZMQ_EXPORT int zsock_sndtimeo(void *self);
CZMQ_EXPORT int zsock_tcp_keepalive(void *self);
CZMQ_EXPORT int zsock_tcp_keepalive_idle(void *self);
CZMQ_EXPORT int zsock_tcp_keepalive_cnt(void *self);
CZMQ_EXPORT int zsock_tcp_keepalive_intvl(void *self);
CZMQ_EXPORT char *zsock_tcp_accept_filter(void *self);
CZMQ_EXPORT int zsock_rcvmore(void *self);
CZMQ_EXPORT SOCKET zsock_fd(void *self);
CZMQ_EXPORT int zsock_events(void *self);
CZMQ_EXPORT char *zsock_last_endpoint(void *self);

//  Set socket options
CZMQ_EXPORT void zsock_set_tos(void *self, int tos);
CZMQ_EXPORT void zsock_set_router_handover(void *self, int router_handover);
CZMQ_EXPORT void zsock_set_router_mandatory(void *self, int router_mandatory);
CZMQ_EXPORT void zsock_set_probe_router(void *self, int probe_router);
CZMQ_EXPORT void zsock_set_req_relaxed(void *self, int req_relaxed);
CZMQ_EXPORT void zsock_set_req_correlate(void *self, int req_correlate);
CZMQ_EXPORT void zsock_set_conflate(void *self, int conflate);
CZMQ_EXPORT void zsock_set_zap_domain(void *self, const char *zap_domain);
CZMQ_EXPORT void zsock_set_plain_server(void *self, int plain_server);
CZMQ_EXPORT void zsock_set_plain_username(void *self, const char *plain_username);
CZMQ_EXPORT void zsock_set_plain_password(void *self, const char *plain_password);
CZMQ_EXPORT void zsock_set_curve_server(void *self, int curve_server);
CZMQ_EXPORT void zsock_set_curve_publickey(void *self, const char *curve_publickey);
CZMQ_EXPORT void zsock_set_curve_publickey_bin(void *self, const byte *curve_publickey);
CZMQ_EXPORT void zsock_set_curve_secretkey(void *self, const char *curve_secretkey);
CZMQ_EXPORT void zsock_set_curve_secretkey_bin(void *self, const byte *curve_secretkey);
CZMQ_EXPORT void zsock_set_curve_serverkey(void *self, const char *curve_serverkey);
CZMQ_EXPORT void zsock_set_curve_serverkey_bin(void *self, const byte *curve_serverkey);
CZMQ_EXPORT void zsock_set_gssapi_server(void *self, int gssapi_server);
CZMQ_EXPORT void zsock_set_gssapi_plaintext(void *self, int gssapi_plaintext);
CZMQ_EXPORT void zsock_set_gssapi_principal(void *self, const char *gssapi_principal);
CZMQ_EXPORT void zsock_set_gssapi_service_principal(void *self, const char *gssapi_service_principal);
CZMQ_EXPORT void zsock_set_ipv6(void *self, int ipv6);
CZMQ_EXPORT void zsock_set_immediate(void *self, int immediate);
CZMQ_EXPORT void zsock_set_router_raw(void *self, int router_raw);
CZMQ_EXPORT void zsock_set_ipv4only(void *self, int ipv4only);
CZMQ_EXPORT void zsock_set_delay_attach_on_connect(void *self, int delay_attach_on_connect);
CZMQ_EXPORT void zsock_set_sndhwm(void *self, int sndhwm);
CZMQ_EXPORT void zsock_set_rcvhwm(void *self, int rcvhwm);
CZMQ_EXPORT void zsock_set_affinity(void *self, int affinity);
CZMQ_EXPORT void zsock_set_subscribe(void *self, const char *subscribe);
CZMQ_EXPORT void zsock_set_unsubscribe(void *self, const char *unsubscribe);
CZMQ_EXPORT void zsock_set_identity(void *self, const char *identity);
CZMQ_EXPORT void zsock_set_rate(void *self, int rate);
CZMQ_EXPORT void zsock_set_recovery_ivl(void *self, int recovery_ivl);
CZMQ_EXPORT void zsock_set_sndbuf(void *self, int sndbuf);
CZMQ_EXPORT void zsock_set_rcvbuf(void *self, int rcvbuf);
CZMQ_EXPORT void zsock_set_linger(void *self, int linger);
CZMQ_EXPORT void zsock_set_reconnect_ivl(void *self, int reconnect_ivl);
CZMQ_EXPORT void zsock_set_reconnect_ivl_max(void *self, int reconnect_ivl_max);
CZMQ_EXPORT void zsock_set_backlog(void *self, int backlog);
CZMQ_EXPORT void zsock_set_maxmsgsize(void *self, int maxmsgsize);
CZMQ_EXPORT void zsock_set_multicast_hops(void *self, int multicast_hops);
CZMQ_EXPORT void zsock_set_rcvtimeo(void *self, int rcvtimeo);
CZMQ_EXPORT void zsock_set_sndtimeo(void *self, int sndtimeo);
CZMQ_EXPORT void zsock_set_xpub_verbose(void *self, int xpub_verbose);
CZMQ_EXPORT void zsock_set_tcp_keepalive(void *self, int tcp_keepalive);
CZMQ_EXPORT void zsock_set_tcp_keepalive_idle(void *self, int tcp_keepalive_idle);
CZMQ_EXPORT void zsock_set_tcp_keepalive_cnt(void *self, int tcp_keepalive_cnt);
CZMQ_EXPORT void zsock_set_tcp_keepalive_intvl(void *self, int tcp_keepalive_intvl);
CZMQ_EXPORT void zsock_set_tcp_accept_filter(void *self, const char *tcp_accept_filter);
#endif

#if (ZMQ_VERSION_MAJOR == 3)
//  Get socket options
CZMQ_EXPORT int zsock_ipv4only(void *self);
CZMQ_EXPORT int zsock_type(void *self);
CZMQ_EXPORT int zsock_sndhwm(void *self);
CZMQ_EXPORT int zsock_rcvhwm(void *self);
CZMQ_EXPORT int zsock_affinity(void *self);
CZMQ_EXPORT char *zsock_identity(void *self);
CZMQ_EXPORT int zsock_rate(void *self);
CZMQ_EXPORT int zsock_recovery_ivl(void *self);
CZMQ_EXPORT int zsock_sndbuf(void *self);
CZMQ_EXPORT int zsock_rcvbuf(void *self);
CZMQ_EXPORT int zsock_linger(void *self);
CZMQ_EXPORT int zsock_reconnect_ivl(void *self);
CZMQ_EXPORT int zsock_reconnect_ivl_max(void *self);
CZMQ_EXPORT int zsock_backlog(void *self);
CZMQ_EXPORT int zsock_maxmsgsize(void *self);
CZMQ_EXPORT int zsock_multicast_hops(void *self);
CZMQ_EXPORT int zsock_rcvtimeo(void *self);
CZMQ_EXPORT int zsock_sndtimeo(void *self);
CZMQ_EXPORT int zsock_tcp_keepalive(void *self);
CZMQ_EXPORT int zsock_tcp_keepalive_idle(void *self);
CZMQ_EXPORT int zsock_tcp_keepalive_cnt(void *self);
CZMQ_EXPORT int zsock_tcp_keepalive_intvl(void *self);
CZMQ_EXPORT char *zsock_tcp_accept_filter(void *self);
CZMQ_EXPORT int zsock_rcvmore(void *self);
CZMQ_EXPORT SOCKET zsock_fd(void *self);
CZMQ_EXPORT int zsock_events(void *self);
CZMQ_EXPORT char *zsock_last_endpoint(void *self);

//  Set socket options
CZMQ_EXPORT void zsock_set_router_raw(void *self, int router_raw);
CZMQ_EXPORT void zsock_set_ipv4only(void *self, int ipv4only);
CZMQ_EXPORT void zsock_set_delay_attach_on_connect(void *self, int delay_attach_on_connect);
CZMQ_EXPORT void zsock_set_sndhwm(void *self, int sndhwm);
CZMQ_EXPORT void zsock_set_rcvhwm(void *self, int rcvhwm);
CZMQ_EXPORT void zsock_set_affinity(void *self, int affinity);
CZMQ_EXPORT void zsock_set_subscribe(void *self, const char *subscribe);
CZMQ_EXPORT void zsock_set_unsubscribe(void *self, const char *unsubscribe);
CZMQ_EXPORT void zsock_set_identity(void *self, const char *identity);
CZMQ_EXPORT void zsock_set_rate(void *self, int rate);
CZMQ_EXPORT void zsock_set_recovery_ivl(void *self, int recovery_ivl);
CZMQ_EXPORT void zsock_set_sndbuf(void *self, int sndbuf);
CZMQ_EXPORT void zsock_set_rcvbuf(void *self, int rcvbuf);
CZMQ_EXPORT void zsock_set_linger(void *self, int linger);
CZMQ_EXPORT void zsock_set_reconnect_ivl(void *self, int reconnect_ivl);
CZMQ_EXPORT void zsock_set_reconnect_ivl_max(void *self, int reconnect_ivl_max);
CZMQ_EXPORT void zsock_set_backlog(void *self, int backlog);
CZMQ_EXPORT void zsock_set_maxmsgsize(void *self, int maxmsgsize);
CZMQ_EXPORT void zsock_set_multicast_hops(void *self, int multicast_hops);
CZMQ_EXPORT void zsock_set_rcvtimeo(void *self, int rcvtimeo);
CZMQ_EXPORT void zsock_set_sndtimeo(void *self, int sndtimeo);
CZMQ_EXPORT void zsock_set_xpub_verbose(void *self, int xpub_verbose);
CZMQ_EXPORT void zsock_set_tcp_keepalive(void *self, int tcp_keepalive);
CZMQ_EXPORT void zsock_set_tcp_keepalive_idle(void *self, int tcp_keepalive_idle);
CZMQ_EXPORT void zsock_set_tcp_keepalive_cnt(void *self, int tcp_keepalive_cnt);
CZMQ_EXPORT void zsock_set_tcp_keepalive_intvl(void *self, int tcp_keepalive_intvl);
CZMQ_EXPORT void zsock_set_tcp_accept_filter(void *self, const char *tcp_accept_filter);
#endif

#if (ZMQ_VERSION_MAJOR == 2)
//  Get socket options
CZMQ_EXPORT int zsock_hwm(void *self);
CZMQ_EXPORT int zsock_swap(void *self);
CZMQ_EXPORT int zsock_affinity(void *self);
CZMQ_EXPORT char *zsock_identity(void *self);
CZMQ_EXPORT int zsock_rate(void *self);
CZMQ_EXPORT int zsock_recovery_ivl(void *self);
CZMQ_EXPORT int zsock_recovery_ivl_msec(void *self);
CZMQ_EXPORT int zsock_mcast_loop(void *self);
#if (ZMQ_VERSION_MINOR == 2)
CZMQ_EXPORT int zsock_rcvtimeo(void *self);
#endif
#if (ZMQ_VERSION_MINOR == 2)
CZMQ_EXPORT int zsock_sndtimeo(void *self);
#endif
CZMQ_EXPORT int zsock_sndbuf(void *self);
CZMQ_EXPORT int zsock_rcvbuf(void *self);
CZMQ_EXPORT int zsock_linger(void *self);
CZMQ_EXPORT int zsock_reconnect_ivl(void *self);
CZMQ_EXPORT int zsock_reconnect_ivl_max(void *self);
CZMQ_EXPORT int zsock_backlog(void *self);
CZMQ_EXPORT int zsock_type(void *self);
CZMQ_EXPORT int zsock_rcvmore(void *self);
CZMQ_EXPORT SOCKET zsock_fd(void *self);
CZMQ_EXPORT int zsock_events(void *self);

//  Set socket options
CZMQ_EXPORT void zsock_set_hwm(void *self, int hwm);
CZMQ_EXPORT void zsock_set_swap(void *self, int swap);
CZMQ_EXPORT void zsock_set_affinity(void *self, int affinity);
CZMQ_EXPORT void zsock_set_identity(void *self, const char *identity);
CZMQ_EXPORT void zsock_set_rate(void *self, int rate);
CZMQ_EXPORT void zsock_set_recovery_ivl(void *self, int recovery_ivl);
CZMQ_EXPORT void zsock_set_recovery_ivl_msec(void *self, int recovery_ivl_msec);
CZMQ_EXPORT void zsock_set_mcast_loop(void *self, int mcast_loop);
#if (ZMQ_VERSION_MINOR == 2)
CZMQ_EXPORT void zsock_set_rcvtimeo(void *self, int rcvtimeo);
#endif
#if (ZMQ_VERSION_MINOR == 2)
CZMQ_EXPORT void zsock_set_sndtimeo(void *self, int sndtimeo);
#endif
CZMQ_EXPORT void zsock_set_sndbuf(void *self, int sndbuf);
CZMQ_EXPORT void zsock_set_rcvbuf(void *self, int rcvbuf);
CZMQ_EXPORT void zsock_set_linger(void *self, int linger);
CZMQ_EXPORT void zsock_set_reconnect_ivl(void *self, int reconnect_ivl);
CZMQ_EXPORT void zsock_set_reconnect_ivl_max(void *self, int reconnect_ivl_max);
CZMQ_EXPORT void zsock_set_backlog(void *self, int backlog);
CZMQ_EXPORT void zsock_set_subscribe(void *self, const char *subscribe);
CZMQ_EXPORT void zsock_set_unsubscribe(void *self, const char *unsubscribe);
#endif

//  Self test of this class
CZMQ_EXPORT void zsock_option_test(bool verbose);</code></pre>
<h2>Description</h2>
<p>The zsock_option class provides access to the 0MQ getsockopt/setsockopt API. All methods in this class take a void * &quot;polymorphic&quot; reference, which can be either a zsock_t or a zactor_r reference, or a libzmq void *. </p>
<p> This class is generated, using the GSL code generator. See the sockopts XML file, which provides the metadata, and the sock_option.gsl template, which does the work.</p>
<h2>Example</h2>
<p><code>From zsock_option_test method</code>. </p>
<pre><code>zsock_t *self;
#if (ZMQ_VERSION_MAJOR == 4)
#if defined(ZMQ_TOS)
self = zsock_new(ZMQ_DEALER);
assert(self);
zsock_set_tos(self, 1);
assert(zsock_tos(self) == 1);
zsock_tos(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_ROUTER_HANDOVER)
self = zsock_new(ZMQ_ROUTER);
assert(self);
zsock_set_router_handover(self, 1);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_ROUTER_MANDATORY)
self = zsock_new(ZMQ_ROUTER);
assert(self);
zsock_set_router_mandatory(self, 1);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_PROBE_ROUTER)
self = zsock_new(ZMQ_DEALER);
assert(self);
zsock_set_probe_router(self, 1);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_REQ_RELAXED)
self = zsock_new(ZMQ_REQ);
assert(self);
zsock_set_req_relaxed(self, 1);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_REQ_CORRELATE)
self = zsock_new(ZMQ_REQ);
assert(self);
zsock_set_req_correlate(self, 1);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_CONFLATE)
self = zsock_new(ZMQ_PUSH);
assert(self);
zsock_set_conflate(self, 1);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_ZAP_DOMAIN)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_zap_domain(self, &quot;test&quot;);
char *zap_domain = zsock_zap_domain(self);
assert(zap_domain);
free(zap_domain);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_MECHANISM)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_mechanism(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_PLAIN_SERVER)
self = zsock_new(ZMQ_PUB);
assert(self);
zsock_set_plain_server(self, 1);
assert(zsock_plain_server(self) == 1);
zsock_plain_server(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_PLAIN_USERNAME)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_plain_username(self, &quot;test&quot;);
char *plain_username = zsock_plain_username(self);
assert(plain_username);
free(plain_username);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_PLAIN_PASSWORD)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_plain_password(self, &quot;test&quot;);
char *plain_password = zsock_plain_password(self);
assert(plain_password);
free(plain_password);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_IPV6)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_ipv6(self, 1);
assert(zsock_ipv6(self) == 1);
zsock_ipv6(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_IMMEDIATE)
self = zsock_new(ZMQ_DEALER);
assert(self);
zsock_set_immediate(self, 1);
assert(zsock_immediate(self) == 1);
zsock_immediate(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_ROUTER_RAW)
self = zsock_new(ZMQ_ROUTER);
assert(self);
zsock_set_router_raw(self, 1);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_IPV4ONLY)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_ipv4only(self, 1);
assert(zsock_ipv4only(self) == 1);
zsock_ipv4only(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_DELAY_ATTACH_ON_CONNECT)
self = zsock_new(ZMQ_PUB);
assert(self);
zsock_set_delay_attach_on_connect(self, 1);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_TYPE)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_type(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_SNDHWM)
self = zsock_new(ZMQ_PUB);
assert(self);
zsock_set_sndhwm(self, 1);
assert(zsock_sndhwm(self) == 1);
zsock_sndhwm(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_RCVHWM)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_rcvhwm(self, 1);
assert(zsock_rcvhwm(self) == 1);
zsock_rcvhwm(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_AFFINITY)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_affinity(self, 1);
assert(zsock_affinity(self) == 1);
zsock_affinity(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_SUBSCRIBE)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_subscribe(self, &quot;test&quot;);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_UNSUBSCRIBE)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_unsubscribe(self, &quot;test&quot;);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_IDENTITY)
self = zsock_new(ZMQ_DEALER);
assert(self);
zsock_set_identity(self, &quot;test&quot;);
char *identity = zsock_identity(self);
assert(identity);
free(identity);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_RATE)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_rate(self, 1);
assert(zsock_rate(self) == 1);
zsock_rate(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_RECOVERY_IVL)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_recovery_ivl(self, 1);
assert(zsock_recovery_ivl(self) == 1);
zsock_recovery_ivl(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_SNDBUF)
self = zsock_new(ZMQ_PUB);
assert(self);
zsock_set_sndbuf(self, 1);
assert(zsock_sndbuf(self) == 1);
zsock_sndbuf(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_RCVBUF)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_rcvbuf(self, 1);
assert(zsock_rcvbuf(self) == 1);
zsock_rcvbuf(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_LINGER)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_linger(self, 1);
assert(zsock_linger(self) == 1);
zsock_linger(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_RECONNECT_IVL)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_reconnect_ivl(self, 1);
assert(zsock_reconnect_ivl(self) == 1);
zsock_reconnect_ivl(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_RECONNECT_IVL_MAX)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_reconnect_ivl_max(self, 1);
assert(zsock_reconnect_ivl_max(self) == 1);
zsock_reconnect_ivl_max(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_BACKLOG)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_backlog(self, 1);
assert(zsock_backlog(self) == 1);
zsock_backlog(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_MAXMSGSIZE)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_maxmsgsize(self, 1);
assert(zsock_maxmsgsize(self) == 1);
zsock_maxmsgsize(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_MULTICAST_HOPS)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_multicast_hops(self, 1);
assert(zsock_multicast_hops(self) == 1);
zsock_multicast_hops(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_RCVTIMEO)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_rcvtimeo(self, 1);
assert(zsock_rcvtimeo(self) == 1);
zsock_rcvtimeo(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_SNDTIMEO)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_sndtimeo(self, 1);
assert(zsock_sndtimeo(self) == 1);
zsock_sndtimeo(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_XPUB_VERBOSE)
self = zsock_new(ZMQ_XPUB);
assert(self);
zsock_set_xpub_verbose(self, 1);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_TCP_KEEPALIVE)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_tcp_keepalive(self, 1);
assert(zsock_tcp_keepalive(self) == 1);
zsock_tcp_keepalive(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_TCP_KEEPALIVE_IDLE)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_tcp_keepalive_idle(self, 1);
assert(zsock_tcp_keepalive_idle(self) == 1);
zsock_tcp_keepalive_idle(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_TCP_KEEPALIVE_CNT)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_tcp_keepalive_cnt(self, 1);
assert(zsock_tcp_keepalive_cnt(self) == 1);
zsock_tcp_keepalive_cnt(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_TCP_KEEPALIVE_INTVL)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_tcp_keepalive_intvl(self, 1);
assert(zsock_tcp_keepalive_intvl(self) == 1);
zsock_tcp_keepalive_intvl(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_TCP_ACCEPT_FILTER)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_tcp_accept_filter(self, &quot;127.0.0.1&quot;);
char *tcp_accept_filter = zsock_tcp_accept_filter(self);
assert(tcp_accept_filter);
free(tcp_accept_filter);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_RCVMORE)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_rcvmore(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_FD)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_fd(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_EVENTS)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_events(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_LAST_ENDPOINT)
self = zsock_new(ZMQ_SUB);
assert(self);
char *last_endpoint = zsock_last_endpoint(self);
assert(last_endpoint);
free(last_endpoint);
zsock_destroy(&amp;self);
#endif
#endif

#if (ZMQ_VERSION_MAJOR == 3)
#if defined(ZMQ_ROUTER_RAW)
self = zsock_new(ZMQ_ROUTER);
assert(self);
zsock_set_router_raw(self, 1);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_IPV4ONLY)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_ipv4only(self, 1);
assert(zsock_ipv4only(self) == 1);
zsock_ipv4only(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_DELAY_ATTACH_ON_CONNECT)
self = zsock_new(ZMQ_PUB);
assert(self);
zsock_set_delay_attach_on_connect(self, 1);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_TYPE)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_type(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_SNDHWM)
self = zsock_new(ZMQ_PUB);
assert(self);
zsock_set_sndhwm(self, 1);
assert(zsock_sndhwm(self) == 1);
zsock_sndhwm(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_RCVHWM)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_rcvhwm(self, 1);
assert(zsock_rcvhwm(self) == 1);
zsock_rcvhwm(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_AFFINITY)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_affinity(self, 1);
assert(zsock_affinity(self) == 1);
zsock_affinity(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_SUBSCRIBE)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_subscribe(self, &quot;test&quot;);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_UNSUBSCRIBE)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_unsubscribe(self, &quot;test&quot;);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_IDENTITY)
self = zsock_new(ZMQ_DEALER);
assert(self);
zsock_set_identity(self, &quot;test&quot;);
char *identity = zsock_identity(self);
assert(identity);
free(identity);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_RATE)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_rate(self, 1);
assert(zsock_rate(self) == 1);
zsock_rate(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_RECOVERY_IVL)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_recovery_ivl(self, 1);
assert(zsock_recovery_ivl(self) == 1);
zsock_recovery_ivl(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_SNDBUF)
self = zsock_new(ZMQ_PUB);
assert(self);
zsock_set_sndbuf(self, 1);
assert(zsock_sndbuf(self) == 1);
zsock_sndbuf(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_RCVBUF)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_rcvbuf(self, 1);
assert(zsock_rcvbuf(self) == 1);
zsock_rcvbuf(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_LINGER)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_linger(self, 1);
assert(zsock_linger(self) == 1);
zsock_linger(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_RECONNECT_IVL)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_reconnect_ivl(self, 1);
assert(zsock_reconnect_ivl(self) == 1);
zsock_reconnect_ivl(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_RECONNECT_IVL_MAX)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_reconnect_ivl_max(self, 1);
assert(zsock_reconnect_ivl_max(self) == 1);
zsock_reconnect_ivl_max(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_BACKLOG)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_backlog(self, 1);
assert(zsock_backlog(self) == 1);
zsock_backlog(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_MAXMSGSIZE)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_maxmsgsize(self, 1);
assert(zsock_maxmsgsize(self) == 1);
zsock_maxmsgsize(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_MULTICAST_HOPS)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_multicast_hops(self, 1);
assert(zsock_multicast_hops(self) == 1);
zsock_multicast_hops(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_RCVTIMEO)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_rcvtimeo(self, 1);
assert(zsock_rcvtimeo(self) == 1);
zsock_rcvtimeo(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_SNDTIMEO)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_sndtimeo(self, 1);
assert(zsock_sndtimeo(self) == 1);
zsock_sndtimeo(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_XPUB_VERBOSE)
self = zsock_new(ZMQ_XPUB);
assert(self);
zsock_set_xpub_verbose(self, 1);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_TCP_KEEPALIVE)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_tcp_keepalive(self, 1);
assert(zsock_tcp_keepalive(self) == 1);
zsock_tcp_keepalive(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_TCP_KEEPALIVE_IDLE)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_tcp_keepalive_idle(self, 1);
assert(zsock_tcp_keepalive_idle(self) == 1);
zsock_tcp_keepalive_idle(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_TCP_KEEPALIVE_CNT)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_tcp_keepalive_cnt(self, 1);
assert(zsock_tcp_keepalive_cnt(self) == 1);
zsock_tcp_keepalive_cnt(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_TCP_KEEPALIVE_INTVL)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_tcp_keepalive_intvl(self, 1);
assert(zsock_tcp_keepalive_intvl(self) == 1);
zsock_tcp_keepalive_intvl(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_TCP_ACCEPT_FILTER)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_tcp_accept_filter(self, &quot;127.0.0.1&quot;);
char *tcp_accept_filter = zsock_tcp_accept_filter(self);
assert(tcp_accept_filter);
free(tcp_accept_filter);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_RCVMORE)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_rcvmore(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_FD)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_fd(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_EVENTS)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_events(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_LAST_ENDPOINT)
self = zsock_new(ZMQ_SUB);
assert(self);
char *last_endpoint = zsock_last_endpoint(self);
assert(last_endpoint);
free(last_endpoint);
zsock_destroy(&amp;self);
#endif
#endif

#if (ZMQ_VERSION_MAJOR == 2)
#if defined(ZMQ_HWM)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_hwm(self, 1);
assert(zsock_hwm(self) == 1);
zsock_hwm(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_SWAP)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_swap(self, 1);
assert(zsock_swap(self) == 1);
zsock_swap(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_AFFINITY)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_affinity(self, 1);
assert(zsock_affinity(self) == 1);
zsock_affinity(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_IDENTITY)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_identity(self, &quot;test&quot;);
char *identity = zsock_identity(self);
assert(identity);
free(identity);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_RATE)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_rate(self, 1);
assert(zsock_rate(self) == 1);
zsock_rate(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_RECOVERY_IVL)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_recovery_ivl(self, 1);
assert(zsock_recovery_ivl(self) == 1);
zsock_recovery_ivl(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_RECOVERY_IVL_MSEC)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_recovery_ivl_msec(self, 1);
assert(zsock_recovery_ivl_msec(self) == 1);
zsock_recovery_ivl_msec(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_MCAST_LOOP)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_mcast_loop(self, 1);
assert(zsock_mcast_loop(self) == 1);
zsock_mcast_loop(self);
zsock_destroy(&amp;self);
#endif
#if (ZMQ_VERSION_MINOR == 2)
#if defined(ZMQ_RCVTIMEO)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_rcvtimeo(self, 1);
assert(zsock_rcvtimeo(self) == 1);
zsock_rcvtimeo(self);
zsock_destroy(&amp;self);
#endif
#endif
#if (ZMQ_VERSION_MINOR == 2)
#if defined(ZMQ_SNDTIMEO)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_sndtimeo(self, 1);
assert(zsock_sndtimeo(self) == 1);
zsock_sndtimeo(self);
zsock_destroy(&amp;self);
#endif
#endif
#if defined(ZMQ_SNDBUF)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_sndbuf(self, 1);
assert(zsock_sndbuf(self) == 1);
zsock_sndbuf(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_RCVBUF)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_rcvbuf(self, 1);
assert(zsock_rcvbuf(self) == 1);
zsock_rcvbuf(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_LINGER)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_linger(self, 1);
assert(zsock_linger(self) == 1);
zsock_linger(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_RECONNECT_IVL)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_reconnect_ivl(self, 1);
assert(zsock_reconnect_ivl(self) == 1);
zsock_reconnect_ivl(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_RECONNECT_IVL_MAX)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_reconnect_ivl_max(self, 1);
assert(zsock_reconnect_ivl_max(self) == 1);
zsock_reconnect_ivl_max(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_BACKLOG)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_backlog(self, 1);
assert(zsock_backlog(self) == 1);
zsock_backlog(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_SUBSCRIBE)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_subscribe(self, &quot;test&quot;);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_UNSUBSCRIBE)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_set_unsubscribe(self, &quot;test&quot;);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_TYPE)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_type(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_RCVMORE)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_rcvmore(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_FD)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_fd(self);
zsock_destroy(&amp;self);
#endif
#if defined(ZMQ_EVENTS)
self = zsock_new(ZMQ_SUB);
assert(self);
zsock_events(self);
zsock_destroy(&amp;self);
#endif
#endif
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
