---
title: "phar-default(1)"
name: "phar-default"
section: "1"
letter: "p"
url: "/docs/linux/man/1-phar-default/"
description: "phar, phar.phar – PHAR (PHP archive) command line tool"
---

<p>phar, phar.phar &#8211; PHAR (PHP archive) command line tool </p>
<h2>Synopsis</h2>
<p> <code>phar</code> &lt;command&gt; [options] &#8230; </p>
<h2>Description</h2>
<p> The <code>PHAR</code> file format provides a way to put entire PHP applications into a single file called a &quot;phar&quot; (PHP Archive) for easy distribution and installation. </p>
<p> With the <code>phar</code> command you can create, update or extract PHP archives. </p>
<p> Commands: add compress delete extract help help-list info list meta-del meta-get meta-set pack sign stub-get stub-set tree version </p>
<h2>add command</h2>
<p> Add entries to a PHAR package. </p>
<p> Required arguments:</p>
<dl COMPACT>
<dt><code>-f </code><i>file</i></dt>
<dd> Specifies the phar <i>file</i> to work on.</dd>
<dt><code>&#8230;</code></dt>
<dd> Any number of input files and directories. If -i is in use then ONLY files and matching the given regular expression are being packed. If -x is given then files matching that regular expression are NOT being packed.</dd></dl>
<p> Optional arguments:</p>
<dl COMPACT>
<dt><code>-a </code><i>alias</i></dt>
<dd> Provide an <i>alias</i> name for the phar file.</dd>
<dt><code>-c </code><i>algo</i></dt>
<dd> Compression algorithm (see <code>COMPRESSION</code>  )</dd>
<dt><code>-i </code><i>regex</i></dt>
<dd> Specifies a regular expression for input files.</dd>
<dt><code>-l </code><i>level</i></dt>
<dd> Number of preceding subdirectories to strip from file entries</dd>
<dt><code>-x </code><i>regex</i></dt>
<dd> Regular expression for input files to exclude. </dd>
</dl>
<h2>compress command</h2>
<p> Compress or uncompress all files or a selected entry. </p>
<p> Required arguments:</p>
<dl COMPACT>
<dt><code>-c </code><i>algo</i></dt>
<dd> Compression algorithm (see <code>COMPRESSION</code>  )</dd>
<dt><code>-f </code><i>file</i></dt>
<dd> Specifies the phar <i>file</i> to work on.</dd></dl>
<p> Optional arguments:</p>
<dl COMPACT>
<dt><code>-e </code><i>entry</i></dt>
<dd> Name of <i>entry</i> to work on (must include PHAR internal directory name if any). </dd>
</dl>
<h2>delete command</h2>
<p> Delete entry from a PHAR archive </p>
<p> Required arguments:</p>
<dl COMPACT>
<dt><code>-e </code><i>entry</i></dt>
<dd> Name of <i>entry</i> to work on (must include PHAR internal directory name if any).</dd>
<dt><code>-f </code><i>file</i></dt>
<dd> Specifies the phar <i>file</i> to work on. </dd>
</dl>
<h2>extract command</h2>
<p> Extract a PHAR package to a directory. </p>
<p> Required arguments:</p>
<dl COMPACT>
<dt><code>-f </code><i>file</i></dt>
<dd> Specifies the phar <i>file</i> to work on.</dd></dl>
<p> Optional arguments:</p>
<dl COMPACT>
<dt><code>-i </code><i>regex</i></dt>
<dd> Specifies a regular expression for input files.</dd>
<dt><code>-x </code><i>regex</i></dt>
<dd> Regular expression for input files to exclude.</dd>
<dt><code>&#8230;</code></dt>
<dd> Directory to extract to (defaults to &#8216;.&#8217;). </dd>
</dl>
<h2>help command</h2>
<p> This help or help for a selected command. </p>
<p> Optional arguments:</p>
<dl COMPACT>
<dt><code>&#8230;</code></dt>
<dd> Optional command to retrieve help for. </dd>
</dl>
<h2>help-list command</h2>
<p> Lists available commands. </p>
<h2>info command</h2>
<p> Get information about a PHAR package. </p>
<p> By using -k it is possible to return a single value. </p>
<p> Required arguments:</p>
<dl COMPACT>
<dt><code>-f </code><i>file</i></dt>
<dd> Specifies the phar <i>file</i> to work on.</dd></dl>
<p> Optional arguments:</p>
<dl COMPACT>
<dt><code>-k </code><i>index</i></dt>
<dd> Subscription <i>index</i> to work on. </dd>
</dl>
<h2>list command</h2>
<p> List contents of a PHAR archive. </p>
<p> Required arguments:</p>
<dl COMPACT>
<dt><code>-f </code><i>file</i></dt>
<dd> Specifies the phar <i>file</i> to work on.</dd></dl>
<p> Optional arguments:</p>
<dl COMPACT>
<dt><code>-i </code><i>regex</i></dt>
<dd> Specifies a regular expression for input files.</dd>
<dt><code>-x </code><i>regex</i></dt>
<dd> Regular expression for input files to exclude. </dd>
</dl>
<h2>meta-del command</h2>
<p> Delete meta information of a PHAR entry or a PHAR package. </p>
<p> If -k is given then the metadata is expected to be an array and the given index is being deleted. </p>
<p> If something was deleted the return value is 0 otherwise it is 1. </p>
<p> Required arguments:</p>
<dl COMPACT>
<dt><code>-f </code><i>file</i></dt>
<dd> Specifies the phar <i>file</i> to work on.</dd></dl>
<p> Optional arguments:</p>
<dl COMPACT>
<dt><code>-e </code><i>entry</i></dt>
<dd> Name of <i>entry</i> to work on (must include PHAR internal directory name if any).</dd>
<dt><code>-k </code><i>index</i></dt>
<dd> Subscription <i>index</i> to work on. </dd>
</dl>
<h2>meta-get command</h2>
<p> Get meta information of a PHAR entry or a PHAR package in serialized from. If no output file is specified for meta data then stdout is being used. You can also specify a particular index using -k. In that case the metadata is expected to be an array and the value of the given index is returned using echo rather than using serialize. If that index does not exist or no meta data is present then the return value is 1. </p>
<p> Required arguments:</p>
<dl COMPACT>
<dt><code>-f </code><i>file</i></dt>
<dd> Specifies the phar <i>file</i> to work on.</dd></dl>
<p> Optional arguments:</p>
<dl COMPACT>
<dt><code>-e </code><i>entry</i></dt>
<dd> Name of <i>entry</i> to work on (must include PHAR internal directory name if any).</dd>
<dt><code>-k </code><i>index</i></dt>
<dd> Subscription <i>index</i> to work on. </dd>
</dl>
<h2>meta-set command</h2>
<p> Set meta data of a PHAR entry or a PHAR package using serialized input. If no input file is specified for meta data then stdin is being used. You can also specify a particular index using -k. In that case the metadata is expected to be an array and the value of the given index is being set. If the metadata is not present or empty a new array will be created. If the metadata is present and a flat value then the return value is 1. Also using -k the input is been taken directly rather then being serialized. </p>
<p> Required arguments:</p>
<dl COMPACT>
<dt><code>-f </code><i>file</i></dt>
<dd> Specifies the phar <i>file</i> to work on.</dd>
<dt><code>-m </code><i>meta</i></dt>
<dd> Meta data to store with entry (serialized php data).</dd></dl>
<p> Optional arguments:</p>
<dl COMPACT>
<dt><code>-e </code><i>entry</i></dt>
<dd> Name of <i>entry</i> to work on (must include PHAR internal directory name if any).</dd>
<dt><code>-k </code><i>index</i></dt>
<dd> Subscription <i>index</i> to work on. </dd>
</dl>
<h2>pack command</h2>
<p> Pack files into a PHAR archive. </p>
<p> When using -s &lt;stub&gt;, then the stub file is being excluded from the list of input files/dirs.To create an archive that contains PEAR class PHP_Archive then point -p argument to PHP/Archive.php. </p>
<p> Required arguments:</p>
<dl COMPACT>
<dt><code>-f </code><i>file</i></dt>
<dd> Specifies the phar <i>file</i> to work on.</dd>
<dt><code>&#8230;</code></dt>
<dd> Any number of input files and directories. If -i is in use then ONLY files and matching the given regular expression are being packed. If -x is given then files matching that regular expression are NOT being packed.</dd></dl>
<p> Optional arguments:</p>
<dl COMPACT>
<dt><code>-a </code><i>alias</i></dt>
<dd> Provide an <i>alias</i> name for the phar file.</dd>
<dt><code>-b </code><i>bang</i></dt>
<dd> Hash-bang line to start the archive (e.g. #!/usr/bin/php). The hash mark itself &#8216;#!&#8217; and the newline character are optional.</dd>
<dt><code>-c </code><i>algo</i></dt>
<dd> Compression algorithm (see <code>COMPRESSION</code>  )</dd>
<dt><code>-h </code><i>hash</i></dt>
<dd> Selects the <i>hash</i> algorithm (see <code>HASH</code>  )</dd>
<dt><code>-i </code><i>regex</i></dt>
<dd> Specifies a regular expression for input files.</dd>
<dt><code>-l </code><i>level</i></dt>
<dd> Number of preceding subdirectories to strip from file entries</dd>
<dt><code>-p </code><i>loader</i></dt>
<dd> Location of PHP_Archive class file (pear list-files PHP_Archive).You can use &#8216;0&#8217; or &#8216;1&#8217; to locate it automatically using the mentioned pear command. When using &#8216;0&#8217; the command does not error out when the class file cannot be located. This switch also adds some code around the stub so that class PHP_Archive gets registered as phar:// stream wrapper if necessary. And finally this switch will add the file phar.inc from this package and load it to ensure class Phar is present.</dd>
<dt><code>-s </code><i>stub</i></dt>
<dd> Select the <i>stub</i> file.</dd>
<dt><code>-x </code><i>regex</i></dt>
<dd> Regular expression for input files to exclude.</dd>
<dt><code>-y </code><i>key</i></dt>
<dd> Private <i>key</i> for OpenSSL signing. </dd>
</dl>
<h2>sign command</h2>
<p> Set signature hash algorithm. </p>
<p> Required arguments:</p>
<dl COMPACT>
<dt><code>-f </code><i>file</i></dt>
<dd> Specifies the phar <i>file</i> to work on.</dd>
<dt><code>-h </code><i>hash</i></dt>
<dd> Selects the <i>hash</i> algorithm (see <code>HASH</code>  )</dd></dl>
<p> Optional arguments:</p>
<dl COMPACT>
<dt><code>-y </code><i>key</i></dt>
<dd> Private <i>key</i> for OpenSSL signing. </dd>
</dl>
<h2>stub-get command</h2>
<p> Get the stub of a PHAR file. If no output file is specified as stub then stdout is being used. </p>
<p> Required arguments:</p>
<dl COMPACT>
<dt><code>-f </code><i>file</i></dt>
<dd> Specifies the phar <i>file</i> to work on.</dd></dl>
<p> Optional arguments:</p>
<dl COMPACT>
<dt><code>-s </code><i>stub</i></dt>
<dd> Select the <i>stub</i> file. </dd>
</dl>
<h2>stub-set command</h2>
<p> Set the stub of a PHAR file. If no input file is specified as stub then stdin is being used. </p>
<p> Required arguments:</p>
<dl COMPACT>
<dt><code>-f </code><i>file</i></dt>
<dd> Specifies the phar <i>file</i> to work on.</dd></dl>
<p> Optional arguments:</p>
<dl COMPACT>
<dt><code>-b </code><i>bang</i></dt>
<dd> Hash-bang line to start the archive (e.g. #!/usr/bin/php). The hash mark itself &#8216;#!&#8217; and the newline character are optional.</dd>
<dt><code>-p </code><i>loader</i></dt>
<dd> Location of PHP_Archive class file (pear list-files PHP_Archive).You can use &#8216;0&#8217; or &#8216;1&#8217; to locate it automatically using the mentioned pear command. When using &#8216;0&#8217; the command does not error out when the class file cannot be located. This switch also adds some code around the stub so that class PHP_Archive gets registered as phar:// stream wrapper if necessary. And finally this switch will add the file phar.inc from this package and load it to ensure class Phar is present.</dd>
<dt><code>-s </code><i>stub</i></dt>
<dd> Select the <i>stub</i> file. </dd>
</dl>
<h2>tree command</h2>
<p> Get a directory tree for a PHAR archive. </p>
<p> Required arguments:</p>
<dl COMPACT>
<dt><code>-f </code><i>file</i></dt>
<dd> Specifies the phar <i>file</i> to work on.</dd></dl>
<p> Optional arguments:</p>
<dl COMPACT>
<dt><code>-i </code><i>regex</i></dt>
<dd> Specifies a regular expression for input files.</dd>
<dt><code>-x </code><i>regex</i></dt>
<dd> Regular expression for input files to exclude. </dd>
</dl>
<h2>version command</h2>
<p> Get information about the PHAR environment and the tool version. </p>
<h2>Compression</h2>
<p> Algorithms:</p>
<dl COMPACT>
<dt><code>0</code></dt>
<dd> No compression</dd>
<dt><code>none</code></dt>
<dd> No compression</dd>
<dt><code>auto</code></dt>
<dd> Automatically select compression algorithm</dd>
<dt><code>gz</code></dt>
<dd> GZip compression</dd>
<dt><code>gzip</code></dt>
<dd> GZip compression</dd>
<dt><code>bz2</code></dt>
<dd> BZip2 compression</dd>
<dt><code>bzip2</code></dt>
<dd> BZip2 compression </dd>
</dl>
<h2>Hash</h2>
<p> Algorithms:</p>
<dl COMPACT>
<dt><code>md5</code></dt>
<dd> MD5</dd>
<dt><code>sha1</code></dt>
<dd> SHA1</dd>
<dt><code>sha256</code></dt>
<dd> SHA256</dd>
<dt><code>sha512</code></dt>
<dd> SHA512</dd>
<dt><code>openssl</code></dt>
<dd> OpenSSL using SHA-1</dd>
<dt><code>openssl_sha256</code></dt>
<dd> OpenSSL using SHA-256</dd>
<dt><code>openssl_sha512</code></dt>
<dd> OpenSSL using SHA-512 </dd>
</dl>
<h2>See Also</h2>
<p> For a more or less complete description of PHAR look here: </p>
<p> <code><a rel="nofollow" href="http://php.net/phar">http://php.net/phar</a></code> </p>
<h2>Bugs</h2>
<p> You can view the list of known bugs or report any new bug you found at: </p>
<p> <code><a rel="nofollow" href="http://bugs.php.net">http://bugs.php.net</a></code></p>
<h2>Authors</h2>
<p> The PHP Group: Thies C. Arntzen, Stig Bakken, Andi Gutmans, Rasmus Lerdorf, Sam Ruby, Sascha Schumann, Zeev Suraski, Jim Winstead, Andrei Zmievski. </p>
<p> Work for the PHP archive was done by Gregory Beaver, Marcus Boerger. </p>
<p> A List of active developers can be found here: </p>
<p> <code><a rel="nofollow" href="http://www.php.net/credits.php">http://www.php.net/credits.php</a></code> </p>
<p> And last but not least PHP was developed with the help of a huge amount of contributors all around the world.</p>
<h2>Version Information</h2>
<p> This manpage describes <code>phar</code>, version 8.1.2-1ubuntu2.11.</p>
<h2>Copyright</h2>
<p> Copyright &#169; The PHP Group </p>
<p> This source file is subject to version 3.01 of the PHP license, that is bundled with this package in the file LICENSE, and is available through the world-wide-web at the following url: </p>
<p> <code><a rel="nofollow" href="https://www.php.net/license/3_01.txt">https://www.php.net/license/3_01.txt</a></code> </p>
<p> If you did not receive a copy of the PHP license and are unable to obtain it through the world-wide-web, please send a note to <code>license [at] php.net</code> so we can mail you a copy immediately.</p>
