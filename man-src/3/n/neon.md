---
title: "neon(3)"
name: "neon"
section: "3"
letter: "n"
url: "/docs/linux/man/3-neon/"
description: "neon – HTTP and WebDAV client library"
---

<p>neon &#8211; HTTP and WebDAV client library</p>
<h2>Description</h2>
<p>neon is an HTTP and WebDAV client library. The major abstractions exposed are the HTTP <i>session</i>, created by ne_session_create; and the HTTP <i>request</i>, created by ne_request_create. HTTP authentication is handled transparently for server and proxy servers, see ne_set_server_auth; complete SSL/TLS support is also included, see ne_ssl_set_verify.</p>
<h2>Conventions</h2>
<p>Some conventions are used throughout the neon API, to provide a consistent and simple interface; these are documented below.</p>
<h3>Thread-safeness and global initialization</h3>
<p>neon itself is implemented to be thread-safe (avoiding any use of global state), but relies on the operating system providing a thread-safe resolver interface. Modern operating systems offer the thread-safe <code>getaddrinfo</code> interface, which neon supports; some others implement <code>gethostbyname</code> using thread-local storage. </p>
<p> To allow thread-safe use of SSL in the OpenSSL and GnuTLS libraries neon must be configured using the &#8211;enable-threadsafe-ssl; if this is done, locking callbacks will be registered by ne_sock_init; note that care must be exercised if neon is used in conjunction with another library which uses OpenSSL or GnuTLS. </p>
<p> Some platforms and libraries used by neon require global initialization before use; notably: </p>
<dl>
<dd>&bull; The SIGPIPE signal disposition must be set to <i>ignored</i> or otherwise handled to avoid process termination when writing to a socket which has been shutdown by the peer.</dl>
<dl>
<dd>&bull; OpenSSL and GnuTLS require global initialization to load shared lookup tables.</dl>
<dl>
<dd>&bull; The Win32 socket library requires initialization before use.</dl>
<p> The ne_sock_init function should be called before any other use of neon to perform any necessary initialization needed for the particular platform. Applications wishing to perform all the necessary process-global initialization steps themselves may omit to call ne_sock_init (and ne_sock_exit); neon neither checks whether these functions are called nor calls them itself. </p>
<p> For some applications and configurations it may be necessary to call ne_i18n_init to initialize the support for internationalization in neon.</p>
<h3>Asynchronous signal safety</h3>
<p>No function in neon is defined to be &#8220;async-signal safe&#8221; &#8211; that is, no function is safe to call from a signal handler. Any call into the neon library from a signal handler will have undefined behaviour &#8211; in other words, it may crash the process.</p>
<h3>Functions using global state</h3>
<p>Any function in neon may modify the errno global variable as a side-effect. Except where explicitly documented, the value of errno is unspecified after any neon function call. </p>
<p> Other than in the use of errno, the only functions which use or modify process-global state in neon are as follows: </p>
<dl>
<dd>&bull; ne_sock_init, ne_i18n_init, and ne_sock_exit, as described above</dl>
<dl>
<dd>&bull; <code>ne_debug_init</code> and <code>ne_debug</code>, if enabled at compile time; for debugging output</dl>
<dl>
<dd>&bull; ne_oom_callback for installing a process-global callback to be invoked on <code>malloc</code> failure</dl>
<h3>Namespaces</h3>
<p>To avoid possible collisions between names used for symbols and preprocessor macros by an application and the libraries it uses, it is good practice for each library to reserve a particular <i>namespace prefix</i>. An application which ensures it uses no names with these prefixes is then guaranteed to avoid such collisions. </p>
<p> The neon library reserves the use of the namespace prefixes ne_ and NE_. The libraries used by neon may also reserve certain namespaces; collisions between these libraries and a neon-based application will not be detected at compile time, since the underlying library interfaces are not exposed through the neon header files. Such collisions can only be detected at link time, when the linker attempts to resolve symbols. The following list documents some of the namespaces claimed by libraries used by neon; this list may be incomplete. </p>
<p> SSL, ssl, TLS, tls, ERR_, BIO_, d2i_, i2d_, ASN1_</p>
<dl>
<dd>Some of the many prefixes used by the OpenSSL library; little attempt has been made to keep exported symbols within any particular prefixes for this library.</dl>
<p> gnutls_, gcry_, gpg_</p>
<dl>
<dd>Namespaces used by the GnuTLS library (and dependencies thereof)</dl>
<p> XML_, Xml[A-Z]</p>
<dl>
<dd>Namespaces used by the expat library.</dl>
<p> xml[A-Z], html[A-Z], docb[A-Z]</p>
<dl>
<dd>Namespaces used by the libxml2 library; a relatively small number of symbols are used without these prefixes.</dl>
<p> inflate, deflate, crc32, compress, uncompres, adler32, zlib</p>
<dl>
<dd>Namespaces used by the zlib library; a relatively small number of symbols are used without these prefixes.</dl>
<p> krb5, gss, GSS, asn1, decode_krb5, encode_krb5, profile, mit</p>
<dl>
<dd>Some of the prefixes used by the MIT GSSAPI library and dependencies thereof; a number of symbols lie outside these prefixes.</dl>
<p> pakchois_</p>
<dl>
<dd>Namespace used by the pakchois library.</dl>
<p> px_</p>
<dl>
<dd>Namespace used by the libproxy library.</dl>
<h3>Argument validation</h3>
<p>neon does not attempt to validate that the parameters passed to functions conform to the API (for instance, checking that pointer arguments are not NULL). Any use of the neon API which is not documented to produce a certain behaviour results is said to produce <i>undefined behaviour</i>; it is likely that neon will segfault under these conditions.</p>
<h3>URI paths, WebDAV metadata</h3>
<p>The path strings passed to any function must be <i>URI-encoded</i> by the application; neon never performs any URI encoding or decoding internally. WebDAV property names and values must be valid UTF-8 encoded Unicode strings.</p>
<h3>User interaction</h3>
<p>As a pure library interface, neon will never produce output on <code>stdout</code> or <code>stderr</code>; all user interaction is the responsibilty of the application.</p>
<h3>Memory handling</h3>
<p>neon does not attempt to cope gracefully with an out-of-memory situation; instead, by default, the <code>abort</code> function is called to immediately terminate the process. An application may register a custom function which will be called before <code>abort</code> in such a situation; see ne_oom_callback.</p>
<h3>Callbacks and userdata</h3>
<p>Whenever a callback is registered, a userdata pointer is also used to allow the application to associate a context with the callback. The userdata is of type <code>void *</code>, allowing any pointer to be used.</p>
<h3>Large File Support</h3>
<p>Since version 0.27.0, neon transparently uses the &quot;LFS transitional&quot; interfaces in places where file-backed file descriptors are manipulated. This means files larger than 2GiB can be handled on platforms with a native 32-bit off_t type, where LFS support is available. </p>
<p> Some interfaces use the ne_off_t type, which is defined to be either off_t or off64_t according to whether LFS support is detected at build time. neon does not use or require the -D_FILE_OFFSET_BITS=64 macro definition.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-ne_session_create/">ne_session_create</a>(3), ne_oom_callback</p>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
