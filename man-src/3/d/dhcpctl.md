---
title: "dhcpctl(3)"
name: "dhcpctl"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dhcpctl/"
description: "dhcpctl_initialize – dhcpctl library initialization."
---

<h2 class="name">NAME</h2>
<p> <code>dhcpctl_initialize</code> &#8211; dhcpctl library initialization. </p>
<h2>SYNOPSIS</h2>
<p> Fd #include &lt;dhcpctl/dhcpctl.h&gt; Ft dhcpctl_status Fo dhcpctl_initialize Fa void Fc Ft dhcpctl_status Fo dhcpctl_connect Fa dhcpctl_handle *cxn Fa const char *host Fa int port Fa dhcpctl_handle auth Fc Ft dhcpctl_status Fo dhcpctl_wait_for_completion Fa dhcpctl_handle object Fa dhcpctl_status *status Fc Ft dhcpctl_status Fo dhcpctl_get_value Fa dhcpctl_data_string *value Fa dhcpctl_handle object Fa const char *name Fc Ft dhcpctl_status Fo dhcpctl_get_boolean Fa int *value Fa dhcpctl_handle object Fa const char *name Fc Ft dhcpctl_status Fo dhcpctl_set_value Fa dhcpctl_handle object Fa dhcpctl_data_string value Fa const char *name Fc Ft dhcpctl_status Fo dhcpctl_set_string_value Fa dhcpctl_handle object Fa const char *value Fa const char *name Fc Ft dhcpctl_status Fo dhcpctl_set_boolean_value Fa dhcpctl_handle object Fa int value Fa const char *name Fc Ft dhcpctl_status Fo dhcpctl_set_int_value Fa dhcpctl_handle object Fa int value Fa const char *name Fc Ft dhcpctl_status Fo dhcpctl_object_update Fa dhcpctl_handle connection Fa dhcpctl_handle object Fc Ft dhcpctl_status Fo dhcpctl_object_refresh Fa dhcpctl_handle connection Fa dhcpctl_handle object Fc Ft dhcpctl_status Fo dhcpctl_object_remove Fa dhcpctl_handle connection Fa dhcpctl_handle object Fc Ft dhcpctl_status Fo dhcpctl_set_callback Fa dhcpctl_handle object Fa void *data Fa void (*function) (dhcpctl_handle, dhcpctl_status, void *) Fc Ft dhcpctl_status Fo dhcpctl_new_authenticator Fa dhcpctl_handle *object Fa const char *name Fa const char *algorithm Fa const char *secret Fa unsigned secret_len Fc Ft dhcpctl_status Fo dhcpctl_new_object Fa dhcpctl_handle *object Fa dhcpctl_handle connection Fa const char *object_type Fc Ft dhcpctl_status Fo dhcpctl_open_object Fa dhcpctl_handle object Fa dhcpctl_handle connection Fa int flags Fc Ft isc_result_t Fo omapi_data_string_new Fa dhcpctl_data_string *data Fa unsigned int length Fa const char *filename, Fa int lineno Fc Ft isc_result_t Fo dhcpctl_data_string_dereference Fa dhcpctl_data_string * Fa const char * Fa int Fc</p>
<h2>DESCRIPTION</h2>
<p> The dhcpctl set of functions provide an API that can be used to communicate with and manipulate a running ISC DHCP server. All functions return a value of <code>isc_result_t</code> The return values reflects the result of operations to local data structures. If an operation fails on the server for any reason, then the error result will be returned through the second parameter of the Fn dhcpctl_wait_for_completion call. </p>
<p> Fn dhcpctl_initialize sets up the data structures the library needs to do its work. This function must be called once before any other. </p>
<p> Fn dhcpctl_connect opens a connection to the DHCP server at the given host and port. If an authenticator has been created for the connection, then it is given as the 4th argument. On a successful return the address pointed at by the first argument will have a new connection object assigned to it. </p>
<p> For example: </p>
<blockquote>
<pre><code>
s = dhcpctl_connect(&amp;cxn, "127.0.0.1", 7911, NULL);
</code></pre>
</blockquote>
<p> connects to the DHCP server on the localhost via port 7911 (the standard OMAPI port). No authentication is used for the connection. </p>
<p> Fn dhcpctl_wait_for_completion flushes a pending message to the server and waits for the response. The result of the request as processed on the server is returned via the second parameter. </p>
<blockquote><p>
s = dhcpctl_wait_for_completion(cxn, &amp;wv);<br />
if (s != ISC_R_SUCCESS)<br />
    local_failure(s);<br />
else if (wv != ISC_R_SUCCESS)<br />
    server_failure(wc);
 </p></blockquote>
<p> The call to Fn dhcpctl_wait_for_completion won&#8217;t return until the remote message processing completes or the connection to the server is lost. </p>
<p> Fn dhcpctl_get_value extracts a value of an attribute from the handle. The value can be of any length and is treated as a sequence of bytes. The handle must have been created first with Fn dhcpctl_new_object and opened with Fn dhcpctl_open_object . The value is returned via the parameter named &#8220;value&#8221; The last parameter is the name of attribute to retrieve. </p>
<blockquote><p>
dhcpctl_data_string value = NULL;<br />
dhcpctl_handle lease;<br />
time_t thetime;<br />
s = dhcpctl_get_value(&amp;value, lease, &#8220;ends&#8221;);<br />
assert(s == ISC_R_SUCCESS &amp;&amp; value-&gt;len == sizeof(thetime));<br />
memcpy(&amp;thetime, value-&gt;value, value-&gt;len);
 </p></blockquote>
<p> Fn dhcpctl_get_boolean extracts a boolean valued attribute from the object handle. </p>
<p> The Fn dhcpctl_set_value , Fn dhcpctl_set_string_value , Fn dhcpctl_set_boolean_value , and Fn dhcpctl_set_int_value functions all set a value on the object handle. </p>
<p> Fn dhcpctl_object_update function queues a request for all the changes made to the object handle be be sent to the remote for processing. The changes made to the atributes on the handle will be applied to remote object if permitted. </p>
<p> Fn dhcpctl_object_refresh queues up a request for a fresh copy of all the attribute values to be sent from the remote to refresh the values in the local object handle. </p>
<p> Fn dhcpctl_object_remove queues a request for the removal on the server of the object referenced by the handle. </p>
<p> The Fn dhcpctl_set_callback function sets up a user-defined function to be called when an event completes on the given object handle. This is needed for asynchronous handling of events, versus the synchronous handling given by Fn dhcpctl_wait_for_completion . When the function is called the first parameter is the object the event arrived for, the second is the status of the message that was processed, the third is the same value as the second parameter given to Fn dhcpctl_set_callback . </p>
<p> The Fn dhcpctl_new_authenticator creates a new authenticator object to be used for signing the messages that cross over the network. The &#8220;name&#8221; &#8220;algorithm&#8221; and &#8220;secret&#8221; values must all match what the server uses and are defined in its configuration file. The created object is returned through the first parameter and must be used as the 4th parameter to Fn dhcpctl_connect . Note that the &#8216;secret&#8217; value must not be base64 encoded, which is different from how the value appears in the dhcpd.conf file. </p>
<p> Fn dhcpctl_new_object creates a local handle for an object on the the server. The &#8220;object_type&#8221; parameter is the ascii name of the type of object being accessed. e.g. Qq lease . This function only sets up local data structures, it does not queue any messages to be sent to the remote side, Fn dhcpctl_open_object does that. </p>
<p> Fn dhcpctl_open_object builds and queues the request to the remote side. This function is used with handle created via Fn dhcpctl_new_object . The flags argument is a bit mask with the following values available for setting:</p>
<dl>
<dt><code>DHCPCTL_CREATE</code></p>
<dd> if the object does not exist then the remote will create it</p>
<dt><code>DHCPCTL_UPDATE</code></p>
<dd> update the object on the remote side using the attributes already set in the handle.</p>
<dt><code>DHCPCTL_EXCL</code></p>
<dd> return and error if the object exists and DHCPCTL_CREATE was also specified</dl>
<p> The Fn omapi_data_string_new function allocates a new Ft dhcpctl_data_string object. The data string will be large enough to hold &#8220;length&#8221; bytes of data. The &#8220;file &#8221; and &#8220;lineno&#8221; arguments are the source file location the call is made from, typically by using the <code>__FILE__</code> and <code>__LINE__</code> macros or the <code>MDL</code> macro defined in </p>
<p> Fn dhcpctl_data_string_dereference deallocates a data string created by Fn omapi_data_string_new . The memory for the object won&#8217;t be freed until the last reference is released.</p>
<h2>EXAMPLES</h2>
<p> The following program will connect to the DHCP server running on the local host and will get the details of the existing lease for IP address 10.0.0.101. It will then print out the time the lease is due to expire. Note that most error checking has been ommitted for brevity. </p>
<blockquote>
<pre><code>
#include "dhcpctl.h"
#include "omapip/result.h"
#include &lt;arpa/inet.h&gt;
#include &lt;netinet/in.h&gt;
#include &lt;stdarg.h&gt;
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;sys/socket.h&gt;
#include &lt;sys/time.h&gt;
int main(int argc, char **argv)
{
    dhcpctl_data_string ipaddrstring = NULL;
    dhcpctl_data_string value = NULL;
    dhcpctl_handle connection = NULL;
    dhcpctl_handle lease = NULL;
    isc_result_t waitstatus;
    struct in_addr convaddr;
    time_t thetime;
    dhcpctl_initialize();
    dhcpctl_connect(&amp;connection, "127.0.0.1",
                    7911, 0);

    dhcpctl_new_object(&amp;lease, connection,
                       "lease");
    memset(&amp;ipaddrstring, 0, sizeof ipaddrstring);
    inet_pton(AF_INET, "10.0.0.101",
              &amp;convaddr);
    omapi_data_string_new(&amp;ipaddrstring,
                          4, MDL);
    memcpy(ipaddrstring-&gt;value, &amp;convaddr.s_addr, 4);
    dhcpctl_set_value(lease, ipaddrstring,
                      "ip-address");
    dhcpctl_open_object(lease, connection, 0);
    dhcpctl_wait_for_completion(lease,
                                &amp;waitstatus);
    if (waitstatus != ISC_R_SUCCESS) {
        /* server not authoritative */
        exit(0);
    }
    dhcpctl_data_string_dereference(&amp;ipaddrstring,
                                    MDL);
    dhcpctl_get_value(&amp;value, lease, "ends");
    memcpy(&amp;thetime, value-&gt;value, value-&gt;len);
    dhcpctl_data_string_dereference(&amp;value, MDL);
    fprintf(stdout, "ending time is %s",
            ctime(&amp;thetime));
}
</code></pre>
</blockquote>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-omapi/">omapi</a>(3), <a href="/docs/linux/man/1-omshell/">omshell</a>(1), <a href="/docs/linux/man/8-dhcpd/">dhcpd</a>(8), <a href="/docs/linux/man/8-dhclient/">dhclient</a>(8), <a href="/docs/linux/man/5-dhcpd-conf/">dhcpd.conf</a>(5), <a href="/docs/linux/man/5-dhclient-conf/">dhclient.conf</a>(5).</p>
<h2>AUTHOR</h2>
<p> <i>dhcpctl</i> was written by Ted Lemon of Nominum, Inc. This preliminary documentation was written by James Brister of Nominum, Inc. </p>
<h2>Index</h2>
