---
title: "gcdmaster(1)"
name: "gcdmaster"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gcdmaster/"
description: "gcdmaster – Graphical front end to cdrdao for composing audio CDs"
---

<h2>NAME</h2>
<p> gcdmaster &#8211; Graphical front end to cdrdao for composing audio CDs</p>
<h2>SYNOPSIS</h2>
<p> <code>gcdmaster</code> [<i>toc-file</i>]</p>
<h2>DESCRIPTION</h2>
<p> <i>gcdmaster</i> allows the creation of toc-files for cdrdao and can control the recording process. Its main application is the composition of audio CDs from one or more audio files. It supports PQ-channel editing, entry of meta data like ISRC codes/CD-TEXT and non destructive cut of the audio data. </p>
<p> If a <i>toc-file</i> is specified it will be read and the referenced audio data will be displayed. It is also possible to specify a &quot;.cue&quot; file. </p>
<p> The GUI periodically polls all configured CD-ROM and CD-recorder devices (see section DEVICE CONFIGURE DIALOG) to retrieve their status (ready, busy, no disk). This is done by sending a TEST UNIT READY command to the devices. Following problems may arise:</p>
<dl>
<dt>o</p>
<dd> Some devices (e.g. the Philips CDD2600) block the SCSI bus when a TEST UNIT READY is issued while it logs in a new medium. This will cause a buffer under run for all currently recording devices that are connected to the same bus.</p>
<dt>o</p>
<dd> The GUI cannot detect if a device is used by another program. It will continue to poll the device which may disturb the operation of the other program.</dl>
<p> The GUI supports recording of the same or different projects on multiple devices in parallel. However, there are some caveats and your system must meat some prerequisites:</p>
<dl>
<dt>o</p>
<dd> Under Linux a kernel version &gt;= 2.2.6 should be used. The generic SCSI device of older kernels does not support parallel access to multiple devices.</p>
<dt>o</p>
<dd> The bandwidths of the disks that contain the source data and the involved busses must be big enough to serve all recorder devices.</p>
<dt>o</p>
<dd> Some recorder devices may block the SCSI bus when the disk is ejected by the software after the burning process (e.g. the Plextor PX-R412). For this reason a warning message will be displayed if the &quot;Eject&quot; button is checked in the &quot;Record&quot; dialog. Manually ejecting a disk seems not to be a problem.</p>
<dt>o</p>
<dd> ATAPI devices supported by the &#8216;generic-mmc&#8217; driver will block the IDE bus while writing the lead-in and lead-out. Thus parallel writing with such devices connected to the same IDE channel will not work. There is a way to avoid this blocking with some ATAPI devices but it is not implemented, yet. </p>
</dl>
<h2>CONCEPTS</h2>
<p> The main idea of this GUI is to maintain a continuous stream of audio data that can be composed of several audio files. It is possible to use only portions of audio files in the audio stream which is the basic idea for the non destructive cut capability. </p>
<p> For example, if you cut out some samples in the middle of an audio file the result will be a portion that starts at the beginning of the audio file and ends at the beginning of the cut region and a second portion that starts at the end of the cut region and reaches until the end of the audio file. Of course, all of this is hidden by the GUI and you will just see the result. </p>
<p> Track and index marks are placed relatively to the continuous audio stream. It is not necessary to have a separate audio file for each track. Track/index marks can be set, moved and deleted without influencing the audio data stream. </p>
<h3>Sample Marker</h3>
<p> A sample marker serves as an insertion position for audio data. It is equivalent to the cursor of a text editor. All functions that insert audio data require a defined marker. At most one sample marker may be active at any time. </p>
<h3>Sample Selection</h3>
<p> A sample selection specifies a continuous range of audio samples. At most one sample selection may be active at any time. </p>
<h3>Track Mark</h3>
<p> A track mark specifies a point in the audio stream where the track number or the index number changes. Track marks are written as a pair of two numbers like 5.1 for track 5, index 1. Track numbers may be in the range 1..99, the valid range for index numbers is 0..99. Index 0 represents the pre-gap of a track where the track relative time counts backwards down to zero. Index 1 marks the real start of the track. This position is stored in the central toc of the CD and is used by CD players to directly jump to a track. All index numbers &gt; 2 may be used to subdivide a track but have no further effect. Some CD players may jump to such index marks. </p>
<p> Track marks may be selected to show data about a track or to perform operations on the complete track. At most one track mark may be selected at any time. </p>
<h3>Times</h3>
<p> The time is usually displayed as m:s:f.x where m represents minutes, s represents seconds (0..59), f represents frames (0..74, 1/75 second) and x stands for samples (0..587, 1/44100 second). </p>
<h2>MAIN WINDOW</h2>
<p> The main window consists of a menu bar, a sample display, a marker/selection line, a button line and a status line. </p>
<p> The title of the main window shows the current toc-file name. A &quot;(*)&quot; behind the name indicates that changes have not been saved. </p>
<h3>Menu Bar</h3>
<p> The functions that are accessible via the menu bar are described in section MENU FUNCTIONS. </p>
<h3>Sample Display</h3>
<p> The sample display provides a visual representation of the audio stream and the placed track/index markers. </p>
<p> The samples are displayed as two separate graphs for the left and right channel where the x-axis represents the time and the y-axis denotes the amplitude (linearly scaled). If a pixel represents more than 1 sample the maximum and minimum amplitude of all samples that fall within this pixel is displayed. It is possible to zoom in and out and change the displayed portion with the scroll bar. </p>
<p> The track/index markers are shown on top of the two graphs. Track marks with index 1 are represented by filled track symbol. All other track marks use a hollow track symbol. The track/index number pair is displayed on the right side of a track symbol. </p>
<p> Track marks can be selected or moved by clicking or dragging with the mouse pointer located over a track symbol. The track/index number pairs are not sensitive. </p>
<h3>Marker/Selection Line</h3>
<p> This line shows the actual cursor and active marker position and the active sample selection. </p>
<p> The cursor field is read-only and shows the time value of the actual mouse pointer position within the audio stream if it is located inside the sample display. During playback the cursor field shows the time value of currently audible sound. </p>
<p> The marker field shows the time value of the active marker. A time value may be entered and hitting the return key sets the new marker position if the time value is valid. </p>
<p> The sample selection fields show the active selected sample range. Time values may be entered and hitting the return key in one of these fields sets the new sample selection if the time values are valid. </p>
<h3>Button Line</h3>
<p> The zoom/select radio buttons specify the behavior when dragging with the mouse in the sample display. If &quot;zoom&quot; is active the sample display will zoom to selected sample range. If &quot;select&quot; is active the active sample selection will be set to the selected sample range. </p>
<p> The play button will playback the currently active sample selection via the sound card. If no sample selection is active the currently displayed sample range will be used. While playing the current project is set to read-only state and all operations that would modify the project are disabled. </p>
<h3>Status Line</h3>
<p> The status line shows more information about the last executed action or an error message if an action could not be executed. </p>
<h2>MENU FUNCTIONS</h2>
<h3>File-&gt;New</h3>
<p> Starts a new project. If the current work is not saved a confirmation box will be opened. </p>
<h3>File-&gt;Open</h3>
<p> Opens a file selector box to select a toc-file or a .cue file that should be read. If the current work is not saved a confirmation box will pop up. </p>
<h3>File-&gt;Save</h3>
<p> Saves current work as a toc-file with the current file name. </p>
<h3>File-&gt;Save As</h3>
<p> Opens a file sector box to select a toc-file to which the current work is saved. </p>
<h3>File-&gt;Quit</h3>
<p> Quits gcdmaster. If the current work is not saved a confirmation box will pop up. </p>
<h3>View-&gt;Zoom To Selection</h3>
<p> Zooms the sample display to the currently active sample selection. If no sample selection is active nothing will happen. </p>
<h3>View-&gt;Zoom out</h3>
<p> Doubles the range of displayed samples. </p>
<h3>View-&gt;Fullview</h3>
<p> Shows all samples of the audio stream in the sample display. </p>
<h3>Edit-&gt;Cut</h3>
<p> Removes the active selected sample range from the audio stream. The audio file on the disk will not be touched by this operation. The sample marker will be set so that a following &quot;Paste&quot; operation will revert the effect of this operation. </p>
<p> If no sample selection is active nothing will happen. </p>
<h3>Edit-&gt;Paste</h3>
<p> Pastes the samples that were previously removed with &quot;Cut&quot; at the current sample marker position. The sample selection is set to the pasted samples so that a following &quot;Cut&quot; operation will revert the effect of this operation. </p>
<p> If no sample marker is set nothing will happen. </p>
<h3>Edit-&gt;Add Track Mark</h3>
<p> Adds a track mark with index 1 at the active sample marker position. The position will be rounded to the next frame boundary. If the previous or the new track would be shorter than 4 seconds no track mask is created. </p>
<p> If no sample marker is active nothing will happen. </p>
<h3>Edit-&gt;Add Index Mark</h3>
<p> Adds a track mark with index &gt; 1 at the active sample marker position. The position will be rounded to the next frame boundary. Index marks cannot be created in the pre-gap area of a track. </p>
<p> If no sample marker is active nothing will happen. </p>
<h3>Edit-&gt;Add Pre-Gap</h3>
<p> Adds a track mark with index 0 (pre-gap) at the active sample marker position. Index 0 can only be added right before a track mark with index 1. If the length of the previous track would be shorter than 4 seconds after inserting the pre-gap this operation is not performed. </p>
<p> If no sample marker is active nothing will happen. </p>
<h3>Edit-&gt;Remove Track Mark</h3>
<p> Removes selected track mark with any index. If a track mark with index 1 is removed all track marks of this track will be removed. </p>
<p> If no track marker is selected nothing will happen. </p>
<h3>Tools-&gt;Disk Info</h3>
<p> Opens the non modal &quot;Disk Info&quot; dialog box. See section DISK INFO DIALOG for more details. </p>
<h3>Tools-&gt;Track Info</h3>
<p> Opens the non modal &quot;Track Info&quot; dialog box. See section TRACK INFO DIALOG for more details. </p>
<h3>Tools-&gt;Append Track</h3>
<p> Opens a non modal file selector dialog box to select an audio file that will be completely appended to the audio stream. A track mark with index 1 is added at the beginning of the appended audio data. </p>
<p> The non modal file selector box is shared for &quot;Tools-&gt;Append Track&quot;, &quot;Tools-&gt;Append File&quot; and &quot;Tools-&gt;Insert File&quot;. </p>
<h3>Tools-&gt;Append File</h3>
<p> Opens a non modal file selector dialog box to select an audio file that will be completely appended to the audio stream. </p>
<p> The non modal file selector box is shared for &quot;Tools-&gt;Append Track&quot;, &quot;Tools-&gt;Append File&quot; and &quot;Tools-&gt;Insert File&quot;. </p>
<h3>Tools-&gt;Insert File</h3>
<p> Opens a non modal file selector dialog box to select an audio file that will be completely inserted in the audio stream at the active marker position. If no sample marker is active nothing will happen. </p>
<p> The non modal file selector box is shared for &quot;Tools-&gt;Append Track&quot;, &quot;Tools-&gt;Append File&quot; and &quot;Tools-&gt;Insert File&quot;. </p>
<h3>Tools-&gt;Append Silence</h3>
<p> Opens a non modal dialog box that can be used to append silence to the audio stream. </p>
<p> The non model dialog box is shared for &quot;Tools-&gt;Append Silence&quot; and &quot;Tools-&gt;Insert Silence&quot;. </p>
<h3>Tools-&gt;Insert Silence</h3>
<p> Opens a non modal dialog box that can be used to insert silence in the audio stream at the active marker position. If no sample marker is active nothing will happen. </p>
<p> The non model dialog box is shared for &quot;Tools-&gt;Append Silence&quot; and &quot;Tools-&gt;Insert Silence&quot;. </p>
<h3>Settings-&gt;Devices</h3>
<p> Opens the non modal &quot;Configure Devices&quot; dialog box. See section DEVICE CONFIGURE DIALOG for more details. </p>
<h3>Actions-&gt;Record</h3>
<p> Opens the non modal &quot;Record&quot; dialog box. See section RECORD DIALOG for more details. </p>
<h2>DISK INFO DIALOG (Tools-&gt;Disk Info)</h2>
<p> This non modal dialog shows summary information about the whole project and allows editing of meta data that is valid for the complete disk. </p>
<p> The &quot;Apply&quot; button must be used to make changes permanent. If the summary information changes before the &quot;Apply&quot; button was hit, e.g. by adding a new track, all changes will be lost. </p>
<p> The &quot;Cancel&quot; button withdraws all changes and closes the dialog box. </p>
<h3>Summary Frame</h3>
<p> Shows the total number of tracks, i.e. number of track marks with index 1, and the total length of the audio stream. </p>
<h3>Sub-Channel Frame</h3>
<p> Allows entry and editing of data that is written to the sub-channels of a disk. The scope of this data covers the whole disk. </p>
<p> The &quot;Toc Type&quot; option menu can be used to select the type of the table of contents that will be written to the disk. Currently, for projects that are solely created with this GUI only the type &quot;CD-DA&quot; or &quot;CD-ROM-XA&quot; makes sense. If you read a toc-file that contains data track specifications another type may be displayed. </p>
<p> The &quot;UPC/EAN&quot; edit field sets the catalog number of the disk. Exactly 13 digits must be entered to set the catalog number. To clear the catalog number the edit field must be completely cleared. </p>
<h3>CD-TEXT Frame</h3>
<p> CD-TEXT data can be specified for up to 8 different languages. Each language is reference by a language number 0..7. The first language should have language number 0. Language numbers should be used continuously. </p>
<p> The actual language for a language number is specified with the &quot;Language&quot; option menu: The option &quot;Unknown&quot; is shown for an unknown language code (e.g. if the toc-file was edited manually). It is not possible to select this option. Option &quot;Undefined&quot; means that no language was assigned for this language number. It is possible to enter CD-TEXT data and the entered data will be saved to the toc-file but it will not be recorded to a CD-R/CD-RW. The remaining options select the desired language. Each language can be assigned only to one language number. </p>
<p> The remaining CD-TEXT fields contain ASCII data. It is not necessary to use them all but at least &quot;Title&quot; and &quot;Performer&quot; should be filled. </p>
<h2>TRACK INFO DIALOG (Tools-&gt;Track Info)</h2>
<p> This non modal dialog shows information about a selected track and allows editing of track specific meta data. If no track mark is selected all fields will be cleared and set insensitive. </p>
<p> The &quot;Apply&quot; button must be used to make changes permanent. If the track information changes, e.g. by adding a index mark, or another track mark is selected before the &quot;Apply&quot; button was hit all changes will be lost. </p>
<p> The &quot;Cancel&quot; button withdraws all changes and closes the dialog box. </p>
<h3>Summary Frame</h3>
<p> Shows the length of the pre-gap (0 if no pre-gap is defined), the absolute start and end time, the track length excluding the pre-gap length and the number of index marks &gt; 1. </p>
<h3>Sub-Channel Frame</h3>
<p> Allows editing of all data that is written to the Q sub-channels of the track: </p>
<dl>
<dt>Copy:</p>
<dd> Digital copy permitted when selected. </p>
<dt>Pre Emphasis:</p>
<dd> Audio data of track has pre emphasis when selected. </p>
<dt>Two/Four Channel Audio:</p>
<dd> Select &quot;Four Channel Audio&quot; if the audio data encodes more than two channels. Of course, only two real channels will be recorded on a CD-R/CD-RW in any case. </p>
<dt>ISRC:</p>
<dd> Allows to edit the ISRC code of the track. The first fields holds the country code; it will only accept capital letters. The second field holds the owner code, capital letters and digits are allowed. The remaining fields holds the year and a serial number and will only accept digits. All fields must be filled to set the ISRC code and all fields must be cleared to remove it. </p>
</dl>
<h3>CD-TEXT Frame</h3>
<p> Allows to enter and edit the CD-TEXT data of each language number for this track. All fields are optional but at least &quot;Title&quot; and &quot;Performer&quot; should be filled. </p>
<h2>DEVICE CONFIGURE DIALOG (Settings-&gt;Devices)</h2>
<p> This non modal dialog shows the settings of all attached SCSI or ATAPI devices that identify themselves as CD-ROM or WORM device. </p>
<p> All device settings that differ from the default settings will be permanently stored in the <i>$HOME/.gnome/GnomeCDMaster</i> configuration file. </p>
<p> The &quot;Apply&quot; button must be used to make all changes permanent. The &quot;Reset&quot; button reverts all changes since the last apply or the dialog box was opened. The &quot;Cancel&quot; button withdraws all changes and closes the dialog box. </p>
<h3>Devices Frame</h3>
<p> The browser shows the SCSI address (bus,id,lun) and the vendor/model string of all available devices. If devices are not automatically detected it is possible to add devices manually to the browser (see &quot;Add Device&quot; Frame). </p>
<p> The &quot;Status&quot; column shows the actual device status: </p>
<dl>
<dt>Ready:</p>
<dd> Device has a disk loaded and is ready for an action.</p>
<dt>Busy:</p>
<dd> Device is active with an unspecified action.</p>
<dt>Recording:</p>
<dd> Device is recording.</p>
<dt>No disk:</p>
<dd> Device has no disk loaded.</p>
<dt>Not available:</p>
<dd> Device cannot be accessed.</dl>
<p> The &quot;Rescan&quot; button can be used to start the automatic drive detection process. All changes will be lost and the newly detected devices take immediate effect without hitting &quot;Apply&quot;. </p>
<p> The &quot;Delete&quot; button removes the selected device. The change takes immediate effect and all other changes will be lost. </p>
<h3>Device Settings Frame</h3>
<p> This frame allows to edit the settings of the currently selected device. </p>
<dl>
<dt>Device Type:</p>
<dd> This option menu defines the device type which is used to control which actions can be performed with this device: CD-ROM: read only device, CD-R: CD-R recorder device, CD-RW: CD-RW/CD-R recorder device. </p>
<dt>Driver:</p>
<dd> Option menu to select the driver that is used to access the device. If the device is known by the internal device database the correct driver is selected automatically. Otherwise &quot;Undefined&quot; will be shown and a suitable driver must be selected before any action can be performed with this device. </p>
<dt>Driver Options:</p>
<dd> Enter special driver options here. The available options are described in the README (the documentation will be moved to this place soon). If the device is known by the internal device database the correct option flags are selected automatically. </p>
<dt>Device Node:</p>
<dd> This field is only required for operating systems that cannot access a SCSI device by the bus,id,lun triple. In this case the device node that must be used to access the device should be entered here. </p>
</dl>
<h3>Add Device Frame</h3>
<p> This frame can be used to manually add a device. The bus,id,lun triple of the device and the vendor/product string must be specified before the &quot;Add&quot; button has an effect. It is not possible to overwrite an existing device with the same bus,id,lun triple. Use the &quot;Delete&quot; button of the &quot;Devices&quot; frame first in this case. </p>
<h2>RECORD DIALOG (Actions-&gt;Record)</h2>
<p> This non modal dialog can be used to record the actual project on a CD-R/CD-RW. It is possible to record the actual project on multiple recorders simultaneously. </p>
<p> The &quot;Start&quot; button will start recording processes on all devices that are selected in the &quot;Available Recorder Devices&quot; browser. For this purpose the <i>cdrdao</i> executable will be called and should be available in your PATH. For each selected device a non modal progress dialog will be opened. </p>
<p> After the recording is started on all selected devices it is possible to load another toc-file or continue editing the existing project. It is also safely possible to quit the GUI. The recording will continue in background but you will have no feedback about the progress. </p>
<p> The &quot;Cancel&quot; button will close the dialog box. </p>
<h3>Available Recorder Devices Frame</h3>
<p> The browser shows all devices with device type CD-R or CD-RW. Only devices with &quot;Ready&quot; status are selectable. </p>
<h3>Record Options Frame</h3>
<dl>
<dt>Simulate/Write:</p>
<dd> Selects between simulated or real writing process. </p>
<dt>Close Disk:</p>
<dd> If selected disk will not be appendable. Otherwise the recorded session is kept open. </p>
<p> Note: The drivers &#8216;generic-mmc-raw&#8217;, </p>
<blockquote><p>man2html: unable to open or read file </p></blockquote>
<dt>Eject:</p>
<dd> If selected the disk will be ejected after a successful writing process. </p>
<p> Warning: This may cause buffer under runs with certain device combinations if multiple devices are recording. </p>
<dt>Recording Speed:</p>
<dd> May be used to set an upper limit for the used recording speed. If a recorder device does not support the speed the next lower possible speed is used. </p>
<dt>Reload:</p>
<dd> If selected the disk will be automatically reloaded if it appears to be not empty or not appendable. This is required after a simulation run for some devices (e.g. the Philips CDD2x00 recorder familiy). </p>
<p> Warning: This may cause buffer under runs with certain device combinations if multiple devices are recording. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt>cdrdao:</p>
<dd> executed for recording</p>
<dt>$HOME/.gnome/GnomeCDMaster:</p>
<dd> stores settings permanently </p>
</dl>
<h2>AUTHOR</h2>
<p> Andreas Mueller mueller [at] daneb.ping.de</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cdrdao/">cdrdao</a></code>(1), <a href="/docs/linux/man/1-cdda2wav/">cdda2wav</a><code>(1), <a href="/docs/linux/man/1-cdparanoia/">cdparanoia</a></code>(1) </p>
<h2>Index</h2>
