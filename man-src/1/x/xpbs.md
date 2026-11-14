---
title: "xpbs(1)"
name: "xpbs"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xpbs/"
description: "xpbs – GUI front end to PBS commands"
---

<h2 class="name">NAME</h2>
<p> xpbs &#8211; GUI front end to PBS commands </p>
<h2>SYNOPSIS</h2>
<p> xpbs [-admin]</p>
<h2>DESCRIPTION</h2>
<p> The <code>xpbs</code> command provides a user-friendly point-and-click interface to PBS commands. Please see the sections below for a tour and tutorials. Also, within every dialog box, a <code>Help</code> button can be found for assistance.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-admin</p>
<dd> A mode where additional buttons are made available for terminating PBS servers, starting/stopping/disabling/enabling queues, and running/rerunning jobs.</dl>
<h2>GETTING STARTED</h2>
<p> Running <code>xpbs</code> will initialize the X resource database from various sources in the following order:</p>
<dl>
<dt>1.</p>
<dd> The <code>RESOURCE_MANAGER</code> property on the root window (updated via xrdb) with settings usually defined in the .Xdefaults file</p>
<dt>2.</p>
<dd> Preference settings defined by the system administrator in the global xpbsrc file</p>
<dt>3.</p>
<dd> User&#8217;s ~/.xpbsrc file &#8211; this file defines various X resources like fonts, colors, list of PBS hosts to query, criteria for listing queues and jobs, and various view states. See PREFERENCES section below for a list of resources that can be set.</dl>
<h2>RUNNING XPBS</h2>
<p> To run <code>xpbs</code> as a regular, non-privileged user, type:</p>
<dl>
<dt>
<dd>
<p> <code> </p>
</dl>
<p> To run xpbs</code> with the additional purpose of terminating PBS servers, stopping and starting queues, or running/rerunning jobs, then run:</p>
<dl>
<dt>
<dd>
<p> <code> </p>
</dl>
<p> NOTE: Be sure to appropriately set ~/.rhosts file if you&#8217;re planning to submit jobs to some remote server, and expecting output files to be returned to the local host (where xpbs was run). Usually, adding the PBS hostname running the server to your .rhosts file locally, and adding the name of the local machine to the .rhosts file at remote host, should be sufficient. </p>
<p> Also, be sure that the PBS client commands are in the default PATH because xpbs</code> will call these commands.</p>
<h2>THE XPBS DISPLAY</h2>
<p> This section describes the main parts of the <code>xpbs</code> display. The main window is composed of 5 distinct areas (subwindows) arranged vertically (one on top of another) in the following order:</p>
<dl>
<dt>
<dd> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1) Menu<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2) Hosts<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>3) Queues<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>4) Jobs<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>5) Info
</dl>
<p> <code>Menu</code>. The Menu area is composed of a row of command buttons that signal some action with a click of the left mouse button. The buttons are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>Manual Update</p>
<dd> to update the information on hosts, queues, and jobs.</p>
<dt>Auto Update</p>
<dd> same as <i> except updating is done automatically every &lt;some specified&gt; number of minutes.</p>
<dt>Track Job</p>
<dd> for periodically checking for returned output files of jobs.</p>
<dt>Preferences</p>
<dd> for setting certain parameters such as the list of server host(s) to query.</p>
<dt>Help</p>
<dd> contains some help information.</p>
<dt>About</p>
<dd> tells of the author and who to send comments, bugs, suggestions to.</p>
<dt>Close</p>
<dd> for exiting </i><code>xpbs</code> plus saving the current setup information (if anything had changed) in the user&#8217;s $HOME/.xpbsrc file. Information saved include the selected host(s), queue(s), job(s), the different jobs listing criteria, the view states (i.e. minimized/maximized) of the Hosts, Queues, Jobs, and INFO regions, and anything in the Preferences section.</dl>
</dl>
<p> <code>Hosts</code>. The Hosts area is composed of a leading horizontal HOSTS bar, a listbox, and a set of command buttons. The HOSTS bar contains a minimize/maximize button, identified by a dot or a rectangular image, for displaying or iconizing the Hosts region. The listbox displays information about favorite server host(s), and each entry is meant to be selected via a single left mouse button click, shift key + mouse button 1 click for contiguous selection, or cntrl key + mouse button 1 click for non-contiguous selection. The command buttons represent actions on selected host(s), and commonly found buttons are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>detail</p>
<dd> for obtaining detailed information about selected server host(s). This functionality can also be achieved by double clicking on an entry in the Hosts listbox.</p>
<dt>Submit</p>
<dd> for submitting a job to any of the queues managed by the selected host(s).</p>
<dt>terminate</p>
<dd> for terminating PBS servers on selected host(s). (-admin only)</dl>
</dl>
<p> The server hosts can be chosen by specifying in the ~/.xpbsrc file (or .Xdefaults) the resource:</p>
<dl>
<dt>
<dd>
<p> *serverHosts:<tt>&nbsp;<wbr>&nbsp;<wbr></tt>hostname1 hostname2 &#8230;</p>
</dl>
<p> Another way of specifying the host is to click on the Preferences button in the Menu region, and manipulate the server Hosts entry widget from the preferences dialog box. </p>
<p> <code>Queues</code>. The Queues area is composed of a leading horizontal QUEUES bar, a listbox, and a set of command buttons. The QUEUES bar lists the hosts that are consulted when listing queues; the bar also contains a minimize/maximize button for displaying or iconizing the Queues region. The listbox displays information about queues managed by the server host(s) selected from the Hosts listbox; each listbox entry is meant to be selected (highlighted) via a single left mouse button click, shift key + mouse button 1 click for contiguous selection, or cntrl key + mouse button 1 click for non-contiguous selection. The command buttons represent actions for operating on selected queue(s), and commonly found buttons are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>detail</p>
<dd> for obtaining detailed information about selected queue(s). This functionality can also be achieved by double clicking on a Queues listbox entry.</p>
<dt>stop</p>
<dd> for stopping the selected queue(s). (-admin only)</p>
<dt>start</p>
<dd> for starting the selected queue(s). (-admin only)</p>
<dt>disable</p>
<dd> for disabling the selected queue(s). (-admin only)</p>
<dt>enable</p>
<dd> for enabling the selected queue(s). (-admin only)</dl>
</dl>
<p> <code>Jobs</code>. The Jobs area is composed of a leading horizontal JOBS bar, a listbox, and a set of command buttons. The JOBS bar lists the queues that are consulted when listing jobs; the bar also contains a minimize/maximize button for displaying or iconizing the Jobs region. The listbox displays information about jobs that are found in the queue(s) selected from the Queues listbox; each listbox entry is meant to be selected (highlighted) via a single left mouse button click, shift key + mouse button 1 click for contiguous selection, or cntrl key + mouse button 1 click for non-contiguous selection. The region just above the Jobs listbox shows a collection of command buttons whose labels describe criteria used for filtering the Jobs listbox contents. The list of jobs can be selected according to the owner of jobs (Owners), job state (Job_States), name of the job (Job_Name), type of hold placed on the job (Hold_Types), the account name associated with the job (Account_Name), checkpoint attribute (Checkpoint), time the job is eligible for queueing/execution (Queue_Time), resources requested by the job (Resources), priority attached to the job (Priority), and whether or not the job is rerunnable (Rerunnable). The selection criteria can be modified by clicking on any of the appropriate command buttons to bring up a selection box. The criteria command buttons are accompanied by a <i> button, which when clicked, will update the contents of the Jobs listbox based on the new selection criteria. Please see </i><code><a href="//www.systutorials.com/docs/linux/man/1B-qselect/">qselect</a>(1B)</code> for more details on how the jobs are filtered. </p>
<p> Finally, to the right of the listbox, the Jobs region is accompanied by the following command buttons, for operating on selected job(s):</p>
<dl>
<dt>
<dd>
<dl>
<dt>detail</p>
<dd> for obtaining detailed information about selected job(s). This functionality can also be achieved by double clicking on a Jobs listbox entry.</p>
<dt>modify</p>
<dd> for modifying attributes of the selected job(s).</p>
<dt>delete</p>
<dd> for deleting the selected job(s).</p>
<dt>hold</p>
<dd> for placing some type of hold on selected job(s).</p>
<dt>release</p>
<dd> for releasing held job(s).</p>
<dt>signal</p>
<dd> for sending signals to selected job(s) that are running.</p>
<dt>msg</p>
<dd> for writing a message string into the output streams of the selected job(s).</p>
<dt>move</p>
<dd> for moving selected job(s) into some specified destination queue.</p>
<dt>order</p>
<dd> for exchanging order of two selected jobs in a queue.</p>
<dt>run</p>
<dd> for running selected job(s). (-admin only)</p>
<dt>rerun</p>
<dd> for requeueing selected job(s) that are running. (-admin only)</dl>
</dl>
<p> <code>Info</code>. The Info Area shows the progress of the commands&#8217; executed by <code>xpbs</code>. Look into this box for errors. The INFO bar also contains a minimize/maximize button for displaying or iconizing the Info region.</p>
<h2>WIDGETS USED IN XPBS</h2>
<p> Some of the widgets used in <code>xpbs</code> and how they are manipulated are described in the following: </p>
<dl>
<dt>1.</p>
<dd> <code>listbox</code> &#8211; can be multi-selectable (a number of entries can be selected/highlighted using a mouse click) or single-selectable (one entry can be highlighted at a time). For a multi-selectable listbox, the following operations are allowed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>a.</p>
<dd> single click with mouse button 1 to select/highlight an entry.</p>
<dt>b.</p>
<dd> shift key + mouse button 1 to contiguously select more than one entry.</p>
<dt>c.</p>
<dd> cntrl key + mouse button 1 to non-contiguously select more than one entry. NOTE: For systems running Tk &lt; 4.0, the newly selected item is reshuffled to appear next to already selected items.</p>
<dt>d.</p>
<dd> click the <i> button to select all entries or deselect all entries at once.</p>
<dt>e.</p>
<dd> double clicking an entry usually activates some action that uses the selected entry as a parameter. </p>
</dl>
</dl>
<dt>2.</p>
<dd> </i><code>scrollbar</code> &#8211; usually appears either vertically or horizontally and contains 5 distinct areas that are mouse clicked to achieve different effects:</p>
<dl>
<dt>
<dd>
<dl>
<dt>top arrow</p>
<dd> Causes the view in the associated widget to shift up by one unit (i.e. the object appears to move down one unit in its window). If the button is held down the action will auto-repeat.</p>
<dt>top gap</p>
<dd> Causes the view in the associated window to shift up by one less than the number of units in the window (i.e. the portion of the object that used to appear at the very top of the window will now appear at the very bottom). If the button is held down the action will auto-repeat.</p>
<dt>slider</p>
<dd> Pressing button 1 in this area has no immediate effect except to cause the slider to appear sunken rather than raised. However, if the mouse is moved with the button down then the slider will be dragged, adjusting the view as the mouse is moved.</p>
<dt>bottom gap</p>
<dd> Causes the view in the associated window to shift down by one less than the number of units in the window (i.e. the portion of the object that used to appear at the very bottom of the window will now appear at the very top). If the button is held down the action will auto-repeat.</p>
<dt>bottom arrow</p>
<dd> Causes the view in the associated window to shift down by one unit (i.e. the object appears to move up one unit in its window). If the button is held down the action will auto-repeat.</dl>
</dl>
<dt>3.</p>
<dd> <code>entry</code> &#8211; brought into focus with a click of the left mouse button. To manipulate this widget, simply type in the text value. Use of arrow keys, mouse selection of text for deletion or overwrite, copying and pasting with sole use of mouse buttons are permitted. This widget is usually accompanied by a scrollbar for horizontally scanning a long text entry string. </p>
<dt>4.</p>
<dd> <code>matrix of entry boxes</code> &#8211; usually shown as several rows of entry widgets where a number of entries (called fields) can be found per row. The matrix is accompanied by up/down arrow buttons for paging through the rows of data, and each group of fields gets one scrollbar for horizontally scanning long entry strings. Moving from field to field can be done using the &lt;Tab&gt;, &lt;Cntrl-f&gt;, or &lt;Cntrl-b&gt; (move backwards) keys. </p>
<dt>5.</p>
<dd> <code>spinbox</code> &#8211; a combination of an entry widget and a horizontal scrollbar. The entry widget will only accept values that fall within a defined list of valid values, and incrementing through the valid values is done by clicking on the up/down arrows.</p>
<dt>6.</p>
<dd> <code>button</code> &#8211; a rectangular region appearing either raised or pressed that invokes an action when clicked with the left mouse button. When the button appears pressed, then hitting the &lt;RETURN&gt; key will automatically select the button.</p>
<dt>7.</p>
<dd> <code>text</code> &#8211; an editor like widget. This widget is brought into focus with a click of the left mouse button. To manipulate this widget, simply type in the text. Use of arrow keys, backspace/delete key, mouse selection of text for deletion or overwrite, copying and pasting with sole use of mouse buttons are permitted. This widget is usually accompanied by a scrollbar for vertically scanning a long entry.</dl>
<h2>SUBMITTING JOBS</h2>
<p> Submitting a PBS job requires only to manipulate the widgets found in the Submit window. The submit dialog box is composed of 4 distinct regions: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1) Job Script<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2) OPTIONS<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>3) OTHER OPTIONS<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>4) Command Buttons </p>
<p> The Job Script file region is at the upper left, the OPTIONS region containing various widgets for setting job attributes is scattered all over the dialog box, the OTHER OPTIONS is located just below the Job Script file region, and Command Buttons region is at the bottom. </p>
<p> The job script region is composed of a header box, the text box, FILE entry box, and a couple of buttons labeled <i> and If you have a script file containing PBS options and executable lines, then type the name of the file on the FILE entry box, and then click on the button. The various widgets in the Submit window will get loaded with values found in the script file. The script file text box will only be loaded with executable lines (non-PBS) found in the script. The job script header box has a entry box that can be modified to specify the PBS directive to look for when parsing a script file for PBS options. If you don&#8217;t have a script file, you can start typing the executable lines of the job in the file text box. </p>
<p> To submit a job, perform the following steps:</p>
<dl>
<dt>
<dd>
<dl>
<dt>1.</p>
<dd> Select a host from the HOSTS listbox in the main </i><code>xpbs</code> display.</p>
<dt>2.</p>
<dd> Click on the <i> button located in the Menu bar.</p>
<dt>3.</p>
<dd> Specify the script file containing the job execution lines and job property values, or simply type in the execution lines in the FILE textbox.</p>
<dt>4.</p>
<dd> Start manipulating the various widgets in the Submit window. Particularly, pay close attention to the Destination listbox. This box lists all the queues found in the host that you selected. A special entry called </i><code> refers to the default queue at host. Select appropriately the destination queue of the job. More options can be found by clicking the OTHER OPTIONS buttons.</p>
<dt>5.</p>
<dd> At the bottom of the Submit window, click </code><i> You can also click on to run the job interactively. Running a job interactively will open an xterm window to your display host containing the session. </p>
<p> NOTE: The script FILE entry box is accompanied by a button that you click to save the current widget values to the specified file in a form that can later be read by </i><code>xpbs</code> or by the <code>qsub</code> command.</dl>
</dl>
<h2>MODIFYING ATTRIBUTES OF JOBS</h2>
<p> Modifying a PBS job requires only to manipulate the widgets found in the Modify window. To modify a job or jobs, do the following steps:</p>
<dl>
<dt>
<dd>
<dl>
<dt>1.</p>
<dd> Select one or more jobs from the JOBS listbox in the main <code>xpbs</code> display.</p>
<dt>2.</p>
<dd> Click on the <i> button located to the right of the listbox.</p>
<dt>3.</p>
<dd> The Modify window is structured similarly to the Submit window. Simply manipulate the widgets to specify replacement or additional values of job attributes.</p>
<dt>4.</p>
<dd> Click on the button located at the bottom of the dialog box.</dl>
</dl>
<p> </i></p>
<h2>DELETING JOBS</h2>
<p> Deleting a PBS job requires only to manipulate the widgets found in the Delete window. To delete a job or jobs, do the following steps:</p>
<dl>
<dt>
<dd>
<dl>
<dt>1.</p>
<dd> Select one or more jobs from the JOBS listbox in the main <code>xpbs</code> display.</p>
<dt>2.</p>
<dd> Click on the <i> button located to the right of the listbox.</p>
<dt>3.</p>
<dd> Manipulate the spinbox widget to set the kill delay signal interval.</p>
<dt>4.</p>
<dd> Click on the button located at the bottom of the dialog box.</dl>
</dl>
<p> </i></p>
<h2>TRACKING RETURNED OUTPUT FILES</h2>
<p> If you want to be informed of returned output files of current jobs, and be able to quickly see the contents of those files, then enable the <code> feature as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt>1.</p>
<dd> Submit all the jobs that you want monitored.</p>
<dt>2.</p>
<dd> Click on the </code><i> button located in the Menu bar to bring up the Track Job dialog box.</p>
<dt>3.</p>
<dd> Specify the list of user names, whose jobs are to be monitored for returned output files, in the matrix located at the upper left of the dialog box.</p>
<dt>4.</p>
<dd> Manipulate the minutes spinbox, located just below the user names matrix, to specify the interval value when output files will be periodically checked.</p>
<dt>5.</p>
<dd> Specify the location of job output files (whether locally or remotely) by clicking on one of the radio buttons located at the upper right of the dialog box. Returned locally means the output files will be returned back to the host where </i><code>xpbs</code> was run. If the output files are returned to some remote host, then <code>xpbs</code> will execute an<br />
 <code><br />
 to test the existence of the files. RSH is whatever you set the remote shell command to in the corresponding entry box. </p>
<p> NOTE: Be sure the files are accessible from the host where xpbs</code> was run (i.e. .rhosts appropriately set).</p>
<dt>6.</p>
<dd> Click <i> button located at the bottom of the dialog box to:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;</p>
<dd> cancel any previous tracking</p>
<dt>&#8211;</p>
<dd> build a new list of jobs to be monitored for returned output files based on currently queued jobs.</p>
<dt>&#8211;</p>
<dd> start periodic tracking.</dl>
</dl>
<dt>7.</p>
<dd> Click on button.</dl>
</dl>
<p> When an output file for a job being monitored is found, then the button (the one that originally invoked the Track Job dialog box) will turn into a different color, and the listbox, located in the Track Job dialog box, is then loaded with the corresponding job id(s). Then double click on a job id to see the contents of the output file and the error file. Click if you want to cancel tracking. </i></p>
<h2>LEAVING XPBS</h2>
<p> Click on the Close button located in the Menu bar to leave <code>xpbs</code>. If anything had changed, it will bring up a dialog box asking for a confirmation in regards to saving state information like the view states (minimize/maximize) of the HOSTS, QUEUES, JOBS, and INFO subwindows, and various criteria for listing queues and jobs. The information is saved in ~/.xpbsrc file.</p>
<h2>PREFERENCES</h2>
<p> The resources that can be set in the X resources file, ~/.xpbsrc, are:</p>
<dl>
<dt>*serverHosts</p>
<dd> list of server hosts (space separated) to query by <code>xpbs</code>.</p>
<dt>*timeoutSecs</p>
<dd> specify the number of seconds before timing out waiting for a connection to a PBS host.</p>
<dt>*xtermCmd</p>
<dd> the xterm command to run driving an interactive PBS session.</p>
<dt>*labelFont</p>
<dd> font applied to text appearing in labels.</p>
<dt>*fixlabelFont</p>
<dd> font applied to text that label fixed-width widgets such as listbox labels. This must be a fixed-width font.</p>
<dt>*textFont</p>
<dd> font applied to a text widget. Keep this as fixed-width font.</p>
<dt>*backgroundColor</p>
<dd> the color applied to background of frames, buttons, entries, scrollbar handles.</p>
<dt>*foregroundColor</p>
<dd> the color applied to text in any context (under selection, insertion, etc&#8230;).</p>
<dt>*activeColor</p>
<dd> the color applied to the background of a selection, a selected command button, or a selected scroll bar handle.</p>
<dt>*disabledColor</p>
<dd> color applied to a disabled widget.</p>
<dt>*signalColor</p>
<dd> color applied to buttons that signal something to the user about a change of state. For example, the color of the <i> button when returned output files are detected.</p>
<dt>*shadingColor</p>
<dd> a color shading applied to some of the frames to emphasize focus as well as decoration.</p>
<dt>*selectorColor</p>
<dd> the color applied to the selector box of a radiobutton or checkbutton.</p>
<dt>*selectHosts</p>
<dd> list of hosts (space separated) to automatically select/highlight in the HOSTS listbox.</p>
<dt>*selectQueues</p>
<dd> list of queues (space separated) to automatically select/highlight in the QUEUES listbox.</p>
<dt>*selectJobs</p>
<dd> list of jobs (space separated) to automatically select/highlight in the JOBS listbox.</p>
<dt>*selectOwners</p>
<dd> list of owners checked when limiting the jobs appearing on the Jobs listbox in the main </i><code>xpbs</code> window. Specify value as &quot;Owners: &lt;list_of_owners&gt;&quot;. See -u option in <code><a href="//www.systutorials.com/docs/linux/man/1B-qselect/">qselect</a>(1B)</code> for format of &lt;list_of_owners&gt;.</p>
<dt>*selectStates</p>
<dd> list of job states to look for (do not space separate) when limiting the jobs appearing on the Jobs listbox in the main <code>xpbs</code> window. Specify value as &quot;Job_States: &lt;states_string&gt;&quot;. See -s option in <code><a href="//www.systutorials.com/docs/linux/man/1B-qselect/">qselect</a>(1B)</code> for format of &lt;states_string&gt;.</p>
<dt>*selectRes</p>
<dd> list of resource amounts (space separated) to consult when limiting the jobs appearing on the Jobs listbox in the main <code>xpbs</code> window. Specify value as &quot;Resources: &lt;res_string&gt;&quot;. See -l option in <code><a href="//www.systutorials.com/docs/linux/man/1B-qselect/">qselect</a>(1B)</code> for format of &lt;res_string&gt;.</p>
<dt>*selectExecTime</p>
<dd> the Execution Time attribute to consult when limiting the list of jobs appearing on the Jobs listbox in the main <code>xpbs</code> window. Specify value as &quot;Queue_Time: &lt;exec_time&gt;&quot;. See -a option in <code><a href="//www.systutorials.com/docs/linux/man/1B-qselect/">qselect</a>(1B)</code> for format of &lt;exec_time&gt;.</p>
<dt>*selectAcctName</p>
<dd> the name of the account that will be checked when limiting the jobs appearing on the Jobs listbox in the main <code>xpbs</code> window. Specify value as &quot;Account_Name: &lt;account_name&gt;&quot;. See -A option in <code><a href="//www.systutorials.com/docs/linux/man/1B-qselect/">qselect</a>(1B)</code> for format of &lt;account_name&gt;.</p>
<dt>*selectCheckpoint</p>
<dd> the checkpoint attribute relationship (including the logical operator) to consult when limiting the list of jobs appearing on the Jobs listbox in the main <code>xpbs</code> window. Specify value as &quot;Checkpoint: &lt;checkpoint_arg&gt;&quot;. See -c option in <code><a href="//www.systutorials.com/docs/linux/man/1B-qselect/">qselect</a>(1B)</code> for format of &lt;checkpoint_arg&gt;.</p>
<dt>*selectHold</p>
<dd> the hold types string to look for in a job when limiting the jobs appearing on the Jobs listbox in the main <code>xpbs</code> window. Specify value as &quot;Hold_Types: &lt;hold_string&gt;&quot;. See -h option in <code><a href="//www.systutorials.com/docs/linux/man/1B-qselect/">qselect</a>(1B)</code> for format of &lt;hold_string&gt;.</p>
<dt>*selectPriority</p>
<dd> the priority relationship (including the logical operator) to consult when limiting the list of jobs appearing on the Jobs listbox in the main <code>xpbs</code> window. Specify value as &quot;Priority: &lt;priority_value&gt;&quot;. See -p option in <code><a href="//www.systutorials.com/docs/linux/man/1B-qselect/">qselect</a>(1B)</code> for format of &lt;priority_value&gt;.</p>
<dt>*selectRerun</p>
<dd> the rerunnable attribute to consult when limiting the list of jobs appearing on the Jobs listbox in the main <code>xpbs</code> window. Specify value as &quot;Rerunnable: &lt;rerun_val&gt;&quot;. See -r option in <code><a href="//www.systutorials.com/docs/linux/man/1B-qselect/">qselect</a>(1B)</code> for format of &lt;rerun_val&gt;.</p>
<dt>*selectJobName</p>
<dd> name of the job that will be checked when limiting the jobs appearing on the Jobs listbox in the main <code>xpbs</code> window. Specify value as &quot;Job_Name: &lt;jobname&gt;&quot;. See -N option in <code><a href="//www.systutorials.com/docs/linux/man/1B-qselect/">qselect</a>(1B)</code> for format of &lt;jobname&gt;.</p>
<dt>*iconizeHostsView</p>
<dd> a boolean value (true or false) indicating whether or not to iconize the HOSTS region.</p>
<dt>*iconizeQueuesView</p>
<dd> a boolean value (true or false) indicating whether or not to iconize the QUEUES region.</p>
<dt>*iconizeJobsView</p>
<dd> a boolean value (true or false) indicating whether or not to iconize the JOBS region.</p>
<dt>*iconizeInfoView</p>
<dd> a boolean value (true or false) indicating whether or not to iconize the INFO region.</p>
<dt>*jobResourceList</p>
<dd> a curly-braced list of resource names as according to architecture known to xpbs. The format is as follows:<br />
 { &lt;arch-type1&gt; resname1 resname2 &#8230; resnameN }<br />
 { &lt;arch-type2&gt; resname1 resname2 &#8230; resnameN } </p>
<p>&nbsp;<wbr>. . .<br />
 { &lt;arch-typeN&gt; resname1 resname2 &#8230; resnameN }</dl>
<h2>XPBS AND PBS COMMANDS</h2>
<p> <code>xpbs</code> calls PBS commands as follows:</p>
<dl>
<dt><code>Command Button</code></p>
<dd> <code>PBS Command</code></p>
<dt>detail (Hosts)</p>
<dd> qstat -B -f &lt;selected server_host(s)&gt;</p>
<dt>terminate</p>
<dd> qterm &lt;selected server_host(s)&gt;</p>
<dt>detail (Queues)</p>
<dd> qstat -Q -f &lt;selected queue(s)&gt;</p>
<dt>stop</p>
<dd> qstop &lt;selected queue(s)&gt;</p>
<dt>start</p>
<dd> qstart &lt;selected queue(s)&gt;</p>
<dt>enable</p>
<dd> qenable &lt;selected queue(s)&gt;</p>
<dt>disable</p>
<dd> qdisable &lt;selected queue(s)&gt;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt>detail (Jobs)</p>
<dd> qstat -f &lt;selected job(s)&gt;</p>
<dt>modify</p>
<dd> qalter &lt;selected job(s)&gt;</p>
<dt>delete</p>
<dd> qdel &lt;selected job(s)&gt;</p>
<dt>hold</p>
<dd> qhold &lt;selected job(s)&gt;</p>
<dt>release</p>
<dd> qrls &lt;selected job(s)&gt;</p>
<dt>run</p>
<dd> qrun &lt;selected job(s)&gt;</p>
<dt>rerun</p>
<dd> qrerun &lt;selected job(s)&gt;</p>
<dt>signal</p>
<dd> qsig &lt;selected job(s)&gt;</p>
<dt>msg</p>
<dd> qmsg &lt;selected job(s)&gt;</p>
<dt>move</p>
<dd> qmove &lt;selected job(s)&gt;</p>
<dt>order</p>
<dd> qorder &lt;selected job(s)&gt;</dl>
<h2>EXIT STATUS</h2>
<p> Upon successful processing, the <code>xpbs</code> exit status will be a value of zero. </p>
<p> If the xpbs command fails, the command exits with a value greater than zero.</p>
<h2>SEE ALSO</h2>
<p> <a href="//www.systutorials.com/docs/linux/man/1B-qalter/">qalter</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qdel/">qdel</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qhold/">qhold</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qmove/">qmove</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qmsg/">qmsg</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qrerun/">qrerun</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qrls/">qrls</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qselect/">qselect</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qsig/">qsig</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qstat/">qstat</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qorder/">qorder</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qsub/">qsub</a>(1B), <a href="//www.systutorials.com/docs/linux/man/8B-qdisable/">qdisable</a>(8B), <a href="//www.systutorials.com/docs/linux/man/8B-qenable/">qenable</a>(8B), <a href="//www.systutorials.com/docs/linux/man/8B-qrun/">qrun</a>(8B), <a href="//www.systutorials.com/docs/linux/man/8B-qstart/">qstart</a>(8B), <a href="//www.systutorials.com/docs/linux/man/8B-qstop/">qstop</a>(8B), <a href="//www.systutorials.com/docs/linux/man/8B-qterm/">qterm</a>(8B). </p>
<h2>Index</h2>
