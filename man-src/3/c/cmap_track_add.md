---
title: "cmap_track_add(3)"
name: "cmap_track_add"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmap_track_add/"
description: "cmap_track_add – Set tracking function for values in CMAP"
---

<h2 class="name">NAME</h2>
<p> cmap_track_add &#8211; Set tracking function for values in CMAP</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;corosync/cmap.h&gt;</code> </p>
<p> <code>cs_error_t cmap_track_add (cmap_handle_t </code><i>handle</i><code>, const char *</code><i>key_name</i><code>, int32_t </code><i>track_type</i><code>, cmap_notify_fn_t </code><i>notify_fn</i><code>, void *</code><i>user_data</i><code>, cmap_track_handle_t *</code><i>cmap_track_handle</i><code>);</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>cmap_track_add</code> function is used to set function which tracks changes in CMAP. One CMAP connection can track multiple keys and also it&#8217;s possible to track one key multiple times. The <i>handle</i> argument is connection to CMAP database obtained by calling <code><a href="/docs/linux/man/3-cmap_initialize/">cmap_initialize</a>(3)</code> function. <i>key_name</i> argument is ether exact key name or prefix of key name to track changes on. <i>track_type</i> is bitfield which may consist of following values: </p>
<p> <code>CMAP_TRACK_ADD</code> &#8211; track addition of new key (or key added in callback) </p>
<p> <code>CMAP_TRACK_DELETE</code> &#8211; track deletion of key (or key deleted in callback) </p>
<p> <code>CMAP_TRACK_MODIFY</code> &#8211; track modification of key (or key modified in callback) </p>
<p> <code>CMAP_TRACK_PREFIX</code> &#8211; whole prefix is tracked, instead of key only, so &quot;totem.&quot; tracking means that &quot;totem.nodeid&quot;, &quot;totem.version&quot;, &#8230; applies (this value is never returned in callback) </p>
<p> <i>notify_fn</i> is pointer to function which is called when value is changed. It&#8217;s definition and meaning of parameters is discussed below. <i>user_data</i> argument is passed directly to <i>notify_fn</i> without any changes. <i>cmap_track_handle</i> is used for removing of tracking when no longer needed by calling <code><a href="/docs/linux/man/3-cmap_track_delete/">cmap_track_delete</a>(3)</code> function. </p>
<p> Callback function is defined as:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre><code>
typedef void (*cmap_notify_fn_t)(
    cmap_handle_t cmap_handle,
    cmap_track_handle_t cmap_track_handle,
    int32_t event,
    const char *key_name,
    struct cmap_notify_value new_value,
    struct cmap_notify_value old_value,
    void *user_data);
</code></pre>
</dl>
<dt>
<dd></dl>
<p> where <i>cmap_handle</i> is handle used in registration of track function. <i>cmap_track_handle</i> is handle returned by <code>cmap_track_add</code> function. <i>event</i> is one of <code>CMAP_TRACK_ADD</code>, <code>CMAP_TRACK_DELETE</code> or <code>CMAP_TRACK_MODIFY</code>. <i>key_name</i> is name of changed key. <i>new_value</i> is new value of key, or unset if <i>event</i> is <code>CMAP_TRACK_DELETE</code>. <i>old_value</i> is previous value of key or unset if <i>event</i> is <code>CMAP_TRACK_ADD</code> or for some special keys set directly by Corosync due to speed optimalizations. Both <i>new_value</i> and <i>old_value</i> are structures defined as:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre><code>
struct cmap_notify_value {
    cmap_value_types_t type;
    size_t len;
    const void *data;
};
</code></pre>
</dl>
<dt>
<dd></dl>
<p> If value is unset, all fields are set to 0. Otherwise <i>type</i> is one of cmap types (as described in <code><a href="/docs/linux/man/3-cmap_get/">cmap_get</a>(3)</code> function), <i>len</i> is length of value in cmap and <i>data</i> is pointer to value of item. Data storage is dynamically allocated by caller and notify function must not try to free it. </p>
<h2>RETURN VALUE</h2>
<p> This call returns the CS_OK value if successful. It can return CS_ERR_INVALID_PARAM if notify_fn is NULL or track_type is invalid value. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cmap_track_delete/">cmap_track_delete</a></code>(3), <code><a href="/docs/linux/man/3-cmap_initialize/">cmap_initialize</a></code>(3), <code><a href="/docs/linux/man/3-cmap_get/">cmap_get</a></code>(3), <code><a href="/docs/linux/man/3-cmap_dispatch/">cmap_dispatch</a></code>(3), <code><a href="/docs/linux/man/8-cmap_overview/">cmap_overview</a></code>(8) </p>
<p> <code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable </p>
<p> <code>CS_ERR_INVALID_PARAM</code> Invalid argument </p>
<p> <code>CS_ERR_ACCESS</code> Permission denied </p>
<p> <code>CS_ERR_LIBRARY</code> The connection failed </p>
<p> <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal </p>
<p> <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported </p>
<p> <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received </p>
<p> <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
<h2>Index</h2>
