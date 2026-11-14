---
title: "krb5_introduction(3)"
name: "krb5_introduction"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_introduction/"
description: "krb5_introduction – Introduction to the Kerberos 5 API"
---

<h2 class="name">NAME</h2>
<p> krb5_introduction &#8211; Introduction to the Kerberos 5 API</p>
<h2>Kerberos 5 API Overview</h2>
<p> All functions are documented in manual pages. This section tries to give an overview of the major components used in Kerberos library, and point to where to look for a specific function.</p>
<h3>Kerberos context</h3>
<p> A kerberos context (krb5_context) holds all per thread state. All global variables that are context specific are stored in this structure, including default encryption types, credential cache (for example, a ticket file), and default realms. </p>
<p> The internals of the structure should never be accessed directly, functions exist for extracting information. </p>
<p> See the manual page for <code>krb5_init_context()</code> how to create a context and module <code>Heimdal Kerberos 5 library</code> for more information about the functions.</p>
<h3>Kerberos authentication context</h3>
<p> Kerberos authentication context (krb5_auth_context) holds all context related to an authenticated connection, in a similar way to the kerberos context that holds the context for the thread or process. </p>
<p> The krb5_auth_context is used by various functions that are directly related to authentication between the server/client. Example of data that this structure contains are various flags, addresses of client and server, port numbers, keyblocks (and subkeys), sequence numbers, replay cache, and checksum types.</p>
<h3>Kerberos principal</h3>
<p> The Kerberos principal is the structure that identifies a user or service in Kerberos. The structure that holds the principal is the krb5_principal. There are function to extract the realm and elements of the principal, but most applications have no reason to inspect the content of the structure. </p>
<p> The are several ways to create a principal (with different degree of portability), and one way to free it. </p>
<p> See also the page <code>The principal handing functions.</code> for more information and also module <code>Heimdal Kerberos 5 principal functions</code>.</p>
<h3>Credential cache</h3>
<p> A credential cache holds the tickets for a user. A given user can have several credential caches, one for each realm where the user have the initial tickets (the first krbtgt). </p>
<p> The credential cache data can be stored internally in different way, each of them for different proposes. File credential (FILE) caches and processes based (KCM) caches are for permanent storage. While memory caches (MEMORY) are local caches to the local process. </p>
<p> Caches are opened with <code>krb5_cc_resolve()</code> or created with <code>krb5_cc_new_unique()</code>. </p>
<p> If the cache needs to be opened again (using <code>krb5_cc_resolve()</code>) <code>krb5_cc_close()</code> will close the handle, but not the remove the cache. <code>krb5_cc_destroy()</code> will zero out the cache, remove the cache so it can no longer be referenced. </p>
<p> See also <code>The credential cache functions</code> and <code>Heimdal Kerberos 5 credential cache functions</code> .</p>
<h3>Kerberos errors</h3>
<p> Kerberos errors are based on the com_err library. All error codes are 32-bit signed numbers, the first 24 bits define what subsystem the error originates from, and last 8 bits are 255 error codes within the library. Each error code have fixed string associated with it. For example, the error-code -1765328383 have the symbolic name KRB5KDC_ERR_NAME_EXP, and associated error string &#8220;Client&#8217;s entry in database has expired&#8221;. </p>
<p> This is a great improvement compared to just getting one of the unix error-codes back. However, Heimdal have an extention to pass back customised errors messages. Instead of getting Key table entry not found&#8221;, the user might backfailed to find host/host.example.com [at] EXAMLE.COM(kvno 3) in keytab /etc/krb5.keytab (des-cbc-crc)&#8221;. This improves the chance that the user find the cause of the error so you should use the customised error message whenever it&#8217;s available. </p>
<p> See also module <code>Heimdal Kerberos 5 error reporting functions</code> .</p>
<h3>Keytab management</h3>
<p> A keytab is a storage for locally stored keys. Heimdal includes keytab support for Kerberos 5 keytabs, Kerberos 4 srvtab, AFS-KeyFile&#8217;s, and for storing keys in memory. </p>
<p> Keytabs are used for servers and long-running services. </p>
<p> See also <code>The keytab handing functions</code> and <code>Heimdal Kerberos 5 keytab handling functions</code> .</p>
<h3>Kerberos crypto</h3>
<p> Heimdal includes a implementation of the Kerberos crypto framework, all crypto operations. To create a crypto context call <code>krb5_crypto_init()</code>. </p>
<p> See also module <code>Heimdal Kerberos 5 cryptography functions</code> .</p>
<h2>Walkthrough of a sample Kerberos 5 client</h2>
<p> This example contains parts of a sample TCP Kerberos 5 clients, if you want a real working client, please look in appl/test directory in the Heimdal distribution. </p>
<p> All Kerberos error-codes that are returned from kerberos functions in this program are passed to krb5_err, that will print a descriptive text of the error code and exit. Graphical programs can convert error-code to a human readable error-string with the <code>krb5_get_error_message()</code> function. </p>
<p> Note that you should not use any Kerberos function before <code>krb5_init_context()</code> have completed successfully. That is the reason err() is used when <code>krb5_init_context()</code> fails. </p>
<p> First the client needs to call krb5_init_context to initialise the Kerberos 5 library. This is only needed once per thread in the program. If the function returns a non-zero value it indicates that either the Kerberos implementation is failing or it&#8217;s disabled on this host. </p>
<pre><code>
*#include&lt;krb5.h&gt;
    *
        *int
            *
            main(int argc, char **argv)
                *
{
    *krb5_context context;
    **if (krb5_init_context(&amp;context)) * errx(1, "krb5_context");
    *
</code></pre>
<p> Now the client wants to connect to the host at the other end. The preferred way of doing this is using getaddrinfo (for operating system that have this function implemented), since getaddrinfo is neutral to the address type and can use any protocol that is available. </p>
<p>*struct addrinfo *ai, *a;<br />
*struct addrinfo hints;<br />
*int error;<br />
**memset(&amp;hints, 0, sizeof(hints));<br />
*hints.ai_socktype = SOCK_STREAM;<br />
*hints.ai_protocol = IPPROTO_TCP;<br />
**error = getaddrinfo(hostname, &#8220;pop3&#8221;, &amp;hints, &amp;ai);<br />
*if (error) * errx(1, &#8220;%s: %s&#8221;, hostname, gai_strerror(error));<br />
**for (a = ai; a != NULL; a = a-&gt;ai_next)<br />
{<br />
    *int s;<br />
    **s = socket(a-&gt;ai_family, a-&gt;ai_socktype, a-&gt;ai_protocol);<br />
    *if (s &lt; 0) * continue;<br />
    *if (connect(s, a-&gt;ai_addr, a-&gt;ai_addrlen) &lt; 0)<br />
    {<br />
        *warn(&#8220;connect(%s)&#8221;, hostname);<br />
        *close(s);<br />
        *continue;<br />
        *<br />
    }<br />
    *freeaddrinfo(ai);<br />
    *ai = NULL;<br />
    *<br />
}<br />
*if (ai)<br />
{<br />
    *freeaddrinfo(ai);<br />
    *errx(&#8220;failed to contact %s&#8221;, hostname);<br />
    *<br />
}<br />
*</p>
<p> Before authenticating, an authentication context needs to be created. This context keeps all information for one (to be) authenticated connection (see krb5_auth_context). </p>
<p>*status = krb5_auth_con_init(context, &amp;auth_context);<br />
*if (status) * krb5_err(context, 1, status, &#8220;krb5_auth_con_init&#8221;);<br />
*</p>
<p> For setting the address in the authentication there is a help function krb5_auth_con_setaddrs_from_fd() that does everything that is needed when given a connected file descriptor to the socket. </p>
<p>*status = krb5_auth_con_setaddrs_from_fd(context,<br />
                                         *auth_context,<br />
                                         *&amp;sock);<br />
*if (status) * krb5_err(context, 1, status,<br />
                        *&#8221;krb5_auth_con_setaddrs_from_fd&#8221;);<br />
*</p>
<p> The next step is to build a server principal for the service we want to connect to. (See also <code>krb5_sname_to_principal()</code>.) </p>
<p>*status = krb5_sname_to_principal(context,<br />
                                  *hostname,<br />
                                  *service,<br />
                                  *KRB5_NT_SRV_HST,<br />
                                  *&amp;server);<br />
*if (status) * krb5_err(context, 1, status, &#8220;krb5_sname_to_principal&#8221;);<br />
*</p>
<p> The client principal is not passed to krb5_sendauth() function, this causes the krb5_sendauth() function to try to figure it out itself. </p>
<p> The server program is using the function krb5_recvauth() to receive the Kerberos 5 authenticator. </p>
<p> In this case, mutual authentication will be tried. That means that the server will authenticate to the client. Using mutual authentication is required to avoid man-in-the-middle attacks, since it enables the user to verify that they are talking to the right server (a server that knows the key). </p>
<p> If you are using a non-blocking socket you will need to do all work of krb5_sendauth() yourself. Basically you need to send over the authenticator from krb5_mk_req() and, in case of mutual authentication, verifying the result from the server with krb5_rd_rep(). </p>
<p>*status = krb5_sendauth(context,<br />
                        *&amp;auth_context,<br />
                        *&amp;sock,<br />
                        *VERSION,<br />
                        *NULL,<br />
                        *server,<br />
                        *AP_OPTS_MUTUAL_REQUIRED,<br />
                        *NULL,<br />
                        *NULL,<br />
                        *NULL,<br />
                        *NULL,<br />
                        *NULL,<br />
                        *NULL);<br />
*if (status) * krb5_err(context, 1, status, &#8220;krb5_sendauth&#8221;);<br />
*</p>
<p> Once authentication has been performed, it is time to send some data. First we create a krb5_data structure, then we sign it with krb5_mk_safe() using the auth_context that contains the session-key that was exchanged in the krb5_sendauth()/krb5_recvauth() authentication sequence. </p>
<p>*data.data = &#8220;hej&#8221;;<br />
*data.length = 3;<br />
**krb5_data_zero(&amp;packet);<br />
**status = krb5_mk_safe(context,<br />
                        *auth_context,<br />
                        *&amp;data,<br />
                        *&amp;packet,<br />
                        *NULL);<br />
*if (status) * krb5_err(context, 1, status, &#8220;krb5_mk_safe&#8221;);<br />
*</p>
<p> And send it over the network. </p>
<p>*len = packet.length;<br />
*net_len = htonl(len);<br />
**if (krb5_net_write(context, &amp;sock, &amp;net_len, 4) != 4) * err(1, &#8220;krb5_net_write&#8221;);<br />
*if (krb5_net_write(context, &amp;sock, packet.data, len) != len) * err(1, &#8220;krb5_net_write&#8221;);<br />
*</p>
<p> To send encrypted (and signed) data krb5_mk_priv() should be used instead. krb5_mk_priv() works the same way as krb5_mk_safe(), with the exception that it encrypts the data in addition to signing it. </p>
<p>*data.data = &#8220;hemligt&#8221;;<br />
*data.length = 7;<br />
**krb5_data_free(&amp;packet);<br />
**status = krb5_mk_priv(context,<br />
                        *auth_context,<br />
                        *&amp;data,<br />
                        *&amp;packet,<br />
                        *NULL);<br />
*if (status) * krb5_err(context, 1, status, &#8220;krb5_mk_priv&#8221;);<br />
*</p>
<p> And send it over the network. </p>
<pre><code>
*len = packet.length;
*net_len = htonl(len);
**if (krb5_net_write(context, &amp;sock, &amp;net_len, 4) != 4) * err(1, "krb5_net_write");
*if (krb5_net_write(context, &amp;sock, packet.data, len) != len) * err(1, "krb5_net_write");
*
    *
</code></pre>
<p> The server is using krb5_rd_safe() and krb5_rd_priv() to verify the signature and decrypt the packet.</p>
<h2>Validating a password in an application</h2>
<p> See the manual page for krb5_verify_user().</p>
<h2>API differences to MIT Kerberos</h2>
<p> This section is somewhat disorganised, but so far there is no overall structure to the differences, though some of the have their root in that Heimdal uses an ASN.1 compiler and MIT doesn&#8217;t.</p>
<h3>Principal and realms</h3>
<p> Heimdal stores the realm as a krb5_realm, that is a char *. MIT Kerberos uses a krb5_data to store a realm. </p>
<p> In Heimdal krb5_principal doesn&#8217;t contain the component name_type; it&#8217;s instead stored in component name.name_type. To get and set the nametype in Heimdal, use <code>krb5_principal_get_type()</code> and <code>krb5_principal_set_type()</code>. </p>
<p> For more information about principal and realms, see krb5_principal.</p>
<h3>Error messages</h3>
<p> To get the error string, Heimdal uses <code>krb5_get_error_message()</code>. This is to return custom error messages (like Can&#8217;t find host/datan.example.com\@CODE.COM in /etc/krb5.conf.&#8221; instead of aKey table entry not found&#8221; that error_message returns. </p>
<p> Heimdal uses a threadsafe(r) version of the com_err interface; the global com_err table isn&#8217;t initialised. Then error_message returns quite a boring error string (just the error code itself). </p>
<h2>Index</h2>
