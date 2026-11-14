---
title: "wl_client_flush(3)"
name: "wl_client_flush"
section: "3"
letter: "w"
url: "/docs/linux/man/3-wl_client_flush/"
description: "wl_client –"
---

<p>wl_client &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Member Functions</h3>
<pre><code>void wl_client_flush (struct wl_client *client)



struct wl_display * wl_client_get_display (struct wl_client *client)



void wl_client_get_credentials (struct wl_client *client, pid_t *pid, uid_t *uid, gid_t *gid)



struct wl_resource * wl_client_get_object (struct wl_client *client, uint32_t id)



Public Attributes
struct wl_connection * connection



struct wl_event_source * source



struct wl_display * display



struct wl_resource * display_resource



uint32_t id_count



uint32_t mask



struct wl_list link



struct wl_map objects



struct wl_signal destroy_signal



struct ucred ucred



int error</code></pre>
<h2>Member Function Documentation</h2>
<h3>void wl_client_flush (struct <code>wl_client</code> *client)</h3>
<p>Flush pending events to the client </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>client</i> The client object</dl>
<p> Events sent to clients are queued in a buffer and written to the socket later &#8211; typically when the compositor has handled all requests and goes back to block in the event loop. This function flushes all queued up events for a client immediately.</p>
<h3>void wl_client_get_credentials (struct <code>wl_client</code> *client, pid_t *pid, uid_t *uid, gid_t *gid)</h3>
<p>Return Unix credentials for the client </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>client</i> The display object<br />
 <i>pid</i> Returns the process ID<br />
 <i>uid</i> Returns the user ID<br />
 <i>gid</i> Returns the group ID</dl>
<p> This function returns the process ID, the user ID and the group ID for the given client. The credentials come from getsockopt() with SO_PEERCRED, on the client socket fd. All the pointers can be NULL, if the caller is not interested in a particular ID. </p>
<p> Be aware that for clients that a compositor forks and execs and then connects using socketpair(), this function will return the credentials for the compositor. The credentials for the socketpair are set at creation time in the compositor.</p>
<h3>struct <code>wl_display</code> * wl_client_get_display (struct <code>wl_client</code> *client)</h3>
<p>Get the display object for the given client </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>client</i> The client object</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The display object the client is associated with.</dl>
<h3>struct <code>wl_resource</code> * wl_client_get_object (struct <code>wl_client</code> *client, uint32_tid)</h3>
<p>Look up an object in the client name space </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>client</i> The client object<br />
 <i>id</i> The object id</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The object or NULL if there is not object for the given ID</dl>
<p> This looks up an object in the client object name space by its object ID.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Wayland from the source code.</p>
