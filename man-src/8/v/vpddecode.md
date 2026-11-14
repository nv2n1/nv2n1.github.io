---
title: "vpddecode(8)"
name: "vpddecode"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vpddecode/"
description: "vpddecode – VPD structure decoder"
---

<p>vpddecode &#8211; <font SIZE="-1">VPD</font> structure decoder</p>
<h2>Synopsis</h2>
<p><code>vpddecode</code> [<code>OPTIONS</code>]</p>
<h2>Description</h2>
<p><code>vpddecode</code> prints the &quot;vital product data&quot; information that can be found in almost all IBM and Lenovo computers. Available items are:</p>
<dl>
<dt>&bull;</p>
<dd><font SIZE="-1">BIOS</font> Build <font SIZE="-1">ID</font></p>
<dt>&bull;</p>
<dd>Box Serial Number</p>
<dt>&bull;</p>
<dd>Motherboard Serial Number</p>
<dt>&bull;</p>
<dd>Machine Type/Model</dl>
<p> Some systems have these additional items:</p>
<dl>
<dt>&bull;</p>
<dd>BIOS Release Date</p>
<dt>&bull;</p>
<dd>Default Flash Image File Name</dl>
<p> Note that these additional items are not documented by IBM, so this is guess work, and as such should not be blindly trusted. Feedback about the accuracy of these labels is welcome.</p>
<h2>Options</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;dev-mem FILE</code></p>
<dd>Read memory from device <code>FILE</code> (default: <code>/dev/mem</code>)</p>
<dt><code>-s</code>, <code>&#8211;string KEYWORD</code></p>
<dd>Only display the value of the <font SIZE="-1">VPD</font> string identified by <code>KEYWORD</code>. <code>KEYWORD</code> must be a keyword from the following list: <code>bios-build-id</code>, <code>box-serial-number</code>, <code>motherboard-serial-number</code>, <code>machine-type-model</code>, <code>bios-release-date</code>. Each keyword corresponds to an offset and a length within the <font SIZE="-1">VPD</font> record. Not all strings may be defined on all <font SIZE="-1">VPD</font>-enabled systems. If <code>KEYWORD</code> is not provided or not valid, a list of all valid keywords is printed and <code>vpddecode</code> exits with an error. This option cannot be used more than once. Mutually exclusive with <code>&#8211;dump</code>.</p>
<dt><code>-u</code>, <code>&#8211;dump</code></p>
<dd>Do not decode the VPD records, dump their contents as hexadecimal instead. Note that this is still a text output, no binary data will be thrown upon you. ASCII equivalent is displayed when possible. This option is mainly useful for debugging. Mutually exclusive with <code>&#8211;string</code>.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Display usage information and exit</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Display the version and exit</dl>
<h2>Files</h2>
<p><i>/dev/mem</i></p>
<h2>Author</h2>
<p>Jean Delvare</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-biosdecode/">biosdecode</a></code>(8), <code><a href="/docs/linux/man/8-dmidecode/">dmidecode</a></code>(8), <code><a href="/docs/linux/man/4-mem/">mem</a></code>(4), <code><a href="/docs/linux/man/8-ownership/">ownership</a></code>(8) </p>
