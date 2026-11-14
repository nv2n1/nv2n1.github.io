---
title: "shigofumi(1)"
name: "shigofumi"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shigofumi/"
description: "shigofumi – ISDS client"
---

<h2 class="name">NAME</h2>
<p> shigofumi &#8211; ISDS client </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>shigofumi</code> [<code>-c</code>&nbsp;<wbr><i>FILE</i>]</p>
<dt> <code>shigofumi</code> [<code>-c</code>&nbsp;<wbr><i>FILE</i>] <code>-e</code>&nbsp;<wbr><i>COMMANDS</i></p>
<dt> <code>shigofumi</code> <code>-V</code></dl>
<h2>DESCRIPTION</h2>
<dd>Shigofumi is an ISDS client based on libisds library. The client can access ISDS, processes local message and delivery details, and submit file to authorized conversion. </p>
<p> Shigofumi is command line oriented program. Once you start it, use <code>help</code> to get list of embedded commands. Use <code>help </code><i>COMMAND</i> to get details about selected <i>COMMAND</i>. Be ware that command listing changes contextually. User can use casual readline shortcuts for line editing (like tab completing). </p>
<p> While transmitting data over Internet, a progress-bar is updated. User can cancel current network operation by emitting SIGINT signal (Ctrl+C usually).</p>
<h2>OPTIONS</h2>
<p> <code>-c </code><i>FILE</i></p>
<dl>
<dt>
<dd> Use configuration <i>FILE</i> instead of default one.</dl>
<p> <code>-e </code><i>COMMANDS</i></p>
<dl>
<dt>
<dd> Run shigofumi in batch mode: execute each command and terminate then. </p>
<p> Commands are delimited by new line (
 or ). If any command fails, other commands will not be processed and shigofumi will quit immediately with non-zero exit code. If all commands succeed, shigofumi will return zero code. </p>
<p> <code>Example 1. Authorized Conversion from Shell</code> </p>
<dl>
<dt>
<dd>
<pre>
$ shigofumi -e 'convert /etc/passwd'
</pre>
</dl>
<p> The command submits /etc/passwd file to authorized conversion. Although it&#8217;s syntactically correct, it will fail because plain text files are not allowed to be converted. Check always return code in your scripts.</dl>
<p> <code>-V</code></p>
<dl>
<dt>
<dd> Show program version and linked libraries details and exit.</dl>
<h2>SHIGOFUMI COMMAND LANGUAGE</h2>
<p> The language is straightforward. Each command is one case sensitive word followed by (empty) sequence of arguments. Command and arguments are separated by one or more white spaces. If you need to embed white space into argument, use backslash (\) to escape it. If you need to write backslash, escape it with backslash again. Also quotation is supported with double quotes (&quot;). White space and pipe symbol loose their delimiting properties until next double quotes. Backslash is still meta-character inside quoted string and it can be used to embed double quotes into quoted string. </p>
<p> The argument list can be terminated prematurely with pipe character (|). In that case, the rest of the line will be considered as shell command and output of preceding shigofumi command will be passed to standard input of the shell command. </p>
<p> If argument type is file name, you can use tilde symbol (~) as abbreviation for user&#8217;s home directory. Home directory is derived from <code>HOME</code> environment variable. </p>
<p> Command names, file names and message identifiers can be completed by pressing completion key (depends on readline configuration, Tab usually). They are expanded only after commands expecting argument of appropriate type. </p>
<p> Set of available commands changes with context. E.g. If a message is loaded, commands for message operation like save to file will become available. Also meaning of the same command can change. E.g. <code>show</code> command will print list of incoming messages if such list is loaded; if a message is loaded, it will print the message. List of currently available commands can be obtained by <code>help</code> command. </p>
<p> Syntax help for a command is printed after calling command with invalid option or by <code>help</code> command with interested command as first argument. Command option <code>-h</code> is reserved as invalid option and shows always command usage.</p>
<h2>ISDS</h2>
<p> ISDS (Informační systém datových schránek / Data Box Information System) is defined by m[blue]<code>Czech ISDS Act (300/2008 Coll.)</code>m[]<font SIZE="-2">[1]</font> and implied documents. Current implementation details are described in Provozní řád that can be downloaded from m[blue]<code>Dokumenty ke stažení section of ISDS Information Portal</code>m[]<font SIZE="-2">[2]</font>. </p>
<p> The system is designed to deliver messages between public authorities (government, courts etc.) and other entities (corporations, persons, other government or municipality offices) in reliable and traceable way. </p>
<p> Shigofumi implements following ISDS operations: Log in by name and password, Log in by name and password and one-time pasword, Log in by name and/or password and/or X.509 certificate, Listing incoming and outgoing message, Accepting commercial message, Retrieving incoming and outgoing message, Explicit marking a message as read, Verifying message hash, Getting message hash stored in ISDS, Verifying message authenticity, Retrieving delivery details, Getting message sender name, Sending a message to one or more recipients, Searching a box by any criteria, Searching a box by full-text, Getting a box status, Changing user password, Getting user password expiration time, Getting details about user&#8217;s box, Listing box users, Getting archive with list of all boxes, Re-signing message or delivery datails, Getting details about credit for sending commercial messages. </p>
<p> In addition, Shigofumi can save a message and delivery details into local file and load it later again. Program can save each document into local file.</p>
<h2>AUTHORIZED CONVERSION</h2>
<p> Czech government offers a document conversion from digital to analogue form and vice versa preserving legal impacts. This is done at Czech POINT meeting place (in government, municipality or post office usually). Visit m[blue]<code>Czech POINT web site</code>m[]<font SIZE="-2">[3]</font> for more details. </p>
<p> Shigofumi allows to submit a digital document (local file or document delivered by an ISDS message) for authorized conversion into Czech POINT deposit. If deposit accepts the document, it will return a document identifier that user is required to tell to an officer in a office where he wants to obtain analogue version of his document. </p>
<p> Please note the deposit keeps submitted document for limited period only. Old documents (30 days currently) are removed automatically. Note also PDF documents with valid digital signature can be converted only.</p>
<h2>ENVIRONMENT</h2>
<p> <code>EDITOR</code></p>
<dl>
<dt>
<dd> Text editor to use if <code>VISUAL</code> is not set.</dl>
<p> <code>VISUAL</code></p>
<dl>
<dt>
<dd> Text editor to use.</dl>
<h2>FILES</h2>
<p> ~/.shigofumirc</p>
<dl>
<dt>
<dd> Default configuration file location.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-shigofumirc/">shigofumirc</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> <code>Petr Písař</code></p>
<dl>
<dt>
<dd> He&#8217;s written Shigofumi and libisds.</dl>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Czech<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ISDS Act&nbsp;<wbr>(300/2008 Coll.)</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://portal.gov.cz/zakon/300/2008">http://portal.gov.cz/zakon/300/2008</a></dl>
<dt> 2.</p>
<dd> Dokumenty ke stažení section of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ISDS Information Portal</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.datoveschranky.info/ke-stazeni">http://www.datoveschranky.info/ke-stazeni</a></dl>
<dt> 3.</p>
<dd> Czech POINT web site</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://www.czechpoint.cz/">https://www.czechpoint.cz/</a></dl>
</dl>
<h2>Index</h2>
