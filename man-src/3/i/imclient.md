---
title: "imclient(3)"
name: "imclient"
section: "3"
letter: "i"
url: "/docs/linux/man/3-imclient/"
description: "imclient library – authenticating callback interface to IMAP/IMSP servers"
---

<p>&nbsp;<wbr>*</p>
<h2 class="name">NAME</h2>
<p> imclient library &#8211; authenticating callback interface to IMAP/IMSP servers </p>
<h2>SYNOPSIS</h2>
<p> <code> #include &lt;cyrus/imclient.h&gt; </p>
<p> </code> </p>
<p> void imclient_close (struct imclient *</code><i>imclient</i><code>);</code> </p>
<p> <code>void imclient_setflags(struct imclient *</code><i>imclient</i><code>, int</code><i>flags</i><code>);</code> </p>
<p> <code>void imclient_clearflags (struct imclient *</code><i>imclient</i><code>, int</code><i>flags</i><code>);</code> </p>
<p> <code>char* imclient_servername (struct imclient *</code><i>imclient</i><code>);</code> </p>
<p> <code>void imclient_addcallback (struct imclient * imclient ,&#8230;);</code> </p>
<p> <code>void imclient_send (struct imclient *</code><i>imclient</i><code>, void (*</code><i>finishproc</i><code>)(), void *</code><i>finishrock</i><code>, const char *</code><i>fmt</i><code>, &#8230;);</code> </p>
<p> <code>void imclient_getselectinfo (struct imclient *</code><i>imclient</i><code>, int *</code><i>fd</i><code>, int * </code><i>wanttowrite</i><code>);</code> </p>
<p> <code>void imclient_processoneevent (struct imclient *</code><i>imclient</i><code>);</code> </p>
<p> <code>int imclient_authenticate (struct imclient *</code><i>imclient</i><code>, struct sasl_client **</code><i>availmech</i><code>, const char *</code><i>service</i><code>, const char *</code><i>user</i><code>, int </code><i>protallowed</i><code>);</code> </p>
<p> <code>int imclient_havetls ();</code> </p>
<p> <code>int imclient_starttls (struct imclient *</code><i>imclient</i><code>, char *</code><i>cert_file</i><code>, char *</code><i>key_file</i><code>, char *</code><i>CAfile</i><code>, char *</code><i>CApath</i><code>);</code> </p>
<h2>DESCRIPTION</h2>
<p> The imclient library functions are distributed with Cyrus IMAP and IMSP. These functions are used for building IMAP/IMSP client software. These functions handle Kerberos authentication and can set callbacks based on the keyword in untagged replies or based on the command tag at the end of command replies. </p>
<p> Users must link with the -lcyrus switch, and must supply a function called <i>fatal</i> to be called in case of any error within <i>libcyrus.a.</i> </p>
<p> All of the <code>imclient</code> functions begin with the prefix <i>imclient</i> and takes an argument of type <code>struct imclient *</code> as the first argument which is initialized by <code>imclient_connect</code> and freed by <code>imclient_close.</code> </p>
<p> See below for a description of each function. </p>
<dl>
<dt><code>imclient_connect()</p>
<dd> Connects the client server to the host. If successful, it returns 0 and sets the imclient argument to a pointer to an imclient </code> struct. The <code>imclient </code> struct represents the current connection, flags, and callbacks. On failure, the current <code>errno</code> is returned if a system call failed, -1 is returned if the host name was not found, and -2 is returned if the service name was not found.</p>
<dt><code>imclient_close()</p>
<dd> Closes and frees the imclient </code> connection.</p>
<dt><code>&nbsp;<wbr>imclient_setflags()</p>
<dd> Sets the flags specified by the flags</code> argument on the <code>imclient</code> connection. Currently the only flag allowed is <code>IMCLIENT_CONN_NONSYNCLITERAL</code> (this flag indicates that the server supports non-synchronizing literals described by the LITERAL+ extension).</p>
<dt><code>imclient_clearflags()</p>
<dd> Clears the flags specified by the flags</code> argument on the <code>imclient</code> connection.</p>
<dt><code>imclient_servername()</p>
<dd> Returns a char * pointer to the name of the server connected to by imclient.</code></p>
<dt><code>imclient_addcallback()</p>
<dd> Adds an untagged data callback to the imclient</code> connection. The function <code>imclient_addcallback</code> takes callbacks of the type <code>imclient_proc_t</code> which is defined to be: typedef void imclient_proc_t (struct imclient *imclient, void *rock, struct imclient_reply *reply); </p>
<p> and <code>struct imclient_reply *</code> is defined to be: </p>
<p> struct imclient_reply {<br />
&nbsp;<wbr>char&nbsp;<wbr>*keyword;<br />
&nbsp;<wbr>long msgno;<br />
&nbsp;<wbr>char&nbsp;<wbr>*text; }; </p>
<p> After the first argument <code>imclient,</code> there can be zero or more instances of the set of <code>keyword,</code> <code>flags,</code> <code>proc,</code> and <code>rock,</code> each adding or changing a single callback. Each instance adds or changes the callback for <code>keyword. </code> The argument, <code>flags,</code> specifies information about the parsing of the untagged data. <code>proc</code> and <code>rock</code> specify the callback function and rock to invoke when the untagged data is received. <code>proc</code> may be a null pointer, in which case no function is invoked. The callback function may not call the functions <code>imclient_close(), imclient_send(), imclient_eof(),</code> <code>imclient_processoneevent(),</code> or <code>imclient_authenticate()</code> on the connection. The callback function may over write the text of untagged data.</p>
<dt><code>imclient_send()</p>
<dd> Sends a new command to the imclient</code> connection. <code>finishproc</code> and <code>finnishrock</code> are the function and rock called when the command completes. <code>functionproc</code> may be a null pointer, in which case no callback is made. The call back function may not call the functions <code>imclient_close(), imclient_send(), imclient_eof(), imclient_processoneevent(), </code> or <code>imclient_authenticate() </code> on the connection. The argument, <code>fmt</code> , is a print like specification of the command. It must not include the tag as the tag is automatically added by imclient_send(). The defined %-sequences are: </p>
<p> <code>%%</code> for % </p>
<p> <code>%a</code> for an IMAP atom </p>
<p> <code>%s</code> for an astring (which will be quoted or literalized as needed) </p>
<p> <code>%d</code> for a decimal </p>
<p> <code>%u</code> for an unsigned decimal </p>
<p> <code>%v</code> for #astring (argument is a null-terminated array of <code>char *</code> which are written as space separated astrings)</p>
<dt><code>imclient_getselectinfo()</p>
<dd> Gets the information for calling <a href="/docs/linux/man/2-select/">select</a>(2).</code> <code>fd</code> is filled in with the file descriptor to <code><a href="/docs/linux/man/2-select/">select</a>(2)</code> for read. <code>wanttowrite</code> is filled in with a nonzero value if select should be used for write as well.</p>
<dt><code>imclient_processoneevent()</p>
<dd> Processes one input or output event on the imclient</code> connection.</p>
<dt><code>imclient_authenticate()</p>
<dd> Authenticates the imclient </code> connection using one of the mechanisms in <code>availmech.</code> The argument, <code>user,</code> if not NULL, specifies the user to authenticate as. If the user is NULL, the current user is used. The argument <code>protallowed</code> is a bitmask of permissible protection mechanisms. </p>
<p> On success, 0 is returned. On failure (i.e., &quot;BAD&quot; keyboard, or no authentication mechanisms worked), 1 is returned. On extreme failure (premature &quot;OK&quot;), 2 is returned.</p>
<dt><code>imclient_havetls()</p>
<dd> Returns a Boolean indicating whether the imclient</code> library was compiled with TLS (SSL) support. If so, <code>imclient_starttls()</code> may be used to secure the IMAP connection.</p>
<dt><code>imclient_starttls()</p>
<dd> Issues a STARTTLS command on an existing IMAP connection and negotiates the secure link. The cert_file</code> and <code>key_file</code> arguments specify the client certificate and secret key to use to authenticate ourselves to the server. If client authentication is not needed, set both of these arguments to NULL. </p>
<p> The <code>CAfile</code> and <code>CApath</code> arguments specify a file or directory, respectively, of CA certificates for validating server certificates. (See <code><a href="/docs/linux/man/3-ssl_ctx_load_verify_locations/">SSL_CTX_load_verify_locations</a>(3)</code> for details.) If both of these are NULL, the client will be unable to validate the server&#8217;s certificate, in which case the connection may succeed but a warning will be printed to stdout. </p>
</dl>
<h2>EXAMPLES</h2>
<p> The following code is a possible skeletion of <code>imclient</code> that relies on Kerberos to do authentication. This code preforms an IMAP CAPABILITY request and prints out the result. </p>
<pre><code>
struct sasl_client;
#include &lt;cyrus/imclient.h&gt;
#include &lt;cyrus/sasl.h&gt;
#include &lt;cyrus/xmalloc.h&gt; /* example uses xstrdup */
#include &lt;stdio.h&gt;
extern struct sasl_client krb_sasl_client;
struct sasl_client *login_sasl_client[] = {
    &amp;krb_sasl_client,
    NULL};
struct imclient *imclient;
char server[] = "cyrus.andrew.cmu.edu";
char port[] = "imap";
void fatal(char *message, int rc)
{
    fprintf(stderr, "fatal error: %s
", message);
    exit(rc);
}
static void callback_capability(struct imclient *imclient,
                                void *rock,
                                struct imclient_reply *reply)
{
    if (reply-&gt;text != NULL) {
        *((char **)rock) = xstrdup(reply-&gt;text);
    }
}
static void end_command(struct imclient *connection, void *rock, struct imclient_reply *inmsg)
{
    (*(int *)rock)--;
}
main()
{
    char *capability_string;
    int nc;

    if (imclient_connect(&amp;imclient, server, port)) {
        fprintf(stderr,
                "error: Couldn't connect to %s %s
",
                server, port);
        exit(1);
    }
    if (imclient_authenticate(imclient, login_sasl_client, "imap"
                              /* service */,
                              NULL /* user */, SASL_PROT_ANY)) {
        exit(1);
    }
    imclient_addcallback(imclient, "CAPABILITY",
                         CALLBACK_NOLITERAL,
                         callback_capability,
                         &amp;capability_string,
                         NULL);

    nc = 1;

    imclient_send(imclient, end_command,
                  (void *)&amp;nc, "CAPABILITY");

    while (nc &gt; 0) {
        imclient_processoneevent(imclient);
    }

    if (strstr("LITERAL+", capability_string)) {
        imclient_setflags(imclient, IMCLIENT_CONN_NONSYNCLITERAL);
    }
    imclient_send(imclient, NULL, NULL, "LOGOUT");
    imclient_close(imclient);
    printf("capability text is: %s
", capability_string);
    free(capability_string);
}
</code></pre>
<h2>BUGS</h2>
<p> No known bugs. </p>
<h2>SEE ALSO</h2>
<p> <code>cyradm, imapd, imspd,</code> RFC2033 (IMAP LITERAL+ extension), RFC2060 (IMAP4rev1 specification), and <code><a href="/docs/linux/man/2-select/">select</a>(2)</code> </p>
<h2>KEYWORDS</h2>
<p> IMAP, ACAP, IMSP, Kerberos, Authentication </p>
<h2>Index</h2>
