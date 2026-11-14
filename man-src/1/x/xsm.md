---
title: "xsm(1)"
name: "xsm"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xsm/"
description: "xsm – X Session Manager"
---

<h2 class="name">NAME</h2>
<p> xsm &#8211; X Session Manager </p>
<h2>SYNOPSIS</h2>
<p> <code>xsm</code> [-display <i>display</i>] [-session <i>sessionName</i>] [-verbose]</p>
<h2>DESCRIPTION</h2>
<p> <i>xsm</i> is a session manager. A session is a group of applications, each of which has a particular state. <i>xsm</i> allows you to create arbitrary sessions &#8211; for example, you might have a &quot;light&quot; session, a &quot;development&quot; session, or an &quot;xterminal&quot; session. Each session can have its own set of applications. Within a session, you can perform a &quot;checkpoint&quot; to save application state, or a &quot;shutdown&quot; to save state and exit the session. When you log back in to the system, you can load a specific session, and you can delete sessions you no longer want to keep. </p>
<p> Some session managers simply allow you to manually specify a list of applications to be started in a session. <i>xsm</i> is more powerful because it lets you run applications and have them automatically become part of the session. On a simple level, <i>xsm</i> is useful because it gives you this ability to easily define which applications are in a session. The true power of <i>xsm</i>, however, can be taken advantage of when more and more applications learn to save and restore their state.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-display </code><i>display</i></p>
<dd> Causes <i>xsm</i> to connect to the specified X display.</p>
<dt><code>-session </code><i>sessionName</i></p>
<dd> Causes <i>xsm</i> to load the specified session, bypassing the session menu.</p>
<dt><code>-verbose</code></p>
<dd> Turns on debugging information.</dl>
<h2>SETUP</h2>
<h3>.xsession file</h3>
<p> Using <i>xsm</i> requires a change to your <i>.xsession</i> file: </p>
<p> The last program executed by your <i>.xsession</i> file should be <i>xsm</i>. With this configuration, when the user chooses to shut down the session using <i>xsm</i>, the session will truly be over. </p>
<p> Since the goal of the session manager is to restart clients when logging into a session, your .xsession file, in general, should not directly start up applications. Rather, the applications should be started within a session. When <i>xsm</i> shuts down the session, <i>xsm</i> will know to restart these applications. Note however that there are some types of applications that are not &quot;session aware&quot;. <i>xsm</i> allows you to manually add these applications to your session (see the section titled <i>Client List</i>). </p>
<h3>SM_SAVE_DIR environment variable</h3>
<p> If the <i>SM_SAVE_DIR</i> environment variable is defined, <i>xsm</i> will save all configuration files in this directory. Otherwise, they will be stored in the user&#8217;s home directory. Session aware applications are also encouraged to save their checkpoint files in the <i>SM_SAVE_DIR</i> directory, although the user should not depend on this convention. </p>
<h3>Default Startup Applications</h3>
<p> The first time <i>xsm</i> is started, it will need to locate a list of applications to start up. For example, this list might include a window manager, a session management proxy, and an xterm. <i>xsm</i> will first look for the file <i>.xsmstartup</i> in the user&#8217;s home directory. If that file does not exist, it will look for the <i>system.xsm</i> file that was set up at installation time. Note that <i>xsm</i> provides a &quot;fail safe&quot; option when the user chooses a session to start up. The fail safe option simply loads the default applications described above. </p>
<p> Each line in the startup file should contain a command to start an application. A sample startup file might look this: </p>
<p> &lt;start of file&gt;<br />
 twm<br />
 smproxy<br />
 xterm<br />
 &lt;end of file&gt; </p>
<h2>STARTING A SESSION</h2>
<p> When <i>xsm</i> starts up, it first checks to see if the user previously saved any sessions. If no saved sessions exist, <i>xsm</i> starts up a set of default applications (as described above in the section titled <i>Default Startup Applications</i>). If at least one session exists, a session menu is presented. The <code>-session</code> option forces the specified <i>sessionName</i> session to be loaded, bypassing the session menu.</p>
<h3>The session menu</h3>
<p> The session menu presents the user with a list of sessions to choose from. The user can change the currently selected session with the mouse, or by using the up and down arrows on the keyboard. Note that sessions which are locked (i.e. running on a different display) can not be loaded or deleted. </p>
<p> The following operations can be performed from the session menu: </p>
<dl>
<dt><code>Load Session</code></p>
<dd> Pressing this button will load the currently selected session. Alternatively, hitting the Return key will also load the currently selected session, or the user can double click a session from the list.</p>
<dt><code>Delete Session</code></p>
<dd> This operation will delete the currently selected session, along with all of the application checkpoint files associated with the session. After pressing this button, the user will be asked to press the button a second time in order to confirm the operation.</p>
<dt><code>Default/Fail Safe</code></p>
<dd> <i>xsm</i> will start up a set of default applications (as described above in the section titled <i>Default Startup Applications</i>). This is useful when the user wants to start a fresh session, or if the session configuration files were corrupted and the user wants a &quot;fail safe&quot; session.</p>
<dt><code>Cancel</code></p>
<dd> Pressing this button will cause <i>xsm</i> to exit. It can also be used to cancel a &quot;Delete Session&quot; operation.</dl>
<h2>CONTROLLING A SESSION</h2>
<p> After <i>xsm</i> determines which session to load, it brings up its main window, then starts up all applications that are part of the session. The title bar for the session manager&#8217;s main window will contain the name of the session that was loaded. </p>
<p> The following options are available from <i>xsm</i>&#8216;s main window:</p>
<dl>
<dt><code>Client List</code></p>
<dd> Pressing this button brings up a window containing a list of all clients that are in the current session. For each client, the host machine that the client is running on is presented. As clients are added and removed from the session, this list is updated to reflect the changes. The user is able to control how these clients are restarted (see below). </p>
<p> By pressing the <code>View Properties</code> button, the user can view the session management properties associated with the currently selected client. </p>
<p> By pressing the <code>Clone</code> button, the user can start a copy of the selected application. </p>
<p> By pressing the <code>Kill Client</code> button, the user can remove a client from the session. </p>
<p> By selecting a restart hint from the <code>Restart Hint</code> menu, the user can control the restarting of a client. The following hints are available: </p>
<p> <code>&#8211;</code> The <code>Restart If Running</code> hint indicates that the client should be restarted in the next session if it is connected to the session manager at the end of the current session. </p>
<p> <code>&#8211;</code> The <code>Restart Anyway</code> hint indicates that the client should be restarted in the next session even if it exits before the current session is terminated. </p>
<p> <code>&#8211;</code> The <code>Restart Immediately</code> hint is similar to the <code>Restart Anyway</code> hint, but in addition, the client is meant to run continuously. If the client exits, the session manager will try to restart it in the current session. </p>
<p> <code>&#8211;</code> The <code>Restart Never</code> hint indicates that the client should not be restarted in the next session. </p>
<p> Note that all X applications may not be &quot;session aware&quot;. Applications that are not session aware are ones that do not support the X Session Management Protocol or they can not be detected by the Session Management Proxy (see the section titled <i>THE PROXY</i>). <i>xsm</i> allows the user to manually add such applications to the session. The bottom of the <i>Client List</i> window contains a text entry field in which application commands can be typed in. Each command should go on its own line. This information will be saved with the session at checkpoint or shutdown time. When the session is restarted, <i>xsm</i> will restart these applications in addition to the regular &quot;session aware&quot; applications. </p>
<p> Pressing the <code>Done</code> button removes the <code>Client List</code> window.</p>
<dt><code>Session Log&#8230;</code></p>
<dd> The Session Log window presents useful information about the session. For example, when a session is restarted, all of the restart commands will be displayed in the log window.</p>
<dt><code>Checkpoint</code></p>
<dd> By performing a checkpoint, all applications that are in the session are asked to save their state. Not every application will save its complete state, but at a minimum, the session manager is guaranteed that it will receive the command required to restart the application (along with all command line options). A window manager participating in the session should guarantee that the applications will come back up with the same window configurations. </p>
<p> If the session being checkpointed was never assigned a name, the user will be required to specify a session name. Otherwise, the user can perform the checkpoint using the current session name, or a new session name can be specified. If the session name specified already exists, the user will be given the opportunity to specify a different name or to overwrite the already existing session. Note that a session which is locked can not be overwritten. </p>
<p> When performing a checkpoint, the user must specify a <code>Save Type</code> which informs the applications in the session how much state they should save. </p>
<p> The <code>Local</code> type indicates that the application should save enough information to restore the state as seen by the user. It should not affect the state as seen by other users. For example, an editor would create a temporary file containing the contents of its editing buffer, the location of the cursor, etc&#8230; </p>
<p> The <code>Global</code> type indicates that the application should commit all of its data to permanent, globally accessible storage. For example, the editor would simply save the edited file. </p>
<p> The <code>Both</code> type indicates that the application should do both of these. For example, the editor would save the edited file, then create a temporary file with information such as the location of the cursor, etc&#8230; </p>
<p> In addition to the <code>Save Type</code>, the user must specify an <code>Interact Style</code>. </p>
<p> The <code>None</code> type indicates that the application should not interact with the user while saving state. </p>
<p> The <code>Errors</code> type indicates that the application may interact with the user only if an error condition arises. </p>
<p> The <code>Any</code> type indicates that the application may interact with the user for any purpose. Note that <i>xsm</i> will only allow one application to interact with the user at a time. </p>
<p> After the checkpoint is completed, <i>xsm</i> will, if necessary, display a window containing the list of applications which did not report a successful save of state.</p>
<dt><code>Shutdown</code></p>
<dd> A shutdown provides all of the options found in a checkpoint, but in addition, can cause the session to exit. Note that if the interaction style is <code>Errors</code> or <code>Any</code>, the user may cancel the shutdown. The user may also cancel the shutdown if any of the applications report an unsuccessful save of state. </p>
<p> The user may choose to shutdown the session with our without performing a checkpoint.</dl>
<h2>HOW <i>XSM</i> RESPONDS TO SIGNALS</h2>
<p> <i>xsm</i> will respond to a SIGTERM signal by performing a shutdown with the following options: fast, no interaction, save type local. This allows the user&#8217;s session to be saved when the system is being shutdown. It can also be used to perform a remote shutdown of a session. </p>
<p> <i>xsm</i> will respond to a SIGUSR1 signal by performing a checkpoint with the following options: no interaction, save type local. This signal can be used to perform a remote checkpoint of a session. </p>
<h2>THE PROXY</h2>
<p> Since not all applications have been ported to support the X Session Management Protocol, a proxy service exists to allow &quot;old&quot; clients to work with the session manager. In order for the proxy to detect an application joining a session, one of the following must be true: </p>
<p> &#8211; The application maps a top level window containing the <code>WM_CLIENT_LEADER</code> property. This property provides a pointer to the client leader window which contains the <code>WM_CLASS</code>, <code>WM_NAME</code>, <code>WM_COMMAND</code>, and <code>WM_CLIENT_MACHINE</code> properties. </p>
<p> or &#8230; </p>
<p> &#8211; The application maps a top level window which does not contain the <code>WM_CLIENT_LEADER</code> property. However, this top level window contains the <code>WM_CLASS</code>, <code>WM_NAME</code>, <code>WM_COMMAND</code>, and <code>WM_CLIENT_MACHINE</code> properties. </p>
<p> An application that support the <code>WM_SAVE_YOURSELF</code> protocol will receive a <code>WM_SAVE_YOURSELF</code> client message each time the session manager issues a checkpoint or shutdown. This allows the application to save state. If an application does not support the <code>WM_SAVE_YOURSELF</code> protocol, then the proxy will provide enough information to the session manager to restart the application (using <code>WM_COMMAND</code>), but no state will be restored. </p>
<h2>REMOTE APPLICATIONS</h2>
<p> <i>xsm</i> requires a remote execution protocol in order to restart applications on remote machines. Currently, <i>xsm</i> supports the <i>rstart</i> protocol. In order to restart an application on remote machine <code>X</code>, machine <code>X</code> must have <i>rstart</i> installed. In the future, additional remote execution protocols may be supported.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-smproxy/">smproxy</a>(1), <a href="/docs/linux/man/1-rstart/">rstart</a>(1)</p>
<h2>AUTHORS</h2>
<p> Ralph Mor, X Consortium<br />
 Jordan Brown, Quarterdeck Office Systems </p>
<h2>Index</h2>
