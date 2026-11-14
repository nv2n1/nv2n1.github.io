---
title: "sd_journal_open_files(3)"
name: "sd_journal_open_files"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_journal_open_files/"
description: "sd_journal_open, sd_journal_open_directory, sd_journal_open_files, sd_journal_open_container, sd_journal_close, sd_journal, SD_JOURNAL_LOCAL_ONLY, SD_JOURNAL_RUNTIME_ONLY, SD_JOURNAL_SYSTEM, SD_JOU..."
---

<p>sd_journal_open, sd_journal_open_directory, sd_journal_open_files, sd_journal_open_container, sd_journal_close, sd_journal, SD_JOURNAL_LOCAL_ONLY, SD_JOURNAL_RUNTIME_ONLY, SD_JOURNAL_SYSTEM, SD_JOURNAL_CURRENT_USER &#8211; Open the system journal for reading</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;systemd/sd-journal.h&gt;

int sd_journal_open(sd_journal **ret, int flags);

int sd_journal_open_directory(sd_journal **ret, const char *path, int flags);

int sd_journal_open_files(sd_journal **ret, const char **paths, int flags);

int sd_journal_open_container(sd_journal **ret, const char *machine, int flags);

void sd_journal_close(sd_journal *j);</code></pre>
<h2>Description</h2>
<p><code>sd_journal_open()</code></p>
<dd>opens the log journal for reading. It will find all journal files automatically and interleave them automatically when reading. As first argument it takes a pointer to a <i>sd_journal</i> pointer, which on success will contain a journal context object. The second argument is a flags field, which may consist of the following flags ORed together: <code>SD_JOURNAL_LOCAL_ONLY</code> makes sure only journal files generated on the local machine will be opened. <code>SD_JOURNAL_RUNTIME_ONLY</code> makes sure only volatile journal files will be opened, excluding those which are stored on persistent storage. <code>SD_JOURNAL_SYSTEM</code> will cause journal files of system services and the kernel (in opposition to user session processes) to be opened. <code>SD_JOURNAL_CURRENT_USER</code> will cause journal files of the current user to be opened. If neither <code>SD_JOURNAL_SYSTEM</code> nor <code>SD_JOURNAL_CURRENT_USER</code> are specified, all journal file types will be opened. </p>
<p> <code>sd_journal_open_directory()</code> is similar to <code>sd_journal_open()</code> but takes an absolute directory path as argument. All journal files in this directory will be opened and interleaved automatically. This call also takes a flags argument, but it must be passed as 0 as no flags are currently understood for this call. </p>
<p> <code>sd_journal_open_files()</code> is similar to <code>sd_journal_open()</code> but takes a <code>NULL</code>-terminated list of file paths to open. All files will be opened and interleaved automatically. This call also takes a flags argument, but it must be passed as 0 as no flags are currently understood for this call. Please note that in the case of a live journal, this function is only useful for debugging, because individual journal files can be rotated at any moment, and the opening of specific files is inherently racy. </p>
<p> <code>sd_journal_open_container()</code> is similar to <code>sd_journal_open()</code> but opens the journal files of a running OS container. The specified machine name refers to a container that is registered with <code><a href="/docs/linux/man/8-systemd-machined/">systemd-machined</a></code>(8). </p>
<p> <i>sd_journal</i> objects cannot be used in the child after a fork. Functions which take a journal object as an argument (<code>sd_journal_next()</code> and others) will return <code>-ECHILD</code> after a fork. </p>
<p> <code>sd_journal_close()</code> will close the journal context allocated with <code>sd_journal_open()</code> or <code>sd_journal_open_directory()</code> and free its resources. </p>
<p> When opening the journal only journal files accessible to the calling user will be opened. If journal files are not accessible to the caller, this will be silently ignored. </p>
<p> See <code><a href="/docs/linux/man/3-sd_journal_next/">sd_journal_next</a></code>(3) for an example of how to iterate through the journal after opening it with <code>sd_journal_open()</code>. </p>
<p> A journal context object returned by <code>sd_journal_open()</code> references a specific journal entry as <i>current</i> entry, similar to a file seek index in a classic file system file, but without absolute positions. It may be altered with <code><a href="/docs/linux/man/3-sd_journal_next/">sd_journal_next</a></code>(3) and <code><a href="/docs/linux/man/3-sd_journal_seek_head/">sd_journal_seek_head</a></code>(3) and related calls. The current entry position may be exported in <i>cursor</i> strings, as accessible via <code><a href="/docs/linux/man/3-sd_journal_get_cursor/">sd_journal_get_cursor</a></code>(3). Cursor strings may be used to globally identify a specific journal entry in a stable way and then later to seek to it (or if the specific entry is not available locally, to its closest entry in time) <code><a href="/docs/linux/man/3-sd_journal_seek_cursor/">sd_journal_seek_cursor</a></code>(3). </p>
<p> Notification of journal changes is available via <code>sd_journal_get_fd()</code> and related calls.</p>
<h2>Return Value</h2>
<p>The <code>sd_journal_open()</code>, <code>sd_journal_open_directory()</code>, and <code>sd_journal_open_files()</code> calls return 0 on success or a negative errno-style error code. <code>sd_journal_close()</code> returns nothing.</p>
<h2>Notes</h2>
<p>The <code>sd_journal_open()</code>, <code>sd_journal_open_directory()</code> and <code>sd_journal_close()</code> interfaces are available as a shared library, which can be compiled and linked to with the <code>libsystemd</code>&nbsp;<wbr><code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) file.</p>
<h2>History</h2>
<p><code>sd_journal_open()</code>, <code>sd_journal_close()</code>, <code>SD_JOURNAL_LOCAL_ONLY</code>, <code>SD_JOURNAL_RUNTIME_ONLY</code>, <code>SD_JOURNAL_SYSTEM_ONLY</code> were added in systemd-38. </p>
<p> <code>sd_journal_open_directory()</code> was added in systemd-187. </p>
<p> <code>SD_JOURNAL_SYSTEM</code>, <code>SD_JOURNAL_CURRENT_USER</code>, and <code>sd_journal_open_files()</code> were added in systemd-205. <code>SD_JOURNAL_SYSTEM_ONLY</code> was deprecated.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-sd-journal/">sd-journal</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_next/">sd_journal_next</a></code>(3), <code><a href="/docs/linux/man/3-sd_journal_get_data/">sd_journal_get_data</a></code>(3), <code><a href="/docs/linux/man/8-systemd-machined/">systemd-machined</a></code>(8) </p>
