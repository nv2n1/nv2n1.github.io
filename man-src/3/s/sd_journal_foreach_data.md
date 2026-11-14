---
title: "sd_journal_foreach_data(3)"
name: "sd_journal_foreach_data"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_journal_foreach_data/"
---

sd_journal_get_data, sd_journal_enumerate_data, sd_journal_restart_data, SD_JOURNAL_FOREACH_DATA, sd_journal_set_data_threshold, sd_journal_get_data_threshold - Read data fields from the current journal entry 

<h2>Synopsis</h2><pre>#include &lt;systemd/sd-journal.h&gt;</pre><dl COMPACT><dt> <b>int sd_journal_get_data(sd_journal&nbsp;<wbr>*</b><i>j</i><b>, const char&nbsp;<wbr>*</b><i>field</i><b>, const void&nbsp;<wbr>**</b><i>data</i><b>, size_t&nbsp;<wbr>*</b><i>length</i><b>);</b>
<dt> <b>int sd_journal_enumerate_data(sd_journal&nbsp;<wbr>*</b><i>j</i><b>, const void&nbsp;<wbr>**</b><i>data</i><b>, size_t&nbsp;<wbr>*</b><i>length</i><b>);</b>
<dt> <b>void sd_journal_restart_data(sd_journal&nbsp;<wbr>*</b><i>j</i><b>);</b>
<dt> <b>SD_JOURNAL_FOREACH_DATA(sd_journal&nbsp;<wbr>*</b><i>j</i><b>, const void&nbsp;<wbr>*</b><i>data</i><b>, size_t&nbsp;<wbr></b><i>length</i><b>);</b>
<dt> <b>int sd_journal_set_data_threshold(sd_journal&nbsp;<wbr>*</b><i>j</i><b>, size_t&nbsp;<wbr></b><i>sz</i><b>);</b>
<dt> <b>int sd_journal_get_data_threshold(sd_journal&nbsp;<wbr>*</b><i>j</i><b>, size_t&nbsp;<wbr>*</b><i>sz</i><b>);</b></dl><h2>Description</h2><b>sd_journal_get_data()</b>
<dd>gets the data object associated with a specific field from the current journal entry. It takes four arguments: the journal context object, a string with the field name to request, plus a pair of pointers to pointer/size variables where the data object and its size shall be stored in. The field name should be an entry field name. Well-known field names are listed in <b><a HREF="/docs/linux/man/7-systemd-journal-fields/">systemd.journal-fields</a></b>(7). The returned data is in a read-only memory map and is only valid until the next invocation of <b>sd_journal_get_data()</b> or <b>sd_journal_enumerate_data()</b>, or the read pointer is altered. Note that the data returned will be prefixed with the field name and '='. Also note that by default data fields larger than 64K might get truncated to 64K. This threshold may be changed and turned off with <b>sd_journal_set_data_threshold()</b> (see below). 

 <b>sd_journal_enumerate_data()</b> may be used to iterate through all fields of the current entry. On each invocation the data for the next field is returned. The order of these fields is not defined. The data returned is in the same format as with <b>sd_journal_get_data()</b> and also follows the same life-time semantics. 

 <b>sd_journal_restart_data()</b> resets the data enumeration index to the beginning of the entry. The next invocation of <b>sd_journal_enumerate_data()</b> will return the first field of the entry again. 

 Note that the <b>SD_JOURNAL_FOREACH_DATA()</b> macro may be used as a handy wrapper around <b>sd_journal_restart_data()</b> and <b>sd_journal_enumerate_data()</b>. 

 Note that these functions will not work before <b><a HREF="/docs/linux/man/3-sd_journal_next/">sd_journal_next</a></b>(3) (or related call) has been called at least once, in order to position the read pointer at a valid entry. 

 <b>sd_journal_set_data_threshold()</b> may be used to change the data field size threshold for data returned by <b>sd_journal_get_data()</b>, <b>sd_journal_enumerate_data()</b> and <b>sd_journal_enumerate_unique()</b>. This threshold is a hint only: it indicates that the client program is interested only in the initial parts of the data fields, up to the threshold in size -- but the library might still return larger data objects. That means applications should not rely exclusively on this setting to limit the size of the data fields returned, but need to apply a explicit size limit on the returned data as well. This threshold defaults to 64K by default. To retrieve the complete data fields this threshold should be turned off by setting it to 0, so that the library always returns the complete data objects. It is recommended to set this threshold as low as possible since this relieves the library from having to decompress large compressed data objects in full. 

 <b>sd_journal_get_data_threshold()</b> returns the currently configured data field size threshold.
<h2>Return Value</h2><b>sd_journal_get_data()</b> returns 0 on success or a negative errno-style error code. If the current entry does not include the specified field, -ENOENT is returned. If <b><a HREF="/docs/linux/man/3-sd_journal_next/">sd_journal_next</a></b>(3) has not been called at least once, -EADDRNOTAVAIL is returned. <b>sd_journal_enumerate_data()</b> returns a positive integer if the next field has been read, 0 when no more fields are known, or a negative errno-style error code. <b>sd_journal_restart_data()</b> returns nothing. <b>sd_journal_set_data_threshold()</b> and <b>sd_journal_get_threshold()</b> return 0 on success or a negative errno-style error code.
<h2>Notes</h2>The <b>sd_journal_get_data()</b>, <b>sd_journal_enumerate_data()</b>, <b>sd_journal_restart_data()</b>, <b>sd_journal_set_data_threshold()</b> and <b>sd_journal_get_data_threshold()</b> interfaces are available as a shared library, which can be compiled and linked to with the <b>libsystemd</b>&nbsp;<wbr><b><a HREF="/docs/linux/man/1-pkg-config/">pkg-config</a></b>(1) file.
<h2>Examples</h2>See <b><a HREF="/docs/linux/man/3-sd_journal_next/">sd_journal_next</a></b>(3) for a complete example how to use <b>sd_journal_get_data()</b>. 

 Use the <b>SD_JOURNAL_FOREACH_DATA</b> macro to iterate through all fields of the current journal entry: 

<dl COMPACT><dd><pre>...
int print_fields(sd_journal *j) {
 const void *data;
 size_t length;
 SD_JOURNAL_FOREACH_DATA(j, data, length)
 printf(&quot;%.*s\n&quot;, (int) length, data);
}
...</pre></dl><h2>See Also</h2><b><a HREF="/docs/linux/man/1-systemd/">systemd</a></b>(1), <b><a HREF="/docs/linux/man/7-systemd-journal-fields/">systemd.journal-fields</a></b>(7), <b><a HREF="/docs/linux/man/3-sd-journal/">sd-journal</a></b>(3), <b><a HREF="/docs/linux/man/3-sd_journal_open/">sd_journal_open</a></b>(3), <b><a HREF="/docs/linux/man/3-sd_journal_next/">sd_journal_next</a></b>(3), <b><a HREF="/docs/linux/man/3-sd_journal_get_realtime_usec/">sd_journal_get_realtime_usec</a></b>(3), <b><a HREF="/docs/linux/man/3-sd_journal_query_unique/">sd_journal_query_unique</a></b>(3)
