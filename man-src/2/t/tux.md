---
title: "tux(2)"
name: "tux"
section: "2"
letter: "t"
url: "/docs/linux/man/2-tux/"
description: "tux – interact with the TUX kernel subsystem"
---

<h2>NAME</h2>
<p> tux &#8211; interact with the TUX kernel subsystem</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/tuxmodule.h&gt;
int tux(unsigned int action, user_req_t *req);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>tux()</code> system call calls the kernel to perform an <i>action</i> on behalf of the currently executing user-space TUX module. </p>
<p> <i>action</i> can be one of:<br />
enum tux_actions {<br />
    TUX_ACTION_STARTUP = 1,<br />
    TUX_ACTION_SHUTDOWN = 2,<br />
    TUX_ACTION_STARTTHREAD = 3,<br />
    TUX_ACTION_STOPTHREAD = 4,<br />
    TUX_ACTION_EVENTLOOP = 5,<br />
    TUX_ACTION_GET_OBJECT = 6,<br />
    TUX_ACTION_SEND_OBJECT = 7,<br />
    TUX_ACTION_READ_OBJECT = 8,<br />
    TUX_ACTION_FINISH_REQ = 9,<br />
    TUX_ACTION_FINISH_CLOSE_REQ = 10,<br />
    TUX_ACTION_REGISTER_MODULE = 11,<br />
    TUX_ACTION_UNREGISTER_MODULE = 12,<br />
    TUX_ACTION_CURRENT_DATE = 13,<br />
    TUX_ACTION_REGISTER_MIMETYPE = 14,<br />
    TUX_ACTION_READ_HEADERS = 15,<br />
    TUX_ACTION_POSTPONE_REQ = 16,<br />
    TUX_ACTION_CONTINUE_REQ = 17,<br />
    TUX_ACTION_REDIRECT_REQ = 18,<br />
    TUX_ACTION_READ_POST_DATA = 19,<br />
    TUX_ACTION_SEND_BUFFER = 20,<br />
    TUX_ACTION_WATCH_PROXY_SOCKET = 21,<br />
    TUX_ACTION_WAIT_PROXY_SOCKET = 22,<br />
    TUX_ACTION_QUERY_VERSION = 23,<br />
    MAX_TUX_ACTION<br />
};</p>
<p> The first <i>action</i> values listed below are administrative and are normally used only in the tux program. </p>
<p> TUX_ACTION_STARTUP starts the tux subsystem, and takes a NULL <i>req</i>. TODO: Only root can use TUX_ACTION_STARTUP. </p>
<p> TUX_ACTION_SHUTDOWN stops the tux subsystem, and takes any <i>req</i>, even a zero-filled <i>req</i>. </p>
<p> TUX_ACTION_STARTTHREAD is called once per thread with a <i>req-&gt;thread_nr</i> element monotonically increasing from 0. </p>
<p> TUX_ACTION_STOPTHREAD is not currently used by the tux daemon because all threads are automatically stopped on TUX_ACTION_SHUTDOWN. It remains available because it may be useful in circumstances that the tux daemon does not yet handle. </p>
<p> TUX_ACTION_REGISTER_MODULE Register a user-space module identified by the <i>req-&gt;modulename</i> string. One VFS name can be registered only once. </p>
<p> <i>req-&gt;version_major</i>, <i>req-&gt;version_minor</i>, and <i>req-&gt;version_patch</i> have to be set appropriately from TUX_MAJOR_VERSION, TUX_MINOR_VERSION, and TUX_PATCHLEVEL_VERSION, respectively; the kernel will sanity-check binary compatibility of the module. </p>
<p> TUX_ACTION_UNREGISTER_MODULE Unregister a user-space module identified by the req-&gt;modulename string. Only registered modules can be unregistered. </p>
<p> TUX_ACTION_CURRENT_DATE Set the current date string to req-&gt;new_date. The date string must be RFC 1123-compliant and increase monotonically. The tux daemon normally calls this once per second. </p>
<p> TUX_ACTION_REGISTER_MIMETYPE Sets the extension req-&gt;objectname to map to mimetype req-&gt;object_addr. The tux daemon normally registers the mime types in /etc/tux.mime.types, but modules could conceivably create their own mimetype mappings. </p>
<p> TUX_ACTION_QUERY_VERSION Return the major version, minor version, and patchlevel of the kernel TUX subsystem, encoded in the return value as<br />
 (TUX_MAJOR_VERSION &lt;&lt; 24) | (TUX_MINOR_VERSION &lt;&lt; 16) |<br />
&nbsp;<wbr>TUX_PATCHLEVEL_VERSION<br />
 If the system call sets errno to EINVAL, assume major version 2, minor version 1. </p>
<p> The rest of the <i>action</i> values are used to respond to TUX events. The general architecture is that TUX&#8217;s event loop is invoked to catch HTTP events, and then responses are generated in response to those events. </p>
<p> TUX_ACTION_EVENTLOOP invokes the TUX event loop&#8212;the TUX subsystem will either immediately return with a new request <i>req</i>, or will wait for new requests to arrive. </p>
<p> TUX_ACTION_GET_OBJECT issues a request for the URL object named in <i>req-&gt;objectname</i>. If the object is not immediately available then the currently handled request is suspended, and a new request is returned, or the TUX subsystem waits for new requests. </p>
<p> A URL object is a data stream that is accessed via a URL and is directly associated with a file pointed to by that URL. (In the future, we may extend the concept of a URL object.) </p>
<p> TUX_ACTION_SEND_OBJECT sends the current URL object to the client. </p>
<p> TUX_ACTION_READ_OBJECT reads the current URL object into the address specified by <i>req-&gt;object_addr</i>. TUX_ACTION_READ_OBJECT must not be called unless <i>req-&gt;objectlen</i> &gt;= 0. </p>
<p> TUX_ACTION_READ_HEADERS reads a non-zero-delimited string into req-&gt;object_addr, with the length of the string kept in req-&gt;objectlen. This is a workaround used to read fields that tux does not currently parse; if you need it, report it as a bug so that more fields can be added to user_req (unless your use is so specialized that it will be of no general utility). </p>
<p> TUX_ACTION_POSTPONE_REQ postpones the request, meaning that no tux system calls will return data for this request until TUX_ACTION_CONTINUE_REQ is called. </p>
<p> TUX_ACTION_CONTINUE_REQ continues a postponed request. Unlike a normal TUX_ACTION, it takes as its argument the socket descriptor (this allows it to be called from a program that is unrelated to the program that called TUX_ACTION_POSTPONE_REQ if necessary). It is called like this: </p>
<pre>
    ret = tux(TUX_ACTION_CONTINUE_REQ, (user_req_t *)socket);
</pre>
<p> TUX_ACTION_READ_POST_DATA is an atomic action (it will always return with the same request, no need to handle a new request) that puts the non-zero-delimited POST data, up to the maximum set in req-&gt;objectlen (and limited by /proc/sys/net/tux/max_header_len), into req-&gt;object_addr, ands resets req-&gt;objectlen to the length. </p>
<p> TUX_ACTION_REDIRECT_REQ causes the request to be redirected to the secondary server. (No need to call TUX_ACTION_FINISH_REQ.) </p>
<p> TUX_ACTION_FINISH_REQ finishes and logs the request. </p>
<p> TUX_ACTION_FINISH_CLOSE_REQ is like TUX_ACTION_FINISH_REQ except that it also closes HTTP 1.1 keepalive connections. </p>
<p> TUX_ACTION_SEND_BUFFER is like TUX_ACTION_SEND_OBJECT except that it sends whatever is in the req-&gt;object_addr buffer. This can be used as a generic output buffer. </p>
<p> TUX_ACTION_WATCH_PROXY_SOCKET sets up a non-TUX socket to be used with TUX_ACTION_WAIT_PROXY_SOCKET. The socket must be a network socket. The function is atomic. Repeated calls to this action will replace the previous proxy socket, so there is no need to deinitialize it. The socket file descriptor must be put into req-&gt;object_addr. </p>
<p> TUX_ACTION_WAIT_PROXY_SOCKET postpones the current request until there are input packets on the socket that was set up via TUX_ACTION_WATCH_PROXY_SOCKET. The proxy socket has a keepalive timer running. The request will be resumed once there is input activity on the socket &#8211; the module can use nonblocking recv() on the socket to process input packets. </p>
<p> user_req_t <i>req</i> is the request returned by the TUX subsystem. Defined fields depend on the version. For major version 2, they are:<br />
typedef struct user_req_s {<br />
    int version_major;<br />
    int version_minor;<br />
    int version_patch;<br />
    int http_version;<br />
    int http_method;<br />
    int sock;<br />
    int event;<br />
    int thread_nr;<br />
    void *id;<br />
    void *priv;<br />
    int http_status;<br />
    int bytes_sent;<br />
    char *object_addr;<br />
    int module_index;<br />
    char modulename[MAX_MODULENAME_LEN];<br />
    unsigned int client_host;<br />
    unsigned int objectlen;<br />
    char query[MAX_URI_LEN];<br />
    char objectname[MAX_URI_LEN];<br />
    unsigned int cookies_len;<br />
    char cookies[MAX_COOKIE_LEN];<br />
    char content_type[MAX_FIELD_LEN];<br />
    char user_agent[MAX_FIELD_LEN];<br />
    char accept[MAX_FIELD_LEN];<br />
    char accept_charset[MAX_FIELD_LEN];<br />
    char accept_encoding[MAX_FIELD_LEN];<br />
    char accept_language[MAX_FIELD_LEN];<br />
    char cache_control[MAX_FIELD_LEN];<br />
    char if_modified_since[MAX_FIELD_LEN];<br />
    char negotiate[MAX_FIELD_LEN];<br />
    char pragma[MAX_FIELD_LEN];<br />
    char referer[MAX_FIELD_LEN];<br />
    char *post_data;<br />
    char new_date[DATE_LEN];<br />
    int keep_alive;<br />
} user_req_t;<br />
 For major version 3, they are:<br />
typedef struct user_req_s {<br />
    uint32_t version_major;<br />
    uint32_t version_minor;<br />
    uint32_t version_patch;<br />
    uint32_t http_version;<br />
    uint32_t http_method;<br />
    uint32_t http_status;<br />
    uint32_t sock;<br />
    uint32_t event;<br />
    uint32_t error;<br />
    uint32_t thread_nr;<br />
    uint32_t bytes_sent;<br />
    uint32_t client_host;<br />
    uint32_t objectlen;<br />
    uint32_t module_index;<br />
    uint32_t keep_alive;<br />
    uint32_t cookies_len;<br />
    uint64_t id;<br />
    uint64_t priv;<br />
    uint64_t object_addr;<br />
    uint8_t query[MAX_URI_LEN];<br />
    uint8_t objectname[MAX_URI_LEN];<br />
    uint8_t cookies[MAX_COOKIE_LEN];<br />
    uint8_t content_type[MAX_FIELD_LEN];<br />
    uint8_t user_agent[MAX_FIELD_LEN];<br />
    uint8_t accept[MAX_FIELD_LEN];<br />
    uint8_t accept_charset[MAX_FIELD_LEN];<br />
    uint8_t accept_encoding[MAX_FIELD_LEN];<br />
    uint8_t accept_language[MAX_FIELD_LEN];<br />
    uint8_t cache_control[MAX_FIELD_LEN];<br />
    uint8_t if_modified_since[MAX_FIELD_LEN];<br />
    uint8_t negotiate[MAX_FIELD_LEN];<br />
    uint8_t pragma[MAX_FIELD_LEN];<br />
    uint8_t referer[MAX_FIELD_LEN];<br />
    uint8_t new_date[DATE_LEN];<br />
} user_req_t;</p>
<dl>
<dt>version_major</p>
<dd> Always set to TUX_MAJOR_VERSION, used to flag binary incompatibility.</p>
<dt>version_minor</p>
<dd> Always set to TUX_MINOR_VERSION, used to flag binary incompatibility.</p>
<dt>version_patch</p>
<dd> Always set to TUX_PATCHLEVEL_VERSION, used to flag binary incompatibility.</p>
<dt>http_version</p>
<dd> One of <code>HTTP_1_0</code> or <code>HTTP_1_1</code></p>
<dt>http_method</p>
<dd> One of <code>METHOD_NONE</code>, <code>METHOD_GET</code>, <code>METHOD_HEAD</code>, <code>METHOD_POST</code>, or <code>METHOD_PUT</code></p>
<dt>sock</p>
<dd> Socket file descriptor; writing to this will send data to the connected client associated with this request. Do not read from this socket file descriptor; you could potentially confuse the HTTP engine.</p>
<dt>event</p>
<dd> Private, per-request state for use in tux modules. The system will preserve this value as long as a request is active.</p>
<dt>thread_nr</p>
<dd> Thread index; see discussion of <i>TUX_ACTION_STARTTHREAD</i>.</p>
<dt>id</p>
<dd> A tux-daemon-internal value that is used to multiplex requests to the correct modules.</p>
<dt>priv</p>
<dd> Works just like <i>event</i>, except that it is a pointer to private data instead of an integer.</p>
<dt>http_status</p>
<dd> Set the error status as an integer for error reporting. The status is good by default, so it should not be modified except to report errors.</p>
<dt>bytes_sent</p>
<dd> When you write to sock, you must set bytes_sent to the total number of bytes sent since the last tux() operation on this <i>req</i>, or the log entry&#8217;s bytes sent counter will be incorrect. (This may change or disappear in future versions of tux.)</p>
<dt>object_addr</p>
<dd> Set to an address for a buffer of at least <i>req-&gt;objectlen</i> size into which to read an object from the URL cache with the TUX_ACTION_READ_OBJECT <i>action</i>. TUX_ACTION_READ_OBJECT must not be called unless <i>req-&gt;objectlen</i> &gt;= 0, and TUX implicitly relies on <i>req-&gt;object_addr</i> being at least <i>req-&gt;objectlen</i> in size.</p>
<dt>module_index</p>
<dd> Used by the <a href="/docs/linux/man/8-tux/">tux</a>(8) daemon to determine which loadable module to associate with a <i>req</i>.</p>
<dt>modulename</p>
<dd> The name of the module as set by TUX_ACTION_REGISTER_MODULE; private data to the tux daemon.</p>
<dt>client_host</p>
<dd> The IP address of the host to which sock is connected.</p>
<dt>objectlen</p>
<dd> The size of a file that satisfies the current request and which is currently living in the URL cache. This is set if a request returns after TUX_ACTION_GET_OBJECT. A module should make sure that the buffer at <i>req-&gt;object_addr</i> is at least <i>req-&gt;objectlen</i> in size before calling TUX_ACTION_READ_OBJECT.</p>
<dt>query</p>
<dd> The full query string sent from the client.</p>
<dt>objectname</p>
<dd> Specifies the name of a URL to get with the TUX_ACTION_GET_OBJECT <i>action</i>. If the URL is not immediately available (that is, is not in the URL cache), the request is queued and the tux subsystem may go on to other ready requests while waiting.</p>
<dt>cookies_len</p>
<dd> If cookies are in the request header, <i>cookies_len</i> contains the length of the <i>cookies</i> string</p>
<dt>cookies</p>
<dd> If cookies are in the request header, <i>cookies</i> is the string in which the cookies are passed to the module.</p>
<dt>content_type</p>
<dd> The Content-Type header value for the request</p>
<dt>user_agent</p>
<dd> The User-Agent header value for the request</p>
<dt>accept</p>
<dd> The Accept header value for the request</p>
<dt>accept_charset</p>
<dd> The Accept-Charset header value for the request</p>
<dt>accept_encoding</p>
<dd> The Accept-Encoding header value for the request</p>
<dt>accept_language</p>
<dd> The Accept-Language header value for the request</p>
<dt>cache_control</p>
<dd> The Cache-Control header value for the request</p>
<dt>if_modified_since</p>
<dd> The If-Modified-Since header value for the request</p>
<dt>negotiate</p>
<dd> The Negotiate header value for the request</p>
<dt>pragma</p>
<dd> The Pragma header value for the request</p>
<dt>referer</p>
<dd> The Referer header value for the request</p>
<dt>post_data</p>
<dd> For POST requests, the incoming data is placed in post_data.</p>
<dt>new_date</p>
<dd> Returns the current date/time</p>
<dt>keep_alive</p>
<dd> The KeepAlive header value for the request </p>
</dl>
<h2>RETURN VALUE</h2>
<p> <code>tux()</code> returns the following values: </p>
<pre><code>
enum tux_reactions {
    TUX_RETURN_USERSPACE_REQUEST = 0,
    TUX_RETURN_EXIT = 1,
    TUX_RETURN_SIGNAL = 2,
};
</code></pre>
<p> TUX_RETURN_USERSPACE_REQUEST means that the kernel has put a new request into <i>req</i>; the request must be responded to with one of TUX_ACTION_GET_OBJECT, TUX_ACTION_SEND_OBJECT, TUX_ACTION_READ_OBJECT, or TUX_ACTION_FINISH_REQ. </p>
<p> TUX_RETURN_EXIT means that TUX has been stopped. </p>
<p> TUX_RETURN_SIGNAL means that a signal has occured. No new request is scheduled. </p>
<h2>ERRORS</h2>
<p> Any negative value (such as -EFAULT, -EINVAL) is an indication of an error. </p>
<h2>BUGS</h2>
<p> This man page is incomplete. </p>
<h2>Index</h2>
