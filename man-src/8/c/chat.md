---
title: "chat(8)"
name: "chat"
section: "8"
letter: "c"
url: "/docs/linux/man/8-chat/"
description: "chat – Automated conversational script with a modem"
---
<p>chat &#8211; Automated conversational script with a modem </p>
<h2>SYNOPSIS</h2>
<p> <code>chat</code> [ <i>options</i> ] <i>script</i>  </p>
<h2>DESCRIPTION</h2>
<p>The <i>chat</i> program defines a conversational exchange between the computer and the modem. Its primary purpose is to establish the connection between the Point-to-Point Protocol Daemon (<i>pppd</i>) and the remote&#8217;s <i>pppd</i> process.  </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f </code><i>&lt;chat file&gt;</i></dt>
<dd> <p> Read the chat script from the chat <i>file</i>. The use of this option is mutually exclusive with the chat script parameters. The user must have read access to the file. Multiple lines are permitted in the file. Space or horizontal tab characters should be used to separate the strings. </p>
 </dd>
<dt><code>-t </code><i>&lt;timeout&gt;</i></dt>
<dd> <p> Set the timeout for the expected string to be received. If the string is not received within the time limit then the reply string is not sent. An alternate reply may be sent or the script will fail if there is no alternate reply string. A failed script will cause the <i>chat</i> program to terminate with a non-zero error code. You can also use the TIMEOUT string in order to specify the timeout. </p>
 </dd>
<dt><code>-r </code><i>&lt;report file&gt;</i></dt>
<dd> <p> Set the file for output of the report strings. If you use the keyword <i>REPORT</i>, the resulting strings are written to this file. If this option is not used and you still use <i>REPORT</i> keywords, the <i>stderr</i> file is used for the report strings. </p>
 </dd>
<dt><code>-e</code></dt>
<dd> <p> Start with the echo option turned on. Echoing may also be turned on or off at specific points in the chat script by using the <i>ECHO</i> keyword. When echoing is enabled, all output from the modem is echoed to <i>stderr</i>. </p>
 </dd>
<dt><code>-E</code></dt>
<dd> <p> Enables environment variable substitution within chat scripts using the standard <i>$xxx</i> syntax. </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> Request that the <i>chat</i> script be executed in a verbose mode. The <i>chat</i> program will then log the execution state of the chat script as well as all text received from the modem and the output strings sent to the modem. The default is to log through the SYSLOG; the logging method may be altered with the -S and -s flags. </p>
 </dd>
<dt><code>-V</code></dt>
<dd> <p> Request that the <i>chat</i> script be executed in a stderr verbose mode. The <i>chat</i> program will then log all text received from the modem and the output strings sent to the modem to the stderr device. This device is usually the local console at the station running the chat or pppd program. </p>
 </dd>
<dt><code>-s</code></dt>
<dd> <p> Use stderr. All log messages from &#8216;-v&#8217; and all error messages will be sent to stderr. </p>
 </dd>
<dt><code>-S</code></dt>
<dd> <p> Do not use the SYSLOG. By default, error messages are sent to the SYSLOG. The use of -S will prevent both log messages from &#8216;-v&#8217; and error messages from being sent to the SYSLOG. </p>
 </dd>
<dt><code>-T </code><i>&lt;phone number&gt;</i></dt>
<dd> <p> Pass in an arbitrary string, usually a phone number, that will be substituted for the \T substitution metacharacter in a send string. </p>
 </dd>
<dt><code>-U </code><i>&lt;phone number 2&gt;</i></dt>
<dd> <p> Pass in a second string, usually a phone number, that will be substituted for the \U substitution metacharacter in a send string. This is useful when dialing an ISDN terminal adapter that requires two numbers. </p>
 </dd>
<dt><code>script</code></dt>
<dd> <p> If the script is not specified in a file with the <i>-f</i> option then the script is included as parameters to the <i>chat</i> program. </p>
 </dd></dl>
<h2>CHAT SCRIPT</h2>
<p>The <i>chat</i> script defines the communications. </p>
<p>A script consists of one or more &quot;expect-send&quot; pairs of strings, separated by spaces, with an optional &quot;subexpect-subsend&quot; string pair, separated by a dash as in the following example: </p>
<dl>
<dd> <p> ogin:-BREAK-ogin: ppp ssword: hello2u2 </p>
 </dd></dl>
<p>This line indicates that the <i>chat</i> program should expect the string &quot;ogin:&quot;. If it fails to receive a login prompt within the time interval allotted, it is to send a break sequence to the remote and then expect the string &quot;ogin:&quot;. If the first &quot;ogin:&quot; is received then the break sequence is not generated. </p>
<p>Once it received the login prompt the <i>chat</i> program will send the string ppp and then expect the prompt &quot;ssword:&quot;. When it receives the prompt for the password, it will send the password hello2u2. </p>
<p>A carriage return is normally sent following the reply string. It is not expected in the &quot;expect&quot; string unless it is specifically requested by using the \r character sequence. </p>
<p>The expect sequence should contain only what is needed to identify the string. Since it is normally stored on a disk file, it should not contain variable information. It is generally not acceptable to look for time strings, network identification strings, or other variable pieces of data as an expect string. </p>
<p>To help correct for characters which may be corrupted during the initial sequence, look for the string &quot;ogin:&quot; rather than &quot;login:&quot;. It is possible that the leading &quot;l&quot; character may be received in error and you may never find the string even though it was sent by the system. For this reason, scripts look for &quot;ogin:&quot; rather than &quot;login:&quot; and &quot;ssword:&quot; rather than &quot;password:&quot;. </p>
<p>A very simple script might look like this: </p>
<dl>
<dd> <p> ogin: ppp ssword: hello2u2 </p>
 </dd></dl>
<p>In other words, expect ....ogin:, send ppp, expect ...ssword:, send hello2u2. </p>
<p>In actual practice, simple scripts are rare. At the vary least, you should include sub-expect sequences should the original string not be received. For example, consider the following script: </p>
<dl>
<dd> <p> ogin:--ogin: ppp ssword: hello2u2 </p>
 </dd></dl>
<p>This would be a better script than the simple one used earlier. This would look for the same login: prompt, however, if one was not received, a single return sequence is sent and then it will look for login: again. Should line noise obscure the first login prompt then sending the empty line will usually generate a login prompt again.  </p>
<h2>COMMENTS</h2>
<p> Comments can be embedded in the chat script. A comment is a line which starts with the <code>#</code> (hash) character in column 1. Such comment lines are just ignored by the chat program. If a &#8216;#&#8216; character is to be expected as the first character of the expect sequence, you should quote the expect string. If you want to wait for a prompt that starts with a # (hash) character, you would have to write something like this: </p>
<dl>
<dd> <p> # Now wait for the prompt and send logout string <br />
 &#8216;# &#8216; logout </p>
 </dd></dl>
<h2>SENDING DATA FROM A FILE</h2>
<p> If the string to send starts with an at sign (@), the rest of the string is taken to be the name of a file to read to get the string to send. If the last character of the data read is a newline, it is removed. The file can be a named pipe (or fifo) instead of a regular file. This provides a way for <code>chat</code> to communicate with another program, for example, a program to prompt the user and receive a password typed in. </p>
<h2>ABORT STRINGS</h2>
<p> Many modems will report the status of the call as a string. These strings may be <code>CONNECTED</code> or <code>NO CARRIER</code> or <code>BUSY</code>. It is often desirable to terminate the script should the modem fail to connect to the remote. The difficulty is that a script would not know exactly which modem string it may receive. On one attempt, it may receive <code>BUSY</code> while the next time it may receive <code>NO CARRIER</code>. </p>
<p>These &quot;abort&quot; strings may be specified in the script using the <i>ABORT</i> sequence. It is written in the script as in the following example: </p>
<dl>
<dd> <p> ABORT BUSY ABORT &#8216;NO CARRIER&#8217; &#8216;&#8216; ATZ OK ATDT5551212 CONNECT </p>
 </dd></dl>
<p>This sequence will expect nothing; and then send the string ATZ. The expected response to this is the string <i>OK</i>. When it receives <i>OK</i>, the string ATDT5551212 to dial the telephone. The expected string is <i>CONNECT</i>. If the string <i>CONNECT</i> is received the remainder of the script is executed. However, should the modem find a busy telephone, it will send the string <i>BUSY</i>. This will cause the string to match the abort character sequence. The script will then fail because it found a match to the abort string. If it received the string <i>NO CARRIER</i>, it will abort for the same reason. Either string may be received. Either string will terminate the <i>chat</i> script.  </p>
<h2>CLR_ABORT STRINGS</h2>
<p> This sequence allows for clearing previously set <code>ABORT</code> strings. <code>ABORT</code> strings are kept in an array of a pre-determined size (at compilation time); <code>CLR_ABORT</code> will reclaim the space for cleared entries so that new strings can use that space.  </p>
<h2>SAY STRINGS</h2>
<p> The <code>SAY</code> directive allows the script to send strings to the user at the terminal via standard error. If <code>chat</code> is being run by pppd, and pppd is running as a daemon (detached from its controlling terminal), standard error will normally be redirected to the file /etc/ppp/connect-errors. </p>
<p> <code>SAY</code> strings must be enclosed in single or double quotes. If carriage return and line feed are needed in the string to be output, you must explicitly add them to your string. </p>
<p>The SAY strings could be used to give progress messages in sections of the script where you want to have &#8216;ECHO OFF&#8217; but still let the user know what is happening. An example is: </p>
<dl>
<dd> <p> ABORT BUSY <br />
 ECHO OFF <br />
 SAY &quot;Dialling your ISP...\n&quot; <br />
 &#8216;&#8216; ATDT5551212 <br />
 TIMEOUT 120 <br />
 SAY &quot;Waiting up to 2 minutes for connection ... &quot; <br />
 CONNECT &#8216;&#8216; <br />
 SAY &quot;Connected, now logging in ...\n&quot; <br />
 ogin: account <br />
 ssword: pass <br />
 $ \c <br />
 SAY &quot;Logged in OK ...\n&quot; <i>etc ...</i> </p>
 </dd></dl>
<p>This sequence will only present the SAY strings to the user and all the details of the script will remain hidden. For example, if the above script works, the user will see: </p>
<dl>
<dd> <p> Dialling your ISP... <br />
 Waiting up to 2 minutes for connection ... Connected, now logging in ... <br />
 Logged in OK ... </p>
 </dd></dl>
<h2>REPORT STRINGS</h2>
<p> A <code>report</code> string is similar to the ABORT string. The difference is that the strings, and all characters to the next control character such as a carriage return, are written to the report file. </p>
<p>The report strings may be used to isolate the transmission rate of the modem&#8217;s connect string and return the value to the chat user. The analysis of the report string logic occurs in conjunction with the other string processing such as looking for the expect string. The use of the same string for a report and abort sequence is probably not very useful, however, it is possible. </p>
<p>The report strings to no change the completion code of the program. </p>
<p>These &quot;report&quot; strings may be specified in the script using the <i>REPORT</i> sequence. It is written in the script as in the following example: </p>
<dl>
<dd> <p> REPORT CONNECT ABORT BUSY &#8216;&#8216; ATDT5551212 CONNECT &#8216;&#8216; ogin: account </p>
 </dd></dl>
<p>This sequence will expect nothing; and then send the string ATDT5551212 to dial the telephone. The expected string is <i>CONNECT</i>. If the string <i>CONNECT</i> is received the remainder of the script is executed. In addition the program will write to the expect-file the string &quot;CONNECT&quot; plus any characters which follow it such as the connection rate.  </p>
<h2>CLR_REPORT STRINGS</h2>
<p> This sequence allows for clearing previously set <code>REPORT</code> strings. <code>REPORT</code> strings are kept in an array of a pre-determined size (at compilation time); <code>CLR_REPORT</code> will reclaim the space for cleared entries so that new strings can use that space.  </p>
<h2>ECHO</h2>
<p> The echo options controls whether the output from the modem is echoed to <i>stderr</i>. This option may be set with the <i>-e</i> option, but it can also be controlled by the <i>ECHO</i> keyword. The &quot;expect-send&quot; pair <i>ECHO</i> <i>ON</i> enables echoing, and <i>ECHO</i> <i>OFF</i> disables it. With this keyword you can select which parts of the conversation should be visible. For instance, with the following script: </p>
<dl>
<dd> <p> ABORT &#8216;BUSY&#8217; <br />
 ABORT &#8216;NO CARRIER&#8217; <br />
 &#8216;&#8216; ATZ <br />
 OK\r\n ATD1234567 <br />
 \r\n \c <br />
 ECHO ON <br />
 CONNECT \c <br />
 ogin: account </p>
 </dd></dl>
<p>all output resulting from modem configuration and dialing is not visible, but starting with the <i>CONNECT</i> (or <i>BUSY</i>) message, everything will be echoed.  </p>
<h2>HANGUP</h2>
<p> The HANGUP options control whether a modem hangup should be considered as an error or not. This option is useful in scripts for dialling systems which will hang up and call your system back. The HANGUP options can be <code>ON</code> or <code>OFF</code>. <br />
 When HANGUP is set OFF and the modem hangs up (e.g., after the first stage of logging in to a callback system), <code>chat</code> will continue running the script (e.g., waiting for the incoming call and second stage login prompt). As soon as the incoming call is connected, you should use the <code>HANGUP ON</code> directive to reinstall normal hang up signal behavior. Here is an (simple) example script: </p>
<dl>
<dd> <p> ABORT &#8216;BUSY&#8217; <br />
 &#8216;&#8216; ATZ <br />
 OK\r\n ATD1234567 <br />
 \r\n \c <br />
 CONNECT \c <br />
 &#8216;Callback login:&#8216; call_back_ID <br />
 HANGUP OFF <br />
 ABORT &quot;Bad Login&quot; <br />
 &#8216;Callback Password:&#8216; Call_back_password <br />
 TIMEOUT 120 <br />
 CONNECT \c <br />
 HANGUP ON <br />
 ABORT &quot;NO CARRIER&quot; <br />
 ogin:--BREAK--ogin: real_account <br />
 <i>etc ...</i> </p>
 </dd></dl>
<h2>TIMEOUT</h2>
<p> The initial timeout value is 45 seconds. This may be changed using the <code>-t</code> parameter. You can also specify &quot;TIMEOUT 0&quot;. </p>
<p>To change the timeout value for the next expect string, the following example may be used: </p>
<dl>
<dd> <p> ATZ OK ATDT5551212 CONNECT TIMEOUT 10 ogin:--ogin: TIMEOUT 5 assword: hello2u2 </p>
 </dd></dl>
<p>This will change the timeout to 10 seconds when it expects the login: prompt. The timeout is then changed to 5 seconds when it looks for the password prompt. </p>
<p>The timeout, once changed, remains in effect until it is changed again.  </p>
<h2>SENDING EOT</h2>
<p> The special reply string of <i>EOT</i> indicates that the chat program should send an EOT character to the remote. This is normally the End-of-file character sequence. A return character is not sent following the EOT. The EOT sequence may be embedded into the send string using the sequence <i>^D</i>.  </p>
<h2>GENERATING BREAK</h2>
<p> The special reply string of <i>BREAK</i> will cause a break condition to be sent. The break is a special signal on the transmitter. The normal processing on the receiver is to change the transmission rate. It may be used to cycle through the available transmission rates on the remote until you are able to receive a valid login prompt. The break sequence may be embedded into the send string using the <i>\K</i> sequence.  </p>
<h2>ESCAPE SEQUENCES</h2>
<p> The expect and reply strings may contain escape sequences. All of the sequences are legal in the reply string. Many are legal in the expect. Those which are not valid in the expect sequence are so indicated. </p>
<dl>
<dt><code>&#8216;&#8216;</code></dt>
<dd> <p> Expects or sends a null string. If you send a null string then it will still send the return character. This sequence may either be a pair of apostrophe or quote characters. </p>
 </dd>
<dt><code>\b</code></dt>
<dd> <p> represents a backspace character. </p>
 </dd>
<dt><code>\c</code></dt>
<dd> <p> Suppresses the newline at the end of the reply string. This is the only method to send a string without a trailing return character. It must be at the end of the send string. For example, the sequence hello\c will simply send the characters h, e, l, l, o. <i>(not valid in expect.)</i> </p>
 </dd>
<dt><code>\d</code></dt>
<dd> <p> Delay for one second. The program uses <a href="/docs/linux/man/1-sleep/">sleep</a>(1) which will delay to a maximum of one second. <i>(not valid in expect.)</i> </p>
 </dd>
<dt><code>\K</code></dt>
<dd> <p> Insert a BREAK <i>(not valid in expect.)</i> </p>
 </dd>
<dt><code>\n</code></dt>
<dd> <p> Send a newline or linefeed character. </p>
 </dd>
<dt><code>\N</code></dt>
<dd> <p> Send a null character. The same sequence may be represented by \0. <i>(not valid in expect.)</i> </p>
 </dd>
<dt><code>\p</code></dt>
<dd> <p> Pause for a fraction of a second. The delay is 1/10th of a second. <i>(not valid in expect.)</i> </p>
 </dd>
<dt><code>\q</code></dt>
<dd> <p> Suppress writing the string to the SYSLOG file. The string ?????? is written to the log in its place. <i>(not valid in expect.)</i> </p>
 </dd>
<dt><code>\r</code></dt>
<dd> <p> Send or expect a carriage return. </p>
 </dd>
<dt><code>\s</code></dt>
<dd> <p> Represents a space character in the string. This may be used when it is not desirable to quote the strings which contains spaces. The sequence &#8216;HI TIM&#8217; and HI\sTIM are the same. </p>
 </dd>
<dt><code>\t</code></dt>
<dd> <p> Send or expect a tab character. </p>
 </dd>
<dt><code>\T</code></dt>
<dd> <p> Send the phone number string as specified with the <i>-T</i> option <i>(not valid in expect.)</i> </p>
 </dd>
<dt><code>\U</code></dt>
<dd> <p> Send the phone number 2 string as specified with the <i>-U</i> option <i>(not valid in expect.)</i> </p>
 </dd>
<dt><code>\\</code></dt>
<dd> <p> Send or expect a backslash character. </p>
 </dd>
<dt><code>\ddd</code></dt>
<dd> <p> Collapse the octal digits (ddd) into a single ASCII character and send that character. <i>(some characters are not valid in expect.)</i> </p>
 </dd>
<dt><code>^C</code></dt>
<dd> <p> Substitute the sequence with the control character represented by C. For example, the character DC1 (17) is shown as ^Q. <i>(some characters are not valid in expect.)</i> </p>
 </dd></dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> Environment variables are available within chat scripts, if the <i>-E</i> option was specified in the command line. The metacharacter <i>$</i> is used to introduce the name of the environment variable to substitute. If the substitution fails, because the requested environment variable is not set, <i>nothing</i> is replaced for the variable.  </p>
<h2>TERMINATION CODES</h2>
<p> The <i>chat</i> program will terminate with the following completion codes. </p>
<dl>
<dt><code>0</code></dt>
<dd> <p> The normal termination of the program. This indicates that the script was executed without error to the normal conclusion. </p>
 </dd>
<dt><code>1</code></dt>
<dd> <p> One or more of the parameters are invalid or an expect string was too large for the internal buffers. This indicates that the program as not properly executed. </p>
 </dd>
<dt><code>2</code></dt>
<dd> <p> An error occurred during the execution of the program. This may be due to a read or write operation failing for some reason or chat receiving a signal such as SIGINT. </p>
 </dd>
<dt><code>3</code></dt>
<dd> <p> A timeout event occurred when there was an <i>expect</i> string without having a &quot;-subsend&quot; string. This may mean that you did not program the script correctly for the condition or that some unexpected event has occurred and the expected string could not be found. </p>
 </dd>
<dt><code>4</code></dt>
<dd> <p> The first string marked as an <i>ABORT</i> condition occurred. </p>
 </dd>
<dt><code>5</code></dt>
<dd> <p> The second string marked as an <i>ABORT</i> condition occurred. </p>
 </dd>
<dt><code>6</code></dt>
<dd> <p> The third string marked as an <i>ABORT</i> condition occurred. </p>
 </dd>
<dt><code>7</code></dt>
<dd> <p> The fourth string marked as an <i>ABORT</i> condition occurred. </p>
 </dd>
<dt><code>...</code></dt>
<dd> <p> The other termination codes are also strings marked as an <i>ABORT</i> condition. </p>
 </dd></dl>
<p>Using the termination code, it is possible to determine which event terminated the script. It is possible to decide if the string &quot;BUSY&quot; was received from the modem as opposed to &quot;NO DIAL TONE&quot;. While the first event may be retried, the second will probably have little chance of succeeding during a retry.  </p>
<h2>SEE ALSO</h2>
<p> Additional information about <i>chat</i> scripts may be found with UUCP documentation. The <i>chat</i> script was taken from the ideas proposed by the scripts used by the <i>uucico</i> program. </p>
<p> uucico(1), <a href="/docs/linux/man/1-uucp/">uucp</a>(1)  </p>
<h2>COPYRIGHT</h2>
<p> The <i>chat</i> program is in public domain. This is not the GNU public license. If it breaks then you get to keep both pieces. </p>
