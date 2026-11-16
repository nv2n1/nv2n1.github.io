---
title: "offlineimapui(7)"
name: "offlineimapui"
section: "7"
letter: "o"
url: "/docs/linux/man/7-offlineimapui/"
---

offlineimapui - The User Interfaces

<h2>Description</h2>

OfflineIMAP comes with different UIs, each aiming its own purpose.

<h2>Ttyui</h2>

TTYUI interface is for people running in terminals. It prints out basic status messages and is generally friendly to use on a console or xterm.

<h2>Basic</h2>

Basic is designed for situations in which OfflineIMAP will be run non-attended and the status of its execution will be logged. 

 This user interface is not capable of reading a password from the keyboard; account passwords must be specified using one of the configuration file options. For example, it will not print periodic sleep announcements and tends to be a tad less verbose, in general.

<h2>Blinkenlights</h2>

Blinkenlights is an interface designed to be sleek, fun to watch, and informative of the overall picture of what OfflineIMAP is doing. 

 Blinkenlights contains a row of &quot;LEDs&quot; with command buttons and a log. The log shows more detail about what is happening and is color-coded to match the color of the lights. 

 Each light in the Blinkenlights interface represents a thread of execution --- that is, a particular task that OfflineIMAP is performing right now. The colors indicate what task the particular thread is performing, and are as follows: 

<dl><dd>&bull; Black 
</dd><dl><dd><pre>indicates that this light's thread has terminated; it will light up again
later when new threads start up. So, black indicates no activity.</pre></dd></dl></dl><dl><dd>&bull; Red (Meaning 1) 
</dd><dl><dd><pre>is the color of the main program's thread, which basically does nothing but
monitor the others. It might remind you of HAL 9000 in 2001.</pre></dd></dl></dl><dl><dd>&bull; Gray 
</dd><dl><dd><pre>indicates that the thread is establishing a new connection to the IMAP
server.</pre></dd></dl></dl><dl><dd>&bull; Purple 
</dd><dl><dd><pre>is the color of an account synchronization thread that is monitoring the
progress of the folders in that account (not generating any I/O).</pre></dd></dl></dl><dl><dd>&bull; Cyan 
</dd><dl><dd><pre>indicates that the thread is syncing a folder.</pre></dd></dl></dl><dl><dd>&bull; Green 
</dd><dl><dd><pre>means that a folder's message list is being loaded.</pre></dd></dl></dl><dl><dd>&bull; Blue 
</dd><dl><dd><pre>is the color of a message synchronization controller thread.</pre></dd></dl></dl><dl><dd>&bull; Orange 
</dd><dl><dd><pre>indicates that an actual message is being copied. (We use fuchsia for fake
messages.)</pre></dd></dl></dl><dl><dd>&bull; Red (meaning 2) 
</dd><dl><dd><pre>indicates that a message is being deleted.</pre></dd></dl></dl><dl><dd>&bull; Yellow / bright orange 
</dd><dl><dd><pre>indicates that message flags are being added.</pre></dd></dl></dl><dl><dd>&bull; Pink / bright red 
</dd><dl><dd><pre>indicates that message flags are being removed.</pre></dd></dl></dl><dl><dd>&bull; Red / Black Flashing 
</dd><dl><dd><pre>corresponds to the countdown timer that runs between synchronizations.</pre></dd></dl></dl>
 

 The name of this interfaces derives from a bit of computer history. Eric Raymond's Jargon File defines blinkenlights, in part, as: 

<dl><dd><pre>Front-panel diagnostic lights on a computer, esp. a dinosaur. Now that
dinosaurs are rare, this term usually refers to status lights on a modem,
network hub, or the like.</pre></dd></dl>
 

 This term derives from the last word of the famous blackletter-Gothic sign in mangled pseudo-German that once graced about half the computer rooms in the English-speaking world. One version ran in its entirety as follows: 

<dl><dd><pre>ACHTUNG! ALLES LOOKENSPEEPERS!</pre></dd></dl><dl><dd><pre>Das computermachine ist nicht fuer gefingerpoken und mittengrabben.
Ist easy schnappen der springenwerk, blowenfusen und poppencorken
mit spitzensparken. Ist nicht fuer gewerken bei das dumpkopfen.
Das rubbernecken sichtseeren keepen das cotten-pickenen hans in das
pockets muss; relaxen und watchen das blinkenlichten.</pre></dd></dl>

<h2>Quiet</h2>

It will output nothing except errors and serious warnings. Like Basic, this user interface is not capable of reading a password from the keyboard; account passwords must be specified using one of the configuration file options.

<h2>Syslog</h2>

Syslog is designed for situations where OfflineIMAP is run as a daemon (e.g., as a systemd --user service), but errors should be forwarded to the system log. Like Basic, this user interface is not capable of reading a password from the keyboard; account passwords must be specified using one of the configuration file options.

<h2>Machineui</h2>

MachineUI generates output in a machine-parsable format. It is designed for other programs that will interface to OfflineIMAP.

<h2>See Also</h2>

<dl><dd><pre><a HREF="//www.systutorials.com/docs/linux/man/1-offlineimap/">offlineimap</a>(1)</pre></dd></dl>
 
