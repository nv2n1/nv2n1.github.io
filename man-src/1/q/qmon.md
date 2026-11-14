---
title: "qmon(1)"
name: "qmon"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qmon/"
description: "qmon – X-Windows OSF/Motif graphical user interface for xxQS_NAMExx"
---

<h2 class="name">NAME</h2>
<p> qmon &#8211; X-Windows OSF/Motif graphical user interface for xxQS_NAMExx </p>
<h2>SYNTAX</h2>
<p> <code>qmon</code> [options]</p>
<h2>DESCRIPTION</h2>
<p> <i>Qmon</i> allows administrators and users to manipulate the xxQS_NAMExx system from an X-Window environment. <i>Qmon</i> provides various dialogues linked together in multiple ways. For each task the user wishes to accomplish via <i>qmon</i> a corresponding dialogue is provided. There are multiple ways to address the proper dialogue for a certain task: </p>
<dl>
<dt>&bull;</p>
<dd> The <i>qmon</i> main window that comes up first on start-up contains icon buttons for all major administrative and user tasks. A functionality tooltip is displayed when pointing at the different icons.</p>
<dt>&bull;</p>
<dd> A <code>Task</code> pulldown menu button appears in the <i>qmon</i> main window menu bar. Clicking on it opens a list of available tasks. Selecting one of them opens the corresponding dialogue.</p>
<dt>&bull;</p>
<dd> The <code>Task</code> pulldown menu also contains the key accelerators which can be used to invoke the task dialogues directly from the main window by pressing a certain sequence on the keyboard.</p>
<dt>&bull;</p>
<dd> While navigating through a certain dialogue and its dialogue sub-hierarchy, links to other dialogues occur whenever a connection between both dialogues is obvious. Pushing the buttons that identify the links opens up the other dialogues.</dl>
<h2>OPTIONS</h2>
<p> The supported options are the standard X Toolkit options as described in section <code>Options</code>. Furthermore, <i>qmon</i> supports:</p>
<dl>
<dt><code>-cmap</code></p>
<dd> Installs a private color map for <i>qmon</i>. This is sometimes useful if other applications have already allocated lots of colors and if <i>qmon</i>, therefore prints corresponding error messages. <code>Note</code>, however, that using a private color map will result in color map switches whenever you enter or leave <i>qmon</i> windows.</p>
<dt><code>-fontFamily {big|medium|small}</code></p>
<dd> Notifies <i>qmon</i> to use different size font families for different resolution sizes.</p>
<dt><code>-help</code></p>
<dd> Displays usage information.</p>
<dt><code>-nologo</code></p>
<dd> Startup without logo.</dl>
<h2>DIALOGUES</h2>
<h3><code>Job Control</code></h3>
<p> The <code>Job Control</code> dialogue provides a folder of tabulated lists of the still pending jobs, already running jobs and recently finished jobs. The dialogue allows for detailed information on the jobs as well as for the deletion and suspension of jobs being selected. In addition the job control dialogue offers links to the <code>Submit</code> dialogue in order to submit new jobs or to change attributes of pending jobs (<code>Qalter</code> button). The fields displayed in the tabular display and the jobs displayed can be customized by pressing the <code>Customize</code> button. This customization can be saved to the <i>~/.qmon_preferences</i> file and is used on following startup for the initial configuration of the <code>Job Control</code> dialogue. </p>
<h3><code>Queue Control</code></h3>
<p> The <code>Queue Control</code> dialogue with its sub-dialogue hierarchy enables the user to control the status of the xxQS_NAMExx queues actually configured in the system and allows the administrator to add new queues or to modify or delete existing ones. The <code>Queue Control</code> dialogue shows a tabbed view of Cluster Queues or their corresponding Queue Instances in a tabular way. </p>
<p> By pushing the <code>Add</code>, <code>Clone</code> or <code>Modify</code> button, a sub-dialogue for configuring xxQS_NAMExx queues is opened. A queue needs to be selected to use the clone and modify operation. The configuration sub-dialogue allows for definition of the queue and its attributes. The configuration sub-dialogue contains in the upper section the queue name and a list of hosts or hostgroups for which this queue contains the configuration. The lower section contains a list of hosts or hostgroups at the left, where the default attributes are shown when the &quot;@/&quot; entry is highlighted. These default attributes can be overruled on a hostgroup or host basis by enabling attributes and changing their values after this hostgroup or host entry has been added in the &quot;Attributes for Host/Hostgroup&quot; listbox. The queue configuration parameters (see are subdivided into different categories (<code>General Configuration</code>, <code>Execution Methods</code>, <code>Checkpointing</code>, <code>Load/Suspend Thresholds</code>, <code>Limits</code>, <code>Complexes</code>, <code>User Access</code>, <code>Project Access, Subordinate Queues</code>, <code>Owners</code>) which are selectable by the tab widget area presented in the lower region of the queue configuration sub-dialogue. The administrator may select previously-configured settings from already existing queues (<code>Clone</code> button). By pushing the <code>Ok</code> button, the definitions are registered with The <code>Queue Control</code> dialogue can be customized in a similar way as the <code>Job Control</code> dialogue. The settings applied here are also saved in <i>~/.qmon_preferences</i>.</p>
<h3><code>Submit</code></h3>
<p> The <code>Job Submission</code> dialogue serves for submitting batch and interactive jobs and is also invoked when changing attributes of pending jobs from the <code>Job Control</code> dialogue explained above (<code>Qalter</code> button). To toggle between batch and interactive jobs please use the <code>Batch/Interactive</code> button at the top of the button column on the right side of the <code>Job Submission</code> screen. </p>
<p> The dialogue consists of a folder containing two job preparation dialogue pages. The most frequently used parameters in the course of a job submission are offered on the <code>General</code> page. A job script has to be defined; all other fields are optional. If the job demands specification of advanced requirements, the <code>Advanced</code> tab can be used to switch to an enhanced parameter display. </p>
<p> If resource requirements are mandatory for the job, the <code>Request Resources</code> icon button has to be used to pop up the <code>Requested Resources</code> sub-dialogue. This sub-dialogue allows for selection of the required resources of the job and for definition of the quantities in which this resources are to be provided. The <code>Available Resources</code> are constituted from those complex attributes declared <i>requestable</i> (see for details). Resource requirements can be made <code>Hard</code>, i.e. they must be met before a job can be started in a queue, or <code>Soft</code>, i.e. they are granted on an as-available basis. </p>
<p> Closing the <code>Requested Resources</code> sub-dialogue with the done button books the specified requirement for the job. Pushing the <code>Submit</code> button on the top level <code>Submit</code> dialogue submits the job.</p>
<h3><code>Complex Config</code></h3>
<p> The <code>Complex Config</code> allows the administrator to add new complex attributes or to modify or delete existing ones (see The complex configuration dialogue provides a tabulated list of the complex attribute entries and an input region for the declaration of new or modified entries. The <code>Add</code> button updates the tabulated list with a new attribute. The <code>Modify</code> button changes a highlighted existing entry. The <code>Delete</code> button removes the highlighted attributes. The <code>Load and Save</code> buttons allow saving or reloading the whole attribute list to or from file. The <code>Ok</code> button registers the additional or modified complex attributes with</p>
<h3><code>Host Config</code></h3>
<p> Four types of host related lists can be maintained via the <code>Host Config</code> dialogue: </p>
<pre>
<dl><dt><dd>Administration Hosts
Submit Hosts
Host Groups
Execution Hosts
</dl>
</pre>
<p> The host list to be manipulated is selected via clicking at one of the tabs named correspondingly. The first two host lists only provide for adding or deleting entries, thereby allowing administrative or submit permission for the hosts on the lists, or denying it otherwise respectively. The host group list allows the manipulation of host groups. Host groups can reference either other host groups or hosts. The execution host list entries in addition provide the ability to define scaling factors for the load sensors, consumable complex attributes and access attributes (access, xaccess and projects, xprojects) as described in CPU, memory and I/O usage reported for running jobs can be scaled in addition and the relative performance of a host can be defined with the <code>Resource Capability Factor</code> (see</p>
<h3><code>Cluster Config</code></h3>
<p> This dialogue maintains the cluster global configuration as well as host specific derivatives (see When opened, the dialogue displays a selection list for all hosts which have a configuration assigned. The special name &quot;global&quot; refers to the cluster global configuration. By pushing the <code>Add/Modify</code> button a sub-dialogue is opened, which allows for modification of the cluster configuration. For host specific configurations the &#8216;global&#8217; host specific configuration fields are set insensitive and only the allowed parameters can be manipulated.</p>
<h3><code>Scheduler Config</code></h3>
<p> The <code>Scheduler Configuration</code> dialogue provides the means to change the behavior of the xxQS_NAMExx scheduler thread part of process. The dialogue contains a representation for all scheduler configuration parameters as described in It is subdivided in the two sections <code>General Parameters</code> and <code>Load Adjustments</code>, which can be selected via the corresponding tabs. The <code>Ok</code> button registers any changes with</p>
<h3><code>Calendar Config</code></h3>
<p> The <code>Calendar Config</code> allows the administrator to add new calendars or to modify or delete existing ones (see The dialogue offers a selection list for the existing calendars and displays the configuration of the one being selected. By pushing the <code>Delete</code> button, the selected calendar is deleted from the configuration. Pushing the <code>Add</code>/<code>Modify</code> button will open a calendar configuration dialogue, which allows to create new calendars or which provides the means to change the existing ones. The <code>Ok</code> button registers the additional or modified calendar with</p>
<h3><code>User Config</code></h3>
<p> User permissions are controlled via the <code>User Config</code> dialogue. The tab widget in the left section of the dialogue allows for selecting between </p>
<pre>
<dl><dt><dd>Configuration of <code>Manager</code> accounts.
Configuration of <code>Operator</code> accounts.
Definition of <code>Usersets</code>.
Definition of <code>User</code> accounts.
</dl>
</pre>
<p> Those user accounts added to the list of manager or operator accounts are given permission to act as managers or operators respectively when accessing xxQS_NAMExx under their own account. </p>
<p> The userset lists are used together with the <code>user_lists</code> and <code>xuser_lists</code> host, queue, project and cluster configuration parameters (see and to control access of users to hosts, queues, projects and the entire cluster. A userset is just a collection of user names and UNIX group names. Group names are identified by prefixing them with a &quot;@&quot; sign. The already-defined usersets are displayed in a selection list. These lists can be modified, and new lists can be created, using the <code>Userset</code> definition dialogue. </p>
<p> Usersets can be used as <code>Access List</code> and/or as <code>Department</code> required for the so called <code>Functional Policy</code> and <code>Override Policy</code> (see <code>Ticket Config</code> below). </p>
<p> User names can be added to the system as entries to the xxQS_NAMExx user database (see here a default project can be attached to the user too. This can be done with the <code>User</code> sub-dialogue. </p>
<p> The <code>Tickets</code> button in the button list on the right side of the dialogue opens the <code>Ticket Config</code> dialogue (see below).</p>
<h3><code>PE Config</code></h3>
<p> Parallel environment (PE) interfaces can be configured with this dialogue. PE interfaces are necessary to describe how parallel programming environments like PVM (Parallel Virtual Machine), MPI (Message Passing Interface), or shared memory parallel systems, are to be instantiated and to impose access restrictions onto the PEs. When the dialogue is opened a list of the configured PEs is displayed, together with the current configuration (see of the selected PE interface. To add new PE interfaces, or to modify existing ones, an <code>Add</code> and a <code>Modify</code> button are available which open a PE interface configuration sub-dialogue. After applying the changes and quitting this sub-dialogue with the <code>OK</code> button, the new or modified PE interface is registered with</p>
<h3><code>Checkpoint Config</code></h3>
<p> Checkpointing environment interfaces can be configured with this dialogue. Checkpointing environments are necessary to describe the attributes which the different checkpointing methods and their derivatives on various operating system platforms supported by xxQS_NAMExx have. When the dialogue is opened a list of the already configured checkpointing environments is displayed together with the current configuration (see of the selected checkpointing environment. To add new checkpointing environments, or to modify existing ones, an <code>Add</code> and a <code>Modify</code> button is available which opens a checkpointing environment configuration sub-dialogue. After applying the changes and quitting this sub-dialogue with the <code>OK</code> button, the new or modified checkpointing environment is registered with</p>
<h3><code>Ticket Conf</code></h3>
<p> This dialogue offers an overview and editing screen for allocating tickets to the share-based, functional and override scheduling policies. </p>
<p> The <code>Deadline Job</code> button opens the <code>User Conf</code> dialogue box. Please change to the Userset sub-dialogue and select the userset named &quot;deadlineusers&quot;. Only users of this userset may submit deadline jobs. </p>
<p> The <code>Share Tree Policy</code> button opens the dialogue for creating and editing the xxQS_NAMExx share tree (see and for a description of the configuration parameters). </p>
<p> The <code>Functional Policy</code> button opens the dialogue for creating and editing the allocation of the functional shares (see and for a description of the different types of functional shares and the configurable weighting parameters). </p>
<p> The <code>Override Policy</code> button opens the dialogue for creating and editing the allocation of override tickets (see and for a description of the different types of override tickets).</p>
<h3><code>Project Conf</code></h3>
<p> This button opens a dialog for creating projects.<br />
 The dialogue offers a selection list for the existing projects and displays the configuration of the one being selected. By pushing the <code>Delete</code> button, the selected project is deleted from the configuration. Pushing the <code>Add</code>/<code>Modify</code> button will open a project configuration dialogue, which allows creating new projects changing existing ones. Project configuration in essence means giving or denying access to a project for usersets (see <code>User Conf</code> above as well as The Ok button registers the additional or modified project with</p>
<h3><code>Browser</code></h3>
<p> The <code>Object Browser</code> dialogue&#8217;s purpose is manifold: First of all, xxQS_NAMExx and <i>qmon</i> Messages, such as notification of error or success concerning a previously taken action, can be displayed in the dialogue&#8217;s output window. Also the standard output and the standard error output of <i>qmon</i> can be diverted to the <code>Object Browser</code> output window. </p>
<p> Additionally the <code>Object Browser</code> can be used to display continuous information about xxQS_NAMExx objects as the mouse pointer moves over their representation as icons or table entries in other <i>qmon</i> dialogues. Currently, only the display of the configuration of two xxQS_NAMExx objects in two separate dialogues is supported:</p>
<dl>
<dt>&bull;</p>
<dd> Queue configurations are displayed as soon as the mouse pointer enters a queue icon in the top level <code>Queue Control</code> dialogue (see above). This facility is activated by pushing the <code>Queue</code> button in the <code>Object Browser</code> dialogue.</p>
<dt>&bull;</p>
<dd> Detailed job information is printed as soon as the user moves the mouse pointer over a line in the <code>Job Control</code> dialogue (see above) assigned to a running or pending job.</p>
<dt>&bull;</p>
<dd> Additionally job scheduling information is displayed in the browser if the <code>Why?</code> button in the <code>Job Control</code> dialogue is pressed. In this case the Browser dialogue is opened implicitly and any scheduling related information is displayed.</dl>
<h3><code>Exit</code></h3>
<p> The <code>Exit</code> icon button is not linked with a dialogue. Its sole purpose is to close all active <i>qmon</i> dialogues and to exit the application.</p>
<h2>RESOURCES</h2>
<p> The available resources, their meaning and the syntax to be followed in order to modify them are described in the default <i>qmon</i> resource file (see the section <code>Files</code> below for the location of the resource file).</p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>xxQS_NAME_Sxx_ROOT</code></p>
<dd> Specifies the location of the xxQS_NAMExx standard configuration files.</p>
<dt><code>xxQS_NAME_Sxx_CELL</code></p>
<dd> If set, specifies the default xxQS_NAMExx cell. To address a xxQS_NAMExx cell <i>qmon</i> uses (in the order of precedence): </p>
<dl>
<dt>
<dd> The name of the cell specified in the environment variable xxQS_NAME_Sxx_CELL, if it is set. </p>
<p> The name of the default cell, i.e. <code>default</code>. </p>
</dl>
<dt><code>xxQS_NAME_Sxx_DEBUG_LEVEL</code></p>
<dd> If set, specifies that debug information should be written to stderr. In addition the level of detail in which debug information is generated is defined.</p>
<dt><code>xxQS_NAME_Sxx_QMASTER_PORT</code></p>
<dd> If set, specifies the tcp port on which is expected to listen for communication requests. Most installations will use a services map entry instead to define that port.</p>
<dt><code>SGE_LOAD_AVG</code></p>
<dd> Specify a load parameter (see to use instead of <code>load_avg</code> when displaying/selecting load values.</dl>
<h2>RESTRICTIONS</h2>
<p> If the line to be entered in an editing window is longer than the width of the window, then the text just runs off the end of the window.</p>
<h2>FILES</h2>
<pre>
<i>&lt;xxqs_name_sxx_root&gt;/qmon/Qmon</i> <i>Qmon</i> sample resources file
<i>/usr/lib/X11/defaults/Qmon</i>     <i>Qmon</i> system resources file
<i>$HOME/Qmon</i>                     <i>Qmon</i> user resources file
<i>$HOME/.qmon_preferences</i>        <i>Qmon</i> job/queue customization file
</pre>
<h2>SEE ALSO</h2>
<h2>COPYRIGHT</h2>
<p> See and the information provided in &lt;xxqs_name_sxx_root&gt;/3rd_party/qmon for a statement of further rights and permissions and for credits to be given to public domain and freeware widget developers. </p>
<h2>Index</h2>
<dt><a href="#lbAV">RESOURCES</a></p>
<dd>
<dt><a href="#lbAW">ENVIRONMENT VARIABLES</a></p>
<dd>
<dt><a href="#lbAX">RESTRICTIONS</a></p>
<dd>
<dt><a href="#lbAY">FILES</a></p>
<dd>
<dt><a href="#lbAZ">SEE ALSO</a></p>
<dd>
<dt><a href="#lbBA">COPYRIGHT</a></p>
<dd></dl>
