---
title: "dvdauthor(1)"
name: "dvdauthor"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dvdauthor/"
description: "dvdauthor – assembles multiple mpeg program streams into a suitable DVD filesystem"
---

<h2 class="name">NAME</h2>
<p> dvdauthor &#8211; assembles multiple mpeg program streams into a suitable DVD filesystem </p>
<h2>SYNOPSIS</h2>
<p> <code>dvdauthor</code> [ <code>-o </code><i>output-dir</i> ] <code>-x </code><i>xml-control-file</i> </p>
<p> <code>dvdauthor</code> [ <code>-o </code><i>output-dir</i> ] [ <code>-j</code> | <code>&#8211;jumppad</code> | <code>-g</code> | <code>&#8211;allgprm</code> ] [ <code>-T</code> | <code>&#8211;toc</code> ] [ <i>menu or title options</i> ] </p>
<h2>DVD BACKGROUND</h2>
<p> At a high level, a DVD is a collection of menus and titles. Conceptually, a menu contains buttons which can be assigned actions and provides a list of choices to the end user, while a title contains the main content of the DVD. However, in reality many of the features available in menus (including buttons, pausing, and looping) are also available in titles. </p>
<p> The menus and titles are divided into titlesets and the VMGM menu set. A titleset can contain a number of menus and titles which are meant to act together. The &quot;menu&quot;, &quot;audio&quot;, &quot;subtitle&quot;, and &quot;angle&quot; buttons on the DVD player&#8217;s remote control will all access menus in the same titleset as the title which is being played. All the titles and menus of a given titleset have the same video, audio, and subtitle settings (the definitions for the menus are independent from the definitions for the titles), so if you want to have different settings (for example widescreen vs standard aspect ratios), then you need separate titlesets. Titlesets are not meant to jump to one another, so the VMGM menu domain is used. It is a collection of menus (no titles) that can access the menus and titles of all the titlesets. </p>
<p> One of the most frustrating things when deciding how to author a DVD is that there are often many ways to accomplish the same task. For example, you must decide whether to locate menus at the VMGM level or the titleset level. A typical setup is to locate the high level menus at the VMGM level, and the low level configuration menus (scene / audio / subtitle selection) at the titleset. If there are DVD extras, perhaps with a lower quality audio track and a 4:3 aspect ratio, then they would be in a separate titleset with a menu to select among the extras located at the titleset level.</p>
<h2>DVDAUTHOR DESCRIPTION</h2>
<p> <code>dvdauthor</code> works in discrete operations. It authors each titleset one at a time, and then finally authors the VMGM to complete the disc. At that point the contents can be written out to a DVD. If you are controlling <code>dvdauthor</code> with command line arguments, then each step will occur independently; however if you are using the XML control file, then you have the option of combining some or all the steps into one. </p>
<p> The VOBs passed to <code>dvdauthor</code> must have DVD NAV (VOBU) packets multiplexed in at the correct locations. Many tools can do this, including <code>mplex</code> from mjpegtools 1.6.0 or later. <code>dvdauthor</code> will then fill these packets in with the correct data. Special care has been taken to ensure <code>dvdauthor</code> is fifo compliant; that is every source VOB can be the output of another program (such as <code>mplex</code>). This can make execution faster on many systems by avoiding extra filesystem accesses.</p>
<h2>COMMAND LINE DESCRIPTION</h2>
<dl>
<dt><code>-o </code><i>output-dir</i></p>
<dd>
<dt><code>-O </code><i>output-dir</i></p>
<dd> The destination directory to store the DVD-Video file structure in. If -O is specified, then any existing directory is (safely) deleted (only items that look like part of a DVD-Video structure are removed).</p>
<dt><code>-x </code><i>xml-control-file</i></p>
<dd> Specifies the control file describing the output structure to create.</dl>
<p> Note that the remaining command-line options are <code>deprecated</code>. Use the XML control file instead.</p>
<dl>
<dt><code>-j</code></p>
<dd>
<dt><code>&#8211;jumppad</code></p>
<dd> Enables the creation of jumppads, which allow greater flexibility in choosing jump/call destinations.</p>
<dt><code>-g</code></p>
<dd>
<dt><code>&#8211;allgprm</code></p>
<dd> Enable the use of all 16 general purpose registers. Prohibits the use of jumppad and some complex expressions that require temporary registers.</p>
<dt><code>-T</code></p>
<dd> Creates the table of contents file instead of a titleset. If this option is used, it should be listed first, and you may not specify any titles.</p>
<dt><code>-m</code></p>
<dd> Creates a menu.</p>
<dt><code>-t</code></p>
<dd> Creates a title.</p>
<dt><code>-v </code><i>video-opts</i></p>
<dd>
<dt><code>&#8211;video=</code><i>video-opts</i></p>
<dd> A plus (+) separated list of video options. Dvdauthor will try to infer any unspecified options. pal, ntsc, 4:3, 16:9, 720xfull, 720&#215;576, 720&#215;480, 704xfull, 704&#215;576, 704&#215;480, 352xfull, 352&#215;576, 352&#215;480, 352xhalf, 352&#215;288, 352&#215;240, nopanscan, noletterbox, crop. Default is 4:3, 720xfull</p>
<dt><code>-a </code><i>audio-opts</i></p>
<dd>
<dt><code>&#8211;audio=</code><i>audio-opts</i></p>
<dd> A plus (+) separated list of options for an audio track, with each track separated by a comma (,). For example -a ac3+en,mp2+de specifies two audio tracks: the first is an English track encoded in AC3, the second is a German track encoded using MPEG-1 layer 2 compression. ac3, mp2, pcm, dts, 16bps, 20bps, 24bps, drc, surround, nolang, 1ch, 2ch, 3ch, 4ch, 5ch, 6ch, 7ch, 8ch, and any two letter ISO 639 language abbreviation. Default is 1 track, mp2, 20bps, nolang, 2ch. &#8216;ac3&#8217; implies drc, 6ch.</p>
<dt><code>-s </code><i>subpicture-opts</i></p>
<dd>
<dt><code>&#8211;subpictures=</code><i>subpicture-opts</i></p>
<dd> A plus (+) separated list of options for a subpicture track, with each track separated by a comma (,). nolang and any two letter language abbreviation (see -a) Default is no subpicture tracks.</p>
<dt><code>-e </code><i>entry(s)</i></p>
<dd>
<dt><code>&#8211;entry=</code><i>entry(s)</i></p>
<dd> Makes the current menu the default for certain circumstances. It is a comma separated list of any of: </p>
<p> for TOC menus: title </p>
<p> for VTS menus: root, ptt, audio, subtitle, angle</p>
<dt><code>-p </code><i>palette-file</i></p>
<dd>
<dt><code>&#8211;palette=</code><i>palette-file</i></p>
<dd> Specifies where to get the subpicture palette. Settable per title and per menu. If the filename ends in .rgb (case insensitive) then it is assumed to be RGB, otherwise it is YUV. Entries should be 6 hexadecimal digits. <i>FILE</i> defaults to xste-palette.dat</p>
<dt><code>-c </code><i>chapterpts</i></p>
<dd>
<dt><code>&#8211;chapters=</code><i>chapterpts</i></p>
<dd> Specifies a comma (,) separated list of chapter markers. Each marker is of the form [[h:]mm:]ss[.frac] and is relative to the SCR of the next file listed (independent of any timestamp transposing that occurs within dvdauthor). The chapter markers ONLY apply to the next file listed. Defaults to 0.</p>
<dt><code>-f </code><i>mpeg-file</i></p>
<dd>
<dt><code>&#8211;file=</code><i>mpeg-file</i></p>
<dd>
<dt><i>mpeg-file</i></p>
<dd> Specifies either a file, a pipe, or a shell command ending in | which supplies an MPEG-2 system stream with VOB sectors inserted in the appropriate places (using mplex -f 8 to generate)</p>
<dt><code>-b </code><i>buttondef</i></p>
<dd>
<dt><code>&#8211;button=</code><i>X1xY1-X2xY2,commandlist</i></p>
<dd> creates a button of the specified size. See LANGUAGE DESCRIPTION for a description of <i>commandlist</i>.</p>
<dt><code>-i </code><i>[pre|post]=commandlist</i></p>
<dd>
<dt><code>&#8211;instructions=</code><i>[pre|post]=commandlist</i></p>
<dd> Executes the <i>commandlist</i> instructions either before or at the end of the menu/title. See LANGUAGE DESCRIPTION for the format of <i>commandlist.</i></dl>
<h2>XML DESCRIPTION</h2>
<p> Here is the basic structure of the control file: </p>
<pre><code>
&lt;dvdauthor [dest="output-dir"] [jumppad="1|on|yes" | allgprm="1|on|yes"] [format="ntsc|pal"] [provider="provider"]&gt;
   &lt;vmgm&gt;
      [&lt;fpc&gt;commands;&lt;/fpc&gt;]
      &lt;menus [lang="language-code"]&gt;
         &lt;video [format="ntsc|pal"] [aspect="4:3|16:9"]
                [resolution="XxY"] 
                [widescreen="nopanscan|noletterbox|crop"] /&gt;
         &lt;audio [format="mp2|ac3|dts|pcm"] [channels="numchannels"]
                [quant="16bps|20bps|24bps|drc"] [dolby="surround"]
                [samplerate="48khz|96khz"] [lang="language"]
                [content="normal|impaired|comments1|comments2"] /&gt;
         [&lt;audio ... /&gt;]
         &lt;subpicture [lang="language-code"]&gt;
            &lt;stream mode="normal|widescreen|letterbox|panscan"
                [content="normal|large|children|normal_cc|large_cc|children_cc|forced|director|large_director|children_director"]
                id="streamid" /&gt;
            [&lt;stream ... /&gt;]
         &lt;/subpicture&gt;
         [&lt;subpicture ... /&gt;]
         &lt;pgc [entry="title"] [palette="yuvfile|rgbfile"]
              [pause="seconds|inf"]&gt;
            &lt;subpicture&gt;
               [&lt;stream ... /&gt;]
            &lt;/subpicture&gt;
            &lt;pre&gt; commands; &lt;/pre&gt;
            &lt;vob file="file.mpg" [chapters="chapter-list"]
                 [pause="seconds|inf"]&gt;
                 &lt;cell [start="timestamp"] [end="timestamp"]
                    [chapter="1|on|yes" | program="1|on|yes"] [pause="seconds|inf"]&gt;
                    commands;
                 &lt;/cell&gt;
            &lt;/vob&gt;
            [&lt;vob ... /&gt;]
            &lt;button [name="buttonname"]&gt; commands; &lt;/button&gt;
            [&lt;button ... /&gt;]
            &lt;post&gt; commands; &lt;/post&gt;
         &lt;/pgc&gt;
         [&lt;pgc ... /&gt;]
      &lt;/menus&gt;
      [&lt;menus ... /&gt;]
   &lt;/vmgm&gt;
   &lt;titleset&gt;
      &lt;menus [lang="language-code"]&gt;
         [&lt;video ... /&gt;]
         [&lt;audio ... /&gt;]
         &lt;pgc [entry="entries"]
              [palette="yuvfile|rgbfile"] [pause="seconds|inf"]&gt;
            [...]
         &lt;/pgc&gt;
         [&lt;pgc ... /&gt;]
      &lt;/menus&gt;
      [&lt;menus ... /&gt;]
      &lt;titles&gt;
         [&lt;video ... /&gt;]
         [&lt;audio ... /&gt;]
         &lt;pgc [entry="notitle"] [palette="yuvfile|rgbfile"] [pause="seconds|inf"]&gt;
            [...]
         &lt;/pgc&gt;
         [&lt;pgc ... /&gt;]
      &lt;/titles&gt;
   &lt;/titleset&gt;
   [&lt;titleset ... /&gt;]
&lt;/dvdauthor&gt;
</code></pre>
<p> A breakdown of the control file:</p>
<dl>
<dt><code>&lt;dvdauthor [dest=&quot;</code><i>output-dir</i><code>&quot;] [jumppad=&quot;1|on|yes&quot; | allgprm=&quot;1|on|yes&quot;] [format=&quot;ntsc|pal&quot;] [provider=&quot;</code><i>provider</i><code>&quot;]&gt;</code></p>
<dd> Initiates dvdauthor. dest denotes the directory where <code>dvdauthor</code> will write the files. This is overridden by the -o option. Contains up to one &lt;vmgm&gt; tag and any number of &lt;titleset&gt;&#8217;s.</p>
<dt><code>&lt;vmgm&gt;</code></p>
<dd>
<dt><code>&lt;titleset&gt;</code></p>
<dd> Constructs of a VMGM level menu set or a title set. Contains zero or more &lt;menus&gt; tags and if a titleset, up to one &lt;titles&gt; tag.</p>
<dt><code>&lt;menus [lang=&quot;</code><i>language-code</i><code>&quot;]&gt;</code></p>
<dd> Marks a list of menus with a common language for this VMGM menu set or titleset, called in <code>dvdauthor</code> terminology a &quot;pgcgroup.&quot; Contains up to one &lt;video&gt; tag, up to one &lt;audio&gt; tag, up to one &lt;subpicture&gt; tag, and any number of &lt;pgc&gt; tags.</p>
<dt><code>&lt;titles&gt;</code></p>
<dd> Marks the list of titles for this titleset, called in <code>dvdauthor</code> terminology a &quot;pgcgroup.&quot; Contains up to one &lt;video&gt; tag, up to eight &lt;audio&gt; tags, up to 32 &lt;subpicture&gt; tags, and any number of &lt;pgc&gt; tags.</p>
<dt><code>&lt;video [format=&quot;ntsc|pal&quot;] [aspect=&quot;4:3|16:9&quot;] [resolution=&quot;</code><i>XxY</i><code>&quot;]  [widescreen=&quot;nopanscan|noletterbox|crop&quot;] /&gt;</code></p>
<dd> Manually configures the video parameters for this pgcgroup. If any of these are not set, then they will be inferred from the source stream. Note that the DVD format only specifically supports 720&#215;480, 704&#215;480, 352&#215;480, and 352&#215;240 resolutions for NTSC, and 720&#215;576, 704&#215;576, 352&#215;576, and 352&#215;288 resolutions for PAL, but DVD author will accept a wider range of inputs and round up to the nearest size.</p>
<dt><code>&lt;audio [format=&quot;mp2|ac3|dts|pcm&quot;] [channels=&quot;</code><i>numchannels</i><code>&quot;] [dolby=&quot;surround&quot;] [quant=&quot;16bps|20bps|24bps|drc&quot;] [samplerate=&quot;48khz|96khz&quot;] [lang=&quot;</code><i>language</i><code>&quot;] [content=&quot;normal|impaired|comments1|comments2&quot;] /&gt;</code></p>
<dd> Manually configures an audio stream for this pgcgroup. List once for each stream. Most parameters are inferred automatically from the source VOBs except for PCM parameters. However, language and content must be manually specified. Note that it is possible to just list the language and content attributes and let <code>dvdauthor</code> fill in the rest.</p>
<dt><code>&lt;subpicture [lang=&quot;</code><i>language</i><code>&quot;] [content=&quot;normal|large|children|normal_cc|large_cc|children_cc|forced|director|large_director|children_director&quot;] /&gt;</code></p>
<dd> Manually configures a subpicture/subtitle for this pgcgroup or PGC. At the pgcgroup level, list once for each language. Occurrences at the PGC level don&#8217;t have lang or content attributes; they inherit those from the corresponding &lt;subpicture&gt; tag at the pgcgroup level.</p>
<dt><code>&lt;stream mode=&quot;normal|widescreen|letterbox|panscan&quot; id=&quot;</code><i>streamid</i><code>&quot; /&gt;</code></p>
<dd> Specifies the ID of a stream that is the representation of this subpicture in a particular display mode. This can be specified per-PGC, or pgcgroup-wide.</p>
<dt><code>&lt;pgc [entry=&quot;</code><i>entries</i><code>&quot;] [palette=&quot;</code><i>yuvfile|rgbfile</i><code>&quot;] [pause=&quot;</code><i>seconds</i><code>|inf&quot;]&gt;</code></p>
<dd> A PGC is just a fancy term for either a menu or a title. It has a special meaning in the DVD spec so I have retained its use here. PGC&#8217;s can have commands that get executed before they start playing or after they finish; see &lt;pre&gt; and &lt;post&gt; tags below. </p>
<p> If the PGC is a menu, you can specify one or more entries for it. This means that if you press the corresponding button on your DVD remote, then it will go to this menu. For a VMGM level menu, the only choice is title, which on my remote corresponds to the top menu button. For a titleset level menu, you can use root, subtitle, audio, angle, and ptt. If you want more than one, separate them by a space or a comma. Note that root entry is meant for commands that jump from a VMGM level menu to a titleset menu. </p>
<p> If the PGC is in a titleset, then it is assumed to be a title unless entry=&quot;notitle&quot; is specified. </p>
<p> All button and menu masks and all subtitles within a PGC must share the same 16 color palette. If you use <code>spumux</code> to generate the subtitle/subpicture packets, then the color information will be automatically passed to <code>dvdauthor</code>; however, if you use another subtitler or want to have more control over the palette, you can manually specify it with the palette attribute. The first 16 entries of the file should be the 16 colors of the palette, listed as 6 digit hexadecimal numbers representing either the RGB breakdown (if the filename ends in .rgb or the YUV breakdown (if the filename does not end in .rgb. After that, the button group information can be listed as pairs of 8 digit hexadecimal numbers; up to three button groups may be specified. </p>
<p> If you have a short video sequence or just want the video to pause at the end, you can use the pause attribute to set the number of seconds (as an integer) from 1 to 254. If you want the video to pause indefinitely, use inf.</p>
<dt><code>&lt;pre&gt; </code><i>commands;</i><code> &lt;/pre&gt;</code></p>
<dd>
<dt><code>&lt;post&gt; </code><i>commands;</i><code> &lt;/post&gt;</code></p>
<dd> Sets the commands to execute before or after a PGC plays. It can be used to loop the current video (by having a &lt;post&gt; jump &#8230; &lt;/post&gt; sequence), or to conditionally skip certain chapters if a flag has been set.</p>
<dt><code>&lt;fpc&gt; </code><i>commands;</i><code> &lt;/fpc&gt;</code></p>
<dd> Sets the commands to execute when the disk is first put in the player (FPC = First Program Chain). It can be used to jump to a particular menu or initialize registers on startup. If not specified, an implicit one will be created that jumps to the first menu found, or if there is no menu it will jump to the first title..</p>
<dt><code>&lt;vob file=&quot;</code><i>file.mpg</i><code>&quot; [chapters=&quot;</code><i>chapter-list</i><code>&quot;] [pause=&quot;</code><i>seconds</i><code>|inf&quot;] /&gt;</code></p>
<dd> Specifies an input video file for a menu or title, with optional chapter points and pause at the end.</p>
<dt><code>&lt;cell [start=&quot;</code><i>timestamp</i><code>&quot;] [end=&quot;</code><i>timestamp</i><code>&quot;] [chapter=&quot;1|on|yes&quot; | program=&quot;1|on|yes&quot;] [pause=&quot;</code><i>seconds</i><code>|inf&quot;]&gt; </code><i>commands;</i><code> &lt;/cell&gt;</code></p>
<dd> A more detailed way of specifying marker points in a title. If present, then the containing &lt;vob&gt; must not have a chapters attribute. A cell can have a VM command attached to it, to be executed when it plays. If the program attribute is set, then this cell will be a point that the user can skip to using the prev/next buttons on their DVD player remote. If the chapter attribute is set (implies program is set as well), then this cell is also a chapter point.</p>
<dt><code>&lt;button [name=&quot;</code><i>buttonname</i><code>&quot;]&gt; </code><i>commands;</i><code> &lt;/button&gt;</code></p>
<dd> Specifies the commands to be executed when the user selects the button with the specified name. You define button names and placements with <code>spumux</code>.</dl>
<h2>LANGUAGE DESCRIPTION</h2>
<p> The language is quite simple and roughly looks like C.</p>
<dl>
<dt>&bull;</p>
<dd> Statements are terminated with a semicolon.</p>
<dt>&bull;</p>
<dd> Statements can span multiple lines.</p>
<dt>&bull;</p>
<dd> Multiple statements can appear on one line.</p>
<dt>&bull;</p>
<dd> Whitespace (space, tab, newlines) are not important, except to separate keywords and identifiers.</p>
<dt>&bull;</p>
<dd> C-style /* &#8230; */ comments are allowed. Or you can use XML comments &lt;!&#8211; like this &#8211;&gt;</dl>
<h3>VARIABLES</h3>
<p> The DVD virtual machine processes 16 bit values. It supports up to 16 general purpose registers; however <code>dvdauthor</code> reserves 3 for internal use. Thus register 0-12 are available for use and are referred to as g0 through g12. </p>
<p> There are also 24 system registers, which can be referred to as s0 through s23. Not all of these can be set. Many of these have mnemonic synonyms.</p>
<dl>
<dt><code>audio (s1, rw)</code></p>
<dd> Denotes the audio stream, ranging from 0-7.</p>
<dt><code>subtitle (s2, rw)</code></p>
<dd> The subtitle track, ranging from 0-31. If you want the subtitle to always be displayed, then you should add 64 (i.e. choose 64-95). Simply selecting the track (0-31) means that only the forced subtitles will be displayed, whereas enabling the track (64-95) means that all the subtitles will be displayed. This allows you to have forced subtitles only for the parts of the movie where the actors are speaking a foreign (to the viewer) language, but still have normal subtitles for the hearing impaired. The hearing impaired viewers would enable the track (64-95) while the other viewers would just select the track (0-31) they would be able to share the track.</p>
<dt><code>angle (s3, rw)</code></p>
<dd> Selects the angle (currently untested).</p>
<dt><code>button (s8, rw)</code></p>
<dd> Denotes the currently highlighted button. Note that the value is multiplied by 1024, so the first button is 1024, the second is 2048, etc.</dl>
<h3>EXPRESSIONS</h3>
<p> Expressions follow typical C syntax except that booleans are not convertible to integers and vice versa. Operators and comparisons are: </p>
<p> ==, !=, &gt;=, &gt;, &lt;=, &lt;, &amp;&amp;, ||, !, eq, ne, ge, gt, le, lt, and, or, xor, not, +, -, *, /, %, &amp;, |, ^ </p>
<p> Since the code is encapsulated in XML, the parser will catch any unescaped &lt; characters (i.e. not written as &quot;&amp;lt;&quot;), thus alphabetic mnemonics have been provided for all comparison operators for consistency. Or you can put the code in a &lt;![CDATA[ &#8230; ]]&gt; section. </p>
<p> There is also a numerical function:</p>
<dl>
<dt><code>random(</code><i>EXPRESSION</i><code>)</code></p>
<dd> Computes a pseudo-random number, between 1 and the supplied number, inclusively.</dl>
<h3>BLOCKS</h3>
<p> Blocks are either a single statement (terminated by a semicolon), or a group of statements wrapped in curly braces. For example:</p>
<dl>
<dt>&bull;</p>
<dd>
<pre>
g3 = s7;
</pre>
<dt>&bull;</p>
<dd>
<pre><code>
{
    audio = 1;
    subtitle = 65;
    jump vmgm menu 3;
}
</code></pre>
</dl>
<h3>STATEMENTS</h3>
<p> The statements supported are fairly simple at the moment.</p>
<dl>
<dt><i>VARIABLE</i><code> = </code><i>EXPRESSION</i><code>;</code></p>
<dd> Sets a variable equal to the result of an equation.</p>
<dt><code>if (</code><i>EXPRESSION</i><code>) </code><i>BLOCK;</i></p>
<dd>
<dt><code>if (</code><i>EXPRESSION</i><code>) </code><i>BLOCK;</i><code> else </code><i>BLOCK;</i></p>
<dd> Calculates the expression; if true, then it executes the block of code.</p>
<dt><code>jump </code><i>TARGET</i><code>;</code></p>
<dd>
<dt><code>call </code><i>TARGET</i><code> [resume </code><i>CELL</i><code>];</code></p>
<dd>
<dt><code>resume;</code></p>
<dd> Jumps to a particular title or menu, or calls a particular menu, or returns to the calling title. You can only execute a call from a title to a menu; all other forms are illegal. The purpose of using call instead of jump (besides the fact that they support a mutually exclusive list of targets) is to allow the menu to return to the point in the title where the call originated using resume. You can manually specify the return cell by using the resume keyword, however if you do not specify one and you use the command in a post instruction block, then it will presume cell 1.</dl>
<h3>TARGETS</h3>
<p> The following are possible targets (note that menus do not have chapters):</p>
<dl>
<dt><code>[vmgm | titleset </code><i>X</i><code>] menu</code></p>
<dd>
<dt><code>[vmgm | titleset </code><i>X</i><code>] menu </code><i>Y</i></p>
<dd>
<dt><code>[vmgm | titleset </code><i>X</i><code>] menu entry </code><i>Z</i></p>
<dd> Targets either the default menu, a menu number Y, or the menu denoted as the entry for Z. The menu is in either the VMGM or titleset domain. If you wish to target a menu in the current domain then you can omit the domain moniker.</p>
<dt><code>[titleset </code><i>X</i><code>] title </code><i>Y</i><code> [chapter </code><i>Z</i><code>]</code></p>
<dd> Targets a title, or a chapter in a title. Numbering starts at 1. All of the titles on the disc are accessible in the VMGM domain, or you can access them by titleset instead.</p>
<dt><code>pgc </code><i>Z</i></p>
<dd> Targets a PGC in the current VMGM or titleset.</p>
<dt><code>chapter </code><i>Z</i></p>
<dd> Targets a chapter in the current title.</p>
<dt><code>program </code><i>Z</i></p>
<dd>
<dt><code>cell </code><i>Z</i></p>
<dd> Targets a program or cell in the current PGC. You can use this to create looping menus: jump cell 1;</p>
<dt><code>cell top</code></p>
<dd>
<dt><code>next cell</code></p>
<dd>
<dt><code>prev cell</code></p>
<dd>
<dt><code>program top</code></p>
<dd>
<dt><code>next program</code></p>
<dd>
<dt><code>prev program</code></p>
<dd>
<dt><code>pgc top</code></p>
<dd>
<dt><code>next pgc</code></p>
<dd>
<dt><code>prev pgc</code></p>
<dd>
<dt><code>up pgc</code></p>
<dd>
<dt><code>pgc tail</code></p>
<dd> (Jump only) performs relative transfers of control within the current menu/title. &quot;cell/program/pgc top&quot; goes back to the start of the current cell/program/PGC; &quot;next/prev cell/program/pgc&quot; goes to the next or previous cell/program/PGC; &quot;up pgc&quot; goes to the &quot;up&quot; PGC (not currently settable in <code>dvdauthor</code>); and &quot;pgc tail&quot; goes to the &lt;post&gt; sequence in the current PGC.</dl>
<p> Chapters are numbered from 1 in each title, while programs are numbered from 1 in each PGC. Thus, the latter can reset independently of the former when there is more than one PGC in a title.</p>
<h2>LIMITATIONS</h2>
<p> The following limits are imposed by the DVD-Video spec. </p>
<p> There can be no more than 99 titlesets, no more than 99 menus in the VMG or a titleset, and no more than 99 titles in a titleset. </p>
<p> Each title may be made up of up to 999 PGCs. Each PGC may consist of up to 255 programs. The &lt;pre&gt; and &lt;post&gt; sections of a PGC put together can contain no more than 128 VM instructions. </p>
<p> Since there is only one VOB file (VIDEO_TS.VOB) in the VMG, the total amount of video in the VMG menus must fit into 1073709056 bytes (524272 sectors of 2kiB each). In each titleset, all the menu video must fit in the first VOB (VTS_nn_0.VOB), so is limited to the same amount. &lt;marc.leeman [at] gmail.com&gt; MarcLeeman2003Marc Leeman </p>
<h2>Index</h2>
