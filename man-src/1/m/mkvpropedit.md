---
title: "mkvpropedit(1)"
name: "mkvpropedit"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mkvpropedit/"
description: "mkvpropedit – Modify properties of existing Matroska(TM) files without a complete remux"
---

<h2 class="name">NAME</h2>
<p> mkvpropedit &#8211; Modify properties of existing Matroska(TM) files without a complete remux </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mkvpropedit</code> [options] {source-filename} {actions}</dl>
<h2>DESCRIPTION</h2>
<dd>This program analyses an existing Matroska(TM) file and modifies some of its properties. Then it writes those modifications to the existing file. Among the properties that can be changed are the segment information elements (e.g. the title) and the track headers (e.g. the language code, &#8216;default track&#8217; flag or the name). </p>
<p> Options: </p>
<p> <code>-l</code>, <code>&#8211;list-property-names</code></p>
<dl>
<dt>
<dd> Lists all known and editable property names, their type (string, integer, boolean etc) and a short description. The program exits afterwards. Therefore the <i>source-filename</i> parameter does not have to be supplied.</dl>
<p> <code>-p</code>, <code>&#8211;parse-mode</code> <i>mode</i></p>
<dl>
<dt>
<dd> Sets the parse mode. The parameter &#8216;<i>mode</i>&#8216; can either be &#8216;fast&#8217; (which is also the default) or &#8216;full&#8217;. The &#8216;fast&#8217; mode does not parse the whole file but uses the meta seek elements for locating the required elements of a source file. In 99% of all cases this is enough. But for files that do not contain meta seek elements or which are damaged the user might have to set the &#8216;full&#8217; parse mode. A full scan of a file can take a couple of minutes while a fast scan only takes seconds.</dl>
<p> Actions that deal with track and segment info properties: </p>
<p> <code>-e</code>, <code>&#8211;edit</code> <i>selector</i></p>
<dl>
<dt>
<dd> Sets the Matroska(TM) file section (segment information or a certain track&#8217;s headers) that all following add, set and delete actions operate on. This option can be used multiple times in order to make modifications to more than one element. </p>
<p> By default <code><a href="/docs/linux/man/1-mkvpropedit/">mkvpropedit</a></code>(1) will edit the segment information section. </p>
<p> See the section about edit selectors for a full description of the syntax.</dl>
<p> <code>-a</code>, <code>&#8211;add</code> <i>name</i>=<i>value</i></p>
<dl>
<dt>
<dd> Adds a property <i>name</i> with the value <i>value</i>. The property will be added even if such a property exists already. Note that most properties are unique and cannot occur more than once.</dl>
<p> <code>-s</code>, <code>&#8211;set</code> <i>name</i>=<i>value</i></p>
<dl>
<dt>
<dd> Sets all occurrences of the property <i>name</i> to the value <i>value</i>. If no such property exists then it will be added.</dl>
<p> <code>-d</code>, <code>&#8211;delete</code> <i>name</i></p>
<dl>
<dt>
<dd> Deletes all occurrences of the property <i>name</i>. Note that some properties are required and cannot be deleted.</dl>
<p> Actions that deal with tags and chapters: </p>
<p> <code>-t</code>, <code>&#8211;tags</code> <i>selector</i>:<i>filename</i></p>
<dl>
<dt>
<dd> Add or replace tags in the file with the ones from filename or remove them if filename is empty. <code><a href="/docs/linux/man/1-mkvpropedit/">mkvpropedit</a></code>(1) reads the same XML tag format that <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) reads as well. </p>
<p> The <i>selector</i> must be one of the words <code>all</code>, <code>global</code> or <code>track</code>. For <code>all</code><code><a href="/docs/linux/man/1-mkvpropedit/">mkvpropedit</a></code>(1) will replace or remove all tags in a file. With <code>global</code> only global tags will be replaced or removed. </p>
<p> With <code>track</code><code><a href="/docs/linux/man/1-mkvpropedit/">mkvpropedit</a></code>(1) will replace tags for a specific track. Additionally the tags read from filename will be assigned to the same track. The track is specified in the same way edit selectors are specified (see below), e.g. &#8211;tags track:a1:new-audio-tags.xml.</dl>
<p> <code>-c</code>, <code>&#8211;chapters</code> <i>filename</i></p>
<dl>
<dt>
<dd> Add or replace chapters in the file with the ones from filename or remove them if filename is empty. <code><a href="/docs/linux/man/1-mkvpropedit/">mkvpropedit</a></code>(1) reads the same XML and simple chapter formats that <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) reads as well.</dl>
<p> Actions for handling attachments: </p>
<p> <code>&#8211;add-attachment</code> <i>filename</i></p>
<dl>
<dt>
<dd> Adds a new attachment from <i>filename</i>. </p>
<p> If the option <code>&#8211;attachment-name</code> has been used prior to this option then its value is used as the new attachment&#8217;s name. Otherwise it is derived from <i>filename</i>. </p>
<p> If the option <code>&#8211;attachment-mime-type</code> has been used prior to this option then its value is used as the new attachment&#8217;s MIME type. Otherwise it is auto-detected from the content of <i>filename</i>. </p>
<p> If the option <code>&#8211;attachment-description</code> has been used prior to this option then its value is used as the new attachment&#8217;s description. Otherwise no description will be set.</dl>
<p> <code>&#8211;replace-attachment</code> <i>selector</i>:<i>filename</i></p>
<dl>
<dt>
<dd> Replaces one or more attachments that match <i>selector</i> with the file <i>filename</i>. If more than one existing attachment matches <i>selector</i> then all of their contents will be replaced by the content of <i>filename</i>. </p>
<p> The <i>selector</i> can have one of four forms. They&#8217;re exlained below in the section attachment selectors. </p>
<p> If the option <code>&#8211;attachment-name</code> has been used prior to this option then its value is used as the replaced attachment&#8217;s name. Otherwise the name is not changed. </p>
<p> If the option <code>&#8211;attachment-mime-type</code> has been used prior to this option then its value is used as the replaced attachment&#8217;s MIME type. Otherwise the MIME type is not changed. </p>
<p> If the option <code>&#8211;attachment-description</code> has been used prior to this option then its value is used as the replaced attachment&#8217;s description. Otherwise no description is not changed.</dl>
<p> <code>&#8211;delete-attachment</code> <i>selector</i></p>
<dl>
<dt>
<dd> Deletes one or more attachments that match <i>selector</i>. </p>
<p> The <i>selector</i> can have one of four forms. They&#8217;re exlained below in the section attachment selectors.</dl>
<p> Options for attachment actions: </p>
<p> <code>&#8211;attachment-name</code> <i>name</i></p>
<dl>
<dt>
<dd> Sets the name to use for the following <code>&#8211;add-attachment</code> or <code>&#8211;replace-attachment</code> operation.</dl>
<p> <code>&#8211;attachment-mime-type</code> <i>mime-type</i></p>
<dl>
<dt>
<dd> Sets the MIME type to use for the following <code>&#8211;add-attachment</code> or <code>&#8211;replace-attachment</code> operation.</dl>
<p> <code>&#8211;attachment-description</code> <i>description</i></p>
<dl>
<dt>
<dd> Sets the description to use for the following <code>&#8211;add-attachment</code> or <code>&#8211;replace-attachment</code> operation.</dl>
<p> Other options: </p>
<p> <code>&#8211;command-line-charset</code> <i>character-set</i></p>
<dl>
<dt>
<dd> Sets the character set to convert strings given on the command line from. It defaults to the character set given by system&#8217;s current locale.</dl>
<p> <code>&#8211;output-charset</code> <i>character-set</i></p>
<dl>
<dt>
<dd> Sets the character set to which strings are converted that are to be output. It defaults to the character set given by system&#8217;s current locale.</dl>
<p> <code>-r</code>, <code>&#8211;redirect-output</code> <i>file-name</i></p>
<dl>
<dt>
<dd> Writes all messages to the file <i>file-name</i> instead of to the console. While this can be done easily with output redirection there are cases in which this option is needed: when the terminal reinterprets the output before writing it to a file. The character set set with <code>&#8211;output-charset</code> is honored.</dl>
<p> <code>&#8211;ui-language</code> <i>code</i></p>
<dl>
<dt>
<dd> Forces the translations for the language <i>code</i> to be used (e.g. &#8216;de_DE&#8217; for the German translations). It is preferable to use the environment variables <i>LANG</i>, <i>LC_MESSAGES</i> and <i>LC_ALL</i> though. Entering &#8216;list&#8217; as the <i>code</i> will cause <code><a href="/docs/linux/man/1-mkvextract/">mkvextract</a></code>(1) to output a list of available translations.</dl>
<p> <code>&#8211;debug</code> <i>topic</i></p>
<dl>
<dt>
<dd> Turn on debugging for a specific feature. This option is only useful for developers.</dl>
<p> <code>&#8211;engage</code> <i>feature</i></p>
<dl>
<dt>
<dd> Turn on experimental features. A list of available features can be requested with <code>mkvpropedit &#8211;engage list</code>. These features are not meant to be used in normal situations.</dl>
<p> <code>&#8211;gui-mode</code></p>
<dl>
<dt>
<dd> Turns on GUI mode. In this mode specially-formatted lines may be output that can tell a controlling GUI what&#8217;s happening. These messages follow the format &#8216;#GUI#message&#8217;. The message may be followed by key/value pairs as in &#8216;#GUI#message#key1=value1#key2=value2&#8230;&#8217;. Neither the messages nor the keys are ever translated and always output in English.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Be verbose and show all the important Matroska(TM) elements as they&#8217;re read.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show usage information and exit.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Show version information and exit.</dl>
<p> <code>&#8211;check-for-updates</code></p>
<dl>
<dt>
<dd> Checks online for new releases by downloading the URL m[blue]<code><a rel="nofollow" href="http://mkvtoolnix-releases.bunkus.org/latest-release.xml">http://mkvtoolnix-releases.bunkus.org/latest-release.xml</a></code>m[]. Four lines will be output in key=value style: the URL from where the information was retrieved (key version_check_url), the currently running version (key running_version), the latest release&#8217;s version (key available_version) and the download URL (key download_url). </p>
<p> Afterwards the program exists with an exit code of 0 if no newer release is available, with 1 if a newer release is available and with 2 if an error occured (e.g. if the update information could not be retrieved). </p>
<p> This option is only available if the program was built with support for libcurl.</dl>
<p> <code>@</code><i>options-file</i></p>
<dl>
<dt>
<dd> Reads additional command line arguments from the file <i>options-file</i>. Lines whose first non-whitespace character is a hash mark (&#8216;#&#8217;) are treated as comments and ignored. White spaces at the start and end of a line will be stripped. Each line must contain exactly one option. </p>
<p> Several chars can be escaped, e.g. if you need to start a non-comment line with &#8216;#&#8217;. The rules are described in the section about escaping text. </p>
<p> The command line &#8216;<code>mkvpropedit source.mkv &#8211;edit track:a2 &#8211;set name=Comments</code>&#8216; could be converted into the following option file: </p>
<dl>
<dt>
<dd>
<pre>
# Modify source.mkv
source.mkv
# Edit the second audio track
--edit
track:a2
# and set the title to 'Comments'
--set
name=Comments
</pre>
</dl>
</dl>
<h2>EDIT SELECTORS</h2>
<p> The <code>&#8211;edit</code> option sets the Matroska(TM) file section (segment information or a certain track&#8217;s headers) that all following add, set and delete actions operate on. This stays valid until the next <code>&#8211;edit</code> option is found. The argument to this option is called the edit selector. </p>
<p> By default <code><a href="/docs/linux/man/1-mkvpropedit/">mkvpropedit</a></code>(1) will edit the segment information section.</p>
<h3>Segment information</h3>
<p> The segment information can be selected with one of these three words: &#8216;info&#8217;, &#8216;segment_info&#8217; or &#8216;segmentinfo&#8217;. It contains properties like the segment title or the segment UID.</p>
<h3>Track headers</h3>
<p> Track headers can be selected with a slightly more complex selector. All variations start with &#8216;track:&#8217;. The track header properties include elements like the language code, &#8216;default track&#8217; flag or the track&#8217;s name. </p>
<p> <code>track:</code><i>n</i></p>
<dl>
<dt>
<dd> If the parameter <i>n</i> is a number then the <i>n</i>th track will be selected. The track order is the same that <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1)&#8217;s <code>&#8211;identify</code> option outputs. </p>
<p> Numbering starts at 1.</dl>
<p> <code>track:</code><i>t</i><i>n</i></p>
<dl>
<dt>
<dd> If the parameter starts with a single character <i>t</i> followed by a <i>n</i> then the <i>n</i>th track of a specific track type will be selected. The track type parameter <i>t</i> must be one of these four characters: &#8216;a&#8217; for an audio track, &#8216;b&#8217; for a button track, &#8216;s&#8217; for a subtitle track and &#8216;v&#8217; for a video track. The track order is the same that <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1)&#8217;s <code>&#8211;identify</code> option outputs. </p>
<p> Numbering starts at 1.</dl>
<p> <code>track:</code>=<i>uid</i></p>
<dl>
<dt>
<dd> If the parameter starts with a &#8216;=&#8217; followed by a number <i>uid</i> then the track whose track UID element equals this <i>uid</i>. Track UIDs can be obtained with <code><a href="/docs/linux/man/1-mkvinfo/">mkvinfo</a></code>(1).</dl>
<p> <code>track:</code>@<i>number</i></p>
<dl>
<dt>
<dd> If the parameter starts with a &#8216;@&#8217; followed by a number <i>number</i> then the track whose track number element equals this <i>number</i>. Track number can be obtained with <code><a href="/docs/linux/man/1-mkvinfo/">mkvinfo</a></code>(1).</dl>
<h3>Notes</h3>
<p> Due to the nature of the track edit selectors it is possible that several selectors actually match the same track headers. In such cases all actions for those edit selectors will be combined and executed in the order in which they&#8217;re given on the command line.</p>
<h2>ATTACHMENT SELECTORS</h2>
<p> An attachment selector is used with the two actions <code>&#8211;replace-attachment</code> and <code>&#8211;delete-attachment</code>. It can have one of the following four forms: </p>
<dl>
<dt>
<dd> 1. Selection by attachment ID. In this form the selector is simply a number, the attachment&#8217;s ID as output by <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1)&#8217;s identification command.</dl>
<dl>
<dt>
<dd> 2. Selection by attachment UID (unique ID). In this form the selector is the equal sign = followed by a number, the attachment&#8217;s unique ID as output by <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1)&#8217;s verbose identification command.</dl>
<dl>
<dt>
<dd> 3. Selection by attachment name. In this form the selector is the literal word name: followed by the existing attachment&#8217;s name. If this selector is used with <code>&#8211;replace-attachment</code> then colons within the name to match must be escaped as 
