---
title: "pam_conv(3)"
name: "pam_conv"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pam_conv/"
description: "pam_conv – PAM conversation function"
---

<p>pam_conv &#8211; PAM conversation function</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;security/pam_appl.h&gt;
struct pam_message {
    int msg_style;
    const char *msg;
};

struct pam_response {
    char *resp;
    int resp_retcode;
};

struct pam_conv {
    int (*conv)(int num_msg, const struct pam_message **msg,
                struct pam_response **resp, void *appdata_ptr);
    void *appdata_ptr;
};</code></pre>
<h2>Description</h2>
<p>The PAM library uses an application-defined callback to allow a direct communication between a loaded module and the application. This callback is specified by the <i>struct pam_conv</i> passed to <code><a href="/docs/linux/man/3-pam_start/">pam_start</a></code>(3) at the start of the transaction. </p>
<p> When a module calls the referenced conv() function, the argument <i>appdata_ptr</i> is set to the second element of this structure. </p>
<p> The other arguments of a call to conv() concern the information exchanged by module and application. That is to say, <i>num_msg</i> holds the length of the array of pointers, <i>msg</i>. After a successful return, the pointer <i>resp</i> points to an array of pam_response structures, holding the application supplied text. The <i>resp_retcode</i> member of this struct is unused and should be set to zero. It is the caller&#8217;s responsibility to release both, this array and the responses themselves, using <code><a href="/docs/linux/man/3-free/">free</a></code>(3). Note, <i>*resp</i> is a <i>struct pam_response</i> array and not an array of pointers. </p>
<p> The number of responses is always equal to the <i>num_msg</i> conversation function argument. This does require that the response array is <code><a href="/docs/linux/man/3-free/">free</a></code>(3)&#8217;d after every call to the conversation function. The index of the responses corresponds directly to the prompt index in the pam_message array. </p>
<p> On failure, the conversation function should release any resources it has allocated, and return one of the predefined PAM error codes. </p>
<p> Each message can have one of four types, specified by the <i>msg_style</i> member of <i>struct pam_message</i>: </p>
<p> PAM_PROMPT_ECHO_OFF</p>
<dl>
<dd>Obtain a string without echoing any text.</dl>
<p> PAM_PROMPT_ECHO_ON</p>
<dl>
<dd>Obtain a string whilst echoing text.</dl>
<p> PAM_ERROR_MSG</p>
<dl>
<dd>Display an error message.</dl>
<p> PAM_TEXT_INFO</p>
<dl>
<dd>Display some text.</dl>
<p> The point of having an array of messages is that it becomes possible to pass a number of things to the application in a single call from the module. It can also be convenient for the application that related things come at once: a windows based application can then present a single form with many messages/prompts on at once. </p>
<p> In passing, it is worth noting that there is a descrepency between the way Linux-PAM handles the const struct pam_message **msg conversation function argument from the way that Solaris&#8217; PAM (and derivitives, known to include HP/UX, are there others?) does. Linux-PAM interprets the msg argument as entirely equivalent to the following prototype const struct pam_message *msg[] (which, in spirit, is consistent with the commonly used prototypes for argv argument to the familiar main() function: char **argv; and char *argv[]). Said another way Linux-PAM interprets the msg argument as a pointer to an array of num_msg read only &#8216;struct pam_message&#8217; pointers. Solaris&#8217; PAM implementation interprets this argument as a pointer to a pointer to an array of num_msg pam_message structures. Fortunately, perhaps, for most module/application developers when num_msg has a value of one these two definitions are entirely equivalent. Unfortunately, casually raising this number to two has led to unanticipated compatibility problems. </p>
<p> For what its worth the two known module writer work-arounds for trying to maintain source level compatibility with both PAM implementations are: </p>
<dl>
<dd>&bull; never call the conversation function with num_msg greater than one.</dl>
<dl>
<dd>&bull; set up msg as doubly referenced so both types of conversation function can find the messages. That is, make </p>
<dl>
<dd>
<pre> msg[n] = &amp; (( *msg )[n])</pre>
</dl>
</dl>
<h2>Return Values</h2>
<p>PAM_BUF_ERR</p>
<dl>
<dd>Memory buffer error.</dl>
<p> PAM_CONV_ERR</p>
<dl>
<dd>Conversation failure. The application should not set <i>*resp</i>.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>Success.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pam_start/">pam_start</a></code>(3), <code><a href="/docs/linux/man/3-pam_set_item/">pam_set_item</a></code>(3), <code><a href="/docs/linux/man/3-pam_get_item/">pam_get_item</a></code>(3), <code><a href="/docs/linux/man/3-pam_strerror/">pam_strerror</a></code>(3), <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8) </p>
