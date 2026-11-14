---
title: "opensc-explorer(1)"
name: "opensc-explorer"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opensc-explorer/"
description: "opensc-explorer – generic interactive utility for accessing smart card and similar security token functions"
---

<h2 class="name">NAME</h2>
<p> opensc-explorer &#8211; generic interactive utility for accessing smart card and similar security token functions </p>
<h2>SYNOPSIS</h2>
<p> <code>opensc-explorer</code> [OPTIONS]</p>
<h2>DESCRIPTION</h2>
<p> The <code>opensc-explorer</code> utility can be used interactively to perform miscellaneous operations such as exploring the contents of or sending arbitrary APDU commands to a smart card or similar security token.</p>
<h2>OPTIONS</h2>
<p> The following are the command-line options for <code>opensc-explorer</code>. There are additional interactive commands available once it is running. </p>
<p> <code>&#8211;reader</code> num, <code>-r</code> num</p>
<dl>
<dt>
<dd> Use the given reader number. The default is 0, the first reader in the system.</dl>
<p> <code>&#8211;card-driver</code> driver, <code>-c</code> driver</p>
<dl>
<dt>
<dd> Use the given card driver. The default is auto-detected.</dl>
<p> <code>&#8211;verbose, -v</code></p>
<dl>
<dt>
<dd> Causes <code>opensc-explorer</code> to be more verbose. Specify this flag several times to enable debug output in the opensc library.</dl>
<h2>COMMANDS</h2>
<p> The following commands are supported at the <code>opensc-explorer</code> interactive prompt. </p>
<p> <code>ls</code></p>
<dl>
<dt>
<dd> list all files in the current DF</dl>
<p> <code>cd</code> <i>file-id</i></p>
<dl>
<dt>
<dd> change to another DF specified by <i>file-id</i></dl>
<p> <code>cat</code></p>
<dl>
<dt>
<dd> print the contents of the currently selected EF</dl>
<p> <code>info</code> [<i>file-id</i>]</p>
<dl>
<dt>
<dd> display attributes of a file specified by <i>file-id</i>. If <i>file-id</i> is not supplied, the attributes of the current file are printed.</dl>
<p> <code>create</code> <i>file-id</i> <i>size</i></p>
<dl>
<dt>
<dd> create a new EF. <i>file-id</i> specifies the id number and <i>size</i> is the size of the new file.</dl>
<p> <code>delete</code> <i>file-id</i></p>
<dl>
<dt>
<dd> remove the EF or DF specified by <i>file-id</i></dl>
<p> <code>verify</code> <i>key-type</i><i>key-id</i> [<i>key</i>]</p>
<dl>
<dt>
<dd> present a PIN or key to the card. Where <i>key-type</i> can be one of CHV, KEY or PRO. <i>key-id</i> is a number representing the key or PIN number. <i>key</i> is the key or PIN to be verified in hex. </p>
<p> Example: verify CHV0 31:32:33:34:00:00:00:00</dl>
<p> <code>change CHV</code><i>id [old-pin] new-pin</i></p>
<dl>
<dt>
<dd> change a PIN </p>
<p> Example: change CHV0 31:32:33:34:00:00:00:00 &#8216;secret&#8217;</dl>
<p> <code>put</code> <i>file-id</i> [<i>input</i>]</p>
<dl>
<dt>
<dd> copy a local file to the card. The local file is specified by <i>input</i> while the card file is specified by <i>file-id</i></dl>
<p> <code>get</code> <i>file-id</i> [<i>output</i>]</p>
<dl>
<dt>
<dd> copy an EF to a local file. The local file is specified by <i>output</i> while the card file is specified by <i>file-id</i>.</dl>
<p> <code>mkdir</code> <i>file-id</i> <i>size</i></p>
<dl>
<dt>
<dd> create a DF. <i>file-id</i> specifies the id number and <i>size</i> is the size of the new file.</dl>
<p> <code>pksign</code></p>
<dl>
<dt>
<dd> create a public key signature. NOTE: This command is currently not implemented.</dl>
<p> <code>pkdecrypt</code></p>
<dl>
<dt>
<dd> perform a public key decryption. NOTE: This command is currently not implemented.</dl>
<p> <code>erase</code></p>
<dl>
<dt>
<dd> erase the card, if the card supports it.</dl>
<p> <code>quit</code></p>
<dl>
<dt>
<dd> exit the program</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-opensc/">opensc</a>(7), <a href="/docs/linux/man/1-opensc-tool/">opensc-tool</a>(1) </p>
<h2>Index</h2>
