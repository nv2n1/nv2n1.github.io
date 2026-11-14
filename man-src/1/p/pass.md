---
title: "pass(1)"
name: "pass"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pass/"
description: "pass – stores, retrieves, generates, and synchronizes passwords securely"
---

<h2 class="name">NAME</h2>
<p> pass &#8211; stores, retrieves, generates, and synchronizes passwords securely</p>
<h2>SYNOPSIS</h2>
<p> <code>pass</code> [ <i>COMMAND</i> ] [ <i>OPTIONS</i> ]&#8230; [ <i>ARGS</i> ]&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>pass </code> is a very simple password store that keeps passwords inside <code><a href="/docs/linux/man/1-gpg2/">gpg2</a></code>(1) encrypted files inside a simple directory tree residing at <i>~/.password-store</i>. The <code>pass</code> utility provides a series of commands for manipulating the password store, allowing the user to add, remove, edit, synchronize, generate, and manipulate passwords. </p>
<p> If no COMMAND is specified, COMMAND defaults to either <code>show</code> or <code>ls</code>, depending on the type of specifier in ARGS. Otherwise COMMAND must be one of the valid commands listed below. </p>
<p> Several of the commands below rely on or provide additional functionality if the password store directory is also a git repository. If the password store directory is a git repository, all password store modification commands will cause a corresponding git commit. See the <i>EXTENDED GIT EXAMPLE</i> section for a detailed description using <code>init</code> and <code><a href="/docs/linux/man/1-git/">git</a></code>(1). </p>
<p> The <code>init</code> command must be run before other commands in order to initialize the password store with the correct gpg key id. Passwords are encrypting using the gpg key set with <code>init</code>. </p>
<p> There is a corresponding bash completion script for use with tab completing password names in <code><a href="/docs/linux/man/1-bash/">bash</a></code>(1). </p>
<h2>COMMANDS</h2>
<dl>
<dt><code>init</code> [ <i>&#8211;reencrypt</i>, <i>-e</i> ] [ <i>&#8211;path=sub-folder</i>, <i>-p sub-folder</i> ] <i>gpg-id&#8230;</i></p>
<dd> Initialize new password storage and use <i>gpg-id</i> for encryption. Multiple gpg-ids may be specified, in order to encrypt each password with multiple ids. This command must be run first before a password store can be used. If <i>&#8211;reencrypt</i> or <i>-e</i> is specified, reencrypt all existing passwords in the password store using <i>gpg-id</i>. Note that use of <code><a href="/docs/linux/man/1-gpg-agent/">gpg-agent</a></code>(1) is recommended so that the batch decryption does not require as much user intervention. If <i>&#8211;path</i> or <i>-p</i> is specified, along with an argument, a specific gpg-id or set of gpg-ids is assigned for that specific sub folder of the password store.</p>
<dt><code>ls</code> <i>subfolder</i></p>
<dd> List names of passwords inside the tree at <i>subfolder</i> by using the <code><a href="/docs/linux/man/1-tree/">tree</a></code>(1) program. This command is alternatively named <code>list</code>.</p>
<dt><code>show</code> [ <i>&#8211;clip</i>, <i>-c</i> ] <i>pass-name</i></p>
<dd> Decrypt and print a password named <i>pass-name</i>. If <i>&#8211;clip</i> or <i>-c</i> is specified, do not print the password but instead copy the first line to the clipboard using <code><a href="/docs/linux/man/1-xclip/">xclip</a></code>(1) and then restore the clipboard after 45 (or <i>PASSWORD_STORE_CLIP_TIME</i>) seconds.</p>
<dt><code>insert</code> [ <i>&#8211;echo</i>, <i>-e</i> | <i>&#8211;multiline</i>, <i>-m</i> ] [ <i>&#8211;force</i>, <i>-f</i> ] <i>pass-name</i></p>
<dd> Insert a new password into the password store called <i>pass-name</i>. This will read the new password from standard in. If <i>&#8211;echo</i> or <i>-e</i> is <i>not</i> specified, disable keyboard echo when the password is entered and confirm the password by asking for it twice. If <i>&#8211;multiline</i> or <i>-m</i> is specified, lines will be read until EOF or Ctrl+D is reached. Otherwise, only a single line from standard in is read. Prompt before overwriting an existing password, unless <i>&#8211;force</i> or <i>-f</i> is specified.</p>
<dt><code>edit</code> <i>pass-name</i></p>
<dd> Insert a new password or edit an existing password using the default text editor specified by the environment variable <i>EDITOR</i> or using <code><a href="/docs/linux/man/1-vi/">vi</a></code>(1) as a fallback. This mode makes use of temporary files for editing, but care is taken to ensure that temporary files are created in <i>/dev/shm</i> in order to avoid writing to difficult-to-erase disk sectors. If <i>/dev/shm</i> is not accessible, fallback to the ordinary <i>TMPDIR</i> location, and print a warning.</p>
<dt><code>generate</code> [ <i>&#8211;no-symbols</i>, <i>-n</i> ] [ <i>&#8211;clip</i>, <i>-c</i> ] [ <i>&#8211;force</i>, <i>-f</i> ] <i>pass-name pass-length</i></p>
<dd> Generate a new password using <code><a href="/docs/linux/man/1-pwgen/">pwgen</a></code>(1) of length <i>pass-length</i> and insert into <i>pass-name</i>. If <i>&#8211;no-symbols</i> or <i>-n</i> is specified, do not use any non-alphanumeric characters in the generated password. If <i>&#8211;clip</i> or <i>-c</i> is specified, do not print the password but instead copy it to the clipboard using <code><a href="/docs/linux/man/1-xclip/">xclip</a></code>(1) and then restore the clipboard after 45 (or <i>PASSWORD_STORE_CLIP_TIME</i>) seconds. Prompt before overwriting an existing password, unless <i>&#8211;force</i> or <i>-f</i> is specified.</p>
<dt><code>rm</code> [ <i>&#8211;recursive</i>, <i>-r</i> ] [ <i>&#8211;force</i>, <i>-f</i> ] <i>pass-name</i></p>
<dd> Remove the password named <i>pass-name</i> from the password store. This command is alternatively named <code>remove</code> or <code>delete</code>. If <i>&#8211;recursive</i> or <i>-r</i> is specified, delete pass-name recursively if it is a directory. If <i>&#8211;force</i> or <i>-f</i> is specified, do not interactively prompt before removal.</p>
<dt><code>git</code> <i>git-command-args</i>&#8230;</p>
<dd> If the password store is a git repository, pass <i>git-command-args</i> as arguments to <code><a href="/docs/linux/man/1-git/">git</a></code>(1) using the password store as the git repository. If <i>git-command-args</i> is <code>init</code>, in addition to initializing the git repository, add the current contents of the password store to the repository in an initial commit. If the git config key <i>pass.signcommits</i> is set to <i>true</i>, then all commits will be signed using <i>user.signingkey</i> or the default git signing key. This config key may be turned on using: <code>`pass git config &#8211;bool &#8211;add pass.signcommits true`</code></p>
<dt><code>help</code></p>
<dd> Show usage message.</p>
<dt><code>version</code></p>
<dd> Show version information. </p>
</dl>
<h2>SIMPLE EXAMPLES</h2>
<dl>
<dt>Initialize password store</p>
<dd> <code>zx2c4 [at] laptop ~ $ pass init Jason [at] zx2c4.com </code><br />
 mkdir: created directory 18/home/zx2c4/.password-store19<br />
 Password store initialized for Jason [at] zx2c4.com.</p>
<dt>List existing passwords in store</p>
<dd> <code>zx2c4 [at] laptop ~ $ pass </code><br />
 Password Store<br />
 1C0000 Business<br />
 02 1C0000 some-silly-business-site.com<br />
 02 140000 another-business-site.net<br />
 1C0000 Email<br />
 02 1C0000 donenfeld.com<br />
 02 140000 zx2c4.com<br />
 140000 France </p>
<p>&nbsp;<wbr>1C0000 bank&nbsp;<wbr> </p>
<p>&nbsp;<wbr>1C0000 freebox&nbsp;<wbr> </p>
<p>&nbsp;<wbr>140000 mobilephone&nbsp;<wbr>&nbsp;<wbr> </p>
<p> Alternatively, &quot;<code>pass ls</code>&quot;.</p>
<dt>Show existing password</p>
<dd> <code>zx2c4 [at] laptop ~ $ pass Email/zx2c4.com </code><br />
 sup3rh4x3rizmynam3</p>
<dt>Copy existing password to clipboard</p>
<dd> <code>zx2c4 [at] laptop ~ $ pass -c Email/zx2c4.com </code><br />
 Copied Email/jason [at] zx2c4.com to clipboard. Will clear in 45 seconds.</p>
<dt>Add password to store</p>
<dd> <code>zx2c4 [at] laptop ~ $ pass insert Business/cheese-whiz-factory </code><br />
 Enter password for Business/cheese-whiz-factory: omg so much cheese what am i gonna do</p>
<dt>Add multiline password to store</p>
<dd> <code>zx2c4 [at] laptop ~ $ pass insert -m Business/cheese-whiz-factory </code><br />
 Enter contents of Business/cheese-whiz-factory and press Ctrl+D when finished: </p>
<p>&nbsp;<wbr><br />
 Hey this is my<br />
 awesome<br />
 multi<br />
 line<br />
 passworrrrrrrrd.<br />
 ^D</p>
<dt>Generate new password</p>
<dd> <code>zx2c4 [at] laptop ~ $ pass generate Email/jasondonenfeld.com 15 </code><br />
 The generated password to Email/jasondonenfeld.com is:<br />
 $(-QF&amp;Q=IN2nFBx</p>
<dt>Generate new alphanumeric password</p>
<dd> <code>zx2c4 [at] laptop ~ $ pass generate -n Email/jasondonenfeld.com 12</code><br />
 The generated password to Email/jasondonenfeld.com is:<br />
 YqFsMkBeO6di</p>
<dt>Generate new password and copy it to the clipboard</p>
<dd> <code>zx2c4 [at] laptop ~ $ pass generate -c Email/jasondonenfeld.com 19</code><br />
 Copied Email/jasondonenfeld.com to clipboard. Will clear in 45 seconds.</p>
<dt>Remove password from store</p>
<dd> <code>zx2c4 [at] laptop ~ $ pass remove Business/cheese-whiz-factory </code><br />
 rm: remove regular file 18/home/zx2c4/.password-store/Business/cheese-whiz-factory.gpg19? y<br />
 removed 18/home/zx2c4/.password-store/Business/cheese-whiz-factory.gpg19 </p>
</dl>
<h2>EXTENDED GIT EXAMPLE</h2>
<p> Here, we initialize new password store, create a git repository, and then manipulate and sync passwords. Make note of the arguments to the first call of <code>pass git push</code>; consult <code><a href="/docs/linux/man/1-git-push/">git-push</a></code>(1) for more information. </p>
<p> <code>zx2c4 [at] laptop ~ $ pass init Jason [at] zx2c4.com </code><br />
 mkdir: created directory 18/home/zx2c4/.password-store19<br />
 Password store initialized for Jason [at] zx2c4.com. </p>
<p> <code>zx2c4 [at] laptop ~ $ pass git init </code><br />
 Initialized empty Git repository in /home/zx2c4/.password-store/.git/<br />
 [master (root-commit) 998c8fd] Added current contents of password store. </p>
<p>&nbsp;<wbr>1 file changed, 1 insertion(+) </p>
<p>&nbsp;<wbr>create mode 100644 .gpg-id </p>
<p> <code>zx2c4 [at] laptop ~ $ pass git remote add origin kexec.com:pass-store </code> </p>
<p> <code>zx2c4 [at] laptop ~ $ pass generate Amazon/amazonemail [at] email.com 21 </code><br />
 mkdir: created directory 18/home/zx2c4/.password-store/Amazon19<br />
 [master 30fdc1e] Added generated password for Amazon/amazonemail [at] email.com to store.<br />
 1 file changed, 0 insertions(+), 0 deletions(-)<br />
 create mode 100644 Amazon/amazonemail [at] email.com.gpg<br />
 The generated password to Amazon/amazonemail [at] email.com is:<br />
 &lt;5m,_BrZY`antNDxKN&lt;0A </p>
<p> <code>zx2c4 [at] laptop ~ $ pass git push -u &#8211;all</code><br />
 Counting objects: 4, done.<br />
 Delta compression using up to 2 threads.<br />
 Compressing objects: 100% (3/3), done.<br />
 Writing objects: 100% (4/4), 921 bytes, done.<br />
 Total 4 (delta 0), reused 0 (delta 0)<br />
 To kexec.com:pass-store<br />
 * [new branch] master -&gt; master<br />
 Branch master set up to track remote branch master from origin. </p>
<p> <code>zx2c4 [at] laptop ~ $ pass insert Amazon/otheraccount [at] email.com </code><br />
 Enter password for Amazon/otheraccount [at] email.com: som3r3a11yb1gp4ssw0rd!!88**<br />
 [master b9b6746] Added given password for Amazon/otheraccount [at] email.com to store.<br />
 1 file changed, 0 insertions(+), 0 deletions(-)<br />
 create mode 100644 Amazon/otheraccount [at] email.com.gpg </p>
<p> <code>zx2c4 [at] laptop ~ $ pass rm Amazon/amazonemail [at] email.com </code><br />
 rm: remove regular file 18/home/zx2c4/.password-store/Amazon/amazonemail [at] email.com.gpg19? y<br />
 removed 18/home/zx2c4/.password-store/Amazon/amazonemail [at] email.com.gpg19<br />
 rm &#8216;Amazon/amazonemail [at] email.com.gpg&#8217;<br />
 [master 288b379] Removed Amazon/amazonemail [at] email.com from store.<br />
 1 file changed, 0 insertions(+), 0 deletions(-)<br />
 delete mode 100644 Amazon/amazonemail [at] email.com.gpg </p>
<p> <code>zx2c4 [at] laptop ~ $ pass git push</code><br />
 Counting objects: 9, done.<br />
 Delta compression using up to 2 threads.<br />
 Compressing objects: 100% (5/5), done.<br />
 Writing objects: 100% (7/7), 1.25 KiB, done.<br />
 Total 7 (delta 0), reused 0 (delta 0)<br />
 To kexec.com:pass-store </p>
<h2>FILES</h2>
<dl>
<dt><code>~/.password-store</code></p>
<dd> The default password storage directory.</p>
<dt><code>~/.password-store/.gpg-id</code></p>
<dd> Contains the default gpg key identification used for encryption and decryption. Multiple gpg keys may be specified in this file, one per line. If this file exists in any sub directories, passwords inside those sub directories are encrypted using those keys. This should be set using the <code>init</code> command. </p>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><i>PASSWORD_STORE_DIR</i></p>
<dd> Overrides the default password storage directory.</p>
<dt><i>PASSWORD_STORE_KEY</i></p>
<dd> Overrides the default gpg key identification set by <code>init</code>. Keys must not contain spaces and thus use of the hexidecimal key signature is recommended. Multiple keys may be specified separated by spaces.</p>
<dt><i>PASSWORD_STORE_GIT</i></p>
<dd> Overrides the default root of the git repository, which is helpful if <i>PASSWORD_STORE_DIR</i> is temporarily set to a sub-directory of the default password store.</p>
<dt><i>PASSWORD_STORE_X_SELECTION</i></p>
<dd> Overrides the selection passed to <code>xclip</code>, by default <i>clipboard</i>. See <code><a href="/docs/linux/man/1-xclip/">xclip</a></code>(1) for more info.</p>
<dt><i>PASSWORD_STORE_CLIP_TIME</i></p>
<dd> Specifies the number of seconds to wait before restoring the clipboard, by default <i>45</i> seconds.</p>
<dt><i>PASSWORD_STORE_UMASK</i></p>
<dd> Sets the umask of all files modified by pass, by default <i>077</i>.</p>
<dt><i>EDITOR</i></p>
<dd> The location of the text editor used by <code>edit</code>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gpg2/">gpg2</a></code>(1), <code><a href="/docs/linux/man/1-pwgen/">pwgen</a></code>(1), <code><a href="/docs/linux/man/1-git/">git</a></code>(1), <code><a href="/docs/linux/man/1-xclip/">xclip</a></code>(1). </p>
<h2>AUTHOR</h2>
<p> <code>pass</code> was written by Jason A. Donenfeld For updates and more information, a project page is available on the World Wide Web </p>
<h2>COPYING</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA. </p>
<h2>Index</h2>
