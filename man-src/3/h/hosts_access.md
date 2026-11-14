---
title: "hosts_access(3)"
name: "hosts_access"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hosts_access/"
---

<h2>NAME</h2>

 hosts_access, hosts_ctl, request_init, request_set - access control library

<h2>SYNOPSIS</h2>

 <pre><code>
#include "tcpd.h"
extern int allow_severity;
extern int deny_severity;
struct request_info *request_init(request, key, value, ..., 0) struct request_info *request;
struct request_info *request_set(request, key, value, ..., 0) struct request_info *request;
int hosts_access(request)
struct request_info *request;
int hosts_ctl(daemon, client_name, client_addr, client_user)
char *daemon;
char *client_name;
char *client_addr;
char *client_user;
</code></pre>

<h2>DESCRIPTION</h2>

 The routines described in this document are part of the <i>libwrap.a</i> library. They implement a rule-based access control language with optional shell commands that are executed when a rule fires. 

 request_init() initializes a structure with information about a client request. request_set() updates an already initialized request structure. Both functions take a variable-length list of key-value pairs and return their first argument. The argument lists are terminated with a zero key value. All string-valued arguments are copied. The expected keys (and corresponding value types) are:
<dl>
<dt>RQ_FILE (int)
<dd> The file descriptor associated with the request.
<dt>RQ_CLIENT_NAME (char *)
<dd> The client host name.
<dt>RQ_CLIENT_ADDR (char *)
<dd> A printable representation of the client network address.
<dt>RQ_CLIENT_SIN (struct sockaddr_in *)
<dd> An internal representation of the client network address and port. The contents of the structure are not copied.
<dt>RQ_SERVER_NAME (char *)
<dd> The hostname associated with the server endpoint address.
<dt>RQ_SERVER_ADDR (char *)
<dd> A printable representation of the server endpoint address.
<dt>RQ_SERVER_SIN (struct sockaddr_in *)
<dd> An internal representation of the server endpoint address and port. The contents of the structure are not copied.
<dt>RQ_DAEMON (char *)
<dd> The name of the daemon process running on the server host.
<dt>RQ_USER (char *)
<dd> The name of the user on whose behalf the client host makes the request.</dl>
 

 hosts_access() consults the access control tables described in the <i><a HREF="/docs/linux/man/5-hosts_access/">hosts_access</a>(5)</i> manual page. When internal endpoint information is available, host names and client user names are looked up on demand, using the request structure as a cache. hosts_access() returns zero if access should be denied. 

 hosts_ctl() is a wrapper around the request_init() and hosts_access() routines with a perhaps more convenient interface (though it does not pass on enough information to support automated client username lookups). The client host address, client host name and username arguments should contain valid data or STRING_UNKNOWN. hosts_ctl() returns zero if access should be denied. 

 The <i>allow_severity</i> and <i>deny_severity</i> variables determine how accepted and rejected requests may be logged. They must be provided by the caller and may be modified by rules in the access control tables.

<h2>DIAGNOSTICS</h2>

 Problems are reported via the syslog daemon.

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/5-hosts_access/">hosts_access</a>(5), format of the access control tables. <a HREF="/docs/linux/man/5-hosts_options/">hosts_options</a>(5), optional extensions to the base language.

<h2>FILES</h2>

 /etc/hosts.allow, /etc/hosts.deny, access control tables.

<h2>BUGS</h2>

 hosts_access() uses the strtok() library function. This may interfere with other code that relies on strtok().

<h2>AUTHOR</h2>

 <pre>
Wietse Venema (wietse [at] wzv.win.tue.nl)
Department of Mathematics and Computing Science
Eindhoven University of Technology
Den Dolech 2, P.O. Box 513, 
5600 MB Eindhoven, The Netherlands
</pre>

<h2>Index</h2>


