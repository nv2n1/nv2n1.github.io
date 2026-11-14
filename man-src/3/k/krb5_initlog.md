---
title: "krb5_initlog(3)"
name: "krb5_initlog"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_initlog/"
description: "krb5_initlog krb5_openlog krb5_closelog krb5_addlog_dest krb5_addlog_func krb5_log krb5_vlog krb5_log_msg krb5_vlog_msg – Heimdal logging functions"
---

<h2 class="name">NAME</h2>
<p> <code>krb5_initlog</code> <code>krb5_openlog</code> <code>krb5_closelog</code> <code>krb5_addlog_dest</code> <code>krb5_addlog_func</code> <code>krb5_log</code> <code>krb5_vlog</code> <code>krb5_log_msg</code> <code>krb5_vlog_msg</code> &#8211; Heimdal logging functions </p>
<h2>LIBRARY</h2>
<p> Kerberos 5 Library (libkrb5, -lkrb5)</p>
<h2>SYNOPSIS</h2>
<p> In krb5.h Ft typedef void Fn *krb5_log_log_func_t const char *time const char *message void *data Ft typedef void Fn *krb5_log_close_func_t void *data Ft krb5_error_code Fn krb5_addlog_dest krb5_context context krb5_log_facility *facility const char *destination Ft krb5_error_code Fn krb5_addlog_func krb5_context context krb5_log_facility *facility int min int max krb5_log_log_func_t log krb5_log_close_func_t close void *data Ft krb5_error_code Fn krb5_closelog krb5_context context krb5_log_facility *facility Ft krb5_error_code Fn krb5_initlog krb5_context context const char *program krb5_log_facility **facility Ft krb5_error_code Fn krb5_log krb5_context context krb5_log_facility *facility int level const char *format &#8230; Ft krb5_error_code Fn krb5_log_msg krb5_context context krb5_log_facility *facility char **reply int level const char *format &#8230; Ft krb5_error_code Fn krb5_openlog krb5_context context const char *program krb5_log_facility **facility Ft krb5_error_code Fn krb5_vlog krb5_context context krb5_log_facility *facility int level const char *format va_list arglist Ft krb5_error_code Fn krb5_vlog_msg krb5_context context krb5_log_facility *facility char **reply int level const char *format va_list arglist</p>
<h2>DESCRIPTION</h2>
<p> These functions logs messages to one or more destinations. </p>
<p> The Fn krb5_openlog function creates a logging Fa facility , that is used to log messages. A facility consists of one or more destinations (which can be files or syslog or some other device). The Fa program parameter should be the generic name of the program that is doing the logging. This name is used to lookup which destinations to use. This information is contained in the <code>logging</code> section of the krb5.conf configuration file. If no entry is found for Fa program , the entry for <code>default</code> is used, or if that is missing too, <code>SYSLOG</code> will be used as destination. </p>
<p> To close a logging facility, use the Fn krb5_closelog function. </p>
<p> To log a message to a facility use one of the functions Fn krb5_log , Fn krb5_log_msg , Fn krb5_vlog , or Fn krb5_vlog_msg . The functions ending in <code>_msg</code> return in Fa reply a pointer to the message that just got logged. This string is allocated, and should be freed with Fn free . The Fa format is a standard Fn printf style format string (but see the BUGS section). </p>
<p> If you want better control of where things gets logged, you can instead of using Fn krb5_openlog call Fn krb5_initlog , which just initializes a facility, but doesn&#8217;t define any actual logging destinations. You can then add destinations with the Fn krb5_addlog_dest and Fn krb5_addlog_func functions. The first of these takes a string specifying a logging destination, and adds this to the facility. If you want to do some non-standard logging you can use the Fn krb5_addlog_func function, which takes a function to use when logging. The Fa log function is called for each message with Fa time being a string specifying the current time, and Fa message the message to log. Fa close is called when the facility is closed. You can pass application specific data in the Fa data parameter. The Fa min and Fa max parameter are the same as in a destination (defined below). To specify a max of infinity, pass -1. </p>
<p> Fn krb5_openlog calls Fn krb5_initlog and then calls Fn krb5_addlog_dest for each destination found.</p>
<h3>Destinations</h3>
<p> The defined destinations (as specified in krb5.conf follows:</p>
<dl>
<dt><code>STDERR</code></p>
<dd> This logs to the program&#8217;s stderr.</p>
<dt><code>FILE: /file </code></p>
<dd>
<dt><code>FILE= /file </code></p>
<dd> Log to the specified file. The form using a colon appends to the file, the form with an equal truncates the file. The truncating form keeps the file open, while the appending form closes it after each log message (which makes it possible to rotate logs). The truncating form is mainly for compatibility with the MIT libkrb5.</p>
<dt><code>DEVICE= /device </code></p>
<dd> This logs to the specified device, at present this is the same as <code>FILE:/device</code></p>
<dt><code>CONSOLE</code></p>
<dd> Log to the console, this is the same as <code>DEVICE=/dev/console</code></p>
<dt><code>SYSLOG </code>[:priority [:facility] ]</p>
<dd> Send messages to the syslog system, using priority, and facility. To get the name for one of these, you take the name of the macro passed to <a href="/docs/linux/man/3-syslog/">syslog</a>(3), and remove the leading <code>LOG_</code> <code>( LOG_NOTICE</code> becomes <code>NOTICE )</code> The default values (as well as the values used for unrecognised values), are <code>ERR</code> and <code>AUTH</code> respectively. See <a href="/docs/linux/man/3-syslog/">syslog</a>(3) for a list of priorities and facilities.</dl>
<p> Each destination may optionally be prepended with a range of logging levels, specified as <code>min-max/</code> If the Fa level parameter to Fn krb5_log is within this range (inclusive) the message gets logged to this destination, otherwise not. Either of the min and max valued may be omitted, in this case min is assumed to be zero, and max is assumed to be infinity. If you don&#8217;t include a dash, both min and max gets set to the specified value. If no range is specified, all messages gets logged.</p>
<h2>EXAMPLES</h2>
<blockquote>
<pre>
[logging]
        kdc = 0/FILE:/var/log/kdc.log
        kdc = 1-/SYSLOG:INFO:USER
        default = STDERR
</pre>
</blockquote>
<p> This will log all messages from the <code>kdc</code> program with level 0 to /var/log/kdc.log other messages will be logged to syslog with priority <code>LOG_INFO</code> and facility <code>LOG_USER</code> All other programs will log all messages to their stderr.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-syslog/">syslog</a>(3), krb5.conf5</p>
<h2>BUGS</h2>
<p> These functions use Fn asprintf to format the message. If your operating system does not have a working Fn asprintf , a replacement will be used. At present this replacement does not handle some correct conversion specifications (like floating point numbers). Until this is fixed, the use of these conversions should be avoided. </p>
<p> If logging is done to the syslog facility, these functions might not be thread-safe, depending on the implementation of Fn openlog , and Fn syslog . </p>
<h2>Index</h2>
