---
title: "uvszprintf(3)"
name: "uvszprintf"
section: "3"
letter: "u"
url: "/docs/linux/man/3-uvszprintf/"
description: "uvszprintf – Writes formatted data into a buffer, using size and variable arguments. Allegro game programming library."
---

<p>uvszprintf &#8211; Writes formatted data into a buffer, using size and variable arguments. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int uvszprintf(char *buf, int size, const char *format, va_list args);</code></pre>
<h2>Description</h2>
<p>This is like uszprintf(), but you pass the variable argument list directly, instead of the arguments themselves. Example: </p>
<pre><code>#include &lt;stdarg.h&gt;

void log_message(const char *format, ...)
{
    char buffer[100];
    va_list parameters;

    va_start(parameters, format);
    uvszprintf(buffer, sizeof(buffer), format, parameters);
    va_end(parameters);

    append_buffer_to_logfile(log_name, buffer);
    send_buffer_to_other_networked_players(multicast_ip, buffer);
    and_also_print_it_on_the_screen(cool_font, buffer);
}

void some_other_function(void)
{
    log_message(&quot;Hello %s, are you %d years old?
&quot;, &quot;Dave&quot;, 25);
}</code></pre>
<h2>Return Value</h2>
<p>Returns the number of characters that would have been written without eventual truncation (like with uvsprintf), not including the terminating null character. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uconvert/">uconvert</a></code>(3), <code><a href="/docs/linux/man/3-uszprintf/">uszprintf</a></code>(3), <code><a href="/docs/linux/man/3-uvsprintf/">uvsprintf</a></code>(3) </p>
