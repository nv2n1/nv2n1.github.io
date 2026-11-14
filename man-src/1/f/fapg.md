---
title: "fapg(1)"
name: "fapg"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fapg/"
description: "fapg – Fast Audio Playlist Generator"
---

<h2 class="name">NAME</h2>
<p> fapg &#8211; Fast Audio Playlist Generator</p>
<h2>SYNOPSIS</h2>
<p> <code>fapg [</code> <i>options</i> <code>]</code> <i>/path/to/mp3/dir1 </i> <code>[</code> <i>/path/to/mp3/dir2 </i> <code>&#8230; ]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>fapg</code> is a tool to generate list of audio files (Wav, MP2, MP3, Ogg, etc) in various formats (M3U, PLS, XSPF, HTML, RSS, etc). It is very useful if you have a large amount of audio files and you want to quickly and frequently build a playlist. It is coded in C to be as fast as possible, and does not use any specific audio library (like ID3Lib). This allow you to deploy it faster and easier, and to have better performances since the less informations are loaded. On the other hand, this tool is not (yet) compatible with all the known formats. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-b|&#8211;backslash</p>
<dd> Replace the &#8216;/&#8217; with &#8221; in Unix path.</p>
<dt>-d|&#8211;debug</p>
<dd> Display useful messages if the program fails ;)</p>
<dt>-f|&#8211;format=m3u|pls|xspf|html|rss|pla|txx</p>
<dd> Choose which format of playlist you want to generate (default is m3u).</p>
<dt>-g|&#8211;genre=#:#:&#8230;</p>
<dd> Choose which genres (numerical values only) will be included in the generated playlist (default is all).</p>
<dt>-n|&#8211;nohardlink</p>
<dd> Avoid to parse twice the files because of hardlinks.</p>
<dt>-o|&#8211;output=/path/to/file.m3u</p>
<dd> Choose the name of the playlist file to generate (default behavior is to display on standard output).</p>
<dt>-p|&#8211;prefix=/the/prefix</p>
<dd> Replace the Unix path with another string (useful to give a Samba path for example).</p>
<dt>-r|&#8211;recursive</p>
<dd> Recursively read the subdirectories.</p>
<dt>-w|&#8211;windows</p>
<dd> Replace all Unix characters with Windows characters.</p>
<dt>-x|&#8211;exclude=#:#:&#8230;</p>
<dd> Choose which genres (numerical values only) will be excluded in the generated playlist (default is none).</p>
<dt>-c|&#8211;command=&lt;intern|&#8230;&gt;</p>
<dd> External binary or script that produces additional fields for RSS feeds (slow).</p>
<dt>-s|&#8211;stdin</p>
<dd> Read filenames and/or directories from standard input instead of command line. </p>
</dl>
<h2>EXAMPLES</h2>
<p> Generate a PLS playlist for an album: <code>fapg &#8211;format=pls &#8211;output=~/path/to/album/list.pls ~/path/to/album</code><br />
&nbsp;<wbr> You have a file server using Samba which shares a large amount of audio files for Windows powered computers using Winamp. The directory on the server containing the files is <i>/samba/mp3 </i> and is visible on the Windows network as <i>\\server\mp3</i> : <code>cd /samba/mp3 &amp;&amp; fapg &#8211;backslash &#8211;output=/samba/mp3/list.m3u &#8211;prefix=&#8217;\\server\mp3\&#8217; &#8211;recursive &#8211;windows ./</code><br />
&nbsp;<wbr> An HTML playlist for an album: <code>fapg &#8211;output=fapg.html ~/path/to/album</code> </p>
<p> A playlist that contains all your classical tracks may receive the genres to include (or exclude) in one or multiple portions <code>fapg &#8211;genre=32:105 &#8211;genre=106:104:103 /path/to/all/music</code> </p>
<p> Generate a podcasting XML file using an external program rss.sh to generate a detailed description: <code>fapg &#8211;output=dir.xml -f rss -c /usr/local/bin/rss.sh -r &#8211;prefix=<a rel="nofollow" href="http://thisserver/basedir">http://thisserver/basedir</a> path/to/mp3</code> </p>
<p> Generate a playlist that will work on a Sansa e200 series MP3 player: <code>fapg -f pla -o /path/to/playlist.pla /path/to/all/music</code> </p>
<p> if command starts with <i>intern</i> the build-in description (Author,Title,Link) is generated. Please note that in all given directories ( and in &#8230;basedir/xml ) files called podcast.jpg are referenced. Many header fields are set to defaults using environment variables like LOGNAME or LANG. </p>
<h2>AUTHOR</h2>
<p> Antoine Jacquet &lt;royale [at] zerezo.com&gt;, <a rel="nofollow" href="http://royale.zerezo.com/fapg/.">http://royale.zerezo.com/fapg/.</a> Manpage by Thomas Kappler &lt;thomas.kappler [at] stud.uni-karlsruhe.de&gt;. </p>
<h2>Index</h2>
