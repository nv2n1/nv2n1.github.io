---
title: "gio(1)"
name: "gio"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gio/"
description: "gio – GIO commandline tool"
---

<h2 class="name">NAME</h2>
<p> gio &#8211; GIO commandline tool </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gio</code> help [<i>COMMAND</i>]</p>
<dt> <code>gio</code> version</p>
<dt> <code>gio</code> cat <i>LOCATION</i>&#8230;</p>
<dt> <code>gio</code> copy [<i>OPTION</i>&#8230;] <i>SOURCE</i>&#8230; <i>DESTINATION</i></p>
<dt> <code>gio</code> info [<i>OPTION</i>&#8230;] <i>LOCATION</i>&#8230;</p>
<dt> <code>gio</code> launch <i>DESKTOP-FILE</i> [<i>FILE-ARG</i>&#8230;]</p>
<dt> <code>gio</code> list [<i>OPTION</i>&#8230;] [<i>LOCATION</i>&#8230;]</p>
<dt> <code>gio</code> mime <i>MIMETYPE</i> [<i>HANDLER</i>]</p>
<dt> <code>gio</code> mkdir [<i>OPTION</i>&#8230;] <i>LOCATION</i>&#8230;</p>
<dt> <code>gio</code> monitor [<i>OPTION</i>&#8230;] [<i>LOCATION</i>&#8230;]</p>
<dt> <code>gio</code> mount [<i>OPTION</i>&#8230;] [<i>LOCATION</i>&#8230;]</p>
<dt> <code>gio</code> move [<i>OPTION</i>&#8230;] <i>SOURCE</i>&#8230; <i>DESTINATION</i></p>
<dt> <code>gio</code> open <i>LOCATION</i>&#8230;</p>
<dt> <code>gio</code> rename <i>LOCATION</i> <i>NAME</i></p>
<dt> <code>gio</code> remove [<i>OPTION</i>&#8230;] <i>LOCATION</i>&#8230;</p>
<dt> <code>gio</code> save [<i>OPTION</i>&#8230;] <i>DESTINATION</i></p>
<dt> <code>gio</code> set [<i>OPTION</i>&#8230;] <i>LOCATION</i> <i>ATTRIBUTE</i> <i>VALUE</i>&#8230;</p>
<dt> <code>gio</code> trash [<i>OPTION</i>&#8230;] [<i>LOCATION</i>&#8230;]</p>
<dt> <code>gio</code> tree [<i>OPTION</i>&#8230;] [<i>LOCATION</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>gio</code></p>
<dd>is a utility that makes many of the GIO features available from the commandline. In doing so, it provides commands that are similar to traditional utilities, but let you use GIO locations instead of local files: for example you can use something like <a href="smb://server/resource/file.txt">smb://server/resource/file.txt</a> as a location. </p>
<p> Plain filenames which contain a colon will be interpreted as URIs with an unknown protocol. To avoid this, prefix them with a path such as ./, or with the file: protocol.</p>
<h2>COMMANDS</h2>
<p> <code>help</code> [<i>COMMAND</i>]</p>
<dl>
<dt>
<dd> Displays a short synopsis of the available commands or provides detailed help on a specific command.</dl>
<p> <code>version</code></p>
<dl>
<dt>
<dd> Prints the GLib version to which <code>gio</code> belongs.</dl>
<p> <code>cat</code> <i>LOCATION</i>&#8230;</p>
<dl>
<dt>
<dd> Concatenates the given files and prints them to the standard output. </p>
<p> The <code>cat</code> command works just like the traditional <code>cat</code> utility. </p>
<p> Note: just pipe through <code>cat</code> if you need its formatting options like <code>-n</code>, <code>-T</code> or other.</dl>
<p> <code>copy</code> [<i>OPTION</i>&#8230;] <i>SOURCE</i>&#8230; <i>DESTINATION</i></p>
<dl>
<dt>
<dd> Copies one or more files from <i>SOURCE</i> to <i>DESTINATION</i>. If more than one source is specified, the destination must be a directory. </p>
<p> The <code>copy</code> command is similar to the traditional <code>cp</code> utility. </p>
<p> <font SIZE="+1"> <code>Options</code></p>
<dl>
<dt>
<dd>
<p> <code>-T</code>, <code>&#8211;no-target-directory</code></p>
<dl>
<dt>
<dd> Don&#8217;t copy into <i>DESTINATION</i> even if it is a directory.</dl>
<p> <code>-p</code>, <code>&#8211;progress</code></p>
<dl>
<dt>
<dd> Show progress.</dl>
<p> <code>-i</code>, <code>&#8211;interactive</code></p>
<dl>
<dt>
<dd> Prompt for confirmation before overwriting files.</dl>
<p> <code>&#8211;preserve</code></p>
<dl>
<dt>
<dd> Preserve all attributes of copied files.</dl>
<p> <code>-b</code>, <code>&#8211;backup</code></p>
<dl>
<dt>
<dd> Create backups of existing destination files.</dl>
<p> <code>-P</code>, <code>&#8211;no-dereference</code></p>
<dl>
<dt>
<dd> Never follow symbolic links.</dl>
<p> <code>&#8211;default-permissions</code></p>
<dl>
<dt>
<dd> Use the default permissions of the current process for the destination file, rather than copying the permissions of the source file.</dl>
</dl>
</dl>
<p> <code>info</code> [<i>OPTION</i>&#8230;] <i>LOCATION</i>&#8230;</p>
<dl>
<dt>
<dd> Shows information about the given locations. </p>
<p> The <code>info</code> command is similar to the traditional <code>ls</code> utility. </p>
<p> </font><font SIZE="+2"> <code>Options</code></p>
<dl>
<dt>
<dd>
<p> <code>-w</code>, <code>&#8211;query-writable</code></p>
<dl>
<dt>
<dd> List writable attributes.</dl>
<p> <code>-f</code>, <code>&#8211;filesystem</code></p>
<dl>
<dt>
<dd> Show information about the filesystem that the given locations reside on.</dl>
<p> <code>-a</code> <code>&#8211;attributes=</code><i>ATTRIBUTES</i></p>
<dl>
<dt>
<dd> The attributes to get. </p>
<p> Attributes can be specified with their GIO name, e.g. standard::icon, or just by namespace, e.g. unix, or by *, which matches all attributes. Several attributes or groups of attributes can be specified, separated by comma. </p>
<p> By default, all attributes are listed.</dl>
<p> <code>-n</code>, <code>&#8211;nofollow-symlinks</code></p>
<dl>
<dt>
<dd> Don&#8217;t follow symbolic links.</dl>
</dl>
</dl>
<p> <code>launch</code> <i>DESKTOP-FILE</i> [<i>FILE-ARG</i>&#8230;]</p>
<dl>
<dt>
<dd> Launch a desktop file from any location given. </p>
<p> The <code>launch</code> command extends the behavior of the <code>open</code> command by allowing any desktop file to be launched, not only those registered as file handlers.</dl>
<p> <code>list</code> [<i>OPTION</i>&#8230;] [<i>LOCATION</i>&#8230;]</p>
<dl>
<dt>
<dd> Lists the contents of the given locations. If no location is given, the contents of the current directory are shown. </p>
<p> The <code>list</code> command is similar to the traditional <code>ls</code> utility. </p>
<p> </font><font SIZE="+3"> <code>Options</code></p>
<dl>
<dt>
<dd>
<p> <code>-a</code> <code>&#8211;attributes=</code><i>ATTRIBUTES</i></p>
<dl>
<dt>
<dd> The attributes to get. </p>
<p> Attributes can be specified with their GIO name, e.g. standard::icon, or just by namespace, e.g. unix, or by *, which matches all attributes. Several attributes or groups of attributes can be specified, separated by comma. </p>
<p> By default, all attributes are listed.</dl>
<p> <code>-h</code>, <code>&#8211;hidden</code></p>
<dl>
<dt>
<dd> Show hidden files.</dl>
<p> <code>-l</code>, <code>&#8211;long</code></p>
<dl>
<dt>
<dd> Use a long listing format.</dl>
<p> <code>-n</code>, <code>&#8211;nofollow-symlinks</code></p>
<dl>
<dt>
<dd> Don&#8217;t follow symbolic links.</dl>
<p> <code>-d</code>, <code>&#8211;print-display-names</code></p>
<dl>
<dt>
<dd> Print display names.</dl>
<p> <code>-u</code>, <code>&#8211;print-uris</code></p>
<dl>
<dt>
<dd> Print full URIs.</dl>
</dl>
</dl>
<p> <code>mime</code> <i>MIMETYPE</i> [<i>HANDLER</i>]</p>
<dl>
<dt>
<dd> If no handler is given, the <code>mime</code> command lists the registered and recommended applications for the mimetype. If a handler is given, it is set as the default handler for the mimetype. </p>
<p> Handlers must be specified by their desktop file name, including the extension. Example: org.gnome.gedit.desktop.</dl>
<p> <code>mkdir</code> [<i>OPTION</i>&#8230;] <i>LOCATION</i>&#8230;</p>
<dl>
<dt>
<dd> Creates directories. </p>
<p> The <code>mkdir</code> command is similar to the traditional <code>mkdir</code> utility. </p>
<p> </font><font SIZE="+4"> <code>Options</code></p>
<dl>
<dt>
<dd>
<p> <code>-p</code>, <code>&#8211;parent</code></p>
<dl>
<dt>
<dd> Create parent directories when necessary.</dl>
</dl>
</dl>
<p> <code>monitor</code> [<i>OPTION</i>&#8230;] [<i>LOCATION</i>&#8230;]</p>
<dl>
<dt>
<dd> Monitors files or directories for changes, such as creation deletion, content and attribute changes, and mount and unmount operations affecting the monitored locations. </p>
<p> The <code>monitor</code> command uses the GIO file monitoring APIs to do its job. GIO has different implementations for different platforms. The most common implementation on Linux uses inotify. </p>
<p> </font><font SIZE="+5"> <code>Options</code></p>
<dl>
<dt>
<dd>
<p> <code>-d</code>, <code>&#8211;dir=</code><i>LOCATION</i></p>
<dl>
<dt>
<dd> Monitor the given location as a directory. Normally, the file type is used to determine whether to monitor a file or directory.</dl>
<p> <code>-f</code>, <code>&#8211;file=</code><i>LOCATION</i></p>
<dl>
<dt>
<dd> Monitor the given location as a file. Normally, the file type is used to determine whether to monitor a file or directory.</dl>
<p> <code>-D</code>, <code>&#8211;direct=</code><i>LOCATION</i></p>
<dl>
<dt>
<dd> Monitor the file directly. This allows changes made via hardlinks to be captured.</dl>
<p> <code>-s</code>, <code>&#8211;silent=</code><i>LOCATION</i></p>
<dl>
<dt>
<dd> Monitor the file directly, but don&#8217;t report changes.</dl>
<p> <code>-n</code>, <code>&#8211;no-moves</code></p>
<dl>
<dt>
<dd> Report moves and renames as simple deleted/created events.</dl>
<p> <code>-m</code>, <code>&#8211;mounts</code></p>
<dl>
<dt>
<dd> Watch for mount events.</dl>
</dl>
</dl>
<p> <code>mount</code> [<i>OPTION</i>&#8230;] [<i>LOCATION</i>&#8230;]</p>
<dl>
<dt>
<dd> Provides commandline access to various aspects of GIO&#8217;s mounting functionality. </p>
<p> Mounting refers to the traditional concept of arranging multiple file systems and devices in a single tree, rooted at /. Classical mounting happens in the kernel and is controlled by the mount utility. GIO expands this concept by introducing mount daemons that can make file systems available to GIO applications without kernel involvement. </p>
<p> GIO mounts can require authentication, and the <code>mount</code> command may ask for user IDs, passwords, and so on, when required. </p>
<p> </font><font SIZE="+6"> <code>Options</code></p>
<dl>
<dt>
<dd>
<p> <code>-m</code>, <code>&#8211;mountable</code></p>
<dl>
<dt>
<dd> Mount as mountable.</dl>
<p> <code>-d</code>, <code>&#8211;device=</code><i>ID</i></p>
<dl>
<dt>
<dd> Mount volume with device file, or other identifier.</dl>
<p> <code>-u</code>, <code>&#8211;unmount</code></p>
<dl>
<dt>
<dd> Unmount the location.</dl>
<p> <code>-e</code>, <code>&#8211;eject</code></p>
<dl>
<dt>
<dd> Eject the location.</dl>
<p> <code>-t</code>, <code>&#8211;stop=</code><i>DEVICE</i></p>
<dl>
<dt>
<dd> Stop drive with device file.</dl>
<p> <code>-s</code>, <code>&#8211;unmount-scheme=</code><i>SCHEME</i></p>
<dl>
<dt>
<dd> Unmount all mounts with the given scheme.</dl>
<p> <code>-f</code>, <code>&#8211;force</code></p>
<dl>
<dt>
<dd> Ignore outstanding file operations when unmounting or ejecting.</dl>
<p> <code>-a</code>, <code>&#8211;anonymous</code></p>
<dl>
<dt>
<dd> Use an anonymous user when authenticating.</dl>
<p> <code>-l</code>, <code>&#8211;list</code></p>
<dl>
<dt>
<dd> List all GIO mounts.</dl>
<p> <code>-o</code>, <code>&#8211;monitor</code></p>
<dl>
<dt>
<dd> Monitor mount-related events.</dl>
<p> <code>-i</code>, <code>&#8211;detail</code></p>
<dl>
<dt>
<dd> Show extra information.</dl>
<p> <code>&#8211;tcrypt-pim</code></p>
<dl>
<dt>
<dd> The numeric PIM when unlocking a VeraCrypt volume.</dl>
<p> <code>&#8211;tcrypt-hidden</code></p>
<dl>
<dt>
<dd> Mount a TCRYPT hidden volume.</dl>
<p> <code>&#8211;tcrypt-system</code></p>
<dl>
<dt>
<dd> Mount a TCRYPT system volume.</dl>
</dl>
</dl>
<p> <code>move</code> [<i>OPTION</i>&#8230;] <i>SOURCE</i>&#8230; <i>DESTINATION</i></p>
<dl>
<dt>
<dd> Moves one or more files from <i>SOURCE</i> to <i>DESTINATION</i>. If more than one source is specified, the destination must be a directory. </p>
<p> The <code>move</code> command is similar to the traditional <code>mv</code> utility. </p>
<p> </font><font SIZE="+7"> <code>Options</code></p>
<dl>
<dt>
<dd>
<p> <code>-T</code>, <code>&#8211;no-target-directory</code></p>
<dl>
<dt>
<dd> Don&#8217;t copy into <i>DESTINATION</i> even if it is a directory.</dl>
<p> <code>-p</code>, <code>&#8211;progress</code></p>
<dl>
<dt>
<dd> Show progress.</dl>
<p> <code>-i</code>, <code>&#8211;interactive</code></p>
<dl>
<dt>
<dd> Prompt for confirmation before overwriting files.</dl>
<p> <code>-b</code>, <code>&#8211;backup</code></p>
<dl>
<dt>
<dd> Create backups of existing destination files.</dl>
<p> <code>-C</code>, <code>&#8211;no-copy-fallback</code></p>
<dl>
<dt>
<dd> Don&#8217;t use copy and delete fallback.</dl>
</dl>
</dl>
<p> <code>open</code> <i>LOCATION</i>&#8230;</p>
<dl>
<dt>
<dd> Opens files with the default application that is registered to handle files of this type. </p>
<p> GIO obtains this information from the shared-mime-info database, with per-user overrides stored in <code>$XDG_DATA_HOME</code>/applications/mimeapps.list. </p>
<p> The <code>mime</code> command can be used to change the default handler for a mimetype. </p>
<p> Environment variables will not be set on the application, as it may be an existing process which is activated to handle the new file.</dl>
<p> <code>rename</code> <i>LOCATION</i> <i>NAME</i></p>
<dl>
<dt>
<dd> Renames a file. </p>
<p> The <code>rename</code> command is similar to the traditional <code>rename</code> utility.</dl>
<p> <code>remove</code> [<i>OPTION</i>&#8230;] <i>LOCATION</i>&#8230;</p>
<dl>
<dt>
<dd> Deletes each given file. </p>
<p> This command removes files irreversibly. If you want a reversible way to remove files, see the <code>trash</code> command. </p>
<p> Note that not all URI schemes that are supported by GIO may allow deletion of files. </p>
<p> The <code>remove</code> command is similar to the traditional <code>rm</code> utility. </p>
<p> </font><font SIZE="+8"> <code>Options</code></p>
<dl>
<dt>
<dd>
<p> <code>-f</code>, <code>&#8211;force</code></p>
<dl>
<dt>
<dd> Ignore non-existent and non-deletable files.</dl>
</dl>
</dl>
<p> <code>save</code> [<i>OPTION</i>&#8230;] <i>DESTINATION</i></p>
<dl>
<dt>
<dd> Reads from standard input and saves the data to the given location. </p>
<p> This is similar to just redirecting output to a file using traditional shell syntax, but the <code>save</code> command allows saving to location that GIO can write to. </p>
<p> </font><font SIZE="+9"> <code>Options</code></p>
<dl>
<dt>
<dd>
<p> <code>-b</code>, <code>&#8211;backup</code></p>
<dl>
<dt>
<dd> Back up existing destination files.</dl>
<p> <code>-c</code>, <code>&#8211;create</code></p>
<dl>
<dt>
<dd> Only create the destination if it doesn&#8217;t exist yet.</dl>
<p> <code>-a</code>, <code>&#8211;append</code></p>
<dl>
<dt>
<dd> Append to the end of the file.</dl>
<p> <code>-p</code>, <code>&#8211;private</code></p>
<dl>
<dt>
<dd> When creating, restrict access to the current user.</dl>
<p> <code>-u</code>, <code>&#8211;unlink</code></p>
<dl>
<dt>
<dd> When replacing, replace as if the destination did not exist.</dl>
<p> <code>-v</code>, <code>&#8211;print-etag</code></p>
<dl>
<dt>
<dd> Print the new ETag in the end.</dl>
<p> <code>-e</code>, <code>&#8211;etag=</code><i>ETAG</i></p>
<dl>
<dt>
<dd> The ETag of the file that is overwritten.</dl>
</dl>
</dl>
<p> <code>set</code> <i>LOCATION</i> <i>ATTRIBUTE</i> <i>VALUE</i>&#8230;</p>
<dl>
<dt>
<dd> Sets a file attribute on a file. </p>
<p> File attributes can be specified with their GIO name, e.g standard::icon. Note that not all GIO file attributes are writable. Use the <code>&#8211;query-writable</code> option of the <code>info</code> command to list writable file attributes. </p>
<p> If the <i>TYPE</i> is unset, <i>VALUE</i> does not have to be specified. If the <i>TYPE</i> is stringv, multiple values can be given. </p>
<p> <code>Options</code></p>
<dl>
<dt>
<dd>
<p> <code>-t</code>, <code>&#8211;type=</code><i>TYPE</i></p>
<dl>
<dt>
<dd> Specifies the type of the attribute. Supported types are string, stringv, bytestring, boolean, uint32, int32, uint64, int64 and unset. </p>
<p> If the type is not specified, string is assumed.</dl>
<p> <code>-n</code>, <code>&#8211;nofollow-symlinks</code></p>
<dl>
<dt>
<dd> Don&#8217;t follow symbolic links.</dl>
</dl>
</dl>
<p> <code>trash</code> [<i>OPTION</i>&#8230;] [<i>LOCATION</i>&#8230;]</p>
<dl>
<dt>
<dd> Sends files or directories to the &#8216;Trashcan&#8217; or restore them from &#8216;Trashcan&#8217;. This can be a different folder depending on where the file is located, and not all file systems support this concept. In the common case that the file lives inside a user&#8217;s home directory, the trash folder is <code>$XDG_DATA_HOME</code>/Trash. </p>
<p> Note that moving files to the trash does not free up space on the file system until the &#8216;Trashcan&#8217; is emptied. If you are interested in deleting a file irreversibly, see the <code>remove</code> command. </p>
<p> Inspecting and emptying the &#8216;Trashcan&#8217; is normally supported by graphical file managers such as Nautilus, but you can also see the trash with the command: <code>gio trash &#8211;list</code> or <code>gio list trash://</code>. </p>
<p> <code>Options</code></p>
<dl>
<dt>
<dd>
<p> <code>-f</code>, <code>&#8211;force</code></p>
<dl>
<dt>
<dd> Ignore non-existent and non-deletable files.</dl>
<p> <code>&#8211;empty</code></p>
<dl>
<dt>
<dd> Empty the trash.</dl>
<p> <code>&#8211;list</code></p>
<dl>
<dt>
<dd> List files in the trash with their original locations</dl>
<p> <code>&#8211;restore</code></p>
<dl>
<dt>
<dd> Restore a file from trash to its original location. A URI beginning with trash:// is expected here. If the original directory doesn&#8217;t exist, it will be recreated.</dl>
</dl>
</dl>
<p> <code>tree</code> [<i>OPTION</i>&#8230;] [<i>LOCATION</i>&#8230;]</p>
<dl>
<dt>
<dd> Lists the contents of the given locations recursively, in a tree-like format. If no location is given, it defaults to the current directory. </p>
<p> The <code>tree</code> command is similar to the traditional <code>tree</code> utility. </p>
<p> <code>Options</code></p>
<dl>
<dt>
<dd>
<p> <code>-h</code>, <code>&#8211;hidden</code></p>
<dl>
<dt>
<dd> Show hidden files.</dl>
<p> <code>-l</code>, <code>&#8211;follow-symlinks</code></p>
<dl>
<dt>
<dd> Follow symbolic links.</dl>
</dl>
</dl>
<p> </font></p>
<h2>EXIT STATUS</h2>
<p> On success 0 is returned, a non-zero failure code otherwise.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cat/">cat</a></code>(1), <code><a href="/docs/linux/man/1-cp/">cp</a></code>(1), <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1), <code><a href="/docs/linux/man/1-mkdir/">mkdir</a></code>(1), <code><a href="/docs/linux/man/1-mv/">mv</a></code>(1), <code><a href="/docs/linux/man/1-rm/">rm</a></code>(1), <code><a href="/docs/linux/man/1-tree/">tree</a></code>(1). </p>
<h2>Index</h2>
