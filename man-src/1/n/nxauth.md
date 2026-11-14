---
title: "nxauth(1)"
name: "nxauth"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nxauth/"
description: "nxauth – NoMachine X authority file utility"
---

<h2>NAME</h2>
<p> nxauth &#8211; NoMachine X authority file utility</p>
<h2>SYNOPSIS</h2>
<p> <code>nxauth</code> [ <code>-f</code> <i>authfile</i> ] [ <code>-vqib</code> ] [ <i>command arg &#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <i>nxauth</i> program is used to edit and display the authorization information used in connecting to the X server. This program is usually used to extract authorization records from one machine and merge them in on another (as is the case when using remote logins or granting access to other users). Commands (described below) may be entered interactively, on the <i>nxauth</i> command line, or in scripts. Note that this program does <code>not</code> contact the X server except when the generate command is used. Normally <i>nxauth</i> is not used to create the authority file entry in the first place; <i>xdm</i> does that.</p>
<h2>OPTIONS</h2>
<p> The following options may be used with <i>nxauth</i>. They may be given individually (e.g., <i>-q -i</i>) or may combined (e.g., <i>-qi</i>).</p>
<dl>
<dt><code>-f </code><i>authfile</i></p>
<dd> This option specifies the name of the authority file to use. By default, <i>nxauth</i> will use the file specified by the nxauthORITY environment variable or <i>.Xauthority</i> in the user&#8217;s home directory.</p>
<dt><code>-q</code></p>
<dd> This option indicates that <i>nxauth</i> should operate quietly and not print unsolicited status messages. This is the default if an <i>nxauth</i> command is is given on the command line or if the standard output is not directed to a terminal.</p>
<dt><code>-v</code></p>
<dd> This option indicates that <i>nxauth</i> should operate verbosely and print status messages indicating the results of various operations (e.g., how many records have been read in or written out). This is the default if <i>nxauth</i> is reading commands from its standard input and its standard output is directed to a terminal.</p>
<dt><code>-i</code></p>
<dd> This option indicates that <i>nxauth</i> should ignore any authority file locks. Normally, <i>nxauth</i> will refuse to read or edit any authority files that have been locked by other programs (usually <i>xdm</i> or another <i>nxauth</i>).</p>
<dt><code>-b</code></p>
<dd> This option indicates that <i>nxauth</i> should attempt to break any authority file locks before proceeding. Use this option only to clean up stale locks.</dl>
<h2>COMMANDS</h2>
<p> The following commands may be used to manipulate authority files:</p>
<dl>
<dt><code>add </code><i>displayname protocolname hexkey</i></p>
<dd> An authorization entry for the indicated display using the given protocol and key data is added to the authorization file. The data is specified as an even-lengthed string of hexadecimal digits, each pair representing one octet. The first digit of each pair gives the most significant 4 bits of the octet, and the second digit of the pair gives the least significant 4 bits. For example, a 32 character hexkey would represent a 128-bit value. A protocol name consisting of just a single period is treated as an abbreviation for <i>MIT-MAGIC-COOKIE-1</i>. </p>
<dt><code>generate </code><i>displayname protocolname</i> [trusted|untrusted]</p>
<dd> [timeout <i>seconds</i>] [group <i>group-id</i>] [<code>data </code><i>hexdata</i>] </p>
<p> This command is similar to add. The main difference is that instead of requiring the user to supply the key data, it connects to the server specified in <i>displayname</i> and uses the SECURITY extension in order to get the key data to store in the authorization file. If the server cannot be contacted or if it does not support the SECURITY extension, the command fails. Otherwise, an authorization entry for the indicated display using the given protocol is added to the authorization file. A protocol name consisting of just a single period is treated as an abbreviation for <i>MIT-MAGIC-COOKIE-1</i>. </p>
<p> If the <code>trusted</code> option is used, clients that connect using this authorization will have full run of the display, as usual. If <code>untrusted</code> is used, clients that connect using this authorization will be considered untrusted and prevented from stealing or tampering with data belonging to trusted clients. See the SECURITY extension specification for full details on the restrictions imposed on untrusted clients. The default is <code>untrusted</code>. </p>
<p> The <code>timeout</code> option specifies how long in seconds this authorization will be valid. If the authorization remains unused (no clients are connected with it) for longer than this time period, the server purges the authorization, and future attempts to connect using it will fail. Note that the purging done by the server does <code>not</code> delete the authorization entry from the authorization file. The default timeout is 60 seconds. </p>
<p> The <code>group</code> option specifies the application group that clients connecting with this authorization should belong to. See the application group extension specification for more details. The default is to not belong to an application group. </p>
<p> The <code>data</code> option specifies data that the server should use to generate the authorization. Note that this is <code>not</code> the same data that gets written to the authorization file. The interpretation of this data depends on the authorization protocol. The <i>hexdata</i> is in the same format as the <i>hexkey</i> described in the add command. The default is to send no data. </p>
<dt><code>[n]extract </code><i>filename displayname&#8230;</i></p>
<dd> Authorization entries for each of the specified displays are written to the indicated file. If the <i>nextract</i> command is used, the entries are written in a numeric format suitable for non-binary transmission (such as secure electronic mail). The extracted entries can be read back in using the <i>merge</i> and <i>nmerge</i> commands. If the filename consists of just a single dash, the entries will be written to the standard output.</p>
<dt><code>[n]list </code>[<i>displayname</i>&#8230;]</p>
<dd> Authorization entries for each of the specified displays (or all if no displays are named) are printed on the standard output. If the <i>nlist</i> command is used, entries will be shown in the numeric format used by the <i>nextract</i> command; otherwise, they are shown in a textual format. Key data is always displayed in the hexadecimal format given in the description of the <i>add</i> command.</p>
<dt><code>[n]merge </code>[<i>filename</i>&#8230;]</p>
<dd> Authorization entries are read from the specified files and are merged into the authorization database, superceding any matching existing entries. If the <i>nmerge</i> command is used, the numeric format given in the description of the <i>extract</i> command is used. If a filename consists of just a single dash, the standard input will be read if it hasn&#8217;t been read before.</p>
<dt><code>remove </code><i>displayname</i>&#8230;</p>
<dd> Authorization entries matching the specified displays are removed from the authority file.</p>
<dt><code>source </code><i>filename</i></p>
<dd> The specified file is treated as a script containing <i>nxauth</i> commands to execute. Blank lines and lines beginning with a sharp sign (#) are ignored. A single dash may be used to indicate the standard input, if it hasn&#8217;t already been read.</p>
<dt><code>info</code></p>
<dd> Information describing the authorization file, whether or not any changes have been made, and from where <i>nxauth</i> commands are being read is printed on the standard output.</p>
<dt><code>exit</code></p>
<dd> If any modifications have been made, the authority file is written out (if allowed), and the program exits. An end of file is treated as an implicit <i>exit</i> command.</p>
<dt><code>quit</code></p>
<dd> The program exits, ignoring any modifications. This may also be accomplished by pressing the interrupt character.</p>
<dt><code>help [</code><i>string</i>]</p>
<dd> A description of all commands that begin with the given string (or all commands if no string is given) is printed on the standard output.</p>
<dt><code>?</code></p>
<dd> A short list of the valid commands is printed on the standard output.</dl>
<h2>DISPLAY NAMES</h2>
<p> Display names for the <i>add</i>, <i>[n]extract</i>, <i>[n]list</i>, <i>[n]merge</i>, and <i>remove</i> commands use the same format as the DISPLAY environment variable and the common <i>-display</i> command line argument. Display-specific information (such as the screen number) is unnecessary and will be ignored. Same-machine connections (such as local-host sockets, shared memory, and the Internet Protocol hostname <i>localhost</i>) are referred to as <i>hostname</i>/unix:<i>displaynumber</i> so that local entries for different machines may be stored in one authority file.</p>
<h2>EXAMPLE</h2>
<p> The most common use for <i>nxauth</i> is to extract the entry for the current display, copy it to another machine, and merge it into the user&#8217;s authority file on the remote machine: </p>
<pre>
        %  nxauth extract - $DISPLAY | rsh otherhost nxauth merge -
</pre>
<p> The following command contacts the server :0 to create an authorization using the MIT-MAGIC-COOKIE-1 protocol. Clients that connect with this authorization will be untrusted. </p>
<pre>
        %  nxauth generate :0 .
</pre>
<h2>ENVIRONMENT</h2>
<p> This <i>nxauth</i> program uses the following environment variables:</p>
<dl>
<dt><code>XAUTHORITY</code></p>
<dd> to get the name of the authority file to use if the <i>-f</i> option isn&#8217;t used.</p>
<dt><code>HOME</code></p>
<dd> to get the user&#8217;s home directory if XAUTHORITY isn&#8217;t defined.</dl>
<h2>FILES</h2>
<dl>
<dt><i>$HOME/.Xauthority</i></p>
<dd> default authority file if XAUTHORITY isn&#8217;t defined.</dl>
<h2>BUGS</h2>
<p> Users that have unsecure networks should take care to use encrypted file transfer mechanisms to copy authorization entries between machines. Similarly, the <i>MIT-MAGIC-COOKIE-1</i> protocol is not very useful in unsecure environments. Sites that are interested in additional security may need to use encrypted authorization mechanisms such as Kerberos. </p>
<p> Spaces are currently not allowed in the protocol name. Quoting could be added for the truly perverse.</p>
<h2>AUTHOR</h2>
<p> Jim Fulton, MIT X Consortium </p>
<h2>Index</h2>
