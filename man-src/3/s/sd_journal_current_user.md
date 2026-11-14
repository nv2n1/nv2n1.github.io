---
title: "sd_journal_current_user(3)"
name: "sd_journal_current_user"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_journal_current_user/"
---

sd_journal_open, sd_journal_open_directory, sd_journal_open_files, sd_journal_open_container, sd_journal_close, sd_journal, SD_JOURNAL_LOCAL_ONLY, SD_JOURNAL_RUNTIME_ONLY, SD_JOURNAL_SYSTEM, SD_JOURNAL_CURRENT_USER - Open the system journal for reading 

<h2>Synopsis</h2><pre>#include &lt;systemd/sd-journal.h&gt;</pre><dl COMPACT><dt> <b>int sd_journal_open(sd_journal&nbsp;<wbr>**</b><i>ret</i><b>, int&nbsp;<wbr></b><i>flags</i><b>);</b>
<dt> <b>int sd_journal_open_directory(sd_journal&nbsp;<wbr>**</b><i>ret</i><b>, const char&nbsp;<wbr>*</b><i>path</i><b>, int&nbsp;<wbr></b><i>flags</i><b>);</b>
<dt> <b>int sd_journal_open_files(sd_journal&nbsp;<wbr>**</b><i>ret</i><b>, const char&nbsp;<wbr>**</b><i>paths</i><b>, int&nbsp;<wbr></b><i>flags</i><b>);</b>
<dt> <b>int sd_journal_open_container(sd_journal&nbsp;<wbr>**</b><i>ret</i><b>, const char&nbsp;<wbr>*</b><i>machine</i><b>, int&nbsp;<wbr></b><i>flags</i><b>);</b>
<dt> <b>void sd_journal_close(sd_journal&nbsp;<wbr>*</b><i>j</i><b>);</b></dl><h2>Description</h2><b>sd_journal_open()</b>
<dd>opens the log journal for reading. It will find all journal files automatically and interleave them automatically when reading. As first argument it takes a pointer to a <i>sd_journal</i> pointer, which on success will contain a journal context object. The second argument is a flags field, which may consist of the following flags ORed together: <b>SD_JOURNAL_LOCAL_ONLY</b> makes sure only journal files generated on the local machine will be opened. <b>SD_JOURNAL_RUNTIME_ONLY</b> makes sure only volatile journal files will be opened, excluding those which are stored on persistent storage. <b>SD_JOURNAL_SYSTEM</b> will cause journal files of system services and the kernel (in opposition to user session processes) to be opened. <b>SD_JOURNAL_CURRENT_USER</b> will cause journal files of the current user to be opened. If neither <b>SD_JOURNAL_SYSTEM</b> nor <b>SD_JOURNAL_CURRENT_USER</b> are specified, all journal file types will be opened. 

 <b>sd_journal_open_directory()</b> is similar to <b>sd_journal_open()</b> but takes an absolute directory path as argument. All journal files in this directory will be opened and interleaved automatically. This call also takes a flags argument, but it must be passed as 0 as no flags are currently understood for this call. 

 <b>sd_journal_open_files()</b> is similar to <b>sd_journal_open()</b> but takes a <b>NULL</b>-terminated list of file paths to open. All files will be opened and interleaved automatically. This call also takes a flags argument, but it must be passed as 0 as no flags are currently understood for this call. Please note that in the case of a live journal, this function is only useful for debugging, because individual journal files can be rotated at any moment, and the opening of specific files is inherently racy. 

 <b>sd_journal_open_container()</b> is similar to <b>sd_journal_open()</b> but opens the journal files of a running OS container. The specified machine name refers to a container that is registered with <b><a HREF="/docs/linux/man/8-systemd-machined/">systemd-machined</a></b>(8). 

 <i>sd_journal</i> objects cannot be used in the child after a fork. Functions which take a journal object as an argument (<b>sd_journal_next()</b> and others) will return <b>-ECHILD</b> after a fork. 

 <b>sd_journal_close()</b> will close the journal context allocated with <b>sd_journal_open()</b> or <b>sd_journal_open_directory()</b> and free its resources. 

 When opening the journal only journal files accessible to the calling user will be opened. If journal files are not accessible to the caller, this will be silently ignored. 

 See <b><a HREF="/docs/linux/man/3-sd_journal_next/">sd_journal_next</a></b>(3) for an example of how to iterate through the journal after opening it with <b>sd_journal_open()</b>. 

 A journal context object returned by <b>sd_journal_open()</b> references a specific journal entry as <i>current</i> entry, similar to a file seek index in a classic file system file, but without absolute positions. It may be altered with <b><a HREF="/docs/linux/man/3-sd_journal_next/">sd_journal_next</a></b>(3) and <b><a HREF="/docs/linux/man/3-sd_journal_seek_head/">sd_journal_seek_head</a></b>(3) and related calls. The current entry position may be exported in <i>cursor</i> strings, as accessible via <b><a HREF="/docs/linux/man/3-sd_journal_get_cursor/">sd_journal_get_cursor</a></b>(3). Cursor strings may be used to globally identify a specific journal entry in a stable way and then later to seek to it (or if the specific entry is not available locally, to its closest entry in time) <b><a HREF="/docs/linux/man/3-sd_journal_seek_cursor/">sd_journal_seek_cursor</a></b>(3). 

 Notification of journal changes is available via <b>sd_journal_get_fd()</b> and related calls.
<h2>Return Value</h2>The <b>sd_journal_open()</b>, <b>sd_journal_open_directory()</b>, and <b>sd_journal_open_files()</b> calls return 0 on success or a negative errno-style error code. <b>sd_journal_close()</b> returns nothing.
<h2>Notes</h2>The <b>sd_journal_open()</b>, <b>sd_journal_open_directory()</b> and <b>sd_journal_close()</b> interfaces are available as a shared library, which can be compiled and linked to with the <b>libsystemd</b>&nbsp;<wbr><b><a HREF="/docs/linux/man/1-pkg-config/">pkg-config</a></b>(1) file.
<h2>History</h2><b>sd_journal_open()</b>, <b>sd_journal_close()</b>, <b>SD_JOURNAL_LOCAL_ONLY</b>, <b>SD_JOURNAL_RUNTIME_ONLY</b>, <b>SD_JOURNAL_SYSTEM_ONLY</b> were added in systemd-38. 

 <b>sd_journal_open_directory()</b> was added in systemd-187. 

 <b>SD_JOURNAL_SYSTEM</b>, <b>SD_JOURNAL_CURRENT_USER</b>, and <b>sd_journal_open_files()</b> were added in systemd-205. <b>SD_JOURNAL_SYSTEM_ONLY</b> was deprecated.
<h2>See Also</h2><b><a HREF="/docs/linux/man/1-systemd/">systemd</a></b>(1), <b><a HREF="/docs/linux/man/3-sd-journal/">sd-journal</a></b>(3), <b><a HREF="/docs/linux/man/3-sd_journal_next/">sd_journal_next</a></b>(3), <b><a HREF="/docs/linux/man/3-sd_journal_get_data/">sd_journal_get_data</a></b>(3), <b><a HREF="/docs/linux/man/8-systemd-machined/">systemd-machined</a></b>(8)
