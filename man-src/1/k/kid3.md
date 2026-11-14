---
title: "kid3(1)"
name: "kid3"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kid3/"
description: "kid3, kid3-qt, kid3-cli – Kid3 ID3 Tagger"
---

<h2 class="name">NAME</h2>
<p> kid3, kid3-qt, kid3-cli &#8211; Kid3 ID3 Tagger </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>kid3</code> [<code>&#8211;help</code> | <code>&#8211;help-qt</code> | <code>&#8211;help-kde</code> | <code>&#8211;help-all</code></p>
<dd>
&nbsp;<wbr>|<code>&#8211;author</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;version</code>&nbsp;<wbr>|&nbsp;<wbr><code>&#8211;license</code>]&nbsp;<wbr>[<i>FILE</i>&#8230;]</p>
<dt> <code>kid3-qt</code> [<code>Qt-options</code>] [<i>FILE</i>&#8230;]</p>
<dt> <code>kid3-cli</code> [<code>-h</code> | <code>&#8211;help</code>] [<code>-c COMMAND1</code>] [<code>-c COMMAND2</code>&#8230;] [<i>FILE</i>&#8230;]</dl>
<h2>OPTIONS</h2>
<p> <i>FILE</i></p>
<dl>
<dt>
<dd>
<dd>If <i>FILE</i> is the path to a directory, it will be opened. If one or more file paths are given, their common directory is opened and the files are selected.</dl>
<h3>kid3</h3>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help about options.</dl>
<p> <code>&#8211;help-qt</code></p>
<dl>
<dt>
<dd> Show Qt specific options, see <code><a href="/docs/linux/man/7-qtoptions/">qtoptions</a></code>(7).</dl>
<p> <code>&#8211;help-kde</code></p>
<dl>
<dt>
<dd> Show KDE specific options, see <code><a href="/docs/linux/man/7-kdeoptions/">kdeoptions</a></code>(7).</dl>
<p> <code>&#8211;help-all</code></p>
<dl>
<dt>
<dd> Show all options.</dl>
<p> <code>&#8211;author</code></p>
<dl>
<dt>
<dd> Show author information.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Show version information.</dl>
<p> <code>&#8211;license</code></p>
<dl>
<dt>
<dd> Show license information.</dl>
<h3>kid3-qt</h3>
<p> <code>Qt-options</code></p>
<dl>
<dt>
<dd> See <code><a href="/docs/linux/man/7-qtoptions/">qtoptions</a></code>(7), however, the options have &quot;-&quot; as a prefix, not &quot;&#8211;&quot;.</dl>
<h3>kid3-cli</h3>
<p> <code>-c</code></p>
<dl>
<dt>
<dd> Execute a command. Multiple <code>-c</code> options are possible, they are executed in sequence. See the section about kid3-cli for a description of the available commands.</dl>
<p> <code>-h</code>|<code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help about options and commands.</dl>
<h2>INTRODUCTION</h2>
<p> Kid3 is an application to edit the ID3v1 and ID3v2 tags in MP3 files in an efficient way. These tags can be edited by most MP3 players, but not in a very comfortable and efficient way. Moreover the tags in Ogg/Vorbis, FLAC, MPC, APE, MP4/AAC, MP2, Speex, TrueAudio, WavPack, WMA, WAV, AIFF files and tracker modules (MOD, S3M, IT, XM) are supported too. </p>
<p> Kid3 does not grab nor encode MP3 files, but it is targeted to edit the ID3 tags of all files of an album in an efficient way, i.e. with as few mouse clicks and key strokes as possible. Where most other programs can edit either ID3v1 or ID3v2 tags, Kid3 has full control over both versions, can convert tags between the two formats and has access to all ID3v2 tags. Tags of multiple files can be set to the same value, e.g. the artist, album, year and genre of all files of an album typically have the same values and can be set together. If the information for the tags is contained in the file name, the tags can be automatically set from the file name. It is also possible to set the file name according to the tags found in the file in arbitrary formats. </p>
<p> The editing task is further supported by automatic replacement of characters or substrings, for instance to remove illegal characters from filenames. Automatic control of upper and lower case characters makes it easy to use a consistent naming scheme in all tags. </p>
<p> The tag information for full albums can be taken from m[blue]<code>gnudb.org</code>m[]<font SIZE="-2">[1]</font>, m[blue]<code>TrackType.org</code>m[]<font SIZE="-2">[2]</font>, m[blue]<code>MusicBrainz</code>m[]<font SIZE="-2">[3]</font>, m[blue]<code>Discogs</code>m[]<font SIZE="-2">[4]</font>, m[blue]<code>Amazon</code>m[]<font SIZE="-2">[5]</font> or other sources of track lists. The import format is freely configurable by regular expressions. </p>
<p> Please report any problems or feature requests to the author.</p>
<h2>USING KID3</h2>
<h3>Kid3 features</h3>
<dl>
<dt>
<dd> &bull; Edit ID3v1.1 tags</dl>
<dl>
<dt>
<dd> &bull; Edit all ID3v2.3 and ID3v2.4 frames</dl>
<dl>
<dt>
<dd> &bull; Edit tags of multiple files</dl>
<dl>
<dt>
<dd> &bull; Convert between ID3v1 and ID3v2 tags</dl>
<dl>
<dt>
<dd> &bull; Edit MP3, Ogg/Vorbis, FLAC, MPC, APE, MP4/AAC, MP2, Speex, TrueAudio, WavPack, WMA, WAV and AIFF tags</dl>
<dl>
<dt>
<dd> &bull; Generate tags from filename</dl>
<dl>
<dt>
<dd> &bull; Generate tags from the contents of tag fields</dl>
<dl>
<dt>
<dd> &bull; Generate filename from tags</dl>
<dl>
<dt>
<dd> &bull; Generate and change directory names from tags</dl>
<dl>
<dt>
<dd> &bull; Generate playlist file</dl>
<dl>
<dt>
<dd> &bull; Automatic case conversion and string translation</dl>
<dl>
<dt>
<dd> &bull; Import from m[blue]<code>gnudb.org</code>m[]<font SIZE="-2">[1]</font>, m[blue]<code>TrackType.org</code>m[]<font SIZE="-2">[2]</font>, m[blue]<code>MusicBrainz</code>m[]<font SIZE="-2">[3]</font>, m[blue]<code>Discogs</code>m[]<font SIZE="-2">[4]</font>, m[blue]<code>Amazon</code>m[]<font SIZE="-2">[5]</font> and other data sources</dl>
<dl>
<dt>
<dd> &bull; Export as CSV, HTML, playlist, Kover XML and other formats. Exported CSV files can be imported again.</dl>
<h3>Example Usage</h3>
<p> This section describes a typical session with Kid3. Let&#8217;s assume we have a directory containing MP3 files with the tracks from the album &quot;Let&#8217;s Tag&quot; from the band &quot;One Hit Wonder&quot;. The directory is named in the &quot;artist &#8211; album&quot; format, in our case One Hit Wonder &#8211; Let&#8217;s Tag. The directory contains the tracks in the &quot;track title.mp3&quot; format, which I think is useful because the filenames are short (important when using mobile MP3 players with small displays) and in the correct order when sorted alphabetically (important when using hardware MP3 players which play the tracks in alphabetical order or in the order in which they are burnt on CD and that order is alphabetical when using <code>mkisofs</code>). Besides this, the artist and album information is already in the directory name and does not have to be repeated in the filename. But back to our example, the directory listing looks like this: </p>
<p> 01 Intro.mp3 </p>
<p> 02 We Only Got This One.mp3 </p>
<p> 03 Outro.mp3 </p>
<p> These files have no tags yet and we want to generate them using Kid3. We use Open (File menu or toolbar) and select one of the files in this directory. All files will be displayed in the file listbox. Lazy as we are, we want to use the information in the directory and file names to generate tags. Therefore we select all files, then click the To:Tag 1 button in the File section. This will set the title, artist, album and track values in all files. To set the year and genre values of all files, we keep all files selected and type in &quot;2002&quot; for the Year and select &quot;Pop&quot; from the Genre combobox. To set only these two values, their checkboxes are automatically checked and all other checkboxes are left unchecked. Now we change the selection by only selecting the first file and we see that all tags contain the correct values. The tags of the other files can be verified too by selecting them one by one. When we are satisfied with the tags, we use Save (File menu or toolbar). Selecting Create Playlist from the File menu will generate a file One Hit Wonder &#8211; Let&#8217;s Tag.m3u in the directory.</p>
<h2>COMMAND REFERENCE</h2>
<h3>The GUI Elements</h3>
<p> The Kid3 GUI is separated in five sections: At the left are the file and directory listboxes, the right side contains the File, Tag 1 and Tag 2 sections. </p>
<p> <font SIZE="+1"> <code>File List</code></p>
<dl>
<dt>
<dd>
<p> The file list contains the names of all the files in the opened directory which match the selected file name filter (typically *.mp3 *.ogg *.flac *.mpc *.aac *.m4a *.m4b *.m4p *.mp4 *.mp2 *.spx *.tta *.wv *.wma *.wav *.aiff *.ape). A single or multiple files can be selected. To select no file, click into the empty area after the listbox entries. The selection determines the files which are affected by the operations which are available by using the buttons described below. </p>
<p> At the left of the names an icon can be displayed: a disc to show that the file has been modified or information about which tags are present (V1, V2, V1V2 or NO TAG, no icon is displayed if the file has not been read in yet). </p>
<p> Directories are displayed with a folder icon. If a directory is opened, its files are displayed in a hierarchical tree. By selecting files from subdirectories, operations can be executed on files in different directories, which is useful if the music collection is organized with a folder for each artist containing folders for albums of this artist. </p>
<p> Clicking the right mouse button inside the file list opens a context menu with the following commands: </p>
<dl>
<dt>
<dd> &bull; Expand all: Expands all folder trees</dl>
<dl>
<dt>
<dd> &bull; Collapse all: Collapses all folder trees</dl>
<dl>
<dt>
<dd> &bull; Rename: Changes the name of a file</dl>
<dl>
<dt>
<dd> &bull; Move to Trash: Moves a file to the trash</dl>
<dl>
<dt>
<dd> &bull; Play: Plays a file, see Play</dl>
<dl>
<dt>
<dd> &bull; The subsequent entries are user commands, which can be defined in the User Actions tab of Configure Kid3. The playback on double click can also be activated there.</dl>
</dl>
<p> </font><font SIZE="+2"> <code>Directory List</code></p>
<dl>
<dt>
<dd>
<p> The directory list contains the names of the directories in the opened directory, as well as the current (.) and the parent (..) directory. It allows to quickly change the directory without using the Open&#8230; command or drag and drop.</dl>
<p> </font><font SIZE="+3"> <code>File</code></p>
<dl>
<dt>
<dd>
<p> Shows information about the encoding (MP3, Ogg, FLAC, MPC, APE, MP2, MP4, AAC, Speex, TrueAudio, WavPack, WMA, WAV, AIFF), bit rate, sample rate, channels and the length of the file. </p>
<p> The Name line edit contains the name of the file (if only a single file is selected). If this name is changed, the file will be renamed when the Save command is used. </p>
<p> The Format combo box and line edit contains the format to be used when the filename is generated from the first or the second tag. The filename can contain arbitrary characters, even a directory part separated by a slash from the file name, but that directory must already exist for the renaming to succeed. The following special codes are used to insert tag values into the filename: </p>
<dl>
<dt>
<dd> &bull; %s %{title} Title (Song)</dl>
<dl>
<dt>
<dd> &bull; %a %{artist} Artist</dl>
<dl>
<dt>
<dd> &bull; %l %{album} Album</dl>
<dl>
<dt>
<dd> &bull; %c %{comment} Comment</dl>
<dl>
<dt>
<dd> &bull; %y %{year} Year</dl>
<dl>
<dt>
<dd> &bull; %t %{track} Track (e.g. 01)</dl>
<dl>
<dt>
<dd> &bull; %t %{track.n} Track with field width n (e.g. 001 for %{track.3})</dl>
<dl>
<dt>
<dd> &bull; %T %{tracknumber} Track (without leading zeros, e.g. 1)</dl>
<dl>
<dt>
<dd> &bull; %g %{genre} Genre</dl>
<dl>
<dt>
<dd> &bull; %{ignore} Ignored when generating tags from the file name</dl>
<p> The format codes are not restricted to the examples given above. Any frame name can be used, for instance unified frame names like <code>%{bpm}</code> or format specific names like <code>%{popm}</code>. </p>
<p> A second Format combo box (with arrow down) is used to generate the tags from the filename. If the format of the filename does not match this pattern, a few other commonly used formats are tried. </p>
<p> Some commonly used filename formats are already available in the combo box, but it is also possible to type in some special format into the line edit. </p>
<p> From:Tag 1, Tag 2: Sets the filename using the selected format and the first tag or the second tag, respectively. </p>
<p> To:Tag 1, Tag 2: The tags are set from the filename. First, the format specified in Format is used. If the existing filename does not match this format, the following formats are tried: </p>
<dl>
<dt>
<dd> &bull; Artist &#8211; Album/Track Song</dl>
<dl>
<dt>
<dd> &bull; Album/Track &#8211; Artist &#8211; Song</dl>
<dl>
<dt>
<dd> &bull; /Artist &#8211; Album &#8211; Track &#8211; Song</dl>
<dl>
<dt>
<dd> &bull; Album/Artist &#8211; Track &#8211; Song</dl>
<dl>
<dt>
<dd> &bull; Album/Artist &#8211; Song</dl>
<dl>
<dt>
<dd> &bull; Artist/Album/Track Song</dl>
<p> If a single file is selected, the GUI controls are filled with the values extracted from the filename. If multiple files are selected, the tags of the files are directly set according to the filenames.</dl>
<p> </font><font SIZE="+4"> <code>Tag 1</code></p>
<dl>
<dt>
<dd>
<p> The line edit widgets for Title, Artist, Album, Comment, Year, Track and Genre are used to edit the corresponding value in the first tag of the selected files. The value will be changed when the file selection is altered or before operations like Save and Quit and when the corresponding check box at the left of the field name is checked. This is useful to change only some values and leave the other values unchanged. </p>
<p> If a single file is selected, all check boxes are checked and the line edit widgets contain the values found in the tags of this file. If a tag is not found in the file, the corresponding empty value is displayed, which is an empty string for the Title, Artist, Album and Comment line edits, 0 for the numerical Year and Track edits and an empty selected value for the Genre combo box. The values can be changed and if the corresponding check box is checked, they will be set for the selected file after the selection is changed. The file is then marked as modified by a disk symbol in the file listbox but remains unchanged until the Save command is used. </p>
<p> If multiple files are selected, only the values which are identical in all selected files are displayed. In all other controls, the empty values as described above are displayed. All check boxes are unchecked to avoid unwanted changes. If a value has to be set for all selected files, it can be edited and the checkbox has to be set. The values will be set for all selected files when the selection is changed and can be saved using the Save command. </p>
<p> The check boxes also control the operation of most commands affecting the tags, such as copy, paste and transfer between tags 1 and 2. To make it easier to use with multiple files where all check boxes are unchecked, these commands behave in the same way when all check boxes are checked and when all check boxes are unchecked. </p>
<p> From Tag 2: The tag 1 fields are set from the corresponding values in tag 2. If a single file is selected, the GUI controls are filled with the values from tag 2. If multiple files are selected, the tags of the files are directly set. </p>
<p> Copy: The copy buffer is filled with the Tag 1 values. Only values with checked checkbox will be used in subsequent Paste commands. </p>
<p> Paste: Pastes the values from the copy buffer into the GUI controls. </p>
<p> Remove: This will set all GUI controls to their empty values which results in removing all values. The saved file will then contain no tag 1.</dl>
<p> </font><font SIZE="+5"> <code>Tag 2</code></p>
<dl>
<dt>
<dd>
<p> The GUI controls function in the same way as described for the Tag 1 section, but the size of the strings is not limited. </p>
<p> For the tag 2 Genre you can also use your own names besides the genres listed in the combo box, just type the name into the line edit. </p>
<p> The tag 2 can not only contain the same values as the tag 1, the format is built in a flexible way from several frames which are themselves composed of several fields. The tag 2 table shows all the frames which are available in the selected file. </p>
<p> Edit: This will open a window which allows to edit all fields of the selected frame. If multiple files are selected, the edited fields are applied to all selected files which contain such a frame. </p>
<p> Add: A requester to select the frame type will appear and a frame of the selected type can be edited and added to the file. This works also to add a frame to multiple selected files. </p>
<p> Delete: Deletes the selected frame in the selected files. </p>
<p> Drag album artwork here is shown if the file does not contain embedded cover art. A picture can be added using drag and drop from a browser or file manager and will be displayed here. Picture frames can be edited or added by double clicking on this control.</dl>
<p> </font></p>
<h3>The File Menu</h3>
<p> File → Open&#8230; (Ctrl+O)</p>
<dl>
<dt>
<dd> Opens a directory. All files matching the selected file name filter will be displayed in the file listbox and the chosen file is selected.</dl>
<p> File → Open Recent</p>
<dl>
<dt>
<dd> Opens a recently opened directory.</dl>
<p> File → Open Directory&#8230; (Ctrl+D)</p>
<dl>
<dt>
<dd> Opens a directory. All files matching the selected file name filter will be displayed in the file listbox.</dl>
<p> File → Save (Ctrl+S)</p>
<dl>
<dt>
<dd> Saves all changed files in the directory. The changed files are marked with a disk symbol in the file listbox. If any file names have been changed, those files will be renamed.</dl>
<p> File → Revert</p>
<dl>
<dt>
<dd> Reverts the changes of one or multiple files. If no files are selected in the file listbox, the changes of all files will be reverted, else only the changes of the selected files are reverted.</dl>
<p> File → Import&#8230;</p>
<dl>
<dt>
<dd> The Import dialog can be used to import data directly from a freedb.org server, from a MusicBrainz server, from Discogs, Amazon or other sources of album track lists in textual format. </p>
<p> Import from a freedb.org server is possible using a dialog which appears when From Server:gnudb.org or TrackType.org is selected. The artist and album name to search for can be entered in the two topmost fields, the albums which match the query will be displayed when Find is clicked and the results from m[blue]<code><a rel="nofollow" href="http://www.gnudb.org">www.gnudb.org</a></code>m[]<font SIZE="-2">[6]</font> are received. Importing the track data for an album is done by double-clicking the album in the list. The freedb.org server to import from can be selected as well as the CGI path. The imported data is displayed in the preview table of the import dialog. When satisfied with the displayed tracks, they can be imported by terminating the import dialog with OK. </p>
<p> A search on the Discogs server can be performed using Discogs. As in the gnudb.org dialog, you can enter artist and album and then choose from a list of releases. If Standard Tags is marked, the standard information is imported, e.g. artist, album, and title. If Additional Tags is marked, more information is imported if available, e.g. performers, arrangers, or the publisher. If Cover Art is marked, cover art will be downloaded if available. </p>
<p> A search on Amazon can be performed using Amazon. As in the gnudb.org dialog, you can enter artist and album and then choose from a list of releases. If Additional Tags is marked, more information is imported if available, e.g. performers, arrangers, or the publisher. If Cover Art is marked, cover art will be downloaded if available. </p>
<p> You can search in the same way in the release database of MusicBrainz using From MusicBrainz Release. The workflow is the same as described for From gnudb.org. </p>
<p> Import from a MusicBrainz server is possible using the dialog which appears when From MusicBrainz Fingerprint is selected. The Server can be selected as in the freedb import dialog. Below is a table displaying the imported track data. The right column shows the state of the MusicBrainz query, which starts with &quot;Pending&quot; when the dialog is opened. Then the fingerprint is looked up and if it does not yield a result, another lookup using the tags in the file is tried. Thus it can be helpful for a successful MusicBrainz query to store known information (e.g. artist and album) in the tags before the import. If a result was found, the search ends in the state &quot;Recognized&quot;, otherwise nothing was found or multiple ambiguous results and one of them has to be selected by the user. OK and Apply use the imported data, Cancel closes the dialog. The closing can take a while since the whole MusicBrainz machinery has to be shut down. </p>
<p> For the import of textual data, From File/Clipboard opens a subdialog, where several preconfigured import formats are available. The first two, &quot;CSV unquoted&quot; and &quot;CSV quoted&quot; can be used to import data which was exported by the Export dialog. The CSV data can be edited with a spreadsheet, and shall be written using tabs as delimiters. Import should then be possible using &quot;CSV quoted&quot;, which is more flexible than &quot;CSV unquoted&quot;. However, its fields cannot contain any double quotes. If you only export from Kid3 and import later, &quot;CSV unquoted&quot; can be used as a simple format for this purpose. </p>
<p> The next format, &quot;freedb HTML text&quot;, can be used to copy information from an HTML page of m[blue]<code>freedb.org</code>m[]<font SIZE="-2">[7]</font>. Search an album in freedb and if the desired information is displayed in the web browser, copy the contents to the clipboard. Then click the From Clipboard button and the imported tracks will be displayed in the preview table at the top of the dialog. If you are satisfied with the imported data, terminate the dialog with OK, which will insert the data into the tags of the current directory. The destination (Tag 1, Tag 2 or Tag 1 and Tag 2) can be selected with a combo box. The files in the current directory should be in the correct track order to get their tags assigned. This is the case if they are numbered. </p>
<p> The next preconfigured import format, &quot;freedb HTML source&quot;, can be used, if the data is available as an HTML document. Import is possible using the From File button, which opens a file selector, or copying its contents from an editor and then importing from clipboard. This format can be useful for offline import, although the HTML document could also be opened in a browser and then be imported in the first format via the clipboard. </p>
<p> More preconfigured formats, e.g. &quot;Track Title Time&quot;, are available. An empty custom format can be created with Add to be set by the user. Two lines below the format name can be set with a regular expression to capture the fields from the import text. The first regular expression will be parsed once per document to gather per-album data such as artist, album, year and genre. The second line is tried to match from the start of the document to the end to get track data, usually number and title. The regular expressions include all the features offered by Qt, which is most of the what Perl offers. Bracketing constructs &quot;(..)&quot; create capture buffers for the fields to import and are preceded by Kid3 specific codes to specify which field to capture. The codes are the same as used for the filename format, besides the codes listed below, any frame name is possible: </p>
<dl>
<dt>
<dd> &bull; %s %{title} Title (Song)</dl>
<dl>
<dt>
<dd> &bull; %a %{artist} Artist</dl>
<dl>
<dt>
<dd> &bull; %l %{album} Album</dl>
<dl>
<dt>
<dd> &bull; %c %{comment} Comment</dl>
<dl>
<dt>
<dd> &bull; %y %{year} Year</dl>
<dl>
<dt>
<dd> &bull; %t %{track} Track</dl>
<dl>
<dt>
<dd> &bull; %g %{genre} Genre</dl>
<dl>
<dt>
<dd> &bull; %d %{duration} Duration</dl>
<p> For example, a track regular expression (second line) to import from an .m3u playlist could be &quot;%{track}(\d+)\s+%{title}(\S[^
]*)\.mp3[
]&quot;. All formats can be changed by editing the regular expressions and the name and then clicking Save Settings. They will be stored in the kid3rc file in the configuration directory. This file can be directly edited to have more import formats or it can be deleted to revert to the default formats. Formats can be deleted using Remove. </p>
<p> Accuracy shows an estimation of how good the imported information matches the given tracks. It uses track durations or file names to calculate the level of similarity in percent. Cover Art shows the URL of the album cover image which will be downloaded. </p>
<p> To check whether the imported tracks match the current set of files, the duration of the imported tracks can be compared with the duration of the files. This option can be enabled with the checkbox Check maximum allowable time difference and the maximum tolerated difference in time can be set in seconds. If a mismatch in a length is detected, the length is displayed with a red background in the preview table. </p>
<p> It the files are ordered differently than the imported tracks, their assigned tracks have to be changed. This task can be facilitated using the Match with buttons Length, Track, and Title, which will reorder the tracks according to the corresponding field. To correct the assignments manually, a track can be dragged with the left mouse button and the Ctrl key hold down, and then dropped at the new location. </p>
<p> When the import dialog is opened, it contains the actual contents of the tags. The tag type (Tag 1, Tag 2, Tag 1 and Tag 2) can be selected using the Destination combo box. The button on the right of this combo box can be used to revert the table to the current contents of the tags. The checkboxes in the first table column can be used to select the tracks which are imported. This can be useful if a folder contains the tracks of both CDs of a double CD and only the tracks of the second CD have to be imported. </p>
<p> To identify the tracks which are imported, it is possible to display the file names or the full paths to the files using the context menu of the table header. The values in the import table can be edited. The revert-button to the right of the Destination combo box can be used to restore the contents of the tags, which can also be useful after changing the Destination. </p>
<p> Almost all dialogs feature a Save Settings button, which can be used to store the dialog specific settings and the window size persistently. </p>
<p> From Tags leads to a subdialog to set tag frames from the contents of other tag frames. This can be used to simply copy information between tags or extract a part from one frame and insert it in another. </p>
<p> As in the import from file/clipboard, there are freely configurable formats to perform different operations. Already preconfigured are formats to copy the Album value to Album Artist, Composer or Conductor, and to extract the Track Number from Title fields which contain a number. There is also a format to extract a Subtitle from a Title field. </p>
<p> The following example explains how to add a custom format, which sets the information from the Subtitle field also in the Comment field. Create a new format using Add and set a new name, e.g. &quot;Subtitle to Comment&quot;. Then enter &quot;%{subtitle}&quot; in Source and &quot;%{comment}(.*)&quot; for Extraction and click Save Settings. </p>
<p> The expression in Source can contain format codes for arbitrary tag frames, multiple codes can be used to combine the contents from different frames. For each track, a text is generated from its tags using the Source format, and the regular expression from Extraction is applied to this text to set new values for the tags. Format codes are used before the capturing parentheses to specify the tag frame where the captured text shall be stored. It works in the same way as for the import from file/clipboard.</dl>
<p> File → Import from gnudb.org&#8230;</p>
<dl>
<dt>
<dd> Import from a freedb.org server using gnudb.org album search. This menu item opens the same import dialog as Import&#8230;, but opens directly the gnudb.org dialog.</dl>
<p> File → Import from TrackType.org&#8230;</p>
<dl>
<dt>
<dd> Import from the TrackType.org server. This menu item opens the same import dialog as Import&#8230;, but opens directly the TrackType.org dialog.</dl>
<p> File → Import from Discogs&#8230;</p>
<dl>
<dt>
<dd> Import from the Discogs server. This menu item opens the same import dialog as Import&#8230;, but opens directly the From Discogs dialog.</dl>
<p> File → Import from Amazon&#8230;</p>
<dl>
<dt>
<dd> Import from Amazon. This menu item opens the same import dialog as Import&#8230;, but opens directly the From Amazon dialog.</dl>
<p> File → Import from MusicBrainz Release&#8230;</p>
<dl>
<dt>
<dd> Import from the MusicBrainz release database. This menu item opens the same import dialog as Import&#8230;, but opens directly the From MusicBrainz Release dialog.</dl>
<p> File → Import from MusicBrainz Fingerprint&#8230;</p>
<dl>
<dt>
<dd> Import from a MusicBrainz server. This menu item opens the same import dialog as Import&#8230;, but opens directly the From MusicBrainz Fingerprint dialog.</dl>
<p> File → Automatic Import&#8230;</p>
<dl>
<dt>
<dd> Automatic Import allows to import information for multiple albums from various web services. If directories are selected in the file list, track data for the selected directories will be imported. If no directory is selected, all directories in the file list will be imported. </p>
<p> The tag type (Tag 1, Tag 2, Tag 1 and Tag 2) can be selected using the Destination combo box. </p>
<p> Profiles determine which servers will be contacted to fetch album information. Some profiles are predefined (All, MusicBrainz, Discogs, Cover Art), custom profiles can be added using the Add button at the right of the Profile combo box. </p>
<p> The table below shows the servers which will be used when importing album information using the selected profile. The import process for an album is finished if all required information has been found, so the order of the rows in the table is important. It can be changed using the Move Up and Move Down buttons. Edit can be used to change an existing entry. The Server selection offers the same servers as can be used in the import functions. Standard Tags, Additional Tags, Cover Art determine the information which shall be fetched from the server. Finally, Accuracy is the minimum accuracy which must be achieved to accept the imported data. If the accuracy is insufficient, the next server in the list will be tried. The same dialog containing the server properties appears when Add is clicked to add a new server entry. Existing entries can be deleted using Remove. </p>
<p> To launch an automatic batch import with the selected profile, click Start. Details about the running import are displayed at the top of the dialog. The process can be aborted with the Abort button. </p>
</dl>
<p> File → Browse Cover Art&#8230;</p>
<dl>
<dt>
<dd> The Browse Cover Art dialog helps to find album cover art. Artist/Album is filled from the tags if possible. Source offers a variety of websites with album cover art. The URL with artist and album as parameters can be found beneath the name. URL-encoded values for artist and album can be inserted using <code>%u{artist}</code> and <code>%u{album}</code>, other values from the tags are possible too, as described in Configure Kid3, User Actions. More sources can be entered after the entry &quot;Custom Source&quot; by replacing &quot;Custom Source&quot; with the source&#8217;s name, pressing Enter, then inserting the URL and finally pressing Save Settings. The resulting browser command is displayed at the top of the dialog and can be started by clicking Browse. The browser, which can be configured in the settings, is started with the selected source. A cover image can then be dragged from the browser into the Kid3 window and will be set in the picture frame of the selected files. </p>
<p> Because not all browsers support drag&#8217;n&#8217;drop of images and the pictures on websites often have a URL, in such cases Kid3 will receive the URL and not the picture. If the URL points to a picture, it will be downloaded. However, if the URL refers to some other web resource, it has to be translated to the corresponding picture. Such mappings are defined in the table URL extraction. The left column Match contains a regular expression which is compared with the URL. If it matches, the captured expressions in parentheses are inserted into the pattern of the right Picture URL column (at the positions marked with \1 etc.). The replaced regular expression contains the URL of the picture. By this means cover art can be imported from Amazon, Google Images, etc. using drag&#8217;n&#8217;drop. It is also possible to define your own mappings.</dl>
<p> File → Export&#8230;</p>
<dl>
<dt>
<dd> The Export Dialog is used to store data from the tags in a file or the clipboard. The editor at the top shows a preview of the data to export. If the export data contain tabulator characters, the export is displayed in a table. The data will be generated from the tags in the current directory according to the configured format. </p>
<p> The format settings are similar as in the Import dialog: The topmost field contains the title (e.g. &quot;CSV unquoted&quot;), followed by the header, which will be generated at the begin of the file. The track data follows; it is used for every track. Finally, the trailer can be used to generate some finishing text. </p>
<p> The format fields do not contain regular expressions as in the Import dialog, but only output format expressions with special %-expressions, which will be replaced by values from the tags. The whole thing works like the file name format, and the same codes are used plus some additional codes. Not only the codes listed below but all tag frame names can be used. </p>
<dl>
<dt>
<dd> &bull; %s %{title} Title (Song)</dl>
<dl>
<dt>
<dd> &bull; %a %{artist} Artist</dl>
<dl>
<dt>
<dd> &bull; %l %{album} Album</dl>
<dl>
<dt>
<dd> &bull; %c %{comment} Comment</dl>
<dl>
<dt>
<dd> &bull; %y %{year} Year</dl>
<dl>
<dt>
<dd> &bull; %t %{track} Track (e.g. 01)</dl>
<dl>
<dt>
<dd> &bull; %t %{track.n} Track with field width n (e.g. 001 for %{track.3})</dl>
<dl>
<dt>
<dd> &bull; %T %{tracknumber} Track (without leading zeros, e.g. 1)</dl>
<dl>
<dt>
<dd> &bull; %g %{genre} Genre</dl>
<dl>
<dt>
<dd> &bull; %f %{file} File name</dl>
<dl>
<dt>
<dd> &bull; %p %{filepath} Path</dl>
<dl>
<dt>
<dd> &bull; %u %{url} URL</dl>
<dl>
<dt>
<dd> &bull; %d %{duration} Duration in minutes:seconds</dl>
<dl>
<dt>
<dd> &bull; %D %{seconds} Duration in seconds</dl>
<dl>
<dt>
<dd> &bull; %n %{tracks} Number of tracks of the album</dl>
<dl>
<dt>
<dd> &bull; %e %{extension} File extension</dl>
<dl>
<dt>
<dd> &bull; %O %{tag1} The format of tag 1 (ID3v1.1 or empty if not existing)</dl>
<dl>
<dt>
<dd> &bull; %o %{tag2} The format of tag 2 (ID3v2.3.0, ID3v2.4.0, ID3v2.2.0, ID3v2.2.1, Vorbis, APE, MP4, ASF, or empty if not existing)</dl>
<dl>
<dt>
<dd> &bull; %b %{bitrate} Bit rate in kbit/s</dl>
<dl>
<dt>
<dd> &bull; %v %{vbr} VBR or empty (only for ID3v2.3 with id3lib)</dl>
<dl>
<dt>
<dd> &bull; %r %{samplerate} Sample rate in Hz</dl>
<dl>
<dt>
<dd> &bull; %m %{mode} Channel mode (Stereo or Joint Stereo)</dl>
<dl>
<dt>
<dd> &bull; %h %{channels} Number of channels (1 or 2)</dl>
<dl>
<dt>
<dd> &bull; %k %{codec} Codec (e.g. MPEG 1 Layer 3, MP4, Ogg Vorbis, FLAC, MPC, APE, ASF, AIFF, WAV)</dl>
<p> A few formats are predefined. &quot;CSV unquoted&quot; separates the fields by tabs. Data in this format can be imported again into Kid3 using the import format with the same name. &quot;CSV quoted&quot; additionally encloses the fields by double quotes, which eases the import into spreadsheet applications. However, the fields shall not contain any double quotes when this format is used. &quot;Extended M3U&quot; and &quot;Extended PLS&quot; generate playlists with extended attributes and absolute path names. &quot;HTML&quot; can be used to generate an HTML page with hyperlinks to the tracks. &quot;Kover XML&quot; creates a file which can be imported by the cover printing program Kover. &quot;Technical Details&quot; provides information about bit rate, sample rate, channels, etc. Finally, &quot;Custom Format&quot; is left empty for definition of a custom format. You can define more formats of your own by adding lines in the file kid3rc in the configuration directory. The other formats can be adapted to your needs. </p>
<p> The source of the tags to generate the export data (Tag 1 or Tag 2) can be selected with a combo box. Pushing To File or To Clipboard stores the data in a file or on the clipboard. OK and Cancel close the dialog, whereas OK accepts the current dialog settings.</dl>
<p> File → Create Playlist</p>
<dl>
<dt>
<dd> Creates a playlist. The format and contents of the playlist can be set by various options. </p>
<p> The name of the playlist can be the Same as directory name or use a Format with values from the tags, e.g. &quot;%{artist} &#8211; %{album}&quot; to have the artist and album name in the playlist file name. The format codes are the same as for Export. The extension depends on the playlist format. </p>
<p> The location of the generated playlist is determined by the selection of the Create in combo box. </p>
<p> Current directory</p>
<dl>
<dt>
<dd> The playlist is created in the current directory and contains only files of the current directory.</dl>
<p> Every directory</p>
<dl>
<dt>
<dd> A playlist is created in every directory which contains listed files, and each playlist contains the files of that directory.</dl>
<p> Top-level directory</p>
<dl>
<dt>
<dd> Only one playlist is created in the top-level directory (i.e. the directory of the file list) and it contains the listed files of the top-level directory and all of its sub-directories.</dl>
<p> The Format of the playlist can be M3U, PLS or XSPF. </p>
<p> If Include only the selected files is checked, only the selected files will be included in the playlist. If a directory is selected, all of its files are selected. If this check box is not activated, all audio files are included in the playlist. </p>
<p> Sort by file name selects the usual case where the files are ordered by file name. With Sort by tag field, it is possible to sort by a format string with values from tag fields. For instance, &quot;%{track.3}&quot; can be used to sort by track number (the &quot;.3&quot; is used to get three digits with leading zeros because strings are used for sorting). It is also possible to use multiple fields, e.g. &quot;%{genre}%{year}&quot; to sort using a string composed of genre and year. </p>
<p> The playlist entries will have relative or absolute file paths depending on whether Use relative path for files in playlist or Use full path for files in playlist is set. </p>
<p> When Write only list of files is set, the playlist will only contain the paths to the files. To generate an extended playlist with additional information, a format string can be set using the Write info using control.</dl>
<p> File → Quit (Ctrl+Q)</p>
<dl>
<dt>
<dd> Quits the application.</dl>
<h3>The Edit Menu</h3>
<p> Edit → Select All (Alt+A)</p>
<dl>
<dt>
<dd> Selects all files.</dl>
<p> Edit → Deselect (Ctrl+Shift+A)</p>
<dl>
<dt>
<dd> Deselects all files.</dl>
<p> Edit → Select All in Directory</p>
<dl>
<dt>
<dd> Selects all files of the current directory.</dl>
<p> Edit → Previous File (Alt+Up)</p>
<dl>
<dt>
<dd> Selects the previous file.</dl>
<p> Edit → Next File (Alt+Down)</p>
<dl>
<dt>
<dd> Selects the next file.</dl>
<h3>The Tools Menu</h3>
<p> Tools → Apply Filename Format</p>
<dl>
<dt>
<dd> When Format while editing is switched off for the filename format in the configuration dialog, this menu item can be used to apply the configured format to the names of the selected files. This can also be used to check whether the file names conform with the configured format by applying the format to all saved files and then checking if any files were changed (and therefore marked with a disk symbol in the file listbox).</dl>
<p> Tools → Apply Tag Format</p>
<dl>
<dt>
<dd> When Format while editing is switched off for the tag format in the configuration dialog, this menu item can be used to apply the configured format to the tags of the selected files. This can also be used to check whether the tags conform with the configured format by applying the format to all saved files and then checking if any files were changed (and therefore marked with a disk symbol in the file listbox).</dl>
<p> Tools → Apply Text Encoding</p>
<dl>
<dt>
<dd> Sets the Text encoding selected in Settings/Configure Kid3&#8230;/Tags/Tag 2 for all selected files. If UTF8 is selected, UTF16 will be used for ID3v2.3.0 tags because UTF8 is not supported for this format.</dl>
<p> Tools → Rename Directory&#8230;</p>
<dl>
<dt>
<dd> This dialog offers the possibility to automatically rename the currently open directory according to the tags in the files. Several formats are preconfigured to include information about artist, album and year in the directory name. It is also possible to set a custom format, the following special codes are used to insert tag values into the directory name: </p>
<dl>
<dt>
<dd> &bull; %s %{title} Title (Song)</dl>
<dl>
<dt>
<dd> &bull; %a %{artist} Artist</dl>
<dl>
<dt>
<dd> &bull; %l %{album} Album</dl>
<dl>
<dt>
<dd> &bull; %c %{comment} Comment</dl>
<dl>
<dt>
<dd> &bull; %y %{year} Year</dl>
<dl>
<dt>
<dd> &bull; %t %{track} Track (e.g. 01)</dl>
<dl>
<dt>
<dd> &bull; %t %{track.n} Track with field width n (e.g. 001 for %{track.3})</dl>
<dl>
<dt>
<dd> &bull; %T %{tracknumber} Track (without leading zeros, e.g. 1)</dl>
<dl>
<dt>
<dd> &bull; %g %{genre} Genre</dl>
<p> If a directory separator &quot;/&quot; is found in the format, multiple directories are created. If you want to create a new directory instead of renaming the current directory, select Create Directory instead of Rename Directory. The source of the tag information can be chosen between From Tag 1 and Tag 2, From Tag 1 and From Tag 2. A preview for the rename operation performed on the first file can be seen in the From and To sections of the dialog. </p>
<p> Multiple directories can be renamed by selecting them.</dl>
<p> Tools → Number Tracks&#8230;</p>
<dl>
<dt>
<dd> If the track numbers in the tags are not set or have the wrong values, this function can number the tracks automatically in ascending order. The start number can be set in the dialog. If only part of the tracks have to be numbered, they must be selected. </p>
<p> When Total number of tracks is checked, the number of tracks will also be set in the tags. </p>
<p> It is possible to number the tracks over multiple directories. The folders have to be expanded and selected.</dl>
<p> Tools → Filter&#8230;</p>
<dl>
<dt>
<dd> The filter can be used to display only those files which match certain criteria. This is helpful if you want to organize a large collection and only edit those files which are not in the desired scheme. The expression defining which files to display uses the same format codes which are used in the file name format, import and export. </p>
<dl>
<dt>
<dd> &bull; %s %{title} Title (Song)</dl>
<dl>
<dt>
<dd> &bull; %a %{artist} Artist</dl>
<dl>
<dt>
<dd> &bull; %l %{album} Album</dl>
<dl>
<dt>
<dd> &bull; %c %{comment} Comment</dl>
<dl>
<dt>
<dd> &bull; %y %{year} Year</dl>
<dl>
<dt>
<dd> &bull; %t %{track} Track (e.g. 01)</dl>
<dl>
<dt>
<dd> &bull; %t %{track.n} Track with field width n (e.g. 001 for %{track.3})</dl>
<dl>
<dt>
<dd> &bull; %T %{tracknumber} Track (without leading zeros, e.g. 1)</dl>
<dl>
<dt>
<dd> &bull; %g %{genre} Genre</dl>
<dl>
<dt>
<dd> &bull; %f %{file} File name</dl>
<dl>
<dt>
<dd> &bull; %p %{filepath} Absolute path to file</dl>
<dl>
<dt>
<dd> &bull; %e %{extension} File extension</dl>
<dl>
<dt>
<dd> &bull; %O %{tag1} The format of tag 1 (ID3v1.1 or empty if not existing)</dl>
<dl>
<dt>
<dd> &bull; %o %{tag2} The format of tag 2 (ID3v2.3.0, ID3v2.4.0, ID3v2.2.0, ID3v2.2.1, Vorbis, APE, MP4, ASF, or empty if not existing)</dl>
<dl>
<dt>
<dd> &bull; %b %{bitrate} Bit rate in kbit/s</dl>
<dl>
<dt>
<dd> &bull; %v %{vbr} VBR or empty (only for ID3v2.3 with id3lib)</dl>
<dl>
<dt>
<dd> &bull; %r %{samplerate} Sample rate in Hz</dl>
<dl>
<dt>
<dd> &bull; %m %{mode} Channel mode (Stereo or Joint Stereo)</dl>
<dl>
<dt>
<dd> &bull; %h %{channels} Number of channels (1 or 2)</dl>
<dl>
<dt>
<dd> &bull; %k %{codec} Codec (e.g. MPEG 1 Layer 3, MP4, Ogg Vorbis, FLAC, MPC, APE, ASF, AIFF, WAV)</dl>
<dl>
<dt>
<dd> &bull; %1a %1{artist}, &#8230; Use the prefix 1 to get values of tag 1</dl>
<dl>
<dt>
<dd> &bull; %2a %2{artist}, &#8230; Use the prefix 2 to get values of tag 2</dl>
<p> These codes are replaced with the values for the file, and the resulting strings can be compared with the following operations: </p>
<dl>
<dt>
<dd> &bull; s1 equals s2: true if s1 and s2 are equal.</dl>
<dl>
<dt>
<dd> &bull; s1 contains s2: true if s1 contains s2, i.e. s2 is a substring of s1.</dl>
<dl>
<dt>
<dd> &bull; s matches re: true if s matches the regular expression re.</dl>
<p> True expressions are replaced by 1, false by 0. True values are represented by 1, true, on and yes, false values by 0, false, off and no. Boolean operations are not, and, or (in this order of precedence) and can be grouped by parentheses. </p>
<p> Some filter rules are predefined and can serve as examples for your own expressions: </p>
<p> All</p>
<dl>
<dt>
<dd> When the file list is filtered &#8211; this is shown by &quot;[filtered]&quot; in the window title &#8211; and all files shall be displayed again, the filtering can be reverted using this filter. It uses an empty expression, but a true value would have the same effect.</dl>
<p> Filename Tag Mismatch</p>
<dl>
<dt>
<dd> <code> not (%{filepath} contains &quot;%{artist} &#8211; %{album}/%{track} %{title}&quot;) </code> </p>
<p> Tests if the file path conforms with the file name format. This rule is automatically adapted if the file name format changes.</dl>
<p> No Tag 1</p>
<dl>
<dt>
<dd> <code> %{tag1} equals &quot;&quot; </code> </p>
<p> Displays only files which do not have a tag 1.</dl>
<p> No Tag 2</p>
<dl>
<dt>
<dd> <code> %{tag2} equals &quot;&quot; </code> </p>
<p> Displays only files which do not have a tag 2.</dl>
<p> ID3v2.3.0 Tag</p>
<dl>
<dt>
<dd> <code> %{tag2} equals &quot;ID3v2.3.0&quot; </code> </p>
<p> Displays only files which have an ID3v2.3.0 tag.</dl>
<p> ID3v2.4.0 Tag</p>
<dl>
<dt>
<dd> <code> %{tag2} equals &quot;ID3v2.4.0&quot; </code> </p>
<p> Displays only files which have an ID3v2.4.0 tag.</dl>
<p> Tag 1 != Tag 2</p>
<dl>
<dt>
<dd> <code> not (%1{title} equals %2{title} and %1{album} equals %2{album} and %1{artist} equals %2{artist} and %1{comment} equals %2{comment} and %1{year} equals %2{year} and %1{track} equals %2{track} and %1{genre} equals %2{genre}) </code> </p>
<p> Displays files with differences between tag 1 and tag2.</dl>
<p> Tag 1 == Tag 2</p>
<dl>
<dt>
<dd> <code> %1{title} equals %2{title} and %1{album} equals %2{album} and %1{artist} equals %2{artist} and %1{comment} equals %2{comment} and %1{year} equals %2{year} and %1{track} equals %2{track} and %1{genre} equals %2{genre} </code> </p>
<p> Displays files with identical tag 1 and tag 2.</dl>
<p> Incomplete</p>
<dl>
<dt>
<dd> <code> %{title} equals &quot;&quot; or %{artist} equals &quot;&quot; or %{album} equals &quot;&quot; or %{year} equals &quot;&quot; or %{tracknumber} equals &quot;&quot; or %{genre} equals &quot;&quot; </code> </p>
<p> Displays files with empty values in the standard tags (title, artist, album, date, track number, genre).</dl>
<p> No Picture</p>
<dl>
<dt>
<dd> <code> %{picture} equals &quot;&quot; </code> </p>
<p> Displays only files which do not have a picture.</dl>
<p> Custom Filter</p>
<dl>
<dt>
<dd> To add your own filter, select this entry. For instance, if you want to have a filter for artists starting with &quot;The&quot;, replace &quot;Custom Filter&quot; with the name &quot;The Bands&quot; and press Enter. Then insert the following expression into the line edit: </p>
<p> <code> %{artist} matches &quot;The.*&quot; </code> </p>
<p> Then click Save Settings. Click Apply to filter the files. All files processed are displayed in the text view, with a &quot;+&quot; for those who match the filter and a &quot;-&quot; for the others. When finished, only the files with an artist starting with &quot;The&quot; are displayed, and the window title is marked with &quot;[filtered]&quot;.</dl>
</dl>
<p> Tools → Convert ID3v2.3 to ID3v2.4</p>
<dl>
<dt>
<dd> If there are any ID3v2.3 tags in the selected files, they will be converted to ID3v2.4 tags. Frames which are not supported by TagLib will be discarded. Only files without unsaved changes will be converted.</dl>
<p> Tools → Convert ID3v2.4 to ID3v2.3</p>
<dl>
<dt>
<dd> If there are any ID3v2.4 tags in the selected files, they will be converted to ID3v2.3 tags. Only files without unsaved changes will be converted.</dl>
<p> Tools → Play</p>
<dl>
<dt>
<dd> This opens a simple toolbar to play audio files. It contains buttons for the basic operations (Play/Pause, Stop playback, Previous Track, Next Track, Close), sliders for position and volume and a display of the current position. If multiple files are selected, the selected tracks are played, else all files will be played.</dl>
<h3>The Settings Menu</h3>
<p> Settings → Show Toolbar</p>
<dl>
<dt>
<dd> Toggles displaying of the toolbar.</dl>
<p> Settings → Show Statusbar</p>
<dl>
<dt>
<dd> Toggles displaying of the statusbar, which displays longer actions such as opening or saving a directory.</dl>
<p> Settings → Show Picture</p>
<dl>
<dt>
<dd> Toggles displaying of the album cover art preview picture.</dl>
<p> Settings → Auto Hide Tags</p>
<dl>
<dt>
<dd> Empty tags are automatically hidden if this option is active. The File, Tag 1 and Tag 2 sections can be manually collapsed and expanded by clicking on the corresponding -/+ buttons.</dl>
<p> Settings → Configure Kid3&#8230;</p>
<dl>
<dt>
<dd> Opens the configuration dialog, which consists of pages for tags, files, user actions, and network settings. </p>
<p> Tag specific options can be found on the Tags page, which is itself separated into three tabs for Tag 1, Tag 2, and Tag 1 and Tag 2. </p>
<p> If Mark truncated fields is checked, truncated ID3v1.1 fields will be marked red. The text fields of ID3v1.1 tags can only have 30 characters, the comment only 28 characters. Also the genre and track numbers are restricted, so that fields can be truncated when imported or transferred from ID3v2. Truncated fields and the file will be marked red, and the mark will be removed after the field has been edited. </p>
<p> With Text encoding for ID3v1 it is possible to set the character set used in ID3v1 tags. This encoding is supposed to be ISO-8859-1, so it is recommended to keep this default value. However, there are tags around with different encoding, so it can be set here and the ID3v1 tags can then be copied to ID3v2 which supports Unicode. </p>
<p> The check box Use track/total number of tracks format controls whether the track number field of ID3v2 tags contains simply the track number or additionally the total number of tracks in the directory. </p>
<p> When Genre as text instead of numeric string is checked, all ID3v2 genres will be stored as a text string even if there is a corresponding code for ID3v1 genres. If this option is not set, genres for which an ID3v1 code exists are stored as the number of the genre code (in parentheses for ID3v2.3). Thus the genre Metal is stored as &quot;Metal&quot; or &quot;(9)&quot; depending on this option. Genres which are not in the list of ID3v1 genres are always stored as a text string. The purpose of this option is improved compatibility with devices which do not correctly interpret genre codes. </p>
<p> Text encoding defines the default encoding used for ID3v2 frames and can be set to ISO-8859-1, UTF16, or UTF8. UTF8 is not valid for ID3v2.3.0 frames; if it is set, UTF16 will be used instead. For ID3v2.4.0 frames, all three encodings are possible. </p>
<p> Version used for new tags determines whether new ID3v2 tags are created as version 2.3.0 or 2.4.0. In the first case, id3lib is used as it was in earlier versions of Kid3 and TagLib is only applied when an ID3v2.4.0 tag is encountered. In the second case, ID3v2.4.0 (TagLib), TagLib is generally used for MP3 files; changed or newly created tags will then be saved in version 2.4.0. When ID3v2.3.0 (TagLib) is selected, TagLib is also used for ID3v2.3.0 tags. </p>
<p> Track number digits is the number of digits in Track Number fields. Leading zeros are used to pad. For instance, with a value of 2 the track number 5 is set as &quot;05&quot;. </p>
<p> The combo box Comment field name is only relevant for Ogg/Vorbis and FLAC files and sets the name of the field used for comments. Different applications seem to use different names, &quot;COMMENT&quot; for instance is used by xmms, whereas amaroK uses &quot;DESCRIPTION&quot;. </p>
<p> The format of pictures in Ogg/Vorbis files is determined by Picture field name, which can be METADATA_BLOCK_PICTURE or COVERART. The first is the official standard and uses the same format as pictures in FLAC tags. COVERART is an earlier unofficial way to include pictures in Vorbis comments. It can be used for compatibility with legacy players. </p>
<p> Custom Genres can be used to define genres which are not available in the standard genre list, e.g. &quot;Gothic Metal&quot;. Such custom genres will appear in the Genre combo box of Tag 2. For ID3v1.1 tags, only the predefined genres can be used. </p>
<p> The list of custom genres can also be used to reduce the number of genres available in the Genre combo box to those typically used. If your collection mostly contains music in the genres Metal, Gothic Metal, Ancient and Hard Rock, you can enter those genres and mark Show only custom genres. The Tag 2Genre combo box will then only contain those four genres and you will not have to search through the complete genres list for them. In this example, only Metal and Hard Rock will be listed in the tag 1 genres list, because those two custom genres entries are standard genres. If Show only custom genres is not active, the custom genres can be found at the end of the genres list. </p>
<p> Quick Access Tags defines which frame types are always shown in the Tag 2 section. Such frames can then be added without first using the Add button. </p>
<p> Tag Format contains options for the format of the tags. When Format while editing is checked, the format configuration is automatically used while editing text in the line edits. The Case conversion can be set to No changes, All lowercase, All uppercase, First letter uppercase or All first letters uppercase. To use locale-aware conversion between lowercase and uppercase characters, a locale can be selected in the combobox below. The string replacement list can be set to arbitrary string mappings. To add a new mapping, select the From cell of a row and insert the text to replace, then go to the To column and enter the replacement text. To remove a mapping set the From cell to an empty value (e.g. by first typing space and then backspace). Inserting and deleting rows is also possible using a context menu which appears when the right mouse button is clicked. Replacement is only active, if the String replacement checkbox is checked. </p>
<p> On the page Files the check box Load last-opened files can be marked so that Kid3 will open and select the last selected file when it is started the next time. Preserve file timestamp can be checked to preserve the file modification time stamp. Filename for cover sets the name which is suggested when an embedded image is exported to a file. </p>
<p> If Mark changes is active, changed fields are marked with a light gray label background. </p>
<p> Filename Format contains options for the format of the filenames. The same options as in Tag Format are available. </p>
<p> The User Actions page contains a table with the commands which are available in the context menu of the file list. For critical operations such as deleting files, it is advisable to mark Confirm to pop up a confirmation dialog before executing the command. Output can be marked to see the output written by console commands (standard output and standard error). Name is the name displayed in the context menu. Command is the command line to be executed. Arguments can be passed using the following codes: </p>
<dl>
<dt>
<dd> &bull; %F %{files} File paths (a list if multiple files selected)</dl>
<dl>
<dt>
<dd> &bull; %f %{file} File path to single file</dl>
<dl>
<dt>
<dd> &bull; %uF %{urls} URLs (a list if multiple files selected)</dl>
<dl>
<dt>
<dd> &bull; %uf %{url} URL to single file</dl>
<dl>
<dt>
<dd> &bull; %d %{directory} Directory</dl>
<dl>
<dt>
<dd> &bull; %s %{title} Title (Song)</dl>
<dl>
<dt>
<dd> &bull; %a %{artist} Artist</dl>
<dl>
<dt>
<dd> &bull; %l %{album} Album</dl>
<dl>
<dt>
<dd> &bull; %c %{comment} Comment</dl>
<dl>
<dt>
<dd> &bull; %y %{year} Year</dl>
<dl>
<dt>
<dd> &bull; %t %{track} Track (e.g. 01)</dl>
<dl>
<dt>
<dd> &bull; %t %{track.n} Track with field width n (e.g. 001 for %{track.3})</dl>
<dl>
<dt>
<dd> &bull; %T %{tracknumber} Track (without leading zeros, e.g. 1)</dl>
<dl>
<dt>
<dd> &bull; %g %{genre} Genre</dl>
<dl>
<dt>
<dd> &bull; %b %{browser} Command to start the web browser</dl>
<p> The command which will be inserted with %{browser} can be defined in the Web browser line edit above. Commands starting with %{browser} can be used to fetch information about the audio files from the web, for instance </p>
<dl>
<dt>
<dd>
<pre><code>
% {browser} http: // lyricwiki.org/%u{artist}:%u{title}
</code></pre>
</dl>
<p> will query the lyrics for the current song in m[blue]<code>LyricWiki</code>m[]<font SIZE="-2">[8]</font>. The &quot;u&quot; in %u{artist} and %u{title} is used to URL-encode the artist %{artist} and song %{title} information. It is easy to define your own queries in the same way, e.g. an image search with m[blue]<code>Google</code>m[]<font SIZE="-2">[9]</font>: </p>
<dl>
<dt>
<dd>
% {browser} http: // images.google.com/images?q=%u{artist}%20%u{album}
</dl>
<p> To add album cover art to tag 2, you can search for images with Google or Amazon using the commands described above. The picture can be added to the tag with drag and drop. You can also add an image with Add, then select the Picture frame and import an image file or paste from the clipboard. Picture frames are supported for ID3v2, MP4, FLAC, Ogg and ASF tags. </p>
<p> To add and delete entries in the table, a context menu can be used. </p>
<p> The Network page contains only a field to insert the proxy address and optionally the port, separated by a colon. The proxy will be used when importing from an Internet server when the checkbox is checked. </p>
<p> In the Plugins page, available plugins can be enabled or disabled. The plugins are separated into two sections. The Metadata Plugins &amp; Priority list contains plugins which support audio file formats. The order of the plugins is important because they are tried from top to bottom. Some formats are supported by multiple plugins, so files will be opened with the first plugin supporting them. The TaglibMetadata supports most formats, if it is at the top of the list, it will open most of the files. If you want to use a different plugin for a file format, make sure that it is listed before the TaglibMetadata plugin. Details about the metadata plugin and why you may want to use them instead of TagLib are listed below. </p>
<dl>
<dt>
<dd> &bull; Id3libMetadata: Uses m[blue]<code>id3lib</code>m[]<font SIZE="-2">[10]</font> for ID3v1.1 and ID3v2.3 tags in MP3, MP2, AAC files. Supports a few more frame types than TagLib. Another reason to use it is that TagLib only supports ID3v2.3 since version 1.8.</dl>
<dl>
<dt>
<dd> &bull; OggFlacMetadata: Uses m[blue]<code>libogg</code>m[]<font SIZE="-2">[11]</font>, m[blue]<code>libvorbis, libvorbisfile</code>m[]<font SIZE="-2">[12]</font> for Ogg files, and additionally m[blue]<code>libFLAC++ and libFLAC</code>m[]<font SIZE="-2">[13]</font> for FLAC files. Reasons to use them are pictures in Ogg files, which are not supported by TagLib and that these are the official libraries for these formats.</dl>
<dl>
<dt>
<dd> &bull; TaglibMetadata: Uses m[blue]<code>TagLib</code>m[]<font SIZE="-2">[14]</font> which supports a lot of audio file formats. Since version 1.8, it also supports ID3v2.3, so it can be used for all audio files supported by Kid3.</dl>
<dl>
<dt>
<dd> &bull; Mp4v2Metadata: m[blue]<code>mp4v2</code>m[]<font SIZE="-2">[15]</font> was originally used by Kid3 to support M4A files. However, newer versions of TagLib provide good M4A support, so this plugin is not built by default.</dl>
<p> The Available Plugins section lists the remaining plugins. Their order is not important, but they can be enabled or disabled using the check boxes. </p>
<dl>
<dt>
<dd> &bull; AmazonImport: Used for the Import from Amazon&#8230; function.</dl>
<dl>
<dt>
<dd> &bull; DiscogsImport: Used for the Import from Discogs&#8230; function.</dl>
<dl>
<dt>
<dd> &bull; FreedbImport: Used for the Import from gnudb.org&#8230; and Import from TrackType.org&#8230; functions.</dl>
<dl>
<dt>
<dd> &bull; MusicBrainzImport: Used for the Import from MusicBrainz Release&#8230; function.</dl>
<dl>
<dt>
<dd> &bull; AcoustidImport: Used for the Import from MusicBrainz Fingerprint&#8230; function, which depends on the m[blue]<code>Chromaprint</code>m[]<font SIZE="-2">[16]</font> and m[blue]<code>libav</code>m[]<font SIZE="-2">[17]</font> libraries.</dl>
<p> Plugins which are disabled will not be loaded. This can be used to optimize resource usage and startup time. The settings on this page take only effect after a restart of Kid3.</dl>
<p> Settings → Configure Shortcuts&#8230;</p>
<dl>
<dt>
<dd> Opens a dialog to assign keyboard shortcuts for most of the program functions. There are even functions without corresponding menu or button available, e.g. next file, previous file, select all. </p>
</dl>
<h3>The Help Menu</h3>
<p> Help → Kid3 Handbook</p>
<dl>
<dt>
<dd> Opens this handbook.</dl>
<p> Help → About Kid3</p>
<dl>
<dt>
<dd> Displays a short information about Kid3;.</dl>
<h2>KID3-CLI</h2>
<h3>Commands</h3>
<p> <code>kid3-cli</code> offers a command-line-interface for Kid3. If a directory path is used, the directory is opened. If one or more file paths are given, the common directory is opened and the files are selected. Subsequent commands will then work on these files. Commands are specified using <code>-c</code> options. If multiple commands are passed, they are executed in the given order. If files are modified by the commands, they will be saved at the end. If no command options are passed, <code>kid3-cli</code> starts in interactive mode. Commands can be entered and will operate on the current selection. The following sections list all available commands. </p>
<p> <font SIZE="+1"> <code>Help</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>help</code> [<i>COMMAND-NAME</i>]</dl>
<dd>Displays help about the parameters of <i>COMMAND-NAME</i> or about all commands if no command name is given.</dl>
<p> </font><font SIZE="+2"> <code>Quit application</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>exit</code> [force]</dl>
<dd>Exit application. If there are modified unsaved files, the <i>force</i> parameter is required.</dl>
<p> </font><font SIZE="+3"> <code>Change directory</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>cd</code> [<i>DIRECTORY</i>]</dl>
<dd>If no <i>DIRECTORY</i> is given, change to the home directory. If a directory is given, change into the directory. If one or more file paths are given, change to their common directory and select the files.</dl>
<p> </font><font SIZE="+4"> <code>Print the current working directory</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>pwd</code></dl>
<dd>Print the filename of the current working directory.</dl>
<p> </font><font SIZE="+5"> <code>Directory list</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>ls</code></dl>
<dd>List the contents of the current directory. This corresponds to the file list in the Kid3 GUI. Four characters before the file names show the state of the file. </p>
<dl>
<dt>
<dd> &bull; &gt; File is selected.</dl>
<dl>
<dt>
<dd> &bull; * File is modified.</dl>
<dl>
<dt>
<dd> &bull; 1 File has a tag 1, otherwise &#8216;-&#8216; is displayed.</dl>
<dl>
<dt>
<dd> &bull; 2 File has a tag 2, otherwise &#8216;-&#8216; is displayed.</dl>
<dl>
<dt>
<dd> </font></p>
<pre>
kid3-cli&gt; <code>ls</code>
  1- 01 Intro.mp3
&gt; 12 02 We Only Got This One.mp3
 *1- 03 Outro.mp3
</pre>
</dl>
<p> In this example, all files have a tag 1, the second file also has a tag 2 and it is selected. The third file is modified.</dl>
<p> <font SIZE="+1"> <code>Save the changed files</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>save</code></dl>
</dl>
<dd> </font><font SIZE="+2"> <code>Select file</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>select</code> [all | none | first | previous | next | <i>FILE</i>&#8230;]</dl>
<dd>To select all files, enter <code>select all</code>, to deselect all files, enter <code>select none</code>. To traverse the files in the current directory start with <code>select first</code>, then go forward using <code>select next</code> or backward using <code>select previous</code>. Specific files can be added to the current selection by giving their file names. Wildcards are possible, so <code>select *.mp3</code> will select all MP3 files in the current directory. </p>
<dl>
<dt>
<dd> </font></p>
<pre>
kid3-cli&gt; <code>select first</code>
kid3-cli&gt; <code>ls</code>
&gt; 1- 01 Intro.mp3
  12 02 We Only Got This One.mp3
 *1- 03 Outro.mp3
kid3-cli&gt; <code>select next</code>
kid3-cli&gt; <code>ls</code>
  1- 01 Intro.mp3
&gt; 12 02 We Only Got This One.mp3
 *1- 03 Outro.mp3
kid3-cli&gt; <code>select *.mp3</code>
kid3-cli&gt; <code>ls</code>
&gt; 1- 01 Intro.mp3
&gt; 12 02 We Only Got This One.mp3
&gt;*1- 03 Outro.mp3
</pre>
</dl>
</dl>
<p> <font SIZE="+1"> <code>Select tag</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>tag</code> [<i>TAG-NUMBERS</i>]</dl>
<dd>Many commands have an optional <i>TAG-NUMBERS</i> parameter, which specifies whether the command operates on tag 1 or tag 2. If this parameter is omitted, the default tag numbers are used, which can be set by this command. At startup, is is set to 12 which means that information is read from tag 2 if available, else from tag 1; modifications are done on tag 2. The <i>TAG-NUMBERS</i> can be set to <code>1</code> or <code>2</code> to operate only on the corresponding tag. If the parameter is omitted, the current setting is displayed.</dl>
<p> </font><font SIZE="+2"> <code>Get tag frame</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>get</code> [all | <i>FRAME-NAME</i>] [<i>TAG-NUMBERS</i>]</dl>
<dd>This command can be used to read the value of a specific tag frame or get information about all tag frames (if the argument is omitted or <code>all</code> is used). Modified frames are marked with a &#8216;*&#8217;. </p>
<dl>
<dt>
<dd> </font></p>
<pre>
kid3-cli&gt; <code>get</code>
File: MPEG 1 Layer 3 192 kbps 44100 Hz Joint Stereo
  Name: 01 Intro.mp3
Tag 1: ID3v1.1
  Title         Intro
  Artist        One Hit Wonder
  Album         Let's Tag
  Date          2013
  Track Number  1
  Genre         Pop
kid3-cli&gt; <code>get title</code>
Intro
</pre>
</dl>
</dl>
<p> <font SIZE="+1"> <code>Set tag frame</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>set</code> {<i>FRAME-NAME</i>} {<i>FRAME-VALUE</i>} [<i>TAG-NUMBERS</i>]</dl>
<dd>This command sets the value of a specific tag frame. </p>
<dl>
<dt>
<dd> </font></p>
<pre>
kid3-cli&gt; <code>set remixer &quot;O.H. Wonder&quot;</code>
</pre>
</dl>
<p> To set the contents of a picture frame from a file, use </p>
<dl>
<dt>
<dd>
<pre>
<code>set picture:&quot;/path/to/folder.jpg&quot; &quot;Picture Description&quot;</code>
</pre>
</dl>
</dl>
<p> <font SIZE="+1"> <code>Revert</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>revert</code></dl>
<dd>Revert all modifications in the selected files (or all files if no files are selected).</dl>
<p> </font><font SIZE="+2"> <code>Import from file or clipboard</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>import</code> {<i>FILE</i>} {<i>FORMAT-NAME</i>} [<i>TAG-NUMBERS</i>]</dl>
<dd>Tags are imported from the file <i>FILE</i> (or from the clipboard if <code>clipboard</code> is used for <i>FILE</i>) in the format with the name <i>FORMAT-NAME</i> (e.g. <code>&quot;CSV unquoted&quot;</code>, see Import).</dl>
<p> </font><font SIZE="+3"> <code>Automatic import</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>autoimport</code> [<i>PROFILE-NAME</i>] [<i>TAG-NUMBERS</i>]</dl>
<dd>Batch import using profile <i>PROFILE-NAME</i> (see Automatic Import, <code>&quot;All&quot;</code> is used if omitted).</dl>
<p> </font><font SIZE="+4"> <code>Download album cover artwork</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>albumart</code> {<i>URL</i>} [all]</dl>
<dd>Set the album artwork by downloading a picture from <i>URL</i>. The rules defined in the Browse Cover Art dialog are used to transform general URLs (e.g. from Amazon) to a picture URL. To set the album cover from a local picture file, use the set command. </p>
<dl>
<dt>
<dd> </font></p>
<pre>
kid3-cli&gt; <code>albumart
<a rel="nofollow" href="http://www.amazon.com/Versus-World-Amon-Amarth/dp/B000078DOC">http://www.amazon.com/Versus-World-Amon-Amarth/dp/B000078DOC</a></code>
</pre>
</dl>
</dl>
<p> <font SIZE="+1"> <code>Export to file or clipboard</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>export</code> {<i>FILE</i>} {<i>FORMAT-NAME</i>} [<i>TAG-NUMBERS</i>]</dl>
<dd>Tags are exported to file <i>FILE</i> (or to the clipboard if <code>clipboard</code> is used for <i>FILE</i>) in the format with the name <i>FORMAT-NAME</i> (e.g. <code>&quot;CSV unquoted&quot;</code>, see Export).</dl>
<p> </font><font SIZE="+2"> <code>Create playlist</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>playlist</code></dl>
<dd>Create playlist in the format set in the configuration, see Create Playlist.</dl>
<p> </font><font SIZE="+3"> <code>Apply filename format</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>filenameformat</code></dl>
<dd>Apply file name format set in the configuration, see Apply Filename Format.</dl>
<p> </font><font SIZE="+4"> <code>Apply tag format</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>tagformat</code></dl>
<dd>Apply tag name format set in the configuration, see Apply Tag Format.</dl>
<p> </font><font SIZE="+5"> <code>Apply text encoding</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>textencoding</code></dl>
<dd>Apply text encoding set in the configuration, see Apply Text Encoding.</dl>
<p> </font><font SIZE="+6"> <code>Rename directory</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>renamedir</code> [<i>FORMAT</i>] [create | rename | dryrun] [<i>TAG-NUMBERS</i>]</dl>
<dd>Rename or create directories from the values in the tags according to a given <i>FORMAT</i> (e.g. <code>%{artist} &#8211; %{album}</code>, see Rename Directory), if no format is given, the format defined in the Rename directory dialog is used. The default mode is <code>rename</code>; to create directories, <code>create</code> must be given explicitly. The rename actions will be performed immediately, to just see what would be done, use the <code>dryrun</code> option.</dl>
<p> </font><font SIZE="+7"> <code>Number tracks</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>numbertracks</code> [<i>TRACK-NUMBER</i>] [<i>TAG-NUMBERS</i>]</dl>
<dd>Number the selected tracks starting with <i>TRACK-NUMBER</i> (1 if omitted).</dl>
<p> </font><font SIZE="+8"> <code>Filter</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>filter</code> [<i>FILTER-NAME</i> | <i>FILTER-FORMAT</i>]</dl>
<dd>Filter the files so that only the files matching the <i>FILTER-FORMAT</i> are visible. The name of a predefined filter expression (e.g. <code>&quot;Filename Tag Mismatch&quot;</code>) can be used instead of a filter expression, see Filter. </p>
<dl>
<dt>
<dd> </font></p>
<pre>
kid3-cli&gt; <code>filter '%{title} contains &quot;tro&quot;'</code>
Started
  /home/urs/One Hit Wonder - Let's Tag
+ 01 Intro.mp3
- 02 We Only Got This One.mp3
+ 03 Outro.mp3
Finished
kid3-cli&gt; <code>ls</code>
  1- 01 Intro.mp3
  1- 03 Outro.mp3
kid3-cli&gt; <code>filter All</code>
Started
  /home/urs/One Hit Wonder - Let's Tag
+ 01 Intro.mp3
+ 02 We Only Got This One.mp3
+ 03 Outro.mp3
Finished
kid3-cli&gt; <code>ls</code>
  1- 01 Intro.mp3
  12 02 We Only Got This One.mp3
  1- 03 Outro.mp3
</pre>
</dl>
</dl>
<p> <font SIZE="+1"> <code>Convert ID3v2.3 to ID3v2.4</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>to24</code></dl>
</dl>
<dd> </font><font SIZE="+2"> <code>Convert ID3v2.4 to ID3v2.3</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>to23</code></dl>
</dl>
<dd> </font><font SIZE="+3"> <code>Filename from tag</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>fromtag</code> [<i>FORMAT</i>] [<i>TAG-NUMBERS</i>]</dl>
<dd>Set the file names of the selected files from values in the tags, for example <code>fromtag &quot;%{track} &#8211; %{title}&quot; 1</code>. If no format is specified, the format set in the GUI is used.</dl>
<p> </font><font SIZE="+4"> <code>Tag from filename</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>totag</code> [<i>FORMAT</i>] [<i>TAG-NUMBERS</i>]</dl>
<dd>Set the tag frames from the file names, for example <code>totag &quot;%{albumartist} &#8211; %{album}/%{track} %{title}&quot; 2</code>. If no format is specified, the format set in the GUI is used. If the format of the filename does not match this pattern, a few other commonly used formats are tried.</dl>
<p> </font><font SIZE="+5"> <code>Tag to other tag</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>syncto</code> {<i>TAG-NUMBER</i>}</dl>
<dd>Copy the tag frames from one tag to the other tag, e.g. to set the ID3v2 tag from the ID3v1 tag, use <code>syncto 2</code>.</dl>
<p> </font><font SIZE="+6"> <code>Copy</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>copy</code> [<i>TAG-NUMBER</i>]</dl>
<dd>Copy the tag frames of the selected file to the internal copy buffer. They can then be set on another file using the <code>paste</code> command.</dl>
<p> </font><font SIZE="+7"> <code>Paste</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>paste</code> [<i>TAG-NUMBER</i>]</dl>
<dd>Set tag frames from the contents of the <code>copy</code> buffer in the selected files.</dl>
<p> </font><font SIZE="+8"> <code>Remove</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>remove</code> [<i>TAG-NUMBER</i>]</dl>
<dd>Remove a tag.</dl>
<p> </font><font SIZE="+9"> <code>Play</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>play</code> [pause | stop | previous | next]</dl>
<dd>Start audio playback. Once it has been started, it can be controlled with the <code>pause</code> (to pause and resume), <code>stop</code>, <code>previous</code> and <code>next</code> options.</dl>
<p> </font></p>
<h3>Examples</h3>
<p> Set album cover in all files of a directory using the batch import function: </p>
<dl>
<dt>
<dd>
<pre>
<code>kid3-cli -c 'autoimport &quot;Cover Art&quot;' /path/to/dir</code>
</pre>
</dl>
<p> Remove comment frames and apply the tag format in both tags of all MP3 files of a directory: </p>
<dl>
<dt>
<dd>
<pre>
<code>kid3-cli -c 'set comment &quot;&quot; 1' -c 'set comment &quot;&quot; 2' \
-c 'tagformat 1' -c 'tagformat 2' /path/to/dir/*.mp3</code>
</pre>
</dl>
<p> Automatically import tag 2, synchronize to tag 1, set file names from tag 2 and finally create a playlist: </p>
<dl>
<dt>
<dd>
<pre>
<code>kid3-cli -c autoimport -c 'syncto 1' -c fromtag -c playlist \
  /path/to/dir/*.mp3</code>
</pre>
</dl>
<p> For all files with an ID3v2.4.0 tag, convert to ID3v2.3.0 and remove the arranger frame: </p>
<dl>
<dt>
<dd>
<pre>
<code>kid3-cli -c &quot;filter 'ID3v2.4.0 Tag'&quot; -c &quot;select all&quot; -c to23 \
  -c &quot;set arranger ''&quot; /path/to/dir</code>
</pre>
</dl>
<h2>CREDITS AND LICENSE</h2>
<p> Kid3 </p>
<p> Program written by Urs Fleisch &lt;ufleisch at users.sourceforge.net&gt; </p>
<p> m[blue]<code>FDL</code>m[]<font SIZE="-2">[18]</font> </p>
<p> m[blue]<code>GPL</code>m[]<font SIZE="-2">[19]</font></p>
<h2>INSTALLATION</h2>
<h3>How to obtain Kid3</h3>
<p> Kid3 can be found at m[blue]<code><a rel="nofollow" href="http://kid3.sourceforge.net">http://kid3.sourceforge.net</a></code>m[].</p>
<h3>Requirements</h3>
<p> Kid3 needs m[blue]<code>Qt</code>m[]<font SIZE="-2">[20]</font>. m[blue]<code>KDE</code>m[]<font SIZE="-2">[21]</font> is recommended but not necessary, as Kid3 can also be compiled as a Qt application. Kid3 can be compiled for systems where these libraries are available, e.g. for GNU/Linux, Windows and Mac OS X. To tag Ogg/Vorbis files, m[blue]<code>libogg</code>m[]<font SIZE="-2">[11]</font>, m[blue]<code>libvorbis and libvorbisfile</code>m[]<font SIZE="-2">[12]</font> are required, for FLAC files m[blue]<code>libFLAC++ and libFLAC</code>m[]<font SIZE="-2">[13]</font>. m[blue]<code>id3lib</code>m[]<font SIZE="-2">[10]</font> is used for MP3 files. These four formats are also supported by m[blue]<code>TagLib</code>m[]<font SIZE="-2">[14]</font>, which can also handle MPC, APE, MP2, Speex, TrueAudio, WavPack, WMA, WAV, AIFF files and tracker modules. To import from acoustic fingerprints, m[blue]<code>Chromaprint</code>m[]<font SIZE="-2">[16]</font> and m[blue]<code>libav</code>m[]<font SIZE="-2">[17]</font> are used. </p>
<p> Kid3 is available for most Linux distributions, Windows and Mac OS X. Links can be found on m[blue]<code><a rel="nofollow" href="http://kid3.sourceforge.net">http://kid3.sourceforge.net</a></code>m[].</p>
<h3>Compilation and Installation</h3>
<p> You can compile Kid3 with or without KDE. Without KDE, Kid3 is a simple Qt application and lacks some configuration and session features. </p>
<p> For a KDE 4 version, go into the top directory and type </p>
<dl>
<dt>
<dd>
<pre>
% <code>cmake .</code>
% <code>make</code>
% <code>make install</code>
</pre>
</dl>
<p> To compile for different versions of Qt or KDE, set the corresponding <code>cmake</code> options. </p>
<p> If not all libraries are present, Kid3 is built with reduced functionality. So you should take care to have all desired development packages installed. On the other side, <code>cmake</code>-options control which libraries are compiled in. The default is <code>-D WITH_TAGLIB:BOOL=ON -D WITH_MP4V2:BOOL=OFF -D WITH_ID3LIB:BOOL=ON -D WITH_CHROMAPRINT:BOOL=ON -D WITH_VORBIS:BOOL=ON -D WITH_FLAC:BOOL=ON </code>. These options can be disabled using <code>OFF</code>. </p>
<p> To build Kid3 as a Qt application without KDE, use the <code>cmake</code> option <code>-DWITH_APPS=Qt</code>. To build both a KDE and a Qt application, set <code>-DWITH_APPS=&quot;Qt;KDE&quot;</code>. </p>
<p> Qt 4 or Qt 5 can be used. To force the use of Qt 4, set <code>-DWITH_QT4=ON</code>, to force the use of Qt 5, set <code>-DWITH_QT5=ON</code>, if both these options are OFF (default), Qt 4 is preferred if both versions are installed. To use a specific Qt installation, set <code>-DQT_QMAKE_EXECUTABLE=/path/to/qmake</code>. </p>
<p> Generation of RPM-Packages is supported by the file kid3.spec, for Debian-Packages, the script build-deb.shis available. </p>
<p> The Qt application can also be compiled for Windows and Mac OS X. The scripts in the folders win32 and macosx can be used to build and create packages. The libraries can be installed using buildlibs.sh.</p>
<h3>Configuration</h3>
<p> With KDE, the file name filter and format, the import formats, the filename and ID3 formats, the toolbar and statusbar settings as well as the window size will be be saved in the standard location in file kid3rc. As a Qt application, this file is in .config/Kid3/Kid3.conf. On Windows, the configuration is stored in the registry.</p>
<h2>D-BUS INTERFACE</h2>
<h3>D-Bus Examples</h3>
<p> The Qt 4 and KDE 4 versions on Linux offer a D-Bus-Interface to control Kid3 by scripts. Scripts can be written in any language with D-Bus-bindings (e.g. in Python) and can be added to the User Actions to extend the functionality of Kid3. </p>
<p> The artist in tag 2 of the current file can be set to the value &quot;One Hit Wonder&quot; with the following code: </p>
<p> Shell</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
dbus-send --dest=net.sourceforge.kid3 --print-reply=literal \
/Kid3 net.sourceforge.Kid3.setFrame int32:2 string:'Artist' \
string:'One Hit Wonder'
</pre>
</dl>
<p> or easier with Qt&#8217;s <code>qdbus</code> (<code>qdbusviewer</code> can be used to explore the interface in a GUI): </p>
<dl>
<dt>
<dd>
<pre>
qdbus net.sourceforge.kid3 /Kid3 setFrame 2 Artist \
'One Hit Wonder'
</pre>
</dl>
</dl>
<p> Python</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
import dbus
kid3 = dbus.SessionBus().get_object(
  'net.sourceforge.kid3', '/Kid3')
kid3.setFrame(2, 'Artist', 'One Hit Wonder')
</pre>
</dl>
</dl>
<p> Perl</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre><code>
use Net::DBus;
$kid3 = Net::DBus-&gt;session-&gt;get_service(
                              "net.sourceforge.kid3")
            -&gt;get_object(
                "/Kid3", "net.sourceforge.Kid3");
$kid3-&gt;setFrame(2, "Artist", "One Hit Wonder");
</code></pre>
</dl>
</dl>
<h3>D-Bus API</h3>
<p> The D-Bus API is specified in net.sourceforge.Kid3.xml. The Kid3 interface has the following methods: </p>
<p> <font SIZE="+1"> <code>Open file or directory</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>boolean openDirectory(string&nbsp;<wbr></code><i>path</i><code>);</code></dl>
<p> <i>path</i></p>
<dl>
<dt>
<dd>
<dd>path to file or directory</dl>
<p> Returns true if OK.</dl>
<p> </font><font SIZE="+2"> <code>Save all modified files</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>boolean save(void);</code></dl>
<dd>Returns true if OK.</dl>
<p> </font><font SIZE="+3"> <code>Get a detailed error message provided by some methods</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>string getErrorMessage(void);</code></dl>
<dd>Returns detailed error message.</dl>
<p> </font><font SIZE="+4"> <code>Revert changes in the selected files</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>revert(void);</code></dl>
</dl>
<dd> </font><font SIZE="+5"> <code>Start an automatic batch import</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>boolean batchImport(int32&nbsp;<wbr></code><i>tagMask</i><code>, string&nbsp;<wbr></code><i>profileName</i><code>);</code></dl>
<p> <i>tagMask</i></p>
<dl>
<dt>
<dd>
<dd>tag mask (bit 0 for tag 1, bit 1 for tag 2)</dl>
<p> <i>profileName</i></p>
<dl>
<dt>
<dd> name of batch import profile to use</dl>
</dl>
<p> </font><font SIZE="+6"> <code>Import tags from a file</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>boolean importFromFile(int32&nbsp;<wbr></code><i>tagMask</i><code>, string&nbsp;<wbr></code><i>path</i><code>, int32&nbsp;<wbr></code><i>fmtIdx</i><code>);</code></dl>
<p> <i>tagMask</i></p>
<dl>
<dt>
<dd>
<dd>tag bit (1 for tag 1, 2 for tag 2)</dl>
<p> <i>path</i></p>
<dl>
<dt>
<dd> path of file</dl>
<p> <i>fmtIdx</i></p>
<dl>
<dt>
<dd> index of format</dl>
<p> Returns true if OK.</dl>
<p> </font><font SIZE="+7"> <code>Download album cover art</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>downloadAlbumArt(string&nbsp;<wbr></code><i>url</i><code>, boolean&nbsp;<wbr></code><i>allFilesInDir</i><code>);</code></dl>
<p> <i>url</i></p>
<dl>
<dt>
<dd>
<dd>URL of picture file or album art resource</dl>
<p> <i>allFilesInDir</i></p>
<dl>
<dt>
<dd> true to add the image to all files in the directory</dl>
</dl>
<p> </font><font SIZE="+8"> <code>Export tags to a file</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>boolean exportToFile(int32&nbsp;<wbr></code><i>tagMask</i><code>, string&nbsp;<wbr></code><i>path</i><code>, int32&nbsp;<wbr></code><i>fmtIdx</i><code>);</code></dl>
<p> <i>tagMask</i></p>
<dl>
<dt>
<dd>
<dd>tag bit (1 for tag 1, 2 for tag 2)</dl>
<p> <i>path</i></p>
<dl>
<dt>
<dd> path of file</dl>
<p> <i>fmtIdx</i></p>
<dl>
<dt>
<dd> index of format</dl>
<p> Returns true if OK.</dl>
<p> </font><font SIZE="+9"> <code>Create a playlist</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>boolean createPlaylist(void);</code></dl>
<dd>Returns true if OK.</dl>
<p> <code>Quit the application</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>quit(void);</code></dl>
</dl>
<dd> <code>Select all files</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>selectAll(void);</code></dl>
</dl>
<dd> <code>Deselect all files</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>deselectAll(void);</code></dl>
</dl>
<dd> <code>Set the first file as the current file</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>boolean firstFile(void);</code></dl>
<dd>Returns true if there is a first file.</dl>
<p> <code>Set the previous file as the current file</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>boolean previousFile(void);</code></dl>
<dd>Returns true if there is a previous file.</dl>
<p> <code>Set the next file as the current file</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>boolean nextFile(void);</code></dl>
<dd>Returns true if there is a next file.</dl>
<p> <code>Select the first file</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>boolean selectFirstFile(void);</code></dl>
<dd>Returns true if there is a first file.</dl>
<p> <code>Select the previous file</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>boolean selectPreviousFile(void);</code></dl>
<dd>Returns true if there is a previous file.</dl>
<p> <code>Select the next file</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>boolean selectNextFile(void);</code></dl>
<dd>Returns true if there is a next file.</dl>
<p> <code>Select the current file</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>boolean selectCurrentFile(void);</code></dl>
<dd>Returns true if there is a current file.</dl>
<p> <code>Expand or collapse the current file item if it is a directory</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>boolean expandDirectory(void);</code></dl>
<dd>A file list item is a directory if getFileName() returns a name with &#8216;/&#8217; as the last character. </p>
<p> Returns true if current file item is a directory.</dl>
<p> <code>Apply the file name format</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>applyFilenameFormat(void);</code></dl>
</dl>
<dd> <code>Apply the tag format</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>applyTagFormat(void);</code></dl>
</dl>
<dd> <code>Apply text encoding</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>applyTextEncoding(void);</code></dl>
</dl>
<dd> <code>Set the directory name from the tags</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>boolean setDirNameFromTag(int32&nbsp;<wbr></code><i>tagMask</i><code>, string&nbsp;<wbr></code><i>format</i><code>, boolean&nbsp;<wbr></code><i>create</i><code>);</code></dl>
<p> <i>tagMask</i></p>
<dl>
<dt>
<dd>
<dd>tag mask (bit 0 for tag 1, bit 1 for tag 2)</dl>
<p> <i>format</i></p>
<dl>
<dt>
<dd> directory name format</dl>
<p> <i>create</i></p>
<dl>
<dt>
<dd> true to create, false to rename</dl>
<p> Returns true if OK, else the error message is available using getErrorMessage().</dl>
<p> <code>Set subsequent track numbers in the selected files</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>numberTracks(int32&nbsp;<wbr></code><i>tagMask</i><code>, int32&nbsp;<wbr></code><i>firstTrackNr</i><code>);</code></dl>
<p> <i>tagMask</i></p>
<dl>
<dt>
<dd>
<dd>tag mask (bit 0 for tag 1, bit 1 for tag 2)</dl>
<p> <i>firstTrackNr</i></p>
<dl>
<dt>
<dd> number to use for first file</dl>
</dl>
<p> <code>Filter the files</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>filter(string&nbsp;<wbr></code><i>expression</i><code>);</code></dl>
<p> <i>expression</i></p>
<dl>
<dt>
<dd>
<dd>filter expression</dl>
</dl>
<p> <code>Convert ID3v2.3 tags to ID3v2.4</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>convertToId3v24(void);</code></dl>
</dl>
<dd> <code>Convert ID3v2.4 tags to ID3v2.3</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>convertToId3v23(void);</code></dl>
<dd>Returns true if OK.</dl>
<p> <code>Get path of directory</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>string getDirectoryName(void);</code></dl>
<dd>Returns absolute path of directory.</dl>
<p> <code>Get name of current file</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>string getFileName(void);</code></dl>
<dd>Returns true absolute file name, ends with &quot;/&quot; if it is a directory.</dl>
<p> <code>Set name of selected file</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>setFileName(string&nbsp;<wbr></code><i>name</i><code>);</code></dl>
<p> <i>name</i></p>
<dl>
<dt>
<dd>
<dd>file name</dl>
<p> The file will be renamed when the directory is saved.</dl>
<p> <code>Set format to use when setting the filename from the tags</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>setFileNameFormat(string&nbsp;<wbr></code><i>format</i><code>);</code></dl>
<p> <i>format</i></p>
<dl>
<dt>
<dd>
<dd>file name format</dl>
</dl>
<p> <code>Set the file names of the selected files from the tags</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>setFileNameFromTag(int32&nbsp;<wbr></code><i>tagMask</i><code>);</code></dl>
<p> <i>tagMask</i></p>
<dl>
<dt>
<dd>
<dd>tag bit (1 for tag 1, 2 for tag 2)</dl>
</dl>
<p> <code>Get value of frame</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>string getFrame(int32&nbsp;<wbr></code><i>tagMask</i><code>, string&nbsp;<wbr></code><i>name</i><code>);</code></dl>
<p> <i>tagMask</i></p>
<dl>
<dt>
<dd>
<dd>tag bit (1 for tag 1, 2 for tag 2)</dl>
<p> <i>name</i></p>
<dl>
<dt>
<dd> name of frame (e.g. &quot;artist&quot;)</dl>
<p> To get binary data like a picture, the name of a file to write can be added after the <i>name</i>, e.g. &quot;Picture:/path/to/file&quot;. </p>
<p> Returns value of frame.</dl>
<p> <code>Set value of frame</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>boolean setFrame(int32&nbsp;<wbr></code><i>tagMask</i><code>, string&nbsp;<wbr></code><i>name</i><code>, string&nbsp;<wbr></code><i>value</i><code>);</code></dl>
<p> <i>tagMask</i></p>
<dl>
<dt>
<dd>
<dd>tag bit (1 for tag 1, 2 for tag 2)</dl>
<p> <i>name</i></p>
<dl>
<dt>
<dd> name of frame (e.g. &quot;artist&quot;)</dl>
<p> <i>value</i></p>
<dl>
<dt>
<dd> value of frame</dl>
<p> For tag 2 (<i>tagMask</i> 2), if no frame with <i>name</i> exists, a new frame is added, if <i>value</i> is empty, the frame is deleted. To add binary data like a picture, a file can be added after the <i>name</i>, e.g. &quot;Picture:/path/to/file&quot;. </p>
<p> Returns true if OK.</dl>
<p> <code>Get all frames of a tag</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>array of string getTag(int32&nbsp;<wbr></code><i>tagMask</i><code>);</code></dl>
<p> <i>tagMask</i></p>
<dl>
<dt>
<dd>
<dd>tag bit (1 for tag 1, 2 for tag 2)</dl>
<p> Returns list with alternating frame names and values.</dl>
<p> <code>Get technical information about file</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>array of string getInformation(void);</code></dl>
<dd>Properties are Format, Bitrate, Samplerate, Channels, Duration, Channel Mode, VBR, Tag 1, Tag 2. Properties which are not available are omitted. </p>
<p> Returns list with alternating property names and values.</dl>
<p> <code>Set tag from file name</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>setTagFromFileName(int32&nbsp;<wbr></code><i>tagMask</i><code>);</code></dl>
<p> <i>tagMask</i></p>
<dl>
<dt>
<dd>
<dd>tag bit (1 for tag 1, 2 for tag 2)</dl>
</dl>
<p> <code>Set tag from other tag</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>setTagFromOtherTag(int32&nbsp;<wbr></code><i>tagMask</i><code>);</code></dl>
<p> <i>tagMask</i></p>
<dl>
<dt>
<dd>
<dd>tag bit (1 for tag 1, 2 for tag 2)</dl>
</dl>
<p> <code>Copy tag</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>copyTag(int32&nbsp;<wbr></code><i>tagMask</i><code>);</code></dl>
<p> <i>tagMask</i></p>
<dl>
<dt>
<dd>
<dd>tag bit (1 for tag 1, 2 for tag 2)</dl>
</dl>
<p> <code>Paste tag</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>pasteTag(int32&nbsp;<wbr></code><i>tagMask</i><code>);</code></dl>
<p> <i>tagMask</i></p>
<dl>
<dt>
<dd>
<dd>tag bit (1 for tag 1, 2 for tag 2)</dl>
</dl>
<p> <code>Remove tag</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>removeTag(int32&nbsp;<wbr></code><i>tagMask</i><code>);</code></dl>
<p> <i>tagMask</i></p>
<dl>
<dt>
<dd>
<dd>tag bit (1 for tag 1, 2 for tag 2)</dl>
</dl>
<p> <code>Reparse the configuration</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>reparseConfiguration(void);</code></dl>
<dd>Automated configuration changes are possible by modifying the configuration file and then reparsing the configuration.</dl>
<p> <code>Plays the selected files</code></p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>playAudio(void);</code></dl>
</dl>
<p> </font></p>
<h2>AUTHOR</h2>
<p> <code>Urs Fleisch</code> &lt;ufleisch at users.sourceforge.net&gt;</p>
<dl>
<dt>
<dd>
<dd>Software development</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2013 Urs Fleisch </p>
<p> m[blue]<code>FDL</code>m[] </p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> gnudb.org</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://gnudb.org">http://gnudb.org</a></dl>
<dt> 2.</p>
<dd> TrackType.org</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://tracktype.org">http://tracktype.org</a></dl>
<dt> 3.</p>
<dd> MusicBrainz</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://musicbrainz.org">http://musicbrainz.org</a></dl>
<dt> 4.</p>
<dd> Discogs</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://discogs.com">http://discogs.com</a></dl>
<dt> 5.</p>
<dd> Amazon</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.amazon.com">http://www.amazon.com</a></dl>
<dt> 6.</p>
<dd> <a rel="nofollow" href="http://www.gnudb.org">www.gnudb.org</a></p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.gnudb.org">http://www.gnudb.org</a></dl>
<dt> 7.</p>
<dd> freedb.org</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://freedb.org">http://freedb.org</a></dl>
<dt> 8.</p>
<dd> LyricWiki</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.lyricwiki.org">http://www.lyricwiki.org</a></dl>
<dt> 9.</p>
<dd> Google</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.google.com">http://www.google.com</a></dl>
<dt>10.</p>
<dd> id3lib</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://id3lib.sourceforge.net">http://id3lib.sourceforge.net</a></dl>
<dt>11.</p>
<dd> libogg</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://xiph.org/ogg/">http://xiph.org/ogg/</a></dl>
<dt>12.</p>
<dd> libvorbis, libvorbisfile</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://xiph.org/vorbis/">http://xiph.org/vorbis/</a></dl>
<dt>13.</p>
<dd> libFLAC++ and libFLAC</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://flac.sourceforge.net">http://flac.sourceforge.net</a></dl>
<dt>14.</p>
<dd> TagLib</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://taglib.github.io/">http://taglib.github.io/</a></dl>
<dt>15.</p>
<dd> mp4v2</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://code.google.com/p/mp4v2">http://code.google.com/p/mp4v2</a></dl>
<dt>16.</p>
<dd> Chromaprint</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://acoustid.org/chromaprint">http://acoustid.org/chromaprint</a></dl>
<dt>17.</p>
<dd> libav</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://libav.org/">http://libav.org/</a></dl>
<dt>18.</p>
<dd> FDL</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.gnu.org/licenses/licenses.html#FDL">http://www.gnu.org/licenses/licenses.html#FDL</a></dl>
<dt>19.</p>
<dd> GPL</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.gnu.org/licenses/licenses.html#GPL">http://www.gnu.org/licenses/licenses.html#GPL</a></dl>
<dt>20.</p>
<dd> Qt</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://qt-project.org/">http://qt-project.org/</a></dl>
<dt>21.</p>
<dd> KDE</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.kde.org">http://www.kde.org</a></dl>
</dl>
<h2>Index</h2>
