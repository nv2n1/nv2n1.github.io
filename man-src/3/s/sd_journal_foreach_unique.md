---
title: "sd_journal_foreach_unique(3)"
name: "sd_journal_foreach_unique"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_journal_foreach_unique/"
---

sd_journal_query_unique, sd_journal_enumerate_unique, sd_journal_restart_unique, SD_JOURNAL_FOREACH_UNIQUE - Read unique data fields from the journal 

<h2>Synopsis</h2><pre>#include &lt;systemd/sd-journal.h&gt;</pre><dl COMPACT><dt> <b>int sd_journal_query_unique(sd_journal&nbsp;<wbr>*</b><i>j</i><b>, const char&nbsp;<wbr>*</b><i>field</i><b>);</b>
<dt> <b>int sd_journal_enumerate_unique(sd_journal&nbsp;<wbr>*</b><i>j</i><b>, const void&nbsp;<wbr>**</b><i>data</i><b>, size_t&nbsp;<wbr>*</b><i>length</i><b>);</b>
<dt> <b>void sd_journal_restart_unique(sd_journal&nbsp;<wbr>*</b><i>j</i><b>);</b>
<dt> <b>SD_JOURNAL_FOREACH_UNIQUE(sd_journal&nbsp;<wbr>*</b><i>j</i><b>, const void&nbsp;<wbr>*</b><i>data</i><b>, size_t&nbsp;<wbr></b><i>length</i><b>);</b></dl><h2>Description</h2><b>sd_journal_query_unique()</b>
<dd>queries the journal for all unique values the specified field can take. It takes two arguments: the journal to query and the field name to look for. Well-known field names are listed on <b><a HREF="/docs/linux/man/7-systemd-journal-fields/">systemd.journal-fields</a></b>(7). Field names must be specified without a trailing '='. After this function has been executed successfully the field values may be queried using <b>sd_journal_enumerate_unique()</b>. Invoking this call a second time will change the field name being queried and reset the enumeration index to the first field value that matches. 

 <b>sd_journal_enumerate_unique()</b> may be used to iterate through all data fields which match the previously selected field name as set with <b>sd_journal_query_unique()</b>. On each invocation the next field data matching the field name is returned. The order of the returned data fields is not defined. It takes three arguments: the journal context object, plus a pair of pointers to pointer/size variables where the data object and its size shall be stored in. The returned data is in a read-only memory map and is only valid until the next invocation of <b>sd_journal_enumerate_unique()</b>. Note that the data returned will be prefixed with the field name and '='. Note that this call is subject to the data field size threshold as controlled by <b>sd_journal_set_data_threshold()</b>. 

 <b>sd_journal_restart_unique()</b> resets the data enumeration index to the beginning of the list. The next invocation of <b>sd_journal_enumerate_unique()</b> will return the first field data matching the field name again. 

 Note that the <b>SD_JOURNAL_FOREACH_UNIQUE()</b> macro may be used as a handy wrapper around <b>sd_journal_restart_unique()</b> and <b>sd_journal_enumerate_unique()</b>. 

 Note that these functions currently are not influenced by matches set with <b>sd_journal_add_match()</b> but this might change in a later version of this software.
<h2>Return Value</h2><b>sd_journal_query_unique()</b> returns 0 on success or a negative errno-style error code. <b>sd_journal_enumerate_unique()</b> returns a positive integer if the next field data has been read, 0 when no more fields are known, or a negative errno-style error code. <b>sd_journal_restart_unique()</b> returns nothing.
<h2>Notes</h2>The <b>sd_journal_query_unique()</b>, <b>sd_journal_enumerate_unique()</b> and <b>sd_journal_restart_unique()</b> interfaces are available as a shared library, which can be compiled and linked to with the <b>libsystemd</b>&nbsp;<wbr><b><a HREF="/docs/linux/man/1-pkg-config/">pkg-config</a></b>(1) file.
<h2>Examples</h2>Use the <b>SD_JOURNAL_FOREACH_UNIQUE</b> macro to iterate through all values a field of the journal can take. The following example lists all unit names referenced in the journal: 

<dl COMPACT><dd><pre>#include &lt;stdio.h&gt;
#include &lt;string.h&gt;
#include &lt;systemd/sd-journal.h&gt;
int main(int argc, char *argv[]) {
 sd_journal *j;
 const void *d;
 size_t l;
 int r;
 r = sd_journal_open(&amp;j, SD_JOURNAL_LOCAL_ONLY);
 if (r &lt; 0) {
 fprintf(stderr, &quot;Failed to open journal: %s\n&quot;, strerror(-r));
 return 1;
 }
 r = sd_journal_query_unique(j, &quot;_SYSTEMD_UNIT&quot;);
 if (r &lt; 0) {
 fprintf(stderr, &quot;Failed to query journal: %s\n&quot;, strerror(-r));
 return 1;
 }
 SD_JOURNAL_FOREACH_UNIQUE(j, d, l)
 printf(&quot;%.*s\n&quot;, (int) l, (const char*) d);
 sd_journal_close(j);
 return 0;
}</pre></dl><h2>See Also</h2><b><a HREF="/docs/linux/man/1-systemd/">systemd</a></b>(1), <b><a HREF="/docs/linux/man/7-systemd-journal-fields/">systemd.journal-fields</a></b>(7), <b><a HREF="/docs/linux/man/3-sd-journal/">sd-journal</a></b>(3), <b><a HREF="/docs/linux/man/3-sd_journal_open/">sd_journal_open</a></b>(3), <b><a HREF="/docs/linux/man/3-sd_journal_get_data/">sd_journal_get_data</a></b>(3), <b><a HREF="/docs/linux/man/3-sd_journal_add_match/">sd_journal_add_match</a></b>(3)
