---
title: "auparse_add_callback(3)"
name: "auparse_add_callback"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_add_callback/"
description: "auparse_add_callback – add a callback handler for notifications"
---

<h2>NAME</h2>
<p> auparse_add_callback &#8211; add a callback handler for notifications</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<pre><code>
void auparse_add_callback(auparse_state_t *au, auparse_callback_ptr callback,
                          void *user_data, user_destroy user_destroy_func);
</code></pre>
<h2>DESCRIPTION</h2>
<p> auparse_add_callback adds a callback function to the parse state which is invoked to notify the application of parsing events. This is part of the event feed API. </p>
<p> The signature of the callback is: </p>
<p>void auparse_callback(auparse_state_t *au, auparse_cb_event_t cb_event_type,<br />
                      void *user_data);</p>
<p> When the callback is invoked it is passed: </p>
<dl>
<dt><i>au</i></p>
<dd>
&nbsp;<wbr>a pointer to the parse_state</p>
<dt><i>cb_event_type</i></p>
<dd> enumerated value indicating the reason why the callback was invoked</p>
<dt><i>user_data</i></p>
<dd> pointer to user supplied private data. May be NULL.</p>
<dt><i>user_destroy_func</i></p>
<dd> pointer to function called when user_data is destroyed. May be NULL. The signature is: </p>
<pre><code>
void destroy(void *user_data);
</code></pre>
<p> The destroy() function should be prepared to accept user_data possibly being NULL.</dl>
<p> The <i>cb_event_type</i> argument indicates why the callback was invoked. It&#8217;s possible values are: </p>
<dl>
<dt><code>AUPARSE_CB_EVENT_READY</code></p>
<dd> A complete event has been parsed and is ready to be examined. This is logically equivalent to the parse state immediately following <i>auparse_next_event()</i></dl>
<p> See <a href="/docs/linux/man/3-auparse_feed/">auparse_feed</a>(3) for a complete code example.</p>
<h2>RETURN VALUE</h2>
<p> Returns the previous callback pointer. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_feed/">auparse_feed</a></code>(3), <code><a href="/docs/linux/man/3-auparse_flush_feed/">auparse_flush_feed</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> John Dennis </p>
<h2>Index</h2>
