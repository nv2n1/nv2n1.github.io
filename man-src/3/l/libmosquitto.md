---
title: "libmosquitto(3)"
name: "libmosquitto"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libmosquitto/"
description: "libmosquitto – MQTT version 3.1 client library"
---

<h2 class="name">NAME</h2>
<p> libmosquitto &#8211; MQTT version 3.1 client library </p>
<h2>DESCRIPTION</h2>
<p> This is an overview of how to use libmosquitto to create MQTT aware client programs. There may be separate man pages on each of the functions described here in the future. There is also a binding for libmosquitto for C++ and a Python implementation. They are not documented here but operate in a similar way. </p>
<p> This is fairly incomplete, please see mosquitto.h for a better description of the functions.</p>
<h2>LIBMOSQUITTO SYMBOL NAMES</h2>
<p> All public functions in libmosquitto have the prefix &quot;mosquitto_&quot;. Any other functions defined in the source code are to be treated as private functions and may change between any release. Do not use these functions!</p>
<h2>FUNCTIONS</h2>
<h3>Library version</h3>
<dl>
<dt> <code>int mosquitto_lib_version(int&nbsp;<wbr>*</code><i>major</i><code>, int&nbsp;<wbr>*</code><i>minor</i><code>, int&nbsp;<wbr>*</code><i>revision</i><code>);</code></dl>
<dd>Obtain version information about the library. If any of major, minor or revision are not NULL they will return the corresponding version numbers. The return value is an integer representation of the complete version number (e.g. 1009001 for 1.9.1) that can be used for comparisons.</p>
<h3>Library initialisation and cleanup</h3>
<dl>
<dt> <code>int mosquitto_lib_init(void);</code></p>
<dt> <code>int mosquitto_lib_cleanup(void);</code></dl>
<dd>Call mosquitto_lib_init() before using any of the other library functions and mosquitto_lib_cleanup() after finishing with the library.</p>
<h3>Client constructor/destructor</h3>
<dl>
<dt> <code>struct mosquitto *mosquitto_new(const char&nbsp;<wbr>*</code><i>id</i><code>, bool&nbsp;<wbr></code><i>clean_session</i><code>, void&nbsp;<wbr>*</code><i>userdata</i><code>);</code></dl>
<dd>Create a new mosquitto client instance.</p>
<dl>
<dt> <code>void mosquitto_destroy(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>);</code></dl>
<dd>Use to free memory associated with a mosquitto client instance.</p>
<dl>
<dt> <code>int mosquitto_reinitialise(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>, const char&nbsp;<wbr>*</code><i>id</i><code>, bool&nbsp;<wbr></code><i>clean_session</i><code>, void&nbsp;<wbr>*</code><i>userdata</i><code>);</code></dl>
<h3>Authentication and encryption</h3>
<dl>
<dt> <code>int mosquitto_username_pw_set(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>, const char&nbsp;<wbr>*</code><i>username</i><code>, const char&nbsp;<wbr>*</code><i>password</i><code>);</code></p>
<dt> <code>int mosquitto_tls_set(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>, const char&nbsp;<wbr>*</code><i>cafile</i><code>, const char&nbsp;<wbr>*</code><i>capath</i><code>, const char&nbsp;<wbr>*</code><i>certfile</i><code>, const char&nbsp;<wbr>*</code><i>keyfile</i><code>, int&nbsp;<wbr></code><i>(*pw_callback)(char&nbsp;<wbr>*buf, int size, int rwflag, void&nbsp;<wbr>*userdata)</i><code>);</code></p>
<dt> <code>int mosquitto_tls_opts_set(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>, int&nbsp;<wbr></code><i>cert_reqs</i><code>, const char&nbsp;<wbr>*</code><i>tls_version</i><code>, const char&nbsp;<wbr>*</code><i>ciphers</i><code>);</code></p>
<dt> <code>int mosquitto_tls_insecure_set(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>, bool&nbsp;<wbr></code><i>value</i><code>);</code></p>
<dt> <code>int mosquitto_tls_psk_set(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>, const char&nbsp;<wbr>*</code><i>psk</i><code>, const char&nbsp;<wbr>*</code><i>identity</i><code>, const char&nbsp;<wbr>*</code><i>ciphers</i><code>);</code></dl>
<h3>Wills</h3>
<dl>
<dt> <code>int mosquitto_will_set(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>, const char&nbsp;<wbr>*</code><i>topic</i><code>, int&nbsp;<wbr></code><i>payloadlen</i><code>, const void&nbsp;<wbr>*</code><i>payload</i><code>, int&nbsp;<wbr></code><i>qos</i><code>, bool&nbsp;<wbr></code><i>retain</i><code>);</code></p>
<dt> <code>int mosquitto_will_clear(</code><i>struct mosquitto&nbsp;<wbr>*mosq</i><code>);</code></dl>
<h3>Connect/disconnect</h3>
<dl>
<dt> <code>int mosquitto_connect(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>, const char&nbsp;<wbr>*</code><i>host</i><code>, int&nbsp;<wbr></code><i>port</i><code>, int&nbsp;<wbr></code><i>keepalive</i><code>);</code></p>
<dt> <code>int mosquitto_connect_bind(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>, const char&nbsp;<wbr>*</code><i>host</i><code>, int&nbsp;<wbr></code><i>port</i><code>, int&nbsp;<wbr></code><i>keepalive</i><code>, const char&nbsp;<wbr>*</code><i>bind_address</i><code>);</code></p>
<dt> <code>int mosquitto_connect_async(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>, const char&nbsp;<wbr>*</code><i>host</i><code>, int&nbsp;<wbr></code><i>port</i><code>, int&nbsp;<wbr></code><i>keepalive</i><code>);</code></p>
<dt> <code>int mosquitto_connect_bind_async(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>, const char&nbsp;<wbr>*</code><i>host</i><code>, int&nbsp;<wbr></code><i>port</i><code>, int&nbsp;<wbr></code><i>keepalive</i><code>, const char&nbsp;<wbr>*</code><i>bind_address</i><code>);</code></p>
<dt> <code>int mosquitto_reconnect(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>);</code></p>
<dt> <code>int mosquitto_reconnect_async(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>);</code></p>
<dt> <code>int mosquitto_disconnect(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>);</code></dl>
<h3>Publish</h3>
<dl>
<dt> <code>int mosquitto_publish(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>, int&nbsp;<wbr>*</code><i>mid</i><code>, const char&nbsp;<wbr>*</code><i>topic</i><code>, int&nbsp;<wbr></code><i>payloadlen</i><code>, const void&nbsp;<wbr>*</code><i>payload</i><code>, int&nbsp;<wbr></code><i>qos</i><code>, bool&nbsp;<wbr></code><i>retain</i><code>);</code></dl>
<h3>Subscribe/unsubscribe</h3>
<dl>
<dt> <code>int mosquitto_subscribe(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>, int&nbsp;<wbr>*</code><i>mid</i><code>, const char&nbsp;<wbr>*</code><i>sub</i><code>, int&nbsp;<wbr></code><i>qos</i><code>);</code></p>
<dt> <code>int mosquitto_unsubscribe(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>, int&nbsp;<wbr>*</code><i>mid</i><code>, const char&nbsp;<wbr>*</code><i>sub</i><code>);</code></dl>
<h3>Network loop</h3>
<dl>
<dt> <code>int mosquitto_loop(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>, int&nbsp;<wbr></code><i>timeout</i><code>, int&nbsp;<wbr></code><i>max_packets</i><code>);</code></p>
<dt> <code>int mosquitto_loop_read(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>, int&nbsp;<wbr></code><i>max_packets</i><code>);</code></p>
<dt> <code>int mosquitto_loop_write(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>, int&nbsp;<wbr></code><i>max_packets</i><code>);</code></p>
<dt> <code>int mosquitto_loop_misc(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>);</code></p>
<dt> <code>int mosquitto_loop_forever(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>, int&nbsp;<wbr></code><i>timeout</i><code>, int&nbsp;<wbr></code><i>max_packets</i><code>);</code></p>
<dt> <code>int mosquitto_socket(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>);</code></p>
<dt> <code>bool mosquitto_want_write(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>);</code></dl>
<h3>Threaded network loop</h3>
<dl>
<dt> <code>int mosquitto_loop_start(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>);</code></p>
<dt> <code>int mosquitto_loop_stop(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>, bool&nbsp;<wbr></code><i>force</i><code>);</code></dl>
<h3>Misc client functions</h3>
<dl>
<dt> <code>int mosquitto_max_inflight_messages_set(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>, unsigned int&nbsp;<wbr></code><i>max_inflight_messages</i><code>);</code></p>
<dt> <code>int mosquitto_message_retry_set(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>, unsigned int&nbsp;<wbr></code><i>message_retry</i><code>);</code></p>
<dt> <code>int mosquitto_reconnect_delay_set(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>, unsigned int&nbsp;<wbr></code><i>reconnect_delay</i><code>, unsigned int&nbsp;<wbr></code><i>reconnect_delay_max</i><code>, bool&nbsp;<wbr></code><i>reconnect_exponential_backoff</i><code>);</code></p>
<dt> <code>int mosquitto_user_data_set(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>, void&nbsp;<wbr>*</code><i>userdata</i><code>);</code></dl>
<h3>Callbacks</h3>
<dl>
<dt> <code>int mosquitto_connect_callback_set(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>, void&nbsp;<wbr></code><i>(*on_connect)(struct mosquitto&nbsp;<wbr>*, void&nbsp;<wbr>*, int)</i><code>);</code></p>
<dt> <code>int mosquitto_disconnect_callback_set(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>, void&nbsp;<wbr></code><i>(*on_disconnect)(struct mosquitto&nbsp;<wbr>*, void&nbsp;<wbr>*, int)</i><code>);</code></p>
<dt> <code>int mosquitto_publish_callback_set(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>, void&nbsp;<wbr></code><i>(*on_publish)(struct mosquitto&nbsp;<wbr>*, void&nbsp;<wbr>*, int)</i><code>);</code></p>
<dt> <code>int mosquitto_message_callback_set(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>, void&nbsp;<wbr></code><i>(*on_message)(struct mosquitto&nbsp;<wbr>*, void&nbsp;<wbr>*, const struct mosquitto_message&nbsp;<wbr>*)</i><code>);</code></p>
<dt> <code>int mosquitto_subscribe_callback_set(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>, void&nbsp;<wbr></code><i>(*on_subscribe)(struct mosquitto&nbsp;<wbr>*, void&nbsp;<wbr>*, int, int, const int&nbsp;<wbr>*)</i><code>);</code></p>
<dt> <code>int mosquitto_unsubscribe_callback_set(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>, void&nbsp;<wbr></code><i>(*on_unsubscribe)(struct mosquitto&nbsp;<wbr>*, void&nbsp;<wbr>*, int)</i><code>);</code></p>
<dt> <code>int mosquitto_log_callback_set(struct mosquitto&nbsp;<wbr>*</code><i>mosq</i><code>, void&nbsp;<wbr></code><i>(*on_unsubscribe)(struct mosquitto&nbsp;<wbr>*, void&nbsp;<wbr>*, int, const char&nbsp;<wbr>*)</i><code>);</code></dl>
<h3>Utility functions</h3>
<dl>
<dt> <code>const char *mosquitto_connack_string(int&nbsp;<wbr></code><i>connack_code</i><code>);</code></p>
<dt> <code>int mosquitto_message_copy(struct mosquitto_message&nbsp;<wbr>*</code><i>dst</i><code>, const struct mosquitto_message&nbsp;<wbr>*</code><i>src</i><code>);</code></p>
<dt> <code>int mosquitto_message_free(struct mosquitto_message&nbsp;<wbr>**</code><i>message</i><code>);</code></p>
<dt> <code>const char *mosquitto_strerror(int&nbsp;<wbr></code><i>mosq_errno</i><code>);</code></p>
<dt> <code>int mosquitto_sub_topic_tokenise(const char&nbsp;<wbr>*</code><i>subtopic</i><code>, char&nbsp;<wbr>***</code><i>topics</i><code>, int&nbsp;<wbr>*</code><i>count</i><code>);</code></p>
<dt> <code>int mosquitto_sub_topic_tokens_free(char&nbsp;<wbr>***</code><i>topics</i><code>, int&nbsp;<wbr></code><i>count</i><code>);</code></p>
<dt> <code>int mosquitto_topic_matches_sub(const char&nbsp;<wbr>*</code><i>sub</i><code>, const char&nbsp;<wbr>*</code><i>topic</i><code>, bool&nbsp;<wbr>*</code><i>result</i><code>);</code></dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre><code>
#include &lt;mosquitto.h&gt;
#include &lt;stdio.h&gt;
void my_message_callback(struct mosquitto *mosq, void *userdata, const struct mosquitto_message *message)
{
    if (message-&gt;payloadlen) {
        printf("%s %s
", message-&gt;topic, message-&gt;payload);
    } else {
        printf("%s (null)
", message-&gt;topic);
    }
    fflush(stdout);
}
void my_connect_callback(struct mosquitto *mosq, void *userdata, int result)
{
    int i;
    if (!result) {
        /* Subscribe to broker information topics on successful connect. */
        mosquitto_subscribe(mosq, NULL, "$SYS/#", 2);
    } else {
        fprintf(stderr, "Connect failed
");
    }
}
void my_subscribe_callback(struct mosquitto *mosq, void *userdata, int mid, int qos_count, const int *granted_qos)
{
    int i;
    printf("Subscribed (mid: %d): %d", mid, granted_qos[0]);
    for (i = 1; i &lt; qos_count; i++) {
        printf(", %d", granted_qos[i]);
    }
    printf("
");
}
void my_log_callback(struct mosquitto *mosq, void *userdata, int level, const char *str)
{
    /* Pring all log messages regardless of level. */
    printf("%s
", str);
}
int main(int argc, char *argv[])
{
    int i;
    char *host = "localhost";
    int port = 1883;
    int keepalive = 60;
    bool clean_session = true;
    struct mosquitto *mosq = NULL;
    mosquitto_lib_init();
    mosq = mosquitto_new(NULL, clean_session, NULL);
    if (!mosq) {
        fprintf(stderr, "Error: Out of memory.
");
        return 1;
    }
    mosquitto_log_callback_set(mosq, my_log_callback);
    mosquitto_connect_callback_set(mosq, my_connect_callback);
    mosquitto_message_callback_set(mosq, my_message_callback);
    mosquitto_subscribe_callback_set(mosq, my_subscribe_callback);
    if (mosquitto_connect(mosq, host, port, keepalive)) {
        fprintf(stderr, "Unable to connect.
");
        return 1;
    }
    mosquitto_loop_forever(mosq, -1, 1);
    mosquitto_destroy(mosq);
    mosquitto_lib_cleanup();
    return 0;
}
</code></pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-mosquitto/">mosquitto</a></code>(8)<code><a href="/docs/linux/man/7-mqtt/">mqtt</a></code>(7)</p>
<h2>AUTHOR</h2>
<p> Roger Light &lt;roger [at] atchoo.org&gt; </p>
<h2>Index</h2>
