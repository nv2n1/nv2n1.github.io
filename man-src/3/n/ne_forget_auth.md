---
title: "ne_forget_auth(3)"
name: "ne_forget_auth"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_forget_auth/"
description: "ne_set_server_auth, ne_set_proxy_auth, ne_forget_auth – register authentication callbacks"
---

<p>ne_set_server_auth, ne_set_proxy_auth, ne_forget_auth &#8211; register authentication callbacks</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_auth.h&gt;

typedef int (*ne_auth_creds)(void *userdata, const char *realm, int attempt, char *username, char *password);

void ne_set_server_auth(ne_session *session, ne_auth_creds callback, void *userdata);

void ne_set_proxy_auth(ne_session *session, ne_auth_creds callback, void *userdata);

void ne_forget_auth(ne_session *session);</code></pre>
<h2>Description</h2>
<dd>The <code>ne_auth_creds</code> function type defines a callback which is invoked when a server or proxy server requires user authentication for a particular request. The <i>realm</i> string is supplied by the server. The <i>attempt</i> is a counter giving the number of times the request has been retried with different authentication credentials. The first time the callback is invoked for a particular request, <i>attempt</i> will be zero. To retry the request using new authentication credentials, the callback should return zero, and the <i>username</i> and <i>password</i> buffers must contain NUL-terminated strings. The NE_ABUFSIZ constant gives the size of these buffers.</p>
<dl>
<dd><font SIZE="+1"> <code>Tip</code> </font><br />
 If you only wish to allow the user one attempt to enter credentials, use the value of the <i>attempt</i> parameter as the return value of the callback.  To abort the request, the callback should return a non-zero value; in which case the contents of the <i>username</i> and <i>password</i> buffers are ignored. The <code>ne_forget_auth</code> function can be used to discard the cached authentication credentials.</p>
<h2>Examples</h2>
<pre><code>/* Function which prompts for a line of user input: */
extern char *prompt_for(const char *prompt);

static int
my_auth(void *userdata, const char *realm, int attempts,
        char *username, char *password)
{
    strncpy(username, prompt_for(&quot;Username: &quot;), NE_ABUFSIZ);
    strncpy(password, prompt_for(&quot;Password: &quot;), NE_ABUFSIZ);
    return attempts;
}

int main(...)
{
    ne_session *sess = ne_session_create(...);

    ne_set_server_auth(sess, my_auth, NULL);

    /* ... */
}</code></pre>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
