---
title: "ecore_con(3)"
name: "ecore_con"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_con/"
description: "Ecore_Con.h – Sockets functions."
---

<p>Ecore_Con.h &#8211; Sockets functions. </p>
<h2>Synopsis</h2>
<h3>Typedefs</h3>
<p>typedef struct _Ecore_Con_Server <code>Ecore_Con_Server</code><br />
 <i>A connection handle. </i><br />
 typedef struct _Ecore_Con_Client <code>Ecore_Con_Client</code><br />
 <i>A connection handle. </i></p>
<h3>Functions</h3>
<p>EAPI int <code>ecore_con_init</code> (void)<br />
 <i>Initialises the Ecore_Con library. </i><br />
 EAPI int <code>ecore_con_shutdown</code> (void)<br />
 <i>Shuts down the Ecore_Con library. </i><br />
 EAPI <code>Ecore_Con_Server</code> * <code>ecore_con_server_add</code> (Ecore_Con_Type type, const char *name, int port, const void *data)<br />
 <i>Creates a server to listen for connections. </i><br />
 EAPI <code>Ecore_Con_Server</code> * <code>ecore_con_server_connect</code> (Ecore_Con_Type type, const char *name, int port, const void *data)<br />
 <i>Creates a server object to represent the server listening at the given port. </i><br />
 EAPI void * <code>ecore_con_server_del</code> (<code>Ecore_Con_Server</code> *svr)<br />
 <i>Closes the connection and frees the given server. </i><br />
 EAPI void * <code>ecore_con_server_data_get</code> (<code>Ecore_Con_Server</code> *svr)<br />
 <i>Retrieves the data associated with the given server. </i><br />
 EAPI int <code>ecore_con_server_connected_get</code> (<code>Ecore_Con_Server</code> *svr)<br />
 <i>Retrieves whether the given server is currently connected. </i><br />
 EAPI Ecore_List * <code>ecore_con_server_clients_get</code> (<code>Ecore_Con_Server</code> *svr)<br />
 <i>Retrieves the current list of clients. </i><br />
 EAPI int <code>ecore_con_server_send</code> (<code>Ecore_Con_Server</code> *svr, const void *data, int size)<br />
 <i>Sends the given data to the given server. </i><br />
 EAPI void <code>ecore_con_server_client_limit_set</code> (<code>Ecore_Con_Server</code> *svr, int client_limit, char reject_excess_clients)<br />
 <i>Sets a limit on the number of clients that can be handled concurrently by the given server, and a policy on what to do if excess clients try to connect. </i><br />
 EAPI char * <code>ecore_con_server_ip_get</code> (<code>Ecore_Con_Server</code> *svr)<br />
 <i>Gets the IP address of a server that has been connected to. </i><br />
 EAPI void <code>ecore_con_server_flush</code> (<code>Ecore_Con_Server</code> *svr)<br />
 <i>Flushes all pending data to the given server. </i><br />
 EAPI int <code>ecore_con_client_send</code> (<code>Ecore_Con_Client</code> *cl, const void *data, int size)<br />
 <i>Sends the given data to the given client. </i><br />
 EAPI <code>Ecore_Con_Server</code> * <code>ecore_con_client_server_get</code> (<code>Ecore_Con_Client</code> *cl)<br />
 <i>Retrieves the server representing the socket the client has connected to. </i><br />
 EAPI void * <code>ecore_con_client_del</code> (<code>Ecore_Con_Client</code> *cl)<br />
 <i>Closes the connection and frees memory allocated to the given client. </i><br />
 EAPI void <code>ecore_con_client_data_set</code> (<code>Ecore_Con_Client</code> *cl, const void *data)<br />
 <i>Sets the data associated with the given client to </i>data.<br />
 EAPI void * <code>ecore_con_client_data_get</code> (<code>Ecore_Con_Client</code> *cl)<br />
 <i>Retrieves the data associated with the given client. </i><br />
 EAPI char * <code>ecore_con_client_ip_get</code> (<code>Ecore_Con_Client</code> *cl)<br />
 <i>Gets the IP address of a cleint that has connected. </i><br />
 EAPI void <code>ecore_con_client_flush</code> (<code>Ecore_Con_Client</code> *cl)<br />
 <i>Flushes all pending data to the given client. </i><br />
 EAPI int <code>ecore_con_ssl_available_get</code> (void)<br />
 <i>Returns if SSL support is available. </i><br />
 EAPI int <code>ecore_con_url_init</code> (void)<br />
 <i>Initialises the Ecore_Con_Url library. </i><br />
 EAPI int <code>ecore_con_url_shutdown</code> (void)<br />
 <i>Shuts down the Ecore_Con_Url library. </i><br />
 EAPI Ecore_Con_Url * <code>ecore_con_url_new</code> (const char *url)<br />
 <i>Creates and initializes a new Ecore_Con_Url. </i><br />
 EAPI void <code>ecore_con_url_destroy</code> (Ecore_Con_Url *url_con)<br />
 <i>Frees the Ecore_Con_Url. </i><br />
 EAPI void <code>ecore_con_url_data_set</code> (Ecore_Con_Url *url_con, void *data)<br />
 <i>FIXME: To be documented. </i><br />
 EAPI void * <code>ecore_con_url_data_get</code> (Ecore_Con_Url *url_con)<br />
 <i>FIXME: To be documented. </i><br />
 EAPI int <code>ecore_con_url_url_set</code> (Ecore_Con_Url *url_con, const char *url)<br />
 <i>FIXME: To be documented. </i><br />
 EAPI void <code>ecore_con_url_fd_set</code> (Ecore_Con_Url *url_con, int fd)<br />
 <i>FIXME: To be documented. </i><br />
 EAPI int <code>ecore_con_url_received_bytes_get</code> (Ecore_Con_Url *url_con)<br />
 <i>FIXME: To be documented. </i><br />
 EAPI int <code>ecore_con_url_send</code> (Ecore_Con_Url *url_con, void *data, size_t length, char *content_type)<br />
 <i>FIXME: To be documented. </i><br />
 EAPI void <code>ecore_con_url_time</code> (Ecore_Con_Url *url_con, Ecore_Con_Url_Time condition, time_t tm)<br />
 <i>FIXME: To be documented. </i><br />
 EAPI int <code>ecore_con_url_ftp_upload</code> (Ecore_Con_Url *url_con, char *filename, char *user, char *pass, char *upload_dir)<br />
 <i>Makes a FTP upload. </i><br />
 EAPI void <code>ecore_con_url_verbose_set</code> (Ecore_Con_Url *url_con, int verbose)<br />
 <i>Enable or disable libcurl verbose output, useful for debug. </i><br />
 EAPI void <code>ecore_con_url_ftp_use_epsv_set</code> (Ecore_Con_Url *url_con, int use_epsv)<br />
 <i>Enable or disable EPSV extension. </i></p>
<h2>Detailed Description</h2>
<p>Sockets functions. </p>
<p> The Ecore Connection Library ( Ecore_Con ) provides simple mechanisms for communications between programs using reliable sockets. It saves the programmer from having to worry about file descripters and waiting for incoming connections. </p>
<p> There are two main objects in the Ecore_Con library: the Ecore_Con_Server and the Ecore_Con_Client. </p>
<p> The Ecore_Con_Server represents a server that can be connected to. It is used regardless of whether the program is acting as a server or client itself. </p>
<p> To create a listening server, call <code>ecore_con_server_add()</code>. </p>
<p> To connect to a server, call <code>ecore_con_server_connect()</code>. Data can then be sent to the server using the <code>ecore_con_server_send()</code>. </p>
<p> Whenever a client connection is made to an Ecore_Con_Server, a ECORE_CON_CLIENT_ADD event is emitted. Any event callbacks that are called receive a Ecore_Con_Client object, which represents a connection that that particular client. </p>
<p> Functions are described in the following groupings: </p>
<dl COMPACT>
<dt>*</p>
<dd><code>Ecore Connection Library Functions</code></p>
<dt>*</p>
<dd><code>Ecore Connection Server Functions</code></p>
<dt>*</p>
<dd><code>Ecore Connection Client Functions</code></p>
<dt>*</p>
<dd><code>Ecore URL Connection Functions</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
