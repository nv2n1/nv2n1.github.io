---
title: "sd_journal_foreach_backwards(3)"
name: "sd_journal_foreach_backwards"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_journal_foreach_backwards/"
---

sd_journal_next, sd_journal_previous, sd_journal_next_skip, sd_journal_previous_skip, SD_JOURNAL_FOREACH, SD_JOURNAL_FOREACH_BACKWARDS - Advance or set back the read pointer in the journal 

<h2>Synopsis</h2><pre>#include &lt;systemd/sd-journal.h&gt;</pre><dl COMPACT><dt> <b>int sd_journal_next(sd_journal&nbsp;<wbr>*</b><i>j</i><b>);</b>
<dt> <b>int sd_journal_previous(sd_journal&nbsp;<wbr>*</b><i>j</i><b>);</b>
<dt> <b>int sd_journal_next_skip(sd_journal&nbsp;<wbr>*</b><i>j</i><b>, uint64_t&nbsp;<wbr></b><i>skip</i><b>);</b>
<dt> <b>int sd_journal_previous_skip(sd_journal&nbsp;<wbr>*</b><i>j</i><b>, uint64_t&nbsp;<wbr></b><i>skip</i><b>);</b>
<dt> <b>SD_JOURNAL_FOREACH(sd_journal&nbsp;<wbr>*</b><i>j</i><b>);</b>
<dt> <b>SD_JOURNAL_FOREACH_BACKWARDS(sd_journal&nbsp;<wbr>*</b><i>j</i><b>);</b></dl><h2>Description</h2><b>sd_journal_next()</b>
<dd>advances the read pointer into the journal by one entry. The only argument taken is a journal context object as allocated via <b><a HREF="/docs/linux/man/3-sd_journal_open/">sd_journal_open</a></b>(3). After successful invocation the entry may be read with functions such as <b><a HREF="/docs/linux/man/3-sd_journal_get_data/">sd_journal_get_data</a></b>(3). 

 Similarly, <b>sd_journal_previous()</b> sets the read pointer back one entry. 

 <b>sd_journal_next_skip()</b> and <b>sd_journal_previous_skip()</b> advance/set back the read pointer by multiple entries at once, as specified in the <i>skip</i> parameter. 

 The journal is strictly ordered by reception time, and hence advancing to the next entry guarantees that the entry then pointing to is later in time than then previous one, or has the same timestamp. 

 Note that <b><a HREF="/docs/linux/man/3-sd_journal_get_data/">sd_journal_get_data</a></b>(3) and related calls will fail unless <b>sd_journal_next()</b> has been invoked at least once in order to position the read pointer on a journal entry. 

 Note that the <b>SD_JOURNAL_FOREACH()</b> macro may be used as a wrapper around <b><a HREF="/docs/linux/man/3-sd_journal_seek_head/">sd_journal_seek_head</a></b>(3) and <b>sd_journal_next()</b> in order to make iterating through the journal easier. See below for an example. Similarly, <b>SD_JOURNAL_FOREACH_BACKWARDS()</b> may be used for iterating the journal in reverse order.
<h2>Return Value</h2>The four calls return the number of entries advanced/set back on success or a negative errno-style error code. When the end or beginning of the journal is reached, a number smaller than requested is returned. More specifically, if <b>sd_journal_next()</b> or <b>sd_journal_previous()</b> reach the end/beginning of the journal they will return 0, instead of 1 when they are successful. This should be considered an EOF marker.
<h2>Notes</h2>The <b>sd_journal_next()</b>, <b>sd_journal_previous()</b>, <b>sd_journal_next_skip()</b> and <b>sd_journal_previous_skip()</b> interfaces are available as a shared library, which can be compiled and linked to with the <b>libsystemd</b>&nbsp;<wbr><b><a HREF="/docs/linux/man/1-pkg-config/">pkg-config</a></b>(1) file.
<h2>Examples</h2>Iterating through the journal: 

<dl COMPACT><dd><pre>#include &lt;stdio.h&gt;
#include &lt;string.h&gt;
#include &lt;systemd/sd-journal.h&gt;
int main(int argc, char *argv[]) {
 int r;
 sd_journal *j;
 r = sd_journal_open(&amp;j, SD_JOURNAL_LOCAL_ONLY);
 if (r &lt; 0) {
 fprintf(stderr, &quot;Failed to open journal: %s\n&quot;, strerror(-r));
 return 1;
 }
 SD_JOURNAL_FOREACH(j) {
 const char *d;
 size_t l;
 r = sd_journal_get_data(j, &quot;MESSAGE&quot;, (const void **)&amp;d, &amp;l);
 if (r &lt; 0) {
 fprintf(stderr, &quot;Failed to read message field: %s\n&quot;, strerror(-r));
 continue;
 }
 printf(&quot;%.*s\n&quot;, (int) l, d);
 }
 sd_journal_close(j);
 return 0;
}</pre></dl><h2>See Also</h2><b><a HREF="/docs/linux/man/1-systemd/">systemd</a></b>(1), <b><a HREF="/docs/linux/man/3-sd-journal/">sd-journal</a></b>(3), <b><a HREF="/docs/linux/man/3-sd_journal_open/">sd_journal_open</a></b>(3), <b><a HREF="/docs/linux/man/3-sd_journal_get_data/">sd_journal_get_data</a></b>(3), <b><a HREF="/docs/linux/man/3-sd_journal_get_realtime_usec/">sd_journal_get_realtime_usec</a></b>(3), <b><a HREF="/docs/linux/man/3-sd_journal_get_cursor/">sd_journal_get_cursor</a></b>(3)
