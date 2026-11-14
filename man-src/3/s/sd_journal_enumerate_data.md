---
title: "sd_journal_enumerate_data(3)"
name: "sd_journal_enumerate_data"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_journal_enumerate_data/"
description: "sd_journal_get_data, sd_journal_enumerate_data, sd_journal_restart_data, SD_JOURNAL_FOREACH_DATA, sd_journal_set_data_threshold, sd_journal_get_data_threshold – Read data fields from the current jo..."
---

<p>sd_journal_get_data, sd_journal_enumerate_data, sd_journal_restart_data, SD_JOURNAL_FOREACH_DATA, sd_journal_set_data_threshold, sd_journal_get_data_threshold &#8211; Read data fields from the current journal entry</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;systemd/sd-journal.h&gt;

int sd_journal_get_data(sd_journal *j, const char *field, const void **data, size_t *length);

int sd_journal_enumerate_data(sd_journal *j, const void **data, size_t *length);

void sd_journal_restart_data(sd_journal *j);

SD_JOURNAL_FOREACH_DATA(sd_journal *j, const void *data, size_t length);

int sd_journal_set_data_threshold(sd_journal *j, size_t sz);

int sd_journal_get_data_threshold(sd_journal *j, size_t *sz);</code></pre>
<h2>Description</h2>
<p><code>sd_journal_get_data()</code></p>
<dd>gets the data object associated with a specific field from the current journal entry. It takes four arguments: the journal context object, a string with the field name to request, plus a pair of pointers to pointer/size variables where the data object and its size shall be stored in. The field name should be an entry field name. Well-known field names are listed in <code><a href="/docs/linux/man/7-systemd-journal-fields/">systemd.journal-fields</a></code>(7). The returned data is in a read-only memory map and is only valid until the next invocation of <code>sd_journal_get_data()</code> or <code>sd_journal_enumerate_data()</code>, or the read pointer is altered. Note that the data returned will be prefixed with the field name and &#8216;=&#8217;. Also note that by default data fields larger than 64K might get truncated to 64K. This threshold may be changed and turned off with <code>sd_journal_set_data_threshold()</code> (see below). </p>
<p> <code>sd_journal_enumerate_data()</code> may be used to iterate through all fields of the current entry. On each invocation the data for the next field is returned. The order of these fields is not defined. The data returned is in the same format as with <code>sd_journal_get_data()</code> and also follows the same life-time semantics. </p>
<p> <code>sd_journal_restart_data()</code> resets the data enumeration index to the beginning of the entry. The next invocation of <code>sd_journal_enumerate_data()</code> will return the first field of the entry again. </p>
<p> Note that the <code>SD_JOURNAL_FOREACH_DATA()</code> macro may be used as a handy wrapper around <code>sd_journal_restart_data()</code> and <code>sd_journal_enumerate_data()</code>. </p>
<p> Note that these functions will not work before <code><a href="/docs/linux/man/3-sd_journal_next/">sd_journal_next</a></code>(3) (or related call) has been called at least once, in order to position the read pointer at a valid entry. </p>
<p> <code>sd_journal_set_data_threshold()</code> may be used to change the data field size threshold for data returned by <code>sd_journal_get_data()</code>, <code>sd_journal_enumerate_data()</code> and <code>sd_journal_enumerate_unique()</code>. This threshold is a hint only: it indicates that the client program is interested only in the initial parts of the data fields, up to the threshold in size &#8212; but the library might still return larger data objects. That means applications should not rely exclusively on this setting to limit the size of the data fields returned, but need to apply a explicit size limit on the returned data as well. This threshold defaults to 64K by default. To retrieve the complete data fields this threshold should be turned off by setting it to 0, so that the library always returns the complete data objects. It is recommended to set this threshold as low as possible since this relieves the library from having to decompress large compressed data objects in full. </p>
<p> <code>sd_journal_get_data_threshold()</code> returns the currently configured data field size threshold.</p>
<h2>Return Value</h2>
<p><code>sd_journal_get_data()</code> returns 0 on success or a negative errno-style error code. If the current entry does not include the specified field, -ENOENT is returned. If <code><a href="/docs/linux/man/3-sd_journal_next/">sd_journal_next</a></code>(3) has not been called at least once, -EADDRNOTAVAIL is returned. <code>sd_journal_enumerate_data()</code> returns a positive integer if the next field has been read, 0 when no more fields are known, or a negative errno-style error code. <code>sd_journal_restart_data()</code> returns nothing. <code>sd_journal_set_data_threshold()</code> and <code>sd_journal_get_threshold()</code> return 0 on success or a negative errno-style error code.</p>
<h2>Notes</h2>
<p>The <code>sd_journal_get_data()</code>, <code>sd_journal_enumerate_data()</code>, <code>sd_journal_restart_data()</code>, <code>sd_journal_set_data_threshold()</code> and <code>sd_journal_get_data_threshold()</code> interfaces are available as a shared library, which can be compiled and linked to with the <code>libsystemd</code>&nbsp;<wbr><code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) file.</p>
<h2>Examples</h2>
<p>See <code><a href="/docs/linux/man/3-sd_journal_next/">sd_journal_next</a></code>(3) for a complete example how to use <code>sd_journal_get_data()</code>. </p>
<p> Use the <code>SD_JOURNAL_FOREACH_DATA</code> macro to iterate through all fields of the current journal entry: </p>
<dl>
<dd>
<pre>...
int print_fields(sd_journal *j) {
 const void *data;
 size_t length;
 SD_JOURNAL_FOREACH_DATA(j, data, length)
 printf(&quot;%.*s
&quot;, (int) length, data);
}
...</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/7-systemd-journal-fields/">systemd.journal-fields</a></code>(7), <code><a href="/docs/linux/man/3-sd-journal/">sd-journal</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_open/">sd_journal_open</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_next/">sd_journal_next</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_get_realtime_usec/">sd_journal_get_realtime_usec</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_query_unique/">sd_journal_query_unique</a></code>(3) </p>
