---
title: "cue2toc(1)"
name: "cue2toc"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cue2toc/"
description: "cue2toc – convert CUE to TOC format"
---

<h2 class="name">NAME</h2>
<p> cue2toc &#8211; convert CUE to TOC format</p>
<h2>SYNOPSIS</h2>
<p> <code>cue2toc</code> [<code>-hnqv</code>] [<code>-o</code> <i>tocfile</i>] [<code>-w</code> <i>wavefile</i>] [<i>cuefile</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>Cue2toc</code> converts <i>cuefile</i> from CUE to TOC format and writes the result to <i>tocfile</i>. If either <i>cuefile</i> or <i>tocfile</i> is omitted or a single dash &quot;-&quot; <code>cue2toc</code> reads from standard input and writes to standard ouput respectively. </p>
<p> CUE files are text files describing the layout of a CD-Rom and typically carry the extension &quot;.cue&quot;. </p>
<p> Cdrdao is a CD-burning application which has its own native TOC format to describe the disc layout. Although cdrdao has direct support for reading CUE files, it is currently limited to data tracks only. So <code>cue2toc</code>&#8216;s main usefulness lies in converting CUE files containing audio tracks. </p>
<p> Output of CD-Text data can be disabled with the <code>-n</code> option. </p>
<p> CUE files often come with MP3 files but since cdrdao doesnt support decoding them on the fly they probably must be decoded by other means prior to writing the CD (e.g. using <code>lame</code>). For this reason you can specify a filename with the <code>-w</code> option to be used for all audio tracks instead of the one in the CUE file. Of course this is only really useful if all the tracks are based on the same file. This seems to be the case quite often however. </p>
<p> <code>Cue2toc</code> normally displays warning messages for unsupported commands and constructs. The <code>-q</code> option disables these warnings. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> print a short help message </p>
<dt><code>-n</code></p>
<dd> no CD-Text; disable output of CD-Text information </p>
<dt><code>-o </code><i>tocfile</i></p>
<dd> write result to <i>tocfile</i> instead of standard ouput </p>
<dt><code>-q</code></p>
<dd> quiet mode; do not print warnings </p>
<dt><code>-v</code></p>
<dd> print version number </p>
<dt><code>-w </code><i>wavefile</i></p>
<dd> use <i>wavefile</i> for all audio tracks </p>
</dl>
<h2>CUE FORMAT</h2>
<p> What follows is a description of the CUE format expected by <code>cue2toc</code>. For information about the TOC format please consult the <code><a href="/docs/linux/man/1-cdrdao/">cdrdao</a></code>(1) manual page. </p>
<p> CUE files consist of commands and their arguments which must be separated from each other by any number of whitespace characters. Space, horizontal tabulator, newline and carriage return are recognized as whitespace characters except inside strings surrounded by double quotes, where they are part of the string. Commands are not case sensitive. CD-Text data can be at most 80 characters per item. </p>
<p> Timecode values are accepted in the forms &quot;X:X:X&quot;, &quot;X:X&quot; and &quot;X&quot; where each &quot;X&quot; must consist of at most two digits and may be zero padded to the left. They are interpreted as &quot;M:S:F&quot;, &quot;S:F&quot; and &quot;F&quot; respectively where &quot;M&quot; means &quot;minutes&quot; and must be in the range 0 &lt;= M &lt;= 99, &quot;S&quot; means &quot;seconds&quot; and must be in the range 0 &lt;= S &lt;= 59, and &quot;F&quot; means &quot;frames&quot; and must be in the range 0 &lt;= F &lt;= 74. </p>
<p> CUE files are logically divided into a global section and one to 99 track sections. Inside these sections the following commands are allowed: </p>
<h3>Global Section</h3>
<p> <code>REM</code> <i>anything_to_newline</i><br />
 <code>CATALOG</code> <i>string</i><br />
 <code>CDTEXTFILE</code> <i>string</i><br />
 <code>TITLE</code> <i>string</i><br />
 <code>PERFORMER</code> <i>string</i><br />
 <code>SONGWRITER</code> <i>string</i><br />
 <code>FILE</code> <i>string</i> <code>BINARY</code>|<code>MOTOROLA</code>|<code>AIFF</code>|<code>WAVE</code>|<code>MP3</code> </p>
<dl>
<dt><code>REM</code></p>
<dd> Optional. Introduces a comment. Anything from there on up to and including the next newline character is ignored. Comments can appear anywhere in the file but not between a command and its arguments. </p>
<dt><code>CATALOG</code></p>
<dd> Optional. The Media Catalog Number of the disc. Must be exactly 13 characters. </p>
<dt><code>CDTEXTFILE</code></p>
<dd> Optional. Specifies an external file containing CD-Text data. Ignored. </p>
<dt><code>TITLE</code></p>
<dd> Optional. The CD-Text title of the disc. </p>
<dt><code>PERFORMER</code></p>
<dd> Optional. The CD-Text performer of the disc. </p>
<dt><code>SONGWRITER</code></p>
<dd> Optional. The CD-Text songwriter of the disc. </p>
<dt><code>FILE</code></p>
<dd> Required. The name and type of the file to be used for all following tracks. The <i>string</i> contains the name of the file followed by one of <code>BINARY</code>, <code>MOTOROLA</code>, <code>AIFF</code>, <code>WAVE</code> or <code>MP3</code>. As far as <code>cue2toc</code> is concerned the type of the file is effectively ignored. Nonetheless <code>MOTOROLA</code>, <code>AIFF</code> and <code>MP3</code> cause printing of a warning message since these file types can not be used directly with cdrdao. </p>
</dl>
<p> The first appearance of a <code>TRACK</code> command causes leaving of the global section and entering the track section. </p>
<h3>Track Section</h3>
<p> <code>TRACK</code> <i>number</i> <i>mode</i><br />
 <code>REM</code> <i>anything_to_newline</i><br />
 <code>FLAGS</code> [<code>DCP</code>] [<code>4CH</code>] [<code>PRE</code>] [<code>SCMS</code>]<br />
 <code>ISRC</code> <i>string</i><br />
 <code>TITLE</code> <i>string</i><br />
 <code>PERFORMER</code> <i>string</i><br />
 <code>SONGWRITER</code> <i>string</i><br />
 <code>PREGAP</code> <i>timecode</i><br />
 <code>INDEX</code> <i>number</i> <i>timecode</i><br />
 <code>POSTGAP</code> <i>timecode</i><br />
 <code>FILE</code> <i>string</i> <code>BINARY</code>|<code>MOTOROLA</code>|<code>AIFF</code>|<code>WAVE</code>|<code>MP3</code> </p>
<dl>
<dt><code>TRACK</code></p>
<dd> Required. Starts a new track definition. The <i>number</i> is ignored. The <i>mode</i> must be one of <code>AUDIO</code>, <code>MODE1/2048</code>, <code>MODE1/2352</code>, <code>MODE2/2336</code> or <code>MODE2/2352</code>. </p>
<dt><code>FLAGS</code></p>
<dd> Optional. Defines the flags for this track. Must be followed by one or more of the following commands: <code>DCP</code> (digital copy permitted), <code>4CH</code> (four channel audio), <code>PRE</code> (pre-emphasis enabled) and <code>SCMS</code> (serial copy management system). <code>SCMS</code> is ignored because there is no corresponding option in the TOC format. </p>
<dt><code>ISRC</code></p>
<dd> Optional. The International Standard Recording Code for this track. Must be exactly 12 characters long. </p>
<dt><code>TITLE</code></p>
<dd> Optional. The CD-Text title of this track. </p>
<dt><code>PERFORMER</code></p>
<dd> Optional. The CD-Text performer of this track. </p>
<dt><code>SONWRITER</code></p>
<dd> Optional. The CD-Text songwriter of this track. </p>
<dt><code>PREGAP</code></p>
<dd> Optional. The length of the track pregap to be filled with zero data. Mutually exclusive with <code>INDEX 0</code>. </p>
<dt><code>POSTGAP</code></p>
<dd> Optional. The length of the track postgap to be filled with zero data. </p>
<dt><code>INDEX</code></p>
<dd> Optional. The <i>number</i> must be in the range 0 &lt;= <i>number</i> &lt;= 99. Index number 1 specifies the start of the track. Index number 0 is the start of the track pregap filled with data from the file, i.e. the difference between index 0 and index 1 is the length of the pregap. Index 0 is mutually exclusive with <code>PREGAP</code>. Index numbers greater than 1 specify subindexes for this track and must be sequential. </p>
<dt><code>FILE</code></p>
<dd> Optional in track section. The syntax is the same as described above and if it appears inside a track specification it takes effect on the next <code>TRACK</code> command. </p>
</dl>
<h2>LIMITATIONS</h2>
<p> The command <code>CDTEXTFILE</code> and the flag <code>SCMS</code> have no equivalent in the TOC format and are ignored. </p>
<p> CUE files containing data tracks which specify a starting time greater than zero cannot be converted by <code>cue2toc</code> because the TOC format does not provide a way to specify a starting time at all for data tracks. However if the CUE file does not contain any audio tracks you can try to use the CUE file directly with cdrdao. </p>
<h2>EXAMPLE</h2>
<p> Suppose we have the following CUE file &quot;uwe.froehn.cue&quot; describing an audio CD with CD-Text data: </p>
<pre>
REM Example CUE file with audio tracks
CATALOG 1234567890123
TITLE &quot;Der Berg ruft&quot;
PERFORMER &quot;Uwe Froehn&quot;
FILE &quot;uwe.froehn.mp3&quot; MP3
TRACK 01 AUDIO
  TITLE &quot;Meine Mama ist die Beste&quot;
  PERFORMER &quot;Uwe Froehn&quot;
  SONGWRITER &quot;Hansi Klabuster&quot;
  REM two seconds pregap filled with audio data
  INDEX 00 00:00:00
  INDEX 01 00:02:00
  REM subindexes
  INDEX 02 00:35:17
  INDEX 03 01:12:44
TRACK 02 AUDIO
  TITLE &quot;Hoch oben im Tal&quot;
  SONGWRITER &quot;Gabi Geil&quot;
  REM no pregap
  INDEX 01 02:45:38
TRACK 03 AUDIO
  REM pregap with zero data
  PREGAP 00:4:47
  INDEX 01 07:58:74
  REM postgap with zero data
  POSTGAP 00:35:00
</pre>
<p> Since cdrdao cannot decode the MP3 file on the fly this step must be carried out by hand, e.g. using lame: </p>
<pre>
lame --decode uwe.froehn.mp3 uwe.froehn.wav
</pre>
<p> Although the filename appears only once in the example CUE file it gets written for every track in the TOC file so you would need to edit lots of occurences of the filename in the TOC file by hand. For this reason you can specify a string with the <code>-w</code> option to be used by <code>cue2toc</code> as the filename for all audio tracks. The command </p>
<pre>
cue2toc -w uwe.froehn.wav -o uwe.froehn.toc uwe.froehn.cue
</pre>
<p> should produce the file uwe.froehn.toc with the following content: </p>
<pre><code>
CATALOG "1234567890123" CD_DA
    CD_TEXT
{
    LANGUAGE_MAP{
        0 : EN
    } LANGUAGE 0
    {
        TITLE "Der Berg ruft" PERFORMER "Uwe Froehn"
    }
}
TRACK AUDIO
    CD_TEXT
{
    LANGUAGE 0
    {
        TITLE "Meine Mama ist die Beste" PERFORMER "Uwe Froehn" SONGWRITER "Hansi Klabuster"
    }
}
AUDIOFILE "uwe.froehn.wav" 00 : 00 : 00 02 : 45 : 38 START 00 : 02 : 00 INDEX 00 : 35 : 17 INDEX 01 : 12 : 44 TRACK AUDIO
    CD_TEXT
{
    LANGUAGE 0
    {
        TITLE "Hoch oben im Tal" SONGWRITER "Gabi Geil"
    }
}
AUDIOFILE "uwe.froehn.wav" 02 : 45 : 38 05 : 13 : 36 TRACK AUDIO
    PREGAP 00 : 04 : 47 AUDIOFILE "uwe.froehn.wav" 07 : 58 : 74 SILENCE 00 : 35 : 00
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cdrdao/">cdrdao</a></code>(1), <code><a href="/docs/linux/man/1-lame/">lame</a></code>(1) </p>
<h2>BUGS</h2>
<p> Since <code>cue2toc</code>&#8216;s definition of the CUE format is entirely based on a number of different CUE files the author came across there is a very high probability that it will not work correctly with all the other CUE files you might encounter. If this is the case for you please send the problematic CUE file along with the version number of <code>cue2toc</code> to &lt;dermatsch [at] gmx.de&gt;. </p>
<h2>AUTHOR</h2>
<p> Matthias Czapla &lt;dermatsch [at] gmx.de&gt; </p>
<h2>Index</h2>
