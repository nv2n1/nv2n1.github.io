---
title: "print_time_table(3)"
name: "print_time_table"
section: "3"
letter: "p"
url: "/docs/linux/man/3-print_time_table/"
description: "parse_time print_time_table unparse_time unparse_time_approx – parse and unparse time intervals"
---

<p><code>parse_time</code> <code>print_time_table</code> <code>unparse_time</code> <code>unparse_time_approx</code> &#8211; parse and unparse time intervals</p>
<h2>Library</h2>
<p>The roken library (libroken, -lroken)</p>
<h2>Synopsis</h2>
<pre><code>Fd #include &lt;parse_time.h&gt;

Ft int

Fn parse_time const char *timespec const char *def_unit

Ft void

Fn print_time_table FILE *f

Ft size_t

Fn unparse_time int seconds char *buf size_t len

Ft size_t

Fn unparse_time_approx int seconds char *buf size_t len</code></pre>
<h2>Description</h2>
<p>The Fn parse_time function converts the period of time specified into a number of seconds. The Fa timespec can be any number of Aq number unit pairs separated by comma and whitespace. The number can be negative. Numbers without explicit units are taken as being Fa def_unit . </p>
<p> The Fn unparse_time and Fn unparse_time_approx do the opposite of Fn parse_time , that is they take a number of seconds and express that as human readable strings. Fa unparse_time produces an exact time, while Fa unparse_time_approx restricts the result to include only one unit. </p>
<p> Fn print_time_table prints a descriptive list of available units on the passed file descriptor. </p>
<p> The possible units include:</p>
<dl>
<dt><code>second , s</code></p>
<dd>
<dt><code>minute , m</code></p>
<dd>
<dt><code>hour , h</code></p>
<dd>
<dt><code>day</code></p>
<dd>
<dt><code>week</code></p>
<dd>seven days</p>
<dt><code>month</code></p>
<dd>30 days</p>
<dt><code>year</code></p>
<dd>365 days</dl>
<p> Units names can be arbitrarily abbreviated (as long as they are unique).</p>
<h2>Return Values</h2>
<p>Fn parse_time returns the number of seconds that represents the expression in Fa timespec or -1 on error. Fn unparse_time and Fn unparse_time_approx return the number of characters written to Fa buf . if the return value is greater than or equal to the Fa len argument, the string was too short and some of the printed characters were discarded.</p>
<h2>Examples</h2>
<pre><code>#include &lt;parse_time.h&gt;
#include &lt;stdio.h&gt;

int main(int argc, char **argv)
{
    int i;
    int result;
    char buf[128];
    print_time_table(stdout);
    for (i = 1; i &lt; argc; i++) {
        result = parse_time(argv[i], &quot;second&quot;);
        if (result == -1) {
            fprintf(stderr, &quot;%s: parse error
&quot;, argv[i]);
            continue;
        }
        printf(&quot;--
&quot;);
        printf(&quot;parse_time = %d
&quot;, result);
        unparse_time(result, buf, sizeof(buf));
        printf(&quot;unparse_time = %s
&quot;, buf);
        unparse_time_approx(result, buf, sizeof(buf));
        printf(&quot;unparse_time_approx = %s
&quot;, buf);
    }
    return 0;
}

$./ a.out &quot;1 minute 30 seconds&quot;
          &quot;90 s&quot;
          &quot;1 y -1 s&quot; 1 year = 365 days 1 month = 30 days 1 week = 7 days 1 day = 24 hours 1 hour = 60 minutes 1 minute = 60 seconds 1 second-- parse_time = 90 unparse_time = 1 minute 30 seconds
    unparse_time_approx = 1 minute-- parse_time = 90 unparse_time = 1 minute 30 seconds
        unparse_time_approx = 1 minute-- parse_time = 31535999 unparse_time = 12 months 4 days 23 hours 59 minutes 59 seconds
            unparse_time_approx = 12 months</code></pre>
<h2>Bugs</h2>
<p>Since Fn parse_time returns -1 on error there is no way to parse &quot;minus one second&quot;. Currently &quot;s&quot; at the end of units is ignored. This is a hack for English plural forms. If these functions are ever localised, this scheme will have to change. </p>
