---
title: "snmp_alarm_register(3)"
name: "snmp_alarm_register"
section: "3"
letter: "s"
url: "/docs/linux/man/3-snmp_alarm_register/"
description: "snmp_alarm_register, snmp_alarm_register_hr, snmp_alarm_unregister – alarm functions"
---

<p>snmp_alarm_register, snmp_alarm_register_hr, snmp_alarm_unregister &#8211; alarm functions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;net-snmp/utilities.h&gt;
unsigned int

snmp_alarm_register(unsigned int seconds,

                    unsigned int flags,

                    SNMPAlarmCallback *f_callback,

                    void *clientarg);
unsigned int

snmp_alarm_register_hr(struct timeval t,

                       unsigned int flags,

                       SNMPAlarmCallback *f_callback,

                       void *clientarg);
void

snmp_alarm_unregister(unsigned int reg);</code></pre>
<h2>Description</h2>
<p>These functions implement support for a generic timer handling mechanism for multiple parts of an application to register function callbacks to happen at a particular time in the future.</p>
<h2>Usage</h2>
<p>The usage is fairly simple and straight-forward: Simply create a function you want called back at some point in the future. The function definition should be similar to:</p>
<dl>
<dd><code>void my_callback(unsigned int </code><i>reg</i><code>, void *</code><i>clientarg</i><code>);</code></dl>
<p> Then, call <code>snmp_alarm_register()</code> to register your callback to be called <i>seconds</i> from now. The <i>flags</i> field should either be <i>SA_REPEAT</i> or <i>NULL.</i> If flags is set with <i>SA_REPEAT,</i> then the registered callback function will be called every <i>seconds.</i> If <i>flags</i> is <i>NULL</i> then the function will only be called once and then removed from the alarm system registration. </p>
<p> The <i>clientarg</i> parameter in the registration function is used only by the client function and is stored and passed back directly to them on every call to the system. </p>
<p> The <code>snmp_alarm_register()</code> function returns a unique <i>unsigned int</i> (which is also passed as the first argument of each callback), which can then be used to remove the callback from the queue at a later point in the future using the <code>snmp_alarm_unregister()</code> function. If the <code>snmp_alarm_register()</code> call fails it returns zero. In particular, note that it is entirely permissible for an alarm function to unregister itself. </p>
<p> The <code>snmp_alarm_register_hr()</code> function is identical in operation to the <code>snmp_alarm_register()</code> function, but takes a <i>struct timeval</i> as a first parameter, and schedules the callback after the period represented by <i>t</i> (the letters <code>hr</code> stand for &quot;high resolution&quot;). The operation of this function is dependent on the provision of the <code><a href="/docs/linux/man/2-setitimer/">setitimer</a></code>(2) system call by the operating system. If this system call is not available, the alarm will be scheduled as if <code>snmp_alarm_register()</code> had been called with a first argument equal to the value of the <i>tv_sec</i> member of <i>t.</i> See, however, the notes below.</p>
<h2>Initialization</h2>
<p>The <code>init_snmp()</code> function initialises the snmp_alarm subsystem by calling <code>init_snmp_alarm()</code> and then <code>init_alarm_post_config()</code> to set up the first timer to initialise the callback function. These two functions should not be used directly by applications.</p>
<h2>Notes</h2>
<p>The default behaviour of the snmp_alarm subsystem is to request <i>SIGALRM</i> signals from the operating system via the <code><a href="/docs/linux/man/2-alarm/">alarm</a></code>(2) or <code><a href="/docs/linux/man/2-setitimer/">setitimer</a></code>(2) system calls. This has the disadvantage, however, that no other part of the application can use the <i>SIGLARM</i> functionality (or, if some other part of the application <i>does</i> use the <i>SIGALRM</i> functionality, the snmp_alarm subsystem will not work correctly). </p>
<p> If your application runs a <code><a href="/docs/linux/man/2-select/">select</a></code>(2)-based event loop, however, there is no need to use <i>SIGALRM</i> for the snmp_alarm subsystem, leaving it available for other parts of the application. This is done by making the following call: </p>
<pre>netsnmp_ds_set_boolean(NETSNMP_DS_LIBRARY_ID, 
 NETSNMP_DS_LIB_ALARM_DONT_USE_SIG, 1);</pre>
<p>before calling <code>init_snmp().</code> Then, <code>snmp_select_info()</code> takes alarms into account when calculating the timeout value to be used for <code><a href="/docs/linux/man/2-select/">select</a></code>(2). All you need to do is call <code>run_alarms()</code> when <code><a href="/docs/linux/man/2-select/">select</a></code>(2) times out (return value of zero). This is the approach taken in the agent; see <i>snmpd.c.</i> Furthermore, when using this method, high resolution alarms do not depend on the presence of the <code><a href="/docs/linux/man/2-setitimer/">setitimer</a></code>(2) system call, although overall precision is of course still determined by the underlying operating system. Recommended.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-netsnmp_session_api/">netsnmp_session_api</a></code>(3), <code><a href="/docs/linux/man/3-default_store/">default_store</a></code>(3), <code><a href="/docs/linux/man/2-alarm/">alarm</a></code>(2), <code><a href="/docs/linux/man/2-setitimer/">setitimer</a></code>(2), <code><a href="/docs/linux/man/2-select/">select</a></code>(2) </p>
