---
title: "zshzftpsys(1)"
name: "zshzftpsys"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zshzftpsys/"
description: "zshzftpsys – zftp function front-end"
---

<h2 class="name">NAME</h2>
<p> zshzftpsys &#8211; zftp function front-end </p>
<h2>DESCRIPTION</h2>
<p> This describes the set of shell functions supplied with the source distribution as an interface to the <code>zftp</code> builtin command, allowing you to perform FTP operations from the shell command line or within functions or scripts. The interface is similar to a traditional FTP client (e.g. the <code>ftp</code> command itself, see <i><a href="/docs/linux/man/1-ftp/">ftp</a></i>(1)), but as it is entirely done within the shell all the familiar completion, editing and globbing features, and so on, are present, and macros are particularly simple to write as they are just ordinary shell functions. </p>
<p> The prerequisite is that the <code>zftp</code> command, as described in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1) , must be available in the version of <code>zsh</code> installed at your site. If the shell is configured to load new commands at run time, it probably is: typing `<code>zmodload zsh/zftp</code>&#8216; will make sure (if that runs silently, it has worked). If this is not the case, it is possible <code>zftp</code> was linked into the shell anyway: to test this, type `<code>which zftp</code>&#8216; and if <code>zftp</code> is available you will get the message `<code>zftp: shell built-in command</code>&#8216;. </p>
<p> Commands given directly with <code>zftp</code> builtin may be interspersed between the functions in this suite; in a few cases, using <code>zftp</code> directly may cause some of the status information stored in shell parameters to become invalid. Note in particular the description of the variables <code>$ZFTP_TMOUT</code>, <code>$ZFTP_PREFS</code> and <code>$ZFTP_VERBOSE</code> for <code>zftp</code>. </p>
<h2>INSTALLATION</h2>
<p> You should make sure all the functions from the <code>Functions/Zftp</code> directory of the source distribution are available; they all begin with the two letters `<code>zf</code>&#8216;. They may already have been installed on your system; otherwise, you will need to find them and copy them. The directory should appear as one of the elements of the <code>$fpath</code> array (this should already be the case if they were installed), and at least the function <code>zfinit</code> should be autoloaded; it will autoload the rest. Finally, to initialize the use of the system you need to call the <code>zfinit</code> function. The following code in your <code>.zshrc</code> will arrange for this; assume the functions are stored in the directory <code>~/myfns</code>: </p>
<dl>
<dt>
<dd>
<pre>
<code>fpath=(~/myfns $fpath)
autoload -U zfinit
zfinit</code>
</pre>
</dl>
<p> Note that <code>zfinit</code> assumes you are using the <code>zmodload</code> method to load the <code>zftp</code> command. If it is already built into the shell, change <code>zfinit</code> to <code>zfinit -n</code>. It is helpful (though not essential) if the call to <code>zfinit</code> appears after any code to initialize the new completion system, else unnecessary <code>compctl</code> commands will be given. </p>
<h2>FUNCTIONS</h2>
<p> The sequence of operations in performing a file transfer is essentially the same as that in a standard FTP client. Note that, due to a quirk of the shell&#8217;s <code>getopts</code> builtin, for those functions that handle options you must use `<code>&#8211;</code><code>&#8211;</code>&#8216; rather than `<code>&#8211;</code>&#8216; to ensure the remaining arguments are treated literally (a single `<code>&#8211;</code>&#8216; is treated as an argument). </p>
<h3>Opening a connection</h3>
<dl>
<dt>
<dd> <code>zfparams</code> [ <i>host</i> [ <i>user</i> [ <i>password</i> &#8230; ] ] ] Set or show the parameters for a future <code>zfopen</code> with no arguments. If no arguments are given, the current parameters are displayed (the password will be shown as a line of asterisks). If a <i>host</i> is given, and either the <i>user</i> or <i>password</i> is not, they will be prompted for; also, any parameter given as `<code>?</code>&#8216; will be prompted for, and if the `<code>?</code>&#8216; is followed by a string, that will be used as the prompt. As <code>zfopen</code> calls <code>zfparams</code> to store the parameters, this usually need not be called directly.</p>
<dl>
<dt>
<dd>
<p> A single argument `<code>&#8211;</code>&#8216; will delete the stored parameters. This will also cause the memory of the last directory (and so on) on the other host to be deleted.</dl>
<dt><code>zfopen</code> [ <code>-1</code> ] [ <i>host</i> [ <i>user</i> [ <i>password</i> [ <i>account</i> ] ] ] ]</p>
<dd> If <i>host</i> is present, open a connection to that host under username <i>user</i> with password <i>password</i> (and, on the rare occasions when it is necessary, account <i>account</i>). If a necessary parameter is missing or given as `<code>?</code>&#8216; it will be prompted for. If <i>host</i> is not present, use a previously stored set of parameters.</p>
<dl>
<dt>
<dd>
<p> If the command was successful, and the terminal is compatible with <code>xterm</code> or is <code>sun-cmd</code>, a summary will appear in the title bar, giving the local <code>host:directory</code> and the remote <code>host:directory</code>; this is handled by the function <code>zftp_chpwd</code>, described below. </p>
<p> Normally, the <i>host</i>, <i>user</i> and <i>password</i> are internally recorded for later re-opening, either by a <code>zfopen</code> with no arguments, or automatically (see below). With the option `<code>-1</code>&#8216;, no information is stored. Also, if an open command with arguments failed, the parameters will not be retained (and any previous parameters will also be deleted). A <code>zfopen</code> on its own, or a <code>zfopen -1</code>, never alters the stored parameters. </p>
<p> Both <code>zfopen</code> and <code>zfanon</code> (but not <code>zfparams</code>) understand URLs of the form <code>ftp://</code><i>host</i>/<i>path&#8230;</i> as meaning to connect to the <i>host</i>, then change directory to <i>path</i> (which must be a directory, not a file). The `<code>ftp://</code>&#8216; can be omitted; the trailing `<code>/</code>&#8216; is enough to trigger recognition of the <i>path</i>. Note prefixes other than `<code>ftp:</code>&#8216; are not recognized, and that all characters after the first slash beyond <i>host</i> are significant in <i>path</i>.</dl>
<dt><code>zfanon</code> [ <code>-1</code> ] <i>host</i></p>
<dd> Open a connection <i>host</i> for anonymous FTP. The username used is `<code>anonymous</code>&#8216;. The password (which will be reported the first time) is generated as <i>user</i><code>@</code><i>host</i>; this is then stored in the shell parameter <code>$EMAIL_ADDR</code> which can alternatively be set manually to a suitable string.</dl>
<h3>Directory management</h3>
<dl>
<dt>
<dd> <code>zfcd</code> [ <i>dir</i> ]</p>
<dt>
<dd> <code>zfcd &#8211;</code></p>
<dt>
<dd> <code>zfcd</code> <i>old</i> <i>new</i> Change the current directory on the remote server: this is implemented to have many of the features of the shell builtin <code>cd</code>.</p>
<dl>
<dt>
<dd>
<p> In the first form with <i>dir</i> present, change to the directory <i>dir</i>. The command `<code>zfcd ..</code>&#8216; is treated specially, so is guaranteed to work on non-UNIX servers (note this is handled internally by <code>zftp</code>). If <i>dir</i> is omitted, has the effect of `<code>zfcd ~</code>&#8216;. </p>
<p> The second form changes to the directory previously current. </p>
<p> The third form attempts to change the current directory by replacing the first occurrence of the string <i>old</i> with the string <i>new</i> in the current directory. </p>
<p> Note that in this command, and indeed anywhere a remote filename is expected, the string which on the local host corresponds to `<code>~</code>&#8216; is converted back to a `<code>~</code>&#8216; before being passed to the remote machine. This is convenient because of the way expansion is performed on the command line before <code>zfcd</code> receives a string. For example, suppose the command is `<code>zfcd ~/foo</code>&#8216;. The shell will expand this to a full path such as `<code>zfcd /home/user2/pws/foo</code>&#8216;. At this stage, <code>zfcd</code> recognises the initial path as corresponding to `<code>~</code>&#8216; and will send the directory to the remote host as <code>~/foo</code>, so that the `<code>~</code>&#8216; will be expanded by the server to the correct remote host directory. Other named directories of the form `<code>~name</code>&#8216; are not treated in this fashion.</dl>
<dt><code>zfhere</code></p>
<dd> Change directory on the remote server to the one corresponding to the current local directory, with special handling of `<code>~</code>&#8216; as in <code>zfcd</code>. For example, if the current local directory is <code>~/foo/bar</code>, then <code>zfhere</code> performs the effect of `<code>zfcd ~/foo/bar</code>&#8216;.</p>
<dt><code>zfdir</code> [ <code>-rfd</code> ] [ <code>&#8211;</code> ] [ <i>dir-options</i> ] [ <i>dir</i> ]</p>
<dd> Produce a long directory listing. The arguments <i>dir-options</i> and <i>dir</i> are passed directly to the server and their effect is implementation dependent, but specifying a particular remote directory <i>dir</i> is usually possible. The output is passed through a pager given by the environment variable <code>$PAGER</code>, or `<code>more</code>&#8216; if that is not set.</p>
<dl>
<dt>
<dd>
<p> The directory is usually cached for re-use. In fact, two caches are maintained. One is for use when there is no <i>dir-options</i> or <i>dir</i>, i.e. a full listing of the current remote directory; it is flushed when the current remote directory changes. The other is kept for repeated use of <code>zfdir</code> with the same arguments; for example, repeated use of `<code>zfdir /pub/gnu</code>&#8216; will only require the directory to be retrieved on the first call. Alternatively, this cache can be re-viewed with the <code>-r</code> option. As relative directories will confuse <code>zfdir</code>, the <code>-f</code> option can be used to force the cache to be flushed before the directory is listed. The option <code>-d</code> will delete both caches without showing a directory listing; it will also delete the cache of file names in the current remote directory, if any.</dl>
<dt><code>zfls</code> [ <i>ls-options</i> ] [ <i>dir</i> ]</p>
<dd> List files on the remote server. With no arguments, this will produce a simple list of file names for the current remote directory. Any arguments are passed directly to the server. No pager and no caching is used.</dl>
<h3>Status commands</h3>
<dl>
<dt>
<dd> <code>zftype</code> [ <i>type</i> ] With no arguments, show the type of data to be transferred, usually ASCII or binary. With an argument, change the type: the types `<code>A</code>&#8216; or `<code>ASCII</code>&#8216; for ASCII data and `<code>B</code>&#8216; or `<code>BINARY</code>&#8216;, `<code>I</code>&#8216; or `<code>IMAGE</code>&#8216; for binary data are understood case-insensitively.</p>
<dt><code>zfstat</code> [ <code>-v</code> ]</p>
<dd> Show the status of the current or last connection, as well as the status of some of <code>zftp</code>&#8216;s status variables. With the <code>-v</code> option, a more verbose listing is produced by querying the server for its version of events, too.</dl>
<h3>Retrieving files</h3>
<p> The commands for retrieving files all take at least two options. <code>-G</code> suppresses remote filename expansion which would otherwise be performed (see below for a more detailed description of that). <code>-t</code> attempts to set the modification time of the local file to that of the remote file: see the description of the function <code>zfrtime</code> below for more information. </p>
<dl>
<dt>
<dd> <code>zfget</code> [ <code>-Gtc</code> ] <i>file1</i> &#8230; Retrieve all the listed files <i>file1</i> &#8230; one at a time from the remote server. If a file contains a `<code>/</code>&#8216;, the full name is passed to the remote server, but the file is stored locally under the name given by the part after the final `<code>/</code>&#8216;. The option <code>-c</code> (cat) forces all files to be sent as a single stream to standard output; in this case the <code>-t</code> option has no effect.</p>
<dt><code>zfuget</code> [ <code>-Gvst</code> ] <i>file1</i> &#8230;</p>
<dd> As <code>zfget</code>, but only retrieve files where the version on the remote server is newer (has a later modification time), or where the local file does not exist. If the remote file is older but the files have different sizes, or if the sizes are the same but the remote file is newer, the user will usually be queried. With the option <code>-s</code>, the command runs silently and will always retrieve the file in either of those two cases. With the option <code>-v</code>, the command prints more information about the files while it is working out whether or not to transfer them.</p>
<dt><code>zfcget</code> [ <code>-Gt</code> ] <i>file1</i> &#8230;</p>
<dd> As <code>zfget</code>, but if any of the local files exists, and is shorter than the corresponding remote file, the command assumes that it is the result of a partially completed transfer and attempts to transfer the rest of the file. This is useful on a poor connection which keeps failing.</p>
<dl>
<dt>
<dd>
<p> Note that this requires a commonly implemented, but non-standard, version of the FTP protocol, so is not guaranteed to work on all servers.</dl>
<dt>
<dd> <code>zfgcp</code> [ <code>-Gt</code> ] <i>remote-file</i> <i>local-file</i></p>
<dt>
<dd> <code>zfgcp</code> [ <code>-Gt</code> ] <i>rfile1</i> &#8230; <i>ldir</i> This retrieves files from the remote server with arguments behaving similarly to the <code>cp</code> command.</p>
<dl>
<dt>
<dd>
<p> In the first form, copy <i>remote-file</i> from the server to the local file <i>local-file</i>. </p>
<p> In the second form, copy all the remote files <i>rfile1</i> &#8230; into the local directory <i>ldir</i> retaining the same basenames. This assumes UNIX directory semantics.</dl>
</dl>
<h3>Sending files</h3>
<dl>
<dt>
<dd> <code>zfput</code> [ <code>-r</code> ] <i>file1</i> &#8230; Send all the <i>file1</i> &#8230; given separately to the remote server. If a filename contains a `<code>/</code>&#8216;, the full filename is used locally to find the file, but only the basename is used for the remote file name.</p>
<dl>
<dt>
<dd>
<p> With the option <code>-r</code>, if any of the <i>files</i> are directories they are sent recursively with all their subdirectories, including files beginning with `<code>.</code>&#8216;. This requires that the remote machine understand UNIX file semantics, since `<code>/</code>&#8216; is used as a directory separator.</dl>
<dt><code>zfuput</code> [ <code>-vs</code> ] <i>file1</i> &#8230;</p>
<dd> As <code>zfput</code>, but only send files which are newer than their remote equivalents, or if the remote file does not exist. The logic is the same as for <code>zfuget</code>, but reversed between local and remote files.</p>
<dt><code>zfcput</code> <i>file1</i> &#8230;</p>
<dd> As <code>zfput</code>, but if any remote file already exists and is shorter than the local equivalent, assume it is the result of an incomplete transfer and send the rest of the file to append to the existing part. As the FTP append command is part of the standard set, this is in principle more likely to work than <code>zfcget</code>.</p>
<dt>
<dd> <code>zfpcp</code> <i>local-file</i> <i>remote-file</i></p>
<dt>
<dd> <code>zfpcp</code> <i>lfile1</i> &#8230; <i>rdir</i> This sends files to the remote server with arguments behaving similarly to the <code>cp</code> command.</p>
<dl>
<dt>
<dd>
<p> With two arguments, copy <i>local-file</i> to the server as <i>remote-file</i>. </p>
<p> With more than two arguments, copy all the local files <i>lfile1</i> &#8230; into the existing remote directory <i>rdir</i> retaining the same basenames. This assumes UNIX directory semantics. </p>
<p> A problem arises if you attempt to use <code>zfpcp</code> <i>lfile1</i> <i>rdir</i>, i.e. the second form of copying but with two arguments, as the command has no simple way of knowing if <i>rdir</i> corresponds to a directory or a filename. It attempts to resolve this in various ways. First, if the <i>rdir</i> argument is `<code>.</code>&#8216; or `<code>..</code>&#8216; or ends in a slash, it is assumed to be a directory. Secondly, if the operation of copying to a remote file in the first form failed, and the remote server sends back the expected failure code 553 and a reply including the string `<code>Is a directory</code>&#8216;, then <code>zfpcp</code> will retry using the second form.</dl>
</dl>
<h3>Closing the connection</h3>
<dl>
<dt>
<dd> <code>zfclose</code> Close the connection.</dl>
<h3>Session management</h3>
<dl>
<dt>
<dd> <code>zfsession</code> [ <code>-lvod</code> ] [ <i>sessname</i> ] Allows you to manage multiple FTP sessions at once. By default, connections take place in a session called `<code>default</code>&#8216;; by giving the command `<code>zfsession</code> <i>sessname</i>&#8216; you can change to a new or existing session with a name of your choice. The new session remembers its own connection, as well as associated shell parameters, and also the host/user parameters set by <code>zfparams</code>. Hence you can have different sessions set up to connect to different hosts, each remembering the appropriate host, user and password.</p>
<dl>
<dt>
<dd>
<p> With no arguments, <code>zfsession</code> prints the name of the current session; with the option <code>-l</code> it lists all sessions which currently exist, and with the option <code>-v</code> it gives a verbose list showing the host and directory for each session, where the current session is marked with an asterisk. With <code>-o</code>, it will switch to the most recent previous session. </p>
<p> With <code>-d</code>, the given session (or else the current one) is removed; everything to do with it is completely forgotten. If it was the only session, a new session called `<code>default</code>&#8216; is created and made current. It is safest not to delete sessions while background commands using <code>zftp</code> are active.</dl>
<dt><code>zftransfer</code> <i>sess1</i><code>:</code><i>file1</i> <i>sess2</i><code>:</code><i>file2</i></p>
<dd> Transfer files between two sessions; no local copy is made. The file is read from the session <i>sess1</i> as <i>file1</i> and written to session <i>sess2</i> as file <i>file2</i>; <i>file1</i> and <i>file2</i> may be relative to the current directories of the session. Either <i>sess1</i> or <i>sess2</i> may be omitted (though the colon should be retained if there is a possibility of a colon appearing in the file name) and defaults to the current session; <i>file2</i> may be omitted or may end with a slash, in which case the basename of <i>file1</i> will be added. The sessions <i>sess1</i> and <i>sess2</i> must be distinct.</p>
<dl>
<dt>
<dd>
<p> The operation is performed using pipes, so it is required that the connections still be valid in a subshell, which is not the case under versions of some operating systems, presumably due to a system bug.</dl>
</dl>
<h3>Bookmarks</h3>
<p> The two functions <code>zfmark</code> and <code>zfgoto</code> allow you to `bookmark&#8217; the present location (host, user and directory) of the current FTP connection for later use. The file to be used for storing and retrieving bookmarks is given by the parameter <code>$ZFTP_BMFILE</code>; if not set when one of the two functions is called, it will be set to the file <code>.zfbkmarks</code> in the directory where your zsh startup files live (usually <code>~</code>). </p>
<dl>
<dt>
<dd> <code>zfmark</code> [ <i>bookmark</i> ] If given an argument, mark the current host, user and directory under the name <i>bookmark</i> for later use by <code>zfgoto</code>. If there is no connection open, use the values for the last connection immediately before it was closed; it is an error if there was none. Any existing bookmark under the same name will be silently replaced.</p>
<dl>
<dt>
<dd>
<p> If not given an argument, list the existing bookmarks and the points to which they refer in the form <i>user</i><code>@</code><i>host</i><code>:</code><i>directory</i>; this is the format in which they are stored, and the file may be edited directly.</dl>
<dt><code>zfgoto</code> [ <code>-n</code> ] <i>bookmark</i></p>
<dd> Return to the location given by <i>bookmark</i>, as previously set by <code>zfmark</code>. If the location has user `<code>ftp</code>&#8216; or `<code>anonymous</code>&#8216;, open the connection with <code>zfanon</code>, so that no password is required. If the user and host parameters match those stored for the current session, if any, those will be used, and again no password is required. Otherwise a password will be prompted for.</p>
<dl>
<dt>
<dd>
<p> With the option <code>-n</code>, the bookmark is taken to be a nickname stored by the <code>ncftp</code> program in its bookmark file, which is assumed to be <code>~/.ncftp/bookmarks</code>. The function works identically in other ways. Note that there is no mechanism for adding or modifying <code>ncftp</code> bookmarks from the zftp functions.</dl>
</dl>
<h3>Other functions</h3>
<p> Mostly, these functions will not be called directly (apart from <code>zfinit</code>), but are described here for completeness. You may wish to alter <code>zftp_chpwd</code> and <code>zftp_progress</code>, in particular. </p>
<dl>
<dt>
<dd> <code>zfinit</code> [ <code>-n</code> ] As described above, this is used to initialize the zftp function system. The <code>-n</code> option should be used if the zftp command is already built into the shell.</p>
<dt><code>zfautocheck</code> [ <code>-dn</code> ]</p>
<dd> This function is called to implement automatic reopening behaviour, as described in more detail below. The options must appear in the first argument; <code>-n</code> prevents the command from changing to the old directory, while <code>-d</code> prevents it from setting the variable <code>do_close</code>, which it otherwise does as a flag for automatically closing the connection after a transfer. The host and directory for the last session are stored in the variable <code>$zflastsession</code>, but the internal host/user/password parameters must also be correctly set.</p>
<dt><code>zfcd_match </code><i>prefix</i> <i>suffix</i></p>
<dd> This performs matching for completion of remote directory names. If the remote server is UNIX, it will attempt to persuade the server to list the remote directory with subdirectories marked, which usually works but is not guaranteed. On other hosts it simply calls <code>zfget_match</code> and hence completes all files, not just directories. On some systems, directories may not even look like filenames.</p>
<dt><code>zfget_match </code><i>prefix</i> <i>suffix</i></p>
<dd> This performs matching for completion of remote filenames. It caches files for the current directory (only) in the shell parameter <code>$zftp_fcache</code>. It is in the form to be called by the <code>-K</code> option of <code>compctl</code>, but also works when called from a widget-style completion function with <i>prefix</i> and <i>suffix</i> set appropriately.</p>
<dt><code>zfrglob </code><i>varname</i></p>
<dd> Perform remote globbing, as describes in more detail below. <i>varname</i> is the name of a variable containing the pattern to be expanded; if there were any matches, the same variable will be set to the expanded set of filenames on return.</p>
<dt><code>zfrtime</code> <i>lfile</i> <i>rfile</i> [ <i>time</i> ]</p>
<dd> Set the local file <i>lfile</i> to have the same modification time as the remote file <i>rfile</i>, or the explicit time <i>time</i> in FTP format <code>CCYYMMDDhhmmSS</code> for the GMT timezone. This uses the shell&#8217;s <code>zsh/datetime</code> module to perform the conversion from GMT to local time.</p>
<dt><code>zftp_chpwd</code></p>
<dd> This function is called every time a connection is opened, or closed, or the remote directory changes. This version alters the title bar of an <code>xterm</code>-compatible or <code>sun-cmd</code> terminal emulator to reflect the local and remote hostnames and current directories. It works best when combined with the function <code>chpwd</code>. In particular, a function of the form</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre><code>
chpwd()
{
    if
        [[-n $ZFTP_USER]];
    then
        zftp_chpwd else
#usual chpwd e.g put host : directory in title bar
        fi
}
</code></pre>
</dl>
<p> fits in well.</dl>
<dt><code>zftp_progress</code></p>
<dd> This function shows the status of the transfer. It will not write anything unless the output is going to a terminal; however, if you transfer files in the background, you should turn off progress reports by hand using `<code>zstyle &#8216;:zftp:*&#8217; progress none</code>&#8216;. Note also that if you alter it, any output <i>must</i> be to standard error, as standard output may be a file being received. The form of the progress meter, or whether it is used at all, can be configured without altering the function, as described in the next section.</p>
<dt><code>zffcache</code></p>
<dd> This is used to implement caching of files in the current directory for each session separately. It is used by <code>zfget_match</code> and <code>zfrglob</code>.</dl>
<h2>MISCELLANEOUS FEATURES</h2>
<h3>Configuration</h3>
<p> Various styles are available using the standard shell style mechanism, described in <i><a href="/docs/linux/man/1-zshmodules/">zshmodules</a></i>(1). Briefly, the command `<code>zstyle &#8216;:zftp:*&#8217;</code> <i>style</i> <i>value</i> &#8230;&#8217;. defines the <i>style</i> to have value <i>value</i>; more than one value may be given, although that is not useful in the cases described here. These values will then be used throughout the zftp function system. For more precise control, the first argument, which gives a context in which the style applies, can be modified to include a particular function, as for example `<code>:zftp:zfget</code>&#8216;: the style will then have the given value only in the <code>zfget</code> function. Values for the same style in different contexts may be set; the most specific function will be used, where strings are held to be more specific than patterns, and longer patterns and shorter patterns. Note that only the top level function name, as called by the user, is used; calling of lower level functions is transparent to the user. Hence modifications to the title bar in <code>zftp_chpwd</code> use the contexts <code>:zftp:zfopen</code>, <code>:zftp:zfcd</code>, etc., depending where it was called from. The following styles are understood: </p>
<dl>
<dt>
<dd> <code>progress</code> Controls the way that <code>zftp_progress</code> reports on the progress of a transfer. If empty, unset, or `<code>none</code>&#8216;, no progress report is made; if `<code>bar</code>&#8216; a growing bar of inverse video is shown; if `<code>percent</code>&#8216; (or any other string, though this may change in future), the percentage of the file transferred is shown. The bar meter requires that the width of the terminal be available via the <code>$COLUMNS</code> parameter (normally this is set automatically). If the size of the file being transferred is not available, <code>bar</code> and <code>percent</code> meters will simply show the number of bytes transferred so far.</p>
<dl>
<dt>
<dd>
<p> When <code>zfinit</code> is run, if this style is not defined for the context <code>:zftp:*</code>, it will be set to `bar&#8217;.</dl>
<dt><code>update</code></p>
<dd> Specifies the minimum time interval between updates of the progress meter in seconds. No update is made unless new data has been received, so the actual time interval is limited only by <code>$ZFTP_TIMEOUT</code>.</p>
<dl>
<dt>
<dd>
<p> As described for <code>progress</code>, <code>zfinit</code> will force this to default to 1.</dl>
<dt><code>remote-glob</code></p>
<dd> If set to `<code>1</code>&#8216;, `<code>yes</code>&#8216; or `<code>true</code>&#8216;, filename generation (globbing) is performed on the remote machine instead of by zsh itself; see below.</p>
<dt><code>titlebar</code></p>
<dd> If set to `<code>1</code>&#8216;, `<code>yes</code>&#8216; or `<code>true</code>&#8216;, <code>zftp_chpwd</code> will put the remote host and remote directory into the titlebar of terminal emulators such as xterm or sun-cmd that allow this.</p>
<dl>
<dt>
<dd>
<p> As described for <code>progress</code>, <code>zfinit</code> will force this to default to 1.</dl>
<dt><code>chpwd</code></p>
<dd> If set to `<code>1</code>&#8216; `<code>yes</code>&#8216; or `<code>true</code>&#8216;, <code>zftp_chpwd</code> will call the function <code>chpwd</code> when a connection is closed. This is useful if the remote host details were put into the terminal title bar by <code>zftp_chpwd</code> and your usual <code>chpwd</code> also modifies the title bar.</p>
<dl>
<dt>
<dd>
<p> When <code>zfinit</code> is run, it will determine whether <code>chpwd</code> exists and if so it will set the default value for the style to 1 if none exists already.</dl>
</dl>
<p> Note that there is also an associative array <code>zfconfig</code> which contains values used by the function system. This should not be modified or overwritten. </p>
<h3>Remote globbing</h3>
<p> The commands for retrieving files usually perform filename generation (globbing) on their arguments; this can be turned off by passing the option <code>-G</code> to each of the commands. Normally this operates by retrieving a complete list of files for the directory in question, then matching these locally against the pattern supplied. This has the advantage that the full range of zsh patterns (respecting the setting of the option <code>EXTENDED_GLOB</code>) can be used. However, it means that the directory part of a filename will not be expanded and must be given exactly. If the remote server does not support the UNIX directory semantics, directory handling is problematic and it is recommended that globbing only be used within the current directory. The list of files in the current directory, if retrieved, will be cached, so that subsequent globs in the same directory without an intervening <code>zfcd</code> are much faster. </p>
<p> If the <code>remote-glob</code> style (see above) is set, globbing is instead performed on the remote host: the server is asked for a list of matching files. This is highly dependent on how the server is implemented, though typically UNIX servers will provide support for basic glob patterns. This may in some cases be faster, as it avoids retrieving the entire list of directory contents. </p>
<h3>Automatic and temporary reopening</h3>
<p> As described for the <code>zfopen</code> command, a subsequent <code>zfopen</code> with no parameters will reopen the connection to the last host (this includes connections made with the <code>zfanon</code> command). Opened in this fashion, the connection starts in the default remote directory and will remain open until explicitly closed. </p>
<p> Automatic re-opening is also available. If a connection is not currently open and a command requiring a connection is given, the last connection is implicitly reopened. In this case the directory which was current when the connection was closed again becomes the current directory (unless, of course, the command given changes it). Automatic reopening will also take place if the connection was close by the remote server for whatever reason (e.g. a timeout). It is not available if the <code>-1</code> option to <code>zfopen</code> or <code>zfanon</code> was used. </p>
<p> Furthermore, if the command issued is a file transfer, the connection will be closed after the transfer is finished, hence providing a one-shot mode for transfers. This does not apply to directory changing or listing commands; for example a <code>zfdir</code> may reopen a connection but will leave it open. Also, automatic closure will only ever happen in the same command as automatic opening, i.e a <code>zfdir</code> directly followed by a <code>zfget</code> will never close the connection automatically. </p>
<p> Information about the previous connection is given by the <code>zfstat</code> function. So, for example, if that reports: </p>
<dl>
<dt>
<dd>
<pre>
<code>Session:        default
Not connected.
Last session:   <a href="ftp://ftp.bar.com">ftp.bar.com</a>:/pub/textfiles</code>
</pre>
</dl>
<p> then the command <code>zfget file.txt</code> will attempt to reopen a connection to <code><a href="ftp://ftp.bar.com">ftp.bar.com</a></code>, retrieve the file <code>/pub/textfiles/file.txt</code>, and immediately close the connection again. On the other hand, <code>zfcd ..</code> will open the connection in the directory <code>/pub</code> and leave it open. </p>
<p> Note that all the above is local to each session; if you return to a previous session, the connection for that session is the one which will be reopened. </p>
<h3>Completion</h3>
<p> Completion of local and remote files, directories, sessions and bookmarks is supported. The older, <code>compctl</code>-style completion is defined when <code>zfinit</code> is called; support for the new widget-based completion system is provided in the function <code>Completion/Zsh/Command/_zftp</code>, which should be installed with the other functions of the completion system and hence should automatically be available. </p>
<h2>Index</h2>
