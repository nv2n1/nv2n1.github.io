---
title: "sd_journal_previous_skip(3)"
name: "sd_journal_previous_skip"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_journal_previous_skip/"
description: "sd_journal_next, sd_journal_previous, sd_journal_next_skip, sd_journal_previous_skip, SD_JOURNAL_FOREACH, SD_JOURNAL_FOREACH_BACKWARDS – Advance or set back the read pointer in the journal"
---

<p>sd_journal_next, sd_journal_previous, sd_journal_next_skip, sd_journal_previous_skip, SD_JOURNAL_FOREACH, SD_JOURNAL_FOREACH_BACKWARDS &#8211; Advance or set back the read pointer in the journal</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;systemd/sd-journal.h&gt;

int sd_journal_next(sd_journal *j);

int sd_journal_previous(sd_journal *j);

int sd_journal_next_skip(sd_journal *j, uint64_t skip);

int sd_journal_previous_skip(sd_journal *j, uint64_t skip);

SD_JOURNAL_FOREACH(sd_journal *j);

SD_JOURNAL_FOREACH_BACKWARDS(sd_journal *j);</code></pre>
<h2>Description</h2>
<p><code>sd_journal_next()</code></p>
<dd>advances the read pointer into the journal by one entry. The only argument taken is a journal context object as allocated via <code><a href="/docs/linux/man/3-sd_journal_open/">sd_journal_open</a></code>(3). After successful invocation the entry may be read with functions such as <code><a href="/docs/linux/man/3-sd_journal_get_data/">sd_journal_get_data</a></code>(3). </p>
<p> Similarly, <code>sd_journal_previous()</code> sets the read pointer back one entry. </p>
<p> <code>sd_journal_next_skip()</code> and <code>sd_journal_previous_skip()</code> advance/set back the read pointer by multiple entries at once, as specified in the <i>skip</i> parameter. </p>
<p> The journal is strictly ordered by reception time, and hence advancing to the next entry guarantees that the entry then pointing to is later in time than then previous one, or has the same timestamp. </p>
<p> Note that <code><a href="/docs/linux/man/3-sd_journal_get_data/">sd_journal_get_data</a></code>(3) and related calls will fail unless <code>sd_journal_next()</code> has been invoked at least once in order to position the read pointer on a journal entry. </p>
<p> Note that the <code>SD_JOURNAL_FOREACH()</code> macro may be used as a wrapper around <code><a href="/docs/linux/man/3-sd_journal_seek_head/">sd_journal_seek_head</a></code>(3) and <code>sd_journal_next()</code> in order to make iterating through the journal easier. See below for an example. Similarly, <code>SD_JOURNAL_FOREACH_BACKWARDS()</code> may be used for iterating the journal in reverse order.</p>
<h2>Return Value</h2>
<p>The four calls return the number of entries advanced/set back on success or a negative errno-style error code. When the end or beginning of the journal is reached, a number smaller than requested is returned. More specifically, if <code>sd_journal_next()</code> or <code>sd_journal_previous()</code> reach the end/beginning of the journal they will return 0, instead of 1 when they are successful. This should be considered an EOF marker.</p>
<h2>Notes</h2>
<p>The <code>sd_journal_next()</code>, <code>sd_journal_previous()</code>, <code>sd_journal_next_skip()</code> and <code>sd_journal_previous_skip()</code> interfaces are available as a shared library, which can be compiled and linked to with the <code>libsystemd</code>&nbsp;<wbr><code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) file.</p>
<h2>Examples</h2>
<p>Iterating through the journal: </p>
<pre><code>#include &lt;stdio.h&gt;
#include &lt;string.h&gt;
#include &lt;systemd/sd-journal.h&gt;

int main(int argc, char *argv[])
{
    int r;
    sd_journal *j;
    r = sd_journal_open(&amp;j, SD_JOURNAL_LOCAL_ONLY);
    if (r &lt; 0) {
        fprintf(stderr, &quot;Failed to open journal: %s
&quot;, strerror(-r));
        return 1;
    }
    SD_JOURNAL_FOREACH(j)
    {
        const char *d;
        size_t l;

        r = sd_journal_get_data(j, &quot;MESSAGE&quot;, (const void **)&amp;d, &amp;l);
        if (r &lt; 0) {
            fprintf(stderr, &quot;Failed to read message field: %s
&quot;, strerror(-r));
            continue;
        }

        printf(&quot;%.*s
&quot;, (int)l, d);
    }
    sd_journal_close(j);
    return 0;
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-sd-journal/">sd-journal</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_open/">sd_journal_open</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_get_data/">sd_journal_get_data</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_get_realtime_usec/">sd_journal_get_realtime_usec</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_get_cursor/">sd_journal_get_cursor</a></code>(3) </p>
