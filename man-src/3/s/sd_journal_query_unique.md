---
title: "sd_journal_query_unique(3)"
name: "sd_journal_query_unique"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_journal_query_unique/"
description: "sd_journal_query_unique, sd_journal_enumerate_unique, sd_journal_restart_unique, SD_JOURNAL_FOREACH_UNIQUE – Read unique data fields from the journal"
---

<p>sd_journal_query_unique, sd_journal_enumerate_unique, sd_journal_restart_unique, SD_JOURNAL_FOREACH_UNIQUE &#8211; Read unique data fields from the journal</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;systemd/sd-journal.h&gt;

int sd_journal_query_unique(sd_journal *j, const char *field);

int sd_journal_enumerate_unique(sd_journal *j, const void **data, size_t *length);

void sd_journal_restart_unique(sd_journal *j);

SD_JOURNAL_FOREACH_UNIQUE(sd_journal *j, const void *data, size_t length);</code></pre>
<h2>Description</h2>
<p><code>sd_journal_query_unique()</code></p>
<dd>queries the journal for all unique values the specified field can take. It takes two arguments: the journal to query and the field name to look for. Well-known field names are listed on <code><a href="/docs/linux/man/7-systemd-journal-fields/">systemd.journal-fields</a></code>(7). Field names must be specified without a trailing &#8216;=&#8217;. After this function has been executed successfully the field values may be queried using <code>sd_journal_enumerate_unique()</code>. Invoking this call a second time will change the field name being queried and reset the enumeration index to the first field value that matches. </p>
<p> <code>sd_journal_enumerate_unique()</code> may be used to iterate through all data fields which match the previously selected field name as set with <code>sd_journal_query_unique()</code>. On each invocation the next field data matching the field name is returned. The order of the returned data fields is not defined. It takes three arguments: the journal context object, plus a pair of pointers to pointer/size variables where the data object and its size shall be stored in. The returned data is in a read-only memory map and is only valid until the next invocation of <code>sd_journal_enumerate_unique()</code>. Note that the data returned will be prefixed with the field name and &#8216;=&#8217;. Note that this call is subject to the data field size threshold as controlled by <code>sd_journal_set_data_threshold()</code>. </p>
<p> <code>sd_journal_restart_unique()</code> resets the data enumeration index to the beginning of the list. The next invocation of <code>sd_journal_enumerate_unique()</code> will return the first field data matching the field name again. </p>
<p> Note that the <code>SD_JOURNAL_FOREACH_UNIQUE()</code> macro may be used as a handy wrapper around <code>sd_journal_restart_unique()</code> and <code>sd_journal_enumerate_unique()</code>. </p>
<p> Note that these functions currently are not influenced by matches set with <code>sd_journal_add_match()</code> but this might change in a later version of this software.</p>
<h2>Return Value</h2>
<p><code>sd_journal_query_unique()</code> returns 0 on success or a negative errno-style error code. <code>sd_journal_enumerate_unique()</code> returns a positive integer if the next field data has been read, 0 when no more fields are known, or a negative errno-style error code. <code>sd_journal_restart_unique()</code> returns nothing.</p>
<h2>Notes</h2>
<p>The <code>sd_journal_query_unique()</code>, <code>sd_journal_enumerate_unique()</code> and <code>sd_journal_restart_unique()</code> interfaces are available as a shared library, which can be compiled and linked to with the <code>libsystemd</code>&nbsp;<wbr><code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) file.</p>
<h2>Examples</h2>
<p>Use the <code>SD_JOURNAL_FOREACH_UNIQUE</code> macro to iterate through all values a field of the journal can take. The following example lists all unit names referenced in the journal: </p>
<pre><code>#include &lt;stdio.h&gt;
#include &lt;string.h&gt;
#include &lt;systemd/sd-journal.h&gt;

int main(int argc, char *argv[])
{
    sd_journal *j;
    const void *d;
    size_t l;
    int r;

    r = sd_journal_open(&amp;j, SD_JOURNAL_LOCAL_ONLY);
    if (r &lt; 0) {
        fprintf(stderr, &quot;Failed to open journal: %s
&quot;, strerror(-r));
        return 1;
    }
    r = sd_journal_query_unique(j, &quot;_SYSTEMD_UNIT&quot;);
    if (r &lt; 0) {
        fprintf(stderr, &quot;Failed to query journal: %s
&quot;, strerror(-r));
        return 1;
    }
    SD_JOURNAL_FOREACH_UNIQUE(j, d, l)
    printf(&quot;%.*s
&quot;, (int)l, (const char *)d);
    sd_journal_close(j);
    return 0;
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/7-systemd-journal-fields/">systemd.journal-fields</a></code>(7), <code><a href="/docs/linux/man/3-sd-journal/">sd-journal</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_open/">sd_journal_open</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_get_data/">sd_journal_get_data</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_add_match/">sd_journal_add_match</a></code>(3) </p>
