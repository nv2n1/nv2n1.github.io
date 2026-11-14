---
title: "catgets(3)"
name: "catgets"
section: "3"
letter: "c"
url: "/docs/linux/man/3-catgets/"
description: "catgets – get message from a message catalog"
---

<h2 class="name">NAME</h2>
<p> catgets &#8211; get message from a message catalog </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;nl_types.h&gt;
char *catgets(nl_catd catalog, int set_number, int message_number,
              const char *message);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>catgets</code>() reads the message <i>message_number</i>, in set <i>set_number</i>, from the message catalog identified by <i>catalog</i>, where <i>catalog</i> is a catalog descriptor returned from an earlier call to <code><a href="/docs/linux/man/3-catopen/">catopen</a></code>(3). The fourth argument, <i>message</i>, points to a default message string which will be returned by <code>catgets</code>() if the identified message catalog is not currently available. The message-text is contained in an internal buffer area and should be copied by the application if it is to be saved or modified. The return string is always terminated with a null byte (&#8216;
