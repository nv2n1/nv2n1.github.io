---
title: "iceauth(1)"
name: "iceauth"
section: "1"
letter: "i"
url: "/docs/linux/man/1-iceauth/"
description: "iceauth – ICE authority file utility"
---

<h2 class="name">NAME</h2>
<p> iceauth &#8211; ICE authority file utility </p>
<h2>SYNOPSIS</h2>
<p> <code>iceauth</code> [ <code>-f</code> <i>authfile</i> ] [ <code>-vqibuV</code> ] [ <i>command arg &#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <i>iceauth</i> program is used to edit and display the authorization information used in connecting with ICE. This program is usually used to extract authorization records from one machine and merge them in on another (as is the case when using remote logins or granting access to other users). Commands (described below) may be entered interactively, on the <i>iceauth</i> command line, or in scripts.</p>
<h2>OPTIONS</h2>
<p> <code>-f</code> <i>authfile</i> Name of the authority file to use. Will default to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the file currently in use by the session. </p>
<p> <code>-v</code> Turns on extra messages (verbose mode) </p>
<p> <code>-q</code> Turns off extra messages (quiet mode) </p>
<p> <code>-i</code> Ignore the locks on the authority file </p>
<p> <code>-b</code> Break the locks on the authority file </p>
<p> <code>-u</code> Print basic usage instructions </p>
<p> <code>-V</code> Print version and exit </p>
<h2>USAGE</h2>
<p> When <i>iceauth</i> is run it will allow the following set of commands to be entered interactively or in scripts. </p>
<p> <code>?</code> </p>
<p> List available commands. </p>
<p> <code>help</code> </p>
<p> Print help information. You may supply a command name to <i>help</i> to get specific information about it. </p>
<p> <code>info</code> </p>
<p> Print information about the entries in the authority file. </p>
<p> <code>list</code> </p>
<p> List (print) entries in the authority file. You may specify optional modifiers as below to specify which entries are listed. </p>
<p> <i>list</i> [ <i>protocol_name</i> ] [ <i>protocol_data</i> ] [ <i>netid</i> ] [ <i>authname</i> ] </p>
<p> <code>add</code> </p>
<p> Add an entry to the authority file. This must be in the format </p>
<p> <i>add</i> <i>protocol_name</i> <i>protocol_data</i> <i>netid</i> <i>authname</i> <i>authdata</i> </p>
<p> <code>remove</code> </p>
<p> Remove entries from the authority file. </p>
<p> <i>remove</i> [ <i>protocol_name</i> ] [ <i>protocol_data</i> ] [ <i>netid</i> ] [ <i>authname</i> ] </p>
<p> <code>extract</code> </p>
<p> Extract entries from the authority file in to a destination file. You must supply the path to the destination to this command as in the following format. Optional specifiers allow you to narrow which entries are extracted. </p>
<p> <i>extract</i> <i>filename</i> [ <i>protocol_name</i> ] [ <i>protocol_data</i> ] [ <i>netid</i> ] [ <i>authname</i> ] </p>
<p> <code>merge</code> </p>
<p> Merge entries from other files in to the authority file selected by the program. You may supply any number of file paths to this command as follows: </p>
<p> <i>merge</i> <i>filename1</i> [ <i>filename2</i> ] [ <i>filename3</i> ] &#8230; </p>
<p> <code>exit</code> </p>
<p> Save changes and exit the program. </p>
<p> <code>quit</code> </p>
<p> Abort changes and exit the program without saving. </p>
<p> <code>source</code> </p>
<p> Read and execute commands from a file. </p>
<p> <i>source</i> <i>filename</i> </p>
<h2>AUTHOR</h2>
<p> Ralph Mor, X Consortium </p>
<h2>Index</h2>
