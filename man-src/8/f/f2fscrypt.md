---
title: "f2fscrypt(8)"
name: "f2fscrypt"
section: "8"
letter: "f"
url: "/docs/linux/man/8-f2fscrypt/"
description: "f2fscrypt – f2fs filesystem encryption utility"
---

<p>f2fscrypt &#8211; f2fs filesystem encryption utility</p>
<h2>Synopsis</h2>
<p><code>f2fscrypt add_key -S </code>[<code> -k </code><i>keyring</i> ] [<code>-v</code>] [<code>-q</code>] [ <i> path</i> &#8230; ]<br />
 <code>f2fscrypt new_session</code><br />
 <code>f2fscrypt get_policy </code><i>path</i> &#8230;<br />
 <code>f2fscrypt set_policy </code><i>policy path</i> &#8230;</p>
<h2>Description</h2>
<p><code>f2fscrypt</code> performs encryption management for f2fs file systems.</p>
<h2>Commands</h2>
<dl>
<dt><code>f2fscrypt add_key -S </code>[<code> -k </code><i>keyring</i> ] [<code>-v</code>] [<code>-q</code>] [ <i> path</i> &#8230; ]</p>
<dd>Prompts the user for a passphrase and inserts it into the specified keyring. If no keyring is specified, f2fscrypt will use the session keyring if it exists or the user session keyring if it does not.</p>
<dd>If one or more directory paths are specified, f2fscrypt will try to set the policy of those directories to use the key just entered by the user.</p>
<dt><code>f2fscrypt get_policy </code><i>path</i> &#8230;</p>
<dd>Print the policy for the directories specified on the command line.</p>
<dt><code>f2fscrypt new_session</code></p>
<dd>Give the invoking process (typically a shell) a new session keyring, discarding its old session keyring.</p>
<dt><code>f2fscrypt set_policy </code><i>policy path</i> &#8230;</p>
<dd>Sets the policy for the directories specified on the command line. All directories must be empty to set the policy; if the directory already has a policy established, f2fscrypt will validate that the policy matches what was specified. A policy is an encryption key identifier consisting of 16 hexadecimal characters.</dl>
<h2>Notes</h2>
<p>The target directory must be empty.</p>
<h2>Example</h2>
<pre>Formats a f2fs filesytem that supports encrypt.
# mkfs.f2fs -O encrypt /dev/sdxx
# mount /dev/sdxx /encrypted/
# mkdir /encrypted/dir
First create the key in the keyring use an simple salt
(or generate a random salt).
Then use it to set the policy for the directory to be encrypted.
# f2fscrypt add_key -S 0x1234
 Enter passphrase (echo disabled):
 Added key with descriptor [28e21cc0c4393da1]
# f2fscrypt set_policy 28e21cc0c4393da1 /encrypted/dir
 Key with descriptor [28e21cc0c4393da1] applied to /encrypted/dir.
# touch /encrypted/dir/test.txt
# ls -l /encrypted/dir/
 -rw-r--r--. 1 root root 0 Mar 5 21:41 test.txt
After each reboot, the same command can be used set the key for
decryption of the directory and its descendants.
# ls -l /encrypted/dir/
 -rw-r--r--. 1 root root 0 Mar 5 21:41 zbx7tsUEMLzh+AUVMkQcnB
# f2fscrypt get_policy /encrypted/dir/
 /encrypted/dir/: 28e21cc0c4393da1
# f2fscrypt add_key -S 0x1234
 Enter passphrase (echo disabled):
 Added key with descriptor [28e21cc0c4393da1]
# ls -l /encrypted/dir/
 -rw-r--r--. 1 root root 0 Mar 5 21:41 test.txt
Show process keyrings.
# keyctl show
 Session Keyring
 84022412 --alswrv 0 0 keyring: _ses
 204615789 --alswrv 0 65534 \_ keyring: _uid.0
 529474961 --alsw-v 0 0 \_ logon: f2fs:28e21cc0c4393da1</pre>
<h2>Author</h2>
<p>Written by Kinglong Mee &lt;kinglongmee [at] gmail.com&gt;, Migrated from e4crypt that Written by Michael Halcrow &lt;mhalcrow [at] google.com&gt;, Ildar Muslukhov &lt;muslukhovi [at] gmail.com&gt;, and Theodore Ts&#8217;o &lt;tytso [at] mit.edu&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1), <code><a href="/docs/linux/man/8-mkfs-f2fs/">mkfs.f2fs</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8). </p>
