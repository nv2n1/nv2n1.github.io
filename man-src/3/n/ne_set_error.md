---
title: "ne_set_error(3)"
name: "ne_set_error"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_set_error/"
description: "ne_get_error, ne_set_error – error handling for HTTP sessions"
---

<p>ne_get_error, ne_set_error &#8211; error handling for HTTP sessions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_session.h&gt;

const char *ne_get_error(ne_sesssion *session);

void ne_set_error(ne_sesssion *session, const char *format, ...);</code></pre>
<h2>Description</h2>
<dd>The session error string is used to store any human-readable error information associated with any errors which occur whilst using the HTTP session. </p>
<p> The <code>ne_get_error</code> function returns the current session error string. This string persists only until it is changed by a subsequent operation on the session. If localisation was enabled at build time, and if necessary enabled at run-time if necessary using ne_i18n_init, the returned string may have been translated into the user&#8217;s current locale. </p>
<p> The <code>ne_set_error</code> function can be used to set a new session error string, using a <code>printf</code>-style format string interface.</p>
<h2>Return Value</h2>
<p><code>ne_set_error</code> returns a constant NUL-terminated string. In the default English locale, the returned string will <i>not</i> have a terminating &#8220;.&#8221; period character.</p>
<h2>Examples</h2>
<p>Retrieve the current error string: ne_session *sess = ne_session_create(&#8230;);<br />
&#8230;<br />
ne_set_error(sess, &quot;Response missing header %s&quot;, &quot;somestring&quot;); Set a new error string: </p>
<pre><code>ne_session *sess = ne_session_create(...);
...
ne_set_error(sess, &quot;Response missing header %s&quot;, &quot;somestring&quot;);</code></pre>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
