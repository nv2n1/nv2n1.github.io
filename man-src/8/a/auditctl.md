---
title: "auditctl(8)"
name: "auditctl"
section: "8"
letter: "a"
url: "/docs/linux/man/8-auditctl/"
description: "auditctl – a utility to assist controlling the kernel’s audit system"
---

<p>auditctl &#8211; a utility to assist controlling the kernel&#8217;s audit system</p>
<h2>Synopsis</h2>
<p><code>auditctl</code> [<i>options</i>]</p>
<h2>Description</h2>
<p>The <code>auditctl</code> program is used to configure kernel options related to auditing, to see status of the configuration, and to load discretionary audit rules.</p>
<h2>Configuration Options</h2>
<dl>
<dt><code>-b&nbsp;<wbr></code><i>backlog</i></p>
<dd>Set max number of outstanding audit buffers allowed (Kernel Default=64) If all buffers are full, the failure flag is consulted by the kernel for action.</p>
<dt><code>-c</code></p>
<dd>Continue loading rules in spite of an error. This summarizes the results of loading the rules. The exit code will not be success if any rule fails to load.</p>
<dt><code>-D</code></p>
<dd>Delete all rules and watches. This can take a key option (-k), too.</p>
<dt><code>-e</code> [<code>0</code>..<code>2</code>]</p>
<dd>Set enabled flag. When <code>0</code> is passed, this can be used to temporarily disable auditing. When <code>1</code> is passed as an argument, it will enable auditing. To lock the audit configuration so that it can&#8217;t be changed, pass a <code>2</code> as the argument. Locking the configuration is intended to be the last command in audit.rules for anyone wishing this feature to be active. Any attempt to change the configuration in this mode will be audited and denied. The configuration can only be changed by rebooting the machine.</p>
<dt><code>-f</code> [<code>0</code>..<code>2</code>]</p>
<dd>Set failure mode <code>0</code>=silent <code>1</code>=printk <code>2</code>=panic. This option lets you determine how you want the kernel to handle critical errors. Example conditions where this mode may have an effect includes: transmission errors to userspace audit daemon, backlog limit exceeded, out of kernel memory, and rate limit exceeded. The default value is <code>1</code>. Secure environments will probably want to set this to <code>2</code>.</p>
<dt><code>-h</code></p>
<dd>Help</p>
<dt><code>-i</code></p>
<dd>When given by itself, ignore errors when reading rules from a file. This causes auditctl to always return a success exit code. If passed as an argument to <code>-s</code> then it gives an interpretation of the numbers to human readable words if possible.</p>
<dt><code>&#8211;loginuid-immutable</code></p>
<dd>This option tells the kernel to make loginuids unchangeable once they are set. Changing loginuids requires CAP_AUDIT_CONTROL. So, its not something that can be done by unprivileged users. Setting this makes loginuid tamper-proof, but can cause some problems in certain kinds of containers.</p>
<dt><code>-q&nbsp;<wbr></code><i>mount-point,subtree</i></p>
<dd>If you have an existing directory watch and bind or move mount another subtree in the watched subtree, you need to tell the kernel to make the subtree being mounted equivalent to the directory being watched. If the subtree is already mounted at the time the directory watch is issued, the subtree is automatically tagged for watching. Please note the comma separating the two values. Omitting it will cause errors.</p>
<dt><code>-r&nbsp;<wbr></code><i>rate</i></p>
<dd>Set limit in messages/sec (<code>0</code>=none). If this <i>rate</i> is non-zero and is exceeded, the failure flag is consulted by the kernel for action. The default value is <code>0</code>.</p>
<dt><code>&#8211;reset-lost</code></p>
<dd>Reset the lost record counter shown by the status command.</p>
<dt><code>-R&nbsp;<wbr></code><i>file</i></p>
<dd>Read rules from a <i>file</i>. The rules must be 1 per line and in the order that they are to be executed in. The rule file must be owned by root and not readable by other users or it will be rejected. The rule file may have comments embedded by starting the line with a &#8216;#&#8217; character. Rules that are read from a file are identical to what you would type on a command line except they are not preceded by auditctl (since auditctl is the one executing the file) and you would not use shell escaping since auditctl is reading the file instead of bash.</p>
<dt><code>-t</code></p>
<dd>Trim the subtrees after a mount command.</dl>
<h2>Status Options</h2>
<dl>
<dt><code>-l</code></p>
<dd>List all rules 1 per line. Two more options may be given to this command. You can give either a key option (-k) to list rules that match a key or a (-i) to have a0 through a3 interpreted to help determine the syscall argument values are correct .</p>
<dt><code>-m&nbsp;<wbr></code><i>text</i></p>
<dd>Send a user space message into the audit system. This can only be done if you have CAP_AUDIT_WRITE capability (normally the root user has this). The resulting event will be the USER type.</p>
<dt><code>-s</code></p>
<dd>Report the kernel&#8217;s audit subsystem status. It will tell you the in-kernel values that can be set by <code>-e</code>, <code>-f</code>, <code>-r</code>, and <code>-b</code> options. The pid value is the process number of the audit daemon. Note that a pid of 0 indicates that the audit daemon is not running. The lost entry will tell you how many event records that have been discarded due to the kernel audit queue overflowing. The backlog field tells how many event records are currently queued waiting for auditd to read them. This option can be followed by the <code>-i</code> to get a couple fields interpreted.</p>
<dt><code>-v</code></p>
<dd>Print the version of auditctl. </p>
</dl>
<h2>Rule Options</h2>
<dl>
<dt><code>-a&nbsp;<wbr></code><i>[</i><code>list,action</code><i>|</i><code>action,list</code><i>]</i></p>
<dd>Append rule to the end of <i>list</i> with <i>action</i>. Please note the comma separating the two values. Omitting it will cause errors. The fields may be in either order. It could be list,action or action,list. The following describes the valid <i>list</i> names:</p>
<dl>
<dd>
<dl>
<dt><code>task</code></p>
<dd>Add a rule to the per task list. This rule list is used only at the time a task is created &#8212; when fork() or clone() are called by the parent task. When using this list, you should only use fields that are known at task creation time, such as the uid, gid, etc.</p>
<dt><code>exit</code></p>
<dd>Add a rule to the syscall exit list. This list is used upon exit from a system call to determine if an audit event should be created.</p>
<dt><code>user</code></p>
<dd>Add a rule to the user message filter list. This list is used by the kernel to filter events originating in user space before relaying them to the audit daemon. It should be noted that the only fields that are valid are: uid, auid, gid, pid, subj_user, subj_role, subj_type, subj_sen, subj_clr, and msgtype. All other fields will be treated as non-matching. It should be understood that any event originating from user space from a process that has CAP_AUDIT_WRITE will be recorded into the audit trail. This means that the most likely use for this filter is with rules that have an action of never since nothing has to be done to allow events to be recorded.</p>
<dt><code>exclude</code></p>
<dd>Add a rule to the event type exclusion filter list. This list is used to filter events that you do not want to see. For example, if you do not want to see any avc messages, you would using this list to record that. Events can be excluded by process ID, user ID, group ID, login user ID, message type or subject context</dl>
</dl>
<p> The following describes the valid <i>actions</i> for the rule:</p>
<dl>
<dd>
<dl>
<dt><code>never</code></p>
<dd>No audit records will be generated. This can be used to suppress event generation. In general, you want suppressions at the top of the list instead of the bottom. This is because the event triggers on the first matching rule.</p>
<dt><code>always</code></p>
<dd>Allocate an audit context, always fill it in at syscall entry time, and always write out a record at syscall exit time.</dl>
</dl>
<dt><code>-A&nbsp;<wbr></code><i>list</i><code>,</code><i>action</i></p>
<dd>Add rule to the beginning <i>list</i> with <i>action</i>.</p>
<dt><code>-C</code> [<i>f</i><code>=</code><i>f</i> | <i>f</i><code>!=</code><i>f</i>]</p>
<dd>Build an inter-field comparison rule: field, operation, field. You may pass multiple comparisons on a single command line. Each one must start with <code>-C</code>. Each inter-field equation is anded with each other as well as equations starting with <code>-F</code> to trigger an audit record. There are 2 operators supported &#8211; equal, and not equal. Valid fields are:</p>
<dl>
<dd>
<dl>
<dt><code>auid, uid, euid, suid, fsuid, obj_uid; and gid, egid, sgid, fsgid, obj_gid</code></p>
<dd></dl>
</dl>
<dl>
<dd>The two groups of uid and gid cannot be mixed. But any comparison within the group can be made. The obj_uid/gid fields are collected from the object of the event such as a file or directory.</dl>
<dt><code>-d&nbsp;<wbr></code><i>list</i><code>,</code><i>action</i></p>
<dd>Delete rule from <i>list</i> with <i>action</i>. The rule is deleted only if it exactly matches syscall name(s) and every field name and value.</p>
<dt><code>-F</code> [<i>n</i><code>=</code><i>v</i> | <i>n</i><code>!=</code><i>v</i> | <i>n</i><code>&lt;</code><i>v</i> | <i>n</i><code>&gt;</code><i>v</i> | <i>n</i><code>&lt;=</code><i>v</i> | <i>n</i><code>&gt;=</code><i>v</i> | <i>n</i><code>&amp;</code><i>v</i> | <i>n</i><code>&amp;=</code><i>v</i>]</p>
<dd>Build a rule field: name, operation, value. You may have up to 64 fields passed on a single command line. Each one must start with <code>-F</code>. Each field equation is anded with each other (as well as equations starting with <code>-C</code>) to trigger an audit record. There are 8 operators supported &#8211; equal, not equal, less than, greater than, less than or equal, and greater than or equal, bit mask, and bit test respectively. Bit test will &quot;and&quot; the values and check that they are equal, bit mask just &quot;ands&quot; the values. Fields that take a user ID may instead have the user&#8217;s name; the program will convert the name to user ID. The same is true of group names. Valid fields are:</p>
<dl>
<dd>
<dl>
<dt><code>a0, a1, a2, a3</code></p>
<dd>Respectively, the first 4 arguments to a syscall. Note that string arguments are not supported. This is because the kernel is passed a pointer to the string. Triggering on a pointer address value is not likely to work. So, when using this, you should only use on numeric values. This is most likely to be used on platforms that multiplex socket or IPC operations.</p>
<dt><code>arch</code></p>
<dd>The CPU architecture of the syscall. The arch can be found doing &#8216;uname -m&#8217;. If you do not know the arch of your machine but you want to use the 32 bit syscall table and your machine supports 32 bit, you can also use <code>b32</code> for the arch. The same applies to the 64 bit syscall table, you can use <code>b64.</code> In this way, you can write rules that are somewhat arch independent because the family type will be auto detected. However, syscalls can be arch specific and what is available on x86_64, may not be available on ppc. The arch directive should precede the -S option so that auditctl knows which internal table to use to look up the syscall numbers.</p>
<dt><code>auid</code></p>
<dd>The original ID the user logged in with. Its an abbreviation of audit uid. Sometimes its referred to as loginuid. Either the user account text or number may be used.</p>
<dt><code>devmajor</code></p>
<dd>Device Major Number</p>
<dt><code>devminor</code></p>
<dd>Device Minor Number</p>
<dt><code>dir</code></p>
<dd>Full Path of Directory to watch. This will place a recursive watch on the directory and its whole subtree. It can only be used on exit list. See &quot;<code>-w</code>&quot;.</p>
<dt><code>egid</code></p>
<dd>Effective Group ID. May be numeric or the groups name.</p>
<dt><code>euid</code></p>
<dd>Effective User ID. May be numeric or the user account name.</p>
<dt><code>exe</code></p>
<dd>Absolute path to application that while executing this rule will apply to. This can only be used on the exit list.</p>
<dt><code>exit</code></p>
<dd>Exit value from a syscall. If the exit code is an errno, you may use the text representation, too.</p>
<dt><code>fsgid</code></p>
<dd>Filesystem Group ID. May be numeric or the groups name.</p>
<dt><code>fsuid</code></p>
<dd>Filesystem User ID. May be numeric or the user account name.</p>
<dt><code>filetype</code></p>
<dd>The target file&#8217;s type. Can be either file, dir, socket, link, character, block, or fifo.</p>
<dt><code>gid</code></p>
<dd>Group ID. May be numeric or the groups name.</p>
<dt><code>inode</code></p>
<dd>Inode Number</p>
<dt><code>key</code></p>
<dd>This is another way of setting a filter key. See discussion above for <code>-k</code> option.</p>
<dt><code>msgtype</code></p>
<dd>This is used to match the event&#8217;s record type. It should only be used on the exclude or user filter lists.</p>
<dt><code>obj_uid</code></p>
<dd>Object&#8217;s UID</p>
<dt><code>obj_gid</code></p>
<dd>Object&#8217;s GID</p>
<dt><code>obj_user</code></p>
<dd>Resource&#8217;s SE Linux User</p>
<dt><code>obj_role</code></p>
<dd>Resource&#8217;s SE Linux Role</p>
<dt><code>obj_type</code></p>
<dd>Resource&#8217;s SE Linux Type</p>
<dt><code>obj_lev_low</code></p>
<dd>Resource&#8217;s SE Linux Low Level</p>
<dt><code>obj_lev_high</code></p>
<dd>Resource&#8217;s SE Linux High Level</p>
<dt><code>path</code></p>
<dd>Full Path of File to watch. It can only be used on exit list.</p>
<dt><code>perm</code></p>
<dd>Permission filter for file operations. See &quot;<code>-p</code>&quot;. It can only be used on exit list. You can use this without specifying a syscall and the kernel will select the syscalls that satisfy the permissions being requested.</p>
<dt><code>pers</code></p>
<dd>OS Personality Number</p>
<dt><code>pid</code></p>
<dd>Process ID</p>
<dt><code>ppid</code></p>
<dd>Parent&#8217;s Process ID</p>
<dt><code>subj_user</code></p>
<dd>Program&#8217;s SE Linux User</p>
<dt><code>subj_role</code></p>
<dd>Program&#8217;s SE Linux Role</p>
<dt><code>subj_type</code></p>
<dd>Program&#8217;s SE Linux Type</p>
<dt><code>subj_sen</code></p>
<dd>Program&#8217;s SE Linux Sensitivity</p>
<dt><code>subj_clr</code></p>
<dd>Program&#8217;s SE Linux Clearance</p>
<dt><code>sgid</code></p>
<dd>Saved Group ID. See <a href="/docs/linux/man/2-getresgid/">getresgid</a>(2) man page.</p>
<dt><code>success</code></p>
<dd>If the exit value is &gt;= 0 this is true/yes otherwise its false/no. When writing a rule, use a 1 for true/yes and a 0 for false/no</p>
<dt><code>suid</code></p>
<dd>Saved User ID. See <a href="/docs/linux/man/2-getresuid/">getresuid</a>(2) man page.</p>
<dt><code>uid</code></p>
<dd>User ID. May be numeric or the user account name.</dl>
</dl>
<dt><code>-k&nbsp;<wbr></code><i>key</i></p>
<dd>Set a filter key on an audit rule. The filter key is an arbitrary string of text that can be up to 31 bytes long. It can uniquely identify the audit records produced by a rule. Typical use is for when you have several rules that together satisfy a security requirement. The key value can be searched on with ausearch so that no matter which rule triggered the event, you can find its results. The key can also be used on delete all (-D) and list rules (-l) to select rules with a specific key. You may have more than one key on a rule if you want to be able to search logged events in multiple ways or if you have an audispd plugin that uses a key to aid its analysis.</p>
<dt><code>-p</code> [<code>r</code>|<code>w</code>|<code>x</code>|<code>a</code>]</p>
<dd>Describe the permission access type that a file system watch will trigger on. <code>r</code>=read, <code>w</code>=write, <code>x</code>=execute, <code>a</code>=attribute change. These permissions are not the standard file permissions, but rather the kind of syscall that would do this kind of thing. The read &amp; write syscalls are omitted from this set since they would overwhelm the logs. But rather for reads or writes, the open flags are looked at to see what permission was requested.</p>
<dt><code>-S</code> [<i>Syscall name or number</i>|<code>all</code>]</p>
<dd>Any <i>syscall name</i> or <i>number</i> may be used. The word &#8216;<code>all</code>&#8216; may also be used. If the given syscall is made by a program, then start an audit record. If a field rule is given and no syscall is specified, it will default to all syscalls. You may also specify multiple syscalls in the same rule by using multiple -S options in the same rule. Doing so improves performance since fewer rules need to be evaluated. Alternatively, you may pass a comma separated list of syscall names. If you are on a bi-arch system, like x86_64, you should be aware that auditctl simply takes the text, looks it up for the native arch (in this case b64) and sends that rule to the kernel. If there are no additional arch directives, IT WILL APPLY TO BOTH 32 &amp; 64 BIT SYSCALLS. This can have undesirable effects since there is no guarantee that any syscall has the same number on both 32 and 64 bit interfaces. You will likely want to control this and write 2 rules, one with arch equal to b32 and one with b64 to make sure the kernel finds the events that you intend. See the arch field discussion for more info.</p>
<dt><code>-w&nbsp;<wbr></code><i>path</i></p>
<dd>Insert a watch for the file system object at <i>path</i>. You cannot insert a watch to the top level directory. This is prohibited by the kernel. Wildcards are not supported either and will generate a warning. The way that watches work is by tracking the inode internally. If you place a watch on a file, its the same as using the -F path option on a syscall rule. If you place a watch on a directory, its the same as using the -F dir option on a syscall rule. The -w form of writing watches is for backwards compatibility and the syscall based form is more expressive. Unlike most syscall auditing rules, watches do not impact performance based on the number of rules sent to the kernel. The only valid options when using a watch are the -p and -k. If you need to anything fancy like audit a specific user accessing a file, then use the syscall auditing form with the path or dir fields. See the EXAMPLES section for an example of converting one form to another.</p>
<dt><code>-W&nbsp;<wbr></code><i>path</i></p>
<dd>Remove a watch for the file system object at <i>path</i>. The rule must match exactly. See <code>-d</code> discussion for more info.</dl>
<h2>Performance Tips</h2>
<p>Syscall rules get evaluated for each syscall for every program. If you have 10 syscall rules, every program on your system will delay during a syscall while the audit system evaluates each rule. Too many syscall rules will hurt performance. Try to combine as many as you can whenever the filter, action, key, and fields are identical. For example: </p>
<pre><code>auditctl -a always,exit -S openat -F success=0</code></pre>
<pre><code>auditctl -a always,exit -S truncate -F success=0</code></pre>
<p>could be re-written as one rule: </p>
<pre><code>auditctl -a always,exit -S openat -S truncate -F success=0</code></pre>
<p>Also, try to use file system auditing wherever practical. This improves performance. For example, if you were wanting to capture all failed opens &amp; truncates like above, but were only concerned about files in /etc and didn&#8217;t care about /usr or /sbin, its possible to use this rule: </p>
<pre><code>auditctl -a always,exit -S openat -S truncate -F dir=/etc -F success=0</code></pre>
<p>This will be higher performance since the kernel will not evaluate it each and every syscall. It will be handled by the filesystem auditing code and only checked on filesystem related syscalls.</p>
<h2>Examples</h2>
<p>To see all syscalls made by a specific program: </p>
<pre><code>auditctl -a always,exit -S all -F pid=1005</code></pre>
<p>To see files opened by a specific user: </p>
<pre><code>auditctl -a always,exit -S openat -F auid=510</code></pre>
<p>To see unsuccessful openat calls: </p>
<pre><code>auditctl -a always,exit -S openat -F success=0</code></pre>
<p>To watch a file for changes (2 ways to express): </p>
<pre><code>auditctl -w /etc/shadow -p wa</code>
<code>auditctl -a always,exit -F path=/etc/shadow -F perm=wa</code></pre>
<p>To recursively watch a directory for changes (2 ways to express): </p>
<pre><code>auditctl -w /etc/ -p wa</code>
<code>auditctl -a always,exit -F dir=/etc/ -F perm=wa</code></pre>
<p>To see if an admin is accessing other user&#8217;s files: </p>
<pre><code>auditctl -a always,exit -F dir=/home/ -F uid=0 -C auid!=obj_uid</code></pre>
<h2>Files</h2>
<dl>
<dt><i>/etc/audit/audit.rules</i></p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-audit-rules/">audit.rules</a></code>(7), <code><a href="/docs/linux/man/8-auditd/">auditd</a></code>(8). </p>
<h2>Author</h2>
<p>Steve Grubb</p>
