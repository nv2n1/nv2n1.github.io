---
title: "qblog-h(3)"
name: "qblog-h"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qblog-h/"
description: "qblog.h –"
---

<p>qblog.h &#8211; </p>
<p> The logging API provides four main parts (basics, filtering, threading &amp; blackbox).</p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;stdint.h&gt;

#include &lt;stdlib.h&gt;

#include &lt;stdio.h&gt;

#include &lt;stdarg.h&gt;

#include &lt;errno.h&gt;

#include &lt;syslog.h&gt;

#include &lt;string.h&gt;

#include &lt;qb/qbutil.h&gt;

#include &lt;qb/qbconfig.h&gt;</code></pre>
<h3>Data Structures</h3>
<p>struct qb_log_callsite</p>
<p>    An instance of this structure is created in a special ELF section at every dynamic debug callsite.</p>
<p>    union qb_log_ctl2_arg_t</p>
<p>        Macros<br />
#define LOG_TRACE (LOG_DEBUG + 1)</p>
<p>#define QB_LOG_MAX_LEN 512</p>
<p>#define QB_LOG_STRERROR_MAX_LEN 128</p>
<p>#define QB_LOG_INIT_DATA(name)</p>
<p>#define QB_LOG_TAG_LIBQB_MSG_BIT 31</p>
<p>#define QB_LOG_TAG_LIBQB_MSG (1 &lt;&lt; QB_LOG_TAG_LIBQB_MSG_BIT)</p>
<p>#define qb_logt(priority, tags, fmt, args&#8230;)</p>
<p>            This is the function to generate a log message if you want to manually add tags.</p>
<p>#define qb_log(priority, fmt, args&#8230;) qb_logt(priority, 0, fmt, ##args)</p>
<p>    This is the main function to generate a log message.</p>
<p>#define QB_XC &#8216;&#8217;</p>
<p>#define QB_XS &#8216;&#8217;</p>
<p>#define qb_perror(priority, fmt, args&#8230;)</p>
<p>    This is similar to perror except it goes into the logging system.</p>
<p>#define qb_enter() qb_log(LOG_TRACE, &#8216;ENTERING %s()&#8217;, __func__)</p>
<p>#define qb_leave() qb_log(LOG_TRACE, &#8216;LEAVING %s()&#8217;, __func__)</p>
<p>#define QB_LOG_CTL2_I32(a) ((qb_log_ctl2_arg_t){.i32 = (a)})</p>
<p>#define QB_LOG_CTL2_S(a) ((qb_log_ctl2_arg_t){.s = (a)})</p>
<p>    Typedefs<br />
 typedef const char *(* <code>qb_log_tags_stringify_fn</code> )(uint32_t <code>tags</code>) </p>
<p> typedef void(* <code>qb_log_filter_fn</code> )(struct <code>qb_log_callsite</code> *cs) </p>
<p> typedef void(* <code>qb_log_logger_fn</code> )(int32_t t, struct <code>qb_log_callsite</code> *cs, time_t timestamp, const char *msg) </p>
<p> typedef void(* <code>qb_log_vlogger_fn</code> )(int32_t t, struct <code>qb_log_callsite</code> *cs, time_t timestamp, va_list ap) </p>
<p> typedef void(* <code>qb_log_close_fn</code> )(int32_t t) </p>
<p> typedef void(* <code>qb_log_reload_fn</code> )(int32_t t)</p>
<h3>Enumerations</h3>
<p>enum qb_log_target_slot { QB_LOG_TARGET_START, QB_LOG_TARGET_STATIC_START = QB_LOG_TARGET_START, QB_LOG_SYSLOG = QB_LOG_TARGET_STATIC_START, QB_LOG_STDERR, QB_LOG_BLACKBOX, QB_LOG_STDOUT, QB_LOG_TARGET_STATIC_MAX, QB_LOG_TARGET_STATIC_END = QB_LOG_TARGET_STATIC_MAX &#8211; 1, QB_LOG_TARGET_DYNAMIC_START = QB_LOG_TARGET_STATIC_MAX, QB_LOG_TARGET_MAX = 32, QB_LOG_TARGET_DYNAMIC_END = QB_LOG_TARGET_MAX &#8211; 1, QB_LOG_TARGET_END = QB_LOG_TARGET_DYNAMIC_END }</p>
<p>enum qb_log_target_state { QB_LOG_STATE_UNUSED = 1, QB_LOG_STATE_DISABLED = 2, QB_LOG_STATE_ENABLED = 3 }</p>
<p>enum qb_log_conf { QB_LOG_CONF_ENABLED, QB_LOG_CONF_FACILITY, QB_LOG_CONF_DEBUG, QB_LOG_CONF_SIZE, QB_LOG_CONF_THREADED, QB_LOG_CONF_PRIORITY_BUMP, QB_LOG_CONF_STATE_GET, QB_LOG_CONF_FILE_SYNC, QB_LOG_CONF_EXTENDED, QB_LOG_CONF_IDENT }</p>
<p>enum qb_log_filter_type { QB_LOG_FILTER_FILE, QB_LOG_FILTER_FUNCTION, QB_LOG_FILTER_FORMAT, QB_LOG_FILTER_FILE_REGEX, QB_LOG_FILTER_FUNCTION_REGEX, QB_LOG_FILTER_FORMAT_REGEX }</p>
<p>enum qb_log_filter_conf { QB_LOG_FILTER_ADD, QB_LOG_FILTER_REMOVE, QB_LOG_FILTER_CLEAR_ALL, QB_LOG_TAG_SET, QB_LOG_TAG_CLEAR, QB_LOG_TAG_CLEAR_ALL }</p>
<p>Functions<br />
 struct <code>qb_log_callsite</code> <code>__attribute__</code> ((<a href="/docs/linux/man/8-aligned/">aligned</a>(8))) </p>
<p> void <code>qb_log_real_</code> (struct <code>qb_log_callsite</code> *cs,&#8230;)<br />
 <i>Internal function: use </i><code>qb_log()</code> or <code>qb_logt()</code><br />
 void <code>qb_log_real_va_</code> (struct <code>qb_log_callsite</code> *cs, va_list ap) </p>
<p> void <code>qb_log_from_external_source</code> (const char *<code>function</code>, const char *<code>filename</code>, const char *<code>format</code>, uint8_t <code>priority</code>, uint32_t <code>lineno</code>, uint32_t <code>tags</code>,&#8230;) <code>__attribute__</code>((<code>format</code>(printf<br />
 <i>This function is to import logs from other code (like libraries) that provide a callback with their logs. </i><br />
 void struct <code>qb_log_callsite</code> * <code>qb_log_callsite_get</code> (const char *<code>function</code>, const char *<code>filename</code>, const char *<code>format</code>, uint8_t <code>priority</code>, uint32_t <code>lineno</code>, uint32_t <code>tags</code>)<br />
 <i>Get or create a callsite at the given position. </i><br />
 void <code>qb_log_from_external_source_va</code> (const char *<code>function</code>, const char *<code>filename</code>, const char *<code>format</code>, uint8_t <code>priority</code>, uint32_t <code>lineno</code>, uint32_t <code>tags</code>, va_list ap) <code>__attribute__</code>((<code>format</code>(printf </p>
<p> void <code>qb_log_init</code> (const char *name, int32_t facility, uint8_t <code>priority</code>)<br />
 <i>Init the logging system. </i><br />
 void <code>qb_log_fini</code> (void)<br />
 <i>Logging system finalization function. </i><br />
 int32_t <code>qb_log_callsites_register</code> (struct <code>qb_log_callsite</code> *_start, struct <code>qb_log_callsite</code> *_stop)<br />
 <i>If you are using dynamically loadable modules via dlopen() and you load them after </i><code>qb_log_init()</code> then after you load the module you will need to do the following to get the filters to work in that module:<br />
 void <code>qb_log_callsites_dump</code> (void)<br />
 <i>Dump the callsite info to stdout. </i><br />
 int32_t <code>qb_log_ctl</code> (int32_t target, enum <code>qb_log_conf</code> conf_type, int32_t arg)<br />
 <i>Main logging control function. </i><br />
 int32_t <code>qb_log_ctl2</code> (int32_t target, enum <code>qb_log_conf</code> conf_type, <code>qb_log_ctl2_arg_t</code> arg)<br />
 <i>Extension of main logging control function accepting also strings. </i><br />
 int32_t <code>qb_log_filter_ctl</code> (int32_t value, enum <code>qb_log_filter_conf</code> c, enum <code>qb_log_filter_type</code> type, const char *text, uint8_t low_priority)<br />
 <i>This allows you modify the &#8216;tags&#8217; and &#8216;targets&#8217; callsite fields at runtime. </i><br />
 int32_t <code>qb_log_filter_ctl2</code> (int32_t value, enum <code>qb_log_filter_conf</code> c, enum <code>qb_log_filter_type</code> type, const char *text, uint8_t high_priority, uint8_t low_priority)<br />
 <i>This extends </i><code>qb_log_filter_ctl()</code> by been able to provide a high_priority.<br />
 int32_t <code>qb_log_filter_fn_set</code> (<code>qb_log_filter_fn</code> fn)<br />
 <i>Instead of using the </i><code>qb_log_filter_ctl()</code> functions you can apply the filters manually by defining a callback and setting the targets field using <code>qb_bit_set()</code> and <code>qb_bit_clear()</code> like the following below:<br />
 void <code>qb_log_tags_stringify_fn_set</code> (<code>qb_log_tags_stringify_fn</code> fn)<br />
 <i>Set the callback to map the &#8216;tags&#8217; bit map to a string. </i><br />
 void <code>qb_log_format_set</code> (int32_t t, const char *<code>format</code>)<br />
 <i>Set the format specifiers. </i><br />
 int32_t <code>qb_log_file_open</code> (const char *<code>filename</code>)<br />
 <i>Open a log file. </i><br />
 void <code>qb_log_file_close</code> (int32_t t)<br />
 <i>Close a log file and release is resources. </i><br />
 int32_t <code>qb_log_thread_priority_set</code> (int32_t policy, int32_t <code>priority</code>)<br />
 <i>When using threaded logging set the pthread policy and priority. </i><br />
 int32_t <code>qb_log_thread_start</code> (void)<br />
 <i>Start the logging pthread. </i><br />
 ssize_t <code>qb_log_blackbox_write_to_file</code> (const char *<code>filename</code>)<br />
 <i>Write the blackbox to file. </i><br />
 void <code>qb_log_blackbox_print_from_file</code> (const char *<code>filename</code>)<br />
 <i>Read the blackbox for file and print it out. </i><br />
 int32_t <code>qb_log_custom_open</code> (<code>qb_log_logger_fn</code> log_fn, <code>qb_log_close_fn</code> close_fn, <code>qb_log_reload_fn</code> reload_fn, void *user_data)<br />
 <i>Open a custom log target. </i><br />
 void <code>qb_log_custom_close</code> (int32_t t)<br />
 <i>Close a custom log target and release is resources. </i><br />
 void * <code>qb_log_target_user_data_get</code> (int32_t t)<br />
 <i>Retrieve the user data set by either qb_log_custom_open or qb_log_target_user_data_set. </i><br />
 int32_t <code>qb_log_target_user_data_set</code> (int32_t t, void *user_data)<br />
 <i>Associate user data with this log target. </i><br />
 void <code>qb_log_target_format</code> (int32_t target, struct <code>qb_log_callsite</code> *cs, time_t timestamp, const char *formatted_message, char *output_buffer)<br />
 <i>format the callsite and timestamp info according to the format set using </i><code>qb_log_format_set()</code> It is intended to be used from your custom logger function.<br />
 int32_t <code>qb_log_facility2int</code> (const char *fname)<br />
 <i>Convert string &#8216;auth&#8217; to equivalent number &#8216;LOG_AUTH&#8217; etc. </i><br />
 const char * <code>qb_log_facility2str</code> (int32_t fnum)<br />
 <i>Convert number &#8216;LOG_AUTH&#8217; to equivalent string &#8216;auth&#8217; etc. </i></p>
<h3>Variables</h3>
<pre><code>const char * function



const char * filename



const char * format



uint8_t priority



uint32_t lineno



uint32_t targets



uint32_t tags



struct qb_log_callsite __start___verbose []



struct qb_log_callsite __stop___verbose []



enum qb_log_target_slot __attribute__</code></pre>
<h2>Detailed Description</h2>
<p>The logging API provides four main parts (basics, filtering, threading &amp; blackbox). </p>
<p> The idea behind this logging system is not to be prescriptive but to provide a set of tools to help the developer achieve what they want quickly and easily. </p>
<p> <code>Basic logging API.</code></p>
<dl>
<dd>Call <code>qb_log()</code> to generate a log message. Then to write the message somewhere meaningful call <code>qb_log_ctl()</code> to configure the targets.</dl>
<p> Simplest possible use: </p>
<pre>* main() {
* qb_log_init(&quot;simple-log&quot;, LOG_DAEMON, LOG_INFO);
* // ...
* qb_log(LOG_WARNING, &quot;watch out&quot;);
* // ...
* qb_log_fini();
* }
* </pre>
<p><code>Configuring log targets.</code></p>
<dl>
<dd>A log target can be syslog, stderr, the blackbox, stdout, or a text file. By default only syslog is enabled.</dl>
<p> To enable a target do the following: </p>
<pre>* qb_log_ctl(QB_LOG_BLACKBOX, QB_LOG_CONF_ENABLED, QB_TRUE);
* </pre>
<p>syslog, stderr, the blackbox, and stdout are static (they don&#8217;t need to be created, just enabled or disabled). However you can open multiple logfiles (QB_LOG_TARGET_MAX &#8211; QB_LOG_TARGET_STATIC_MAX). To do this, use the following code: </p>
<pre>* mytarget = qb_log_file_open(&quot;/var/log/mylogfile&quot;);
* qb_log_ctl(mytarget, QB_LOG_CONF_ENABLED, QB_TRUE);
* </pre>
<p>Once your targets are enabled/opened you can configure them as follows: Configure the size of blackbox </p>
<pre>* qb_log_ctl(QB_LOG_BLACKBOX, QB_LOG_CONF_SIZE, 1024*10);
* </pre>
<p>Make logging to file threaded: </p>
<pre>* qb_log_ctl(mytarget, QB_LOG_CONF_THREADED, QB_TRUE);
* </pre>
<p>To workaround your syslog daemon filtering all messages &gt; LOG_INFO </p>
<pre>* qb_log_ctl(QB_LOG_SYSLOG, QB_LOG_CONF_PRIORITY_BUMP,
* LOG_INFO - LOG_DEBUG);
* </pre>
<p>To ensure all logs to file targets are fsync&#8217;ed (default QB_FALSE) </p>
<pre>* qb_log_ctl(mytarget, QB_LOG_CONF_FILE_SYNC, QB_TRUE);
* </pre>
<p><code>Filtering messages.</code></p>
<dl>
<dd>To have more power over what log messages go to which target you can apply filters to the targets. What happens is the desired callsites have the correct bit set. Then when the log message is generated it gets sent to the targets based on which bit is set in the callsite&#8217;s &#8216;target&#8217; bitmap. Messages can be filtered based on the:</p>
<dl>
<dt>1.</p>
<dd>filename + priority</p>
<dt>2.</p>
<dd>function name + priority</p>
<dt>3.</p>
<dd>format string + priority</dl>
</dl>
<p> So to make all logs from evil_function() go to stderr, do the following: </p>
<pre>* qb_log_filter_ctl(QB_LOG_STDERR, QB_LOG_FILTER_ADD,
* QB_LOG_FILTER_FUNCTION, &quot;evil_function&quot;, LOG_TRACE);
* </pre>
<p>So to make all logs from totem* (with a priority &lt;= LOG_INFO) go to stderr, do the following: </p>
<pre>* qb_log_filter_ctl(QB_LOG_STDERR, QB_LOG_FILTER_ADD,
* QB_LOG_FILTER_FILE, &quot;totem&quot;, LOG_INFO);
* </pre>
<p>So to make all logs with the substring &#8216;ringbuffer&#8217; go to stderr, do the following: </p>
<pre>* qb_log_filter_ctl(QB_LOG_STDERR, QB_LOG_FILTER_ADD,
* QB_LOG_FILTER_FORMAT, &quot;ringbuffer&quot;, LOG_TRACE);
* </pre>
<p><code>Thread safe non-blocking logging.</code></p>
<dl>
<dd>Logging is only thread safe when threaded logging is in use. If you plan on logging from multiple threads, you must initialize libqb&#8217;s logger thread and use qg_log_filter_ctl to set the QB_LOG_CONF_THREADED flag on all the logging targets in use.</dl>
<p> To achieve non-blocking logging, so that any calls to write() or syslog() will not hold up your program, you can use threaded logging as well. </p>
<p> Threaded logging use: </p>
<pre>* main() {
* qb_log_init(&quot;simple-log&quot;, LOG_DAEMON, LOG_INFO);
* qb_log_ctl(QB_LOG_SYSLOG, QB_LOG_CONF_THREADED, QB_TRUE);
* // ...
* daemonize();
* // call this after you fork()
* qb_log_thread_start();
* // ...
* qb_log(LOG_WARNING, &quot;watch out&quot;);
* // ...
* qb_log_fini();
* }
* </pre>
<p><code>A blackbox for in-field diagnosis.</code></p>
<dl>
<dd>This stores log messages in a ringbuffer so they can be written to file if the program crashes (you will need to catch SIGSEGV). These can then be easily printed out later.</dl>
<p> <code>Note:</code></p>
<dl>
<dd>the blackbox is not enabled by default.</dl>
<p> Blackbox usage: </p>
<pre>*
* static void sigsegv_handler(int sig)
* {
* (void)signal (SIGSEGV, SIG_DFL);
* qb_log_blackbox_write_to_file(&quot;simple-log.fdata&quot;);
* qb_log_fini();
* raise(SIGSEGV);
* }
*
* main() {
*
* signal(SIGSEGV, sigsegv_handler);
*
* qb_log_init(&quot;simple-log&quot;, LOG_DAEMON, LOG_INFO);
* qb_log_filter_ctl(QB_LOG_BLACKBOX, QB_LOG_FILTER_ADD,
* QB_LOG_FILTER_FILE, &quot;*&quot;, LOG_DEBUG);
* qb_log_ctl(QB_LOG_BLACKBOX, QB_LOG_CONF_SIZE, 1024*10);
* qb_log_ctl(QB_LOG_BLACKBOX, QB_LOG_CONF_ENABLED, QB_TRUE);
* // ...
* qb_log(LOG_WARNING, &quot;watch out&quot;);
* // ...
* qb_log_fini();
* }
* </pre>
<p><code>Tagging messages.</code></p>
<dl>
<dd>You can tag messages using the second argument to <code>qb_logt()</code> or by using <code>qb_log_filter_ctl()</code>. This can be used to add feature or sub-system information to the logs.</dl>
<pre>* const char* my_tags_stringify(uint32_t tags) {
* if (qb_bit_is_set(tags, QB_LOG_TAG_LIBQB_MSG_BIT) {
* return &quot;libqb&quot;;
* } else if (tags == 3) {
* return &quot;three&quot;;
* } else {
* return &quot;MAIN&quot;;
* }
* }
* main() {
* // ...
* qb_log_tags_stringify_fn_set(my_tags_stringify);
* qb_log_format_set(QB_LOG_STDERR, &quot;[%5g] %p %b&quot;);
* // ...
* qb_logt(LOG_INFO, 3, &quot;hello&quot;);
* qb_logt(LOG_INFO, 0, &quot;hello&quot;);
* }
* </pre>
<p>&nbsp;<wbr>The code above will produce:&nbsp;<wbr> </p>
<pre>* [libqb] some message
* [three] info hello
* [MAIN ] info hello
* </pre>
<p>&nbsp;<wbr></p>
<h2>Macro Definition Documentation</h2>
<h3>#define LOG_TRACE (LOG_DEBUG + 1)</h3>
<h3>#define qb_enter() <code>qb_log</code>(<code>LOG_TRACE</code>, &#8216;ENTERING %s()&#8217;, __func__)</h3>
<h3>#define qb_leave() <code>qb_log</code>(<code>LOG_TRACE</code>, &#8216;LEAVING %s()&#8217;, __func__)</h3>
<h3>#define qb_log(<code>priority</code>, fmt, args&#8230;) <code>qb_logt</code>(<code>priority</code>, 0, fmt, ##args)</h3>
<p>This is the main function to generate a log message. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>priority</i> this takes syslog priorities.<br />
 <i>fmt</i> usual printf style format specifiers<br />
 <i>args</i> usual printf style args</dl>
<h3>#define QB_LOG_CTL2_I32(a) ((<code>qb_log_ctl2_arg_t</code>) { .i32 = (a) })</h3>
<h3>#define QB_LOG_CTL2_S(a) ((<code>qb_log_ctl2_arg_t</code>) { .s = (a) })</h3>
<h3>#define QB_LOG_INIT_DATA(name)</h3>
<p><code>Value:</code> </p>
<pre>void name(void); void name(void) { if (__start___verbose != __stop___verbose) {<a href="//www.systutorials.com/docs/linux/man/1-assert/">assert</a>(1);} } void __attribute__ ((constructor)) name(void);</pre>
<h3>#define QB_LOG_MAX_LEN 512</h3>
<h3>#define QB_LOG_STRERROR_MAX_LEN 128</h3>
<h3>#define QB_LOG_TAG_LIBQB_MSG (1 &lt;&lt; <code>QB_LOG_TAG_LIBQB_MSG_BIT</code>)</h3>
<h3>#define QB_LOG_TAG_LIBQB_MSG_BIT 31</h3>
<h3>#define qb_logt(<code>priority</code>, <code>tags</code>, fmt, args&#8230;)</h3>
<p><code>Value:</code> </p>
<pre>do { static struct qb_log_callsite descriptor __attribute__((section(&quot;__verbose&quot;), <a href="//www.systutorials.com/docs/linux/man/8-aligned/">aligned</a>(8))) = { __func__, __FILE__, fmt, priority, __LINE__, 0, tags }; \
 qb_log_real_(&amp;descriptor, ##args); } while(0)</pre>
<p>This is the function to generate a log message if you want to manually add tags. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>priority</i> this takes syslog priorities.<br />
 <i>tags</i> this is a uint32_t that you can use with <code>qb_log_tags_stringify_fn_set()</code> to &#8216;tag&#8217; a log message with a feature or sub-system then you can use &#8216;%g&#8217; in the format specifer to print it out.<br />
 <i>fmt</i> usual printf style format specifiers<br />
 <i>args</i> usual printf style args</dl>
<h3>#define qb_perror(<code>priority</code>, fmt, args&#8230;)</h3>
<p><code>Value:</code> </p>
<pre>do { char _perr_buf_[QB_LOG_STRERROR_MAX_LEN]; const char *_perr_str_ = qb_strerror_r(errno, _perr_buf_, sizeof(_perr_buf_)); \
 qb_logt(priority, 0, fmt &quot;: %s (%d)&quot;, ##args, _perr_str_, errno); } while(0)</pre>
<p>This is similar to perror except it goes into the logging system. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>priority</i> this takes syslog priorities.<br />
 <i>fmt</i> usual printf style format specifiers<br />
 <i>args</i> usual printf style args</dl>
<p> <code>Note:</code></p>
<dl>
<dd>Because <code>qb_perror()</code> adds the system error message and error number onto the end of the given fmt, that information will become extended information if QB_XS is used inside fmt and will not show up in any logs that strip extended information.</dl>
<h3>#define QB_XC &#8216;&#8217;</h3>
<h3>#define QB_XS &#8216;&#8217;</h3>
<h2>Typedef Documentation</h2>
<h3>typedef void(* qb_log_close_fn)(int32_t t)</h3>
<h3>typedef void(* qb_log_filter_fn)(struct <code>qb_log_callsite</code> *cs)</h3>
<h3>typedef void(* qb_log_logger_fn)(int32_t t, struct <code>qb_log_callsite</code> *cs, time_t timestamp, const char *msg)</h3>
<h3>typedef void(* qb_log_reload_fn)(int32_t t)</h3>
<h3>typedef const char*(* qb_log_tags_stringify_fn)(uint32_t <code>tags</code>)</h3>
<h3>typedef void(* qb_log_vlogger_fn)(int32_t t, struct <code>qb_log_callsite</code> *cs, time_t timestamp, va_list ap)</h3>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>qb_log_conf</code></h3>
<p><code>Enumerator</code></p>
<dl>
<dt><i>QB_LOG_CONF_ENABLED </i></p>
<dd>
<dt><i>QB_LOG_CONF_FACILITY </i></p>
<dd>
<dt><i>QB_LOG_CONF_DEBUG </i></p>
<dd>
<dt><i>QB_LOG_CONF_SIZE </i></p>
<dd>
<dt><i>QB_LOG_CONF_THREADED </i></p>
<dd>
<dt><i>QB_LOG_CONF_PRIORITY_BUMP </i></p>
<dd>
<dt><i>QB_LOG_CONF_STATE_GET </i></p>
<dd>
<dt><i>QB_LOG_CONF_FILE_SYNC </i></p>
<dd>
<dt><i>QB_LOG_CONF_EXTENDED </i></p>
<dd>
<dt><i>QB_LOG_CONF_IDENT </i></p>
<dd></dl>
<h3>enum <code>qb_log_filter_conf</code></h3>
<p><code>Enumerator</code></p>
<dl>
<dt><i>QB_LOG_FILTER_ADD </i></p>
<dd>
<dt><i>QB_LOG_FILTER_REMOVE </i></p>
<dd>
<dt><i>QB_LOG_FILTER_CLEAR_ALL </i></p>
<dd>
<dt><i>QB_LOG_TAG_SET </i></p>
<dd>
<dt><i>QB_LOG_TAG_CLEAR </i></p>
<dd>
<dt><i>QB_LOG_TAG_CLEAR_ALL </i></p>
<dd></dl>
<h3>enum <code>qb_log_filter_type</code></h3>
<p><code>Enumerator</code></p>
<dl>
<dt><i>QB_LOG_FILTER_FILE </i></p>
<dd>
<dt><i>QB_LOG_FILTER_FUNCTION </i></p>
<dd>
<dt><i>QB_LOG_FILTER_FORMAT </i></p>
<dd>
<dt><i>QB_LOG_FILTER_FILE_REGEX </i></p>
<dd>
<dt><i>QB_LOG_FILTER_FUNCTION_REGEX </i></p>
<dd>
<dt><i>QB_LOG_FILTER_FORMAT_REGEX </i></p>
<dd></dl>
<h3>enum <code>qb_log_target_slot</code></h3>
<p><code>Enumerator</code></p>
<dl>
<dt><i>QB_LOG_TARGET_START </i></p>
<dd>
<dt><i>QB_LOG_TARGET_STATIC_START </i></p>
<dd>
<dt><i>QB_LOG_SYSLOG </i></p>
<dd>
<dt><i>QB_LOG_STDERR </i></p>
<dd>
<dt><i>QB_LOG_BLACKBOX </i></p>
<dd>
<dt><i>QB_LOG_STDOUT </i></p>
<dd>
<dt><i>QB_LOG_TARGET_STATIC_MAX </i></p>
<dd>
<dt><i>QB_LOG_TARGET_STATIC_END </i></p>
<dd>
<dt><i>QB_LOG_TARGET_DYNAMIC_START </i></p>
<dd>
<dt><i>QB_LOG_TARGET_MAX </i></p>
<dd>
<dt><i>QB_LOG_TARGET_DYNAMIC_END </i></p>
<dd>
<dt><i>QB_LOG_TARGET_END </i></p>
<dd></dl>
<h3>enum <code>qb_log_target_state</code></h3>
<p><code>Enumerator</code></p>
<dl>
<dt><i>QB_LOG_STATE_UNUSED </i></p>
<dd>
<dt><i>QB_LOG_STATE_DISABLED </i></p>
<dd>
<dt><i>QB_LOG_STATE_ENABLED </i></p>
<dd></dl>
<h2>Function Documentation</h2>
<h3>struct <code>qb_log_callsite</code> __attribute__ ((<a href="/docs/linux/man/8-aligned/">aligned</a>(8)))</h3>
<h3>void qb_log_blackbox_print_from_file (const char *filename)</h3>
<p>Read the blackbox for file and print it out.</p>
<h3>ssize_t qb_log_blackbox_write_to_file (const char *filename)</h3>
<p>Write the blackbox to file.</p>
<h3>void struct <code>qb_log_callsite</code>* qb_log_callsite_get (const char *function, const char *filename, const char *format, uint8_tpriority, uint32_tlineno, uint32_ttags)</h3>
<p>Get or create a callsite at the given position. The result can then be passed into <code>qb_log_real_()</code> </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>function</i> originating function name<br />
 <i>filename</i> originating filename<br />
 <i>format</i> format string<br />
 <i>priority</i> this takes syslog priorities.<br />
 <i>lineno</i> file line number<br />
 <i>tags</i> the tag</dl>
<h3>void qb_log_callsites_dump (void)</h3>
<p>Dump the callsite info to stdout.</p>
<h3>int32_t qb_log_callsites_register (struct <code>qb_log_callsite</code> *_start, struct <code>qb_log_callsite</code> *_stop)</h3>
<p>If you are using dynamically loadable modules via dlopen() and you load them after <code>qb_log_init()</code> then after you load the module you will need to do the following to get the filters to work in that module: </p>
<pre>* _start = dlsym (dl_handle, &quot;__start___verbose&quot;);
* _stop = dlsym (dl_handle, &quot;__stop___verbose&quot;);
* qb_log_callsites_register(_start, _stop);
* </pre>
<p>&nbsp;<wbr></p>
<h3>int32_t qb_log_ctl (int32_ttarget, enum <code>qb_log_conf</code>conf_type, int32_targ)</h3>
<p>Main logging control function. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>target</i> QB_LOG_SYSLOG, QB_LOG_STDERR or result from <code>qb_log_file_open()</code><br />
 <i>conf_type</i> configuration directive (&#8216;what to configure&#8217;) that accepts int32_t argument determining the new value unless ignored for particular directive altogether (incompatible directives: QB_LOG_CONF_IDENT)<br />
 <i>arg</i> the new value for a state-changing configuration directive, ignored otherwise</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>qb_log_conf</code></dl>
<p> <code>Return values:</code></p>
<dl>
<dd><i>-errno</i> on error<br />
 <i>0</i> on success<br />
 <i>qb_log_target_state</i> for QB_LOG_CONF_STATE_GET</dl>
<h3>int32_t qb_log_ctl2 (int32_ttarget, enum <code>qb_log_conf</code>conf_type, <code>qb_log_ctl2_arg_t</code>arg)</h3>
<p>Extension of main logging control function accepting also strings. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>target</i> QB_LOG_SYSLOG, QB_LOG_STDERR or result from <code>qb_log_file_open()</code><br />
 <i>conf_type</i> configuration directive (&#8216;what to configure&#8217;) that accepts either int32_t or a null-terminated string argument determining the new value unless ignored for particular directive (compatible directives: those valid for qb_log_ctl</p>
<dl>
<dt>&bull;</p>
<dd>QB_LOG_CONF_IDENT)</dl>
<p> <i>arg</i> the new value for a state-changing configuration directive, ignored otherwise; for QB_LOG_CONF_IDENT, &#8216;s&#8217; member as new identifier to openlog(), for all qb_log_ctl-compatible ones, &#8216;i32&#8217; member is assumed (although a preferred way is to use that original function directly as it allows for more type safety)</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>qb_log_ctl</code></dl>
<p> <code>Note:</code></p>
<dl>
<dd>You can use QB_LOG_CTL2_I32 and QB_LOG_CTL2_S macros for a convenient on-the-fly construction of the object to be passed as an arg argument.</dl>
<h3>void qb_log_custom_close (int32_tt)</h3>
<p>Close a custom log target and release is resources.</p>
<h3>int32_t qb_log_custom_open (<code>qb_log_logger_fn</code>log_fn, <code>qb_log_close_fn</code>close_fn, <code>qb_log_reload_fn</code>reload_fn, void *user_data)</h3>
<p>Open a custom log target. </p>
<p> <code>Return values:</code></p>
<dl>
<dd><i>-errno</i> on error<br />
 <i>value</i> in inclusive range QB_LOG_TARGET_DYNAMIC_START to QB_LOG_TARGET_DYNAMIC_END (to be passed into other qb_log_* functions)</dl>
<h3>int32_t qb_log_facility2int (const char *fname)</h3>
<p>Convert string &#8216;auth&#8217; to equivalent number &#8216;LOG_AUTH&#8217; etc.</p>
<h3>const char* qb_log_facility2str (int32_tfnum)</h3>
<p>Convert number &#8216;LOG_AUTH&#8217; to equivalent string &#8216;auth&#8217; etc.</p>
<h3>void qb_log_file_close (int32_tt)</h3>
<p>Close a log file and release is resources.</p>
<h3>int32_t qb_log_file_open (const char *filename)</h3>
<p>Open a log file. </p>
<p> <code>Return values:</code></p>
<dl>
<dd><i>-errno</i> on error<br />
 <i>value</i> in inclusive range QB_LOG_TARGET_DYNAMIC_START to QB_LOG_TARGET_DYNAMIC_END (to be passed into other qb_log_* functions)</dl>
<h3>int32_t qb_log_filter_ctl (int32_tvalue, enum <code>qb_log_filter_conf</code>c, enum <code>qb_log_filter_type</code>type, const char *text, uint8_tlow_priority)</h3>
<p>This allows you modify the &#8216;tags&#8217; and &#8216;targets&#8217; callsite fields at runtime.</p>
<h3>int32_t qb_log_filter_ctl2 (int32_tvalue, enum <code>qb_log_filter_conf</code>c, enum <code>qb_log_filter_type</code>type, const char *text, uint8_thigh_priority, uint8_tlow_priority)</h3>
<p>This extends <code>qb_log_filter_ctl()</code> by been able to provide a high_priority.</p>
<h3>int32_t qb_log_filter_fn_set (<code>qb_log_filter_fn</code>fn)</h3>
<p>Instead of using the <code>qb_log_filter_ctl()</code> functions you can apply the filters manually by defining a callback and setting the targets field using <code>qb_bit_set()</code> and <code>qb_bit_clear()</code> like the following below: </p>
<pre>* static void
* m_filter(struct qb_log_callsite *cs)
* {
* if ((cs-&gt;priority &gt;= LOG_ALERT &amp;&amp;
* cs-&gt;priority &lt;= LOG_DEBUG) &amp;&amp;
* strcmp(cs-&gt;filename, &quot;my_c_file.c&quot;) == 0) {
* qb_bit_set(cs-&gt;targets, QB_LOG_SYSLOG);
* } else {
* qb_bit_clear(cs-&gt;targets, QB_LOG_SYSLOG);
* }
* }
* </pre>
<p>&nbsp;<wbr></p>
<h3>void qb_log_fini (void)</h3>
<p>Logging system finalization function. It releases any shared memory. Stops the logging thread if running. Flushes the last messages to their destinations.</p>
<h3>void qb_log_format_set (int32_tt, const char *format)</h3>
<p>Set the format specifiers. n FUNCTION NAME f FILENAME l FILELINE p PRIORITY t TIMESTAMP b BUFFER g TAGS N name (passed into qb_log_init) P PID H hostname </p>
<p> any number between % and character specify field length to pad or chop</p>
<h3>void qb_log_from_external_source (const char *function, const char *filename, const char *format, uint8_tpriority, uint32_tlineno, uint32_ttags, &#8230;)</h3>
<p>This function is to import logs from other code (like libraries) that provide a callback with their logs. </p>
<p> <code>Note:</code></p>
<dl>
<dd>the performance of this will not impress you, as the filtering is done on each log message, not beforehand. So try doing basic pre-filtering.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>function</i> originating function name<br />
 <i>filename</i> originating filename<br />
 <i>format</i> format string<br />
 <i>priority</i> this takes syslog priorities.<br />
 <i>lineno</i> file line number<br />
 <i>tags</i> this is a uint32_t that you can use with <code>qb_log_tags_stringify_fn_set()</code> to &#8216;tag&#8217; a log message with a feature or sub-system then you can use &#8216;%g&#8217; in the format specifer to print it out.</dl>
<h3>void qb_log_from_external_source_va (const char *function, const char *filename, const char *format, uint8_tpriority, uint32_tlineno, uint32_ttags, va_listap)</h3>
<h3>void qb_log_init (const char *name, int32_tfacility, uint8_tpriority)</h3>
<p>Init the logging system. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>name</i> will be passed into openlog()<br />
 <i>facility</i> default for all new targets.<br />
 <i>priority</i> a basic filter with this priority will be added.</dl>
<h3>void qb_log_real_ (struct <code>qb_log_callsite</code> *cs, &#8230;)</h3>
<p>Internal function: use <code>qb_log()</code> or <code>qb_logt()</code></p>
<h3>void qb_log_real_va_ (struct <code>qb_log_callsite</code> *cs, va_listap)</h3>
<h3>void qb_log_tags_stringify_fn_set (<code>qb_log_tags_stringify_fn</code>fn)</h3>
<p>Set the callback to map the &#8216;tags&#8217; bit map to a string.</p>
<h3>void qb_log_target_format (int32_ttarget, struct <code>qb_log_callsite</code> *cs, time_ttimestamp, const char *formatted_message, char *output_buffer)</h3>
<p>format the callsite and timestamp info according to the format set using <code>qb_log_format_set()</code> It is intended to be used from your custom logger function.</p>
<h3>void* qb_log_target_user_data_get (int32_tt)</h3>
<p>Retrieve the user data set by either qb_log_custom_open or qb_log_target_user_data_set.</p>
<h3>int32_t qb_log_target_user_data_set (int32_tt, void *user_data)</h3>
<p>Associate user data with this log target. </p>
<p> <code>Note:</code></p>
<dl>
<dd>only use this with custom targets</dl>
<h3>int32_t qb_log_thread_priority_set (int32_tpolicy, int32_tpriority)</h3>
<p>When using threaded logging set the pthread policy and priority. </p>
<p> <code>Return values:</code></p>
<dl>
<dd><i>-errno</i> on error<br />
 <i>0</i> success</dl>
<h3>int32_t qb_log_thread_start (void)</h3>
<p>Start the logging pthread.</p>
<h2>Variable Documentation</h2>
<h3>enum <code>qb_log_target_slot</code> __attribute__</h3>
<h3>struct <code>qb_log_callsite</code> __start___verbose[]</h3>
<h3>struct <code>qb_log_callsite</code> __stop___verbose[]</h3>
<h3>const char* filename</h3>
<h3>const char* format</h3>
<h3>const char* function</h3>
<h3>uint32_t lineno</h3>
<h3>uint8_t priority</h3>
<h3>uint32_t tags</h3>
<h3>uint32_t targets</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libqb from the source code.</p>
