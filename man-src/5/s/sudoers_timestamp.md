---
title: "sudoers_timestamp(5)"
name: "sudoers_timestamp"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sudoers_timestamp/"
description: "sudoers_timestamp – Sudoers Time Stamp Format"
---

<p>Sudo 1.9.9</p>
<h2>Name</h2>
<p><code>sudoers_timestamp</code> &#8211; Sudoers Time Stamp Format</p>
<h2>Description</h2>
<p>The <code>sudoers</code> plugin uses per-user time stamp files for credential caching. Once a user has been authenticated, they may use <code>sudo</code> without a password for a short period of time Po <code>15</code> minutes unless overridden by the <i>timestamp_timeout</i> option Pc . By default, <code>sudoers</code> uses a separate record for each terminal, which means that a user&#8217;s login sessions are authenticated separately. The <i>timestamp_type</i> option can be used to select the type of time stamp record <code>sudoers</code> will use. A multi-record time stamp file format was introduced in <code>sudo</code> 1.8.10 that uses a single file per user. Previously, a separate file was used for each user and terminal combination unless tty-based time stamps were disabled. The new format is extensible and records of multiple types and versions may coexist within the same file. All records, regardless of type or version, begin with a 16-bit version number and a 16-bit record size. </p>
<pre><code>Time stamp records have the following structure :

/* Time stamp entry types */
#define TS_GLOBAL 0x01   /* not restricted by tty or ppid */
#define TS_TTY 0x02      /* restricted by tty */
#define TS_PPID 0x03     /* restricted by ppid */
#define TS_LOCKEXCL 0x04 /* special lock record */

/* Time stamp flags */
#define TS_DISABLED 0x01 /* entry disabled */
#define TS_ANYUID 0x02   /* ignore uid, only valid in key */

    struct timestamp_entry {
    unsigned short version;     /* version number */
    unsigned short size;        /* entry size */
    unsigned short type;        /* TS_GLOBAL, TS_TTY, TS_PPID */
    unsigned short flags;       /* TS_DISABLED, TS_ANYUID */
    uid_t auth_uid;             /* uid to authenticate as */
    pid_t sid;                  /* session ID associated with tty/ppid */
    struct timespec start_time; /* session/ppid start time */
    struct timespec ts;         /* time stamp (CLOCK_MONOTONIC) */
    union {
        dev_t ttydev; /* tty device number */
        pid_t ppid;   /* parent pid */
    } u;
};</code></pre>
<p> The timestamp_entry struct fields are as follows:</p>
<dl>
<dt><code>version</code></p>
<dd>The version number of the timestamp_entry struct. New entries are created with a version number of 2. Records with different version numbers may coexist in the same file but are not inter-operable.</p>
<dt><code>size</code></p>
<dd>The size of the record in bytes.</p>
<dt><code>type</code></p>
<dd>The record type, currently <code>TS_GLOBAL</code> <code>TS_TTY</code> or <code>TS_PPID</code></p>
<dt><code>flags</code></p>
<dd>Zero or more record flags which can be bit-wise ORed together. Supported flags are <code>TS_DISABLED</code> for records disabled via <code>sudo</code> &#8211;<code>k</code> and <code>TS_ANYUID</code> which is used only when matching records.</p>
<dt><code>auth_uid</code></p>
<dd>The user-ID that was used for authentication. Depending on the value of the <i>rootpw</i> <i>runaspw</i> and <i>targetpw</i> options, the user-ID may be that of the invoking user, the root user, the default runas user or the target user.</p>
<dt><code>sid</code></p>
<dd>The ID of the user&#8217;s terminal session, if present. The session ID is only used when matching records of type <code>TS_TTY</code></p>
<dt><code>start_time</code></p>
<dd>The start time of the session leader for records of type <code>TS_TTY</code> or of the parent process for records of type <code>TS_PPID</code> The <i>start_time</i> is used to help prevent re-use of a time stamp record after a user has logged out. Not all systems support a method to easily retrieve a process&#8217;s start time. The <i>start_time</i> field was added in <code>sudoers</code> version 1.8.22 for the second revision of the timestamp_entry struct.</p>
<dt><code>ts</code></p>
<dd>The actual time stamp. A monotonic time source (which does not move backward) is used if the system supports it. Where possible, <code>sudoers</code> uses a monotonic timer that increments even while the system is suspended. The value of <i>ts</i> is updated each time a command is run via <code>sudo</code> If the difference between <i>ts</i> and the current time is less than the value of the <i>timestamp_timeout</i> option, no password is required.</p>
<dt><code>u.ttydev</code></p>
<dd>The device number of the terminal associated with the session for records of type <code>TS_TTY</code></p>
<dt><code>u.ppid</code></p>
<dd>The ID of the parent process for records of type <code>TS_PPID</code></dl>
<h2>Locking</h2>
<p>In <code>sudoers</code> versions 1.8.10 through 1.8.14, the entire time stamp file was locked for exclusive access when reading or writing to the file. Starting in <code>sudoers</code> 1.8.15, individual records are locked in the time stamp file instead of the entire file and the lock is held for a longer period of time. This scheme is described below. </p>
<p> The first record in the time stamp file is of type <code>TS_LOCKEXCL</code> and is used as a <i>lock</i> record to prevent more than one <code>sudo</code> process from adding a new record at the same time. Once the desired time stamp record has been located or created (and locked), the <code>TS_LOCKEXCL</code> record is unlocked. The lock on the individual time stamp record, however, is held until authentication is complete. This allows <code>sudoers</code> to avoid prompting for a password multiple times when it is used more than once in a pipeline. </p>
<p> Records of type <code>TS_GLOBAL</code> cannot be locked for a long period of time since doing so would interfere with other <code>sudo</code> processes. Instead, a separate lock record is used to prevent multiple <code>sudo</code> processes using the same terminal (or parent process ID) from prompting for a password as the same time.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-sudoers/">sudoers</a>(5), <a href="/docs/linux/man/8-sudo/">sudo</a>(8)</p>
<h2>History</h2>
<p>Originally, <code>sudo</code> used a single zero-length file per user and the file&#8217;s modification time was used as the time stamp. Later versions of <code>sudo</code> added restrictions on the ownership of the time stamp files and directory as well as checks on the validity of the time stamp itself. Notable changes were introduced in the following <code>sudo</code> versions:</p>
<dl>
<dt><code>1.4.0</code></p>
<dd>Support for tty-based time stamp file was added by appending the terminal name to the time stamp file name.</p>
<dt><code>1.6.2</code></p>
<dd>The time stamp file was replaced by a per-user directory which contained any tty-based time stamp files.</p>
<dt><code>1.6.3p2</code></p>
<dd>The target user name was added to the time stamp file name when the <i>targetpw</i> option was set.</p>
<dt><code>1.7.3</code></p>
<dd>Information about the terminal device was stored in tty-based time stamp files for validity checks. This included the terminal device numbers, inode number and, on systems where it was not updated when the device was written to, the inode change time. This helped prevent re-use of the time stamp file after logout.</p>
<dt><code>1.8.6p7</code></p>
<dd>The terminal session ID was added to tty-based time stamp files to prevent re-use of the time stamp by the same user in a different terminal session. It also helped prevent re-use of the time stamp file on systems where the terminal device&#8217;s inode change time was updated by writing.</p>
<dt><code>1.8.10</code></p>
<dd>A new, multi-record time stamp file format was introduced that uses a single file per user. The terminal device&#8217;s change time was not included since most systems now update the change time after a write is performed as required by POSIX.</p>
<dt><code>1.8.15</code></p>
<dd>Individual records are locked in the time stamp file instead of the entire file and the lock is held until authentication is complete.</p>
<dt><code>1.8.22</code></p>
<dd>The start time of the terminal session leader or parent process is now stored in non-global time stamp records. This prevents re-use of the time stamp file after logout in most cases. </p>
<p> Support was added for the kernel-based tty time stamps available in Ox which do not use an on-disk time stamp file.</dl>
<h2>Authors</h2>
<p>Many people have worked on <code>sudo</code> over the years; this version consists of code written primarily by: </p>
<blockquote><p> An Todd C. Miller </p></blockquote>
<p> See the CONTRIBUTORS file in the <code>sudo</code> distribution (<a rel="nofollow" href="https://www.sudo.ws/contributors.html)">https://www.sudo.ws/contributors.html)</a> for an exhaustive list of people who have contributed to <code>sudo</code></p>
<h2>Bugs</h2>
<p>If you feel you have found a bug in <code>sudo</code> please submit a bug report at <a rel="nofollow" href="https://bugzilla.sudo.ws/">https://bugzilla.sudo.ws/</a></p>
<h2>Support</h2>
<p>Limited free support is available via the sudo-users mailing list, see <a rel="nofollow" href="https://www.sudo.ws/mailman/listinfo/sudo-users">https://www.sudo.ws/mailman/listinfo/sudo-users</a> to subscribe or search the archives.</p>
<h2>Disclaimer</h2>
<p><code>sudo</code> is provided &#8220;AS IS&#8221; and any express or implied warranties, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose are disclaimed. See the LICENSE file distributed with <code>sudo</code> or <a rel="nofollow" href="https://www.sudo.ws/license.html">https://www.sudo.ws/license.html</a> for complete details.</p>
