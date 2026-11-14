---
title: "phar7-2(1)"
name: "phar7-2"
section: "1"
letter: "p"
url: "/docs/linux/man/1-phar7-2/"
description: "phar, phar.phar – PHAR (PHP archive) command line tool"
---

<p>phar, phar.phar &#8211; PHAR (PHP archive) command line tool </p>
<h2>Synopsis</h2>
<p><code>phar</code> &lt;command&gt; [options] &#8230; </p>
<h2>Description</h2>
<p>The <code>PHAR</code> file format provides a way to put entire PHP applications into a single file called a &quot;phar&quot; (PHP Archive) for easy distribution and installation. </p>
<p> With the <code>phar</code> command you can create, update or extract PHP archives. </p>
<p> Commands: add compress delete extract help help-list info list meta-del meta-get meta-set pack sign stub-get stub-set tree version </p>
<h2>add command</h2>
<p>Add entries to a PHAR package. </p>
<p> Required arguments:</p>
<dl COMPACT>
<dd><code>-f </code><i>file</i> Specifies the phar <i>file</i> to work on.</p>
<dd><code>&#8230;</code> Any number of input files and directories. If -i is in use then ONLY files and matching the given regular expression are being packed. If -x is given then files matching that regular expression are NOT being packed.</dl>
<p> Optional arguments:</p>
<dl COMPACT>
<dd><code>-a </code><i>alias</i> Provide an <i>alias</i> name for the phar file.</p>
<dd><code>-c </code><i>algo</i> Compression algorithm (see <font SIZE="-1"><code>COMPRESSION</code> </font> )</p>
<dd><code>-i </code><i>regex</i> Specifies a regular expression for input files.</p>
<dd><code>-l </code><i>level</i> Number of preceding subdirectories to strip from file entries</p>
<dd><code>-x </code><i>regex</i> Regular expression for input files to exclude. </p>
</dl>
<h2>compress command</h2>
<p>Compress or uncompress all files or a selected entry. </p>
<p> Required arguments:</p>
<dl COMPACT>
<dd><code>-c </code><i>algo</i> Compression algorithm (see <font SIZE="-1"><code>COMPRESSION</code> </font> )</p>
<dd><code>-f </code><i>file</i> Specifies the phar <i>file</i> to work on.</dl>
<p> Optional arguments:</p>
<dl COMPACT>
<dd><code>-e </code><i>entry</i> Name of <i>entry</i> to work on (must include PHAR internal directory name if any). </p>
</dl>
<h2>delete command</h2>
<p>Delete entry from a PHAR archive </p>
<p> Required arguments:</p>
<dl COMPACT>
<dd><code>-e </code><i>entry</i> Name of <i>entry</i> to work on (must include PHAR internal directory name if any).</p>
<dd><code>-f </code><i>file</i> Specifies the phar <i>file</i> to work on. </p>
</dl>
<h2>extract command</h2>
<p>Extract a PHAR package to a directory. </p>
<p> Required arguments:</p>
<dl COMPACT>
<dd><code>-f </code><i>file</i> Specifies the phar <i>file</i> to work on.</dl>
<p> Optional arguments:</p>
<dl COMPACT>
<dd><code>-i </code><i>regex</i> Specifies a regular expression for input files.</p>
<dd><code>-x </code><i>regex</i> Regular expression for input files to exclude.</p>
<dd><code>&#8230;</code> Directory to extract to (defaults to &#8216;.&#8217;). </p>
</dl>
<h2>help command</h2>
<p>This help or help for a selected command. </p>
<p> Optional arguments:</p>
<dl COMPACT>
<dd><code>&#8230;</code> Optional command to retrieve help for. </p>
</dl>
<h2>help-list command</h2>
<p>Lists available commands. </p>
<h2>info command</h2>
<p>Get information about a PHAR package. </p>
<p> By using -k it is possible to return a single value. </p>
<p> Required arguments:</p>
<dl COMPACT>
<dd><code>-f </code><i>file</i> Specifies the phar <i>file</i> to work on.</dl>
<p> Optional arguments:</p>
<dl COMPACT>
<dd><code>-k </code><i>index</i> Subscription <i>index</i> to work on. </p>
</dl>
<h2>list command</h2>
<p>List contents of a PHAR archive. </p>
<p> Required arguments:</p>
<dl COMPACT>
<dd><code>-f </code><i>file</i> Specifies the phar <i>file</i> to work on.</dl>
<p> Optional arguments:</p>
<dl COMPACT>
<dd><code>-i </code><i>regex</i> Specifies a regular expression for input files.</p>
<dd><code>-x </code><i>regex</i> Regular expression for input files to exclude. </p>
</dl>
<h2>meta-del command</h2>
<p>Delete meta information of a PHAR entry or a PHAR package. </p>
<p> If -k is given then the metadata is expected to be an array and the given index is being deleted. </p>
<p> If something was deleted the return value is 0 otherwise it is 1. </p>
<p> Required arguments:</p>
<dl COMPACT>
<dd><code>-f </code><i>file</i> Specifies the phar <i>file</i> to work on.</dl>
<p> Optional arguments:</p>
<dl COMPACT>
<dd><code>-e </code><i>entry</i> Name of <i>entry</i> to work on (must include PHAR internal directory name if any).</p>
<dd><code>-k </code><i>index</i> Subscription <i>index</i> to work on. </p>
</dl>
<h2>meta-get command</h2>
<p>Get meta information of a PHAR entry or a PHAR package in serialized from. If no output file is specified for meta data then stdout is being used. You can also specify a particular index using -k. In that case the metadata is expected to be an array and the value of the given index is returned using echo rather than using serialize. If that index does not exist or no meta data is present then the return value is 1. </p>
<p> Required arguments:</p>
<dl COMPACT>
<dd><code>-f </code><i>file</i> Specifies the phar <i>file</i> to work on.</dl>
<p> Optional arguments:</p>
<dl COMPACT>
<dd><code>-e </code><i>entry</i> Name of <i>entry</i> to work on (must include PHAR internal directory name if any).</p>
<dd><code>-k </code><i>index</i> Subscription <i>index</i> to work on. </p>
</dl>
<h2>meta-set command</h2>
<p>Set meta data of a PHAR entry or a PHAR package using serialized input. If no input file is specified for meta data then stdin is being used. You can also specify a particular index using -k. In that case the metadata is expected to be an array and the value of the given index is being set. If the metadata is not present or empty a new array will be created. If the metadata is present and a flat value then the return value is 1. Also using -k the input is been taken directly rather then being serialized. </p>
<p> Required arguments:</p>
<dl COMPACT>
<dd><code>-f </code><i>file</i> Specifies the phar <i>file</i> to work on.</p>
<dd><code>-m </code><i>meta</i> Meta data to store with entry (serialized php data).</dl>
<p> Optional arguments:</p>
<dl COMPACT>
<dd><code>-e </code><i>entry</i> Name of <i>entry</i> to work on (must include PHAR internal directory name if any).</p>
<dd><code>-k </code><i>index</i> Subscription <i>index</i> to work on. </p>
</dl>
<h2>pack command</h2>
<p>Pack files into a PHAR archive. </p>
<p> When using -s &lt;stub&gt;, then the stub file is being excluded from the list of input files/dirs.To create an archive that contains PEAR class PHP_Archive then point -p argument to PHP/Archive.php. </p>
<p> Required arguments:</p>
<dl COMPACT>
<dd><code>-f </code><i>file</i> Specifies the phar <i>file</i> to work on.</p>
<dd><code>&#8230;</code> Any number of input files and directories. If -i is in use then ONLY files and matching the given regular expression are being packed. If -x is given then files matching that regular expression are NOT being packed.</dl>
<p> Optional arguments:</p>
<dl COMPACT>
<dd><code>-a </code><i>alias</i> Provide an <i>alias</i> name for the phar file.</p>
<dd><code>-b </code><i>bang</i> Hash-bang line to start the archive (e.g. #!/usr/bin/php). The hash mark itself &#8216;#!&#8217; and the newline character are optional.</p>
<dd><code>-c </code><i>algo</i> Compression algorithm (see <font SIZE="-1"><code>COMPRESSION</code> </font> )</p>
<dd><code>-h </code><i>hash</i> Selects the <i>hash</i> algorithm (see <font SIZE="-1"><code>HASH</code> </font> )</p>
<dd><code>-i </code><i>regex</i> Specifies a regular expression for input files.</p>
<dd><code>-l </code><i>level</i> Number of preceding subdirectories to strip from file entries</p>
<dd><code>-p </code><i>loader</i> Location of PHP_Archive class file (pear list-files PHP_Archive).You can use &#8216;0&#8217; or &#8216;1&#8217; to locate it automatically using the mentioned pear command. When using &#8216;0&#8217; the command does not error out when the class file cannot be located. This switch also adds some code around the stub so that class PHP_Archive gets registered as phar:// stream wrapper if necessary. And finally this switch will add the file phar.inc from this package and load it to ensure class Phar is present.</p>
<dd><code>-s </code><i>stub</i> Select the <i>stub</i> file.</p>
<dd><code>-x </code><i>regex</i> Regular expression for input files to exclude.</p>
<dd><code>-y </code><i>key</i> Private <i>key</i> for OpenSSL signing. </p>
</dl>
<h2>sign command</h2>
<p>Set signature hash algorithm. </p>
<p> Required arguments:</p>
<dl COMPACT>
<dd><code>-f </code><i>file</i> Specifies the phar <i>file</i> to work on.</p>
<dd><code>-h </code><i>hash</i> Selects the <i>hash</i> algorithm (see <font SIZE="-1"><code>HASH</code> </font> )</dl>
<p> Optional arguments:</p>
<dl COMPACT>
<dd><code>-y </code><i>key</i> Private <i>key</i> for OpenSSL signing. </p>
</dl>
<h2>stub-get command</h2>
<p>Get the stub of a PHAR file. If no output file is specified as stub then stdout is being used. </p>
<p> Required arguments:</p>
<dl COMPACT>
<dd><code>-f </code><i>file</i> Specifies the phar <i>file</i> to work on.</dl>
<p> Optional arguments:</p>
<dl COMPACT>
<dd><code>-s </code><i>stub</i> Select the <i>stub</i> file. </p>
</dl>
<h2>stub-set command</h2>
<p>Set the stub of a PHAR file. If no input file is specified as stub then stdin is being used. </p>
<p> Required arguments:</p>
<dl COMPACT>
<dd><code>-f </code><i>file</i> Specifies the phar <i>file</i> to work on.</dl>
<p> Optional arguments:</p>
<dl COMPACT>
<dd><code>-b </code><i>bang</i> Hash-bang line to start the archive (e.g. #!/usr/bin/php). The hash mark itself &#8216;#!&#8217; and the newline character are optional.</p>
<dd><code>-p </code><i>loader</i> Location of PHP_Archive class file (pear list-files PHP_Archive).You can use &#8216;0&#8217; or &#8216;1&#8217; to locate it automatically using the mentioned pear command. When using &#8216;0&#8217; the command does not error out when the class file cannot be located. This switch also adds some code around the stub so that class PHP_Archive gets registered as phar:// stream wrapper if necessary. And finally this switch will add the file phar.inc from this package and load it to ensure class Phar is present.</p>
<dd><code>-s </code><i>stub</i> Select the <i>stub</i> file. </p>
</dl>
<h2>tree command</h2>
<p>Get a directory tree for a PHAR archive. </p>
<p> Required arguments:</p>
<dl COMPACT>
<dd><code>-f </code><i>file</i> Specifies the phar <i>file</i> to work on.</dl>
<p> Optional arguments:</p>
<dl COMPACT>
<dd><code>-i </code><i>regex</i> Specifies a regular expression for input files.</p>
<dd><code>-x </code><i>regex</i> Regular expression for input files to exclude. </p>
</dl>
<h2>version command</h2>
<p>Get information about the PHAR environment and the tool version. </p>
<h2>Compression</h2>
<p>Algorithms:</p>
<dl COMPACT>
<dd><code>0</code> No compression</p>
<dd><code>none</code> No compression</p>
<dd><code>auto</code> Automatically select compression algorithm</p>
<dd><code>gz</code> GZip compression</p>
<dd><code>gzip</code> GZip compression</p>
<dd><code>bz2</code> BZip2 compression</p>
<dd><code>bzip2</code> BZip2 compression </p>
</dl>
<h2>Hash</h2>
<p>Algorithms:</p>
<dl COMPACT>
<dd>
<dd><code>md5</code> MD5</p>
<dd><code>sha1</code> SHA1</p>
<dd><code>sha256</code> SHA256</p>
<dd><code>sha512</code> SHA512</p>
<dd><code>openssl</code> OpenSSL </p>
</dl>
<h2>See Also</h2>
<p>For a more or less complete description of PHAR look here: </p>
<p> <code><a rel="nofollow" href="http://php.net/phar">http://php.net/phar</a></code> </p>
<h2>Bugs</h2>
<p>You can view the list of known bugs or report any new bug you found at: </p>
<p> <code><a rel="nofollow" href="http://bugs.php.net">http://bugs.php.net</a></code></p>
<h2>Authors</h2>
<p>The PHP Group: Thies C. Arntzen, Stig Bakken, Andi Gutmans, Rasmus Lerdorf, Sam Ruby, Sascha Schumann, Zeev Suraski, Jim Winstead, Andrei Zmievski. </p>
<p> Work for the PHP archive was done by Gregory Beaver, Marcus Boerger. </p>
<p> A List of active developers can be found here: </p>
<p> <code><a rel="nofollow" href="http://www.php.net/credits.php">http://www.php.net/credits.php</a></code> </p>
<p> And last but not least PHP was developed with the help of a huge amount of contributors all around the world.</p>
<h2>Version Information</h2>
<p>This manpage describes <code>phar</code>, version 7.2.24-0ubuntu0.18.04.6.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 1997-2018 The PHP Group </p>
<p> This source file is subject to version 3.01 of the PHP license, that is bundled with this package in the file LICENSE, and is available through the world-wide-web at the following url: </p>
<p> <code><a rel="nofollow" href="http://www.php.net/license/3_01.txt">http://www.php.net/license/3_01.txt</a></code> </p>
<p> If you did not receive a copy of the PHP license and are unable to obtain it through the world-wide-web, please send a note to <code>license [at] php.net</code> so we can mail you a copy immediately.</p>
