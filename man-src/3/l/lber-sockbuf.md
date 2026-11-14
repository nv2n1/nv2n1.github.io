---
title: "lber-sockbuf(3)"
name: "lber-sockbuf"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lber-sockbuf/"
description: "ber_sockbuf_alloc, ber_sockbuf_free, ber_sockbuf_ctrl, ber_sockbuf_add_io, ber_sockbuf_remove_io, Sockbuf_IO – OpenLDAP LBER I/O infrastructure"
---

<h2 class="name">NAME</h2>
<p> ber_sockbuf_alloc, ber_sockbuf_free, ber_sockbuf_ctrl, ber_sockbuf_add_io, ber_sockbuf_remove_io, Sockbuf_IO &#8211; OpenLDAP LBER I/O infrastructure </p>
<h2>LIBRARY</h2>
<p> OpenLDAP LBER (liblber, -llber)</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;lber.h&gt;</code> </p>
<p> <code>Sockbuf *ber_sockbuf_alloc( void );</code> </p>
<p> <code>void ber_sockbuf_free(Sockbuf *</code><i>sb</i><code>);</code> </p>
<p> <code>int ber_sockbuf_ctrl(Sockbuf *</code><i>sb</i><code>, int </code><i>opt</i><code>, void *</code><i>arg</i><code>);</code> </p>
<p> <code>int ber_sockbuf_add_io(Sockbuf *</code><i>sb</i><code>, Sockbuf_IO *</code><i>sbio</i><code>, int </code><i>layer</i><code>, void *</code><i>arg</i><code>);</code> </p>
<p> <code>int ber_sockbuf_remove_io(Sockbuf *</code><i>sb</i><code>, Sockbuf_IO *</code><i>sbio</i><code>, int </code><i>layer</i><code>);</code> </p>
<pre><code>
typedef struct sockbuf_io_desc {
    int sbiod_level;
    Sockbuf *sbiod_sb;
    Sockbuf_IO *sbiod_io;
    void *sbiod_pvt;
    struct sockbuf_io_desc *sbiod_next;
} Sockbuf_IO_Desc;
typedef struct sockbuf_io {
    int (*sbi_setup)(Sockbuf_IO_Desc *sbiod, void *arg);
    int (*sbi_remove)(Sockbuf_IO_Desc *sbiod);
    int (*sbi_ctrl)(Sockbuf_IO_Desc *sbiod, int opt, void *arg);
    ber_slen_t (*sbi_read)(Sockbuf_IO_Desc *sbiod, void *buf, ber_len_t len);
    ber_slen_t (*sbi_write)(Sockbuf_IO_Desc *sbiod, void *buf, ber_len_t len);
    int (*sbi_close)(Sockbuf_IO_Desc *sbiod);
} Sockbuf_IO;
</code></pre>
<h2>DESCRIPTION</h2>
<p> These routines are used to manage the low level I/O operations performed by the Lightweight BER library. They are called implicitly by the other libraries and usually do not need to be called directly from applications. The I/O framework is modularized and new transport layers can be supported by appropriately defining a <code>Sockbuf_IO</code> structure and installing it onto an existing <code>Sockbuf</code>. <code>Sockbuf</code> structures are allocated and freed by <code>ber_sockbuf_alloc</code>() and <code>ber_sockbuf_free</code>(), respectively. The <code>ber_sockbuf_ctrl</code>() function is used to get and set options related to a <code>Sockbuf</code> or to a specific I/O layer of the <code>Sockbuf</code>. The <code>ber_sockbuf_add_io</code>() and <code>ber_sockbuf_remove_io</code>() functions are used to add and remove specific I/O layers on a <code>Sockbuf</code>. </p>
<p> Options for <code>ber_sockbuf_ctrl</code>() include:</p>
<dl>
<dt><code>LBER_SB_OPT_HAS_IO</code></p>
<dd> Takes a <code>Sockbuf_IO *</code> argument and returns 1 if the given handler is installed on the <code>Sockbuf</code>, otherwise returns 0.</p>
<dt><code>LBER_SB_OPT_GET_FD</code></p>
<dd> Retrieves the file descriptor associated to the <code>Sockbuf</code>; <code>arg</code> must be a <code>ber_socket_t *</code>. The return value will be 1 if a valid descriptor was present, -1 otherwise.</p>
<dt><code>LBER_SB_OPT_SET_FD</code></p>
<dd> Sets the file descriptor of the <code>Sockbuf</code> to the descriptor pointed to by <code>arg</code>; <code>arg</code> must be a <code>ber_socket_t *</code>. The return value will always be 1.</p>
<dt><code>LBER_SB_OPT_SET_NONBLOCK</code></p>
<dd> Toggles the non-blocking state of the file descriptor associated to the <code>Sockbuf</code>. <code>arg</code> should be NULL to disable and non-NULL to enable the non-blocking state. The return value will be 1 for success, -1 otherwise.</p>
<dt><code>LBER_SB_OPT_DRAIN</code></p>
<dd> Flush (read and discard) all available input on the <code>Sockbuf</code>. The return value will be 1.</p>
<dt><code>LBER_SB_OPT_NEEDS_READ</code></p>
<dd> Returns non-zero if input is waiting to be read.</p>
<dt><code>LBER_SB_OPT_NEEDS_WRITE</code></p>
<dd> Returns non-zero if the <code>Sockbuf</code> is ready to be written.</p>
<dt><code>LBER_SB_OPT_GET_MAX_INCOMING</code></p>
<dd> Returns the maximum allowed size of an incoming message; <code>arg</code> must be a <code>ber_len_t *</code>. The return value will be 1.</p>
<dt><code>LBER_SB_OPT_SET_MAX_INCOMING</code></p>
<dd> Sets the maximum allowed size of an incoming message; <code>arg</code> must be a <code>ber_len_t *</code>. The return value will be 1. </p>
</dl>
<p> Options not in this list will be passed down to each <code>Sockbuf_IO</code> handler in turn until one of them processes it. If the option is not handled <code>ber_sockbuf_ctrl</code>() will return 0. </p>
<p> Multiple <code>Sockbuf_IO</code> handlers can be stacked in multiple layers to provide various functionality. Currently defined layers include</p>
<dl>
<dt><code>LBER_SBIOD_LEVEL_PROVIDER</code></p>
<dd> the lowest layer, talking directly to a network</p>
<dt><code>LBER_SBIOD_LEVEL_TRANSPORT</code></p>
<dd> an intermediate layer</p>
<dt><code>LBER_SBIOD_LEVEL_APPLICATION</code></p>
<dd> a higher layer</dl>
<p> Currently defined <code>Sockbuf_IO</code> handlers in liblber include</p>
<dl>
<dt><code>ber_sockbuf_io_tcp</code></p>
<dd> The default stream-oriented provider</p>
<dt><code>ber_sockbuf_io_fd</code></p>
<dd> A stream-oriented provider for local IPC sockets</p>
<dt><code>ber_sockbuf_io_dgram</code></p>
<dd> A datagram-oriented provider. This handler is only present if the liblber library was built with LDAP_CONNECTIONLESS defined.</p>
<dt><code>ber_sockbuf_io_readahead</code></p>
<dd> A buffering layer, usually used with a datagram provider to hide the datagram semantics from upper layers.</p>
<dt><code>ber_sockbuf_io_debug</code></p>
<dd> A generic handler that outputs hex dumps of all traffic. This handler may be inserted multiple times at arbitrary layers to show the flow of data between other handlers.</dl>
<p> Additional handlers may be present in libldap if support for them was enabled:</p>
<dl>
<dt><code>ldap_pvt_sockbuf_io_sasl</code></p>
<dd> An application layer handler for SASL encoding/decoding.</p>
<dt><code>sb_tls_sbio</code></p>
<dd> A transport layer handler for SSL/TLS encoding/decoding. Note that this handler is private to the library and is not exposed in the API.</dl>
<p> The provided handlers are all instantiated implicitly by libldap, and applications generally will not need to directly manipulate them. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-lber-decode/">lber-decode</a></code>(3), <code><a href="/docs/linux/man/3-lber-encode/">lber-encode</a></code>(3), <code><a href="/docs/linux/man/3-lber-types/">lber-types</a></code>(3), <code><a href="/docs/linux/man/3-ldap_get_option/">ldap_get_option</a></code>(3) </p>
<h2>ACKNOWLEDGEMENTS</h2>
<p> <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release. </p>
<h2>Index</h2>
