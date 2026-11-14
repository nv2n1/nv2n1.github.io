---
title: "bwrap(1)"
name: "bwrap"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bwrap/"
description: "bwrap – container setup utility"
---

<h2 class="name">NAME</h2>
<p> bwrap &#8211; container setup utility </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>bwrap</code> [<i>OPTION</i>&#8230;] [<i>COMMAND</i>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>bwrap</code></p>
<dd>is a privileged helper for container setup. You are unlikely to use it directly from the commandline, although that is possible. </p>
<p> It works by creating a new, completely empty, filesystem namespace where the root is on a tmpfs that is invisible from the host, and which will be automatically cleaned up when the last process exits. You can then use commandline options to construct the root filesystem and process environment for the command to run in the namespace. </p>
<p> By default, <code>bwrap</code> creates a new mount namespace for the sandbox. Optionally it also sets up new user, ipc, pid, network and uts namespaces (but note the user namespace is required if bwrap is not installed setuid root). The application in the sandbox can be made to run with a different UID and GID. </p>
<p> If needed (e.g. when using a PID namespace) <code>bwrap</code> is running a minimal pid 1 process in the sandbox that is responsible for reaping zombies. It also detects when the initial application process (pid 2) dies and reports its exit status back to the original spawner. The pid 1 process exits to clean up the sandbox when there are no other processes in the sandbox left.</p>
<h2>OPTIONS</h2>
<p> When options are used multiple times, the last option wins, unless otherwise specified. </p>
<p> General options: </p>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print help and exit</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print version</dl>
<p> <code>&#8211;args </code><code>FD</code></p>
<dl>
<dt>
<dd> Parse nul-separated arguments from the given file descriptor. This option can be used multiple times to parse options from multiple sources.</dl>
<p> Options related to kernel namespaces: </p>
<p> <code>&#8211;unshare-user</code></p>
<dl>
<dt>
<dd> Create a new user namespace</dl>
<p> <code>&#8211;unshare-user-try</code></p>
<dl>
<dt>
<dd> Create a new user namespace if possible else skip it</dl>
<p> <code>&#8211;unshare-ipc</code></p>
<dl>
<dt>
<dd> Create a new ipc namespace</dl>
<p> <code>&#8211;unshare-pid</code></p>
<dl>
<dt>
<dd> Create a new pid namespace</dl>
<p> <code>&#8211;unshare-net</code></p>
<dl>
<dt>
<dd> Create a new network namespace</dl>
<p> <code>&#8211;unshare-uts</code></p>
<dl>
<dt>
<dd> Create a new uts namespace</dl>
<p> <code>&#8211;unshare-cgroup</code></p>
<dl>
<dt>
<dd> Create a new cgroup namespace</dl>
<p> <code>&#8211;unshare-cgroup-try</code></p>
<dl>
<dt>
<dd> Create a new cgroup namespace if possible else skip it</dl>
<p> <code>&#8211;unshare-all</code></p>
<dl>
<dt>
<dd> Unshare all possible namespaces. Currently equivalent with: <code>&#8211;unshare-user-try</code> <code>&#8211;unshare-ipc</code> <code>&#8211;unshare-pid</code> <code>&#8211;unshare-net</code> <code>&#8211;unshare-uts</code> <code>&#8211;unshare-cgroup-try</code></dl>
<p> <code>&#8211;userns </code><code>FD</code></p>
<dl>
<dt>
<dd> Use an existing user namespace instead of creating a new one. The namespace must fulfil the permission requirements for setns(), which generally means that it must be a descendant of the currently active user namespace, owned by the same user. </p>
<p> This is incompatible with &#8211;unshare-user, and doesn&#8217;t work in the setuid version of bubblewrap.</dl>
<p> <code>&#8211;userns2 </code><code>FD</code></p>
<dl>
<dt>
<dd> After setting up the new namespace, switch into the specified namespace. For this to work the specified namespace must be a descendant of the user namespace used for the setup, so this is only useful in combination with &#8211;userns. </p>
<p> This is useful because sometimes bubblewrap itself creates nested user namespaces (to work around some kernel issues) and &#8211;userns2 can be used to enter these.</dl>
<p> <code>&#8211;pidns </code><code>FD</code></p>
<dl>
<dt>
<dd> Use an existing pid namespace instead of creating one. This is often used with &#8211;userns, because the pid namespace must be owned by the same user namespace that bwrap uses. </p>
<p> Note that this can be combined with &#8211;unshare-pid, and in that case it means that the sandbox will be in its own pid namespace, which is a child of the passed in one.</dl>
<p> <code>&#8211;uid </code><code>UID</code></p>
<dl>
<dt>
<dd> Use a custom user id in the sandbox (requires <code>&#8211;unshare-user</code>)</dl>
<p> <code>&#8211;gid </code><code>GID</code></p>
<dl>
<dt>
<dd> Use a custom group id in the sandbox (requires <code>&#8211;unshare-user</code>)</dl>
<p> <code>&#8211;hostname </code><code>HOSTNAME</code></p>
<dl>
<dt>
<dd> Use a custom hostname in the sandbox (requires <code>&#8211;unshare-uts</code>)</dl>
<p> Options about environment setup: </p>
<p> <code>&#8211;chdir </code><code>DIR</code></p>
<dl>
<dt>
<dd> Change directory to DIR</dl>
<p> <code>&#8211;setenv </code><code>VAR</code><code>VALUE</code></p>
<dl>
<dt>
<dd> Set an environment variable</dl>
<p> <code>&#8211;unsetenv </code><code>VAR</code></p>
<dl>
<dt>
<dd> Unset an environment variable</dl>
<p> <code>&#8211;clearenv</code></p>
<dl>
<dt>
<dd> Unset all environment variables, except for <code>PWD</code> and any that are subsequently set by <code>&#8211;setenv</code></dl>
<p> Options for monitoring the sandbox from the outside: </p>
<p> <code>&#8211;lock-file </code><code>DEST</code></p>
<dl>
<dt>
<dd> Take a lock on DEST while the sandbox is running. This option can be used multiple times to take locks on multiple files.</dl>
<p> <code>&#8211;sync-fd </code><code>FD</code></p>
<dl>
<dt>
<dd> Keep this file descriptor open while the sandbox is running</dl>
<p> Filesystem related options. These are all operations that modify the filesystem directly, or mounts stuff in the filesystem. These are applied in the order they are given as arguments. </p>
<p> Any missing parent directories that are required to create a specified destination are automatically created as needed. Their permissions are normally set to 0755 (rwxr-xr-x). However, if a <code>&#8211;perms</code> option is in effect, and it sets the permissions for group or other to zero, then newly-created parent directories will also have their corresponding permission set to zero. </p>
<p> <code>&#8211;perms </code><code>OCTAL</code></p>
<dl>
<dt>
<dd> This option does nothing on its own, and must be followed by one of the options that it affects. It sets the permissions for the next operation to OCTAL. Subsequent operations are not affected: for example, &#8211;perms 0700 &#8211;tmpfs /a &#8211;tmpfs /b will mount /a with permissions 0700, then return to the default permissions for /b.</dl>
<p> <code>&#8211;bind </code><code>SRC</code><code>DEST</code></p>
<dl>
<dt>
<dd> Bind mount the host path SRC on DEST</dl>
<p> <code>&#8211;bind-try </code><code>SRC</code><code>DEST</code></p>
<dl>
<dt>
<dd> Equal to <code>&#8211;bind</code> but ignores non-existent SRC</dl>
<p> <code>&#8211;dev-bind </code><code>SRC</code><code>DEST</code></p>
<dl>
<dt>
<dd> Bind mount the host path SRC on DEST, allowing device access</dl>
<p> <code>&#8211;dev-bind-try </code><code>SRC</code><code>DEST</code></p>
<dl>
<dt>
<dd> Equal to <code>&#8211;dev-bind</code> but ignores non-existent SRC</dl>
<p> <code>&#8211;ro-bind </code><code>SRC</code><code>DEST</code></p>
<dl>
<dt>
<dd> Bind mount the host path SRC readonly on DEST</dl>
<p> <code>&#8211;ro-bind-try </code><code>SRC</code><code>DEST</code></p>
<dl>
<dt>
<dd> Equal to <code>&#8211;ro-bind</code> but ignores non-existent SRC</dl>
<p> <code>&#8211;remount-ro </code><code>DEST</code></p>
<dl>
<dt>
<dd> Remount the path DEST as readonly. It works only on the specified mount point, without changing any other mount point under the specified path</dl>
<p> <code>&#8211;proc </code><code>DEST</code></p>
<dl>
<dt>
<dd> Mount procfs on DEST</dl>
<p> <code>&#8211;dev </code><code>DEST</code></p>
<dl>
<dt>
<dd> Mount new devtmpfs on DEST</dl>
<p> <code>&#8211;tmpfs </code><code>DEST</code></p>
<dl>
<dt>
<dd> Mount new tmpfs on DEST. If the previous option was <code>&#8211;perms</code>, it sets the mode of the tmpfs. Otherwise, the tmpfs has mode 0755.</dl>
<p> <code>&#8211;mqueue </code><code>DEST</code></p>
<dl>
<dt>
<dd> Mount new mqueue on DEST</dl>
<p> <code>&#8211;dir </code><code>DEST</code></p>
<dl>
<dt>
<dd> Create a directory at DEST. If the directory already exists, its permissions are unmodified, ignoring <code>&#8211;perms</code> (use <code>&#8211;chmod</code> if the permissions of an existing directory need to be changed). If the directory is newly created and the previous option was <code>&#8211;perms</code>, it sets the mode of the directory. Otherwise, newly-created directories have mode 0755.</dl>
<p> <code>&#8211;file </code><code>FD</code><code>DEST</code></p>
<dl>
<dt>
<dd> Copy from the file descriptor FD to DEST. If the previous option was <code>&#8211;perms</code>, it sets the mode of the new file. Otherwise, the file has mode 0666 (note that this is not the same as <code>&#8211;bind-data</code>).</dl>
<p> <code>&#8211;bind-data </code><code>FD</code><code>DEST</code></p>
<dl>
<dt>
<dd> Copy from the file descriptor FD to a file which is bind-mounted on DEST. If the previous option was <code>&#8211;perms</code>, it sets the mode of the new file. Otherwise, the file has mode 0600 (note that this is not the same as <code>&#8211;file</code>).</dl>
<p> <code>&#8211;ro-bind-data </code><code>FD</code><code>DEST</code></p>
<dl>
<dt>
<dd> Copy from the file descriptor FD to a file which is bind-mounted read-only on DEST. If the previous option was <code>&#8211;perms</code>, it sets the mode of the new file. Otherwise, the file has mode 0600 (note that this is not the same as <code>&#8211;file</code>).</dl>
<p> <code>&#8211;symlink </code><code>SRC</code><code>DEST</code></p>
<dl>
<dt>
<dd> Create a symlink at DEST with target SRC</dl>
<p> <code>&#8211;chmod </code><code>OCTAL</code><code>PATH</code></p>
<dl>
<dt>
<dd> Set the permissions of PATH, which must already exist, to OCTAL.</dl>
<p> Lockdown options: </p>
<p> <code>&#8211;seccomp </code><code>FD</code></p>
<dl>
<dt>
<dd> Load and use seccomp rules from FD. The rules need to be in the form of a compiled cBPF program, as generated by seccomp_export_bpf. If this option is given more than once, only the last one is used. Use <code>&#8211;add-seccomp-fd</code> if multiple seccomp programs are needed.</dl>
<p> <code>&#8211;add-seccomp-fd </code><code>FD</code></p>
<dl>
<dt>
<dd> Load and use seccomp rules from FD. The rules need to be in the form of a compiled cBPF program, as generated by seccomp_export_bpf. This option can be repeated, in which case all the seccomp programs will be loaded in the order given (note that the kernel will evaluate them in reverse order, so the last program on the bwrap command-line is evaluated first). All of them, except possibly the last, must allow use of the PR_SET_SECCOMP prctl. This option cannot be combined with <code>&#8211;seccomp</code>.</dl>
<p> <code>&#8211;exec-label </code><code>LABEL</code></p>
<dl>
<dt>
<dd> Exec Label from the sandbox. On an SELinux system you can specify the SELinux context for the sandbox process(s).</dl>
<p> <code>&#8211;file-label </code><code>LABEL</code></p>
<dl>
<dt>
<dd> File label for temporary sandbox content. On an SELinux system you can specify the SELinux context for the sandbox content.</dl>
<p> <code>&#8211;block-fd </code><code>FD</code></p>
<dl>
<dt>
<dd> Block the sandbox on reading from FD until some data is available.</dl>
<p> <code>&#8211;userns-block-fd </code><code>FD</code></p>
<dl>
<dt>
<dd> Do not initialize the user namespace but wait on FD until it is ready. This allow external processes (like newuidmap/newgidmap) to setup the user namespace before it is used by the sandbox process.</dl>
<p> <code>&#8211;info-fd </code><code>FD</code></p>
<dl>
<dt>
<dd> Write information in JSON format about the sandbox to FD.</dl>
<p> <code>&#8211;new-session</code></p>
<dl>
<dt>
<dd> Create a new terminal session for the sandbox (calls setsid()). This disconnects the sandbox from the controlling terminal which means the sandbox can&#8217;t for instance inject input into the terminal. </p>
<p> Note: In a general sandbox, if you don&#8217;t use &#8211;new-session, it is recommended to use seccomp to disallow the TIOCSTI ioctl, otherwise the application can feed keyboard input to the terminal.</dl>
<p> <code>&#8211;die-with-parent</code></p>
<dl>
<dt>
<dd> Ensures child process (COMMAND) dies when bwrap&#8217;s parent dies. Kills (SIGKILL) all bwrap sandbox processes in sequence from parent to child including COMMAND process when bwrap or bwrap&#8217;s parent dies. See prctl, PR_SET_PDEATHSIG.</dl>
<p> <code>&#8211;as-pid-1</code></p>
<dl>
<dt>
<dd> Do not create a process with PID=1 in the sandbox to reap child processes.</dl>
<p> <code>&#8211;cap-add </code><code>CAP</code></p>
<dl>
<dt>
<dd> Add the specified capability when running as privileged user. It accepts the special value ALL to add all the permitted caps.</dl>
<p> <code>&#8211;cap-drop </code><code>CAP</code></p>
<dl>
<dt>
<dd> Drop the specified capability when running as privileged user. It accepts the special value ALL to drop all the caps. By default no caps are left in the sandboxed process. The <code>&#8211;cap-add</code> and <code>&#8211;cap-drop</code> options are processed in the order they are specified on the command line. Please be careful to the order they are specified.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>HOME</code></p>
<dl>
<dt>
<dd> Used as the cwd in the sandbox if <code>&#8211;chdir</code> has not been explicitly specified and the current cwd is not present inside the sandbox. The <code>&#8211;setenv</code> option can be used to override the value that is used here.</dl>
<h2>EXIT STATUS</h2>
<p> The <code>bwrap</code> command returns the exit status of the initial application process (pid 2 in the sandbox). </p>
<h2>Index</h2>
