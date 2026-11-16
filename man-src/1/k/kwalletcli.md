---
title: "kwalletcli(1)"
name: "kwalletcli"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kwalletcli/"
description: "kwalletcli – command line interface to the KDE Wallet"
---

<h2>NAME</h2>
<p> <code>kwalletcli</code> &#8211; command line interface to the KDE Wallet</p>
<h2>SYNOPSIS</h2>
<p> [-<code>q</code> ] &#8211;<code>hV</code><br />
 [-<code>q</code> ] &#8211;<code>f </code><i>folder</i> &#8211;<code>e </code><i>entry</i> [-<code>P | p </code><i>password</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The utility is a command line interface to KWallet. It will only work if KDE is running (DCOP) and reachable (via X11). can be used to get password entries from the Wallet, or to write them there. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-e </code><i>entry</i></dt>
<dd> Define the key (<i>entry</i> ) to use when accessing the Wallet. Mandatory.</dd>
<dt><code>-f </code><i>folder</i></dt>
<dd> Set the <i>folder</i> to use when accessing the Wallet. Mandatory.</dd>
<dt><code>-h</code></dt>
<dd> Display the usage.</dd>
<dt><code>-P</code></dt>
<dd> Read the password to write from standard input. Currently limited to 65535 octets.</dd>
<dt><code>-p </code><i>password</i></dt>
<dd> Write <i>password</i> into the designated location in the Wallet.</dd>
<dt><code>-q</code></dt>
<dd> Be more quiet. In combination with &#8211;<code>V</code> do not display anything.</dd>
<dt><code>-V</code></dt>
<dd> Display the version information.</dd></dl>
<p> Default mode of operation, that is, unless &#8211;<code>P</code> or &#8211;<code>p</code> are used, is to read the password from the Wallet and print it to standard output as-is, without any trailing newline. </p>
<p> All input and output is assumed to be in UTF-8. The password string (whether read from standard input or command line) is now converted from &#8220;possibly UTF-8 but binary transparent&#8221; to standards-conformant UTF-8 for the Qt side, and back upon reading out.</p>
<h2>RETURN VALUES</h2>
<p> The utility exits 0 on success or &gt;0 if an error occurred:</p>
<dl>
<dt><code>1</code></dt>
<dd> The entry specified cannot be found (read access).</dd>
<dt><code>2</code></dt>
<dd> The usage was shown.</dd>
<dt><code>3</code></dt>
<dd> The Wallet could not be opened. May be a missing DCOP connection. Perhaps <code>DISPLAY</code> is not set.</dd>
<dt><code>4</code></dt>
<dd> The folder specified cannot be found (read access).</dd>
<dt><code>5</code></dt>
<dd> The folder specified cannot be opened.</dd>
<dt><code>6</code></dt>
<dd> The value to the key specified could not be retrieved.</dd>
<dt><code>8</code></dt>
<dd> An error occurred trying to write the value.</dd></dl>
<p> The exit codes 1 and 4, on reading, are not fatal; they merely indicate that the folder or entry specified does not exist. The other errors are fatal and may be used to indicate the user that the KWallet should not be used any more during the current session.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></dt>
<dd> The X11 display to use for communicating with the KDE Wallet.</dd></dl>
<h2>SEE ALSO</h2>
<p> kwalletcli_getpin1</p>
<h2>AUTHORS</h2>
<p> was written by An mirabilos Aq m@mirbsd.org mostly for tarent solutions GmbH.</p>
<h2>CAVEATS</h2>
<p> Do not use &#8211;<code>p </code><i>password</i> to store it, unless you absolutely must. It is a security risk, because the command line invocation is public information in a normal Unix environment. Use &#8211;<code>P</code> instead and provide the <i>password</i> on standard input. </p>
<p> Beware of trailing newlines, especially outside of <a href="/docs/linux/man/1-mksh/">mksh</a>(1) scripts!</p>
<h2>BUGS</h2>
<p> If <code>DISPLAY</code> is not set, not valid, or <code>kdeinit</code> or <code>kdeinit4</code> cannot start for other reasons, may not recover gracefully. In KDE 4 versions, this may even result in a Segmentation fault. The author does not know of a way to catch this early; patches are welcome. </p>
<p> There is no way (yet) to set a wallet other than the default wallet. While this is a possible enhancement to the CLI, there is no feasible way to expose this functionality to the various front-ends, such as pinentry-kwallet1, anyway, so the priority of fixing this is low. </p>
<h2>Index</h2>
