---
title: "mkvpropedit(1)"
name: "mkvpropedit"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mkvpropedit/"
description: "mkvpropedit – Modify properties of existing Matroska(TM) files without a complete remux"
---
<h2 class="name">NAME</h2>
<p> mkvpropedit - Modify properties of existing Matroska(TM) files without a complete remux </p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>mkvpropedit</code> [options] {source-filename} {actions} </dt>
</dl>
<h2>DESCRIPTION</h2>
<dd> <p> This program analyses an existing Matroska(TM) file and modifies some of its properties. Then it writes those modifications to the existing file. Among the properties that can be changed are the segment information elements (e.g. the title) and the track headers (e.g. the language code, &#8216;default track&#8217; flag or the name). </p>
<p> Options: </p>
<p> <code>-l</code>, <code>--list-property-names</code> </p>
 </dd>
<dl>
<dd> <p> Lists all known and editable property names, their type (string, integer, boolean etc) and a short description. The program exits afterwards. Therefore the <i>source-filename</i> parameter does not have to be supplied. </p>
 </dd></dl>
<p> <code>-p</code>, <code>--parse-mode</code> <i>mode</i> </p>
<dl>
<dd> <p> Sets the parse mode. The parameter &#8216;<i>mode</i>&#8216; can either be &#8216;fast&#8217; (which is also the default) or &#8216;full&#8217;. The &#8216;fast&#8217; mode does not parse the whole file but uses the meta seek elements for locating the required elements of a source file. In 99% of all cases this is enough. But for files that do not contain meta seek elements or which are damaged the user might have to set the &#8216;full&#8217; parse mode. A full scan of a file can take a couple of minutes while a fast scan only takes seconds. </p>
 </dd></dl>
<p> Actions that deal with track and segment info properties: </p>
<p> <code>-e</code>, <code>--edit</code> <i>selector</i> </p>
<dl>
<dd> <p> Sets the Matroska(TM) file section (segment information or a certain track&#8217;s headers) that all following add, set and delete actions operate on. This option can be used multiple times in order to make modifications to more than one element. </p>
<p> By default <code><a href="/docs/linux/man/1-mkvpropedit/">mkvpropedit</a></code>(1) will edit the segment information section. </p>
<p> See the section about edit selectors for a full description of the syntax. </p>
 </dd></dl>
<p> <code>-a</code>, <code>--add</code> <i>name</i>=<i>value</i> </p>
<dl>
<dd> <p> Adds a property <i>name</i> with the value <i>value</i>. The property will be added even if such a property exists already. Note that most properties are unique and cannot occur more than once. </p>
 </dd></dl>
<p> <code>-s</code>, <code>--set</code> <i>name</i>=<i>value</i> </p>
<dl>
<dd> <p> Sets all occurrences of the property <i>name</i> to the value <i>value</i>. If no such property exists then it will be added. </p>
 </dd></dl>
<p> <code>-d</code>, <code>--delete</code> <i>name</i> </p>
<dl>
<dd> <p> Deletes all occurrences of the property <i>name</i>. Note that some properties are required and cannot be deleted. </p>
 </dd></dl>
<p> Actions that deal with tags and chapters: </p>
<p> <code>-t</code>, <code>--tags</code> <i>selector</i>:<i>filename</i> </p>
<dl>
<dd> <p> Add or replace tags in the file with the ones from filename or remove them if filename is empty. <code><a href="/docs/linux/man/1-mkvpropedit/">mkvpropedit</a></code>(1) reads the same XML tag format that <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) reads as well. </p>
<p> The <i>selector</i> must be one of the words <code>all</code>, <code>global</code> or <code>track</code>. For <code>all</code><code><a href="/docs/linux/man/1-mkvpropedit/">mkvpropedit</a></code>(1) will replace or remove all tags in a file. With <code>global</code> only global tags will be replaced or removed. </p>
<p> With <code>track</code><code><a href="/docs/linux/man/1-mkvpropedit/">mkvpropedit</a></code>(1) will replace tags for a specific track. Additionally the tags read from filename will be assigned to the same track. The track is specified in the same way edit selectors are specified (see below), e.g. --tags track:a1:new-audio-tags.xml. </p>
 </dd></dl>
<p> <code>-c</code>, <code>--chapters</code> <i>filename</i> </p>
<dl>
<dd> <p> Add or replace chapters in the file with the ones from filename or remove them if filename is empty. <code><a href="/docs/linux/man/1-mkvpropedit/">mkvpropedit</a></code>(1) reads the same XML and simple chapter formats that <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) reads as well. </p>
 </dd></dl>
<p> Actions for handling attachments: </p>
<p> <code>--add-attachment</code> <i>filename</i> </p>
<dl>
<dd> <p> Adds a new attachment from <i>filename</i>. </p>
<p> If the option <code>--attachment-name</code> has been used prior to this option then its value is used as the new attachment&#8217;s name. Otherwise it is derived from <i>filename</i>. </p>
<p> If the option <code>--attachment-mime-type</code> has been used prior to this option then its value is used as the new attachment&#8217;s MIME type. Otherwise it is auto-detected from the content of <i>filename</i>. </p>
<p> If the option <code>--attachment-description</code> has been used prior to this option then its value is used as the new attachment&#8217;s description. Otherwise no description will be set. </p>
 </dd></dl>
<p> <code>--replace-attachment</code> <i>selector</i>:<i>filename</i> </p>
<dl>
<dd> <p> Replaces one or more attachments that match <i>selector</i> with the file <i>filename</i>. If more than one existing attachment matches <i>selector</i> then all of their contents will be replaced by the content of <i>filename</i>. </p>
<p> The <i>selector</i> can have one of four forms. They&#8217;re exlained below in the section attachment selectors. </p>
<p> If the option <code>--attachment-name</code> has been used prior to this option then its value is used as the replaced attachment&#8217;s name. Otherwise the name is not changed. </p>
<p> If the option <code>--attachment-mime-type</code> has been used prior to this option then its value is used as the replaced attachment&#8217;s MIME type. Otherwise the MIME type is not changed. </p>
<p> If the option <code>--attachment-description</code> has been used prior to this option then its value is used as the replaced attachment&#8217;s description. Otherwise no description is not changed. </p>
 </dd></dl>
<p> <code>--delete-attachment</code> <i>selector</i> </p>
<dl>
<dd> <p> Deletes one or more attachments that match <i>selector</i>. </p>
<p> The <i>selector</i> can have one of four forms. They&#8217;re exlained below in the section attachment selectors. </p>
 </dd></dl>
<p> Options for attachment actions: </p>
<p> <code>--attachment-name</code> <i>name</i> </p>
<dl>
<dd> <p> Sets the name to use for the following <code>--add-attachment</code> or <code>--replace-attachment</code> operation. </p>
 </dd></dl>
<p> <code>--attachment-mime-type</code> <i>mime-type</i> </p>
<dl>
<dd> <p> Sets the MIME type to use for the following <code>--add-attachment</code> or <code>--replace-attachment</code> operation. </p>
 </dd></dl>
<p> <code>--attachment-description</code> <i>description</i> </p>
<dl>
<dd> <p> Sets the description to use for the following <code>--add-attachment</code> or <code>--replace-attachment</code> operation. </p>
 </dd></dl>
<p> Other options: </p>
<p> <code>--command-line-charset</code> <i>character-set</i> </p>
<dl>
<dd> <p> Sets the character set to convert strings given on the command line from. It defaults to the character set given by system&#8217;s current locale. </p>
 </dd></dl>
<p> <code>--output-charset</code> <i>character-set</i> </p>
<dl>
<dd> <p> Sets the character set to which strings are converted that are to be output. It defaults to the character set given by system&#8217;s current locale. </p>
 </dd></dl>
<p> <code>-r</code>, <code>--redirect-output</code> <i>file-name</i> </p>
<dl>
<dd> <p> Writes all messages to the file <i>file-name</i> instead of to the console. While this can be done easily with output redirection there are cases in which this option is needed: when the terminal reinterprets the output before writing it to a file. The character set set with <code>--output-charset</code> is honored. </p>
 </dd></dl>
<p> <code>--ui-language</code> <i>code</i> </p>
<dl>
<dd> <p> Forces the translations for the language <i>code</i> to be used (e.g. &#8216;de_DE&#8217; for the German translations). It is preferable to use the environment variables <i>LANG</i>, <i>LC_MESSAGES</i> and <i>LC_ALL</i> though. Entering &#8216;list&#8217; as the <i>code</i> will cause <code><a href="/docs/linux/man/1-mkvextract/">mkvextract</a></code>(1) to output a list of available translations. </p>
 </dd></dl>
<p> <code>--debug</code> <i>topic</i> </p>
<dl>
<dd> <p> Turn on debugging for a specific feature. This option is only useful for developers. </p>
 </dd></dl>
<p> <code>--engage</code> <i>feature</i> </p>
<dl>
<dd> <p> Turn on experimental features. A list of available features can be requested with <code>mkvpropedit --engage list</code>. These features are not meant to be used in normal situations. </p>
 </dd></dl>
<p> <code>--gui-mode</code> </p>
<dl>
<dd> <p> Turns on GUI mode. In this mode specially-formatted lines may be output that can tell a controlling GUI what&#8217;s happening. These messages follow the format &#8216;#GUI#message&#8217;. The message may be followed by key/value pairs as in &#8216;#GUI#message#key1=value1#key2=value2...&#8216;. Neither the messages nor the keys are ever translated and always output in English. </p>
 </dd></dl>
<p> <code>-v</code>, <code>--verbose</code> </p>
<dl>
<dd> <p> Be verbose and show all the important Matroska(TM) elements as they&#8217;re read. </p>
 </dd></dl>
<p> <code>-h</code>, <code>--help</code> </p>
<dl>
<dd> <p> Show usage information and exit. </p>
 </dd></dl>
<p> <code>-V</code>, <code>--version</code> </p>
<dl>
<dd> <p> Show version information and exit. </p>
 </dd></dl>
<p> <code>--check-for-updates</code> </p>
<dl>
<dd> <p> Checks online for new releases by downloading the URL m[blue]<code><a rel="nofollow" href="http://mkvtoolnix-releases.bunkus.org/latest-release.xml">http://mkvtoolnix-releases.bunkus.org/latest-release.xml</a></code>m[]. Four lines will be output in key=value style: the URL from where the information was retrieved (key version_check_url), the currently running version (key running_version), the latest release&#8217;s version (key available_version) and the download URL (key download_url). </p>
<p> Afterwards the program exists with an exit code of 0 if no newer release is available, with 1 if a newer release is available and with 2 if an error occured (e.g. if the update information could not be retrieved). </p>
<p> This option is only available if the program was built with support for libcurl. </p>
 </dd></dl>
<p> <code>@</code><i>options-file</i> </p>
<dl>
<dd> <p> Reads additional command line arguments from the file <i>options-file</i>. Lines whose first non-whitespace character is a hash mark (&#8216;#&#8216;) are treated as comments and ignored. White spaces at the start and end of a line will be stripped. Each line must contain exactly one option. </p>
<p> Several chars can be escaped, e.g. if you need to start a non-comment line with &#8216;#&#8216;. The rules are described in the section about escaping text. </p>
<p> The command line &#8216;<code>mkvpropedit source.mkv --edit track:a2 --set name=Comments</code>&#8216; could be converted into the following option file: </p>
 </dd>
<dl>
<dd> <pre><code># Modify source.mkv
source.mkv
# Edit the second audio track
--edit
track:a2
# and set the title to 'Comments'
--set
name=Comments
</code></pre>
 </dd></dl>
</dl>
<h2>EDIT SELECTORS</h2>
<p> The <code>--edit</code> option sets the Matroska(TM) file section (segment information or a certain track&#8217;s headers) that all following add, set and delete actions operate on. This stays valid until the next <code>--edit</code> option is found. The argument to this option is called the edit selector. </p>
<p> By default <code><a href="/docs/linux/man/1-mkvpropedit/">mkvpropedit</a></code>(1) will edit the segment information section.  </p>
<h3>Segment information</h3>
<p> The segment information can be selected with one of these three words: &#8216;info&#8217;, &#8216;segment_info&#8217; or &#8216;segmentinfo&#8217;. It contains properties like the segment title or the segment UID.  </p>
<h3>Track headers</h3>
<p> Track headers can be selected with a slightly more complex selector. All variations start with &#8216;track:&#8216;. The track header properties include elements like the language code, &#8216;default track&#8217; flag or the track&#8217;s name. </p>
<p> <code>track:</code><i>n</i> </p>
<dl>
<dd> <p> If the parameter <i>n</i> is a number then the <i>n</i>th track will be selected. The track order is the same that <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1)&#8216;s <code>--identify</code> option outputs. </p>
<p> Numbering starts at 1. </p>
 </dd></dl>
<p> <code>track:</code><i>t</i><i>n</i> </p>
<dl>
<dd> <p> If the parameter starts with a single character <i>t</i> followed by a <i>n</i> then the <i>n</i>th track of a specific track type will be selected. The track type parameter <i>t</i> must be one of these four characters: &#8216;a&#8217; for an audio track, &#8216;b&#8217; for a button track, &#8216;s&#8217; for a subtitle track and &#8216;v&#8217; for a video track. The track order is the same that <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1)&#8216;s <code>--identify</code> option outputs. </p>
<p> Numbering starts at 1. </p>
 </dd></dl>
<p> <code>track:</code>=<i>uid</i> </p>
<dl>
<dd> <p> If the parameter starts with a &#8216;=&#8216; followed by a number <i>uid</i> then the track whose track UID element equals this <i>uid</i>. Track UIDs can be obtained with <code><a href="/docs/linux/man/1-mkvinfo/">mkvinfo</a></code>(1). </p>
 </dd></dl>
<p> <code>track:</code>@<i>number</i> </p>
<dl>
<dd> <p> If the parameter starts with a &#8216;@&#8216; followed by a number <i>number</i> then the track whose track number element equals this <i>number</i>. Track number can be obtained with <code><a href="/docs/linux/man/1-mkvinfo/">mkvinfo</a></code>(1). </p>
 </dd></dl>
<h3>Notes</h3>
<p> Due to the nature of the track edit selectors it is possible that several selectors actually match the same track headers. In such cases all actions for those edit selectors will be combined and executed in the order in which they&#8217;re given on the command line.  </p>
<h2>ATTACHMENT SELECTORS</h2>
<p> An attachment selector is used with the two actions <code>--replace-attachment</code> and <code>--delete-attachment</code>. It can have one of the following four forms: </p>
<dl>
<dd> <p> 1. Selection by attachment ID. In this form the selector is simply a number, the attachment&#8217;s ID as output by <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1)&#8216;s identification command. </p>
 </dd></dl>
<dl>
<dd> <p> 2. Selection by attachment UID (unique ID). In this form the selector is the equal sign = followed by a number, the attachment&#8217;s unique ID as output by <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1)&#8216;s verbose identification command. </p>
 </dd></dl>
<dl>
<dd> <p> 3. Selection by attachment name. In this form the selector is the literal word name: followed by the existing attachment&#8217;s name. If this selector is used with <code>--replace-attachment</code> then colons within the name to match must be escaped as \c. </p>
 </dd></dl>
<dl>
<dd> <p> 4. Selection by MIME type. In this form the selector is the literal word mime-type: followed by the existing attachment&#8217;s MIME type. If this selector is used with <code>--replace-attachment</code> then colons within the MIME type to match must be escaped as \c. </p>
 </dd></dl>
<h2>EXAMPLES</h2>
<p> The following example edits a file called &#8216;movie.mkv&#8217;. It sets the segment title and modifies the language code of an audio and a subtitle track. Note that this example can be shortened by leaving out the first <code>--edit</code> option because editing the segment information element is the default for all options found before the first <code>--edit</code> option anyway. </p>
<dl>
<dd> <pre><code>$ mkvpropedit movie.mkv --edit info --set &quot;title=The movie&quot; --edit track:a1 --set language=fre --edit track:a2 --set language=ita
</code></pre>
 </dd></dl>
<p> The second example removes the &#8216;default track flag&#8217; from the first subtitle track and sets it for the second one. Note that <code><a href="/docs/linux/man/1-mkvpropedit/">mkvpropedit</a></code>(1), unlike <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1), does not set the &#8216;default track flag&#8217; of other tracks to &#8216;0&#8217; if it is set to &#8216;1&#8217; for a different track automatically. </p>
<dl>
<dd> <pre><code>$ mkvpropedit movie.mkv --edit track:s1 --set flag-default=0 --edit track:s2 --set flag-default=1
</code></pre>
 </dd></dl>
<p> Replacing the tags for the second subtitle track in a file looks like this: </p>
<dl>
<dd> <pre><code>$ mkvpropedit movie.mkv --tags track:s2:new-subtitle-tags.xml
</code></pre>
 </dd></dl>
<p> Removing all tags requires leaving out the file name: </p>
<dl>
<dd> <pre><code>$ mkvpropedit movie.mkv --tags all:
</code></pre>
 </dd></dl>
<p> Replacing the chapters in a file looks like this: </p>
<dl>
<dd> <pre><code>$ mkvpropedit movie.mkv --chapters new-chapters.xml
</code></pre>
 </dd></dl>
<p> Removing all chapters requires leaving out the file name: </p>
<dl>
<dd> <pre><code>$ mkvpropedit movie.mkv --chapters ''
</code></pre>
 </dd></dl>
<p> Adding a font file (Arial.ttf) as an attachment: </p>
<dl>
<dd> <pre><code>$ mkvpropedit movie.mkv --add-attachment Arial.ttf
</code></pre>
 </dd></dl>
<p> Adding a font file (89719823.ttf) as an attachment and providing some information as it really is just Arial: </p>
<dl>
<dd> <pre><code>$ mkvpropedit movie.mkv --attachment-name Arial.ttf --attachment-description 'The Arial font as a TrueType font' --attachment-mime-type application/x-truetype-font --add-attachment 89719823.ttf
</code></pre>
 </dd></dl>
<p> Replacing one attached font (Comit.ttf) file with another one (Arial.ttf): </p>
<dl>
<dd> <pre><code>$ mkvpropedit movie.mkv --attachment-name Arial.ttf --attachment-description 'The Arial font as a TrueType font' --replace-attachment name:Comic.ttf:Arial.ttf
</code></pre>
 </dd></dl>
<p> Deleting the second attached file, whatever it may be: </p>
<dl>
<dd> <pre><code>$ mkvpropedit movie.mkv --delete-attachment 2
</code></pre>
 </dd></dl>
<p> Deleting all attached fonts by MIME type: </p>
<dl>
<dd> <pre><code>$ mkvpropedit movie.mkv --delete-attachment mime-type:application/x-truetype-font
</code></pre>
 </dd></dl>
<h2>EXIT CODES</h2>
<p> <code><a href="/docs/linux/man/1-mkvpropedit/">mkvpropedit</a></code>(1) exits with one of three exit codes: </p>
<dl>
<dd> <p> &bull; <code>0</code> -- This exit codes means that the modification has completed successfully. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>1</code> -- In this case <code><a href="/docs/linux/man/1-mkvpropedit/">mkvpropedit</a></code>(1) has output at least one warning, but the modification did continue. A warning is prefixed with the text &#8216;Warning:&#8216;. Depending on the issues involved the resulting files might be ok or not. The user is urged to check both the warning and the resulting files. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; <code>2</code> -- This exit code is used after an error occurred. <code><a href="/docs/linux/man/1-mkvpropedit/">mkvpropedit</a></code>(1) aborts right after outputting the error message. Error messages range from wrong command line arguments over read/write errors to broken files. </p>
 </dd></dl>
<h2>TEXT FILES AND CHARACTER SET CONVERSIONS</h2>
<p> For an in-depth discussion about how all tools in the MKVToolNix suite handle character set conversions, input/output encoding, command line encoding and console encoding please see the identically-named section in the <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) man page.  </p>
<h2>ESCAPING SPECIAL CHARS IN TEXT</h2>
<p> There are a few places in which special characters in text must or should be escaped. The rules for escaping are simple: each character that needs escaping is replaced with a backslash followed by another character. </p>
<p> The rules are: &#8216; &#8216; (a space) becomes &#8216;\s&#8217;, &#8216;&quot;&#8216; (double quotes) becomes &#8216;\2&#8217;, &#8216;:&#8216; becomes &#8216;\c&#8217;, &#8216;#&#8216; becomes &#8216;\h&#8217; and &#8216;\&#8216; (a single backslash) itself becomes &#8216;\\&#8216;.  </p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> <code><a href="/docs/linux/man/1-mkvpropedit/">mkvpropedit</a></code>(1) uses the default variables that determine the system&#8217;s locale (e.g. <i>LANG</i> and the <i>LC_*</i> family). Additional variables: </p>
<p> <i>MKVTOOLNIX_DEBUG</i> and its short form <i>MTX_DEBUG</i> </p>
<dl>
<dd> <p> The content is treated as if it had been passed via the <code>--debug</code> option. </p>
 </dd></dl>
<p> <i>MKVTOOLNIX_ENGAGE</i> and its short form <i>MTX_ENGAGE</i> </p>
<dl>
<dd> <p> The content is treated as if it had been passed via the <code>--engage</code> option. </p>
 </dd></dl>
<p> <i>MKVTOOLNIX_OPTIONS</i> and its short form <i>MTX_OPTIONS</i> </p>
<dl>
<dd> <p> The content is split on white space. The resulting partial strings are treated as if it had been passed as command line options. If you need to pass special characters (e.g. spaces) then you have to escape them (see the section about escaping special characters in text). </p>
 </dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1), <code><a href="/docs/linux/man/1-mkvinfo/">mkvinfo</a></code>(1), <code><a href="/docs/linux/man/1-mkvextract/">mkvextract</a></code>(1), <code><a href="/docs/linux/man/1-mmg/">mmg</a></code>(1)  </p>
<h2>WWW</h2>
<p> The latest version can always be found at m[blue]<code>the MKVToolNix homepage</code>m[]<font SIZE="-2">[1]</font>.  </p>
<h2>AUTHOR</h2>
<p> <code>Moritz Bunkus</code> &lt;moritz [at] bunkus.org&gt; </p>
<dl>
<dd> <p> Developer </p>
 </dd></dl>
<h2>NOTES</h2>
<dl>
<dt> 1.</dt>
<dd> <p> the MKVToolNix homepage </p>
 </dd>
<dl>
<dd> <p> <a rel="nofollow" href="http://www.bunkus.org/videotools/mkvtoolnix/">http://www.bunkus.org/videotools/mkvtoolnix/</a> </p>
 </dd></dl>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNOPSIS</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">EDIT SELECTORS</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAF">Segment information</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">Track headers</a></dt>
<dd>  </dd>
<dt><a href="#lbAH">Notes</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAI">ATTACHMENT SELECTORS</a></dt>
<dd>  </dd>
<dt><a href="#lbAJ">EXAMPLES</a></dt>
<dd>  </dd>
<dt><a href="#lbAK">EXIT CODES</a></dt>
<dd>  </dd>
<dt><a href="#lbAL">TEXT FILES AND CHARACTER SET CONVERSIONS</a></dt>
<dd>  </dd>
<dt><a href="#lbAM">ESCAPING SPECIAL CHARS IN TEXT</a></dt>
<dd>  </dd>
<dt><a href="#lbAN">ENVIRONMENT VARIABLES</a></dt>
<dd>  </dd>
<dt><a href="#lbAO">SEE ALSO</a></dt>
<dd>  </dd>
<dt><a href="#lbAP">WWW</a></dt>
<dd>  </dd>
<dt><a href="#lbAQ">AUTHOR</a></dt>
<dd>  </dd>
<dt><a href="#lbAR">NOTES</a></dt>
<dd>  </dd></dl>
