---
title: "ne_get_server_hostport(3)"
name: "ne_get_server_hostport"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_get_server_hostport/"
description: "ne_set_useragent, ne_set_read_timeout, ne_set_connect_timeout, ne_get_scheme, ne_get_server_hostport – common properties for HTTP sessions"
---

<p>ne_set_useragent, ne_set_read_timeout, ne_set_connect_timeout, ne_get_scheme, ne_get_server_hostport &#8211; common properties for HTTP sessions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_session.h&gt;

void ne_set_useragent(ne_session *session, const char *product);

void ne_set_read_timeout(ne_session *session, int timeout);

void ne_set_connect_timeout(ne_session *session, int timeout);

const char *ne_get_scheme(ne_sesssion *session);

const char *ne_get_server_hostport(ne_sesssion *session);</code></pre>
<h2>Description</h2>
<dd>The User-Agent request header is used to identify the software which generated the request for statistical or debugging purposes. neon does not send a User-Agent header unless a call is made to the <code>ne_set_useragent</code>. <code>ne_set_useragent</code> must be passed a product string conforming to RFC2616&#8217;s product token grammar; of the form &quot;Product/Version&quot;. </p>
<p> When neon reads from a socket, by default the read operation will time out after 60 seconds, and the request will fail giving an <code>NE_TIMEOUT</code> error. To configure this timeout interval, call <code>ne_set_read_timeout</code> giving the desired number of seconds as the <i>timeout</i> parameter. </p>
<p> When a connection is being established to a server, normally only the system&#8217;s TCP timeout handling will apply. To configure a specific (and probably shorter) timeout, the <code>ne_set_connect_timeout</code> can be used, giving the desired number of seconds as the <i>timeout</i> parameter. If 0 is passed, then the default behaviour of using the system TCP timeout will be used. </p>
<p> The scheme used to initially create the session will be returned by <code>ne_get_scheme</code>. </p>
<p> The hostport pair with which the session is associated will be returned by the <code>ne_get_server_hostport</code>; for example <a rel="nofollow" href="http://www.example.com">www.example.com</a>:8080. Note that the :port will be omitted if the default port for the scheme is used.</p>
<h2>Examples</h2>
<p>Set a user-agent string: ne_session *sess = ne_session_create(&#8230;);<br />
ne_set_read_timeout(sess, 30); Set a 30 second read timeout: </p>
<pre><code>ne_session *sess = ne_session_create(...);
ne_set_read_timeout(sess, 30);</code></pre>
<h2>See Also</h2>
<p>ne_session_create, ne_set_session_flag.</p>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
