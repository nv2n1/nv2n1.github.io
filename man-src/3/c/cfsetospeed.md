---
title: "cfsetospeed(3)"
name: "cfsetospeed"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cfsetospeed/"
description: "termios, tcgetattr, tcsetattr, tcsendbreak, tcdrain, tcflush, tcflow, cfmakeraw, cfgetospeed, cfgetispeed, cfsetispeed, cfsetospeed, cfsetspeed – get and set terminal attributes, line control, get ..."
---

<h2 class="name">NAME</h2>
<p> termios, tcgetattr, tcsetattr, tcsendbreak, tcdrain, tcflush, tcflow, cfmakeraw, cfgetospeed, cfgetispeed, cfsetispeed, cfsetospeed, cfsetspeed &#8211; get and set terminal attributes, line control, get and set baud rate </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;termios.h&gt;
#include &lt;unistd.h&gt;
int tcgetattr(int fd, struct termios *termios_p);
int tcsetattr(int fd, int optional_actions,
              const struct termios *termios_p);
int tcsendbreak(int fd, int duration);
int tcdrain(int fd);
int tcflush(int fd, int queue_selector);
int tcflow(int fd, int action);
void cfmakeraw(struct termios *termios_p);
speed_t cfgetispeed(const struct termios *termios_p);
speed_t cfgetospeed(const struct termios *termios_p);
int cfsetispeed(struct termios *termios_p, speed_t speed);
int cfsetospeed(struct termios *termios_p, speed_t speed);
int cfsetspeed(struct termios *termios_p, speed_t speed);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>cfsetspeed</code>(), <code>cfmakeraw</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> The termios functions describe a general terminal interface that is provided to control asynchronous communications ports.</p>
<h3>The termios structure</h3>
<p> Many of the functions described here have a <i>termios_p</i> argument that is a pointer to a <i>termios</i> structure. This structure contains at least the following members: </p>
<p> tcflag_t c_iflag; /* input modes */ tcflag_t c_oflag; /* output modes */ tcflag_t c_cflag; /* control modes */ tcflag_t c_lflag; /* local modes */ cc_t c_cc[NCCS]; /* special characters */ </p>
<p> The values that may be assigned to these fields are described below. In the case of the first four bit-mask fields, the definitions of some of the associated flags that may be set are exposed only if a specific feature test macro (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)) is defined, as noted in brackets (&quot;[]&quot;). </p>
<p> In the descriptions below, &quot;not in POSIX&quot; means that the value is not specified in POSIX.1-2001, and &quot;XSI&quot; means that the value is specified in POSIX.1-2001 as part of the XSI extension. </p>
<p> <i>c_iflag</i> flag constants:</p>
<dl>
<dt><code>IGNBRK</code></p>
<dd> Ignore BREAK condition on input.</p>
<dt><code>BRKINT</code></p>
<dd> If <code>IGNBRK</code> is set, a BREAK is ignored. If it is not set but <code>BRKINT</code> is set, then a BREAK causes the input and output queues to be flushed, and if the terminal is the controlling terminal of a foreground process group, it will cause a <code>SIGINT</code> to be sent to this foreground process group. When neither <code>IGNBRK</code> nor <code>BRKINT</code> are set, a BREAK reads as a null byte (&#8216;
