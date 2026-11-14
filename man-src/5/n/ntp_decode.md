---
title: "ntp_decode(5)"
name: "ntp_decode"
section: "5"
letter: "n"
url: "/docs/linux/man/5-ntp_decode/"
description: "ntp_decode – ntpd Event Messages and Status Words"
---

<p>ntp_decode &#8211; ntpd Event Messages and Status Words</p>
<h2>&nbsp;<wbr></h2>
<h2>Introduction</h2>
<p>This page lists the status words, event messages and error codes used for <code>ntpd</code> reporting and monitoring. Status words are used to display the current status of the running program. There is one system status word and a peer status word for each association. There is a clock status word for each association that supports a reference clock. There is a flash code for each association which shows errors found in the last packet received (pkt) and during protocol processing (peer). These are commonly viewed using the <code>ntpq</code> program. </p>
<p> Significant changes in program state are reported as events. There is one set of system events and a set of peer events for each association. In addition, there is a set of clock events for each association that supports a reference clock. Events are normally reported to the <code>protostats</code> monitoring file and optionally to the system log. In addition, if the trap facility is configured, events can be reported to a remote program that can page an administrator. </p>
<p> This page also includes a description of the error messages produced by the Autokey protocol. These messages are normally sent to the <code>cryptostats</code> monitoring file. </p>
<p> In the following tables the Code Field is the status or event code assigned and the Message Field a short string used for display and event reporting. The Description field contains a longer explanation of the status or event. Some messages include additional information useful for error diagnosis and performance assessment.</p>
<h2>System Status Word</h2>
<p>The system status word consists of four fields LI (0-1), Source (2-7), Count (8-11) and Code (12-15). It is reported in the first line of the <code>rv</code> display produced by the <code>ntpq</code> program. </p>
<table BORDER WIDTH=100%>
<tr VALIGN=top>
<td>
&nbsp;<wbr>Leap&nbsp;<wbr>&nbsp;<wbr></td>
<td> Source </td>
<td> Count </td>
<td> Code
</td>
</tr>
</table>
<p> The Leap Field displays the system leap indicator bits coded as follows: </p>
<table BORDER WIDTH=100%>
<tr VALIGN=top>
<td>
&nbsp;<wbr>Code&nbsp;<wbr>&nbsp;<wbr></td>
<td> Message </td>
<td> Description </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>0</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>leap_none</code> </td>
<td> normal synchronized state </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>1</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>leap_add_sec</code> </td>
<td> insert second after 23:59:59 of the current day </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>2</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>leap_del_sec</code> </td>
<td> delete second 23:59:59 of the current day </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>3</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>leap_alarm</code> </td>
<td> never synchronized </td>
<td>
</td>
</tr>
</table>
<p> The Source Field displays the current synchronization source coded as follows:. </p>
<table BORDER WIDTH=100%>
<tr VALIGN=top>
<td>
&nbsp;<wbr>Code&nbsp;<wbr>&nbsp;<wbr></td>
<td> Message </td>
<td> Description </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>0</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>sync_unspec</code> </td>
<td> not yet synchronized </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>1</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>sync_pps</code> </td>
<td> pulse-per-second signal (Cs, Ru, GPS, etc.) </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>2</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>sync_lf_radio</code> </td>
<td> VLF/LF radio (WWVB, DCF77, etc.) </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>3</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>sync_hf_radio</code> </td>
<td> MF/HF radio (WWV, etc.) </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>4</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>sync_uhf_radio</code> </td>
<td> VHF/UHF radio/satellite (GPS, Galileo, etc.) </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>5</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>sync_local</code> </td>
<td> local timecode (IRIG, LOCAL driver, etc.) </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>6</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>sync_ntp</code> </td>
<td> NTP </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>7</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>sync_other</code> </td>
<td> other (IEEE 1588, openntp, crony, etc.) </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>8</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>sync_wristwatch</code> </td>
<td> eyeball and wristwatch </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>9</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>sync_telephone</code> </td>
<td> telephone modem (ACTS, PTB, etc.) </td>
<td>
</td>
</tr>
</table>
<p> The Count Field displays the number of events since the last time the code changed. Upon reaching 15, subsequent events with the same code are ignored. </p>
<p> The Event Field displays the most recent event message coded as follows: </p>
<table BORDER WIDTH=100%>
<tr VALIGN=top>
<td>
&nbsp;<wbr>Code&nbsp;<wbr>&nbsp;<wbr></td>
<td> Message </td>
<td> Description </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>00</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>unspecified</code> </td>
<td> unspecified </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>01</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>freq_not_set</code> </td>
<td> frequency file not available </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>02</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>freq_set</code> </td>
<td> frequency set from frequency file </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>03</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>spike_detect</code> </td>
<td> spike detected </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>04</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>freq_mode</code> </td>
<td> initial frequency training mode </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>05</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>clock_sync</code> </td>
<td> clock synchronized </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>06</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>restart</code> </td>
<td> program restart </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>07</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>panic_stop</code> </td>
<td> clock error more than 600 s </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>08</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>no_system_peer</code> </td>
<td> no system peer </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>09</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>leap_armed</code> </td>
<td> leap second armed from file or Autokey </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>0a</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>leap_disarmed</code> </td>
<td> leap second disarmed </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>0b</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>leap_event</code> </td>
<td> leap event </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>0c</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>clock_step</code> </td>
<td> clock stepped </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>0d</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>kern</code> </td>
<td> kernel information message </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>0e</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>TAI&#8230;</code> </td>
<td> leapsecond values update from file </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>0f</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>stale leapsecond values</code> </td>
<td> new NIST leapseconds file needed </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr><code>10</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>clockhop</code> </td>
<td> spurious clock hop suppressed </td>
<td>
</td>
</tr>
</table>
<h2>Peer Status Word</h2>
<p>The peer status word consists of four fields: Status (0-4), Select (5-7), Count (8-11) and Code (12-15). It is reported in the first line of the <code>rv </code><i>associd</i> display produced by the <code>ntpq</code> program. </p>
<table BORDER WIDTH=100%>
<tr VALIGN=top>
<td>
&nbsp;<wbr>Status&nbsp;<wbr>&nbsp;<wbr></td>
<td> Select </td>
<td> Count </td>
<td> Code
</td>
</tr>
</table>
<p> The Status Field displays the peer status code bits in hexadecimal; each bit is an independent flag. (Note this field is 5 bits wide, and combines with the the 3-bit-wide Select Field to create the first full byte of the peer status word.) The meaning of each bit in the Status Field is listed in the following table: </p>
<table BORDER WIDTH=100%>
<tr VALIGN=top>
<td>
&nbsp;<wbr>Code&nbsp;<wbr>&nbsp;<wbr></td>
<td> Message </td>
<td> Description </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>08</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>bcst</code> </td>
<td> broadcast association </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>10</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>reach</code> </td>
<td> host reachable </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>20</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>authenb</code> </td>
<td> authentication enabled </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>40</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>auth</code> </td>
<td> authentication ok </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>80</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>config</code> </td>
<td> persistent association </td>
<td>
</td>
</tr>
</table>
<p> The Select Field displays the current selection status. (The T Field in the following table gives the corresponding tally codes used in the <code>ntpq peers</code> display.) The values are coded as follows: </p>
<table BORDER WIDTH=100%>
<tr VALIGN=top>
<td>
&nbsp;<wbr>Code&nbsp;<wbr>&nbsp;<wbr></td>
<td> Message </td>
<td> T </td>
<td> Description
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>0</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>sel_reject</code> </td>
<td> </td>
<td> discarded as not valid (TEST10-TEST13)
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>1</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>sel_falsetick</code> </td>
<td> <code>x</code> </td>
<td> discarded by intersection algorithm
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>2</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>sel_excess</code> </td>
<td> <code>46</code> </td>
<td> discarded by table overflow (not used)
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>3</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>sel_outlyer</code> </td>
<td> <code>&#8211;</code> </td>
<td> discarded by the cluster algorithm
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>4</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>sel_candidate</code> </td>
<td> <code>+</code> </td>
<td> included by the combine algorithm
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>5</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>sel_backup</code> </td>
<td> <code>#</code> </td>
<td> backup (more than <code>tos maxclock</code> sources)
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>6</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>sel_sys.peer</code> </td>
<td> <code>*</code> </td>
<td> system peer
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>7</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>sel_pps.peer</code> </td>
<td> <code>o</code> </td>
<td> PPS peer (when the prefer peer is valid)
</td>
</tr>
</table>
<p> The Count Field displays the number of events since the last time the code changed. Upon reaching 15, subsequent events with the same code are ignored. </p>
<p> The Event Field displays the most recent event message coded as follows: </p>
<table BORDER WIDTH=100%>
<tr VALIGN=top>
<td>
&nbsp;<wbr>Code&nbsp;<wbr>&nbsp;<wbr></td>
<td> Message </td>
<td> Description </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>01</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>mobilize</code> </td>
<td> association mobilized </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>02</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>demobilize</code> </td>
<td> association demobilized </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>03</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>unreachable</code> </td>
<td> server unreachable </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>04</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>reachable</code> </td>
<td> server reachable </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>05</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>restart</code> </td>
<td> association restart </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>06</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>no_reply</code> </td>
<td> no server found (<code>ntpdate</code> mode) </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>07</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>rate_exceeded</code> </td>
<td> rate exceeded (kiss code <code>RATE</code>) </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>08</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>access_denied</code> </td>
<td> access denied (kiss code <code>DENY</code>) </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>09</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>leap_armed</code> </td>
<td> leap armed from server LI code </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>0a</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>sys_peer</code> </td>
<td> become system peer </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>0b</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>clock_event</code> </td>
<td> see clock status word </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>0c</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>bad_auth</code> </td>
<td> authentication failure </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>0d</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>popcorn</code> </td>
<td> popcorn spike suppressor </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>0e</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>interleave_mode</code> </td>
<td> entering interleave mode </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>0f</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>interleave_error</code> </td>
<td> interleave error (recovered) </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>10</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>TAI&#8230;</code> </td>
<td> leapsecond values update from server </td>
<td>
</td>
</tr>
</table>
<h2>Clock Status Word</h2>
<p>The clock status word consists of four fields: Unused (0-7), Count (8-11) and Code (12-15). It is reported in the first line of the <code>clockvar </code><i>associd</i> display produced by the <code>ntpq</code> program. </p>
<table BORDER WIDTH=100%>
<tr VALIGN=top>
<td>
&nbsp;<wbr>Unused&nbsp;<wbr>&nbsp;<wbr></td>
<td> Count </td>
<td> Code </td>
<td>
</td>
</tr>
</table>
<p> The Count Field displays the number of events since the last <code>lockvar</code> command, while the Event Field displays the most recent event message coded as follows: </p>
<table BORDER WIDTH=100%>
<tr VALIGN=top>
<td>
&nbsp;<wbr>Code&nbsp;<wbr>&nbsp;<wbr></td>
<td> Message </td>
<td> Description </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>00</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>clk_unspe</code> </td>
<td> nominal </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>01</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>clk_noreply</code> </td>
<td> no reply to poll </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>02</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>clk_badformat</code> </td>
<td> bad timecode format </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>03</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>clk_fault</code> </td>
<td> hardware or software fault </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>04</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>clk_bad_signal</code> </td>
<td> signal loss </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>05</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>clk_bad_date</code> </td>
<td> bad date format </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>06</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>clk_bad_time</code> </td>
<td> bad time format </td>
<td>
</td>
</tr>
</table>
<p> When the clock driver sets the code to a new value, a <code>clock_alarm</code> (11) peer event is reported.</p>
<h2>Flash Status Word</h2>
<p>The flash status word is displayed by the <code>ntpq</code> program <code>rv</code> command. It consists of a number of bits coded in hexadecimal as follows: </p>
<table BORDER WIDTH=100%>
<tr VALIGN=top>
<td>
&nbsp;<wbr>Code&nbsp;<wbr>&nbsp;<wbr></td>
<td> Tag </td>
<td> Message </td>
<td> Description
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>0001</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> TEST1 </td>
<td> <code>pkt_dup</code> </td>
<td> duplicate packet
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>0002</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> TEST2 </td>
<td> <code>pkt_bogus</code> </td>
<td> bogus packet
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>0004</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> TEST3 </td>
<td> <code>pkt_unsync</code> </td>
<td> protocol unsynchronized
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>0008</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> TEST4 </td>
<td> <code>pkt_denied</code> </td>
<td> access denied
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>0010</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> TEST5 </td>
<td> <code>pkt_auth</code> </td>
<td> bad authentication
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>0020</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> TEST6 </td>
<td> <code>pkt_stratum</code> </td>
<td> bad synch or stratum
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>0040</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> TEST7 </td>
<td> <code>pkt_header</code> </td>
<td> bad header
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>0080</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> TEST8 </td>
<td> <code>pkt_autokey</code> </td>
<td> bad autokey
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>0100</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> TEST9 </td>
<td> <code>pkt_crypto</code> </td>
<td> bad crypto
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>0200</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> TEST10 </td>
<td> <code>peer_stratum</code> </td>
<td> peer bad synch or stratum
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>0400</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> TEST11 </td>
<td> <code>peer_dist</code> </td>
<td> peer distance exceeded
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>0800</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> TEST12 </td>
<td> <code>peer_loop</code> </td>
<td> peer synchronization loop
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>1000</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> TEST13 </td>
<td> <code>peer_unreach</code> </td>
<td> peer unreachable
</td>
</tr>
</table>
<h2>Kiss Codes</h2>
<p>Kiss codes are used in kiss-o&#8217;-death (koD) packets, billboard displays and log messages. They consist of a string of four zero-padded ASCII charactes. In practice they are informal and tend to change with time and implementation. Some of these codes can appear in the reference identifier field in <code>ntpq</code> billboards. Following is the current list: </p>
<table BORDER WIDTH=100%>
<tr VALIGN=top>
<td>
&nbsp;<wbr>Code&nbsp;<wbr>&nbsp;<wbr></td>
<td> Description </td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>ACST</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> manycast server </td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>AUTH</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> authentication error </td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>AUTO</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> Autokey sequence error </td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>BCST</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> broadcast server </td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>CRYPT</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> Autokey protocol error </td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>DENY</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> access denied by server </td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>INIT</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> association initialized </td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>MCST</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> multicast server </td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>RATE</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> rate exceeded </td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>TIME</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> association timeout </td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>STEP</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> step time change </td>
<td></td>
<td>
</td>
</tr>
</table>
<h2>Crypto Messages</h2>
<p>These messages are sent to the <code>cryptostats</code> file when an error is detected in the Autokey protocol. </p>
<table BORDER WIDTH=100%>
<tr VALIGN=top>
<td>
&nbsp;<wbr>Code&nbsp;<wbr>&nbsp;<wbr></td>
<td> Message </td>
<td> Description </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>01</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>bad_format</code> </td>
<td> bad extension field format or length </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>02</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>bad_timestamp</code> </td>
<td> bad timestamp </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>03</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>bad_filestamp</code> </td>
<td> bad filestamp </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>04</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>bad_public_key</code> </td>
<td> bad or missing public key </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>05</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>bad_digest</code> </td>
<td> unsupported digest type </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>06</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>bad_identity</code> </td>
<td> unsupported identity type </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>07</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>bad_siglength</code> </td>
<td> bad signature length </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>08</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>bad signature</code> </td>
<td> extension field signature not verified </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>09</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>cert_not_verified</code> </td>
<td> certificate signature not verified </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>0a</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>cert_expired</code> </td>
<td> host certificate expired </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>0b</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>bad_cookie</code> </td>
<td> bad or missing cookie </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>0c</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>bad_leapseconds</code> </td>
<td> bad or missing leapseconds values </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>0d</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>cert_missing</code> </td>
<td> bad or missing certificate </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>0e</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>bad_group_key</code> </td>
<td> bad or missing group key </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr><code>0f</code>&nbsp;<wbr>&nbsp;<wbr></td>
<td> <code>proto_error</code> </td>
<td> protocol error </td>
<td>
</td>
</tr>
</table>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ntpq/">ntpq</a>(8), <a href="/docs/linux/man/5-ntp_mon/">ntp_mon</a>(5) The official HTML documentation. This file was automatically generated from HTML source. </p>
