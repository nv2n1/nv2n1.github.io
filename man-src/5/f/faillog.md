---
title: "faillog(5)"
name: "faillog"
section: "5"
letter: "f"
url: "/docs/linux/man/5-faillog/"
description: "faillog – login failure logging file"
---

<p>faillog &#8211; login failure logging file</p>
<h2>Description</h2>
<p>/var/log/faillog maintains a count of login failures and the limits for each account. The file contains fixed length records, indexed by numerical UID. Each record contains the count of login failures since the last successful login; the maximum number of failures before the account is disabled; the line on which the last login failure occurred; the date of the last login failure; and the duration (in seconds) during which the account will be locked after a failure. The structure of the file is: </p>
<pre><code>struct faillog {
    short fail_cnt;
    short fail_max;
    char fail_line[12];
    time_t fail_time;
    long fail_locktime;
};</code></pre>
<h2>Files</h2>
<p>/var/log/faillog</p>
<dl>
<dd>Failure logging file.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-faillog/">faillog</a></code>(8) </p>
