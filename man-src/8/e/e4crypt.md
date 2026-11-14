---
title: "e4crypt(8)"
name: "e4crypt"
section: "8"
letter: "e"
url: "/docs/linux/man/8-e4crypt/"
description: "e4crypt – ext4 file system encryption utility"
---

<p>e4crypt &#8211; ext4 file system encryption utility</p>
<h2>Synopsis</h2>
<p><code>e4crypt add_key -S </code>[<code> -k </code><i>keyring</i> ] [<code>-v</code>] [<code>-q</code>] [<code> -p </code><i>pad</i> ] [ <i>path</i> &#8230; ]<br />
 <code>e4crypt new_session</code><br />
 <code>e4crypt get_policy </code><i>path</i> &#8230;<br />
 <code>e4crypt set_policy </code>[<code> -p </code><i>pad</i> ] <i>policy path</i> &#8230;</p>
<h2>Description</h2>
<p><code>e4crypt</code> performs encryption management for ext4 file systems.</p>
<h2>Commands</h2>
<dl>
<dt><code>e4crypt add_key </code>[<code>-vq</code>] [<code>-S</code><i> salt</i> ] [<code>-k </code><i>keyring</i> ] [<code> -p </code><i>pad</i> ] [ <i>path</i> &#8230; ]</p>
<dd>Prompts the user for a passphrase and inserts it into the specified keyring. If no keyring is specified, e4crypt will use the session keyring if it exists or the user session keyring if it does not.</p>
<dd>The <i>salt</i> argument is interpreted in a number of different ways, depending on how its prefix value. If the first two characters are &quot;s:&quot;, then the rest of the argument will be used as an text string and used as the salt value. If the first two characters are &quot;0x&quot;, then the rest of the argument will be parsed as a hex string as used as the salt. If the first characters are &quot;f:&quot; then the rest of the argument will be interpreted as a filename from which the salt value will be read. If the string begins with a &#8216;/&#8217; character, it will similarly be treated as filename. Finally, if the <i>salt</i> argument can be parsed as a valid UUID, then the UUID value will be used as a salt value.</p>
<dd>The <i>keyring</i> argument specifies the keyring to which the key should be added.</p>
<dd>The <i>pad</i> value specifies the number of bytes of padding will be added to directory names for obfuscation purposes. Valid <i>pad</i> values are 4, 8, 16, and 32.</p>
<dd>If one or more directory paths are specified, e4crypt will try to set the policy of those directories to use the key just added by the <code>add_key</code> command. If a salt was explicitly specified, then it will be used to derive the encryption key of those directories. Otherwise a directory-specific default salt will be used.</p>
<dt><code>e4crypt get_policy </code><i>path</i> &#8230;</p>
<dd>Print the policy for the directories specified on the command line.</p>
<dt><code>e4crypt new_session</code></p>
<dd>Give the invoking process (typically a shell) a new session keyring, discarding its old session keyring.</p>
<dt><code>e4crypt set_policy </code>[<code> -p </code><i>pad</i> ] <i>policy path</i> &#8230;</p>
<dd>Sets the policy for the directories specified on the command line. All directories must be empty to set the policy; if the directory already has a policy established, e4crypt will validate that the policy matches what was specified. A policy is an encryption key identifier consisting of 16 hexadecimal characters.</dl>
<h2>Author</h2>
<p>Written by Michael Halcrow &lt;mhalcrow [at] google.com&gt;, Ildar Muslukhov &lt;muslukhovi [at] gmail.com&gt;, and Theodore Ts&#8217;o &lt;tytso [at] mit.edu&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1), <code><a href="/docs/linux/man/8-mke2fs/">mke2fs</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8). </p>
